# Research Commons Mirror Handoff

## Authority and scope

Canonical continuation record for the Research Commons workstream in `StegVerse-Labs/StegScholar`.

Goal Task ID: `RC-CTRL-001`
goal_id: RC-CTRL-001
Canonical branch: `main`
Canonical owner: StegVerse-Labs/StegScholar repository-native workstream

Read before mutation:
1. `RESEARCH_COMMONS_MIRROR_HANDOFF.md`
2. `research_commons/control/task-registry.json`
3. `research_commons/published_research_graph/graph.json`
4. `research_commons/published_research_graph/SEVENTH_SOURCE_SCREENING_NOTE.md`
5. issue #21, issue #37, and issue #38
6. before any Site mutation, `StegVerse-Labs/Site/docs/SITE_MIRROR_HANDOFF.md`

## Active goal

`RC-CTRL-001` owns governed Research Commons ingestion, research indexing and relation lineage, validation, reuse boundaries, and Site projection without transferring publication or scientific authority.

## Canonical graph state

Six external ingestions remain canonical. Seventh-source screening remains `NO_ADMISSION`; no new document, claim, evidence, or relation has been admitted. The Published Research Graph remains unchanged and every graph authority effect remains `NONE`.

The preserved Gridworlds baseline-result digest remains `sha256:ed8887f7e1b48fbd0e0904e04802a10d8f5536ceb428d21c5c849fc55bd64fab`.

## Seventh-source frozen threshold

A seventh external graph source may be admitted only if independently authored and either:
- directly benchmarks at least two already represented side-effect mitigation mechanisms under the same environment/protocol; or
- independently reproduces or fails to reproduce one represented mechanism in a substantially different domain.

The threshold is not satisfied by conceptual adjacency, one represented mechanism plus an unrepresented method, another gridworld-style modification, an AUP-inspired replacement method in a different domain, or a formal-only extension.

## Seventh-source screening — `NO_ADMISSION`

Screening record: `research_commons/published_research_graph/SEVENTH_SOURCE_SCREENING_NOTE.md`.

Do not re-screen candidates recorded there, including Overman and Bayati (2026), `Calibrating Conservatism for Scalable Oversight`, and Nayebi (2026), `Core Safety Values for Provably Corrigible Agents`.

Fourth continuation findings:
- Overman and Bayati independently evaluate CCO on MACHIAVELLI and modified SWE-bench and separately implement a fixed-λ AUP baseline. Protocol inspection shows AUP itself is exercised only in their controlled non-stationary species-harm gridworld; the substantially different domains use CCO. It therefore does not reproduce/fail to reproduce represented AUP in a substantially different domain and does not compare two represented mechanisms under one protocol.
- Nayebi independently extends AUP into partially observed corrigibility with a belief-based formulation and stepwise inaction-style counterfactual structure, but the work is formal/theoretical rather than the required empirical reproduction with explicit task-performance and side-effect outcomes.

These are screening dispositions only, not scientific rejections, and carry `authority_effect: NONE`.

### Fourth continuation receipts

PR #93 branch `rc-ctrl-001-seventh-source-screening-4` was based on canonical main `b416079da1225586fe47436c8f96d94d07e22de1`.
Exact head `40b67877f5aa6811d40633bb4afebd3ac3d4b3f1` passed:
- Build and validate Research Commons run `35167298424`, run 154, success.
- Validate Research Commons Control State run `35167298392`, run 645, success.
- Test Readiness run `35167298410`, run 888, success.

PR #93 merged with expected-head protection as `6332aa99c62a18e331c961fd65362dbc5544846f`.
Post-merge main validation passed:
- Build and validate Research Commons run `35167358012`, run 155, success.
- Validate Research Commons Control State run `35167358015`, run 646, success.
- Test Readiness run `35167357966`, run 889, success.

PR #93 changed only the screening record and canonical handoff. `graph.json` remained unchanged.

## Existing Site projection blocker

```text
dispatch_state: BLOCKED
blockers:
- projection_manifest_not_authorized
- sv-gcat-bcat-admissibility-2026: blocked_pending_source_reconciliation
- sv-god-framework-2026: blocked_pending_complete_source_record
authority_effect: NONE
```

## Validation

```text
python research_commons/tools/build_publisher_indexes.py
python research_commons/tools/validate_publisher_papers.py
python research_commons/tools/validate_published_research_graph.py
python research_commons/tools/detect_duplicates.py
python research_commons/tools/validate_site_projection.py
python research_commons/tools/build_site_projection_dispatch.py
python research_commons/tools/check_research_commons_control_state.py
```

## Cross-repository dependencies

- `GCAT-BCAT-Engine/Publisher`: publication custody and Publisher reconciliation authority.
- `StegVerse-Labs/StegScholar`: graph identity, provenance, relation lineage, review-state validation, and graph custody.
- `StegVerse-Labs/Site`: projection acceptance/deployment only after its own orchestrator admission.
- `admissibility-wiki`, `stegguardian-wiki`, and `master-records`: no propagation without a versioned destination contract and receipt.

## Coordination state

`RC-004` remains `MACHINE_OWNED` source-drift observation. `RC-005` remains `BLOCKED` Site projection. No competing handoff or child Goal Task has been created.

## Archive conditions

This fourth screening continuation is archiveable only after this handoff-only reconciliation passes exact-head hosted validation, merges with expected-head protection, and post-merge validation is observed. `NO_ADMISSION` remains fail-closed until qualifying evidence exists.

## Next executable action

Continue `RC-CTRL-001` source discovery only for a genuinely new independently authored empirical paper that clears the frozen threshold. Do not re-screen any candidate in `SEVENTH_SOURCE_SCREENING_NOTE.md`. Prefer a same-protocol quantitative comparison of two or more represented mechanisms; otherwise require an actual independent empirical reproduction/failure of AUP, Relative Reachability, or future-task preservation in a substantially different domain with explicit task-performance and side-effect outcomes. If no source clears the threshold, preserve `NO_ADMISSION`, leave `graph.json` unchanged, and retain `authority_effect: NONE`.
