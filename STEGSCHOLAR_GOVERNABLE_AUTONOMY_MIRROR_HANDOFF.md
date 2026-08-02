# StegScholar Governable Autonomy Mirror Handoff

## Repository and authoritative scope

- Organization: `StegVerse-Labs`
- Repository: `StegScholar`
- Branch: `main`
- Program target: `research-programs/governable-autonomy/`
- Paper targets: `papers/`
- Canonical issue lane: issues #1-#12 and #46

This is the authoritative continuation record for the **Governable Autonomy** research program. It does not replace `STEGSCHOLAR_MIRROR_HANDOFF.md`, which remains authoritative for Recoverability Geometry / Rigel Number work, or other scoped handoffs under `docs/` and `funding/`.

The program is a candidate systems-governance architecture. Claims remain conceptual or formal hypotheses until supported by proofs, executable models, simulations, incident studies, independent review, or empirical validation.

## Originating session goal

Create a public, peer-reviewable StegScholar program for the current governance papers; formalize Boundary-Condition Autonomy as the execution gateway between complex autonomy and external reality; preserve additional paper candidates; generate reproducible papers and diagrams; and make federal security requirements the minimum rather than the target ceiling.

## Current paper set

1. `GA-001` — *Governance Invariant for Autonomous Systems*
2. `GA-002` — *Survivable Governance*
3. `GA-003` — *Formal Model Sketch: Survivable Governance Under Epistemic Constraint*
4. `GA-004` — *Trust-Bounded Socio-Technical Systems: Architectural Primitives for Auditability and Failure*
5. `GA-005` — *Ghost Credentials and Phantom Trust*
6. `GA-006` — *Boundary-Condition Autonomy*

## Durable conceptual decisions

1. Trust is mutable system state, not a permanent assumption.
2. Audit status, including irrecoverable audit loss, is operational state.
3. Credential validity is distinct from continuing authority justification.
4. Autonomy is a revocable execution mode governed by enforceable boundary conditions.
5. Binding governance occurs at the state-transition or execution boundary where an action commits external or system state.
6. BCAT is the gateway between complex autonomy and reality: autonomous components may propose actions; the execution control plane decides whether those proposals may cross the boundary.
7. As epistemic support, state integrity, incentive alignment, verification capacity, or enforcement capacity deteriorates, the permitted action set should contract rather than persist by inheritance.
8. At a critical degradation threshold, execution may become discrete or binary: `ALLOW/DENY` or `CONTINUE/PAUSE`.
9. Proposed safety invariant: **If epistemic certainty decreases, execution authority must not expand.**
10. The scalar form `E(t+1) < E(t) => A(t+1) <= A(t)` is provisional; a set-based model is expected to handle emergency action classes more accurately.
11. The architecture bounds execution. It does not by itself solve alignment, ethics, semantic correctness, or global optimization.
12. Absolute compute availability cannot be guaranteed. The model must define degraded-capacity behavior, minimum enforcement capacity where feasible, fail-safe thresholds, and authorized recovery paths.
13. State integrity may require a first-class variable such as `I in {Trusted, Degraded, Compromised}`; this remains an open formalization task.

## Unified program model

```text
Trust state
    -> Auditability
    -> Credential legitimacy
    -> Boundary enforcement
    -> Execution authority at commit
    -> External or system reality
```

Intended degraded-state progression:

```text
Open -> Constrained -> Revoked
```

This is a normative architecture proposal, not an empirical law.

## Federal-floor-plus security decision

Applicable United States federal security requirements are the minimum control floor. StegScholar must exceed that floor where stronger controls are feasible and proportionate.

Canonical policy: `SECURITY_BASELINE.md`

The baseline references NIST SP 800-53 Rev. 5 control families, NIST SP 800-218 SSDF, FIPS 140-3 validated cryptography where applicable, and CISA Secure by Design principles. It explicitly avoids claiming FISMA compliance, FedRAMP authorization, certification, or federal approval.

Required controls include fail-closed validation, least privilege, source and artifact provenance, reproducible generation, separated authority states, expiring claims, collision prevention, dependency integrity, secret minimization, artifact hashes, truthful review status, recovery authority, private vulnerability handling, and durable audit evidence.

## Completed durable infrastructure

