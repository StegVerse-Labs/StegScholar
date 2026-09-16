# StegScholar

StegScholar is the scholarly research repository for StegVerse.

This repository tracks:
- Peer-review research papers
- Submission history and outcomes
- Figures and diagrams
- Reading lists and prior work
- Evolving research primitives and terminology
- Governed Research Commons Wiki entries

## Research Commons Wiki

The `research_commons/` directory is the governed discovery and synthesis layer for research artifacts that contributors explicitly authorize StegVerse to retain, index, or publish.

It preserves provenance, consent, license terms, knowledge posture, disagreement, corrections, retractions, and reuse lineage. Shared research is not automatically public, validated, reusable, or accepted as true.

First exemplar: `research_commons/topics/TIDC-001/`.

## Published Research Graph

`research_commons/published_research_graph/` is the source-neutral relation layer for StegVerse and external published research. It assigns stable document, claim, evidence, and relation identities while preserving source custody and version provenance.

Document identity may retain DOI, canonical URL, content hash, and source-native version identity. Relations are typed and evidence-bearing, with explicit provenance, confidence, review state, and `authority_effect: NONE`.

Machine-discovered relations must enter as `candidate`; they cannot become `admitted` without accepted review evidence. A machine-discovered rejection must likewise retain rejected review evidence. Explicit source relations may be admitted without implying scientific truth. No graph edge establishes causation, priority, replication, publication authority, governance authority, execution authority, or reuse admissibility.

The current Publisher-paper relation set remains intact under `research_commons/sources/publisher-papers/`; the Published Research Graph generalizes that capability instead of replacing Publisher custody.

The first external exemplar is Amodei et al., *Concrete Problems in AI Safety* (`arXiv:1606.06565v2`, DOI `10.48550/arXiv.1606.06565`). Its source custody remains external. A bounded evidence-backed conceptual relation connects its safe-exploration discussion of irrecoverable consequences to the existing IICT recoverability/reconstructability claim. The stronger machine-discovered `independently_converges_with` candidate has now been reviewed and rejected because the retained sources establish conceptual correspondence but do not establish independent development, priority, or convergence.

The second external exemplar is Leike et al., *AI Safety Gridworlds* (`arXiv:1711.09883v2`, DOI `10.48550/arXiv.1711.09883`). The source explicitly cites *Concrete Problems in AI Safety*, operationalizes safety problems as reinforcement-learning environments, includes safe exploration and irreversible side effects, and reports baseline evaluation of A2C and Rainbow. The graph records an explicit `cites` edge and a bounded `extends` edge to the first external paper, plus a non-authorizing conceptual relation to IICT recoverability. The stronger machine-discovered `independently_converges_with` candidate has now been reviewed and rejected because the retained evidence supports conceptual correspondence but does not establish independent convergence.

The third external exemplar is Krakovna et al., *Avoiding Side Effects By Considering Future Tasks* (NeurIPS 2020; `arXiv:2010.07877v1`, DOI `10.48550/arXiv.2010.07877`). The published paper explicitly cites both *AI Safety Gridworlds* and *Concrete Problems in AI Safety*, formalizes interference incentives, introduces a future-task auxiliary reward with a baseline policy, and reports gridworld evidence that the method avoids the tested side effects and interference more effectively than a reversibility penalty. The graph records this as a bounded `refines` relation to the Gridworlds irreversible-side-effects mechanism/result, not as a replication of all Gridworlds findings. Together with the existing Gridworlds-to-Concrete and Concrete-to-IICT edges, this creates a provenance-preserving multi-hop external-to-external-to-StegVerse research chain without changing scientific or governance authority.

The fourth external exemplar is Krakovna et al., *Penalizing Side Effects using Stepwise Relative Reachability* (AISafety@IJCAI 2019; `arXiv:1806.01186v2`, DOI `10.48550/arXiv.1806.01186`). The paper uses AI Safety Gridworlds-based experiments to separate side-effect penalty design into baseline-state and deviation-measure choices, shows a concrete failure mode for penalizing irreversibility alone when the task itself requires irreversible action, and reports that the stepwise inaction baseline combined with relative reachability avoids the represented interference, offsetting, and effectiveness failures. The graph therefore records both a bounded `refines` edge and a mechanism-specific `challenges` edge to the Gridworlds reversibility treatment; neither edge claims replication of the full benchmark or contradiction of the broader safety problem.

Validation:

```text
python research_commons/tools/validate_published_research_graph.py
```

The workflow requires the unreviewed-promotion fixture to fail, and separately requires reviewed promotion and reviewed rejection fixtures to pass. Review changes graph relation state only; it does not create scientific, publication, governance, execution, or reuse-admissibility authority.

## External-framework comparisons

