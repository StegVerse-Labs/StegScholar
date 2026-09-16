from __future__ import annotations

import json
from pathlib import Path
import unittest

from scripts.validate_gtg_assurance_reference_integration import evaluate_gtg, validate, validate_schema_boundaries

ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "fixtures/gtg-assurance-reference-integration/cases.json"
TT_SCHEMA = ROOT / "schemas/tt-transition-cell.schema.json"


class GtgAssuranceReferenceIntegrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads(FIXTURES.read_text())
        cls.records = cls.data["assurance_records"]
        cls.cases = {case["case_id"]: case for case in cls.data["cases"]}

    def test_full_validator(self):
        validate()

    def test_schema_boundary(self):
        validate_schema_boundaries()
        tt = json.loads(TT_SCHEMA.read_text())
        self.assertIn("gtg_record_ref", tt["required"])
        self.assertNotIn("governance_assurance", tt["properties"])

    def test_historical_record_without_assurance_is_valid(self):
        gtg = self.cases["historical-no-assurance"]["gtg"]
        self.assertEqual(evaluate_gtg(gtg, self.records), "VALID")

    def test_required_unresolved_fails_closed(self):
        gtg = self.cases["required-unresolved-fails-closed"]["gtg"]
        self.assertEqual(evaluate_gtg(gtg, self.records), "FAIL_CLOSED_REQUIRED")

    def test_correlation_mismatches_are_rejected(self):
        for case_id in (
            "gate-candidate-mismatch",
            "independent-review-gate-mismatch",
            "architecture-candidate-mismatch",
        ):
            with self.subTest(case_id=case_id):
                self.assertEqual(evaluate_gtg(self.cases[case_id]["gtg"], self.records), "INVALID_BINDING")

    def test_authority_promotion_is_rejected(self):
        gtg = self.cases["authority-effect-promotion-rejected"]["gtg"]
        self.assertEqual(evaluate_gtg(gtg, self.records), "INVALID_BINDING")

    def test_optional_not_applicable_is_neutral(self):
        gtg = self.cases["optional-not-applicable-is-neutral"]["gtg"]
        self.assertEqual(evaluate_gtg(gtg, self.records), "VALID")

    def test_architecture_neutrality_does_not_force_allow(self):
        gtg = self.cases["architecture-neutrality-does-not-force-allow"]["gtg"]
        self.assertEqual(gtg["disposition"], "DENY")
        self.assertEqual(evaluate_gtg(gtg, self.records), "VALID")

    def test_tt_reconstructs_only_through_gtg_record_ref(self):
        case_by_record = {case["gtg"]["record_id"]: case for case in self.data["cases"]}
        for tt_case in self.data["tt_cases"]:
            tt = tt_case["tt"]
            self.assertNotIn("governance_assurance", tt)
            gtg_case = case_by_record[tt["gtg_record_ref"]]
            self.assertEqual(evaluate_gtg(gtg_case["gtg"], self.records), tt_case["expected"])


if __name__ == "__main__":
    unittest.main()
