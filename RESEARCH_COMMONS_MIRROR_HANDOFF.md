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

The 2026-09-15 continuation extended the existing Publisher-only reusable relation graph into a source-neutral Published Research Graph. This remains an extension of RC-008 under `RC-CTRL-001`; no separable child Goal Task was required because ownership, authority boundaries, validation, and repository destination remained the same.

## Durable prior state

Previously validated Research Commons implementation includes Publisher-paper registry/pages, Publisher relation records, reconciliation and deterministic indexes, duplicate detection, reuse request/decision and contributor-posture schemas, Site dispatch/acceptance contracts, fail-closed projection generation, and repository-native validation/drift workflows.

Historical Publisher-only validation remains recorded by PR #39 / workflow run `30743296790` / artifact `8832017929`.

## Published Research Graph extension — merged 2026-09-15

Implementation PR: `StegVerse-Labs/StegScholar#66`
Validated PR head: `6555f9dbd44074293382b3e4c479cbdde1578b50`
Merge SHA: `5daf590c4c439b3c425eca1ab25f359d85345de3`
Hosted validation: `Build and validate Research Commons` run `34992566832`, run number 65, conclusion `success`.
Additional exact-head checks: Test Readiness run `34992566835` success; Research Commons Control State run `34992566883` success; Architecture Neutral Admissibility run `34992566857` success; Independent Review run `34992566925` success.

The hosted Research Commons job proved JSON parsing, Publisher index build, Publisher validation, source-neutral Published Research Graph validation, duplicate detection, Site projection boundary validation, fail-closed dispatch build, Research Commons control-state validation, and validation-artifact upload all succeeded at the validated PR head.

Implemented surfaces:
- `research_commons/published_research_graph/schema.json`
- `research_commons/published_research_graph/graph.json`
- `research_commons/tools/validate_published_research_graph.py`
- `.github/workflows/build-and-validate-research-commons.yml`
- `README.md`

### Identity model

The graph separates document (`RC-DOC-*`), claim (`RC-CLM-*`), evidence (`RC-EVD-*`), and relation (`RC-REL-*`) identity. Document identity preserves source-native version identity and may carry DOI, canonical URL, and content hash. External published research requires at least one durable source locator from DOI, canonical URL, or content hash. Source custody remains with the source authority.

### Relation vocabulary

Supported relations are `cites`, `supports`, `corroborates`, `contradicts`, `challenges`, `extends`, `refines`, `replicates`, `fails_to_replicate`, `uses_method_from`, `uses_data_from`, `shares_evidence_with`, `derives_from`, `supersedes`, `independently_converges_with`, and `conceptually_related`.

Relations distinguish `explicit_source`, `human_asserted`, and `machine_discovered` assertion modes and `candidate`, `admitted`, `rejected`, and `superseded` states.

### Candidate/admitted invariant

Machine-discovered relations enter as `candidate` with pending review. A machine-discovered relation may become `admitted` only with accepted review evidence including reviewer identity and review time. The deterministic validator rejects machine-discovered admitted relations lacking that evidence.

Existing Publisher `related_to` records are projected only as `conceptually_related`; their meaning is not strengthened and the Publisher source relation file remains intact.

### Scientific and authority boundary

Every graph document and relation has `authority_effect: NONE`. A graph node or edge does not establish scientific truth, causation, priority/authorship, successful replication, publication standing/custody, reuse admissibility, governance authority, or execution authority. Graph admission means only that the relation record passed declared provenance/review requirements.

## First authentic external published-research ingestion — merged 2026-09-16

Implementation PR: `StegVerse-Labs/StegScholar#69`
Base head: `3db553c987671eb98c09e4e7c75fdfeb232aa0ef`
Validated PR head: `2f704c9a9712077f41da0517891ae17ee8c5aa00`
Merge SHA: `c330e774e3995248d07b299467e4227ae72a6239`
Hosted validation: `Build and validate Research Commons` run `35047331587`, run number 72, conclusion `success`.
Additional exact-head checks: Test Readiness run `35047331605` success; Independent Review run `35047331591` success; Architecture Neutral Admissibility run `35047331594` success.

Ingested external source:
- title: `Concrete Problems in AI Safety`
- authors: Dario Amodei, Chris Olah, Jacob Steinhardt, Paul Christiano, John Schulman, Dan Mané
- document identity: `RC-DOC-ARXIV-1606-06565`
- version identity: `arxiv:1606.06565v2`
- DOI: `10.48550/arXiv.1606.06565`
- canonical URL: `https://arxiv.org/abs/1606.06565`
- source custody: retained by arXiv/original authors
- authority effect: `NONE`

The external paper's Section 2 safe-exploration discussion explicitly identifies negative or irrecoverable consequences as a safety concern. The existing IICT Commons entry separately records irreversible commitment, preserved reconstructability, and a contradiction class involving reduced recoverability or review quality. The graph therefore records one bounded human-asserted `conceptually_related` edge between anchored claims/evidence without asserting support, derivation, equivalence, validation, or priority.

A second relation, `RC-REL-EXT-AISAFETY-IICT-CANDIDATE-001`, is machine-discovered `independently_converges_with`, confidence `0.68`, state `candidate`, review `pending`. It remains non-admitted.

Deterministic negative proof:
- fixture: `research_commons/published_research_graph/fixtures/invalid-machine-admitted-without-review.json`
- validator now accepts `--graph` for deterministic fixture evaluation
- workflow attempts to validate a machine-discovered relation marked `admitted` with pending/no reviewer evidence
- success criterion is validator failure with exact error: `machine-discovered admitted relation RC-REL-FIXTURE-UNREVIEWED-PROMOTION requires accepted review evidence`
- hosted run `35047331587` completed successfully, proving the workflow observed and required that rejection.

README now records the external exemplar and candidate-promotion negative fixture. No source custody, scientific authority, publication authority, governance authority, execution authority, or reuse-admissibility authority changed.

## Existing Site projection blocker

The pre-existing Site projection remains independently blocked pending Publisher reconciliation/authorization. This graph extension does not bypass or resolve that gate.

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

`RC-004` remains machine-owned source-drift observation. `RC-005` remains blocked Site projection. The source-neutral graph extension and first external ingestion are merged into `main` under `RC-CTRL-001`/RC-008. No competing handoff or child Goal Task was created.

No Site, admissibility-wiki, stegguardian-wiki, or master-records propagation is claimed by this repository-local ingestion.

## Archive conditions

The source-neutral graph extension and first external-source ingestion are repository-complete after expected-head-protected merges and hosted exact-head validation. Ongoing RC-004 and RC-005 repository-native states continue independently.

## Next executable action

Add a second external published source that either cites, challenges, refines, or empirically tests one of the graph's existing claims, then exercise cross-external-paper relation discovery and review while preserving candidate/admitted separation and source custody.
