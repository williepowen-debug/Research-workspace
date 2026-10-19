"""Independent re-derivation from saved raw prices and row-level exports."""
from pathlib import Path
from datetime import datetime, timezone
from zoneinfo import ZoneInfo
import csv,json,statistics
D=Path(__file__).resolve().parent
j=json.loads((D/'analysis.json').read_text())
ny=ZoneInfo('America/New_York')
def series(s):
    z=json.loads((D/'raw'/f'chart-{s}.json').read_text())['chart']['result'][0]
    return {datetime.fromtimestamp(t,ny).date().isoformat():p for t,p in zip(z['timestamp'],z['indicators']['adjclose'][0]['adjclose']) if p is not None and datetime.fromtimestamp(t,ny).date().isoformat()<=j['end']}
p=series('SPY');r=series('RSP');ds=sorted(p);checked=0
for study in j['studies'].values():
    for arm,events in study['events'].items():
        indexes=[]
        for e in events:
            i=ds.index(e['date']);indexes.append(i)
            for h,x in e['outcomes'].items():
                h=int(h);v=[p[d] for d in ds[i:i+h+1]]
                ret=100*(v[-1]/v[0]-1)
                # All running-prefix maxima, rather than the implementation's streaming peak.
                dd=100*min(v[k]/max(v[:k+1])-1 for k in range(len(v)))
                assert abs(ret-x['return_pct'])<1e-9
                assert abs(dd-x['max_closing_drawdown_pct'])<1e-9
                assert abs(100*(min(v)/v[0]-1)-x['min_return_from_entry_pct'])<1e-9
                checked+=1
        assert all(b-a>=126 for a,b in zip(indexes,indexes[1:]))
phases={}
for n in [20,60]:
    gaps=[]
    first=next(i for i in range(n,len(ds)-126) if all(d in r for d in ds[i-n:i+1]))
    for phase in range(126):
        arms={True:[],False:[]};next_i={True:first+phase,False:first+phase}
        for i in range(first+phase,len(ds)-126):
            a,b=ds[i-n],ds[i]
            if a not in r or b not in r:continue
            cap=p[b]/p[a]-1
            if cap<=0:continue
            narrow=(r[b]/r[a])/(1+cap)-1<0
            if i<next_i[narrow]:continue
            arms[narrow].append(100*(p[ds[i+63]]/p[b]-1));next_i[narrow]=i+126
        gaps.append(statistics.mean(arms[True])-statistics.mean(arms[False]))
    phases[str(n)]={'posthoc_sampling_sensitivity':True,'phase_count':126,
                    'narrow_minus_broad_63session_mean_min_pp':min(gaps),
                    'max_pp':max(gaps),'negative_phases':sum(v<0 for v in gaps)}
q=json.loads((D/'quality-screen.json').read_text());rows=list(csv.DictReader((D/'quality-screen-stocks.csv').open()))
quality_validation={}
for w in q['results']:
    n=w['sessions'];gg={}
    for x in rows:
        if int(x['sessions'])==n:
            gg.setdefault(x['sector'],{}).setdefault(x['qual_member'],[]).append(float(x['raw_price_return_pct']))
    vals=[]
    for sec,g in gg.items():
        if sec in ['XLF','XLRE'] or not all(k in g for k in ['True','False']):continue
        vals.append(statistics.mean(g['True'])-statistics.mean(g['False']))
    assert abs(statistics.mean(vals)-w['nonfinancial_nonREIT_sector_mean_gap_pp'])<1e-9
    quality_validation[str(n)]={'sectors':len(vals),'leave_one_sector_out_min_pp':min(statistics.mean(vals[:i]+vals[i+1:]) for i in range(len(vals))),
                                'leave_one_sector_out_max_pp':max(statistics.mean(vals[:i]+vals[i+1:]) for i in range(len(vals)))}
assert all(x['up']+x['down']+x['flat']==x['coverage'] for x in j['breadth_daily'])
assert all(x['maximum_relative_difference']==0 for x in j['same_vendor_retrieval_crosscheck'].values())
out={'asof':datetime.now(timezone.utc).isoformat(),'outcome_horizons_independently_recomputed':checked,
     'forward_returns_drawdowns_spacing':'PASS','breadth_partitions':'PASS',
     'same_vendor_recent_history_crosscheck':'PASS; not independent source',
     'posthoc_phase_sensitivity':phases,'quality_csv_recomputation':'PASS','quality_sensitivity':quality_validation,
     'threshold_correction':'At-least20bp sensitivity uses >=20; reviewer-found initial >20 changed, main sample unchanged.',
     'limits':'Calculation validation is not validation of a predictive or causal model.'}
(D/'validation.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
