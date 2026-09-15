from __future__ import annotations

import json
from pathlib import Path
import unittest

from scripts.validate_gate_legitimacy import derive_legitimacy_state, validate_fixture_file

ROOT = Path(__file__).resolve().parents[1]
FIXTURE_PATH = ROOT / "fixtures/gate-legitimacy/gate-legitimacy-cases.json"


class GateLegitimacyInvariantTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = json.loads(FIXTURE_PATH.read_text())
        cls.cases = {case["case_id"]: case for case in cls.payload["cases"]}

    def test_all_fixtures_validate(self) -> None:
        result = validate_fixture_file(FIXTURE_PATH)
        self.assertEqual(result["result"], "PASS", result)

    def test_missing_standard_provenance_is_illegitimate(self) -> None:
        record = self.cases["GL-MISSING-STANDARD-PROVENANCE-001"]["record"]
        state, reasons = derive_legitimacy_state(record)
        self.assertEqual(state, "ILLEGITIMATE")
        self.assertIn("MISSING_STANDARD_PROVENANCE", reasons)

    def test_posthoc_evidence_rules_are_illegitimate(self) -> None:
        record = self.cases["GL-POSTHOC-EVIDENCE-RULES-001"]["record"]
        state, reasons = derive_legitimacy_state(record)
        self.assertEqual(state, "ILLEGITIMATE")
        self.assertIn("EVIDENCE_RULES_NOT_PREDECLARED", reasons)

    def test_rule_controller_overlap_requires_independent_review(self) -> None:
        record = self.cases["GL-EVALUATOR-RULE-CONTROLLER-CONFLICT-001"]["record"]
        state, reasons = derive_legitimacy_state(record)
        self.assertEqual(state, "CONFLICTED")
        self.assertIn("INDEPENDENT_REVIEW_REQUIRED", reasons)

    def test_execution_controller_overlap_requires_independent_review(self) -> None:
        record = self.cases["GL-EVALUATOR-EXECUTION-CONTROLLER-CONFLICT-001"]["record"]
        state, reasons = derive_legitimacy_state(record)
        self.assertEqual(state, "CONFLICTED")
        self.assertIn("INDEPENDENT_REVIEW_REQUIRED", reasons)

    def test_disclosed_conflict_can_be_mitigated_without_minting_authority(self) -> None:
        record = self.cases["GL-CONFLICT-MITIGATED-BY-INDEPENDENT-REVIEW-001"]["record"]
        state, _ = derive_legitimacy_state(record)
        self.assertEqual(state, "LEGITIMATE")
        self.assertEqual(record["authority_effect"], "NONE")

    def test_legitimate_gate_can_still_reference_candidate_deny(self) -> None:
        record = self.cases["GL-VALID-001"]["record"]
        state, _ = derive_legitimacy_state(record)
        self.assertEqual(state, "LEGITIMATE")
        self.assertEqual(record["candidate_disposition_ref"], "gtg:deny-candidate-a")


if __name__ == "__main__":
    unittest.main()
