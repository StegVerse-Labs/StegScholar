#!/usr/bin/env python3
"""Evaluate Rigel validation outputs into a durable machine-owned task state.

The evaluator fails closed. It never equates file presence with scientific support.
It emits exactly one of COMPLETE, BLOCKED, RETRY, REVIEW_REQUIRED, or FAILED and
identifies the next executable repository task.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Any

VALID_STATES = {"COMPLETE", "BLOCKED", "RETRY", "REVIEW_REQUIRED", "FAILED"}


def read_json(path: Path) -> dict[str, Any]:
    if not path.is_file():
        raise FileNotFoundError(str(path))
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"Expected object in {path}")
    return data


def finite_number(value: Any) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(float(value))


def model_metric(models: dict[str, Any], name: str, key: str) -> float:
    model = models.get(name)
    if not isinstance(model, dict):
        raise ValueError(f"Missing model {name}")
    value = model.get(key)
    if not finite_number(value):
        raise ValueError(f"Missing finite {key} for {name}")
    return float(value)


def evaluate(baselines: dict[str, Any], ablation: dict[str, Any]) -> dict[str, Any]:
    models = baselines.get("models")
    if not isinstance(models, dict):
        raise ValueError("baseline metrics missing models")

    required = {
        "total_latency",
        "lambda_times_total",
        "decomposed_latency",
        "decomposed_burdens",
        "rigel_number",
    }
    missing_models = sorted(required - set(models))
    if missing_models:
        raise ValueError(f"missing models: {missing_models}")

    total_auc = model_metric(models, "total_latency", "ood_auc")
    lambda_auc = model_metric(models, "lambda_times_total", "ood_auc")
    decomposed_auc = model_metric(models, "decomposed_latency", "ood_auc")
    burden_auc = model_metric(models, "decomposed_burdens", "ood_auc")
    rigel_auc = model_metric(models, "rigel_number", "ood_auc")

    total_ece = model_metric(models, "total_latency", "ood_expected_calibration_error_10_bin")
    lambda_ece = model_metric(models, "lambda_times_total", "ood_expected_calibration_error_10_bin")
    decomposed_ece = model_metric(models, "decomposed_latency", "ood_expected_calibration_error_10_bin")
    burden_ece = model_metric(models, "decomposed_burdens", "ood_expected_calibration_error_10_bin")

    fraction = ablation.get("partition_dependent_fraction")
    scenarios = ablation.get("scenario_count")
    if not finite_number(fraction) or not isinstance(scenarios, int) or scenarios < 100:
        raise ValueError("ablation summary lacks valid scenario_count or partition_dependent_fraction")

    best_aggregate_auc = max(total_auc, lambda_auc)
    best_decomposed_auc = max(decomposed_auc, burden_auc)
    best_aggregate_ece = min(total_ece, lambda_ece)
    best_decomposed_ece = decomposed_ece if decomposed_auc >= burden_auc else burden_ece

    auc_delta = best_decomposed_auc - best_aggregate_auc
    calibration_delta = best_decomposed_ece - best_aggregate_ece
    partition_effect_observed = float(fraction) > 0.0

    # A positive candidate result still requires independent package cross-check,
    # paired uncertainty, and manuscript review, so it is REVIEW_REQUIRED rather
    # than COMPLETE. A negative result is also REVIEW_REQUIRED because the theory
    # must be revised or rejected rather than silently marked complete.
    if not partition_effect_observed:
        status = "REVIEW_REQUIRED"
        next_task = {
            "task_id": "RIGEL-REVISE-PHASE-HYPOTHESIS-006",
            "owner_repository": "StegVerse-Labs/StegScholar",
            "location": "papers/recoverability-geometry-rigel-number/claims-register.md",
            "action": "Revise or reject the phase-location hypothesis for the current scalar benchmark and record the null result.",
        }
        reason = "No matched scenario changed outcome when phase allocation changed at fixed total latency."
    elif auc_delta <= 0.0:
        status = "REVIEW_REQUIRED"
        next_task = {
            "task_id": "RIGEL-REVISE-PREDICTIVE-CLAIM-007",
            "owner_repository": "StegVerse-Labs/StegScholar",
            "location": "papers/recoverability-geometry-rigel-number/claims-register.md",
            "action": "Record that decomposed latency did not outperform both aggregate baselines in held-out evaluation and revise the predictive claim.",
        }
        reason = "Phase allocation affected some matched outcomes, but fitted decomposed latency did not exceed the strongest aggregate baseline."
    else:
        status = "REVIEW_REQUIRED"
        next_task = {
            "task_id": "RIGEL-STATISTICAL-CROSSCHECK-005",
            "owner_repository": "StegVerse-Labs/StegScholar",
            "location": "papers/recoverability-geometry-rigel-number/simulations/crosscheck_baselines.py",
            "action": "Cross-check fitted results with a trusted statistical package and add paired bootstrap intervals for AUC differences before any support claim.",
        }
        reason = "Candidate improvement observed, but independent statistical cross-check and paired uncertainty remain mandatory."

    state = {
        "schema_version": "1.0",
        "goal_id": "RIGEL-VALIDATION-001",
        "status": status,
        "reason": reason,
        "evidence": {
            "ood_auc": {
                "total_latency": total_auc,
                "lambda_times_total": lambda_auc,
                "decomposed_latency": decomposed_auc,
                "decomposed_burdens": burden_auc,
                "rigel_number": rigel_auc,
                "best_decomposed_minus_best_aggregate": auc_delta,
            },
            "calibration": {
                "best_decomposed_minus_best_aggregate_ece": calibration_delta,
            },
            "constant_total_latency_ablation": {
                "scenario_count": scenarios,
                "partition_dependent_fraction": float(fraction),
            },
        },
        "next_executable_task": next_task,
        "claim_boundary": (
            "This state evaluates one constructed scalar benchmark only. It does not establish "
            "a universal Ri=1 threshold, cross-domain validity, publication readiness, or release readiness."
        ),
    }
    if state["status"] not in VALID_STATES:
        raise AssertionError("invalid state")
    return state


def failure_state(message: str) -> dict[str, Any]:
    return {
        "schema_version": "1.0",
        "goal_id": "RIGEL-VALIDATION-001",
        "status": "FAILED",
        "reason": message,
        "next_executable_task": {
            "task_id": "RIGEL-REPAIR-VALIDATION-EVIDENCE-004",
            "owner_repository": "StegVerse-Labs/StegScholar",
            "location": ".github/workflows/rigel-validation.yml",
            "action": "Repair missing or malformed validation outputs and rerun the repository workflow.",
        },
        "claim_boundary": "Missing evidence is never treated as success.",
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--baseline-metrics", type=Path, required=True)
    parser.add_argument("--ablation-summary", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        state = evaluate(read_json(args.baseline_metrics), read_json(args.ablation_summary))
        exit_code = 0
    except Exception as exc:  # fail closed and preserve a machine-readable record
        state = failure_state(f"{type(exc).__name__}: {exc}")
        exit_code = 1
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(state, indent=2, sort_keys=True), encoding="utf-8")
    print(json.dumps(state, indent=2, sort_keys=True))
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
