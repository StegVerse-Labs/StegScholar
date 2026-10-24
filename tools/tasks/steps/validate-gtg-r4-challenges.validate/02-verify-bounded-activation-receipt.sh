python - <<'PY'
import json
from pathlib import Path
task = json.loads(Path('coordination/gtg-r4-challenge-task.json').read_text())
receipt = json.loads(Path('coordination/gtg-r4-challenge-validation-receipt.json').read_text())
assert task['task_id'] == 'SV-GTG-R4-CHALLENGE-007'
assert task['external_task'] is False
assert task['dependency_posture'] == 'NONE'
assert receipt['task_id'] == task['task_id']
for value in receipt['claims'].values():
    assert value is False
print('STEGVERSE GTG R4 CHALLENGE RECEIPT: PASS')
PY
