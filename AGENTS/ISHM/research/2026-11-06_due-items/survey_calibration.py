#!/usr/bin/env python3
"""ISHM 2026-11-06 survey-band descriptive counts. Research candidates only; registers nothing.
Run from this directory: python3 -I survey_calibration.py. Reads saved snapshots; no network."""
import json, csv
def series(p, code='in'):
    j = json.load(open(p))
    s = [x for x in j['series']['docs'] if x['series_code'] == code][0]
    return dict(zip(s['period'], s['value']))
no, inv = series('sources/dbn_neword.json'), series('sources/dbn_inventories.json')
months = sorted(set(no) & set(inv))
sp = {m: round(no[m] - inv[m], 1) for m in months}
def pairs(ms, f):
    el = q = st = 0; prev = False
    for a, b in zip(ms, ms[1:]):
        el += 1; hit = f(a) and f(b); q += hit
        st += hit and not prev; prev = hit
    return el, q, st
out = {'ISM_NO_INV': {'source': 'DBnomics ISM neword/inventories Index, indexed 2026-01-07, SECONDARY-SOURCE, vintage UNKNOWN',
  'start': months[0], 'end': months[-1], 'months': len(months), 'negative_months': sum(v < 0 for v in sp.values()),
  'zero_months': sum(v == 0 for v in sp.values()), 'positive_months': sum(v > 0 for v in sp.values()),
  'min': min(sp.values()), 'max': max(sp.values()), 'last_6': {m: sp[m] for m in months[-6:]}}}
for name, f in (('lt0_two', lambda m: sp[m] < 0), ('gt0_two', lambda m: sp[m] > 0), ('gte_4p1', lambda m: sp[m] >= 4.1)):
    e, q, s = pairs(months, f); out['ISM_NO_INV'][name] = {'eligible_pairs': e, 'qualifying_pairs': q, 'pct': round(100*q/e, 1), 'episode_starts': s}
out['ISM_NO_INV']['months_gte_4p1'] = sum(v >= 4.1 for v in sp.values())
rows = {}
for l in open('../../data/REGIONAL_BREADTH.tsv'):
    if l.startswith('#') or l.startswith('Ref_Period'): continue
    c = l.rstrip('\n').split('\t')
    if c[8] == 'COMPLETE': rows[c[0]] = int(c[7])
rows['2026-10'] = 1   # research/2026-10-31_backlog/REGIONAL_BREADTH_2026-10_COMPLETE.tsv, current as of 2026-10-31
ms = sorted(rows)
def adj(ms):
    # join only true calendar neighbours
    def nxt(m):
        y, mo = map(int, m.split('-')); return f'{y+(mo==12)}-{1 if mo==12 else mo+1:02d}'
    return ms, nxt
def count(sample, f):
    _, nxt = adj(sample); S = set(sample); el = q = st = 0; prev = False
    for m in sample:
        if nxt(m) in S:
            el += 1; h = f(m) and f(nxt(m)); q += h; st += h and not prev; prev = h
        else: prev = False
    return {'months': len(sample), 'hits': sum(f(m) for m in sample), 'eligible_pairs': el, 'qualifying_pairs': q, 'pct': round(100*q/el, 1), 'episode_starts': st}
ex = [m for m in ms if not ('2020-03' <= m <= '2021-06')]
rec = [m for m in ms if m >= '2016-11']
rf = lambda m: rows[m] <= 1
df = lambda m: rows[m] >= 3
out['REGIONAL'] = {'through': ms[-1], 'latest_two': {m: rows[m] for m in ms[-2:]},
  'recovery_le1_of5_two': {'FULL': count(ms, rf), 'RECENT10Y': count(rec, rf), 'EX_PANDEMIC': count(ex, rf)},
  'deterioration_ge3_of5_two': {'FULL': count(ms, df), 'RECENT10Y': count(rec, df), 'EX_PANDEMIC': count(ex, df)}}
json.dump(out, open('SURVEY_CALIBRATION.json', 'w'), indent=1)
print(json.dumps(out, indent=1))
