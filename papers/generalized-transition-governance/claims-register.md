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
| GTG-001 | Governance applies to a candidate transition in a reconstructed context, not merely to an actor or artifact in isolation. | DEFINITION | Bind candidate, context, evidence, policy, authority, relational state, and commit-time state. |
| GTG-002 | Approval, visibility, capability, execution, continuity, admissibility, and authority are distinct properties. | DEFINITION / ESTABLISHED governance principle in bounded forms | Preserve separate fields and create negative fixtures for unlawful collapse. |
| GTG-003 | Historical authorization is always sufficient for present execution. | DISALLOWED OVERCLAIM | Commit-time standing, policy, delegation, relationship, and context must be reconstructable. |
| GTG-004 | A relational condition is governed only when it can materially alter the transition disposition under declared rules. | DEFINITION / TESTABLE implementation criterion | Provide paired fixtures with recognized-but-inert and recognized-and-operative relations. |
| GTG-005 | Every governance conflict has one universal precedence ordering. | DISALLOWED OVERCLAIM | Precedence is profile-bound and may require fail-closed or defer behavior. |
| GTG-006 | A reachable transition need not be admissible. | DEFINITION | Add a physically or computationally reachable transition that receives `DENY`. |
| GTG-007 | An admissible transition need not be authorized for the proposing or executing actor. | DEFINITION | Separate admissibility and authority sets and add a negative authority fixture. |
| GTG-008 | The current `ALLOW` solution set may be empty. | DEFINITION / MODEL-DERIVED | Add a fixture whose reachable, admissible, authorized, relationally valid, and commit-valid sets have no common member. |

## Relational governance activation claims

| ID | Claim | Status | Required evidence or action |
|---|---|---|---|
| GTG-R-001 | Recognition or representation of a relationship is insufficient for operational governance. | DEFINITION / TESTABLE implementation criterion | Fixture where a relation is logged but omitted from the disposition calculation. |
| GTG-R-002 | Governance activation is a typed internal sub-operator of the GTG governance operator. | DEFINITION | Bind `ACTIVE`, `INACTIVE`, `INCOMPLETE`, `NOT_APPLICABLE`, and `ERROR` in schema and validator. |
| GTG-R-003 | An undefined, omitted, or unmapped activation state may not default to `ALLOW`. | DEFINITION | Negative schema and validator cases. |
| GTG-R-004 | `NOT_APPLICABLE` must be justified and reconstructable when relational relevance could materially affect the candidate transition. | DEFINITION / TESTABLE implementation criterion | Reject an unjustified `NOT_APPLICABLE` assertion in the presence of a known relevant relation. |
| GTG-R-005 | Individual authorization of all visible actors does not imply admissibility of their combined transition. | DEFINITION / TESTABLE HYPOTHESIS | Multi-actor fixture with individually valid authority and a relationally induced non-`ALLOW` result. |
| GTG-R-006 | A proposal-time relational judgment is evidence, not continuity of commit-time validity. | DEFINITION | Fixture with relational state drift between proposal and commit. |
| GTG-R-007 | Missing materially relevant relational state may require `FAIL_CLOSED` or `DEFER`, but the distinction must be governed by an explicit recoverability rule. | TESTABLE HYPOTHESIS | Paired fixtures for irrecoverable missing consent and resolvable reviewer-standing evidence. |
| GTG-R-008 | Relational outcome sensitivity means the relevant relation can change a disposition under at least one declared condition; it does not require every case to change outcome. | DEFINITION / TESTABLE implementation criterion | Counterfactual paired inputs differing only in one governing relational variable. |
| GTG-R-009 | Relational integrity is a typed combination of evidence, constraints, authority, standing, consent, consequence, and continuation requirements rather than one universal scalar. | MODEL-DERIVED | Define typed fields and fixtures demonstrating non-interchangeability. |
| GTG-R-010 | A continuation record must preserve enough relational and governance material for independent reconstruction and challenge after the acting entity disappears or loses standing. | TESTABLE HYPOTHESIS | Positive reconstruction fixture and negative omission cases. |

## Outcome claims

