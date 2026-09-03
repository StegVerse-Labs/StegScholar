# Governance-Native AI Epistemic Transition Definitions

## Status

Working definitions for issue #52. These are research terms, not canonical StegVerse ontology.

## Entity state

A representation of the condition of the governance-native entity at a given transition locus.

An entity state is not classified as correct or incorrect merely because an observer prefers another state.

## Transition

A realized or candidate relation between entity states.

This lane treats the existence of a realized transition separately from any observer-side evaluation of its desirability, expectedness, admissibility, or harm.

## Observer

Any entity or mechanism that forms a representation of a transition or consequence from a particular observance locus.

Observer state may be incomplete and is not presumed identical to entity state or environmental state.

## Observance locus

The location in the transition/consequence path from which a claim is formed.

Initial loci:

```text
L0: originating entity internal state
L1: egress / boundary crossing
L2: receiving-domain ingress
L3: receiving-domain state transition
L4: external / physical consequence
```

A claim proven at one locus MUST NOT be silently promoted to a stronger claim at another locus.

## Expectation

An observer-side prediction about a future or contemporaneous consequence.

Expectation is epistemic and does not by itself constrain transition truth.

## Desire

An observer-side preference over possible outcomes.

Desire is evaluative, not evidence that an undesired state was impossible or invalid.

## Demand

A declared requirement that an observer or governing context expects a consequence to satisfy.

Demand differs from transition truth. Demand satisfaction is evaluated after or against observance unless the demand is explicitly part of the entity's own transition structure.

## Preference

A ranking or weighting over outcomes or trajectories.

Preference can guide selection without converting non-preferred realized states into non-states.

## Consequence

A state change or externally meaningful effect attributable to a transition at a declared observance locus and system boundary.

Consequence claims require the observance locus to be explicit.

## Residual

A representation of divergence between an observer-side model and observed consequence.

For expectation `E` and observation `O`:

```text
R = Residual(E, O)
```

A non-zero residual is evidence of divergence, not automatic evidence of invalidity, lack of authority, or governance failure.

## Unknown variable

A variable whose existence or effect is not represented in the current model but is required to reconcile observed consequence with the model.

## Partially known variable

A represented variable whose value, range, causal relation, timing, coupling, or observability is incomplete.

## Model revision

A change to the observer's or entity's represented relationships based on new evidence, including residuals.

Model revision is one candidate mechanism for learning by error.

## Governance-native

A system is governance-native, for purposes of this research lane, when governance semantics participate in the structure that defines its state transitions rather than existing solely as an external approval wrapper around an otherwise unconstrained model.

This is a working definition and must be tested.

## Wrapper governance

A system arrangement in which an otherwise independent model proposes an action and a distinct governance system evaluates whether that action may proceed.

Wrapper governance may remain appropriate for non-native systems, cross-domain effects, tools, actuators, or receiving jurisdictions.

## Authority

A deliberately unsettled term in this lane.

Current research question:

```text
Is authority an intrinsic primitive of governance-native internal transitions,
or a relation introduced at observer, jurisdictional, resource, or consequence boundaries?
```

No answer is assumed.

## Admissibility

Also unsettled.

This lane will test whether admissibility is:

1. intrinsic to an entity's transition structure;
2. observer-relative evaluation;
3. boundary-specific acceptance;
4. or some combination that must not be collapsed into a universal permission step.

## Error

A term that MUST be qualified.

Possible meanings include:

- prediction error: expected consequence differs from observed consequence;
- measurement error: observation differs from underlying state;
- model error: represented relation is inconsistent with evidence;
- implementation defect: system behavior differs from its declared specification;
- preference failure: consequence differs from desired outcome;
- demand failure: consequence fails a declared requirement.

The lane MUST NOT use "error" as shorthand for "a reached state the observer dislikes."

## Harm

A consequence classification relative to a declared affected party, value function, safety boundary, or external criterion.

Harm may warrant consequence bounding while remaining analytically distinct from whether the underlying entity transition occurred.

## Consequence bounding

Mechanisms that limit external effect without necessarily suppressing epistemic divergence.

Examples include reversibility, resource ceilings, sandboxing, rate limits, financial exposure limits, actuator constraints, and receiving-domain acceptance conditions.

## Learning by error

A process in which divergence between model expectation and observed consequence contributes to model revision.

Minimum abstract sequence:

```text
prediction
-> transition
-> observation
-> residual
-> revision
```

The research lane will test whether governance architectures can preserve this sequence while bounding consequence.

## Open semantic conflicts with existing TT/GTG language

The following existing concepts require explicit comparison rather than silent reuse:

- `ALLOW`
- `DENY`
- `FAIL_CLOSED`
- authority references
- guard result
- governance disposition
- constraint violation
- commit-time validity

The question is not whether these concepts are useful. It is whether they are universal primitives of governance-native intelligence or constructs appropriate to wrapper governance and boundary control.
