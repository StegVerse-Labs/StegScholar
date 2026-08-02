# StegScholar Funding Mirror Handoff

## Active goal

- Goal ID: `FUNDING-PIPELINE-001`
- Goal: operate a governed, machine-verifiable StegVerse funding portfolio, advance the NSF PESOSE Track 1 application, and open additional noncompeting high-fit funding lanes without moving applicant, IP, budget, institutional, or sponsor-submission authority into StegScholar.
- Originating session goals: identify the canonical grants repository; search broadly for fitting opportunities; begin strong applications; validate and automate continuation; preserve authority boundaries; broaden the funding search.
- Repository: `StegVerse-Labs/StegScholar`
- Branch: `main`
- Parent authority: `STEGSCHOLAR_MIRROR_HANDOFF.md`
- Task registry: `funding/coordination/funding-tasks.json`

## Active applications and portfolio lanes

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
- Application record: `funding/applications/active/FUNDING-OTF-ICRP-2026-001.json`
- Concept note: `funding/applications/active/FUNDING-OTF-ICRP-2026-001-concept-note.md`
- Research focus: privacy-preserving evidence for shutdown-resilient and censored communications.
- Release condition: eligible individual submission, committed no-go, formal decline, or supersession by a stronger OTF application.
- Collision boundary: no duplicate ICRP concept note using the same research question or applicant identity.

### NSF SBIR/STTR commercial pathway

- Candidate ID: `FUNDING-NSF-SBIR-2026-001`
- State: `BLOCKED — ELIGIBILITY REVIEW`
- Canonical assessment: `funding/applications/candidates/FUNDING-NSF-SBIR-2026-001-assessment.md`
- Consolidated topics: Artificial Intelligence and Cybersecurity and Authentication.
- Release condition: qualifying U.S. small-business, ownership, PI employment, product-rights and candidate-selection evidence.

### Academic-partner portfolio

The expanded scan preserves SaTC 2.0, Future Computing Research, Mathematical Foundations of Artificial Intelligence, EDU Core Research, CyberTraining and Cybersecurity Innovation for Cyberinfrastructure as partner-led candidates. No application is opened until an eligible lead institution and qualifying PI are recorded.

Canonical scan: `funding/opportunities/2026-08-02-expanded-scan.md`.

## Authority boundaries

- StegScholar owns opportunity intake, application drafting, evidence maps, sponsor requirements, application state and submission receipts.
- StegFinCo owns authoritative budget review and financial execution where its contract applies.
- Protected-disclosure authority remains blocked at `funding/dependencies/stegpatents-authority-gap.md` until a canonical repository or named human IP authority issues a classification.
- Human corporate authority owns legal applicant, ownership/control, employment, registrations and submission authority.
- Academic institutions own institutional eligibility and appointment authority for partner-led NSF applications.
- The OTF ICRP individual applicant owns identity, CV, experience, availability, work authorization and certifications; a host organization is not selected before a Stage 2 invitation.
- StegOps-Deliverables activates only after a verified award.

## Completed implementation

### PESOSE package

The funding control surface, reusable schemas, contracts, opportunity scan, PESOSE application records, project summary, milestones, provisional budget and substantive Project Description are committed and hosted-validated.

Latest Project Description validation:

- workflow run `30758261196`;
- job `91524128700`, success;
- artifact `8836617427`;
- digest `sha256:6fd7baac0d02db6f4c9e03037be7df875b147ca2e4e38fcc17d93672ac8b5fe0`.

### StegFinCo integration

- handoff: `StegVerse-Labs/StegFinCo/FINCO_FUNDING_MIRROR_HANDOFF.md`;
- request validation run `30749323611`;
- job `91500408682`, success;
- artifact `8833913602`;
- digest `sha256:601c0bcab8085be66846459929787c7d86dbaaba14761cefa44ebf7174775f7c`;
- state: `NOT_APPROVED`.

### Expanded portfolio

Committed expanded-scan and application artifacts:

- expanded opportunity scan: commit `23df9ba41f32044c6256dffaa8cc040e69e102a0`;
- OTF ICRP application record: commit `b36078d3ddd24e8e255629b96e299abe8575ae7b`;
- OTF ICRP concept note: commit `772f04511f9b3c7949556d7b2ff2c8c0905f02a7`;
- NSF SBIR assessment: commit `21606e16600ee35f97c62a4516c67b477e6b8fa2`;
- sponsor-aware validator: commit `b3aac7f5cd2cc01b74bbfde9d254c65c5478bc61`;
- portfolio task registry: commit `7fae04217ae791d2385547c3d64d56a3daad9090`.

The OTF concept note includes a research problem, measurable questions, controlled methods, privacy and safety evaluation, technical outputs, internet-freedom relevance, ethical safeguards, applicant/host posture, evidence gaps and a fail-closed submission prohibition.

