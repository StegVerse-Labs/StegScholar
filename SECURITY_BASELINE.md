# StegScholar Security Baseline

## Policy

Applicable United States federal security requirements are the minimum control floor for StegScholar. Repository, build, publication, review, and deployment controls must exceed that floor when stronger controls are feasible and proportionate.

This file defines engineering requirements. It does not claim that StegScholar, any paper, or any deployment is federally authorized, FISMA compliant, FedRAMP authorized, or independently certified.

## Minimum reference floor

The program must track and map applicable controls from:

- NIST SP 800-53 Rev. 5 control families;
- NIST SP 800-218 Secure Software Development Framework;
- FIPS 140-3 validated cryptographic modules where cryptographic protection is required in an applicable deployment;
- CISA Secure by Design principles;
- applicable privacy, records-retention, accessibility, export-control, procurement, and incident-reporting obligations for the actual deployment context.

Where requirements conflict, the stricter applicable control governs unless a documented legal or safety exception is approved by the authorized owner.

## Mandatory repository controls

1. **Fail closed.** Missing or invalid evidence, schemas, hashes, review records, ownership, or claims blocks release and publication.
2. **Least privilege.** Workflows receive only required permissions. Default workflow permissions are read-only.
3. **Protected provenance.** Canonical sources, generated artifacts, review records, and releases must identify the source revision and cryptographic hash.
4. **Reproducible generation.** Published PDFs and diagrams must be generated from committed sources using pinned or recorded dependencies.
5. **Separated authority.** Authorship, implementation, validation, peer review, release approval, and publication are distinct states and must not be inferred from one another.
6. **No silent success.** Validators must distinguish COMPLETE, BLOCKED, RETRY, REVIEW_REQUIRED, FAILED, CLAIMED, SUPERSEDED, and MERGED.
7. **Expiring claims.** Implementation, validation, and integration claims require collision boundaries and a release or expiration condition.
8. **Dependency integrity.** Third-party actions and dependencies must be version-pinned; immutable commit pinning is required for production workflows where practicable.
9. **Secret minimization.** No secrets, credentials, tokens, private keys, or sensitive personal data may be committed. Workflows must avoid secrets unless strictly required.
10. **Artifact integrity.** Release artifacts require SHA-256 hashes, source revision, generation receipt, and verification result.
11. **Review truthfulness.** Public comments, conceptual comparisons, citations, or social-media exchanges are not independent peer review or endorsement.
12. **Recovery authority.** Degraded or compromised systems may not self-expand authority without an independently authorized recovery basis.
13. **Security reporting.** Suspected vulnerabilities must be handled through a private reporting path before public disclosure when exploitation risk exists.
14. **Audit durability.** Control decisions and release evidence must be retained in repository-native records sufficient for independent reconstruction.

## Release gate

A release or public-paper promotion is prohibited unless:

- required source files exist;
- repository validation passes;
- generated artifacts have recorded hashes;
- review and claims states are valid;
- no conflicting active claim exists;
- known limitations and claims scope are present;
- security-impacting changes have a review record;
- the applicable mirror handoff is current;
- the release owner explicitly authorizes the transition.

## Required evidence classes

- source commit SHA;
- validator receipt;
- workflow run and job result when hosted validation is required;
- artifact SHA-256;
- review record identifiers;
- active or released task claim;
- release or publication authorization;
- propagation receipts for downstream repositories.

## Exceeding the floor

StegScholar additionally requires execution-boundary governance for publication and release: a proposed output cannot cross into a public or release state solely because its content exists. Evidence, authority, integrity, review state, and collision controls must be revalidated at the transition boundary.
