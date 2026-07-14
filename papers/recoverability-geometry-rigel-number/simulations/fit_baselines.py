#!/usr/bin/env python3
"""Fit leakage-controlled baselines for the scalar delayed-control benchmark.

Uses only the Python standard library. Models are fit on the declared `train`
parameter region and evaluated on the held-out `ood` region. The outcome is
failure = 1 - recovered, which remains independently defined by the simulator.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import random
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Iterable, Sequence


@dataclass(frozen=True)
class Row:
    split: str
    failure: int
    alpha_total: float
    lambda_growth: float
    alpha_o: float
    alpha_i: float
    alpha_r: float
    burden_o: float
    burden_i: float
    burden_r: float
    controller_gain: float
    initial_abs_x: float
    process_noise_sd: float
    sensor_noise_sd: float
    rigel_number: float


@dataclass
class Standardizer:
    means: list[float]
    scales: list[float]

    @classmethod
    def fit(cls, matrix: Sequence[Sequence[float]]) -> "Standardizer":
        width = len(matrix[0])
        means: list[float] = []
        scales: list[float] = []
        for column in range(width):
            values = [float(row[column]) for row in matrix]
            mean = sum(values) / len(values)
            variance = sum((value - mean) ** 2 for value in values) / max(1, len(values) - 1)
            scale = math.sqrt(variance)
            means.append(mean)
            scales.append(scale if scale > 1e-12 else 1.0)
        return cls(means=means, scales=scales)

    def transform(self, matrix: Sequence[Sequence[float]]) -> list[list[float]]:
        return [
            [(float(value) - self.means[index]) / self.scales[index] for index, value in enumerate(row)]
            for row in matrix
        ]


@dataclass
class LogisticModel:
    weights: list[float]

    def predict_probability(self, features: Sequence[float]) -> float:
        z = self.weights[0] + sum(weight * value for weight, value in zip(self.weights[1:], features))
        if z >= 0:
            return 1.0 / (1.0 + math.exp(-z))
        exp_z = math.exp(z)
        return exp_z / (1.0 + exp_z)


def load_rows(path: Path) -> list[Row]:
    rows: list[Row] = []
    with path.open(newline="", encoding="utf-8") as handle:
        for record in csv.DictReader(handle):
            raw_ri = record["rigel_number"]
            rigel = 1e6 if raw_ri == "inf" else float(raw_ri)
            rows.append(
                Row(
                    split=record["split"],
                    failure=1 - int(record["recovered"]),
                    alpha_total=float(record["alpha_total"]),
                    lambda_growth=float(record["lambda_growth"]),
                    alpha_o=float(record["alpha_o"]),
                    alpha_i=float(record["alpha_i"]),
                    alpha_r=float(record["alpha_r"]),
                    burden_o=float(record["burden_o"]),
                    burden_i=float(record["burden_i"]),
                    burden_r=float(record["burden_r"]),
                    controller_gain=float(record["controller_gain"]),
                    initial_abs_x=float(record["initial_abs_x"]),
                    process_noise_sd=float(record["process_noise_sd"]),
                    sensor_noise_sd=float(record["sensor_noise_sd"]),
                    rigel_number=rigel,
                )
            )
    if not rows:
        raise ValueError(f"No rows found in {path}")
    return rows


def fit_logistic(
    matrix: Sequence[Sequence[float]],
    labels: Sequence[int],
    *,
    learning_rate: float = 0.05,
    iterations: int = 2500,
    l2: float = 1e-3,
) -> LogisticModel:
    width = len(matrix[0])
    weights = [0.0] * (width + 1)
    n = float(len(matrix))
    for step in range(iterations):
        gradients = [0.0] * len(weights)
        for features, label in zip(matrix, labels):
            z = weights[0] + sum(weight * value for weight, value in zip(weights[1:], features))
            if z >= 0:
                probability = 1.0 / (1.0 + math.exp(-z))
            else:
                exp_z = math.exp(z)
                probability = exp_z / (1.0 + exp_z)
            error = probability - label
            gradients[0] += error
            for index, value in enumerate(features, start=1):
                gradients[index] += error * value
        gradients[0] /= n
        for index in range(1, len(weights)):
            gradients[index] = gradients[index] / n + l2 * weights[index]
        rate = learning_rate / math.sqrt(1.0 + step / 500.0)
        for index in range(len(weights)):
            weights[index] -= rate * gradients[index]
    return LogisticModel(weights=weights)


def rank_auc(labels: Sequence[int], scores: Sequence[float]) -> float:
    pairs = sorted(zip(scores, labels), key=lambda item: item[0])
    positives = sum(labels)
    negatives = len(labels) - positives
    if positives == 0 or negatives == 0:
        return float("nan")
    rank_sum = 0.0
    index = 0
    while index < len(pairs):
        end = index + 1
        while end < len(pairs) and pairs[end][0] == pairs[index][0]:
            end += 1
        average_rank = ((index + 1) + end) / 2.0
        rank_sum += average_rank * sum(label for _, label in pairs[index:end])
        index = end
    return (rank_sum - positives * (positives + 1) / 2.0) / (positives * negatives)


def brier(labels: Sequence[int], probabilities: Sequence[float]) -> float:
    return sum((probability - label) ** 2 for probability, label in zip(probabilities, labels)) / len(labels)


def calibration_error(labels: Sequence[int], probabilities: Sequence[float], bins: int = 10) -> float:
    total = len(labels)
    error = 0.0
    for bin_index in range(bins):
        low = bin_index / bins
        high = (bin_index + 1) / bins
        indices = [
            index
            for index, probability in enumerate(probabilities)
            if probability >= low and (probability < high or (bin_index == bins - 1 and probability <= high))
        ]
        if not indices:
            continue
        observed = sum(labels[index] for index in indices) / len(indices)
        predicted = sum(probabilities[index] for index in indices) / len(indices)
        error += len(indices) / total * abs(observed - predicted)
    return error


def bootstrap_interval(
    labels: Sequence[int],
    scores: Sequence[float],
    metric: Callable[[Sequence[int], Sequence[float]], float],
    *,
    seed: int,
    replicates: int,
) -> dict[str, float]:
    rng = random.Random(seed)
    estimates: list[float] = []
    n = len(labels)
    for _ in range(replicates):
        indices = [rng.randrange(n) for _ in range(n)]
        sample_labels = [labels[index] for index in indices]
        sample_scores = [scores[index] for index in indices]
        estimate = metric(sample_labels, sample_scores)
        if math.isfinite(estimate):
            estimates.append(estimate)
    if not estimates:
        return {"lower_95": float("nan"), "upper_95": float("nan"), "replicates_used": 0}
    estimates.sort()
    low_index = max(0, int(0.025 * (len(estimates) - 1)))
    high_index = min(len(estimates) - 1, int(0.975 * (len(estimates) - 1)))
    return {
        "lower_95": estimates[low_index],
        "upper_95": estimates[high_index],
        "replicates_used": len(estimates),
    }


def feature_map(name: str, row: Row) -> list[float]:
    common = [
        row.lambda_growth,
        row.controller_gain,
        row.initial_abs_x,
        row.process_noise_sd,
        row.sensor_noise_sd,
    ]
    if name == "total_latency":
        return [row.alpha_total] + common
    if name == "lambda_times_total":
        return [row.lambda_growth * row.alpha_total] + common
    if name == "decomposed_latency":
        return [row.alpha_o, row.alpha_i, row.alpha_r] + common
    if name == "decomposed_burdens":
        return [row.burden_o, row.burden_i, row.burden_r] + common
    if name == "rigel_number":
        return [row.rigel_number] + common
    raise KeyError(name)


def evaluate_model(name: str, train: Sequence[Row], ood: Sequence[Row], bootstrap_replicates: int, seed: int) -> dict[str, object]:
    train_x_raw = [feature_map(name, row) for row in train]
    ood_x_raw = [feature_map(name, row) for row in ood]
    train_y = [row.failure for row in train]
    ood_y = [row.failure for row in ood]
    standardizer = Standardizer.fit(train_x_raw)
    train_x = standardizer.transform(train_x_raw)
    ood_x = standardizer.transform(ood_x_raw)
    model = fit_logistic(train_x, train_y)
    probabilities = [model.predict_probability(features) for features in ood_x]
    auc = rank_auc(ood_y, probabilities)
    return {
        "features": name,
        "train_count": len(train),
        "ood_count": len(ood),
        "ood_failure_rate": sum(ood_y) / len(ood_y),
        "ood_auc": auc,
        "ood_auc_bootstrap_95": bootstrap_interval(
            ood_y,
            probabilities,
            rank_auc,
            seed=seed,
            replicates=bootstrap_replicates,
        ),
        "ood_brier": brier(ood_y, probabilities),
        "ood_expected_calibration_error_10_bin": calibration_error(ood_y, probabilities),
        "weights_standardized": model.weights,
        "standardization": {"means": standardizer.means, "scales": standardizer.scales},
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--episodes-csv", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--bootstrap-replicates", type=int, default=500)
    parser.add_argument("--seed", type=int, default=20260714)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.bootstrap_replicates < 100:
        raise SystemExit("--bootstrap-replicates must be at least 100")
    rows = load_rows(args.episodes_csv)
    train = [row for row in rows if row.split == "train"]
    ood = [row for row in rows if row.split == "ood"]
    if not train or not ood:
        raise SystemExit("Both train and ood rows are required")

    model_names = [
        "total_latency",
        "lambda_times_total",
        "decomposed_latency",
        "decomposed_burdens",
        "rigel_number",
    ]
    results = {
        "schema_version": "1.0",
        "source": str(args.episodes_csv),
        "outcome": "failure = 1 - recovered",
        "split_policy": "fit on train parameter region; evaluate only on ood region",
        "bootstrap_replicates": args.bootstrap_replicates,
        "models": {
            name: evaluate_model(name, train, ood, args.bootstrap_replicates, args.seed + index)
            for index, name in enumerate(model_names)
        },
        "claim_rule": (
            "No support is claimed unless a decomposed model exceeds both total-latency baselines "
            "on held-out AUC with uncertainty and does not materially worsen calibration."
        ),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(results, indent=2, sort_keys=True, allow_nan=False), encoding="utf-8")
    print(json.dumps(results["models"], indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
