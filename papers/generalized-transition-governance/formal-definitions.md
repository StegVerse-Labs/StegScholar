# Generalized Transition Governance: Formal Definitions

## Status

Canonical working definitions for the GTG research volume set. These definitions are normative only within the StegScholar research formalism and do not create legal, certification, execution, or universal governance authority.

## 1. Candidate transition

A candidate transition is an ordered proposal:

```text
tau = (S_t, u, S*)
```

where:

- `S_t` is the reconstructed current state;
- `u` is the proposed action, operation, or transition instruction;
- `S*` is the proposed, predicted, or intended post-state.

A candidate transition is not an authorization and does not imply admissibility.

## 2. Relational state

The relational state at time `t` is:

```text
R_t = {r_1, ..., r_n}
```

where each `r_i` is a declared relation among one or more participants, systems, observers, authorities, environments, or consequence paths.

A relational state may include:

- dependency;
- consent;
- custody;
- delegation;
- obligation;
- conflict;
- vulnerability;
- coupled risk;
- shared resource use;
- observer standing;
- continuation and challenge rights.

## 3. Relevant relational projection

The relevant relational projection is:

```text
Rel(R_t, tau)
```

It is the smallest declared subset of `R_t` sufficient to evaluate whether relational facts may materially affect the governance disposition of `tau`.

A projection is insufficient when omission of a known relevant relation could change the disposition or erase a required dissent, authority defect, evidence requirement, or consequence path.

## 4. Governance basis

The governance basis is:

```text
B_t = Basis(Rel(R_t, tau), A_t, P_t, K_t, E_t, O_t)
```

where the basis may include:

- authority and delegation;
- policy;
- constraint;
- consent;
- evidence;
- responsibility;
- standing;
- consequence;
- continuation;
- appeal and correction rights.

A represented relation without an applicable basis is not automatically governing.

## 5. Governance activation operator

Governance activation is a typed internal sub-operator of GTG:

```text
A_g = Activate(Rel(R_t, tau), B_t, t_c)
```

with:

```text
A_g in {ACTIVE, INACTIVE, INCOMPLETE, NOT_APPLICABLE, ERROR}
```

### ACTIVE

The relevant relational projection is reconstructable at the commit boundary, an applicable governance basis exists, and the relation is incorporated into the governance calculation such that it can alter the disposition under declared rules.

### INACTIVE

A relevant relational condition exists, but the declared activation requirements are not satisfied. `INACTIVE` may not be interpreted as permission.

### INCOMPLETE

A materially relevant relational condition is known or reasonably indicated, but required state, evidence, authority, or reconstruction material is missing or unresolved.

### NOT_APPLICABLE

No materially relevant relational condition applies to the candidate transition under the declared scope. This state must be justified and reconstructable; it may not be used to bypass known relational relevance.

### ERROR

The activation mechanism failed to produce a valid typed result. `ERROR` may not default to `ALLOW`.

## 6. Activation conditions

A working activation rule is:

```text
Activate(Rel(R_t, tau), B_t, t_c) = ACTIVE
```

only when:

```text
Discoverable(Rel(R_t, tau))
and Reconstructable(Rel(R_t, tau), t_c)
and Applicable(B_t, t_c)
and Incorporated(Rel(R_t, tau), G)
and OutcomeSensitive(Rel(R_t, tau), g)
```

`OutcomeSensitive` means capable of changing the disposition under at least one declared admissibility condition. It does not require a changed outcome in every evaluated case.

## 7. Governance context

The governance context is:

```text
Gamma_t = (S_t, R_t, C_t, E_t, A_t, P_t, K_t, O_t, lambda, chi_t)
```

where:

- `C_t` is environmental and operational context;
- `E_t` is the evidence set;
- `A_t` is the authority and delegation set;
- `P_t` is the policy set;
- `K_t` is the constraint set;
- `O_t` is the observer and reviewer set;
- `lambda` is the declared governance scale;
- `chi_t` is the reconstructed commit-time state.

## 8. Governance operator

The GTG governance operator is:

```text
G : (tau, Gamma_t, A_g) -> g
```

with:

