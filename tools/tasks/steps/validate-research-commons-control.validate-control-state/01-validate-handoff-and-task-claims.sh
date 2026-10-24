mkdir -p reports
python research_commons/tools/check_research_commons_control_state.py | tee reports/research-commons-control-state.json
