# StegScholar Governable Autonomy Mirror Handoff

## Repository and canonical scope

- Organization/repository: `StegVerse-Labs/StegScholar`
- Branch: `main`
- Program: `research-programs/governable-autonomy/`
- Papers: `papers/`
- Figures: `figures/governable-autonomy/`
- Canonical task lane: issues #1-#12 and #46

This is the authoritative continuation record for the **Governable Autonomy** program. It does not replace `STEGSCHOLAR_MIRROR_HANDOFF.md` for Recoverability Geometry / Rigel Number work or scoped handoffs under `docs/` and `funding/`.

The program is a candidate systems-governance architecture. Its claims remain conceptual or formal hypotheses until supported by proofs, executable models, simulations, incident studies, independent review, or empirical validation.

## Originating session goal

Create a public, peer-reviewable StegScholar program for the governance papers; formalize Boundary-Condition Autonomy as the execution gateway between complex autonomy and external reality; preserve additional paper candidates; generate reproducible papers and diagrams; and make applicable federal security requirements the minimum rather than the target ceiling.

## Current paper set

- `GA-001` — *Governance Invariant for Autonomous Systems*
- `GA-002` — *Survivable Governance*
- `GA-003` — *Formal Model Sketch: Survivable Governance Under Epistemic Constraint*
- `GA-004` — *Trust-Bounded Socio-Technical Systems: Architectural Primitives for Auditability and Failure*
- `GA-005` — *Ghost Credentials and Phantom Trust*
- `GA-006` — *Boundary-Condition Autonomy*

## Durable conceptual decisions

1. Trust is mutable system state.
2. Audit status, including irrecoverable audit loss, is operational state.
3. Credential validity is distinct from continuing authority justification.
4. Autonomy is a revocable execution mode governed by enforceable boundary conditions.
5. Binding governance occurs at the state-transition boundary where an action commits external or system state.
6. BCAT is the gateway between complex autonomy and reality: autonomous components propose; the execution control plane decides whether a proposal may cross the boundary.
7. As epistemic support, state integrity, incentive alignment, verification capacity, or enforcement capacity deteriorates, the permitted action set should contract rather than persist by inheritance.
8. At critical degradation, execution may become binary: `ALLOW/DENY` or `CONTINUE/PAUSE`.
9. Proposed invariant: **If epistemic certainty decreases, execution authority must not expand.**
10. The scalar form `E(t+1) < E(t) => A(t+1) <= A(t)` is provisional; a set-based authority model is expected to handle emergency classes more accurately.
11. The architecture bounds execution; it does not solve alignment, ethics, semantic correctness, or global optimization.
12. Absolute compute availability cannot be guaranteed. The model must define degraded-capacity behavior, minimum enforcement capacity where feasible, fail-safe thresholds, and authorized recovery.
13. State integrity may require `I in {Trusted, Degraded, Compromised}`; that extension is not yet settled.

## Unified model

```text
Trust state
    -> Auditability
    -> Credential legitimacy
    -> Boundary enforcement
    -> Execution authority at commit
    -> External or system reality
```

Normative degraded-state progression:

```text
Open -> Constrained -> Revoked
```

## Federal-floor-plus security decision

Applicable United States federal security requirements are the minimum control floor. StegScholar must exceed that floor where stronger controls are feasible and proportionate.

Canonical policy: `SECURITY_BASELINE.md`

The baseline references NIST SP 800-53 Rev. 5 control families, NIST SP 800-218 SSDF, FIPS 140-3 validated cryptography where applicable, and CISA Secure by Design principles. It does not claim FISMA compliance, FedRAMP authorization, certification, federal approval, or deployment authorization.

Required controls include fail-closed validation, least privilege, source/artifact provenance, reproducible generation, separated authority states, expiring collision-controlled claims, dependency integrity, secret minimization, hashes, truthful review status, recovery authority, private vulnerability handling, and durable audit evidence.

## Completed durable infrastructure

