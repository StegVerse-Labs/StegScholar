# Transition Table Mirror Handoff

This file is the current source of truth for continuing Transition Table (TT) work in `StegVerse-Labs/StegScholar`.

## Current Goal

Formalize the Transition Table as the explicit, reconstructable representation layer that binds current state, triggering event, guards, authority, evidence, action, governance result, commit-time validity, consequence, transition identity, observer posture, and receipts into inspectable transition cells and bounded transition elements.

The canonical sequence is:

```text
RTG -> GTG -> TT
```

```text
RTG describes transition geometry and relational intersections.
GTG determines admissibility, standing, authority, and governance disposition.
TT records the exact transition rule, decision path, realized or withheld state change, consequence relation, observation posture, and bounded unresolved transition structure.
```

## Current Activation Goal

```text
Goal id: tt-canonical-transition-cell-v0.1
State: FOUNDATIONAL_FORMALISM_DRAFTING
Authority posture: research and representation formalism only; a table row or transition element does not create authority, truth, certification, execution permission, physical proof, or temporal ontology.
Manual task requirement: none for the consequence/observer extension installed below.
User manual action required: false.
```

## Source-of-Truth Boundaries

1. A TT cell represents a bounded transition determination; it does not itself grant standing.
2. Proposal-time and commit-time state must be distinguishable.
3. `ALLOW`, `DENY`, `FAIL_CLOSED`, `DEFER`, `TRANSFORM`, and `ERROR` must remain distinct.
4. Missing evidence, authority, policy, or reconstruction may not default to `ALLOW`.
5. Historical cells are immutable records; corrections and supersessions require linked successor cells.
6. A transition row must preserve both executed and withheld actions.
7. A deterministic table may still embody incorrect policy; structural validity is not substantive correctness.
8. Observer, reviewer, approver, executor, and reconstructor roles must be explicit.
9. Cross-scale projections require declared mappings and cannot silently alter cell semantics.
10. A row without a receipt is an assertion, not a reconstructable transition record.
11. No visible target-state change does not prove no transition occurred.
12. `NOT_OBSERVED` is independent of governance disposition and execution posture.
13. Black/unknown TT space is bounded unresolved transition structure, not empty space.
14. Distinct realized transitions require distinct complete identity-bearing signatures; individual scalar components need not be unique.
15. Primitive transition representation does not require a universal goal, persistence objective, observer-assigned timestamp, or metric duration.
16. Temporal attribution from reconstructed continuity is not proof that physical time is observer-dependent or nonexistent without observation.
17. Entropy/physical-inscription bookkeeping requires a declared implementation and system boundary; TT does not assert a universal exact entropy price or unique scalar thermodynamic fingerprint.

## Canonical Transition Cell

```text
TT_cell = (
  cell_id,
  subject_id,
  pre_state,
  candidate_transition,
  trigger,
  context,
  evidence_refs,
  policy_refs,
  authority_refs,
  constraints,
  guard_result,
  gtg_result,
  commit_state,
  action,
  post_state,
  consequence_ref?,
  transition_element_ref?,
  projection_relation?,
  observer_refs,
  receipt_refs,
  predecessor,
  supersedes,
  scale
)
```

The machine-readable cell schema is `schemas/tt-transition-cell.schema.json`.

## Consequence Semantics

For a fully specified deterministic action-plane condition `Omega`:

```text
R(Omega) = S_post
```

and:

```text
exists! S_post such that R(Omega) = S_post
```

`Consequence(Omega)` is the uniquely realized successor state under those exact declared parameters. This uniqueness claim is conditional on a complete deterministic model; stochastic or under-specified models must preserve their uncertainty.

Governance disposition is not identical to consequence. A disposition participates in reconciliation; consequence is the realized successor state.

## Projection-Preserving Transitions

TT explicitly permits:

```text
X_pre != X_post
and
P_target(X_pre) = P_target(X_post)
```

Therefore a `DENY` or `FAIL_CLOSED` may be a real transition even where the proposed target projection remains unchanged.

Observer equivalence is separately represented:

```text
X_pre ~_O X_post
iff
H_O(X_pre) = H_O(X_post)
```

so the following combinations are valid representation targets:

