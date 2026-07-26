#!/usr/bin/env python3
"""Build deterministic Research Commons indexes from the Publisher paper registry."""
from __future__ import annotations

import hashlib
import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "sources" / "publisher-papers" / "registry.json"
INDEX_DIR = ROOT / "indexes" / "publisher-papers"
RECEIPT = ROOT / "sources" / "publisher-papers" / "registry-hash-receipt.json"


def canonical_bytes(value: object) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> None:
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    entries = registry["entries"]

    categories: dict[str, list[dict[str, str]]] = defaultdict(list)
    statuses: dict[str, list[dict[str, str]]] = defaultdict(list)
    postures: dict[str, list[dict[str, str]]] = defaultdict(list)

    for entry in entries:
        item = {
            "commons_id": entry["commons_id"],
            "publisher_id": entry["publisher_id"],
            "title": entry["title"],
            "page": f"../../sources/publisher-papers/{entry['publisher_id']}.md",
        }
        categories[entry["category"]].append(item)
        statuses[entry["publisher_status"]].append(item)
        postures[entry["commons_posture"]].append(item)

    write_json(INDEX_DIR / "categories.json", {"index_type": "category", "entries": categories})
    write_json(INDEX_DIR / "publisher-statuses.json", {"index_type": "publisher_status", "entries": statuses})
    write_json(INDEX_DIR / "knowledge-postures.json", {"index_type": "commons_posture", "entries": postures})

    digest = hashlib.sha256(canonical_bytes(registry)).hexdigest()
    write_json(
        RECEIPT,
        {
            "receipt_type": "research_commons_registry_hash",
            "registry_id": registry["registry_id"],
            "canonicalization": "RFC8785-like sorted compact JSON; UTF-8",
            "algorithm": "sha256",
            "digest": digest,
            "entry_count": len(entries),
            "creates_publication_authority": False,
            "creates_reuse_authority": False,
        },
    )
    print(f"built indexes and registry receipt: sha256:{digest}")


if __name__ == "__main__":
    main()
