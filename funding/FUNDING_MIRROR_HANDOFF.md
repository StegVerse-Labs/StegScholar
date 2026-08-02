# StegScholar Funding Mirror Handoff

## Active goal

- Goal ID: `FUNDING-PIPELINE-001`
- Goal: operate a governed, machine-verifiable StegVerse funding portfolio, advance the NSF PESOSE Track 1 application, and maintain additional noncompeting high-fit funding lanes without moving applicant, IP, budget, institutional, ethical-review, or sponsor-submission authority into StegScholar.
- Originating goals: select the canonical grants repository; search broadly; begin strong applications; automate validation; integrate authority repositories; broaden the search; consolidate continuation.
- Repository: `StegVerse-Labs/StegScholar`
- Branch: `main`
- Parent authority: `STEGSCHOLAR_MIRROR_HANDOFF.md`
- Task registry: `funding/coordination/funding-tasks.json`

## Canonical portfolio

### NSF PESOSE Track 1

- Application ID: `FUNDING-NSF-PESOSE-2026-001`
- Deadline: `2026-09-01T17:00:00-05:00`
- State: `CLAIMED_FOR_IMPLEMENTATION`
- Canonical narrative: `funding/applications/active/FUNDING-NSF-PESOSE-2026-001-project-description.md`
- Release condition: authorized submission, committed no-go, qualified-lead supersession, or deadline.

### OTF Information Controls Research Program

- Application ID: `FUNDING-OTF-ICRP-2026-001`
- Deadline: `2026-09-07T23:59:00+00:00`
- State: `CLAIMED_FOR_IMPLEMENTATION`
- Record: `funding/applications/active/FUNDING-OTF-ICRP-2026-001.json`
- Concept note: `funding/applications/active/FUNDING-OTF-ICRP-2026-001-concept-note.md`
- Research focus: privacy-preserving evidence for shutdown-resilient and censored communications.
- Release condition: eligible individual submission, committed no-go, formal decline, or supersession.

### NSF SBIR/STTR

- Candidate ID: `FUNDING-NSF-SBIR-2026-001`
- State: `BLOCKED — ELIGIBILITY REVIEW`
- Assessment: `funding/applications/candidates/FUNDING-NSF-SBIR-2026-001-assessment.md`
- Consolidated topics: Artificial Intelligence and Cybersecurity and Authentication.
- Release condition: qualifying U.S. small business, ownership, PI employment, product-rights and candidate-selection evidence.

### Academic-partner candidates

SaTC 2.0, Future Computing Research, Mathematical Foundations of Artificial Intelligence, EDU Core Research, CyberTraining and Cybersecurity Innovation for Cyberinfrastructure remain partner-led candidates. No application may open until an eligible lead institution, qualifying PI appointment and project-specific interest are recorded.

Canonical scan: `funding/opportunities/2026-08-02-expanded-scan.md`.

## Authority boundaries

- StegScholar owns opportunity intake, drafting, evidence maps, sponsor requirements, application state and submission receipts.
- StegFinCo owns authoritative budget review and financial execution where its contract applies.
- Protected-disclosure authority remains blocked at `funding/dependencies/stegpatents-authority-gap.md` until a canonical repository or named human IP authority issues a classification.
- Human corporate authority owns legal applicant, ownership/control, employment, registrations and submission authority.
- Academic institutions own institutional eligibility and appointment authority for partner-led applications.
- The eventual OTF individual applicant owns identity, CV, experience, availability, work authorization and certifications; a host organization is deferred until a Stage 2 invitation.
- StegOps-Deliverables activates only after a verified award.

## Completed implementation

Expanded portfolio artifacts:

- `funding/opportunities/2026-08-02-expanded-scan.md` — commit `23df9ba41f32044c6256dffaa8cc040e69e102a0`;
- OTF application record — commit `b36078d3ddd24e8e255629b96e299abe8575ae7b`;
- OTF concept note — commit `772f04511f9b3c7949556d7b2ff2c8c0905f02a7`;
- NSF SBIR assessment — commit `21606e16600ee35f97c62a4516c67b477e6b8fa2`;
- sponsor-aware validator — commit `b3aac7f5cd2cc01b74bbfde9d254c65c5478bc61`;
- initial portfolio registry — commit `7fae04217ae791d2385547c3d64d56a3daad9090`;
- installation receipt — `funding/evidence/expanded-scan-installation.json`;
- hosted-evidence receipt commit `f98d717a56513aa77dbffacae7c63bf7e032d2c5`;
- validated registry commit `280cfe2a2fcdfc30711c7573646ebcc561926f88`.

The OTF concept note includes a defined research problem, measurable questions, controlled methods, privacy and safety evaluation, technical outputs, internet-freedom relevance, ethical safeguards, applicant/host posture, evidence gaps and fail-closed submission language.

## Hosted validation evidence

Expanded portfolio validation:

