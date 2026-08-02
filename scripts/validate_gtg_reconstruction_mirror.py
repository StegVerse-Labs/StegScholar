#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "manifests" / "gtg-reconstruction-mirror-v1.json"


def fail(message: str) -> None:
    raise SystemExit(f"GTG RECONSTRUCTION MIRROR: FAIL - {message}")


def require_active_evidence(level: dict, prefix: str) -> None:
    if level.get("target_state") != "ACTIVE" or level.get("factory_state") != "ACTIVE" or level.get("mirror_state") != "ACTIVE":
        fail(f"{prefix} active posture mismatch")
    for key in ("target_commit", "factory_commit"):
        if not level.get(key):
            fail(f"{prefix} {key} missing")
    for key in ("target_workflow_run", "target_artifact_id", "factory_workflow_run", "factory_artifact_id"):
        if not isinstance(level.get(key), int):
            fail(f"{prefix} {key} missing")
    for key in ("target_artifact_digest", "factory_artifact_digest"):
        value = level.get(key)
        if not isinstance(value, str) or not value.startswith("sha256:"):
            fail(f"{prefix} {key} missing")


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

    r3, r4, r5 = (data.get("levels", {}).get(key, {}) for key in ("R3", "R4", "R5"))
    if not r3.get("target_commit") or not r3.get("factory_commit") or any(r3.get(k) != "ACTIVE" for k in ("target_state", "factory_state", "mirror_state")):
        fail("R3 active posture mismatch")

    if not r4.get("target_commit") or r4.get("target_state") != "ACTIVE":
        fail("R4 target posture mismatch")
    if r4.get("factory_commit") is None:
        if r4.get("factory_state") != "PENDING" or r4.get("mirror_state") != "PARTIAL":
            fail("R4 pending posture mismatch")
    elif r4.get("factory_state") != "ACTIVE" or r4.get("mirror_state") != "ACTIVE":
        fail("R4 active posture mismatch")

    if not r5.get("stegverse_commit") or r5.get("stegverse_state") != "ACTIVE_INTERNAL_VALIDATION":
        fail("StegVerse R5 research binding missing")
    if r5.get("target_commit") is None and r5.get("factory_commit") is None:
        if r5.get("target_state") != "NOT_TESTED" or r5.get("factory_state") != "NOT_TESTED" or r5.get("mirror_state") != "ACTIVE_BOUNDED_RESEARCH":
            fail("R5 pre-canonical posture mismatch")
    else:
        require_active_evidence(r5, "R5")

    claims = data.get("claims", {})
    if not claims or any(value is not False for value in claims.values()):
        fail("prohibited claim enabled or claims missing")

    print("GTG RECONSTRUCTION MIRROR: PASS - R3/R4 active; R5 evidence-consistent; StegVerse remains a bounded mirror; all authority claims false")


if __name__ == "__main__":
    main()
