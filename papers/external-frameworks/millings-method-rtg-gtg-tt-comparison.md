# Millings Method™ and StegVerse RTG → GTG → TT

## A provenance-preserving external-framework comparison candidate

**Status:** research comparison candidate, not certification or equivalence claim  
**StegVerse Goal Task:** `MILLINGS-RTG-GTG-TT-COMPARISON-001`  
**Millings provenance:** independently authored by Frederick Redditt; this document does not assert shared authorship, derivation, endorsement, or technical identity.

## 1. Scope and evidence boundary

This comparison uses only propositions present in public statements supplied to the StegVerse research process. It does **not** treat those statements as a complete specification of the Millings Method.

Accordingly, this document compares **expressed functional propositions** against the current StegVerse `RTG -> GTG -> TT` contract. Where the source material does not establish a Millings mechanism, data structure, algorithm, disposition algebra, runtime, or proof system, the comparison says so rather than inferring one.

The purpose is to answer four questions:

1. Where do the two architectures express the same governance concern?
2. Where are they only partially aligned?
3. Where does StegVerse contain machinery not established by the supplied Millings evidence?
4. Does the comparison expose useful additions to the StegVerse canonical transition model?

## 2. StegVerse baseline

The current StegVerse cross-layer contract defines:

```text
RTG = describes the realized or candidate relational transition geometry
GTG = evaluates whether a candidate realization may commit
TT  = records the decision, commit, execution, observation, and continuation states
```

Its canonical flow is:

```text
RTG event candidate
-> material relational projection
-> GTG governance context
-> GTG activation result
-> GTG disposition
-> TT decision cell
-> commit-time revalidation
-> TT execution record
-> TT observation record
-> comparative reconstruction
```

Critical boundaries already include:

- RTG reachability does not imply GTG admissibility.
- GTG `ALLOW` does not prove TT execution.
- TT execution does not prove observation or correctness.
- proposal-time authority can become stale before commit.
- correction and supersession preserve history rather than erase it.
- non-identifiability must remain explicit when multiple explanations fit the evidence.

## 3. Supplied Millings-side propositions

The available public statements support the following bounded propositions:

### M1 — Capability and transition authority are different

A capable system need not possess unilateral authority to turn its conclusions into consequential external actions.

### M2 — Observation is not authority

Evidence that something was observed does not itself create permission or standing to act.

### M3 — Governance is not execution

A governance determination and an execution event are separate facts.

### M4 — Execution is not consequence

The occurrence of execution does not establish the resulting state.

### M5 — Execution receipts are not sufficient consequence proof

A receipt that execution occurred is not independently sufficient evidence of what actually formed afterward.

### M6 — Pre-execution evidence and post-execution reconciliation are both necessary

A governed transition should establish current evidence, admissibility, and authority before execution, then compare the execution record with evidence of the resulting state.

### M7 — Continuation must be re-earned after material change

Materially changed conditions should invalidate inherited continuation and require renewed evaluation.

### M8 — Fitness must not collapse into architectural conformity

A genuinely different architecture should be permitted to establish fitness through valid evidence rather than being rejected because it does not follow incumbent pathways.

### M9 — Governance gates themselves require legitimacy tests

Where a gate exercises public, quasi-public, safety, accreditation, or infrastructure authority, the legitimacy of the gate should itself be testable.

The supplied questions include whether the standard is neutral, whether independent systems can satisfy it, whether evidence is evaluated consistently, and whether adverse decisions can be challenged and independently reviewed.

## 4. Proposition mapping