- `research-programs/governable-autonomy/README.md`
- `research-programs/governable-autonomy/ARTIFACT_MANIFEST.md`
- `research-programs/governable-autonomy/paper-registry.json`
- canonical manuscript scaffolds for `GA-001` through `GA-006`
- `figures/governable-autonomy/README.md`
- `SECURITY_BASELINE.md`
- `research-programs/governable-autonomy/review-schema.json`
- `research-programs/governable-autonomy/task-claims.json`
- `tools/validate_governable_autonomy.py`
- `.github/workflows/governable-autonomy-validate.yml`
- `research-programs/governable-autonomy/receipts/GA-SEC-001-installation.json`

## Security/validation claim

- Task: `GA-SEC-001`
- Issue: #46
- State: `MACHINE_OWNED`
- Owner: `github-actions:governable-autonomy-validate`
- Role: validation
- Claim registry: `research-programs/governable-autonomy/task-claims.json`
- Claim created: `2026-08-02T22:49:51Z`
- Claim expires: `2026-08-04T22:49:51Z`
- Collision boundary: security baseline, review schema, claim registry, validator, validation workflow, this handoff, and the installation receipt only
- Excluded scopes: `funding/`, Recoverability Geometry / Rigel Number, and unrelated handoffs
- Release condition: inspect a successful hosted workflow run, validate job and decoded logs, inspect the uploaded `COMPLETE` receipt artifact, update issue #46, and mark the claim `COMPLETE` or release it
- Expiration policy: if evidence is unavailable at expiration, mark `BLOCKED` and create a new explicit validation claim; do not silently extend or infer success

## Validation evidence

### Proven

- The security policy, review schema, claim registry, validator, workflow, canonical handoff, and installation receipt were committed to `main`.
- The review schema fails closed on undeclared fields and restricts independent-review and replication state claims.
- The claim registry defines allowed states, an expiration, expected evidence, collision boundaries, and a next task.
- The workflow uses read-only repository permission, disables persisted checkout credentials, has a five-minute timeout, runs the fail-closed validator, verifies the receipt result, and requires artifact upload.
- Installation receipt: `research-programs/governable-autonomy/receipts/GA-SEC-001-installation.json` with result `REVIEW_REQUIRED`.

### Pending machine observation

- A successful hosted workflow run has not been directly observed.
- No validate-job conclusion, decoded log, or uploaded workflow receipt has been inspected.
- The commit-run connector returned no observable run for workflow commit `58c34a225953c2b363828b6fc2900595bd005f48`.
- Therefore workflow success is not claimed. Issue #46 remains open and the repository workflow owns observation.

## External discussion provenance

A public LinkedIn discussion with Saida Harle sharpened the framing around operational pressure, constraint reconciliation, state integrity, and authority at state transitions. Saida referenced Dr. Masayuki Otani's ARETABA/MGAG work and a point of irreversibility described as `T(e)`.

These are related-work and conceptual-provenance inputs, not peer review, endorsement, validation, or proof of equivalence. Primary sources and exact definitions must be verified before public citation or comparison. See issue #9.

## Artifact status

Conversation-runtime bundles `stegscholar_v1_bundle.zip` and `stegscholar_v2_system_papers.zip` are non-authoritative reconstruction aids. They are not release artifacts or conference-ready papers because canonical binary hashes and reproducible source-to-artifact receipts were not committed. See issue #3.

## Public peer-review portal decision

StegScholar requires a public research and peer-review section on StegVerse.org that distinguishes stable papers, working papers, draft concepts, research notes, diagrams/models, validation artifacts, and superseded/merged work.

Each paper page must expose version, maturity, review state, claims scope, canonical source, artifact hashes, limitations, citation guidance, and a durable feedback path. `stable-paper` means internally version-stable, not independently reviewed. Site implementation must read `StegVerse-Labs/Site/docs/SITE_MIRROR_HANDOFF.md` before mutation. See issue #1.

## Durable execution inventory

