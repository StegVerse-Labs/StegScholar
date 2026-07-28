# Generalized Transition Governance Mirror Handoff

This file is the current source of truth for continuing Generalized Transition Governance (GTG) work in `StegVerse-Labs/StegScholar`.

## Current Goal

Formalize GTG as the governance layer that determines which candidate state transitions may be admitted, denied, deferred, fail-closed, or transformed when multiple systems, authorities, observers, relationships, and scales interact.

GTG is downstream of descriptive transition geometry and upstream of executable transition tables:

```text
RTG: what transition relations and intersections exist?
GTG: which of those relations become operationally governing, admissible, and under whose standing?
TT: how are those determinations represented and executed as explicit transition rules?
```

## Current Activation Goal

```text
Goal id: gtg-definitions-claims-and-fixtures-v0.1
State: CANONICAL_DEFINITION_AND_TEST_DESIGN
Authority posture: research governance formalism only; no certification, legal authority, execution authority, universal ethical law, or universal governance claim is created.
Manual task requirement: none.
User manual action required: false.
```

## Completed Activation Milestone

The relational-governance activation doctrine has now been integrated into the canonical GTG foundation.

```text
Canonical foundation commit:
0eac767f4883ce2c2ba66d2ca04e3e747980ca7b
```

The foundation now includes:

- relational state as a first-class governance-context object;
- relevant relational projection;
- governance activation as a typed internal sub-operator of `G`;
- activation states `ACTIVE`, `INACTIVE`, `INCOMPLETE`, `NOT_APPLICABLE`, and `ERROR`;
- recognition-versus-governance separation;
- relationally induced inadmissibility;
- baseline activation-to-disposition mapping;
- commit-time relational reconstruction;
- continuation-record requirements;
- RTG and TT bindings;
- canonical-versus-bridge-paper authority boundaries.

## Source-of-Truth Boundaries

1. GTG does not replace domain law, safety rules, policy, consent, or operator authority.
2. An `ALLOW` result is valid only relative to a declared context, evidence set, authority set, relational state, scale, and commit-time state.
3. `DENY`, `FAIL_CLOSED`, `DEFER`, and `TRANSFORM` are first-class outcomes, not errors or incomplete `ALLOW` states.
4. Historical approval does not automatically survive policy, identity, evidence, delegation, relational, or environmental change.
5. Observation, review, approval, execution, reconstruction, and correction are distinct authorities unless explicitly combined by valid standing.
6. A governance result may be structurally valid yet substantively wrong; independent review and falsification remain necessary.
7. GTG must preserve divergent determinations and cannot silently collapse disagreement into consensus.
8. Cross-scale governance requires declared scale maps and preserved invariants; rules cannot be assumed to transfer unchanged between scales.
9. Governance applies to transitions, not merely outputs.
10. No framework may infer authority from visibility, publication, possession, technical capability, or relational awareness alone.
11. A relationship is not operationally governed merely because it exists, is represented, or is understood.
12. Canonical GTG doctrine must stabilize before extraction into a comparative bridge paper.
13. `NOT_APPLICABLE` is distinct from missing relational evidence and must not be used to bypass a materially relevant relationship.
14. No unmapped activation state may default to `ALLOW`.

## Canonical Working Objects

```text
Candidate transition: tau
Current state: S_t
Proposed post-state: S_t+1
Relational state: R_t
Relevant relational projection: Rel(R_t, tau)
Applicable relational basis: Basis(R_t, tau)
Context: C_t
Evidence set: E_t
Authority set: A_t
Policy set: P_t
Constraint set: K_t
Observer/reviewer set: O_t
Scale parameter: lambda
Admissibility function: G
Governance activation sub-operator: Act
Governance activation predicate: Activate
Governance result: g
Commit-time reconstruction: chi_t
Standing function: sigma
Appeal/correction relation: alpha
Continuation record: C_(t+1)
```

## Canonical Governance and Activation Functions

```text
Act : (Rel(R_t, tau), Basis(R_t, tau), chi_t) -> a
```

with:

```text
a in {ACTIVE, INACTIVE, INCOMPLETE, NOT_APPLICABLE, ERROR}
```

and:

```text
g = G(tau, Gamma_t, a)
```

with:

```text
g in {ALLOW, DENY, FAIL_CLOSED, DEFER, TRANSFORM, ERROR}
```

A transition may execute only when result, standing, activation state, and commit-time reconstruction jointly satisfy the governing rule.

## Core GTG Distinction

```text
Possible transitions != admissible transitions
Admissible transitions != authorized transitions
Authorized transitions != executed transitions
Executed transitions != legitimate transitions after later review
Recognized relationships != governed relationships
Individually authorized actors != relationally admissible combined transition
```

