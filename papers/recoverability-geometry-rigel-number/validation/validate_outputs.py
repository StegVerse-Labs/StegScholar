#!/usr/bin/env python3
"""Validate outputs produced by scalar_delayed_control.py.

Fails closed when required files, schema fields, finite metrics, split coverage,
or deterministic configuration evidence are missing.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
from pathlib import Path

REQUIRED_SUMMARY_METRICS = {
    "count",
    "failure_rate",
    "auc_total_latency",
    "auc_lambda_times_latency",
    "auc_rigel_number",
    "mean_rigel_recovered",
    "mean_rigel_failed",
}

REQUIRED_EPISODE_COLUMNS = {
    "episode_id",
    "split",
    "alpha_o",
    "alpha_i",
    "alpha_r",
    "alpha_total",
    "lambda_growth",
    "delta_0",
    "V",
    "rigel_number",
    "max_abs_x",
    "terminal_mean_abs_x",
    "safety_violated",
    "recovered",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def require(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def finite_probability(value: object) -> bool:
    return isinstance(value, (int, float)) and math.isfinite(float(value)) and 0.0 <= float(value) <= 1.0


def validate(output_dir: Path, expected_episodes: int) -> dict[str, object]:
    errors: list[str] = []
    warnings: list[str] = []
    summary_path = output_dir / "summary.json"
    config_path = output_dir / "config.json"
    episodes_path = output_dir / "episodes.csv"

    for path in (summary_path, config_path, episodes_path):
        require(path.is_file(), f"missing required output: {path}", errors)
    if errors:
        return {"status": "FAILED", "errors": errors, "warnings": warnings}

    summary = json.loads(summary_path.read_text(encoding="utf-8"))
    config = json.loads(config_path.read_text(encoding="utf-8"))
    require(summary.get("episodes") == expected_episodes, "summary episode count mismatch", errors)
    require(config.get("episodes") == expected_episodes, "config episode count mismatch", errors)
    require(config.get("seed") is not None, "deterministic seed missing", errors)

    splits = summary.get("splits")
    require(isinstance(splits, dict), "summary.splits missing", errors)
    if isinstance(splits, dict):
        for split in ("train", "ood", "all"):
            metrics = splits.get(split)
            require(isinstance(metrics, dict), f"missing split metrics: {split}", errors)
            if not isinstance(metrics, dict):
                continue
            require(REQUIRED_SUMMARY_METRICS.issubset(metrics), f"missing metrics in split: {split}", errors)
            require(int(metrics.get("count", 0)) > 0, f"empty split: {split}", errors)
            require(finite_probability(metrics.get("failure_rate")), f"invalid failure rate: {split}", errors)
            for name in ("auc_total_latency", "auc_lambda_times_latency", "auc_rigel_number"):
                require(finite_probability(metrics.get(name)), f"invalid {name}: {split}", errors)

    row_count = 0
    split_counts = {"train": 0, "ood": 0}
    recovered_values: set[str] = set()
    with episodes_path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        require(reader.fieldnames is not None, "episodes.csv has no header", errors)
        if reader.fieldnames is not None:
            require(REQUIRED_EPISODE_COLUMNS.issubset(reader.fieldnames), "episodes.csv missing required columns", errors)
        for row in reader:
            row_count += 1
            split = row.get("split", "")
            if split in split_counts:
                split_counts[split] += 1
            recovered_values.add(row.get("recovered", ""))
            try:
                total = float(row["alpha_total"])
                parts = float(row["alpha_o"]) + float(row["alpha_i"]) + float(row["alpha_r"])
                require(abs(total - parts) <= 1e-9, f"latency decomposition mismatch at row {row_count}", errors)
                require(float(row["V"]) > 0.0, f"nonpositive V at row {row_count}", errors)
                require(float(row["delta_0"]) > 0.0, f"nonpositive delta_0 at row {row_count}", errors)
            except (KeyError, TypeError, ValueError) as exc:
                errors.append(f"invalid numeric row {row_count}: {exc}")
            if len(errors) > 100:
                errors.append("validation stopped after more than 100 errors")
                break

    require(row_count == expected_episodes, "episodes.csv row count mismatch", errors)
    require(split_counts["train"] > 0 and split_counts["ood"] > 0, "train/OOD split coverage missing", errors)
    require({"0", "1"}.issubset(recovered_values), "both recovery outcome classes are required", errors)

    auc_support = None
    if isinstance(splits, dict) and isinstance(splits.get("ood"), dict):
        ood = splits["ood"]
        auc_support = float(ood["auc_rigel_number"]) > max(
            float(ood["auc_total_latency"]), float(ood["auc_lambda_times_latency"])
        )
        if not auc_support:
            warnings.append("candidate score did not outperform both declared OOD baselines; no support may be claimed")

    manifest = {
        "summary.json": sha256(summary_path),
        "config.json": sha256(config_path),
        "episodes.csv": sha256(episodes_path),
    }
    report = {
        "status": "FAILED" if errors else "COMPLETE",
        "errors": errors,
        "warnings": warnings,
        "expected_episodes": expected_episodes,
        "observed_episodes": row_count,
        "split_counts": split_counts,
        "candidate_ood_support": auc_support,
        "claim_boundary": "Validation success proves executable and structurally valid outputs only; scientific support requires stronger fitted baselines, ablations, intervals, and replication.",
        "sha256": manifest,
    }
    return report


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--expected-episodes", type=int, required=True)
    parser.add_argument("--report", type=Path, required=True)
    args = parser.parse_args()

    report = validate(args.output_dir, args.expected_episodes)
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(report, indent=2, sort_keys=True), encoding="utf-8")
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if report["status"] == "COMPLETE" else 1


if __name__ == "__main__":
    raise SystemExit(main())
