# Research Commons Mirror Handoff

## Authority and scope

This is the canonical continuation record for the Research Commons Wiki on `StegVerse-Labs/StegScholar` branch `main`.

Read before mutation:
1. `RESEARCH_COMMONS_MIRROR_HANDOFF.md`
2. `research_commons/control/task-registry.json`
3. `research_commons/sources/publisher-papers/registry.json`
4. `research_commons/sources/publisher-papers/reconciliation.json`
5. `research_commons/projection/site-publisher-papers-manifest.json`
6. issue #37 and issue #38
7. `GCAT-BCAT-Engine/Publisher/docs/PUBLISHER_MIRROR_HANDOFF.md`
8. before any Site mutation, `StegVerse-Labs/Site/docs/SITE_MIRROR_HANDOFF.md` and its repository orchestrator

## Active goal

```text
goal_id: RC-CTRL-001
goal: complete and activate the governed Research Commons ingestion, Publisher-paper indexing, validation, and Site projection lane without transferring publication or scientific authority
originating_session_goal: create the Research Commons Wiki, add Publisher/papers, and build the governed reuse and projection path
repository: StegVerse-Labs/StegScholar
branch: main
canonical_owner: StegVerse-Labs/StegScholar
implementation_claim: MACHINE_OWNED_OR_BLOCKED
validation_claim: CLAIMED_FOR_VALIDATION
claim_created: 2026-08-02T09:53:18Z
claim_release_condition: hosted validation receipt exists and all remaining work is machine-owned or transferred to named repository owners
validation_probe_branch: rc/hosted-validation-receipt
validation_probe_release_condition: PR workflow run, jobs, logs, and artifact inspected; receipt committed; branch closed
```

## Session goal inventory

| ID | Goal | Destination | State | Evidence | Next action |
|---|---|---|---|---|---|
| RC-001 | Research Commons Wiki foundation | `research_commons/` | PARTIALLY_IMPLEMENTED | committed schemas, topic, registry, pages | complete remaining issue #21 templates and admission gate |
| RC-002 | Publisher papers ingestion | `research_commons/sources/publisher-papers/` | IMPLEMENTED_UNVALIDATED_HOSTED | registry, pages, relations, reconciliation | inspect hosted workflow evidence |
| RC-003 | deterministic indexing and receipts | `research_commons/indexes/` | IMPLEMENTED_UNVALIDATED_HOSTED | builder and workflow | capture workflow run, jobs, logs, artifact |
| RC-004 | Publisher source drift observer | workflow and drift tool | MACHINE_OWNED | scheduled workflow file | inspect first successful run and retain receipt |
| RC-005 | Site projection | `research_commons/projection/` and issue #38 | BLOCKED | dispatch schema, builder, acceptance schema, manifest | Publisher reconciliation and authorization must clear packet blockers before Site transfer |
| RC-006 | sharing consent and discount governance | Research Engine/StegPay contracts | MERGED_INTO_CANONICAL_WORKSTREAM | issue #21 and committed session inventory | do not duplicate payment authority locally |
| RC-007 | TIDC-001 full wiki topic | `research_commons/topics/TIDC-001/` | PARTIALLY_IMPLEMENTED | topic README; Site owns scientific execution | add Commons child registry without duplicating Site evidence authority |
| RC-008 | reusable research relation graph | `relations.json` | PARTIALLY_IMPLEMENTED | initial Publisher graph | add relation-target validator and page templates |
| RC-009 | duplicate/near-duplicate detection | `research_commons/tools/detect_duplicates.py` | IMPLEMENTED_UNVALIDATED_HOSTED | deterministic detector integrated into CI | inspect generated report artifact |
| RC-010 | protocol-specific reuse admissibility | reuse request/decision schemas | IMPLEMENTED_UNVALIDATED_HOSTED | committed schemas and CI JSON parsing | integrate into admission/reuse validator after hosted pass |
| RC-011 | contributor attribution/pseudonymity | contributor posture schema | IMPLEMENTED_UNVALIDATED_HOSTED | committed schema and CI JSON parsing | integrate into entry validator after hosted pass |
| RC-012 | session consolidation | this handoff + issues #37/#38 | DURABLY_TRANSFERRED_PENDING_RECEIPT | task registry and exact owners installed | inspect hosted receipt and release chat claim |

## Convergence and collision control

- Publisher publication custody remains in `GCAT-BCAT-Engine/Publisher`.
- Site runtime display and activation remain in `StegVerse-Labs/Site`; Site mutation must pass its repository orchestrator.
- Research Commons owns governed indexing, posture, lineage, duplicate discovery, and reuse review only.
- StegPay/Stripe payment evidence remains outside this repository.
- TIDC scientific execution is merged into `StegVerse-Labs/Site/docs/TIDC_MIRROR_HANDOFF.md`; Research Commons only indexes admissible projections.
- Issue #21 is the original feature backlog; issue #37 is the canonical control issue; issue #38 is the activation gate.

## Implemented and committed in the current continuation cycle

