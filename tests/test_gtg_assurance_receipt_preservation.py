import copy
import json
import unittest
from pathlib import Path

from scripts.validate_gtg_assurance_consumer_compatibility_sweep import synthetic_case
from scripts.validate_gtg_fixtures import canonical_hash, validate_case

ROOT = Path(__file__).resolve().parents[1]
TT_SCHEMA = ROOT / "schemas" / "tt-transition-cell.schema.json"


class TestGtgAssuranceReceiptPreservation(unittest.TestCase):
    def test_optional_assurance_is_preserved_exactly_and_reconstructable(self):
        case = synthetic_case()
        errors, receipt = validate_case(case, set())
        self.assertEqual(errors, [])
        self.assertIsNotNone(receipt)
        self.assertEqual(receipt["governance_assurance"], case["governance_assurance"])
        reconstructed = json.loads(json.dumps(receipt, sort_keys=True))
        self.assertEqual(reconstructed["governance_assurance"], case["governance_assurance"])
        receipt_without_hash = dict(reconstructed)
        stored_hash = receipt_without_hash.pop("receipt_hash")
        self.assertEqual(stored_hash, canonical_hash(receipt_without_hash))

    def test_absent_assurance_remains_absent_and_historical_shape_stays_compatible(self):
        case = synthetic_case()
        case.pop("governance_assurance")
        errors, receipt = validate_case(case, set())
        self.assertEqual(errors, [])
        self.assertIsNotNone(receipt)
        self.assertNotIn("governance_assurance", receipt)

    def test_receipt_hash_changes_when_preserved_assurance_changes(self):
        case = synthetic_case()
        errors, first = validate_case(case, set())
        self.assertEqual(errors, [])
        changed = copy.deepcopy(case)
        changed["governance_assurance"]["assurance_id"] = "sweep-probe-changed"
        errors, second = validate_case(changed, set())
        self.assertEqual(errors, [])
        self.assertNotEqual(first["receipt_hash"], second["receipt_hash"])

    def test_assurance_cannot_promote_authority(self):
        case = synthetic_case()
        case["governance_assurance"]["authority_effect"] = "ALLOW"
        errors, receipt = validate_case(case, set())
        self.assertIsNone(receipt)
        self.assertTrue(any("authority_effect must equal NONE" in error for error in errors))

    def test_tt_schema_remains_unchanged(self):
        tt = json.loads(TT_SCHEMA.read_text(encoding="utf-8"))
        self.assertIn("gtg_record_ref", tt["required"])
        self.assertNotIn("governance_assurance", tt["properties"])


if __name__ == "__main__":
    unittest.main()
