#!/usr/bin/env python3
"""Build a hash-bound Research Commons Site dispatch packet.

The builder is fail-closed: unresolved projection blockers produce a BLOCKED packet.
It never asserts Site acceptance or activation.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "research_commons/sources/publisher-papers/registry.json"
MANIFEST = ROOT / "research_commons/projection/site-publisher-papers-manifest.json"
OBSERVATION = ROOT / "research_commons/sources/publisher-papers/source-observation.json"
OUTPUT = ROOT / "research_commons/projection/site-projection-dispatch-packet.json"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    registry = json.loads(REGISTRY.read_text())
    manifest = json.loads(MANIFEST.read_text())
    blockers = []
    if manifest.get("activation_status") != "authorized":
        blockers.append("projection_manifest_not_authorized")
    for entry in manifest.get("entries", []):
        if str(entry.get("public_eligibility", "")).startswith("blocked_"):
            blockers.append(f"{entry.get('publisher_id')}: {entry.get('public_eligibility')}")

    packet = {
        "packet_id": "RC-SITE-DISPATCH-2026-08-02-001",
        "source_repository": "StegVerse-Labs/StegScholar",
        "source_commit": "0000000000000000000000000000000000000000",
        "publisher_observation_ref": str(OBSERVATION.relative_to(ROOT)),
        "registry_ref": str(REGISTRY.relative_to(ROOT)),
        "registry_sha256": sha256(REGISTRY),
        "projection_manifest_ref": str(MANIFEST.relative_to(ROOT)),
        "projection_manifest_sha256": sha256(MANIFEST),
        "entries": [
            {
                "publisher_id": entry["publisher_id"],
                "commons_page": entry["commons_page"],
                "eligibility": entry["public_eligibility"],
                "disclaimer": entry["display_disclaimer"],
            }
            for entry in manifest.get("entries", [])
        ],
        "dispatch_state": "BLOCKED" if blockers else "READY_FOR_SITE_REVIEW",
        "blockers": blockers,
        "authority_effect": "NONE",
    }
    OUTPUT.write_text(json.dumps(packet, indent=2) + "\n")
    print(json.dumps(packet, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
