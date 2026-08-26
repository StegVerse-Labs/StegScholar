# AI Cognitive Substitution / Learning Transition Integrity Mirror Handoff

Status: ACTIVE RESEARCH — PRIMARY/COUNTEREVIDENCE REVIEW STARTED / EVIDENCE INFRASTRUCTURE PARTIAL / SCIENTIFIC VALIDATION PENDING
Updated: 2026-08-26
Repository: `StegVerse-Labs/StegScholar`
Branch: `main`
Parent authority: `RESEARCH_COMMONS_MIRROR_HANDOFF.md`
Topic: `AI-COGNITIVE-SUBSTITUTION-001`
Canonical owner: StegScholar Research Commons
Continuation owner: existing Research Commons feature workstream / issue #21 unless a later repository-native claim explicitly promotes this topic to a dedicated execution issue

This handoff is subordinate to the Research Commons handoff and governs only the bounded evidence question of when AI assistance amplifies human learning versus substitutes for cognitive transitions that an educational or evaluative process intended the human to perform. It creates no scientific, educational-policy, publication, admissibility, clinical, or product authority.

## Session trigger and scope

Originating discovery source:

`https://futurism.com/future-society/students-lose-ability-think-ai`

Source posture: `USER_SUPPLIED_SECONDARY_JOURNALISM_TRIGGER`.
Authority effect: `NONE`.

The article and the session's interpretation are research-discovery inputs, not validated scientific findings.

## Canonical conceptual framing

1. **Capability produced is not the same as cognitive work performed.** A high-quality answer or artifact can coexist with little human reasoning during its production.
2. **The key risk hypothesis is unobserved cognitive substitution.** The relevant concern is not simply AI use, but a condition in which AI performs cognitive transitions that the learning process intended the human to traverse while the terminal artifact makes that substitution difficult to observe.
3. **Terminal-artifact evaluation is insufficient by itself for learning provenance.** Assessing only the essay, proof, program, answer, or other final output may not establish that the learner acquired the intended capability.
4. **Learning may be represented as state transitions rather than only output quality.** Illustrative modeling aid: `S0 vague intuition -> S1 proposition -> S2 conflicting evidence -> S3 discrimination -> S4 revised proposition -> S5 defensible conclusion`.
5. **AI can amplify rather than replace those transitions.** Candidate pattern: human proposition -> AI counterexample -> human discrimination -> AI alternative -> human reasoned acceptance/rejection -> revised human proposition.
6. **Governance/evaluation implication.** A future learning-integrity system should distinguish human-acquired state transitions, machine contribution, evidence provenance, and terminal artifact quality rather than treating those as interchangeable.

These remain research hypotheses/modeling distinctions, not validated metrics or causal findings.

## Evidence admission boundary

Before promotion, primary or authoritative research records must preserve:

- study design and population;
- sample size and assignment method;
- AI condition and comparator condition;
- outcome type: self-report, behavioral, physiological, academic, transfer, or longitudinal;
- measured construct: critical thinking, recall, cognitive effort, dependence, metacognition, neural activity/connectivity, task accuracy, transfer, or another variable;
- causal versus correlational status;
- effect sizes and uncertainty where available;
- replication, external validity, and confounding limits;
- temporary task-state versus durable capability interpretation;
- peer-review/version status;
- contradictory, null, and limitation evidence.

Secondary headlines or summaries cannot authorize claims such as `AI causes loss of thinking ability`.

## Canonical files

```text
research_commons/topics/AI-COGNITIVE-SUBSTITUTION-001/AI_COGNITIVE_SUBSTITUTION_MIRROR_HANDOFF.md
research_commons/topics/AI-COGNITIVE-SUBSTITUTION-001/session-trigger-2026-08-26.md
research_commons/topics/AI-COGNITIVE-SUBSTITUTION-001/evidence-registry.v1.json
research_commons/topics/AI-COGNITIVE-SUBSTITUTION-001/evidence-matrix.md
research_commons/topics/AI-COGNITIVE-SUBSTITUTION-001/claim-measurement-taxonomy.v1.json
research_commons/topics/AI-COGNITIVE-SUBSTITUTION-001/contradiction-map.v1.json
```

No duplicate topic/execution lane was found before this continuation. Parent Research Commons issue #21 remains the higher-level feature owner.

## 2026-08-26 machine-execution advancement

### Discovery-source decomposition

The Futurism trigger was inspected directly. It materially points to:

- a New York Times essay with expert commentary, retained only as a secondary discovery surface because its content was not directly reviewable through the current retrieval path;
- `Kosmyna et al., Your Brain on ChatGPT: Accumulation of Cognitive Debt when Using an AI Assistant for Essay Writing Task, arXiv:2506.08872 (2025)`.

