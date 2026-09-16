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
8. `research_commons/published_research_graph/SEVENTH_SOURCE_SCREENING_NOTE.md`
9. issue #21, issue #37, and issue #38
10. `GCAT-BCAT-Engine/Publisher/docs/PUBLISHER_MIRROR_HANDOFF.md`
11. before any Site mutation, `StegVerse-Labs/Site/docs/SITE_MIRROR_HANDOFF.md`

## Active goal

`RC-CTRL-001` owns governed Research Commons ingestion, research indexing and relation lineage, validation, reuse boundaries, and Site projection without transferring publication or scientific authority. The source-neutral Published Research Graph remains an extension of RC-008 under this goal.

## Canonical graph state

Six external ingestions remain canonical. The seventh-source screening pass admitted no new document, claim, evidence, or relation. The Published Research Graph is unchanged by this pass.

Every graph document and relation retains `authority_effect: NONE`. No graph edge establishes scientific truth, causation, priority/authorship, publication standing/custody, reuse admissibility, governance authority, or execution authority.

The sixth source remains Turner, Ratzlaff, and Tadepalli, `Avoiding Side Effects in Complex Environments` (NeurIPS 2020; arXiv `2006.06547v1`), represented as `RC-DOC-NEURIPS-2020-F50A6C02` with external NeurIPS/arXiv/original-author custody. Its bounded SafeLife refinement and reachability-scaling challenge remain unchanged.

The prior sixth-source implementation/reconciliation/integrity-repair chain remains canonical through main `68f86889856f18f48d70ced726ba6f212b8309db`; the preserved Gridworlds baseline-result digest remains `sha256:ed8887f7e1b48fbd0e0904e04802a10d8f5536ceb428d21c5c849fc55bd64fab`.

## Seventh-source frozen threshold

A seventh external graph source may be admitted only if it is independently authored and either:
- directly benchmarks at least two already represented side-effect mitigation mechanisms under the same environment/protocol; or
- independently reproduces or fails to reproduce one represented mechanism in a substantially different domain.

Prefer same-protocol quantitative AUP-vs-relative-reachability-vs-future-task evidence reporting both side-effect and task-performance outcomes. Conceptual adjacency, comparison involving only one represented mechanism, or a modified related implementation in another gridworld-style benchmark does not satisfy this threshold by itself.

## Seventh-source screening pass — `NO_ADMISSION`

Screening record: `research_commons/published_research_graph/SEVENTH_SOURCE_SCREENING_NOTE.md`.

The pass screened and rejected for this specific admission threshold:
- Vamplew, Foale, Dazeley, and Bignold (2021), `Potential-based multiobjective reinforcement learning approaches to low-impact agents for AI safety`, DOI `10.1016/j.engappai.2021.104186`: independent and empirical, but only Relative Reachability is already represented in the head-to-head comparison, its RR implementation is modified, and the domain remains gridworld-style RL.
- Burden, Hernandez-Orallo, and O hEigeartaigh (2021), `Negative Side Effects and AI Agent Indicators: Experiments in SafeLife`: independent and quantitative, but evaluates DQN, PPO, and a random agent rather than a represented side-effect mitigation mechanism.
- Lindner, Matoba, and Meulemans (2021), `Challenges for Using Impact Regularizers to Avoid Negative Side Effects`, arXiv `2101.12509`: independent and directly analyzes RR, attainable utility, and future-task approaches, but does not provide the required same-protocol empirical benchmark or substantially different-domain reproduction.
- Turner, Hadfield-Menell, and Tadepalli (2020), `Conservative Agency via Attainable Utility Preservation`: directly compares AUP and RR, but fails this continuation's frozen independence criterion because it belongs to the AUP source family.

These are screening dispositions only, not scientific rejections. They carry `authority_effect: NONE` and cannot create or deny scientific, publication, governance, execution, or reuse authority.

### Screening implementation receipts

PR: `StegVerse-Labs/StegScholar#87`
Branch: `rc-ctrl-001-seventh-source-screening`
Base main: `68f86889856f18f48d70ced726ba6f212b8309db`
Validated exact head: `9308b46df7dd0d224fcf3020aa1ba9e3cbfe8eee`
Merge SHA: `7e21ba38b3406a61faeafcb50f6aab1d777c598c`
Expected-head protection: merge was performed against exact head `9308b46df7dd0d224fcf3020aa1ba9e3cbfe8eee`.

Exact-head hosted validation:
- `Build and validate Research Commons` run `35143573594`, run number 133, success.
- `Validate Research Commons Control State` run `35143573400`, run number 625, success.
- `Test Readiness` run `35143573475`, run number 860, success.

Post-merge main evidence at `7e21ba38b3406a61faeafcb50f6aab1d777c598c`:
- `Build and validate Research Commons` run `35143624048`, run number 134, success.
- `Validate Research Commons Control State` run `35143624082`, run number 626, success.
- `Test Readiness` run `35143624100`, run number 861, success.

No `graph.json` mutation occurred in PR #87. The pass adds only the screening record, graph-local README threshold/status, and canonical handoff state.

## Existing Site projection blocker

The pre-existing Site projection remains independently blocked pending Publisher reconciliation/authorization. This screening work does not bypass or resolve that gate.

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

This handoff-only reconciliation must pass exact-head hosted validation and merge with expected-head protection. Post-reconciliation build/control evidence must then be observed before checkout.

## Cross-repository dependencies

- `GCAT-BCAT-Engine/Publisher`: publication custody, source catalog, and Publisher reconciliation authority.
- `StegVerse-Labs/StegScholar`: graph identity, provenance, relation lineage, review-state validation, and Research Commons graph custody.
- `StegVerse-Labs/Site`: projection acceptance/deployment only after its own orchestrator admission.
- `admissibility-wiki`, `stegguardian-wiki`, and `master-records`: no propagation asserted without a versioned destination contract and receipt.

## Coordination state

`RC-004` remains machine-owned source-drift observation. `RC-005` remains blocked Site projection. No competing handoff or child Goal Task has been created.

## Archive conditions

The screening pass is repository-complete at implementation/merge level and has a durable `NO_ADMISSION` result. This final handoff reconciliation is archiveable only after its exact head passes the canonical hosted validation set, merges with expected-head protection, and post-reconciliation build/control evidence is observed. Lack of a qualifying seventh source is not permission to lower the frozen threshold.

## Next executable action

Continue `RC-CTRL-001` source discovery only for a genuinely independent empirical paper that clears the frozen seventh-source threshold. Prefer a same-protocol quantitative comparison of two or more represented mechanisms; otherwise require an actual independent reproduction or failure-to-reproduce of one represented mechanism in a substantially different domain. If no source clears the threshold, preserve `NO_ADMISSION` and add no graph node or relation.
