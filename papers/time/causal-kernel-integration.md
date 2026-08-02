# Causal Kernel Integration for StegVerse Time

Status: bounded research formalism

## Purpose

This document installs a temporal substrate compatible with *Time After Causality v0.3.1* while preserving StegVerse distinctions among continuity, identity, causal compatibility, governance admissibility, execution authority, and transition receipts.

## Layering

```text
continuity observation
  -> identity and relatedness evidence
  -> declared event/state ontology
  -> invariant precedence kernel K
  -> causally compatible completion support Omega
  -> operational quotient Q
  -> resolution maps R
  -> RTG geometry
  -> GTG decision
  -> TT receipt
```

## Definitions

### Continuity evidence

Evidence by which observations are classified as states or events of one continuing subject or process. The formal declaration does not create continuity; it records a bounded reconstruction of it.

### Temporal declaration

```text
Lambda = (events, identity_rules, resolution, patches, branch_orders, evidence_refs)
```

A declaration MUST NOT silently change event identity, subject identity, scale, or resolving power.

### Invariant precedence kernel

For nonempty supported branch orders `P_gamma` over one declared event set:

```text
K = intersection(P_gamma)
```

`K` contains only precedence relations present in every supported branch. It is not a complete branch order.

### Causally compatible completion

A branch order extending `K` and satisfying the declaration's causal and resolution constraints. This term replaces `admissible completion` at the temporal layer to avoid collision with GTG governance admissibility.

### Operational quotient

An equivalence relation identifying serializations whose reordering is operationally invisible under the declared algebra. Quotienting MUST NOT erase evidence required for independent reconstruction.

### Resolution map

A declared refinement or coarse-graining map. A coarse chronology is accepted only when a fine-resolution witness supports that order. Otherwise the translation is blocked.

## Non-equivalences

```text
causally compatible != governance admissible
structurally valid != substantively correct
observable order != arbitrary serialization
identity assertion != identity reconstruction
ALLOW != execution
recorded state change != legitimate transition
```

## Integration contracts

### Temporal substrate to RTG

RTG receives:

- kernel relations;
- supported branch identifiers;
- declared scale;
- operational equivalence classes;
- resolution maps;
- evidence references.

RTG MUST NOT reinterpret gauge-equivalent serializations as distinct physical or governed transitions without additional evidence.

### RTG to GTG

GTG receives candidate relational transitions from RTG. It evaluates standing, authority, policy, evidence, constraints, and commit-time validity. Causal compatibility alone MUST NOT produce `ALLOW`.

### GTG to TT

TT records the evaluated candidate, result, realized or withheld action, post-state if any, receipt references, and predecessor/supersession links. `DENY`, `FAIL_CLOSED`, `DEFER`, `TRANSFORM`, and `ERROR` remain first-class history.

## Validation invariants

1. Kernel relations are acyclic and appear in every branch order.
2. Every branch uses the declared event set.
3. Every branch extends the kernel.
4. A declared coarse chronology has a fine witness.
5. Operationally equivalent fine representatives induce equivalent coarse classes where lumpability is claimed.
6. Evidence references are present for event identity and kernel declaration.
7. No field labels causal compatibility as GTG admissibility.
8. No transition is represented as executed solely because it is causally compatible.

## Scientific boundaries

This integration does not claim:

- unique temporal dynamics;
- metric duration or clock emergence;
- a thermodynamic arrow;
- Lorentzian continuum recovery;
- Einstein dynamics;
- a new empirical prediction beyond established higher-order process physics.

Those remain open research questions.
