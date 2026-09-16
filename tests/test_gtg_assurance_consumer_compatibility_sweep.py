import unittest

from scripts.validate_gtg_assurance_consumer_compatibility_sweep import run_sweep


class TestGtgAssuranceConsumerCompatibilitySweep(unittest.TestCase):
    def test_legacy_fixture_receipt_now_preserves_optional_assurance(self):
        result = run_sweep()
        self.assertTrue(result["source_assurance_present"])
        self.assertTrue(result["serialized_assurance_preserved"])
        self.assertIsNone(result["demonstrated_gap"])
        self.assertFalse(result["derived_task_required"])

    def test_no_tt_duplication_or_authority_promotion(self):
        result = run_sweep()
        self.assertFalse(result["tt_duplicates_assurance"])
        self.assertFalse(result["authority_promotion_observed"])
        self.assertEqual(result["tt_reconstruction_relation"], "gtg_record_ref")


if __name__ == "__main__":
    unittest.main()
