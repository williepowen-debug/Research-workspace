#!/usr/bin/env python3
"""One-off grader for BND-25 (belly-led 9/16 session) and BND-26 (1y1y >= 4.95 any session 9/16..9/23), FRED H.15 primary, cache-busted."""
import urllib.request, time, sys
S=['DGS1MO','DGS3MO','DGS6MO','DGS1','DGS2','DGS3','DGS5','DGS7','DGS10','DGS20','DGS30']
def pull(s):
    u=f"https://fred.stlouisfed.org/graph/fredgraph.csv?id={s}&cosd=2026-09-10&_={int(time.time())}"
    rows=[l.split(',') for l in urllib.request.urlopen(u,timeout=30).read().decode().strip().split('\n')[1:]]
    return {d:(float(v) if v!='.' else None) for d,v in rows}
data={s:pull(s) for s in S}
dates=sorted(set().union(*[set(v) for v in data.values()]))
print('frontier per series:', {s:max(d for d,v in data[s].items() if v is not None) for s in S})
if '2026-09-16' in data['DGS10'] and data['DGS10']['2026-09-16'] is not None:
    d=[ (s, data[s]['2026-09-16']-data[s]['2026-09-15']) for s in S if data[s].get('2026-09-15') is not None and data[s].get('2026-09-16') is not None]
    print('Δ 9/15→9/16 (bp):', [(s, round(x*100,1)) for s,x in d])
    mx=max(abs(x) for _,x in d); winners=[s for s,x in d if abs(abs(x)-mx)<1e-9]
    belly={'DGS2','DGS3','DGS5'}
    print('BND-25: max |Δ| =', round(mx*100,1),'bp at', winners, '→', 'TRUE' if winners and all(w in belly for w in winners) else 'FALSE', '(letter: every tenor attaining the largest absolute one-session change lies in {DGS2,DGS3,DGS5})')
else:
    print('BND-25: 9/16 DGS cells NOT published — not gradeable')
for dt in [x for x in dates if '2026-09-16'<=x<='2026-09-23']:
    a,b=data['DGS1'].get(dt),data['DGS2'].get(dt)
    if a is not None and b is not None:
        f=2*b-a; print(f'BND-26 {dt}: 1y1y = 2*{b}-{a} = {f:.2f}', '→ ≥4.95 ⇒ FALSE' if round(f,2)>=4.95 else 'ok (<4.95)')
