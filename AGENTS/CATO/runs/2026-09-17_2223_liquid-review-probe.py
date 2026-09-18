"""CATO independent offline review probes; no network or owner-file writes."""
import importlib.util
import contextlib
import io
import json
import sys
import types
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
fake_fetch = types.ModuleType('fetch')
fake_fetch.fred_fetch = lambda *a, **k: []
fake_fetch.price_fetch = lambda *a, **k: {}
sys.modules['fetch'] = fake_fetch

def load(name, path):
    spec = importlib.util.spec_from_file_location(name, ROOT / path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

boot = load('liquid_boot_review', 'AGENTS/LIQUID/scripts/boot.py')
watch = load('liquid_watch_review', 'AGENTS/LIQUID/scripts/hy_oas_watch.py')
classify, hy = watch._load_config()

def emit(name, result):
    print(json.dumps({'case': name, 'actual': result}, ensure_ascii=False))

def credit(hy_values, euro_date='2026-09-16'):
    base = {
        'BAMLH0A0HYM2': (hy_values[0], '2026-09-16', hy_values, None),
        'BAMLH0A3HYC': (10.76, '2026-09-16', [10.76], None),
        'BAMLH0A1HYBB': (1.55, '2026-09-16', [1.55], None),
        'BAMLC0A0CM': (.78, '2026-09-16', [.78], None),
        'BAMLHE00EHYIOAS': (3.0, euro_date, [3.0], None),
    }
    boot.fred_series = lambda sid, n=6: base[sid]
    boot.RESULTS.clear()
    boot.build_credit()
    return {r['label']: r for r in boot.RESULTS}

for name, vals in [('pretrigger_268_267', [2.68, 2.67]),
                   ('confirmation_321_322', [3.21, 3.22]),
                   ('strict_280_boundary', [2.8, 2.79])]:
    emit(name, credit(vals)['HY OAS'])
emit('euro_missing_date', credit([2.7], None)['Euro HY OAS'])

boot.RESULTS.clear()
boot.diff_dated('CREDIT', 'helper_control', 300, None, 270, '2026-09-16', lambda _: ('green', 'graded'))
emit('shared_helper_missing_date_control', boot.RESULTS[-1])

dom = {sid: (v, d, [v], None) for sid, v, d in [
    ('SOFR', 3.87, '2026-09-17'),
    ('SOFR75', 3.92, '2026-09-17'),
    ('SOFR99', 3.95, '2026-09-16'),
    ('DGS2', 4.74, '2026-09-16'),
    ('DGS10', 5.01, '2026-09-16'),
    ('DGS30', 5.35, '2026-09-16'),
    ('WRESBAL', 3013800, '2026-09-16'),
    ('RRPONTSYD', .28, '2026-09-17'),
    ('RPONTSYD', 40, '2026-09-17'),
    ('RPONMBSD', 20, '2026-09-16'),
]}
boot.fred_series = lambda sid, n=6: dom[sid]
boot.fred_pairs = lambda sid, n=14: ([('2026-09-17', 3.90), ('2026-09-16', 3.65)], None)
boot.RESULTS.clear()
boot.build_domestic()
for row in boot.RESULTS:
    if row['label'] in ('SOFR', 'SOFR99−SOFR (dispersion)', 'SRF usage', 'SOFR-IORB', 'SOFR99−IORB (079 ARM leg)'):
        emit('domestic_' + row['label'], row)

prior = {'zone': 'green', 'sev': 0, 'obs_date': '2026-09-10', 'sub260': 0}
one = watch.decide(259, '2026-09-11', prior, hy, classify)
# Real publication on Monday is 270, but watcher misses Monday's run.
# main() fetches 2 observations yet passes only latest to decide().
missed = watch.decide(259, '2026-09-15', one['state'], hy, classify)
emit('missed_reset_259_270_259_but_middle_not_polled', missed)
two = watch.decide(258, '2026-09-14', one['state'], hy, classify)
repeat = watch.decide(258, '2026-09-14', two['state'], hy, classify)
emit('repeat_same_published_observation_after_fire', repeat)
reset = watch.decide(270, '2026-09-15', two['state'], hy, classify)
again1 = watch.decide(259, '2026-09-16', reset['state'], hy, classify)
again2 = watch.decide(258, '2026-09-17', again1['state'], hy, classify)
emit('second_fire_after_terminal_fire_and_reset', again2)
emit('watcher_existing_selftest_rc', watch.selftest())

obdc = (11.11 / 11.40 - 1) * 100
bizd = (13.10 / 13.33 - 1) * 100
emit('obdc_minus_bizd_return_pp', round(obdc-bizd, 6))

# End-to-end display probes: a safe row object is insufficient if render hides it.
dom.update({sid: (v, '2026-09-17', [v], None) for sid, v in [
    ('SOFR', 3.62), ('SOFR75', 3.67), ('SOFR99', 3.70),
    ('DGS2', 4.2), ('DGS10', 4.4), ('DGS30', 4.95),
    ('RPONTSYD', 0), ('RPONMBSD', 0),
]})
boot.fred_pairs = lambda sid, n=14: ([('2026-09-16', 3.65)], None)
boot.RESULTS.clear()
boot.build_domestic()
with contextlib.redirect_stdout(io.StringIO()) as buf:
    boot.render(False)
emit('stale_iorb_full_domestic_default_render', buf.getvalue())
emit('stale_iorb_arm_row_hidden_by_default', next(r for r in boot.RESULTS if r['label']=='SOFR99−IORB (079 ARM leg)'))

boot.price_fetch = lambda tickers: {t: {'price': 100.0, 'asof': '2026-09-16'} for t in tickers}
boot.RESULTS.clear()
boot.build_prices()
for verbose in (False, True):
    with contextlib.redirect_stdout(io.StringIO()) as buf:
        boot.render(verbose)
    emit('prices_render_verbose_'+str(verbose), {'date_visible': '2026-09-16' in buf.getvalue(), 'stdout': buf.getvalue()})

boot.price_fetch = lambda tickers: {t: {'price': 100.0} for t in tickers}
boot.RESULTS.clear()
boot.build_prices()
with contextlib.redirect_stdout(io.StringIO()) as buf:
    boot.render(False)
emit('all_price_dates_missing_default_render', buf.getvalue())
