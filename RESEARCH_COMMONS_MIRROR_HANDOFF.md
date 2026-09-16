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

The source-neutral graph implementation and six external ingestions are canonical. Both machine-discovered IICT independent-convergence candidates remain explicitly rejected after review; bounded `conceptually_related` edges remain non-authorizing.

Every graph document and relation retains `authority_effect: NONE`. No graph edge establishes scientific truth, causation, priority/authorship, publication standing/custody, reuse admissibility, governance authority, or execution authority.

### Sixth external ingestion

Turner, Ratzlaff, and Tadepalli, `Avoiding Side Effects in Complex Environments`, NeurIPS 2020, arXiv `2006.06547v1`, is represented as `RC-DOC-NEURIPS-2020-F50A6C02` with source custody retained by NeurIPS proceedings / arXiv / original authors.

Bounded relations:
- `RC-REL-SAFELIFE-REFINES-GRIDWORLDS-001`: empirical refinement from small deterministic Gridworlds into substantially larger stochastic procedurally generated SafeLife environments.
- `RC-REL-SAFELIFE-CHALLENGES-RR-SCALING-001`: mechanism-specific challenge to reachability-penalty scalability; does not invalidate the earlier toy-environment RR result.

Implementation PR #83 exact head `5fb46e44318daeb9846643ec492be54d75b8bf7c` passed Research Commons build/control/Test Readiness runs `35101921005`, `35101920606`, and `35101920712` and merged with expected-head protection as `32d6db88c2f682ff44043394e0d547a8d0b35755`. Post-merge runs `35102021141`, `35102021136`, and `35102021124` passed.

Reconciliation PR #84 exact head `639927026ec0c47da1717f2e7ab2560fb493393a` passed runs `35102309409`, `35102309386`, and `35102309541` and merged with expected-head protection as `52b961c5cd34ecc06fcf79d42afba9bb5da8e5d3`. Post-reconciliation runs `35102355014`, `35102355044`, and `35102355193` passed.

A subsequent canonical integrity audit found a transcription defect in the preserved `RC-CLM-ARXIV-1711-09883-BASELINE-RESULT` digest. PR #85 restored the exact prior digest `sha256:ed8887f7e1b48fbd0e0904e04802a10d8f5536ceb428d21c5c849fc55bd64fab`; exact head `1a12f086a6da688befe4b8c464f17c11a5aacf52` passed runs `35102782020`, `35102782053`, and `35102781933`, merged with expected-head protection as `ba36d24eb7d81e7d4a83453692ad60dfdb12aa20`, and post-repair runs `35102827088`, `35102827035`, and `35102827030` passed.

Final handoff reconciliation PR #86 exact head `f1d862717fad6c2e2d0920830104f3d7c4c204df` passed runs `35102986260`, `35102986310`, and `35102986353`, merged with expected-head protection as `68f86889856f18f48d70ced726ba6f212b8309db`, and post-final runs `35103029308`, `35103029423`, and `35103029305` passed.

## Seventh-source frozen threshold

A seventh external graph source may be admitted only if it is independently authored and either:
- directly benchmarks at least two already represented side-effect mitigation mechanisms under the same environment/protocol; or
- independently reproduces or fails to reproduce one represented mechanism in a substantially different domain.

Prefer same-protocol quantitative AUP-vs-relative-reachability-vs-future-task evidence reporting both side-effect and task-performance outcomes. Reject conceptual-only extensions and do not weaken independence, reproduction, or domain-change semantics post hoc.

## Seventh-source screening pass — no admission

The screening record is `research_commons/published_research_graph/SEVENTH_SOURCE_SCREENING_NOTE.md`. The Published Research Graph itself is unchanged in this pass.

Rejected candidates:
- Vamplew, Foale, Dazeley, and Bignold (2021), `Potential-based multiobjective reinforcement learning approaches to low-impact agents for AI safety`, DOI `10.1016/j.engappai.2021.104186`: independent and empirical, and directly compares the authors' TLOA method with a learned Relative Reachability variant across four benchmark environments, but only RR is already represented, the RR implementation is modified, and the evaluation remains gridworld-style RL rather than a substantially different domain.
- Burden, Hernandez-Orallo, and O hEigeartaigh (2021), `Negative Side Effects and AI Agent Indicators: Experiments in SafeLife`: independent and quantitative, but evaluates DQN, PPO, and a random agent rather than AUP, RR, or future-task mitigation; therefore it does not reproduce or compare a represented mitigation mechanism.
- Lindner, Matoba, and Meulemans (2021), `Challenges for Using Impact Regularizers to Avoid Negative Side Effects`, arXiv `2101.12509`: independently authored and directly analyzes RR, attainable utility, and future-task approaches, but does not provide the required same-protocol empirical benchmark or different-domain reproduction.
- Turner, Hadfield-Menell, and Tadepalli (2020), `Conservative Agency via Attainable Utility Preservation`: directly benchmarks AUP against RR, but fails this continuation's frozen independence criterion because it is the AUP source family.

No scientific rejection beyond the stated continuation threshold is asserted. Screening disposition has `authority_effect: NONE` and cannot create or deny scientific, publication, governance, execution, or reuse authority.

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

The current screening-only branch must pass exact-head hosted validation before merge. Because the graph is intentionally unchanged, validation must confirm that the screening record and README/handoff changes do not alter graph identity, authority semantics, or Site projection state.

## Cross-repository dependencies

- `GCAT-BCAT-Engine/Publisher`: publication custody, source catalog, and Publisher reconciliation authority.
- `StegVerse-Labs/StegScholar`: graph identity, provenance, relation lineage, review-state validation, and Research Commons graph custody.
- `StegVerse-Labs/Site`: projection acceptance/deployment only after its own orchestrator admission.
- `admissibility-wiki`, `stegguardian-wiki`, and `master-records`: no propagation asserted without a versioned destination contract and receipt.

## Coordination state

`RC-004` remains machine-owned source-drift observation. `RC-005` remains blocked Site projection. No competing handoff or child Goal Task has been created.

## Archive conditions

This screening pass is archiveable only after its exact PR head passes the canonical Research Commons hosted validation set, merges with expected-head protection, post-merge build/control evidence is observed, and this handoff is reconciled with those exact receipts. The seventh external source remains unfilled; lack of a qualifying source is not permission to lower the frozen threshold.

## Next executable action

Continue source discovery for a genuinely independent empirical paper that clears the frozen seventh-source threshold. Prefer a same-protocol quantitative comparison of two or more represented mechanisms; otherwise require an actual independent reproduction or failure-to-reproduce of one represented mechanism in a substantially different domain. If no source clears the threshold, preserve `NO_ADMISSION` and add no graph node or relation.
