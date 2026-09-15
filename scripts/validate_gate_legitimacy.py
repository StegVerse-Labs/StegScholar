from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
FIXTURE_PATH = ROOT / "fixtures/gate-legitimacy/gate-legitimacy-cases.json"

VALID_STATES = {"LEGITIMATE", "ILLEGITIMATE", "CONFLICTED", "UNRESOLVED"}


def _present(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def derive_legitimacy_state(record: dict[str, Any]) -> tuple[str, list[str]]:
    reasons: list[str] = []

    if record.get("authority_effect") != "NONE":
        return "ILLEGITIMATE", ["AUTHORITY_EFFECT_MUST_BE_NONE"]

    standard = record.get("governing_standard") or {}
    if not _present(standard.get("standard_ref")):
        reasons.append("MISSING_STANDARD_REF")
    if not _present(standard.get("provenance_ref")):
        reasons.append("MISSING_STANDARD_PROVENANCE")
    if not _present(standard.get("authority_ref")):
        reasons.append("MISSING_STANDARD_AUTHORITY")
    if standard.get("status") == "INVALID":
        reasons.append("INVALID_STANDARD_BASIS")
    if reasons:
        return "ILLEGITIMATE", reasons
    if standard.get("status") in {"CONFLICTED", "UNRESOLVED"}:
        return "UNRESOLVED", ["STANDARD_BASIS_NOT_RESOLVED"]

    evidence = record.get("evidence_rules") or {}
    if not _present(evidence.get("rule_set_ref")):
        reasons.append("MISSING_EVIDENCE_RULE_SET")
    if not _present(evidence.get("provenance_ref")):
        reasons.append("MISSING_EVIDENCE_RULE_PROVENANCE")
    if not _present(evidence.get("controller_ref")):
        reasons.append("MISSING_EVIDENCE_RULE_CONTROLLER")
    if evidence.get("frozen_before_candidate_evaluation") is not True:
        reasons.append("EVIDENCE_RULES_NOT_PREDECLARED")
    if evidence.get("status") == "INVALID":
        reasons.append("INVALID_EVIDENCE_RULE_BASIS")
    if reasons:
        return "ILLEGITIMATE", reasons
    if evidence.get("status") in {"CONFLICTED", "UNRESOLVED"}:
        return "UNRESOLVED", ["EVIDENCE_RULE_BASIS_NOT_RESOLVED"]

    evaluator = record.get("evaluator") or {}
    if not _present(evaluator.get("evaluator_ref")):
        return "UNRESOLVED", ["MISSING_EVALUATOR_REF"]
    if not _present(evaluator.get("standing_ref")):
        return "UNRESOLVED", ["MISSING_EVALUATOR_STANDING"]
    if evaluator.get("status") == "INVALID":
        return "ILLEGITIMATE", ["INVALID_EVALUATOR_STANDING"]

    execution = record.get("execution_path") or {}
    if not _present(execution.get("path_ref")):
        return "UNRESOLVED", ["MISSING_EXECUTION_PATH_REF"]
    if not _present(execution.get("controller_ref")):
        return "UNRESOLVED", ["MISSING_EXECUTION_PATH_CONTROLLER"]
    if execution.get("status") == "INVALID":
        return "ILLEGITIMATE", ["INVALID_EXECUTION_PATH_BASIS"]

    conflict_present = any(
        bool(evaluator.get(flag))
        for flag in (
            "same_as_standard_controller",
            "same_as_evidence_rule_controller",
            "same_as_execution_path_controller",
        )
    ) or bool(evaluator.get("conflict_refs")) or bool(execution.get("conflict_refs"))

    review = record.get("challenge_review") or {}
    if conflict_present:
        if review.get("independent_review_required") is not True:
            return "CONFLICTED", ["MATERIAL_CONFLICT_REQUIRES_INDEPENDENT_REVIEW"]
        if review.get("independent_review_satisfied") is not True:
            return "CONFLICTED", ["INDEPENDENT_REVIEW_REQUIRED"]
        if not _present(review.get("independent_review_ref")):
            return "CONFLICTED", ["MISSING_INDEPENDENT_REVIEW_REF"]

    if evaluator.get("status") == "UNRESOLVED" or execution.get("status") == "UNRESOLVED":
        return "UNRESOLVED", ["ROLE_OR_EXECUTION_CONTROL_NOT_RESOLVED"]

    return "LEGITIMATE", ["ALL_REQUIRED_PREDICATES_SATISFIED"]


def validate_record(record: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    required = {
        "schema_version",
        "record_id",
        "gate_id",
        "governing_standard",
        "evidence_rules",
        "evaluator",
        "execution_path",
        "challenge_review",
        "assessment",
        "authority_effect",
    }
    missing = sorted(required - set(record))
    if missing:
        errors.append(f"missing required keys: {missing}")
        return errors

    if record.get("schema_version") != "0.1.0":
        errors.append("schema_version must be 0.1.0")
    if record.get("authority_effect") != "NONE":
        errors.append("authority_effect must be NONE")

    assessment = record.get("assessment") or {}
    claimed_state = assessment.get("legitimacy_state")
    if claimed_state not in VALID_STATES:
        errors.append(f"invalid legitimacy_state: {claimed_state}")
    derived_state, _ = derive_legitimacy_state(record)
    if claimed_state != derived_state:
        errors.append(f"claimed state {claimed_state} != derived state {derived_state}")

    return errors


def validate_fixture_file(path: Path = FIXTURE_PATH) -> dict[str, Any]:
    payload = json.loads(path.read_text())
    results = []
    for case in payload.get("cases", []):
        record = case["record"]
        errors = validate_record(record)
        derived_state, reasons = derive_legitimacy_state(record)
        if derived_state != case.get("expected_state"):
            errors.append(
                f"fixture expected {case.get('expected_state')} != derived {derived_state}"
            )
        results.append(
            {
                "case_id": case.get("case_id"),
                "derived_state": derived_state,
                "reasons": reasons,
                "errors": errors,
            }
        )
    return {
        "result": "PASS" if all(not item["errors"] for item in results) else "FAIL",
        "cases": results,
    }


def main() -> int:
    result = validate_fixture_file()
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["result"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
