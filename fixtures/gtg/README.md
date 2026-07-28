# GTG Deterministic Fixtures

## Status

Research validation fixtures for Generalized Transition Governance v0.1. These fixtures do not create certification, execution authority, legal authority, or protocol conformance status.

## Current bundle

```text
fixtures/gtg/activation_cases.json
```

The bundle currently exercises:

1. recognized-but-inactive relational governance;
2. individually authorized actors with a jointly inadmissible transition;
3. stale or unreconstructable relational state at commit time;
4. remediable standing defects producing `DEFER`;
5. authorized `TRANSFORM` with replacement availability;
6. justified `NOT_APPLICABLE`;
7. misuse of `NOT_APPLICABLE` against a material relation;
8. deterministic `ALLOW` under complete active governance conditions.

## Validator

```bash
python scripts/validate_gtg_fixtures.py
```

The validator checks:

- fixture structure and identifier uniqueness;
- canonical activation state membership;
- canonical governance disposition membership;
- exact activation-test field coverage;
- typed boolean activation tests;
- deterministic activation derivation;
- deterministic activation-to-disposition derivation;
- fail-closed handling for `INACTIVE`, `INCOMPLETE`, and `ERROR`;
- justification requirements for `NOT_APPLICABLE`;
- prevention of `NOT_APPLICABLE` where a material relation exists.

## Maturity boundary

Passing these fixtures establishes only that the implemented research rules behave deterministically for the committed cases. It does not establish empirical validity, universal governance correctness, substantive legitimacy, or readiness for normative projection into `Admissible-Existence/AE`.

Before protocol projection, the fixture set must also cover:

- consent defects;
- unknown activation states;
- evaluator failure;
- multiple-governance conflict preservation;
- purpose-inverting boundaries;
- authority non-inheritance;
- continuation after actor termination;
- identical outputs produced through materially different authority histories;
- RTG descriptions and TT cells lacking sufficient GTG evidence.
