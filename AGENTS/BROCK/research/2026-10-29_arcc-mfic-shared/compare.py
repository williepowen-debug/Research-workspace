"""ARCC vs MFIC shared-borrower marks at 6/30/2026.

usage: python3 compare.py <scratch dir holding arcc.htm/.json mfic.htm/.json> <out dir>
Perimeter: first SOI only (positions in HTML rows up to the 6/30 'Total Investments' row),
tie-checked against each balance sheet. Matching is by normalised borrower NAME and is a
CANDIDATE list: a shared name is not proof of the same tranche, lien or terms.
"""
import json, re, sys, collections, html as H
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / '2026-10-23_bdc-software-exposure/scripts'))
from rows import rows

S, OUT = Path(sys.argv[1]), Path(sys.argv[2])
CUT = {'arcc': 1932, 'mfic': 932}
TIE = {'arcc': 29_349.3e6, 'mfic': 2_770.342e6}
STOP = {'inc', 'llc', 'lp', 'l p', 'ltd', 'corp', 'corporation', 'co', 'company', 'holdings', 'holding',
        'holdco', 'parent', 'buyer', 'bidco', 'topco', 'midco', 'intermediate', 'the', 'group', 'limited', 'plc'}

def order(t):
    k, o = 0, {}
    for texts, ff in rows(S / f'{t}.htm'):
        if ff:
            k += 1
        for _, c in ff:
            o.setdefault(c, k)
    return o

def toks(s):
    s = H.unescape(s).lower().replace('&', ' and ')
    s = re.sub(r'\(.*?\)', ' ', s)
    return [w for w in re.sub(r'[^a-z0-9 ]', ' ', s).split() if w not in STOP]

DEBT = re.compile(r'first lien|second lien|senior secured|term loan|revolv|delayed draw|subordinated|unitranche|secured debt|unsecured debt|notes', re.I)
EQUITY = re.compile(r'equity|common|preferred|warrant|units|membership|shares|interests', re.I)

data = {}
for t in ('arcc', 'mfic'):
    o = order(t)
    R = [r for r in json.load(open(S / f'{t}.json')) if o.get(r['ctx'], 10**9) <= CUT[t] and 'fv' in r]
    fv = sum(r['fv'] for r in R)
    assert abs(fv - TIE[t]) / TIE[t] < 0.005, (t, fv / 1e6)
    print(f'{t}: {len(R)} first-SOI positions, FV {fv/1e6:,.1f}M (balance sheet {TIE[t]/1e6:,.1f}M)')
    data[t] = R

# ARCC borrower = text before ' | '; MFIC id = '<industry> <group> <entity> <instrument>' with no separator.
arcc_iss = collections.defaultdict(list)
for r in data['arcc']:
    arcc_iss[r['id'].split(' | ')[0].strip()].append(r)
mfic_norm = [(' ' + ' '.join(toks(r['id'])) + ' ', r) for r in data['mfic']]

pairs = []
for name, A in arcc_iss.items():
    k = toks(name)
    if not k or (len(k) == 1 and len(k[0]) < 6):
        continue  # too generic to search for as a substring
    key = ' ' + ' '.join(k) + ' '
    M = [r for s, r in mfic_norm if key in s]
    if M:
        pairs.append((name, A, M))

def debt_stats(P, t):
    d = [r for r in P if r.get('cost', 0) > 0 and r.get('fv', 0) > 0
         and (DEBT.search(r['id']) and not (t == 'mfic' and EQUITY.search(r['id'].split(' - ')[0][-40:]) and not DEBT.search(r['id'])))]
    eq = [r for r in P if r not in d and r.get('fv', 0) > 0]
    cost = sum(r['cost'] for r in d); fv = sum(r['fv'] for r in d)
    dp = [r for r in d if r.get('par_unit') == 'USD' and r.get('par', 0) > 0]
    par = sum(r['par'] for r in dp); fvp = sum(r['fv'] for r in dp)
    return dict(debt_cost=cost, debt_fv=fv, fv_cost=fv / cost if cost else None,
                fv_par=fvp / par if par else None, n_debt=len(d), n_par=len(dp),
                eq_fv=sum(r['fv'] for r in eq))

out = []
for name, A, M in pairs:
    a, m = debt_stats(A, 'arcc'), debt_stats(M, 'mfic')
    out.append(dict(borrower=name, arcc=a, mfic=m,
                    arcc_ids=[r['id'] for r in A], mfic_ids=[r['id'] for r in M]))
OUT.mkdir(parents=True, exist_ok=True)
json.dump(out, open(OUT / 'pairs.json', 'w'), indent=1)

both = [p for p in out if p['arcc']['fv_cost'] and p['mfic']['fv_cost']]
print(f'name matches: {len(out)}; with debt at both: {len(both)}')
gap = [(p['mfic']['fv_cost'] - p['arcc']['fv_cost'], p) for p in both]
w = sum(p['mfic']['debt_cost'] for _, p in gap)
wavg = sum(g * p['mfic']['debt_cost'] for g, p in gap) / w
med = sorted(g for g, _ in gap)[len(gap) // 2]
print(f'MFIC minus ARCC debt FV/cost, pp: median {100*med:+.2f}, MFIC-cost-weighted {100*wavg:+.2f}, MFIC shared debt cost {w/1e6:,.1f}M')
for lo, hi in [(-1, -0.10), (-0.10, -0.03), (-0.03, -0.01), (-0.01, 0.01), (0.01, 0.03), (0.03, 1)]:
    S_ = [p for g, p in gap if lo <= g < hi]
    print(f'  gap [{100*lo:+.0f},{100*hi:+.0f}) pp: n={len(S_)}  MFIC cost {sum(p["mfic"]["debt_cost"] for p in S_)/1e6:,.1f}M')
print('largest |gap| (MFIC cost >= $5M):')
for g, p in sorted(gap, key=lambda x: -abs(x[0])):
    if p['mfic']['debt_cost'] >= 5e6:
        print(f"  {p['borrower'][:44]:44s} ARCC {p['arcc']['fv_cost']:.3f}  MFIC {p['mfic']['fv_cost']:.3f}  gap {100*g:+.1f}pp  MFIC cost {p['mfic']['debt_cost']/1e6:.1f}M  ARCC cost {p['arcc']['debt_cost']/1e6:.1f}M")
mf_tot = sum(r['cost'] for r in data['mfic'] if r.get('cost', 0) > 0)
print(f'coverage: shared MFIC debt cost = {100*w/mf_tot:.1f}% of MFIC first-SOI cost')
