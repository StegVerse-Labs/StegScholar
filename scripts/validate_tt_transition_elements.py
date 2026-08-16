#!/usr/bin/env python3
"""Validate TT minimal transition-element fixtures.

This validator intentionally checks bounded research invariants without claiming
that schema validity proves a physical transition, historical truth, authority,
or a unique thermodynamic signature.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_FIXTURE = ROOT / "fixtures" / "tt" / "transition-element-cases.json"

EXISTENCE = {"CONFIRMED", "INFERRED", "UNKNOWN"}
OBSERVATION = {"OBSERVED", "PARTIAL", "NOT_OBSERVED", "UNKNOWN"}
ATTRIBUTION = {"KNOWN", "BOUNDED", "UNRESOLVED"}
DISPOSITIONS = {"ALLOW", "DENY", "FAIL_CLOSED", "DEFER", "TRANSFORM", "ERROR", "UNKNOWN", None}
TEMPORAL = {"ORDERED", "PARTIAL_ORDER", "UNKNOWN"}

REQUIRED = {
    "schema_version",
    "transition_id",
    "existence_posture",
    "preserved_projection_refs",
    "signature_evidence_refs",
    "observation_posture",
    "attribution_posture",
    "unresolved_fields",
}


def validate_element(element: dict) -> list[str]:
    errors: list[str] = []

    missing = sorted(REQUIRED - element.keys())
    if missing:
        errors.append(f"missing required fields: {missing}")
        return errors

    if element["schema_version"] != "0.1.0":
        errors.append("schema_version must be 0.1.0")
    if not isinstance(element["transition_id"], str) or not element["transition_id"].strip():
        errors.append("transition_id must be a non-empty string")
    if element["existence_posture"] not in EXISTENCE:
        errors.append("invalid existence_posture")
    if element["observation_posture"] not in OBSERVATION:
        errors.append("invalid observation_posture")
    if element["attribution_posture"] not in ATTRIBUTION:
        errors.append("invalid attribution_posture")
    if element.get("governance_disposition") not in DISPOSITIONS:
        errors.append("invalid governance_disposition")
    if element.get("temporal_order_posture", "UNKNOWN") not in TEMPORAL:
        errors.append("invalid temporal_order_posture")

    for field in ("preserved_projection_refs", "signature_evidence_refs", "unresolved_fields"):
        if not isinstance(element[field], list):
            errors.append(f"{field} must be an array")

    # Unknown transition existence may not be silently converted into a known
    # governance outcome. This is the machine-readable form of the black/unknown
    # non-overclaim rule.
    if element["existence_posture"] == "UNKNOWN" and element.get("governance_disposition") not in {None, "UNKNOWN"}:
        errors.append("UNKNOWN transition existence cannot assert a governance disposition")

    # NOT_OBSERVED is explicitly permitted for DENY, FAIL_CLOSED, and realized
    # execution elsewhere in TT. Absence of observation is not absence of event.
    # Therefore no validator rule rejects those combinations.

    # If attribution is known and a concrete disposition is asserted, some
    # signature or receipt evidence must be present.
    if (
        element["attribution_posture"] == "KNOWN"
        and element.get("governance_disposition") not in {None, "UNKNOWN"}
        and not element["signature_evidence_refs"]
    ):
        errors.append("known attribution with concrete disposition requires signature evidence")

    # A black/inferred element may omit identity_signature, but if present it
    # must carry a signature_id. Distinct signature IDs are checked across the
    # fixture set below.
    sig = element.get("identity_signature")
    if sig is not None:
        if not isinstance(sig, dict) or not isinstance(sig.get("signature_id"), str) or not sig["signature_id"].strip():
            errors.append("identity_signature requires non-empty signature_id")

    return errors


def validate_fixture(payload: dict) -> tuple[bool, list[str]]:
    failures: list[str] = []
    seen_transition_ids: set[str] = set()
    seen_signature_ids: set[str] = set()

    cases = payload.get("cases")
    if not isinstance(cases, list):
        return False, ["fixture requires cases array"]

    for case in cases:
        name = case.get("name", "<unnamed>")
        expect_valid = case.get("expect_valid")
        element = case.get("element")
        if not isinstance(element, dict):
            failures.append(f"{name}: missing element object")
            continue

        errors = validate_element(element)
        actual_valid = not errors
        if actual_valid != expect_valid:
            failures.append(f"{name}: expected valid={expect_valid}, got valid={actual_valid}; errors={errors}")

        # Identity checks only apply to cases expected to be valid.
        if expect_valid and actual_valid:
            tid = element["transition_id"]
            if tid in seen_transition_ids:
                failures.append(f"{name}: duplicate transition_id {tid}")
            seen_transition_ids.add(tid)

            sig = element.get("identity_signature")
            if sig:
                sid = sig["signature_id"]
                if sid in seen_signature_ids:
                    failures.append(f"{name}: duplicate identity signature {sid}")
                seen_signature_ids.add(sid)

    return not failures, failures


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_FIXTURE
    payload = json.loads(path.read_text(encoding="utf-8"))
    ok, failures = validate_fixture(payload)
    if not ok:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1
    print(f"PASS: {len(payload['cases'])} TT transition-element cases")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
