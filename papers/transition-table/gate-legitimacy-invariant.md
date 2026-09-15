# Gate Legitimacy as a Separate Governance Invariant

Status: Draft formalism under `GATE-LEGITIMACY-INVARIANT-001`

## Abstract

A governance system can have a visible gate and still fail to justify why that gate is entitled to decide. This note separates **candidate admissibility** from **gate legitimacy**. Candidate admissibility asks whether a proposed transition satisfies the governing requirements. Gate legitimacy asks whether the gate evaluating that candidate is itself grounded in inspectable standards, predeclared evidence rules, valid evaluator standing, disclosed conflicts, bounded execution-path control, and meaningful challenge/review conditions.

The distinction is intentionally non-authorizing. A gate-legitimacy record does not issue a governance disposition, create execution authority, or override RTG/GTG/TT. It supplies evidence that GTG may consume when determining whether a gate is fit to participate in a disposition.

## 1. Core distinction

Let `g` be a governance gate and `c` a candidate transition.

```text
GateLegitimate(g) != CandidateAllowed(c)
```

A legitimate gate may correctly return `DENY`, `DEFER`, `TRANSFORM`, or `FAIL_CLOSED` for a candidate that does not satisfy substantive requirements. Conversely, an illegitimate gate does not become legitimate because it happens to return a desirable result.

This prevents two common collapses:

1. treating a favorable disposition as proof that the decision surface was valid; and
2. treating the existence of a formal process as proof that the process was legitimately constituted.

## 2. Proposed gate-legitimacy record

A first-class record should preserve at least five independently inspectable dimensions.

### 2.1 Governing-standard provenance

The rule or standard applied by the gate must identify:

- the governing standard reference;
- provenance for that standard;
- the authority/standing under which it applies;
- whether competing standards create an unresolved conflict.

A missing or conflicted standard basis cannot be represented as `LEGITIMATE` merely because a candidate can still be evaluated mechanically.

### 2.2 Evidence-rule provenance and temporal binding

The gate must identify the evidence rule set used to evaluate candidates, including who controls that rule set and whether it was frozen before candidate-specific evaluation began.

A rule set that can be rewritten after the candidate's evidence is visible creates a post-hoc-selection risk. The record therefore includes an explicit `frozen_before_candidate_evaluation` predicate. A false predicate is a legitimacy failure for that evaluation event.

### 2.3 Evaluator standing and conflicts

The evaluator must expose:

- evaluator identity/reference;
- standing/reference for the evaluator's role;
- conflicts with the standard author/controller;
- conflicts with the evidence-rule controller;
- conflicts with the execution-path controller;
- any additional declared conflict references.

Conflict does not automatically imply corruption, but an undisclosed or unmitigated conflict prevents the gate from being represented as independently legitimate.

### 2.4 Execution-path control

A gate that evaluates a candidate and also unilaterally controls the path by which accepted or rejected outcomes are materialized may require stronger review evidence. The record therefore identifies execution-path control separately from evaluator identity.

This does not assert that role overlap is always invalid. It asserts that role overlap is material evidence and may require an independent review/mitigation reference before a `LEGITIMATE` state can be claimed.

### 2.5 Challenge and review conditions

The record distinguishes:

- whether a challenge path exists;
- whether independent review is required for the present conflict posture;
- whether that independent review has been satisfied;
- the evidence reference for that review when present.

This task does not define the full deterministic reviewer-independence predicate. That remains the separately registered `INDEPENDENT-REVIEW-PREDICATE-001` child. The gate-legitimacy record only exposes the dependency point so the later predicate can be integrated without changing the record's authority model.

## 3. Proposed state model

The bounded legitimacy state is:

```text
LEGITIMATE
ILLEGITIMATE
CONFLICTED
UNRESOLVED
```

Interpretation:

- `LEGITIMATE`: every required legitimacy predicate is satisfied for the recorded evaluation event.
- `ILLEGITIMATE`: at least one deterministic legitimacy predicate is violated, such as missing standard authority or post-hoc evidence rules.
- `CONFLICTED`: material role/control conflict exists and the required independent mitigation/review is not yet satisfied.
- `UNRESOLVED`: required evidence is absent or insufficient to determine legitimacy without asserting a violation that has not been established.

`UNRESOLVED` and `CONFLICTED` must not be promoted to `LEGITIMATE` by default.

## 4. Deterministic invariants

For a record to claim `LEGITIMATE`, all of the following must hold:

1. governing standard reference, provenance reference, and authority reference are present;
2. governing-standard status is `VALID`;
3. evidence rule set reference, provenance reference, and controller reference are present;
4. evidence rules were frozen before candidate-specific evaluation;
5. evidence-rule status is `VALID`;
6. evaluator reference and standing reference are present;
7. evaluator status is `VALID`;
8. execution-path reference and controller reference are present;
9. execution-path status is `VALID`;
10. if a material evaluator/control conflict exists, independent review is required and satisfied;
11. authority effect is exactly `NONE`.

If governing-standard provenance is missing or the standard authority is invalid, the expected state is `ILLEGITIMATE`.

If evidence rules were not frozen before candidate evaluation, the expected state is `ILLEGITIMATE`.

If a material control conflict exists and independent review is required but not satisfied, the expected state is `CONFLICTED`.

If required evidence is absent without proving a direct violation, the expected state is `UNRESOLVED`.

## 5. Relationship to RTG, GTG, and TT

### RTG

RTG may identify where a gate sits in the relation/transition geometry and which roles or systems intersect at that point. Gate legitimacy does not replace that geometry.

### GTG

GTG is the primary consumer candidate. GTG can treat the gate-legitimacy record as evidence when deciding whether a governance disposition is admissible. The record itself does not emit `ALLOW`, `DENY`, or any other GTG outcome.

A future integration may require a GTG rule such as:

```text
if required_gate_legitimacy_state != LEGITIMATE:
    disposition cannot default to ALLOW
```

This note does not install that rule into canonical GTG; it identifies the bounded integration point for falsification and review.

### TT

TT may reference the gate-legitimacy record in the evidence/policy/authority trail for a transition cell. TT records the resulting governance path, execution state, consequence relation, observation posture, and receipts; it does not infer gate legitimacy from a later successful consequence.

## 6. Falsification cases

The proposal should be rejected or revised if deterministic testing shows any of the following:

- standard provenance adds no independently testable information beyond existing authority references;
- evidence-rule temporal binding cannot be represented without duplicating an already-canonical primitive;
- conflict handling necessarily conflates gate legitimacy with reviewer independence or candidate admissibility;
- execution-path control cannot be represented without assigning authority to the record itself;
- the state model permits `LEGITIMATE` despite a failed required predicate;
- a legitimate gate cannot still represent a substantive candidate `DENY` without contradiction.

## 7. Adoption criteria

Adoption into the canonical transition model is warranted only if deterministic fixtures establish that the record catches failure classes not already represented by the current RTG/GTG/TT fields while preserving all authority separations.

Minimum acceptance evidence:

- valid baseline case;
- missing standard-provenance failure;
- post-hoc evidence-rule failure;
- evaluator/evidence-rule-controller conflict case;
- evaluator/execution-path-controller conflict case;
- legitimate-gate / candidate-denied case showing non-equivalence;
- validator proof that `authority_effect` cannot become authorizing.

## 8. Provenance boundary

This StegVerse formalism was derived as a refinement candidate after the provenance-preserving Millings Method comparison. The independently authored Millings Method is not represented as the source of StegVerse RTG, GTG, TT, or the exact schema/validator mechanics defined here.
