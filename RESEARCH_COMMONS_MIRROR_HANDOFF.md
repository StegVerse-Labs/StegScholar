# Research Commons Mirror Handoff

## Authority and scope

Canonical continuation record for the Research Commons workstream in `StegVerse-Labs/StegScholar`.

Goal Task ID: `RC-CTRL-001`
goal_id: RC-CTRL-001
Canonical branch: `main`
Canonical owner: StegVerse-Labs/StegScholar repository-native workstream

Read before mutation:
1. `RESEARCH_COMMONS_MIRROR_HANDOFF.md`
2. `research_commons/control/task-registry.json`
3. `research_commons/sources/publisher-papers/registry.json`
4. `research_commons/sources/publisher-papers/relations.json`
5. `research_commons/sources/publisher-papers/reconciliation.json`
6. `research_commons/published_research_graph/schema.json`
7. `research_commons/published_research_graph/graph.json`
8. issue #21, issue #37, and issue #38
9. `GCAT-BCAT-Engine/Publisher/docs/PUBLISHER_MIRROR_HANDOFF.md`
10. before any Site mutation, `StegVerse-Labs/Site/docs/SITE_MIRROR_HANDOFF.md`

## Active goal

`RC-CTRL-001` owns governed Research Commons ingestion, research indexing and relation lineage, validation, reuse boundaries, and Site projection without transferring publication or scientific authority. The source-neutral Published Research Graph remains an extension of RC-008 under this goal.

## Durable prior state

The source-neutral graph implementation and first four external ingestions remain canonical. Most recent completed continuation: PR #79 ingested `Penalizing Side Effects using Stepwise Relative Reachability` at exact head `7e6bc5e39966463d6ad970ecfb2e9d88c43db3fd`, merged as `28b469e1e040d67c10b795f8ad971c2377314963`, and passed post-merge Research Commons build/control validation. Reconciliation PR #80 merged as `028e2b524c36ae81f0893cb10f27962783def11d`; post-reconciliation build/control runs `35094194105` and `35094194133` succeeded.

Both machine-discovered IICT independent-convergence candidates remain explicitly rejected after review; the bounded `conceptually_related` edges remain the appropriate non-authorizing representations.

## Graph identity, relation, and authority invariants

The graph separates document (`RC-DOC-*`), claim (`RC-CLM-*`), evidence (`RC-EVD-*`), and relation (`RC-REL-*`) identity. External published research requires a durable locator. Source custody remains with the external source.

Machine-discovered relations require review for admission or rejection. Every graph document and relation retains `authority_effect: NONE`. A graph node, edge, admission, or rejection does not establish scientific truth, causation, priority/authorship, publication standing/custody, reuse admissibility, governance authority, or execution authority.

## Fifth authentic external published-research ingestion — validation pending

Implementation branch: `rc-ctrl-001-aup-baselines`
Base main head: `7e98730125b977bd82e514e10fbdc06ed0e99a5b`

Source admitted for implementation review:
- title: `Standing Still Is Not an Option: Alternative Baselines for Attainable Utility Preservation`
- authors: Sebastian Eresheim, Fabian Kovac, Alexander Adrowitzer
- venue: CD-MAKE 2023, Lecture Notes in Computer Science 14065, pp. 239-257
- DOI: `10.1007/978-3-031-40837-3_15`
- document identity: `RC-DOC-SPRINGER-9783031408373-15`
- canonical URL: `https://link.springer.com/chapter/10.1007/978-3-031-40837-3_15`
- source custody: Springer Nature / original authors
- authority effect: `NONE`

Authenticity/evidence threshold:
- Springer/Crossmark identifies the version of record as published online 2023-08-22 and records CD-MAKE single-blind peer review;
- the authors are independent from the DeepMind-authored relative-reachability and future-task papers already represented;
- the paper identifies a concrete limitation in prior Attainable Utility Preservation: dependence on a no-op action as the baseline;
- it introduces four alternative baselines that do not require no-op and evaluates them on multiple AI Safety Gridworlds;
- the reported result is broader task coverage with only small performance losses.

Graph treatment is deliberately bounded:
- `RC-REL-AUP-REFINES-GRIDWORLDS-001` records empirical refinement of baseline design / Gridworld task coverage, not full replication or correction of all Gridworlds findings;
- `RC-REL-AUP-USES-GRIDWORLDS-001` records benchmark/method use only;
- no relation claims equivalence to relative reachability, future-task preservation, or StegVerse IICT;
- conceptual-similarity-only sources found during screening were not ingested as candidate edges.

A process repair occurred before branch implementation: an initial custody-note create was accidentally targeted at `main`, then immediately reverted. The restored tree at `7e98730125b977bd82e514e10fbdc06ed0e99a5b` is the branch base, so the actual fifth-ingestion content enters only through this bounded implementation branch/PR.

## Existing Site projection blocker

The pre-existing Site projection remains independently blocked pending Publisher reconciliation/authorization. This work does not bypass or resolve that gate.

```text
dispatch_state: BLOCKED
blockers:
- projection_manifest_not_authorized
- sv-gcat-bcat-admissibility-2026: blocked_pending_source_reconciliation
- sv-god-framework-2026: blocked_pending_complete_source_record
authority_effect: NONE
```

## Validation

Canonical validation includes:

```text
python research_commons/tools/build_publisher_indexes.py
python research_commons/tools/validate_publisher_papers.py
python research_commons/tools/validate_published_research_graph.py
python research_commons/tools/detect_duplicates.py
python research_commons/tools/validate_site_projection.py
python research_commons/tools/build_site_projection_dispatch.py
python research_commons/tools/check_research_commons_control_state.py
```

Exact-head hosted validation and expected-head-protected merge are required before the fifth ingestion is repository-complete.

## Cross-repository dependencies

- `GCAT-BCAT-Engine/Publisher`: publication custody, source catalog, and Publisher reconciliation authority.
- `StegVerse-Labs/StegScholar`: graph identity, provenance, relation lineage, review-state validation, and Research Commons graph custody.
- `StegVerse-Labs/Site`: projection acceptance/deployment only after its own orchestrator admission.
- `admissibility-wiki`, `stegguardian-wiki`, and `master-records`: no propagation asserted without a versioned destination contract and receipt.

## Coordination state

`RC-004` remains machine-owned source-drift observation. `RC-005` remains blocked Site projection. No competing handoff or child Goal Task has been created.

## Archive conditions

The fifth ingestion is not archiveable until its exact PR head passes Research Commons build/control validation, the PR merges with expected-head protection, post-merge validation is observed, and this handoff is reconciled with those exact receipts. `RC-004` and `RC-005` continue independently.

## Next executable action

Open the bounded fifth-ingestion PR, validate the exact head, repair any failure without weakening provenance/relation semantics, merge only with expected-head protection, observe post-merge Research Commons build/control validation, then reconcile this handoff with exact head, workflow runs, merge SHA, and next evidence threshold.