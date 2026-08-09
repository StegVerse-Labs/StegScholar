#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

GAP_DIMENSIONS = {
    "systematic clinical-trial registry mapping for implantable BCIs": ["safety_regulatory", "intracortical_wireless_read", "endovascular_or_endocisternal"],
    "primary-source regulatory and safety evidence by modality": ["safety_regulatory"],
    "TMS/tES WRITE evidence mapped to StegNeuro envelope fields": ["tms_tes_write", "bidirectional_read_write"],
    "wireless fully implanted human BCI architecture": ["intracortical_wireless_read", "endovascular_or_endocisternal"],
    "decoder-prior/confabulation studies with explicit zero-signal or prior-ablation controls": ["decoder_prior_confound", "speech_inner_speech"],
    "direct comparison of READ and WRITE spatial/temporal resolution across modalities": ["bidirectional_read_write", "ecog_surface_read", "noninvasive_eeg_meg", "functional_ultrasound_read", "focused_ultrasound_write", "tms_tes_write"],
    "device-specific calibration drift and chronic reliability datasets": ["calibration_drift_reliability", "reproducible_data"],
    "patent landscape crosswalk": [],
}


def load(path: str) -> dict:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def norm(s: str) -> str:
    return " ".join((s or "").lower().split())


def select_candidates(triage: dict, dimensions: list[str], limit: int = 8) -> list[dict]:
    items = []
    for item in triage.get("items", []):
        if item.get("classification") != "ADMIT_SOURCE":
            continue
        coverage = set(item.get("coverage_dimensions") or [])
        if dimensions and not coverage.intersection(dimensions):
            continue
        items.append({
            "doi": item.get("doi"),
            "title": item.get("title"),
            "year": item.get("year"),
            "provider": item.get("provider"),
            "coverage_dimensions": sorted(coverage),
            "state": "REVIEW_REQUIRED",
            "authority_effect": "NONE",
        })
    items.sort(key=lambda x: (-(x.get("year") or 0), norm(x.get("title") or "")))
    return items[:limit]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--triage", required=True)
    ap.add_argument("--gap-map", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    triage = load(args.triage)
    gap_map = load(args.gap_map)
    open_gaps = gap_map.get("open_required_gaps", [])

    queue = []
    for gap in open_gaps:
        gap_name = gap.get("gap", "")
        dimensions = GAP_DIMENSIONS.get(gap_name, [])
        queue.append({
            "gap": gap_name,
            "gap_state": gap.get("state", "OPEN"),
            "candidate_dimensions": dimensions,
            "candidate_review_queue": select_candidates(triage, dimensions),
            "next_action": (
                "REVIEW_SOURCE_CONTENT" if dimensions else "SPECIALIZED_PROVIDER_OR_PATENT_SEARCH_REQUIRED"
            ),
            "machine_boundary": "metadata may prioritize candidates but may not promote scientific claims",
        })

    counts = triage.get("counts", {})
    receipt = {
        "schema": "stegscholar.continuation-state.v1",
        "topic_id": gap_map.get("topic_id"),
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "state": "REVIEW_REQUIRED" if open_gaps else "COMPLETE",
        "owner": "StegVerse-Labs/StegScholar#50",
        "observer": ".github/workflows/stegneuro-bci-source-discovery.yml",
        "authority_effect": "NONE",
        "registry_effect": "NONE",
        "reviewed_source_count": gap_map.get("reviewed_source_count", 0),
        "open_required_gap_count": len(open_gaps),
        "triage_counts": counts,
        "provider_error_count": len(triage.get("provider_errors", [])),
        "queues": queue,
        "next_executable_task": (
            "review highest-priority source-content queue for named evidence gaps"
            if open_gaps else
            "reconcile consumers and close successor issue"
        ),
        "release_condition": "every named gap COVERED or durably BLOCKED/NOT_APPLICABLE with reviewed evidence",
    }

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(receipt, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({
        "state": receipt["state"],
        "open_required_gap_count": receipt["open_required_gap_count"],
        "queued_gap_count": len(queue),
    }))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
