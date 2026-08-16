# Transition Table — Consequence and Observer Semantics

## Status

Canonical working extension to the Transition Table (TT) research formalism. This document defines consequence, transition identity, projection-preserving transitions, observer-relative visibility, black/unknown transition space, and temporal attribution. It is a research and representation formalism only; it does not create execution authority or assert a new physical law of time.

## 1. Primitive transition

A realized transition is written:

```text
S_a --tau--> S_b
```

The primitive transition does not require a goal, persistence predicate, observer-assigned timestamp, or metric duration in order to be represented as a transition.

Goal, persistence, and temporal coordinates are additional relations or attributes that may be introduced only when their own standing is established.

## 2. Complete reconciliation condition

Let the action-plane input condition be:

```text
Omega = (S_pre, proposed_action, governance_context, action_constraints,
         admissibility_context, evidence, authority, policy, scale, other_declared_parameters)
```

For a fully specified deterministic model, the reconciliation operator is:

```text
R(Omega) = S_post
```

with exactly one realized successor under those exact parameters:

```text
exists! S_post such that R(Omega) = S_post
```

This uniqueness is conditional on the declared model being complete and deterministic. Unresolved, stochastic, or under-specified models MUST NOT be coerced into this uniqueness claim.

## 3. Consequence

**Consequence** is the uniquely realized successor state that satisfies the complete reconciliation of the proposed action with the governing, admissibility, state, and declared contextual conditions at the action-plane crossing.

```text
Consequence(Omega) = S_post
```

Counterfactual alternatives require changing at least one member of `Omega` or changing the model.

A governance disposition is not itself the consequence. `ALLOW`, `DENY`, `FAIL_CLOSED`, `DEFER`, `TRANSFORM`, and `ERROR` describe parts of the reconciliation. The consequence is the realized successor state produced by that reconciliation.

## 4. Full state and projections

A TT state MAY be modeled as a tuple of projections:

```text
X = (X_target, X_governance, X_record, X_observer, X_environment, ...)
```

A transition may change the full state while preserving one or more projections.

Define projection `P_k` over state `X`.

A **projection-preserving transition** satisfies:

```text
X_pre != X_post
and
P_k(X_pre) = P_k(X_post)
```

This relation is first-class TT structure.

## 5. DENY and FAIL_CLOSED are transitions

A `DENY` or `FAIL_CLOSED` result MUST NOT be represented as absence of transition merely because the proposed target transformation was withheld.

A target-preserving denial may satisfy:

```text
X_pre != X_post
P_target(X_pre) = P_target(X_post)
GTG_result = DENY
```

A target-preserving fail-closed transition may satisfy:

```text
X_pre != X_post
P_target(X_pre) = P_target(X_post)
GTG_result = FAIL_CLOSED
```

The full successor state differs because the proposal was evaluated and resolved, even when the target projection remains observationally unchanged.

## 6. Observer-relative equivalence

Let observer `O` have observation map:

```text
H_O : X -> Y_O
```

Two states are observationally equivalent for `O` when:

```text
X_a ~_O X_b  iff  H_O(X_a) = H_O(X_b)
```

Therefore a real transition may satisfy both:

```text
X_pre != X_post
H_O(X_pre) = H_O(X_post)
```

This is an **unobserved transition for observer O**, not a no-transition event.

Observability and governance disposition are independent axes. The TT MUST permit, among other combinations:

```text
DENY + NOT_OBSERVED
FAIL_CLOSED + NOT_OBSERVED
EXECUTED + NOT_OBSERVED
```

## 7. Minimal transition element

When evidence supports transition existence but not full reconstruction, TT MAY record a minimal transition element:

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

Required semantics:

```text
existence_posture in {CONFIRMED, INFERRED, UNKNOWN}
observation_posture in {OBSERVED, PARTIAL, NOT_OBSERVED, UNKNOWN}
attribution_posture in {KNOWN, BOUNDED, UNRESOLVED}
```

A minimal element MUST NOT assert an action, cause, governance result, temporal position, or unique reconstruction that is not supported by evidence.

## 8. Black and unknown transition space

A **black transition element** is a minimal element for which enough residue exists to preserve a transition locus or transition-existence claim, while the transition geometry remains insufficiently identifiable.

Formally, evidence `E` may support:

```text
P(exists tau | E) >= eta_exist
```

while no specific candidate meets the attribution threshold:

