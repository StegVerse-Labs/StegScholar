# Transition Table — Formal Definitions

## Status

Canonical working definitions for the TT research volume. These definitions specify representation and validation semantics; they do not create execution authority.

## 1. Transition cell

A transition cell is:

```text
T_c = (
  cell_id,
  pre_state_ref,
  trigger,
  proposal_ref,
  evidence_refs,
  relational_projection,
  authority_and_standing,
  policy_and_constraint_refs,
  guards,
  gtg_activation,
  gtg_disposition,
  commit_state_ref,
  action,
  post_state_ref,
  observer_refs,
  receipt_refs,
  predecessor_refs,
  supersession_ref,
  scale
)
```

A cell is a typed record. Its presence does not prove that execution occurred.

## 2. Cell phases

A cell may pass through:

```text
PROPOSED
EVALUATED
COMMIT_READY
COMMITTED
EXECUTED
OBSERVED
RECONSTRUCTED
SUPERSEDED
FAILED
```

Every phase change must be explicit. Missing phases may not be inferred from later visibility.

## 3. Guards

A guard is a predicate:

```text
g_j : Context -> {TRUE, FALSE, UNKNOWN, ERROR}
```

A required guard must evaluate `TRUE` before commit. `UNKNOWN` and `ERROR` may not default to `TRUE`.

## 4. Decision validity

```text
DecisionValid(T_c) =
  [gtg_disposition in declared outcome set]
  and [authority_and_standing reconstructable]
  and [required evidence present]
  and [policy and constraints current]
  and [all required guards typed]
```

Decision validity is not execution validity.

## 5. Commit validity

```text
CommitValid(T_c, t_c) =
  DecisionValid(T_c)
  and [gtg_disposition = ALLOW]
  and [commit_state_ref reconstructs current state]
  and [all commit guards = TRUE]
  and [execution authority valid at t_c]
```

## 6. Execution record

```text
X_c = (
  cell_id,
  executor,
  execution_start,
  execution_end,
  applied_action,
  execution_environment,
  observed_effects,
  failure_state,
  artifact_hashes
)
```

An execution record must not be synthesized from an intended action alone.

## 7. Observation record

```text
O_c = (
  cell_id,
  observer,
  observation_time,
  observed_state,
  method,
  uncertainty,
  standing,
  evidence_refs
)
```

No observation is equivalent to an explicit `NOT_OBSERVED` state, not to success.

## 8. Receipt bundle

```text
R_c = (
  decision_receipt,
  commit_receipt,
  execution_receipt,
  observation_receipt,
  reconstruction_receipt,
  correction_and_supersession_refs
)
```

A bundle may be partial. Completeness must be declared.

## 9. State continuity

For predecessor cell `T_a` and successor cell `T_b`:

```text
Continuous(T_a, T_b) =
  [T_a.post_state_ref = T_b.pre_state_ref]
  or [declared translation record bridges them]
```

A hash match proves byte identity only, not semantic continuity.

## 10. Compound transition

For ordered cells:

```text
C = T_1 ; T_2 ; ... ; T_n
```

A compound transition is valid only when every adjacency is continuous, every required disposition remains valid at its commit boundary, and failure behavior is declared.

## 11. Atomic compound transition

```text
Atomic(C) = all cells commit or none become effective
```

Atomicity must be evidenced by the execution environment; it may not be claimed from table structure alone.

## 12. Concurrent transitions

For cells `T_a` and `T_b` sharing state or resources:

```text
Concurrent(T_a, T_b)
```

requires declared conflict, serialization, commutativity, merge, or fail-closed semantics.

A commutativity claim requires:

```text
Apply(T_a, Apply(T_b, S)) ~= Apply(T_b, Apply(T_a, S))
```

under declared invariants and tolerance.

## 13. Transform cell

When GTG returns `TRANSFORM`:

```text
T_original -> T_replacement
```

The replacement must preserve references to the original proposal, transformation authority, changed intent surface, and independent GTG evaluation.

## 14. Historical immutability

A committed historical cell is not edited to express a later truth.

```text
T_c^(n+1) supersedes T_c^n
```

Corrections and supersessions preserve the prior cell and explain the change.

## 15. Scale projection

For scale map `A_(lambda->mu)`:

```text
Project(T_c^lambda) = T_c^mu
```

A projection must declare which fields, invariants, and receipts are preserved, aggregated, hidden, or made uncertain.

## 16. Reconstruction

```text
Reconstruct(R_c) -> T_hat_c
```

A reconstruction result must identify:

- recovered fields;
- asserted but unverified fields;
- missing fields;
- conflicts;
- uncertainty;
- whether decision, execution, and observation were independently established.

## 17. Determinism

A deterministic TT validator must produce the same result for the same canonical inputs and validator version:

```text
Validate(input, version) = result
```

Canonicalization rules are part of the validation contract.

## 18. Invalid inference rules

The following implications are prohibited:

```text
proposal -> approval
approval -> current authority
ALLOW -> execution
execution -> observation
observation -> correctness
receipt -> semantic truth
hash match -> authority
publication -> commit validity
```

## 19. Cross-layer binding

A complete research test binds:

```text
RTG event description
-> GTG governance context and disposition
-> TT cell and receipts
```

The TT representation must cite the RTG event and GTG determination versions used.

## 20. Failure conditions

A TT implementation fails when it:

- permits required `UNKNOWN` or `ERROR` guards to pass;
- conflates decision with execution;
- loses predecessor or supersession relations;
- cannot distinguish missing observation from success;
- accepts stale authority at commit;
- rewrites historical cells;
- omits conflict semantics for concurrent cells;
- or produces non-deterministic validation from identical canonical inputs.

## 21. Definition maturity

These definitions are `DRAFT_CANONICAL`. Promotion requires schema binding, deterministic fixtures, validator coverage, falsification tests, cross-layer cases, and an internal review receipt.
