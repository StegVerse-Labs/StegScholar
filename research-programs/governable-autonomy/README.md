# Governable Autonomy Research Program

## Purpose

The Governable Autonomy program studies how autonomous socio-technical systems can remain governable when trust, auditability, state integrity, incentive alignment, or verification capacity deteriorate.

This program treats execution authority as a runtime control-plane property rather than an inherited consequence of model capability, credentials, policy documents, or prior approval.

## Core proposition

Autonomous components may propose actions. The execution control plane determines whether those actions may cross the state-transition boundary into external or system reality.

## Proposed safety invariant

> If epistemic support decreases, execution authority must not expand.

A provisional scalar form is:

```text
E(t+1) < E(t)  =>  A(t+1) <= A(t)
```

A set-based formulation is expected to be more precise because emergency action classes may change without increasing total effective authority.

## Program taxonomy

| Class | Meaning |
|---|---|
| `stable-paper` | Internally version-stable; not necessarily externally reviewed |
| `working-paper` | Coherent manuscript under active revision |
| `draft-concept` | Defined thesis or model requiring substantial formalization |
| `research-note` | Narrow observation, derivation, or related-work record |
| `diagram-model` | Source-controlled explanatory or formal visual model |
| `validation-artifact` | Test, simulation, corpus, proof attempt, or empirical result |
| `superseded-merged` | Retained for provenance but replaced or incorporated elsewhere |

## Current papers

| ID | Title | Program role | Current status |
|---|---|---|---|
| `GA-001` | Governance Invariant for Autonomous Systems | Anchor safety property | `draft-concept` |
| `GA-002` | Survivable Governance | Governance under uncertainty | `working-paper` reconstruction |
| `GA-003` | Formal Model Sketch: Survivable Governance Under Epistemic Constraint | Minimal state model | `working-paper` reconstruction |
| `GA-004` | Trust-Bounded Socio-Technical Systems: Architectural Primitives for Auditability and Failure | Trust, auditability, and boundary primitives | `working-paper` reconstruction |
| `GA-005` | Ghost Credentials and Phantom Trust | Credential and authority failure modes | `working-paper` reconstruction |
| `GA-006` | Boundary-Condition Autonomy | Execution-boundary enforcement architecture | `working-paper` reconstruction |

## Unified architecture

```text
Trust state
    -> Auditability
    -> Credential legitimacy
    -> Boundary enforcement
    -> Execution authority at commit
    -> External or system reality
```

The intended degraded-state progression is:

```text
Open -> Constrained -> Revoked
```

At a critical degradation threshold, execution may collapse to a discrete decision such as `ALLOW/DENY` or `CONTINUE/PAUSE`.

## Shared models and diagrams

The program requires source-controlled diagrams for:

1. Governable Autonomy Stack
2. Epistemic degradation and authority contraction
3. Execution gateway between complex autonomy and reality
4. State-transition / irreversibility boundary
5. Paper contribution map

Each diagram must state whether it is descriptive, normative, or hypothesized and must include an accessible text alternative.

## Validation tracks

- Formal execution-boundary model
- Degraded compute and enforcement-capacity semantics
- State-integrity and compromised-state recovery model
- Monotonic authority-contraction property tests
- Distributed-system failure-case corpus
- Related-work verification
- Additional paper inventory

## Public peer review

The future StegVerse.org portal must distinguish internal paper maturity from external review status. Public discussion, conceptual comparison, or citation by another researcher is not independent peer review or endorsement.

## Authoritative records

- `STEGSCHOLAR_GOVERNABLE_AUTONOMY_MIRROR_HANDOFF.md`
- `research-programs/governable-autonomy/ARTIFACT_MANIFEST.md`
- `research-programs/governable-autonomy/paper-registry.json`

## Active issues

- #1 Public peer-review portal
- #2 Additional paper inventory
- #3 Reproducible paper artifacts
- #4 Review evidence/status model
- #5 Failure-case validation
- #6 Architecture diagrams
- #7 BCAT execution-boundary model
- #8 Release cross-updates
- #9 Related-work record
- #10 Compute-floor semantics
- #11 State-integrity model
- #12 Property tests
- #18 Paper-status registry
- #20 Canonical source directories

## Claims discipline

This program does not claim to solve alignment, ethics, semantic correctness, or global optimization. Its current propositions remain conceptual or formal hypotheses until supported by proofs, implementations, simulations, incident studies, independent review, or empirical validation.
