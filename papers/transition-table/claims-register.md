# Transition Table Claims Register

## Purpose

This register controls claims for the Transition Table (TT) as the canonical representation and receipt layer connecting RTG-described transitions to GTG-governed dispositions.

## Status labels

- **DEFINITION**
- **MODEL-DERIVED**
- **TESTABLE HYPOTHESIS**
- **ESTABLISHED DOMAIN RESULT**
- **SPECULATIVE EXTENSION**
- **DISALLOWED OVERCLAIM**

## Core representation claims

| ID | Claim | Status | Required evidence or action |
|---|---|---|---|
| TT-001 | A transition cell binds a candidate pre-state, trigger, evidence, policy, authority, guards, governance result, commit-time state, action, post-state, observers, and receipts. | DEFINITION | Publish canonical schema with required and optional fields. |
| TT-002 | A recorded post-state alone is sufficient to reconstruct the governing transition. | DISALLOWED OVERCLAIM | Preserve candidate, evidence, authority, policy, decision, and lineage. |
| TT-003 | Transition cells may be linked into compound transitions with explicit predecessor and dependency relations. | DEFINITION | Define ordering, concurrency, cancellation, and partial-failure semantics. |
| TT-004 | The same semantic transition always has one unique serialization. | DISALLOWED OVERCLAIM unless canonicalization profile is declared | Define canonical encoding, normalization, and version behavior. |
| TT-005 | For a fully specified deterministic action-plane model, consequence is the uniquely realized successor state under the exact declared reconciliation parameters. | DEFINITION / MODEL-DERIVED | Preserve model-completeness and determinism preconditions; do not coerce unresolved or stochastic cases into uniqueness. |
| TT-006 | A governance disposition is identical to consequence. | DISALLOWED OVERCLAIM | Keep disposition as an input/result of reconciliation and consequence as the realized successor state. |

## Historical and continuity claims

| ID | Claim | Status | Required evidence or action |
|---|---|---|---|
| TT-H-001 | Historical records should not be silently rewritten when standing, policy, evidence, or interpretation changes. | DEFINITION / governance requirement | Require supersession and correction links. |
| TT-H-002 | Correction requires erasure of the prior record. | DISALLOWED OVERCLAIM | Preserve prior state and append correction or supersession. |
| TT-H-003 | A valid chain requires declared linkage and continuity checks between relevant pre- and post-states. | MODEL-DERIVED | Implement deterministic broken-link and mismatched-state fixtures. |
| TT-H-004 | Hash continuity proves semantic continuity. | DISALLOWED OVERCLAIM | Byte identity, schema validity, semantic continuity, and authority continuity remain distinct. |
| TT-H-005 | Distinct realized transitions require distinct complete transition signatures in at least one identity-bearing coordinate. | DEFINITION | Enforce unique transition identity and signature references within a declared TT continuity set. |
| TT-H-006 | Every scalar component of a transition signature must itself be unique. | DISALLOWED OVERCLAIM | Permit equal entropy, energy, action, or disposition values while preserving full-signature distinction. |

## Governance binding claims

| ID | Claim | Status | Required evidence or action |
|---|---|---|---|
| TT-G-001 | A TT cell records a GTG disposition but does not independently create authority. | DEFINITION | Add authority-non-inheritance invariant. |
| TT-G-002 | An `ALLOW` record is sufficient evidence that execution occurred. | DISALLOWED OVERCLAIM | Separate decision, commit attempt, execution, observation, and receipt states. |
| TT-G-003 | A `TRANSFORM` result requires a new or derived candidate linked to the original proposal. | DEFINITION | Require transformation lineage and renewed evaluation reference. |
| TT-G-004 | `DEFER`, `ERROR`, and `FAIL_CLOSED` may be omitted because no state transition occurred. | DISALLOWED OVERCLAIM | Non-execution outcomes are material governance events and require receipts. |
| TT-G-005 | `DENY` and `FAIL_CLOSED` may be real transitions even when the proposed target-state projection is preserved. | DEFINITION / MODEL-DERIVED | Add projection-preserving transition fixtures and validator rules. |

## Observer and black-space claims

| ID | Claim | Status | Required evidence or action |
|---|---|---|---|
| TT-O-001 | No visible target-state change proves that no transition occurred. | DISALLOWED OVERCLAIM | Separate full-state change from declared projections. |
| TT-O-002 | `NOT_OBSERVED` is orthogonal to governance disposition and execution status. | DEFINITION | Permit `DENY + NOT_OBSERVED`, `FAIL_CLOSED + NOT_OBSERVED`, and `EXECUTED + NOT_OBSERVED`. |
| TT-O-003 | A bounded minimal transition element may preserve transition existence while leaving action, cause, disposition, signature, or temporal order unresolved. | DEFINITION | Bind `schemas/tt-transition-element.schema.json` and deterministic fixtures. |
| TT-O-004 | Black or unknown TT space is equivalent to absence of a transition. | DISALLOWED OVERCLAIM | Preserve the strongest supported transition-existence posture and unresolved fields. |
| TT-O-005 | Distinct complete transition signatures may be observationally equivalent for a particular observer. | MODEL-DERIVED | Keep observer projection separate from transition identity. |
| TT-O-006 | A minimal black-space element may assert a specific action, cause, disposition, or temporal position without supporting evidence. | DISALLOWED OVERCLAIM | Validator must reject or preserve those fields as unresolved/unknown. |

## Temporal and teleology claims

