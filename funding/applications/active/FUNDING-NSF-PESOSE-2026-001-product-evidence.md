# NSF PESOSE Public Product Evidence Crosswalk

## Decision posture

The current application does not yet have a submission-ready open-source product anchor.

## Candidate 1 — StegVerse-Labs/StegCore

- Public repository: yes.
- Defined role: commit-time allow, deny, or defer decision engine consuming continuity, action intent, policy, consent, and delegation evidence.
- Documented boundaries: yes.
- Public root license: not found during repository inspection on 2026-08-02.
- Runtime maturity: repository README states v0.1 is documentation-first and that code under `src/stegcore/` is scaffolding and substrate for future runtimes.
- Development/testing evidence: some repository-local validators are documented, but no complete PESOSE evidence package for users, contributors, releases, dissemination, or production adoption is installed.
- PESOSE disposition: promising technical anchor, but currently `REVIEW_REQUIRED`; cannot be represented as a robust transitioned open-source product without licensing and maturity corrections.

## Candidate 2 — StegVerse-Labs/StegTalk

- Public repository: yes.
- Defined role: device-agnostic secure communication layer across multiple transports.
- Public root license: not found during repository inspection on 2026-08-02.
- Runtime maturity: README is primarily architectural and aspirational; verified implementation, testing, release, user, and contributor evidence has not yet been established in this application record.
- PESOSE disposition: strong societal-need narrative, but currently weaker than StegCore as an inspectable technical transition anchor.

## Anchor decision

Retain StegCore as the provisional anchor because NSF's 2026 Dear Colleague Letter explicitly encourages PESOSE proposals concerning protocols enabling AI-agent ecosystems. This does not waive the general PESOSE requirement for an existing publicly available open-source product, current development/testing details, dissemination methods, users, contributors, and third-party collaboration evidence.

## Mandatory evidence before internal review

1. Install or identify an approved public open-source license in the anchor repository.
2. Replace ambiguous scaffolding claims with an accurate component maturity inventory.
3. Identify the exact product artifact being transitioned, not the entire StegVerse vision.
4. Record deterministic tests, workflows, release artifacts, and current limitations.
5. Record dissemination channels.
6. Record verified users and contributors.
7. Obtain three to five letters from independent current users or contributors, as required by NSF 26-506.
8. Create a references-cited entry for the public repository because URLs may not appear directly in the Project Description.

## Fail-closed rule

The proposal must remain `DRAFTING` and may not enter `INTERNAL_REVIEW` while the anchor lacks a verified license, product boundary, development/testing evidence, dissemination evidence, user/contributor evidence, and at least three qualifying collaboration-letter commitments.
