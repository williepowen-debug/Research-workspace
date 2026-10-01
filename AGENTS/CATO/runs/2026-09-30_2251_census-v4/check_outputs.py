"""Independent arithmetic/coverage checks over saved exports; writes checks.json.
Usage: python3 -B check_outputs.py /path/to/v4/output
This checks author outputs, not external event truth or forecast eligibility.
"""
import collections
import csv
from decimal import Decimal as D
import hashlib
import io
import json
from pathlib import Path
import sys

HERE=Path(__file__).resolve().parent
out=Path(sys.argv[1])
def read(path): return list(csv.DictReader(io.StringIO(path.read_text()),delimiter='\t'))
def measured(s): return s not in ('','UNKNOWN')
def score(rs, field, outcome):
    if not rs: return {'n':0}
    pairs=[(D(r[field]),D(outcome(r))) for r in rs]
    n=D(len(pairs)); b=sum(y for p,y in pairs)/n; bs=sum((p-y)**2 for p,y in pairs)/n
    return {'n':len(pairs),'brier':float(bs),'base_rate':float(b),'baseline':float(b*(1-b))}

rows=read(out/'rows_v4.tsv')
old=read(HERE.parent/'2026-09-30_2251_census-v3-evidence/rows_v3.tsv')
key=lambda r:(r['desk'],r['pred_id'])
assert len(rows)==len({key(r) for r in rows})==534
assert {key(r) for r in rows}=={key(r) for r in old}
by_key={key(r):r for r in rows}
old_by_key={key(r):r for r in old}
meta=json.loads((out/'provenance_v4.json').read_text())
assert dict(collections.Counter(r['disposition'] for r in rows))==meta['dispositions']
assert hashlib.sha256((HERE/'census_v4.py').read_bytes()).hexdigest()==meta['script_sha256']
assert hashlib.sha256((HERE/'annotations.json').read_bytes()).hexdigest()==meta['annotations_sha256']
sources=[json.loads(l) for l in (out/'sources_v4.jsonl').read_text().splitlines()]
assert {key(r) for r in sources}=={key(r) for r in rows}
for r in rows:
    for f in ('p_current','p_recorded_grade','p_earliest_observed'):
        assert not measured(r[f]) or 0<=D(r[f])<=1
    if not r['disposition'].startswith('binary_'):
        assert all(r[f]=='UNKNOWN' for f in ('brier_current','brier_recorded','brier_earliest'))
    for p,b in [('p_current','brier_current'),('p_recorded_grade','brier_recorded'),('p_earliest_observed','brier_earliest')]:
        if measured(r[b]):
            assert measured(r[p]) and measured(r['outcome'])
            assert abs((D(r[p])-D(r['outcome']))**2-D(r[b]))<D('1e-12')
    if r['first_at_source_file_birth']=='1':
        source=next(s for s in sources if key(s)==key(r))['history_candidates'][0]
        assert source['commit']==source['file_birth_commit']

old_scored=[r for r in old if not r['exclusion_reason']]
old_first=[r for r in old_scored if measured(r['p_first_committed'])]
matched=[r for r in rows if measured(r['brier_current']) and measured(r['brier_earliest'])]
new_current=[r for r in rows if measured(r['brier_current'])]
new_recorded=[r for r in rows if measured(r['brier_recorded'])]
new_earliest=[r for r in rows if measured(r['brier_earliest'])]
metrics={
 'v3_current':score(old_scored,'p_scored',lambda r:'1' if r['class']=='CONFIRMED' else '0'),
 'v3_first':score(old_first,'p_first_committed',lambda r:'1' if r['class']=='CONFIRMED' else '0'),
 'v4_current':score(new_current,'p_current',lambda r:r['outcome']),
 'v4_recorded_subset':score(new_recorded,'p_recorded_grade',lambda r:r['outcome']),
 'v4_earliest_filtered':score(new_earliest,'p_earliest_observed',lambda r:r['outcome']),
 'matched_current':score(matched,'p_current',lambda r:r['outcome']),
 'matched_earliest':score(matched,'p_earliest_observed',lambda r:r['outcome']),
}
for view,k in [('current_cell_sensitivity','v4_current'),('recorded_grading_subset','v4_recorded_subset'),
 ('earliest_identity_usable_sensitivity','v4_earliest_filtered'),('matched_p_current','matched_current'),('matched_p_earliest_observed','matched_earliest')]:
    s=next(r for r in read(out/'summary_v4.tsv') if r['desk']=='FLEET' and r['view']==view)
    assert int(s['n'])==metrics[k]['n']
    assert abs(float(s['brier'])-metrics[k]['brier'])<1e-12

changed=[{'desk':r['desk'],'pred_id':r['pred_id'],'v3_first':old_by_key[key(r)]['p_first_committed'],
          'v4_earliest':r['p_earliest_observed'],'flags':r['history_flags']} for r in rows
         if measured(old_by_key[key(r)]['p_first_committed']) and measured(r['p_earliest_observed'])
         and D(old_by_key[key(r)]['p_first_committed'])!=D(r['p_earliest_observed'])]
result={'pin':meta['pin'],'population':len(rows),'dispositions':meta['dispositions'],'metrics':metrics,
 'changed_numeric_earliest':changed,
 'changed_first_commit_count':sum(not r['first_commit'].startswith(old_by_key[key(r)]['first_commit_sha']) for r in rows),
 'history_flags':dict(collections.Counter(f for r in rows for f in r['history_flags'].split(';'))),
 'current_scores_removed':[key(r) for r in old_scored if not measured(by_key[key(r)]['brier_current'])],
 'matched_rows_with_first_not_open':sum('first_seen_not_open' in r['history_flags'] for r in matched),
 'matched_rows_at_file_birth':sum(r['first_at_source_file_birth']=='1' for r in matched),
 'checks':'PASS: fixed population, source/script hashes, probability bounds, exclusion arithmetic and independent Decimal Brier recomputation.'}
(out/'checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
