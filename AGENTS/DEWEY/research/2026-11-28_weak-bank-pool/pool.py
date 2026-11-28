"""Leg C: is the pool of weak banks growing? Four sets per quarter, 3/31/2019 to 9/30/2026, FDIC BankFind population.
Run from repo root: python3 AGENTS/DEWEY/research/2026-11-28_weak-bank-pool/pool.py
Reads ./fdic/fdic-<REPDTE>.json.gz and ./fdic/failed-banks.csv; writes ./out/pool-by-quarter.tsv, failures.tsv, below-adequate-20260930.tsv, members.json.
Population: every FDIC financials row except BKCLASS OI (insured branches of foreign banks) and NC (non-bank trust companies),
 as in the 11/11 003R method. A ratio reported as 0 is treated as not reported.
Definitions (all FDIC fields; $ thousands):
 RBC reporter = RBCRWAJ reported and > 0; otherwise CBLR elector (leverage-only; INFERRED from the blank ratio).
 Set 1 PCA lines on ANY ratio. RBC reporters: well-capitalized line total 10 / tier1 8 / CET1 6.5 / leverage 5;
   adequately: 8 / 6 / 4.5 / 4; significantly undercapitalized line: 6 / 4 / 3 / 3.
   CBLR electors: well = CBLR leverage line (8.0 for 2020Q2-Q4, 8.5 for 2021, 9.0 otherwise, 8.0 from 9/30/2026 per 12 CFR 324.12 as amended 2026-07-01; the 2-quarter grace period is
   NOT modelled, so 1a over-counts CBLR banks); adequately = leverage 4; significantly = leverage 3.
   1d critically undercapitalized proxy: tier 1 capital (RBCT1) / ASSET <= 2% (PCA uses tangible equity = tier 1 + perpetual
   preferred not in tier 1, over total assets; close but not identical).
 Set 2 Texas-ratio form: (NCLNLS + ORE) > (RBCT1 + LNATRES); a non-positive denominator counts as in.
   2g variant (not in 'any'): the same with GAAP tangible equity (EQ - INTAN), which carries AOCI securities losses and so
   inflates the set from 2022 (shown to make the point; not used).
 Set 3 one-quarter net loss: NETINCQ < -10% of the same bank's EQ at the prior quarter-end (2019Q1 has no prior: not computed).
 Set 4 BRO/DEP > 15% AND RBCRWAJ < 12 (within 2 points of the 10% line); RBC reporters only.
   4c variant (reported separately, not in 'any'): CBLR electors with BRO/DEP > 15% and leverage < CBLR line + 2.
"""
import json, gzip, csv, io, os, datetime
B = 'AGENTS/DEWEY/research/2026-11-28_weak-bank-pool/'
D = sorted(f[5:13] for f in os.listdir(B + 'fdic') if f.startswith('fdic-') and not f.startswith('fdic-t1-') and f.endswith('.json.gz'))
def load(d):
    t1 = {r['data']['CERT']: r['data'].get('RBCT1') for r in json.load(gzip.open(f'{B}fdic/fdic-t1-{d}.json.gz'))['data']}
    out = {r['data']['CERT']: r['data'] for r in json.load(gzip.open(f'{B}fdic/fdic-{d}.json.gz'))['data'] if r['data'].get('BKCLASS') not in ('OI', 'NC')}
    for c, r in out.items(): r['RBCT1'] = t1.get(c)
    return out
def n(x): return x if isinstance(x, (int, float)) else None
def nr(x): return x if isinstance(x, (int, float)) and x != 0 else None   # ratios: a reported 0 is treated as not reported
def cblr_line(d):
    if '20200630' <= d <= '20201231': return 8.0
    if '20210331' <= d <= '20211231': return 8.5
    if d >= '20260930': return 8.0   # 12 CFR 324.12 reads "greater than 8 percent" from the 2026-07-01 eCFR version (9 before)
    return 9.0
def sets(r, prev, d):
    A = n(r.get('ASSET')) or 0; eq = n(r.get('EQ')); intan = n(r.get('INTAN')) or 0; alw = n(r.get('LNATRES')) or 0
    tr, t1, c1, lev = nr(r.get('RBCRWAJ')), nr(r.get('RBC1RWAJ')), nr(r.get('IDT1CER')), nr(r.get('RBC1AAJ'))
    rbc = bool(tr and tr > 0); s = {}
    if rbc:
        def below(lines): return any(v is not None and v < L for v, L in zip((tr, t1, c1, lev), lines))
        s['1a_below_well'] = below((10, 8, 6.5, 5)); s['1b_below_adequate'] = below((8, 6, 4.5, 4)); s['1c_below_undercap'] = below((6, 4, 3, 3))
    else:
        s['1a_below_well'] = lev is not None and lev < cblr_line(d); s['1b_below_adequate'] = lev is not None and lev < 4; s['1c_below_undercap'] = lev is not None and lev < 3
    te = (eq - intan) if eq is not None else None          # GAAP tangible equity (includes AOCI)
    t1c = n(r.get('RBCT1'))                                 # tier 1 capital (excludes AOCI for banks that opted out)
    s['1d_critical_proxy'] = bool(t1c is not None and A > 0 and t1c / A <= 0.02)
    bad = (n(r.get('NCLNLS')) or 0) + (n(r.get('ORE')) or 0)
    cush = (t1c if t1c is not None else (te or 0)) + alw
    s['2_texas'] = bool(bad > 0 and (cush <= 0 or bad > cush))
    cg = (te or 0) + alw
    s['2g_texas_gaap'] = bool(bad > 0 and (cg <= 0 or bad > cg))
    ni = n(r.get('NETINCQ')); peq = n(prev.get('EQ')) if prev else None
    s['3_qloss'] = bool(ni is not None and peq and peq > 0 and ni < -0.10 * peq)
    bro, dep = n(r.get('BRO')) or 0, n(r.get('DEP')) or 0
    s['4_brokered_thin'] = bool(rbc and dep > 0 and bro / dep > 0.15 and tr < 12)
    s['4c_cblr_variant'] = bool((not rbc) and dep > 0 and bro / dep > 0.15 and lev is not None and lev < cblr_line(d) + 2)
    s['1a_rbc_reporters'] = bool(rbc and s['1a_below_well'])
    # 'any' uses the RBC-reporter half of 1a: the CBLR leverage line without its 2-quarter grace period over-counts (2021-22, 9/2026)
    s['any'] = any(s[k] for k in ('1a_rbc_reporters', '1b_below_adequate', '1c_below_undercap', '1d_critical_proxy', '2_texas', '3_qloss', '4_brokered_thin'))
    return s, rbc
