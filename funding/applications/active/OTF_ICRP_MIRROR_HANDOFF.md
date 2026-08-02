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
- `../../coordination/otf-icrp-tasks.json`

## Completed implementation

- Concept note and application record installed.
- Applicant eligibility and submission gate installed.
- Ethics and safety plan installed with current state `SYNTHETIC_ONLY`; field activity prohibited.
- Six-month milestone and evaluation plan installed.
- Budget request installed with amount unset, state `DRAFT_UNAPPROVED`, and self-approval prohibited.
- Dedicated fail-closed validator installed and integrated into `.github/workflows/funding-state-validation.yml`.
- Initial hosted run `30768922744`, job `91552517780`, exposed a validator marker mismatch after the global validator passed. No artifact was uploaded.
- Validator corrected on main in commit `5798c82d307529dc63301b9f119262a9c6603897` and on validation branch in commit `df2928ce80a205819a73d634f981d8ab87ec57b7`.

## Hosted validation evidence

- PR: `#44`
- Branch: `funding/validate-otf-package-20260802`
- Successful run: `30768955549`
- Job: `91552600642`
- Global funding validator: `success`
- OTF ICRP package validator: `success`
- Artifact upload: `success`
- Artifact: `8839878425`, `funding-state-validation`
- Size: `1219` bytes
- Digest: `sha256:665373a7572586b48ae3a2b7b57c9f1c62088bbf09c04d0438f555a4ac7795fb`
- Expiration: `2026-10-31T21:55:30Z`

This proves file presence, application binding, fail-closed applicant and disclosure states, unapproved budget state, synthetic-only field controls, milestone markers, workflow execution, and dual-receipt artifact creation. It does not prove applicant identity, qualifications, ethical approval, budget approval, IP clearance, submission, or award.

## Incomplete tasks

- Named applicant identity and protected contact record.
- CV/resume and evidence of relevant technical, research, internet-freedom or affected-community experience.
- Work-eligibility, conflict, surveillance-technology, and availability declarations.
- Qualified ethical-review pathway before participant or field work.
- Applicant-specific approved budget.
- Application-specific IP and disclosure classification.
- Final applicant authorization and submission receipt.

## Validation commands

```bash
python funding/tools/validate_otf_icrp_package.py
python funding/tools/validate_funding_state.py
```

## Integration and propagation

- Parent portfolio coordination remains in `funding/FUNDING_MIRROR_HANDOFF.md`.
- StegOps-Deliverables activates only after a verified award.
- No Site, Publisher, wiki, or master-records propagation is authorized before submission, award, publication, or custody classification.

## Session consolidation

MERGED INTO:

- this handoff;
- `funding/coordination/otf-icrp-tasks.json`;
- the six authoritative OTF application files;
- the dedicated validator and hosted artifact evidence above.

## Completion accounting

- developed files: `9/9` repository-owned OTF package and control files;
- validation: `2/2` static and hosted validation complete;
- integration: `1/4` application binding complete; applicant, ethics, budget and IP authority responses pending;
- goal activation: `68%` toward authorized OTF concept-note submission;
- session consolidation: `1/1` unique OTF continuation path preserved.

## Archive condition

This session-specific implementation is archive-ready because every remaining task is durably assigned with a release condition. Application submission remains blocked by named human authority evidence.
