"""Reproduce evidence preparation from captured sources; never grade or write live ledgers."""
from pathlib import Path
from datetime import datetime,date,timezone
import csv,json,hashlib,sys
P=Path(__file__).resolve().parent;SAM=P.parents[2];R=P/'raw'
sys.path.insert(0,str(SAM/'scripts'));import cftc_jpy
legacy=cftc_jpy.parse_jpy_fields(cftc_jpy.find_jpy_row((R/'cftc-legacy.txt').read_text()))
f=cftc_jpy.find_jpy_row((R/'cftc-tff.txt').read_text()); cohorts=[]
for name,i,di in [('Dealer',8,25),('Asset manager',11,28),('Leveraged funds',14,31),('Other reportables',17,34)]:
 l,s,spread=map(int,f[i:i+3]);dl,ds,dsp=map(int,f[di:di+3]);cohorts.append(dict(cohort=name,long=l,short=s,spread=spread,net=l-s,delta_long=dl,delta_short=ds,delta_spread=dsp,delta_net=dl-ds))
assert legacy['date']==f[2]=='2026-09-01' and legacy['oi']==int(f[7])
# Same report's five populations including spreading must reconcile to OI on BOTH sides.
assert sum(x['long']+x['spread'] for x in cohorts)+int(f[22])==legacy['oi']
assert sum(x['short']+x['spread'] for x in cohorts)+int(f[23])==legacy['oi']
ust={datetime.strptime(r['Date'],'%m/%d/%Y').date().isoformat():float(r['3 Mo']) for r in csv.DictReader((R/'u-s-treasury.csv').open())}
px={}
for name in ['6ju26','6jz26','6jh27','fxy','usdjpy','eurjpy','audjpy','sp500']:
 px[name]={r['Date'][:10]:r for r in csv.DictReader((R/(name+'-daily.csv')).open())}
# Exchange values transcribed from CME Sep-8 FINAL bulletin 172, p1; retrieval via browser.
settlements={'6ju26':.0065110,'6jz26':.0065570,'6jh27':.0066035}
settlement_errors={n:float(px[n]['2026-09-08']['Close'])-v for n,v in settlements.items()}
assert max(abs(v) for v in settlement_errors.values())<.00000051  # Yahoo rounds the March half-point up; preserve the discrepancy.
def pair(n,f):
 out=[]
 for d in sorted(set(px[n])&set(px[f])&set(ust)):
  near,far=float(px[n][d]['Close']),float(px[f][d]['Close']);implied=(far/near-1)*365/91*100
  out.append(dict(date=d,near=near,far=far,near_volume=int(px[n][d]['Volume']),far_volume=int(px[f][d]['Volume']),implied_pct=implied,bill_pct=ust[d],assumed_jpy_pct=1.0,residual_bp=(implied-(ust[d]-1))*100))
 return out
old,new=pair('6ju26','6jz26'),pair('6jz26','6jh27')
with (P/'candidate-pair-observations.csv').open('w') as o:
 w=csv.DictWriter(o,fieldnames=list(new[0]));w.writeheader();w.writerows(new)
vix={datetime.strptime(r['DATE'],'%m/%d/%Y').date().isoformat():float(r['CLOSE']) for r in csv.DictReader((R/'vix.csv').open())}
dates=sorted(d for d in vix if '2026-06-22'<=d<='2026-09-09');episodes=[]
for i,d in enumerate(dates):
 if not i:continue
 prev=dates[i-1];r={'date':d,'previous_vix_date':prev,'vix_close':vix[d],'vix_delta':vix[d]-vix[prev],'vix_pct':(vix[d]/vix[prev]-1)*100}
 for name in ['fxy','usdjpy','eurjpy','audjpy','sp500']:
  r[name+'_vendor_daily_pct']=None if not (d in px[name] and prev in px[name]) else (float(px[name][d]['Close'])/float(px[name][prev]['Close'])-1)*100
 episodes.append(r)
with (P/'episode-screen.csv').open('w') as o:
 w=csv.DictWriter(o,fieldnames=list(episodes[0]));w.writeheader();w.writerows(episodes)
fxy=px['fxy'];start=float(fxy['2026-06-22']['Close']);lastday=max(fxy)
fxyr=[]
for a,b in zip(sorted(fxy),sorted(fxy)[1:]):fxyr.append({'date':b,'previous_date':a,'return_pct':(float(fxy[b]['Close'])/float(fxy[a]['Close'])-1)*100})
original_rows=[]
for r in csv.reader((SAM/'thesis/PREDICTIONS.tsv').open(),delimiter='\t'):
 if r and r[0] in ['SAM-28','SAM-31']:original_rows.append(r)
(P/'prediction-rows-frozen.json').write_text(json.dumps({'source':'thesis/PREDICTIONS.tsv','sha256':hashlib.sha256((SAM/'thesis/PREDICTIONS.tsv').read_bytes()).hexdigest(),'rows':original_rows},indent=2,ensure_ascii=False)+'\n')
result={'settlement_errors_usd_per_jpy':settlement_errors,'official_candidate_sep8_residual_bp':((settlements['6jh27']/settlements['6jz26']-1)*365/91*100-(ust['2026-09-08']-1))*100,'cftc_legacy':legacy,'cftc_tff':cohorts,'pair_tenor_days':(date(2027,3,15)-date(2026,12,14)).days,'candidate_last':new[-1],'candidate_sep8':next(r for r in new if r['date']=='2026-09-08'),'old_sep8':next(r for r in old if r['date']=='2026-09-08'),'matched_candidate_observations':len(new),'top_vix_delta_screens':sorted(episodes,key=lambda r:r['vix_delta'],reverse=True)[:8],'largest_fxy_daily_rises':sorted(fxyr,key=lambda r:r['return_pct'],reverse=True)[:5],'fxy_start_close':start,'fxy_last_date':lastday,'fxy_last_close':float(fxy[lastday]['Close']),'fxy_start_to_last_pct':(float(fxy[lastday]['Close'])/start-1)*100,'warning':'SCREENS ONLY. Daily clocks differ; no route qualification or prediction grade. No new VIX threshold or return baseline adopted.'}
(P/'analysis.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