```text
DENY + NOT_OBSERVED
FAIL_CLOSED + NOT_OBSERVED
EXECUTED + NOT_OBSERVED
```

## Minimal / Black Transition Element

When evidence is insufficient for a complete TT cell, the bounded minimum is represented by `schemas/tt-transition-element.schema.json`:

```text
TE_min = (
  transition_id,
  existence_posture,
  pre_state_ref?,
  post_state_ref?,
  preserved_projection_refs,
  signature_evidence_refs,
  observation_posture,
  attribution_posture,
  unresolved_fields
)
```

The element may preserve `CONFIRMED`, `INFERRED`, or `UNKNOWN` transition-existence posture while refusing unsupported claims about action, cause, governance disposition, signature, or temporal order.

A black element is not evidence that nothing occurred. It is the strongest bounded statement that the transition relation or residue can support without fabricating missing structure.

## Transition Identity

TT adopts the complete-signature identity rule:

```text
Sigma(tau_i) = Sigma(tau_j)  =>  tau_i = tau_j
```

or equivalently:

```text
tau_i != tau_j  =>  Sigma(tau_i) != Sigma(tau_j)
```

This applies to the complete identity-bearing transition representation. Equal entropy, energy, action, or governance-result scalars do not collapse distinct transitions when another identity-bearing coordinate differs.

## Temporal Attribution Boundary

The bounded formal dependency installed for TT is:

```text
realized transition
-> observed or reconstructed relation
-> continuity ordering
-> temporal attribution by an observer/model
```

Goal and persistence are not primitive TT requirements. Persistence requires an identity rule across already-related states; a goal requires a declared preference/objective over states or transitions.

TT does not infer from this dependency that physical time is nonexistent without observers, and it does not claim metric duration or clock emergence.

## Physical Inscription Boundary

TT may bind evidence for physical or informational inscription and may separately reference resolution, target-change, and inscription costs under a declared system boundary.

This is bookkeeping and a research test surface, not a universal thermodynamic law. The stronger claims that every transition has an exact universal entropy price or a uniquely recoverable scalar entropy signature remain disallowed overclaims.

## Installed Consequence / Observer Extension

The following surfaces are installed on `main`:

```text
papers/transition-table/consequence-and-observer-semantics.md
papers/transition-table/formal-definitions.md       # sections 22-29 bind the extension
papers/transition-table/claims-register.md          # consequence, identity, observer, temporal, entropy claims
schemas/tt-transition-element.schema.json
schemas/tt-transition-cell.schema.json              # consequence/element/projection references
fixtures/tt/transition-element-cases.json
scripts/validate_tt_transition_elements.py
tests/test_tt_transition_elements.py
.github/workflows/validate-tt.yml
```

Deterministic installed cases currently cover:

- target-preserving invisible `DENY`;
- target-preserving invisible `FAIL_CLOSED`;
- inferred black transition with unresolved attribution and temporal order;
- invalid unknown-existence element that overclaims a concrete `DENY` disposition;
- explicit test that `DENY + NOT_OBSERVED` is valid representation;
- explicit test that unknown transition existence cannot silently assert `DENY`.

## Validation Evidence

`Validate Transition Table` GitHub Actions run `31931076534` completed successfully at commit:

```text
c952cdb906a4bc68593e2fe7b7e4e83fc4dd1e09
```

The workflow runs the dependency-free transition-element validator and the focused TT pytest suite. Earlier workflow attempts exposed a missing test-runner dependency; `.github/workflows/validate-tt.yml` was corrected to install `pytest`, after which run `31931076534` passed.

The handoff update itself should be followed by the workflow triggered from this commit; do not replace the successful `31931076534` evidence with a later run unless that run has itself completed successfully.

## Minimal Transition Rule

```text
(pre_state, trigger, guard) -> (result, action, post_state, receipt)
```

The minimal governed rule remains insufficient unless authority, evidence, policy, context, and commit-time reconstruction are recoverable either directly or by immutable reference. `TE_min` is a separate bounded representation for cases where full governed reconstruction is not supportable.

## Canonical Outcome Semantics

