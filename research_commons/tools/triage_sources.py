#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path

COVERAGE = {
    "intracortical_wired_read": ["intracortical", "wired", "speech", "motor cortex"],
    "intracortical_wireless_read": ["wireless", "intracortical", "implant"],
    "ecog_surface_read": ["electrocorticography", "ecog", "surface cortical", "microecog"],
    "endovascular_or_endocisternal": ["endovascular", "stentrode", "endocisternal"],
    "noninvasive_eeg_meg": ["eeg", "meg", "non-invasive", "noninvasive"],
    "fnirs_optical_read": ["fnirs", "nirs", "near infrared", "optical"],
    "functional_ultrasound_read": ["functional ultrasound", "ultrasonic brain-machine", "fus imaging"],
    "focused_ultrasound_write": ["focused ultrasound", "neuromodulation"],
    "tms_tes_write": ["transcranial magnetic", "tms", "transcranial electrical", "tdcs", "tes"],
    "bidirectional_read_write": ["bidirectional", "recording and stimulation", "read", "write"],
    "speech_inner_speech": ["speech", "imagined speech", "inner speech", "language decoding"],
    "calibration_drift_reliability": ["calibration", "drift", "non-stationarity", "long-term", "chronic", "reliability", "multi-session"],
    "safety_regulatory": ["safety", "clinical trial", "feasibility study", "adverse event", "first-in-human"],
    "decoder_prior_confound": ["language model", "prior", "confound", "zero signal", "ablation"],
    "reproducible_data": ["dataset", "open-access", "data descriptor", "reproducible"]
}

REJECT_PATTERNS = [
    "peripheral nerve", "hypoglossal", "subthalamic nucleus", "decision letter",
    "book chapter", "systematic review", "task-oriented review", "review of wireless", "nerve electrode"
]
SUPPLEMENT_RE = re.compile(r"(?:/mm\d+$|_supp\d*|\.s00\d$)", re.I)


def norm(s: str | None) -> str:
    return " ".join((s or "").lower().split())


def all_reviewed_sources(registry: dict, additions: dict | None) -> list[dict]:
    out = list(registry.get("sources", []))
    if additions:
        out.extend(additions.get("sources", []))
    return out


def registry_keys(sources: list[dict]) -> tuple[set[str], set[str]]:
    dois, titles = set(), set()
    for src in sources:
        sid = str(src.get("id") or "")
        if sid.startswith("doi:"):
            dois.add(sid[4:].lower())
        titles.add(norm(src.get("title")))
    return dois, titles


def classify(item: dict, reviewed_dois: set[str], reviewed_titles: set[str], published_dois: set[str]) -> tuple[str, str]:
    doi, title = norm(item.get("doi")), norm(item.get("title"))
    if doi in reviewed_dois or title in reviewed_titles:
        return "DUPLICATE", "already present in reviewed source set"
    if doi and SUPPLEMENT_RE.search(doi):
        parent = doi.split("/mm", 1)[0].split(".s00", 1)[0]
        if parent in published_dois or parent in reviewed_dois:
            return "DUPLICATE", "supplementary object for an existing or separately indexed publication"
        return "REJECT_SOURCE", "supplementary object is not an independently reviewable primary source"
    if any(p in title for p in REJECT_PATTERNS):
        return "REJECT_SOURCE", "secondary, peripheral, or non-central material for this topic"
    if not title:
        return "RETRY", "missing title metadata"
    if item.get("type") == "posted-content":
        return "ADMIT_SOURCE", "relevant preprint candidate; check for later version of record before registry promotion"
    central = ["brain-computer", "brain computer", "neural interface", "intracortical", "electrocortic", "eeg", "meg", "ultrasound", "stentrode", "brain-machine"]
    if any(k in title for k in central):
        return "ADMIT_SOURCE", "metadata indicates direct relevance; scientific claims still require source-content review"
    return "REJECT_SOURCE", "metadata does not establish direct relevance to the neural BCI evidence topic"


def coverage_for(text: str) -> list[str]:
    return [key for key, tokens in COVERAGE.items() if any(tok in text for tok in tokens)]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--candidates", required=True)
    ap.add_argument("--registry", required=True)
    ap.add_argument("--reviewed-additions")
    ap.add_argument("--triage-out", required=True)
    ap.add_argument("--gap-out", required=True)
    args = ap.parse_args()

    candidates = json.loads(Path(args.candidates).read_text(encoding="utf-8"))
    registry = json.loads(Path(args.registry).read_text(encoding="utf-8"))
    additions = json.loads(Path(args.reviewed_additions).read_text(encoding="utf-8")) if args.reviewed_additions else None
    reviewed = all_reviewed_sources(registry, additions)
    reviewed_dois, reviewed_titles = registry_keys(reviewed)
    published_dois = {norm(c.get("doi")) for c in candidates.get("candidates", []) if c.get("doi") and c.get("type") != "posted-content"}

    triaged, counts = [], Counter()
    coverage_candidates: dict[str, int] = Counter()
    for item in candidates.get("candidates", []):
        state, reason = classify(item, reviewed_dois, reviewed_titles, published_dois)
        text = norm((item.get("title") or "") + " " + (item.get("query") or ""))
        coverage = coverage_for(text)
        if state == "ADMIT_SOURCE":
            for key in coverage:
                coverage_candidates[key] += 1
        counts[state] += 1
        triaged.append({
            "doi": item.get("doi"), "title": item.get("title"), "year": item.get("year"),
            "provider": item.get("provider"), "classification": state, "reason": reason,
            "coverage_dimensions": coverage, "registry_effect": "NONE", "authority_effect": "NONE"
        })
    for err in candidates.get("errors", []):
        counts[err.get("state", "RETRY")] += 1

    reviewed_text = " ".join(norm(json.dumps(s, ensure_ascii=False)) for s in reviewed)
    dimensions = []
    for key, tokens in COVERAGE.items():
        covered = any(tok in reviewed_text for tok in tokens)
        candidate_count = coverage_candidates.get(key, 0)
        state = "COVERED_REVIEWED" if covered else ("CANDIDATE_AVAILABLE" if candidate_count else "GAP")
        dimensions.append({"dimension": key, "state": state, "reviewed_support": covered, "review_required_candidate_count": candidate_count})

    known_gaps = registry.get("known_gaps", [])
    dispositions = (additions or {}).get("gap_disposition", {})
    named_gap_state = [{"gap": gap, "state": dispositions.get(gap, "OPEN")} for gap in known_gaps]
    open_required = [g for g in named_gap_state if g["state"] != "COVERED"]

    triage_doc = {
        "topic_id": candidates.get("topic_id"), "state": "REVIEW_REQUIRED",
        "classification_scope": "metadata relevance and queue routing only",
        "authority_effect": "NONE", "registry_effect": "NONE",
        "counts": dict(sorted(counts.items())), "provider_errors": candidates.get("errors", []), "items": triaged
    }
    gap_doc = {
        "topic_id": candidates.get("topic_id"), "state": "ACTIVE_GAP_MAP", "authority_effect": "NONE",
        "reviewed_source_count": len(reviewed),
        "coarse_coverage_dimensions": dimensions,
        "named_gap_state": named_gap_state,
        "open_required_gaps": open_required,
        "open_required_gap_count": len(open_required)
    }
    Path(args.triage_out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.gap_out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.triage_out).write_text(json.dumps(triage_doc, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    Path(args.gap_out).write_text(json.dumps(gap_doc, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"triage_counts": triage_doc["counts"], "reviewed_sources": len(reviewed), "open_required_gaps": len(open_required)}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
