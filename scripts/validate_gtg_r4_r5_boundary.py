#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CASES = ROOT / "coordination" / "gtg-r4-r5-boundary-cases.json"


def classify(case: dict) -> str:
    if case.get("execution_authorized") is True:
        return "BOUNDARY_FAIL_CLOSED"
    if case["r4"] != "VALID":
        return "BOUNDARY_FAIL_CLOSED"
    r5 = case["r5"]
    if r5 == "OBSERVED_FRESH_BOUND":
        return "BOUNDARY_SURVIVES"
    if r5 in {"MISSING_CUSTODY", "STALE", "INTERNAL_ONLY"}:
        return "BOUNDARY_PARTIAL"
    return "BOUNDARY_FAIL_CLOSED"


def main() -> None:
    data = json.loads(CASES.read_text())
    cases = data.get("cases", [])
    if len(cases) != 10:
        raise SystemExit("R4-R5 BOUNDARY: FAIL - expected ten cases")
    ids = [c["id"] for c in cases]
    if len(ids) != len(set(ids)):
        raise SystemExit("R4-R5 BOUNDARY: FAIL - duplicate case IDs")
    for case in cases:
        actual = classify(case)
        if actual != case["expected"]:
            raise SystemExit(f"R4-R5 BOUNDARY: FAIL - {case['id']} expected {case['expected']} got {actual}")
    for key, value in data.get("claims", {}).items():
        if value is not False:
            raise SystemExit(f"R4-R5 BOUNDARY: FAIL - prohibited claim enabled: {key}")
    print("R4-R5 BOUNDARY: PASS - ten bounded cases validated; no authority effect created")


if __name__ == "__main__":
    main()
