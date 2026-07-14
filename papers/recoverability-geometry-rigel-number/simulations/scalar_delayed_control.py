#!/usr/bin/env python3
"""Synthetic delayed-control benchmark for Recoverability Geometry.

The failure label is defined independently from the candidate Rigel number:
an episode succeeds only when the plant remains inside a hard safety bound and
returns to the target set during the terminal recovery window.

The script uses only the Python standard library. It emits episode-level CSV,
a JSON summary, and deterministic configuration metadata suitable for replay.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import random
import statistics
from collections import deque
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable, Sequence


@dataclass(frozen=True)
class Config:
    seed: int = 20260714
    episodes: int = 10_000
    dt: float = 0.01
    horizon_s: float = 8.0
    recovery_window_s: float = 1.0
    target_abs_x: float = 0.15
    safety_abs_x: float = 4.0
    control_limit: float = 8.0
    observation_delay_s: tuple[float, float] = (0.00, 0.25)
    commitment_delay_s: tuple[float, float] = (0.00, 0.25)
    realization_delay_s: tuple[float, float] = (0.00, 0.25)
    plant_growth_rate: tuple[float, float] = (0.20, 1.40)
    controller_gain: tuple[float, float] = (1.00, 4.50)
    initial_abs_x: tuple[float, float] = (0.20, 1.50)
    process_noise_sd: tuple[float, float] = (0.00, 0.10)
    sensor_noise_sd: tuple[float, float] = (0.00, 0.10)
    margin_floor: float = 1e-9


@dataclass
class Episode:
    episode_id: int
    split: str
    alpha_o: float
    alpha_i: float
    alpha_r: float
    alpha_total: float
    lambda_growth: float
    controller_gain: float
    initial_abs_x: float
    process_noise_sd: float
    sensor_noise_sd: float
    delta_0: float
    V: float
    kappa: float
    rigel_number: float
    burden_o: float
    burden_i: float
    burden_r: float
    max_abs_x: float
    terminal_mean_abs_x: float
    safety_violated: int
    recovered: int


def clamp(value: float, low: float, high: float) -> float:
    return max(low, min(high, value))


def sample_uniform(rng: random.Random, bounds: Sequence[float]) -> float:
    return rng.uniform(float(bounds[0]), float(bounds[1]))


def delay_steps(delay_s: float, dt: float) -> int:
    return max(0, int(round(delay_s / dt)))


def delayed_value(queue: deque[float], value: float, steps: int) -> float:
    queue.append(value)
    while len(queue) > steps + 1:
        queue.popleft()
    return queue[0] if len(queue) == steps + 1 else queue[-1]


def rigel_number(lam: float, alpha: float, V: float, delta_0: float, kappa: float, floor: float) -> float:
    ratio = V / max(kappa * delta_0, floor)
    if ratio <= 1.0:
        return math.inf
    denominator = math.log(ratio)
    return lam * alpha / denominator if denominator > 0.0 else math.inf


def split_for_episode(index: int) -> str:
    # Held-out parameter region: every fifth episode is sampled from the upper
    # delay/growth ranges rather than merely held out at random.
    return "ood" if index % 5 == 0 else "train"


def bounded_sample(rng: random.Random, bounds: Sequence[float], split: str, upper_region: bool = False) -> float:
    low, high = float(bounds[0]), float(bounds[1])
    if split == "ood" and upper_region:
        cut = low + 0.72 * (high - low)
        return rng.uniform(cut, high)
    if split == "train" and upper_region:
        cut = low + 0.72 * (high - low)
        return rng.uniform(low, cut)
    return rng.uniform(low, high)


def run_episode(index: int, cfg: Config, rng: random.Random) -> Episode:
    split = split_for_episode(index)
    alpha_o = bounded_sample(rng, cfg.observation_delay_s, split, True)
    alpha_i = bounded_sample(rng, cfg.commitment_delay_s, split, True)
    alpha_r = bounded_sample(rng, cfg.realization_delay_s, split, True)
    lam = bounded_sample(rng, cfg.plant_growth_rate, split, True)
    gain = sample_uniform(rng, cfg.controller_gain)
    x0_abs = sample_uniform(rng, cfg.initial_abs_x)
    process_sd = sample_uniform(rng, cfg.process_noise_sd)
    sensor_sd = sample_uniform(rng, cfg.sensor_noise_sd)
    x = x0_abs if rng.random() < 0.5 else -x0_abs

    obs_steps = delay_steps(alpha_o, cfg.dt)
    commit_steps = delay_steps(alpha_i, cfg.dt)
    realize_steps = delay_steps(alpha_r, cfg.dt)
    obs_q: deque[float] = deque()
    commit_q: deque[float] = deque()
    act_q: deque[float] = deque()

    terminal_samples: list[float] = []
    max_abs_x = abs(x)
    safety_violated = False
    total_steps = int(round(cfg.horizon_s / cfg.dt))
    recovery_steps = max(1, int(round(cfg.recovery_window_s / cfg.dt)))

    for step in range(total_steps):
        measured = x + rng.gauss(0.0, sensor_sd)
        observed = delayed_value(obs_q, measured, obs_steps)
        proposed_u = clamp(-gain * observed, -cfg.control_limit, cfg.control_limit)
        committed_u = delayed_value(commit_q, proposed_u, commit_steps)
        realized_u = delayed_value(act_q, committed_u, realize_steps)
        process = rng.gauss(0.0, process_sd)
        x += cfg.dt * (lam * x + realized_u + process)
        max_abs_x = max(max_abs_x, abs(x))
        if abs(x) > cfg.safety_abs_x:
            safety_violated = True
        if step >= total_steps - recovery_steps:
            terminal_samples.append(abs(x))

    terminal_mean = statistics.fmean(terminal_samples)
    recovered = (not safety_violated) and terminal_mean <= cfg.target_abs_x

    # V and delta_0 are measured independently from the candidate outcome:
    # V is initial distance to the hard safety boundary; delta_0 is the
    # combined initial state/sensor uncertainty proxy.
    V = max(cfg.safety_abs_x - x0_abs, cfg.margin_floor)
    delta_0 = max(math.hypot(x0_abs, sensor_sd), cfg.margin_floor)
    kappa = 1.0
    alpha = alpha_o + alpha_i + alpha_r
    ri = rigel_number(lam, alpha, V, delta_0, kappa, cfg.margin_floor)

    return Episode(
        episode_id=index,
        split=split,
        alpha_o=alpha_o,
        alpha_i=alpha_i,
        alpha_r=alpha_r,
        alpha_total=alpha,
        lambda_growth=lam,
        controller_gain=gain,
        initial_abs_x=x0_abs,
        process_noise_sd=process_sd,
        sensor_noise_sd=sensor_sd,
        delta_0=delta_0,
        V=V,
        kappa=kappa,
        rigel_number=ri,
        burden_o=lam * alpha_o,
        burden_i=lam * alpha_i,
        burden_r=lam * alpha_r,
        max_abs_x=max_abs_x,
        terminal_mean_abs_x=terminal_mean,
        safety_violated=int(safety_violated),
        recovered=int(recovered),
    )


def rank_auc(labels: Sequence[int], scores: Sequence[float]) -> float:
    pairs = sorted(zip(scores, labels), key=lambda item: item[0])
    n_pos = sum(labels)
    n_neg = len(labels) - n_pos
    if n_pos == 0 or n_neg == 0:
        return float("nan")
    rank_sum = 0.0
    index = 0
    while index < len(pairs):
        end = index + 1
        while end < len(pairs) and pairs[end][0] == pairs[index][0]:
            end += 1
        avg_rank = ((index + 1) + end) / 2.0
        rank_sum += avg_rank * sum(label for _, label in pairs[index:end])
        index = end
    return (rank_sum - n_pos * (n_pos + 1) / 2.0) / (n_pos * n_neg)


def summarize(rows: Sequence[Episode], cfg: Config) -> dict[str, object]:
    result: dict[str, object] = {"config": asdict(cfg), "episodes": len(rows), "splits": {}}
    for split in ("train", "ood", "all"):
        subset = list(rows) if split == "all" else [row for row in rows if row.split == split]
        failure = [1 - row.recovered for row in subset]
        finite_ri = [row.rigel_number if math.isfinite(row.rigel_number) else 1e9 for row in subset]
        metrics = {
            "count": len(subset),
            "failure_rate": statistics.fmean(failure) if subset else float("nan"),
            "auc_total_latency": rank_auc(failure, [row.alpha_total for row in subset]),
            "auc_lambda_times_latency": rank_auc(failure, [row.lambda_growth * row.alpha_total for row in subset]),
            "auc_rigel_number": rank_auc(failure, finite_ri),
            "mean_rigel_recovered": statistics.fmean(
                [row.rigel_number for row in subset if row.recovered and math.isfinite(row.rigel_number)]
            ) if any(row.recovered and math.isfinite(row.rigel_number) for row in subset) else float("nan"),
            "mean_rigel_failed": statistics.fmean(
                [row.rigel_number for row in subset if not row.recovered and math.isfinite(row.rigel_number)]
            ) if any((not row.recovered) and math.isfinite(row.rigel_number) for row in subset) else float("nan"),
        }
        result["splits"][split] = metrics
    result["interpretation_rule"] = (
        "No support is claimed unless the candidate score improves on total latency "
        "and lambda*latency in the held-out OOD parameter region."
    )
    return result


def write_csv(path: Path, rows: Iterable[Episode]) -> None:
    rows = list(rows)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(asdict(rows[0]).keys()))
        writer.writeheader()
        for row in rows:
            record = asdict(row)
            if not math.isfinite(record["rigel_number"]):
                record["rigel_number"] = "inf"
            writer.writerow(record)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--episodes", type=int, default=10_000)
    parser.add_argument("--seed", type=int, default=20260714)
    parser.add_argument("--output-dir", type=Path, default=Path("generated/scalar-delayed-control"))
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.episodes < 100:
        raise SystemExit("--episodes must be at least 100")
    cfg = Config(seed=args.seed, episodes=args.episodes)
    rng = random.Random(cfg.seed)
    rows = [run_episode(index, cfg, rng) for index in range(cfg.episodes)]
    summary = summarize(rows, cfg)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    write_csv(args.output_dir / "episodes.csv", rows)
    (args.output_dir / "summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True, allow_nan=False), encoding="utf-8"
    )
    (args.output_dir / "config.json").write_text(
        json.dumps(asdict(cfg), indent=2, sort_keys=True), encoding="utf-8"
    )
    print(json.dumps(summary["splits"], indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
