# StegPatents Source Contract for Funding Applications

## Purpose

Define the only authorized path for using invention, patent, licensing, ownership, or disclosure-status information in StegScholar funding applications.

## Source authority

- Producer authority: `StegVerse-Labs/StegPatents`
- Consumer authority: `StegVerse-Labs/StegScholar/funding/`
- Consumer may summarize only records explicitly classified for the target application.

## Required source record

Each imported IP posture must provide:

- application ID;
- invention or portfolio identifier;
- ownership posture;
- filing posture;
- licensing posture;
- disclosure classification: `PUBLIC_APPROVED`, `APPLICATION_ONLY`, `REVIEW_REQUIRED`, or `PROHIBITED`;
- approved summary text or an explicit prohibition;
- approving authority;
- approval timestamp;
- source commit, immutable record, or receipt reference;
- expiration or re-review condition.

## Fail-closed rules

- Missing source evidence means `REVIEW_REQUIRED`.
- StegScholar must not infer patent status from repository names, drafts, conversations, or unpublished descriptions.
- `PROHIBITED` material must not enter application narratives, attachments, collaboration letters, public repositories, or downstream publication manifests.
- A changed application narrative requires renewed review when it materially changes protected technical disclosure.

## Output location

Application-specific reviews belong at:

`funding/applications/active/<APPLICATION-ID>-ip-review.json`

## Release condition

The PESOSE application IP gate is released only when StegPatents-authorized evidence identifies the exact reviewed narrative revision and permits its disclosure classification.
