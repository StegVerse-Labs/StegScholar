python papers/recoverability-geometry-rigel-number/simulations/fit_baselines.py \
  --episodes-csv generated/scalar-delayed-control/episodes.csv \
  --output generated/scalar-delayed-control/baseline-evaluation.json \
  --bootstrap-replicates "${{ steps.run_sizes.outputs.bootstrap_replicates }}" \
  --seed 20260714
