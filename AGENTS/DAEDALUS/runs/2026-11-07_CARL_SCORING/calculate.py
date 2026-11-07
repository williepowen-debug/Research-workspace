#!/usr/bin/env python3
"""One-off reproducible arithmetic for the authorized November 7 CARL review.
Not a new standing checker, grading rule, or replacement for CARL's ledger.
Run from the Git root. Reads the committed pin in INPUTS.json, never moving HEAD.
"""
import hashlib
import json
import re
import subprocess
from decimal import Decimal as D
from pathlib import Path

HERE = Path(__file__).resolve().parent
meta = json.loads((HERE / 'INPUTS.json').read_text())
ledger = 'AGENTS/CARL/thesis/PREDICTIONS.tsv'
raw = subprocess.check_output(['git', 'show', meta['pin'] + ':' + ledger])
assert hashlib.sha256(raw).hexdigest() == next(x['sha256'] for x in meta['inputs'] if x['path'] == ledger)
lines = [(n, l.split('\t')) for n, l in enumerate(raw.decode().splitlines(), 1) if l and not l.startswith('#')]
header = lines[0][1]
rows = [(n, dict(zip(header, cells))) for n, cells in lines[1:]]
assert all(len(cells) == len(header) for _, cells in lines)
original = {'CRL-01':75,'CRL-03':90,'CRL-04':88,'CRL-07':80,'CRL-08':85,'CRL-09':75,'CRL-11':85,'CRL-16':60,'CRL-18':60,'CRL-21':60,'CRL-24':60}
provenance = {
 'CRL-01':('91c301279','AGENTS/CARL/workbook/PREDICTIONS.tsv','CRL-01'),
 'CRL-03':('4e8c98359','AGENTS/CARL/STATUS.md','Fannie MF DQ >0.80%'),
 'CRL-04':('4e8c98359','AGENTS/CARL/STATUS.md','Student 90+ >10%'),
 'CRL-07':('9e30a573c1','AGENTS/CARL/workbook/PREDICTIONS.tsv','CRL-07'),
 'CRL-08':('9e30a573c1','AGENTS/CARL/workbook/PREDICTIONS.tsv','CRL-08'),
 'CRL-09':('9220f8917','AGENTS/CARL/STATUS.md','| CRL-09 |'),
 'CRL-11':('3427660fc','AGENTS/CARL/STATUS.md','| CRL-11 |'),
 'CRL-16':('bf073316af','AGENTS/CARL/thesis/PREDICTIONS.tsv','CRL-16'),
 'CRL-18':('41a3ba284e','AGENTS/CARL/thesis/PREDICTIONS.tsv','CRL-18'),
 'CRL-21':('41a3ba284e','AGENTS/CARL/thesis/PREDICTIONS.tsv','CRL-21'),
 'CRL-24':('6e748c97e1','AGENTS/CARL/thesis/PREDICTIONS.tsv','CRL-24'),
 'CRL-15':('bf073316af','AGENTS/CARL/thesis/PREDICTIONS.tsv','CRL-15'),
 'CRL-23':('af5ed9a7f3','AGENTS/CARL/thesis/PREDICTIONS.tsv','CRL-23')}
evidence = {}
for id_, (commit, path, needle) in provenance.items():
 blob = subprocess.check_output(['git','show',commit+':'+path])
 matches = [(n,l) for n,l in enumerate(blob.decode().splitlines(),1) if needle in l]
 assert len(matches) == 1, (id_,matches)
 evidence[id_] = {'commit':subprocess.check_output(['git','rev-parse',commit],text=True).strip(), 'commit_time':subprocess.check_output(['git','show','-s','--format=%cI',commit],text=True).strip(), 'path':path,'blob_sha256':hashlib.sha256(blob).hexdigest(),'line':matches[0][0],'text':matches[0][1]}
scored=[]; excluded=[]
for line,r in rows:
 id_=r['Pred_ID']
 if r['Status'] not in ('CONFIRMED','MISSED'):
  excluded.append({'id':id_,'status':r['Status']}); continue
 p=D(re.search(r'(\d+)%',r['Confidence']).group(1))/100
 p0=D(original[id_])/100; y=D(r['Status']=='CONFIRMED')
 scored.append({'id':id_,'line':line,'outcome':int(y),'original_probability':str(p0),'eligible_scoring_probability':str(p),'original_loss':str((p0-y)**2),'eligible_loss':str((p-y)**2)})
assert {r['id'] for r in scored} == set(original)
assert next(r for r in scored if r['id']=='CRL-21')['eligible_scoring_probability']=='0.6'
summary={'n':len(scored),'hits':sum(r['outcome'] for r in scored),'misses':sum(1-r['outcome'] for r in scored)}
for label,col in [('original','original_loss'),('eligible','eligible_loss')]:
 s=sum(D(r[col]) for r in scored);summary[label+'_sum']=str(s);summary[label+'_mean']=str(s/len(scored))
summary['before_CRL21_60_restore_same_cohort']=str((D(summary['eligible_sum'])-D('.36')+D('.0625'))/len(scored))
summary['constant_50_percent_brier']='0.25'
summary['limitations']='Existing outcome grades retained, not independently source-regraded. Original series includes earliest-known CRL11 (not proved Date_Made) and changed-question lineages CRL07/08. OPEN CRL15/23 excluded. MIXED is not assigned 0.5.'
out={'pin':meta['pin'],'summary':summary,'scored':scored,'excluded':excluded,'historical_evidence':evidence,'open_marks':[{'id':'CRL-15','first_call':'0.65','undated_intermediate':'0.35','dated_2026_11_06':'0.10','outcome':None},{'id':'CRL-23','first_call':'0.70','undated_intermediate':'0.45','dated_2026_11_06':'0.15','outcome':None}]}
(HERE/'RESULTS.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(summary,indent=2))
