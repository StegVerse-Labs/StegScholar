# Gate Legitimacy Invariant Mirror Handoff

Updated: 2026-09-15
Goal Task ID: `GATE-LEGITIMACY-INVARIANT-001`
COSV: `40000100100000`
Status: `ACTIVE / CLAIMED_IMPLEMENTATION`
Parent comparison: `MILLINGS-RTG-GTG-TT-COMPARISON-001` (`RETIRED / COMPLETED`)

## Goal

Determine whether StegVerse governance gates require a first-class, inspectable legitimacy record and falsification protocol covering standard provenance, evidence-rule provenance, evaluator standing/conflicts, execution-path control, challenge paths, and review independence.

## Selection rationale

This child is selected before `INDEPENDENT-REVIEW-PREDICATE-001` because gate legitimacy defines the broader object within which reviewer independence is one possible evidence dimension. It is selected before `ARCHITECTURE-NEUTRAL-ADMISSIBILITY-001` because the latter can remain independently falsifiable after gate legitimacy is established. This ordering creates no dependency claim for either sibling and does not modify their `ACTIVE / UNCLAIMED` state.

## Collision check-in

Canonical source, open PRs, and active branches were checked for the exact task identity and equivalent implementation terminology. No competing branch, open PR, or pre-existing first-class `gate_legitimacy` record/falsification protocol was observed. Existing GTG authority/standing, evidence provenance, dissent, appeal/correction, and TT consequence/receipt semantics are adjacent substrate, not duplicates.

## Scope

This is research/formalism only. It must not create a new governance authority source or make gate-legitimacy metadata override an otherwise valid GTG disposition.

Current claimed surfaces:

- `papers/transition-table/gate-legitimacy-invariant.md`
- `schemas/gate-legitimacy-record.schema.json`
- `fixtures/gate-legitimacy/gate-legitimacy-cases.json`
- `scripts/validate_gate_legitimacy.py`
- `tests/test_gate_legitimacy.py`
- `README.md`

## Core proposition under test

A governance gate may be structurally present yet illegitimate as a decision surface if the governing standard, evidence rules, evaluator standing, execution-path control, or challenge/review conditions are not independently inspectable enough to distinguish substantive governance from self-authored or self-protecting gatekeeping.

Gate legitimacy is therefore separate from candidate admissibility:

`GateLegitimate(g) != CandidateAllowed(c)`

A legitimate gate may DENY a candidate on substantive grounds. An illegitimate gate may not acquire validity merely because its disposition happens to be desirable.

## Required outputs

- proposed `gate_legitimacy` object and field semantics;
- negative cases showing why source provenance alone is insufficient;
- tests for missing/conflicting standard authority, post-hoc evidence-rule control, evaluator conflict, and execution-path control;
- explicit distinction between gate legitimacy and candidate admissibility;
- adoption/rejection criteria for RTG/GTG/TT integration.

## Authority ceiling

The gate-legitimacy record is evidence about the fitness of a gate to participate in governance. It does not:

- mint governance or execution authority;
- issue an ALLOW/DENY disposition;
- override GTG;
- prove execution or consequence;
- certify an external framework;
- reopen the retired Millings parent.

## Completion threshold

Complete only when the proposed object is either rejected with a falsification-backed rationale or accepted with deterministic fixtures, validator coverage, and a documented integration boundary. Source completion alone does not claim canonical adoption until validation and merge evidence are observed.
