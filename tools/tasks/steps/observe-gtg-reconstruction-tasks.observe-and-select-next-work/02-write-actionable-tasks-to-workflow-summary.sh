echo '## GTG reconstruction execution queue' >> "$GITHUB_STEP_SUMMARY"
python - <<'PY' >> "$GITHUB_STEP_SUMMARY"
import json
from pathlib import Path
report = json.loads(Path('coordination/gtg-reconstruction-task-report.json').read_text())
print(f"Factory R4 observation: `{report['factory_r4_observation']['state']}`")
for task in report['actionable_tasks']:
    print(f"- **{task['task_id']}**")
    print(f"  - Exists at: `{task['exists_at']}`")
    print(f"  - Execute at: `{task['execution_path']}`")
    print(f"  - Next action: {task['next_action']}")
PY
