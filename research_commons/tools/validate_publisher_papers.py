#!/usr/bin/env python3
"""Validate the Publisher paper projection in Research Commons.

This validator checks internal consistency only. It does not certify Publisher
content, scientific validity, publication status, or reuse admissibility.
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SOURCE_DIR = ROOT / "research_commons" / "sources" / "publisher-papers"


def load_json(name: str) -> dict:
    path = SOURCE_DIR / name
    if not path.is_file():
        raise SystemExit(f"missing required file: {path}")
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise SystemExit(f"invalid JSON in {path}: {exc}") from exc


def main() -> int:
    registry = load_json("registry.json")
    relations = load_json("relations.json")
    reconciliation = load_json("reconciliation.json")

    entries = registry.get("entries")
    if not isinstance(entries, list) or not entries:
        raise SystemExit("registry entries must be a non-empty list")

    publisher_ids: set[str] = set()
    commons_ids: set[str] = set()
    errors: list[str] = []

    for entry in entries:
        publisher_id = entry.get("publisher_id")
        commons_id = entry.get("commons_id")
        if not publisher_id or not commons_id:
            errors.append("every registry entry requires publisher_id and commons_id")
            continue
        if publisher_id in publisher_ids:
            errors.append(f"duplicate publisher_id: {publisher_id}")
        if commons_id in commons_ids:
            errors.append(f"duplicate commons_id: {commons_id}")
        publisher_ids.add(publisher_id)
        commons_ids.add(commons_id)

        page = SOURCE_DIR / f"{publisher_id}.md"
        if not page.is_file():
            errors.append(f"missing Commons page for {publisher_id}: {page.name}")
        if entry.get("reuse_requires_new_admissibility") is not True:
            errors.append(f"{publisher_id} must require new reuse admissibility")

    relation_rows = relations.get("relations", [])
    if not isinstance(relation_rows, list):
        errors.append("relations must be a list")
    else:
        for index, relation in enumerate(relation_rows):
            subject = relation.get("subject")
            if subject not in publisher_ids:
                errors.append(f"relation[{index}] has unknown subject: {subject}")
            if not relation.get("predicate") or not relation.get("object"):
                errors.append(f"relation[{index}] requires predicate and object")
            if not relation.get("posture"):
                errors.append(f"relation[{index}] requires posture")

    reconciliation_rows = reconciliation.get("records", [])
    reconciled_ids = {
        row.get("paper_id") for row in reconciliation_rows if isinstance(row, dict)
    }
    missing_reconciliation = publisher_ids - reconciled_ids
    extra_reconciliation = reconciled_ids - publisher_ids
    if missing_reconciliation:
        errors.append(
            "missing reconciliation rows: " + ", ".join(sorted(missing_reconciliation))
        )
    if extra_reconciliation:
        errors.append(
            "unknown reconciliation rows: " + ", ".join(sorted(extra_reconciliation))
        )

    expected_union = reconciliation.get("summary", {}).get("union_record_count")
    if expected_union != len(publisher_ids):
        errors.append(
            f"union_record_count={expected_union!r} does not match registry count={len(publisher_ids)}"
        )

    if errors:
        print("Research Commons Publisher-paper validation: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Research Commons Publisher-paper validation: PASS")
    print(f"entries={len(publisher_ids)}")
    print(f"relations={len(relation_rows)}")
    print("authority_boundary=internal consistency only")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
