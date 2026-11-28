"""Second-bank screen: which insured banks share United Fidelity Bank's (cert 29566) Call Report shape.
Run from repo root:
  python3 AGENTS/DEWEY/research/2026-11-27_second-bank-screen/screen.py <fdic_dir> <outdir>
<fdic_dir> holds fdic-<REPDTE>.json[.gz] from pull_fdic.py (committed copies: ./fdic/). Writes screen-<REPDTE>.tsv and summary.json.
All money $thousands. FDIC field -> Call Report item, verified on cert 29566 at 9/30/2026 against its SDF:
  LNREMULT=RC-C 1.d (1460) · LNLSGR=RCFD/RCON 2122 · NAREMULT/P3REMULT/P9REMULT=RC-N 1.d (3501/3499/3500)
  BRO=RC-E M1.b (2365) · INVSUORE=RC 9 (3656, RE ventures) · INVSUB=RC 8 (2130) · LNEXAMT=RC-M 1.a (6164, insiders)
  RBC=RC-R 47a (3792) · RBCRWAJ/RBC1RWAJ/IDT1CER/RBC1AAJ = total/T1/CET1/leverage ratios (7205/7206/P793/7204)
Not in FDIC (so not used across quarters): RCON2746 (CRE loans not secured by RE), CBLR election (RCOALE74),
loans to affiliates (no Call Report item), related-party receivables (inside RC-F 'other assets', free text).
Thresholds were set by DEWEY on 2026-11-28 KNOWING United Fidelity's values; they are deliberately looser than UFB.
"""
import json, sys, os, math, gzip
FD, OUT = sys.argv[1], sys.argv[2]
DATES = ['20250930','20251231','20260331','20260630','20260930']
def load(d):
    p = f'{FD}/fdic-{d}.json'
    fh = gzip.open(p + '.gz', 'rt') if os.path.exists(p + '.gz') else open(p)
    return {r['data']['CERT']: r['data'] for r in json.load(fh)['data']}
def n(x): return x if isinstance(x,(int,float)) else None
def pct(a,b): return None if a is None or not b else 100.0*a/b
TH = dict(mf_share=50.0, mf_cap=300.0, ventures_cap=25.0, insider_cap=18.8, brokered=15.0,
          margin=2.0, mf_stress=5.0, mf_stress_rise=2.0, cov=50.0, na_floor=1.0, shortlist_mf_cap=100.0)
# insider_cap 18.8% = the population's 90th percentile at both 6/30 and 9/30/2026 (DEWEY computed; UFB sat at the 80th/92nd)
LINES = dict(total=8.0, tier1=6.0, cet1=4.5, leverage=4.0)   # 'adequately capitalized' minimums (12 CFR 6.4 / 324.403)
def row(r, p):
    A, L = n(r.get('ASSET')), n(r.get('LNLSGR'))
    rbc, t1, all_ = n(r.get('RBC')), n(r.get('RBCT1')), n(r.get('LNATRES')) or 0
    tr, t1r, cr, lev = n(r.get('RBCRWAJ')), n(r.get('RBC1RWAJ')), n(r.get('IDT1CER')), n(r.get('RBC1AAJ'))
    cblr = not tr  # no risk-based ratio reported -> CBLR elector (INFERRED from blank; RCOALE74 not in FDIC)
    cap = rbc if rbc else ((t1 or 0) + all_ or None)
    capbasis = 'RBC' if rbc else 'T1+ALLL'
    mf, na, p3, p9 = n(r.get('LNREMULT')) or 0, n(r.get('NAREMULT')) or 0, n(r.get('P3REMULT')) or 0, n(r.get('P9REMULT')) or 0
    cre = sum(n(r.get(k)) or 0 for k in ('LNRECONS','LNREMULT','LNRENROT'))
    ven = (n(r.get('INVSUORE')) or 0) + (n(r.get('INVSUB')) or 0)
    ins = n(r.get('LNEXAMT'))
    bro, dep = n(r.get('BRO')), n(r.get('DEP'))
    nal, alw = n(r.get('NALNLS')) or 0, all_
    if cblr: margins = {'leverage': (lev - LINES['leverage']) if lev is not None else None}
    else: margins = {'total': tr - 8.0 if tr is not None else None, 'tier1': t1r - 6.0 if t1r is not None else None,
                     'cet1': cr - 4.5 if cr is not None else None, 'leverage': lev - 4.0 if lev is not None else None}
    mvals = [v for v in margins.values() if v is not None]
    o = dict(CERT=r['CERT'], NAME=r.get('NAME'), STALP=r.get('STALP'), CITY=r.get('CITY'), BKCLASS=r.get('BKCLASS'),
             ASSET=A, LNLSGR=L, cap=cap, capbasis=capbasis, cblr=cblr,
             mf=mf, mf_share=pct(mf, L), mf_cap=pct(mf, cap), cre_cap=pct(cre, cap), cons_cap=pct(n(r.get('LNRECONS')) or 0, cap),
             ventures=ven, ventures_cap=pct(ven, cap), insider=ins, insider_cap=pct(ins, cap),
             bro_share=pct(bro, dep), min_margin=min(mvals) if mvals else None,
             min_line=min(margins, key=lambda k: margins[k] if margins[k] is not None else 1e9) if mvals else None,
             tot_ratio=tr, lev_ratio=lev, cet1_ratio=cr,
             mf_na=na, mf_p3=p3, mf_p9=p9, mf_na_pct=pct(na, mf) if mf else None, mf_p3_pct=pct(p3, mf) if mf else None,
             mf_stress=pct(na + p3 + p9, mf) if mf else None, nal_pct=pct(nal, L), cov=pct(alw, nal) if nal else None)
    if p:
        q = row(p, None)
        o['d_mf_stress'] = (o['mf_stress'] - q['mf_stress']) if (o['mf_stress'] is not None and q['mf_stress'] is not None) else None
        o['d_mf_na'] = na - (q['mf_na'] or 0); o['d_mf_p3'] = p3 - (q['mf_p3'] or 0)
        o['d_bro_share'] = (o['bro_share'] - q['bro_share']) if (o['bro_share'] is not None and q['bro_share'] is not None) else None
    else:
        o['d_mf_stress'] = o['d_mf_na'] = o['d_mf_p3'] = o['d_bro_share'] = None
    f = {}
    f['A1_mf_share'] = bool(o['mf_share'] is not None and o['mf_share'] >= TH['mf_share'])
    f['A2_mf_cap'] = bool(o['mf_cap'] is not None and o['mf_cap'] >= TH['mf_cap'])
    f['B1_ventures'] = bool((o['ventures_cap'] or 0) >= TH['ventures_cap'])
    f['B2_insider'] = bool((o['insider_cap'] or 0) >= TH['insider_cap'])
    f['C_brokered'] = bool((o['bro_share'] or 0) >= TH['brokered'])
    f['D_thin_capital'] = bool(o['min_margin'] is not None and o['min_margin'] < TH['margin'])
    f['E_mf_stress'] = bool(mf >= 10000 and ((o['mf_stress'] or 0) >= TH['mf_stress'] or (o['d_mf_stress'] or 0) >= TH['mf_stress_rise']))
    f['F_thin_reserve'] = bool(o['cov'] is not None and o['cov'] < TH['cov'] and (o['nal_pct'] or 0) >= TH['na_floor'])
    o.update(f); o['n_struct'] = sum(f[k] for k in ('A1_mf_share','A2_mf_cap','B1_ventures','B2_insider','C_brokered'))
    o['n_stress'] = sum(f[k] for k in ('D_thin_capital','E_mf_stress','F_thin_reserve')); o['n_all'] = o['n_struct'] + o['n_stress']
    return o