K = ['1a_below_well', '1a_rbc_reporters', '1b_below_adequate', '1c_below_undercap', '1d_critical_proxy', '2_texas', '2g_texas_gaap', '3_qloss', '4_brokered_thin', '4c_cblr_variant', 'any']
os.makedirs(B + 'out', exist_ok=True)
rows = []; members = {}; prev = {}; data = {}
for d in D:
    cur = load(d); data[d] = cur
    tot_n, tot_a = len(cur), sum(n(r.get('ASSET')) or 0 for r in cur.values())
    agg = {k: [0, 0.0] for k in K}; mem = {k: [] for k in K}; ncblr = 0
    for c, r in cur.items():
        s, rbc = sets(r, prev.get(c), d); ncblr += (not rbc)
        if d == D[0]: s['3_qloss'] = None
        for k in K:
            if s.get(k): agg[k][0] += 1; agg[k][1] += n(r.get('ASSET')) or 0; mem[k].append(c)
    members[d] = mem
    rows.append([d, tot_n, round(tot_a / 1e6, 1), ncblr] + sum(([agg[k][0], round(agg[k][1] / 1e6, 2)] for k in K), []))
    prev = cur
hdr = ['REPDTE', 'banks', 'assets_$B', 'cblr_electors'] + sum(([k + '_n', k + '_assets_$B'] for k in K), [])
with open(B + 'out/pool-by-quarter.tsv', 'w') as fh:
    fh.write('\t'.join(hdr) + '\n')
    for r in rows: fh.write('\t'.join(map(str, r)) + '\n')
json.dump(members, open(B + 'out/members.json', 'w'))
# failures since 2023
t = open(B + 'fdic/failed-banks.csv', 'rb').read().decode('utf-8-sig', 'replace')
F = list(csv.reader(io.StringIO(t)))
out = []
for f in F[1:]:
    cd = datetime.datetime.strptime(f[5].strip(), '%d-%b-%y').date()
    if cd.year < 2023: continue
    cert = int(f[3]); qs = [d for d in D if datetime.date(int(d[:4]), int(d[4:6]), int(d[6:])) < cd]
    inq = {k: [d for d in qs if cert in members[d][k]] for k in K}
    first_any = inq['any'][0] if inq['any'] else ''
    # start of the last continuous run in 'any' ending at the last reported quarter before closing
    run = ''
    rep = [d for d in qs if cert in data[d]]
    if rep and cert in members[rep[-1]]['any']:
        i = len(rep) - 1
        while i > 0 and cert in members[rep[i - 1]]['any']: i -= 1
        run = rep[i]
    def qb(d): return '' if not d else sum(1 for x in qs if x >= d)
    out.append([f[0], cert, f[2], cd.isoformat(), rep[-1] if rep else '', round((n(data[rep[-1]][cert].get('ASSET')) or 0) / 1e6, 2) if rep else '',
                first_any, qb(first_any), run, qb(run)] + [inq[k][0] if inq[k] else '' for k in K[:-1]])
with open(B + 'out/failures.tsv', 'w') as fh:
    fh.write('\t'.join(['bank', 'cert', 'state', 'closed', 'last_report', 'last_assets_$B', 'first_in_any', 'quarters_before_close', 'last_run_start', 'run_quarters_before_close'] + ['first_' + k for k in K[:-1]]) + '\n')
    for r in out: fh.write('\t'.join(map(str, r)) + '\n')
# 9/30/2026 below adequately capitalized: facts
d = D[-1]; cur = data[d]
with open(B + 'out/below-adequate-20260930.tsv', 'w') as fh:
    fh.write('cert\tname\tstate\tclass\tassets_$M\ttotal_rbc\ttier1\tcet1\tleverage\tcblr\tequity_$M\tnoncurrent_$M\tore_$M\tqtr_net_income_$M\n')
    for c in members[d]['1b_below_adequate']:
        r = cur[c]; _, rbc = sets(r, data[D[-2]].get(c), d)
        f2 = lambda x: '' if n(r.get(x)) is None else f'{n(r.get(x)):.2f}'
        fh.write('\t'.join(map(str, [c, r.get('NAME'), r.get('STALP'), r.get('BKCLASS'), round((r.get('ASSET') or 0) / 1e3, 1), f2('RBCRWAJ'), f2('RBC1RWAJ'), f2('IDT1CER'), f2('RBC1AAJ'), not rbc,
                round((r.get('EQ') or 0) / 1e3, 1), round((r.get('NCLNLS') or 0) / 1e3, 1), round((r.get('ORE') or 0) / 1e3, 1), round((r.get('NETINCQ') or 0) / 1e3, 1)])) + '\n')
print('quarters', len(D), D[0], D[-1])
