# Recoverability Geometry and the Rigel Number

## A framework for bounded interaction with dynamical reality

**Rigel Randolph**

## Abstract

Systems that observe, interpret, commit, and act upon changing environments operate under finite sensing, inference, coordination, propagation, and actuation delays. This paper introduces a candidate interaction formalism that separates total latency into observation, commitment, and realization components; represents governance, constraints, and execution on a simplex; and compares lag-amplified uncertainty with an available recoverability margin. Under a provisional exponential-growth model, the resulting dimensionless Rigel number is the ratio of realized interaction latency to a modeled critical recoverable latency. The framework is positioned as an overlay for bounded interaction rather than a replacement for domain-specific physics. It yields falsifiable predictions for delayed control, AI-in-the-loop instrumentation, distributed systems, ecological resilience, and synchronization models. The proposed threshold and cross-domain generality remain unvalidated.

## 1. Problem statement

A system interacting with reality does not observe and act instantaneously. Its interaction loop includes at least:

1. acquisition or reconstruction of state;
2. inference, decision, coordination, or commitment;
3. realization through propagation, storage, or actuation.

Many models use an aggregate delay. The present framework asks whether the internal partition of delay carries additional predictive information, especially when different phases have different failure mechanisms and mitigation strategies.

## 2. Interaction latency decomposition

Define total interaction latency as

\[
\alpha = \alpha_o + \alpha_i + \alpha_r,
\]

where:

- \(\alpha_o\) is observation or reconstruction latency;
- \(\alpha_i\) is inference, commitment, consensus, or transition-to-irreversibility latency;
- \(\alpha_r\) is realization, write, propagation, or actuation latency.

The additive expression is a first-order accounting identity. It does not imply that the phases are independent. A more complete model may include cross-couplings, overlap, queues, feedback, and conditional branching.

## 3. G-C-E interaction simplex

Let

\[
x=(G,C,E)\in\Delta^2,
\]

with

\[
G+C+E=1,\qquad G,C,E\ge 0.
\]

The coordinates represent normalized contributions of:

- governance: authority, policy, review, and decision structure;
- constraints: physical, informational, safety, resource, and admissibility limits;
- execution: capacity and realized action.

Given nonnegative raw intensities \((\rho_G,\rho_C,\rho_E)\), the barycentric transform is

\[
G=\frac{\rho_G}{\Sigma_\rho},\quad
C=\frac{\rho_C}{\Sigma_\rho},\quad
E=\frac{\rho_E}{\Sigma_\rho},
\]

where \(\Sigma_\rho=\rho_G+\rho_C+\rho_E\).

## 4. Recoverability and disturbance growth

Let \(V(x)>0\) denote a domain-specific recoverability margin. Let initial state uncertainty or disturbance magnitude be \(\delta_0>0\), and suppose local disturbance growth is approximately exponential over the interaction interval:

\[
\delta(t)=\delta_0 e^{\lambda t},
\]

where \(\lambda\) is a local instability-growth rate.

With a conversion factor \(\kappa>0\), define the provisional viability margin

\[
\Psi(x)=V(x)-\kappa\delta_0e^{\lambda\alpha}.
\]

Under these assumptions, recoverability requires

\[
\Psi(x)>0.
\]

The modeled critical latency is therefore

\[
\alpha_{critical}
=
\frac{1}{\lambda}
\ln\!\left(\frac{V}{\kappa\delta_0}\right),
\]

provided \(V>\kappa\delta_0\) and \(\lambda>0\).

## 5. The candidate Rigel number

Define

\[
Ri
=
\frac{\alpha}{\alpha_{critical}}
=
\frac{\lambda(\alpha_o+\alpha_i+\alpha_r)}
{\ln\!\left(V/(\kappa\delta_0)\right)}.
\]

Within the provisional model:

\[
Ri<1\Rightarrow\Psi>0,
\]

\[
Ri=1\Rightarrow\Psi=0,
\]

\[
Ri>1\Rightarrow\Psi<0.
\]

