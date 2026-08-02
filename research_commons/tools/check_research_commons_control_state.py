#!/usr/bin/env python3
"""Validate the canonical Research Commons handoff and task/claim registry."""

from __future__ import annotations

import json
from datetime import datetime, timezone, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HANDOFF = ROOT / "RESEARCH_COMMONS_MIRROR_HANDOFF.md"
REGISTRY = ROOT / "research_commons/control/task-registry.json"
ALLOWED = {
    "UNCLAIMED",
    "CLAIMED_FOR_IMPLEMENTATION",
    "CLAIMED_FOR_VALIDATION",
    "CLAIMED_FOR_INTEGRATION",
    "MACHINE_OWNED",
    "BLOCKED",
    "COMPLETE",
    "SUPERSEDED",
    "MERGED_INTO_CANONICAL_WORKSTREAM",
    "RELEASED",
}


def parse_time(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def fail(message: str) -> None:
    raise SystemExit(f"CONTROL_STATE_INVALID: {message}")


def main() -> None:
    if not HANDOFF.exists():
        fail(f"missing handoff: {HANDOFF.relative_to(ROOT)}")
    if not REGISTRY.exists():
        fail(f"missing registry: {REGISTRY.relative_to(ROOT)}")

    handoff = HANDOFF.read_text(encoding="utf-8")
    required_handoff_terms = [
        "goal_id: RC-CTRL-001",
        "research_commons/control/task-registry.json",
        "## Archive conditions",
        "## Cross-repository dependencies",
    ]
    for term in required_handoff_terms:
        if term not in handoff:
            fail(f"handoff missing required term: {term}")

    data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    if data.get("registry_id") != "RC-CTRL-001":
        fail("unexpected registry_id")
    if data.get("canonical_handoff") != "RESEARCH_COMMONS_MIRROR_HANDOFF.md":
        fail("canonical handoff mismatch")

    tasks = data.get("tasks")
    if not isinstance(tasks, list) or not tasks:
        fail("tasks must be a non-empty list")

    seen: set[str] = set()
    now = datetime.now(timezone.utc)
    ttl = timedelta(hours=int(data.get("claim_ttl_hours", 72)))
    stale: list[str] = []

    for task in tasks:
        task_id = task.get("task_id")
        if not task_id or task_id in seen:
            fail(f"missing or duplicate task_id: {task_id}")
        seen.add(task_id)

        state = task.get("claim_state")
        if state not in ALLOWED:
            fail(f"{task_id}: invalid claim_state {state}")

        for field in (
            "originating_goal",
            "surface",
            "owner",
            "role",
            "release_condition",
            "expected_evidence",
            "collision_boundary",
            "next_task_after_release",
        ):
            if not task.get(field):
                fail(f"{task_id}: missing {field}")

        timestamp = task.get("claim_timestamp")
        if state.startswith("CLAIMED_FOR_") or state == "MACHINE_OWNED":
            if not timestamp:
                fail(f"{task_id}: active claim missing timestamp")
            if state != "MACHINE_OWNED" and now - parse_time(timestamp) > ttl:
                stale.append(task_id)

    required_tasks = {"RC-002", "RC-004", "RC-005", "RC-009", "RC-010", "RC-011", "RC-012"}
    missing = required_tasks - seen
    if missing:
        fail(f"missing required tasks: {sorted(missing)}")
    if stale:
        fail(f"stale claims require release, block, or evidence-backed renewal: {stale}")

    print(json.dumps({
        "state": "COMPLETE",
        "registry_id": data["registry_id"],
        "task_count": len(tasks),
        "active_claims": sum(1 for task in tasks if str(task["claim_state"]).startswith("CLAIMED_FOR_")),
        "machine_owned": sum(1 for task in tasks if task["claim_state"] == "MACHINE_OWNED"),
        "stale_claims": [],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