- Program index and taxonomy: `research-programs/governable-autonomy/README.md`
- Artifact manifest: `research-programs/governable-autonomy/ARTIFACT_MANIFEST.md`
- Machine-readable paper registry: `research-programs/governable-autonomy/paper-registry.json`
- Canonical manuscript scaffolds for `GA-001` through `GA-006`
- Shared figure source target: `figures/governable-autonomy/`
- Federal-floor-plus security policy: `SECURITY_BASELINE.md`
- Review-evidence JSON Schema: `research-programs/governable-autonomy/review-schema.json`
- Expiring task-claim registry: `research-programs/governable-autonomy/task-claims.json`
- Fail-closed validator: `tools/validate_governable_autonomy.py`
- Hosted validation workflow: `.github/workflows/governable-autonomy-validate.yml`

## Active implementation claim

- Task ID: `GA-SEC-001`
- Originating goal: federal security requirements are the floor and StegScholar must exceed them
- Issue: #46
- Claim registry: `research-programs/governable-autonomy/task-claims.json`
- State: `CLAIMED_FOR_IMPLEMENTATION`
- Claimant: `governable-autonomy-security-validation-lane`
- Branch: `main`
- Claim created: `2026-08-02T22:49:51Z`
- Claim expires: `2026-08-03T22:49:51Z`
- Release condition: scoped files committed, deterministic validator passes, hosted workflow run/jobs/logs/artifact inspected, issue #46 updated, and claim released or transferred
- Collision boundary: only the security baseline, review schema, claim registry, validator, validation workflow, and this handoff are claimed; `funding/`, Recoverability Geometry, and other handoff scopes are excluded

## Validation state

### Proven

- Required security, schema, claim, validator, and workflow files were committed directly to `main`.
- Review schema is closed to undeclared fields and constrains independent-review and replication states.
- Claim registry defines the canonical claim-state vocabulary, expiration, evidence expectations, collision boundaries, and next task.
- Workflow permissions are read-only, checkout credentials are not persisted, execution is time-bounded, validation is fail closed, and a receipt artifact is required.

### Not yet proven

- No successful hosted workflow run, job log, or uploaded receipt artifact has yet been directly inspected for the new validation workflow.
- The available commit-run connector returned no observable run for commit `58c34a225953c2b363828b6fc2900595bd005f48`; this is an evidence gap, not a workflow-success claim.
- Issue #46 and claim `GA-SEC-001` remain open until hosted evidence is observed or the claim expires and is reassigned.

## External discussion and related-work provenance

A public LinkedIn discussion with Saida Harle sharpened the control-plane framing around operational pressure, constraint reconciliation, state integrity, and authority at state-transition boundaries. Saida referenced Dr. Masayuki Otani's ARETABA/MGAG work and a point of irreversibility described as `T(e)`.

These are related-work and conceptual-provenance inputs only—not independent peer review, endorsement, validation, or proof of equivalence. Primary sources and exact definitions must be verified before citation or public comparison. See issue #9.

## Generated artifact status

Conversation-runtime bundles `stegscholar_v1_bundle.zip` and `stegscholar_v2_system_papers.zip` are non-authoritative reconstruction aids. Their canonical sources, exact contents, build process, and hashes were not durably committed with the binaries. They must not be treated as release artifacts or conference-ready papers. See issue #3.

## Public peer-review decision

StegScholar requires a public-facing research and peer-review section on StegVerse.org that distinguishes stable papers, working papers, draft concepts, research notes, diagrams/models, validation artifacts, and superseded/merged work.

Each public paper page must expose version, maturity, review state, claims scope, canonical source, artifact hashes, limitations, citation guidance, and a durable feedback path. `stable-paper` means internally version-stable, not externally peer-reviewed. Site implementation must read `StegVerse-Labs/Site/docs/SITE_MIRROR_HANDOFF.md` before mutation. See issue #1.

## Task inventory and ownership

