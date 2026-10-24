python - <<'PY'
import json
from pathlib import Path
ledger = json.loads(Path('coordination/gtg-reconstruction-tasks.json').read_text())
tasks = {task['task_id']: task for task in ledger['tasks']}
assert tasks['SV-GTG-R5-DESIGN-003']['status'] == 'COMPLETE'
assert tasks['SV-GTG-R5-FIXTURES-004']['status'] == 'COMPLETE'
assert tasks['SV-GTG-R5-MIRROR-005']['status'] == 'COMPLETE'
for value in ledger['claims'].values():
    assert value is False
print('STEGVERSE GTG R5 POSTURE: PASS')
PY
