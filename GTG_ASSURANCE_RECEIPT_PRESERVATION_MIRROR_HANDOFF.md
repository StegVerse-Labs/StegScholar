# GTG Assurance Receipt Preservation Mirror Handoff

Updated: 2026-09-16
Goal Task ID: `GTG-ASSURANCE-RECEIPT-PRESERVATION-001`
COSV: `10100000100000`
Status: `ACTIVE / CLAIMED_IMPLEMENTATION`
Parent sweep: `GTG-ASSURANCE-CONSUMER-COMPATIBILITY-SWEEP-001` (`RETIRED / COMPLETED`)
Implementation branch: `gtg-assurance-receipt-preservation-001`

## Demonstrated gap

The bounded consumer-compatibility sweep proved before repair that `scripts/validate_gtg_fixtures.py:validate_case` accepted a source fixture containing optional `governance_assurance` but its emitted `GTG-DECISION-*` receipt was built from an explicit field list that dropped the assurance object.

Gap classification: `ASSURANCE_DROPPED_BY_LEGACY_FIXTURE_RECEIPT_SERIALIZER`.

## Collision check

No open StegScholar or `.github` PR matching this repair task was found, and no matching StegScholar branch existed before claim. The bounded child task was therefore claimed without reopening the retired parent sweep.

## Repair applied on branch

- `scripts/validate_gtg_fixtures.py` now preserves the exact optional `governance_assurance` object in each emitted case receipt when present.
- No `governance_assurance` field is emitted when the source case omits it.
- Preserved assurance must retain `authority_effect: NONE`; any other value fails validation.
- `receipt_hash` is computed only after optional assurance is inserted, so the preserved representation is covered deterministically.
- Existing GTG activation/disposition derivation is unchanged.
- TT is unchanged and continues to reconstruct cross-layer state only through `gtg_record_ref`.

## Regression coverage

`tests/test_gtg_assurance_receipt_preservation.py` checks exact assurance round-trip preservation, historical absent-assurance compatibility, receipt-hash sensitivity to assurance changes, mandatory `authority_effect: NONE`, and unchanged TT schema ownership.

`tests/test_gtg_assurance_consumer_compatibility_sweep.py` now verifies that the formerly demonstrated serializer gap is repaired while preserving the sweep's non-authority and no-TT-duplication observations. The retired sweep's historical evidence remains in its paper/handoff and is not reopened.

## Required repair properties

- exact assurance preservation sufficient for reconstruction;
- no assurance field added to receipts when absent from the source case;
- `authority_effect: NONE` remains mandatory for preserved assurance content;
- historical receipts remain readable without retroactive mutation;
- receipt hashing covers the preserved representation deterministically;
- TT remains unchanged and continues to use only `gtg_record_ref` for cross-layer ownership;
- no change to GTG disposition algebra.

## Completion threshold

Do not retire this task until the implementation PR reaches exact-head green validation, merges, and canonical `.github` coordination is reconciled with merged evidence.
