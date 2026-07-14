# Rigel Validation Progress

## Current implementation state

The first reproducible validation lane now contains:

- `scalar_delayed_control.py` — independent-outcome scalar delayed-control benchmark;
- `test_scalar_delayed_control.py` — deterministic implementation tests;
- `scalar-delayed-control.config.json` — canonical benchmark declaration;
- `scalar-delayed-control.config.schema.json` — machine-readable configuration contract;
- `constant_total_latency_ablation.py` — matched-scenario phase-redistribution benchmark;
- `.github/workflows/rigel-validation.yml` — automated tests, canonical simulation, ablation, receipts, hashing, and artifact upload.

## Commits

- Scalar benchmark source: `46322db84e2d3d71df47cd4b13e04974b5c2c396`
- Simulation methodology: `26675a62afe817e6bdfc3d00dd2c33560a6069f4`
- Deterministic test suite: `db3b23bdb141576ac7ba09909599eab562c370a1`
- Canonical configuration: `0fdf314808862dab39269d325722d8b71e095cb8`
- Configuration schema: `e42047f4da0fa3c992fa33f4c2ad0a42faf66ce9`
- Simulation README update: `a27747e5fa18a100bd4ad9b4a4f6e7b4cb9e5eaa`
- Initial validation workflow: `1d2bff0182372be135651aee19814f7f0e82efb1`
- Constant-total-latency ablation: `f9a2933a3c3f5226b9e9a8e4056aee2222b3b4c2`
- Workflow integration of ablation: `b3ee3bd4e23f050f84562e0db76806556a0b9d15`

## What the constant-total-latency ablation tests

Each matched scenario uses identical:

- total latency;
- plant-growth rate;
- controller gain;
- initial state magnitude;
- process-noise level;
- sensor-noise level;
- stochastic seed.

Only the partition of total latency among observation, commitment, and realization phases changes.

The benchmark records whether matched scenarios produce different independently defined recovery outcomes. A nonzero partition-dependent fraction is evidence that the internal location of delay matters in this constructed model. It is not evidence of cross-domain universality.

## Current evidence status

Source and workflow infrastructure are committed. No successful workflow execution, generated artifact hashes, or validation receipts have yet been inspected and durably cited here.

Therefore:

- implementation status: **committed**;
- execution status: **pending verification**;
- empirical support status: **not established**;
- cross-domain claim status: **unvalidated**.

## Immediate continuation sequence

1. Inspect the workflow run triggered by commit `b3ee3bd4e23f050f84562e0db76806556a0b9d15`.
2. If failed, inspect job steps and logs, patch the implementation, and rerun.
3. If successful, download the workflow artifact and record:
   - run ID;
   - commit SHA;
   - receipt contents;
   - output hashes;
   - scalar benchmark metrics;
   - constant-total-latency ablation metrics.
4. Add fitted baselines and uncertainty intervals only after the raw run is verified.
5. Do not characterize results as supporting the candidate framework until held-out comparisons exceed both total latency and `lambda * total latency` with uncertainty reported.
