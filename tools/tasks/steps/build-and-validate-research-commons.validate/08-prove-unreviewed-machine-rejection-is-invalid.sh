set +e
output=$(python research_commons/tools/validate_published_research_graph.py --graph research_commons/published_research_graph/fixtures/invalid-machine-rejected-without-review.json 2>&1)
status=$?
set -e
printf '%s\n' "$output"
test "$status" -ne 0
printf '%s\n' "$output" | grep -F "machine-discovered rejected relation RC-REL-FIXTURE-UNREVIEWED-REJECTION requires rejected review evidence"
