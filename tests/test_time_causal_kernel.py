#!/usr/bin/env python3
from __future__ import annotations
import subprocess, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / "scripts" / "validate_time_causal_kernel.py"
CASES = {
    "minimal-valid.json": 0,
    "lumpability-valid.json": 0,
    "cyclic-kernel.json": 1,
    "unsupported-branch.json": 1,
    "manufactured-coarse-chronology.json": 1,
    "lumpability-invalid.json": 1,
    "gtg-boundary-invalid.json": 1,
}

def main() -> int:
    failures = []
    for name, expected in CASES.items():
        path = ROOT / "fixtures" / "time-causal-kernel" / name
        result = subprocess.run([sys.executable, str(VALIDATOR), str(path)], capture_output=True, text=True)
        if result.returncode != expected:
            failures.append(f"{name}: expected {expected}, got {result.returncode}: {result.stdout}{result.stderr}")
        else:
            print(f"PASS {name}: exit {result.returncode}")
    if failures:
        print("TIME CAUSAL KERNEL MATRIX FAILED", file=sys.stderr)
        for failure in failures: print(f"- {failure}", file=sys.stderr)
        return 1
    print("TIME CAUSAL KERNEL MATRIX PASSED")
    return 0

if __name__ == "__main__": raise SystemExit(main())
