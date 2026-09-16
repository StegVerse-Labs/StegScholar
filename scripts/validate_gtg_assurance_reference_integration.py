from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "fixtures/gtg-assurance-reference-integration/cases.json"
GTG_DECISION_SCHEMA = ROOT / "schemas/gtg-decision.schema.json"
GTG_RECORD_SCHEMA = ROOT / "schemas/gtg-governance-record.schema.json"
GTG_ASSURANCE_SCHEMA = ROOT / "schemas/gtg-governance-assurance.schema.json"
TT_SCHEMA = ROOT / "schemas/tt-transition-cell.schema.json"
GATE_SCHEMA = ROOT / "schemas/gate-legitimacy-record.schema.json"
REVIEW_SCHEMA = ROOT / "schemas/independent-review-record.schema.json"
ARCH_SCHEMA = ROOT / "schemas/architecture-neutral-admissibility-record.schema.json"

SLOT_TYPES = {
    "gate_legitimacy": "GATE_LEGITIMACY",
    "independent_review": "INDEPENDENT_REVIEW",
    "architecture_neutral_admissibility": "ARCHITECTURE_NEUTRAL_ADMISSIBILITY",
}
VALID_TYPES = set(SLOT_TYPES.values())


def _load(path: Path) -> dict:
    return json.loads(path.read_text())


def _reject_authority_promotion(record: dict, binding: dict) -> bool:
    return record.get("authority_effect") != "NONE" or binding.get("authority_effect") != "NONE"


def _correlation_matches(gtg: dict, binding: dict, record: dict) -> bool:
    corr = binding.get("correlation", {})
    candidate = corr.get("candidate_transition_id")
    if candidate is not None and candidate != gtg["candidate_transition_id"]:
        return False

    assurance_type = binding["assurance_type"]
    if assurance_type == "GATE_LEGITIMACY":
        if corr.get("gate_id") is not None and corr["gate_id"] != record.get("gate_id"):
            return False
        record_candidate = record.get("candidate_ref")
        if record_candidate is not None and record_candidate != gtg["candidate_transition_id"]:
            return False
        return True

    if assurance_type == "INDEPENDENT_REVIEW":
        if corr.get("gate_id") is not None and corr["gate_id"] != record.get("challenged_gate_ref"):
            return False
        if corr.get("rule_ref") is not None and corr["rule_ref"] != record.get("challenged_rule_ref"):
            return False
        if corr.get("evaluator_ref") is not None and corr["evaluator_ref"] != record.get("original_evaluator_ref"):
            return False
        return True

    if assurance_type == "ARCHITECTURE_NEUTRAL_ADMISSIBILITY":
        return record.get("candidate_ref") == gtg["candidate_transition_id"]

    return False


def evaluate_gtg(gtg: dict, records: dict[str, dict]) -> str:
    assurance = gtg.get("governance_assurance")
    if assurance is None:
        return "VALID"

    if assurance.get("authority_effect") != "NONE":
        return "INVALID_BINDING"

    required_types = assurance.get("required_types")
    bindings = assurance.get("bindings")
    if not isinstance(required_types, list) or len(required_types) != len(set(required_types)):
        return "INVALID_BINDING"
    if any(t not in VALID_TYPES for t in required_types):
        return "INVALID_BINDING"
    if not isinstance(bindings, dict):
        return "INVALID_BINDING"

    bound_by_type: dict[str, dict] = {}
    for slot, binding in bindings.items():
        expected_type = SLOT_TYPES.get(slot)
        if expected_type is None or not isinstance(binding, dict):
            return "INVALID_BINDING"
        if binding.get("assurance_type") != expected_type:
            return "INVALID_BINDING"
        if binding.get("authority_effect") != "NONE":
            return "INVALID_BINDING"
        if expected_type in bound_by_type:
            return "INVALID_BINDING"
        bound_by_type[expected_type] = binding

        applicability = binding.get("applicability")
        validation_state = binding.get("validation_state")
        record_ref = binding.get("record_ref")

        if applicability == "NOT_APPLICABLE":
            if record_ref is not None or validation_state != "NOT_APPLICABLE":
                return "INVALID_BINDING"
            continue

        if applicability not in {"REQUIRED", "OPTIONAL"}:
            return "INVALID_BINDING"

        if validation_state == "UNRESOLVED":
            if expected_type in required_types:
                return "FAIL_CLOSED_REQUIRED"
            continue
        if validation_state != "VALID":
            return "INVALID_BINDING"
        if not record_ref or record_ref not in records:
            return "INVALID_BINDING"

        record = records[record_ref]
        if record.get("record_type") != expected_type:
            return "INVALID_BINDING"
        if _reject_authority_promotion(record, binding):
            return "INVALID_BINDING"
        if not _correlation_matches(gtg, binding, record):
            return "INVALID_BINDING"

    for required_type in required_types:
        binding = bound_by_type.get(required_type)
        if binding is None:
            return "FAIL_CLOSED_REQUIRED"
        if binding.get("applicability") != "REQUIRED":
            return "FAIL_CLOSED_REQUIRED"
        if binding.get("validation_state") == "UNRESOLVED":
            return "FAIL_CLOSED_REQUIRED"
        if binding.get("validation_state") != "VALID":
            return "INVALID_BINDING"

    return "VALID"


