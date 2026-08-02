#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "coordination" / "gtg-reconstruction-tasks.json"
REPORT = ROOT / "coordination" / "gtg-reconstruction-task-report.json"

VALID_STATUSES = {
    "READY",
    "RUNNING",
    "ACTIVE_VALIDATION",
    "QUEUED",
    "BLOCKED",
    "BLOCKED_OBSERVED",
    "COMPLETE",
}
ACTIONABLE_STATUSES = {"READY", "RUNNING", "ACTIVE_VALIDATION"}


def fail(message: str) -> None:
    raise SystemExit(f"GTG TASK ORCHESTRATOR: FAIL - {message}")


def github_json(url: str) -> object | None:
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "stegverse-gtg-task-orchestrator"}
    token = os.getenv("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    request = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            return json.loads(response.read().decode("utf-8"))
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError):
        return None


def observe_factory_r4() -> dict:
    pulls = github_json(
        "https://api.github.com/repos/Admissible-Existence/ae-validation-factory/pulls?state=closed&per_page=100"
    )
    if not isinstance(pulls, list):
        return {"state": "OBSERVATION_UNAVAILABLE", "commit": None}
    candidates = []
    for pull in pulls:
        title = str(pull.get("title", "")).lower()
        body = str(pull.get("body", "")).lower()
        if pull.get("merged_at") and ("r4" in title or "authority reconstruction" in title or "factory-r4" in body):
            candidates.append(pull)
    if not candidates:
        return {"state": "FACTORY_R4_NOT_ACTIVE", "commit": None}
    newest = sorted(candidates, key=lambda item: item.get("merged_at") or "")[-1]
    return {"state": "FACTORY_R4_ACTIVE", "commit": newest.get("merge_commit_sha"), "pull": newest.get("number")}


def validate_task(task: dict, ids: set[str]) -> None:
    required = {
        "task_id", "title", "exists_at", "execution_repository", "execution_path",
        "status", "execution_mode", "dependencies", "next_action", "completion_evidence",
        "on_complete_activate"
    }
    missing = required - set(task)
    if missing:
        fail(f"{task.get('task_id', '<unknown>')} missing fields: {sorted(missing)}")
    if task["status"] not in VALID_STATUSES:
        fail(f"{task['task_id']} invalid status: {task['status']}")
    if not task["exists_at"].startswith("StegVerse-Labs/StegScholar:"):
        fail(f"{task['task_id']} has no StegVerse task location")
    if task["execution_repository"] != "StegVerse-Labs/StegScholar":
        fail(f"{task['task_id']} incorrectly delegates execution outside StegVerse")
    if not task["execution_path"] or not task["next_action"] or not task["completion_evidence"]:
        fail(f"{task['task_id']} is status-only and would halt development")
    for dependency in task["dependencies"]:
        if isinstance(dependency, str) and dependency not in ids:
            fail(f"{task['task_id']} references unknown task dependency {dependency}")


def main() -> None:
    ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
    tasks = ledger.get("tasks", [])
    if not tasks:
        fail("incomplete program has no tasks")
    ids = {task.get("task_id") for task in tasks}
    if None in ids or len(ids) != len(tasks):
        fail("task IDs missing or duplicated")
    for task in tasks:
        validate_task(task, ids)

    observation = observe_factory_r4()
    actionable: list[dict] = []
    effective_statuses: dict[str, str] = {}
    for task in tasks:
        effective_status = task["status"]
        if task["task_id"] == "SV-GTG-R4-OBSERVE-001" and observation["state"] == "FACTORY_R4_ACTIVE":
            effective_status = "COMPLETE"
        if task["task_id"] == "SV-GTG-R4-MIRROR-002" and observation["state"] == "FACTORY_R4_ACTIVE":
            effective_status = "READY"
        effective_statuses[task["task_id"]] = effective_status
        if effective_status in ACTIONABLE_STATUSES:
            actionable.append({
                "task_id": task["task_id"],
                "status": effective_status,
                "exists_at": task["exists_at"],
                "execution_path": task["execution_path"],
                "next_action": task["next_action"]
            })

    incomplete = any(status != "COMPLETE" for status in effective_statuses.values())
    if incomplete and not actionable:
        fail("development would halt: no executable local task is exposed")

    report = {
        "schema_version": "stegverse-gtg-task-report.v1",
        "program": ledger["program"],
        "factory_r4_observation": observation,
        "effective_statuses": effective_statuses,
        "actionable_tasks": actionable,
        "development_halted": False,
        "archive_ready": False,
        "authority_effect": False,
        "execution_authorized": False
    }
    REPORT.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))
    print(f"GTG TASK ORCHESTRATOR: PASS - {len(actionable)} executable local task(s)")


if __name__ == "__main__":
    main()
