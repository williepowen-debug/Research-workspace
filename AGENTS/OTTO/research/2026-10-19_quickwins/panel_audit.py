"""Re-read 15 relevant reports, save evidence and compute fixed matched-month comparisons."""
import concurrent.futures,csv,gzip,hashlib,importlib.util,json,pathlib
from decimal import Decimal as D
B=pathlib.Path(__file__).resolve().parent;desk=B.parents[1]
spec=importlib.util.spec_from_file_location('otto_panel',desk/'scripts/panel_10d.py');p=importlib.util.module_from_spec(spec);spec.loader.exec_module(p)
rows=list(csv.DictReader((desk/'workbook/PANEL_10D.tsv').open(),delimiter='\t'));lookup={(r['deal'],r['collection_period'][:7]):r for r in rows}
new=[r for r in rows if r['collection_period'].startswith('2026-09')]
jobs=[]
for r in new:
 for month in ['2025-09','2026-08','2026-09']:jobs.append(lookup[(r['deal'],month)])
def read(r):
 name=r['deal'].replace(' ','_')+'-'+r['collection_period'][:7];raw=p.fetch(r['source_url']).encode('utf-8');txt=p.flatten(raw.decode('utf-8'));(B/'sources'/(name+'.html.gz')).write_bytes(gzip.compress(raw,mtime=0));(B/'sources'/(name+'.txt')).write_text(txt)
 vals,miss=p.parse(txt,r['issuer']);d=p.derive(vals,r['issuer']);cp,cm=p.collection_period(txt);ms,mm=p.months_seasoned(txt,r['issuer']);assert cp==r['collection_period'] and str(ms)==r['months_seasoned']
 for k in ['dq_60plus_pct','cnl_pct','ext_rate_pct']:
  if r[k]:assert d[k] is not None and abs(D(str(d[k]))-D(r[k]))<=D('.01'),(name,k,d[k],r[k])
 return {'name':name,'url':r['source_url'],'sha256':hashlib.sha256(raw).hexdigest(),'filing_date':r['filing_date'],'collection_period':cp,'clock':ms,'dq':r['dq_60plus_pct'],'ext':r['ext_rate_pct'],'misses':miss}
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:manifest=list(ex.map(read,jobs))
(B/'panel_manifest.json').write_text(json.dumps(manifest,indent=2))
comps=[]
for r in new:
 prev=lookup[(r['deal'],'2026-08')];year=lookup[(r['deal'],'2025-09')]
 row={'deal':r['deal'],'tier':r['tier'],'period':'2026-09','dq':r['dq_60plus_pct'],'dq_aug':prev['dq_60plus_pct'],'dq_prior_sep':year['dq_60plus_pct'],'dq_mom_pp':str(D(r['dq_60plus_pct'])-D(prev['dq_60plus_pct'])),'dq_yoy_pp':str(D(r['dq_60plus_pct'])-D(year['dq_60plus_pct'])),'ext':r['ext_rate_pct'],'ext_aug':prev['ext_rate_pct'],'ext_prior_sep':year['ext_rate_pct'],'ext_mom_pp':str(D(r['ext_rate_pct'])-D(prev['ext_rate_pct'])) if r['ext_rate_pct'] else None,'ext_yoy_pp':str(D(r['ext_rate_pct'])-D(year['ext_rate_pct'])) if r['ext_rate_pct'] else None,'current_url':r['source_url'],'prior_sep_url':year['source_url']};comps.append(row)
counts=[]
for r in rows:
 month=r['collection_period'][:7]
 if '2026-04'<=month<='2026-09' and (r['deal'],'2025'+month[4:]) in lookup:
  yr=lookup[(r['deal'],'2025'+month[4:])]
  counts.append((r['deal'],month,str(D(r['dq_60plus_pct'])-D(yr['dq_60plus_pct']))))
means={t:str(sum(D(x['dq_yoy_pp']) for x in comps if x['tier']==t)/len([x for x in comps if x['tier']==t])) for t in ['BROAD','CARVANA']}
out={'new_rows':comps,'september_yoy_tier_means':means,'available_matched_months':counts,'worse_count':sum(D(x[2])>0 for x in counts),'total':len(counts),'source_checks':len(manifest),'turn':any(D(x['dq_yoy_pp'])<0 for x in comps) or any(D(v)<=0 for v in means.values()),'coverage':'September 5/9; Exeter 4/9 remains August, not September'}
(B/'panel_comparison.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
