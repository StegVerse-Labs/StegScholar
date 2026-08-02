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
- Hosted application validation: run `30758261196`, job `91524128700`, artifact `8836617427`.
- StegFinCo budget-intake validation: run `30749323611`, job `91500408682`, artifact `8833913602`, approval `NOT_APPROVED`.
- Release condition: authorized submission, committed no-go, qualified-lead supersession, or deadline.

### OTF Information Controls Research Program

- ID: `FUNDING-OTF-ICRP-2026-001`
- Deadline: `2026-09-07T23:59:00+00:00`
- State: `CLAIMED_FOR_IMPLEMENTATION`
- Canonical sub-handoff: `funding/applications/active/OTF_ICRP_MIRROR_HANDOFF.md`
- Package: application record, concept note, eligibility gate, ethics/safety plan, milestones, and unapproved budget request.
- Operational state: `DRAFTING`, field activity `SYNTHETIC_ONLY`, budget `DRAFT_UNAPPROVED`.
- Initial validation defect: run `30768922744`, job `91552517780`.
- Corrected hosted validation: run `30768955549`, job `91552600642`, artifact `8839878425`, digest `sha256:665373a7572586b48ae3a2b7b57c9f1c62088bbf09c04d0438f555a4ac7795fb`.
- Release condition: named eligible applicant submission, committed no-go, formal decline, supersession, or deadline.

### Other lanes

- NSF SBIR/STTR candidate `FUNDING-NSF-SBIR-2026-001` remains `BLOCKED — ELIGIBILITY REVIEW` at `funding/applications/candidates/FUNDING-NSF-SBIR-2026-001-assessment.md`.
- SaTC 2.0, Future Computing Research, Mathematical Foundations of AI, EDU Core Research, CyberTraining, and CICI remain partner-led candidates blocked until eligible institutions and qualifying PI appointments are recorded.
- Canonical opportunity scan: `funding/opportunities/2026-08-02-expanded-scan.md`.

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

The repository contains funding schemas, application controls, reusable organization records, authority contracts, opportunity scans, the PESOSE package, the OTF package, the NSF SBIR assessment, sponsor-aware validators, task registries, hosted workflows, receipts, and the StegFinCo budget intake.

OTF package evidence:

- eligibility gate `46305483e472f81b82b2bc7c1989571b4b616017`;
- ethics plan `876dac9a2f575ff812ee714c5d6aac5b0da0bee5`;
- milestones `19b2e6f00726277289287e86566f93ab6782405f`;
- budget request `90feab6fa122a30f1c265b6d2f12fbb08c702976`;
- application binding `e862eab277617dcc9d8ec18e0218410fd58b2f40`;
- validator correction `5798c82d307529dc63301b9f119262a9c6603897`;
- hosted handoff evidence `29870a1422a4e45c251f9b7db1ac55692b428c09`;
- hosted registry evidence `a21689388a74b1119a78d6785bcc9df8d76819bc`.

## Deadline and claim automation

Goal ID: `FUNDING-DEADLINE-WATCH-010`.

Installed:

- `funding/tools/check_funding_deadlines.py` — `1d5310faa254f038df72636e3620c2253f696dfd`;
- `.github/workflows/funding-deadline-watch.yml` — initial `1e9d7149b1169b863ab51c5cc01ade9195dc64e8`, PR-trigger correction `e3a8e489faf1fbb9e305423690202b12bb66df55`;
- `funding/coordination/deadline-watch-tasks.json` — initial `6ee5fb8c97067bb585028259dd81fd74859bbd2c`, hosted-evidence update `c2e2d3b83c2e1f8255d4ff2c43f4c27d302025f4`.

Triggers:

- daily at `13:15 UTC`;
- manual dispatch;
- relevant pushes;
- qualifying pull requests.

Behavior:

- evaluates active-claim expiry;
- evaluates active-application deadlines;
- emits `funding/evidence/latest-deadline-watch.json`;
- uploads artifact `funding-deadline-watch`;
- fails closed on expired active claims or overdue nonterminal applications.

Hosted proof:

- validation PR `#45`;
- request commit `fa7723e4b3248db5c8a1385982904ef463539d6c`;
- validated branch commit `203d769020f57e6304b159f0cb354a23cc47bcd7`;
- workflow run `30769208593`;
- job `91553274727`, success;
- check step success;
- artifact-upload step success;
- artifact `8839953774`, size `1061` bytes;
- digest `sha256:da113b32512289b510ff5c8391188a8f35423153ca80f67aa95b723014e0776f`;
- expiration `2026-10-31T22:02:20Z`.

Observed state at `2026-08-02T22:02:27.918482+00:00`:

- PESOSE claim `ACTIVE`; application `OPEN`; approximately `719.96` hours remained.
- OTF ICRP claim `ACTIVE`; application `OPEN`; approximately `865.94` hours remained.
- failures: none.

The same validation PR also produced successful funding-state run `30769208595`, job `91553274761`, including the global and OTF package validators and receipt upload.

## Exact incomplete tasks

- `FUNDING-NSF-PESOSE-2026-001`: references and sponsor supporting documents under `funding/applications/active/`.
- `FUNDING-PESOSE-HUMAN-GATES-004`: legal applicant, ownership/control, PI employment, UEI, SAM.gov, submission-system, and AOR evidence in `FUNDING-NSF-PESOSE-2026-001-eligibility.md`.
- `FUNDING-PESOSE-PRODUCT-EVIDENCE-005`: license, implemented boundary, dissemination evidence, and three-to-five qualifying letters in `FUNDING-NSF-PESOSE-2026-001-product-evidence.md`.
- `FUNDING-PESOSE-BUDGET-AUTHORITY-006`: authoritative response in `StegVerse-Labs/StegFinCo/funding-intake/FUNDING-NSF-PESOSE-2026-001-budget-response.json`.
- `FUNDING-PESOSE-IP-AUTHORITY-007`: disclosure classification at `funding/dependencies/stegpatents-authority-gap.md`.
- `OTF-APPLICANT-002`: identity, CV, experience, declarations, and availability in `FUNDING-OTF-ICRP-2026-001-eligibility.md`.
- `OTF-ETHICS-003`: qualified review pathway in `FUNDING-OTF-ICRP-2026-001-ethics-safety-plan.md` before field or participant activity.
- `OTF-BUDGET-004`: applicant-specific approved, blocked, or no-go response in `FUNDING-OTF-ICRP-2026-001-budget-request.json`.
- `OTF-IP-005`: application-specific disclosure classification in `FUNDING-OTF-ICRP-2026-001.json`.
- `FUNDING-NSF-SBIR-2026-001`: qualifying company and selected innovation evidence in the SBIR assessment.
- `FUNDING-ACADEMIC-PARTNERS-009`: eligible lead institutions and PI appointments in the expanded scan.
- `DEADLINE-WATCH-OPERATION-002`: machine-owned daily operation in `.github/workflows/funding-deadline-watch.yml`.

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

- task completion: `36/42 = 86%`;
- developed files: `42/42 = 100%` for currently authorized repository-owned artifacts;
- validation: `13/13 = 100%` for repository-owned validation surfaces;
- integration: `9/12 = 75%`;
- propagation: `0/1 = 0%`, not authorized;
- goal activation: `67%` toward governed multi-opportunity operation and authorized submissions;
- session consolidation: `12/12 = 100%`.

## Archive condition

The conversation is archive-ready. The remaining application and authority work is fully assigned to durable registries and machine-owned observation; submission readiness remains separately blocked by named human and repository authorities.
