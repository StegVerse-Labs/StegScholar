python - <<'PY'
import hashlib
import json
import os
from datetime import datetime, timezone
from pathlib import Path

runs = [
    {
        "benchmark_id": "rigel-scalar-delayed-control-v1",
        "output": Path("generated/scalar-delayed-control"),
        "files": ["config.json", "episodes.csv", "summary.json", "baseline-evaluation.json"],
        "command": (
            "python papers/recoverability-geometry-rigel-number/simulations/"
            "scalar_delayed_control.py --episodes "
            "${{ steps.run_sizes.outputs.episodes }} --seed 20260714 "
            "--output-dir generated/scalar-delayed-control; then fit_baselines.py"
        ),
    },
    {
        "benchmark_id": "rigel-constant-total-latency-ablation-v1",
        "output": Path("generated/constant-total-latency-ablation"),
        "files": ["config.json", "episodes.csv", "summary.json"],
        "command": (
            "python papers/recoverability-geometry-rigel-number/simulations/"
            "constant_total_latency_ablation.py --scenarios "
            "${{ steps.run_sizes.outputs.ablation_scenarios }} --seed 20260714 "
            "--total-latency 0.45 "
            "--output-dir generated/constant-total-latency-ablation"
        ),
    },
]

for run in runs:
    output = run["output"]
    files = [output / name for name in run["files"]]
    hashes = {}
    for path in files:
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        hashes[str(path)] = {"sha256": digest, "bytes": path.stat().st_size}

    receipt = {
        "schema_version": "1.2",
        "benchmark_id": run["benchmark_id"],
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "repository": os.environ.get("GITHUB_REPOSITORY"),
        "commit_sha": os.environ.get("GITHUB_SHA"),
        "run_id": os.environ.get("GITHUB_RUN_ID"),
        "run_attempt": os.environ.get("GITHUB_RUN_ATTEMPT"),
        "event_name": os.environ.get("GITHUB_EVENT_NAME"),
        "python": "3.12",
        "command": run["command"],
        "independent_outcome_label": True,
        "files": hashes,
        "validation_state_path": "generated/validation-state.json",
        "claim_limit": (
            "This receipt proves deterministic execution and artifact identity only; "
            "it does not establish cross-domain validity or a universal Ri=1 threshold."
        ),
    }
    (output / "validation-receipt.json").write_text(
        json.dumps(receipt, indent=2, sort_keys=True), encoding="utf-8"
    )
PY
