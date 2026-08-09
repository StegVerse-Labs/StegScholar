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
    "ecog_surface_read": ["electrocorticography", "ecog", "surface cortical"],
    "endovascular_or_endocisternal": ["endovascular", "stentrode", "endocisternal"],
    "noninvasive_eeg_meg": ["eeg", "meg", "non-invasive", "noninvasive"],
    "fnirs_optical_read": ["fnirs", "nirs", "near infrared", "optical"],
    "functional_ultrasound_read": ["functional ultrasound", "ultrasonic brain-machine", "fus imaging"],
    "focused_ultrasound_write": ["focused ultrasound", "neuromodulation"],
    "tms_tes_write": ["transcranial magnetic", "tms", "transcranial electrical", "tdcs", "tes"],
    "bidirectional_read_write": ["bidirectional", "recording and stimulation", "recording and stimulation"],
    "speech_inner_speech": ["speech", "imagined speech", "inner speech", "language decoding"],
    "calibration_drift_reliability": ["calibration", "drift", "non-stationarity", "long-term", "chronic", "reliability"],
    "safety_regulatory": ["safety", "clinical trial", "feasibility study", "adverse event"],
    "decoder_prior_confound": ["language model", "prior", "confound", "zero signal", "ablation"],
    "reproducible_data": ["dataset", "open-access", "data descriptor"]
}

REJECT_PATTERNS = [
    "peripheral nerve",
    "hypoglossal",
    "subthalamic nucleus",
    "decision letter",
    "book chapter",
    "systematic review",
    "task-oriented review",
    "review of wireless",
    "nerve electrode"
]

SUPPLEMENT_RE = re.compile(r"(?:/mm\d+$|_supp\d*|\.s00\d$)", re.I)


def norm(s: str | None) -> str:
    return " ".join((s or "").lower().split())


def registry_keys(registry: dict) -> tuple[set[str], set[str]]:
    dois: set[str] = set()
    titles: set[str] = set()
    for src in registry.get("sources", []):
        sid = str(src.get("id") or "")
        if sid.startswith("doi:"):
            dois.add(sid[4:].lower())
        titles.add(norm(src.get("title")))
    return dois, titles


def classify(item: dict, seed_dois: set[str], seed_titles: set[str], published_dois: set[str]) -> tuple[str, str]:
    doi = norm(item.get("doi"))
    title = norm(item.get("title"))
    if doi in seed_dois or title in seed_titles:
        return "DUPLICATE", "already present in reviewed seed registry"
    if doi and SUPPLEMENT_RE.search(doi):
        parent = doi.split("/mm", 1)[0].split(".s00", 1)[0]
        if parent in published_dois or parent in seed_dois:
            return "DUPLICATE", "supplementary object for an existing or separately indexed publication"
        return "REJECT_SOURCE", "supplementary object is not an independently reviewable primary source"
    if any(p in title for p in REJECT_PATTERNS):
        return "REJECT_SOURCE", "secondary, peripheral, or non-central neural-interface material for this topic"
    if not title:
        return "RETRY", "missing title metadata"
    if item.get("type") == "posted-content":
        return "ADMIT_SOURCE", "relevant preprint candidate; must be checked for later version of record before registry promotion"
    central = ["brain-computer", "brain computer", "neural interface", "intracortical", "electrocortic", "eeg", "meg", "ultrasound", "stentrode", "brain-machine"]
    if any(k in title for k in central):
        return "ADMIT_SOURCE", "metadata indicates direct relevance; scientific claims still require source-content review"
    return "REJECT_SOURCE", "metadata does not establish direct relevance to the neural BCI evidence topic"


def coverage_for(text: str) -> list[str]:
    out = []
    for key, tokens in COVERAGE.items():
        if any(tok in text for tok in tokens):
            out.append(key)
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--candidates", required=True)
    ap.add_argument("--registry", required=True)
    ap.add_argument("--triage-out", required=True)
    ap.add_argument("--gap-out", required=True)
    args = ap.parse_args()

    candidates = json.loads(Path(args.candidates).read_text(encoding="utf-8"))
    registry = json.loads(Path(args.registry).read_text(encoding="utf-8"))
    seed_dois, seed_titles = registry_keys(registry)
    published_dois = {norm(c.get("doi")) for c in candidates.get("candidates", []) if c.get("doi") and c.get("type") != "posted-content"}

    triaged = []
    counts = Counter()
    coverage_candidates: dict[str, int] = Counter()
    for item in candidates.get("candidates", []):
        state, reason = classify(item, seed_dois, seed_titles, published_dois)
        text = norm((item.get("title") or "") + " " + (item.get("query") or ""))
        coverage = coverage_for(text)
        if state == "ADMIT_SOURCE":
            for key in coverage:
                coverage_candidates[key] += 1
        counts[state] += 1
        triaged.append({
            "doi": item.get("doi"),
            "title": item.get("title"),
            "year": item.get("year"),
            "provider": item.get("provider"),
            "classification": state,
            "reason": reason,
            "coverage_dimensions": coverage,
            "registry_effect": "NONE",
            "authority_effect": "NONE"
        })

    for err in candidates.get("errors", []):
        counts[err.get("state", "RETRY")] += 1

    seed_text = " ".join(norm(json.dumps(s, ensure_ascii=False)) for s in registry.get("sources", []))
    gaps = []
    for key, tokens in COVERAGE.items():
        seed_covered = any(tok in seed_text for tok in tokens)
        candidate_count = coverage_candidates.get(key, 0)
        state = "COVERED_REVIEWED_SEED" if seed_covered else ("CANDIDATE_AVAILABLE" if candidate_count else "GAP")
        gaps.append({
            "dimension": key,
            "state": state,
            "reviewed_seed_support": seed_covered,
            "review_required_candidate_count": candidate_count
        })

    triage_doc = {
        "topic_id": candidates.get("topic_id"),
        "state": "REVIEW_REQUIRED",
        "classification_scope": "metadata relevance and queue routing only",
        "authority_effect": "NONE",
        "registry_effect": "NONE",
        "counts": dict(sorted(counts.items())),
        "provider_errors": candidates.get("errors", []),
        "items": triaged
    }
    gap_doc = {
        "topic_id": candidates.get("topic_id"),
        "state": "ACTIVE_GAP_MAP",
        "authority_effect": "NONE",
        "dimensions": gaps,
        "open_dimensions": [g["dimension"] for g in gaps if g["state"] != "COVERED_REVIEWED_SEED"],
        "registry_known_gaps": registry.get("known_gaps", [])
    }

    Path(args.triage_out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.gap_out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.triage_out).write_text(json.dumps(triage_doc, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    Path(args.gap_out).write_text(json.dumps(gap_doc, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"triage_counts": triage_doc["counts"], "open_dimensions": len(gap_doc["open_dimensions"])}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
