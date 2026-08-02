#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "coordination/gtg-r4-r5-subject-continuity-cases.json"
PROHIBITED = {
    "execution_authority",
    "certification_authority",
    "mathematical_closure",
    "independent_verification_complete",
    "release_ready",
    "archive_ready",
}


def classify(case):
    if case.get("contradiction") or case.get("alias_reassigned"):
        return "SUBJECT_CONTINUITY_FAIL_CLOSED"
    if not case.get("binding_present") or not case.get("binding_current"):
        return "SUBJECT_CONTINUITY_FAIL_CLOSED"
    if case.get("transition_subject") != case.get("authority_subject"):
        return "SUBJECT_CONTINUITY_FAIL_CLOSED"
    observed = case.get("observed_subject")
    authority = case.get("authority_subject")
    if observed != authority and not case.get("binding_present"):
        return "SUBJECT_CONTINUITY_FAIL_CLOSED"
    if not case.get("binding_provenance_complete"):
        return "SUBJECT_CONTINUITY_PARTIAL"
    return "SUBJECT_CONTINUITY_SURVIVES"


def main():
    payload = json.loads(DATA.read_text())
    errors = []
    for claim in PROHIBITED:
        if payload.get("claims", {}).get(claim) is not False:
            errors.append(f"claim must remain false: {claim}")
    cases = payload.get("cases", [])
    if len(cases) < 10:
        errors.append("at least ten cases required")
    for case in cases:
        observed = classify(case)
        if observed != case.get("expected"):
            errors.append(f"{case.get('case_id')}: expected {case.get('expected')}, observed {observed}")
    if errors:
        raise SystemExit("\n".join(errors))
    print(json.dumps({"validated_cases": len(cases), "result": "PASS"}, sort_keys=True))


if __name__ == "__main__":
    main()