| ID | Claim | Status | Required evidence or action |
|---|---|---|---|
| TT-T-001 | Primitive transition representation requires an observer-assigned timestamp or metric duration. | DISALLOWED OVERCLAIM | Permit transition elements with unknown temporal order. |
| TT-T-002 | A bounded observer/model may attribute temporal order after establishing or reconstructing continuity relations among states/transitions. | DEFINITION | Preserve distinction between historical occurrence and later temporal attribution. |
| TT-T-003 | The TT proves that physical time does not exist independently of observers. | DISALLOWED OVERCLAIM | Keep the claim limited to formal temporal attribution; physical ontology of time remains outside TT proof. |
| TT-T-004 | Persistence is a primitive requirement of transition occurrence. | DISALLOWED OVERCLAIM | Treat persistence as an identity relation across already-related states. |
| TT-T-005 | Reality or the transition system has a universal goal of persistence. | DISALLOWED OVERCLAIM absent external theory and evidence | Do not introduce teleology into primitive transition semantics. |

## Physical inscription and entropy claims

| ID | Claim | Status | Required evidence or action |
|---|---|---|---|
| TT-P-001 | TT may bind evidence of physical or informational inscription to a realized transition under a declared system boundary. | DEFINITION / TESTABLE implementation criterion | Preserve inscription references and boundary metadata. |
| TT-P-002 | Every transition has a known universal exact entropy price. | DISALLOWED OVERCLAIM | Require explicit physical model, units, system boundary, and derivation before quantitative claims. |
| TT-P-003 | Every transition has a uniquely recoverable scalar thermodynamic signature. | DISALLOWED OVERCLAIM | Transition identity belongs to the complete signature, not necessarily any scalar entropy component. |
| TT-P-004 | A target-preserving transition may still incur resolution and inscription costs even when the proposed target transformation is withheld. | MODEL-DERIVED / TESTABLE HYPOTHESIS | Bind measurements only where a declared physical implementation and system boundary exist. |

## Concurrency and compound-transition claims

| ID | Claim | Status | Required evidence or action |
|---|---|---|---|
| TT-C-001 | Concurrent cells may require conflict detection when they consume or mutate overlapping state. | DEFINITION / TESTABLE implementation criterion | Build compatible and conflicting concurrency fixtures. |
| TT-C-002 | Timestamp order alone establishes causal order. | DISALLOWED OVERCLAIM | Permit logical clocks, dependencies, observer uncertainty, and partial order. |
| TT-C-003 | A compound transition may have admissible components but an inadmissible composition. | MODEL-DERIVED / TESTABLE HYPOTHESIS | Add composition fixture evaluated by GTG. |
| TT-C-004 | Failure of one component always invalidates every prior committed component. | DISALLOWED OVERCLAIM | Declare atomicity, compensation, rollback, and irreversible-consequence semantics. |

## Scale and projection claims

| ID | Claim | Status | Required evidence or action |
|---|---|---|---|
| TT-S-001 | TT may represent scale-relative projections of one extended transition. | DEFINITION | Bind scale identifier, projection rule, and shared event relation. |
| TT-S-002 | Coarse and fine tables must contain identical cells. | DISALLOWED OVERCLAIM | Require declared invariant preservation rather than identical representation. |
| TT-S-003 | Cross-scale projection can be tested for missing links or inconsistent consequences. | TESTABLE HYPOTHESIS | Build paired fine/coarse fixtures with known omissions and controls. |
| TT-S-004 | Full-state transition and observer-visible target projection are interchangeable. | DISALLOWED OVERCLAIM | Declare projection functions and preserve projection-invariant transitions. |

## Receipt claims

| ID | Claim | Status | Required evidence or action |
|---|---|---|---|
| TT-R-001 | A deterministic receipt binds canonical inputs, evaluator version, result, and relevant outputs. | DEFINITION | Define receipt schema and canonicalization profile. |
| TT-R-002 | A cryptographic hash establishes custody, correctness, or reviewer standing. | DISALLOWED OVERCLAIM | Treat each as an independent claim with separate evidence. |
| TT-R-003 | Observer receipts may disagree without invalidating the existence of the underlying event. | MODEL-DERIVED | Preserve divergent observations and confidence or resolution metadata. |
| TT-R-004 | Missing observation should be represented explicitly rather than inferred as success. | DEFINITION | Add `NOT_OBSERVED` and incomplete-evidence fixtures. |

## Required deterministic cases

TT v0.1 must include:

1. complete `ALLOW` decision-to-execution chain;
2. `ALLOW` without observed execution;
3. `DENY`, `DEFER`, `FAIL_CLOSED`, and `ERROR` receipts;
4. `TRANSFORM` with original and successor candidate lineage;
5. broken predecessor link;
6. pre-state/post-state mismatch;
7. concurrent compatible transitions;
8. concurrent conflicting transitions;
9. compound transition whose components pass individually but fail composition;
10. correction and supersession without historical erasure;
11. matching hashes with semantic mismatch;
12. coarse/fine projection with one omitted intermediate transition;
13. target-preserving `DENY + NOT_OBSERVED`;
14. target-preserving `FAIL_CLOSED + NOT_OBSERVED`;
15. inferred black transition with unknown action, disposition, signature, and temporal order;
16. invalid unknown-existence element that overclaims a concrete governance disposition;
17. two distinct realized elements with duplicate identity-bearing signature in one continuity set must fail identity validation.

## Protocol projection threshold

TT may be projected into an AE normative draft only after:

- canonical field definitions and versioning rules exist;
- this claims register is source-bound;
- schema and canonicalization rules exist;
- deterministic fixtures cover all outcome classes;
- validator and falsification protocol exist;
- RTG and GTG bindings are explicit;
- internal review records unresolved semantics.

## Update rule

Every material TT claim must cite an ID from this register. Status advancement requires committed derivation, fixtures, validation evidence, domain evidence, or independent review.