| Millings-side proposition | StegVerse layer(s) | Current relationship | Notes |
| --- | --- | --- | --- |
| M1 Capability != transition authority | RTG + GTG | Strong convergence | RTG may describe a reachable candidate but cannot declare `ALLOW`; GTG authority is separate. |
| M2 Observation != authority | RTG + TT + GTG | Strong convergence | Observer state and evidence references do not mint standing or authority. |
| M3 Governance != execution | GTG + TT | Strong convergence | `GTG ALLOW -> TT execution` is explicitly invalid. |
| M4 Execution != consequence | TT | Strong convergence | TT separates execution, post-state, observation, and consequence relations. |
| M5 Execution receipt != consequence proof | TT | Strong convergence | Missing observation/reconstruction cannot be promoted into success. |
| M6 Pre/post evidence reconciliation | GTG + TT | Strong convergence | Commit-time revalidation precedes execution; observation and comparative reconstruction follow. |
| M7 Continuation must be re-earned | GTG + TT | Strong convergence | Stale authority at commit is a canonical negative case. |
| M8 Fitness != conformity | GTG + external-framework evaluation | Partial convergence | Compatible with current evidence/admissibility principles, but not yet a named cross-layer invariant. |
| M9 Gate legitimacy must itself be testable | GTG + TT | Partial convergence | Appeal, correction, dissent, provenance, and standing exist, but no single explicit gate-legitimacy object currently binds them. |

## 5. Exact convergence

The strongest functional convergence is the separation of **decision authority**, **execution**, and **resulting-state evidence**.

Both frameworks, as represented by the available evidence, reject the shortcut:

```text
admitted -> executed -> therefore correct
```

The StegVerse equivalent is structurally stronger because its current contract separately represents candidate geometry, governance context, disposition, commit-state revalidation, execution state, post-state, observation state, receipts, and reconstruction.

The shared governance proposition can be stated without collapsing provenance:

```text
prior admission is not continuing authority
execution is not consequence
an execution receipt is not consequence proof
```

That is functional convergence, not evidence of common origin.

## 6. Partial convergence

### 6.1 Gate legitimacy

StegVerse already records many ingredients relevant to gate legitimacy:

- policy and governance basis;
- authority and standing;
- evidence provenance;
- dissent;
- appeal and correction paths;
- commit-time validity;
- immutable correction/supersession lineage.

But the cross-layer contract does not presently require a single inspectable object answering:

```text
Who defined this gate?
Who controls the admissible evidence rules?
Who qualifies evaluators?
Who controls access to the execution path?
What independent review exists?
```

That is a meaningful gap exposed by the comparison.

### 6.2 Architecture-neutral fitness

StegVerse does not require external systems to use StegVerse internals in order to be analyzed. Its external-framework work is evidence-bounded and can compare different architectures without granting them authority.

However, the RTG/GTG/TT cross-layer contract does not yet explicitly prohibit this failure mode:

```text
candidate satisfies governing requirement through valid evidence
but is denied solely because it does not follow incumbent architecture
```

The Millings-side framing makes that prohibition worth expressing directly.

### 6.3 Independent review

StegVerse supports dissent, appeal/correction paths, and immutable supersession. Those mechanisms do not automatically prove that a reviewer is independent of the original gatekeeper.

A reviewer-independence predicate therefore remains distinct from the existence of an appeal path.

## 7. Divergence and non-identity

The available Millings evidence does not establish counterparts to several formal StegVerse mechanisms.

### RTG-specific machinery not established by current Millings evidence

- participant-linked relational geometry;
- translation operators;
- transition cost vectors;
- scale mappings;
- invariant sets;
- uncertainty and non-identifiability as first-class export fields.

### GTG-specific machinery not established by current Millings evidence

- the exact disposition set `ALLOW`, `DENY`, `FAIL_CLOSED`, `DEFER`, `TRANSFORM`, `ERROR`;
- activation-result semantics;
- standing/authority import structures;
- deterministic transform handling.

### TT-specific machinery not established by current Millings evidence

- linked immutable transition cells;
- predecessor/supersession lineage;
- observer posture as an explicit state;
- black/unknown transition elements;
- cross-scale projection rules;
- complete transition identity signatures.

Therefore no current evidence supports saying that the Millings Method *is* RTG, GTG, TT, or an equivalent implementation.

## 8. Candidate additions to the StegVerse canonical transition model

The comparison suggests five candidate refinements.

### A1 — Gate Legitimacy Record

Add a governance-side record that can bind:

```text
gate_id
standard_provenance
standard_change_authority
evidence_rule_provenance
evaluator_qualification_basis
evaluator_conflict_refs
execution_path_control_refs
challenge_path_refs
independent_review_basis
legitimacy_observation_state
```

