#!/usr/bin/env python3
"""Validate StegVerse Time causal-kernel fixtures without third-party packages."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Iterable

Relation = tuple[str, str]


def fail(message: str) -> None:
    raise ValueError(message)


def relation_set(raw: Iterable[object], name: str, events: set[str]) -> set[Relation]:
    result: set[Relation] = set()
    for index, item in enumerate(raw):
        if not isinstance(item, list) or len(item) != 2 or not all(isinstance(v, str) for v in item):
            fail(f"{name}[{index}] must be a two-string relation")
        relation = (item[0], item[1])
        if relation[0] not in events or relation[1] not in events:
            fail(f"{name}[{index}] references an undeclared event")
        if relation[0] == relation[1]:
            fail(f"{name}[{index}] is reflexive")
        result.add(relation)
    return result


def is_acyclic(events: set[str], relations: set[Relation]) -> bool:
    outgoing = {event: set() for event in events}
    indegree = {event: 0 for event in events}
    for left, right in relations:
        if right not in outgoing[left]:
            outgoing[left].add(right)
            indegree[right] += 1
    queue = [event for event, degree in indegree.items() if degree == 0]
    visited = 0
    while queue:
        event = queue.pop()
        visited += 1
        for successor in outgoing[event]:
            indegree[successor] -= 1
            if indegree[successor] == 0:
                queue.append(successor)
    return visited == len(events)


def validate(data: object) -> None:
    if not isinstance(data, dict):
        fail("document must be a JSON object")
    required = {
        "declaration_id", "subject_id", "resolution", "events",
        "identity_evidence_refs", "kernel_relations", "branch_orders",
        "operational_quotient", "resolution_maps", "gtg_admissibility",
    }
    missing = sorted(required - data.keys())
    if missing:
        fail(f"missing required fields: {', '.join(missing)}")
    if data["gtg_admissibility"] is not None:
        fail("temporal substrate must not assert GTG admissibility")
    events_raw = data["events"]
    if not isinstance(events_raw, list) or not events_raw or not all(isinstance(v, str) and v for v in events_raw):
        fail("events must be a nonempty string list")
    events = set(events_raw)
    if len(events) != len(events_raw):
        fail("events must be unique")
    evidence = data["identity_evidence_refs"]
    if not isinstance(evidence, list) or not evidence or not all(isinstance(v, str) and v for v in evidence):
        fail("identity_evidence_refs must be nonempty")
    kernel = relation_set(data["kernel_relations"], "kernel_relations", events)
    if not is_acyclic(events, kernel):
        fail("kernel_relations must be acyclic")
    branches = data["branch_orders"]
    if not isinstance(branches, list) or not branches:
        fail("branch_orders must be nonempty")
    branch_ids: set[str] = set()
    for index, branch in enumerate(branches):
        if not isinstance(branch, dict):
            fail(f"branch_orders[{index}] must be an object")
        branch_id = branch.get("branch_id")
        if not isinstance(branch_id, str) or not branch_id or branch_id in branch_ids:
            fail(f"branch_orders[{index}].branch_id must be unique and nonempty")
        branch_ids.add(branch_id)
        relations = relation_set(branch.get("relations", []), f"branch_orders[{index}].relations", events)
        if not is_acyclic(events, relations):
            fail(f"branch {branch_id} is cyclic")
        if not kernel.issubset(relations):
            fail(f"branch {branch_id} does not extend the invariant kernel")
    quotient = data["operational_quotient"]
    if not isinstance(quotient, dict) or not isinstance(quotient.get("equivalence_classes"), list):
        fail("operational_quotient.equivalence_classes must be a list")
    if not isinstance(data["resolution_maps"], list):
        fail("resolution_maps must be a list")


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: validate_time_causal_kernel.py <fixture.json>", file=sys.stderr)
        return 2
    path = Path(sys.argv[1])
    try:
        validate(json.loads(path.read_text(encoding="utf-8")))
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1
    print("PASS: time causal kernel fixture is structurally valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
