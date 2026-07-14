# Governance Invariant for Autonomous Systems

- Paper ID: `GA-001`
- Author: Rigel Randolph
- Version: `0.1.0-draft`
- Status: `draft-concept`
- Review state: `none`

## Abstract

Autonomous socio-technical systems increasingly operate under degraded epistemic conditions in which trust evidence decays, audit history becomes incomplete, state integrity may be uncertain, and verification or enforcement capacity may be constrained. This paper proposes a governability safety property: execution authority must not expand as epistemic support deteriorates. The property is intended to prevent systems from becoming more operationally powerful while knowing less about the legitimacy, integrity, or recoverability of the state in which they act. The paper frames authority as a permitted action set enforced at the state-transition boundary and identifies open questions concerning emergency authority, safe recovery, degraded compute, and authorized re-expansion.

## 1. Problem statement

Policy, credentials, model capability, and prior approval do not by themselves establish continuing authority to commit a state transition. A system may retain syntactically valid authority indicators while the evidence supporting their legitimacy has decayed or disappeared.

## 2. Candidate system model

Let `X_t` denote the governance-relevant state at time `t`. Candidate components include:

```text
X_t = (T_t, U_t, H_t, I_t, C_t, P_t)
```

where:

- `T`: trust support;
- `U`: auditability or reconstructability;
- `H`: currently permitted execution set;
- `I`: state integrity;
- `C`: verification and enforcement capacity;
- `P`: operational or incentive pressure.

The minimal sufficient state remains an open research question.

## 3. Proposed invariant

Scalar shorthand:

```text
E(t+1) < E(t)  =>  A(t+1) <= A(t)
```

Preferred set-based direction:

```text
If epistemic support at t+1 is weaker than at t,
then PermittedActions(t+1) must be a subset of or equal to PermittedActions(t),
unless an explicitly modeled recovery or emergency transition proves that total effective authority has not increased.
```

## 4. Execution-boundary interpretation

The invariant is enforced immediately before an action commits external or system state. Reasoning systems may generate proposals outside the permitted set; proposal generation does not itself establish execution authority.

## 5. Emergency actions

A degraded system may gain access to narrow emergency actions such as isolation, shutdown, rollback request, or evidence preservation. These actions must not be counted as authority expansion merely because they were unavailable during normal operation. The model must compare effective power, scope, reversibility, and consequence rather than only action labels.

## 6. Recovery and re-expansion

Authority may expand only after a defined recovery transition establishes a new trust basis, validates state integrity, restores required enforcement capacity, and records who is authorized to approve re-expansion.

## 7. Threat and failure model

Candidate failures include:

- stale or missing evidence;
- phantom trust;
- ghost credentials;
- compromised live state;
- damaged or overloaded verification infrastructure;
- incentive pressure favoring continuation;
- bypass of the execution gate;
- unauthorized recovery or re-expansion.

## 8. Evaluation plan

- finite-state reference model;
- exhaustive or property-based tests;
- counterexamples involving emergency authority;
- incident-case coding;
- comparison of scalar and set-based authority orders;
- degraded-capacity simulations.

## 9. Limitations

The invariant does not prove action correctness, ethical legitimacy, semantic accuracy, or optimality. No general proof or empirical validation is currently claimed.

## 10. Open tasks

Tracked by issues #5, #7, #10, #11, and #12.
