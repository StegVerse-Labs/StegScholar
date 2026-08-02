#!/usr/bin/env python3
"""Deterministic validation for StegVerse Time causal-kernel fixtures."""
from __future__ import annotations
import json, sys
from pathlib import Path
from typing import Iterable
Relation = tuple[str, str]

def fail(message: str) -> None: raise ValueError(message)

def relation_set(raw: Iterable[object], name: str, events: set[str]) -> set[Relation]:
    result: set[Relation] = set()
    for i, item in enumerate(raw):
        if not isinstance(item, list) or len(item) != 2 or not all(isinstance(v, str) for v in item): fail(f"{name}[{i}] must be a two-string relation")
        a, b = item
        if a not in events or b not in events: fail(f"{name}[{i}] references an undeclared event")
        if a == b: fail(f"{name}[{i}] is reflexive")
        result.add((a, b))
    return result

def is_acyclic(events: set[str], relations: set[Relation]) -> bool:
    out = {e: set() for e in events}; indegree = {e: 0 for e in events}
    for a, b in relations:
        if b not in out[a]: out[a].add(b); indegree[b] += 1
    queue = [e for e, d in indegree.items() if d == 0]; visited = 0
    while queue:
        e = queue.pop(); visited += 1
        for nxt in out[e]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0: queue.append(nxt)
    return visited == len(events)

def projected_order(fine: list[str], mapping: dict[str, str]) -> list[str]:
    result: list[str] = []
    for event in fine:
        coarse = mapping.get(event)
        if coarse is None: fail(f"resolution map has no target for fine event {event}")
        if not result or result[-1] != coarse: result.append(coarse)
    return result

def validate_resolution_maps(maps: object) -> None:
    if not isinstance(maps, list): fail("resolution_maps must be a list")
    for i, item in enumerate(maps):
        if not isinstance(item, dict): fail(f"resolution_maps[{i}] must be an object")
        mapping = item.get("fine_to_coarse"); fine = item.get("fine_serializations"); coarse = item.get("coarse_serializations"); distributions = item.get("quotient_distributions")
        if not isinstance(mapping, dict) or not all(isinstance(k, str) and isinstance(v, str) for k, v in mapping.items()): fail(f"resolution_maps[{i}].fine_to_coarse must map strings to strings")
        if not isinstance(fine, list) or not isinstance(coarse, list): fail(f"resolution_maps[{i}] serialization sets must be lists")
        projected = {tuple(projected_order(seq, mapping)) for seq in fine if isinstance(seq, list) and all(isinstance(v, str) for v in seq)}
        for j, seq in enumerate(coarse):
            if not isinstance(seq, list) or not all(isinstance(v, str) for v in seq): fail(f"resolution_maps[{i}].coarse_serializations[{j}] must be a string list")
            if tuple(seq) not in projected: fail(f"manufactured coarse chronology in map {item.get('map_id', i)}: {seq}")
        if not isinstance(distributions, dict): fail(f"resolution_maps[{i}].quotient_distributions must be an object")
        groups: dict[str, list[dict[str, float]]] = {}
        for representative, record in distributions.items():
            if not isinstance(record, dict) or "class" not in record or "probabilities" not in record: fail(f"quotient distribution {representative} is malformed")
            probs = record["probabilities"]
            if not isinstance(probs, dict) or any(not isinstance(v, (int, float)) or v < 0 for v in probs.values()): fail(f"quotient distribution {representative} has invalid probabilities")
            if abs(sum(probs.values()) - 1.0) > 1e-9: fail(f"quotient distribution {representative} is not normalized")
            groups.setdefault(str(record["class"]), []).append({k: float(v) for k, v in probs.items()})
        for class_id, rows in groups.items():
            if rows and any(row != rows[0] for row in rows[1:]): fail(f"quotient lumpability failure in class {class_id}")

def validate(data: object) -> None:
    if not isinstance(data, dict): fail("document must be a JSON object")
    required = {"declaration_id","subject_id","resolution","events","identity_evidence_refs","kernel_relations","branch_orders","operational_quotient","resolution_maps","gtg_admissibility"}
    missing = sorted(required - data.keys())
    if missing: fail("missing required fields: " + ", ".join(missing))
    if data["gtg_admissibility"] is not None: fail("temporal substrate must not assert GTG admissibility")
    raw_events = data["events"]
    if not isinstance(raw_events, list) or not raw_events or not all(isinstance(v, str) and v for v in raw_events): fail("events must be a nonempty string list")
    events = set(raw_events)
    if len(events) != len(raw_events): fail("events must be unique")
    evidence = data["identity_evidence_refs"]
    if not isinstance(evidence, list) or not evidence or not all(isinstance(v, str) and v for v in evidence): fail("identity_evidence_refs must be nonempty")
    kernel = relation_set(data["kernel_relations"], "kernel_relations", events)
    if not is_acyclic(events, kernel): fail("kernel_relations must be acyclic")
    branches = data["branch_orders"]
    if not isinstance(branches, list) or not branches: fail("branch_orders must be nonempty")
    ids: set[str] = set()
    for i, branch in enumerate(branches):
        if not isinstance(branch, dict): fail(f"branch_orders[{i}] must be an object")
        branch_id = branch.get("branch_id")
        if not isinstance(branch_id, str) or not branch_id or branch_id in ids: fail(f"branch_orders[{i}].branch_id must be unique and nonempty")
        ids.add(branch_id)
        relations = relation_set(branch.get("relations", []), f"branch_orders[{i}].relations", events)
        if not is_acyclic(events, relations): fail(f"branch {branch_id} is cyclic")
        if not kernel.issubset(relations): fail(f"branch {branch_id} does not extend the invariant kernel")
    quotient = data["operational_quotient"]
    if not isinstance(quotient, dict) or not isinstance(quotient.get("equivalence_classes"), list): fail("operational_quotient.equivalence_classes must be a list")
    validate_resolution_maps(data["resolution_maps"])

def main() -> int:
    if len(sys.argv) != 2: print("usage: validate_time_causal_kernel.py <fixture.json>", file=sys.stderr); return 2
    try: validate(json.loads(Path(sys.argv[1]).read_text(encoding="utf-8")))
    except (OSError, json.JSONDecodeError, ValueError) as exc: print(f"FAIL: {exc}", file=sys.stderr); return 1
    print("PASS: time causal kernel fixture is structurally valid"); return 0
if __name__ == "__main__": raise SystemExit(main())
