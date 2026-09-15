from __future__ import annotations
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "scripts/validate_architecture_neutral_admissibility.py"
FIXTURES = ROOT / "fixtures/architecture-neutral-admissibility/cases.json"
SCHEMA = ROOT / "schemas/architecture-neutral-admissibility-record.schema.json"
PAPER = ROOT / "papers/generalized-transition-governance/architecture-neutral-admissibility.md"

spec = importlib.util.spec_from_file_location("arch_neutral", MODULE_PATH)
mod = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(mod)


class ArchitectureNeutralAdmissibilityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads(FIXTURES.read_text())
        cls.cases = {c["case_id"]: c for c in cls.data["cases"]}

    def test_validator_passes_complete_fixture_set(self):
        mod.validate()

    def test_architecture_difference_alone_does_not_create_failure(self):
        novel = self.cases["novel-different-evidence-path-all-pass"]
        incumbent = self.cases["incumbent-all-pass"]
        self.assertTrue(novel["different_from_incumbent"])
        self.assertEqual(mod.classify(novel), "SUBSTANTIVE_REQUIREMENTS_SATISFIED")
        self.assertEqual(mod.classify(incumbent), "SUBSTANTIVE_REQUIREMENTS_SATISFIED")

    def test_conformity_only_denial_is_invalid_basis(self):
        case = self.cases["conformity-only-denial"]
        self.assertTrue(all(v == "PASS" for v in case["checks"].values()))
        self.assertEqual(mod.classify(case), "CONFORMITY_ONLY_DENIAL_INVALID")

    def test_substantive_denials_survive_architecture_neutrality(self):
        for cid in (
            "evidence-failure",
            "authority-failure",
            "standing-failure",
            "safety-constraint-failure",
            "policy-failure",
            "commit-time-failure",
        ):
            with self.subTest(case=cid):
                self.assertEqual(mod.classify(self.cases[cid]), "SUBSTANTIVE_DENIAL_SUPPORTED")

    def test_unresolved_required_state_fails_closed(self):
        self.assertEqual(mod.classify(self.cases["unresolved-required-state"]), "FAIL_CLOSED_REQUIRED")

    def test_schema_and_paper_preserve_non_authority_boundary(self):
        schema = json.loads(SCHEMA.read_text())
        self.assertEqual(schema["properties"]["authority_effect"]["const"], "NONE")
        text = PAPER.read_text()
        self.assertIn("ArchitectureNeutrality(c) != ALLOW(c)", text)
        self.assertIn("does not issue a GTG disposition", text)


if __name__ == "__main__":
    unittest.main()
