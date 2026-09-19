#!/usr/bin/env python3
"""Offline independent review; pinned owner code, temporary output, no owner writes."""
import contextlib
import csv
import io
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import types
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[3]
REV = '885013a68550d83113585bb9a8dba5ec03665e7b'

def blob(path):
    return subprocess.check_output(['git', 'show', f'{REV}:{path}'], cwd=ROOT, text=True)

def rows(path):
    return list(csv.DictReader(io.StringIO('\n'.join(
        x for x in blob(path).splitlines() if not x.startswith('#'))), delimiter='\t'))

def module(path):
    m = types.ModuleType('reviewed_owner_module')
    m.__file__ = str(ROOT / path)
    exec(compile(blob(path), m.__file__, 'exec'), m.__dict__)
    return m

def month(y, m):
    return y * 12 + m - 1

print('PIN', REV)
primary = json.loads(Path(__file__).with_name('2026-09-19_1303_marco-bts-primary.json').read_text())
data = {(r['airport'], r['carrier']): {x['period']: x['total'] for x in r['rows']}
        for r in primary['results']}
print('\nPRIMARY BTS: independently retrieved, selected airport/carrier verified')
for ap in ('MCO', 'FLL', 'MIA'):
    total, nk = data[ap, 'All'], data[ap, 'NK']
    print(ap, 'NK numeric coverage', min(nk), max(nk))
    for p in ('05', '06'):
        prior, now = '2025-' + p, '2026-' + p
        raw = 100 * (total[now] / total[prior] - 1)
        if ap == 'MIA':
            print(ap, now, 'raw', round(raw, 5), 'NK not present in these periods')
            continue
        adjusted = 100 * ((total[now] - nk[now]) / (total[prior] - nk[prior]) - 1)
        offset = 100 * (1 - (total[prior] - total[now]) / (nk[prior] - nk[now]))
        print(ap, now, 'raw', round(raw, 5), 'exNK', round(adjusted, 5),
              'NK prior/current', nk[prior], nk[now], 'passenger-offset %', round(offset, 5))
print('Historical MCO May offset (old total decline 42,884, NK decline 276,008):',
      100 * (1 - 42884 / 276008))
print('Expiry counterexample: May27 total 998000 vs May26 total 1000000/NK3150;',
      'raw', 100 * (998000 / 1000000 - 1), 'exNK', 100 * (998000 / 996850 - 1))
print('Causal counterexample: prior 100 passengers (30 NK + 70 other), current 90 all other;',
      'raw -10%, exNK', 100 * (90 / 70 - 1), '; does not identify latent demand or capacity')

print('\nBTS HELPER: documented carrier pull overwrites all-carrier output')
helper = module('AGENTS/MARCO/tools/bts_airport_pull.py')
with tempfile.TemporaryDirectory(prefix='cato-marco-') as tmp:
    helper.OUT = Path(tmp) / 'bts_airport_pax.tsv'
    helper.pull = lambda ap, carrier, session: {(2026, 6): (100, 0, 100)}
    with contextlib.redirect_stdout(io.StringIO()):
        with patch.object(sys, 'argv', ['bts_airport_pull.py', 'MCO', 'FLL', 'MIA']):
            helper.main()
        before = helper.OUT.read_text()
        with patch.object(sys, 'argv', ['bts_airport_pull.py', 'MCO', '--carrier', 'NK']):
            helper.main()
    after = helper.OUT.read_text()
    assert 'carrier=All' in before and 'FLL\t' in before and 'MIA\t' in before
    assert 'carrier=NK' in after and 'FLL\t' not in after and 'MIA\t' not in after
    print('REPRODUCED: one NK/MCO pull replaces All/MCO+FLL+MIA baseline.')

print('\nMAR-24: recompute monthly events from pinned all-carrier baseline')
traffic = {}
for r in rows('AGENTS/MARCO/baselines/bts_airport_pax.tsv'):
    traffic.setdefault(r['airport'], {})[month(int(r['year']), int(r['month']))] = int(r['total'])
aps = ('MCO', 'FLL', 'MIA')
periods = sorted(set.intersection(*(set(traffic[ap]) for ap in aps)))
signs = {t: all(traffic[ap][t] < traffic[ap][t-12] for ap in aps)
         for t in periods if all(t-12 in traffic[ap] for ap in aps)}
covid = set(range(month(2020, 3), month(2021, 6) + 1))
windows = [t for t in signs if all(t+j in signs for j in (1, 2, 3))]
seed_only = [t for t in windows if t not in covid]
full = [t for t in windows if all(t+j not in covid for j in range(4))]
event = lambda t: any(signs[t+j] for j in (1, 2, 3))
conditional = [t for t in full if signs[t]]
for name, population in [('COVID excluded only at seed', seed_only),
                         ('COVID excluded throughout window', full),
                         ('Conditional on negative seed, full exclusion', conditional)]:
    n = sum(event(t) for t in population)
    print(name, n, '/', len(population), '=', round(100*n/len(population), 5), '%')
print('65-87 range equals iid conversions:', 100*(1-.7**3), 100*(1-.5**3))
mia = traffic['MIA']
q3 = [(y, [month(y, m) for m in (7, 8, 9)]) for y in range(2003, 2026)
      if y not in (2020, 2021)]
q3 = [(y, ts) for y, ts in q3 if all(t in mia and t-12 in mia for t in ts)]
print('MIA Q3 empirical monthly negative', sum(mia[t] < mia[t-12] for _, ts in q3 for t in ts),
      '/', len(q3)*3, '; quarters with any negative',
      sum(any(mia[t] < mia[t-12] for t in ts) for _, ts in q3), '/', len(q3))

print('\nID-01: common two-transition windows, pinned rounded gap values')
gaps = [(r['period'], float(r['gap_auto_minus_air']))
        for r in rows('AGENTS/MARCO/baselines/statcan_canadian_return.tsv')
        if r['gap_auto_minus_air']]
diffs = [round(b[1]-a[1], 8) for a, b in zip(gaps, gaps[1:])]
pairs = list(zip(diffs, diffs[1:]))
print('gaps', gaps)
print('changes', diffs)
print('single', sum(d <= -2.5 for d in diffs), '/', len(diffs))
print('either of two', sum(a <= -2.5 or b <= -2.5 for a,b in pairs), '/', len(pairs))
print('both of two', sum(a <= -2.5 and b <= -2.5 for a,b in pairs), '/', len(pairs))
print('cumulative', sum(a+b <= -2.5 for a,b in pairs), '/', len(pairs))

print('\nNew expiry row: existing owner integrity check')
sys.path.insert(0, str(ROOT / 'AGENTS/MARCO/scripts'))
countdown = module('AGENTS/MARCO/scripts/catalyst_countdown.py')
expiry = [r for r in rows('AGENTS/MARCO/docket/CATALYSTS.tsv') if r['date'] == '2027-08-15']
assert len(expiry) == 1
print(countdown.check_integrity(expiry))
