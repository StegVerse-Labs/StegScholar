# Transition Table: Foundational Formalism

## Abstract

The Transition Table (TT) is the explicit representation layer for governed state change. It binds a pre-state, candidate transition, trigger, context, evidence, policy, authority, constraints, guard evaluation, governance result, commit-time state, action, post-state, observers, and receipts into a reconstructable transition cell.

TT follows Relational Transition Geometry (RTG) and Generalized Transition Governance (GTG): RTG describes the relational transition space; GTG determines admissibility and authority; TT records the bounded rule and resulting disposition.

## 1. Transition cell

Define a transition cell:

```text
c = (
  id,
  q-,
  tau,
  e,
  C,
  E,
  P,
  A,
  K,
  h,
  g,
  chi,
  a,
  q+,
  O,
  rho,
  pi,
  sigma,
  lambda
)
```

where:

- `id` is the stable cell identifier;
- `q-` is the pre-state;
- `tau` is the candidate transition;
- `e` is the triggering event;
- `C` is context;
- `E` is the evidence reference set;
- `P` is the policy reference set;
- `A` is the authority reference set;
- `K` is the constraint set;
- `h` is the guard result;
- `g` is the GTG result;
- `chi` is the commit-time reconstruction;
- `a` is the action or withheld action;
- `q+` is the resulting post-state;
- `O` is the observer/reviewer set;
- `rho` is the receipt set;
- `pi` is the predecessor relation;
- `sigma` is the correction or supersession relation;
- `lambda` is the scale parameter.

## 2. Evaluation function

```text
Eval(c_input) -> (h, g, a, q+, rho)
```

A structurally valid evaluator must always return an explicit result. Absence of a result cannot be interpreted as permission.

```text
undefined != ALLOW
ERROR != ALLOW
missing != ALLOW
```

## 3. Guard and governance separation

A guard answers whether declared local conditions are satisfied. GTG answers whether the candidate transition is admissible and authorized under the broader governance context.

```text
h = Guard(q-, e, C, E, K)
g = G(tau, q-, C, E, A, P, K, O, lambda, chi)
```

A passing guard does not imply an `ALLOW` result:

```text
h = PASS does not imply g = ALLOW
```

Likewise, a policy-compatible transition may still fail because authority or commit-time state is invalid.

## 4. Execution condition

```text
Executable(c) =
  [h = PASS]
  and [g = ALLOW]
  and CommitStateValid(chi)
  and AuthorityValid(A)
  and EvidenceBound(E)
  and ConstraintsSatisfied(K)
```

Only then may the action be enacted.

## 5. Outcome-complete table

A governed TT records more than successful transitions. Let:

```text
TT = C_allow union C_deny union C_fail_closed union C_defer union C_transform union C_error
```

A table that preserves only successful actions cannot reconstruct its governance behavior.

## 6. Historical immutability

Once a cell is committed as a historical receipt, it is immutable. Corrections create successor cells:

```text
c_j supersedes c_i
```

The predecessor remains available and retains its original time-indexed determination.

```text
correction != erasure
supersession != silent replacement
```

## 7. Continuity relation

For sequential cells:

```text
q+_i ~= q-_j
```

The equivalence may be exact, normalized, or scale-projected. The comparison rule must be declared.

Where the relation fails:

```text
q+_i !~= q-_j
```

one of the following must exist:

- an omitted transition cell;
- a scale translation;
- an external intervention;
- a corrupted receipt;
- a false state assertion.

Thus TT continuity checking can expose missing transition history.

## 8. Compound transitions

A compound transition contains subcells:

```text
c* = Compose(c_1, ..., c_n)
```

The composition rule must declare whether execution is:

- atomic;
- ordered;
- partially committable;
- compensating;
- quorum-bound;
- fail-closed on any subcell failure.

The compound result may not be reported as `ALLOW` if a required subcell did not satisfy its declared composition rule.

## 9. Concurrent transitions

For concurrent candidate transitions `tau_1` and `tau_2`, order may affect the result:

```text
Eval(tau_2 after tau_1) != Eval(tau_1 after tau_2)
```

The TT must preserve:

- ordering assumptions;
- shared resources;
- lock or quorum state;
- conflicting authority;
- observed commit order;
- aborted attempts.

## 10. Transform cells

A `TRANSFORM` result creates a new candidate transition rather than silently editing the original:

```text
c_i.g = TRANSFORM
c_i emits tau'
c_j evaluates tau'
```

The relation between `tau` and `tau'` must be receipted. This prevents hidden goal substitution.

## 11. Cross-scale projection

Let `A_(lambda->mu)` be an RTG scale map. A TT projection is valid only if declared invariants are preserved:

```text
Project(TT^lambda) -> TT^mu
```

with:

```text
Pi(TT^lambda) ~= Pi(TT^mu)
```

A coarse table may aggregate cells, but it may not convert a denied or failed-closed transition into an allowed transition without an explicit governance rule and successor record.

## 12. Receipt requirements

A minimal receipt should bind:

```text
receipt = (
  cell_id,
  evaluated_at,
  input_hashes,
  policy_hashes,
  authority_hashes,
  evaluator_id,
  guard_result,
  gtg_result,
  commit_state_hash,
  action_status,
  post_state_hash,
  predecessor_hash,
  signature_or_attestation
)
```

Cryptographic binding can establish integrity of recorded bytes; it does not establish semantic correctness, legitimacy, or valid standing by itself.

## 13. Falsification cases

A TT implementation should fail validation when it:

1. defaults a missing result to `ALLOW`;
2. executes with stale authority;
3. loses a `DENY` or `FAIL_CLOSED` attempt;
4. rewrites a historical cell in place;
5. cannot explain a state discontinuity;
6. collapses `TRANSFORM` into the original transition;
7. reports a compound `ALLOW` despite a required subcell failure;
8. omits commit-time reconstruction;
9. permits cross-scale projection to change outcome semantics silently;
10. produces receipts that cannot be deterministically linked.

## 14. Relationship to RTG and GTG

```text
RTG: describes possible and realized transition relationships.
GTG: determines admissibility, standing, and authority.
TT: records the exact governed state-change determination.
```

The three form a non-collapsing sequence:

```text
geometry != governance
governance != representation
representation != execution authority
```

## 15. Publication boundary

This document defines a research representation formalism. It does not claim that all physical, biological, computational, legal, or social processes can be completely represented by one transition-table schema without domain-specific extensions.