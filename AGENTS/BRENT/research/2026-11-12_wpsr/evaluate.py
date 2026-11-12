#!/usr/bin/env python3
"""BRENT 2026-11-12: WPSR data week 2026-11-06 (Veterans Day release, Thu 12:00 ET) from release-day saved EIA bytes.
Grades BRT-31 week five and BRT-34's first window print by their PREDICTIONS.tsv letters.
Research only; no state writes, threshold or trade authority.
"""
import datetime as dt, hashlib, json
from pathlib import Path
from decimal import Decimal, getcontext
import xlrd
getcontext().prec = 40
D = Path(__file__).resolve().parent
PRIOR = D.parent / '2026-10-28_eia-oct28' / 'psw01.xls'   # last release-day capture on disk (week 10/23)

def series(path, key, sheet):
    book = xlrd.open_workbook(path)
    sh = book.sheet_by_name(sheet)
    keys = sh.row_values(1)
    if key not in keys:
        raise ValueError(f'missing exact series {key} in {path.name}:{sheet}')
    c = keys.index(key); out = {}
    for r in range(3, sh.nrows):
        x = sh.cell_value(r, 0); v = sh.cell_value(r, c)
        if isinstance(x, (int, float)) and v != '':
            out[xlrd.xldate_as_datetime(x, book.datemode).date().isoformat()] = Decimal(str(v))
    return {'file': path.name, 'sheet': sheet, 'column': c, 'series': key, 'title': sh.cell_value(2, c)}, out

W = dt.date(2026, 11, 6)
# ---- BRT-31: WGFUPUS2 (Data 2, weekly), 4-wk avg vs the same 4 weeks 52 weeks (364 days) earlier
gb, g = series(D / 'psw01.xls', 'WGFUPUS2', 'Data 2')
cur = [(W - dt.timedelta(days=7 * k)).isoformat() for k in range(4)]
base = [(dt.date.fromisoformat(x) - dt.timedelta(days=364)).isoformat() for x in cur]
cs = sum(g[k] for k in cur); bs = sum(g[k] for k in base); yoy = (cs / bs - 1) * 100
_, gprev = series(PRIOR, 'WGFUPUS2', 'Data 2')
rev = {k: {'10/28 capture': str(gprev[k]), 'this capture': str(g[k])} for k in cur[1:] + base if k in gprev and gprev[k] != g[k]}
# price leg: GASREGW Monday after the data week (11/9) vs the observation 364 days earlier; EIA weekly retail = same survey
pb, p = series(D / 'eia-retail.xls', 'EMM_EPMR_PTE_NUS_DPG', 'Data 3')
pc = '2026-11-09'; pbd = (dt.date.fromisoformat(pc) - dt.timedelta(days=364)).isoformat()
py = (p[pc] / p[pbd] - 1) * 100 if pc in p and pbd in p else None
# ---- BRT-34: WDISTUS1 (Data 1), strictly below 95,000 thousand barrels
db, d = series(D / 'psw01.xls', 'WDISTUS1', 'Data 1')
dist = d.get(W.isoformat())
# ---- context levels (alert lines 2 and 5), same workbook
_, crude = series(D / 'psw01.xls', 'WCESTUS1', 'Data 1')
_, spr = series(D / 'psw01.xls', 'WCSSTUS1', 'Data 1')
_, gstk = series(D / 'psw01.xls', 'WGTSTUS1', 'Data 1')
prev = (W - dt.timedelta(days=7)).isoformat()
def wow(s): return {'level': str(s[W.isoformat()]), 'wow': str(s[W.isoformat()] - s[prev])}
sha = {f.name: hashlib.sha256(f.read_bytes()).hexdigest() for f in sorted(D.iterdir()) if f.suffix in ('.xls', '.csv', '.txt')}
res = {
    'data_week': W.isoformat(), 'release': '2026-11-12 12:00 ET (EIA schedule page, Veterans Day)',
    'capture': (D / 'capture.txt').read_text().strip() if (D / 'capture.txt').exists() else None,
    'BRT31': {'basis': gb, 'current_rows': {k: str(g[k]) for k in cur}, 'base_rows': {k: str(g[k]) for k in base},
              'current_avg': str(cs / 4), 'base_avg': str(bs / 4), 'yoy_pct': str(yoy),
              'qualifying_week_le_-1.5': yoy <= Decimal('-1.5'), 'above_-1.0': yoy > Decimal('-1.0'),
              'revisions_vs_10_28_capture': rev,
              'price_basis': pb, 'price_current': {pc: str(p.get(pc))}, 'price_base': {pbd: str(p.get(pbd))},
              'price_yoy_pct': None if py is None else str(py), 'price_below_20': None if py is None else bool(py < 20),
              'latest_retail_date': max(p)},
    'BRT34': {'basis': db, 'print': None if dist is None else str(dist), 'prior_week': str(d.get(prev)),
              'below_95000': None if dist is None else bool(dist < Decimal('95000')),
              'distance_to_line': None if dist is None else str(dist - Decimal('95000'))},
    'context': {'commercial_crude_WCESTUS1': wow(crude), 'SPR_WCSSTUS1': wow(spr), 'total_gasoline_WGTSTUS1': wow(gstk)},
    'sha256': sha}
print(json.dumps(res, indent=1))
json.dump(res, open(D / 'evaluation.json', 'w'), indent=1)
