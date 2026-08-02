# Time Causal Kernel Validation Receipt

- Goal: `time-invariant-kernel-integration-v1`
- Branch: `formal/time-invariant-kernel-integration-v1`
- Date: `2026-08-02`
- Validator: `scripts/validate_time_causal_kernel.py`
- Fixture: `fixtures/time-causal-kernel/minimal-valid.json`
- Result: `PASS`
- Observed output: `PASS: time causal kernel fixture is structurally valid`

## Verified invariants

- kernel relation set is acyclic;
- each branch relation set is acyclic;
- each branch extends the invariant kernel;
- temporal substrate does not assert GTG admissibility.

## Validation boundary

This receipt records deterministic local execution against the committed positive fixture. It does not prove negative fixtures, quotient lumpability, RTG integration, GTG integration, TT projection, workflow success, deployment, publication, or release readiness.
