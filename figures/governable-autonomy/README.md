# Governable Autonomy Figures

This directory is the canonical source location for shared Governable Autonomy diagrams.

## Required figures

| ID | Source target | Classification | Purpose |
|---|---|---|---|
| `GA-FIG-001` | `governable-autonomy-stack.svg` | normative | Show trust, auditability, credential legitimacy, boundary enforcement, execution authority, and reality as an integrated governance stack |
| `GA-FIG-002` | `epistemic-authority-contraction.svg` | hypothesized safety behavior | Show authority contraction as epistemic support deteriorates |
| `GA-FIG-003` | `execution-gateway.svg` | conceptual | Show BCAT as the gateway between autonomous proposal generation and binding external state change |
| `GA-FIG-004` | `state-transition-boundary.svg` | related-work-aware conceptual model | Show commit-time authority validation and the practical irreversibility boundary |
| `GA-FIG-005` | `paper-contribution-map.svg` | descriptive program index | Map GA-001 through GA-006 to their contributions |

## Source requirements

Every figure must include:

- editable SVG source;
- a neighboring Markdown text alternative;
- title, figure ID, and version;
- classification as descriptive, normative, or hypothesized;
- claims and limitations;
- source citations for imported terminology;
- rendering verification on GitHub and StegVerse.org.

## Initial text models

### GA-FIG-001

```text
Trust state
    -> Auditability
    -> Credential legitimacy
    -> Boundary enforcement
    -> Execution authority at commit
    -> External or system reality
```

### GA-FIG-002

```text
Epistemic support: High -> Degraded -> Unknown
Permitted mode:     Open -> Constrained -> Revoked
```

This relationship is proposed and must not be presented as a universal empirical law.

### GA-FIG-003

```text
Complex autonomy -> Proposed action -> BCAT execution gate -> Reality
```

### GA-FIG-004

```text
Reversible preparation -> Commit-time validation -> Practical irreversibility -> Consequence
```

External notation such as `T(e)` requires primary-source verification before inclusion.

### GA-FIG-005

```text
GA-004 trust/audit primitives
    + GA-005 credential failure modes
    + GA-002 survivability objective
    + GA-003 state model
    + GA-001 safety invariant
    -> GA-006 BCAT execution architecture
```

## Status

SVG sources are not yet committed. Their implementation remains tracked by issue #6.
