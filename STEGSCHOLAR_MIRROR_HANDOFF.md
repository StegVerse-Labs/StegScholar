# StegScholar Mirror Handoff

## Active goal

- **Goal ID:** `RIGEL-VALIDATION-001`
- **Goal:** Develop, execute, and falsifiably validate *Recoverability Geometry and the Rigel Number* without presenting the candidate formalism as established universal physics.
- **Organization:** `StegVerse-Labs`
- **Repository:** `StegVerse-Labs/StegScholar`
- **Branch:** `main`
- **Canonical paper path:** `papers/recoverability-geometry-rigel-number/`
- **Machine task registry:** `coordination/rigel-validation-tasks.json`

## Scientific posture

The work is a candidate cross-domain systems formalism. Claims concerning physics, cognition, AI, detector systems, ecosystems, synchronization, cosmology, coherence determinants, particle pairing, life, or consciousness remain hypotheses until separately derived and empirically tested.

The current core definitions are:

\[
\alpha=\alpha_o+\alpha_i+\alpha_r,
\]

\[
G+C+E=1,\qquad G,C,E\ge 0,
\]

\[
\Psi=V-\kappa\delta_0e^{\lambda\alpha},
\]

and the candidate dimensionless Rigel number

\[
Ri=\frac{\lambda\alpha}{\ln\!\left(V/(\kappa\delta_0)\right)}
  =\frac{\alpha_{pipeline}}{\alpha_{critical}}.
\]

Within the provisional exponential-growth model, `Ri < 1`, `Ri = 1`, and `Ri > 1` denote modeled recoverable, critical, and nonrecoverable regimes. The threshold follows from the model definition and is not yet an independently demonstrated universal empirical constant.

## Authoritative files

- `papers/recoverability-geometry-rigel-number/manuscript.md`
- `papers/recoverability-geometry-rigel-number/validation-protocol.md`
- `papers/recoverability-geometry-rigel-number/claims-register.md`
- `papers/recoverability-geometry-rigel-number/coherence-determinant-extension.md`
- `papers/recoverability-geometry-rigel-number/validation-progress.md`
- `papers/recoverability-geometry-rigel-number/simulations/README.md`
- `coordination/rigel-validation-tasks.json`
- `.github/workflows/rigel-validation.yml`
- this handoff

## Completed and committed implementation

1. Canonical manuscript and validation protocol are committed.
2. A standard-library scalar delayed-control benchmark is installed at `papers/recoverability-geometry-rigel-number/simulations/scalar_delayed_control.py`.
3. Recovery is labeled independently from the candidate equation using a hard safety boundary and terminal target return.
4. Upper-delay and upper-instability parameter regions are held out for OOD evaluation.
5. Deterministic implementation tests are installed at `papers/recoverability-geometry-rigel-number/simulations/test_scalar_delayed_control.py`.
6. Canonical configuration and JSON Schema are installed at:
   - `papers/recoverability-geometry-rigel-number/simulations/scalar-delayed-control.config.json`
   - `papers/recoverability-geometry-rigel-number/simulations/scalar-delayed-control.config.schema.json`
7. Constant-total-latency matched ablation is installed at `papers/recoverability-geometry-rigel-number/simulations/constant_total_latency_ablation.py`.
8. Leakage-controlled fitted baseline evaluation is installed at `papers/recoverability-geometry-rigel-number/simulations/fit_baselines.py`.
9. A fail-closed validation-state evaluator is installed at `papers/recoverability-geometry-rigel-number/simulations/evaluate_validation_state.py` in commit `715fcf00e911cb3b3b87a5210e845f23a7d2be3b`.
10. A machine-owned task registry with explicit owners, locations, successors, and release conditions is installed at `coordination/rigel-validation-tasks.json` in commit `ceec6763799484d3f2782c643c35f69d7cb72159`.
11. The hosted workflow is installed at `.github/workflows/rigel-validation.yml`. Commit `9aeb9f4cb8f2cfda6827c86854e2505f2bd28e24` adds:
    - deterministic tests;
    - canonical simulation;
    - fitted OOD baselines;
    - constant-total-latency ablation;
    - fail-closed status evaluation;
    - SHA-256 receipts;
    - artifact upload;
    - compact evidence persistence to `evidence/rigel-validation/latest/`;
    - concurrency control and duplicate-change suppression.

## Automation contract

**Owner repository:** `StegVerse-Labs/StegScholar`

**Trigger:** push to `main` affecting the Rigel simulation lane, workflow, or task registry; pull request path match; or manual dispatch.

**Deterministic inputs:** seed `20260714`, declared run sizes, fixed benchmark configuration, source commit.

**Outputs:**

- generated episode datasets;
- scalar summary;
- fitted baseline evaluation;
- matched ablation summary;
- validation receipts with hashes;
- `validation-state.json` with one of `COMPLETE`, `BLOCKED`, `RETRY`, `REVIEW_REQUIRED`, or `FAILED`;
- next executable task and exact repository location.

**Persistent state:** successful non-PR runs must commit compact evidence to `evidence/rigel-validation/latest/`. Missing or malformed evidence produces `FAILED`; it is never treated as success.

