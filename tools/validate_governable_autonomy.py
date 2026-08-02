#!/usr/bin/env python3
"""Fail-closed validation for the StegScholar Governable Autonomy program."""

from __future__ import annotations

import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
PROGRAM = ROOT / "research-programs" / "governable-autonomy"

REQUIRED_FILES = [
    ROOT / "SECURITY_BASELINE.md",
    ROOT / "STEGSCHOLAR_GOVERNABLE_AUTONOMY_MIRROR_HANDOFF.md",
    PROGRAM / "README.md",
    PROGRAM / "ARTIFACT_MANIFEST.md",
    PROGRAM / "paper-registry.json",
    PROGRAM / "review-schema.json",
    PROGRAM / "task-claims.json",
]

ALLOWED_CLAIM_STATES = {
    "UNCLAIMED",
    "CLAIMED_FOR_IMPLEMENTATION",
    "CLAIMED_FOR_VALIDATION",
    "CLAIMED_FOR_INTEGRATION",
    "MACHINE_OWNED",
    "BLOCKED",
    "COMPLETE",
    "SUPERSEDED",
    "MERGED_INTO_CANONICAL_WORKSTREAM",
}

REQUIRED_PAPER_IDS = {f"GA-{n:03d}" for n in range(1, 7)}


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"invalid JSON at {path.relative_to(ROOT)}: {exc}") from exc


def parse_utc(value: str) -> datetime:
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None:
        raise ValueError(f"timestamp lacks timezone: {value}")
    return parsed.astimezone(timezone.utc)


def validate_required_files(errors: list[str]) -> None:
    for path in REQUIRED_FILES:
        if not path.is_file():
            errors.append(f"missing required file: {path.relative_to(ROOT)}")
        elif path.stat().st_size == 0:
            errors.append(f"empty required file: {path.relative_to(ROOT)}")


def validate_registry(errors: list[str]) -> None:
    registry = load_json(PROGRAM / "paper-registry.json")
    papers = registry.get("papers")
    if not isinstance(papers, list):
        errors.append("paper-registry.json: papers must be an array")
        return

    ids = [paper.get("paper_id") for paper in papers if isinstance(paper, dict)]
    if set(ids) != REQUIRED_PAPER_IDS:
        errors.append(f"paper registry IDs must equal {sorted(REQUIRED_PAPER_IDS)}; found {sorted(set(ids))}")
    if len(ids) != len(set(ids)):
        errors.append("paper registry contains duplicate paper IDs")

    allowed_status = set(registry.get("status_values", []))
    allowed_review = set(registry.get("review_state_values", []))
    for paper in papers:
        if not isinstance(paper, dict):
            errors.append("paper registry contains a non-object paper entry")
            continue
        for key in ("paper_id", "slug", "title", "version", "status", "review_state", "canonical_source", "claims_scope", "known_limitations"):
            if key not in paper:
                errors.append(f"{paper.get('paper_id', '<unknown>')}: missing {key}")
        if paper.get("status") not in allowed_status:
            errors.append(f"{paper.get('paper_id')}: invalid status {paper.get('status')}")
        if paper.get("review_state") not in allowed_review:
            errors.append(f"{paper.get('paper_id')}: invalid review_state {paper.get('review_state')}")
        source = paper.get("canonical_source")
        if isinstance(source, str) and not (ROOT / source).is_file():
            errors.append(f"{paper.get('paper_id')}: canonical source missing: {source}")
        if not paper.get("known_limitations"):
            errors.append(f"{paper.get('paper_id')}: known_limitations must not be empty")


def validate_review_schema(errors: list[str]) -> None:
    schema = load_json(PROGRAM / "review-schema.json")
    required = set(schema.get("required", []))
    expected = {"review_id", "paper_id", "paper_version", "review_type", "review_state", "scope", "findings", "evidence_refs", "created_at", "authority", "integrity"}
    missing = expected - required
    if missing:
        errors.append(f"review schema missing required fields: {sorted(missing)}")
    if schema.get("additionalProperties") is not False:
        errors.append("review schema must fail closed with additionalProperties=false")


def validate_claims(errors: list[str]) -> None:
    registry = load_json(PROGRAM / "task-claims.json")
    allowed = set(registry.get("allowed_states", []))
    if allowed != ALLOWED_CLAIM_STATES:
        errors.append("task-claims.json allowed_states do not match canonical state set")

    now = datetime.now(timezone.utc)
    seen_surfaces: dict[str, str] = {}
    active_states = {"CLAIMED_FOR_IMPLEMENTATION", "CLAIMED_FOR_VALIDATION", "CLAIMED_FOR_INTEGRATION", "MACHINE_OWNED"}
    for claim in registry.get("claims", []):
        task_id = claim.get("task_id", "<unknown>")
        state = claim.get("state")
        if state not in ALLOWED_CLAIM_STATES:
            errors.append(f"{task_id}: invalid state {state}")
        for key in ("originating_goal", "repository", "branch", "surfaces", "claimant", "role", "claim_created_at", "release_condition", "expected_evidence", "collision_boundaries"):
            if not claim.get(key):
                errors.append(f"{task_id}: missing or empty {key}")
        if state in active_states:
            expires = claim.get("claim_expires_at")
            if not expires:
                errors.append(f"{task_id}: active claim lacks claim_expires_at")
            else:
                try:
                    if parse_utc(expires) <= now:
                        errors.append(f"{task_id}: active claim expired at {expires}")
                except ValueError as exc:
                    errors.append(f"{task_id}: {exc}")
            for surface in claim.get("surfaces", []):
                previous = seen_surfaces.get(surface)
                if previous:
                    errors.append(f"claim collision: {surface} is active in both {previous} and {task_id}")
                seen_surfaces[surface] = task_id


def main() -> int:
    errors: list[str] = []
    try:
        validate_required_files(errors)
        if not errors:
            validate_registry(errors)
            validate_review_schema(errors)
            validate_claims(errors)
    except ValueError as exc:
        errors.append(str(exc))

    receipt = {
        "validator": "tools/validate_governable_autonomy.py",
        "result": "COMPLETE" if not errors else "FAILED",
        "checked_at": datetime.now(timezone.utc).isoformat(),
        "source_digest": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "errors": errors,
        "next_executable_task": "issue #7 deterministic BCAT execution-boundary model" if not errors else "correct validation failures",
    }
    print(json.dumps(receipt, indent=2, sort_keys=True))
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
