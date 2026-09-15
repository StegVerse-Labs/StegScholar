# Millings Method comparison refinement disposition

Status: terminal comparison disposition for `MILLINGS-RTG-GTG-TT-COMPARISON-001`

## Purpose

Evaluate the five candidate StegVerse refinements produced by the provenance-preserving Millings Method comparison and determine which require genuinely new Goal Tasks versus continuation inside already-canonical workstreams.

## Disposition summary

| Candidate | Existing coverage | Gap | Disposition |
| --- | --- | --- | --- |
| Gate legitimacy | GTG authority/standing, evidence provenance, dissent, appeal/correction | No first-class gate-legitimacy record or falsification protocol | NEW GOAL TASK: `GATE-LEGITIMACY-INVARIANT-001` |
| Architecture-neutral admissibility | Evidence-bounded external-framework analysis; GTG substantive admissibility | No explicit invariant rejecting conformity-only denial | NEW GOAL TASK: `ARCHITECTURE-NEUTRAL-ADMISSIBILITY-001` |
| Independent review | StegScholar review schema has independent-review types and reviewer identity classes; GTG supports dissent/appeal/correction | No deterministic independence predicate across gate ownership, rule authorship, financial/common-control, or execution-path control | NEW GOAL TASK: `INDEPENDENT-REVIEW-PREDICATE-001` |
| Continuation renewal | TT/GTG already require commit-time revalidation, continuing authority, bound evidence; stale-authority case exists | Broader proposal-to-commit fixtures remain in active TT queue | NO NEW TASK; fold into `TT_MIRROR_HANDOFF.md` work item for proposal-time vs commit-time fixtures and authority/evidence revalidation |
| Execution-to-consequence reconciliation | TT already separates post-state, consequence, observation, receipts; RTG/GTG/TT cross-layer contract separates execution state and observation/reconstruction | Full-table validator/receipt integrity and broader schema integration remain active TT work | NO NEW TASK; fold into existing TT full-schema/validator and consequence/observer continuation work |

## Why only three new Goal Tasks

Creating five new tasks would duplicate two work items already owned by the active TT formalism. The task-registry contract requires reusing already-tracked work before deriving adjacent tasks. Continuation renewal and execution-to-consequence reconciliation are therefore recorded as explicit TT acceptance criteria rather than new task identities.

The other three candidates are not currently represented as deterministic cross-layer invariants. They are separable enough to falsify independently and therefore receive distinct task identities.

## Adoption boundaries

No candidate refinement is adopted merely because the external comparison found it attractive. Each new task must support rejection as a legitimate outcome and must preserve the following boundaries:

- provenance comparison does not create authority;
- gate legitimacy does not override substantive disposition;
- architecture neutrality does not weaken evidence, safety, policy, authority, or standing requirements;
- independent review does not create a second governance authority;
- continuation renewal remains contemporaneous governance, not perpetual reapproval;
- execution evidence and consequence evidence remain distinct.

## Parent closeout

The parent comparison has completed its bounded purpose once:

1. provenance was preserved;
2. convergence, partial convergence, and divergence were mapped;
3. prohibited equivalence claims were documented;
4. candidate refinements were evaluated separately;
5. necessary new tasks were derived without duplicating active TT work;
6. source and coordination PRs were merged with successful validation evidence.

No runtime activation, certification, external-framework registry admission, release, or downstream propagation follows from this closeout.
