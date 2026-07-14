# Governable Autonomy Artifact Manifest

## Status

This manifest tracks the canonical and generated artifacts for the StegScholar Governable Autonomy research program.

Current release status: **pre-release / reconstruction required**

## Canonical paper set

| ID | Title | Current status | Canonical source target | Generated artifact target |
|---|---|---|---|---|
| `GA-001` | Governance Invariant for Autonomous Systems | draft-concept | `papers/governance-invariant-for-autonomous-systems/manuscript.md` | `papers/governance-invariant-for-autonomous-systems/dist/` |
| `GA-002` | Survivable Governance | working-paper reconstruction | `papers/survivable-governance/manuscript.md` | `papers/survivable-governance/dist/` |
| `GA-003` | Formal Model Sketch: Survivable Governance Under Epistemic Constraint | working-paper reconstruction | `papers/survivable-governance-formal-model/manuscript.md` | `papers/survivable-governance-formal-model/dist/` |
| `GA-004` | Trust-Bounded Socio-Technical Systems: Architectural Primitives for Auditability and Failure | working-paper reconstruction | `papers/trust-bounded-socio-technical-systems/manuscript.md` | `papers/trust-bounded-socio-technical-systems/dist/` |
| `GA-005` | Ghost Credentials and Phantom Trust | working-paper reconstruction | `papers/ghost-credentials-and-phantom-trust/manuscript.md` | `papers/ghost-credentials-and-phantom-trust/dist/` |
| `GA-006` | Boundary-Condition Autonomy | working-paper reconstruction | `papers/boundary-condition-autonomy/manuscript.md` | `papers/boundary-condition-autonomy/dist/` |

No target path listed above is authoritative until the corresponding file is committed and linked here with its content hash.

## Required shared diagrams

| ID | Diagram | Source target | Classification | Status |
|---|---|---|---|---|
| `GA-FIG-001` | Governable Autonomy Stack | `figures/governable-autonomy/governable-autonomy-stack.svg` | normative architecture proposal | not committed |
| `GA-FIG-002` | Epistemic degradation and authority contraction | `figures/governable-autonomy/epistemic-authority-contraction.svg` | proposed safety behavior | not committed |
| `GA-FIG-003` | Execution gateway between complex autonomy and reality | `figures/governable-autonomy/execution-gateway.svg` | conceptual architecture | not committed |
| `GA-FIG-004` | State-transition / irreversibility boundary | `figures/governable-autonomy/state-transition-boundary.svg` | related-work-aware conceptual model | not committed |
| `GA-FIG-005` | Paper contribution map | `figures/governable-autonomy/paper-contribution-map.svg` | program index | not committed |

Each diagram must include an accessible text alternative and must state whether it is descriptive, normative, or hypothesized.

## Conversation-runtime artifacts

The following files were generated in a prior conversation runtime:

| Artifact | Runtime path/name | Authority status | Reason |
|---|---|---|---|
| v1 bundle | `stegscholar_v1_bundle.zip` | non-authoritative | sources, exact contents, hashes, and reproducible build were not committed |
| v2 bundle | `stegscholar_v2_system_papers.zip` | non-authoritative | papers were abbreviated system-style drafts; sources and build were not committed |

These files may be used only as referential reconstruction aids while available. They must not be published as canonical StegScholar papers, tagged as a release, or described as conference-ready.

## Reproducibility requirements

A paper becomes a canonical generated artifact only when all of the following exist:

1. committed manuscript source;
2. committed bibliography or explicit statement that no bibliography is yet present;
3. committed figure sources;
4. documented build command and dependency versions;
5. generated PDF from the committed source;
6. SHA-256 hash for the generated PDF;
7. paper identifier, title, author, version, date, claims scope, status, and limitations;
8. review-state record distinguishing feedback from independent peer review;
9. successful verification that the generated artifact corresponds to the recorded source revision.

## Candidate build layout

```text
research-programs/governable-autonomy/
  README.md
  ARTIFACT_MANIFEST.md
  paper-registry.json
  review-schema.json

papers/<paper-id>/
  manuscript.md or manuscript.tex
  references.bib
  figures/
  build/
  dist/
  STATUS.md

figures/governable-autonomy/
  *.svg
  *.md
```

The layout is provisional until issue #13 and issue #20 are resolved.

## Review-state discipline

Permitted review-state values are proposed as:

- `none`
- `feedback-invited`
- `comments-received`
- `revision-in-progress`
- `independently-reviewed`
- `replicated`
- `venue-submitted`
- `venue-accepted`

Public comments, LinkedIn responses, conceptual comparisons, and references to related work must not be labeled `independently-reviewed` unless a durable review record and reviewer scope support that claim.

## Current verification status

- Canonical manuscript reconstruction: not complete
- Diagram reconstruction: not complete
- Reproducible build: not complete
- Generated hashes: unavailable
- Invariant proof: unavailable
- Executable reference model: unavailable
- Incident-corpus validation: unavailable
- External peer review: unassigned
- Public portal: tracked by issue #1

## Linked work

- Handoff: `STEGSCHOLAR_GOVERNABLE_AUTONOMY_MIRROR_HANDOFF.md`
- Public portal: #1
- Additional paper inventory: #2
- Artifact reconstruction: #3
- Review/status model: #4
- Incident validation: #5
- Diagram sources: #6
- BCAT formal model: #7
- Release cross-updates: #8
- Related-work verification: #9
- Compute/degraded capacity: #10
- State integrity: #11
- Property tests: #12
- Program index/taxonomy: #13
- Archival criteria: #14
- Implementation sequence: #15
- Handoff creation: #16
- Manifest creation: #17
- Paper registry: #18
- Handoff/manifest verification: #19
- Source directories: #20

## Ownership

- Research direction and authorship: Rigel Randolph
- Manifest maintenance: StegScholar continuation sessions
- Artifact reconstruction: unassigned
- Build verification: unassigned
- External review: unassigned

## Release gate

No Governable Autonomy release or tag should be created until canonical sources, reproducible artifacts, claims scope, review status, and hashes are committed and verified. At release readiness, issue #8 governs checks for `StegVerse-Labs/Site`, `GCAT-BCAT-Engine/Publisher`, `admissibility-wiki`, and `stegguardian-wiki`.
