# Research Commons Mirror Handoff

## Authority and scope

Canonical continuation record for the Research Commons workstream in `StegVerse-Labs/StegScholar`.

Goal Task ID: `RC-CTRL-001`
Canonical branch: `main`
Active implementation branch: `rc-ctrl-001-published-research-graph`
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

The 2026-09-15 continuation extends the existing Publisher-only reusable relation graph into a source-neutral Published Research Graph. This is an extension of RC-008 under the existing `RC-CTRL-001` workstream; no separable child Goal Task is required because ownership, authority boundaries, validation, and repository destination remain the same.

## Durable prior state

Previously validated Research Commons implementation includes:
- Publisher-paper registry and five Commons pages;
- nine Publisher relation records;
- reconciliation state and deterministic indexes;
- duplicate detection;
- reuse request/decision and contributor-posture schemas;
- Site dispatch and acceptance contracts;
- fail-closed projection generation;
- repository-native validation and drift workflows.

Prior hosted validation evidence remains:

```text
pull_request: 39
head_sha: 2eb5a024dca537c02cf1dc65b1c4b4a37e6c78a4
workflow: Build and validate Research Commons
run_id: 30743296790
conclusion: success
artifact_id: 8832017929
artifact_digest: sha256:ad1b972edb6d7913e3fc6c017b22cf0e451bfba0534fc321e05cdcc5a39b5c87
```

That evidence covers the historical Publisher projection only; it is not evidence for the 2026-09-15 Published Research Graph extension.

## Published Research Graph extension — 2026-09-15

Implementation branch starts from exact `main` head `81b79b760078f9e988814378d83a250bc0435065`.

Added:
- `research_commons/published_research_graph/schema.json`
- `research_commons/published_research_graph/graph.json`
- `research_commons/tools/validate_published_research_graph.py`
- Published Research Graph validation step in `.github/workflows/build-and-validate-research-commons.yml`
- README documentation for the source-neutral graph and authority boundaries.

### Identity model

The graph separates:
- document identity: stable `RC-DOC-*` identity plus source-native version identity and optional DOI, canonical URL, and content hash;
- claim identity: `RC-CLM-*` plus source locator and text digest;
- evidence identity: `RC-EVD-*` plus source locator and evidence class;
- relation identity: `RC-REL-*` plus typed subject/object relation, provenance, confidence, review state, and authority effect.

External published research must carry at least one durable source locator from DOI, canonical URL, or content hash. Source custody remains with the source authority.

### Relation vocabulary

Supported typed relations are:

```text
cites
supports
corroborates
contradicts
challenges
extends
refines
replicates
fails_to_replicate
uses_method_from
uses_data_from
shares_evidence_with
derives_from
supersedes
independently_converges_with
conceptually_related
```

Relations distinguish `explicit_source`, `human_asserted`, and `machine_discovered` assertion modes and `candidate`, `admitted`, `rejected`, and `superseded` states.

### Candidate/admitted invariant

Machine-discovered relations are not authoritative discoveries. They enter as `candidate` with pending review. A machine-discovered relation may be `admitted` only when accepted review evidence records reviewer identity and review time. The deterministic validator rejects a machine-discovered admitted relation lacking that review evidence.

Existing Publisher `related_to` records are projected only as `conceptually_related` and are not semantically strengthened. The source Publisher relation file remains intact.

### Scientific and authority boundary

Every graph document and relation has `authority_effect: NONE`.

A graph node or edge does not establish:
- scientific truth or correctness;
- causation;
- priority or authorship;
- successful replication;
- publication standing or publication custody;
- reuse admissibility;
- governance authority;
- execution authority.

Graph admission means only that the relation record passed the graph's declared provenance/review requirements.

## Existing Site projection blocker

The pre-existing Site projection remains independently blocked pending Publisher reconciliation/authorization. The Published Research Graph extension does not bypass or resolve that gate.

```text
dispatch_state: BLOCKED
blockers:
- projection_manifest_not_authorized
- sv-gcat-bcat-admissibility-2026: blocked_pending_source_reconciliation
- sv-god-framework-2026: blocked_pending_complete_source_record
authority_effect: NONE
```

Release sequence remains Publisher reconciliation -> Research Commons validation -> separate projection authorization -> Site review/admission -> deployment evidence -> public-path observation.

## Validation

Repository validation now includes:

```text
python research_commons/tools/build_publisher_indexes.py
python research_commons/tools/validate_publisher_papers.py
python research_commons/tools/validate_published_research_graph.py
python research_commons/tools/detect_duplicates.py
python research_commons/tools/validate_site_projection.py
python research_commons/tools/build_site_projection_dispatch.py
python research_commons/tools/check_research_commons_control_state.py
```

Do not claim this extension validated, merged, or released until exact-head GitHub Actions evidence is green and the PR is merged with expected-head protection.

## Coordination state

`RC-004` remains machine-owned source-drift observation. `RC-005` remains blocked Site projection. The source-neutral graph extension remains inside `RC-CTRL-001`/RC-008 and does not create a competing handoff or publication authority.

No propagation to `admissibility-wiki`, `stegguardian-wiki`, `master-records`, or Site is asserted by this branch.

## Next executable action

Open the implementation PR, obtain exact-head `Build and validate Research Commons` success, inspect failures if any, repair on the same branch, then merge only against the expected validated head. After merge, reconcile this handoff with the merge SHA and hosted run evidence.
