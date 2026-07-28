# Generalized Transition Governance Claims Register

## Purpose

This register controls the research maturity of Generalized Transition Governance (GTG) before any normative protocol projection into `Admissible-Existence/AE`.

## Status labels

- **DEFINITION**
- **MODEL-DERIVED**
- **TESTABLE HYPOTHESIS**
- **ESTABLISHED DOMAIN RESULT**
- **SPECULATIVE EXTENSION**
- **DISALLOWED OVERCLAIM**

## Core governance claims

| ID | Claim | Status | Required evidence or action |
|---|---|---|---|
| GTG-001 | Governance applies to a candidate transition in a reconstructed context, not merely to an actor or artifact in isolation. | DEFINITION | Bind candidate, context, evidence, policy, authority, and commit-time state. |
| GTG-002 | Approval, visibility, capability, execution, continuity, admissibility, and authority are distinct properties. | DEFINITION / ESTABLISHED governance principle in bounded forms | Preserve separate fields and create negative fixtures for unlawful collapse. |
| GTG-003 | Historical authorization is always sufficient for present execution. | DISALLOWED OVERCLAIM | Commit-time standing, policy, delegation, and context must be reconstructable. |
| GTG-004 | A relational condition is governed only when it can materially alter the transition disposition. | DEFINITION / TESTABLE implementation criterion | Provide paired fixtures with recognized-but-inert and recognized-and-operative relations. |
| GTG-005 | Every governance conflict has one universal precedence ordering. | DISALLOWED OVERCLAIM | Precedence is profile-bound and may require fail-closed or defer behavior. |

## Outcome claims

| ID | Claim | Status | Required evidence or action |
|---|---|---|---|
| GTG-O-001 | `ALLOW`, `DENY`, `FAIL_CLOSED`, `DEFER`, `TRANSFORM`, and `ERROR` are semantically distinct outcomes. | DEFINITION | Define entry conditions, precedence, terminality, and permitted continuation for each. |
| GTG-O-002 | `ERROR` is equivalent to `ALLOW` when no explicit denial exists. | DISALLOWED OVERCLAIM | Default must be profile-declared; safety-critical profiles should fail closed. |
| GTG-O-003 | `TRANSFORM` denotes an authorized replacement candidate, not silent mutation of the original proposal. | DEFINITION | Require lineage, changed fields, fresh evidence, and renewed commit-time evaluation. |
| GTG-O-004 | `DEFER` preserves undecided status without fabricating denial or authorization. | DEFINITION | Specify expiry, evidence request, and re-evaluation path. |

## Authority and standing claims

| ID | Claim | Status | Required evidence or action |
|---|---|---|---|
| GTG-A-001 | Capability to perform an action does not establish authority to commit it. | DEFINITION / ESTABLISHED security-governance distinction | Add executable capability-without-authority fixture. |
| GTG-A-002 | Reviewer standing, override authority, execution authority, and observation authority may belong to different entities. | DEFINITION | Represent each authority class separately and test non-inheritance. |
| GTG-A-003 | Repository ownership or publication control establishes substantive correctness. | DISALLOWED OVERCLAIM | Preserve reciprocal review and evidence-bound determinations. |
| GTG-A-004 | Authority may be inferred from a successful prior execution. | DISALLOWED OVERCLAIM | Require current delegation and policy references. |

## Existence-preserving governance claims

| ID | Claim | Status | Required evidence or action |
|---|---|---|---|
| GTG-E-001 | An `ALLOW` set may be constrained to transitions preserving declared minimum existence conditions. | MODEL-DERIVED | Define the protected conditions and demonstrate satisfiable and empty solution sets. |
| GTG-E-002 | Local preservation of one participant is sufficient for global admissibility. | DISALLOWED OVERCLAIM | Multi-entity and environmental consequences must be represented where in scope. |
| GTG-E-003 | An empty admissible solution set requires fabrication of an allowed path. | DISALLOWED OVERCLAIM | Permit `DENY`, `FAIL_CLOSED`, `DEFER`, or redesign. |
| GTG-E-004 | Purpose-inverting boundary maintenance can render an otherwise protective transition inadmissible. | TESTABLE HYPOTHESIS / model-derived witness | Add a deterministic fixture where local boundary maintenance prevents intended recovery. |

## Commit-time reconstruction claims

| ID | Claim | Status | Required evidence or action |
|---|---|---|---|
| GTG-C-001 | Commit-time admissibility requires a declared reconstruction of applicable state, evidence, authority, and policy. | DEFINITION | Define completeness and freshness requirements. |
| GTG-C-002 | Replay under a historical policy proves current admissibility. | DISALLOWED OVERCLAIM | Historical replay and current standing must remain separate. |
| GTG-C-003 | Matching hashes prove semantic correctness or reviewer standing. | DISALLOWED OVERCLAIM | Hashes prove bounded byte identity only. |
| GTG-C-004 | A governance decision should be reproducible when the same canonical inputs and deterministic profile are supplied. | TESTABLE HYPOTHESIS / protocol objective | Implement deterministic fixtures and divergence receipts. |

## Multi-governance claims

| ID | Claim | Status | Required evidence or action |
|---|---|---|---|
| GTG-M-001 | Multiple applicable governance systems may yield conflicting dispositions for one candidate transition. | DEFINITION / ESTABLISHED institutional possibility | Add conflict fixtures and profile-specific resolution rules. |
| GTG-M-002 | The most permissive applicable governance result should always prevail. | DISALLOWED OVERCLAIM | Safety, jurisdiction, delegation, and protected-condition constraints may require stricter handling. |
| GTG-M-003 | Conflict resolution must preserve each input determination and the rule used to derive the composite result. | MODEL-DERIVED governance requirement | Require comparative receipt and no silent overwrite. |

## Required deterministic cases

GTG v0.1 must include:

1. authorized actor with inadmissible joint relation;
2. capable actor without execution authority;
3. stale approval denied at commit time;
4. `TRANSFORM` with complete lineage and renewed evaluation;
5. unresolved evidence producing `DEFER`;
6. evaluator failure producing profile-correct `FAIL_CLOSED` or `ERROR`;
7. multi-governance conflict with preserved divergent findings;
8. existence-preserving solution set with both nonempty and empty cases;
9. purpose-inverting boundary case;
10. authority non-inheritance across publication, review, and execution roles.

## Protocol projection threshold

GTG may be projected into an AE normative draft only after:

- stable definitions and proposition identifiers;
- this claims register is bound to the source version;
- outcome precedence semantics are explicit;
- deterministic fixtures and validator exist;
- falsification criteria exist;
- an internal review receipt records unresolved claims;
- normative additions are distinguished from research claims.

## Update rule

Every material GTG claim must cite an ID from this register. Status advancement requires committed evidence appropriate to the claim.