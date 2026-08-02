# Time Causal Kernel Integration Mirror Handoff

## Active goal

- Goal ID: `time-invariant-kernel-integration-v1`
- Originating session goal: compare and integrate *Time After Causality v0.3.1* with recent StegVerse Time, RTG, GTG, and TT documentation.
- Repository: `StegVerse-Labs/StegScholar`
- Branch: `formal/time-invariant-kernel-integration-v1`
- Canonical owner: StegScholar research lane
- Role: implementation and validation of a bounded temporal substrate; no runtime or execution authority is created.
- Claim state: `CLAIMED_FOR_IMPLEMENTATION`
- Claim created: `2026-08-02T12:06:00-05:00`
- Claim release condition: merge or close the branch after schema, fixture, validator, and review receipt are present.

## Authoritative boundaries

1. `TT_MIRROR_HANDOFF.md` remains canonical for Transition Table work.
2. This handoff owns only the temporal substrate that precedes RTG -> GTG -> TT.
3. The source paper is research-only and explicitly excludes governance and AI applications.
4. The paper's phrase `admissible completion` is normalized here as `causally compatible completion`; GTG retains governance admissibility.
5. Continuity, identity reconstruction, causal compatibility, governance admissibility, execution authority, and recorded realization remain distinct.
6. Resolution changes may remove declared gauge detail but may not manufacture chronology, identity, authority, evidence, or transition semantics.

## Canonical integration sequence

```text
observed continuity
  -> identity and state/event relatedness
  -> invariant causal necessity kernel
  -> causally compatible completion support
  -> RTG relational geometry
  -> GTG admissibility and authority
  -> TT realized or withheld transition receipt
```

## Installed files

- `papers/time/causal-kernel-integration.md`
- `schemas/time-causal-kernel.schema.json`
- `fixtures/time-causal-kernel/minimal-valid.json`
- `scripts/validate_time_causal_kernel.py`

## Validation

```bash
python scripts/validate_time_causal_kernel.py fixtures/time-causal-kernel/minimal-valid.json
```

Expected result: `PASS: time causal kernel fixture is structurally valid`.

## Remaining work

1. Add negative fixtures for cyclic kernels, unsupported branches, and manufactured coarse chronology.
2. Add quotient/lumpability fixtures.
3. Bind the schema to RTG scale-map fields after the RTG canonical repository and handoff are confirmed.
4. Add GTG boundary tests proving causal compatibility does not imply governance admissibility.
5. Add TT projection tests preserving denied, deferred, transformed, failed-closed, and error outcomes.
6. Create internal review receipt and merge decision.
7. After merge, evaluate bounded propagation to `StegVerse-Labs/admissibility-wiki`; Site and Publisher remain blocked pending their canonical handoffs.

## Cross-repository dependencies

- `StegVerse-Labs/StegScholar/TT_MIRROR_HANDOFF.md`
- RTG canonical repository: unresolved in connected state; do not invent destination.
- `StegVerse-Labs/admissibility-wiki`: later bounded explanatory projection only.
- `StegVerse-Labs/Site`: no propagation until `docs/SITE_MIRROR_HANDOFF.md` grants scope.
- `GCAT-BCAT-Engine/Publisher`: no packaging until Publisher handoff grants scope.

## Session consolidation

Transferred session-specific requirements:

- kernel versus complete branch order;
- branch completion versus serialization;
- operational quotienting;
- no manufactured chronology across resolution;
- continuity and identity preceding declared events;
- causal compatibility distinct from governance admissibility;
- RTG -> GTG -> TT integration location;
- open problems remain explicitly open.

Archive condition: this session may close after branch evidence, validator execution evidence, and canonical continuation are durable and no unique requirements remain only in chat.

## Percentages

- Developed files: 4/7 required for initial merge readiness
- Validation: 1/5 planned fixture classes
- Integration: 1/4 layers represented
- Goal activation: 45%
