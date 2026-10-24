python - <<'PY'
import json
from pathlib import Path
receipt = json.loads(Path("governable-autonomy-validation-receipt.json").read_text())
if receipt.get("result") != "COMPLETE":
    raise SystemExit("validation receipt did not report COMPLETE")
PY
