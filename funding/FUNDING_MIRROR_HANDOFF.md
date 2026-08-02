# StegScholar Funding Mirror Handoff

## Active goal

- Goal ID: `FUNDING-PIPELINE-001`
- Goal: operate a governed, machine-verifiable multi-opportunity funding portfolio without transferring applicant, IP, budget, ethics, institutional, or submission authority into StegScholar.
- Repository: `StegVerse-Labs/StegScholar`
- Branch: `main`
- Parent authority: `STEGSCHOLAR_MIRROR_HANDOFF.md`
- Portfolio registry: `funding/coordination/funding-tasks.json`
- OTF registry: `funding/coordination/otf-icrp-tasks.json`
- Deadline-watch registry: `funding/coordination/deadline-watch-tasks.json`

## Canonical portfolio

### NSF PESOSE Track 1

- ID: `FUNDING-NSF-PESOSE-2026-001`
- Deadline: `2026-09-01T17:00:00-05:00`
- State: `CLAIMED_FOR_IMPLEMENTATION`
- Canonical narrative: `funding/applications/active/FUNDING-NSF-PESOSE-2026-001-project-description.md`
- Hosted validation: run `30758261196`, job `91524128700`, artifact `8836617427`.
- Budget intake validation in StegFinCo: run `30749323611`, job `91500408682`, artifact `8833913602`, approval state `NOT_APPROVED`.
- Release condition: authorized submission, committed no-go, qualified-lead supersession, or deadline.

### OTF Information Controls Research Program

- ID: `FUNDING-OTF-ICRP-2026-001`
- Deadline: `2026-09-07T23:59:00+00:00`
- State: `CLAIMED_FOR_IMPLEMENTATION`
- Canonical sub-handoff: `funding/applications/active/OTF_ICRP_MIRROR_HANDOFF.md`
- Package: application record, concept note, eligibility gate, ethics/safety plan, milestones, and unapproved budget request.
- Operational state: `DRAFTING`, field activity `SYNTHETIC_ONLY`, budget `DRAFT_UNAPPROVED`.
- Initial hosted failure: run `30768922744`, job `91552517780`; global validator passed and the OTF validator exposed a marker mismatch.
- Corrected hosted validation: run `30768955549`, job `91552600642`, artifact `8839878425`, digest `sha256:665373a7572586b48ae3a2b7b57c9f1c62088bbf09c04d0438f555a4ac7795fb`.
- Release condition: named eligible applicant submission, committed no-go, formal decline, supersession, or deadline.

### NSF SBIR/STTR candidate

- ID: `FUNDING-NSF-SBIR-2026-001`
- State: `BLOCKED — ELIGIBILITY REVIEW`
- Location: `funding/applications/candidates/FUNDING-NSF-SBIR-2026-001-assessment.md`
- Release condition: qualifying U.S. small business, ownership, PI employment, product rights, and selected Phase I innovation.

### Academic-partner candidates

SaTC 2.0, Future Computing Research, Mathematical Foundations of AI, EDU Core Research, CyberTraining, and CICI remain blocked until an eligible institution, qualifying PI appointment, and project-specific interest are recorded.

Canonical scan: `funding/opportunities/2026-08-02-expanded-scan.md`.

## Authority boundaries

- StegScholar owns opportunity intake, drafting, evidence maps, sponsor requirements, application state, validators, and submission receipts.
- StegFinCo owns authoritative financial approval and execution where contracted.
- Human corporate authority owns legal applicant, ownership/control, employment, registrations, and submission authority.
- The named OTF applicant owns identity, CV, experience, availability, eligibility declarations, and final submission authorization.
- A qualified ethical reviewer owns any transition beyond `SYNTHETIC_ONLY`.
- Protected-disclosure authority remains blocked at `funding/dependencies/stegpatents-authority-gap.md` until a named human IP authority or canonical repository issues a classification.
- Academic institutions own institutional eligibility and PI appointment authority.
- StegOps-Deliverables activates only after a verified award.

## Completed implementation

The repository contains the funding schemas, application controls, reusable organization profile, authority contracts, broad and expanded opportunity scans, PESOSE package, OTF package, NSF SBIR assessment, sponsor-aware validators, task registries, hosted workflows, receipts, and cross-repository StegFinCo budget intake.

Key OTF package commits:

- eligibility gate: `46305483e472f81b82b2bc7c1989571b4b616017`;
- ethics/safety plan: `876dac9a2f575ff812ee714c5d6aac5b0da0bee5`;
- milestones: `19b2e6f00726277289287e86566f93ab6782405f`;
- budget request: `90feab6fa122a30f1c265b6d2f12fbb08c702976`;
- application binding: `e862eab277617dcc9d8ec18e0218410fd58b2f40`;
- OTF validator correction on main: `5798c82d307529dc63301b9f119262a9c6603897`;
- OTF hosted-evidence handoff update: `29870a1422a4e45c251f9b7db1ac55692b428c09`;
- OTF registry hosted-evidence update: `a21689388a74b1119a78d6785bcc9df8d76819bc`.