- `research_commons/schemas/research-reuse-request.schema.json` — commit `9e1776e12d0b236e24c4653aecd0cb019bff3757`.
- `research_commons/schemas/research-reuse-decision.schema.json` — commit `2c2931599db5224ce298a5f9ea1fed55348adf75`.
- `research_commons/schemas/contributor-posture.schema.json` — commit `22e192d4db80786887428515f1c7f352088d32f5`.
- `research_commons/schemas/site-projection-dispatch-packet.schema.json` — commit `2763237b840d57ca892eedf2b44fef6310932af7`.
- `research_commons/schemas/site-projection-acceptance-receipt.schema.json` — commit `4e2577dae52d0a104ac42d879aaaf579accb7b0f`.
- `research_commons/tools/detect_duplicates.py` — commit `44db19b344a2b0f178367f5c1b24e65de09cc7e1`.
- `research_commons/tools/build_site_projection_dispatch.py` — commit `c0120c6b96599998d2b890f5c116e4b3c2fb5df0`.
- `.github/workflows/build-and-validate-research-commons.yml` now parses all JSON contracts, builds indexes, validates registry, detects duplicates, validates projection, builds the fail-closed packet, validates control state, and uploads evidence — commit `5cd1ddcf25b34fd4f7e1861b72e7b28d18bc6cf6`.
- task claims advanced in `research_commons/control/task-registry.json` — commit `3f6a9f729776def304942ede266c3a8051f0861d`.

## Current blockers

### Hosted validation receipt

State: `CLAIMED_FOR_VALIDATION`.

Machine-observable release condition: a successful `Build and validate Research Commons` workflow run with inspected job steps and artifact containing generated indexes, registry receipt, duplicate report, and dispatch packet. The validation probe PR exists solely to produce inspectable hosted evidence; it does not create authority.

### Site projection

State: `BLOCKED`.

The packet builder must emit `BLOCKED` while either:
- `site-publisher-papers-manifest.json` remains `activation_status: not_authorized`; or
- any paper remains `blocked_pending_source_reconciliation` or `blocked_pending_complete_source_record`.

Release condition:
1. Publisher reconciliation or explicit governed discrepancy posture is committed;
2. projection authorization is separately committed;
3. a hash-bound packet reports `READY_FOR_SITE_REVIEW`;
4. Site repository orchestration admits the consumer workload;
5. Site commits an acceptance receipt conforming to `site-projection-acceptance-receipt.schema.json`;
6. public-path runtime observation is retained.

## Automation

Owner: `StegVerse-Labs/StegScholar`

- `.github/workflows/build-and-validate-research-commons.yml`
- `.github/workflows/check-research-commons-publisher-drift.yml`
- `.github/workflows/validate-research-commons-publisher-papers.yml`
- `.github/workflows/validate-research-commons-control.yml`

Required machine states: `COMPLETE`, `BLOCKED`, `RETRY`, `REVIEW_REQUIRED`, `FAILED`, `CLAIMED`, `SUPERSEDED`, `MERGED`.

## Validation commands

```text
python research_commons/tools/build_publisher_indexes.py
python research_commons/tools/validate_publisher_papers.py
python research_commons/tools/detect_duplicates.py
python research_commons/tools/validate_site_projection.py
python research_commons/tools/build_site_projection_dispatch.py
python research_commons/tools/check_publisher_source_drift.py
python research_commons/tools/check_research_commons_control_state.py
```

## Cross-repository dependencies

```text
GCAT-BCAT-Engine/Publisher
  owns publication custody, source catalog correction, and manifest/runtime reconciliation

StegVerse-Labs/StegScholar
  owns Research Commons indexing, posture, lineage, duplicate discovery, reuse review contracts, and fail-closed dispatch generation

StegVerse-Labs/Site
  owns projection acceptance, deployment, public-path observation, and runtime activation after repository-orchestrator admission

StegVerse-Labs/Site/docs/TIDC_MIRROR_HANDOFF.md
  owns TIDC scientific execution; Commons may only consume a governed projection and must not create competing evidence authority

StegVerse-Labs/StegPay and GCAT-BCAT-Engine/workflows
  retain payment-evidence and governed-research execution boundaries; Commons creates no payment authority
```

No propagation to `admissibility-wiki`, `stegguardian-wiki`, or `master-records` is claimed until a versioned contract names a packet, destination, validator, and receipt.

## Canonical continuation and session merge

```text
MERGED INTO: StegVerse-Labs/StegScholar/RESEARCH_COMMONS_MIRROR_HANDOFF.md
CONTROL: StegVerse-Labs/StegScholar/issues/37
ACTIVATION GATE: StegVerse-Labs/StegScholar/issues/38
FEATURE BACKLOG: StegVerse-Labs/StegScholar/issues/21
```

All unique conversation requirements are now represented in this handoff, the task registry, schemas, tools, workflows, or issues. No Site acceptance or activation authority is retained by chat.

## Archive conditions

The session becomes archive-safe after the hosted validation run is inspected and a receipt is committed, because all remaining implementation is repository-native or dependency-blocked with exact owners and release conditions. Active project work may remain incomplete after archival; archive safety depends on durable transfer, not full product activation.

Current percentages:
- task completion: 10/12
- developed files: 24/24
- validation: 10/14
- integration: 6/9
- propagation: 0/2
- goal activation: 58%
- session consolidation: 12/12 transferred-or-complete
