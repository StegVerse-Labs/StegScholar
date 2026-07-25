# Research Evidence Ledger Standard

## Purpose

StegScholar operates as a recurring, evidence-backed research ledger for hypotheses, methods, source records, mathematical models, generated analyses, verification results, contradictions, revisions, and publication states.

It is modeled after the continuity and evidence discipline of the Executive Rhetoric Ledger, but its unit of analysis is a research claim rather than a political incident.

## Core rule

```text
A model-generated result is a candidate result until its inputs, method, computation, and verification posture are preserved.
Publication does not convert a hypothesis into a finding.
A source may establish that a claim was published without establishing that the claim is correct.
```

## Recurring research cycle

```text
research topic intake
-> hypothesis decomposition
-> source discovery and posture classification
-> event or observation normalization
-> Math Solver analysis request
-> generated result candidate
-> independent verification
-> contradiction and sensitivity search
-> governed review
-> progressive publication
-> later evidence refresh
```

## Research objects

Each topic may contain:

- hypotheses and subhypotheses;
- operational definitions;
- causal models;
- source-posture receipts;
- datasets and event ledgers;
- Math Solver request packets;
- generated calculations, proofs, models, plots, and statistical outputs;
- verification receipts;
- negative controls and falsification tests;
- disagreements and reviewer records;
- publication snapshots;
- supersession and deprecation records.

## Topic states

```text
PROPOSED
PROTOCOL
PILOT
EXPLORATORY
PREREGISTERED
CONFIRMATORY
REPLICATED
REVISED
DEPRECATED
```

No later state erases an earlier state. State transitions append records and preserve prior artifacts.

## Math Solver boundary

Math Solver may:

- normalize equations and variables;
- generate deterministic calculations;
- fit declared models;
- run sensitivity and placebo analyses;
- generate plots and tables;
- produce proof-step or derivation candidates;
- emit machine-readable result packets.

Math Solver may not:

- choose hidden assumptions;
- silently repair missing data;
- convert statistical association into causation;
- promote a candidate result to accepted knowledge;
- overwrite contradictory or failed results;
- claim publication or verification authority.

Every Math Solver output must identify:

```text
request_id
research_topic_id
input_artifact_refs
input_hashes
method_id
method_version
parameters
software_runtime
random_seed_or_determinism_posture
output_artifact_refs
output_hashes
warnings
uncertainty
verification_status
```

## Promotion rule

A generated result may be promoted only when:

1. the request packet is complete;
2. all input references resolve;
3. the method is declared before execution;
4. the output is reproducible or explicitly marked non-deterministic;
5. verification checks pass or unresolved checks remain visible;
6. contradictions and sensitivity results are preserved;
7. a reviewer or governed process records the promotion decision.

## Progressive publication

StegScholar is the research authority repository. Site is the public mirror.

Site may progressively publish:

- hypotheses;
- protocols;
- pilot ledgers;
- exploratory outputs;
- preregistrations;
- confirmatory results;
- replications;
- revisions.

Every public projection must retain the topic state, evidence posture, uncertainty, source repository, artifact version, and superseded status.