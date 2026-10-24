python - <<'PY'
from pathlib import Path
text = Path('scripts/complete_gtg_tasks.py').read_text(encoding='utf-8')
forbidden = (
    'api.github.com/repos/Admissible-Existence/ae-validation-factory',
    'GITHUB_TOKEN',
    'GH_TOKEN',
    'Authorization',
    'urllib.request',
)
found = [marker for marker in forbidden if marker in text]
assert not found, found
assert 'private_repository_queried' in text
assert 'github_token_required' in text
assert 'FACTORY_R4_ACTIVE_PINNED' in text
print('GTG_PINNED_EVIDENCE_ONLY=PASS')
PY