```text
ALLOW       -> action may proceed if commit-time state remains valid
DENY        -> action prohibited under evaluated conditions; target projection may remain invariant
FAIL_CLOSED -> action withheld because a required condition is absent or invalid; target projection may remain invariant
DEFER       -> action withheld pending a declared resolvable dependency
TRANSFORM   -> original action withheld; governed replacement candidate emitted
ERROR       -> evaluation failure; never equivalent to ALLOW
```

## Cell Evaluation

```text
cell_result = Evaluate(
  pre_state,
  candidate_transition,
  trigger,
  context,
  evidence_refs,
  policy_refs,
  authority_refs,
  constraints,
  scale
)
```

Commit-time execution requires:

```text
Execute(cell) only if:
  cell.gtg_result = ALLOW
  and cell.guard_result = PASS
  and CommitStateMatches(cell.commit_state)
  and AuthorityStillValid(cell.authority_refs)
  and EvidenceStillBound(cell.evidence_refs)
```

## Transition Table as Ledger

The TT is not merely a lookup table. It is a linked set of transition receipts and bounded transition elements whose ordering may be complete, partial, or unresolved depending on evidence.

For established continuity relations:

```text
cell_i.post_state ~= cell_j.pre_state
```

where any non-equivalence must be explained by an explicit intervening or scale-translation record.

A complete TT history preserves:

- admitted transitions;
- denied transitions;
- failed-closed attempts;
- deferred dependencies;
- transformations;
- evaluation errors;
- corrections;
- supersessions;
- observer and authority changes;
- unobserved but evidenced transitions;
- black/unknown transition loci without unsupported reconstruction;
- unresolved temporal order where evidence does not justify serialization.

## Immediate Work Queue

The consequence/observer/black-transition extension is installed and has a successful focused validation run. The broader TT v0.1 workstream remains active:

1. Complete canonical cell identity and immutable receipt linkage across the full TT schema.
2. Complete guard precedence and outcome determinism beyond the focused transition-element validator.
3. Complete proposal-time versus commit-time state fixtures.
4. Define and implement compound and concurrent transition cells.
5. Complete predecessor, successor, correction, and supersession semantics.
6. Complete cross-scale TT projection from RTG scale maps.
7. Add full transition-table schema in addition to the existing cell and minimal-element schemas.
8. Expand deterministic fixtures across all governance outcomes and new identity-collision cases.
9. Build the full TT validator for continuity, authority binding, receipt integrity, projection semantics, signature identity, and prohibited implicit `ALLOW` behavior.
10. Add TT falsification protocol and internal review receipt.

## Known Remaining Files and Destinations

```text
StegVerse-Labs/StegScholar:
- papers/transition-table/concurrency-and-compound-transitions.md
- papers/transition-table/falsification-protocol.md
- papers/transition-table/examples/
- schemas/tt-transition-table.schema.json
- expanded fixtures/tt/
- full scripts/validate_transition_table.py
- internal TT review receipt

StegVerse-Labs/admissibility-wiki:
- bounded formalism projection only after StegScholar claim review and destination handoff check

StegVerse-Labs/Site:
- public explanatory projection only after `docs/SITE_MIRROR_HANDOFF.md` grants scope

GCAT-BCAT-Engine/Publisher:
- canonical packaging and publication receipts only after `PUBLISHER_MIRROR_HANDOFF.md` grants scope
```

## Relationship to RTG and GTG

```text
RTG object:
  intersection translation and distributed event ledger

GTG object:
  governance function and admissible solution set

TT object:
  explicit cell or bounded transition element encoding the governed transition relation, consequence posture, observation/reconstruction posture, and receipts
```

A TT implementation must not flatten RTG geometry or GTG authority semantics into an unqualified state change.

## Release Boundary

The TT package is not ready for tagging or release. The consequence/observer extension is installed and focused-validation-backed, but broader release readiness still requires full-table schema and validator coverage, concurrency tests, correction and supersession tests, falsification criteria, cross-layer cases, and an internal review receipt.

## Handoff Instruction

Continue from this file before relying on prior chat context. TT work follows GTG and must preserve the distinctions among representation, authority, execution, consequence, observer visibility, transition identity, temporal attribution, and physical/thermodynamic claims.