#!/usr/bin/env python3
"""Detect exact and normalized-title duplicate Research Commons entries.

This is a discovery control only. It does not determine scientific equivalence.
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "research_commons/sources/publisher-papers/registry.json"
OUTPUT = ROOT / "research_commons/reports/duplicate-detection.json"


def normalize_title(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", value.lower()).strip()


def canonical_hash(entry: dict) -> str:
    material = {
        "title": entry.get("title"),
        "subtitle": entry.get("subtitle"),
        "date": entry.get("date"),
        "version": entry.get("version"),
        "source_path": entry.get("source_path"),
    }
    encoded = json.dumps(material, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


def main() -> int:
    data = json.loads(REGISTRY.read_text())
    entries = data.get("entries", [])
    title_groups: dict[str, list[str]] = {}
    hash_groups: dict[str, list[str]] = {}
    for entry in entries:
        pid = entry["publisher_id"]
        title_groups.setdefault(normalize_title(entry.get("title", "")), []).append(pid)
        hash_groups.setdefault(canonical_hash(entry), []).append(pid)

    normalized_title_duplicates = [v for k, v in title_groups.items() if k and len(v) > 1]
    exact_record_duplicates = [v for v in hash_groups.values() if len(v) > 1]
    result = {
        "detector": "research_commons/tools/detect_duplicates.py",
        "registry": str(REGISTRY.relative_to(ROOT)),
        "entry_count": len(entries),
        "state": "REVIEW_REQUIRED" if normalized_title_duplicates or exact_record_duplicates else "COMPLETE",
        "exact_record_duplicates": exact_record_duplicates,
        "normalized_title_duplicates": normalized_title_duplicates,
        "authority_effect": "NONE",
        "note": "Duplicate detection does not determine scientific equivalence or admissibility."
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    return 1 if exact_record_duplicates else 0


if __name__ == "__main__":
    sys.exit(main())
