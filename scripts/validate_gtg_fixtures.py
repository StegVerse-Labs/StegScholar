#!/usr/bin/env python3
"""Validate deterministic Generalized Transition Governance research fixtures."""

from __future__ import annotations

import argparse
import hashlib
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


def canonical_hash(value: Any) -> str:
    data = json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(data).hexdigest()


def derive_activation(case: dict[str, Any]) -> str:
    tests = case["activation_tests"]
    material = case["material_relation"]

    if case.get("force_not_applicable"):
        return "ERROR" if material else "NOT_APPLICABLE"
    if not material:
        return "NOT_APPLICABLE" if case.get("not_applicable_justification", "").strip() else "ERROR"
    if not tests["discoverable"] or not tests["commit_reconstructable"] or not tests["basis_attached"]:
        return "INCOMPLETE"
    if not tests["included_in_admissibility"] or not tests["outcome_sensitive"]:
        return "INACTIVE"
    return "ACTIVE"


def derive_disposition(case: dict[str, Any], activation: str) -> tuple[str, str]:
    if activation in {"INACTIVE", "INCOMPLETE", "ERROR"}:
        return "FAIL_CLOSED", f"activation:{activation.lower()}"
    if case.get("evidence_complete") is False or case.get("evidence_fresh") is False:
        return "FAIL_CLOSED", "evidence:incomplete_or_stale"
    if case.get("conflict_present"):
        if not case.get("precedence_rule_valid"):
            return "FAIL_CLOSED", "conflict:no_valid_precedence"
        if case.get("conflict_resolvable"):
            return "DEFER", "conflict:resolvable_dependency"
        return "FAIL_CLOSED", "conflict:unresolved"
    if activation == "NOT_APPLICABLE":
        return "ALLOW", "activation:not_applicable_proven"
    if case.get("execution_authority_valid") is False:
        return ("DEFER", "authority:resolvable") if case.get("authority_defect_resolvable") else ("DENY", "authority:invalid")
    if case.get("standing_valid") is False:
        return ("DEFER", "standing:resolvable") if case.get("standing_defect_resolvable") else ("DENY", "standing:invalid")
    if case.get("shared_constraint_satisfied") is False:
        return "DENY", "constraint:violated"
    if case.get("original_admissible") is False:
        if case.get("replacement_available") and case.get("transform_authority_valid"):
            return "TRANSFORM", "transform:authorized_replacement"
        return "DENY", "admissibility:no_valid_replacement"
    return "ALLOW", "all_declared_conditions_satisfied"


def validate_case(case: dict[str, Any], seen: set[str]) -> tuple[list[str], dict[str, Any] | None]:
    errors: list[str] = []
    case_id = case.get("case_id")
    if not isinstance(case_id, str) or not case_id:
        return ["case_id must be a non-empty string"], None
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
        return errors, None

    actual_activation = derive_activation(case)
    actual_disposition, precedence_reason = derive_disposition(case, actual_activation)
    if actual_activation != expected_activation:
        errors.append(f"{case_id}: activation mismatch; expected {expected_activation}, derived {actual_activation}")
    if actual_disposition != expected_disposition:
        errors.append(f"{case_id}: disposition mismatch; expected {expected_disposition}, derived {actual_disposition}")

    receipt = {
        "schema_version": "0.2.0",
        "record_id": f"GTG-DECISION-{case_id}",
        "case_id": case_id,
        "profile": "gtg-research-default-v0.2",
        "claim_ids": claim_ids,
        "activation_result": actual_activation,
        "final_disposition": actual_disposition,
        "precedence_reason": precedence_reason,
        "source_determinations": case.get("source_determinations", []),
        "input_hash": canonical_hash(case),
    }
    receipt["receipt_hash"] = canonical_hash(receipt)
    return errors, receipt


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("fixture", nargs="?", default="fixtures/gtg/activation_cases.json")
    parser.add_argument("--receipt", default="receipts/gtg/fixture-validation-receipt.json")
    parser.add_argument("--no-write", action="store_true")
    args = parser.parse_args()

    path = Path(args.fixture)
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"GTG fixture validation failed: {exc}", file=sys.stderr)
        return 2

    errors: list[str] = []
    if payload.get("schema_version") != "0.2.0":
        errors.append("schema_version must equal 0.2.0")
    if payload.get("profile") != "gtg-research-default-v0.2":
        errors.append("profile must equal gtg-research-default-v0.2")

    cases = payload.get("cases")
    receipts: list[dict[str, Any]] = []
    if not isinstance(cases, list) or not cases:
        errors.append("cases must be a non-empty array")
    else:
        seen: set[str] = set()
        for case in cases:
            if not isinstance(case, dict):
                errors.append("each case must be an object")
                continue
            case_errors, receipt = validate_case(case, seen)
            errors.extend(case_errors)
            if receipt is not None:
                receipts.append(receipt)

    if errors:
        print("GTG fixture validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    result = {
        "schema_version": "0.2.0",
        "valid": True,
        "profile": payload["profile"],
        "fixture_path": str(path),
        "fixture_hash": canonical_hash(payload),
        "case_count": len(cases),
        "case_receipts": receipts,
    }
    result["receipt_hash"] = canonical_hash(result)

    if not args.no_write:
        receipt_path = Path(args.receipt)
        receipt_path.parent.mkdir(parents=True, exist_ok=True)
        receipt_path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    print(json.dumps({"valid": True, "case_count": len(cases), "receipt_hash": result["receipt_hash"]}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
