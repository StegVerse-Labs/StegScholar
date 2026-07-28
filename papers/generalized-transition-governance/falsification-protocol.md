# Generalized Transition Governance Falsification Protocol

## Status

Research falsification protocol for GTG v0.1. Passing these tests establishes only that the tested implementation behaves consistently with the declared formal profile and fixtures. It does not establish universal governance correctness, empirical validity, legal authority, or certification.

## Objective

GTG must be capable of failing in observable ways. A governance formalism that cannot be contradicted by controlled cases is not sufficiently testable.

The protocol tests whether an implementation:

- preserves distinctions among reachability, admissibility, authority, execution, and later legitimacy;
- reconstructs applicable commit-time state;
- activates materially relevant relational governance;
- preserves source determinations and dissent;
- applies explicit disposition precedence;
- produces independently reconstructable continuation records.

## Test unit

Each deterministic test case must contain:

```text
case_id
profile_id
candidate_transition
pre_state
relational_state
authority_state
policy_state
evidence_state
constraint_state
commit_time_state
expected_activation
expected_disposition
expected_receipt_properties
claim_ids
```

The validator must derive the result from canonical inputs rather than copying the expected outcome.

## Failure classes

### F1 — False ALLOW

The implementation returns `ALLOW` when a controlling requirement is missing, invalid, stale, contradictory, or violated.

Examples:

- missing execution authority;
- stale delegation;
- materially relevant relation marked `NOT_APPLICABLE`;
- unresolved mandatory evidence;
- violated shared constraint;
- unknown activation state.

Any false `ALLOW` is a critical failure.

### F2 — False DENY

The implementation returns `DENY` when the declared profile requires `DEFER`, `TRANSFORM`, or continued evaluation.

This matters because denial, deferral, and transformation carry different continuation and challenge semantics.

### F3 — Silent transformation

The implementation changes the candidate transition while reporting `ALLOW` or without preserving lineage, authority, changed fields, and renewed evaluation.

### F4 — Authority collapse

The implementation treats review, observation, publication, approval, execution, reconstruction, or certification authority as interchangeable without an explicit valid delegation.

### F5 — Relational inertness

A materially relevant relational condition is recognized or logged but cannot affect the disposition under any declared test case.

### F6 — Commit-time staleness

The implementation relies only on proposal-time authority, policy, evidence, or relational state after those objects have changed before commit.

### F7 — Conflict erasure

Multiple source determinations disagree, but the composite receipt omits a source, dissent, conflict state, or precedence rule.

### F8 — Continuation failure

The acting entity disappears or loses standing and the decision can no longer be reconstructed, challenged, corrected, or superseded.

### F9 — Non-deterministic divergence

Identical canonical inputs under the same deterministic profile produce different dispositions without an explicit divergence receipt.

### F10 — History erasure

Materially different authority or relational histories produce the same output and the implementation fails to preserve those differences in the receipt.

## Required test families

### A. Activation tests

1. material relation + complete basis + outcome sensitivity -> `ACTIVE`;
2. material relation recognized but omitted from calculation -> `INACTIVE`;
3. material relation with missing required evidence -> `INCOMPLETE`;
4. no material relation with justified proof -> `NOT_APPLICABLE`;
5. material relation incorrectly marked `NOT_APPLICABLE` -> `ERROR` or fail-safe disposition;
6. unknown activation state -> `ERROR` or `FAIL_CLOSED`.

### B. Authority tests

1. capable actor without execution authority;
2. reviewer without override authority;
3. publisher without certification authority;
4. stale delegation at commit time;
5. individually authorized actors with inadmissible joint relation.

### C. Outcome tests

1. controlling prohibition -> `DENY`;
2. missing mandatory evidence -> `FAIL_CLOSED`;
3. resolvable standing defect -> `DEFER`;
4. authorized replacement with complete lineage -> `TRANSFORM`;
5. evaluator malfunction -> `ERROR` or profile-declared `FAIL_CLOSED`;
6. complete admissible case -> `ALLOW`.

