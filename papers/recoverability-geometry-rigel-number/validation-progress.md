# Rigel Validation Progress

## Current implementation state

The first reproducible validation lane now contains:

- `scalar_delayed_control.py` — independent-outcome scalar delayed-control benchmark;
- `test_scalar_delayed_control.py` — deterministic implementation tests;
- `scalar-delayed-control.config.json` — canonical benchmark declaration;
- `scalar-delayed-control.config.schema.json` — machine-readable configuration contract;
- `constant_total_latency_ablation.py` — matched-scenario phase-redistribution benchmark;
- `fit_baselines.py` — leakage-controlled fitted baseline comparison with bootstrap intervals and calibration metrics;
- `.github/workflows/rigel-validation.yml` — automated tests, canonical simulation, ablation, fitted evaluation, receipts, hashing, and artifact upload.

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
- Fitted baseline evaluator: `a76601f3fdef5fc0452e94d9cb23f397aa1df1b1`
- Workflow integration of fitted baselines: `b6526c17c9665085adf623b3fe2294257039d48a`

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

## What the fitted baseline evaluator tests

The evaluator fits models only on the declared `train` parameter region and evaluates them only on the held-out `ood` region. All fitted models receive the same control variables so that the comparison isolates the representation of latency.

Compared models are:

1. total latency;
2. `lambda * total latency`;
3. decomposed raw phase latency;
4. decomposed phase burdens `lambda * alpha_phase`;
5. the candidate Rigel number.

For each model, the evaluator records:

- held-out ROC AUC;
- a percentile bootstrap 95% AUC interval;
- held-out Brier score;
- 10-bin expected calibration error;
- fitted standardized coefficients and training standardization parameters.

The evaluator is intentionally standard-library-only to keep repository replay simple. Its gradient-descent logistic implementation must still be checked against a trusted statistical package before publication-grade inference.

## Current evidence status

Source and workflow infrastructure are committed. No successful workflow execution, generated artifact hashes, validation receipts, or fitted metrics have yet been inspected and durably cited here.

Therefore:

- implementation status: **committed**;
- execution status: **pending verification**;
- empirical support status: **not established**;
- cross-domain claim status: **unvalidated**.

## Claim gate

No support is claimed unless a decomposed model exceeds both total-latency baselines in the held-out parameter region, with uncertainty reported, and without materially worse calibration.

Even if that gate is met, the result supports only the value of phase decomposition in this constructed scalar-control family. It does not establish a universal `Ri = 1` threshold or transfer to detector, neural, biological, social, or cosmological systems.

## Immediate continuation sequence

1. Inspect the workflow run triggered by commit `b6526c17c9665085adf623b3fe2294257039d48a`.
2. If failed, inspect job steps and logs, patch the implementation, and rerun.
3. If successful, download the workflow artifact and record:
   - run ID;
   - commit SHA;
   - receipt contents;
   - output hashes;
   - scalar benchmark metrics;
   - constant-total-latency ablation metrics;
   - fitted held-out baseline metrics and bootstrap intervals.
4. Cross-check logistic coefficients and metrics against a trusted statistics implementation.
5. Add paired bootstrap intervals for differences in AUC, Brier score, and calibration rather than relying only on separate intervals.
6. Add a delayed Kuramoto benchmark with independently defined synchronization recovery.
7. Do not characterize results as supporting the candidate framework until the claim gate is met and independently reviewed.
