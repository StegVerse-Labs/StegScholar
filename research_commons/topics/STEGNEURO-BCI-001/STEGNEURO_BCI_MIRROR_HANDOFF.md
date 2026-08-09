# StegNeuro BCI Research Mirror Handoff

Status: ACTIVE — MACHINE DISCOVERY + REVIEWED PRIMARY SOURCES + OPEN NAMED GAPS
Updated: 2026-08-09
Repository: `StegVerse-Labs/StegScholar`
Branch: `main`
Parent authority: `RESEARCH_COMMONS_MIRROR_HANDOFF.md`
Topic: `STEGNEURO-BCI-001`
Canonical owner: StegScholar Research Commons
Active issue: `#49`

This handoff is subordinate to the Research Commons handoff and governs only the StegNeuro BCI evidence topic. It does not create scientific, device, activation, patent, or publication authority.

## Goal

Maintain a current, reconstructable research and data-source map for wired, wireless, implanted, minimally invasive, and non-invasive BCIs relevant to StegNeuro device/adaptor claims, Comms-Gateway neural interaction profiles, StegCore neural-governance assumptions, PAT-004 technical evidence, and related papers/formalisms.

## Canonical files

```text
research_commons/protocols/generalized-research-discovery.md
research_commons/topics/STEGNEURO-BCI-001/README.md
research_commons/topics/STEGNEURO-BCI-001/registry.json
research_commons/topics/STEGNEURO-BCI-001/reviewed-sources-2026-08-09.json
research_commons/topics/STEGNEURO-BCI-001/search-plan.json
research_commons/tools/discover_sources.py
research_commons/tools/triage_sources.py
.github/workflows/stegneuro-bci-source-discovery.yml
```

## Current evidence state

Reviewed source set: 19 primary research/data sources across the seed registry plus the 2026-08-09 reviewed additions.

New bounded primary-source review added:

- human fully implanted endovascular Stentrode SWITCH study;
- minimally invasive high-density cortical microelectrode READ/WRITE system;
- human TMS with intracranial ECoG observation;
- BCI + tDCS human rehabilitation study;
- multi-session NIRS BCI dataset.

These additions close or narrow several evidence gaps but do not establish semantic neural writing, device safety beyond the cited system/study, StegNeuro hardware efficacy, or biological activation.

## Latest hosted discovery and triage

```text
workflow: StegNeuro BCI Source Discovery
run: 31297448482
job: 93204763145
head: c6e6a4cb3111ad72e1c5ccd7031b50bcf3594f30
conclusion: SUCCESS
artifact: 9033411968
artifact digest: sha256:e42a113b00e237cba9359a72d3db0c62b925abc1fcad6dcf829427b5719ab25e
candidate_count: 224
provider_errors: 0
metadata_triage:
  ADMIT_SOURCE: 156
  DUPLICATE: 3
  REJECT_SOURCE: 64
  RETRY: 1
reviewed_source_count: 19
authority_effect: NONE
registry_effect_from_metadata_triage: NONE
```

The prior first run had 56 candidates and 11 Crossref 429 errors. Bounded exponential retry, pacing, and expanded queries are now installed; the current run completed with zero provider errors. Search success does not prove candidate correctness or exhaustive coverage.

## Named evidence-gap state

Authoritative gap dispositions are in `reviewed-sources-2026-08-09.json` and are intentionally stricter than keyword-level coarse coverage.

Covered:

```text
human endovascular BCI primary trial results
optical and fNIRS READ evidence
```

Partial:

```text
TMS and tES WRITE evidence mapped to StegNeuro envelope fields
wireless fully implanted human BCI architecture evidence — endovascular system covered, intracortical/general architecture still open
device-specific calibration drift and chronic reliability datasets
```

Open:

```text
systematic clinical-trial registry mapping for implantable BCIs
primary-source regulatory and safety evidence by modality
decoder-prior/confabulation studies with explicit zero-signal or prior-ablation controls
direct comparison of READ and WRITE spatial/temporal resolution across modalities
patent landscape crosswalk
```

No coarse keyword map may silently convert these named OPEN/PARTIAL gaps to complete.

## Active claim and continuation

```text
task: STEGNEURO-BCI-001-SOURCE-TRIAGE
owner: StegVerse-Labs/StegScholar
issue: #49
role: MACHINE_OWNED_DISCOVERY + REPOSITORY_REVIEW
claim_created: 2026-08-09
release_condition:
  current candidate set has durable classification state
  AND provider errors are resolved/classified
  AND named evidence gaps have explicit dispositions
  AND hosted artifact/digest validates the resulting state
```

The recurring search itself is MACHINE_OWNED. Promotion of candidate metadata into reviewed scientific source records requires source-content evidence; metadata alone has authority effect NONE.

## Search protocol

Every cycle deliberately seeks supporting primary evidence, negative/null evidence, competing modalities, failure modes, safety/regulatory evidence, decoder/model-prior confounds, reproducible datasets, and newer work that may supersede current assumptions.

## Cross-repository consumers

- `StegVerse-Labs/StegNeuro/research/bci-evidence-consumer.json` binds to this topic and reviewed additions.
- `StegVerse-Labs/Patents/PAT-004_MIRROR_HANDOFF.md` may consume bounded technical evidence without legal conclusions.
- Comms-Gateway receives no scientific authority from this topic.
- StegCore real-hardware activation remains independently BLOCKED under `StegVerse-Labs/StegCore#73`.

## Automation

Owner: `StegVerse-Labs/StegScholar`.

Trigger: weekly schedule, workflow dispatch, or mutation to the topic/protocol/discovery/triage surfaces.

Deterministic outputs:

```text
candidate-sources.json
source-triage.json
gap-map.json
```

The artifact persists REVIEW_REQUIRED candidates, explicit gap state, and authority effect NONE. Missing evidence is never success.

## Session consolidation

Session-specific StegNeuro research requirements are durably represented by this handoff, issue #49, the reviewed source record, workflow, search plan, triage tool, and hosted evidence. The conversation does not need to remain active for weekly discovery or the named-gap work to continue.

MERGED INTO: `StegVerse-Labs/StegScholar/research_commons/topics/STEGNEURO-BCI-001/STEGNEURO_BCI_MIRROR_HANDOFF.md` and `StegVerse-Labs/StegScholar#49`.

## Archive condition

The originating conversation may archive when StegNeuro and cross-repository handoffs record this continuation and no chat-only requirement remains. Open evidence gaps do not require retaining a chat session because they have a named repository owner, issue, recurring machine observer, deterministic artifacts, and explicit release conditions.
