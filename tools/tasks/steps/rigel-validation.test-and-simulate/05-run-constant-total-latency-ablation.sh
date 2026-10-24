python papers/recoverability-geometry-rigel-number/simulations/constant_total_latency_ablation.py \
  --scenarios "${{ steps.run_sizes.outputs.ablation_scenarios }}" \
  --seed 20260714 \
  --total-latency 0.45 \
  --output-dir generated/constant-total-latency-ablation