## Exact incomplete tasks

### PESOSE supporting and authority records

- Application task: `FUNDING-NSF-PESOSE-2026-001` at `funding/applications/active/FUNDING-NSF-PESOSE-2026-001-project-description.md`.
- Applicant gates: `FUNDING-PESOSE-HUMAN-GATES-004` at `funding/applications/active/FUNDING-NSF-PESOSE-2026-001-eligibility.md`.
- Product evidence: `FUNDING-PESOSE-PRODUCT-EVIDENCE-005` at `funding/applications/active/FUNDING-NSF-PESOSE-2026-001-product-evidence.md`.
- Budget response: `FUNDING-PESOSE-BUDGET-AUTHORITY-006` at `StegVerse-Labs/StegFinCo/funding-intake/FUNDING-NSF-PESOSE-2026-001-budget-response.json`.
- IP classification: `FUNDING-PESOSE-IP-AUTHORITY-007` at `funding/dependencies/stegpatents-authority-gap.md`.

### OTF ICRP evidence

- Task: `FUNDING-OTF-ICRP-2026-001`.
- Owner: StegScholar OTF ICRP lane plus the eventual named individual applicant.
- Location: `funding/applications/active/FUNDING-OTF-ICRP-2026-001-concept-note.md`.
- Missing evidence: applicant identity, CV, relevant experience, work authorization and certifications, full-time availability, monthly milestones, project duration, budget, ethical-review pathway, protected-disclosure classification and practitioner or partner evidence.
- Release condition: concept note becomes submission-ready, receives a committed no-go, or is superseded.

### NSF SBIR eligibility

- Task: `FUNDING-NSF-SBIR-2026-001`.
- Owner: human corporate authority and StegScholar funding lane.
- Location: `funding/applications/candidates/FUNDING-NSF-SBIR-2026-001-assessment.md`.
- Release condition: qualifying small-business, ownership, PI employment, product rights and one selected Phase I innovation are evidenced.

### Academic partners

- Task: `FUNDING-ACADEMIC-PARTNERS-009`.
- Owner: StegScholar partnership lane.
- Location: `funding/opportunities/2026-08-02-expanded-scan.md`.
- Release condition: a qualifying institution, PI appointment and project-specific interest are recorded before opening any application.

## Automation

Run:

```bash
python funding/tools/validate_funding_state.py
```

The validator now checks both active applications, the OTF concept-note safety controls, sponsor-specific authority assignments, deadlines, evidence references, active claims, the expanded opportunity scan, the SBIR assessment, the PESOSE budget and the Project Description. GitHub Actions triggers on material `funding/**` changes, qualifying pull requests and manual dispatch, producing an inspectable receipt and artifact.

## Propagation

No propagation is authorized to Site, Publisher, admissibility-wiki, stegguardian-wiki or master-records before a validated submission, award, publication or custody classification.

## Session consolidation

MERGED INTO:

- `StegVerse-Labs/StegScholar/funding/FUNDING_MIRROR_HANDOFF.md`;
- `StegVerse-Labs/StegScholar/funding/coordination/funding-tasks.json`;
- `StegVerse-Labs/StegScholar/funding/opportunities/2026-08-02-expanded-scan.md`;
- `StegVerse-Labs/StegScholar/funding/applications/active/FUNDING-OTF-ICRP-2026-001.json`;
- `StegVerse-Labs/StegScholar/funding/applications/active/FUNDING-OTF-ICRP-2026-001-concept-note.md`;
- `StegVerse-Labs/StegScholar/funding/applications/candidates/FUNDING-NSF-SBIR-2026-001-assessment.md`;
- `StegVerse-Labs/StegFinCo/FINCO_FUNDING_MIRROR_HANDOFF.md`.

No session-specific opportunity, selection decision, application draft, blocker, authority boundary or next action remains only in conversation history.

## Completion accounting

Current denominator: 30 canonical funding, application, integration, evidence and expanded-portfolio deliverables.

- task completion: `24/30 = 80%`;
- developed files: `30/30 = 100%` for currently authorized repository-owned artifacts;
- validation: `8/10 = 80%` before hosted expanded-portfolio validation and authority-response validation;
- integration: `6/10 = 60%`;
- propagation: `0/1 = 0%`, not authorized;
- goal activation: `48%` toward an active multi-opportunity StegVerse funding portfolio with two drafted applications and durable commercial/academic candidate lanes;
- session consolidation: `10/10 = 100%`.

## Archive condition

This conversation may be archived after hosted validation of the expanded portfolio is inspected and recorded. Archival will not imply that PESOSE, OTF ICRP, NSF SBIR or any partner-led opportunity is submission-ready.
