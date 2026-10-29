"""Curated-pair version of compare.py: per PAIRS.tsv, debt marks at both lenders, 6/30/2026.
usage: python3 compare_pairs.py <scratch dir> <out dir>"""
import json, sys, csv
from pathlib import Path
sys.argv_saved = list(sys.argv)
exec(open(Path(__file__).with_name("compare.py")).read().split("out = []")[0])  # perimeter, tie checks, debt_stats (also prints its own name-match count)
P = list(csv.DictReader(open(Path(__file__).with_name('PAIRS.tsv')), delimiter='\t'))
res = []
for p in P:
    A = [r for r in data['arcc'] if r['id'].split(' | ')[0].strip().lower().startswith(p['arcc_borrower_startswith'].lower())]
    M = [r for r in data['mfic'] if p['mfic_entity_contains'].lower() in r['id'].lower()]
    assert A and M, p
    a, m = debt_stats(A, 'arcc'), debt_stats(M, 'mfic')
    res.append(dict(pair=p, arcc=a, mfic=m, arcc_ids=[r['id'] for r in A], mfic_ids=[r['id'] for r in M]))
Path(sys.argv[2]).mkdir(parents=True, exist_ok=True)
json.dump(res, open(Path(sys.argv[2]) / 'pairs_curated.json', 'w'), indent=1)
print(f"{'borrower':26s} {'ARCC FV/cost':>12s} {'MFIC FV/cost':>12s} {'gap pp':>7s} {'ARCC FV/par':>11s} {'MFIC FV/par':>11s} {'ARCC $M':>8s} {'MFIC $M':>8s}")
for x in res:
    a, m = x['arcc'], x['mfic']
    f = lambda v: f'{v:.3f}' if v else '  n/a'
    g = (m['fv_cost'] - a['fv_cost']) * 100 if a['fv_cost'] and m['fv_cost'] else float('nan')
    print(f"{x['pair']['arcc_borrower_startswith'][:26]:26s} {f(a['fv_cost']):>12s} {f(m['fv_cost']):>12s} {g:+7.1f} {f(a['fv_par']):>11s} {f(m['fv_par']):>11s} {a['debt_cost']/1e6:8.1f} {m['debt_cost']/1e6:8.1f}")
ok = [x for x in res if x['arcc']['fv_cost'] and x['mfic']['fv_cost']]
w = sum(x['mfic']['debt_cost'] for x in ok)
wg = sum((x['mfic']['fv_cost'] - x['arcc']['fv_cost']) * x['mfic']['debt_cost'] for x in ok) / w
gs = sorted((x['mfic']['fv_cost'] - x['arcc']['fv_cost']) for x in ok)
mf_tot = sum(r['cost'] for r in data['mfic'] if r.get('cost', 0) > 0)
mf_fvc = sum(r['fv'] for r in data['mfic']) / sum(r.get('cost', 0) for r in data['mfic'])
print(f"n={len(ok)} | MFIC minus ARCC FV/cost: median {100*gs[len(gs)//2]:+.2f}pp, MFIC-cost-weighted {100*wg:+.2f}pp | shared MFIC debt cost {w/1e6:.1f}M = {100*w/mf_tot:.1f}% of MFIC first-SOI cost | MFIC whole-book FV/cost {mf_fvc:.3f}")
lo = sum(x['mfic']['debt_fv'] for x in ok) / sum(x['mfic']['debt_cost'] for x in ok)
print(f"shared MFIC debt FV/cost {lo:.3f} vs whole book {mf_fvc:.3f}")
