# Gate Legitimacy Invariant Mirror Handoff

Updated: 2026-09-15
Goal Task ID: `GATE-LEGITIMACY-INVARIANT-001`
COSV: `71000000100100`
Status: `RETIRED / COMPLETED`
Parent comparison: `MILLINGS-RTG-GTG-TT-COMPARISON-001` (`RETIRED / COMPLETED`)

## Goal

Determine whether StegVerse governance gates require a first-class, inspectable legitimacy record and falsification protocol covering standard provenance, evidence-rule provenance, evaluator standing/conflicts, execution-path control, challenge paths, and review independence.

## Result

Accepted as a bounded StegVerse research formalism: gate legitimacy is a distinct evidence invariant and must remain separate from candidate admissibility.

```text
GateLegitimate(g) != CandidateAllowed(c)
```

The deterministic cases established independent failure classes for missing standard provenance, post-hoc evidence-rule mutation, evaluator/evidence-rule-controller overlap, and evaluator/execution-path-controller overlap. A disclosed conflict can be mitigated by independently evidenced review without granting authority to the legitimacy record, and a legitimate gate can still reference a candidate DENY.

## Selection and collision check

This child was selected before the two sibling Millings-derived refinements because it defines the broader gate-level evidence object within which later reviewer-independence evidence may be referenced. Canonical source, open PRs, and active branches were checked before claim. No competing branch, open PR, or equivalent first-class gate-legitimacy record/falsification protocol was observed. Sibling tasks were not claimed or modified.

## Installed source

- `papers/transition-table/gate-legitimacy-invariant.md`
- `schemas/gate-legitimacy-record.schema.json`
- `fixtures/gate-legitimacy/gate-legitimacy-cases.json`
- `scripts/validate_gate_legitimacy.py`
- `tests/test_gate_legitimacy.py`
- `README.md`

## Validation and merge evidence

StegScholar PR #60 exact head `d074b0f2335b545b98daf5ff78013b5f71a6f7a5` completed:

- Validate Transition Table: SUCCESS (run `34983008458`)
- Test Readiness: SUCCESS (run `34983008386`)
- Governable Autonomy Validation: SUCCESS (run `34983008495`)

PR #60 merged at `223150373bcf73bfee6de163372e4fb9b045d380`.

## Integration boundary

This task establishes and validates the record/formalism but does not silently inject it into every GTG/TT transition. The bounded future integration point is:

- GTG may consume a gate-legitimacy reference as evidence when the applicable policy requires gate-legitimacy evaluation;
- TT may retain that reference in the transition evidence trail;
- a non-LEGITIMATE required gate state must never default to ALLOW;
- the record itself never emits an ALLOW/DENY disposition and never mints authority.

Any source mutation that makes gate legitimacy mandatory across canonical GTG/TT schemas is separate integration work and must perform its own collision/compatibility review.

## Authority ceiling

The gate-legitimacy record has `authority_effect: NONE`. It does not mint governance or execution authority, override GTG, prove execution/consequence, certify an external framework, or reopen the retired Millings parent.

## Completion state

```text
coordination_state: RETIRED
checkout_state: COMPLETED
completion.claimed: true
completion.validated: true
archive_ready: true
COSV: 71000000100100
```
