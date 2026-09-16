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

The source-neutral graph implementation and first four external ingestions remain canonical. Both machine-discovered IICT independent-convergence candidates remain explicitly rejected after review; bounded `conceptually_related` edges remain the appropriate non-authorizing representation.

## Graph identity, relation, and authority invariants

The graph separates document (`RC-DOC-*`), claim (`RC-CLM-*`), evidence (`RC-EVD-*`), and relation (`RC-REL-*`) identity. External published research requires a durable locator. Source custody remains with the external source. Machine-discovered relations require review for admission or rejection. Every graph document and relation retains `authority_effect: NONE`; no graph edge establishes scientific truth, causation, priority/authorship, publication standing/custody, reuse admissibility, governance authority, or execution authority.

## Fifth authentic external published-research ingestion — merged 2026-09-16

Implementation PR: `StegVerse-Labs/StegScholar#81`
Implementation branch: `rc-ctrl-001-aup-baselines`
Base main head: `7e98730125b977bd82e514e10fbdc06ed0e99a5b`
Validated exact PR head: `87f40956e747585f3a75bbd67206696e9dc8afce`
Merge SHA: `84ac557f72df0acf8778061e5b2b38e97337444f`
Expected-head protection: merge was performed against exact head `87f40956e747585f3a75bbd67206696e9dc8afce`.

Exact-head hosted validation:
- `Build and validate Research Commons` run `35097670233`, run number 108, success.
- `Validate Research Commons Control State` run `35097670362`, run number 606, success.
- `Test Readiness` run `35097670346`, run number 828, success.
- `Validate Independent Review` run `35097670402`, run number 49, success.
- `Validate Architecture Neutral Admissibility` run `35097670366`, run number 15, success.
- `Validate GTG Assurance Reference Integration` run `35097670312`, run number 10, success.
- `Validate GTG Assurance Consumer Compatibility Sweep` run `35097670375`, run number 10, success.

Post-merge main evidence at `84ac557f72df0acf8778061e5b2b38e97337444f`:
- `Build and validate Research Commons` run `35097721217`, run number 109, success.
- `Validate Research Commons Control State` run `35097721285`, run number 607, success.
- `Test Readiness` run `35097721152`, run number 829, success.
- `Validate Independent Review` run `35097721157`, run number 50, success.

External source:
- title: `Standing Still Is Not an Option: Alternative Baselines for Attainable Utility Preservation`
- authors: Sebastian Eresheim, Fabian Kovac, Alexander Adrowitzer
- venue: CD-MAKE 2023, Lecture Notes in Computer Science 14065, pp. 239-257
- DOI: `10.1007/978-3-031-40837-3_15`
- document identity: `RC-DOC-SPRINGER-9783031408373-15`
- canonical URL: `https://link.springer.com/chapter/10.1007/978-3-031-40837-3_15`
- source custody: Springer Nature / original authors
- authority effect: `NONE`

Source-grounded findings and bounded relations:
- the independently authored peer-reviewed paper identifies prior AUP dependence on a no-op action as a limitation, introduces four alternative baselines without that requirement, and evaluates them on multiple AI Safety Gridworlds with broader task coverage and only small reported performance losses;
- `RC-REL-AUP-REFINES-GRIDWORLDS-001` records bounded empirical refinement of baseline design / Gridworld task coverage, not full replication or correction of all Gridworlds findings;
- `RC-REL-AUP-USES-GRIDWORLDS-001` records benchmark/method use only;
- no relation claims equivalence to relative reachability, future-task preservation, or StegVerse IICT; conceptual-similarity-only screened sources were not ingested.

Process repair: an initial custody-note create was accidentally targeted at `main` as commit `3d253fe9eb23c9c4be3d821faa00bbf76c5adfb0` and immediately reverted as `7e98730125b977bd82e514e10fbdc06ed0e99a5b`, restoring the prior tree before the bounded implementation branch was created. The actual fifth-ingestion content entered canonical main only through validated PR #81.

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

## Cross-repository dependencies

- `GCAT-BCAT-Engine/Publisher`: publication custody, source catalog, and Publisher reconciliation authority.
- `StegVerse-Labs/StegScholar`: graph identity, provenance, relation lineage, review-state validation, and Research Commons graph custody.
- `StegVerse-Labs/Site`: projection acceptance/deployment only after its own orchestrator admission.
- `admissibility-wiki`, `stegguardian-wiki`, and `master-records`: no propagation asserted without a versioned destination contract and receipt.

## Coordination state

`RC-004` remains machine-owned source-drift observation. `RC-005` remains blocked Site projection. No competing handoff or child Goal Task has been created.

## Archive conditions

The fifth ingestion is repository-complete at implementation/merge level: exact PR head validation passed, PR #81 merged with expected-head protection, and the merge commit passed post-merge Research Commons build/control validation. This reconciliation itself must pass hosted validation and merge before this bounded continuation is fully checked out. `RC-004` and `RC-005` continue independently.

## Next executable action

After this reconciliation is green and merged, continue `RC-CTRL-001` only with an independently authored external empirical source that directly compares, challenges, replicates, or materially refines one or more represented side-effect mitigation mechanisms in harder or novel environments. Prefer head-to-head evidence across relative reachability, future-task preservation, AUP variants, or comparable impact regularization; reject conceptual-similarity-only additions and preserve external custody plus `authority_effect: NONE`.