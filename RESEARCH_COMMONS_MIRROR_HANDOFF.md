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

Prefer same-protocol quantitative AUP-vs-relative-reachability-vs-future-task evidence reporting both side-effect and task-performance outcomes. Conceptual adjacency, comparison involving only one represented mechanism, a modified related implementation in another gridworld-style benchmark, or an unrelated side-effect method in a different domain does not satisfy this threshold.

## Seventh-source screening — `NO_ADMISSION`

Screening record: `research_commons/published_research_graph/SEVENTH_SOURCE_SCREENING_NOTE.md`.

Already screened and excluded from re-screening:
- Vamplew, Foale, Dazeley, and Bignold (2021), `Potential-based multiobjective reinforcement learning approaches to low-impact agents for AI safety`;
- Burden, Hernandez-Orallo, and O hEigeartaigh (2021), `Negative Side Effects and AI Agent Indicators: Experiments in SafeLife`;
- Lindner, Matoba, and Meulemans (2021), `Challenges for Using Impact Regularizers to Avoid Negative Side Effects`;
- Turner, Hadfield-Menell, and Tadepalli (2020), `Conservative Agency via Attainable Utility Preservation`;
- Alizadeh Alamdari, Klassen, Toro Icarte, and McIlraith (2022), `Be Considerate: Avoiding Negative Side Effects in Reinforcement Learning`;
- `Adaptive querying for reward learning from human feedback` (Frontiers in Robotics and AI, 2025).

The 2025 adaptive-querying paper is independent and empirical and includes four simulation domains plus an in-person Kinova Gen3 7DoF robotic-arm study, but it evaluates adaptive human-feedback selection / reward learning rather than AUP, Relative Reachability, or future-task preservation. It therefore clears neither frozen admission route. This is a screening disposition only, not a scientific rejection, and carries `authority_effect: NONE`.

### Screening receipts through PR #91

PR #87 exact head `9308b46df7dd0d224fcf3020aa1ba9e3cbfe8eee` merged with expected-head protection as `7e21ba38b3406a61faeafcb50f6aab1d777c598c` after successful validation.
PR #88 exact head `b378ad5219e6ecb84cda312d6328b9921dc91a93` merged with expected-head protection as `5506a721b67c28d5723d4130eb82636c853706af` after successful validation.
PR #89 exact head `127e73d44a473d66d3d9f2489e074a24495c47da` passed build/control/Test Readiness runs `35165120112`, `35165119962`, and `35165120166`, merged as `88ea3a4e0e7105e0b29275d018d4b25432710a54`, and post-merge runs `35165150662`, `35165150628`, and `35165150607` passed.
PR #90 exact head `a4c82f3dc02c0163f5bb813c537937d763eab7d2` passed build/control/Test Readiness runs `35165223952`, `35165223872`, and `35165223849`, merged as `0b29bcb29a9324ea24c74cd4b0f56155da7fa357`, and post-merge runs `35165257283`, `35165257252`, and `35165257288` passed.
PR #91 exact head `a40c640db89f0caa96b45e323b3c5156b40f8a9a` passed build/control/Test Readiness runs `35166311192`, `35166311134`, and `35166311123`, merged with expected-head protection as `250e1a537aa1849b1a68216aa0fa2a20abc5c617`, and post-merge runs `35166344184`, `35166344241`, and `35166344175` passed.

No `graph.json` mutation occurred in these screening/reconciliation PRs.

## Current continuation mutation

Branch: `rc-ctrl-001-seventh-source-screening-3-reconcile`
Base main: `250e1a537aa1849b1a68216aa0fa2a20abc5c617`
Scope: handoff-only reconciliation; `graph.json` remains unchanged.

This continuation is fully checked out only after this reconciliation head passes the canonical hosted validation set, merges with expected-head protection, and post-merge build/control/Test Readiness evidence is observed.

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

This continuation is archiveable only after reconciliation exact-head hosted validation, expected-head-protected merge, and observed post-merge validation. Lack of a qualifying seventh source is not permission to lower the frozen threshold. `NO_ADMISSION` remains the correct fail-closed graph state until qualifying evidence exists.

## Next executable action

Continue `RC-CTRL-001` source discovery only for a genuinely independent empirical paper that clears the frozen seventh-source threshold. Do not re-screen candidates already recorded in `SEVENTH_SOURCE_SCREENING_NOTE.md`. Prefer a same-protocol quantitative comparison of two or more represented mechanisms; otherwise require an actual independent reproduction or failure-to-reproduce of one represented mechanism in a substantially different domain with explicit task-performance and side-effect outcomes. If no source clears the threshold, preserve `NO_ADMISSION`, leave the graph unchanged, and retain `authority_effect: NONE`.