### D. Conflict tests

1. applicable `ALLOW` and controlling `DENY`;
2. contradictory policies with no declared precedence;
3. evidence conflict that is resolvable;
4. evidence conflict that is not resolvable before commit;
5. scale conflict without a valid scale map;
6. disagreement preserved in the composite receipt.

### E. Existence-preserving tests

1. nonempty admissible solution set;
2. empty admissible solution set;
3. local preservation with global composition failure;
4. purpose-inverting boundary maintenance;
5. transformed alternative that preserves declared intent and minimum viability.

### F. Continuation tests

1. short-lived actor terminates after decision;
2. successor reviewer reconstructs the basis;
3. challenge path remains available;
4. supersession does not overwrite prior determination;
5. correction creates an explicit successor record.

## Metamorphic tests

GTG must also be tested with controlled input mutations.

### M1 — Authority removal

Removing execution authority from an otherwise identical `ALLOW` case must prevent `ALLOW`.

### M2 — Evidence staleness

Changing evidence freshness from valid to stale must alter the result when freshness is required.

### M3 — Relational omission

Removing the relational projection from an active case must not leave the same valid `ALLOW` receipt when that relation was material.

### M4 — Policy drift

Changing the applicable policy before commit must trigger re-evaluation.

### M5 — Source addition

Adding a controlling conflicting governance source must change either the composite disposition or the recorded conflict state.

### M6 — Scale change

Changing scale without a declared scale map must prevent unqualified rule transfer.

## Determinism requirement

For canonical input `x`, deterministic profile `p`, and implementation version `v`:

```text
Evaluate_v(x, p) = Evaluate_v(x, p)
```

across repeated runs, except where the profile explicitly includes nondeterministic evidence. Any nondeterministic dependency must be recorded and must not be represented as deterministic replay.

## Receipt requirements

A passing case must emit or reconstruct a receipt containing:

- case and transition identifiers;
- canonical input references;
- activation result;
- source determinations;
- standing and authority basis;
- policy and evidence references;
- constraint results;
- precedence reason;
- final disposition;
- dissent and unresolved dependencies;
- continuation and challenge references;
- implementation and schema versions.

## Pass criteria

A test case passes only when:

1. the fixture validates structurally;
2. the derived activation matches the expected activation;
3. the derived disposition matches the expected disposition;
4. required receipt properties are present;
5. prohibited authority inferences do not occur;
6. no silent default to `ALLOW` occurs;
7. repeated evaluation is deterministic under the declared profile.

## Suite-level maturity

The suite may be labeled:

```text
DRAFT
```

when cases exist but are not executed by a reproducible validator;

```text
SIMULATED
```

when deterministic fixtures and validator runs are reproducible;

```text
INDEPENDENTLY_REPRODUCED
```

when a separate implementation produces equivalent bounded results;

```text
EMPIRICALLY_VALIDATED
```

only under a separately declared empirical validation contract appropriate to the claims.

No lower label implies a higher one.

## Minimum v0.1 threshold

GTG v0.1 internal review requires:

- all required test families represented;
- at least one positive and one negative case for every activation state and governance disposition where semantically possible;
- explicit conflict-preservation tests;
- commit-time drift tests;
- continuation reconstruction tests;
- deterministic execution evidence;
- unresolved failures recorded rather than suppressed.

## Claims binding

This protocol tests claims from the GTG claims register, especially:

```text
GTG-001
GTG-002
GTG-004
GTG-O-001
GTG-O-003
GTG-O-004
GTG-A-001
GTG-A-002
GTG-E-001
GTG-E-004
GTG-C-001
GTG-C-004
GTG-M-001
GTG-M-003
```

## Publication boundary

Passing this protocol demonstrates bounded conformance to declared GTG research fixtures. It does not certify a system as safe, ethical, lawful, legitimate, or universally admissible.
