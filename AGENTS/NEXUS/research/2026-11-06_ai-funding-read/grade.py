"""Reproduce the November 6 letter readings from saved inputs; no network, no owner writes."""
import json
from decimal import Decimal
from pathlib import Path
P = Path(__file__).resolve().parent
def fp(sid, scale=100):
    rows = json.loads((P/'fred'/f'fp_{sid}.json').read_text())['rows']
    return sorted((r['date'], int(Decimal(r['value'])*scale)) for r in rows if r['value'] != '.')
def runs(rows, low, high, n=2):
    up = dn = 0; fire = None; out = []
    for day, v in rows:
        up = up+1 if v >= high else 0
        dn = dn+1 if v <= low else 0
        if fire is None and (up >= n or dn >= n): fire = dict(date=day, branch='UP' if up >= n else 'DOWN')
        out.append((day, v, up, dn))
    return out, fire
res = {}
hy = fp('BAMLH0A0HYM2')
L = dict(hy)['2026-10-08']
win = [c for c in hy if '2026-10-08' < c[0] <= '2026-11-05']
cells, fire = runs(win, L-35, L+35)
claims = fp('ICSA', 1)
cl = [c for c in claims if c[0] >= '2026-10-03']
run = best = 0
for d, v in cl:
    run = run+1 if v >= 230000 else 0; best = max(best, run)
res['M-01'] = dict(L=L, UP_edge=L+35, DOWN_edge=L-35, cells=len(cells), max_HY=max(v for _, v in win),
                   min_HY=min(v for _, v in win), max_up_run=max(c[2] for c in cells), fire=fire,
                   claims=cl, claims_ge_230_max_run=best)
kre = json.loads((P/'KRE_VENDOR.json').read_text())['KRE']['history']
k = [(r['date'], int(Decimal(str(r['close']))*100)) for r in kre]
Lk = dict(k)['2026-10-08']
lo = Lk*92//100; hi = -(-Lk*108//100)
win = [c for c in k if '2026-10-08' < c[0] <= '2026-11-05']
cells, fire = runs(win, lo, hi)
res['M-05'] = dict(L=Lk, low=lo, high=hi, cells=len(cells), max_close=max(v for _, v in win),
                   min_close=min(v for _, v in win), max_up_run=max(c[2] for c in cells), fire=fire)
vix = [c for c in fp('VIXCLS') if c[0] > '2026-10-23']
cells, fire = runs(vix, 1645, 2245)
res['M-04b'] = dict(low=1645, high=2245, cells=cells[-5:], fire=fire)
b = dict(fp('BAMLH0A2HYB')); c = dict(fp('BAMLH0A3HYC')); bb = dict(fp('BAMLH0A1HYBB'))
up = dn = 0; tr = []
for d in sorted(x for x in b if x > '2026-10-23'):
    up = up+1 if b[d] >= 358 and c[d] >= 1416 else 0
    dn = dn+1 if b[d] <= 328 and c[d] <= 1296 else 0
    tr.append((d, b[d], c[d], up, dn))
res['M-08b'] = dict(tail=tr[-4:], BB_latest=bb[max(bb)])
real = [x for x in fp('DFII10') if x[0] > '2026-10-16']
up = dn = 0; tr = []
for i, (d, v) in enumerate(real, 1):
    up = up+1 if v >= 284 else 0; dn = dn+1 if v <= 264 else 0
    tr.append((i, d, v, up, dn))
res['L13'] = dict(tail=tr[-4:], note='cell numbers count FRED rows after 10/16 in this pull; the frozen grid and FRED govern')
hy2 = dict(hy)
res['Guards'] = dict(HY_latest=hy[-1], RED_FT12_gap=hy[-1][1]-260, PRED24_needs=350)
(P/'GRADES.json').write_text(json.dumps(res, indent=1))
print(json.dumps(res, indent=0)[:3000])
