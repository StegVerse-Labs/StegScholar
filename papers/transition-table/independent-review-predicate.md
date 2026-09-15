# Independent Review as a Deterministic Evidence Predicate

Status: draft formalism under `INDEPENDENT-REVIEW-PREDICATE-001`

## Abstract

A review can exist without being independent. Labels such as `independent-peer-review` or `named-independent-reviewer` are useful declarations, but they are not sufficient evidence that the reviewer is separate from the challenged gate, the author/controller of the challenged rule, material financial interests, the original evaluator, or the execution-path controller.

This note defines reviewer independence as a deterministic evidence predicate. The predicate is deliberately non-authorizing: it can establish whether a review satisfies an independence requirement, but it cannot issue a governance disposition, grant execution authority, override GTG, or prove execution or consequence.

## 1. Core distinctions

```text
review_available != independent_review_available
reviewer_identity_label != reviewer_independence_proof
IndependentReview(r) != GovernanceAuthority(r)
```

A review may be available yet fail independence. A review may be independent yet disagree with the challenged decision without thereby replacing the decision. Independence is one evidence property of a review path, not a second governance authority.

## 2. Deterministic predicate

For review record `r`, define five required separation dimensions:

- `common_control`: reviewer and challenged gate are not under the same controlling organization or control group;
- `rule_authorship`: reviewer did not author or control the challenged rule;
- `financial_interest`: reviewer has no unresolved material financial interest in the challenged outcome;
- `evaluator_identity`: reviewer is not the same natural, organizational, or delegated identity as the original evaluator;
- `execution_path_control`: reviewer does not control the execution path whose decision is challenged.

Let each dimension resolve to `SEPARATE`, `CONFLICT`, or `UNRESOLVED` from explicit evidence.

```text
IndependentReviewAvailable(r) =
  review_available(r)
  AND all_required_evidence_bound(r)
  AND every_required_dimension(r) == SEPARATE
```

A `CONFLICT` dimension produces `NOT_INDEPENDENT` unless an explicit mitigation record replaces the conflicted dimension with independently evidenced `SEPARATE`. `UNRESOLVED` never defaults to independent.

## 3. Conflict disclosure is not mitigation

Disclosing a conflict is evidence quality, not independence. A conflict can be mitigated only when the record contains a mitigation reference whose evaluator is itself outside the conflicted control relationship and whose evidence establishes the required separation. Circular self-attestation is invalid.

## 4. Relation to gate legitimacy

The completed gate-legitimacy formalism contains:

```text
independent_review_required
independent_review_satisfied
independent_review_ref
```

This predicate supplies the bounded proof contract for `independent_review_satisfied`. Gate legitimacy may consume the result as evidence, but the reviewer-independence record does not determine gate legitimacy by itself and does not determine candidate admissibility.

## 5. Relation to Governable Autonomy review records

The existing Governable Autonomy review schema can describe an `independent-peer-review` and independent reviewer identity class. A review claiming that state should additionally bind an independence record when the claim depends on structural independence rather than identity labeling alone.

No change to the existing review schema is required by this task. Integration can reference this record in a later compatibility task if desired.

## 6. Falsification cases

The predicate must reject or leave unresolved at least the following:

1. reviewer and gate under common control;
2. reviewer authored or controls the challenged rule;
3. reviewer has material financial interest in the challenged outcome;
4. reviewer is the same evaluator under a different display label;
5. reviewer controls the challenged execution path;
6. any required separation dimension lacks evidence;
7. a disclosed conflict with no independently evidenced mitigation.

It must accept:

- a review with independently evidenced separation across all five dimensions;
- a previously disclosed conflict only after a non-circular mitigation record establishes separation.

## 7. Authority ceiling

An `INDEPENDENT` result means only that the review satisfies the defined independence predicate. It does not mean the review is correct, binding, admissible as the sole evidence, or authorized to replace a governance decision. `authority_effect` is always `NONE`.
