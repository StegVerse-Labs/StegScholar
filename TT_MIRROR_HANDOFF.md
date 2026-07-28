# Transition Table Mirror Handoff

This file is the current source of truth for continuing Transition Table (TT) work in `StegVerse-Labs/StegScholar`.

## Current Goal

Formalize the Transition Table as the explicit, reconstructable representation layer that binds current state, triggering event, guards, authority, evidence, action, governance result, commit-time validity, and receipts into inspectable transition cells.

The canonical sequence is:

```text
RTG -> GTG -> TT
```

```text
RTG describes transition geometry and relational intersections.
GTG determines admissibility, standing, authority, and governance disposition.
TT records the exact transition rule, decision path, and realized or withheld state change.
```

## Current Activation Goal

```text
Goal id: tt-canonical-transition-cell-v0.1
State: FOUNDATIONAL_FORMALISM_DRAFTING
Authority posture: research and representation formalism only; a table row does not create authority, truth, certification, or execution permission.
Manual task requirement: none.
User manual action required: false.
```

## Source-of-Truth Boundaries

1. A TT cell represents a bounded transition determination; it does not itself grant standing.
2. Proposal-time and commit-time state must be distinguishable.
3. `ALLOW`, `DENY`, `FAIL_CLOSED`, `DEFER`, `TRANSFORM`, and `ERROR` must remain distinct.
4. Missing evidence, authority, policy, or reconstruction may not default to `ALLOW`.
5. Historical cells are immutable records; corrections and supersessions require linked successor cells.
6. A transition row must preserve both executed and withheld actions.
7. A deterministic table may still embody incorrect policy; structural validity is not substantive correctness.
8. Observer, reviewer, approver, executor, and reconstructor roles must be explicit.
9. Cross-scale projections require declared mappings and cannot silently alter cell semantics.
10. A row without a receipt is an assertion, not a reconstructable transition record.

## Canonical Transition Cell

```text
TT_cell = (
  cell_id,
  subject_id,
  pre_state,
  candidate_transition,
  trigger,
  context,
  evidence_refs,
  policy_refs,
  authority_refs,
  constraints,
  guard_result,
  gtg_result,
  commit_state,
  action,
  post_state,
  observer_refs,
  receipt_refs,
  predecessor,
  supersedes,
  scale
)
```

## Minimal Transition Rule

```text
(pre_state, trigger, guard) -> (result, action, post_state, receipt)
```

The minimal rule is insufficient for governed use unless authority, evidence, policy, context, and commit-time reconstruction are recoverable either directly or by immutable reference.

## Canonical Outcome Semantics

```text
ALLOW       -> action may proceed if commit-time state remains valid
DENY        -> action prohibited under evaluated conditions
FAIL_CLOSED -> action withheld because a required condition is absent or invalid
DEFER       -> action withheld pending a declared resolvable dependency
TRANSFORM   -> original action withheld; governed replacement candidate emitted
ERROR       -> evaluation failure; never equivalent to ALLOW
```

## Cell Evaluation

```text
cell_result = Evaluate(
  pre_state,
  candidate_transition,
  trigger,
  context,
  evidence_refs,
  policy_refs,
  authority_refs,
  constraints,
  scale
)
```

Commit-time execution requires:

```text
Execute(cell) only if:
  cell.gtg_result = ALLOW
  and cell.guard_result = PASS
  and CommitStateMatches(cell.commit_state)
  and AuthorityStillValid(cell.authority_refs)
  and EvidenceStillBound(cell.evidence_refs)
```

## Transition Table as Ledger

The TT is not merely a lookup table. It is an ordered set of transition receipts:

```text
TT = {cell_1, cell_2, ..., cell_n}
```

with continuity relations:

```text
cell_i.post_state ~= cell_j.pre_state
```

where any non-equivalence must be explained by an explicit intervening or scale-translation record.

A complete TT history preserves:

- admitted transitions;
- denied transitions;
- failed-closed attempts;
- deferred dependencies;
- transformations;
- evaluation errors;
- corrections;
- supersessions;
- observer and authority changes.

## Immediate Work Queue

1. Install the TT foundational formalism.
2. Define canonical cell identity and immutable receipt linkage.
3. Define guard precedence and outcome determinism.
4. Define proposal-time versus commit-time state fields.
5. Define compound and concurrent transition cells.
6. Define predecessor, successor, correction, and supersession semantics.
7. Define cross-scale TT projection from RTG scale maps.
8. Create machine-readable TT cell and table schemas.
9. Create deterministic fixtures for all governance outcomes.
10. Create a validator for continuity, authority binding, receipt integrity, and prohibited implicit `ALLOW` behavior.

## Known Remaining Files and Destinations

```text
StegVerse-Labs/StegScholar:
- papers/transition-table/foundation.md
- papers/transition-table/claims-register.md
- papers/transition-table/formal-definitions.md
- papers/transition-table/concurrency-and-compound-transitions.md
- papers/transition-table/falsification-protocol.md
- papers/transition-table/examples/
- schemas/transition-cell.schema.json
- schemas/transition-table.schema.json
- fixtures/tt/
- scripts/validate_transition_table.py

StegVerse-Labs/admissibility-wiki:
- bounded formalism projection after StegScholar claim review and destination handoff check

StegVerse-Labs/Site:
- public explanatory projection only after `docs/SITE_MIRROR_HANDOFF.md` grants scope

GCAT-BCAT-Engine/Publisher:
- canonical packaging and publication receipts only after `PUBLISHER_MIRROR_HANDOFF.md` grants scope
```

## Relationship to RTG and GTG

```text
RTG object:
  intersection translation and distributed event ledger

GTG object:
  governance function and admissible solution set

TT object:
  explicit cell encoding the governed transition and its receipt
```

A TT implementation must not flatten RTG geometry or GTG authority semantics into an unqualified state change.

## Release Boundary

The TT package is not ready for tagging or release. Release readiness requires formal definitions, schemas, fixtures, deterministic validation, concurrency tests, correction and supersession tests, falsification criteria, and an internal review receipt.

## Handoff Instruction

Continue from this file before relying on prior chat context. TT work follows GTG and must preserve the distinction between representation, authority, and execution.