# GTG Task Observation and Completion Layer

## Purpose

Prevent development from halting at a status statement such as `pending`, `blocked`, `waiting`, or `external task`.

Every incomplete GTG reconstruction objective in StegVerse must exist as a repository-owned task with:

- a stable task identifier;
- an exact repository and path;
- an execution mode;
- dependencies that can be observed by StegVerse;
- a concrete next action;
- completion evidence;
- a successor task or explicit terminal condition.

## Canonical task locations

- Task ledger: `StegVerse-Labs/StegScholar:coordination/gtg-reconstruction-tasks.json`
- Observer/completer: `StegVerse-Labs/StegScholar:scripts/run_gtg_task_orchestrator.py`
- Scheduled execution: `StegVerse-Labs/StegScholar:.github/workflows/observe-gtg-reconstruction-tasks.yml`
- Generated run evidence: workflow artifact `gtg-reconstruction-task-report`

## Anti-stall invariant

```text
program_incomplete => count(executable_local_tasks) >= 1
```

A dependency in another repository does not become an external human task. It becomes a StegVerse-owned observation task. The observer checks the dependency and promotes the next local mutation task when the required evidence appears.

The orchestrator fails closed when:

- an incomplete program exposes no executable local task;
- a task lacks an exact StegVerse location;
- task execution is delegated to another repository;
- a task lacks a next action or completion evidence;
- a task references an unknown dependency;
- authority or execution is inferred from task completion.

## Current execution queue

1. `SV-GTG-R4-OBSERVE-001`
   - Exists at: `coordination/gtg-reconstruction-tasks.json#SV-GTG-R4-OBSERVE-001`
   - Executes at: `scripts/run_gtg_task_orchestrator.py`
   - Purpose: observe the canonical validation-factory R4 merge and receipt.

2. `SV-GTG-R4-MIRROR-002`
   - Exists at: `coordination/gtg-reconstruction-tasks.json#SV-GTG-R4-MIRROR-002`
   - Executes against: `manifests/gtg-reconstruction-mirror-v1.json`
   - Purpose: update the StegVerse R4 mirror binding once observed.

3. `SV-GTG-R5-DESIGN-003`
   - Exists at: `coordination/gtg-reconstruction-tasks.json#SV-GTG-R5-DESIGN-003`
   - Executes at: `papers/generalized-transition-governance/reconstruction/r5-reality-contact.md`
   - Purpose: build the StegVerse R5 research taxonomy without claiming R5 PASS.

4. `SV-GTG-R5-FIXTURES-004`
   - Exists at: `coordination/gtg-reconstruction-tasks.json#SV-GTG-R5-FIXTURES-004`
   - Executes at: `fixtures/gtg/reconstruction/r5/`
   - Purpose: create bounded positive and adversarial reality-contact cases.

## Authority boundary

Task observation, execution, completion, and activation do not create certification, legal authority, execution authority, universal admissibility, mathematical closure, empirical validity, release readiness, or archive readiness.
