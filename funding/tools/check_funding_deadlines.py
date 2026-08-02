#!/usr/bin/env python3
"""Evaluate funding deadlines and active claim expiry without changing authority state."""

from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "funding/coordination/funding-tasks.json"
ACTIVE_DIR = ROOT / "funding/applications/active"
OUTPUT = ROOT / "funding/evidence/latest-deadline-watch.json"
ACTIVE_CLAIM_STATES = {
    "CLAIMED_FOR_IMPLEMENTATION",
    "CLAIMED_FOR_VALIDATION",
    "CLAIMED_FOR_INTEGRATION",
}


def parse_time(value: str, label: str) -> datetime:
    try:
        parsed = datetime.fromisoformat(value)
    except Exception as exc:
        raise ValueError(f"invalid {label} timestamp {value!r}: {exc}") from exc
    if parsed.tzinfo is None:
        raise ValueError(f"{label} timestamp must include timezone: {value}")
    return parsed.astimezone(timezone.utc)


def main() -> int:
    now = datetime.now(timezone.utc)
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    findings: list[dict] = []
    failures: list[str] = []

    for claim in registry.get("claims", []):
        if claim.get("state") not in ACTIVE_CLAIM_STATES:
            continue
        task_id = claim.get("task_id", "UNKNOWN")
        expires_at = claim.get("expires_at")
        if not expires_at:
            failures.append(f"active claim {task_id} has no expires_at")
            continue
        expiry = parse_time(expires_at, f"claim {task_id} expiry")
        remaining_hours = (expiry - now).total_seconds() / 3600
        state = "EXPIRED" if remaining_hours < 0 else "EXPIRING_SOON" if remaining_hours <= 336 else "ACTIVE"
        findings.append({
            "kind": "CLAIM",
            "task_id": task_id,
            "state": state,
            "expires_at": expires_at,
            "hours_remaining": round(remaining_hours, 2),
            "release_condition": claim.get("release_condition"),
        })
        if state == "EXPIRED":
            failures.append(f"active claim {task_id} expired at {expires_at}")

    application_paths = sorted(ACTIVE_DIR.glob("FUNDING-*.json"))
    application_paths = [path for path in application_paths if not path.name.endswith("budget-request.json")]
    for path in application_paths:
        app = json.loads(path.read_text(encoding="utf-8"))
        application_id = app.get("application_id", path.stem)
        deadline_value = app.get("dates", {}).get("deadline")
        if not deadline_value:
            failures.append(f"application {application_id} has no deadline")
            continue
        deadline = parse_time(deadline_value, f"application {application_id} deadline")
        remaining_hours = (deadline - now).total_seconds() / 3600
        state = "OVERDUE" if remaining_hours < 0 else "DUE_SOON" if remaining_hours <= 336 else "OPEN"
        findings.append({
            "kind": "APPLICATION",
            "application_id": application_id,
            "application_state": app.get("state"),
            "deadline_state": state,
            "deadline": deadline_value,
            "hours_remaining": round(remaining_hours, 2),
            "next_action": app.get("next_action"),
        })
        if state == "OVERDUE" and app.get("state") not in {"SUBMITTED", "DECLINED", "WITHDRAWN", "SUPERSEDED", "AWARDED"}:
            failures.append(f"application {application_id} is overdue but remains {app.get('state')}")

    receipt = {
        "result": "FAILED" if failures else "COMPLETE",
        "checked_at": now.isoformat(),
        "goal_id": registry.get("goal_id"),
        "findings": findings,
        "failures": failures,
        "next_executable_task": failures[0] if failures else "continue highest-priority application task before nearest deadline",
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(receipt, indent=2))
    return 1 if failures else 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"FAILED: {exc}", file=sys.stderr)
        raise SystemExit(1)