- validation PR: `#43`;
- branch: `funding/validate-expanded-portfolio-20260802`;
- request commit: `b87fc50b5b87932f8bef22678126e86c15b13174`;
- workflow: `Funding State Validation`;
- run: `30766410128`;
- job: `91545822782`;
- conclusion: `success`;
- validator step: `success`;
- artifact upload: `success`;
- artifact: `8839077504`, `funding-state-validation`;
- size: `750` bytes;
- digest: `sha256:1df59bcdaa14cba17947629fcf60252e56a1872dd6eca0ad8db12fa71f0e2b10`;
- expiration: `2026-10-31T20:47:33Z`.

This proves both active application records, sponsor-specific authority controls, the OTF safety markers, the expanded scan, the SBIR assessment, the PESOSE budget, claims, evidence references and Project Description satisfy the committed validator. It does not prove applicant eligibility, ethical approval, product maturity, IP clearance, approved budgets, partner commitment, sponsor acceptance or submission.

Prior validated paths remain:

- PESOSE Project Description run `30758261196`, job `91524128700`, artifact `8836617427`;
- StegFinCo budget-intake run `30749323611`, job `91500408682`, artifact `8833913602`, state `NOT_APPROVED`.

## Exact incomplete tasks

- `FUNDING-NSF-PESOSE-2026-001`: complete references and supporting documents at `funding/applications/active/`.
- `FUNDING-PESOSE-HUMAN-GATES-004`: legal applicant, ownership, PI employment, UEI, SAM.gov, submission-system and AOR evidence at `FUNDING-NSF-PESOSE-2026-001-eligibility.md`.
- `FUNDING-PESOSE-PRODUCT-EVIDENCE-005`: license, implemented boundary, dissemination and three-to-five independent letters at `FUNDING-NSF-PESOSE-2026-001-product-evidence.md`.
- `FUNDING-PESOSE-BUDGET-AUTHORITY-006`: authoritative response at `StegVerse-Labs/StegFinCo/funding-intake/FUNDING-NSF-PESOSE-2026-001-budget-response.json`.
- `FUNDING-PESOSE-IP-AUTHORITY-007`: disclosure classification at `funding/dependencies/stegpatents-authority-gap.md`.
- `FUNDING-OTF-ICRP-2026-001`: named applicant, CV, experience, eligibility, availability, milestones, budget, ethical-review pathway, IP review and practitioner evidence at `FUNDING-OTF-ICRP-2026-001-concept-note.md`.
- `FUNDING-NSF-SBIR-2026-001`: qualifying small-business, ownership, PI employment, product rights and one selected Phase I innovation at `FUNDING-NSF-SBIR-2026-001-assessment.md`.
- `FUNDING-ACADEMIC-PARTNERS-009`: eligible lead institutions and PI appointments at `funding/opportunities/2026-08-02-expanded-scan.md`.

Every task has an exact owner, location, state and release condition in `funding/coordination/funding-tasks.json`.

## Automation

Run:

```bash
python funding/tools/validate_funding_state.py
```

The GitHub Actions workflow triggers on material `funding/**` changes, qualifying pull requests and manual dispatch. It produces a JSON receipt and uploaded artifact and fails closed on missing records, expired or conflicting claims, unsupported authority changes, missing evidence, unsafe OTF concept controls, unapproved PESOSE budget state or premature submission readiness.

## Propagation

No propagation is authorized to Site, Publisher, admissibility-wiki, stegguardian-wiki or master-records before a validated submission, award, publication or custody classification.

## Session consolidation

MERGED INTO:

- `StegVerse-Labs/StegScholar/funding/FUNDING_MIRROR_HANDOFF.md`;
- `StegVerse-Labs/StegScholar/funding/coordination/funding-tasks.json`;
- `StegVerse-Labs/StegScholar/funding/evidence/expanded-scan-installation.json`;
- `StegVerse-Labs/StegScholar/funding/opportunities/2026-08-02-expanded-scan.md`;
- the OTF ICRP application and concept-note records;
- the NSF SBIR assessment;
- `StegVerse-Labs/StegFinCo/FINCO_FUNDING_MIRROR_HANDOFF.md`.

No opportunity, application decision, blocker, authority boundary, validation evidence or continuation action remains only in conversation history.

## Completion accounting

Current denominator: 31 canonical funding, application, integration, evidence and portfolio deliverables.

- task completion: `25/31 = 81%`;
- developed files: `31/31 = 100%` for currently authorized repository-owned artifacts;
- validation: `9/10 = 90%`, with authority-response validation pending;
- integration: `6/10 = 60%`;
- propagation: `0/1 = 0%`, not authorized;
- goal activation: `55%` toward a multi-opportunity portfolio with two active drafted applications and durable commercial and academic candidate lanes;
- session consolidation: `10/10 = 100%`.

## Archive condition

The conversation is archive-ready because the expanded search, application starts, validation evidence, active claims, blocked authority tasks and next actions are durable and no unique execution responsibility remains only here. Archival does not imply that any application is submission-ready.
