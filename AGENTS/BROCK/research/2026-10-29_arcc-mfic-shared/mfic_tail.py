"""MFIC 6/30/2026 first-SOI: where the below-cost value sits, by company group.
usage: python3 mfic_tail.py <scratch dir> <out dir>"""
import sys, re, collections, json
from pathlib import Path
exec(open(Path(__file__).with_name("compare.py")).read().split("arcc_iss = ")[0])
INSTR = re.compile(r'\s(First Lien|Second Lien|Unsecured|Subordinated|Preferred Equity|Common Equity|Warrants?|Structured|Asset[- ]Based|Secured Debt)\b')
g = collections.defaultdict(lambda: [0.0, 0.0])
for r in data['mfic']:
    m = INSTR.search(r['id']); key = (r['id'][:m.start()] if m else r['id'])
    g[key][0] += r.get('cost', 0); g[key][1] += r['fv']
cost = sum(v[0] for v in g.values()); fv = sum(v[1] for v in g.values())
loss = cost - fv
rows = sorted(((v[1] - v[0], k, v[0], v[1]) for k, v in g.items()), key=lambda x: x[0])
print(f'MFIC first SOI: cost {cost/1e6:,.1f}M  FV {fv/1e6:,.1f}M  net unrealized {-(loss)/1e6:,.1f}M  ({len(g)} entity strings)')
cum = 0
for i, (d, k, c, f) in enumerate(rows[:15], 1):
    cum += d
    print(f'{i:2d} {k[:70]:70s} cost {c/1e6:7.1f} FV {f/1e6:7.1f} FV/cost {f/c if c else 0:.2f}  cum share of net markdown {100*cum/-loss:5.1f}%')
for n in (5, 10, 20):
    s = sum(d for d, *_ in rows[:n]); c = sum(x[2] for x in rows[:n])
    print(f'top {n} markdowns: {-s/1e6:,.1f}M = {100*s/-loss:.0f}% of net markdown, on {100*c/cost:.1f}% of cost')
json.dump([dict(entity=k, cost=c, fv=f) for d, k, c, f in rows], open(Path(sys.argv[2]) / 'mfic_entities.json', 'w'), indent=0)
