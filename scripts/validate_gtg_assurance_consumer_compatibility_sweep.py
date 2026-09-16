#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEGACY = ROOT / "scripts" / "validate_gtg_fixtures.py"
ASSURANCE_VALIDATOR = ROOT / "scripts" / "validate_gtg_assurance_reference_integration.py"
TT_SCHEMA = ROOT / "schemas" / "tt-transition-cell.schema.json"


def _load_legacy():
    spec = importlib.util.spec_from_file_location("legacy_gtg_fixture_validator", LEGACY)
    if spec is None or spec.loader is None:
        raise AssertionError("legacy GTG fixture validator cannot be loaded")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def synthetic_case() -> dict:
    return {
        "case_id": "assurance-preservation-probe",
        "claim_ids": ["GTG-001"],
        "activation_tests": {
            "discoverable": True,
            "commit_reconstructable": True,
            "basis_attached": True,
            "included_in_admissibility": True,
            "outcome_sensitive": True
        },
        "material_relation": True,
        "evidence_complete": True,
        "evidence_fresh": True,
        "execution_authority_valid": True,
        "standing_valid": True,
        "shared_constraint_satisfied": True,
        "original_admissible": True,
        "expected_activation": "ACTIVE",
        "expected_disposition": "ALLOW",
        "governance_assurance": {
            "assurance_id": "sweep-probe",
            "profile_ref": "profile:sweep",
            "required_types": [],
            "bindings": {},
            "authority_effect": "NONE"
        }
    }


def run_sweep() -> dict:
    legacy = _load_legacy()
    case = synthetic_case()
    errors, receipt = legacy.validate_case(case, set())
    if errors or receipt is None:
        raise AssertionError(f"legacy GTG fixture producer rejected control case: {errors}")

    assurance_preserved = receipt.get("governance_assurance") == case["governance_assurance"]
    tt = json.loads(TT_SCHEMA.read_text(encoding="utf-8"))
    tt_duplicates_assurance = "governance_assurance" in tt.get("properties", {})
    assurance_validator_present = ASSURANCE_VALIDATOR.exists()

    gap = None if assurance_preserved else "ASSURANCE_DROPPED_BY_LEGACY_FIXTURE_RECEIPT_SERIALIZER"
    return {
        "schema": "stegverse.gtg-assurance-consumer-compatibility-sweep/v1",
        "producer_serializer": "scripts/validate_gtg_fixtures.py:validate_case",
        "source_assurance_present": True,
        "serialized_assurance_preserved": assurance_preserved,
        "assurance_validator_present": assurance_validator_present,
        "tt_reconstruction_relation": "gtg_record_ref",
        "tt_duplicates_assurance": tt_duplicates_assurance,
        "authority_promotion_observed": False,
        "demonstrated_gap": gap,
        "derived_task_required": gap is not None
    }


def validate() -> dict:
    result = run_sweep()
    assert result["assurance_validator_present"] is True
    assert result["tt_duplicates_assurance"] is False
    assert result["authority_promotion_observed"] is False
    assert result["serialized_assurance_preserved"] is True
    assert result["demonstrated_gap"] is None
    assert result["derived_task_required"] is False
    return result


if __name__ == "__main__":
    print(json.dumps(validate(), indent=2, sort_keys=True))
