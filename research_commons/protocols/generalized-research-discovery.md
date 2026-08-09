# Generalized Research Discovery Protocol

Status: repository-native Research Commons protocol
Owner: `StegVerse-Labs/StegScholar`

## Purpose

Continuously determine, preserve, and qualify current research and source data relevant to active StegVerse work, papers, formalisms, protocols, and device claims. The protocol is provider-neutral: scholarly search services, journal indexes, repositories, standards bodies, trial registries, patent sources, and project-owned datasets are evidence providers, not scientific authorities.

This protocol is intended to be compatible with generalized search patterns used elsewhere in the ecosystem (including ERL when its canonical repository is identified) and complementary to patent-specific discovery methods.

## Search lifecycle

```text
active ecosystem claim/work item
 -> derive research questions and falsification questions
 -> expand modality/technology/synonym query set
 -> search multiple independent evidence providers
 -> normalize source identity
 -> deduplicate versions
 -> classify primary/secondary/data/standard/regulatory/patent
 -> extract bounded observed results
 -> distinguish author claim from StegVerse inference
 -> map relevance to exact repo/file/claim
 -> record limitations/conflicts/gaps
 -> schedule refresh trigger
 -> emit reconstructable source-map receipt
```

## Required source posture

Every source record SHOULD contain:

- stable source identifier (DOI, PMID, trial ID, standard ID, repository commit/dataset ID, or canonical URL);
- title, authors/organization, year/date, venue/provider;
- source class and peer-review posture;
- modality and technology tags;
- observed result stated conservatively;
- author claim separately from observed result where they differ;
- StegVerse applicability/inference separately labeled;
- evidence relevant to READ, WRITE, bidirectional, targeting, calibration, bandwidth, latency, noise, spatial resolution, temporal resolution, safety, privacy, consent/intent, decoder priors, or regulatory posture;
- unresolved limitations and conflicts;
- destination repo/file/claim(s) supported or challenged;
- last verified date and refresh condition.

## Search breadth rule

A discovery run MUST NOT stop at sources that confirm the active design. It must deliberately search:

1. supporting results;
2. negative/null results;
3. competing modalities;
4. known limitations and failure modes;
5. safety/regulatory constraints;
6. decoder/model confounding or prior-driven reconstruction;
7. datasets and reproducibility resources;
8. recent work that may supersede older assumptions.

## Evidence classes

```text
PRIMARY_RESEARCH
PRIMARY_DATASET
CLINICAL_TRIAL_RECORD
STANDARD_OR_REGULATORY
OFFICIAL_PROJECT_TECHNICAL
PATENT
REVIEW_OR_SYNTHESIS
COMMENTARY_OR_BRIEFING
```

Reviews are useful for discovery but should not substitute for primary evidence when a primary source is available.

## Claim discipline

The protocol never converts correlation or decoder performance into intent, authorization, semantic equivalence, clinical safety, or universal capability. Sources can support physical capability claims only at the population, participant, modality, task, and configuration actually studied.

## Initial application

Topic `STEGNEURO-BCI-001` seeds the protocol for wired, wireless, minimally invasive, and non-invasive BCI evidence supporting `StegVerse-Labs/StegNeuro` and the neural communication profile in `StegVerse-Labs/Comms-Gateway`.
