from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/validate_independent_review.py"
FIXTURES = ROOT / "fixtures/independent-review/independent-review-cases.json"
SCHEMA = ROOT / "schemas/independent-review-record.schema.json"
PAPER = ROOT / "papers/transition-table/independent-review-predicate.md"

spec = importlib.util.spec_from_file_location("validate_independent_review", SCRIPT)
mod = importlib.util.module_from_spec(spec)
assert spec and spec.loader
spec.loader.exec_module(mod)


class IndependentReviewPredicateTests(unittest.TestCase):
    def test_fixtures_match_expected_states(self):
        payload = json.loads(FIXTURES.read_text())
        failures = mod.validate_cases(payload["cases"])
        self.assertEqual(failures, [])

    def test_all_required_dimensions_are_present(self):
        self.assertEqual(
            set(mod.REQUIRED_DIMENSIONS),
            {"common_control", "rule_authorship", "financial_interest", "evaluator_identity", "execution_path_control"},
        )

    def test_conflict_is_not_independent(self):
        dimensions = {name: {"state": "SEPARATE", "evidence_refs": [f"ev-{name}"]} for name in mod.REQUIRED_DIMENSIONS}
        dimensions["financial_interest"] = {"state": "CONFLICT", "evidence_refs": ["ev-financial-conflict"]}
        state, reasons = mod.evaluate_review(True, dimensions)
        self.assertEqual(state, "NOT_INDEPENDENT")
        self.assertIn("CONFLICT:financial_interest", reasons)

    def test_missing_evidence_fails_unresolved(self):
        dimensions = {name: {"state": "SEPARATE", "evidence_refs": [f"ev-{name}"]} for name in mod.REQUIRED_DIMENSIONS}
        dimensions["common_control"] = {"state": "SEPARATE", "evidence_refs": []}
        state, reasons = mod.evaluate_review(True, dimensions)
        self.assertEqual(state, "UNRESOLVED")
        self.assertIn("UNRESOLVED:common_control", reasons)

    def test_review_availability_is_not_independence(self):
        state, reasons = mod.evaluate_review(False, {})
        self.assertEqual(state, "UNRESOLVED")
        self.assertEqual(reasons, ["REVIEW_NOT_AVAILABLE"])

    def test_authority_effect_is_none(self):
        schema = json.loads(SCHEMA.read_text())
        self.assertEqual(schema["properties"]["authority_effect"]["const"], "NONE")

    def test_paper_preserves_non_authority_boundary(self):
        text = PAPER.read_text()
        self.assertIn("IndependentReview(r) != GovernanceAuthority(r)", text)
        self.assertIn("reviewer_identity_label != reviewer_independence_proof", text)
        self.assertIn("authority_effect` is always `NONE`", text)


if __name__ == "__main__":
    unittest.main()
