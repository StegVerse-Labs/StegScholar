# NSF PESOSE Public Product Evidence Crosswalk

## Decision posture

The current application does not yet have a submission-ready open-source product anchor.

## Candidate 1 — StegVerse-Labs/StegCore

- Public repository: yes.
- Defined role: commit-time allow, deny, or defer decision engine consuming continuity, action intent, policy, consent, and delegation evidence.
- Technical proof-anchor record: `StegVerse-Labs/StegCore/docs/STEGCORE_PROOF_ANCHOR_MIRROR_HANDOFF.md` identifies StegCore as the single technical proof anchor for StegVerse.
- Documented boundaries: yes.
- Public root license: not found during repository inspection on 2026-08-02.
- Runtime maturity: repository README states v0.1 is documentation-first and that code under `src/stegcore/` is scaffolding and substrate for future runtimes.
- Development/testing evidence: repository-local validators and workflows exist, but no complete PESOSE evidence package for a bounded product release, license, users, contributors, dissemination, or production adoption is installed.
- StegCore-side dependency record: `StegVerse-Labs/StegCore/docs/PESOSE_ANCHOR_PRODUCT_EVIDENCE_REQUEST.md`.
- StegCore-side executable task: issue `StegVerse-Labs/StegCore#47`, “Produce PESOSE anchor-product evidence manifest or record no-go.”
- Required completion artifact: `StegVerse-Labs/StegCore/evidence/pesose-anchor-product.json` or a committed `NO_GO`.
- PESOSE disposition: `BLOCKED`; StegCore is a candidate proof anchor but cannot be represented as the verified existing open-source product until issue #47 acceptance criteria are satisfied.

## Candidate 2 — StegVerse-Labs/StegTalk

- Public repository: yes.
- Defined role: device-agnostic secure communication layer across multiple transports.
- Public root license: not found during repository inspection on 2026-08-02.
- Runtime maturity: README is primarily architectural and aspirational; verified implementation, testing, release, user, and contributor evidence has not yet been established in this application record.
- PESOSE disposition: strong societal-need narrative, but currently weaker than StegCore as an inspectable technical transition anchor.

## Anchor decision

Retain StegCore only as the provisional candidate because NSF's 2026 Dear Colleague Letter encourages PESOSE proposals concerning protocols enabling AI-agent ecosystems. This does not waive the general PESOSE requirement for an existing publicly available open-source product, current development/testing details, dissemination methods, users, contributors, and third-party collaboration evidence.

The cross-repository transfer is now installed and inspectable. It does not release the anchor gate.

## Mandatory evidence before internal review

1. Install an approved public open-source license in the anchor repository and confirm its applicable product boundary.
2. Replace ambiguous scaffolding claims with an accurate implemented-component maturity inventory.
3. Identify the exact product artifact being transitioned, not the entire StegVerse vision.
4. Record an immutable release, deterministic tests, workflows, artifacts, reproducible execution instructions, and current limitations.
5. Record public dissemination channels.
6. Record verified independent users and contributors.
7. Obtain three to five letters from independent current users or contributors, as required by NSF 26-506.
8. Create a complete references-cited entry for the public product and matching inline citation.
9. Obtain maintainer and disclosure-authority approval of the sponsor-facing product description.

## Machine-observable release condition

This gate may advance only when one of the following appears:

- `StegVerse-Labs/StegCore/evidence/pesose-anchor-product.json` satisfying issue #47; or
- a committed StegCore `NO_GO` and a different candidate product with equivalent evidence.

## Fail-closed rule

The proposal must remain `DRAFTING` and may not enter `INTERNAL_REVIEW` while the anchor lacks a verified license, implemented product boundary, immutable release, operational evidence, dissemination evidence, independent user/contributor evidence, and at least three qualifying collaboration-letter commitments.
