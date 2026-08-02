# StegScholar Funding Mirror Handoff

## Active goal

- **Goal ID:** `FUNDING-PIPELINE-001`
- **Goal:** Establish a governed, machine-verifiable grants and external-funding application process in StegScholar without moving patent authority or financial execution into this repository.
- **Originating session goal:** Determine and implement the best repository environment, other than expanding StegPatents, for grants and other funding applications.
- **Repository:** `StegVerse-Labs/StegScholar`
- **Branch:** `main`
- **Parent authority:** `STEGSCHOLAR_MIRROR_HANDOFF.md`
- **Canonical workstream handoff:** this file
- **Task registry:** `funding/coordination/funding-tasks.json`
- **Application schema:** `funding/schemas/application.schema.json`
- **Validator:** `funding/tools/validate_funding_state.py`
- **Workflow:** `.github/workflows/funding-state-validation.yml`

## Authority boundaries

- StegScholar owns opportunity intake, application narratives, evidence crosswalks, submission state, sponsor requirements, review state, and application receipts.
- StegPatents remains authoritative for invention disclosures, patent status, ownership, licensing posture, and disclosure classification.
- StegFinCo remains authoritative for approved budgets, award accounting, drawdowns, matching funds, expenditure controls, and sponsor financial reporting.
- StegOps-Deliverables is the intended owner of post-award sponsor deliverable packaging and closeout bundles.
- No downstream publication, award, deployment, or funding receipt is claimed by this workstream.

## Canonical ownership and claim

- **Task ID:** `FUNDING-CORE-001`
- **Claim state:** `CLAIMED_FOR_IMPLEMENTATION`
- **Claimant:** `repository-native funding lane`
- **Claim created:** `2026-08-02T04:44:00-05:00`
- **Claim expiration:** when all required core files validate on hosted GitHub Actions, or after 14 days without a new commit touching the claimed surfaces.
- **Collision boundary:** `funding/**` and `.github/workflows/funding-state-validation.yml`.
- **Release condition:** validator passes against the committed registry and exemplar application; hosted workflow conclusion is inspected; this handoff is updated with evidence.

## Required core deliverables

1. workstream handoff;
2. deterministic task and claim registry;
3. application JSON Schema;
4. complete exemplar application record;
5. fail-closed validator;
6. hosted validation workflow;
7. reusable organization profile;
8. evidence crosswalk format;
9. submission receipt format;
10. cross-repository source and consumer contracts.

## Installed in this activation

- this handoff;
- `funding/coordination/funding-tasks.json`;
- `funding/schemas/application.schema.json`;
- `funding/applications/examples/FUNDING-EXAMPLE-001.json`;
- `funding/tools/validate_funding_state.py`;
- `.github/workflows/funding-state-validation.yml`.

## Incomplete work

- `funding/reusable/organization-profile/README.md`;
- `funding/schemas/evidence-crosswalk.schema.json`;
- `funding/schemas/submission-receipt.schema.json`;
- `funding/contracts/stegpatents-source-contract.md`;
- `funding/contracts/stegfinco-budget-handoff-contract.md`;
- `funding/contracts/stegops-deliverables-consumer-contract.md`;
- hosted workflow run, job, log, and artifact inspection;
- downstream propagation decision after a real application reaches submission-ready state.

## Validation command

```bash
python funding/tools/validate_funding_state.py
```

The validator must fail closed for missing required files, malformed registry state, duplicate active claims on the same surface, expired claims, invalid application records, missing evidence references, or unassigned incomplete tasks.

## Cross-repository dependencies

- `StegVerse-Labs/StegPatents`: disclosure-safe IP posture source contract, not yet installed.
- `StegVerse-Labs/StegFinCo`: budget and award-accounting handoff contract, not yet installed.
- `StegVerse-Labs/StegOps-Deliverables`: post-award reporting consumer contract, not yet installed.
- `StegVerse-Labs/Site`, `GCAT-BCAT-Engine/Publisher`, `admissibility-wiki`, `stegguardian-wiki`, and `master-records`: no propagation is authorized until an application or award record has a validated publication classification.

## Session consolidation

**MERGED INTO:** `StegVerse-Labs/StegScholar/funding/FUNDING_MIRROR_HANDOFF.md` and `funding/coordination/funding-tasks.json`.

Transferred requirements:

1. StegScholar is the application and research-evidence authority.
2. StegFinCo is downstream financial execution authority.
3. StegPatents remains the protected IP authority.
4. StegOps-Deliverables is the intended sponsor-deliverables owner.
5. A future standalone StegGrants repository is considered only after multiple concurrent applications justify extraction.

## Completion accounting

Denominator: 10 required core deliverables.

- task completion: `6/10 = 60%` after this activation is committed;
- developed files: `6/10 = 60%`;
- validation: `0/3 = 0%` until static execution and hosted workflow inspection;
- integration: `0/3 = 0%` cross-repository contracts;
- propagation: `0/1 = 0%`;
- goal activation: `35%`;
- session consolidation: `5/5 = 100%` requirements transferred.

## Archive condition

This originating session may be archived when all unique requirements are durable in this handoff and registry, no session-only claim remains, and continuation can proceed from repository state. The funding workstream itself may remain incomplete and machine-owned after session archival.