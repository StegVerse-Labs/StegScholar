# StegVerse GTG Task Discovery and Reconciliation Standard

## Purpose

Prevent development from halting because an implemented task is absent from the central task ledger, a completed task retains a stale status, or an observation-only task has no local successor.

## Canonical local sources

The reconciler scans these StegVerse-owned locations:

- `coordination/gtg-reconstruction-tasks.json`
- `coordination/gtg-*-task.json`
- `coordination/gtg-*-validation-receipt.json`
- `manifests/gtg-reconstruction-mirror-v1.json`

## Required invariants

1. Every discovered task has a unique `task_id` and an exact `exists_at` path.
2. Every non-complete task has an executable StegVerse path and concrete next action.
3. A task with an activated receipt cannot remain `ACTIVE_VALIDATION`, `QUEUED`, or `BLOCKED` in the central ledger.
4. A task present in a task file but absent from the central ledger is a reconciliation failure.
5. If all mutation tasks are complete and only observation remains, the ledger must expose a local challenge, fixture-expansion, drift-audit, or receipt-verification successor.
6. No task may be assigned to an external actor or described as an external handoff.
7. Reconciliation cannot enable execution authority, certification, mathematical closure, completed independent verification, release readiness, or archive readiness.

## Outputs

- `coordination/gtg-task-discovery-report.json`
- Nonzero exit on missing, stale, duplicated, externalized, or status-only tasks.

## Bounded posture

This layer reconciles repository work state. It does not establish canonical GTG authority or independent validation.
