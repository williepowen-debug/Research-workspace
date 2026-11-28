"""Cross-check the FDIC 9/30/2026 cells used by the screen against each short-list bank's own SDF filing
(DEWEY 11/11 archive research/2026-11-11_003R-population/call-reports-sdf.tar.gz), and add the two items
FDIC does not carry: RCx2746 (CRE loans not secured by real estate) and RCOALE74 (CBLR election).
Usage: python3 sdf_crosscheck.py <shortlist_sdf_text.json> <fdic-20260930.json> <out.json>
"""
import json, sys
S = json.load(open(sys.argv[1])); F = {str(r['data']['CERT']): r['data'] for r in json.load(open(sys.argv[2]))['data']}
def parse(t):
    d = {}
    for line in t.splitlines()[1:]:
        p = line.split(';')
        if len(p) >= 4: d[p[2]] = p[3]
    return d
def pick(d, code):
    for pre in ('RCFD', 'RCON'):
        if pre + code in d: return d[pre + code]
    return None
def num(x):
    try: return float(str(x).rstrip('%'))
    except: return None
PAIRS = [('LNREMULT', '1460'), ('NAREMULT', '3501'), ('P3REMULT', '3499'), ('P9REMULT', '3500'), ('BRO', '2365'),
         ('INVSUORE', '3656'), ('INVSUB', '2130'), ('LNEXAMT', '6164'), ('LNLSGR', '2122'), ('ASSET', '2170'), ('LNATRES', '3123'), ('NALNLS', '1403')]
out = {}
for c, t in S.items():
    d = parse(t); f = F[c]; res = {'mismatch': []}
    for fk, code in PAIRS:
        a, b = f.get(fk), num(pick(d, code))
        if fk == 'LNREMULT' or fk in ('NAREMULT', 'P3REMULT', 'P9REMULT', 'BRO'):  # domestic-office items: RCON only
            b = num(d.get('RCON' + code)) if ('RCON' + code) in d else b
        if b is None and (a in (0, None)): continue
        if a is None or b is None or abs(a - b) > 0.5: res['mismatch'].append((fk, code, a, b))
    rat = {k: num(d.get('RCFA' + k) or d.get('RCOA' + k)) for k in ('7204', '7205', '7206', 'P793')}
    for fk, k in (('RBC1AAJ', '7204'), ('RBCRWAJ', '7205'), ('RBC1RWAJ', '7206'), ('IDT1CER', 'P793')):
        a = f.get(fk)
        if rat[k] is not None and (a is None or abs(a - rat[k]) > 0.01): res['mismatch'].append((fk, k, a, rat[k]))
    res['cblr_RCOALE74'] = d.get('RCOALE74'); res['cre_not_secured_2746'] = num(pick(d, '2746'))
    res['ratios_sdf'] = rat; res['n_codes'] = len(d)
    out[c] = res
json.dump(out, open(sys.argv[3], 'w'), indent=1)
for c, r in out.items(): print(c, 'codes', r['n_codes'], 'CBLR', r['cblr_RCOALE74'], '2746', r['cre_not_secured_2746'], 'mismatches', r['mismatch'])