```text
for every candidate tau_i:
P(tau = tau_i | E) < eta_attr
```

The probability notation is illustrative; implementations MAY use deterministic evidence classes instead.

Black/unknown space is not empty space. It is bounded unresolved transition structure.

## 9. Transition signature and identity

Every distinct realized transition MUST be distinguishable in the complete transition representation by at least one identity-bearing coordinate.

Define complete transition signature:

```text
Sigma(tau) = (
  transition_id,
  pre_state_relation,
  post_state_relation,
  continuity_position,
  reconciliation_relation,
  physical_or_informational_inscription_refs,
  causal_lineage,
  declared_scale,
  other_identity_bearing_coordinates
)
```

Identity axiom:

```text
Sigma(tau_i) = Sigma(tau_j)  =>  tau_i = tau_j
```

Equivalently:

```text
tau_i != tau_j  =>  Sigma(tau_i) != Sigma(tau_j)
```

This does not require every scalar component of a signature to be unique. Two transitions may have equal measured energy use, entropy production, action type, or governance result while remaining distinct in the complete signature.

Observer projections may collapse distinct signatures:

```text
Sigma(tau_i) != Sigma(tau_j)
while
H_O(Sigma(tau_i)) = H_O(Sigma(tau_j))
```

## 10. Physical inscription and entropy boundary

A realized physical transition requires physical instantiation. TT MAY bind evidence of physical or informational inscription to a transition element.

The research model distinguishes:

```text
Sigma_resolution   = cost associated with evaluating/resolving the transition
Sigma_target       = cost associated with the proposed target transformation
Sigma_inscription  = cost associated with recording/propagating distinguishability
```

These symbols are bookkeeping placeholders, not a claim that a universal exact entropy price has been established for every transition.

For a target-preserving `DENY` or `FAIL_CLOSED`, `Sigma_target` for the proposed target transformation may be absent or zero under the declared boundary while resolution/inscription costs remain nonzero.

The stronger proposition that every transition has a uniquely recoverable thermodynamic signature is NOT established and MUST NOT be inferred from transition identity.

## 11. Continuity and temporal attribution

The TT separates transition occurrence from observer-relative reconstruction of order.

A useful dependency relation is:

```text
realized transition
-> observed or reconstructed relation
-> continuity ordering
-> temporal attribution by an observer/model
```

Once observer `O` establishes an ordered relation:

```text
S_a <_O S_b
```

it MAY assign a temporal coordinate `T_O` such that:

```text
T_O(S_a) < T_O(S_b)
```

This is a formal statement about temporal attribution from reconstructed continuity. It does NOT assert that physical time is nonexistent without observers, nor does it claim metric clock emergence.

An unobserved or black transition may therefore have:

```text
exists tau
and
Order_O(tau) = UNKNOWN
```

Later reconstruction may establish its relative order without changing the historical fact that the transition occurred before it was reconstructed.

## 12. Persistence and goal are non-primitive

Persistence requires comparison across related states and an identity rule for the allegedly persistent object. It is therefore not primitive to transition definition.

A goal requires a declared preference, objective, target, or selection rule among states or transitions. It is likewise not primitive to transition definition.

The TT MUST NOT explain primitive transition occurrence by assuming a universal goal or universal persistence objective unless an external theory explicitly provides and evidences that claim.

## 13. Required non-equivalences

```text
no visible target change != no transition
NOT_OBSERVED != no transition
DENY != no transition
FAIL_CLOSED != no transition
transition identity != unique entropy scalar
transition occurrence != temporal attribution
continuity reconstruction != creation of the historical transition
persistence != primitive transition requirement
goal != primitive transition requirement
```

## 14. Implementation consequences

TT schemas and validators SHOULD support:

- projection-preserving transitions;
- explicit transition-existence posture;
- observer-relative observation posture;
- unresolved/black transition elements;
- transition signature references and identity-bearing fields;
- explicit unknown temporal ordering;
- prohibition on inferring no-transition from unchanged target projection;
- prohibition on inferring temporal position, action, cause, or governance disposition from insufficient evidence.

## 15. Scientific boundary

This extension formalizes representation semantics and research hypotheses. It does not establish a new thermodynamic law, a universal entropy quantum for transitions, a uniquely recoverable entropy fingerprint, a metaphysical goal for reality, or a physical proof that time emerges from observation.