#!/usr/bin/env python3
"""Fail closed when Publisher source identities drift from the pinned observation.

This checker does not fetch GitHub. It compares caller-supplied source identities with
Research Commons' pinned observation receipt so CI or an orchestrator can decide
whether a fresh ingestion/reconciliation run is required.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def load_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise SystemExit(f"cannot read {path}: {exc}") from exc


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--observation",
        default="research_commons/sources/publisher-papers/source-observation.json",
    )
    parser.add_argument("--source-ref", required=True)
    parser.add_argument("--papers-json-sha", required=True)
    parser.add_argument("--manifest-sha", required=True)
    args = parser.parse_args()

    observation = load_json(Path(args.observation))
    observed = {item["path"]: item["blob_sha"] for item in observation["observed_files"]}

    mismatches: list[str] = []
    if args.source_ref != observation["source_ref"]:
        mismatches.append(
            f"source_ref changed: pinned={observation['source_ref']} current={args.source_ref}"
        )
    if args.papers_json_sha != observed.get("papers.json"):
        mismatches.append(
            f"papers.json changed: pinned={observed.get('papers.json')} current={args.papers_json_sha}"
        )
    if args.manifest_sha != observed.get("papers_manifest.yml"):
        mismatches.append(
            "papers_manifest.yml changed: "
            f"pinned={observed.get('papers_manifest.yml')} current={args.manifest_sha}"
        )

    result = {
        "ok": not mismatches,
        "decision": "NO_DRIFT" if not mismatches else "REFRESH_REQUIRED",
        "mismatches": mismatches,
        "grants_sync_authority": False,
        "grants_publication_authority": False,
    }
    print(json.dumps(result, indent=2))
    return 0 if not mismatches else 2


if __name__ == "__main__":
    sys.exit(main())
