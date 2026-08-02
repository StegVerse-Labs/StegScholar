#!/usr/bin/env python3
import json
from pathlib import Path

CASES = Path('coordination/gtg-r4-r5-temporal-continuity-cases.json')


def classify(c):
    vals = [c.get('authority_start'), c.get('authority_end'), c.get('evidence_time'), c.get('evidence_valid_until'), c.get('boundary_time')]
    if c.get('authority_start') is None or c.get('evidence_time') is None or c.get('boundary_time') is None:
        return 'TEMPORAL_CONTINUITY_PARTIAL'
    if c.get('authority_end') is None or c.get('evidence_valid_until') is None:
        return 'TEMPORAL_CONTINUITY_PARTIAL'
    a0, a1, e0, e1, t = vals
    if a1 < a0 or e1 < e0:
        return 'TEMPORAL_CONTINUITY_FAIL_CLOSED'
    revoked = c.get('revoked_at')
    if not (a0 <= t <= a1 and e0 <= t <= e1):
        return 'TEMPORAL_CONTINUITY_FAIL_CLOSED'
    if revoked is not None and revoked <= t:
        return 'TEMPORAL_CONTINUITY_FAIL_CLOSED'
    return 'TEMPORAL_CONTINUITY_SURVIVES'


def main():
    doc = json.loads(CASES.read_text())
    assert len(doc['cases']) >= 10
    failures = []
    for c in doc['cases']:
        actual = classify(c)
        if actual != c['expected']:
            failures.append((c['id'], c['expected'], actual))
    assert all(v is False for v in doc['claims'].values())
    if failures:
        raise SystemExit(f'failures={failures}')
    print(f"GTG R4-R5 TEMPORAL CONTINUITY: PASS ({len(doc['cases'])} cases)")

if __name__ == '__main__':
    main()
