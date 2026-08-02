#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COORD = ROOT / "coordination"
LEDGER_PATH = COORD / "gtg-reconstruction-tasks.json"
REPORT_PATH = COORD / "gtg-task-discovery-report.json"

PROHIBITED_TRUE = {
    "execution_authority",
    "certification_authority",
    "mathematical_closure",
    "independent_verification_complete",
    "release_ready",
    "archive_ready",
}


def fail(message: str) -> None:
    raise SystemExit(f"GTG TASK DISCOVERY: FAIL - {message}")


def load(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"cannot read {path.relative_to(ROOT)}: {exc}")


def main() -> None:
    ledger = load(LEDGER_PATH)
    tasks = ledger.get("tasks", [])
    indexed = {task.get("task_id"): task for task in tasks}
    if None in indexed or len(indexed) != len(tasks):
        fail("central ledger has missing or duplicate task IDs")

    discovered: dict[str, dict] = {}
    for path in sorted(COORD.glob("gtg-*-task.json")):
        data = load(path)
        task_id = data.get("task_id")
        if not task_id:
            fail(f"{path.name} has no task_id")
        if task_id in discovered:
            fail(f"duplicate discovered task {task_id}")
        discovered[task_id] = {"path": str(path.relative_to(ROOT)), "data": data}

    receipts: dict[str, dict] = {}
    for path in sorted(COORD.glob("gtg-*-validation-receipt.json")):
        data = load(path)
        task_id = data.get("task_id")
        if task_id:
            receipts[task_id] = {"path": str(path.relative_to(ROOT)), "data": data}

    missing_from_ledger = sorted(set(discovered) - set(indexed))
    if missing_from_ledger:
        fail(f"discovered tasks absent from central ledger: {missing_from_ledger}")

    stale: list[str] = []
    for task_id, receipt in receipts.items():
        activation = receipt["data"].get("activation_state")
        if activation == "ACTIVE" and task_id in indexed and indexed[task_id].get("status") != "COMPLETE":
            stale.append(task_id)
    if stale:
        fail(f"activated tasks have stale ledger status: {sorted(stale)}")

    for task in tasks:
        if task.get("status") != "COMPLETE":
            if task.get("execution_repository") != "StegVerse-Labs/StegScholar":
                fail(f"{task.get('task_id')} delegates outside StegVerse")
            if not task.get("execution_path") or not task.get("next_action") or not task.get("completion_evidence"):
                fail(f"{task.get('task_id')} is status-only")

    for key, value in ledger.get("claims", {}).items():
        if key in PROHIBITED_TRUE and value is not False:
            fail(f"prohibited claim enabled: {key}")

    noncomplete = [task for task in tasks if task.get("status") != "COMPLETE"]
    mutation_capable = [
        task for task in noncomplete
        if task.get("execution_mode") not in {"AUTOMATED_OBSERVATION"}
    ]
    if noncomplete and not mutation_capable:
        fail("only observation tasks remain; local mutation successor required")

    report = {
        "schema_version": "stegverse-gtg-task-discovery-report.v1",
        "ledger": str(LEDGER_PATH.relative_to(ROOT)),
        "discovered_task_files": {task_id: item["path"] for task_id, item in discovered.items()},
        "receipt_files": {task_id: item["path"] for task_id, item in receipts.items()},
        "noncomplete_tasks": [task.get("task_id") for task in noncomplete],
        "mutation_capable_tasks": [task.get("task_id") for task in mutation_capable],
        "external_tasks": [],
        "development_halted": False,
        "claims_upgraded": False,
    }
    REPORT_PATH.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))
    print("GTG TASK DISCOVERY: PASS")


if __name__ == "__main__":
    main()
