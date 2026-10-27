"""Frozen chronological method comparison, using captured primary SEC indexes only."""
from pathlib import Path
import json,csv,datetime,statistics
HERE=Path(__file__).resolve().parent
D=datetime.date.fromisoformat
rows=json.loads((HERE/'sources/GOOGL-index.json').read_text())
hist=sorted([(D(r['reportDate']),D(r['filingDate']),r['accessionNumber']) for r in rows if r['form']=='10-Q'])
events=sorted({D(r['filingDate']) for r in rows if r['form']=='8-K' and '2.02' in r['items']})
records=[]
for i,(period,filed,acc) in enumerate(hist):
 prior=hist[:i]
 if len(prior)<3: continue
 lag=(filed-period).days; minimum=min((fd-pe).days for pe,fd,_ in prior)
 same=[(fd-pe).days for pe,fd,_ in prior if pe.month==period.month]
 after=sorted(e for e in events if period<=e<=filed)
 release=after[0] if after else None
 records.append(dict(period_end=period.isoformat(),filed=filed.isoformat(),accession=acc,prior_n=len(prior),actual_lag_days=lag,legacy_min_days=minimum,legacy_missed_days=max(0,minimum-lag),same_quarter_prior_n=len(same),same_quarter_min_days=min(same) if len(same)>=3 else '',same_quarter_missed_days=max(0,min(same)-lag) if len(same)>=3 else '',quarter_close_watch_lead_days=lag,actual_8k_detected_on=release.isoformat() if release else '',actual_8k_lead_days=(filed-release).days if release else ''))
with (HERE/'CADENCE_ROLLING.tsv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(records[0]),delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(records)
recent=json.loads((HERE/'sources/GOOGL-submissions.json').read_text())['filings']['recent']
rh=sorted([(D(pe),D(fd)) for form,pe,fd in zip(recent['form'],recent['reportDate'],recent['filingDate']) if form=='10-Q'])
summary={'full_quarterly_observations':len(hist),'first_period':str(hist[0][0]),'last_period':str(hist[-1][0]),'chronological_tests':len(records),'legacy_min_failures':[r for r in records if r['legacy_missed_days']>0],'same_quarter_eligible':sum(r['same_quarter_min_days']!='' for r in records),'same_quarter_failures':[r for r in records if r['same_quarter_missed_days']!='' and r['same_quarter_missed_days']>0],'calendar_watch_cases':len(records),'calendar_watch_lead_range_days':[min(r['quarter_close_watch_lead_days'] for r in records),max(r['quarter_close_watch_lead_days'] for r in records)],'calendar_watch_is_prediction':False,'actual_8k_cases':sum(r['actual_8k_lead_days']!='' for r in records),'actual_8k_is_announced_schedule_backtest':False,'recent_n':len(rh),'latest_lag_days':(rh[-1][1]-rh[-1][0]).days,'prior_recent_min_days':min((fd-pe).days for pe,fd in rh[:-1])}
(HERE/'CADENCE_RESULTS.json').write_text(json.dumps(summary,indent=2));print(json.dumps(summary,indent=2))
