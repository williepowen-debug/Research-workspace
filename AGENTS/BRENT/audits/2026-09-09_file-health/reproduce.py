"""Offline audit probes, using synthetic inputs. Does not alter production code.

These assertions preserve observed defects, not desired production behavior.
After repairs, failure here means re-audit the observation; do not restore bugs.
"""
import contextlib
import importlib.util
import io
import json
import time
from datetime import date, timedelta
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

HERE = Path(__file__).resolve().parent
BRENT = HERE.parents[1]

def module(name):
    spec = importlib.util.spec_from_file_location(name, BRENT/'scripts'/f'{name}.py')
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

eia = module('eia_weekly')
thresholds = module('thresholds')
predictions = module('predictions_due')
cot = module('cot_grade')
countdown = module('catalyst_countdown')
results = {}

# A quote without a current observation falls back to its old previous close.
fake = SimpleNamespace(tickers={'USO':SimpleNamespace(info={
    'previousClose':101.0, 'regularMarketTime':946684800})})
with patch.object(thresholds.yf, 'Tickers', return_value=fake):
    result = thresholds.get_prices(['USO'])
assert result['USO']['price'] == 101.0 and 'date' not in result['USO']
results['previous_close_accepted_without_quote_date'] = result

# Even one metric yields LIVE/rc0; gasoline's missing value prints 'not fired'.
def util_only(series, *args, **kwargs):
    return [{'date':'2026-08-28','value':98.0}] if series == 'WPULEUS3' else []
fake_forge = SimpleNamespace(EIA_API_KEY='synthetic-only', eia_fetch=util_only)
with patch.object(eia,'_forge',fake_forge), patch.object(eia,'HAVE_FORGE',True), patch.object(eia.sys,'argv',['eia_weekly.py','--live']):
    output = io.StringIO()
    with contextlib.redirect_stdout(output):
        rc = eia.main()
assert rc == 0 and 'LIVE (EIA v2 API)' in output.getvalue() and 'not fired' in output.getvalue()
results['single_metric_live_success'] = {'rc':rc, 'output':output.getvalue()}

# Gasoline comparison drops missing values and indexes 52 rows back; no date join.
weekly = [{'date':(date(2026,8,28)-timedelta(days=7*i)).isoformat(),
           'value':None if i==1 else 100.0} for i in range(60)]
def gap_series(series,*args,**kwargs):
    return weekly if series=='WGFUPUS2' else []
fake_forge.eia_fetch = gap_series
with patch.object(eia,'_forge',fake_forge), patch.object(eia,'HAVE_FORGE',True):
    result = eia.fetch_live_metrics()
assert result['gas_yoy_latest'] == 0.0
results['missing_week_still_computes_yoy'] = result

# Actual newest local file is a publication notice, not a numerical report.
latest = eia.find_latest_eia_file()
parsed = eia.extract_metrics(latest.read_text())
results['actual_latest_local_file'] = {'file':str(latest.relative_to(BRENT)), 'metrics':parsed}
assert latest.name == 'eia_2026-09-09.md' and not parsed

# Local source age is mtime based in main; parser/readout can call a green LOCAL
# source a LIVE API pull solely because it begins with a green icon.
old_report = io.StringIO('synthetic old report')
fake_path = SimpleNamespace(name='eia_2026-04-15.md', stat=lambda:SimpleNamespace(st_mtime=time.time()))
with patch.object(eia,'find_latest_eia_file',return_value=fake_path), patch.object(eia,'extract_metrics',return_value={'util':98.0,'week_ending':'2026-04-10'}), patch('builtins.open',return_value=old_report), patch.object(eia.sys,'argv',['eia_weekly.py','--local']):
    output = io.StringIO()
    with contextlib.redirect_stdout(output):
        rc = eia.main()
assert '0d old' in output.getvalue() and 'NOTE: LIVE pull via EIA v2 API' in output.getvalue()
results['old_local_report_shows_fresh_and_live_note'] = {'rc':rc,'output':output.getvalue()}

# Existing COT implementation has correct deadband precedence despite stale docs.
boundaries={n:cot.leg_a(n) for n in [109164,109165,113745,118325,118326]}
assert list(boundaries.values()) == ['SPENT','NO-VERDICT','NO-VERDICT','NO-VERDICT','NOT-SPENT']
results['cot_boundaries_correct'] = boundaries

# 'Trading days' counts weekdays, including the Labor Day exchange holiday.
days = countdown.trading_days_between(date(2026,9,4),date(2026,9,8))
assert days == 2
results['labor_day_counted_as_trading_day'] = days

due, upcoming, unparsed, conditional = predictions.scan(today=date(2027,3,7))
assert 'BRT-07' in [r[0] for r in conditional] and 'BRT-07' not in [r[0] for r in due]
results['outer_bound_not_in_due_scan'] = {'as_of':'2027-03-07','conditional':[r[0] for r in conditional]}

# Future event-conditional rows without an OUTER BOUND cause the display to fail.
with patch.object(predictions,'scan',return_value=([],[],[],[('SYNTHETIC','Within 7 days of reopening','OPEN')])):
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            predictions.main()
    except AttributeError as exc:
        results['conditional_without_bound_display_crash'] = str(exc)
assert 'conditional_without_bound_display_crash' in results

(HERE/'reproductions.json').write_text(json.dumps(results,indent=2)+'\n')
print('Nine offline observations saved; synthetic prices are not market data.')
