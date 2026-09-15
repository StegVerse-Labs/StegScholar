# Millings Method × RTG/GTG/TT Comparison Mirror Handoff

Updated: 2026-09-15
Goal Task ID: `MILLINGS-RTG-GTG-TT-COMPARISON-001`
COSV: `40011100100000`
Status: `ACTIVE / CLAIMED_INTEGRATION`

## Purpose

Formalize the independently authored **Millings Method™** as an external-framework comparison candidate against StegVerse `RTG -> GTG -> TT` without collapsing provenance, authorship, terminology, or authority boundaries.

This comparison is analytical only. It does not claim that the Millings Method derives from StegVerse, that StegVerse derives from the Millings Method, that either framework certifies the other, or that functional convergence proves shared technical identity.

## Provenance boundary

Source material for this comparison is limited to public statements supplied by the user from Frederick Redditt and the StegVerse public discussion around them. The Millings Method remains independently authored. StegVerse terms remain StegVerse terms.

The comparison must distinguish:

- **verbatim/source-attributed Millings claims** from StegVerse interpretations;
- **functional convergence** from implementation equivalence;
- **compatible concerns** from shared mechanism;
- **possible additions to StegVerse** from claims that the Millings Method itself contains those additions.

## Observed Millings-side propositions available for comparison

Current supplied statements support the following bounded propositions:

1. Separating capability from transition authority is preferable to the false choice between stopping intelligence and permitting unconstrained execution.
2. Observation is not authority.
3. Governance is not execution.
4. Execution is not consequence.
5. A receipt of execution is not by itself independent proof of the resulting state.
6. A governed transition should establish current evidence, admissibility, and authority before execution, then compare the execution record with evidence of what actually formed.
7. Materially changed conditions should require continuation to be earned again.
8. Governance gates should not reduce fitness evaluation to conformity with incumbent pathways.
9. Genuinely different architectures should be able to establish fitness through valid evidence.
10. Gate legitimacy itself should be testable: neutrality of the standard, accessibility to independent systems, consistency of evidence evaluation, and meaningful challenge/independent review.

These are evidence-bounded comparison inputs, not a complete specification of the Millings Method.

## Canonical StegVerse comparison target

The authoritative StegVerse comparison contract is:

`papers/rtg-gtg-tt/cross-layer-contract.md`

with TT continuation truth in:

`TT_MIRROR_HANDOFF.md`

StegVerse currently separates:

```text
RTG = candidate/realized relational transition geometry
GTG = admissibility, authority, standing, evidence, constraints, disposition
TT  = explicit decision, commit-time validity, execution, post-state, observation, receipt, correction/supersession record
```

## Initial convergence map

### Strong convergence

- **Capability != transition authority** -> StegVerse keeps descriptive/reasoning reachability distinct from GTG authority.
- **Observation != authority** -> RTG/TT observation state does not mint governance authority.
- **Governance != execution** -> GTG `ALLOW` does not prove TT execution.
- **Execution != consequence** -> TT distinguishes execution state, post-state, consequence relation, and observation.
- **Execution receipt != resulting-state proof** -> TT requires distinct observation/reconstruction evidence.
- **Material change requires renewed standing** -> commit-time revalidation and stale-authority fixtures already encode this principle.
- **Independent evidence path** -> StegVerse external-framework analysis already separates evidence sufficiency from platform conformity.

### Partial convergence requiring care

- **Gate legitimacy review** has analogues in StegVerse dissent, appeal/correction paths, authority provenance, evidence provenance, and fail-closed semantics, but StegVerse does not yet define a single explicit `gate_legitimacy` object across RTG/GTG/TT.
- **Architecture-neutral fitness** is consistent with StegVerse evidence/admissibility principles, but the cross-layer contract does not yet make architectural nonconformity itself a prohibited rejection basis.
- **Independent review of adverse decisions** exists conceptually through appeal/correction/supersession paths, but a deterministic reviewer-independence predicate is not yet a canonical cross-layer invariant.

### Current divergence / non-identity

- RTG is a formal relational-geometry layer with scale/invariant/non-identifiability semantics; no supplied Millings statement establishes an equivalent formal geometry layer.
- GTG has explicit disposition semantics (`ALLOW`, `DENY`, `FAIL_CLOSED`, `DEFER`, `TRANSFORM`, `ERROR`) and authority/standing imports; no supplied Millings statement establishes identical outcome algebra.
- TT is an inspectable linked transition-receipt representation with correction, supersession, observer posture, black/unknown transitions, and cross-scale constraints; no supplied Millings statement establishes an equivalent ledger representation.
- Therefore the current relationship is **functional convergence around transition governance and evidence**, not technical equivalence.

## Candidate additions to StegVerse

The comparison should test, not automatically adopt, the following additions:

1. **Gate-legitimacy invariant**
   - A governance gate should expose the provenance of standards, evidence rules, evaluator standing, and execution-path control.

2. **Architecture-neutral admissibility invariant**
   - A candidate may not be rejected solely because it does not use an incumbent architecture when it can satisfy the governing requirement through independently valid evidence.

3. **Independent-review predicate**
   - An adverse governance disposition should declare whether a genuinely independent review path exists and what qualifies as independence.

4. **Continuation-renewal predicate**
   - Material changes between proposal, commit, execution, and observed consequence should force re-evaluation rather than inherit prior admission.

5. **Execution-to-consequence reconciliation tuple**
   - Preserve distinct references for `execution_receipt`, `resulting_state_evidence`, `consequence_ref`, and `comparison/reconstruction_result`.

These are StegVerse candidate refinements inspired by comparison, not assertions of Millings authorship over StegVerse mechanisms.

## Required deliverable

Create a research comparison document that contains:

- source/provenance section;
- proposition-by-proposition mapping;
- convergence / partial convergence / divergence table;
- prohibited equivalence claims;
- candidate additions with adoption criteria;
- falsification questions for both sides;
- a bounded conclusion stating what can and cannot presently be inferred.

## Validation requirements

Before completion:

- verify every StegVerse claim against current RTG/GTG/TT source;
- preserve independent Millings authorship explicitly;
- avoid attributing unsupplied mechanisms to the Millings Method;
- update this handoff and `README.md`;
- register the task in the canonical Task Registry and COSV surfaces;
- open PRs rather than claiming merge, release, runtime execution, or propagation without evidence.

## Current next action

Materialize the comparison paper, task-registry record/vector, README references, then validate the branch diff and open the required PRs.
