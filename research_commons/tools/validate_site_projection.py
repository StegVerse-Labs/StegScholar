#!/usr/bin/env python3
"""Fail-closed validation for Research Commons Publisher-paper Site projection."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROJECTION = ROOT / "projection" / "site-publisher-papers-manifest.json"
REGISTRY = ROOT / "sources" / "publisher-papers" / "registry.json"
RECEIPT = ROOT / "sources" / "publisher-papers" / "registry-hash-receipt.json"


def fail(message: str) -> None:
    print(f"BLOCK: {message}")
    raise SystemExit(1)


def main() -> None:
    for path in (PROJECTION, REGISTRY, RECEIPT):
        if not path.exists():
            fail(f"missing required artifact: {path.relative_to(ROOT)}")

    projection = json.loads(PROJECTION.read_text(encoding="utf-8"))
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    receipt = json.loads(RECEIPT.read_text(encoding="utf-8"))

    registry_ids = {entry["publisher_id"] for entry in registry["entries"]}
    projected = projection.get("entries", projection.get("papers", []))
    projection_ids = {entry.get("publisher_id") for entry in projected}
    if None in projection_ids:
        fail("projection entry missing publisher_id")
    if not projection_ids.issubset(registry_ids):
        fail("projection includes record absent from canonical Commons registry")
    if receipt.get("registry_id") != registry.get("registry_id"):
        fail("registry hash receipt does not identify current registry")

    authorization = projection.get("projection_authorization", projection.get("authorization", "not_authorized"))
    if authorization not in ("not_authorized", False):
        required = [
            projection.get("publisher_validation_receipt"),
            projection.get("commons_validation_receipt"),
            projection.get("site_acceptance_receipt"),
        ]
        if not all(required):
            fail("projection claims authorization without all three boundary receipts")

    blocked_postures = {"source_record_reconciliation_required"}
    registry_by_id = {entry["publisher_id"]: entry for entry in registry["entries"]}
    for entry in projected:
        source = registry_by_id[entry["publisher_id"]]
        eligible = entry.get("eligible", entry.get("projection_eligible", False))
        if eligible and source["commons_posture"] in blocked_postures:
            fail(f"{entry['publisher_id']} is marked eligible while reconciliation is required")

    print("PASS: Site projection manifest is structurally admissible; no publication authority inferred")


if __name__ == "__main__":
    try:
        main()
    except (KeyError, TypeError, ValueError, json.JSONDecodeError) as exc:
        fail(f"invalid projection data: {exc}")