Adoption criterion: the record must improve auditability without creating a new authority source or allowing legitimacy metadata to override an otherwise valid `DENY`/`FAIL_CLOSED` decision.

### A2 — Architecture-Neutral Admissibility Invariant

Candidate invariant:

```text
Architectural difference alone is not a sufficient denial basis
when the candidate independently satisfies the governing requirement
under the same valid evidence standard.
```

This does not require all architectures to be accepted. It requires the rejection basis to be substantive and evidence-linked rather than incumbent-path conformity alone.

### A3 — Independent Review Predicate

Add an explicit predicate that distinguishes:

```text
review_available
```

from:

```text
independent_review_available
```

Potential independence dimensions include organizational control, financial interest, authorship of the challenged rule, evaluator identity, and execution-path control.

### A4 — Continuation Renewal Trigger

Make material-change invalidation explicit across the transition lifecycle:

```text
proposal_state
-> commit_state
-> execution_context
-> observed_post_state
```

A material change at any authority- or evidence-bearing boundary should produce a new evaluation requirement rather than inherit a prior `ALLOW`.

### A5 — Execution/Consequence Reconciliation Tuple

Require the TT representation to preserve distinct references for:

```text
execution_receipt_ref
resulting_state_evidence_refs
consequence_ref
reconstruction_result
reconciliation_status
```

This would make the existing semantic separation mechanically harder to flatten in downstream implementations.

## 9. Prohibited equivalence claims

Until stronger source evidence exists, the following statements are unsupported:

```text
Millings Method == RTG/GTG/TT
Millings Method implements StegVerse
StegVerse implements the Millings Method
functional convergence proves derivation
similar terminology proves shared authorship
shared governance concern proves identical mechanism
```

The strongest supportable statement is:

> The independently authored Millings Method statements supplied for comparison show meaningful functional convergence with StegVerse around the separation of capability, authority, execution, consequence, evidence, continuation, and gate legitimacy, while the currently documented StegVerse RTG/GTG/TT system contains additional formal machinery not established by the supplied Millings evidence.

## 10. Falsification questions

A serious comparison should be falsifiable on both sides.

### Questions that could weaken the claimed convergence

- Does the full Millings Method permit execution authority to be inherited automatically from a prior decision?
- Does it treat execution receipts as sufficient proof of resulting state?
- Does it allow the evaluator and execution-path controller to be the same interested party without disclosure or review?
- Does it require incumbent implementation structure rather than evidence of fitness?

An affirmative answer to any of these could materially reduce the convergence described here.

### Questions that could expose a StegVerse deficiency

- Can a GTG policy reject a novel architecture solely because it does not match an incumbent implementation, despite satisfying the governing requirement?
- Can an adverse determination expose an appeal path that is not meaningfully independent?
- Can evidence-rule provenance or evaluator conflicts be omitted while a decision remains structurally valid?
- Can a material post-admission change escape renewed governance because it occurs after commit but before consequence is established?
- Can a downstream implementation collapse execution receipt and consequence proof despite the semantic distinction in TT?

A `yes` answer should produce a testable remediation candidate rather than a rhetorical defense.

## 11. Bounded conclusion

The current evidence supports **meaningful architectural convergence without technical identity**.

The most important convergence is not a shared vocabulary. It is a shared separation-of-powers claim:

```text
capability != authority
observation != authority
governance != execution
execution != consequence
execution receipt != consequence proof
prior admission != continuing authority
```

The most useful contribution exposed by the comparison is a stronger treatment of **the gate itself as a governed object**. StegVerse already governs candidate transitions, preserves evidence, separates authority from execution, and records correction. It can be strengthened further by making gate legitimacy, architecture-neutral fitness, and reviewer independence explicit inspectable predicates rather than leaving them distributed across existing fields and processes.

Those additions should be evaluated on their own merits and, if adopted, attributed as StegVerse refinements informed by an external comparison. They should not be represented as imported Millings mechanisms unless the independently authored Millings source material establishes that provenance directly.
