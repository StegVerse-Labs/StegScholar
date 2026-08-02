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
    "funding/schemas/evidence-crosswalk.schema.json",
    "funding/schemas/submission-receipt.schema.json",
    "funding/applications/examples/FUNDING-EXAMPLE-001.json",
    "funding/applications/active/FUNDING-NSF-PESOSE-2026-001.json",
    "funding/applications/active/FUNDING-NSF-PESOSE-2026-001-concept.md",
    "funding/applications/active/FUNDING-NSF-PESOSE-2026-001-eligibility.md",
    "funding/applications/active/FUNDING-NSF-PESOSE-2026-001-product-evidence.md",
    "funding/applications/active/FUNDING-NSF-PESOSE-2026-001-compliance.md",
    "funding/applications/active/FUNDING-NSF-PESOSE-2026-001-project-summary.md",
    "funding/applications/active/FUNDING-NSF-PESOSE-2026-001-milestones.md",
    "funding/applications/active/FUNDING-NSF-PESOSE-2026-001-budget-request.json",
    "funding/reusable/organization-profile/README.md",
    "funding/contracts/stegpatents-source-contract.md",
    "funding/contracts/stegfinco-budget-handoff-contract.md",
    "funding/contracts/stegops-deliverables-consumer-contract.md",
    "funding/tools/validate_funding_state.py",
    ".github/workflows/funding-state-validation.yml",
]
TERMINAL = {"COMPLETE", "SUPERSEDED", "MERGED_INTO_CANONICAL_WORKSTREAM"}
ACTIVE = {"CLAIMED_FOR_IMPLEMENTATION", "CLAIMED_FOR_VALIDATION", "CLAIMED_FOR_INTEGRATION"}
APPLICATION_STATES = {
    "DISCOVERED", "ELIGIBILITY_REVIEW", "GO_NO_GO_REVIEW", "DRAFTING",
    "INTERNAL_REVIEW", "SUBMISSION_READY", "SUBMITTED", "AWARDED",
    "DECLINED", "WITHDRAWN", "BLOCKED", "SUPERSEDED",
}


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
    claim_ids: set[str] = set()
    for claim in claims:
        task_id = claim.get("task_id")
        if not task_id or task_id in claim_ids:
            fail(f"missing or duplicate claim task_id: {task_id}")
        claim_ids.add(task_id)
        state = claim.get("state")
        if state not in allowed:
            fail(f"claim {task_id} has invalid state {state}")
        if state in ACTIVE:
            expiry = datetime.fromisoformat(claim["expires_at"])
            if expiry < now:
                fail(f"claim {task_id} expired at {claim['expires_at']}")
            for surface in claim.get("surfaces", []):
                prior = surfaces.setdefault(surface, task_id)
                if prior != task_id:
                    fail(f"surface collision: {surface} claimed by {prior} and {task_id}")
        for key in ("claimant", "role", "release_condition", "expected_evidence", "collision_boundaries", "next_task_after_release"):
            if not claim.get(key):
                fail(f"claim {task_id} missing {key}")

    task_ids: set[str] = set()
    for task in tasks:
        task_id = task.get("task_id")
        if not task_id or task_id in task_ids:
            fail(f"missing or duplicate task_id: {task_id}")
        task_ids.add(task_id)
        if task.get("state") not in allowed:
            fail(f"task {task_id} has invalid state {task.get('state')}")
        if task.get("state") not in TERMINAL:
            for key in ("owner", "location", "next_action", "validation_state", "integration_state", "evidence_location"):
                if task.get(key) in (None, ""):
                    fail(f"incomplete task {task_id} missing {key}")


def validate_application(app: dict, path: Path) -> None:
    required = {
        "application_id", "opportunity", "applicant", "program", "state", "authority",
        "dates", "evidence_refs", "budget", "publication_classification", "next_action",
    }
    missing = sorted(required - set(app))
    if missing:
        fail(f"{path.relative_to(ROOT)} missing fields: {', '.join(missing)}")
    if app["state"] not in APPLICATION_STATES:
        fail(f"{path.relative_to(ROOT)} has invalid application state {app['state']}")
    if app["authority"] != {
        "application_owner": "StegVerse-Labs/StegScholar",
        "ip_authority": "StegVerse-Labs/StegPatents",
        "budget_authority": "StegVerse-Labs/StegFinCo",
        "deliverables_authority": "StegVerse-Labs/StegOps-Deliverables",
    }:
        fail(f"{path.relative_to(ROOT)} authority boundary is invalid")
    if not app["evidence_refs"]:
        fail(f"{path.relative_to(ROOT)} has no evidence references")
    for ref in app["evidence_refs"] + app["program"].get("research_paths", []):
        if not (ROOT / ref).is_file():
            fail(f"referenced evidence does not exist: {ref}")
    if not all(app["next_action"].get(k) for k in ("owner", "location", "action", "release_condition")):
        fail(f"{path.relative_to(ROOT)} next_action is incomplete")
    if app["state"] == "SUBMISSION_READY":
        if app["budget"].get("status") != "APPROVED":
            fail(f"{path.relative_to(ROOT)} cannot be SUBMISSION_READY without approved budget")
        if app["publication_classification"] == "DISCLOSURE_REVIEW_REQUIRED":
            fail(f"{path.relative_to(ROOT)} cannot be SUBMISSION_READY before disclosure review")


def validate_budget(path: Path) -> None:
    budget = load_json(path)
    lines = budget.get("planning_envelope")
    if not isinstance(lines, list) or not lines:
        fail("PESOSE budget planning_envelope must be a non-empty array")
    calculated = sum(item.get("provisional_amount", 0) for item in lines)
    if calculated != budget.get("total_provisional_amount"):
        fail(f"PESOSE budget arithmetic mismatch: lines={calculated}, total={budget.get('total_provisional_amount')}")
    if calculated > budget.get("ceiling", 0):
        fail("PESOSE provisional budget exceeds sponsor ceiling")
    if budget.get("state") != "DRAFT_UNAPPROVED":
        fail("PESOSE budget must remain DRAFT_UNAPPROVED until StegFinCo approval exists")
    if budget.get("validation", {}).get("authority_approved") is not False:
        fail("PESOSE draft budget must not claim authority approval")


def main() -> int:
    missing = [path for path in REQUIRED if not (ROOT / path).is_file()]
    if missing:
        fail(f"missing required files: {', '.join(missing)}")

    registry = load_json(ROOT / "funding/coordination/funding-tasks.json")
    validate_registry(registry)

    for schema in (
        "funding/schemas/application.schema.json",
        "funding/schemas/evidence-crosswalk.schema.json",
        "funding/schemas/submission-receipt.schema.json",
    ):
        load_json(ROOT / schema)

    application_paths = [ROOT / "funding/applications/examples/FUNDING-EXAMPLE-001.json"]
    application_paths.extend(sorted((ROOT / "funding/applications/active").glob("FUNDING-*.json")))
    application_paths = [p for p in application_paths if not p.name.endswith("budget-request.json")]
    for path in application_paths:
        validate_application(load_json(path), path)

    validate_budget(ROOT / "funding/applications/active/FUNDING-NSF-PESOSE-2026-001-budget-request.json")

    receipt = {
        "result": "COMPLETE",
        "goal_id": registry["goal_id"],
        "validated_files": REQUIRED,
        "validated_applications": [str(path.relative_to(ROOT)) for path in application_paths],
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
