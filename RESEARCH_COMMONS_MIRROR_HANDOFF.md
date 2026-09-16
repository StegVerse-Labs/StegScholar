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

`RC-CTRL-001` owns governed Research Commons ingestion, research indexing and relation lineage, validation, reuse boundaries, and Site projection without transferring publication or scientific authority.

The source-neutral Published Research Graph and external-source ingestion remain extensions of RC-008 under `RC-CTRL-001`; no separable child Goal Task is required because ownership, authority boundaries, validation, and repository destination remain the same.

## Durable prior state

Historical Publisher-only validation remains recorded by PR #39 / workflow run `30743296790` / artifact `8832017929`.

Source-neutral graph implementation: PR #66, validated head `6555f9dbd44074293382b3e4c479cbdde1578b50`, merge `5daf590c4c439b3c425eca1ab25f359d85345de3`, Research Commons run `34992566832` success.

First external ingestion: PR #69, validated head `2f704c9a9712077f41da0517891ae17ee8c5aa00`, merge `c330e774e3995248d07b299467e4227ae72a6239`, Research Commons run `35047331587` success. It ingested Amodei et al., `Concrete Problems in AI Safety`, as `RC-DOC-ARXIV-1606-06565`, preserving DOI/canonical URL/version/source custody and `authority_effect: NONE`.

Second external ingestion: PR #72, validated head `e7614af5b42ef15b05a680264f6c5aa8281b2bf0`, merge `4f2463de23d64b0d1a9f049035fcb369c69a2466`, Research Commons run `35048696191` success. It ingested Leike et al., `AI Safety Gridworlds`, as `RC-DOC-ARXIV-1711-09883` and added explicit `cites`, bounded `extends`, conceptual-IICT, and machine-candidate edges.

Third external ingestion: PR #76, validated head `5d6b2a1ed0e022516c5dbe5a4fbef926c014b31a`, merge `a78e55950600a9b8fb50fe6ebde711729320e949`, Research Commons run `35092985117` success. It ingested Krakovna et al., `Avoiding Side Effects By Considering Future Tasks`, as `RC-DOC-ARXIV-2010-07877`, added explicit citations and a bounded `refines` relation to the Gridworlds side-effects mechanism/result, and rejected `RC-REL-GRIDWORLDS-IICT-CANDIDATE-001` after evidence review.

Reconciliation PR #78 merged as `6869e11a159bd3b685a78fc56a14f4411d73e912`; post-reconciliation Research Commons build run `35093263798` and control-state run `35093263729` both succeeded.

## Graph identity, relation, and authority invariants

The graph separates document (`RC-DOC-*`), claim (`RC-CLM-*`), evidence (`RC-EVD-*`), and relation (`RC-REL-*`) identity. External published research requires at least one durable locator from DOI, canonical URL, or content hash. Source custody remains with the external source.

Supported relations include `cites`, `supports`, `corroborates`, `contradicts`, `challenges`, `extends`, `refines`, `replicates`, `fails_to_replicate`, `uses_method_from`, `uses_data_from`, `shares_evidence_with`, `derives_from`, `supersedes`, `independently_converges_with`, and `conceptually_related`.

Machine-discovered relations require review for admission or rejection. `candidate` requires pending review; `admitted` requires accepted review plus reviewer identity/time; `rejected` requires rejected review plus reviewer identity/time. Every graph document and relation retains `authority_effect: NONE`. A graph node, edge, admission, or rejection does not establish scientific truth, causation, priority/authorship, publication standing/custody, reuse admissibility, governance authority, or execution authority.

## Remaining machine-candidate review — completed 2026-09-16

`RC-REL-EXT-AISAFETY-IICT-CANDIDATE-001` was reviewed against its retained evidence and rejected. The stronger `independently_converges_with` predicate is not supported because `Concrete Problems in AI Safety` and IICT establish only a bounded conceptual relationship around irrecoverability/recoverability; the retained sources do not establish independent development, priority, or convergence. The already-admitted `RC-REL-EXT-AISAFETY-IICT-001` `conceptually_related` edge remains unchanged and is the appropriate representation.

Review state records `state: rejected`, `review_state: rejected`, reviewer `RC-CTRL-001 evidence review`, and `authority_effect: NONE`. The review does not promote, validate, or discredit either underlying paper; it only rejects an over-strong graph predicate.

## Fourth authentic external published-research ingestion — merged 2026-09-16

