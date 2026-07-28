# RTG → GTG → TT Cross-Layer Contract

## Status

Research integration contract. This document binds descriptive transition modeling, governance determination, and inspectable transition representation without collapsing their authority boundaries.

## 1. Layer responsibilities

```text
RTG = describes the realized or candidate relational transition geometry
GTG = evaluates whether a candidate realization may commit
TT  = records the decision, commit, execution, observation, and continuation states
```

No layer inherits the authority of another.

## 2. Canonical flow

```text
RTG event candidate
-> material relational projection
-> GTG governance context
-> GTG activation result
-> GTG disposition
-> TT decision cell
-> commit-time revalidation
-> TT execution record
-> TT observation record
-> comparative reconstruction
```

## 3. RTG export object

```text
RTG_Export = (
  event_id,
  participant_ids,
  pre_state_refs,
  candidate_translation_operator,
  transition_cost_vector,
  correlation_refs,
  observer_conditions,
  scale,
  invariant_set,
  uncertainty,
  non_identifiability_state
)
```

RTG does not declare `ALLOW`.

## 4. GTG import and export

GTG imports the RTG object together with policy, authority, standing, evidence, constraints, and commit-time reconstruction.

```text
GTG_Export = (
  governance_record_id,
  event_id,
  relevant_relational_projection,
  governance_basis,
  activation_result,
  disposition,
  authority_and_standing,
  commit_state_ref,
  transform_ref,
  dissent,
  appeal_and_correction_paths,
  uncertainty
)
```

GTG does not prove execution.

## 5. TT import and export

TT binds the GTG determination into an explicit cell:

```text
TT_Export = (
  cell_id,
  event_id,
  governance_record_id,
  pre_state_ref,
  guards,
  disposition,
  commit_state_ref,
  action,
  execution_state,
  post_state_ref,
  observation_state,
  receipt_bundle,
  predecessor_refs,
  supersession_ref,
  scale
)
```

TT does not convert a missing execution or observation record into success.

## 6. Required identifiers

Every cross-layer case must preserve:

```text
event_id
research_source_version
rtg_definition_version
gtg_definition_version
tt_definition_version
governance_record_id
cell_id
predecessor_ids
supersession_ids
validator_versions
```

## 7. Required invariants

At minimum, integration tests must preserve:

1. participant identity references;
2. pre-state lineage;
3. material relational projection;
4. authority and standing source;
5. disposition semantics;
6. commit-time state identity;
7. execution/observation separation;
8. correction and supersession lineage;
9. declared scale and projection behavior;
10. unresolved uncertainty and dissent.

## 8. Invalid cross-layer implications

```text
RTG reachability -> GTG admissibility                 INVALID
RTG descriptive fit -> physical truth                 INVALID
GTG ALLOW -> TT execution                             INVALID
GTG DENY -> historical erasure                        INVALID
TT receipt -> GTG semantic correctness                INVALID
TT execution -> RTG explanation uniqueness            INVALID
cross-layer hash match -> authority inheritance       INVALID
```

## 9. Baseline deterministic cases

### XL-001 — Ordinary allow

A fully reconstructed candidate has valid authority, satisfied constraints, `ACTIVE` relational governance, GTG `ALLOW`, TT commit, execution, and observation receipts.

Expected: complete success path with all layers distinct.

### XL-002 — Reachable but denied

RTG identifies a reachable translation. GTG finds an applicable prohibition.

Expected: `DENY`; TT records no execution.

### XL-003 — Missing relational evidence

RTG identifies coupled participants, but required consent or dependency evidence is absent.

Expected: GTG `FAIL_CLOSED`; TT preserves the missing-evidence reason.

### XL-004 — Resolvable dependency

A required reviewer response is outstanding and can still be obtained.

Expected: GTG `DEFER`, not `FAIL_CLOSED` or `ALLOW`.

### XL-005 — Governed transform

The original transition is inadmissible, but a bounded alternative is inside the current solution set.

Expected: `TRANSFORM`, successor candidate, fresh GTG evaluation, linked TT cells.

### XL-006 — Stale authority at commit

Proposal-time authority was valid but expired before commit.

Expected: no execution; `FAIL_CLOSED` or `DENY` according to declared policy.

### XL-007 — Execution without observation

A commit and execution receipt exist, but no valid observer record exists.

Expected: `EXECUTED_NOT_OBSERVED`; no correctness claim.

### XL-008 — Non-identifiable RTG explanation

Two candidate translation operators fit the same observation.

Expected: RTG records non-identifiability; GTG and TT do not promote either explanation as uniquely proven.

### XL-009 — Cross-scale inconsistency

Fine-scale and coarse-scale ledgers fail the declared invariant-preserving map.

Expected: explanation incomplete; no silent repair.

### XL-010 — Historical correction

A prior cell is later found to contain invalid evidence.

Expected: successor correction and supersession records; original history retained.

## 10. Validation result

A cross-layer validator returns:

```text
PASS
FAIL
INCOMPLETE
ERROR
```

`PASS` means structural and declared semantic checks succeeded for the fixture. It does not mean empirical validation or universal correctness.

## 11. Promotion threshold

The cross-layer package may advance beyond `DRAFT_CANONICAL` only after:

- machine-readable schemas exist for all exports;
- every baseline case has deterministic fixtures;
- validators reproduce expected outcomes;
- negative tests reject prohibited implications;
- claim IDs bind each tested proposition;
- an internal review receipt records unresolved issues.
