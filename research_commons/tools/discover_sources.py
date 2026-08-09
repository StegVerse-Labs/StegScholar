#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

USER_AGENT = "StegScholar-ResearchCommons/1.0 (https://github.com/StegVerse-Labs/StegScholar)"


def fetch_crossref(query: str, rows: int) -> list[dict]:
    params = urllib.parse.urlencode({"query.bibliographic": query, "rows": rows, "select": "DOI,title,author,published,container-title,URL,type"})
    url = f"https://api.crossref.org/works?{params}"
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as response:
        payload = json.load(response)
    out = []
    for item in payload.get("message", {}).get("items", []):
        doi = (item.get("DOI") or "").lower().strip()
        title = (item.get("title") or [""])[0]
        authors = []
        for author in item.get("author", []):
            name = " ".join(part for part in [author.get("given", ""), author.get("family", "")] if part).strip()
            if name:
                authors.append(name)
        date_parts = ((item.get("published") or {}).get("date-parts") or [[]])[0]
        year = date_parts[0] if date_parts else None
        out.append({
            "provider": "crossref",
            "query": query,
            "doi": doi or None,
            "title": title,
            "authors": authors,
            "year": year,
            "container": (item.get("container-title") or [None])[0],
            "type": item.get("type"),
            "url": item.get("URL"),
            "candidate_state": "REVIEW_REQUIRED",
            "authority_effect": "NONE"
        })
    return out


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--plan", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()

    plan = json.loads(Path(args.plan).read_text(encoding="utf-8"))
    rows = int(plan.get("max_results_per_query", 20))
    candidates: list[dict] = []
    errors: list[dict] = []
    for query in plan.get("queries", []):
        try:
            candidates.extend(fetch_crossref(query, rows))
        except Exception as exc:
            errors.append({"provider": "crossref", "query": query, "error": str(exc), "state": "RETRY"})

    deduped: dict[str, dict] = {}
    for item in candidates:
        key = item.get("doi") or f"title:{item.get('title','').strip().lower()}"
        if key not in deduped:
            deduped[key] = item

    result = {
        "topic_id": plan.get("topic_id"),
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "state": "REVIEW_REQUIRED" if deduped else ("RETRY" if errors else "COMPLETE"),
        "authority_effect": "NONE",
        "auto_merge_into_registry": False,
        "candidate_count": len(deduped),
        "error_count": len(errors),
        "errors": errors,
        "candidates": sorted(deduped.values(), key=lambda x: ((x.get("year") or 0), x.get("title") or ""), reverse=True)
    }
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out).write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"state": result["state"], "candidate_count": result["candidate_count"], "error_count": result["error_count"]}))
    return 0 if deduped else 2


if __name__ == "__main__":
    raise SystemExit(main())
