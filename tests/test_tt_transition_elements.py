import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "validate_tt_transition_elements.py"
FIXTURE = ROOT / "fixtures" / "tt" / "transition-element-cases.json"


def load_validator():
    spec = importlib.util.spec_from_file_location("validate_tt_transition_elements", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_transition_element_fixture_contract():
    import json

    validator = load_validator()
    payload = json.loads(FIXTURE.read_text(encoding="utf-8"))
    ok, failures = validator.validate_fixture(payload)
    assert ok, failures


def test_not_observed_deny_is_valid_transition():
    validator = load_validator()
    element = {
        "schema_version": "0.1.0",
        "transition_id": "test-deny-unobserved",
        "existence_posture": "CONFIRMED",
        "pre_state_ref": "state://pre",
        "post_state_ref": "state://world/post",
        "preserved_projection_refs": ["projection://target"],
        "signature_evidence_refs": ["receipt://deny"],
        "observation_posture": "NOT_OBSERVED",
        "attribution_posture": "KNOWN",
        "governance_disposition": "DENY",
        "temporal_order_posture": "UNKNOWN",
        "unresolved_fields": ["temporal_order", "observer_attribution"],
    }
    assert validator.validate_element(element) == []


def test_unknown_existence_cannot_claim_deny():
    validator = load_validator()
    element = {
        "schema_version": "0.1.0",
        "transition_id": "test-unknown-overclaim",
        "existence_posture": "UNKNOWN",
        "preserved_projection_refs": [],
        "signature_evidence_refs": [],
        "observation_posture": "NOT_OBSERVED",
        "attribution_posture": "UNRESOLVED",
        "governance_disposition": "DENY",
        "temporal_order_posture": "UNKNOWN",
        "unresolved_fields": ["action", "cause", "temporal_order"],
    }
    errors = validator.validate_element(element)
    assert "UNKNOWN transition existence cannot assert a governance disposition" in errors
