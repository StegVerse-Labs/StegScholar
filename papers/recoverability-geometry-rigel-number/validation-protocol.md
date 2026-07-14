# Validation Protocol: Recoverability Geometry and the Rigel Number

## Objective

Determine whether the latency decomposition

\[
\alpha=\alpha_o+\alpha_i+\alpha_r
\]

and candidate Rigel number

\[
Ri=\frac{\lambda\alpha}{\ln\!\left(V/(\kappa\delta_0)\right)}
\]

provide explanatory or predictive value beyond existing aggregate-latency and domain-specific stability models.

## Primary hypotheses

### H1 — Threshold separation

Episodes independently labeled recoverable or failed will show stronger separation by `Ri` than by total latency alone.

### H2 — Phase decomposition

The triplet `(alpha_o, alpha_i, alpha_r)` will improve prediction or diagnosis relative to aggregate `alpha`, after controlling for system state and load.

### H3 — Phase-specific failure modes

Different failure classes will exhibit distinguishable phase burdens:

\[
b_o=\lambda\alpha_o,\quad
b_i=\lambda\alpha_i,\quad
b_r=\lambda\alpha_r.
\]

### H4 — Cross-domain normalization

After domain-specific calibration, normalized criticality may transfer more consistently across systems than raw latency or raw disturbance rate.

This is the highest-risk hypothesis and must not be assumed from the definition.

## Null hypotheses

- Aggregate latency performs as well as or better than decomposed latency.
- `Ri` adds no predictive value beyond accepted domain-specific models.
- Estimated thresholds vary arbitrarily across systems.
- `V`, `lambda`, or `delta_0` cannot be identified reproducibly.

## Stage 1 — Synthetic delayed-control benchmark

### System families

1. Scalar unstable plant:

   \[
   \dot x=ax+bu(t-\tau).
   \]

2. Inverted pendulum or cart-pole with sensing and actuation delays.
3. Queue or buffer model with delayed service scaling.
4. Delayed consensus or coupled-oscillator model.

### Required manipulations

Vary independently:

- observation delay;
- computation/commitment delay;
- realization/actuation delay;
- disturbance growth rate;
- sensor noise or initial uncertainty;
- safety or recoverability margin;
- controller design and gain;
- queue, buffer, or network load.

### Ground truth

Define recoverability independently of the Rigel equation, using one or more of:

- return to a target set within a fixed horizon;
- violation of a control barrier condition;
- entry into an independently computed backward-reachable failure set;
- actuator saturation followed by non-recovery;
- buffer overflow or deadline miss;
- loss of synchronization below a prescribed order parameter.

### Minimum experiment

- At least 10,000 simulated episodes.
- Balanced successful and failed cases where possible.
- Held-out parameter regions, not only random held-out samples.
- Repeated runs under multiple noise levels.

## Stage 2 — Model comparison

Fit and compare:

1. latency-only baseline;
2. total latency plus instability rate;
3. decomposed latency model;
4. domain-specific accepted baseline;
5. full candidate Rigel model;
6. flexible nonparametric model using the same raw variables.

Evaluate:

- area under ROC and precision-recall curves;
- calibration error;
- Brier score;
- out-of-distribution performance;
- threshold stability;
- ablation effects;
- confidence intervals from bootstrap or repeated simulation seeds.

The full framework is supported only if it adds value beyond the strongest reasonable baseline.

## Stage 3 — Real-system traces

### Priority A: open robotics/control logs

Required timestamps:

- sensor acquisition;
- state-estimation availability;
- policy or controller completion;
- command transmission;
- actuator or plant response;
- observed recovery or failure.

### Priority B: distributed-system traces

Required timestamps and states:

- telemetry observation;
- scheduling or consensus commitment;
- rollout or write realization;
- queue or buffer growth;
- rollback margin;
- failure, saturation, or cascade onset.

### Priority C: scientific detector pipelines

Potential variables:

- readout/digitization latency;
- preprocessing or reconstruction latency;
- neural inference latency;
- trigger or storage commitment latency;
- buffer depth and occupancy;
- event loss or deadline margin.

Public calorimeter event datasets alone may not contain the required systems timing. Technical trigger documentation or collaboration-provided traces may be required.

## Stage 4 — Detector-specific pilot

### Narrow research question

Does explicit decomposition of detector-to-capture latency improve resource allocation or event-loss prediction compared with an aggregate timing budget?

### Candidate detector quantity

\[
Ri_{det}
=
\frac{\lambda_{loss}
(\alpha_{readout}+\alpha_{inference}+\alpha_{capture})}
{\ln\!\left(V_{buffer}/(\kappa\delta_{signal})\right)}.
\]

### Required cautions

- Do not interpret shower-energy reconstruction error as timing latency unless the mapping is explicitly derived.
- Separate offline reconstruction from real-time trigger or capture pipelines.
- Use collaboration-approved definitions for buffer margin and event loss.
- Treat energy optimization as an engineering hypothesis until supported by a full power, throughput, and timing model.

## Stage 5 — Kuramoto instantiation

Use a delayed Kuramoto model such as

\[
\dot\theta_i=\omega_i+
\frac{K}{N}\sum_j
\sin(\theta_j(t-\tau)-\theta_i(t)).
\]

Define recoverability independently using the order parameter

\[
r(t)=\left|\frac1N\sum_j e^{i\theta_j(t)}\right|.
\]

Possible ground truth:

- recoverable if `r(t)` returns above a prescribed threshold within horizon `H`;
- failed if synchronization remains below threshold.

Then test whether a Rigel-style normalized delay measure improves prediction of synchronization loss beyond `K`, frequency dispersion, and total delay alone.

## Stage 6 — Hamilton-Jacobi grounding

Derive `V` from a reachability value function for an augmented state containing:

- physical state;
- estimator state;
- queue or pending-decision state;
- committed-but-not-realized action state.

The latency decomposition is rigorous only if each phase corresponds to explicit state evolution or delayed dynamics. Compare the approximate scalar `Ri` with the computed viability kernel.

## Acceptance criteria

The candidate framework advances from conceptual to supported when all are met:

1. `V`, `lambda`, `delta_0`, and latency phases are operationally reproducible.
2. Independent failure labels are used.
3. Decomposed latency improves at least one meaningful metric beyond aggregate latency and accepted baselines.
4. Results replicate across parameter regions or datasets.
5. Failure cases and limits of applicability are documented.
6. Cross-domain claims are limited to domains with successful derivations.

## Rejection or revision criteria

Revise or reject the current form if:

- the logarithmic margin is unstable or non-identifiable;
- the exponential growth approximation fails across the relevant window;
- `Ri` merely restates the definition of failure;
- threshold values are not stable after independent measurement;
- phase decomposition offers no predictive or diagnostic gain;
- accepted domain-specific theories explain the data more parsimoniously.

## Required outputs

- simulation source code;
- machine-readable run configuration;
- raw and derived episode data;
- model-comparison report;
- figures with confidence intervals;
- failure-analysis appendix;
- update to `STEGSCHOLAR_MIRROR_HANDOFF.md` with commit and validation status.
