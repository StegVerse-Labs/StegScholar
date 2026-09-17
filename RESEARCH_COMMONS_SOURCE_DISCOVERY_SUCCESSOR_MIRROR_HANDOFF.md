# Research Commons Source Discovery Successor Mirror Handoff

## Authority and scope

Prepared successor continuation record for the Research Commons source-discovery workstream in `StegVerse-Labs/StegScholar`.

Goal Task ID: `RC-CTRL-002`
goal_id: RC-CTRL-002
Canonical branch: `main`
Predecessor Goal Task ID: `RC-CTRL-001`
Activation state: `UNCLAIMED`
Authority effect: `NONE`

This successor is prepared before the predecessor reaches its 20-prompt ceiling. It MUST NOT run concurrently with `RC-CTRL-001` source discovery and MUST NOT be treated as active until the predecessor is canonically closed or superseded into this successor.

## Inherited frozen source threshold

A seventh external graph source may be admitted only if independently authored and either:
- directly benchmarks at least two already represented side-effect mitigation mechanisms under the same environment/protocol with explicit side-effect and task-performance outcomes; or
- independently reproduces or fails to reproduce one represented mechanism in a substantially different domain with explicit side-effect and task-performance outcomes.

Conceptual adjacency, source-family repeats, one represented mechanism plus an unrepresented method, gridworld-only modifications, inspired replacement methods, formal-only extensions, theses that do not empirically exercise a represented mechanism, and unrelated safety experiments do not satisfy the threshold.

## Inherited canonical state

- Published Research Graph: six external ingestions.
- Seventh-source state: `NO_ADMISSION`.
- `graph.json`: unchanged by predecessor screening passes after the sixth ingestion.
- Screening ledger: `research_commons/published_research_graph/SEVENTH_SOURCE_SCREENING_NOTE.md`.
- Every graph and screening authority effect remains `NONE`.
- `RC-004` remains `MACHINE_OWNED` source-drift observation.
- `RC-005` remains `BLOCKED` Site projection.

## Read before activation

1. `RESEARCH_COMMONS_MIRROR_HANDOFF.md`
2. `RESEARCH_COMMONS_SOURCE_DISCOVERY_SUCCESSOR_MIRROR_HANDOFF.md`
3. `research_commons/control/task-registry.json`
4. `research_commons/published_research_graph/SEVENTH_SOURCE_SCREENING_NOTE.md`
5. `research_commons/published_research_graph/graph.json`

## Collision boundary

Do not activate or claim `RC-CTRL-002` while `RC-CTRL-001` remains the active source-discovery Goal Task. The successor exists only to avoid exceeding the predecessor's prompt ceiling and to preserve continuity without parallel authority.

## Activation condition

Activate `RC-CTRL-002` only after:
- `RC-CTRL-001` has reached its canonical handoff/closure point before or at 20 cumulative Goal prompts;
- predecessor receipts and current `NO_ADMISSION`/graph state are reconciled on canonical `main`;
- the task registry is updated from `UNCLAIMED` to the appropriate active claim state without creating a competing handoff.

## First executable action after activation

Re-read the predecessor handoff and screening ledger, preserve all recorded-candidate exclusions, and continue source discovery only for genuinely new independently authored empirical evidence satisfying the frozen threshold. If no source qualifies, leave `graph.json` and the screening ledger unchanged and preserve `NO_ADMISSION` and `authority_effect: NONE`.

## Archive conditions

This prepared successor handoff remains dormant while `RC-CTRL-002` is `UNCLAIMED`. It becomes the canonical continuation handoff only after predecessor closure and explicit registry activation.
