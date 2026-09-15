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

`RC-004` remains machine-owned source-drift observation. `RC-005` remains blocked Site projection. The source-neutral graph extension is merged into `main` under `RC-CTRL-001`/RC-008. No competing handoff or child Goal Task was created.

No Site, admissibility-wiki, stegguardian-wiki, or master-records propagation is claimed by this completed repository-local extension.

## Archive conditions

The 2026-09-15 source-neutral graph implementation is repository-complete after merge and hosted exact-head validation. Archive/checkout of this bounded continuation is permissible once the post-merge handoff-only commit is observed green under the Research Commons control/build workflows; ongoing RC-004 and RC-005 repository-native states continue independently.

## Next executable action

Use the source-neutral graph ingestion contract to admit the first authentic external published-research document with DOI/canonical URL/content-hash provenance, then exercise an explicit relation and a machine-discovered candidate relation without promoting the candidate unless review evidence satisfies the admitted-state invariant.
