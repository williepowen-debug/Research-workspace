import sys,pathlib,datetime
sys.path.insert(0,'AGENTS/REGINALD/scripts')
import mi3_cohort_screen as m
R={t:r for t,r,*_ in m.COHORT}
Q=['9/30/2025','12/31/2025','3/31/2026','6/30/2026','9/30/2026']
def f(r,q): return m.parse(pathlib.Path(f"/tmp/mi3/fac/{r}_{q.replace('/','-')}.sdf").read_text(errors='replace'))
out=[]
for t,r in R.items():
    d={q:f(r,q) for q in Q}
    co25=d['12/31/2025'].get('RIADC079')-d['9/30/2025'].get('RIADC079'); wd25=d['12/31/2025'].get('RIAD5523',0)-d['9/30/2025'].get('RIAD5523',0)
    co=co25+d['9/30/2026']['RIADC079']; wd=wd25+d['9/30/2026'].get('RIAD5523',0)
    a=d['9/30/2026']['RIAD3123']; out.append((a/co,a/(co+wd),t,wd,co))
    if t in('FLG','EGBN','WAL'): print(t,'Q3 alone CO',d['9/30/2026']['RIADC079']-d['6/30/2026']['RIADC079'],'prov',d['9/30/2026']['RIAD4230']-d['6/30/2026']['RIAD4230'],'wd ytd',d['9/30/2026'].get('RIAD5523',0))
for x in sorted(out): print(f"{x[2]} {x[0]:.2f} incl write-downs {x[1]:.2f} wdTTM {x[3]}")
