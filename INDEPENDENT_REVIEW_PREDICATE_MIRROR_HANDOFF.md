# Independent Review Predicate Mirror Handoff

Updated: 2026-09-15
Goal Task ID: `INDEPENDENT-REVIEW-PREDICATE-001`
COSV: `40000100100000`
Status: `ACTIVE / CLAIMED_IMPLEMENTATION`
Parent comparison: `MILLINGS-RTG-GTG-TT-COMPARISON-001` (`RETIRED / COMPLETED`)
Adjacent completed child: `GATE-LEGITIMACY-INVARIANT-001` (`RETIRED / COMPLETED`)

## Goal

Define and falsify a deterministic predicate that distinguishes merely available review from genuinely independent review for adverse governance dispositions.

## Existing substrate and collision boundary

`research-programs/governable-autonomy/review-schema.json` already supports `independent-peer-review`, `named-independent-reviewer`, and `anonymous-verified-reviewer`, but those labels do not independently establish separation from the challenged gate, challenged rule, financial/common-control interests, or execution-path control.

The completed `gate-legitimacy-record.schema.json` can reference an independent review and record whether it was satisfied, but intentionally does not define the proof predicate. This task fills that bounded gap rather than duplicating gate legitimacy.

No competing branch, open PR, or equivalent deterministic independence predicate was observed during check-in.

## Claimed source surfaces

- `papers/transition-table/independent-review-predicate.md`
- `schemas/independent-review-record.schema.json`
- `fixtures/independent-review/independent-review-cases.json`
- `scripts/validate_independent_review.py`
- `tests/test_independent_review.py`
- `README.md`

## Core proposition

```text
review_available != independent_review_available
reviewer_identity_label != reviewer_independence_proof
IndependentReview(r) != GovernanceAuthority(r)
```

A review is independently available only when the record contains sufficient evidence to resolve the required separation dimensions and no unresolved disqualifying conflict remains.

## Required dimensions

1. common organizational/control ownership;
2. challenged-rule authorship or rule-control overlap;
3. material financial interest;
4. reviewer/evaluator identity collision;
5. execution-path ownership/control overlap.

A disclosed conflict may be mitigated only by explicit evidence satisfying a declared mitigation rule; disclosure by itself is not independence.

## Authority ceiling

The predicate is evidence about review independence. It does not:

- mint governance or execution authority;
- issue an ALLOW/DENY disposition;
- override GTG;
- prove execution, post-state, or consequence;
- make a review decision binding merely because it is independent;
- reopen either retired parent task.

## Completion threshold

Complete only when independence is deterministically reproducible across positive and negative fixtures, including common-control, rule-author, financial-interest, evaluator-identity, execution-path-control, unresolved-evidence, and mitigated-conflict cases, with validator and test coverage.
