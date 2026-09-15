# GTG Assurance Reference Integration Mirror Handoff

Updated: 2026-09-15
Goal Task ID: `GTG-ASSURANCE-REFERENCE-INTEGRATION-001`
COSV: `10100000100000`
Status: `ACTIVE / UNCLAIMED`
Parent review: `GTG-TT-MILLINGS-FORMALISM-COMPATIBILITY-REVIEW-001`

## Goal

Integrate the completed Gate Legitimacy, Independent Review, and Architecture-Neutral Admissibility formalisms into canonical GTG as typed, non-authorizing assurance references while preserving current GTG disposition ownership and TT's existing `gtg_record_ref` relationship.

## Minimum scope

1. Add an optional typed `governance_assurance` object to the canonical GTG decision/governance records.
2. Support three typed slots:
   - gate legitimacy;
   - independent review;
   - architecture-neutral admissibility.
3. For each slot, represent applicability, record reference, and validation state.
4. Deterministically validate schema/type, `authority_effect: NONE`, and subject/candidate/gate/rule/evaluator correlation.
5. Allow profiles to require an assurance check without making every assurance universally mandatory.
6. Add cross-layer GTG->TT tests proving TT reconstruction follows `gtg_record_ref` rather than duplicating assurance state.

## Explicit non-goals

- no new GTG disposition algebra;
- no second governance authority;
- no new TT assurance fields unless falsification demonstrates `gtg_record_ref` is insufficient;
- no duplication of GTG evidence, standing, authority, policy, constraints, or commit-time checks;
- no conversion of any `authority_effect: NONE` record into execution or transition authority;
- no retroactive invalidation of historical GTG/TT records that predate the optional integration.

## Required falsification cases

- mismatched gate/candidate assurance reference rejected;
- independent-review declaration without a validated independent-review record does not satisfy a required slot;
- architecture-neutrality does not force `ALLOW` and cannot override substantive denial;
- gate legitimacy does not mint authority;
- unresolved required assurance fails closed according to profile policy;
- optional/not-applicable assurance does not create false failure;
- TT cell cannot hide an invalid GTG assurance binding;
- TT receives no independently mutable copy of assurance state.

## Completion threshold

Complete only when canonical GTG schemas, fixtures, validators, cross-layer tests, README, and handoff are validated and merged, with TT schema left unchanged unless evidence proves a schema change is required.