os.makedirs(OUT, exist_ok=True)
data = {d: load(d) for d in DATES}
summary = {'thresholds': TH, 'lines': LINES}
for i, d in enumerate(DATES):
    prev = data[DATES[i-1]] if i else {}
    rows = []
    for c, r in data[d].items():
        if r.get('BKCLASS') in ('OI','NC'): continue
        L, A = n(r.get('LNLSGR')), n(r.get('ASSET'))
        if not L or not A or L < 0.10 * A: continue   # loan book under 10% of assets: excluded (trust/card-only shells)
        rows.append(row(r, prev.get(c)))
    rows.sort(key=lambda o: (-((o['mf_cap'] or 0) >= TH['shortlist_mf_cap']), -o['n_all'], -o['n_struct'], -(o['mf_cap'] or 0)))
    keys = list(rows[0].keys())
    with open(f'{OUT}/screen-{d}.tsv', 'w') as fh:
        fh.write('\t'.join(keys) + '\n')
        for o in rows: fh.write('\t'.join('' if o[k] is None else (f'{o[k]:.4f}' if isinstance(o[k], float) else str(o[k])) for k in keys) + '\n')
    ufb = next((o for o in rows if o['CERT'] == 29566), None)
    FL = ('A1_mf_share','A2_mf_cap','B1_ventures','B2_insider','C_brokered','D_thin_capital','E_mf_stress','F_thin_reserve')
    cnt = {k: sum(o[k] for o in rows) for k in FL}
    elig = [o for o in rows if (o['mf_cap'] or 0) >= TH['shortlist_mf_cap']]
    summary[d] = {'banks': len(rows), 'flag_counts': cnt,
                  'mf_cap_ge_100': len(elig),
                  'n_all_dist_eligible': {k: sum(1 for o in elig if o['n_all'] == k) for k in range(9)},
                  'ufb': ufb, 'ufb_rank': (rows.index(ufb) + 1) if ufb else None,
                  'top20': [(o['CERT'], o['NAME'], o['n_struct'], o['n_stress']) for o in rows[:20]]}
json.dump(summary, open(f'{OUT}/summary.json', 'w'), indent=1, default=str)
for d in DATES:
    s = summary[d]; u = s['ufb']
    print(d, 'banks', s['banks'], 'MF/capital>=100%:', s['mf_cap_ge_100'], 'flags', s['flag_counts'], 'n_all(eligible)', s['n_all_dist_eligible'])
    if u: print('   UFB rank', s['ufb_rank'], {k: u[k] for k in ('A1_mf_share','A2_mf_cap','B1_ventures','B2_insider','C_brokered','D_thin_capital','E_mf_stress','F_thin_reserve')},
                'mf_share %.1f mf_cap %.0f ven_cap %.0f ins_cap %.1f bro %.1f margin %.2f(%s) mf_stress %.2f cov %s' % (u['mf_share'], u['mf_cap'], u['ventures_cap'], u['insider_cap'] or -1, u['bro_share'], u['min_margin'], u['min_line'], u['mf_stress'] or 0, u['cov']))
    for t in s['top20'][:16]: print('     ', t)
