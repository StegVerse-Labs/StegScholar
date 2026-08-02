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

    if not r4.get("target_commit") or r4.get("target_state") != "ACTIVE":
        fail("R4 target posture mismatch")
    if r4.get("factory_commit") is None:
        if r4.get("factory_state") != "PENDING" or r4.get("mirror_state") != "PARTIAL":
            fail("R4 without factory commit must remain pending and partial")
    else:
        if r4.get("factory_state") != "ACTIVE" or r4.get("mirror_state") != "ACTIVE":
            fail("R4 with factory commit must be active")
        if not isinstance(r4.get("factory_workflow_run"), int):
            fail("active R4 factory workflow run missing")
        if not isinstance(r4.get("factory_artifact_id"), int):
            fail("active R4 factory artifact ID missing")
        digest = r4.get("factory_artifact_digest")
        if not isinstance(digest, str) or not digest.startswith("sha256:"):
            fail("active R4 factory artifact digest missing")

    if r5.get("target_commit") is not None or r5.get("factory_commit") is not None:
        fail("canonical or factory R5 commit asserted before activation")
    if r5.get("target_state") != "NOT_TESTED" or r5.get("factory_state") != "NOT_TESTED":
        fail("canonical R5 posture overstatement")
    if not r5.get("stegverse_commit"):
        fail("StegVerse R5 validation commit missing")
    if r5.get("stegverse_state") != "ACTIVE_INTERNAL_VALIDATION":
        fail("StegVerse R5 internal state mismatch")
    if r5.get("mirror_state") != "ACTIVE_BOUNDED_RESEARCH":
        fail("StegVerse R5 mirror state mismatch")

    claims = data.get("claims", {})
    if not claims:
        fail("claims missing")
    for key, value in claims.items():
        if value is not False:
            fail(f"prohibited claim enabled: {key}")

    print("GTG RECONSTRUCTION MIRROR: PASS - R3 active; R4 evidence-consistent; StegVerse R5 bounded research active; canonical and independent R5 not tested; all authority claims false")


if __name__ == "__main__":
    main()
