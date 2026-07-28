# Generalized Transition Governance Mirror Handoff

This file is the current source of truth for continuing Generalized Transition Governance (GTG) work in `StegVerse-Labs/StegScholar`.

## Current Goal

Formalize GTG as the governance layer that determines which candidate state transitions may be admitted, denied, deferred, fail-closed, or transformed when multiple systems, authorities, observers, and scales interact.

GTG is downstream of descriptive transition geometry and upstream of executable transition tables:

```text
RTG: what transition relations and intersections exist?
GTG: which of those relations are governable, admissible, and under whose standing?
TT: how are those determinations represented and executed as explicit transition rules?
```

## Current Activation Goal

```text
Goal id: gtg-generalized-admissibility-governance-v0.1
State: FOUNDATIONAL_FORMALISM_DRAFTING
Authority posture: research governance formalism only; no certification, legal authority, execution authority, or universal governance claim is created.
Manual task requirement: none.
User manual action required: false.
```

## Source-of-Truth Boundaries

1. GTG does not replace domain law, safety rules, policy, consent, or operator authority.
2. An `ALLOW` result is valid only relative to a declared context, evidence set, authority set, scale, and commit-time state.
3. `DENY`, `FAIL-CLOSED`, `DEFER`, and `TRANSFORM` are first-class outcomes, not errors or incomplete `ALLOW` states.
4. Historical approval does not automatically survive policy, identity, evidence, delegation, or environmental change.
5. Observation, review, approval, execution, and reconstruction are distinct authorities unless explicitly combined by valid standing.
6. A governance result may be structurally valid yet substantively wrong; independent review and falsification remain necessary.
7. GTG must preserve divergent determinations and cannot silently collapse disagreement into consensus.
8. Cross-scale governance requires declared scale maps and preserved invariants; rules cannot be assumed to transfer unchanged between scales.
9. Governance applies to transitions, not merely outputs.
10. No framework may infer authority from visibility, publication, possession, or technical capability alone.

## Canonical Working Objects

```text
Candidate transition: tau
Current state: S_t
Proposed post-state: S_t+1
Context: C_t
Evidence set: E_t
Authority set: A_t
Policy set: P_t
Constraint set: K_t
Observer/reviewer set: O_t
Scale parameter: lambda
Admissibility function: G
Governance result: g
Commit-time reconstruction: chi_t
Standing function: sigma
Appeal/correction relation: alpha
```

## Canonical Governance Function

```text
g = G(tau, S_t, C_t, E_t, A_t, P_t, K_t, O_t, lambda, chi_t)
```

with:

```text
g in {ALLOW, DENY, FAIL_CLOSED, DEFER, TRANSFORM, ERROR}
```

A transition may execute only when the result, standing, and commit-time reconstruction jointly satisfy the governing rule:

```text
Executable(tau) =
  [g = ALLOW]
  and StandingValid(A_t, tau, C_t)
  and CommitStateValid(chi_t)
  and ConstraintsSatisfied(K_t)
```

## Core GTG Distinction

GTG governs the relation between candidate transitions and existence-preserving admissible solution sets.

```text
Possible transitions != admissible transitions
Admissible transitions != authorized transitions
Authorized transitions != executed transitions
Executed transitions != legitimate transitions after later review
```

The `ALLOW` solution set is therefore not every reachable state. It is the subset of reachable states that remains admissible under the declared constraints and current standing:

```text
ALLOW_set(S_t) = Reachable(S_t) intersection Admissible(C_t, E_t, A_t, P_t, K_t, lambda)
```

Where the admissible set is empty, GTG must not fabricate a transition. It must return `DENY`, `FAIL_CLOSED`, or `DEFER` according to the declared rule.

## Immediate Work Queue

1. Install the GTG foundation note.
2. Define governance outcome semantics and precedence.
3. Define standing, delegation, consent, observation, review, and execution as separable authority classes.
4. Define commit-time reconstruction requirements.
5. Define the existence-preserving `ALLOW` solution-set concept without implying a universal objective function.
6. Define conflict handling for multiple governance matrices.
7. Create toy cases for stale authority, contradictory policy, insufficient evidence, degraded observer standing, and transform-required transitions.
8. Create a machine-readable GTG decision schema.
9. Create deterministic fixtures and a validator.
10. Bind GTG outputs to TT cells only after the GTG result is explicit and reconstructable.

## Known Remaining Files and Destinations

```text
StegVerse-Labs/StegScholar:
- papers/generalized-transition-governance/foundation.md
- papers/generalized-transition-governance/claims-register.md
- papers/generalized-transition-governance/formal-definitions.md
- papers/generalized-transition-governance/conflict-resolution.md
- papers/generalized-transition-governance/falsification-protocol.md
- papers/generalized-transition-governance/examples/
- schemas/gtg-decision.schema.json
- fixtures/gtg/
- scripts/validate_gtg_fixtures.py

StegVerse-Labs/admissibility-wiki:
- bounded public formalism projection after StegScholar claim review and destination handoff check

StegVerse-Labs/Site:
- public explanatory projection only after `docs/SITE_MIRROR_HANDOFF.md` grants scope

GCAT-BCAT-Engine/Publisher:
- canonical paper packaging and publication receipts only after `PUBLISHER_MIRROR_HANDOFF.md` grants scope
```

## Relationship to RTG and TT

```text
RTG supplies:
- participant world-regions
- intersection events
- translation operators
- transition costs
- distributed ledgers
- scale maps

GTG supplies:
- admissibility
- standing
- authority separation
- policy and evidence binding
- commit-time validity
- outcome precedence
- appeals, disputes, and corrections

TT supplies:
- explicit state-transition cells
- guards
- actions
- receipts
- deterministic outcome encoding
- executable or reviewable transition rows
```

## Release Boundary

The GTG package is not ready for tagging or release. Release readiness requires formal definitions, claim statuses, deterministic fixtures, conflict tests, commit-time reconstruction tests, falsification criteria, and an internal review receipt.

## Handoff Instruction

Continue from this file before relying on prior chat context. GTG must remain explicitly bounded between RTG description and TT representation.