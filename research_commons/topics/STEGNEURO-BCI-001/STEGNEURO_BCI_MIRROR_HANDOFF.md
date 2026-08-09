# StegNeuro BCI Research Mirror Handoff

Status: ACTIVE — MACHINE DISCOVERY + REVIEW-REQUIRED SOURCE TRIAGE
Updated: 2026-08-09
Repository: `StegVerse-Labs/StegScholar`
Parent authority: `RESEARCH_COMMONS_MIRROR_HANDOFF.md`
Topic: `STEGNEURO-BCI-001`

This handoff is subordinate to the Research Commons handoff and governs only the StegNeuro BCI evidence topic. It does not create a competing Research Commons authority.

## Goal

Maintain a current, reconstructable research and data-source map for wired, wireless, implanted, minimally invasive, and non-invasive brain–computer interfaces relevant to:

- `StegVerse-Labs/StegNeuro` device/adaptor claims;
- the Comms-Gateway neural interaction profile;
- StegCore neural governance and physical-model assumptions;
- PAT-004 technical evidence and limitation mapping;
- related papers and formalisms.

## Canonical files

```text
research_commons/protocols/generalized-research-discovery.md
research_commons/topics/STEGNEURO-BCI-001/README.md
research_commons/topics/STEGNEURO-BCI-001/registry.json
research_commons/topics/STEGNEURO-BCI-001/search-plan.json
research_commons/tools/discover_sources.py
.github/workflows/stegneuro-bci-source-discovery.yml
```

## Current evidence state

Initial reviewed seed: installed in `registry.json`.

Automated current-source discovery:

```text
run: 31296618774
job: 93202637685
conclusion: SUCCESS
artifact: 9033134803
artifact name: stegneuro-bci-source-candidates
artifact zip sha256: b986f6650e8b593d162b0ac4e8ddc422e605b9f1d86867ebd90fef0d82ba3ee3
candidate_count: 56
provider/query errors: 11
candidate_state: REVIEW_REQUIRED
authority_effect: NONE
auto_merge_into_registry: false
```

The workflow success proves the discovery mechanism ran and preserved its fail-closed posture. It does not prove exhaustive research coverage, candidate correctness, or scientific support for a StegNeuro device.

## Active claim

```text
task: STEGNEURO-BCI-001-SOURCE-TRIAGE
owner: StegVerse-Labs/StegScholar
issue: #49
role: CLAIMED_FOR_RESEARCH_REVIEW
claim_created: 2026-08-09
release_condition:
  every candidate classified ADMIT_SOURCE / REJECT_SOURCE / SUPERSEDED / DUPLICATE / RETRY
  AND 11 provider errors resolved or durably classified
  AND explicit coverage/gap state exists for required modalities and evidence dimensions
  AND updated registry receives hosted digest validation
```

## Search protocol

Every discovery cycle must deliberately seek:

1. supporting primary evidence;
2. negative/null evidence;
3. competing modalities;
4. failure modes and limitations;
5. safety and regulatory evidence;
6. decoder/model-prior confounds;
7. reproducible datasets;
8. newer work that may supersede existing assumptions.

Research results are evidence candidates only. They do not create intent, consent, authority, semantic equivalence, device efficacy, biological activation, or patent conclusions.

## Required coverage

```text
intracortical wired READ
intracortical wireless READ
ECoG / surface cortical interfaces
endovascular / endocisternal approaches
non-invasive EEG / MEG / optical approaches
functional ultrasound READ
focused ultrasound WRITE
TMS / tES and other non-invasive WRITE approaches
bidirectional systems
speech and inner-speech decoding
neural encoding / write evidence
target localization and registration
calibration and chronic drift
bandwidth / latency / noise
spatial and temporal resolution
safety / regulatory posture
decoder-prior and model-contribution controls
reproducible datasets
```

## Known gaps

The registry's `known_gaps` array is authoritative. Current gaps include human endovascular primary-trial mapping, TMS/tES and optical evidence, fully implanted wireless human architecture evidence, decoder-prior ablation/confound studies, cross-modality resolution comparisons, chronic calibration/reliability data, safety/regulatory mapping, and patent-landscape crosswalk.

## Automation

Owner: `StegVerse-Labs/StegScholar`.

Trigger: weekly schedule, workflow dispatch, or changes to the protocol/topic/tool/workflow.

Output: review-required candidate artifact. Missing provider evidence is not success; provider errors are persisted in the artifact.

## Cross-repository consumers

- StegNeuro consumes reviewed evidence through `research/bci-evidence-consumer.json`.
- Patents PAT-004 may consume verified research and implementation evidence for factual technical preparation only.
- Comms-Gateway consumes no scientific authority from this topic; it only owns the interaction protocol.
- StegCore hardware activation remains blocked independently under issue #73.

## Archive condition

This research topic remains active independently of any chat session. The current conversation is not required to operate the weekly discovery workflow, but the broader StegNeuro goal remains incomplete until the requested evidence landscape is materially triaged and the real-device boundary is separately satisfied or explicitly held blocked.
