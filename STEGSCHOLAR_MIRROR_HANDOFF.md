# StegScholar Mirror Handoff

## Canonical track

- **Goal ID:** `RIGEL-VALIDATION-001`
- **Originating session goal:** create, visualize, install, validate, and prepare for publication the research track *Recoverability Geometry and the Rigel Number*.
- **Organization:** `StegVerse-Labs`
- **Repository:** `StegScholar`
- **Default branch:** `main`
- **Canonical research path:** `papers/recoverability-geometry-rigel-number/`
- **Canonical task registry:** `coordination/rigel-validation-tasks.json`
- **Latest verified evidence pointer:** `evidence/rigel-validation/latest.json`
- **Publication affiliation:** `StegVerse Research` unless changed by the author.

This is the canonical continuation record for the Rigel/recoverability research track. It does not supersede unrelated StegScholar handoffs for other research programs.

## Scientific posture

The work is a candidate systems formalism, not an established physical law.

The current model defines:

\[
\alpha=\alpha_o+\alpha_i+\alpha_r,
\]

\[
\Psi=V-\kappa\delta_0e^{\lambda\alpha},
\]

and

\[
Ri=\frac{\lambda\alpha}{\ln\!\left(V/(\kappa\delta_0)\right)}.
\]

Under the stated exponential disturbance model, `Ri=1` is the modeled algebraic boundary. It is not established as a universal empirical transition.

The G-C-E simplex remains a normalized interaction representation:

\[
G+C+E=1,\qquad G,C,E\ge 0.
\]

The proposed mappings to reachability, resilience, synchronization, detector systems, cognition, ecology, AI, or other domains remain domain-specific hypotheses until separately derived and tested.

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

## Canonical owner and claims

- **Implementation owner:** `StegVerse-Labs/StegScholar`.
- **Validation owner:** `.github/workflows/rigel-validation.yml`.
- **Current validation PR:** `#33`, branch `formal/rigel-validation-verification-v1`.
- **Implementation claim:** released after the benchmark/test fixes were committed.
- **Validation claim:** released after workflow run `30739542167`, job `91474345057`, artifact `8830800522`, and receipts were inspected.
- **Collision boundary:** no duplicate scalar benchmark, no duplicate validation handoff, and no publication propagation before publication readiness.

## Verified hosted execution

The first PR-hosted validation run completed successfully after fixing Python 3.12 dynamic-module registration in:

- `simulations/test_scalar_delayed_control.py`;
- `simulations/constant_total_latency_ablation.py`.

Verified evidence:

- workflow run: `30739542167`;
- workflow job: `91474345057`;
- workflow conclusion: `success`;
- repository readiness run: `30739542168`, conclusion `success`;
- artifact: `8830800522`;
- artifact digest: `sha256:24c628a4603ec08e33806f91003145e8743e6972e977da04696278710fb653a9`;
- run receipt: `evidence/rigel-validation/runs/30739542167/run-receipt.json`;
- validation state: `evidence/rigel-validation/runs/30739542167/validation-state.json`.

The pull-request run used 1,000 scalar episodes, 200 OOD episodes, 200 bootstrap replicates, and 250 matched ablation scenarios.

## Verified result and claim revision

The hosted run produced:

- total-latency OOD AUC: `0.9540430483`;
- `lambda * total latency` OOD AUC: `0.9645142525`;
- decomposed-latency OOD AUC: `0.9546247818`;
- decomposed-burdens OOD AUC: `0.9621873182`;
- candidate Rigel-number OOD AUC: `0.8411867365`;
- best decomposed minus strongest aggregate AUC: `-0.0023269343`;
- OOD failure rate: `0.955`;
- partition-dependent matched scenarios: `8/250`, fraction `0.032`.

Therefore:

- the workflow and evidence lane are operational;
- phase allocation affected a small subset of matched outcomes in this constructed model;
- decomposed latency did not outperform the strongest aggregate baseline;
- the current benchmark does not support predictive superiority of decomposed latency;
- the candidate Rigel-number score did not outperform aggregate baselines in this run;
- no universal or cross-domain claim is activated.

The claims register records this as `NOT SUPPORTED IN CURRENT BENCHMARK` for `RG-004` and narrows `RG-005` to a bounded diagnostic hypothesis.

## Component classification

### Complete and validated

- canonical Markdown research installation;
- validation protocol;
- claims register;
- scalar simulator;
- deterministic test suite;
- constant-total-latency ablation;
- fitted OOD baselines;
- fail-closed state evaluator;
- hosted PR execution;
- workflow/job/log inspection;
- artifact and output-hash inspection;
- durable run receipt and validation state;
- task and claim registry.