## Resolved Formal Decision

Activation is treated as a typed internal sub-operator of `G`.

This avoids two errors:

1. treating relational activation as an external approval authority;
2. requiring artificial relational evidence where no material relational projection exists.

`NOT_APPLICABLE` permits full governance evaluation to continue only when declared relevance rules establish that no material relational projection exists. `INACTIVE`, `INCOMPLETE`, and `ERROR` must map through explicit fail-safe disposition rules.

## Immediate Work Queue

1. Create `papers/generalized-transition-governance/formal-definitions.md` with typed definitions for every activation and governance predicate.
2. Create `papers/generalized-transition-governance/claims-register.md` with bounded claim identifiers and maturity states.
3. Formalize `Rel`, `Basis`, `Discoverable`, `Reconstructable`, `Applicable`, `Incorporated`, and `OutcomeSensitive`.
4. Define the proof obligation for `NOT_APPLICABLE` so it cannot become a relational-evidence bypass.
5. Define relational integrity as a typed combination of invariant, predicate, evidence class, and constraint class rather than forcing one universal type.
6. Define complete activation-to-disposition precedence, including conflicts among activation, standing, policy, and evidence failures.
7. Create worked cases where all actors are individually authorized but the combined transition is inadmissible.
8. Create falsification cases distinguishing relational recognition from operational governance.
9. Create a machine-readable GTG decision and activation schema.
10. Create deterministic fixtures and a validator.
11. Bind GTG outputs to TT cells only after the GTG result is explicit and reconstructable.
12. Draft `relational-governance-activation-bridge.md` only after definitions, claim IDs, proposition numbering, and disposition semantics stabilize.

## Known Remaining Files and Destinations

```text
StegVerse-Labs/StegScholar:
- papers/generalized-transition-governance/foundation.md [canonical foundation installed]
- papers/generalized-transition-governance/relational-governance-activation.md [working note installed]
- papers/generalized-transition-governance/formal-definitions.md
- papers/generalized-transition-governance/claims-register.md
- papers/generalized-transition-governance/conflict-resolution.md
- papers/generalized-transition-governance/falsification-protocol.md
- papers/generalized-transition-governance/examples/
- papers/generalized-transition-governance/relational-governance-activation-bridge.md [deferred]
- schemas/gtg-decision.schema.json
- schemas/gtg-governance-activation.schema.json
- fixtures/gtg/
- scripts/validate_gtg_fixtures.py

Admissible-Existence/AE:
- docs/protocols/generalized-transition-governance/specification.md [after StegScholar stabilization]
- docs/protocols/generalized-transition-governance/conformance.md [after fixtures and validator]
- schemas/gtg-protocol.schema.json [after research schema stabilization]

StegVerse-Labs/admissibility-wiki:
- bounded public formalism projection after StegScholar claim review and destination handoff check

StegVerse-Labs/Site:
- public explanatory projection only after `docs/SITE_MIRROR_HANDOFF.md` grants scope

GCAT-BCAT-Engine/Publisher:
- canonical paper packaging and publication receipts only after Publisher handoff authority is confirmed

StegVerse-002/stegguardian-wiki:
- dispute, correction, dissent, standing, continuation, and challenge projection only after destination handoff authority is confirmed
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
- relational governance activation
- admissibility
- standing
- authority separation
- policy and evidence binding
- commit-time validity
- outcome precedence
- continuation requirements
- appeals, disputes, and corrections

TT supplies:
- explicit state-transition cells
- guards
- actions
- receipts
- deterministic outcome encoding
- executable or reviewable transition rows
```

## Planned Bridge Paper

Provisional path:

```text
papers/generalized-transition-governance/relational-governance-activation-bridge.md
```

Provisional title:

```text
Relational Governance Activation: From Relational Integrity to Commit-Time Admissibility
```

This paper is comparative and explanatory. It must not replace the canonical GTG volume treatment.

## Release Boundary

The GTG package is not ready for tagging or release. Release readiness requires formal definitions, claim statuses, theorem or proposition numbering, deterministic fixtures, conflict tests, governance-activation tests, commit-time reconstruction tests, falsification criteria, cross-volume references, and an internal review receipt.

## Handoff Instruction

Continue from this file before relying on prior chat context. The relational-governance activation foundation is integrated. The next priority is the definitions-and-claims layer followed by schemas, fixtures, and deterministic validation. The complete prior discussion has been reduced into this source of truth and is ready for archiving without any additional part of the thread needed to move forward.