| Task | Durable location | State | Canonical owner | Next executable action |
|---|---|---|---|---|
| Security baseline and validation | issue #46; `GA-SEC-001` | MACHINE_OWNED | validation workflow | inspect run/job/log/artifact or mark BLOCKED at expiration |
| Review evidence/status model | issue #4; `review-schema.json` | PARTIAL | StegScholar issue lane | add valid sample record and portal consumer contract |
| BCAT execution-boundary model | issue #7 | UNCLAIMED | StegScholar issue lane | state variables, transition relation, recovery and executable model |
| Compute-floor semantics | issue #10 | UNCLAIMED | StegScholar issue lane | define proposal, verification, enforcement, and recovery capacity |
| State-integrity model | issue #11 | UNCLAIMED | StegScholar issue lane | independence analysis, transition table, recovery authority |
| Authority-contraction tests | issue #12 | BLOCKED | StegScholar issue lane | activates after #7/#10/#11 formalization |
| Diagrams | issue #6 | UNCLAIMED | StegScholar issue lane | source-controlled SVGs and text alternatives |
| Reproducible papers/PDFs | issue #3 | BLOCKED | StegScholar issue lane | complete manuscripts, builds, diagrams, hashes, receipts |
| Failure-case validation | issue #5 | UNCLAIMED | StegScholar issue lane | define corpus and reproducible coding method |
| Related work | issue #9 | UNCLAIMED | StegScholar issue lane | verify primary ARETABA/MGAG sources |
| Additional paper inventory | issue #2 | UNCLAIMED | StegScholar issue lane | create durable candidate inventory |
| Public portal | issue #1; future Site task | BLOCKED | Site integration lane | read Site handoff and consume canonical registry/schema |
| Release propagation | issue #8 | BLOCKED | release integration lane | activate only after release gate passes |

Completed issues: #13, #14, #15, #16, #17, #18, #19, and #20.

## Cross-repository propagation obligations

At release readiness, issue #8 governs applicability and propagation checks for:

- `StegVerse-Labs/Site`
- `GCAT-BCAT-Engine/Publisher`
- `admissibility-wiki`
- `stegguardian-wiki`
- any master-records or publication-custody target identified by current contracts

No propagation, deployment, runtime publication, release, or governed activation is currently claimed.

## Next sequence

1. Repository workflow resolves or blocks `GA-SEC-001`.
2. Issue #4 adds a valid sample review record and portal-consumer contract.
3. Issue #7 formalizes the execution boundary.
4. Issues #10 and #11 integrate degraded capacity and state integrity.
5. Issue #12 adds executable property tests and receipts.
6. Issue #6 creates publication-quality source diagrams.
7. Issue #3 reconstructs reproducible full papers and PDFs.
8. Issues #5 and #9 validate claims and related work.
9. Issue #2 inventories other paper candidates.
10. Issue #1 implements the portal after reading the Site handoff.
11. Release/tag only after reproducibility, security, review, validation, and artifact gates pass.
12. Issue #8 performs downstream applicability, propagation, and receipt verification.

## Known blockers

- Full manuscripts are incomplete.
- No general proof establishes the invariant.
- No executable BCAT model or property tests are committed.
- No incident corpus supports prevalence claims.
- Trust, auditability, state integrity, incentives, and compute capacity are not integrated into one validated model.
- External review is unassigned.
- Hosted validation evidence for issue #46 remains pending under the machine-owned claim.

## Ownership and permitted continuation

- Research direction and authorship: Rigel Randolph
- Canonical continuation: StegScholar Governable Autonomy program
- Current validation owner: repository workflow under `GA-SEC-001`
- Remaining formalization, artifact, review, and portal work: linked issue lanes

Continuation lanes may refine manuscripts and definitions; create state machines, simulations, property tests, counterexamples, diagrams, reproducible builds, security evidence, and related-work records; inventory papers; implement the Site portal after reading its handoff; and update this record with committed evidence.

They must not claim external endorsement, proof, empirical universality, conference readiness, federal authorization/certification, workflow success without inspected evidence, or canonical status for conversation-only binaries.

## Session consolidation and archival condition

Unique decisions, implementation evidence, task ownership, collision boundaries, validation gaps, and next actions from the originating session are now durable in this handoff, issues, claims registry, installation receipt, and workflow.

A session may archive when it has no unreleased session-owned claim or undocumented mutation. Pending workflow observation does not require retaining the originating chat because it is machine-owned, expiring, and has a fail-closed release condition in repository records.
