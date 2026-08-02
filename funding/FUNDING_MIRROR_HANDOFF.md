# StegScholar Funding Mirror Handoff

## Active goal

- **Goal ID:** `FUNDING-PIPELINE-001`
- **Goal:** Establish a governed, machine-verifiable grants and external-funding application process in StegScholar and advance the NSF PESOSE Track 1 application without moving patent authority or financial execution into this repository.
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
- **Eligibility gate:** `funding/applications/active/FUNDING-NSF-PESOSE-2026-001-eligibility.md`
- **Product evidence:** `funding/applications/active/FUNDING-NSF-PESOSE-2026-001-product-evidence.md`
- **Compliance map:** `funding/applications/active/FUNDING-NSF-PESOSE-2026-001-compliance.md`

## Authority boundaries

- StegScholar owns opportunity intake, application narratives, evidence crosswalks, submission state, sponsor requirements, review state, and application receipts.
- StegPatents remains authoritative for protected disclosures, patent status, ownership, licensing posture, and disclosure classification under `funding/contracts/stegpatents-source-contract.md`.
- StegFinCo remains authoritative for approved budgets and financial execution under `funding/contracts/stegfinco-budget-handoff-contract.md`.
- StegOps-Deliverables owns post-award sponsor deliverables after verified award activation under `funding/contracts/stegops-deliverables-consumer-contract.md`.

## Active claims

### Core pipeline

- Task ID: `FUNDING-CORE-001`
- State: `CLAIMED_FOR_IMPLEMENTATION`
- Claimant: repository-native funding lane
- Collision boundary: `funding/**` and `.github/workflows/funding-state-validation.yml`
- Release condition: hosted validator succeeds and run/job/artifact evidence is recorded.

### PESOSE application

- Task ID: `FUNDING-NSF-PESOSE-2026-001`
- State: `CLAIMED_FOR_IMPLEMENTATION`
- Claim expiration: 2026-09-01 at 5:00 p.m. Central time
- Release condition: authorized submission, committed no-go decision, or supersession by a qualified lead applicant.
- Collision boundary: no competing PESOSE application record or unreviewed submission from another StegVerse repository.

## Completed and committed

### Core control surface

1. funding handoff;
2. task and claim registry;
3. application JSON Schema;
4. exemplar application;
5. fail-closed validator;
6. hosted validation workflow;
7. StegPatents source contract;
8. StegFinCo budget handoff contract;
9. StegOps-Deliverables consumer contract.

### Application work

1. broad opportunity scan;
2. canonical PESOSE application record;
3. Track 1 concept narrative;
4. eligibility and submission gate;
5. public-product evidence crosswalk;
6. NSF compliance and seven-page budget map.

## Product evidence finding

`StegVerse-Labs/StegCore` remains the provisional anchor because NSF explicitly encourages PESOSE proposals concerning protocols enabling AI-agent ecosystems. Repository inspection also established material blockers:

- no root `LICENSE` file was found;
- the README describes v0.1 as documentation-first;
- code under `src/stegcore/` is described as scaffolding/substrate;
- users, contributors, dissemination, releases, and three-to-five qualifying collaboration letters are not yet evidenced.

The application must remain `DRAFTING` until these gaps are resolved or a stronger anchor is selected.

## Incomplete work

- `funding/reusable/organization-profile/README.md`;
- `funding/schemas/evidence-crosswalk.schema.json`;
- `funding/schemas/submission-receipt.schema.json`;
- `funding/applications/active/FUNDING-NSF-PESOSE-2026-001-project-summary.md`;
- `funding/applications/active/FUNDING-NSF-PESOSE-2026-001-milestones.md`;
- `funding/applications/active/FUNDING-NSF-PESOSE-2026-001-budget-request.json`;
- application-specific StegPatents review record;
- verified public license and product maturity evidence;
- three to five independent current-user or contributor collaboration letters;
- legal applicant, ownership, PI employment, UEI, SAM.gov, submission-system and AOR evidence;
- hosted workflow run, job, log and artifact inspection.

## Human-authority blockers and release conditions

- Legal applicant and ownership: released by committed formation and ownership/control evidence or a qualified lead applicant record.
- PI employment and work eligibility: released by applicant-held evidence.
- UEI and SAM.gov: released by active registration evidence.
- Submission authority: released by verified Research.gov or Grants.gov organization registration and AOR authority.
- Collaboration letters: released by three to five qualifying independent current users or contributors.

## Validation

Command:

```bash
python funding/tools/validate_funding_state.py
```

No hosted workflow success, artifact, deployment, submission, award, or propagation is claimed until directly inspected.

## Propagation

No propagation is authorized to Site, Publisher, admissibility-wiki, stegguardian-wiki, or master-records before a validated publication or custody classification exists.

## Session consolidation

**MERGED INTO:** `StegVerse-Labs/StegScholar/funding/FUNDING_MIRROR_HANDOFF.md` and `funding/coordination/funding-tasks.json`.

All unique session requirements are now durable: repository choice, opportunity scan, PESOSE selection, application design, eligibility boundaries, product evidence gaps, NSF compliance requirements, and cross-repository authority contracts.

## Completion accounting

Current denominator: 18 required funding and PESOSE deliverables.

- task completion: `12/18 = 67%`;
- developed files: `12/18 = 67%`;
- validation: `2/6 = 33%` (presence and source inspection; hosted execution pending);
- integration: `3/3 = 100%` contracts installed, consumer-side acceptance not yet verified;
- propagation: `0/1 = 0%`;
- goal activation: `48%`;
- session consolidation: `7/7 = 100%`.

## Archive condition

The conversation may be archived because every unique requirement and remaining task is preserved in this handoff and registry with exact owners, locations and release conditions. The funding workstream remains active and repository-owned; archival does not imply application submission readiness.
