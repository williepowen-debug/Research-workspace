from pathlib import Path
import json,datetime as dt,csv,gzip,tarfile
P=Path(__file__).resolve().parent

def prices(s):
 f=P/f'raw/peer-{s}.json'
 if f.exists():data=f.read_text()
 else:
  with tarfile.open(P/'sources.tar.gz') as ar:data=ar.extractfile(f'raw/peer-{s}.json').read().decode()
 j=json.loads(data)['chart']['result'][0]
 return {dt.datetime.fromtimestamp(t,dt.timezone.utc).date().isoformat():v for t,v in zip(j['timestamp'],j['indicators']['adjclose'][0]['adjclose']) if v is not None}
starts={5:'2026-10-12',20:'2026-09-21',60:'2026-07-24'};end='2026-10-19';out=[]
for case,s in [('MOS','ICL'),('HII','FCT.MI'),('ADM','F34.SI'),('CPRT','ACVA')]:
 pr=prices(s);x={'case':case,'candidate':s,'observed_endpoint':pr.get(end),'local_currency_returns':{str(w):pr[end]/pr[d]-1 if end in pr and d in pr else None for w,d in starts.items()}}
 if s=='F34.SI':
  fx=prices('SGD=X');x['usd_returns']={str(w):(pr[end]/fx[end])/(pr[d]/fx[d])-1 if all(z in a for a in [pr,fx] for z in [d,end]) else None for w,d in starts.items()}
 if s=='ICL':
  raw=list(csv.DictReader(gzip.open(P.parent/'2026-10-19_repeat-losers/daily-audit.csv.gz','rt')))
  cond=[r for r in raw if r['symbol']=='MOS' and r['window']=='20' and r['both_up']=='True'];dates=sorted(r['date'] for r in raw if r['symbol']=='MOS' and r['window']=='20');grid=['2026-09-21']+dates
  missing=[d for d in grid if d not in pr];assert not missing
  losses=sum(pr[r['date']]<pr[grid[grid.index(r['date'])-1]] for r in cond);x['20_both_up_loss_fraction']=f'{losses}/{len(cond)}'
  x['disposition']='Return-strength passes20/60; MOS-mapped20BOTH loss fraction compared below. Primary6K retrieved only EPS-average shares, not a verified period-end economic-common count/security-unit proof. Size eligibility unresolved; not accepted control.'
 elif s=='FCT.MI':x['disposition']='October19 adjusted close null; no fill from metadata/unadjusted spot/October16. Primary half-year endpoint404. No comparable frozen endpoint or verified size; reject as usable control.'
 elif s=='F34.SI':x['disposition']='Foreign calendar/FX mismatch retained; primary half-year endpoint404. Compare observed USD returns, no verified formation size. Not accepted control.'
 else:x['disposition']='ACV acquired by CPRTOct16; already deal-affected beforeSep21formation, endpointnull. Not independent operating control; reject before strength/size selection.'
 out.append(x)
(P/'peer-audit.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
