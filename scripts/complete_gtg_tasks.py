#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "coordination" / "gtg-reconstruction-tasks.json"
MANIFEST = ROOT / "manifests" / "gtg-reconstruction-mirror-v1.json"
REPORT = ROOT / "coordination" / "gtg-task-completion-report.json"


def github_json(url: str):
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "stegverse-gtg-completer"}
    token = os.getenv("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=20) as response:
        return json.loads(response.read().decode("utf-8"))


def observe_factory_r4() -> dict:
    pulls = github_json("https://api.github.com/repos/Admissible-Existence/ae-validation-factory/pulls?state=closed&per_page=100")
    candidates = []
    for pull in pulls:
        text = f"{pull.get('title', '')} {pull.get('body', '')}".lower()
        if pull.get("merged_at") and ("factory-r4" in text or "authority reconstruction" in text or " r4 " in f" {text} "):
            candidates.append(pull)
    if not candidates:
        return {"state": "FACTORY_R4_NOT_ACTIVE", "commit": None}
    newest = sorted(candidates, key=lambda item: item.get("merged_at") or "")[-1]
    return {"state": "FACTORY_R4_ACTIVE", "commit": newest.get("merge_commit_sha"), "pull": newest.get("number")}


def main() -> None:
    ledger = json.loads(LEDGER.read_text())
    manifest = json.loads(MANIFEST.read_text())
    observation = observe_factory_r4()
    changed = False

    if observation["state"] == "FACTORY_R4_ACTIVE" and observation.get("commit"):
        r4 = manifest["levels"]["R4"]
        if r4.get("factory_commit") != observation["commit"] or r4.get("factory_state") != "ACTIVE":
            r4["factory_commit"] = observation["commit"]
            r4["factory_state"] = "ACTIVE"
            r4["mirror_state"] = "ACTIVE"
            changed = True
        for task in ledger["tasks"]:
            if task["task_id"] == "SV-GTG-R4-OBSERVE-001":
                task["status"] = "COMPLETE"
                task["completion_evidence"] = f"FACTORY_R4_ACTIVE at {observation['commit']}"
            elif task["task_id"] == "SV-GTG-R4-MIRROR-002":
                task["status"] = "COMPLETE"
                task["completion_evidence"] = f"R4 mirror bound to {observation['commit']}"
        changed = True

    report = {
        "schema_version": "stegverse-gtg-task-completion-report.v1",
        "observation": observation,
        "changed": changed,
        "authority_effect": False,
        "execution_authorized": False,
        "archive_ready": False
    }
    REPORT.write_text(json.dumps(report, indent=2) + "\n")
    if changed:
        MANIFEST.write_text(json.dumps(manifest, indent=2) + "\n")
        LEDGER.write_text(json.dumps(ledger, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
