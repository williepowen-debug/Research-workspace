"""Build UFB (RSSD 391575) quarterly funding table 12/31/2023-9/30/2026.
Sources: 12/2023-6/2026 from PROME/reports/2026-11-11_united-fidelity-follow-up/F-quarterly-history.json
(FFIEC CDR bulk rows); 6/30 and 9/30/2026 from DEWEY's own SDF parse research/2026-11-11_united-fidelity/*-rows.json.
Run from AGENTS/DEWEY:  python3 research/2026-11-16_ufb-brokered-funding/build_table.py
"""
import json
H=json.load(open('../../PROME/reports/2026-11-11_united-fidelity-follow-up/F-quarterly-history.json'))
def sdf(p):
    rows=json.load(open(p)); return {r[2]:r[3] for r in rows[1:]}
S630=sdf('research/2026-11-11_united-fidelity/20260630-rows.json')
S930=sdf('research/2026-11-11_united-fidelity/20260930-rows.json')
Q=['12-31-2023','03-31-2024','06-30-2024','09-30-2024','12-31-2024','03-31-2025','06-30-2025','09-30-2025','12-31-2025','03-31-2026','06-30-2026','09-30-2026']
data={q:(H[q] if q in H else S930) for q in Q}
codes=['RCON2365','RCONHK05','RCONHK06','RCONK220','RCONJH83','RCONK223','RCONMT87','RCONMT89','RCONMT91','RCONMT93','RCONMT95','RCON2200','RCFN2200','RCON5597','RCFDF055','RCFDF056','RCFDF057','RCFDF058','RCFD2651','RCFDF060','RCFDF061','RCFDF062','RCFDF063','RCFDB571','RCFD3190','RCONB993','RCFDB995','RCFD0081','RCFD0071','RCFD0010','RCONB987','RCFDB989','RCFD1754','RCFD1771','RCFD1773','RCFD0416','RCFDJA22','RCFD2170','RCONHK07','RCONHK08','RCONHK11','RCONK222','RCONHK12','RCON6648','RCONJ473','RCONJ474','RCON2215','RCON2385','RCON6810','RCON0352']
# 6/30/2026 cross-check: history file vs own SDF
mism=[c for c in codes if c in S630 and str(H['06-30-2026'].get(c))!=str(S630.get(c))]
print('6/30 history-vs-SDF mismatches:', mism)
def v(q,c):
    x=data[q].get(c); return None if x in (None,'','CONF') else int(x)
out={q:{c:v(q,c) for c in codes} for q in Q}
for q in Q: out[q]['_updated']=data[q].get('Last Date/Time Submission Updated On') or '2026-10-30 (SDF last update)'
json.dump(out,open('research/2026-11-16_ufb-brokered-funding/table.json','w'),indent=1)
m=lambda x: '' if x is None else f'{x/1000:,.1f}'
print('quarter | 2365 brok | HK06 brok<=1y | JH83 recip | K223 listing | MT91+93 sweeps | MT95 nonbrok sweeps | dep total | 5597 unins | FHLB | oth borr | 3190 | 0010 cash | sec HTMamort+AFS | 0416 pledged | assets | HK11+K222 TD<=1y')
for q in Q:
    o=out[q]; fh=sum(o[c] or 0 for c in ['RCFDF055','RCFDF056','RCFDF057','RCFDF058']); ob=sum(o[c] or 0 for c in ['RCFDF060','RCFDF061','RCFDF062','RCFDF063'])
    sec=(o['RCFD1754'] or 0)+(o['RCFD1773'] or 0)
    print(q, m(o['RCON2365']),m(o['RCONHK06']),m(o['RCONJH83']),m(o['RCONK223']),m((o['RCONMT91'] or 0)+(o['RCONMT93'] or 0)+(o['RCONMT87'] or 0)+(o['RCONMT89'] or 0)),m(o['RCONMT95']),m(o['RCON2200']+o['RCFN2200']),m(o['RCON5597']),m(fh),m(ob),m(o['RCFD3190']),m(o['RCFD0010']),m(sec),m(o['RCFD0416']),m(o['RCFD2170']),m(o['RCONHK11']+o['RCONK222']),sep=' | ')
