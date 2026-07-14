# Recoverability Geometry Simulation Harness

## Current benchmark

`scalar_delayed_control.py` implements the first Stage 1 benchmark from the validation protocol using only the Python standard library.

The simulated plant is

\[
\dot x = \lambda x + u + w,
\]

with independently varied observation, commitment, and realization delays. A bounded proportional controller acts through three explicit delay queues.

## Independent outcome definition

The episode outcome is not defined by the Rigel equation.

An episode is labeled recovered only when:

1. the state never crosses the hard safety boundary during the run; and
2. mean absolute state during the terminal recovery window is below the target threshold.

This avoids the circular validation failure in which `Ri` predicts a boundary created by the same equation used to calculate `Ri`.

## Parameter-region holdout

Every fifth episode belongs to an out-of-distribution (`ood`) region sampled from the upper 28 percent of:

- observation delay;
- commitment delay;
- realization delay;
- plant instability-growth rate.

Training-region episodes exclude that upper region for those variables. This is a parameter-region holdout rather than a random row split.

## Candidate and comparison scores

The generated summary reports ROC AUC for:

1. total latency `alpha_total`;
2. `lambda_growth * alpha_total`;
3. candidate `rigel_number`.

These are diagnostic score comparisons, not a complete model-selection result. The next stage must add fitted decomposed-latency, domain-baseline, and flexible nonparametric models with calibration and uncertainty intervals.

## Canonical configuration

The source-controlled benchmark declaration is:

- `scalar-delayed-control.config.json`
- `scalar-delayed-control.config.schema.json`

The JSON declaration mirrors the current Python defaults and records the independent recovery label, held-out parameter region, and candidate comparison scores. The current script still constructs `Config` from its command-line arguments; config-file ingestion remains a follow-on task. Any change to Python defaults must be reflected in the canonical JSON declaration or explicitly documented as an experimental override.

## Run

From the repository root:

```bash
python papers/recoverability-geometry-rigel-number/simulations/scalar_delayed_control.py
```

For a shorter smoke run:

```bash
python papers/recoverability-geometry-rigel-number/simulations/scalar_delayed_control.py \
  --episodes 1000 \
  --seed 20260714 \
  --output-dir generated/scalar-delayed-control-smoke
```

The protocol target remains at least 10,000 episodes.

## Deterministic tests

Run:

```bash
python papers/recoverability-geometry-rigel-number/simulations/test_scalar_delayed_control.py
```

The standard-library test suite verifies:

- delay discretization and queue behavior;
- algebra and monotonic direction of the candidate score;
- deterministic split assignment;
- exact equality of total latency and phase sum;
- phase-burden calculations;
- fixed-seed replay stability;
- outcome-label implications;
- safety violations preventing recovery.

These tests verify implementation mechanics. They do not validate the candidate cross-domain theory or establish an empirical transition at `Ri = 1`.

## Generated outputs

The script writes:

- `episodes.csv` — episode-level raw and derived variables;
- `summary.json` — split-specific metrics and interpretation rule;
- `config.json` — replay configuration.

Generated data are evidence only after the run command, source commit, configuration, and output hashes are recorded together.

## Units and variable definitions

| Variable | Meaning | Units |
|---|---|---|
| `x` | scalar plant state | domain state unit |
| `lambda_growth` | open-loop exponential growth rate | `s^-1` |
| `alpha_o` | observation delay | `s` |
| `alpha_i` | commitment/computation delay | `s` |
| `alpha_r` | realization/actuation delay | `s` |
| `alpha_total` | sum of phase delays | `s` |
| `burden_o`, `burden_i`, `burden_r` | phase-normalized growth burdens | dimensionless |
| `V` | initial distance to hard state boundary | state unit |
| `delta_0` | initial state/sensor uncertainty proxy | state unit |
| `kappa` | state-to-margin conversion | dimensionless in this benchmark |
| `rigel_number` | latency divided by modeled critical latency | dimensionless |

## Interpretation constraints

This benchmark can show whether the proposed score is useful in one constructed dynamical family. It cannot establish:

- a universal transition at `Ri = 1`;
- transfer to detector, neural, biological, social, or AGI systems;
- superiority over accepted domain-specific stability models;
- that the current definitions of `V`, `delta_0`, or `lambda` are unique.

The candidate receives no support from this benchmark unless it improves over both total latency and `lambda * latency` in the held-out parameter region.

## Next benchmark work

1. Execute and verify the deterministic test suite in a repository workflow.
2. Execute the 10,000-episode canonical benchmark and commit a validation receipt with output hashes.
3. Add config-file ingestion and schema validation or a standard-library validation fallback.
4. Add fitted logistic and interaction baselines without data leakage.
5. Add bootstrap confidence intervals and calibration metrics.
6. Add constant-total-latency ablations that redistribute phase delays.
7. Add a delayed-coupled-oscillator benchmark with synchronization ground truth.
8. Add a queue/buffer benchmark with overflow and recovery labels.
