# StegFinCo Budget Handoff Contract

## Authority

- Narrative and sponsor requirement owner: `StegVerse-Labs/StegScholar/funding/`
- Budget approval and financial execution owner: `StegVerse-Labs/StegFinCo`

## Required request payload

A budget request must identify:

- application ID and solicitation;
- deadline and project period;
- maximum sponsor amount;
- prohibited cost sharing or other sponsor limits;
- required experiential activities;
- personnel roles without inventing compensation or employment facts;
- travel, equipment, participant support, subaward, consultant, and indirect-cost assumptions;
- narrative-to-budget work-package mapping;
- unresolved registration or eligibility blockers;
- source commit for the application narrative.

## Required StegFinCo response

- status: `DRAFT`, `APPROVED`, `BLOCKED`, or `REJECTED`;
- direct-cost categories and amounts;
- indirect-cost basis;
- total request;
- budget justification reference;
- assumption and evidence list;
- approver and timestamp;
- immutable receipt or commit reference;
- reapproval trigger.

## Fail-closed rules

- StegScholar may draft planning figures but must not mark a budget `APPROVED`.
- Missing salary, fringe, indirect-rate, legal-entity, or project-period evidence must be explicit rather than estimated as fact.
- The NSF PESOSE total must not exceed USD 300,000 or one year.
- Voluntary committed cost sharing is prohibited.
- Mandatory I-Corps for PESOSE costs must be addressed using current NSF guidance.

## Canonical locations

Request:
`funding/applications/active/<APPLICATION-ID>-budget-request.json`

Response reference:
`StegVerse-Labs/StegFinCo/<canonical funding budget receipt>`

## Release condition

The application budget gate releases only after an approved StegFinCo response matches the current narrative revision and sponsor requirements.
