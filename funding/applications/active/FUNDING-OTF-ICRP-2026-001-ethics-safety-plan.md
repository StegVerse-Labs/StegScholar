# OTF ICRP Ethics and Safety Plan

Application ID: `FUNDING-OTF-ICRP-2026-001`

State: `DRAFTING — FIELD ACTIVITY PROHIBITED`

## Scope boundary

The initial research phase is limited to synthetic traffic, controlled infrastructure, public documentation, and authorized test environments. It will not collect message content, covertly observe users, probe third-party systems without authorization, or conduct field activity involving vulnerable participants.

## Risk classes

1. Re-identification through timestamps, routes, identifiers, locations, or relationship patterns.
2. Operational-security harm caused by revealing measurement methods or affected infrastructure.
3. Retaliation or legal risk to practitioners, participants, or local partners.
4. Dual-use publication of exploit-enabling or censorship-evasion details.
5. False classification of censorship, shutdowns, or compromise.
6. Scope drift from research instrumentation into surveillance capability.

## Required controls

- Synthetic-first development and validation.
- Explicit collection authority and purpose limitation.
- No message-content collection.
- Data minimization and coarse timing/location fields by default.
- No persistent user or device identifiers unless independently justified and approved.
- Separate observed events from inferred classifications and confidence.
- Defined retention, deletion, withdrawal, and breach-response procedures.
- Restricted review of sensitive findings before publication.
- Independent practitioner and affected-community review before any field-oriented activity.
- Stop-work authority for evidence of participant, partner, or community harm.

## Field-activity release gate

Field activity remains prohibited until all of the following exist:

- named qualified ethical reviewer or recognized review pathway;
- written protocol and threat model;
- participant recruitment and consent materials where applicable;
- data-protection and incident-response plan;
- partner duty-of-care assessment;
- explicit applicant authorization;
- documented stop conditions and escalation owner.

## Machine-observable states

- `SYNTHETIC_ONLY`: repository and controlled-environment work permitted.
- `REVIEW_REQUIRED`: proposed participant or field activity exists but approval is absent.
- `APPROVED_FIELD_ACTIVITY`: all release-gate evidence is committed or referenced.
- `STOP_WORK`: credible harm, breach, coercion, or scope violation is detected.

Current state: `SYNTHETIC_ONLY`.
