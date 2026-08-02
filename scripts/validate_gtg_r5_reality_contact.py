#!/usr/bin/env python3
from __future__ import annotations

import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CASES = ROOT / "fixtures" / "gtg" / "reconstruction" / "r5" / "cases.json"
EXTERNAL_CLASSES = {
    "PROVIDER_RECEIPT",
    "CUSTODY_RECEIPT",
    "HUMAN_OBSERVATION",
    "PHYSICAL_MEASUREMENT",
    "EXTERNAL_STATE_ATTESTATION",
}


def classify(case: dict) -> str:
    if case.get("authority_effect") or case.get("execution_authorized"):
        return "R5_FAIL_CLOSED"
    evidence = case.get("evidence", [])
    if not evidence:
        return "R5_NOT_TESTED"
    if case.get("required_external_contact") and not any(item.get("class") in EXTERNAL_CLASSES for item in evidence):
        return "R5_FAIL_CLOSED"
    if any(item.get("contradicted") for item in evidence):
        return "R5_FAIL_CLOSED"
    if any(not item.get("fresh") or not item.get("subject_match") or not item.get("integrity_bound") for item in evidence):
        return "R5_FAIL_CLOSED"
    if any(item.get("class") == "PROVIDER_RECEIPT" and not item.get("effect_proven") for item in evidence):
        return "R5_FAIL_CLOSED"
    if any(not item.get("custody_complete") for item in evidence):
        return "R5_PARTIAL"
    if all(item.get("effect_proven") for item in evidence):
        return "R5_PASS"
    return "R5_PARTIAL"


def fail(message: str) -> None:
    raise SystemExit(f"STEGVERSE GTG R5: FAIL - {message}")


def validate(payload: dict) -> None:
    seen = set()
    for case in payload.get("cases", []):
        case_id = case.get("case_id")
        if not case_id or case_id in seen:
            fail(f"invalid or duplicate case id: {case_id}")
        seen.add(case_id)
        observed = classify(case)
        if observed != case.get("expected"):
            fail(f"{case_id}: expected {case.get('expected')} observed {observed}")
    if len(seen) < 10:
        fail("required fixture coverage missing")


def main() -> None:
    payload = json.loads(CASES.read_text(encoding="utf-8"))
    validate(payload)

    escalated = copy.deepcopy(payload)
    escalated["cases"][0]["authority_effect"] = True
    if classify(escalated["cases"][0]) != "R5_FAIL_CLOSED":
        fail("authority escalation was not rejected")

    internal_only = copy.deepcopy(payload["cases"][0])
    internal_only["evidence"][0]["class"] = "INTERNAL_SIMULATION"
    if classify(internal_only) != "R5_FAIL_CLOSED":
        fail("internal-only evidence was promoted")

    print("STEGVERSE GTG R5: PASS - taxonomy and ten bounded fixtures validated; no R5 completion or authority claim created")


if __name__ == "__main__":
    main()