StegScholar may host provenance-preserving comparisons between independently authored external frameworks and StegVerse research formalisms. Functional convergence must not be represented as shared authorship, derivation, certification, or technical identity.

Completed comparison:
- `papers/external-frameworks/millings-method-rtg-gtg-tt-comparison.md`
- terminal handoff: `MILLINGS_METHOD_RTG_GTG_TT_COMPARISON_MIRROR_HANDOFF.md`
- refinement disposition: `papers/external-frameworks/millings-method-refinement-disposition.md`

Derived refinement tasks:
- `GATE_LEGITIMACY_INVARIANT_MIRROR_HANDOFF.md`
- `ARCHITECTURE_NEUTRAL_ADMISSIBILITY_MIRROR_HANDOFF.md`
- `INDEPENDENT_REVIEW_PREDICATE_MIRROR_HANDOFF.md`

All three Millings-derived refinement tasks are now complete. Continuation-renewal and execution-to-consequence reconciliation remain part of the existing `TT_MIRROR_HANDOFF.md` workstream rather than duplicate Goal Tasks.

## Gate legitimacy formalism

`GATE-LEGITIMACY-INVARIANT-001` completed the first Millings-derived refinement. The validated formalism establishes gate legitimacy as a first-class, non-authorizing evidence invariant separate from the admissibility of the candidate being evaluated.

Canonical source surfaces:
- `papers/transition-table/gate-legitimacy-invariant.md`
- `schemas/gate-legitimacy-record.schema.json`
- `fixtures/gate-legitimacy/gate-legitimacy-cases.json`
- `scripts/validate_gate_legitimacy.py`
- `tests/test_gate_legitimacy.py`

The model preserves governing-standard provenance, evidence-rule provenance and predeclaration, evaluator standing/conflicts, execution-path control, and challenge/review conditions. Deterministic fixtures cover missing standard provenance, post-hoc evidence-rule mutation, evaluator/evidence-rule-controller overlap, evaluator/execution-path-controller overlap, independently mitigated conflict, and the legitimate-gate / candidate-DENY separation.

`GateLegitimate(g)` does not imply `CandidateAllowed(c)`. The record has `authority_effect: NONE`; it cannot mint governance/execution authority, override GTG, or prove execution/consequence.

## Independent review predicate

`INDEPENDENT-REVIEW-PREDICATE-001` completed the second bounded Millings-derived refinement. The validated formalism distinguishes merely available review from structurally independent review. Existing Governable Autonomy review labels remain useful declarations, but independent-review status must be supported by evidence across common control, challenged-rule authorship/control, material financial interest, reviewer/original-evaluator identity, and execution-path control.

Canonical source surfaces:
- `papers/transition-table/independent-review-predicate.md`
- `schemas/independent-review-record.schema.json`
- `fixtures/independent-review/independent-review-cases.json`
- `scripts/validate_independent_review.py`
- `tests/test_independent_review.py`

The deterministic predicate preserves these separations:

```text
review_available != independent_review_available
reviewer_identity_label != reviewer_independence_proof
IndependentReview(r) != GovernanceAuthority(r)
```

`UNRESOLVED` never defaults to independence, and disclosed conflict is not treated as mitigation by itself. The record has `authority_effect: NONE` and cannot mint transition authority or override GTG.

## Architecture-neutral admissibility

`ARCHITECTURE-NEUTRAL-ADMISSIBILITY-001` completed the third bounded Millings-derived refinement. Architectural nonconformity cannot be the sole denial basis when a candidate independently satisfies the same governing requirement through valid evidence.

Canonical source surfaces:
- `papers/generalized-transition-governance/architecture-neutral-admissibility.md`
- `schemas/architecture-neutral-admissibility-record.schema.json`
- `fixtures/architecture-neutral-admissibility/cases.json`
- `scripts/validate_architecture_neutral_admissibility.py`
- `tests/test_architecture_neutral_admissibility.py`

```text
ArchitectureDifferent(c) != SubstantivelyInadmissible(c)
ConformityOnlyDenial(c) = INVALID_DENIAL_BASIS
ArchitectureNeutrality(c) != ALLOW(c)
```

Evidence, authority, standing, safety/constraints, policy, and commit-time failure remain valid substantive denial grounds. Unresolved required state fails closed. The record has `authority_effect: NONE`.

## Post-completion GTG/TT compatibility review

`GTG-TT-MILLINGS-FORMALISM-COMPATIBILITY-REVIEW-001` reviewed the three retired formalisms against the current GTG decision/governance schemas and TT transition-cell schema.

The review found one material integration gap: GTG had generic evidence/challenge references but no typed, correlation-checked binding identifying which gate-legitimacy, independent-review, or architecture-neutrality record applies to the exact governance decision. TT already has the correct ownership relationship through `gtg_record_ref`, so duplicating those assurance records into TT would create drift rather than deterministic value.