| ID | Claim | Status | Required evidence or action |
|---|---|---|---|
| GTG-O-001 | `ALLOW`, `DENY`, `FAIL_CLOSED`, `DEFER`, `TRANSFORM`, and `ERROR` are semantically distinct outcomes. | DEFINITION | Define entry conditions, precedence, terminality, and permitted continuation for each. |
| GTG-O-002 | `ERROR` is equivalent to `ALLOW` when no explicit denial exists. | DISALLOWED OVERCLAIM | Default must be profile-declared; safety-critical profiles should fail closed. |
| GTG-O-003 | `TRANSFORM` denotes an authorized replacement candidate, not silent mutation of the original proposal. | DEFINITION | Require lineage, changed fields, fresh evidence, and renewed commit-time evaluation. |
| GTG-O-004 | `DEFER` preserves undecided status without fabricating denial or authorization. | DEFINITION | Specify expiry, evidence request, and re-evaluation path. |
| GTG-O-005 | Relational activation does not imply automatic denial. | DEFINITION | Fixtures mapping relational findings to each valid disposition where declared conditions support it. |
| GTG-O-006 | `INCOMPLETE` activation must map to a non-`ALLOW` disposition. | DEFINITION / TESTABLE implementation criterion | Define precedence between `FAIL_CLOSED`, `DEFER`, and `ERROR`. |

## Authority and standing claims

| ID | Claim | Status | Required evidence or action |
|---|---|---|---|
| GTG-A-001 | Capability to perform an action does not establish authority to commit it. | DEFINITION / ESTABLISHED security-governance distinction | Add executable capability-without-authority fixture. |
| GTG-A-002 | Reviewer standing, override authority, execution authority, observation authority, transformation authority, and publication authority may belong to different entities. | DEFINITION | Represent each authority class separately and test non-inheritance. |
| GTG-A-003 | Repository ownership or publication control establishes substantive correctness. | DISALLOWED OVERCLAIM | Preserve reciprocal review and evidence-bound determinations. |
| GTG-A-004 | Authority may be inferred from a successful prior execution. | DISALLOWED OVERCLAIM | Require current delegation and policy references. |

## Existence-preserving governance claims

| ID | Claim | Status | Required evidence or action |
|---|---|---|---|
| GTG-E-001 | An `ALLOW` set may be constrained to transitions preserving declared minimum existence conditions. | MODEL-DERIVED | Define the protected conditions and demonstrate satisfiable and empty solution sets. |
| GTG-E-002 | Local preservation of one participant is sufficient for global admissibility. | DISALLOWED OVERCLAIM | Multi-entity and environmental consequences must be represented where in scope. |
| GTG-E-003 | An empty admissible solution set requires fabrication of an allowed path. | DISALLOWED OVERCLAIM | Permit `DENY`, `FAIL_CLOSED`, `DEFER`, or redesign. |
| GTG-E-004 | Purpose-inverting boundary maintenance can render an otherwise protective transition inadmissible. | TESTABLE HYPOTHESIS / model-derived witness | Add a deterministic fixture where local boundary maintenance prevents intended recovery. |
| GTG-E-005 | Existence-preserving governance is underdefined unless protected variables, observer, scale, threshold, and time horizon are declared. | DEFINITION | Paired cases with different declared scale or horizon. |

## Commit-time reconstruction claims

| ID | Claim | Status | Required evidence or action |
|---|---|---|---|
| GTG-C-001 | Commit-time admissibility requires a declared reconstruction of applicable state, relational state, evidence, authority, and policy. | DEFINITION | Define completeness and freshness requirements. |
| GTG-C-002 | Replay under a historical policy proves current admissibility. | DISALLOWED OVERCLAIM | Historical replay and current standing must remain separate. |
| GTG-C-003 | Matching hashes prove semantic correctness or reviewer standing. | DISALLOWED OVERCLAIM | Hashes prove bounded byte identity only. |
| GTG-C-004 | A governance decision should be reproducible when the same canonical inputs and deterministic profile are supplied. | TESTABLE HYPOTHESIS / protocol objective | Implement deterministic fixtures and divergence receipts. |
| GTG-C-005 | Identical outputs may have different governance validity because their authority, evidence, and relational histories differ. | TESTABLE HYPOTHESIS | Paired same-output fixtures with materially different governance histories. |