| Task | Location | State | Owner | Next executable action |
|---|---|---|---|---|
| Public peer-review portal | issue #1; future `StegVerse-Labs/Site` route | UNCLAIMED | unassigned | consume paper registry and review schema after Site handoff review |
| Additional paper inventory | issue #2 | UNCLAIMED | unassigned | create durable candidate inventory |
| Reproducible paper artifacts | issue #3 | BLOCKED | unassigned | complete full manuscripts, build path, figures, and hashes |
| Review evidence/status model | issue #4; `review-schema.json` | PARTIALLY IMPLEMENTED | GA security lane | add sample record and portal consumer contract |
| Invariant incident validation | issue #5 | UNCLAIMED | unassigned | define corpus and coding method |
| Architecture diagrams | issue #6 | UNCLAIMED | unassigned | implement source-controlled SVGs and text alternatives |
| BCAT execution-boundary model | issue #7 | UNCLAIMED | unassigned | formal state/transition model and executable reference |
| Release cross-updates | issue #8 | BLOCKED | release lane unassigned | activates only after release gate passes |
| Related-work verification | issue #9 | UNCLAIMED | unassigned | verify primary Otani/ARETABA/MGAG sources |
| Compute-floor semantics | issue #10 | UNCLAIMED | unassigned | formalize degraded verification/enforcement capacity |
| State-integrity model | issue #11 | UNCLAIMED | unassigned | independence analysis and recovery transition table |
| Authority-contraction tests | issue #12 | BLOCKED | unassigned | depends on executable model from #7/#10/#11 |
| Security baseline and validation | issue #46; `GA-SEC-001` | CLAIMED_FOR_IMPLEMENTATION | current security lane | inspect hosted workflow and receipt; release claim |

## Completed issues

- #13 — Program index and taxonomy
- #14 — Archival and continuation criteria
- #15 — Implementation sequence
- #16 — Governable Autonomy handoff
- #17 — Artifact manifest
- #18 — Paper-status registry
- #19 — Handoff/manifest verification
- #20 — Canonical source directories

## Cross-repository obligations

At genuine release readiness, issue #8 governs applicability and propagation checks for:

- `StegVerse-Labs/Site`
- `GCAT-BCAT-Engine/Publisher`
- `admissibility-wiki`
- `stegguardian-wiki`
- any master-records or publication-custody destination identified by current contracts

No propagation, deployment, runtime publication, release, or governed activation is currently claimed.

## Recommended implementation order

1. Complete hosted validation observation and release `GA-SEC-001` / issue #46.
2. Complete issue #4 with a valid sample review record and portal-consumer contract.
3. Formalize issue #7 execution-boundary model.
4. Integrate issue #10 degraded-capacity semantics and issue #11 state integrity.
5. Implement issue #12 property tests and simulation receipts.
6. Implement issue #6 source-controlled SVG diagrams.
7. Reconstruct issue #3 reproducible full papers and PDFs.
8. Validate claims through issue #5 and related work through issue #9.
9. Inventory additional papers under issue #2.
10. Read the Site handoff and implement issue #1.
11. Release/tag only after reproducibility, security, review, validation, and artifact gates pass.
12. Execute issue #8 propagation assessment and receipts.

## Known blockers and cautions

- Full manuscripts are not complete.
- No general proof establishes the invariant.
- No executable BCAT state machine or property tests are committed.
- No defined incident corpus supports prevalence claims.
- State integrity, incentives, trust, auditability, and compute capacity are not integrated into one validated model.
- External review is unassigned.
- Public Site implementation is unassigned.
- Hosted validation evidence for issue #46 is pending direct observation.

## Ownership

- Research direction and authorship: Rigel Randolph
- Canonical repository continuation: StegScholar Governable Autonomy program
- Security/validation claim: `GA-SEC-001` until its release or expiration condition
- Formal model implementation: unassigned
- Artifact reconstruction: unassigned
- Site implementation: unassigned
- External peer review: unassigned

## Permitted continuation scope

A continuation lane may refine manuscripts and definitions; create state machines, simulations, tests, counterexamples, diagrams, reproducible builds, security evidence, and related-work records; inventory papers; implement the Site portal after reading its handoff; and update this handoff with committed evidence.

A continuation lane must not claim external endorsement, proof, empirical universality, conference readiness, federal authorization, compliance certification, workflow success without inspected evidence, or canonical status for conversation-only binaries.

## Archival condition

A session is archivable when its unique decisions, evidence, tasks, artifact status, ownership changes, and validation boundaries are committed here or in linked durable records; no session-specific mutation remains unverified; and any pending observation is assigned to a durable owner with a machine-observable release condition.
