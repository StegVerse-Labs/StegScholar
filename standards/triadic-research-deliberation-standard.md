# Triadic Research Deliberation Standard

## Purpose

A research topic should not move directly from one user's observation into an executable protocol through a single model's interpretation.

StegScholar therefore uses a triadic deliberation process:

```text
User / Observer-Witness
+ Research Formulation LLM
+ Adversarial Review LLM
-> polished research topic and executable protocol candidate
```

The two LLMs do not vote the user out of the process. The user remains the originating observer, contextual witness, scope authority, and final approver of the research question and protocol boundary.

## Roles

### 1. User / Observer-Witness

The user provides:

- the original observation, anomaly, conjecture, or research interest;
- experiential context and intended meaning;
- corrections when either model misstates the premise;
- priorities, exclusions, and acceptable scope;
- confirmation that the polished topic still represents the intended inquiry;
- final authorization to freeze the protocol.

The user is not required to perform the statistical or computational work. The user's role is epistemic continuity and authorization, not manual research labor.

### 2. Research Formulation LLM

The first model acts as the constructive research architect.

It should:

- clarify the original observation without narrowing it prematurely;
- identify the likely discipline or cross-disciplinary framing;
- perform initial literature and terminology discovery;
- propose research questions and hypotheses;
- define measurable variables and units of analysis;
- suggest data, methods, controls, and publication structure;
- preserve the user's conceptual contribution and vocabulary where useful;
- identify ambiguities requiring user clarification.

Its objective is the strongest coherent version of the proposed research.

### 3. Adversarial Review LLM

The second model acts as an independent methodological critic.

It should:

- attempt to falsify or weaken the proposed framing;
- identify hidden assumptions and category errors;
- search for competing explanations and prior work;
- challenge causal claims, operational definitions, and measurement validity;
- test whether the proposed data can answer the proposed question;
- identify missing negative controls, error models, ethical concerns, and scope limits;
- distinguish researchable claims from rhetorical or metaphysical claims;
- propose alternative formulations where the original cannot be tested directly.

Its objective is not opposition for its own sake. It should produce the strongest valid objections and repair proposals.

## Deliberation sequence

### T0 — Witness statement

The user submits the initial observation in their own terms.

The original statement is preserved unchanged as a provenance artifact.

### T1 — Constructive formulation

The Research Formulation LLM produces:

- interpreted research topic;
- candidate research questions;
- hypotheses;
- definitions;
- proposed evidence and methods;
- uncertainties and clarification requests.

### T2 — Adversarial review

The Adversarial Review LLM receives:

- the original witness statement;
- the constructive formulation;
- available source context;
- the current research constraints.

It returns:

- objections;
- competing hypotheses;
- methodological weaknesses;
- ambiguity findings;
- proposed repairs;
- unresolved questions for the user.

### T3 — User witness correction

The user reviews both outputs and may:

- confirm intended meaning;
- reject an interpretation;
- restore omitted context;
- choose among alternative formulations;
- revise the intended scope;
- identify which disputed assumptions must remain visible.

Neither LLM may silently resolve a disagreement that depends on the user's intended meaning.

### T4 — Reconciliation draft

The two models produce a reconciled topic packet that separates:

```text
agreed formulation
remaining disagreements
user-resolved questions
unresolved empirical questions
protocol assumptions
alternative hypotheses
falsification conditions
```

The reconciliation must not manufacture consensus. Material disagreements remain explicit.

### T5 — Protocol candidate

The Research Formulation LLM converts the reconciled topic into a full proposal and protocol candidate.

The Adversarial Review LLM audits the result against the proposal-completeness and protocol-freeze gates.

### T6 — User authorization

The user approves, rejects, or amends the protocol candidate.

Only an approved version may enter the executable research process.

## Independence requirements

The second model should be independent in role and preferably independent in provider, model family, training lineage, or system configuration where practical.

At minimum:

- the second model must not merely rewrite the first model's answer;
- both outputs must be retained separately;
- prompts, model identifiers, provider identifiers, dates, and versions must be recorded;
- the reconciliation must show which model introduced each material claim or objection;
- agreement between models is not evidence that a claim is true;
- disagreement is not evidence that a claim is false.

## Required topic packet

A topic may pass triadic deliberation only when the packet contains:

```text
original_witness_statement
witness_context
formulation_model_output
review_model_output
user_corrections
reconciliation_record
agreed_research_question
competing_hypotheses
operational_definitions
scope_and_exclusions
proposed_data
proposed_methods
error_and_uncertainty_plan
negative_controls
falsification_conditions
unresolved_disagreements
user_authorization
```

## Governance boundaries

```text
user observation != established fact
LLM agreement != validation
LLM disagreement != falsification
polished wording != methodological adequacy
methodological adequacy != executable authorization
protocol authorization != result acceptance
```

## Why this structure is required

A single-model process risks converting ambiguity into false clarity. A dual-model process without the user risks replacing the originating observation with model consensus. The triadic structure preserves the user's meaning while forcing the research proposal through constructive formulation and independent criticism before execution.