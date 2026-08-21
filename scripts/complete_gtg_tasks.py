#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "coordination" / "gtg-reconstruction-tasks.json"
MANIFEST = ROOT / "manifests" / "gtg-reconstruction-mirror-v1.json"
REPORT = ROOT / "coordination" / "gtg-task-completion-report.json"


def load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path} must contain an object")
    return value


def task_by_id(ledger: dict[str, Any], task_id: str) -> dict[str, Any] | None:
    for task in ledger.get("tasks", []):
        if task.get("task_id") == task_id:
            return task
    return None


def observe_pinned_factory_r4(ledger: dict[str, Any], manifest: dict[str, Any]) -> dict[str, Any]:
    """Consume the repository-resident immutable R4 factory binding.

    StegScholar is not the authority for the private factory repository. Once the
    canonical handoff and mirror manifest have durably pinned an ACTIVE factory
    commit, scheduled maintenance must not reintroduce cross-private-repository
    GitHub-token observation as a prerequisite. If the binding is absent or not
    ACTIVE, fail closed and require an authorized external evidence projection.
    """
    r4 = manifest.get("levels", {}).get("R4", {})
    observe_task = task_by_id(ledger, "SV-GTG-R4-OBSERVE-001") or {}
    mirror_task = task_by_id(ledger, "SV-GTG-R4-MIRROR-002") or {}
    commit = r4.get("factory_commit")
    active = (
        isinstance(commit, str)
        and len(commit) == 40
        and r4.get("factory_state") == "ACTIVE"
        and r4.get("mirror_state") == "ACTIVE"
        and observe_task.get("status") == "COMPLETE"
        and mirror_task.get("status") == "COMPLETE"
    )
    if not active:
        return {
            "state": "AUTHORIZED_FACTORY_EVIDENCE_REQUIRED",
            "commit": commit,
            "source": "repository-resident-mirror",
            "private_repository_queried": False,
            "github_token_required": False,
            "authority_effect": False,
        }
    return {
        "state": "FACTORY_R4_ACTIVE_PINNED",
        "commit": commit,
        "source": "manifests/gtg-reconstruction-mirror-v1.json",
        "task_evidence": {
            "observe": observe_task.get("completion_evidence"),
            "mirror": mirror_task.get("completion_evidence"),
        },
        "private_repository_queried": False,
        "github_token_required": False,
        "authority_effect": False,
    }


def main() -> None:
    ledger = load(LEDGER)
    manifest = load(MANIFEST)
    observation = observe_pinned_factory_r4(ledger, manifest)

    report = {
        "schema_version": "stegverse-gtg-task-completion-report.v1",
        "observation": observation,
        "changed": False,
        "authority_effect": False,
        "execution_authorized": False,
        "archive_ready": False,
    }
    REPORT.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))

    if observation["state"] != "FACTORY_R4_ACTIVE_PINNED":
        raise SystemExit(
            "R4 factory evidence is not durably pinned ACTIVE; "
            "consume an authorized TV/TVC-governed evidence projection before continuing"
        )


if __name__ == "__main__":
    main()
