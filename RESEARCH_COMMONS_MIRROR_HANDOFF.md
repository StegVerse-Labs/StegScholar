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

The source-neutral graph implementation and first five external ingestions remain canonical. Both machine-discovered IICT independent-convergence candidates remain explicitly rejected after review; bounded `conceptually_related` edges remain the appropriate non-authorizing representation.

The fifth external ingestion, Eresheim, Kovac, and Adrowitzer, `Standing Still Is Not an Option: Alternative Baselines for Attainable Utility Preservation`, merged in PR #81 as `84ac557f72df0acf8778061e5b2b38e97337444f`; reconciliation PR #82 merged as `54dedec2c9b8f41fbf769f07e8c3a785591cdb4e`. Post-reconciliation Research Commons build/control runs `35097971975` and `35097971822` succeeded.

## Graph identity, relation, and authority invariants

The graph separates document (`RC-DOC-*`), claim (`RC-CLM-*`), evidence (`RC-EVD-*`), and relation (`RC-REL-*`) identity. External published research requires a durable locator. Source custody remains with the external source. Machine-discovered relations require review for admission or rejection. Every graph document and relation retains `authority_effect: NONE`; no graph edge establishes scientific truth, causation, priority/authorship, publication standing/custody, reuse admissibility, governance authority, or execution authority.

## Sixth authentic external published-research ingestion — validation pending

Implementation branch: `rc-ctrl-001-safelife-aup`
Base main head: `54dedec2c9b8f41fbf769f07e8c3a785591cdb4e`

External source:
- title: `Avoiding Side Effects in Complex Environments`
- authors: Alexander Matt Turner, Neale Ratzlaff, Prasad Tadepalli
- venue: NeurIPS 2020, Advances in Neural Information Processing Systems 33
- arXiv: `2006.06547v1`
- document identity: `RC-DOC-NEURIPS-2020-F50A6C02`
- canonical URL: `https://proceedings.neurips.cc/paper/2020/hash/f50a6c02a3fc5a3a5d4d9391f05f3efc-Abstract.html`
- source custody: NeurIPS proceedings / arXiv / original authors
- authority effect: `NONE`

Admission/evidence threshold:
- the paper is a NeurIPS 2020 published empirical evaluation rather than a conceptual-only proposal;
- it moves AUP from toy Gridworlds into SafeLife, contrasting dozens of states with billions, deterministic with stochastic dynamics, preset with randomly generated environments, one with many side-effect opportunities, and immediate effects with delayed chaotic effects;
- it evaluates AUP on four SafeLife tasks using a single learned auxiliary reward and compares against PPO, DQN, AUP projection, and naive baselines;
- it reports that AUP can complete the represented tasks while avoiding many side effects with modest overhead;
- it explicitly states a scalability limitation for state-reachability penalties: naive estimation of all reachability functions is quadratic in state-space size.

Bounded graph treatment:
- `RC-REL-SAFELIFE-REFINES-GRIDWORLDS-001` records material empirical refinement from the represented small deterministic Gridworlds regime into a much larger stochastic procedurally generated environment class; it does not claim replication or correction of all Gridworlds findings;
- `RC-REL-SAFELIFE-CHALLENGES-RR-SCALING-001` records a mechanism-specific challenge to scalability of the represented reachability-style approach; it does not dispute the earlier relative-reachability toy-environment result;
- no relation asserts equivalence among AUP, relative reachability, future-task preservation, or StegVerse IICT;
- conceptual-similarity-only sources are not admitted.

Source custody is additionally preserved in `research_commons/published_research_graph/sources/RC-DOC-NEURIPS-2020-F50A6C02.md`.

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

Exact-head hosted validation and expected-head-protected merge are required before the sixth ingestion is repository-complete.

## Cross-repository dependencies

- `GCAT-BCAT-Engine/Publisher`: publication custody, source catalog, and Publisher reconciliation authority.
- `StegVerse-Labs/StegScholar`: graph identity, provenance, relation lineage, review-state validation, and Research Commons graph custody.
- `StegVerse-Labs/Site`: projection acceptance/deployment only after its own orchestrator admission.
- `admissibility-wiki`, `stegguardian-wiki`, and `master-records`: no propagation asserted without a versioned destination contract and receipt.

## Coordination state

`RC-004` remains machine-owned source-drift observation. `RC-005` remains blocked Site projection. No competing handoff or child Goal Task has been created.

## Archive conditions

The sixth ingestion is not archiveable until its exact PR head passes Research Commons build/control validation, the PR merges with expected-head protection, post-merge validation is observed, and this handoff is reconciled with exact receipts. `RC-004` and `RC-005` continue independently.

## Next executable action

Open the bounded sixth-ingestion PR, validate the exact head, repair any failure without weakening provenance/relation semantics, merge only with expected-head protection, observe post-merge Research Commons build/control validation, then reconcile this handoff with exact head, workflow runs, merge SHA, and the next evidence threshold.
