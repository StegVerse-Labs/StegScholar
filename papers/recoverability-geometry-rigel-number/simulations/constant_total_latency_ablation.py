#!/usr/bin/env python3
"""Constant-total-latency ablation for the Rigel validation program.

This benchmark holds total latency fixed while redistributing it among observation,
commitment, and realization phases. Outcome labels remain independent of the Rigel
number. The goal is to test whether phase partition carries information beyond total
latency in the current delayed-control family.
"""

from __future__ import annotations

import argparse
import csv
import importlib.util
import json
import random
import statistics
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable

MODULE_PATH = Path(__file__).with_name("scalar_delayed_control.py")
SPEC = importlib.util.spec_from_file_location("scalar_delayed_control", MODULE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(f"Unable to load benchmark module from {MODULE_PATH}")
BASE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = BASE
SPEC.loader.exec_module(BASE)


@dataclass(frozen=True)
class Partition:
    name: str
    fraction_o: float
    fraction_i: float
    fraction_r: float

    def delays(self, total: float) -> tuple[float, float, float]:
        return (
            total * self.fraction_o,
            total * self.fraction_i,
            total * self.fraction_r,
        )


@dataclass
class AblationRow:
    scenario_id: int
    partition: str
    alpha_total: float
    alpha_o: float
    alpha_i: float
    alpha_r: float
    lambda_growth: float
    controller_gain: float
    initial_abs_x: float
    process_noise_sd: float
    sensor_noise_sd: float
    recovered: int
    safety_violated: int
    max_abs_x: float
    terminal_mean_abs_x: float


PARTITIONS = (
    Partition("balanced", 1 / 3, 1 / 3, 1 / 3),
    Partition("observation_heavy", 0.80, 0.10, 0.10),
    Partition("commitment_heavy", 0.10, 0.80, 0.10),
    Partition("realization_heavy", 0.10, 0.10, 0.80),
    Partition("observation_light", 0.05, 0.475, 0.475),
    Partition("commitment_light", 0.475, 0.05, 0.475),
    Partition("realization_light", 0.475, 0.475, 0.05),
)


def simulate_fixed(
    *,
    cfg: BASE.Config,
    alpha_o: float,
    alpha_i: float,
    alpha_r: float,
    lam: float,
    gain: float,
    x0_abs: float,
    process_sd: float,
    sensor_sd: float,
    seed: int,
) -> tuple[int, int, float, float]:
    """Run one deterministic episode for a fixed parameter tuple."""

    rng = random.Random(seed)
    x = x0_abs if rng.random() < 0.5 else -x0_abs

    obs_steps = BASE.delay_steps(alpha_o, cfg.dt)
    commit_steps = BASE.delay_steps(alpha_i, cfg.dt)
    realize_steps = BASE.delay_steps(alpha_r, cfg.dt)
    from collections import deque

    obs_q = deque()
    commit_q = deque()
    act_q = deque()

    terminal_samples: list[float] = []
    max_abs_x = abs(x)
    safety_violated = False
    total_steps = int(round(cfg.horizon_s / cfg.dt))
    recovery_steps = max(1, int(round(cfg.recovery_window_s / cfg.dt)))

    for step in range(total_steps):
        measured = x + rng.gauss(0.0, sensor_sd)
        observed = BASE.delayed_value(obs_q, measured, obs_steps)
        proposed_u = BASE.clamp(-gain * observed, -cfg.control_limit, cfg.control_limit)
        committed_u = BASE.delayed_value(commit_q, proposed_u, commit_steps)
        realized_u = BASE.delayed_value(act_q, committed_u, realize_steps)
        process = rng.gauss(0.0, process_sd)
        x += cfg.dt * (lam * x + realized_u + process)
        max_abs_x = max(max_abs_x, abs(x))
        if abs(x) > cfg.safety_abs_x:
            safety_violated = True
        if step >= total_steps - recovery_steps:
            terminal_samples.append(abs(x))

    terminal_mean = statistics.fmean(terminal_samples)
    recovered = (not safety_violated) and terminal_mean <= cfg.target_abs_x
    return int(recovered), int(safety_violated), max_abs_x, terminal_mean


def generate_rows(scenarios: int, seed: int, total_latency: float) -> list[AblationRow]:
    cfg = BASE.Config(episodes=max(100, scenarios))
    sampler = random.Random(seed)
    rows: list[AblationRow] = []

    for scenario_id in range(scenarios):
        lam = sampler.uniform(*cfg.plant_growth_rate)
        gain = sampler.uniform(*cfg.controller_gain)
        x0_abs = sampler.uniform(*cfg.initial_abs_x)
        process_sd = sampler.uniform(*cfg.process_noise_sd)
        sensor_sd = sampler.uniform(*cfg.sensor_noise_sd)
        episode_seed = sampler.randrange(0, 2**63)

        for partition in PARTITIONS:
            alpha_o, alpha_i, alpha_r = partition.delays(total_latency)
            recovered, safety_violated, max_abs_x, terminal_mean = simulate_fixed(
                cfg=cfg,
                alpha_o=alpha_o,
                alpha_i=alpha_i,
                alpha_r=alpha_r,
                lam=lam,
                gain=gain,
                x0_abs=x0_abs,
                process_sd=process_sd,
                sensor_sd=sensor_sd,
                seed=episode_seed,
            )
            rows.append(
                AblationRow(
                    scenario_id=scenario_id,
                    partition=partition.name,
                    alpha_total=total_latency,
                    alpha_o=alpha_o,
                    alpha_i=alpha_i,
                    alpha_r=alpha_r,
                    lambda_growth=lam,
                    controller_gain=gain,
                    initial_abs_x=x0_abs,
                    process_noise_sd=process_sd,
                    sensor_noise_sd=sensor_sd,
                    recovered=recovered,
                    safety_violated=safety_violated,
                    max_abs_x=max_abs_x,
                    terminal_mean_abs_x=terminal_mean,
                )
            )
    return rows


def summarize(rows: Iterable[AblationRow]) -> dict[str, object]:
    rows = list(rows)
    by_partition: dict[str, dict[str, float | int]] = {}
    for partition in PARTITIONS:
        subset = [row for row in rows if row.partition == partition.name]
        by_partition[partition.name] = {
            "count": len(subset),
            "recovery_rate": statistics.fmean(row.recovered for row in subset),
            "safety_violation_rate": statistics.fmean(row.safety_violated for row in subset),
            "mean_max_abs_x": statistics.fmean(row.max_abs_x for row in subset),
            "mean_terminal_abs_x": statistics.fmean(row.terminal_mean_abs_x for row in subset),
        }

    scenario_patterns: dict[str, int] = {}
    scenario_ids = sorted({row.scenario_id for row in rows})
    for scenario_id in scenario_ids:
        subset = sorted(
            (row for row in rows if row.scenario_id == scenario_id),
            key=lambda row: row.partition,
        )
        pattern = ",".join(f"{row.partition}:{row.recovered}" for row in subset)
        scenario_patterns[pattern] = scenario_patterns.get(pattern, 0) + 1

    differing = 0
    for scenario_id in scenario_ids:
        labels = {row.recovered for row in rows if row.scenario_id == scenario_id}
        differing += int(len(labels) > 1)

    return {
        "scenario_count": len(scenario_ids),
        "row_count": len(rows),
        "partition_count": len(PARTITIONS),
        "partitions": by_partition,
        "scenarios_with_partition_dependent_outcome": differing,
        "partition_dependent_fraction": differing / len(scenario_ids) if scenario_ids else 0.0,
        "outcome_patterns": scenario_patterns,
        "interpretation_rule": (
            "Partition effects are supported in this benchmark only if matched scenarios with "
            "identical total latency and plant parameters show reproducible outcome differences. "
            "Such differences remain benchmark-specific and do not establish cross-domain universality."
        ),
    }


def write_csv(path: Path, rows: Iterable[AblationRow]) -> None:
    rows = list(rows)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(asdict(rows[0]).keys()))
        writer.writeheader()
        for row in rows:
            writer.writerow(asdict(row))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--scenarios", type=int, default=2000)
    parser.add_argument("--seed", type=int, default=20260714)
    parser.add_argument("--total-latency", type=float, default=0.45)
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("generated/constant-total-latency-ablation"),
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.scenarios < 100:
        raise SystemExit("--scenarios must be at least 100")
    if args.total_latency < 0.0:
        raise SystemExit("--total-latency must be nonnegative")

    rows = generate_rows(args.scenarios, args.seed, args.total_latency)
    summary = summarize(rows)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    write_csv(args.output_dir / "episodes.csv", rows)
    (args.output_dir / "summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True), encoding="utf-8"
    )
    (args.output_dir / "config.json").write_text(
        json.dumps(
            {
                "benchmark_id": "rigel-constant-total-latency-ablation-v1",
                "scenarios": args.scenarios,
                "seed": args.seed,
                "total_latency": args.total_latency,
                "partitions": [asdict(partition) for partition in PARTITIONS],
            },
            indent=2,
            sort_keys=True,
        ),
        encoding="utf-8",
    )
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
