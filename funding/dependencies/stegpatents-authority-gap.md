# StegPatents Authority Dependency Gap

## Application

`FUNDING-NSF-PESOSE-2026-001`

## Observation

No connected or discoverable repository named `StegVerse-Labs/StegPatents` was found during the 2026-08-02 funding integration pass.

The existing StegScholar contract names StegPatents as the intended protected-disclosure and IP-classification authority, but no repository-native handoff, task registry, or application-specific response location can currently be installed there.

## State

- Task: `FUNDING-PESOSE-IP-AUTHORITY-007`
- State: `BLOCKED`
- Owner: human IP authority or the future canonical StegPatents repository
- Current authority surface: this dependency record plus `funding/contracts/stegpatents-source-contract.md`
- Release condition: either:
  1. the canonical StegPatents repository becomes connected and an application-specific disclosure-review record is committed there; or
  2. a named human IP authority commits a disclosure classification in an approved durable repository location.

## Prohibitions

- Do not infer that a repository exists because the authority name appears in a contract.
- Do not treat absence of a patent filing as permission to publish technical details.
- Do not move protected-disclosure authority into StegScholar.
- Do not mark the application `SUBMISSION_READY` while disclosure classification remains unresolved.

## Required response fields

- application ID;
- reviewed files and commit SHAs;
- inventions or disclosures implicated;
- publication-safe, disclosure-review-required, restricted, or blocked classification;
- redactions or substitutions required;
- reviewer identity and authority;
- review timestamp;
- evidence references.

## Canonical continuation

`StegVerse-Labs/StegScholar/funding/coordination/funding-tasks.json`
