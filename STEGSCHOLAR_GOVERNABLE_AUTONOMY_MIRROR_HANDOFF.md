# StegScholar Governable Autonomy Mirror Handoff

## Repository

- Organization: `StegVerse-Labs`
- Repository: `StegScholar`
- Default branch: `main`
- Research-program target: `research-programs/governable-autonomy/`
- Related paper targets: `papers/`

## Source-of-truth scope

This handoff is the authoritative continuation record for the **Governable Autonomy** research program in StegScholar.

It does not replace `STEGSCHOLAR_MIRROR_HANDOFF.md`, which remains authoritative for the separate Recoverability Geometry / Rigel Number research track.

The program is a candidate systems-governance architecture. Its claims remain conceptual or formal hypotheses until supported by proofs, implementations, simulations, incident studies, independent review, or empirical validation.

## Current paper set

1. *Survivable Governance*
2. *Formal Model Sketch: Survivable Governance Under Epistemic Constraint*
3. *Trust-Bounded Socio-Technical Systems: Architectural Primitives for Auditability and Failure*
4. *Ghost Credentials and Phantom Trust*
5. *Boundary-Condition Autonomy*
6. *Governance Invariant for Autonomous Systems* — proposed anchor paper

## Durable conceptual decisions

1. Treat trust as mutable system state rather than a permanent assumption.
2. Treat audit status, including irrecoverable audit loss, as operational state.
3. Separate credential validity from continuing authority justification.
4. Treat autonomy as a revocable system mode governed by enforceable boundary conditions.
5. Place binding governance at the state-transition or execution boundary where an action commits external or system state.
6. Model BCAT as a gateway between complex autonomy and external reality: autonomous components may propose actions, while the execution control plane determines whether those actions may cross the boundary.
7. As epistemic support, state integrity, incentive alignment, verification capacity, or enforcement capacity deteriorates, the permitted action set should contract rather than persist by inheritance.
8. At a critical degradation threshold, execution may collapse to a discrete or binary boundary such as `ALLOW/DENY` or `CONTINUE/PAUSE`.
9. Proposed safety invariant:

   ```text
   If epistemic certainty decreases, execution authority must not expand.
   ```

   A candidate scalar expression is:

   ```text
   E(t+1) < E(t)  =>  A(t+1) <= A(t)
   ```

   This notation is provisional. A set-based authority model may be more precise because emergency actions can change class without increasing total effective authority.
10. The architecture bounds execution; it does not by itself solve alignment, ethics, semantic correctness, or global optimization.
11. Compute availability cannot be guaranteed absolutely. The formal model must instead define degraded-capacity behavior, a minimum enforcement floor where feasible, safe pause/refusal thresholds, and authorized recovery paths.
12. State integrity may require a first-class variable such as `I in {Trusted, Degraded, Compromised}`; this remains an open formalization task rather than a settled model extension.

## Unified program view

The working architecture is:

```text
Trust state
    -> Auditability
    -> Credential legitimacy
    -> Boundary enforcement
    -> Execution authority at commit
    -> External or system reality
```

Across epistemic degradation, the intended authority progression is:

```text
Open -> Constrained -> Revoked
```

This is a normative architecture proposal, not an empirical law.

## External discussion and related-work provenance

A public LinkedIn discussion with Saida Harle helped sharpen the control-plane framing around operational pressure, constraint reconciliation, state integrity, and authority at state-transition boundaries. Saida referenced Dr. Masayuki Otani's ARETABA/MGAG work and a point of irreversibility described as `T(e)`.

These exchanges are related-work and conceptual-provenance inputs only. They are not independent peer review, endorsement, validation, or proof of equivalence. Primary sources and exact definitions must be verified before citation or public comparison. See issue #9.

## Generated artifact status

Two conversation-runtime bundles were generated:

- `stegscholar_v1_bundle.zip`
- `stegscholar_v2_system_papers.zip`

They are **non-authoritative** because their canonical manuscript sources, diagram sources, build process, hashes, and exact contents have not been committed and reproduced from the repository. They must not be treated as release artifacts or conference-ready papers. See issues #3 and #17.

## Public peer-review decision