```text
g in {ALLOW, DENY, FAIL_CLOSED, DEFER, TRANSFORM, ERROR}
```

No undefined activation state or governance result may be coerced into `ALLOW`.

## 9. Disposition semantics

### ALLOW

The proposed transition is currently reachable, admissible, authorized, relationally evaluated where applicable, and commit-valid under the declared scope.

### DENY

The transition has been sufficiently evaluated and a governing prohibition applies.

### FAIL_CLOSED

The transition is withheld because required evidence, authority, standing, relational reconstruction, boundary integrity, or validation material is absent, invalid, or non-reconstructable.

### DEFER

A resolvable dependency remains outstanding and no final disposition is yet warranted.

### TRANSFORM

The original transition is inadmissible, but a governed alternative may be proposed without silently substituting intent or exceeding transformation authority.

### ERROR

The governance mechanism failed to produce a valid disposition. It must not be treated as `ALLOW`.

## 10. ALLOW solution set

Let:

```text
Reachable(S_t)
Admissible(Gamma_t)
Authorized(A_t, tau)
RelationallyValid(Rel(R_t, tau), A_g)
CommitValid(chi_t)
```

Then:

```text
ALLOW_set(S_t, Gamma_t) =
  Reachable(S_t)
  intersection Admissible(Gamma_t)
  intersection Authorized(A_t, tau)
  intersection RelationallyValid(Rel(R_t, tau), A_g)
  intersection CommitValid(chi_t)
```

The set may be empty. GTG must not fabricate a transition when it is empty.

## 11. Relationally induced inadmissibility

For actors `a_1 ... a_n`:

```text
AND_i Authorized(a_i) does not imply Admissible(tau | R_t)
```

Individual authorization is insufficient when the combined relational configuration introduces a conflict, coupled harm, consent defect, authority defect, scale mismatch, invalid aggregation, continuation failure, or other governing condition.

## 12. Commit-time relational reconstruction

The commit-time relational state is:

```text
R_commit = ReconstructRelationalState(R_t, tau, t_c)
```

A proposal-time relational judgment is evidence, not continuity of validity.

```text
RelationalCommitValid(tau) =
  [Activate(Rel(R_commit, tau), B_commit, t_c) in {ACTIVE, NOT_APPLICABLE}]
  and [G(tau, Gamma_commit, A_g) = ALLOW]
```

`NOT_APPLICABLE` is admissible only when its justification is explicit and reconstructable.

## 13. Authority classes

GTG distinguishes at minimum:

```text
propose
observe
review
approve
execute
reconstruct
appeal
correct
transform
certify
publish
```

Possession of one class does not imply another. Any combination must be declared, bounded, and reconstructable.

## 14. Continuation record

A continuation record is:

```text
C_(t+1) = (
  transition_id,
  source_state_ref,
  proposed_post_state_ref,
  relational_projection,
  governance_basis,
  activation_result,
  governance_disposition,
  authority_and_standing,
  evidence_refs,
  policy_and_constraint_refs,
  dissent,
  appeal_and_correction_paths,
  commit_time,
  reconstruction_material
)
```

The continuation record must preserve enough information for independent reconstruction and challenge after the acting entity disappears or loses standing.

## 15. Composition of multiple governance matrices

For multiple determinations:

```text
g_i = G_i(tau, Gamma_i, A_g_i)
```

composition requires an explicit operator:

```text
Omega(g_1, ..., g_n, precedence, standing, dissent) -> g*
```

No silent averaging, majority rule, or conflict erasure is permitted unless the composition rule itself has declared standing.

## 16. Relationship to RTG

RTG provides descriptive transition relations, intersections, costs, participant ledgers, and scale maps. GTG evaluates whether a proposed realization may commit under a declared governance context.

```text
RTG description -> relational projection -> GTG activation -> disposition
```

## 17. Relationship to TT

TT is the bounded inspectable or executable representation of a GTG determination.

A typed TT cell may include:

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

GTG supplies the semantics; TT supplies explicit transition encoding and receipts.

## 18. Definition maturity

These definitions are `DRAFT_CANONICAL`. They require claims registration, deterministic fixtures, conflict tests, schema binding, and validator coverage before release promotion.
