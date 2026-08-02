# StegScholar Funding Mirror Handoff

## Active goal

- **Goal ID:** `FUNDING-PIPELINE-001`
- **Goal:** Operate a governed, machine-verifiable grants and external-funding application process in StegScholar and advance the NSF PESOSE Track 1 application without moving patent authority or financial execution into this repository.
- **Originating session goals:** identify the best grants repository; search broadly for fitting opportunities; begin the strongest application; preserve and automate continuation.
- **Repository:** `StegVerse-Labs/StegScholar`
- **Branch:** `main`
- **Parent authority:** `STEGSCHOLAR_MIRROR_HANDOFF.md`
- **Canonical workstream handoff:** this file
- **Task registry:** `funding/coordination/funding-tasks.json`

## Canonical application

- **Application ID:** `FUNDING-NSF-PESOSE-2026-001`
- **Opportunity:** NSF 26-506, PESOSE Track 1
- **Deadline:** 2026-09-01 at 5:00 p.m. submitting organization local time
- **State:** `DRAFTING`
- **Application record:** `funding/applications/active/FUNDING-NSF-PESOSE-2026-001.json`
- **Narrative:** `funding/applications/active/FUNDING-NSF-PESOSE-2026-001-concept.md`
- **Project summary:** `funding/applications/active/FUNDING-NSF-PESOSE-2026-001-project-summary.md`
- **Milestones:** `funding/applications/active/FUNDING-NSF-PESOSE-2026-001-milestones.md`
- **Draft budget request:** `funding/applications/active/FUNDING-NSF-PESOSE-2026-001-budget-request.json`
- **Eligibility gate:** `funding/applications/active/FUNDING-NSF-PESOSE-2026-001-eligibility.md`
- **Product evidence:** `funding/applications/active/FUNDING-NSF-PESOSE-2026-001-product-evidence.md`
- **Compliance map:** `funding/applications/active/FUNDING-NSF-PESOSE-2026-001-compliance.md`

## Authority boundaries

- StegScholar owns opportunity intake, application narratives, evidence crosswalks, submission state, sponsor requirements, review state and application receipts.
- StegPatents remains authoritative for protected disclosures, patent status, ownership, licensing posture and disclosure classification under `funding/contracts/stegpatents-source-contract.md`.
- StegFinCo remains authoritative for approved budgets and financial execution under `funding/contracts/stegfinco-budget-handoff-contract.md`.
- StegOps-Deliverables owns post-award sponsor deliverables after verified award activation under `funding/contracts/stegops-deliverables-consumer-contract.md`.

## Active claims

### Core pipeline validation

- Task ID: `FUNDING-CORE-001`
- State: `CLAIMED_FOR_VALIDATION`
- Claimant: repository-native funding lane
- Collision boundary: `funding/**` and `.github/workflows/funding-state-validation.yml`
- Claim expiration: 2026-08-16 at 04:44 Central time
- Release condition: hosted validator succeeds and run, job, log and artifact evidence is recorded.

### PESOSE application implementation

- Task ID: `FUNDING-NSF-PESOSE-2026-001`
- State: `CLAIMED_FOR_IMPLEMENTATION`
- Claim expiration: 2026-09-01 at 5:00 p.m. Central time
- Release condition: authorized submission, committed no-go decision or supersession by a qualified lead applicant.
- Collision boundary: no competing PESOSE application record or unreviewed submission from another StegVerse repository.

## Complete and committed core package

The original ten-item pipeline denominator is complete at the developed-file level:

1. funding handoff;
2. task and claim registry;
3. application JSON Schema;
4. complete exemplar application;
5. fail-closed validator;
6. hosted validation workflow;
7. reusable organization profile;
8. evidence crosswalk schema;
9. submission receipt schema;
10. cross-repository source and consumer contracts.

The validator now checks the live PESOSE application, all schemas, required contracts, source documents, active claims and provisional budget arithmetic. It prevents `SUBMISSION_READY` when the budget is not approved or disclosure review remains required.

## Application work completed

1. broad opportunity scan;
2. canonical PESOSE application record;
3. Track 1 concept narrative;
4. eligibility and submission gate;
5. public-product evidence crosswalk;
6. NSF compliance and seven-page map;
7. project summary draft;
8. milestone and evaluation plan;
9. provisional budget request capped at USD 300,000 and explicitly unapproved.

## Product evidence finding

`StegVerse-Labs/StegCore` remains the provisional anchor. Repository inspection established material blockers:

- no root `LICENSE` file was found during inspection;
- the README describes v0.1 as documentation-first;
- code under `src/stegcore/` is described as scaffolding or substrate;
- users, contributors, dissemination, releases and three-to-five qualifying collaboration letters are not evidenced.

The application must remain `DRAFTING` until these gaps are resolved or a stronger licensed anchor is selected.

## Exact incomplete tasks and release conditions

### Hosted validation

- Owner: `StegVerse-Labs/StegScholar`
- Location: `.github/workflows/funding-state-validation.yml`
- State: `CLAIMED_FOR_VALIDATION`
- Current observation: no combined commit status was present for validator commit `dfa9a0f531d2dfbcb3fc76892444bf969c38a5ed` when inspected.
- Release condition: successful hosted run, inspected job/logs and artifact digest recorded here.

### Human applicant and submission gates

- Owner: human corporate and applicant-registration authority
- Location: `funding/applications/active/FUNDING-NSF-PESOSE-2026-001-eligibility.md`
- State: `BLOCKED`
- Release condition: committed or referenced legal entity, ownership/control, PI employment, work eligibility, UEI, active SAM.gov, submission-system and AOR evidence.

### Product and adoption evidence

- Owner: StegCore maintainers and StegScholar funding lane
- Location: `funding/applications/active/FUNDING-NSF-PESOSE-2026-001-product-evidence.md`
- State: `BLOCKED`
- Release condition: governing open-source license, precise implemented product boundary, development/testing/dissemination evidence and three to five qualifying independent user or contributor letters.

### IP and budget authority responses

- Owners: `StegVerse-Labs/StegPatents` and `StegVerse-Labs/StegFinCo`
- Locations: `funding/contracts/` and `funding/applications/active/FUNDING-NSF-PESOSE-2026-001-budget-request.json`
- State: `BLOCKED`
- Release condition: application-specific disclosure classification and an approved compliant line-item budget and justification.

### Remaining narrative package

- Owner: StegScholar funding lane
- Location: `funding/applications/active/FUNDING-NSF-PESOSE-2026-001-concept.md`
- State: `CLAIMED_FOR_IMPLEMENTATION`
- Next action: expand the installed concept, summary, milestones and evidence maps into the final solicitation-limited Project Description and supporting documents without inventing eligibility, adoption or maturity evidence.

## Validation

Command:

```bash
python funding/tools/validate_funding_state.py
```

Validation levels currently established:

- file presence: verified through successful repository writes and subsequent reads for authoritative files;
- JSON source validity: designed into the validator but hosted execution remains unproven;
- static source inspection: complete for the validator, application, schemas, contracts, summary, milestones and budget request;
- hosted workflow, job, logs and artifact: pending;
- submission, award, deployment or governed activation: not claimed.

## Propagation

No propagation is authorized to Site, Publisher, admissibility-wiki, stegguardian-wiki or master-records before a validated publication, submission, award or custody classification exists.

## Session consolidation

**MERGED INTO:** `StegVerse-Labs/StegScholar/funding/FUNDING_MIRROR_HANDOFF.md` and `funding/coordination/funding-tasks.json`.

Transferred session goals and requirements:

1. StegScholar selected as canonical application and evidence authority.
2. Broad current funding scan and PESOSE selection.
3. Canonical application, narrative, eligibility, compliance, evidence, summary, milestones and budget-draft records.
4. Separation of StegPatents, StegFinCo and StegOps-Deliverables authorities.
5. Reusable organization profile and machine-readable schemas.
6. Fail-closed validator and hosted workflow.
7. Exact human, product, validation, IP and budget blockers with release conditions.

No unique implementation knowledge remains only in the conversation.

## Completion accounting

Current denominator: 20 developed funding-control and PESOSE application files or deliverables.

- task completion: `16/20 = 80%`;
- developed files: `20/20 = 100%` for the current repository-owned package;
- validation: `3/6 = 50%` (presence, source inspection and deterministic validation design; hosted execution, artifacts and authority-response validation pending);
- integration: `3/6 = 50%` (contracts installed; producer/consumer responses pending);
- propagation: `0/1 = 0%` because no propagation is yet authorized;
- goal activation: `58%` toward authorized PESOSE submission;
- session consolidation: `7/7 = 100%`.

## Archive condition

The conversation is archive-ready because all session-specific goals, decisions, implementation history, current claims, exact blockers and next executable actions are durable in this handoff and registry. Archival does not imply that the PESOSE application is submission-ready; repository-native and named human-authority work remains active.
