# Daily-bar levels and spreads, Wed 11/25 vs Fri 11/27 (capture h1), with Thu 11/26 from the 11/26-night capture f1 (vendor last trade, not a settle).
import json
B='AGENTS/BRENT/research/'
syms=['BZF27.NYM','BZG27.NYM','BZH27.NYM','BZJ27.NYM','CLF27.NYM','CLG27.NYM','CLH27.NYM','HOF27.NYM','HOG27.NYM','RBF27.NYM','USO']
def d(tag,dirn,s,date):
    try: x=[r['close'] for r in json.load(open(f'{B}{dirn}/raw/{tag}_{s}.json'))['daily'] if r['date']==date]
    except Exception: return None
    return x[0] if x else None
L={}
for day,tag,dirn in [('2026-11-25','h1','2026-11-27_ras-tanura'),('2026-11-26','f1','2026-11-26_jazan-refinery'),('2026-11-27','h1','2026-11-27_ras-tanura')]:
    L[day]={s:d(tag,dirn,s,day) for s in syms}
def sp(v):
    g=lambda k:v.get(k)
    f=lambda a,b:(round(a-b,2) if a is not None and b is not None else None)
    return dict(BZF=g('BZF27.NYM'),BZG=g('BZG27.NYM'),CLF=g('CLF27.NYM'),CLG=g('CLG27.NYM'),
      BZ_M1M2=f(g('BZF27.NYM'),g('BZG27.NYM')),BZ_M2M3=f(g('BZG27.NYM'),g('BZH27.NYM')),BZ_GJ=f(g('BZG27.NYM'),g('BZJ27.NYM')),
      CL_GH=f(g('CLG27.NYM'),g('CLH27.NYM')),BZG_CLG=f(g('BZG27.NYM'),g('CLG27.NYM')),BZF_CLF=f(g('BZF27.NYM'),g('CLF27.NYM')),
      HOG_crack=(round(g('HOG27.NYM')*42-g('CLG27.NYM'),2) if g('HOG27.NYM') and g('CLG27.NYM') else None),
      HOG_vs_BZG=(round(g('HOG27.NYM')*42-g('BZG27.NYM'),2) if g('HOG27.NYM') and g('BZG27.NYM') else None),USO=g('USO'))
out={k:sp(v) for k,v in L.items()}
for k,v in out.items(): print(k,{a:(round(b,4) if isinstance(b,float) else b) for a,b in v.items()})
json.dump(dict(raw=L,spreads=out),open(B+'2026-11-27_ras-tanura/levels_h1.json','w'),indent=1)