### First primary study: Kosmyna et al.

Reviewed sources: MIT Media Lab publication/project record, arXiv record/abstract, and available full-text metadata mirrors.

Current bounded facts retained in `evidence-registry.v1.json`:

- 54 participants completed sessions 1-3; 18 completed optional session 4;
- participants were randomly assigned across LLM, Search Engine, and Brain-only groups and balanced with respect to age/gender according to the available full-text record;
- the LLM condition used GPT-4o; Search Engine excluded AI-enhanced answers; Brain-only prohibited external tools;
- session 4 switched returning LLM participants to Brain-only and returning Brain-only participants to LLM;
- the study used EEG connectivity, essay NLP, human/AI scoring, post-task interview/ownership measures, and quotation recall;
- the reported LLM condition had the weakest EEG connectivity of the three conditions and greater difficulty quoting its own produced essays;
- session-4 LLM-to-Brain participants showed reduced alpha/beta connectivity in the study's framing.

Preserved limits:

- essay-writing context only;
- no direct generalization to other LLMs;
- optional session 4 had only 18 participants;
- EEG spatial-resolution and analysis limitations;
- no subtask decomposition of idea generation/drafting/etc.;
- larger/diverse and longitudinal studies are explicitly identified as future work.

Therefore the study supports bounded task-level neural/behavioral differences, not generalized/durable cognitive-loss claims.

### Methodological counterweight

Added `Stankovic et al., Comment on: Your Brain on ChatGPT..., arXiv:2601.00856` as `ACS-SRC-004`.

The comment calls for more conservative interpretation and raises concerns about limited sample size, reproducibility, EEG methodology, reporting inconsistencies, and transparency. This is now a required paired counterweight when interpreting Kosmyna et al.

### Positive/scaffolding counterexample

Added peer-reviewed primary research:

`Peng et al. (2026), Scaffolding human and AI instruction: Neural alignment and learning gains in online education, Neuron, DOI 10.1016/j.neuron.2026.04.005` as `ACS-SRC-005`.

The randomized between-subjects study analyzed 57 students across no-interaction, human pre-lecture interaction, and structured AI pre-lecture interaction conditions. It measured recall, comprehension, difficult-item comprehension, transfer, fMRI neural alignment, gaze alignment, and social closeness. The peer-reviewed paper reports that structured AI-led pre-lecture interaction produced learning/neural-alignment benefits in the overall study framing and learning outcomes statistically comparable to the human-interaction group, while also showing lower social closeness and some lower gaze alignment than the human group.

This materially corrects any universal model that equates `AI assistance` with `cognitive substitution`. Interaction design is now a first-class variable.

### Scaffold-versus-substitute theory lane

Added peer-reviewed hypothesis/theory paper:

`Pereira Campos & Koff (2026), Your brain on ChatGPT, but whose brain? The missing adolescent in AI-cognition research, Frontiers in Developmental Psychology` as `ACS-SRC-006`.

It explicitly separates cognitive debt, reduced neural engagement, and reduced neural connectivity; warns that lower activity/connectivity does not automatically imply worse cognition; treats long-term adolescent effects as an unconfirmed hypothesis; and frames the important distinction as AI substituting for versus scaffolding executive-function processes.

### Machine-readable contradiction map

`contradiction-map.v1.json` is now installed. Current propositions include:

- `AI-assisted educational work necessarily reduces learning` -> `CONTRADICTED_AS_UNIVERSAL_CLAIM`;
- `lower neural connectivity proves lower cognitive ability` -> `NOT_ADMISSIBLE`;
- `Kosmyna et al. establishes durable generalized decline` -> `NOT_SUPPORTED`;
- `AI can function as a learning scaffold rather than substitute` -> `SUPPORTED_IN_AT_LEAST_ONE_BOUNDED_PEER_REVIEWED_DESIGN`;
- `unobserved cognitive substitution is an established scientific construct` -> `UNRESOLVED_PROPOSED_CONSTRUCT`.

### Implementation commits

```text
evidence registry initial: a0135bd60e5dfabb6aa308f8f95aaf9ae568ae63
evidence matrix: 7f63756e3d85b0c63366d8cfa7deb1a12edd2483
claim taxonomy: 02ec8ab9215c06b18099e1128237c7647bc48197
handoff first advancement: 8160bcb5b186b63337704cfcebeedf3cbfc61732
evidence registry counterweight expansion: d3b6766cea7912f09d01500be50b0806d8d242dd
contradiction map: 5c4b5a7ecdfb6c07966585431787aa5d71dee0bc
```

## Current state

