# PESOSE: Track 1: Governed Open-Source Infrastructure for Recoverable AI Agent and Secure Communication Ecosystems

> Application ID: `FUNDING-NSF-PESOSE-2026-001`  
> State: `DRAFTING — NOT SUBMISSION READY`  
> Document role: solicitation-limited Project Description source draft  
> Submission prohibition: unresolved applicant, product-license, adoption, collaboration-letter, IP-review, and budget-approval gates remain controlling.

## 1. Vision and motivating need

AI agents increasingly influence consequential software, communications, financial, research, and public-service operations. Existing systems can often show that an instruction was approved or that an action occurred, but they do not necessarily establish that execution authority remained valid at commit time, that policy and delegation were reconstructable, that evidence remained attributable across transitions, or that operator authority could be safely recovered after degradation.

StegVerse is an emerging family of open protocols, validators, evidence formats, reference implementations, and governance controls directed at this problem. Its research and engineering work distinguishes approval from continuity, execution from admissibility, replayability from reconstructability, and local boundary enforcement from recoverable authority. Related components address governed agents, secure communications, deterministic refusal, provenance-preserving ingestion, transition receipts, and cross-repository evidence custody.

This Track 1 planning project will determine whether those distributed artifacts can support a secure, sustainable, broadly useful open-source ecosystem. It will not presume that current repositories constitute a mature ecosystem or that broad adoption already exists. Instead, the project will test those assumptions, identify a defensible canonical product boundary, and produce the organizational, governance, licensing, security, privacy, community, and sustainability plans required for a later transition effort.

## 2. Existing product and proposed ecosystem boundary

The provisional transition anchor is `StegVerse-Labs/StegCore`, supported by related StegVerse components for agents, communications, identity and continuity evidence, research validation, ingestion, and admissibility. The final anchor decision is itself a Track 1 planning question because current evidence identifies unresolved license, implementation-maturity, dissemination, user, and contributor gaps.

The proposed ecosystem is therefore defined functionally rather than by an unsupported maturity claim. Its intended shared layer consists of:

1. machine-readable authority, policy, delegation, and transition records;
2. deterministic validation and fail-closed execution gates;
3. continuity, admissibility, provenance, and reconstructability evidence;
4. interoperable secure-communication and governed-agent protocols;
5. contribution, release, incident-response, and succession controls;
6. reference implementations and conformance tests that permit independent implementation.

During Track 1, the team will determine which components belong in the canonical product, which remain research artifacts, which should become independent projects, and which should be retired or excluded.

## 3. Ecosystem discovery and validation

The project will conduct structured discovery with prospective users, contributors, maintainers, validators, educators, public-interest organizations, researchers, companies, and government stakeholders working in AI safety, cybersecurity, secure communications, digital rights, research infrastructure, and regulated operations.

Discovery will test specific hypotheses:

- users need execution evidence that distinguishes approval from admissibility;
- implementers need interoperable formats for authority, provenance, and transition validation;
- security-sensitive adopters require fail-closed behavior when evidence is missing or authority cannot be reconstructed;
- independent contributors require bounded roles and transparent decision rights rather than informal repository access;
- a shared open protocol layer can provide more public value than a single proprietary implementation.

Evidence will be collected through interviews, workshops, technical demonstrations, integration exercises, issue and contribution analysis, and documented external implementation attempts. Each hypothesis will receive an explicit outcome of supported, unsupported, inconclusive, or revised. The project will also establish go/no-go criteria for a later Track 2 effort.

## 4. Governance and managing organization

The planning effort will design a managing-organization model that separates powers that are frequently conflated in open-source projects. The model will distinguish research authority, implementation authority, validation authority, release authority, protected-disclosure authority, financial authority, publication authority, and post-award deliverables authority.

Planned governance work includes:

- contributor and maintainer role definitions;
- decision-rights and escalation matrices;
- proposal, review, refusal, appeal, and override procedures;
- conflict-of-interest and recusal controls;
- release and emergency-response authority;
- succession, maintainer continuity, and stale-claim expiration;
- transparent roadmapping and collision prevention;
- evidence requirements for decisions affecting security or compatibility;
- procedures for superseding obsolete artifacts without losing provenance.

The resulting design will be evaluated against practical scenarios such as compromised maintainers, conflicting implementations, urgent security fixes, authority degradation, abandoned dependencies, and disputes over compatibility or disclosure.

## 5. Licensing and intellectual-property boundaries

Track 1 will determine an open-source licensing and contribution model that supports broad implementation while preserving lawful treatment of protected inventions and third-party materials. The project will compare permissive, reciprocal, and protocol-oriented licensing approaches; contributor licensing or developer certificate mechanisms; trademark and compatibility-mark policies; and patent or defensive-publication strategies.

No proposal text will represent a governing license as established until the canonical product has an inspectable license and the application receives an authorized disclosure classification. The planning output will identify what can be openly published, what requires review, what should be separated into reference and protected layers, and how independent implementers can receive clear rights without depending on private interpretation.

## 6. Security, privacy, and supply-chain planning

The ecosystem security plan will address source code, models, workflows, registries, build systems, packages, ingestion bundles, validators, documentation, and release artifacts. The team will develop threat models and controls for:

