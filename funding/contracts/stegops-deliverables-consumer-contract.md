# StegOps-Deliverables Funding Consumer Contract

## Purpose

Define the transition from an awarded funding record in StegScholar to sponsor-deliverable scheduling and closeout custody in `StegVerse-Labs/StegOps-Deliverables`.

## Activation condition

This contract is inactive until an application state is `AWARDED` and award evidence is directly inspectable.

## Required outbound award manifest

- application and award IDs;
- sponsor and program;
- award notice reference;
- approved project period and budget reference;
- required technical, financial, data, security, and closeout reports;
- due dates and recurrence;
- responsible repositories and human authority boundaries;
- publication and disclosure classifications;
- source commits and immutable evidence references;
- amendment and termination handling;
- next executable deliverable.

## Consumer obligations

StegOps-Deliverables must:

- create a deterministic deliverable registry;
- persist state and receipts;
- distinguish `NOT_DUE`, `DRAFTING`, `REVIEW_REQUIRED`, `SUBMISSION_READY`, `SUBMITTED`, `ACCEPTED`, `REJECTED`, `BLOCKED`, and `SUPERSEDED`;
- prevent duplicate submissions;
- preserve sponsor acknowledgments;
- route financial reports to StegFinCo authority;
- route protected disclosures to StegPatents authority;
- fail closed when award terms or evidence are missing.

## Prohibitions

- An application submission is not an award.
- A public announcement is not award authority.
- StegScholar must not activate post-award tasks from an expected or verbal award.
- No propagation to Site, Publisher, admissibility-wiki, stegguardian-wiki, or master-records occurs without the applicable publication or custody classification.

## Release condition

The contract activates only after the award notice, approved budget, project period, reporting terms, and disclosure classification are validated and referenced in a committed outbound manifest.
