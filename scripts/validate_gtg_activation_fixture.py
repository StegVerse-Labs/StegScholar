#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "schemas" / "gtg-governance-activation.schema.json"
FIXTURE = ROOT / "fixtures" / "gtg" / "individually-authorized-relationally-inadmissible.activation.json"

REQUIRED_TESTS = (
    "discoverable",
    "commit_reconstructable",
    "basis_attached",
    "included_in_admissibility",
    "outcome_sensitive",
)


def fail(message: str) -> int:
    print(f"GTG ACTIVATION FIXTURE: FAIL\n- {message}")
    return 1


def main() -> int:
    if not SCHEMA.exists():
        return fail(f"missing {SCHEMA.relative_to(ROOT)}")
    if not FIXTURE.exists():
        return fail(f"missing {FIXTURE.relative_to(ROOT)}")

    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    record = json.loads(FIXTURE.read_text(encoding="utf-8"))

    if schema.get("properties", {}).get("authority", {}).get("properties", {}).get("execution_authority", {}).get("const") is not False:
        return fail("schema must hold execution_authority false")
    if schema.get("properties", {}).get("authority", {}).get("properties", {}).get("certification_authority", {}).get("const") is not False:
        return fail("schema must hold certification_authority false")

    tests = record.get("activation_tests", {})
    missing = [name for name in REQUIRED_TESTS if tests.get(name) is not True]
    if missing:
        return fail("activation predicate incomplete: " + ", ".join(missing))

    if record.get("activation_result") != "ACTIVE":
        return fail("fixture must activate relational governance")

    relation_classes = set(record.get("relational_projection", {}).get("relation_classes", []))
    required_classes = {"AUTHORITY", "CONSTRAINT", "CONSENT", "CONSEQUENCE"}
    if not required_classes.issubset(relation_classes):
        return fail("fixture does not represent the required relational conflict classes")

    participants = record.get("relational_projection", {}).get("participants", [])
    if len(participants) < 3:
        return fail("fixture must include both authorized actors and the protected subject")

    authority = record.get("authority", {})
    if authority.get("execution_authority") is not False:
        return fail("activation record must not inherit execution authority")
    if authority.get("certification_authority") is not False:
        return fail("activation record must not create certification authority")

    continuation = record.get("continuation", {})
    if continuation.get("survives_actor_termination") is not True:
        return fail("relational judgment must survive short-lived actors")
    if not continuation.get("reconstruction_refs"):
        return fail("fixture requires an independent reconstruction reference")

    print("GTG ACTIVATION FIXTURE: PASS")
    print("- relational governance activation: ACTIVE")
    print("- individually authorized actors do not establish joint admissibility")
    print("- execution and certification authority remain false")
    print("- continuation survives actor termination")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
