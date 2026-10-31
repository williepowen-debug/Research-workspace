#!/usr/bin/env python3
"""C5 ->5 long-series base rate (AEOLUS, 2026-10-31).
usage: python3 -I base_rate.py <kaub.csv> <duisburgruhrort.csv> [daily_out.csv]
Daily mean = mean of that LOCAL calendar day's 15-min readings, UNROUNDED; a day with <90 readings is INCOMPLETE and
skipped (never a miss). Joint 3-day test = both legs at/below on 3 consecutive complete days (the registered C5 ->5 rule)."""
import sys
from collections import defaultdict
def daily(path):
    s=defaultdict(float); n=defaultdict(int)
    with open(path) as f:
        next(f)
        for line in f:
            ts,v=line.strip().split(';'); s[ts[:10]]+=float(v); n[ts[:10]]+=1
    return {d:(s[d]/n[d],n[d]) for d in s}
K=daily(sys.argv[1]); D=daily(sys.argv[2]); days=sorted(set(K)&set(D))
if len(sys.argv)>3:
    with open(sys.argv[3],'w') as f:
        f.write('date,kaub_mean_cm,kaub_n,duisburg_ruhrort_mean_cm,duisburg_ruhrort_n\n')
        for d in days: f.write(f'{d},{K[d][0]:.3f},{K[d][1]},{D[d][0]:.3f},{D[d][1]}\n')
comp=[d for d in days if K[d][1]>=90 and D[d][1]>=90]
PAIRS=[(25,153,'NNW record lows (REGISTERED)'),(30,160,''),(35,170,''),(40,180,'Contargo top tier K40 / oblig-end D180'),
       (50,190,''),(65,201,'MNW (mean annual low)'),(77,227,'GlW (navigation reference)')]
print('pair | windows 2000-2025 | years with >=1 window (of 26) | 2026 windows')
for kt,dt,lab in PAIRS:
    w=[comp[i] for i in range(2,len(comp)) if all(K[x][0]<=kt and D[x][0]<=dt for x in comp[i-2:i+1])]
    pre=[x for x in w if x<'2026']; yrs=sorted(set(x[:4] for x in pre))
    print(f'K<={kt} D<={dt} {lab} | {len(pre)} | {len(yrs)} {",".join(yrs)} | {len(w)-len(pre)}')
for nm,st in (('Kaub',K),('Duisburg-Ruhrort',D)):
    pre=[d for d in days if d<'2026']; m=min(pre,key=lambda d:st[d][0])
    print(f'{nm} lowest daily mean 2000-2025: {st[m][0]:.3f} on {m}')