### Implemented but not publication-ready

- manuscript narrative;
- detector case-study framing;
- cross-domain comparisons;
- interactive/runtime figure prototypes.

### Missing or blocked

- balanced scalar benchmark with nondegenerate held-out class balance;
- paired statistical cross-check using a trusted package;
- delayed Kuramoto benchmark;
- queue/buffer or SCW-like benchmark;
- Hamilton-Jacobi augmented-state derivation;
- source-controlled figure generator and SVG assets;
- primary-source bibliography and gap map;
- compiled publication PDF;
- publication outbound manifest and downstream propagation.

## Machine-owned continuation

The task registry assigns every remaining item to a repository location and release condition.

The immediate successor is:

- **Task:** `RIGEL-BALANCED-BENCHMARK-008`
- **Owner:** StegScholar validation workflow
- **Required location:** `papers/recoverability-geometry-rigel-number/simulations/balanced_scalar_benchmark.py`
- **Release condition:** redesigned benchmark removes the 95.5% OOD failure imbalance, preregisters paired comparisons, and emits a new receipt.

The source-controlled figure task remains:

- **Task:** `RIGEL-INTERACTIVE-FIGURE-002`
- **Required location:** `papers/recoverability-geometry-rigel-number/figures/`
- **Release condition:** committed generator and SVG agree with the revised claims and caption.

Publication and propagation remain blocked until their release conditions in `coordination/rigel-validation-tasks.json` are satisfied.

## Cross-repository dependencies and propagation

No downstream repository currently owns canonical scientific authority for this paper.

Potential consumers are:

- `StegVerse-Labs/Site`;
- `GCAT-BCAT-Engine/Publisher`;
- `admissibility-wiki`;
- `stegguardian-wiki`;
- `master-records`.

No propagation is claimed. An outbound manifest must be created at `coordination/rigel-publication-outbound.json` only after publication readiness becomes true.

## Validation commands

```bash
python papers/recoverability-geometry-rigel-number/simulations/test_scalar_delayed_control.py
python papers/recoverability-geometry-rigel-number/simulations/scalar_delayed_control.py --episodes 10000 --seed 20260714 --output-dir generated/scalar-delayed-control
python papers/recoverability-geometry-rigel-number/simulations/fit_baselines.py --episodes-csv generated/scalar-delayed-control/episodes.csv --output generated/scalar-delayed-control/baseline-evaluation.json --bootstrap-replicates 500 --seed 20260714
python papers/recoverability-geometry-rigel-number/simulations/constant_total_latency_ablation.py --scenarios 2000 --seed 20260714 --total-latency 0.45 --output-dir generated/constant-total-latency-ablation
python papers/recoverability-geometry-rigel-number/simulations/evaluate_validation_state.py --baseline-evaluation generated/scalar-delayed-control/baseline-evaluation.json --ablation-summary generated/constant-total-latency-ablation/summary.json --output generated/validation-state.json
```

Hosted validation remains `.github/workflows/rigel-validation.yml`.

## Session consolidation

The originating conversation introduced four durable goal groups:

1. formalize the Rigel/recoverability research framework;
2. create rotatable and publication-quality G-C-E visualizations;
3. install the paper in StegScholar;
4. validate, automate, and constrain publication claims.

All four are now transferred to this handoff and `coordination/rigel-validation-tasks.json`.

**MERGED INTO:** `StegVerse-Labs/StegScholar/STEGSCHOLAR_MIRROR_HANDOFF.md` and `StegVerse-Labs/StegScholar/coordination/rigel-validation-tasks.json`.

The session itself owns no unique implementation role after PR `#33` is merged and the branch evidence becomes part of `main`.

## Completion denominators

For goal `RIGEL-VALIDATION-001`:

- required canonical deliverables: `20`;
- developed canonical deliverables: `16`;
- validated required deliverables: `13/16`;
- integration obligations completed: `1/4`;
- propagation obligations completed: `0/1`;
- session goal groups transferred or complete: `4/4`.

These percentages do not imply publication readiness or cross-domain validity.

## Archive conditions

A session may be archived when:

1. its unique requirements are represented in this handoff or the task registry;
2. any session-owned branch or PR mutation is merged, closed, or superseded with evidence;
3. no session-specific claim remains active;
4. continuation can proceed from repository state without reopening the conversation.

For the originating session, archival becomes valid after PR `#33` is merged or explicitly superseded and the canonical continuation pointers remain accessible on `main`.