Implementation PR: `StegVerse-Labs/StegScholar#79`
Implementation branch: `rc-ctrl-001-relative-reachability`
Base main head: `6869e11a159bd3b685a78fc56a14f4411d73e912`
Validated exact PR head: `7e6bc5e39966463d6ad970ecfb2e9d88c43db3fd`
Merge SHA: `28b469e1e040d67c10b795f8ad971c2377314963`
Expected-head protection: merge was performed against exact head `7e6bc5e39966463d6ad970ecfb2e9d88c43db3fd`.

Exact-head hosted validation:
- `Build and validate Research Commons` run `35093937158`, run number 98, success.
- `Validate Research Commons Control State` run `35093937423`, run number 600, success.
- `Test Readiness` run `35093937205`, run number 815, success.
- `Validate Independent Review` run `35093937263`, run number 46, success.
- `Validate Architecture Neutral Admissibility` run `35093937277`, run number 14, success.
- `Validate GTG Assurance Reference Integration` run `35093937390`, run number 9, success.
- `Validate GTG Assurance Consumer Compatibility Sweep` run `35093937208`, run number 9, success.

Post-merge main evidence at merge SHA `28b469e1e040d67c10b795f8ad971c2377314963`:
- `Build and validate Research Commons` run `35093980195`, run number 99, success.
- `Validate Research Commons Control State` run `35093980112`, run number 601, success.

External source:
- title: `Penalizing Side Effects using Stepwise Relative Reachability`
- authors: Victoria Krakovna, Laurent Orseau, Ramana Kumar, Miljan Martic, Shane Legg
- venue: AISafety@IJCAI 2019 / CEUR Workshop Proceedings Vol. 2419
- document identity: `RC-DOC-ARXIV-1806-01186`
- version identity: `aisafety-ijcai2019:ceur-vol-2419-paper-1;arxiv:1806.01186v2`
- DOI: `10.48550/arXiv.1806.01186`
- canonical URL: `https://ceur-ws.org/Vol-2419/paper_1.pdf`
- source custody: retained by CEUR-WS/arXiv/original authors
- authority effect: `NONE`

Source-grounded findings:
- the paper directly studies side-effect penalties in Gridworlds-style environments and separates the design into baseline-state and deviation-measure components;
- it shows a concrete failure mode for a simple reversibility penalty when task completion itself requires an irreversible action;
- it identifies interference and offsetting incentives introduced by some baseline choices;
- it reports that the stepwise inaction baseline combined with relative reachability avoids the represented failure modes in its gridworld experiments.

Graph relations:
- `RC-REL-RR-REFINES-GRIDWORLDS-001`: bounded `refines` relation to the Gridworlds reversibility mechanism/result because the later work decomposes the mechanism, exposes failure conditions, and evaluates a more specific alternative;
- `RC-REL-RR-CHALLENGES-REVERSIBILITY-PENALTY-001`: bounded mechanism-specific `challenges` relation because the paper demonstrates a failure mode for penalizing irreversibility alone when the objective requires irreversible action.

Neither relation claims that `AI Safety Gridworlds` as a whole is contradicted, replicated, or invalidated. The broader claim that irreversible side effects are a safety problem remains compatible with the new evidence.

This extends the provenance chain:
`Stepwise Relative Reachability`
→ `refines` / `challenges mechanism` → `AI Safety Gridworlds`
→ `cites` / `extends` → `Concrete Problems in AI Safety`
→ `conceptually_related` → StegVerse IICT recoverability.

The chain records relation lineage only and does not create support for IICT, scientific validation, publication authority, governance authority, execution authority, or reuse admissibility.

## Existing Site projection blocker

The pre-existing Site projection remains independently blocked pending Publisher reconciliation/authorization. This graph work does not bypass or resolve that gate.

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

The fourth external ingestion and remaining-machine-candidate review are repository-complete: the exact PR head passed Research Commons build/control and related hosted validation, PR #79 merged with expected-head protection, and the merge commit passed post-merge Research Commons build/control validation. This handoff reconciliation must itself pass hosted validation and merge before the bounded continuation is fully checked out. `RC-004` and `RC-005` continue independently and are not resolved by this work.

## Next executable action

After this reconciliation is green and merged, continue `RC-CTRL-001` only with an authentic external source that independently evaluates, replicates, challenges, or materially refines one of the now-represented side-effect mitigation mechanisms. Prefer an independently authored empirical evaluation of relative reachability, future-task preservation, attainable-utility-style impact regularization, or a comparable mechanism; do not add another source merely for conceptual similarity. Preserve source custody, typed relation semantics, and `authority_effect: NONE`, and do not infer support for StegVerse research from a multi-hop graph path.