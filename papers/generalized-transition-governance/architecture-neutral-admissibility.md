# Architecture-Neutral Admissibility

Status: Draft formalism under `ARCHITECTURE-NEUTRAL-ADMISSIBILITY-001`

## Abstract

A governance system should evaluate whether a candidate satisfies the governing requirement, not whether the candidate resembles an incumbent implementation. Architectural difference may matter when it changes evidence quality, safety, authority, standing, policy compliance, constraints, or commit-time validity. It is not, by itself, a substantive denial basis.

This formalism therefore distinguishes **architecture difference** from **substantive insufficiency**. It does not issue a GTG disposition and it does not create a right to `ALLOW`.

## Core invariant

```text
ArchitectureDifferent(c) != SubstantivelyInadmissible(c)
ConformityOnlyDenial(c) = INVALID_DENIAL_BASIS
ArchitectureNeutrality(c) != ALLOW(c)
```

The governing question is whether the same declared requirement is satisfied through admissible evidence and valid standing, authority, safety/constraints, policy, and commit-time state.

## Substantive dimensions

The minimum deterministic dimensions are:

- evidence sufficiency;
- authority validity;
- standing validity;
- safety/constraint satisfaction;
- policy compliance;
- commit-time validity.

A candidate with a different architecture may still fail any of these dimensions. Such failure remains a valid substantive governance basis. Conversely, when every required dimension is satisfied, `uses_non_incumbent_architecture=true` cannot itself justify denial.

## Evidence-path neutrality

Two candidates need not produce identical evidence artifacts. They must satisfy the same governing requirement under the same declared evidence standard.

```text
same_requirement + different_valid_evidence_path -> MAY_BE_SUBSTANTIVELY_EQUIVALENT
same_requirement + missing_required_evidence     -> SUBSTANTIVE_FAILURE
```

The formalism therefore compares evidence to requirements rather than implementation shape to an incumbent path.

## Deterministic classification

This layer emits only a denial-basis classification:

- `SUBSTANTIVE_REQUIREMENTS_SATISFIED`: all required dimensions pass; no GTG disposition is implied.
- `SUBSTANTIVE_DENIAL_SUPPORTED`: at least one required dimension explicitly fails.
- `FAIL_CLOSED_REQUIRED`: at least one required dimension is unresolved and no explicit failure already determines insufficiency.
- `CONFORMITY_ONLY_DENIAL_INVALID`: all substantive dimensions pass but denial is based only on architectural nonconformity.

`CONFORMITY_ONLY_DENIAL_INVALID` means the stated denial basis is invalid; it does **not** mean GTG must return `ALLOW`. GTG may still discover another valid substantive basis before commit.

## Relationship to Gate Legitimacy

Gate Legitimacy asks whether the gate itself is inspectably fit to participate in governance. Architecture-Neutral Admissibility asks whether a candidate is being rejected for a substantive reason rather than incumbent-path conformity. A legitimate gate can still make an invalid conformity-only denial; an illegitimate gate can still happen to identify a real substantive failure. These are separate axes.

## Relationship to Independent Review

Independent Review determines whether review is structurally independent from the challenged gate and related control interests. It can provide challenge evidence about an architecture-neutrality dispute, but reviewer independence neither proves candidate admissibility nor creates transition authority.

## Relationship to GTG

Current GTG semantics already evaluate standing, authority, policy, evidence, constraints, and commit-time validity. This invariant narrows a failure mode that current semantics do not name explicitly: substituting implementation conformity for one of those substantive conditions.

This formalism remains non-authorizing:

```text
ArchitectureNeutralityEvidence -> GTG input evidence only
ArchitectureNeutralityEvidence !-> ALLOW
ArchitectureNeutralityEvidence !-> execution authority
```

## Falsification requirement

The invariant fails if deterministic evaluation either:

1. permits conformity-only denial after every substantive requirement is satisfied; or
2. suppresses a real denial/FAIL_CLOSED basis merely because the candidate is architecturally novel.

Both directions must remain testable.
