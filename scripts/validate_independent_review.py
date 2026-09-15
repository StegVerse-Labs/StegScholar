#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, Iterable, Tuple

ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "fixtures/independent-review/independent-review-cases.json"
REQUIRED_DIMENSIONS = (
    "common_control",
    "rule_authorship",
    "financial_interest",
    "evaluator_identity",
    "execution_path_control",
)
VALID_STATES = {"SEPARATE", "CONFLICT", "UNRESOLVED"}


def evaluate_review(review_available: bool, dimensions: Dict[str, Dict[str, Any]]) -> Tuple[str, list[str]]:
    if not review_available:
        return "UNRESOLVED", ["REVIEW_NOT_AVAILABLE"]

    reason_codes: list[str] = []
    saw_unresolved = False
    for name in REQUIRED_DIMENSIONS:
        dim = dimensions.get(name)
        if not isinstance(dim, dict):
            return "UNRESOLVED", [f"MISSING_DIMENSION:{name}"]
        state = dim.get("state")
        refs = dim.get("evidence_refs")
        if state not in VALID_STATES:
            return "UNRESOLVED", [f"INVALID_DIMENSION_STATE:{name}"]
        if not isinstance(refs, list):
            return "UNRESOLVED", [f"INVALID_EVIDENCE_REFS:{name}"]
        if state == "CONFLICT":
            reason_codes.append(f"CONFLICT:{name}")
        elif state == "UNRESOLVED" or len(refs) == 0:
            saw_unresolved = True
            reason_codes.append(f"UNRESOLVED:{name}")

    conflicts = [r for r in reason_codes if r.startswith("CONFLICT:")]
    if conflicts:
        return "NOT_INDEPENDENT", conflicts
    if saw_unresolved:
        return "UNRESOLVED", reason_codes
    return "INDEPENDENT", ["ALL_REQUIRED_DIMENSIONS_SEPARATE"]


def validate_cases(cases: Iterable[Dict[str, Any]]) -> list[str]:
    failures: list[str] = []
    for case in cases:
        case_id = case.get("case_id", "<missing>")
        actual, reasons = evaluate_review(bool(case.get("review_available")), case.get("dimensions", {}))
        expected = case.get("expected_state")
        if actual != expected:
            failures.append(f"{case_id}: expected {expected}, got {actual} ({','.join(reasons)})")
    return failures


def main() -> int:
    payload = json.loads(FIXTURES.read_text())
    failures = validate_cases(payload["cases"])
    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1
    print(f"PASS: {len(payload['cases'])} independent-review cases")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
