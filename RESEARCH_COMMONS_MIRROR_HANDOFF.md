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

Six external ingestions remain canonical. Seventh-source screening remains `NO_ADMISSION`; no new document, claim, evidence, or relation has been admitted. The Published Research Graph remains unchanged.

Every graph document and relation retains `authority_effect: NONE`. No graph edge establishes scientific truth, causation, priority/authorship, publication standing/custody, reuse admissibility, governance authority, or execution authority.

The sixth source remains Turner, Ratzlaff, and Tadepalli, `Avoiding Side Effects in Complex Environments` (NeurIPS 2020; arXiv `2006.06547v1`), represented as `RC-DOC-NEURIPS-2020-F50A6C02` with external NeurIPS/arXiv/original-author custody. Its bounded SafeLife refinement and reachability-scaling challenge remain unchanged.

The preserved Gridworlds baseline-result digest remains `sha256:ed8887f7e1b48fbd0e0904e04802a10d8f5536ceb428d21c5c849fc55bd64fab`.

## Seventh-source frozen threshold

A seventh external graph source may be admitted only if it is independently authored and either:
- directly benchmarks at least two already represented side-effect mitigation mechanisms under the same environment/protocol; or
- independently reproduces or fails to reproduce one represented mechanism in a substantially different domain.

Prefer same-protocol quantitative AUP-vs-relative-reachability-vs-future-task evidence reporting both side-effect and task-performance outcomes. Conceptual adjacency, comparison involving only one represented mechanism, or a modified related implementation in another gridworld-style benchmark does not satisfy this threshold by itself.

## Seventh-source screening — `NO_ADMISSION`

Screening record: `research_commons/published_research_graph/SEVENTH_SOURCE_SCREENING_NOTE.md`.

Previously screened and rejected for this specific threshold:
- Vamplew, Foale, Dazeley, and Bignold (2021), `Potential-based multiobjective reinforcement learning approaches to low-impact agents for AI safety`;
- Burden, Hernandez-Orallo, and O hEigeartaigh (2021), `Negative Side Effects and AI Agent Indicators: Experiments in SafeLife`;
- Lindner, Matoba, and Meulemans (2021), `Challenges for Using Impact Regularizers to Avoid Negative Side Effects`;
- Turner, Hadfield-Menell, and Tadepalli (2020), `Conservative Agency via Attainable Utility Preservation`.

The continuation screen added:
- Alizadeh Alamdari, Klassen, Toro Icarte, and McIlraith (2022), `Be Considerate: Avoiding Negative Side Effects in Reinforcement Learning`, AAMAS 2022. It is independently authored and empirical, explicitly situates its considerate-agent approach against RR/AUP/future-task work, and reports qualitative and quantitative gridworld experiments. It does not directly benchmark at least two already represented mitigation mechanisms under one protocol, and its experiments remain gridworld RL rather than a substantially different domain. It therefore does not independently reproduce or fail to reproduce a represented mechanism under the frozen second route.

These are screening dispositions only, not scientific rejections. They carry `authority_effect: NONE` and cannot create or deny scientific, publication, governance, execution, or reuse authority.

### Prior screening receipts

PR #87 exact head `9308b46df7dd0d224fcf3020aa1ba9e3cbfe8eee` passed Research Commons build/control/Test Readiness runs `35143573594`, `35143573400`, and `35143573475`, then merged with expected-head protection as `7e21ba38b3406a61faeafcb50f6aab1d777c598c`. Post-merge runs `35143624048`, `35143624082`, and `35143624100` passed.

Handoff reconciliation PR #88 exact head `b378ad5219e6ecb84cda312d6328b9921dc91a93` passed build/control/Test Readiness runs `35143777121`, `35143777182`, and `35143777206`, then merged with expected-head protection as canonical main `5506a721b67c28d5723d4130eb82636c853706af`. Post-reconciliation runs `35143814305`, `35143814316`, and `35143814344` passed.

No `graph.json` mutation occurred in either PR.

## Current continuation mutation

Branch: `rc-ctrl-001-seventh-source-screening-2`
Base main: `5506a721b67c28d5723d4130eb82636c853706af`
Scope: screening record plus canonical handoff only; `graph.json` must remain byte-for-byte unchanged by this continuation.

The current continuation is complete only after its exact PR head passes the canonical hosted validation set, merges with expected-head protection, post-merge build/control/Test Readiness evidence is observed, and this handoff is reconciled if receipts change.

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

## Cross-repository dependencies

- `GCAT-BCAT-Engine/Publisher`: publication custody, source catalog, and Publisher reconciliation authority.
- `StegVerse-Labs/StegScholar`: graph identity, provenance, relation lineage, review-state validation, and Research Commons graph custody.
- `StegVerse-Labs/Site`: projection acceptance/deployment only after its own orchestrator admission.
- `admissibility-wiki`, `stegguardian-wiki`, and `master-records`: no propagation asserted without a versioned destination contract and receipt.

## Coordination state

`RC-004` remains machine-owned source-drift observation. `RC-005` remains blocked Site projection. No competing handoff or child Goal Task has been created.

## Archive conditions

This continuation is archiveable only after exact-head hosted validation, expected-head-protected merge, and observed post-merge validation. Lack of a qualifying seventh source is not permission to lower the frozen threshold. `NO_ADMISSION` remains the correct fail-closed graph state until qualifying evidence exists.

## Next executable action

Continue `RC-CTRL-001` source discovery only for a genuinely independent empirical paper that clears the frozen seventh-source threshold. Do not re-screen candidates already recorded in `SEVENTH_SOURCE_SCREENING_NOTE.md`. Prefer a same-protocol quantitative comparison of two or more represented mechanisms; otherwise require an actual independent reproduction or failure-to-reproduce of one represented mechanism in a substantially different domain with explicit task-performance and side-effect outcomes. If no source clears the threshold, preserve `NO_ADMISSION`, leave the graph unchanged, and retain `authority_effect: NONE`.
