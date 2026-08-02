# OTF ICRP 2026 Milestones and Evaluation Plan

Application ID: `FUNDING-OTF-ICRP-2026-001`

Planning state: `DRAFT_UNAPPROVED`

## Proposed six-month structure

### Month 1 — Research framing and threat model

- Confirm applicant and ethical-review pathway.
- Finalize research questions and evidence vocabulary.
- Define synthetic scenarios and prohibited data fields.
- Deliverable: threat model, protocol draft, and go/no-go review.

### Month 2 — Synthetic environment and baseline dataset

- Build controlled interference scenarios.
- Generate synthetic records for shutdown, filtering, throttling, DNS manipulation, route disruption, integrity failure, and ordinary outage cases.
- Deliverable: reproducible synthetic dataset and scenario manifest.

### Month 3 — Evidence schema and verifier

- Implement minimal evidence schema.
- Implement deterministic checks for provenance, consent state, prohibited fields, retention class, and classification support.
- Deliverable: prototype schema and verifier.

### Month 4 — Privacy and classification evaluation

- Measure false-positive and false-negative behavior.
- Test content leakage, linkability, location inference, relationship inference, and persistent-identifier risk.
- Deliverable: evaluation report and schema revisions.

### Month 5 — Independent practitioner review

- Conduct structured review with qualified internet-freedom and digital-security practitioners.
- No vulnerable-user field testing is authorized by this milestone.
- Deliverable: review record, unresolved-risk register, and field-readiness decision.

### Month 6 — Reproducibility and dissemination package

- Publish approved synthetic artifacts, documentation, and verifier materials.
- Separate public, restricted, and withheld findings through disclosure review.
- Deliverable: final report, practitioner guide, reproducibility package, and follow-on recommendation.

## Evaluation measures

- Classification accuracy across controlled scenarios.
- Number and severity of prohibited or unnecessary fields identified and removed.
- Re-identification and linkability findings.
- Reproducibility by an independent reviewer.
- Percentage of claims traceable to observed evidence and explicit uncertainty.
- Practitioner assessment of usefulness and safety.
- Compliance with synthetic-only and stop-work controls.

## Stop conditions

Work pauses and enters `STOP_WORK` if testing reveals uncontrolled collection, participant or partner risk, unauthorized third-party interaction, disclosure of sensitive operational details, or inability to support a claimed classification.
