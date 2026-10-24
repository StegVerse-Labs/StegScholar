python - <<'PY'
import json
from pathlib import Path
files = list(Path('research_commons').rglob('*.json'))
for path in files:
    json.loads(path.read_text())
print(f'parsed {len(files)} JSON files')
PY