Review surfaces:
- `papers/rtg-gtg-tt/millings-derived-formalism-compatibility-review.md`
- `GTG_TT_MILLINGS_FORMALISM_COMPATIBILITY_REVIEW_MIRROR_HANDOFF.md`

The minimum derived implementation task is `GTG-ASSURANCE-REFERENCE-INTEGRATION-001`, with handoff `GTG_ASSURANCE_REFERENCE_INTEGRATION_MIRROR_HANDOFF.md`.

## GTG assurance reference integration

`GTG-ASSURANCE-REFERENCE-INTEGRATION-001` implements the compatibility-review result as an additive, non-authorizing GTG surface.

Implementation surfaces:
- `schemas/gtg-governance-assurance.schema.json`
- `schemas/gtg-decision.schema.json`
- `schemas/gtg-governance-record.schema.json`
- `fixtures/gtg-assurance-reference-integration/cases.json`
- `scripts/validate_gtg_assurance_reference_integration.py`
- `tests/test_gtg_assurance_reference_integration.py`
- `.github/workflows/validate-gtg-assurance-reference-integration.yml`

`governance_assurance` is optional in both GTG schemas, preserving historical records that predate the integration. Profiles declare `required_types`; required unresolved assurance fails closed in deterministic validation, while absent optional or `NOT_APPLICABLE` assurance does not create a false failure. Each binding is typed and correlation-checked against the active candidate/gate/rule/evaluator context, and both the binding and referenced source record must retain `authority_effect: NONE`.

The integration does not alter GTG disposition ownership. A valid Architecture-Neutral Admissibility record cannot force `ALLOW`, Gate Legitimacy cannot mint authority, and Independent Review does not become a second governance authority.

TT remains intentionally unchanged: `schemas/tt-transition-cell.schema.json` has no `governance_assurance` field. Cross-layer reconstruction follows only `gtg_record_ref`, preventing independently mutable duplicate assurance state in TT.

## GTG assurance consumer compatibility sweep

`GTG-ASSURANCE-CONSUMER-COMPATIBILITY-SWEEP-001` is retired after deterministically demonstrating one compatibility defect: the legacy `scripts/validate_gtg_fixtures.py:validate_case` serializer dropped optional `governance_assurance` from emitted `GTG-DECISION-*` receipts. No authority promotion or duplicate TT assurance field was observed.

Historical sweep surfaces:
- `papers/rtg-gtg-tt/gtg-assurance-consumer-compatibility-sweep.md`
- `scripts/validate_gtg_assurance_consumer_compatibility_sweep.py`
- `tests/test_gtg_assurance_consumer_compatibility_sweep.py`
- `GTG_ASSURANCE_CONSUMER_COMPATIBILITY_SWEEP_MIRROR_HANDOFF.md`

## GTG assurance receipt preservation

`GTG-ASSURANCE-RECEIPT-PRESERVATION-001` is complete and retired. StegScholar PR #75 repaired the legacy fixture serializer so emitted receipts preserve the exact optional `governance_assurance` object when present, omit it when absent, require `authority_effect: NONE`, and compute `receipt_hash` after preservation. Exact implementation head `d540be925ea6ad54b8fe8dcde2dc328d09eb9caa` passed the GTG, assurance-reference, compatibility-sweep, readiness, independent-review, and architecture-neutral validation workflows before merging as `c75b579fdf8261cb6fcba96d4d0b3cc3b4be3954`.

Repair surfaces:
- `scripts/validate_gtg_fixtures.py`
- `tests/test_gtg_assurance_receipt_preservation.py`
- `tests/test_gtg_assurance_consumer_compatibility_sweep.py`
- `scripts/validate_gtg_assurance_consumer_compatibility_sweep.py`
- `GTG_ASSURANCE_RECEIPT_PRESERVATION_MIRROR_HANDOFF.md`

The repair does not modify GTG activation/disposition algebra or the TT schema. Historical no-assurance receipts remain structurally compatible, and TT continues to use only `gtg_record_ref` for cross-layer reconstruction. The retired parent sweep remains closed and retains the pre-fix evidence that justified this bounded repair.

## Research Themes
- Trust as a system state
- Auditability and irrecoverable audit loss
- Credential lifecycle failures
- Boundary-condition autonomy
- Survivable governance under uncertainty
- Technology-induced discovery clustering
- Governed research reuse and research commons economics

## Design Principles
- Papers are standalone and composable
- No paper depends on StegVerse as a platform
- StegVerse serves only as an existence proof
- Terminology is stable, versioned, and reusable
- Consent is granular and separate from publication
- Shared research preserves disagreement and uncertainty
- Prior research requires a new admissibility review before reuse
- External-framework comparisons preserve independent provenance and distinguish convergence from equivalence

## Status
This repository is actively maintained and expanded as research progresses.