- malicious or compromised contributors;
- poisoned dependencies and model supply chains;
- forged or incomplete evidence;
- authority or policy drift between review and execution;
- replay without reconstructability;
- privacy leakage through logs, metadata, or retained evidence;
- compromised signing or release infrastructure;
- denial of service against validation paths;
- unsafe fallback behavior when required evidence is unavailable.

Planning outputs will define identity, signing, hashing, provenance, chain-of-custody, reproducible validation, release verification, rollback, incident response, recovery, and disclosure procedures. Missing evidence will be treated as a reason for review or refusal rather than silently converted into success.

## 7. Community and contributor development

The project will design accessible pathways for independent developers, researchers, organizations, educators, and public-interest participants to evaluate and contribute to the ecosystem. Planned materials include contributor onboarding, architecture maps, bounded starter tasks, validation challenges, conformance examples, governance orientation, and reference implementation guidance.

Community development will begin with English, Spanish, Simplified Chinese, and Traditional Chinese materials, subject to available resources and validation. The plan will distinguish participation from execution authority: contributors may propose, test, document, or validate work without automatically receiving release, financial, or policy authority.

The project will seek three to five qualifying independent users or contributors whose letters and participation can demonstrate real external interest. Until those relationships are established and documented, the application will not claim an existing community at the level required for submission.

## 8. Sustainability and transition strategy

The sustainability plan will evaluate a mixed model of public research support, sponsorship, implementation services, training, certification or conformance services, institutional membership, and public-good maintenance. It will assess the risks of dependence on a single sponsor, vendor, maintainer, or proprietary platform.

The transition roadmap will define stages for:

1. product-boundary and license resolution;
2. discovery and stakeholder validation;
3. governance and managing-organization design;
4. security and privacy hardening;
5. contributor and adopter onboarding;
6. independent implementation and conformance testing;
7. Track 2 readiness or a documented no-go decision.

Metrics will include validated stakeholder demand, independent implementation attempts, contributor retention, issue resolution, security findings, governance participation, release reproducibility, documentation usability, and evidence that the proposed organization can survive changes in individual maintainers.

## 9. Work plan, milestones, and evaluation

The one-year planning effort is organized into four phases.

### Phase 1 — Evidence baseline and product boundary

- inventory candidate components and current maturity;
- resolve or formally classify license and disclosure gaps;
- establish stakeholder and contributor discovery protocols;
- define measurable hypotheses and go/no-go criteria.

### Phase 2 — Discovery and risk analysis

- conduct stakeholder interviews and technical workshops;
- evaluate user and contributor needs;
- complete security, privacy, supply-chain, and governance threat models;
- test candidate ecosystem boundaries through integration exercises.

### Phase 3 — Organization, licensing, and community design

- draft managing-organization and decision-rights models;
- develop licensing, contribution, and disclosure recommendations;
- produce contributor pathways and multilingual onboarding pilots;
- evaluate sustainability scenarios.

### Phase 4 — Synthesis and transition decision

- publish the ecosystem discovery and maturity assessment;
- finalize governance, security, privacy, community, and sustainability plans;
- issue the transition roadmap and Track 2 readiness determination;
- preserve negative or inconclusive findings rather than forcing a continuation decision.

Evaluation criteria and detailed milestones are maintained in `FUNDING-NSF-PESOSE-2026-001-milestones.md`. Any final schedule, staffing, or cost commitments remain subject to applicant and StegFinCo approval.

## 10. Intellectual merit

The project investigates whether continuity, admissibility, reconstructability, and recoverable authority can operate as an interoperable open layer for AI-agent and secure-communication ecosystems. It will also study whether governance mechanisms grounded in inspectable evidence can improve security, maintainability, and independent implementation relative to informal authority and static approval models.

The planning work will produce testable ecosystem hypotheses, structured evidence, governance designs, threat models, conformance concepts, and explicit transition criteria. Negative results—such as insufficient demand, an incoherent product boundary, or unsustainable governance requirements—will be treated as meaningful findings.

## 11. Broader impacts

A viable ecosystem could lower barriers to trustworthy AI-agent experimentation, improve secure-communication and software-supply-chain practices, support public-interest and educational use, and help organizations evaluate consequential automation with clearer evidence and authority boundaries.

The project will promote accessible documentation, multilingual onboarding, bounded contributor roles, reproducible validation, and participation by academic, industry, government, nonprofit, and independent communities. By preserving refusal, uncertainty, and no-go outcomes as first-class records, the work may also provide a reusable model for responsible open-source ecosystem formation.

## 12. Required pre-submission resolutions

This draft may enter internal review, but sponsor submission is prohibited until the canonical records establish:

1. eligible legal applicant and submission authority;
2. PI and personnel eligibility;
3. active federal registrations;
4. a licensed public open-source anchor and precise implemented boundary;
5. truthful development, testing, dissemination, user, and contributor evidence;
6. three to five qualifying independent collaboration letters;
7. application-specific protected-disclosure clearance;
8. StegFinCo-approved budget and justification;
9. final references, data-management plan, personnel documents, and sponsor-form compliance.
