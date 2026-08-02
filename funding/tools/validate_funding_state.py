#!/usr/bin/env python3
"""Fail-closed validation for the StegScholar funding workstream."""

from __future__ import annotations

import json
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REQUIRED = [
    "funding/FUNDING_MIRROR_HANDOFF.md",
    "funding/coordination/funding-tasks.json",
    "funding/schemas/application.schema.json",
    "funding/applications/examples/FUNDING-EXAMPLE-001.json",
    "funding/tools/validate_funding_state.py",
    ".github/workflows/funding-state-validation.yml",
]
TERMINAL = {"COMPLETE", "SUPERSEDED", "MERGED_INTO_CANONICAL_WORKSTREAM"}
ACTIVE = {"CLAIMED_FOR_IMPLEMENTATION", "CLAIMED_FOR_VALIDATION", "CLAIMED_FOR_INTEGRATION"}


def fail(message: str) -> None:
    raise ValueError(message)


def load_json(path: Path) -> dict:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        fail(f"cannot parse {path.relative_to(ROOT)}: {exc}")
    if not isinstance(value, dict):
        fail(f"{path.relative_to(ROOT)} must contain a JSON object")
    return value


def validate_registry(registry: dict) -> None:
    allowed = set(registry.get("allowed_states", []))
    if not allowed:
        fail("registry allowed_states is empty")
    claims = registry.get("claims")
    tasks = registry.get("tasks")
    if not isinstance(claims, list) or not isinstance(tasks, list):
        fail("registry claims and tasks must be arrays")

    now = datetime.now().astimezone()
    surfaces: dict[str, str] = {}
    for claim in claims:
        state = claim.get("state")
        if state not in allowed:
            fail(f"claim {claim.get('task_id')} has invalid state {state}")
        if state in ACTIVE:
            expiry = datetime.fromisoformat(claim["expires_at"])
            if expiry < now:
                fail(f"claim {claim['task_id']} expired at {claim['expires_at']}")
            for surface in claim.get("surfaces", []):
                prior = surfaces.setdefault(surface, claim["task_id"])
                if prior != claim["task_id"]:
                    fail(f"surface collision: {surface} claimed by {prior} and {claim['task_id']}")
        for key in ("claimant", "role", "release_condition", "expected_evidence", "next_task_after_release"):
            if not claim.get(key):
                fail(f"claim {claim.get('task_id')} missing {key}")

    task_ids = set()
    for task in tasks:
        task_id = task.get("task_id")
        if not task_id or task_id in task_ids:
            fail(f"missing or duplicate task_id: {task_id}")
        task_ids.add(task_id)
        if task.get("state") not in allowed:
            fail(f"task {task_id} has invalid state {task.get('state')}")
        if task.get("state") not in TERMINAL:
            for key in ("owner", "location", "next_action", "evidence_location"):
                if not task.get(key):
                    fail(f"incomplete task {task_id} missing {key}")


def validate_application(app: dict) -> None:
    required = {
        "application_id", "opportunity", "applicant", "program", "state", "authority",
        "dates", "evidence_refs", "budget", "publication_classification", "next_action",
    }
    missing = sorted(required - set(app))
    if missing:
        fail(f"application missing fields: {', '.join(missing)}")
    if app["authority"] != {
        "application_owner": "StegVerse-Labs/StegScholar",
        "ip_authority": "StegVerse-Labs/StegPatents",
        "budget_authority": "StegVerse-Labs/StegFinCo",
        "deliverables_authority": "StegVerse-Labs/StegOps-Deliverables",
    }:
        fail("application authority boundary is invalid")
    if not app["evidence_refs"]:
        fail("application has no evidence references")
    for ref in app["evidence_refs"] + app["program"].get("research_paths", []):
        if not (ROOT / ref).is_file():
            fail(f"referenced evidence does not exist: {ref}")
    if not all(app["next_action"].get(k) for k in ("owner", "location", "action", "release_condition")):
        fail("application next_action is incomplete")


def main() -> int:
    missing = [path for path in REQUIRED if not (ROOT / path).is_file()]
    if missing:
        fail(f"missing required files: {', '.join(missing)}")
    registry = load_json(ROOT / "funding/coordination/funding-tasks.json")
    application = load_json(ROOT / "funding/applications/examples/FUNDING-EXAMPLE-001.json")
    load_json(ROOT / "funding/schemas/application.schema.json")
    validate_registry(registry)
    validate_application(application)
    receipt = {
        "result": "COMPLETE",
        "goal_id": registry["goal_id"],
        "validated_files": REQUIRED,
        "task_count": len(registry["tasks"]),
        "claim_count": len(registry["claims"]),
        "next_executable_task": next(
            (task["task_id"] for task in registry["tasks"] if task["state"] not in TERMINAL),
            None,
        ),
    }
    out = ROOT / "funding/evidence/latest-validation.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(receipt, indent=2))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"FAILED: {exc}", file=sys.stderr)
        raise SystemExit(1)
