# Millings-derived formalism compatibility review: GTG and TT

Status: post-completion compatibility review
Goal Task: `GTG-TT-MILLINGS-FORMALISM-COMPATIBILITY-REVIEW-001`

## Reviewed formalisms

This review treats the following as completed, independently bounded StegVerse formalisms:

- Gate Legitimacy
- Independent Review
- Architecture-Neutral Admissibility

Their retired task identities are not reopened by this review.

## Current canonical GTG coverage

The current GTG decision/governance schemas already represent substantive transition governance: activation, standing, authority, evidence completeness/freshness, policy, constraints, disposition, replacement/transform semantics, source determinations, continuation, challenge/appeal/correction, and reconstruction references.

That means the three completed formalisms must not become a parallel decision algebra.

## Current canonical TT coverage

The current TT transition-cell schema already binds the governing GTG record through `gtg_record_ref`, carries the decision, performs commit-time validation, separates execution from observation and consequence, preserves predecessor/supersession lineage, and retains a receipt.

TT therefore does not need three additional copies of GTG assurance evidence.

## Gap analysis

### 1. Gate Legitimacy

Material gap: GTG has generic evidence and policy references, but no typed field proving that a gate-legitimacy record was the applicable legitimacy assessment for the exact decision context.

Do not duplicate: evaluator standing, evidence refs, policy refs, authority refs, or execution path inside GTG; those already exist in the formalism record and/or GTG.

Needed integration: a typed reference plus applicability and correlation validation.

### 2. Independent Review

Material gap: GTG continuation can carry challenge/appeal references, but it cannot distinguish a merely available review path from a deterministic independent-review assessment, nor validate that the assessment challenges the relevant gate/rule/evaluator context.

Do not duplicate: reviewer-independence dimensions inside GTG.

Needed integration: a typed reference plus applicability and challenged-subject correlation validation.

### 3. Architecture-Neutral Admissibility

Material gap: GTG evaluates substantive admissibility but has no typed way to prove that an architecture-neutrality check was considered where architecture difference was outcome-sensitive.

Do not duplicate: evidence, authority, standing, safety/constraints, policy, or commit-time checks; GTG already owns those substantive checks.

Needed integration: a typed reference plus applicability and candidate/requirement correlation validation.

## Minimum compatible design

Add one optional `governance_assurance` object to canonical GTG records. It should contain typed slots such as:

```text
gate_legitimacy
independent_review
architecture_neutral_admissibility
```

Each slot should declare:

```text
applicability = REQUIRED | OPTIONAL | NOT_APPLICABLE
record_ref = <typed external record reference or null>
validation_state = VALID | INVALID | UNRESOLVED | NOT_APPLICABLE
```

The validator, not the reference itself, determines whether the record:

- has the correct schema/type;
- has `authority_effect: NONE`;
- binds the correct candidate/gate/rule/evaluator/decision context;
- is required by the active profile;
- is unresolved or mismatched.

The assurance object does not emit a GTG disposition. It contributes deterministic evidence to the already-existing GTG decision process.

## Why TT should not gain the same fields

`tt-transition-cell.schema.json` already requires `gtg_record_ref`. The correct cross-layer relationship is:

```text
assurance record -> GTG governance record -> TT cell
```

not:

```text
assurance record -> GTG record
assurance record -> duplicated TT fields
```

Duplicating references into TT adds no authority or deterministic value and creates consistency risk. TT should instead gain compatibility tests proving that reconstruction follows `gtg_record_ref` and that assurance evidence cannot be promoted into execution/consequence authority.

## Falsification rules for integration

The integration is invalid if any of the following becomes possible:

1. `authority_effect: NONE` assurance evidence mints or substitutes for GTG authority.
2. A valid assurance record forces `ALLOW` or overrides a substantive `DENY`/`FAIL_CLOSED`.
3. An architecture-neutrality record duplicates or replaces GTG's substantive evidence/authority/standing/policy/constraint/commit checks.
4. An independent-review label without a validated independent-review record satisfies a required independent-review assurance slot.
5. A gate-legitimacy record for another gate/candidate satisfies the current decision.
6. TT contains a second assurance copy that can diverge from the referenced GTG record.
7. Existing historical GTG/TT records become invalid merely because the optional integration fields did not exist when they were created.

## Task disposition

One integration task is sufficient:

`GTG-ASSURANCE-REFERENCE-INTEGRATION-001`

No separate TT schema-integration task is justified. TT compatibility belongs inside the same integration task as cross-layer validation because its correct implementation is intentionally negative: preserve the existing `gtg_record_ref` ownership relation and prove no duplication/authority promotion occurs.
