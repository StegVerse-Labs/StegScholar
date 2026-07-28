# Relational Governance Activation

## Status

Foundational GTG working note. Canonical placement is within the GTG volume set. A later bridge paper may compare this doctrine with Relational Mechanics or other relational frameworks, but this note is not subordinate to that bridge.

## Problem

A system may represent or understand relationships without allowing those relationships to affect what actions may commit. Representation alone is therefore not governance.

GTG requires a formal distinction among:

- relational existence;
- relational recognition;
- relational relevance;
- governance activation;
- commit-time binding;
- resulting transition disposition;
- continuation of the judgment after the acting entity disappears.

## Core Principle

> A relational condition becomes operationally governing only when its relevant state is reconstructed at a non-bypassable transition boundary, attached to an applicable governance basis, and incorporated into a disposition capable of changing what the system permits to become real.

## Working Objects

```text
R_t                 relational state at time t
tau                 candidate transition
t_c                 commit-boundary time
Rel(R_t, tau)       relational projection relevant to tau
Basis(R_t, tau)     applicable authority, responsibility, constraint,
                    consequence, policy, consent, or evidence basis
Activate(...)       governance activation predicate
g                   governance disposition
C_(t+1)             continuation record
```

## Activation Predicate

A first working form is:

```text
Activate(R_t, tau, t_c) =
  Discoverable(Rel(R_t, tau))
  and Reconstructable(Rel(R_t, tau), t_c)
  and Applicable(Basis(R_t, tau), t_c)
  and Incorporated(Rel(R_t, tau), G)
  and OutcomeSensitive(Rel(R_t, tau), g)
```

This should not yet be treated as a final theorem. Each predicate requires independent definition and falsification criteria.

## Recognition Is Not Governance

```text
Recognized(R_t, tau) != Governed(R_t, tau)
```

A framework fails to govern relationally when it can describe responsibilities, constraints, and consequences but those objects cannot alter the commit-time disposition.

A stronger operational requirement is:

```text
Governed(R_t, tau) -> OutcomeSensitive(Rel(R_t, tau), g)
```

This does not require every relational fact to change every outcome. It requires the relevant relational state to be admissibly capable of changing the outcome under declared rules.

## Relationally Induced Inadmissibility

Suppose each visible actor is independently authorized:

```text
Authorized(a_1) and ... and Authorized(a_n)
```

This does not imply:

```text
Admissible(tau | R_t)
```

The combined relational configuration may produce:

- incompatible duties;
- authority conflicts;
- consent defects;
- coupled harms;
- hidden consequence paths;
- scale mismatch;
- observer or reviewer standing defects;
- invalid aggregation of individually permitted acts;
- loss of continuation or challenge rights.

Thus:

```text
AND_i Authorized(a_i) does not imply Admissible(tau | R_t)
```

## Disposition Mapping

Relational activation does not imply automatic denial. A relational finding may produce:

- `ALLOW` when relational integrity and all other conditions are satisfied;
- `DENY` when a sufficiently evaluated relational prohibition applies;
- `FAIL_CLOSED` when required relational state, authority, evidence, or reconstruction is missing or invalid;
- `DEFER` when a resolvable relational dependency remains outstanding;
- `TRANSFORM` when the original transition is inadmissible but a governed alternative preserves intent and enters the current ALLOW solution set;
- `ERROR` when the governance mechanism cannot produce a valid disposition.

The mapping rule must be explicit and reconstructable.

## Commit-Time Binding

Relational relevance at proposal time is not sufficient. The relevant relational state must be reconstructed at the commit boundary:

```text
R_commit = ReconstructRelationalState(R_t, tau, t_c)
```

A prior relational judgment is evidence, not continuity of validity.

```text
RelationalCommitValid(tau) =
  Activate(R_commit, tau, t_c)
  and [G(tau, Gamma_commit) = ALLOW]
```

## Continuation Requirement

The visible actor may be short-lived, but the judgment cannot be.

The continuation record should preserve at minimum:

```text
C_(t+1) = (
  transition_id,
  relevant_relational_state,
  authority_basis,
  policy_and_constraint_basis,
  evidence_refs,
  expected_consequences,
  activation_result,
  governance_disposition,
  dissent,
  appeal_and_correction_paths,
  commit_time,
  reconstruction_material
)
```

This record must remain independently reconstructable and challengeable after the acting entity disappears or loses standing.

## Relationship to RTG

RTG describes the relational event structure, intersections, translations, costs, and participant ledgers. GTG determines whether a proposed realization of that structure may commit.

```text
RTG relational event description
  -> GTG relational relevance
  -> governance activation
  -> commit-time admissibility
  -> TT representation and receipt
```

## Relationship to TT

The Transition Table should not merely contain a relational label. Its guard and receipt must expose the activated relational basis sufficiently for reconstruction.

A future typed TT cell may include:

```text
TT_cell = (
  pre_state,
  event,
  relational_projection,
  activation_guard,
  authority,
  action,
  disposition,
  continuation_receipt
)
```

## Canonical Placement

This doctrine belongs in the GTG volume set before publication as a standalone comparative bridge paper.

Recommended order:

1. existence and solution-space necessity;
2. relational state and significance;
3. governance activation;
4. commit-time binding;
5. admissibility evaluation;
6. disposition semantics;
7. continuation and challenge;
8. RTG and TT integration.

## Bridge-Paper Boundary

A later paper provisionally titled:

```text
Relational Governance Activation:
From Relational Integrity to Commit-Time Admissibility
```

may compare this doctrine with Relational Mechanics and neighboring frameworks. That paper should cite the canonical GTG definitions after they stabilize and should not become the sole source of the activation doctrine.

## Open Formal Questions

1. Is activation a precondition to `G`, an internal stage of `G`, or a typed sub-operator?
2. Is relational integrity an invariant, predicate, evidence class, constraint class, or typed combination?
3. What minimum relational projection is sufficient for commit-time reconstruction?
4. Which missing relational facts require `FAIL_CLOSED` rather than `DEFER`?
5. How are conflicting relational matrices composed without erasing dissent?
6. How is outcome sensitivity tested without requiring an actual outcome change in every case?
7. What continuation material is sufficient for independent challenge?
8. How does activation behave across scale maps?

## Initial Falsification Cases

The doctrine should be tested against at least these cases:

1. all actors authorized, but combined action violates a shared constraint;
2. relationship recognized in logs but omitted from the governance calculation;
3. relational state valid at proposal time but stale at commit time;
4. missing consent evidence requiring `FAIL_CLOSED`;
5. resolvable observer-standing defect requiring `DEFER`;
6. inadmissible original transition with a valid `TRANSFORM` alternative;
7. short-lived agent disappears and the judgment cannot be reconstructed;
8. two governance matrices disagree and dissent is silently collapsed;
9. relational facts are present but cannot change any disposition;
10. identical outputs arise from materially different relational authority histories.

## Publication Boundary

This note proposes a research formalism. It does not establish a universal ethical law, a complete theory of human legitimacy, legal authority, or empirical validity across all intelligent systems.