**Duplicate prevention:** workflow concurrency is grouped by ref; compact evidence is committed only when the staged content changes; evidence-path commits do not retrigger the workflow.

## Current actual classification

- Manuscript and theory record: **implemented, unvalidated scientifically**.
- Scalar simulator: **implemented, repository-run evidence pending inspection**.
- Deterministic tests: **implemented, hosted result pending inspection**.
- Fitted baselines: **implemented, output pending hosted execution evidence**.
- Constant-total-latency ablation: **implemented, output pending hosted execution evidence**.
- Validation-state automation: **implemented, hosted persistence pending inspection**.
- Kuramoto benchmark: **missing; blocked until scalar interpretation is durably recorded**.
- Queue/SCW-like benchmark: **missing; successor to Kuramoto source completion**.
- Hamilton-Jacobi augmented-state derivation: **missing**.
- Detector-specific instantiation: **partial manuscript treatment only**.
- Source-controlled publication figures: **missing**.
- Primary-source related-work map: **missing**.
- Compiled publication release: **blocked by validation and publication assets**.

## Exact task sequence

The canonical task sequence and machine-observable release conditions are in `coordination/rigel-validation-tasks.json`.

Current active task:

- `RIGEL-VERIFY-WORKFLOW-003`
- location: `evidence/rigel-validation/latest/validation-state.json`
- owner: `.github/workflows/rigel-validation.yml`
- release condition: a successful hosted run persists compact summaries, receipts, and validation state.

Possible deterministic successors are selected from observed evidence:

- `RIGEL-REPAIR-VALIDATION-EVIDENCE-004` at `.github/workflows/rigel-validation.yml` if evidence is missing or malformed;
- `RIGEL-STATISTICAL-CROSSCHECK-005` at `papers/recoverability-geometry-rigel-number/simulations/crosscheck_baselines.py` if candidate improvement is observed;
- `RIGEL-REVISE-PHASE-HYPOTHESIS-006` at `papers/recoverability-geometry-rigel-number/claims-register.md` if fixed-total partitioning changes no outcomes;
- `RIGEL-REVISE-PREDICTIVE-CLAIM-007` at `papers/recoverability-geometry-rigel-number/claims-register.md` if decomposed latency does not exceed both aggregate baselines.

## Validation commands

```bash
python papers/recoverability-geometry-rigel-number/simulations/test_scalar_delayed_control.py

python papers/recoverability-geometry-rigel-number/simulations/scalar_delayed_control.py \
  --episodes 10000 \
  --seed 20260714 \
  --output-dir generated/scalar-delayed-control

python papers/recoverability-geometry-rigel-number/simulations/fit_baselines.py \
  --episodes-csv generated/scalar-delayed-control/episodes.csv \
  --output generated/scalar-delayed-control/baseline-evaluation.json \
  --bootstrap-replicates 500 \
  --seed 20260714

python papers/recoverability-geometry-rigel-number/simulations/constant_total_latency_ablation.py \
  --scenarios 2000 \
  --seed 20260714 \
  --total-latency 0.45 \
  --output-dir generated/constant-total-latency-ablation

python papers/recoverability-geometry-rigel-number/simulations/evaluate_validation_state.py \
  --baseline-metrics generated/scalar-delayed-control/baseline-evaluation.json \
  --ablation-summary generated/constant-total-latency-ablation/summary.json \
  --output generated/validation-state.json
```

## Blockers and authority boundaries

- Hosted run evidence has not yet been directly inspected and cited in this handoff.
- A trusted statistical-package cross-check and paired uncertainty are required before any support claim.
- No production or third-party system may be stressed without explicit authorization and safeguards.
- No institutional outreach may be sent in the author's name without explicit authorization.
- No empirical evidence currently establishes cross-domain clustering at `Ri ≈ 1`.
- `V`, `lambda`, `delta_0`, and `kappa` remain domain-specific operational definitions.
- Fundamental constants remain inputs or scale constraints absent an independent derivation.

## Cross-repository dependencies and propagation

No other repository currently owns the canonical Rigel research record. Site, Publisher, admissibility-wiki, stegguardian-wiki, and master-records propagation is **not activated** because publication and validation criteria are not met. Any future propagation must identify StegScholar as source, validate the consumer contract, and preserve source commit and evidence receipts.

## Completion accounting

Required deliverable inventory for the current validation goal: **20**.

- developed production/research files: **13**;
- scaffolding or stubs: **0**;
- missing required files or evidence surfaces: **7**;
- task completion: **12/20 = 60%**;
- developed-file completion: **13/20 = 65%**;
- validation completion: **4/10 = 40%** because source-level validation lanes exist but hosted evidence, statistical cross-check, and independent benchmark validation remain incomplete;
- integration completion: **2/5 = 40%** because workflow and durable task registry are installed, while persisted hosted evidence and publication consumers are inactive;
- goal activation: **52%**.

## Archive condition

A session working on this track may be archived only when its unique decisions, mutations, evidence, ownership changes, and continuation requirements are committed here or in linked durable records, and no session-owned verification remains pending. Repository incompleteness alone is not a reason to retain a session when all remaining work is machine-owned or durably assigned.
