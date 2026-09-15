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

Continuation-renewal and execution-to-consequence reconciliation remain part of the existing `TT_MIRROR_HANDOFF.md` workstream rather than duplicate Goal Tasks.

## Gate legitimacy formalism

`GATE-LEGITIMACY-INVARIANT-001` is the active first refinement selected from the completed Millings comparison. It tests whether governance needs a first-class, non-authorizing record for the legitimacy of the gate itself, separate from the admissibility of the candidate being evaluated.

Current source surfaces:
- `papers/transition-table/gate-legitimacy-invariant.md`
- `schemas/gate-legitimacy-record.schema.json`
- `fixtures/gate-legitimacy/gate-legitimacy-cases.json`
- `scripts/validate_gate_legitimacy.py`
- `tests/test_gate_legitimacy.py`

The model preserves governing-standard provenance, evidence-rule provenance and predeclaration, evaluator standing/conflicts, execution-path control, and challenge/review conditions. `GateLegitimate(g)` does not imply `CandidateAllowed(c)`: a legitimate gate can still deny a candidate on substantive grounds. The record has `authority_effect: NONE`; it cannot mint governance/execution authority, override GTG, or prove execution/consequence.

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
