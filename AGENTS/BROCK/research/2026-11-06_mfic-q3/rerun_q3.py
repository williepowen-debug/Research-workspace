"""ARCC vs MFIC shared-borrower marks and MFIC tail, re-run on 9/30/2026.

usage: python3 rerun_q3.py <scratch dir holding mfic_q2/mfic_q3/arcc_q3 .htm + .json>
Method and PAIRS.tsv are unchanged from research/2026-10-29_arcc-mfic-shared. The first-SOI
cut is found by walking HTML rows until cumulative FV ties to the balance sheet, not hard-coded.
"""
import json, re, sys, csv, collections
from pathlib import Path
HERE = Path(__file__).resolve().parent
OLD = HERE.parent / '2026-10-29_arcc-mfic-shared'
sys.path.insert(0, str(HERE.parent / '2026-10-23_bdc-software-exposure/scripts'))
from rows import rows
S = Path(sys.argv[1])
TIE = {'mfic_q3': 2_545.145e6, 'mfic_q2': 2_770.342e6, 'arcc_q3': 29_212.6e6}
DEBT = re.compile(r'first lien|second lien|senior secured|term loan|revolv|delayed draw|subordinated|unitranche|secured debt|unsecured debt|notes', re.I)
EQUITY = re.compile(r'equity|common|preferred|warrant|units|membership|shares|interests', re.I)
INSTR = re.compile(r'\s(First Lien|Second Lien|Unsecured|Subordinated|Preferred Equity|Common Equity|Warrants?|Structured|Asset[- ]Based|Secured Debt)', re.I)

def first_soi(t):
    k, o = 0, {}
    for _, ff in rows(S / f'{t}.htm'):
        if ff:
            k += 1
        for _, c in ff:
            o.setdefault(c, k)
    R = [dict(r, k=o.get(r['ctx'], 10**9)) for r in json.load(open(S / f'{t}.json')) if 'fv' in r]
    R.sort(key=lambda r: r['k'])
    cum, keep, best = 0.0, [], None
    for r in R:
        cum += r['fv']; keep.append(r)
        if abs(cum - TIE[t]) / TIE[t] < 0.002:
            best = (list(keep), cum)   # last row inside the tolerance band
    assert best, (t, cum / 1e6)
    print(f'{t}: {len(best[0])} first-SOI positions, FV {best[1]/1e6:,.1f}M vs balance sheet {TIE[t]/1e6:,.1f}M, cost {sum(r.get("cost",0) for r in best[0])/1e6:,.1f}M')
    return best[0]

def debt_stats(P, t):
    d = [r for r in P if r.get('cost', 0) > 0 and r.get('fv', 0) > 0 and DEBT.search(r['id'])
         and not (t == 'mfic' and EQUITY.search(r['id'].split(' - ')[0][-40:]) and not DEBT.search(r['id']))]
    c = sum(r['cost'] for r in d); f = sum(r['fv'] for r in d)
    return dict(cost=c, fv=f, r=(f / c if c else None))

mq3, mq2, aq3 = first_soi('mfic_q3'), first_soi('mfic_q2'), first_soi('arcc_q3')
P = list(csv.DictReader(open(OLD / 'PAIRS.tsv'), delimiter='\t'))
res = []
for p in P:
    A = [r for r in aq3 if r['id'].split(' | ')[0].strip().lower().startswith(p['arcc_borrower_startswith'].lower())]
    M = [r for r in mq3 if p['mfic_entity_contains'].lower() in r['id'].lower()]
    M2 = [r for r in mq2 if p['mfic_entity_contains'].lower() in r['id'].lower()]
    a, m, m2 = debt_stats(A, 'arcc'), debt_stats(M, 'mfic'), debt_stats(M2, 'mfic')
    res.append((p['arcc_borrower_startswith'], a, m, m2, len(A), len(M)))
    g = (m['r'] - a['r']) * 100 if a['r'] and m['r'] else float('nan')
    f = lambda v: f'{v:.3f}' if v else ' n/a '
    print(f"{p['arcc_borrower_startswith'][:26]:26s} ARCC {f(a['r'])} MFIC {f(m['r'])} gap {g:+6.1f}pp | MFIC 6/30 {f(m2['r'])} | MFIC cost {m['cost']/1e6:6.1f}M  nA={len(A)} nM={len(M)}")
ok = [x for x in res if x[1]['r'] and x[2]['r']]
w = sum(x[2]['cost'] for x in ok)
gs = sorted((x[2]['r'] - x[1]['r']) for x in ok)
wg = sum((x[2]['r'] - x[1]['r']) * x[2]['cost'] for x in ok) / w
tot = sum(r.get('cost', 0) for r in mq3)
print(f"n={len(ok)} median {100*gs[len(gs)//2]:+.2f}pp weighted {100*wg:+.2f}pp range {100*gs[0]:+.1f} to {100*gs[-1]:+.1f}; shared cost {w/1e6:.1f}M = {100*w/tot:.1f}% of MFIC cost; shared FV/cost {sum(x[2]['fv'] for x in ok)/w:.3f}; whole book {sum(r['fv'] for r in mq3)/tot:.3f}")

def group(R):
    g = collections.defaultdict(lambda: [0.0, 0.0])
    for r in R:
        m = INSTR.search(r['id']); k = r['id'][:m.start()] if m else r['id']
        g[k][0] += r.get('cost', 0); g[k][1] += r['fv']
    return g
g3, g2 = group(mq3), group(mq2)
loss = sum(v[0] - v[1] for v in g3.values())
rk = sorted(g3.items(), key=lambda kv: kv[1][1] - kv[1][0])
print(f'net below cost 9/30 {loss/1e6:,.1f}M, 6/30 {sum(v[0]-v[1] for v in g2.values())/1e6:,.1f}M')
for i, (k, v) in enumerate(rk[:14], 1):
    o = g2.get(k)
    print(f"{i:2d} {k[-62:]:62s} cost {v[0]/1e6:7.1f} FV {v[1]/1e6:7.1f} FV/cost {v[1]/v[0] if v[0] else 0:.2f} | 6/30 FV {o[1]/1e6 if o else float('nan'):7.1f} FV/cost {o[1]/o[0] if o and o[0] else float('nan'):.2f}")
