#!/usr/bin/env python3
"""Fail-closed validation for PESOSE Track 1 supporting documents."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "funding/applications/active"
FILES = {
    "application": BASE / "FUNDING-NSF-PESOSE-2026-001.json",
    "summary": BASE / "FUNDING-NSF-PESOSE-2026-001-project-summary.md",
    "description": BASE / "FUNDING-NSF-PESOSE-2026-001-project-description.md",
    "references": BASE / "FUNDING-NSF-PESOSE-2026-001-references-cited.md",
    "letters": BASE / "FUNDING-NSF-PESOSE-2026-001-collaboration-letter-intake.md",
    "supplementary": BASE / "FUNDING-NSF-PESOSE-2026-001-supplementary-documents-control.md",
    "product_evidence": BASE / "FUNDING-NSF-PESOSE-2026-001-product-evidence.md",
    "budget": BASE / "FUNDING-NSF-PESOSE-2026-001-budget-request.json",
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def require_phrases(text: str, phrases: tuple[str, ...], label: str) -> None:
    lowered = text.lower()
    for phrase in phrases:
        require(phrase.lower() in lowered, f"{label} missing required phrase: {phrase}")


def main() -> int:
    missing = [name for name, path in FILES.items() if not path.is_file()]
    require(not missing, f"missing PESOSE supporting files: {', '.join(missing)}")

    app = json.loads(FILES["application"].read_text(encoding="utf-8"))
    budget = json.loads(FILES["budget"].read_text(encoding="utf-8"))
    require(app["state"] == "DRAFTING", "PESOSE application must remain DRAFTING")
    require(app["publication_classification"] == "DISCLOSURE_REVIEW_REQUIRED", "PESOSE disclosure review must remain required")
    require(budget["state"] == "DRAFT_UNAPPROVED", "PESOSE budget request must remain DRAFT_UNAPPROVED")
    require(budget.get("validation", {}).get("authority_approved") is False, "PESOSE budget must not claim authority approval")

    summary_lines = [line.rstrip() for line in FILES["summary"].read_text(encoding="utf-8").splitlines()]
    nonempty_summary = [line for line in summary_lines if line.strip()]
    require(nonempty_summary, "project summary is empty")
    require(nonempty_summary[-1].startswith("Keywords:"), "Project Summary final non-empty line must begin with Keywords:")
    keyword_values = [value.strip() for value in nonempty_summary[-1].removeprefix("Keywords:").split(";") if value.strip()]
    require(2 <= len(keyword_values) <= 5, "Project Summary must contain 2 to 5 semicolon-separated keywords")

    references = FILES["references"].read_text(encoding="utf-8")
    require_phrases(references, (
        "required anchor-product citation",
        "anchor-1 — blocked",
        "governing license: `unverified`",
        "no placeholder url or provisional citation may be copied into a sponsor submission",
        "stegverse-labs/stegcore#47",
        "evidence/pesose-anchor-product.json",
        "citation release gate",
    ), "References Cited")

    product_evidence = FILES["product_evidence"].read_text(encoding="utf-8")
    require_phrases(product_evidence, (
        "public repository: yes",
        "documentation-first",
        "public root license: not found",
        "stegverse-labs/stegcore#47",
        "docs/pesose_anchor_product_evidence_request.md",
        "evidence/pesose-anchor-product.json",
        "proposal must remain `drafting`",
    ), "product evidence")

    letters = FILES["letters"].read_text(encoding="utf-8")
    require_phrases(letters, (
        "minimum three and maximum five letters",
        "current users and/or contributors",
        "stegscholar may not fabricate",
        "| 1 | unverified",
        "| 2 | unverified",
        "| 3 | unverified",
        "release condition",
    ), "collaboration-letter intake")

    supplementary = FILES["supplementary"].read_text(encoding="utf-8")
    require_phrases(supplementary, (
        "nsf 26-506",
        "maximum seven pages",
        "maximum $300,000 for up to one year",
        "no voluntary committed cost sharing",
        "i-corps for pesose",
        "three to five qualifying independent current users/contributors",
        "title decision gate",
        "submission-readiness gate",
    ), "supplementary-document control")

    description = FILES["description"].read_text(encoding="utf-8").lower()
    require("drafting — not submission ready" in description, "Project Description must remain not submission ready")
    require("sponsor submission is prohibited until" in description, "Project Description must preserve submission prohibition")

    receipt = {
        "result": "COMPLETE",
        "application_id": app["application_id"],
        "validated_files": [str(path.relative_to(ROOT)) for path in FILES.values()],
        "application_state": app["state"],
        "summary_keyword_count": len(keyword_values),
        "anchor_product_citation_state": "BLOCKED_PENDING_STEGCORE_ISSUE_47_AND_EVIDENCE_MANIFEST",
        "cross_repository_dependency": "StegVerse-Labs/StegCore#47",
        "collaboration_letter_state": "BLOCKED_PENDING_3_TO_5_QUALIFYING_AUTHORS",
        "title_state": "REVIEW_REQUIRED",
        "budget_state": budget["state"],
        "submission_ready": False,
        "next_executable_task": "stegcore_issue_47_emit_evidence_manifest_or_no_go",
    }
    out = ROOT / "funding/evidence/latest-pesose-support-validation.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(receipt, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
