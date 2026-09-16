# GTG Governance Assurance Consumer Compatibility Sweep

Goal Task: `GTG-ASSURANCE-CONSUMER-COMPATIBILITY-SWEEP-001`

## Scope

This bounded sweep reviews the newly merged optional `governance_assurance` field across current repository-visible GTG producers, serializers, validators, reconstruction paths, and active governance consumers. The retired integration task remains closed.

## Inventory

The canonical GTG decision and governance-record schemas accept optional `governance_assurance`; the dedicated assurance validator checks typed bindings, profile-scoped applicability, correlation, and `authority_effect: NONE`. TT retains only `gtg_record_ref` and does not duplicate assurance state.

Repository-visible searches for `governance_assurance`, `gtg_record_ref`, and canonical GTG schema references found the active assurance validator/tests and the established GTG reconstruction relation. The current GTG task orchestrator operates on coordination task metadata and does not reinterpret assurance as authority.

The legacy deterministic GTG fixture producer/serializer `scripts/validate_gtg_fixtures.py:validate_case` was also swept because it emits `GTG-DECISION-*` receipts from GTG fixture cases.

## Demonstrated compatibility gap

A deterministic probe supplies a valid GTG fixture case containing an optional `governance_assurance` object with `authority_effect: NONE`. The legacy validator accepts the case, but the emitted receipt is constructed from an explicit field list that does not include `governance_assurance`. The assurance object is therefore dropped during serialization.

Classification:

`ASSURANCE_DROPPED_BY_LEGACY_FIXTURE_RECEIPT_SERIALIZER`

This is a reconstruction/continuity defect, not an authority defect. No path in the bounded sweep was observed promoting assurance into standing, GTG disposition, execution permission, or consequence truth.

## Non-gaps

- canonical schemas accept the optional assurance field;
- the dedicated assurance validator preserves non-authorizing semantics;
- TT still contains no independently mutable assurance copy;
- `gtg_record_ref` remains the intended GTG-to-TT reconstruction relation;
- task orchestration surfaces operate on coordination metadata and do not consume assurance as authority.

## Derived work

Exactly one bounded implementation Goal Task is justified:

`GTG-ASSURANCE-RECEIPT-PRESERVATION-001`

It should update the legacy GTG fixture receipt producer/serializer so that when a source GTG case contains `governance_assurance`, the receipt retains an exact non-authorizing copy or a deterministic reference/hash sufficient for reconstruction. The repair must preserve historical receipts, continue to omit assurance when absent, and must not make assurance a source of authority or modify TT.

No broader consumer rewrite is justified by current evidence.
