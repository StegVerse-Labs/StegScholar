# Claims Register

## Purpose

This register separates established results, results derived inside the current model, conjectures, analogies, and claims that are currently prohibited because available evidence does not support them.

## Status labels

- **ESTABLISHED:** accepted result from existing physics, mathematics, engineering, or biology; requires primary-source citation in the manuscript.
- **MODEL-DERIVED:** follows algebraically from stated assumptions but is not independently validated.
- **TESTABLE HYPOTHESIS:** has an operational path to falsification.
- **ANALOGY:** structurally suggestive comparison without demonstrated equivalence.
- **SPECULATIVE EXTENSION:** potentially researchable but outside the first paper.
- **DISALLOWED OVERCLAIM:** must not appear as a conclusion without new derivation and evidence.

## Core recoverability claims

| ID | Claim | Status | Required evidence or action |
|---|---|---|---|
| RG-001 | Total interaction latency may be decomposed as observation, commitment, and realization latency. | MODEL-DERIVED accounting identity | Define domain-specific phase boundaries and model overlap/covariance. |
| RG-002 | The Rigel number equals realized pipeline latency divided by modeled critical latency under the exponential disturbance model. | MODEL-DERIVED | Algebra already shown; independent predictive value remains untested. |
| RG-003 | `Ri = 1` is a universal empirical transition. | DISALLOWED OVERCLAIM | Requires independent systems with transitions not defined by the same equation. |
| RG-004 | Decomposed latency predicts failure better than aggregate latency. | TESTABLE HYPOTHESIS | Compare out-of-sample predictive models on simulated and measured datasets. |
| RG-005 | Phase-specific latency burdens identify distinct mitigation strategies. | TESTABLE HYPOTHESIS | Intervention study varying observation, inference, and realization delays independently. |

## Coherence-envelope claims

| ID | Claim | Status | Required evidence or action |
|---|---|---|---|
| CE-001 | Bounded time-dependent systems can be represented by operational stability envelopes in parameter space. | ESTABLISHED in several domain-specific forms; proposed cross-domain abstraction | Cite viability kernels, operating envelopes, phase diagrams, stability regions, and control barrier methods. |
| CE-002 | `R_eff ~ S K_raw / (B H)` is a universal invariant. | DISALLOWED OVERCLAIM | Terms are currently undefined dimensionally and no conservation result exists. |
| CE-003 | Tail amplification, variance, and recovery time can jointly identify an approaching boundary. | TESTABLE HYPOTHESIS | Benchmark against critical-transition indicators and domain baselines. |
| CE-004 | Variance always degrades before the mean. | DISALLOWED OVERCLAIM | Must include masking by redundancy, hard gating, adaptation, and hidden states. |
| CE-005 | Boundary movement under controlled changes in coupling, entropy, and capacity transfers across domains. | TESTABLE HYPOTHESIS | Standardized cross-domain dataset and preregistered comparison. |
| CE-006 | Transform exhaustion is the point at which no admissible intervention restores minimum performance. | MODEL DEFINITION | Define intervention set, threshold, observation interval, and uncertainty. |

## Boundary-intersection claims

| ID | Claim | Status | Required evidence or action |
|---|---|---|---|
| BI-001 | Coupled systems may be analyzed through overlapping viable sets and frequency-dependent coupling. | ESTABLISHED in domain-specific dynamical systems and synchronization theory | Cite delayed coupled oscillators, master stability functions, reachability, and network control. |
| BI-002 | High spectral alignment always increases composite coherence. | DISALLOWED OVERCLAIM | Resonance can destabilize; sign and topology of coupling matter. |
| BI-003 | Boundary proximity increases sensitivity to coupling. | TESTABLE HYPOTHESIS / established in selected critical systems | State domain conditions and compare against bifurcation and susceptibility results. |
| BI-004 | A universal coherence-coupling tensor applies unchanged across physics, brains, and compute. | DISALLOWED OVERCLAIM | At most a common notation until equivalence is derived. |

## Physics and particle claims