## Multi-governance claims

| ID | Claim | Status | Required evidence or action |
|---|---|---|---|
| GTG-M-001 | Multiple applicable governance systems may yield conflicting dispositions for one candidate transition. | DEFINITION / ESTABLISHED institutional possibility | Add conflict fixtures and profile-specific resolution rules. |
| GTG-M-002 | The most permissive applicable governance result should always prevail. | DISALLOWED OVERCLAIM | Safety, jurisdiction, delegation, and protected-condition constraints may require stricter handling. |
| GTG-M-003 | Conflict resolution must preserve each input determination and the rule used to derive the composite result. | MODEL-DERIVED governance requirement | Require comparative receipt and no silent overwrite. |
| GTG-M-004 | Silent averaging, ungoverned majority voting, or dissent erasure cannot establish a valid composite determination. | DEFINITION | Add conflicting-matrix fixture without a standing composition rule. |

## Cross-volume boundary claims

| ID | Claim | Status | Required evidence or action |
|---|---|---|---|
| GTG-X-001 | RTG description of a transition relation does not itself establish GTG admissibility. | DEFINITION | Cross-volume case separating descriptive event structure from governance result. |
| GTG-X-002 | A TT row does not itself establish GTG validity unless its guards and receipts bind a reconstructable GTG determination. | TESTABLE HYPOTHESIS | Typed TT positive and negative fixtures. |
| GTG-X-003 | The relational-governance bridge paper is derivative and may not replace canonical GTG doctrine. | DEFINITION / publication boundary | Require bridge citations to stable GTG proposition IDs before publication. |

## Required deterministic cases

GTG v0.1 must include:

1. authorized actor with inadmissible joint relation;
2. capable actor without execution authority;
3. stale approval denied at commit time;
4. relation recognized in logs but omitted from governance;
5. unjustified `NOT_APPLICABLE` activation;
6. unknown activation state rejected;
7. missing consent producing `FAIL_CLOSED`;
8. resolvable reviewer-standing evidence producing `DEFER`;
9. `TRANSFORM` with complete lineage and renewed evaluation;
10. evaluator failure producing profile-correct `FAIL_CLOSED` or `ERROR`;
11. multi-governance conflict with preserved divergent findings;
12. existence-preserving solution set with both nonempty and empty cases;
13. purpose-inverting boundary case;
14. authority non-inheritance across publication, review, transformation, and execution roles;
15. short-lived actor with reconstructable continuation record;
16. short-lived actor with insufficient continuation material;
17. identical outputs with different governance histories;
18. RTG event and TT row without sufficient GTG evidence.

## Protocol projection threshold

GTG may be projected into an AE normative draft only after:

- stable definitions and proposition identifiers;
- this claims register is bound to the source version;
- activation and outcome precedence semantics are explicit;
- deterministic fixtures and validator exist;
- falsification criteria exist;
- an internal review receipt records unresolved claims;
- normative additions are distinguished from research claims.

## Status advancement rule

A claim may be treated as fixture-supported only when:

1. its terms are defined in `formal-definitions.md`;
2. one or more deterministic fixtures cite the claim ID;
3. expected outcomes are explicit;
4. positive and negative cases are covered;
5. validator evidence preserves inputs, rule versions, results, and failure reasons.

A deterministic existence witness is not empirical validation. Empirical promotion requires a separately declared domain, instrumentation, uncertainty model, falsification threshold, and independent evidence contract.

## Non-claims

GTG does not presently claim:

- a universal ethical law;
- a universal legal authority model;
- that all relationships are discoverable;
- that all governance conflicts are computably resolvable;
- that structural validity guarantees substantive correctness;
- that every system shares one governance operator;
- that deterministic fixtures prove empirical validity;
- that GTG replaces domain law, consent, safety practice, or human judgment.

## Update rule

Every material GTG claim must cite an ID from this register. Status advancement requires committed evidence appropriate to the claim. The register is `DRAFT_CANONICAL` until schemas, fixtures, validators, and review receipts exist.
