"""CATO isolated freshness counterexamples. No network or owner-file mutation."""
import contextlib,io,json,tempfile,types,subprocess
from pathlib import Path
root=Path(__file__).resolve().parents[4]
source=root/'AGENTS/LABOR/scripts/spine_check.py'
m=types.ModuleType('labor_spine_probe');m.__file__=str(source);exec(compile(source.read_text(),str(source),'exec'),m.__dict__)
status=subprocess.check_output(['git','show','d8ef31719:AGENTS/LABOR/STATUS.md'],cwd=root,text=True)
dates={'ICSA':('2026-09-19',197000),'CCSA':('2026-09-12',1719000),'JTSHIL':('2026-08-01',5192),'FLUR':('2026-08-01',4.5)}
rows=status.splitlines()
jrow=next(l for l in rows if l.startswith('| JOLTS hires'))
frow=next(l for l in rows if l.startswith('| FL UR'))
stale=status.replace(jrow,jrow.replace('obs 2026-08-01','obs 2026-07-01'))
results={}
def run(name,txt,feed=None):
 with tempfile.TemporaryDirectory(prefix='cato_labor_spine_') as d:
  p=Path(d)/'STATUS.md';p.write_text(txt);m.STATUS=p;m.fred_newest=lambda sid:(feed or dates)[sid]
  parsed=m.status_obs_dates();s=io.StringIO()
  with contextlib.redirect_stdout(s):rc=m.main()
  results[name]={'rc':rc,'parsed':parsed,'relevant_output':[l.strip() for l in s.getvalue().splitlines() if any(x in l for x in ['JOLTS','FL UR','GATE PASS','GATE FAILED','GATE INCONCLUSIVE'])]}
run('current_status',status)
run('stale_jolts',stale)
run('stale_florida',status.replace(frow,frow.replace('obs 2026-08-01','obs 2026-07-01')))
run('missing_jolts_date',status.replace(jrow,jrow.replace('obs 2026-08-01','August')))
run('missing_florida_date',status.replace(frow,frow.replace('obs 2026-08-01','August')))
run('stale_jolts_plus_history',stale+'\n## Prior source check\nJOLTS hires source retrieved: obs 2026-08-01; current table reconciliation still owed.\n')
run('stale_jolts_plus_other_series_same_line',stale.replace('obs 2026-07-01 · BLS','obs 2026-07-01; FL UR obs 2026-08-01 · BLS'))
run('stale_florida_plus_history',status.replace(frow,frow.replace('obs 2026-08-01','obs 2026-07-01'))+'\n## Prior source check\nFL UR source retrieved: obs 2026-08-01; current table reconciliation still owed.\n')
run('unverified_future_jolts_date',status.replace(jrow,jrow.replace('obs 2026-08-01','obs 2026-09-01')))
run('jolts_source_unavailable',status,{**dates,'JTSHIL':(None,'fixture unavailable')})
run('unrelated_history',stale+'\nUnemployment source retrieved: obs 2026-08-01.\n')
# Follow-up: row shape is not section/series identity.
run('missing_live_jolts_historical_row',status.replace(jrow,'')+'\n## HISTORICAL SOURCE EXTRACT — not reconciled\n'+jrow+'\n')
run('missing_live_florida_historical_row',status.replace(frow,'')+'\n## HISTORICAL SOURCE EXTRACT — not reconciled\n'+frow+'\n')
run('wrong_jolts_measure',status.replace(jrow,'| JOLTS hires rate | 3.3% [obs 2026-08-01] | no gross level read |'))
run('duplicate_identical_tokens',status.replace(jrow,jrow.replace('obs 2026-08-01','obs 2026-08-01; obs 2026-08-01')))
print(json.dumps(results,indent=2))