## Deadline and claim automation

Goal ID: `FUNDING-DEADLINE-WATCH-010`.

Installed:

- `funding/tools/check_funding_deadlines.py` — commit `1d5310faa254f038df72636e3620c2253f696dfd`;
- `.github/workflows/funding-deadline-watch.yml` — commit `1e9d7149b1169b863ab51c5cc01ade9195dc64e8`;
- `funding/coordination/deadline-watch-tasks.json` — commit `6ee5fb8c97067bb585028259dd81fd74859bbd2c`.

The workflow runs daily at `13:15 UTC`, on manual dispatch, and after relevant portfolio changes. It evaluates active claim expiry and application deadlines, emits `funding/evidence/latest-deadline-watch.json`, uploads artifact `funding-deadline-watch`, and fails closed on expired active claims or overdue nonterminal applications.

Hosted execution evidence remains required before the watcher is considered validated.

## Exact incomplete tasks

- `FUNDING-NSF-PESOSE-2026-001`: complete references and sponsor supporting documents under `funding/applications/active/`.
- `FUNDING-PESOSE-HUMAN-GATES-004`: legal applicant, ownership/control, PI employment, UEI, SAM.gov, submission-system, and AOR evidence in `FUNDING-NSF-PESOSE-2026-001-eligibility.md`.
- `FUNDING-PESOSE-PRODUCT-EVIDENCE-005`: license, implemented boundary, dissemination evidence, and three-to-five qualifying letters in `FUNDING-NSF-PESOSE-2026-001-product-evidence.md`.
- `FUNDING-PESOSE-BUDGET-AUTHORITY-006`: authoritative response in `StegVerse-Labs/StegFinCo/funding-intake/FUNDING-NSF-PESOSE-2026-001-budget-response.json`.
- `FUNDING-PESOSE-IP-AUTHORITY-007`: disclosure classification at `funding/dependencies/stegpatents-authority-gap.md`.
- `OTF-APPLICANT-002`: identity, CV, experience, eligibility declarations, and availability in `FUNDING-OTF-ICRP-2026-001-eligibility.md`.
- `OTF-ETHICS-003`: qualified review pathway before any field or participant activity in `FUNDING-OTF-ICRP-2026-001-ethics-safety-plan.md`.
- `OTF-BUDGET-004`: applicant-specific approved, blocked, or no-go budget response in `FUNDING-OTF-ICRP-2026-001-budget-request.json`.
- `OTF-IP-005`: application-specific disclosure classification in `FUNDING-OTF-ICRP-2026-001.json`.
- `FUNDING-NSF-SBIR-2026-001`: qualifying company and candidate evidence in the SBIR assessment.
- `FUNDING-ACADEMIC-PARTNERS-009`: eligible lead institutions and PI appointments in the expanded scan.
- `DEADLINE-WATCH-IMPLEMENTATION-001`: first hosted workflow run, job, logs or steps, artifact, and digest.

Every unresolved task has a named owner, exact location, state, and release condition in the applicable registry.

## Validation commands

```bash
python funding/tools/validate_funding_state.py
python funding/tools/validate_otf_icrp_package.py
python funding/tools/check_funding_deadlines.py
```

## Propagation

No propagation is authorized to Site, Publisher, admissibility-wiki, stegguardian-wiki, or master-records before a verified submission, award, publication, or custody classification.

## Session consolidation

MERGED INTO:

- `funding/FUNDING_MIRROR_HANDOFF.md`;
- `funding/coordination/funding-tasks.json`;
- `funding/applications/active/OTF_ICRP_MIRROR_HANDOFF.md`;
- `funding/coordination/otf-icrp-tasks.json`;
- `funding/coordination/deadline-watch-tasks.json`;
- `StegVerse-Labs/StegFinCo/FINCO_FUNDING_MIRROR_HANDOFF.md`.

No opportunity, implementation fact, validator defect, authority boundary, claim, blocker, or next action remains only in conversation history.

## Completion accounting

Current denominator: 42 canonical funding, application, integration, evidence, automation, and portfolio deliverables.

- task completion: `35/42 = 83%`;
- developed files: `42/42 = 100%` for currently authorized repository-owned artifacts;
- validation: `12/13 = 92%`, with deadline-watch hosted validation pending;
- integration: `8/12 = 67%`;
- propagation: `0/1 = 0%`, not authorized;
- goal activation: `63%` toward governed multi-opportunity operation and authorized submissions;
- session consolidation: `12/12 = 100%`.

## Archive condition

This conversation is archive-safe once deadline-watch hosted execution evidence is recorded. Application submission readiness remains separately blocked by the named human and repository authorities above.