StegScholar requires a public-facing research and peer-review section on StegVerse.org. The portal must distinguish:

- stable papers;
- working papers;
- draft concepts;
- research notes;
- diagrams and models;
- validation artifacts;
- superseded or merged work.

Each public paper page should expose version, status, claims scope, canonical source, generated artifact hashes, known limitations, citation guidance, and a durable feedback path. `stable-paper` means internally version-stable, not externally peer-reviewed. Site implementation must check `StegVerse-Labs/Site/docs/SITE_MIRROR_HANDOFF.md` before mutation. See issue #1.

## Active task map

- #1 — Publish StegScholar peer-review portal on StegVerse.org
- #2 — Formalize additional paper candidates from prior research chats
- #3 — Regenerate and commit source-controlled paper artifacts
- #4 — Define public peer-review evidence and status model
- #5 — Validate the invariant against distributed-system failure cases
- #6 — Create source-controlled architecture diagrams
- #7 — Develop deterministic execution-boundary model for BCAT
- #8 — Cross-update ecosystem documentation at release readiness
- #9 — Establish related-work record for control-plane and irreversibility discussion
- #10 — Define compute-floor and degraded-capacity semantics
- #11 — Add state-integrity and compromised-state recovery model
- #12 — Add monotonic authority-contraction property tests
- #13 — Create program index and paper taxonomy
- #14 — Add archival and continuation criteria
- #15 — Consolidate implementation sequence
- #16 — Create this handoff
- #17 — Create artifact manifest
- #18 — Create machine-readable paper-status registry
- #19 — Implement and verify handoff and manifest
- #20 — Create initial canonical source directories

## Recommended implementation order

1. Maintain this handoff and create the program index/taxonomy.
2. Create the artifact manifest and paper-status registry.
3. Formalize the execution-boundary model, degraded-capacity semantics, and state-integrity model.
4. Implement property tests and simulations.
5. Create reproducible diagrams and paper builds.
6. Validate claims against a defined incident corpus and related work.
7. Inventory additional paper candidates.
8. Publish the public portal.
9. Tag/release only after claims, sources, artifacts, and review status are reproducible.
10. At release readiness, assess and update `StegVerse-Labs/Site`, `GCAT-BCAT-Engine/Publisher`, `admissibility-wiki`, and `stegguardian-wiki` as applicable.

## Known blockers and cautions

- The six-paper corpus has not yet been reconstructed as canonical full manuscripts from committed sources.
- No proof yet establishes the proposed invariant for a general system model.
- No defined incident corpus yet supports claims about prevalence across catastrophic distributed-system failures.
- No executable BCAT reference model or property tests are committed.
- State integrity, incentive alignment, and compute capacity are not yet integrated into one minimal model.
- The relationship to ARETABA/MGAG and `T(e)` is unverified beyond the public reference supplied in discussion.
- External review is unassigned.
- Public Site implementation is unassigned.

## Ownership

- Research direction and authorship: Rigel Randolph
- Repository continuation: StegScholar research program
- Formal model implementation: unassigned
- Artifact reconstruction: unassigned
- Public portal implementation: unassigned
- External peer review: unassigned

## Permitted continuation scope

A continuation session may:

- refine manuscripts, definitions, invariants, threat models, and limitations;
- create state machines, simulations, property tests, and counterexamples;
- reconstruct reproducible diagrams and PDF builds;
- verify and document related work;
- inventory and classify additional paper candidates;
- implement the StegScholar public portal after checking the Site mirror handoff;
- update this handoff and linked issues with committed evidence.

A continuation session must not:

- describe public discussion as peer review or endorsement;
- claim the invariant is proven or empirically universal without evidence;
- claim conference readiness merely because a PDF uses a systems-paper structure;
- claim the five failure classes explain most major incidents without a defined corpus and reproducible analysis;
- present alignment or ethics as solved by execution-boundary enforcement;
- treat conversation-generated binary artifacts as canonical.

## Archival condition

A session working on this track is archivable when its unique decisions, definitions, evidence, tasks, artifact status, and ownership changes are committed here or in linked durable records, and no session-specific mutation remains unverified.
