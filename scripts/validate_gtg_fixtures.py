#!/usr/bin/env python3
"""Validate deterministic Generalized Transition Governance research fixtures."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

ACTIVATION_STATES = {"ACTIVE", "INACTIVE", "INCOMPLETE", "NOT_APPLICABLE", "ERROR"}
DISPOSITIONS = {"ALLOW", "DENY", "FAIL_CLOSED", "DEFER", "TRANSFORM", "ERROR"}
REQUIRED_TESTS = {
    "discoverable",
    "commit_reconstructable",
    "basis_attached",
    "included_in_admissibility",
    "outcome_sensitive",
}


def derive_activation(case: dict[str, Any]) -> str:
    tests = case["activation_tests"]
    material = case["material_relation"]

    if not material:
        justification = case.get("not_applicable_justification", "").strip()
        return "NOT_APPLICABLE" if justification else "ERROR"

    if case.get("expected_activation") == "NOT_APPLICABLE":
        return "ERROR"

    if not tests["discoverable"] or not tests["commit_reconstructable"] or not tests["basis_attached"]:
        return "INCOMPLETE"

    if not tests["included_in_admissibility"] or not tests["outcome_sensitive"]:
        return "INACTIVE"

    return "ACTIVE"


def derive_disposition(case: dict[str, Any], activation: str) -> str:
    if activation in {"INACTIVE", "INCOMPLETE", "ERROR"}:
        return "FAIL_CLOSED"

    if activation == "NOT_APPLICABLE":
        return "ALLOW"

    if case.get("standing_valid") is False:
        return "DEFER" if case.get("standing_defect_resolvable") else "DENY"

    if case.get("shared_constraint_satisfied") is False:
        return "DENY"

    if case.get("original_admissible") is False:
        if case.get("replacement_available") and case.get("transform_authority_valid"):
            return "TRANSFORM"
        return "DENY"

    return "ALLOW"


def validate_case(case: dict[str, Any], seen: set[str]) -> list[str]:
    errors: list[str] = []
    case_id = case.get("case_id")
    if not isinstance(case_id, str) or not case_id:
        return ["case_id must be a non-empty string"]
    if case_id in seen:
        errors.append(f"{case_id}: duplicate case_id")
    seen.add(case_id)

    claim_ids = case.get("claim_ids")
    if not isinstance(claim_ids, list) or not claim_ids or not all(isinstance(x, str) and x for x in claim_ids):
        errors.append(f"{case_id}: claim_ids must be a non-empty string array")

    tests = case.get("activation_tests")
    if not isinstance(tests, dict) or set(tests) != REQUIRED_TESTS:
        errors.append(f"{case_id}: activation_tests must contain exactly {sorted(REQUIRED_TESTS)}")
    elif not all(isinstance(value, bool) for value in tests.values()):
        errors.append(f"{case_id}: all activation tests must be boolean")

    if not isinstance(case.get("material_relation"), bool):
        errors.append(f"{case_id}: material_relation must be boolean")

    expected_activation = case.get("expected_activation")
    expected_disposition = case.get("expected_disposition")
    if expected_activation not in ACTIVATION_STATES:
        errors.append(f"{case_id}: invalid expected_activation {expected_activation!r}")
    if expected_disposition not in DISPOSITIONS:
        errors.append(f"{case_id}: invalid expected_disposition {expected_disposition!r}")

    if errors:
        return errors

    actual_activation = derive_activation(case)
    actual_disposition = derive_disposition(case, actual_activation)
    if actual_activation != expected_activation:
        errors.append(
            f"{case_id}: activation mismatch; expected {expected_activation}, derived {actual_activation}"
        )
    if actual_disposition != expected_disposition:
        errors.append(
            f"{case_id}: disposition mismatch; expected {expected_disposition}, derived {actual_disposition}"
        )
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "fixture",
        nargs="?",
        default="fixtures/gtg/activation_cases.json",
        help="Path to the GTG fixture bundle",
    )
    args = parser.parse_args()

    path = Path(args.fixture)
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"GTG fixture validation failed: {exc}", file=sys.stderr)
        return 2

    errors: list[str] = []
    if payload.get("schema_version") != "0.1.0":
        errors.append("schema_version must equal 0.1.0")
    if not isinstance(payload.get("profile"), str) or not payload["profile"]:
        errors.append("profile must be a non-empty string")

    cases = payload.get("cases")
    if not isinstance(cases, list) or not cases:
        errors.append("cases must be a non-empty array")
    else:
        seen: set[str] = set()
        for case in cases:
            if not isinstance(case, dict):
                errors.append("each case must be an object")
                continue
            errors.extend(validate_case(case, seen))

    if errors:
        print("GTG fixture validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(
        json.dumps(
            {
                "valid": True,
                "profile": payload["profile"],
                "case_count": len(cases),
                "activation_states": sorted(ACTIVATION_STATES),
                "dispositions": sorted(DISPOSITIONS),
            },
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