The threshold at unity follows algebraically from the definition; it is not yet evidence that independently measured systems share a universal empirical transition at the same value.

## 6. Interaction transform

Let a raw system description be

\[
X=(\rho_G,\rho_C,\rho_E,\tau_o,\tau_i,\tau_r,
\lambda,V,\delta_0,\kappa,\mathcal R).
\]

The first-order interaction transform is

\[
T(X)=
(G,C,E,\alpha_o,\alpha_i,\alpha_r,\Psi,Ri),
\]

with

\[
(\alpha_o,\alpha_i,\alpha_r)=(\tau_o,\tau_i,\tau_r).
\]

For physically separated components, propagation delay may be included in the relevant phase, for example

\[
\alpha_r=\tau_{actuation}+\frac{L}{v_{signal}},
\]

with \(v_{signal}\le c\).

## 7. Simplex and replicator interpretation

A candidate dynamical model on the simplex is

\[
\dot G=G(\Phi_G-\bar\Phi),
\]

\[
\dot C=C(\Phi_C-\bar\Phi),
\]

\[
\dot E=E(\Phi_E-\bar\Phi),
\]

where

\[
\bar\Phi=G\Phi_G+C\Phi_C+E\Phi_E.
\]

The effective payoffs \(\Phi_G,\Phi_C,\Phi_E\) may represent contributions to viability, policy fitness, constraint effectiveness, or execution utility. This preserves the simplex normalization and permits attractors, saddles, and bifurcations.

The Rigel number adds a temporal viability restriction to this flow: the configuration may evolve toward a favorable state, yet fail to remain recoverable if its observation-commitment-realization cycle is too slow relative to disturbance growth and margin.

## 8. Relationship to established theories

### 8.1 Hamilton-Jacobi reachability

Hamilton-Jacobi reachability uses a value function to characterize backward-reachable or viable sets. The recoverability margin may be grounded as a reachability value rather than chosen heuristically. Delayed or partially observed dynamics may require state augmentation by estimator and queue states.

### 8.2 Ecological resilience

The recoverability margin resembles distance or energy required to leave a basin of attraction, while \(\lambda\) resembles local disturbance amplification. The latency partition may model observation, institutional response, and ecosystem realization separately.

### 8.3 Kuramoto synchronization

For coupled oscillators, frequency dispersion and delayed coupling oppose synchronization. A Rigel-style quantity may compare phase-divergence growth over sensing, coordination, and coupling delays with a synchronization or basin margin. This mapping must be derived from a delayed Kuramoto model rather than asserted by analogy.

### 8.4 Control and barrier functions

The sign of \(\Psi\) resembles a safety or barrier condition. A rigorous version should identify conditions under which a controller keeps the augmented delayed state inside the viability kernel.

## 9. Applications and instantiations

The following values are illustrative rather than empirical.

### 9.1 Human reaction loop

Let

\[
(\alpha_o,\alpha_i,\alpha_r)=(0.12,0.18,0.10)\ \mathrm{s},
\]

\[
\lambda=2.5\ \mathrm{s}^{-1},\quad
V=0.20,\quad\delta_0=0.01,\quad\kappa=1.
\]

Then

\[
Ri\approx0.334,
\]

and

\[
\Psi\approx0.1728.
\]

### 9.2 Autonomous control loop

Let

\[
(\alpha_o,\alpha_i,\alpha_r)=(0.015,0.020,0.030)\ \mathrm{s},
\]

\[
\lambda=10\ \mathrm{s}^{-1},\quad
V=0.10,\quad\delta_0=0.01.
\]

Then

\[
Ri\approx0.282,
\]

and

\[
\Psi\approx0.0808.
\]

### 9.3 Distributed coordination

Let

\[
(\alpha_o,\alpha_i,\alpha_r)=(0.20,0.50,0.30)\ \mathrm{s},
\]

\[
\lambda_R=1.8\ \mathrm{s}^{-1},\quad
V_R=0.25,\quad\delta_R=0.02.
\]

Then

\[
Ri_R\approx0.713,
\]

and

\[
\Psi_R\approx0.129.
\]

