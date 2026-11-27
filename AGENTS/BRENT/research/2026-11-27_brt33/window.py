# BRT-33 window read for one session from one capture: per-leg VWAP over [14:28,14:30) ET, positive-volume bars only (row letter).
import json, sys
T=sys.argv[1]; DAY=sys.argv[2] if len(sys.argv)>2 else '2026-11-27'
B='AGENTS/BRENT/research/2026-11-27_brt33/raw/'
res={}
for s in ['BZF27.NYM','BZG27.NYM','BZH27.NYM']:
    m=json.load(open(f'{B}{T}_{s}.json'))['m1']
    w=[r for r in m if r['label'].startswith(DAY+'T14:28') or r['label'].startswith(DAY+'T14:29')]
    pv=[r for r in w if r['volume']>0]
    vw=sum(r['close']*r['volume'] for r in pv)/sum(r['volume'] for r in pv) if pv else None
    last=[r['label'] for r in m if r['label'].startswith(DAY)]
    res[s]=dict(bars=w,vwap=vw,last_bar_of_day=last[-1] if last else None,n_day=len(last))
    print(s,'window bars',len(w),'positive',len(pv),'vwap',vw,'last bar',res[s]['last_bar_of_day'])
f,h=res['BZF27.NYM']['vwap'],res['BZH27.NYM']['vwap']
res['M1M3']=round(f-h,4) if f is not None and h is not None else None
res['valid']=res['M1M3'] is not None
print('M1M3',res['M1M3'],'valid',res['valid'])
json.dump(res,open(f'AGENTS/BRENT/research/2026-11-27_brt33/window_{T}.json','w'),indent=1)
