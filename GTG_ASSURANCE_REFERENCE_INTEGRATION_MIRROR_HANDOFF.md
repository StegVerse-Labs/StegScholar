# GTG Assurance Reference Integration Mirror Handoff

Updated: 2026-09-15
Goal Task ID: `GTG-ASSURANCE-REFERENCE-INTEGRATION-001`
COSV: `40000100100000`
Status: `ACTIVE / CLAIMED_IMPLEMENTATION`
Parent review: `GTG-TT-MILLINGS-FORMALISM-COMPATIBILITY-REVIEW-001` (`RETIRED / COMPLETED`)

## Goal

Integrate the completed Gate Legitimacy, Independent Review, and Architecture-Neutral Admissibility formalisms into canonical GTG as typed, non-authorizing assurance references while preserving current GTG disposition ownership and TT's existing `gtg_record_ref` relationship.

## Collision check

Canonical `schemas/gtg-decision.schema.json`, `schemas/gtg-governance-record.schema.json`, and `schemas/tt-transition-cell.schema.json` were reviewed before claim. No existing `governance_assurance` object or equivalent typed binding was present. Open StegScholar PR #51 changes only `coordination/gtg-task-completion-report.json`; it does not modify the schemas, fixtures, validators, tests, workflow, or this handoff. No equivalent assurance-integration PR was found.

## Claimed implementation

1. Add an optional typed `governance_assurance` object to both canonical GTG decision/governance schemas.
2. Support typed slots `gate_legitimacy`, `independent_review`, and `architecture_neutral_admissibility`.
3. Each slot carries applicability, record reference, validation state, correlation data, and `authority_effect: NONE`.
4. `required_types` is profile-scoped. Optional/not-applicable checks do not fail merely by absence; required unresolved/invalid checks deterministically produce `FAIL_CLOSED_REQUIRED` in validation.
5. Validate assurance source type and correlation to the active candidate/gate/rule/evaluator context.
6. Preserve historical GTG records that omit `governance_assurance`.
7. Keep `schemas/tt-transition-cell.schema.json` unchanged and prove reconstruction follows only `gtg_record_ref`.

## Explicit non-goals

- no new GTG disposition algebra;
- no second governance authority;
- no duplicate TT assurance fields;
- no duplication of standing/evidence/authority/policy/constraint/commit-time semantics;
- no conversion of `authority_effect: NONE` into transition or execution authority;
- no retroactive invalidation of historical records.

## Required falsification cases

- historical GTG decision/governance records without assurance remain valid;
- gate-legitimacy candidate/gate mismatch is rejected;
- independent-review challenged-gate/evaluator mismatch is rejected when the active binding declares those correlation keys;
- architecture-neutral candidate mismatch is rejected;
- any assurance record whose `authority_effect` is not `NONE` is rejected;
- required unresolved/invalid assurance returns `FAIL_CLOSED_REQUIRED`;
- optional/not-applicable assurance does not create false failure;
- architecture-neutrality never forces `ALLOW` or overrides a substantive GTG denial;
- TT reconstruction through `gtg_record_ref` recovers the GTG assurance object;
- TT has no `governance_assurance` property and cannot hide an invalid GTG assurance binding.

## Completion threshold

Complete only when canonical GTG schemas, fixtures, validator, tests, workflow, README, and handoff are exact-head green and merged, with TT schema unchanged.
