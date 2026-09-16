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

## Sixth authentic external published-research ingestion — merged 2026-09-16

Implementation PR: `StegVerse-Labs/StegScholar#83`
Implementation branch: `rc-ctrl-001-safelife-aup`
Base main head: `54dedec2c9b8f41fbf769f07e8c3a785591cdb4e`
Validated exact PR head: `5fb46e44318daeb9846643ec492be54d75b8bf7c`
Merge SHA: `32d6db88c2f682ff44043394e0d547a8d0b35755`
Expected-head protection: merge was performed against exact head `5fb46e44318daeb9846643ec492be54d75b8bf7c`.

Exact-head hosted validation:
- `Build and validate Research Commons` run `35101921005`, run number 116, success.
- `Validate Research Commons Control State` run `35101920606`, run number 612, success.
- `Test Readiness` run `35101920712`, run number 838, success.

Post-merge main evidence at `32d6db88c2f682ff44043394e0d547a8d0b35755`:
- `Build and validate Research Commons` run `35102021141`, run number 117, success.
- `Validate Research Commons Control State` run `35102021136`, run number 613, success.
- `Test Readiness` run `35102021124`, run number 839, success.

External source:
- title: `Avoiding Side Effects in Complex Environments`
- authors: Alexander Matt Turner, Neale Ratzlaff, Prasad Tadepalli
- venue: NeurIPS 2020, Advances in Neural Information Processing Systems 33
- arXiv: `2006.06547v1`
- document identity: `RC-DOC-NEURIPS-2020-F50A6C02`
- canonical URL: `https://proceedings.neurips.cc/paper/2020/hash/f50a6c02a3fc5a3a5d4d9391f05f3efc-Abstract.html`
- source custody: NeurIPS proceedings / arXiv / original authors
- authority effect: `NONE`

Source-grounded findings:
- the paper is an independently authored NeurIPS 2020 empirical evaluation rather than a conceptual-only proposal;
- it moves AUP from toy Gridworlds into SafeLife, contrasting dozens of states with billions, deterministic with stochastic dynamics, preset with randomly generated environments, one with many side-effect opportunities, and immediate effects with delayed chaotic effects;
- it evaluates AUP on four SafeLife tasks using a learned auxiliary reward and compares against PPO, DQN, AUP projection, and naive baselines;
- it reports that AUP can complete the represented tasks while avoiding many side effects with modest overhead;
- it identifies a scalability limitation for state-reachability penalties: naive estimation of all reachability functions is quadratic in state-space size.

Bounded graph treatment:
- `RC-REL-SAFELIFE-REFINES-GRIDWORLDS-001` records material empirical refinement from the represented small deterministic Gridworlds regime into a much larger stochastic procedurally generated environment class; it does not claim replication or correction of all Gridworlds findings;
- `RC-REL-SAFELIFE-CHALLENGES-RR-SCALING-001` records a mechanism-specific challenge to scalability of the represented reachability-style approach; it does not dispute the earlier relative-reachability toy-environment result;
- no relation asserts equivalence among AUP, relative reachability, future-task preservation, or StegVerse IICT;
- conceptual-similarity-only sources were not admitted.

Source custody is additionally preserved in `research_commons/published_research_graph/sources/RC-DOC-NEURIPS-2020-F50A6C02.md`, and the graph-local README summarizes the bounded sixth-source treatment.

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

The sixth ingestion is repository-complete at implementation/merge level: exact PR head validation passed, PR #83 merged with expected-head protection, and the merge commit passed post-merge Research Commons build/control/Test Readiness validation. This reconciliation must itself pass exact-head hosted validation and merge with expected-head protection before this bounded continuation is fully checked out. `RC-004` and `RC-005` continue independently.

## Next executable action

After this reconciliation is green and merged, continue `RC-CTRL-001` only with an independently authored empirical source that directly benchmarks at least two represented side-effect mitigation mechanisms under the same environment/protocol, or independently reproduces/fails to reproduce one represented mechanism in a substantially different domain. Prefer direct AUP-vs-relative-reachability-vs-future-task comparisons with quantitative side-effect and task-performance results; reject single-method conceptual extensions, preserve external custody plus `authority_effect: NONE`, and do not infer support for StegVerse research from graph lineage.
