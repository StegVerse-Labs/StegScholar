#!/usr/bin/env python3
"""Validate the source-neutral Published Research Graph.

This validator checks graph identity, provenance, relation state, and authority
boundaries only. It does not certify scientific truth, publication standing,
priority, replication, governance authority, execution authority, or reuse
admissibility.
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
GRAPH_PATH = ROOT / "research_commons" / "published_research_graph" / "graph.json"
SCHEMA_PATH = ROOT / "research_commons" / "published_research_graph" / "schema.json"

ALLOWED_PREDICATES = {
    "cites", "supports", "corroborates", "contradicts", "challenges",
    "extends", "refines", "replicates", "fails_to_replicate",
    "uses_method_from", "uses_data_from", "shares_evidence_with",
    "derives_from", "supersedes", "independently_converges_with",
    "conceptually_related",
}


def load(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise SystemExit(f"cannot load {path}: {exc}") from exc


def main() -> int:
    graph = load(GRAPH_PATH)
    load(SCHEMA_PATH)  # deterministic parse check; no third-party dependency.
    errors: list[str] = []

    if graph.get("graph_version") != "1.0.0":
        errors.append("graph_version must be 1.0.0")
    if graph.get("authority_boundary") is None:
        errors.append("authority_boundary is required")

    documents = graph.get("documents")
    relations = graph.get("relations")
    if not isinstance(documents, list) or not documents:
        errors.append("documents must be a non-empty list")
        documents = []
    if not isinstance(relations, list):
        errors.append("relations must be a list")
        relations = []

    document_ids: set[str] = set()
    anchor_ids: set[str] = set()
    for index, doc in enumerate(documents):
        doc_id = doc.get("document_id")
        if not doc_id or doc_id in document_ids:
            errors.append(f"document[{index}] has missing/duplicate document_id: {doc_id}")
        else:
            document_ids.add(doc_id)
        if doc.get("authority_effect") != "NONE":
            errors.append(f"document[{index}] authority_effect must be NONE")
        provenance = doc.get("provenance", {})
        if provenance.get("custody_retained_by_source") is not True:
            errors.append(f"document[{index}] must retain source custody")
        if not provenance.get("source_authority") or not provenance.get("observed_at"):
            errors.append(f"document[{index}] requires source provenance")
        if doc.get("source_class") == "external_published_research":
            if not any(doc.get(k) for k in ("doi", "canonical_url", "content_hash")):
                errors.append(f"external document {doc_id} requires DOI, canonical_url, or content_hash")
        for kind in ("claims", "evidence"):
            for anchor in doc.get(kind, []):
                anchor_id = anchor.get("claim_id") if kind == "claims" else anchor.get("evidence_id")
                if not anchor_id or anchor_id in anchor_ids:
                    errors.append(f"{doc_id} has missing/duplicate {kind} identity: {anchor_id}")
                else:
                    anchor_ids.add(anchor_id)

    relation_ids: set[str] = set()
    for index, relation in enumerate(relations):
        rel_id = relation.get("relation_id")
        if not rel_id or rel_id in relation_ids:
            errors.append(f"relation[{index}] has missing/duplicate relation_id: {rel_id}")
        else:
            relation_ids.add(rel_id)
        if relation.get("predicate") not in ALLOWED_PREDICATES:
            errors.append(f"relation[{index}] has unsupported predicate: {relation.get('predicate')}")
        if relation.get("authority_effect") != "NONE":
            errors.append(f"relation[{index}] authority_effect must be NONE")
        if relation.get("subject") not in document_ids | anchor_ids:
            errors.append(f"relation[{index}] has unknown subject: {relation.get('subject')}")
        if relation.get("object") not in document_ids | anchor_ids:
            errors.append(f"relation[{index}] has unknown object: {relation.get('object')}")
        confidence = relation.get("confidence")
        if not isinstance(confidence, (int, float)) or not 0 <= confidence <= 1:
            errors.append(f"relation[{index}] confidence must be in [0,1]")
        mode = relation.get("assertion_mode")
        state = relation.get("state")
        review = relation.get("review", {})
        if mode == "machine_discovered" and state == "admitted":
            if review.get("review_state") != "accepted" or not review.get("reviewed_by") or not review.get("reviewed_at"):
                errors.append(f"machine-discovered admitted relation {rel_id} requires accepted review evidence")
        if mode == "machine_discovered" and state == "candidate" and review.get("review_state") != "pending":
            errors.append(f"machine-discovered candidate relation {rel_id} must have pending review")
        for ref in relation.get("evidence_refs", []):
            if ref not in anchor_ids:
                errors.append(f"relation {rel_id} has unknown evidence_ref: {ref}")
        provenance = relation.get("provenance", {})
        if not all(provenance.get(k) for k in ("asserted_by", "observed_at", "basis")):
            errors.append(f"relation {rel_id} requires asserted_by, observed_at, and basis")

    if errors:
        print("Published Research Graph validation: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Published Research Graph validation: PASS")
    print(f"documents={len(documents)}")
    print(f"relations={len(relations)}")
    print("machine_discovered_candidate_default=ENFORCED")
    print("authority_effect=NONE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