| ID | Claim | Status | Required evidence or action |
|---|---|---|---|
| PH-001 | A wavefunction specifies a state; dynamics require an evolution law such as a Hamiltonian or action plus boundary conditions. | ESTABLISHED | Cite standard quantum mechanics and quantum field theory sources. |
| PH-002 | The Heisenberg uncertainty principle follows from noncommuting observables and `hbar`, not from selection of a fermion. | ESTABLISHED | Cite Robertson-Schrödinger uncertainty relation. |
| PH-003 | Conservation laws follow from continuous symmetries under the assumptions of Noether's theorem. | ESTABLISHED | State assumptions precisely. |
| PH-004 | Particle masses, charges, couplings, mediator ranges, lifetimes, confinement, and symmetry breaking affect accessible stable regimes. | ESTABLISHED at domain level | Cite QED, QCD, EFT, atomic, nuclear, and phase-structure literature. |
| PH-005 | The Coherence Determinant Tuple is an established physical object. | DISALLOWED OVERCLAIM | It is a proposed organizing construct only. |
| PH-006 | A charged fermion necessarily requires a complementary opposite-charge particle in every admissible universe. | DISALLOWED OVERCLAIM | Global charge, boundary conditions, gauge constraints, and background sectors require careful treatment. |
| PH-007 | Electron-proton pairing is the unique minimal life-capable pairing. | SPECULATIVE EXTENSION | Requires parameter scans, nuclear/chemical stability analysis, and astrobiology constraints. |
| PH-008 | A universal minimal triad of matter, mediator, and causal structure is proven irreducible. | SPECULATIVE EXTENSION | Compare with interacting field theories, relational formulations, and minimal quantum models. |
| PH-009 | Particle pairing defines a determinant baseline for accessible stable relational regimes. | TESTABLE RESEARCH CONSTRUCT | Formalize as dimensionless parameter vector and test on known bound-state phase diagrams. |

## Neural and biological claims

| ID | Claim | Status | Required evidence or action |
|---|---|---|---|
| NB-001 | Neurons are heterogeneous and not globally interchangeable. | ESTABLISHED | Cite neuronal taxonomy, morphology, electrophysiology, and circuit specialization. |
| NB-002 | Maximal neural coherence requires maximal firing of every necessary neuron. | DISALLOWED OVERCLAIM | High firing can degrade function; define coherence independently of activity magnitude. |
| NB-003 | Global performance may be limited by a bottleneck subsystem. | TESTABLE HYPOTHESIS / established in selected systems | Define network architecture and compare bottleneck versus distributed-failure models. |
| NB-004 | Physics sectors and neural subsystems are mathematically isomorphic. | DISALLOWED OVERCLAIM | Structural analogy only unless a mapping preserving operations and invariants is proven. |
| NB-005 | Life and consciousness are special conjunctions of complementary coherence sets. | SPECULATIVE EXTENSION | Requires explicit variables, dynamics, competing theories, and empirical discriminators. |

## Compute and AGI claims

| ID | Claim | Status | Required evidence or action |
|---|---|---|---|
| CA-001 | Tail latency and recovery behavior can expose distributed-system stability boundaries. | ESTABLISHED in broad engineering terms; specific formal mapping unvalidated | Cite queueing, tail-at-scale, overload control, and resilience literature. |
| CA-002 | SCW can serve as an engineered validation environment. | PLANNED | Use simulation first; production or external testing requires explicit authorization. |
| CA-003 | Coherence geometry is sufficient to solve human-AGI alignment. | DISALLOWED OVERCLAIM | At most it may contribute a boundary and recoverability layer. |
| CA-004 | A shared operational language of limits may improve human-AI governance. | TESTABLE HYPOTHESIS | Implement envelope/downshift policy and compare safety/reliability outcomes. |

## Publication boundary

The first paper may include:

- recoverability geometry;
- latency decomposition;
- dimensionless normalization;
- domain-specific operating envelopes;
- boundary observables;
- one or two carefully derived applications;
- explicit falsification criteria.

The first paper must exclude as conclusions:

- universal coherence conservation;
- derivation of physical constants;
- preferred fermion or unique particle pairing;
- life or consciousness theory;
- spiritual ontology;
- guaranteed AGI alignment;
- claims of prediction of unknown physical regimes without prospective evidence.

## Update rule

Every material manuscript claim must reference an ID in this register. A claim may advance in status only when the linked derivation, primary literature, dataset, simulation, or independent review is committed and cited.
