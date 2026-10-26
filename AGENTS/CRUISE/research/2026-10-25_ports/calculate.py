"""Reproduce this dated pass's arithmetic; no network, schedules or state writes."""
import csv,json
from pathlib import Path
root=Path(__file__).resolve().parent
out=[]
for r in csv.DictReader((line for line in (root/'observations.tsv').open() if not line.startswith('#')),delimiter='\t'):
 r['key']=r['key'].strip()
 value,prior=float(r['value']),float(r['prior'])
 result={'key':r['key'],'value':value,'prior':prior,'change':value-prior,'yoy_pct':100*(value/prior-1),'unit':r['unit'],'source_id':r['source_id']}
 if r['budget']:result.update(budget=float(r['budget']),vs_budget_pct=100*(value/float(r['budget'])-1))
 out.append(result)
# Verify the two published calendar-YTD totals from the monthly inputs.
miami26=[992848,854529,1105472,935893,803422,818524,856560,850097,653705]
miami25=[866958,751399,917945,673583,532771,690294,609215,664394,549218]
assert sum(miami26)==7871050 and sum(miami25)==6255777
# A source-consistency check, NOT a replacement annual series.
fy25_splice=sum(miami25)+541781+797672+868921
quality={'miami_calendar_totals_match_monthly_sums':True,'miami_fy2025_monthly_splice_not_published_annual':fy25_splice,'miami_historical_page_fy2025':8564151,'miami_sept21_release_fy2025':8564225,'warning':'Monthly splice differs from both annual source figures; no fiscal-year reconstruction or cross-port sum is promoted.'}
print(json.dumps({'observations':out,'source_quality':quality},indent=2))
