# Generalized Transition Governance Conflict Resolution

## Status

Research formalism for composing multiple governance determinations without erasing source authority, dissent, unresolved evidence, or profile-specific precedence.

## Problem

A candidate transition may be evaluated by multiple governance systems, authorities, jurisdictions, policies, observers, or scales. Their determinations may disagree.

GTG does not permit silent averaging, permissive collapse, or majority voting unless a declared composition profile grants that rule standing.

## Source determinations

For each applicable governance source `i`:

```text
d_i = (
  source_id_i,
  standing_i,
  scope_i,
  evidence_i,
  policy_i,
  activation_i,
  disposition_i,
  dissent_i
)
```

with:

```text
disposition_i in {ALLOW, DENY, FAIL_CLOSED, DEFER, TRANSFORM, ERROR}
```

A source determination is preserved even when it does not control the composite result.

## Composition operator

```text
Omega(D, profile, chi_commit) -> d*
```

where `D = {d_1, ..., d_n}` and `profile` declares the applicable precedence, scope, standing, conflict, and fail-safe rules.

The composite result must preserve:

- every source determination;
- source standing and scope;
- evidence and policy references;
- unresolved conflicts;
- dissent;
- the selected precedence rule;
- the reason the rule had standing;
- the resulting disposition;
- continuation, appeal, and correction paths.

## Applicability gate

A determination may enter composition only when its source has declared standing and scope for the candidate transition.

```text
ApplicableSource(d_i, tau, chi_commit) =
  StandingValid(d_i)
  and ScopeCovers(d_i, tau)
  and FreshEnough(d_i, chi_commit)
```

An inapplicable source is preserved in the receipt when relevant to challenge or provenance, but it must not silently control the composite outcome.

## Baseline fail-safe precedence

The following is a research baseline, not a universal ordering:

1. invalid or unknown composition mechanism -> `ERROR` or `FAIL_CLOSED` according to profile;
2. missing mandatory source determination -> `FAIL_CLOSED` or `DEFER` according to resolvability;
3. applicable `DENY` under a controlling prohibition -> `DENY`;
4. applicable `FAIL_CLOSED` under a mandatory safety or authority gate -> `FAIL_CLOSED`;
5. resolvable dependency or standing defect -> `DEFER`;
6. authorized and admissible replacement with preserved lineage -> `TRANSFORM`;
7. unanimous or profile-sufficient `ALLOW` with no controlling conflict -> `ALLOW`.

No rule may interpret absence of an explicit denial as `ALLOW` unless the profile explicitly and validly establishes that behavior.

## Conflict classes

### Authority conflict

Two or more sources claim incompatible control over the same transition.

Required response:

- preserve both claims;
- test standing and scope independently;
- apply declared jurisdiction or delegation rules;
- return `DEFER` or `FAIL_CLOSED` when control cannot be resolved safely.

### Policy conflict

Applicable policies require incompatible outcomes.

Required response:

- preserve policy versions and effective times;
- identify the controlling profile rule;
- prohibit silent policy substitution;
- preserve dissent and unresolved interpretation.

### Evidence conflict

Sources rely on incompatible factual records.

Required response:

- preserve each evidence chain;
- distinguish missing evidence from contradictory evidence;
- use `DEFER` when additional evidence is reasonably obtainable;
- use `FAIL_CLOSED` when required evidence cannot be established before commit.

### Scale conflict

A rule valid at one scale conflicts with a rule or invariant at another scale.

Required response:

- declare scale maps;
- identify which invariants must survive translation;
- prohibit transferring a rule unchanged without an admissible scale mapping.

### Relational conflict

Individually authorized actions combine into an inadmissible relational configuration.

Required response:

- evaluate the joint relational projection;
- do not infer joint admissibility from local authorization;
- map the conflict to `DENY`, `FAIL_CLOSED`, `DEFER`, or `TRANSFORM` under the declared profile.

## Non-erasure requirement

For every composition:

```text
Preserve(d_i) = true for all source determinations d_i
```

Preservation does not mean equal controlling weight. It means the final receipt must permit an independent reviewer to reconstruct what each source concluded and why.

## No silent consensus

A composite result is invalid when disagreement is removed without an explicit successor record or declared composition rule.

```text
Divergence(D) and not Preserved(D) -> InvalidComposite
```

## Transformation conflicts

A `TRANSFORM` proposal does not outrank a prohibition automatically. The replacement transition must receive fresh evaluation under all controlling sources.

```text
Omega(D, profile, chi_commit) = TRANSFORM
```

only when:

- the original candidate is not admitted;
- transformation authority is valid;
- replacement lineage is complete;
- user or originating intent is not silently changed;
- the replacement enters the current admissible and authorized solution set.

## Composite receipt

Minimum fields:

```text
CompositeReceipt = (
  candidate_transition_id,
  profile_id,
  source_determinations,
  applicability_results,
  conflicts,
  precedence_rule,
  precedence_authority,
  composite_disposition,
  dissent,
  unresolved_dependencies,
  continuation_refs,
  challenge_refs,
  commit_time
)
```

## Falsification cases

The conflict formalism fails when:

1. a source determination disappears from the composite receipt;
2. the most permissive source wins without declared standing;
3. a stale source controls commit-time outcome;
4. contradictory policies are represented as consensus;
5. an applicable denial is overwritten without an authorized successor rule;
6. a scale conflict is ignored;
7. relationally induced inadmissibility is reduced to individual authorization;
8. a transform candidate bypasses fresh evaluation;
9. dissent exists but is not reconstructable;
10. identical composite outputs conceal materially different source histories.

## Claims binding

This document operationalizes claims including:

```text
GTG-M-001
GTG-M-002
GTG-M-003
GTG-A-002
GTG-C-001
GTG-C-004
GTG-R-004
```

Claim maturity remains controlled by the GTG claims register.

## Publication boundary

This is a research composition formalism. It does not establish universal legal hierarchy, jurisdiction, institutional legitimacy, or a single precedence order for all domains.
