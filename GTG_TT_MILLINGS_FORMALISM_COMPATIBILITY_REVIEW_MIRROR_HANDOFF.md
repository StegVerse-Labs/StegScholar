# GTG/TT Millings Formalism Compatibility Review Mirror Handoff

Updated: 2026-09-15
Goal Task ID: `GTG-TT-MILLINGS-FORMALISM-COMPATIBILITY-REVIEW-001`
COSV: `40000100100000`
Status: `ACTIVE / CLAIMED_INTEGRATION`

## Goal

Review the three retired Millings-derived formalisms against the current canonical GTG and TT schemas and derive only integration work that materially improves deterministic governance without duplicating existing semantics or creating new authority.

## Source state

The following tasks remain terminal and must not be reopened:

- `MILLINGS-RTG-GTG-TT-COMPARISON-001`
- `GATE-LEGITIMACY-INVARIANT-001`
- `INDEPENDENT-REVIEW-PREDICATE-001`
- `ARCHITECTURE-NEUTRAL-ADMISSIBILITY-001`

Reviewed source schemas:

- `schemas/gtg-decision.schema.json`
- `schemas/gtg-governance-record.schema.json`
- `schemas/tt-transition-cell.schema.json`
- `schemas/gate-legitimacy-record.schema.json`
- `schemas/independent-review-record.schema.json`
- `schemas/architecture-neutral-admissibility-record.schema.json`

## Compatibility conclusion

Current GTG already carries substantive standing, authority, evidence, policy, constraints, activation, disposition, challenge/continuation, and commit-state semantics. Current TT already carries a canonical `gtg_record_ref`, decision, commit validation, execution posture, observation posture, consequence relation, and receipts.

The material integration gap is **not** another disposition layer and is **not** a second TT copy of the three formalisms. The gap is a typed, deterministic GTG binding that says which non-authorizing assurance records were applicable to one decision, binds them to the same candidate/decision context, and proves they retained `authority_effect: NONE`.

Generic GTG `evidence.refs`, `continuation.challenge_refs`, `appeal_paths`, and TT `evidence_refs` can carry opaque references but do not currently distinguish:

- gate-legitimacy evidence from ordinary evidence;
- independent-review evidence from merely available review;
- architecture-neutrality assessment from substantive admissibility itself;
- applicable vs not-applicable assurance checks;
- a valid reference from one that is mismatched to another candidate/gate/decision.

## Minimum integration disposition

Exactly one new integration Goal Task is necessary:

`GTG-ASSURANCE-REFERENCE-INTEGRATION-001`

It should add an optional typed GTG assurance-binding object that can reference the three completed formalism records, validate subject/candidate/gate/decision correlation, preserve `authority_effect: NONE`, and declare applicability. Profiles may require one or more assurance checks; absence is not automatically failure unless the active profile says the check is required.

### TT disposition

No new TT transition-cell fields are justified at this stage. `gtg_record_ref` already provides the authoritative linkage to the governance record. Duplicating the three assurance refs inside TT would create a second copy that can drift from GTG.

The integration task should instead add deterministic cross-layer tests proving:

1. TT reconstruction through `gtg_record_ref` can recover the applicable assurance refs;
2. TT does not infer disposition, authority, execution, or consequence from any assurance record;
3. a GTG assurance mismatch cannot be hidden by a syntactically valid TT cell;
4. historical TT cells remain reconstructable without retroactive mutation.

## Authority ceiling

Gate Legitimacy, Independent Review, and Architecture-Neutral Admissibility remain evidence/formalism layers with `authority_effect: NONE`. The integration must not mint standing, authority, credentials, execution permission, GTG disposition, TT execution, or consequence truth.

## Completion threshold

This compatibility-review task completes when the review paper, canonical task record, and the single derived integration task are merged and validated. Implementation of `GTG-ASSURANCE-REFERENCE-INTEGRATION-001` occurs only under that separate task.
