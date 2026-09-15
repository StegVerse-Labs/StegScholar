from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "fixtures/architecture-neutral-admissibility/cases.json"

REQUIRED = ("evidence", "authority", "standing", "safety_constraints", "policy", "commit_time")
VALID = {"PASS", "FAIL", "UNRESOLVED"}


def classify(case: dict) -> str:
    checks = case["checks"]
    missing = [k for k in REQUIRED if k not in checks]
    if missing:
        raise AssertionError(f"missing checks: {missing}")
    bad = {k: v for k, v in checks.items() if k not in REQUIRED or v not in VALID}
    if bad:
        raise AssertionError(f"invalid checks: {bad}")

    failures = [k for k in REQUIRED if checks[k] == "FAIL"]
    unresolved = [k for k in REQUIRED if checks[k] == "UNRESOLVED"]

    if failures:
        return "SUBSTANTIVE_DENIAL_SUPPORTED"
    if unresolved:
        return "FAIL_CLOSED_REQUIRED"
    if case["denial_asserted"] and case["architecture_conformity_only"]:
        return "CONFORMITY_ONLY_DENIAL_INVALID"
    return "SUBSTANTIVE_REQUIREMENTS_SATISFIED"


def validate() -> None:
    data = json.loads(FIXTURES.read_text())
    seen = set()
    required_cases = {
        "incumbent-all-pass",
        "novel-different-evidence-path-all-pass",
        "conformity-only-denial",
        "evidence-failure",
        "authority-failure",
        "standing-failure",
        "safety-constraint-failure",
        "policy-failure",
        "commit-time-failure",
        "unresolved-required-state",
    }
    for case in data["cases"]:
        cid = case["case_id"]
        if cid in seen:
            raise AssertionError(f"duplicate case_id: {cid}")
        seen.add(cid)
        actual = classify(case)
        expected = case["expected_state"]
        if actual != expected:
            raise AssertionError(f"{cid}: expected {expected}, got {actual}")

    if seen != required_cases:
        raise AssertionError(f"case-set mismatch: missing={required_cases-seen}, extra={seen-required_cases}")

    conformity = next(c for c in data["cases"] if c["case_id"] == "conformity-only-denial")
    assert conformity["different_from_incumbent"] is True
    assert all(v == "PASS" for v in conformity["checks"].values())
    assert classify(conformity) == "CONFORMITY_ONLY_DENIAL_INVALID"

    novel = next(c for c in data["cases"] if c["case_id"] == "novel-different-evidence-path-all-pass")
    incumbent = next(c for c in data["cases"] if c["case_id"] == "incumbent-all-pass")
    assert classify(novel) == classify(incumbent) == "SUBSTANTIVE_REQUIREMENTS_SATISFIED"

    for cid in ("evidence-failure", "authority-failure", "standing-failure", "safety-constraint-failure", "policy-failure", "commit-time-failure"):
        case = next(c for c in data["cases"] if c["case_id"] == cid)
        assert classify(case) == "SUBSTANTIVE_DENIAL_SUPPORTED"

    unresolved = next(c for c in data["cases"] if c["case_id"] == "unresolved-required-state")
    assert classify(unresolved) == "FAIL_CLOSED_REQUIRED"


if __name__ == "__main__":
    validate()
    print("architecture-neutral admissibility validation: PASS")
