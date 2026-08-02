#!/usr/bin/env python3
"""Fail-closed validation for the OTF ICRP support package."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "funding/applications/active"
FILES = {
    "application": BASE / "FUNDING-OTF-ICRP-2026-001.json",
    "concept": BASE / "FUNDING-OTF-ICRP-2026-001-concept-note.md",
    "eligibility": BASE / "FUNDING-OTF-ICRP-2026-001-eligibility.md",
    "ethics": BASE / "FUNDING-OTF-ICRP-2026-001-ethics-safety-plan.md",
    "milestones": BASE / "FUNDING-OTF-ICRP-2026-001-milestones.md",
    "budget": BASE / "FUNDING-OTF-ICRP-2026-001-budget-request.json",
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def main() -> int:
    missing = [name for name, path in FILES.items() if not path.is_file()]
    require(not missing, f"missing OTF files: {', '.join(missing)}")

    app = json.loads(FILES["application"].read_text())
    budget = json.loads(FILES["budget"].read_text())
    require(app["state"] == "DRAFTING", "OTF application must remain DRAFTING")
    require(app["applicant"]["organization"] == "UNVERIFIED_OR_INDIVIDUAL_APPLICANT", "applicant must remain unverified")
    require(app["publication_classification"] == "DISCLOSURE_REVIEW_REQUIRED", "disclosure review must remain required")
    require(app["budget"]["status"] == "DRAFT_UNAPPROVED", "application budget must be unapproved")
    require(budget["state"] == "DRAFT_UNAPPROVED", "budget request must be unapproved")
    require(budget["authority"]["approval_state"] == "NOT_APPROVED", "budget authority must not be approved")
    require(budget["authority"]["self_approval_prohibited"] is True, "budget self-approval must be prohibited")
    require(budget["requested_amount"] is None, "requested amount must remain unset until authority review")

    eligibility = FILES["eligibility"].read_text().lower()
    ethics = FILES["ethics"].read_text().lower()
    milestones = FILES["milestones"].read_text().lower()
    concept = FILES["concept"].read_text().lower()

    for phrase in ("not submission ready", "fail-closed rule", "named individual applicant", "submission authority"):
        require(phrase in eligibility, f"eligibility gate missing: {phrase}")
    for phrase in ("field activity prohibited", "synthetic_only", "no message-content collection", "stop_work"):
        require(phrase in ethics, f"ethics plan missing: {phrase}")
    for phrase in ("month 1", "month 6", "evaluation measures", "stop conditions"):
        require(phrase in milestones, f"milestones missing: {phrase}")
    for phrase in ("no collection of message content", "synthetic and controlled data first", "submission prohibition"):
        require(phrase in concept, f"concept note missing: {phrase}")

    receipt = {
        "result": "COMPLETE",
        "application_id": app["application_id"],
        "validated_files": [str(path.relative_to(ROOT)) for path in FILES.values()],
        "application_state": app["state"],
        "budget_state": budget["state"],
        "field_activity_state": "SYNTHETIC_ONLY",
        "submission_ready": False,
        "next_executable_task": "resolve_named_applicant_and_authority_gates",
    }
    out = ROOT / "funding/evidence/latest-otf-icrp-validation.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps(receipt, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
