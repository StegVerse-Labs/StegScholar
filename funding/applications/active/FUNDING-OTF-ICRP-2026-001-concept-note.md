# OTF ICRP 2026 Concept Note

## Application control

- Application ID: `FUNDING-OTF-ICRP-2026-001`
- Program: Open Technology Fund Information Controls Research Program
- Deadline: 2026-09-07 at 23:59 GMT
- State: `DRAFTING — NOT SUBMISSION READY`
- Applicant posture: individual researcher pathway under review
- Host organization: not selected; required only if invited to Stage 2

## Working title

**Governed Evidence for Shutdown-Resilient and Censored Communication Environments**

## Research problem

People operating in information-restricted environments need ways to determine whether communication failures result from ordinary connectivity problems, deliberate filtering, shutdown interference, platform restrictions, compromised infrastructure or security attacks. Existing diagnostic methods can expose message content, user identities, location, social relationships or operational patterns. These risks are especially serious for journalists, civil-society organizations, human-rights defenders and communities facing targeted surveillance.

The proposed research will investigate whether minimal, privacy-preserving evidence records can support useful analysis of censored or shutdown-resilient communications without creating a new surveillance surface. It will focus on observable technical events such as transport availability, delivery-state transitions, integrity failures, route changes, timing classes and recovery behavior while excluding message content and unnecessary personal data.

## Research questions

1. Which technical observations are sufficient to distinguish likely censorship, shutdown interference, infrastructure failure and application-layer security failure without collecting message content?
2. How can observations be transformed into minimal evidence records with explicit provenance, uncertainty and retention boundaries?
3. Can independent reviewers reconstruct the basis for a classification without receiving sensitive user data?
4. Which evidence fields create unacceptable re-identification, location, relationship or operational-security risks?
5. How should tools fail closed when consent, safety, provenance or independent verification is unavailable?

## Proposed methods

### Threat and evidence model

Develop a threat model covering state-sponsored filtering, internet shutdowns, selective throttling, DNS and routing interference, platform blocking, malicious relays, compromised clients, metadata exposure and coercive access to collected evidence.

Define a candidate evidence vocabulary that separates:

- directly observed events;
- inferred classifications;
- confidence and uncertainty;
- collection authority and consent;
- provenance and transformation history;
- retention and deletion requirements;
- safe export and disclosure classes.

### Controlled experiments

Use synthetic traffic and controlled test environments rather than real vulnerable-user communications during initial development. Reproduce selected interference patterns such as blocked endpoints, dropped transports, altered DNS responses, throttling, delayed delivery, integrity failures and intermittent shutdown conditions.

Evaluate whether the evidence vocabulary supports accurate differentiation while minimizing collected data.

### Privacy and safety evaluation

Test candidate records for content leakage, linkability, location inference, relationship inference, persistent identifiers and operational-pattern disclosure. Remove or coarsen fields that are not necessary for the intended analysis.

Conduct structured review with internet-freedom, digital-security and affected-community experts before any field-oriented testing. No real-user collection will occur without an approved ethical and safety protocol.

### Prototype and reproducibility package

Produce a research prototype that converts controlled observations into minimal evidence records and a verifier that checks schema validity, provenance, consent state, prohibited fields and classification support.

Publish synthetic datasets, test scenarios and documentation where disclosure review permits. Sensitive threat details or exploit-enabling material will be withheld or shared through an appropriate restricted process.

## Expected outputs

1. Threat model for evidence collection in censored and shutdown-resilient communications.
2. Minimal privacy-preserving evidence schema.
3. Synthetic interference and failure dataset.
4. Open research prototype and deterministic verifier.
5. Evaluation report covering classification usefulness, false positives, privacy leakage and safety limitations.
6. Practitioner guide for safe evidence collection, export, retention and deletion.
7. Recommendations for interoperability with existing internet-freedom monitoring and shutdown-resilience tools.

## Relevance to internet freedom

The work is intended to help internet-freedom practitioners and affected communities understand communication interference and security failures while reducing the risk that diagnostic data becomes a tool for surveillance or retaliation. The technical outputs could support safer incident triage, comparison across tools and environments, reproducible research and privacy-preserving collaboration between local practitioners and external experts.

The project is not a general secure-messaging commercialization effort. Its scope is limited to censorship, shutdown, surveillance and digital-threat research in information-restricted environments.

## Ethical safeguards

- No collection of message content.
- No covert measurement of users or networks.
- No testing against third-party systems without authorization.
- Synthetic and controlled data first.
- Explicit consent and withdrawal controls for any later participant research.
- Data minimization, retention limits and deletion procedures.
- Risk review before publishing threat details or tooling.
- Stop conditions for evidence of participant, partner or community harm.

## Applicant and host posture

The Stage 1 applicant may use the individual researcher pathway. Before submission, the record must include:

- applicant identity and contact details;
- relevant technical, research and internet-freedom experience;
- work-authorization and sanctions/debarment eligibility where applicable;
- conflict-of-interest declaration;
- confirmation that neither applicant nor proposed host develops or markets surveillance technology;
- realistic full-time availability or a justified project-duration model.

A host organization will be sought only if the concept note is invited to Stage 2. The host must be independent of the applicant’s existing affiliation where OTF rules require it and must have appropriate internet-freedom, research, financial and duty-of-care capacity.

## Current evidence gaps

- named applicant and CV;
- demonstrated internet-freedom or affected-environment experience;
- host-organization candidates;
- technical feasibility evidence from a controlled prototype;
- ethical-review and field-testing pathway;
- project duration, monthly milestones and budget;
- protected-disclosure classification;
- partner or practitioner letters.

## Submission prohibition

This concept note must not be submitted until the applicant identity, experience, eligibility, ethical posture and disclosure review are supported by inspectable evidence. The existence of StegVerse repositories does not itself establish applicant qualifications, internet-freedom impact or OTF eligibility.
