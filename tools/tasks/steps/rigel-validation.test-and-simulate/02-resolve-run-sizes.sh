if [[ "${{ github.event_name }}" == "workflow_dispatch" ]]; then
  echo "episodes=${{ inputs.episodes }}" >> "$GITHUB_OUTPUT"
  echo "ablation_scenarios=${{ inputs.ablation_scenarios }}" >> "$GITHUB_OUTPUT"
  echo "bootstrap_replicates=${{ inputs.bootstrap_replicates }}" >> "$GITHUB_OUTPUT"
elif [[ "${{ github.event_name }}" == "pull_request" ]]; then
  echo "episodes=1000" >> "$GITHUB_OUTPUT"
  echo "ablation_scenarios=250" >> "$GITHUB_OUTPUT"
  echo "bootstrap_replicates=200" >> "$GITHUB_OUTPUT"
else
  echo "episodes=10000" >> "$GITHUB_OUTPUT"
  echo "ablation_scenarios=2000" >> "$GITHUB_OUTPUT"
  echo "bootstrap_replicates=500" >> "$GITHUB_OUTPUT"
fi
