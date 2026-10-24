python - <<'PY'
import json
p = json.load(open('generated/stegneuro-bci/candidate-sources.json'))
t = json.load(open('generated/stegneuro-bci/source-triage.json'))
g = json.load(open('generated/stegneuro-bci/gap-map.json'))
c = json.load(open('research_commons/runtime/STEGNEURO-BCI-001/continuation-latest.json'))
assert p['authority_effect'] == 'NONE'
assert p['auto_merge_into_registry'] is False
assert p['state'] == 'REVIEW_REQUIRED'
assert p['candidate_count'] > 0
assert t['authority_effect'] == 'NONE' and t['registry_effect'] == 'NONE'
assert g['authority_effect'] == 'NONE'
assert g['reviewed_source_count'] >= 19
assert set(i['classification'] for i in t['items']) <= {'ADMIT_SOURCE','REJECT_SOURCE','SUPERSEDED','DUPLICATE','RETRY'}
assert c['authority_effect'] == 'NONE' and c['registry_effect'] == 'NONE'
assert c['owner'] == 'StegVerse-Labs/StegScholar#50'
print('candidate discovery + triage + continuation: fail-closed')
PY
