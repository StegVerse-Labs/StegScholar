#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CASES = ROOT / "coordination" / "gtg-r4-challenge-cases.json"
DOC = ROOT / "papers" / "generalized-transition-governance" / "reconstruction" / "r4-challenge-corpus.md"

ALLOWED = {"CHALLENGE_SURVIVES", "CHALLENGE_PARTIAL", "CHALLENGE_FAIL_CLOSED"}


def fail(message: str) -> None:
    raise SystemExit(f"STEGVERSE GTG R4 CHALLENGES: FAIL - {message}")


def main() -> None:
    if not DOC.exists():
        fail("challenge corpus missing")
    data = json.loads(CASES.read_text(encoding="utf-8"))
    cases = data.get("cases", [])
    if len(cases) != 10:
        fail("expected exactly ten challenge cases")
    ids = {case.get("id") for case in cases}
    if len(ids) != 10 or None in ids:
        fail("case IDs missing or duplicated")
    for case in cases:
        if case.get("expected") not in ALLOWED:
            fail(f"invalid outcome in {case.get('id')}")
    by_condition = {case["condition"]: case["expected"] for case in cases}
    if by_condition.get("current_scope_matched") != "CHALLENGE_SURVIVES":
        fail("positive control mismatch")
    for condition in ("expired_delegation", "revoked_delegation", "conflicting_authority_sources", "scope_mismatch", "subject_mismatch", "consent_without_authority", "standing_without_delegation", "prior_approval_after_change"):
        if by_condition.get(condition) != "CHALLENGE_FAIL_CLOSED":
            fail(f"{condition} must fail closed")
    if by_condition.get("missing_revocation_history") != "CHALLENGE_PARTIAL":
        fail("missing revocation history must remain partial")
    for key, value in data.get("claims", {}).items():
        if value is not False:
            fail(f"prohibited claim enabled: {key}")
    print("STEGVERSE GTG R4 CHALLENGES: PASS - ten bounded cases validated; no authority claim created")


if __name__ == "__main__":
    main()
