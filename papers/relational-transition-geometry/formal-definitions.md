# Relational Transition Geometry — Formal Definitions

## Status

Research formalism draft. These definitions are model objects, not established universal physical laws.

## 1. Construct world-region

For construct `i`, define its realized world-region:

```text
W_i subseteq M x S_i x R_i
```

where `M` is the declared spacetime domain, `S_i` is the construct state space, and `R_i` is its relational participation state.

A world-region is not required to be point-like, sharply bounded, or static.

## 2. Intersection event

For participant set `P_k = {1,...,n}`:

```text
I_k = intersection_i W_i
```

`I_k` denotes the jointly realized region in which the participating constructs become mutually consequential. A nonempty geometric overlap alone is insufficient; the event must include a declared coupling or state-dependence relation.

## 3. Local states

For each participant:

```text
S_i^- = state immediately before the declared event boundary
S_i^+ = state immediately after the declared event boundary
```

The event boundary must specify temporal resolution and observer frame.

## 4. Intersection translation operator

```text
Theta_k : product_i S_i^- -> product_i S_i^+
```

`Theta_k` is the realized translation relation across the intersection. It may be deterministic, stochastic, partially observed, many-to-one, or non-identifiable.

A candidate operator must declare:

- domain and codomain;
- participant set;
- boundary conditions;
- scale;
- uncertainty model;
- conserved or approximately preserved quantities;
- admissible loss of detail.

## 5. Transition-cost vector

```text
kappa_k = (
  kappa_physical,
  kappa_informational,
  kappa_computational,
  kappa_temporal,
  kappa_governance
)
```

No universal unit is assumed across components. Comparison requires a declared normalization map.

## 6. Comparative event ledger

```text
Lambda_k = (
  event_id,
  participant_ids,
  {S_i^-},
  Theta_k,
  kappa_k,
  {S_i^+},
  correlations_k,
  observer_conditions,
  scale,
  uncertainty
)
```

`Lambda_k` is the comparative representation of the event, not necessarily a physically localized object.

## 7. Participant ledger projection

For participant `i`:

```text
L_i^k = pi_i(Lambda_k)
```

where `pi_i` is a participant-relative projection. Different participants may retain different, incomplete, or incompatible projections of the same event.

## 8. Reconstruction sufficiency

Given available projections `Q subseteq {L_i^k}`:

```text
Sufficient(Q, Lambda_k, epsilon)
```

holds when a declared reconstruction procedure recovers the required event invariants within tolerance `epsilon`.

This does not require recovery of every microstate.

## 9. Non-identifiability

An event is non-identifiable under observation set `O` when at least two materially distinct candidate operators remain observationally equivalent:

```text
Theta_a != Theta_b
and
Obs_O(Theta_a) ~= Obs_O(Theta_b)
```

within the declared tolerance.

## 10. Scale parameter

```text
lambda in Lambda
```

`lambda` indexes a declared resolution class. It may encode spatial, temporal, energetic, organizational, informational, or governance resolution, but its dimensions must be explicit.

## 11. Scale map

For scales `lambda` and `mu`:

```text
A_(lambda->mu) : X^(lambda) -> X^(mu)
```

A scale map may aggregate, project, coarse-grain, summarize, or otherwise transform a representation. It must declare what information is preserved, discarded, or made uncertain.

## 12. Invariant projection

```text
Pi : X -> J
```

where `J` is the declared invariant space. Candidate invariants may include causal ordering, conserved quantities, boundary crossings, authority lineage, transition sign, or correlation structure.

## 13. Cross-scale coherence

A candidate explanation is cross-scale coherent between `lambda` and `mu` when:

```text
Pi(A_(lambda->mu)(Theta^(lambda)(x)))
~=
Pi(Theta^(mu)(A_(lambda->mu)(x)))
```

within declared tolerance.

Strict equality is not required unless the scale map is lossless.

## 14. Missing intermediate transition

A missing intermediate transition is indicated when no admissible composition of declared scale maps and operators explains the observed coarse and fine ledgers within tolerance:

```text
not exists H such that
Pi(A_(lambda->mu) o H o Theta^(lambda))
~=
Pi(Theta^(mu) o A_(lambda->mu))
```

This indicates model incompleteness, not automatic discovery of a unique hidden mechanism.

## 15. Observer-relative horizon

For observer `o`, define an accessibility boundary:

```text
H_o = {events or state components not recoverably communicable to o after boundary crossing}
```

A comparative multi-ledger horizon occurs when reconstruction after crossing depends on transformed boundary, environmental, or correlated records rather than direct access to every participant ledger.

Use of gravitational event horizons remains an analogy unless a domain-specific equivalence is derived.

## 16. Identity update

A construct identity state may be modeled as transition-accreted:

```text
I_i(t+1) = I_i(t) plus Delta_i(Lambda_k)
```

where `Delta_i` is the participant-relative identity contribution of event `k`. This is a research representation, not a claim that all metaphysical identity is exhausted by ledger state.

## 17. Explanation admissibility

A candidate explanation `E` is admissible under evidence set `D` when it:

1. reproduces declared observations within tolerance;
2. preserves required invariants;
3. satisfies cost and boundary constraints;
4. remains coherent across declared scales;
5. exposes unresolved non-identifiability;
6. does not claim stronger uniqueness than the evidence supports.

## 18. Failure conditions

An RTG model fails its declared test when it:

- predicts a ledger component that is contradicted by observation;
- violates a required invariant;
- requires an impossible declared cost;
- hides non-identifiability;
- uses an undefined scale map;
- treats analogy as demonstrated equivalence;
- or cannot reproduce the specified cross-scale relation.
