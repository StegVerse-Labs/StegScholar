# StegScholar Mirror Handoff

## Active goal

- **Goal ID:** `RIGEL-VALIDATION-001`
- **Goal:** Develop, execute, and falsifiably validate *Recoverability Geometry and the Rigel Number* without presenting the candidate formalism as established universal physics.
- **Originating session goals:** formalize the framework; create rotatable/publication figures; install the paper in StegScholar; validate and automate continuation.
- **Organization:** `StegVerse-Labs`
- **Repository:** `StegVerse-Labs/StegScholar`
- **Branch:** `main`
- **Canonical paper path:** `papers/recoverability-geometry-rigel-number/`
- **Machine task registry:** `coordination/rigel-validation-tasks.json`
- **Latest verified evidence:** `evidence/rigel-validation/latest.json`

## Scientific posture

The work is a candidate systems formalism, not an established physical law.

\[
\alpha=\alpha_o+\alpha_i+\alpha_r,
\]

\[
G+C+E=1,\qquad G,C,E\ge 0,
\]

\[
\Psi=V-\kappa\delta_0e^{\lambda\alpha},
\]

\[
Ri=\frac{\lambda\alpha}{\ln\!\left(V/(\kappa\delta_0)\right)}.
\]

`Ri=1` is the modeled algebraic boundary under the stated exponential-growth assumptions. It is not established as a universal empirical transition.

## Authoritative files

- `papers/recoverability-geometry-rigel-number/manuscript.md`
- `papers/recoverability-geometry-rigel-number/validation-protocol.md`
- `papers/recoverability-geometry-rigel-number/claims-register.md`
- `papers/recoverability-geometry-rigel-number/coherence-determinant-extension.md`
- `papers/recoverability-geometry-rigel-number/simulations/scalar_delayed_control.py`
- `papers/recoverability-geometry-rigel-number/simulations/test_scalar_delayed_control.py`
- `papers/recoverability-geometry-rigel-number/simulations/constant_total_latency_ablation.py`
- `papers/recoverability-geometry-rigel-number/simulations/fit_baselines.py`
- `papers/recoverability-geometry-rigel-number/simulations/evaluate_validation_state.py`
- `.github/workflows/rigel-validation.yml`
- `coordination/rigel-validation-tasks.json`
- `evidence/rigel-validation/latest.json`
- this handoff

## Canonical ownership and convergence

- **Implementation owner:** `StegVerse-Labs/StegScholar`.
- **Validation owner:** `.github/workflows/rigel-validation.yml`.
- **Canonical continuation:** this handoff plus `coordination/rigel-validation-tasks.json`.
- **Merged session work:** all four originating session goal groups are durably transferred here.
- **Duplicate execution rule:** no second scalar benchmark, no competing handoff, and no publication propagation before publication readiness.

## Verified hosted execution

PR-hosted validation completed after correcting Python 3.12 dynamic module registration in:

- `simulations/test_scalar_delayed_control.py`;
- `simulations/constant_total_latency_ablation.py`.

Directly inspected evidence:

- workflow run: `30739542167`;
- workflow job: `91474345057`;
- workflow conclusion: `success`;
- repository readiness run: `30739542168`, conclusion `success`;
- artifact ID: `8830800522`;
- artifact digest: `sha256:24c628a4603ec08e33806f91003145e8743e6972e977da04696278710fb653a9`;
- run receipt: `evidence/rigel-validation/runs/30739542167/run-receipt.json`;
- validation state: `evidence/rigel-validation/runs/30739542167/validation-state.json`.

## Verified bounded result

The hosted PR run used 1,000 scalar episodes, 200 OOD episodes, 200 bootstrap replicates, and 250 matched ablation scenarios.

Observed OOD AUC:

- total latency: `0.9540430483`;
- `lambda * total latency`: `0.9645142525`;
- decomposed latency: `0.9546247818`;
- decomposed burdens: `0.9621873182`;
- candidate Rigel number: `0.8411867365`.

Additional observations:

- best decomposed minus strongest aggregate AUC: `-0.0023269343`;
- OOD failure rate: `0.955`;
- partition-dependent matched scenarios: `8/250`, fraction `0.032`.

Result:

- execution lane: **validated**;
- phase-allocation effect in this constructed benchmark: **observed but small**;
- predictive superiority of decomposed latency: **not supported in current benchmark**;
- candidate Rigel score superiority: **not supported in current benchmark**;
- universal `Ri=1` or cross-domain validity: **not established**;
- publication readiness: **false**.

The claims register records `RG-004` as `NOT SUPPORTED IN CURRENT BENCHMARK` and narrows `RG-005` to a bounded diagnostic hypothesis.

## Current component classification

### Complete and validated

- canonical manuscript installation;
- validation protocol;
- claims register;
- scalar simulator;
- deterministic tests;
- constant-total-latency ablation;
- fitted OOD baselines;
- fail-closed validation-state evaluator;
- hosted workflow execution;
- job/log/artifact inspection;
- durable output hashes and run receipt;
- task/claim registry.

### Implemented but not publication-ready

- detector case-study framing;
- cross-domain theory mappings;
- runtime/interactive figure prototypes.

### Missing or blocked

- balanced scalar benchmark with nondegenerate OOD class balance;
- paired trusted-package statistical cross-check;
- delayed Kuramoto benchmark;
- queue/SCW-like benchmark;
- Hamilton-Jacobi augmented-state derivation;
- source-controlled figure generator and SVG;
- primary-source bibliography and gap map;
- compiled publication PDF;
- outbound publication manifest and downstream propagation.

## Machine-owned continuation

Active task:

- **Task ID:** `RIGEL-BALANCED-BENCHMARK-008`
- **Owner:** `StegVerse-Labs/StegScholar`
- **Location:** `papers/recoverability-geometry-rigel-number/simulations/balanced_scalar_benchmark.py`
- **Release condition:** remove the 95.5% OOD failure imbalance, preregister paired comparisons, and emit a new validation receipt.

All successor tasks, owners, locations, states, and release conditions are in `coordination/rigel-validation-tasks.json`.

## Cross-repository propagation

Potential consumers:

- `StegVerse-Labs/Site`;
- `GCAT-BCAT-Engine/Publisher`;
- `admissibility-wiki`;
- `stegguardian-wiki`;
- `master-records`.

No propagation is claimed. `coordination/rigel-publication-outbound.json` must not be created until publication readiness is true.

## Validation commands

```bash
python papers/recoverability-geometry-rigel-number/simulations/test_scalar_delayed_control.py
python papers/recoverability-geometry-rigel-number/simulations/scalar_delayed_control.py --episodes 10000 --seed 20260714 --output-dir generated/scalar-delayed-control
python papers/recoverability-geometry-rigel-number/simulations/fit_baselines.py --episodes-csv generated/scalar-delayed-control/episodes.csv --output generated/scalar-delayed-control/baseline-evaluation.json --bootstrap-replicates 500 --seed 20260714
python papers/recoverability-geometry-rigel-number/simulations/constant_total_latency_ablation.py --scenarios 2000 --seed 20260714 --total-latency 0.45 --output-dir generated/constant-total-latency-ablation
python papers/recoverability-geometry-rigel-number/simulations/evaluate_validation_state.py --baseline-metrics generated/scalar-delayed-control/baseline-evaluation.json --ablation-summary generated/constant-total-latency-ablation/summary.json --output generated/validation-state.json
```

## Session consolidation

**MERGED INTO:** `StegVerse-Labs/StegScholar/STEGSCHOLAR_MIRROR_HANDOFF.md` and `StegVerse-Labs/StegScholar/coordination/rigel-validation-tasks.json`.

Transferred session goal groups:

1. formalism and manuscript;
2. rotatable/publication visualization requirement;
3. StegScholar installation;
4. validation, automation, claims discipline, publication, and propagation requirements.

After the verification PR is merged, the originating conversation owns no unique implementation, validation, integration, or observation role.

## Completion accounting

Current goal denominator: `20` canonical deliverables.

- task completion: `16/20 = 80%`;
- developed-file completion: `16/20 = 80%`;
- validation completion: `13/16 = 81%`;
- integration completion: `1/4 = 25%`;
- propagation completion: `0/1 = 0%`;
- goal activation: `68%`;
- session goal transfer: `4/4 = 100%`.

## Archive condition

A session may be archived when its unique requirements are in this handoff or the task registry, any session-owned PR is merged/closed/superseded, no session claim remains active, and continuation can proceed from repository state alone.
