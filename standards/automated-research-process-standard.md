# Automated Governed Research Process Standard

## Purpose

This standard defines the research-topic route corresponding to the Executive Rhetoric Ledger's recurring people-and-events route.

Executive Rhetoric Ledger:

```text
people / institutions / events
-> evidence-backed historical compendium
```

StegScholar automated research process:

```text
research topic
-> user-developed proposal
-> governed protocol approval
-> automated evidence collection
-> dataset construction
-> Math Solver computation
-> uncertainty and error analysis
-> result determination
-> conclusions
-> progressive publication
-> later replication and revision
```

The system is not merely a repository for finished papers. It is a governed research engine that develops, executes, computes, verifies, and maintains research over time.

## Stage model

### R0 — Topic intake

The user introduces a question, observed relationship, conjecture, anomaly, or proposed explanatory model.

Required outputs:

- topic identifier;
- plain-language question;
- initial conjecture;
- known context;
- intended domain;
- immediate exclusions;
- user objectives.

### R1 — Collaborative proposal development

The system researches the topic with the user and produces a research proposal.

The proposal must include:

- research question;
- literature and prior-work map;
- hypotheses and competing hypotheses;
- operational definitions;
- unit of analysis;
- inclusion and exclusion rules;
- variables and measurement plan;
- causal model;
- source strategy;
- expected limitations;
- falsification criteria;
- candidate statistical or mathematical methods;
- required data;
- ethics, legal, and safety considerations where applicable;
- publication plan.

The user may revise assumptions, priorities, scope, and interpretation during this stage.

### R2 — Protocol freeze and authorization

Research execution does not begin merely because a proposal exists.

A proposal must pass a protocol gate recording:

```text
proposal completeness
source availability
method suitability
data feasibility
bias and confound review
negative-control design
error-analysis plan
publication posture
user authorization
```

Passing R2 freezes the first executable protocol version. Later changes require explicit amendments and must preserve the prior version.

### R3 — Automated research execution

The system conducts the approved research process:

- discovers primary and secondary sources;
- captures source posture and provenance;
- constructs event, observation, or experimental records;
- deduplicates and clusters records;
- searches for contradictions and negative cases;
- backfills historical context;
- identifies missing data;
- maintains a research queue until declared stop conditions are met.

Automation may propose additions, but may not silently alter the protocol or promote unsupported claims.

### R4 — Dataset assembly and quality control

The evidence is normalized into a versioned dataset.

Required checks include:

- schema validation;
- duplicate detection;
- missingness report;
- provenance completeness;
- coder agreement where human coding is used;
- outlier review;
- source-dependence analysis;
- measurement-error assessment;
- exclusion ledger;
- unresolved contradiction ledger.

### R5 — Math Solver execution

Math Solver receives a governed request packet containing the approved dataset, method, parameters, assumptions, equations, negative controls, expected outputs, determinism requirements, and authority boundary.

Math Solver produces candidate analytical results, including as applicable:

- descriptive statistics;
- equations and derivations;
- model fitting;
- confidence intervals;
- uncertainty propagation;
- standard errors;
- residual and goodness-of-fit analysis;
- sensitivity analysis;
- placebo and negative-control results;
- error bounds;
- plots and tables;
- proof or computation artifacts.

Math Solver does not decide publication truth or final scientific acceptance.

### R6 — Result validation and error determination

Every generated result must be checked against the declared method and input records.

The result record must include:

```text
estimate or result
units
sample or event count
method
assumptions
standard error
confidence or credible interval
measurement error
model error
sensitivity range
missing-data effect
negative-control outcome
reproducibility status
verification status
```

Where a single numerical error term is inappropriate, the system must preserve separate uncertainty components rather than manufacture one combined precision claim.

### R7 — Conclusion determination

Conclusions are derived only after the error and sensitivity record exists.

Permitted conclusion classes:

```text
SUPPORTED_WITHIN_DECLARED_SCOPE
PARTIALLY_SUPPORTED
MIXED_OR_HETEROGENEOUS
NOT_SUPPORTED
INCONCLUSIVE
FALSIFIED_UNDER_TESTED_MODEL
METHOD_OR_DATA_FAILURE
```

A conclusion must identify:

- which hypothesis was tested;
- which model and data version were used;
- effect size or substantive result;
- uncertainty and error posture;
- alternative explanations still viable;
- limits of generalization;
- conditions that would change the conclusion.

### R8 — Progressive publication

Publication proceeds by state:

```text
PROPOSAL
PROTOCOL
PILOT_DATA
EXPLORATORY_RESULTS
PREREGISTERED_ANALYSIS
CONFIRMATORY_RESULTS
REPLICATION
REVISION
DEPRECATION
```

StegScholar is the research authority repository. Site is the public mirror. Public pages must expose the current state, artifact versions, uncertainty, open contradictions, and superseded conclusions.

### R9 — Recurring refresh

Research topics remain active after publication when new evidence may alter the result.

Each refresh cycle should:

1. search for new evidence and replications;
2. refresh missing outcomes;
3. test whether assumptions or baselines changed;
4. rerun only authorized analyses;
5. compare new results with prior versions;
6. preserve revisions and conclusion changes;
7. republish the current posture without erasing history.

## Authority boundaries

```text
user collaboration != protocol approval
proposal completion != research execution authority
source existence != source truth
Math Solver output != verified result
statistical significance != substantive importance
model fit != causal proof
publication != replication
Site display != research authority
```

## Default stop conditions

A research cycle stops when one of the following is recorded:

- protocol-defined evidence threshold reached;
- declared search space exhausted;
- additional evidence produces negligible information gain;
- data or method failure prevents valid computation;
- user or authorized reviewer pauses the project;
- safety, ethics, or legal boundary blocks continuation;
- conclusion reached with required uncertainty and validation records.

Stopping does not erase pending questions. They move to the next-cycle queue.