def validate_schema_boundaries() -> None:
    decision = _load(GTG_DECISION_SCHEMA)
    governance = _load(GTG_RECORD_SCHEMA)
    assurance = _load(GTG_ASSURANCE_SCHEMA)
    tt = _load(TT_SCHEMA)

    for schema in (decision, governance):
        assert "governance_assurance" in schema["properties"]
        assert schema["properties"]["governance_assurance"]["$ref"] == "gtg-governance-assurance.schema.json"
        assert "governance_assurance" not in schema["required"], "historical records must remain valid"

    assert assurance["properties"]["authority_effect"] == {"const": "NONE"}
    assert set(assurance["properties"]["required_types"]["items"]["enum"]) == VALID_TYPES
    assert set(assurance["properties"]["bindings"]["properties"]) == set(SLOT_TYPES)

    assert "gtg_record_ref" in tt["required"]
    assert "governance_assurance" not in tt["properties"], "TT must not duplicate GTG assurance state"

    for source_schema in (GATE_SCHEMA, REVIEW_SCHEMA, ARCH_SCHEMA):
        source = _load(source_schema)
        assert source["properties"]["authority_effect"] == {"const": "NONE"}


def validate() -> None:
    validate_schema_boundaries()
    data = _load(FIXTURES)
    records = data["assurance_records"]

    expected_case_ids = {
        "historical-no-assurance",
        "all-three-required-valid",
        "gate-candidate-mismatch",
        "independent-review-gate-mismatch",
        "architecture-candidate-mismatch",
        "authority-effect-promotion-rejected",
        "required-unresolved-fails-closed",
        "optional-not-applicable-is-neutral",
        "architecture-neutrality-does-not-force-allow",
    }
    cases = {case["case_id"]: case for case in data["cases"]}
    if set(cases) != expected_case_ids:
        raise AssertionError(f"case-set mismatch: expected={expected_case_ids}, actual={set(cases)}")

    gtg_by_record_id: dict[str, dict] = {}
    result_by_case_id: dict[str, str] = {}
    for case_id, case in cases.items():
        gtg = case["gtg"]
        result = evaluate_gtg(gtg, records)
        result_by_case_id[case_id] = result
        gtg_by_record_id[gtg["record_id"]] = gtg
        if result != case["expected"]:
            raise AssertionError(f"{case_id}: expected {case['expected']}, got {result}")

    assert result_by_case_id["historical-no-assurance"] == "VALID"
    assert result_by_case_id["required-unresolved-fails-closed"] == "FAIL_CLOSED_REQUIRED"
    assert result_by_case_id["optional-not-applicable-is-neutral"] == "VALID"
    assert cases["architecture-neutrality-does-not-force-allow"]["gtg"]["disposition"] == "DENY"
    assert result_by_case_id["architecture-neutrality-does-not-force-allow"] == "VALID"

    expected_tt_ids = {
        "tt-reconstructs-valid-assurance-through-gtg-ref",
        "tt-cannot-hide-invalid-gtg-assurance",
        "tt-historical-gtg-remains-reconstructable",
    }
    tt_cases = {case["case_id"]: case for case in data["tt_cases"]}
    if set(tt_cases) != expected_tt_ids:
        raise AssertionError(f"TT case-set mismatch: expected={expected_tt_ids}, actual={set(tt_cases)}")

    for case_id, case in tt_cases.items():
        gtg_ref = case["tt"]["gtg_record_ref"]
        if gtg_ref not in gtg_by_record_id:
            raise AssertionError(f"{case_id}: missing GTG record {gtg_ref}")
        gtg_case_id = case["expected_gtg_case_id"]
        result = evaluate_gtg(gtg_by_record_id[gtg_ref], records)
        if result != result_by_case_id[gtg_case_id] or result != case["expected"]:
            raise AssertionError(f"{case_id}: GTG reconstruction mismatch")
        if "governance_assurance" in case["tt"]:
            raise AssertionError(f"{case_id}: TT duplicated governance assurance")


if __name__ == "__main__":
    validate()
    print("GTG assurance reference integration validation: PASS")