## 10. AI-mediated detector and scientific-instrument pipelines

An AI-in-the-loop detector pipeline may be partitioned as:

- \(\alpha_o\): sensing, detector response, digitization, readout, or event reconstruction input preparation;
- \(\alpha_i\): feature extraction, neural inference, trigger decision, or commitment;
- \(\alpha_r\): buffer write, event acceptance, storage, control propagation, or experiment adjustment.

A detector-specific candidate measure is

\[
Ri_{det}
=
\frac{\lambda_{loss}
(\alpha_{readout}+\alpha_{inference}+\alpha_{capture})}
{\ln\!\left(V_{buffer}/(\kappa\delta_{signal})\right)}.
\]

This formulation should not be applied to the Akchurin et al. calorimeter-energy-reconstruction paper without verifying whether its reconstruction is offline, real-time, or trigger-bound and without obtaining defensible timing and margin variables.

The practical hypothesis is narrower: decomposing AI-mediated scientific latency may improve diagnosis and resource allocation compared with an aggregate-latency model.

## 11. Numerical delayed-control example

Consider uncertainty with

\[
\lambda=4\ \mathrm{s}^{-1},\quad
V=0.20,\quad
\delta_0=0.01,\quad\kappa=1.
\]

The predicted critical latency is

\[
\alpha_{critical}
=
\frac{1}{4}\ln(20)
\approx0.7489\ \mathrm{s}.
\]

For \(\alpha=0.25\ \mathrm{s}\),

\[
Ri\approx0.334,
\quad
\Psi\approx0.1728.
\]

For \(\alpha=0.75\ \mathrm{s}\),

\[
Ri\approx1.001,
\quad
\Psi\approx-0.0009.
\]

For \(\alpha=1.00\ \mathrm{s}\),

\[
Ri\approx1.335,
\quad
\Psi\approx-0.346.
\]

This example verifies the algebra of the definition, not an independent prediction, because the failure condition and the Rigel number are constructed from the same exponential model. Independent validation requires a system whose observed transition is not defined by the same equation.

## 12. Falsifiable predictions

The research program tests whether:

1. decomposed latency predicts observed failures better than aggregate latency;
2. phase-specific burdens identify distinct failure mechanisms;
3. independently defined recoverability transitions concentrate near a stable normalized boundary;
4. predictive control shifts effective observation burden without merely relabeling delay;
5. distributed coordination exhibits stronger commitment-phase sensitivity than local loops;
6. mappings to reachability, resilience, and synchronization remain valid under domain-specific derivation.

## 13. Dimensional and identification requirements

The following must be resolved before strong claims are made:

- \(V\) and \(\kappa\delta_0\) must have compatible units;
- the logarithm requires a positive dimensionless ratio;
- \(\lambda\alpha\) must be dimensionless;
- \(V\) must be independently measurable or derived from an accepted value function;
- \(\lambda\) must describe the relevant local error or disturbance mode;
- latency phases must have reproducible operational definitions;
- phase overlap and covariance must be modeled when material.

## 14. Physical scales and constants

The general geometry does not presently derive \(\hbar\), \(G\), \(c\), or the cosmological constant. Known constants may enter scale-specific dimensionless groups, for example:

\[
\Xi_c=\frac{\lambda L}{c},
\qquad
\Xi_G=\frac{2GM}{c^2L},
\qquad
\Xi_\Lambda=\Lambda L^2.
\]

At quantum scales, a recoverability model may include a state-resolution floor involving \(\hbar\), but the exact dimensionless construction must be derived from the chosen observable and dynamics.

## 15. Conclusion

The proposed framework treats bounded interaction as a competition among structured latency, disturbance growth, and recoverability margin. Its main candidate contribution is not the existence of delay or viability individually, but their organization into observation, commitment, and realization phases within a simplex-based interaction geometry. The Rigel number provides a compact hypothesis for normalized criticality. Its scientific value depends on rigorous domain mappings, independent validation, and demonstration that the decomposed model improves explanation or prediction beyond established methods.
