# OTF ICRP Mirror Handoff

## Active goal

- Goal ID: `FUNDING-OTF-ICRP-2026-001`
- Goal: prepare a safe, evidence-backed OTF Information Controls Research Program concept note without inventing applicant qualifications or activating field research without review.
- Repository: `StegVerse-Labs/StegScholar`
- Branch: `main`
- Parent handoff: `funding/FUNDING_MIRROR_HANDOFF.md`
- Task registry: `funding/coordination/otf-icrp-tasks.json`

## Active claim

- State: `CLAIMED_FOR_IMPLEMENTATION`
- Owner: StegScholar OTF ICRP lane
- Created: `2026-08-02T15:42:00-05:00`
- Expires: `2026-09-07T23:59:00+00:00`
- Release condition: authorized submission, committed no-go, formal decline, supersession, or deadline.
- Collision boundary: no competing concept note using the same applicant identity and governed-evidence research question.

## Authoritative files

- `FUNDING-OTF-ICRP-2026-001.json`
- `FUNDING-OTF-ICRP-2026-001-concept-note.md`
- `FUNDING-OTF-ICRP-2026-001-eligibility.md`
- `FUNDING-OTF-ICRP-2026-001-ethics-safety-plan.md`
- `FUNDING-OTF-ICRP-2026-001-milestones.md`
- `FUNDING-OTF-ICRP-2026-001-budget-request.json`
- `../../tools/validate_otf_icrp_package.py`

## Completed work

- Concept note installed and previously hosted-validated as part of the expanded portfolio.
- Applicant eligibility and submission gate installed.
- Ethics and safety plan installed with current state `SYNTHETIC_ONLY` and field activity prohibited.
- Six-month milestone and evaluation plan installed.
- Budget request installed with amount unset, state `DRAFT_UNAPPROVED`, and self-approval prohibited.
- Application record updated to bind all support files.
- Dedicated fail-closed validator installed and added to the funding workflow.

## Incomplete work

- Named applicant identity and protected contact record.
- CV/resume and evidence of relevant technical, research, internet-freedom or affected-community experience.
- Work-eligibility, conflict, surveillance-technology, and availability declarations.
- Qualified ethical-review pathway before participant or field work.
- Applicant-specific approved budget.
- Application-specific IP and disclosure classification.
- Final applicant authorization and submission receipt.

## Validation

```bash
python funding/tools/validate_otf_icrp_package.py
python funding/tools/validate_funding_state.py
```

Hosted validation remains required after the current package mutations. Success must include workflow, job, logs or steps, uploaded receipts, artifact ID, and digest.

## Integration and propagation

- Parent portfolio coordination remains in `funding/FUNDING_MIRROR_HANDOFF.md`.
- StegOps-Deliverables activates only after a verified award.
- No Site, Publisher, wiki, or master-records propagation is authorized before submission, award, publication, or custody classification.

## Archive conditions

This session-specific OTF implementation is archive-safe once hosted validation evidence is recorded here and in the task registry. Application submission readiness remains separately blocked by named human authorities.

## Completion accounting

- developed files: `8/8` repository-owned OTF package and control files;
- validation: `1/2` static implementation complete, hosted validation pending;
- integration: `1/4` application binding complete; applicant, ethics, budget and IP authority responses pending;
- goal activation: `60%` toward authorized OTF concept-note submission;
- session consolidation: `1/1` unique OTF continuation path preserved.
