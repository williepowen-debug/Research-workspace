"""Fixed L708 calculation; read saved closes with --replay, otherwise collect Yahoo history."""
import json,math,sys,pathlib,datetime
import numpy as np
BASE=pathlib.Path(__file__).resolve().parent
T=['ENVA','CVNA'];P=['2026-10-02','2026-10-05','2026-10-06','2026-10-07','2026-10-08','2026-10-09','2026-10-13'];S=['2026-09-25','2026-09-28','2026-09-29','2026-09-30','2026-10-01']
if '--replay' in sys.argv:data=json.loads((BASE/'closes.json').read_text())
else:
 import yfinance as yf
 data={}
 for t in T+['SPY']:
  h=yf.Ticker(t).history(start='2026-02-25',end='2026-10-14',auto_adjust=True).sort_index()
  data[t]={d.strftime('%Y-%m-%d'):float(c) for d,c in zip(h.index,h['Close']) if math.isfinite(c)}
 (BASE/'closes.json').write_text(json.dumps(data,indent=2))
cal=sorted(data['SPY']);fit=[d for d in cal if '2026-03-02'<=d<='2026-09-23']
assert len(fit)>130 and all(d in cal for d in P+S)
for t in T:assert all(d in data[t] for d in cal),'missing daily data '+t
prev=lambda d:cal[cal.index(d)-1]
ret=lambda t,a,b:data[t][b]/data[t][a]-1
out={'governing_n':0,'governing_verdict':'NO_INSTRUMENT','basis':'No verified in-window ICE membership join; conditional basket only','fit':{},'primary':{},'secondary':{},'oct13_two_day_sensitivity':{}}
def verdict(rows):
 n=len(rows);need=math.ceil(n/2)
 if n<2:return 'NO_INSTRUMENT'
 half=math.ceil(len(next(iter(rows.values())))/2)
 if sum(sum(z<=-1 for z in zs)>=half for zs in rows.values())>=need:return 'SUPPORTED'
 if sum(sum(abs(z)<=.3 for z in zs)>=half for zs in rows.values())>=need:return 'NOT SUPPORTED'
 return 'MIXED'
for t in T:
 r=np.array([ret(t,prev(d),d) for d in fit]);m=np.array([ret('SPY',prev(d),d) for d in fit]);b=float(np.cov(r,m,ddof=1)[0,1]/np.var(m,ddof=1));sig=float(np.std(r-b*m,ddof=1));assert sig>0
 out['fit'][t]={'beta':b,'sigma':sig,'n':len(fit),'first':fit[0],'last':fit[-1]}
 for label,ds in [('primary',P),('secondary',S)]:
  out[label][t]={d:{'return':ret(t,prev(d),d),'spy':ret('SPY',prev(d),d),'z':float((ret(t,prev(d),d)-b*ret('SPY',prev(d),d))/sig)} for d in ds}
 out['oct13_two_day_sensitivity'][t]=(ret(t,'2026-10-09','2026-10-13')-b*ret('SPY','2026-10-09','2026-10-13'))/(sig*math.sqrt(2))
for label in ['primary','secondary']:
 rows={t:[x['z'] for x in out[label][t].values()] for t in T};out[label+'_conditional_verdict']=verdict(rows)
 print(label,out[label+'_conditional_verdict'])
 for t,zs in rows.items():print(t,' '.join(f'{z:+.3f}' for z in zs),'negative-tail',sum(z<=-1 for z in zs),'near-zero',sum(abs(z)<=.3 for z in zs))
print('fit',out['fit']);print('October 13 two-day sensitivity',out['oct13_two_day_sensitivity'])
(BASE/'equity_result.json').write_text(json.dumps(out,indent=2))
