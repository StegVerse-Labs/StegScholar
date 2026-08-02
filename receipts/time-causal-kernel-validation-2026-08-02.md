# Time Causal Kernel Validation Receipt

- Goal: `time-invariant-kernel-integration-v1`
- Branch: `formal/time-invariant-kernel-integration-v1`
- Date: `2026-08-02`
- Validator: `scripts/validate_time_causal_kernel.py`
- Matrix: `tests/test_time_causal_kernel.py`
- Hosted workflow: `Time Causal Kernel`
- Workflow run: `30766477730`
- Job: `91546000999`
- Head commit validated: `c5839d516c415e65a0a96ba90ac65bf41ac582e9`
- Result: `PASS`

## Fixture matrix

Expected acceptance:

- `fixtures/time-causal-kernel/minimal-valid.json`
- `fixtures/time-causal-kernel/lumpability-valid.json`

Expected rejection:

- `fixtures/time-causal-kernel/cyclic-kernel.json`
- `fixtures/time-causal-kernel/unsupported-branch.json`
- `fixtures/time-causal-kernel/manufactured-coarse-chronology.json`
- `fixtures/time-causal-kernel/lumpability-invalid.json`
- `fixtures/time-causal-kernel/gtg-boundary-invalid.json`

## Verified invariants

- kernel relation sets are acyclic;
- branch relation sets are acyclic;
- every supported branch extends the invariant kernel;
- coarse chronology requires a fine-resolution witness;
- quotient-equivalent representatives must induce identical normalized coarse distributions where lumpability is claimed;
- temporal substrate objects fail closed if they assert GTG admissibility.

## Hosted evidence

The `Time Causal Kernel` workflow completed successfully. Its `validate` job and `Run causal-kernel fixture matrix` step both concluded `success`.

The repository-wide `Test Readiness` workflow run `30766477723` also completed successfully for the same head commit.

## Validation boundary

This receipt proves committed fixture-matrix execution and hosted workflow success. It does not prove RTG binding, GTG runtime integration, TT projection, cross-repository propagation, deployment, publication, governed activation, merge, tag, or release readiness.
