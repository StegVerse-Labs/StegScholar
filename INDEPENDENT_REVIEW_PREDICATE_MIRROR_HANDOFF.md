# Independent Review Predicate Mirror Handoff

Updated: 2026-09-15
Goal Task ID: `INDEPENDENT-REVIEW-PREDICATE-001`
COSV: `71000000100100`
Status: `RETIRED / COMPLETED`
Parent comparison: `MILLINGS-RTG-GTG-TT-COMPARISON-001` (`RETIRED / COMPLETED`)
Adjacent completed child: `GATE-LEGITIMACY-INVARIANT-001` (`RETIRED / COMPLETED`)

## Goal

Define and falsify a deterministic predicate that distinguishes merely available review from genuinely independent review for adverse governance dispositions.

## Result

Accepted as a bounded StegVerse research formalism. The implementation establishes that review availability and independent review are distinct evidence states:

```text
review_available != independent_review_available
reviewer_identity_label != reviewer_independence_proof
IndependentReview(r) != GovernanceAuthority(r)
```

A review is `INDEPENDENT` only when all required dimensions are evidenced `SEPARATE`: common organizational/control ownership, challenged-rule authorship/control, material financial interest, reviewer/original-evaluator identity, and execution-path ownership/control. A `CONFLICT` produces `NOT_INDEPENDENT`; absent review or unresolved required evidence produces `UNRESOLVED`. Neither state defaults to independence.

## Collision disposition

Before claim, canonical source, open PRs, branches, the completed gate-legitimacy formalism, and the Governable Autonomy review schema were checked. No competing deterministic predicate was observed. Existing `independent-peer-review`/reviewer identity labels are declarations, not proof of structural independence. The gate-legitimacy schema's `independent_review_ref` and satisfaction fields are consumer slots, not duplicate predicate logic.

## Installed source

- `papers/transition-table/independent-review-predicate.md`
- `schemas/independent-review-record.schema.json`
- `fixtures/independent-review/independent-review-cases.json`
- `fixtures/independent-review/README.md`
- `scripts/validate_independent_review.py`
- `tests/test_independent_review.py`
- `.github/workflows/validate-independent-review.yml`
- `docs/independent-review-integration-note.md`
- `docs/independent-review-authority-boundary.md`
- `README.md`

## Deterministic cases

Validated cases include:

- fully separated independent review;
- common-control conflict;
- challenged-rule-author/control conflict;
- material financial-interest conflict;
- reviewer/original-evaluator identity collision;
- execution-path-control conflict;
- missing required separation evidence;
- review unavailable;
- a previously conflicted control relationship represented as `SEPARATE` only after independently evidenced mitigation.

Disclosure alone is not mitigation. A mitigation reference is admissible only when the final dimension state is independently evidenced `SEPARATE`; circular self-attestation remains invalid by the formalism.

## Validation and merge evidence

StegScholar implementation PR #62 exact head `e24f000f39427cbb778e81152547ccc368cfa899` completed:

- Validate Independent Review: SUCCESS (run `34985687982`)
- Validate Transition Table: SUCCESS (run `34985687919`)
- Test Readiness: SUCCESS (run `34985687953`)
- Governable Autonomy Validation: SUCCESS (run `34985687912`)

PR #62 merged at `3ae161d82014848363d1c30dde28d8239cb6341c`.

This closeout branch additionally adds the mitigation fixture and terminal handoff state and must itself validate before merge.

## Integration boundary

The predicate may supply evidence to the completed gate-legitimacy formalism when independent review is required. It may also be referenced by future GTG dissent/appeal/correction or TT correction/supersession evidence.

This task does **not** modify the Governable Autonomy review schema, canonical GTG schema, or TT cell schema to make the predicate mandatory. Any mandatory cross-schema integration is separate compatibility work requiring a new collision review.

## Authority ceiling

`authority_effect: NONE` is invariant. An independent review does not become governance authority, cannot issue or override ALLOW/DENY, cannot authorize execution, and does not prove review correctness, execution, post-state, or consequence.

## Completion state

```text
coordination_state: RETIRED
checkout_state: COMPLETED
completion.claimed: true
completion.validated: true
archive_ready: true
COSV: 71000000100100
```

Do not reopen the retired Millings comparison or retired Gate Legitimacy child. Future work continues only under an independently registered adjacent or integration task.
