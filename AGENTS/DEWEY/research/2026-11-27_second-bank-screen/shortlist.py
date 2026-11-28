"""Render the short-list and HOMER-five tables from the screen output (no new data).
Run from repo root: python3 AGENTS/DEWEY/research/2026-11-27_second-bank-screen/shortlist.py
"""
import csv, gzip, json, os
B = 'AGENTS/DEWEY/research/2026-11-27_second-bank-screen/out/'
def rd(d): return list(csv.DictReader(gzip.open(B + f'screen-{d}.tsv.gz', 'rt'), delimiter='\t'))
R9, R6 = rd('20260930'), rd('20260630')
pos9 = {r['CERT']: i + 1 for i, r in enumerate(R9)}; pos6 = {r['CERT']: i + 1 for i, r in enumerate(R6)}
M6 = {r['CERT']: r for r in R6}; M9 = {r['CERT']: r for r in R9}
I = {str(r['data']['CERT']): r['data'] for r in json.load(open(B + 'institutions-shortlist.json'))['data']}
X = json.load(open(B + 'sdf-crosscheck.json'))
TICK = {'30879': 'PROV (parent Provident Financial Holdings)', '32541': 'FLG', '30394': 'CARV (parent Carver Bancorp)',
        '33539': 'PFBC (the bank itself)', '57742': 'MNSB (parent MainStreet Bancshares)'}
FL = [('A1_mf_share', 'MF>=50% of loans'), ('A2_mf_cap', 'MF>=300% of capital'), ('B1_ventures', 'RE ventures+subs>=25% of capital'),
      ('B2_insider', 'insider credit>=18.8% of capital'), ('C_brokered', 'brokered>=15% of deposits'), ('D_thin_capital', 'capital margin<2 pts'),
      ('E_mf_stress', 'MF PD+NA>=5% or +2 pts q/q'), ('F_thin_reserve', 'allowance<50% of nonaccrual')]
def f(x, nd=0):
    try: v = float(x); return f'{v:,.{nd}f}'
    except: return 'n/a'
def flags(r): return ''.join(('A1 ', 'A2 ', 'B1 ', 'B2 ', 'C ', 'D ', 'E ', 'F ')[i] for i, (k, _) in enumerate(FL) if r and r[k] == 'True').strip() or 'none'
def row(c):
    r, q, i = M9[c], M6.get(c), I.get(c, {})
    cre2746 = X.get(c, {}).get('cre_not_secured_2746')
    miss = [lab for k, lab in FL if r[k] != 'True']
    return (f"| {pos9[c]} | {i.get('NAME', r['NAME'])} ({r['CITY'].title()}, {r['STALP']}; cert {c}) | {f(float(r['ASSET'])/1e6, 2)} | {i.get('REGAGNT','')} | "
            f"{TICK.get(c, 'not in SEC ticker list')} | {f(r['mf_share'])} | {f(r['mf_cap'])} | {f(r['cre_cap'])} | {f(r['ventures_cap'], 1)} | {f(r['insider_cap'], 1)} | "
            f"{f(r['bro_share'], 1)} ({f(r['d_bro_share'], 1)}) | {f(r['min_margin'], 2)} {r['min_line']}{' (CBLR)' if r['cblr']=='True' else ''} | {f(r['mf_na_pct'], 2)} | {f(r['mf_p3_pct'], 2)} | {f(r['d_mf_stress'], 2)} | "
            f"{f(r['cov'])} | {flags(r)} | {flags(q) if q else 'n/a'} (rank {pos6.get(c, 'n/a')}) |"), miss, cre2746
hdr = ('| Rank 9/30 | Bank (cert) | Assets $B | Regulator | Listed | MF % loans | MF % capital | CRE % capital | RE ventures % capital | Insider % capital | '
       'Brokered % dep (q/q pts) | Capital margin, pts (line) | MF nonaccrual % | MF 30-89 % | MF stress q/q pts | Allowance % nonaccrual | Flags 9/30 | Flags 6/30 |')
sep = '|' + '---|' * 18
print(hdr); print(sep)
short = [r['CERT'] for r in R9[:15]]
notes = {}
for c in short:
    line, miss, c27 = row(c); print(line); notes[c] = (miss, c27)
print('\nDoes NOT share:')
for c in short: print(f"- {M9[c]['NAME']} ({c}): " + '; '.join(notes[c][0]) + (f"; RCx2746 CRE-not-secured {f(notes[c][1])}K" if notes[c][1] else ''))
print('\nHOMER five:'); print(hdr); print(sep)
for c in ['33539', '5903', '58309', '57742', '34294']:
    line, miss, c27 = row(c); print(line)
    r = M9[c]; print(f"<!-- {c} dNA {r['d_mf_na']} dP3 {r['d_mf_p3']} mf {r['mf']} -->")
