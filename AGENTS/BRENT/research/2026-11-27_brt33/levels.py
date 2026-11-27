# Levels at the 11/27 last bar (capture tag argv[1]) vs the 11/26 night capture f1 (last trade) and the vendor 11/25 daily close.
import json, sys
T=sys.argv[1] if len(sys.argv)>1 else 'g1'
B='AGENTS/BRENT/research/'
def last(tag,dirn,s,day=None):
    d=json.load(open(f'{B}{dirn}/raw/{tag}_{s}.json'))
    m=[r for r in d['m1'] if r['volume']>0 and (day is None or r['label'].startswith(day))]
    return (m[-1]['label'][5:16],m[-1]['close']) if m else (None,None)
def daily(tag,dirn,s,date):
    d=json.load(open(f'{B}{dirn}/raw/{tag}_{s}.json'))['daily']
    x=[r['close'] for r in d if r['date']==date]; return x[0] if x else None
syms=['BZF27.NYM','BZG27.NYM','BZH27.NYM','CLF27.NYM','CLG27.NYM','CLH27.NYM','HOF27.NYM','HOG27.NYM','RBF27.NYM','BZ=F']
out={}
for s in syms:
    lt,lv=last(T,'2026-11-27_brt33',s,'2026-11-27')
    d25=daily(T,'2026-11-27_brt33',s,'2026-11-25')
    try: f1=json.load(open(f'{B}2026-11-26_jazan-refinery/raw/f1_{s}.json'))['daily']; d26=[r['close'] for r in f1 if r['date']=='2026-11-26']; d26=d26[0] if d26 else None
    except Exception: d26=None
    out[s]=dict(last_time=lt,last=lv,daily_1125=d25,daily_1126_from_f1=d26)
    print(s,lt,round(lv,4) if lv else None,'d25',d25,'d26(f1)',d26)
L={k:v['last'] for k,v in out.items()}
x=dict(M1M3=L['BZF27.NYM']-L['BZH27.NYM'],M1M2=L['BZF27.NYM']-L['BZG27.NYM'],M2M3=L['BZG27.NYM']-L['BZH27.NYM'],
 WTI_M1M3=L['CLF27.NYM']-L['CLH27.NYM'],HO_CL_Jan=L['HOF27.NYM']*42-L['CLF27.NYM'],HO_CL_Feb=L['HOG27.NYM']*42-L['CLG27.NYM'],
 RB_CL_Jan=L['RBF27.NYM']*42-L['CLF27.NYM'],c321_Jan=(2*L['RBF27.NYM']*42+L['HOF27.NYM']*42)/3-L['CLF27.NYM'],
 HO_BZG_Feb=L['HOG27.NYM']*42-L['BZG27.NYM'],BZG_CLG=L['BZG27.NYM']-L['CLG27.NYM'])
for k,v in x.items(): print(k,round(v,4))
json.dump(dict(levels=out,derived=x),open(f'{B}2026-11-27_brt33/levels_{T}.json','w'),indent=1)
