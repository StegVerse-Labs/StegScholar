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

## Graph identity, relation, and authority invariants

The graph separates document (`RC-DOC-*`), claim (`RC-CLM-*`), evidence (`RC-EVD-*`), and relation (`RC-REL-*`) identity. External published research requires at least one durable locator from DOI, canonical URL, or content hash. Source custody remains with the external source.

Supported relations include `cites`, `supports`, `corroborates`, `contradicts`, `challenges`, `extends`, `refines`, `replicates`, `fails_to_replicate`, `uses_method_from`, `uses_data_from`, `shares_evidence_with`, `derives_from`, `supersedes`, `independently_converges_with`, and `conceptually_related`.

Machine-discovered relations require review for admission. `candidate` requires pending review; `admitted` requires accepted review plus reviewer identity/time; `rejected` requires rejected review plus reviewer identity/time. Every graph document and relation retains `authority_effect: NONE`. A graph node, edge, admission, or rejection does not establish scientific truth, causation, priority/authorship, publication standing/custody, reuse admissibility, governance authority, or execution authority.

## Second authentic external published-research ingestion — validation pending

Implementation branch: `rc-ctrl-001-second-external-research`
Base main head: `e216da92c627672d5a91e4057a8120acd3baa10b`

External source:
- title: `AI Safety Gridworlds`
- authors: Jan Leike, Miljan Martic, Victoria Krakovna, Pedro A. Ortega, Tom Everitt, Andrew Lefrancq, Laurent Orseau, Shane Legg
- document identity: `RC-DOC-ARXIV-1711-09883`
- version identity: `arxiv:1711.09883v2`
- DOI: `10.48550/arXiv.1711.09883`
- canonical URL: `https://arxiv.org/abs/1711.09883`
- content hash: not asserted; authoritative PDF bytes were not independently retrieved for hashing in this execution
- source custody: retained by arXiv/original authors
- authority effect: `NONE`

Source-grounded graph relations:
- `RC-REL-GRIDWORLDS-CITES-CONCRETE-001`: explicit-source `cites` from `AI Safety Gridworlds` to `Concrete Problems in AI Safety`; the source text explicitly cites Amodei et al. 2016.
- `RC-REL-GRIDWORLDS-EXTENDS-SAFE-EXPLORATION-001`: bounded human-asserted `extends` relation because the later paper cites the earlier technical agenda, implements dedicated safety environments including safe exploration, and evaluates A2C/Rainbow; this records operationalization/empirical treatment, not proof or successful solution.
- `RC-REL-GRIDWORLDS-IICT-REVERSIBILITY-001`: bounded human-asserted `conceptually_related` relation between the Gridworlds irreversible-side-effects/reversibility discussion and IICT recoverability/reconstructability.
- `RC-REL-GRIDWORLDS-IICT-CANDIDATE-001`: machine-discovered `independently_converges_with`, confidence `0.74`, state `candidate`, review `pending`; it is not admitted.

Review-state fixtures:
- existing `invalid-machine-admitted-without-review.json` must fail validation;
- `valid-machine-promoted-after-review.json` must pass with accepted reviewer identity/time while retaining `authority_effect: NONE`;
- `valid-machine-rejected-after-review.json` must pass with rejected reviewer identity/time while retaining provenance and `authority_effect: NONE`.

README and `.github/workflows/build-and-validate-research-commons.yml` are updated on the implementation branch. Do not claim this second ingestion merged or validated until exact-head hosted validation succeeds and merge occurs with expected-head protection.

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

The graph architecture and first external ingestion are repository-complete. This second ingestion is not archive-ready until exact-head validation, expected-head-protected merge, and post-merge handoff reconciliation are recorded. Ongoing RC-004 and RC-005 repository-native states continue independently.

## Next executable action

Open the second-ingestion PR, obtain exact-head green Research Commons validation including promotion/rejection fixture checks, repair any failures on the same branch, merge only with expected-head protection, then reconcile this handoff with PR number, validated head, merge SHA, and post-merge main validation evidence.
