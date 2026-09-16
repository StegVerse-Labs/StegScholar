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

## Graph identity, relation, and authority invariants

The graph separates document (`RC-DOC-*`), claim (`RC-CLM-*`), evidence (`RC-EVD-*`), and relation (`RC-REL-*`) identity. External published research requires at least one durable locator from DOI, canonical URL, or content hash. Source custody remains with the external source.

Supported relations include `cites`, `supports`, `corroborates`, `contradicts`, `challenges`, `extends`, `refines`, `replicates`, `fails_to_replicate`, `uses_method_from`, `uses_data_from`, `shares_evidence_with`, `derives_from`, `supersedes`, `independently_converges_with`, and `conceptually_related`.

Machine-discovered relations require review for admission or rejection. `candidate` requires pending review; `admitted` requires accepted review plus reviewer identity/time; `rejected` requires rejected review plus reviewer identity/time. Every graph document and relation retains `authority_effect: NONE`. A graph node, edge, admission, or rejection does not establish scientific truth, causation, priority/authorship, publication standing/custody, reuse admissibility, governance authority, or execution authority.

## Third authentic external published-research ingestion — validation pending

Implementation branch: `rc-ctrl-001-future-tasks-refinement`
Base main head: `d244907a00e41e83dc3b3aae68441744cafc99f0`

External source:
- title: `Avoiding Side Effects By Considering Future Tasks`
- authors: Victoria Krakovna, Laurent Orseau, Richard Ngo, Miljan Martic, Shane Legg
- venue: NeurIPS 2020, Advances in Neural Information Processing Systems 33
- document identity: `RC-DOC-ARXIV-2010-07877`
- version identity: `neurips2020:dc1913d422398c25c5f0b81cab94cc87;arxiv:2010.07877v1`
- DOI: `10.48550/arXiv.2010.07877`
- canonical URL: `https://proceedings.neurips.cc/paper/2020/hash/dc1913d422398c25c5f0b81cab94cc87-Abstract.html`
- content hash: not asserted; proceedings PDF bytes were inspected through the external proceedings surface but not independently retained as source custody
- source custody: retained by NeurIPS/arXiv/original authors
- authority effect: `NONE`

Source-grounded findings:
- the NeurIPS paper explicitly cites `Concrete Problems in AI Safety` and `AI Safety Gridworlds` in references [2] and [13];
- it formalizes interference incentives, introduces a future-task auxiliary reward and baseline policy, and proves the no-interference result only for the stated deterministic setting;
- it reports gridworld experiments in which the future-task method with a baseline avoids the tested side effects/interference and is more effective than a reversibility penalty on the represented setup;
- therefore `RC-REL-FUTURETASKS-REFINES-GRIDWORLDS-001` is a bounded human-asserted `refines` relation, not a claim that the paper replicated all Gridworlds results.

Multi-hop chain now represented:
`Avoiding Side Effects By Considering Future Tasks`
→ `refines` / `cites` → `AI Safety Gridworlds`
→ `cites` / `extends` → `Concrete Problems in AI Safety`
→ `conceptually_related` → StegVerse IICT recoverability.

This chain records provenance and relation lineage only. It does not create support for IICT, scientific validation of StegVerse research, publication authority, governance authority, execution authority, or reuse admissibility.

## Reviewed machine-candidate disposition

`RC-REL-GRIDWORLDS-IICT-CANDIDATE-001` was reviewed on this continuation and changed from machine-discovered `candidate` / pending review to `rejected` with reviewer identity/time retained. The stronger `independently_converges_with` predicate was rejected because the retained evidence supports conceptual correspondence but does not establish independent development or convergence. The already-admitted bounded `conceptually_related` edge remains the appropriate relation.

`RC-REL-EXT-AISAFETY-IICT-CANDIDATE-001` remains a separate pending machine candidate and was not silently promoted or rejected.

Deterministic fixtures from PR #72 remain the review-state proof surfaces:
- unreviewed machine admission must fail;
- reviewed machine promotion must pass;
- reviewed machine rejection must pass;
- unreviewed machine rejection must fail.

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

Hosted exact-head validation and expected-head-protected merge are still required before this third ingestion may be described as merged or repository-complete.

## Cross-repository dependencies

- `GCAT-BCAT-Engine/Publisher`: publication custody, source catalog, and Publisher reconciliation authority.
- `StegVerse-Labs/StegScholar`: graph identity, provenance, relation lineage, review-state validation, and Research Commons graph custody.
- `StegVerse-Labs/Site`: projection acceptance/deployment only after its own orchestrator admission.
- `admissibility-wiki`, `stegguardian-wiki`, and `master-records`: no propagation asserted without a versioned destination contract and receipt.

## Coordination state

`RC-004` remains machine-owned source-drift observation. `RC-005` remains blocked Site projection. No competing handoff or child Goal Task has been created.

## Archive conditions

The third external ingestion is not archiveable while PR validation or merge evidence is pending. It becomes repository-complete only after the exact PR head is green under the Research Commons build/control workflows, the PR is merged with expected-head protection, the canonical handoff records the validated head and merge SHA, and post-merge main validation is observed. Ongoing `RC-004` and `RC-005` repository-native states continue independently and do not become resolved by this ingestion.

## Next executable action

Obtain exact-head hosted validation for PR #76, repair any remaining validation failure without weakening graph/review invariants, merge only with expected-head protection, then update this handoff with validated head, workflow runs, merge SHA, and post-merge main evidence.
