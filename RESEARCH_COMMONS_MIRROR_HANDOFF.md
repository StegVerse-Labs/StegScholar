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

## Active goal

```text
goal_id: RC-CTRL-001
goal: complete and activate the governed Research Commons ingestion, Publisher-paper indexing, validation, and Site projection lane without transferring publication or scientific authority
originating_session_goal: create the Research Commons Wiki, add Publisher/papers, and build the governed reuse and projection path
repository: StegVerse-Labs/StegScholar
branch: main
canonical_owner: StegVerse-Labs/StegScholar
implementation_claim: CLAIMED_FOR_IMPLEMENTATION
validation_claim: CLAIMED_FOR_VALIDATION
claim_created: 2026-08-02T09:53:18Z
claim_release_condition: required control, validation, dispatch, and acceptance records are complete or transferred to named owners
```

## Session goal inventory

| ID | Goal | Destination | State | Evidence | Next action |
|---|---|---|---|---|---|
| RC-001 | Research Commons Wiki foundation | `research_commons/` | PARTIALLY_IMPLEMENTED | committed schemas, topic, registry, pages | complete issue #21 deliverables |
| RC-002 | Publisher papers ingestion | `research_commons/sources/publisher-papers/` | IMPLEMENTED_UNVALIDATED_HOSTED | registry, pages, relations, reconciliation | inspect hosted workflow evidence |
| RC-003 | deterministic indexing and receipts | `research_commons/indexes/` | IMPLEMENTED_UNVALIDATED_HOSTED | builder and workflow | capture workflow run, jobs, logs, artifact |
| RC-004 | Publisher source drift observer | workflow and drift tool | MACHINE_OWNED | scheduled workflow file | verify first successful scheduled/manual run |
| RC-005 | Site projection | `research_commons/projection/` and issue #38 | BLOCKED | manifest says `not_authorized` | create dispatch packet schema and receipt chain |
| RC-006 | sharing consent and discount governance | Research Engine/StegPay contracts | MERGED_INTO_CANONICAL_WORKSTREAM | issue #21 requirements and session record | preserve cross-repo references; no duplicate local payment authority |
| RC-007 | TIDC-001 full wiki topic | `research_commons/topics/TIDC-001/` | PARTIALLY_IMPLEMENTED | topic README | add child registry and posture records |
| RC-008 | reusable research relation graph | `relations.json` | PARTIALLY_IMPLEMENTED | initial Publisher graph | add validation for allowed relation types and targets |
| RC-009 | duplicate/near-duplicate detection | Research Commons tools | MISSING | issue #21 | implement deterministic exact-hash and normalized-title duplicate detector |
| RC-010 | protocol-specific reuse admissibility | schema/validator | PARTIALLY_IMPLEMENTED | flags exist | add explicit reuse request and decision schemas |
| RC-011 | contributor attribution/pseudonymity | schema | MISSING | issue #21 | add contributor identity posture schema |
| RC-012 | session consolidation | this handoff + issues #37/#38 | ACTIVE | durable transfer started | transfer all unresolved tasks and release chat ownership |

## Convergence and collision control

- Publisher publication custody remains in `GCAT-BCAT-Engine/Publisher`.
- Site runtime display and activation remain in `StegVerse-Labs/Site`.
- Research Commons owns governed indexing, posture, lineage, and reuse review only.
- StegPay/Stripe payment evidence remains outside this repository.
- Issue #21 is the original feature backlog; issue #37 is the canonical control issue; issue #38 is the activation gate.
- No duplicate Research Commons implementation claim was found in the inspected repository state.

## Active claims

Claims are recorded in `research_commons/control/task-registry.json`. Claims expire after 72 hours without a commit, workflow receipt, or issue-state update and must then become `BLOCKED`, `RELEASED`, or renewed with evidence.

## Completed work

- Research Commons root and entry schema.
- TIDC-001 topic seed.
- Publisher-paper registry and five paper pages.
- relation and reconciliation records.
- source observation record.
- search and generated-index tooling.
- projection manifest and fail-closed projection validator.
- drift observer and validation workflows.
- canonical control issues #37 and #38.

## Incomplete work

1. hosted workflow run/job/log/artifact verification for the Research Commons workflows;
2. dispatch packet schema, packet builder, and hash receipt;
3. Site acceptance receipt schema and consumer handoff;
4. duplicate detector;
5. reuse admissibility request/decision schemas and validator;
6. contributor attribution/pseudonymity schema;
7. TIDC-001 child registry;
8. Publisher manifest/runtime reconciliation remains owned by Publisher;
9. runtime Site activation and public-path observation remain owned by Site.

## Automation

Owner: `StegVerse-Labs/StegScholar`

- `.github/workflows/build-and-validate-research-commons.yml`
- `.github/workflows/check-research-commons-publisher-drift.yml`
- `.github/workflows/validate-research-commons-publisher-papers.yml`

Required machine states: `COMPLETE`, `BLOCKED`, `RETRY`, `REVIEW_REQUIRED`, `FAILED`, `CLAIMED`, `SUPERSEDED`, `MERGED`.

## Validation commands

```text
python research_commons/tools/build_publisher_indexes.py
python research_commons/tools/validate_publisher_papers.py
python research_commons/tools/validate_site_projection.py
python research_commons/tools/check_publisher_source_drift.py
python research_commons/tools/check_research_commons_control_state.py
```

## Cross-repository dependencies

```text
GCAT-BCAT-Engine/Publisher source and reconciliation
-> StegVerse-Labs/StegScholar observation, registry, validation, dispatch packet
-> StegVerse-Labs/Site acceptance, projection, runtime observation
```

Potential downstream reuse projections to `admissibility-wiki`, `stegguardian-wiki`, and `master-records` require separate contracts and direct evidence; none is claimed complete here.

## Archive conditions

This session can be archived when all unique session requirements are present in this handoff, issue #37, issue #38, issue #21, or committed files; no chat-only implementation authority remains; active claims are machine-owned or released; and the next executable task is unambiguous.

Current percentages:
- developed files: 18/24
- validation: 8/14
- integration: 4/9
- goal activation: 42%
- session consolidation: 10/12