```text
handoff_state: IMPLEMENTED_ON_MAIN
conceptual_framing: CAPTURED
user_trigger_source: REVIEWED_AS_DISCOVERY_SOURCE
primary_empirical_sources_reviewed: 2
methodological_counterweights_reviewed: 1
peer_reviewed_theory_sources_reviewed: 1
systematic_literature_map: PARTIAL
evidence_registry: IMPLEMENTED_V1
claim_taxonomy: IMPLEMENTED_V1
evidence_matrix: IMPLEMENTED_V1
contradiction_map: IMPLEMENTED_V1_PARTIAL
longitudinal_evidence_review: PENDING
delayed_unaided_transfer_review: PENDING
intervention_comparison_review: STARTED
full_kosmyna_methods_results_statistics_review: PARTIAL
peer_review_status_kosmyna: PREPRINT_NOT_ESTABLISHED_AS_PEER_REVIEWED
independent_review: PENDING
scientific_validation: NOT_CLAIMED
publication: NOT_CLAIMED
activation: NOT_CLAIMED
release: NOT_CLAIMED
```

## Next executable boundary

1. Complete direct full-paper extraction of Kosmyna et al. methods/results/statistics and reconcile each press-propagated numerical claim against the primary paper.
2. Verify whether a peer-reviewed successor/version of arXiv:2506.08872 exists.
3. Expand peer-reviewed studies with **delayed unaided** reasoning/transfer outcomes after AI-supported learning.
4. Add explicit null-result studies and replications.
5. Add head-to-head substitution-versus-scaffolding designs, including critique, tutoring, counterexample, Socratic, retrieval-practice, delayed-feedback, and answer-withholding modes.
6. Build longitudinal evidence sufficient to distinguish task-state effects from persistent capability change.
7. Test whether `unobserved cognitive substitution` has a sufficiently discriminable operational definition to justify a state-transition / learning-provenance schema.
8. Only after that evidence boundary clears: implement schema, deterministic validator, positive/negative/null fixtures, and independent review.

## Unresolved risks and non-claims

- `lower task effort` is not automatically `loss of ability`;
- `different neural activation/connectivity` is not automatically `brain damage`, `cognitive decline`, lower intelligence, or durable impairment;
- better AI-assisted task performance is not automatically human learning;
- better structured-AI learning outcomes do not prove all AI use is beneficial;
- immediate recall is distinct from durable retention and transfer;
- self-reported ownership, confidence, or dependence is not a direct capability measurement;
- educational outcomes may differ by age, domain, task, model, prompting/intervention style, motivation, assessment design, and duration of exposure;
- `unobserved cognitive substitution` remains proposed, not validated;
- the illustrative S0-S5 sequence remains a modeling aid, not a psychometric scale;
- no current source establishes a generalized, durable population-level cognitive-loss effect from LLM use.

## User / credential / external-action boundary

User action required now: `NONE`.

No iPhone-only action, credential, provider activation, external authorization, physical runtime proof, payment, or manual repository setting is required for current research continuation.

## Machine-executable work remaining

- full Kosmyna primary-paper statistical extraction;
- broader systematic primary-source registry expansion;
- null/replication evidence;
- delayed unaided transfer evidence;
- longitudinal evidence;
- structured scaffolding versus substitution intervention review;
- peer-review/version-status verification;
- operational/discriminant validation of the proposed substitution construct;
- independent review;
- schema/validator/fixtures only after evidence justifies the construct;
- release verification and downstream propagation evaluation only after a genuine reviewed release.

## Cross-repository / downstream relationship

Primary authority remains `StegVerse-Labs/StegScholar` Research Commons. A reviewed result could later inform StegVerse learning/evaluation, governance, or Site surfaces, but this research state grants no downstream authority.

No tag/release is warranted. No propagation is currently authorized to `StegVerse-Labs/Site`, `GCAT-BCAT-Engine/Publisher`, `admissibility-wiki`, or `stegguardian-wiki`. If this topic reaches genuine reviewed-release state, create release verification first and then evaluate those destinations for pertinent non-sensitive definitions, evidence boundaries, or user-facing guidance.

## Archive / continuity condition

The conversation is not canonical. Ongoing continuation must begin from this handoff plus the evidence registry, matrix, taxonomy, and contradiction map.

## Progress basis

```text
canonical_topic_files_required_current_phase: 6
canonical_topic_files_developed: 6
scaffolding_or_stubs: 0
conceptual_capture: COMPLETE
primary_evidence_review: 32%
machine_research_infrastructure_for_topic: 62%
contradiction_counterweight_review: 35%
longitudinal_delayed_transfer_review: 0%
independent_review: 0%
reviewed_release: 0%
estimated_topic_goal_activation: 38%
```
