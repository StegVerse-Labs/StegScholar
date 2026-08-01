#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "manifests" / "gtg-reconstruction-mirror-v1.json"


def fail(message: str) -> None:
    raise SystemExit(f"GTG RECONSTRUCTION MIRROR: FAIL - {message}")


def main() -> None:
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))

    if data.get("schema_version") != "STEGSCHOLAR-GTG-RECONSTRUCTION-MIRROR-v1":
        fail("schema version mismatch")

    ownership = data.get("canonical_ownership", {})
    if ownership.get("target_repository") != "Admissible-Existence/GTG":
        fail("canonical target repository mismatch")
    if ownership.get("independent_validation_repository") != "Admissible-Existence/ae-validation-factory":
        fail("factory repository mismatch")
    if ownership.get("stegverse_role") != "RESEARCH_AND_PUBLICATION_MIRROR_ONLY":
        fail("StegVerse role overstatement")

    levels = data.get("levels", {})
    r3 = levels.get("R3", {})
    r4 = levels.get("R4", {})
    r5 = levels.get("R5", {})

    if not r3.get("target_commit") or not r3.get("factory_commit"):
        fail("R3 must bind both target and factory commits")
    if r3.get("target_state") != "ACTIVE" or r3.get("factory_state") != "ACTIVE" or r3.get("mirror_state") != "ACTIVE":
        fail("R3 active posture mismatch")

    if not r4.get("target_commit"):
        fail("R4 target commit missing")
    if r4.get("target_state") != "ACTIVE":
        fail("R4 target must remain active")
    if r4.get("factory_commit") is not None or r4.get("factory_state") != "PENDING" or r4.get("mirror_state") != "PARTIAL":
        fail("R4 must remain partial until factory commit exists")

    if any(r5.get(field) is not None for field in ("target_commit", "factory_commit")):
        fail("R5 commit asserted before activation")
    if r5.get("target_state") != "NOT_TESTED" or r5.get("factory_state") != "NOT_TESTED" or r5.get("mirror_state") != "NOT_TESTED":
        fail("R5 posture overstatement")

    claims = data.get("claims", {})
    if not claims:
        fail("claims missing")
    for key, value in claims.items():
        if value is not False:
            fail(f"prohibited claim enabled: {key}")

    print("GTG RECONSTRUCTION MIRROR: PASS - R3 active, R4 partial, R5 not tested; all authority claims false")


if __name__ == "__main__":
    main()
