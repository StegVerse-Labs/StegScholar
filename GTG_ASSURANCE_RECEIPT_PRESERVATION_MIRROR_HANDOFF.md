# GTG Assurance Receipt Preservation Mirror Handoff

Updated: 2026-09-15
Goal Task ID: `GTG-ASSURANCE-RECEIPT-PRESERVATION-001`
COSV: `10100000100000`
Status: `ACTIVE / UNCLAIMED`
Parent sweep: `GTG-ASSURANCE-CONSUMER-COMPATIBILITY-SWEEP-001`

## Demonstrated gap

The bounded consumer-compatibility sweep proved that `scripts/validate_gtg_fixtures.py:validate_case` accepts a source fixture containing optional `governance_assurance` but its emitted `GTG-DECISION-*` receipt is built from an explicit field list that drops the assurance object.

Gap classification: `ASSURANCE_DROPPED_BY_LEGACY_FIXTURE_RECEIPT_SERIALIZER`.

## Goal

Preserve optional GTG `governance_assurance` across legacy GTG fixture receipt serialization and subsequent reconstruction without promoting assurance into governance, standing, execution, or consequence authority.

## Required repair properties

- exact assurance preservation or deterministic reference/hash preservation sufficient for reconstruction;
- no assurance field added to receipts when absent from the source case;
- `authority_effect: NONE` remains mandatory for any preserved assurance content;
- historical receipts remain readable without retroactive mutation;
- receipt hashing covers the preserved representation deterministically;
- TT remains unchanged and continues to use only `gtg_record_ref` for cross-layer ownership;
- no change to GTG disposition algebra.

## Completion threshold

Complete only after a pre-fix negative fixture reproduces loss, the producer/serializer repair passes deterministic tests, historical no-assurance receipts remain compatible, exact-head validation is green, and canonical coordination is reconciled.
