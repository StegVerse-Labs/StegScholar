echo "Scalar benchmark summary"
cat generated/scalar-delayed-control/summary.json
echo "Held-out fitted baseline evaluation"
cat generated/scalar-delayed-control/baseline-evaluation.json
echo "Constant-total-latency ablation summary"
cat generated/constant-total-latency-ablation/summary.json
echo "Fail-closed validation state"
cat generated/validation-state.json
