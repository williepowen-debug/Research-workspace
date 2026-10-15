"""Read #2 reader-devised CE6-class counterexamples (boot.py). Usage: python ce2_srf.py <ws-root>. Mocked fetch; no writes."""
import sys, io, contextlib, traceback
from pathlib import Path
from unittest import mock
WS = Path(sys.argv[1]).resolve()
sys.path.insert(0, str(WS / 'AGENTS/LIQUID/scripts'))
import boot, sofr_dispersion

def rows(*pairs): return [({'date': d, 'value': v} if d is not None else {'value': v}) for d, v in pairs]
def drive(builder, feeds, labels):
    def ff(sid, limit=5):
        return feeds.get(sid, [{'error': 'synthetic unavailable'}])
    boot.RESULTS.clear()
    try:
        with mock.patch.object(boot, 'fred_fetch', side_effect=ff), \
             mock.patch.object(boot, 'fred_pairs', return_value=([], 'synthetic unavailable')), \
             mock.patch.object(sofr_dispersion, '_load', return_value=[]), \
             contextlib.redirect_stdout(io.StringIO()):
            builder()
    except Exception as e:
        return f'RAISED {type(e).__name__}: {e}'
    return [(r['label'], r['display'], r['marker'], r['asof'], r['note'][:150]) for r in boot.RESULTS if r['label'] in labels]

SRF = ('SRF usage',)
def srf(t, m): return drive(boot.build_domestic, {'RPONTSYD': t, 'RPONMBSD': m}, SRF)

print('M1 T newest parseable (10-13=30), OLDER row non-numeric; MBS 10-13=30 ->',
      srf(rows(('2026-10-13', '30.000'), ('2026-10-10', 'ND')), rows(('2026-10-13', '30.000'))))
print('M2 BOTH legs newest non-numeric, older rows same day 10-10 ->',
      srf(rows(('2026-10-13', 'ND'), ('2026-10-10', '30.000')), rows(('2026-10-13', 'ND'), ('2026-10-10', '30.000'))))
print('M2b BOTH legs newest non-numeric, older rows on DIFFERENT days ->',
      srf(rows(('2026-10-13', 'ND'), ('2026-10-10', '30.000')), rows(('2026-10-13', 'ND'), ('2026-10-09', '30.000'))))
stale = rows(('2026-10-13', 'ND'), ('2026-10-10', 'ND'), ('2026-10-09', 'ND'), ('2026-10-08', 'ND'), ('2026-10-07', 'ND'), ('2026-10-06', '30.000'))
print('M3 T only parseable row 5 obs back (10-06); MBS fresh 10-13 ->', srf(stale, rows(('2026-10-13', '30.000'))))
print('M3b BOTH legs only parseable 10-06 ->', srf(stale, stale))
print('M4 T newest non-numeric, parseable row has NO date key ->',
      srf(rows(('2026-10-13', 'ND'), (None, '30.000')), rows(('2026-10-13', '30.000'))))
print('M5 T newest "nan" (parses as float) ->', srf(rows(('2026-10-13', 'nan'), ('2026-10-10', '30.000')), rows(('2026-10-13', '30.000'))))
print('M5b T newest "inf" ->', srf(rows(('2026-10-13', 'inf'), ('2026-10-10', '30.000')), rows(('2026-10-13', '30.000'))))

# fred_series direct: every caller now sees the value's own row date
with mock.patch.object(boot, 'fred_fetch', return_value=rows(('2026-10-13', 'ND'), ('2026-10-10', '2.59'), ('2026-10-09', '2.58'))):
    print('M6 fred_series newest ND ->', boot.fred_series('X'))
with mock.patch.object(boot, 'fred_fetch', return_value=rows(('2026-10-13', '2.59'), ('2026-10-10', 'ND'), ('2026-10-09', '2.58'))):
    print('M6b fred_series INTERIOR ND (newest parses) ->', boot.fred_series('X'))

# Wrong-owner reach: other two-leg composites that consume fred_series dates (diff_dated)
HY = ('HY OAS', 'HY-IG basis', 'CCC-BB gap')
print('M7 HY newest ND (older 10-10=2.90), IG 10-13=1.00 ->',
      drive(boot.build_credit, {'BAMLH0A0HYM2': rows(('2026-10-13', 'ND'), ('2026-10-10', '2.90')),
                                'BAMLC0A0CM': rows(('2026-10-13', '1.00'))}, HY))
print('M8 HY dashboard: newest 2.59 [10-13], INTERIOR ND [10-10], 2.59 [10-09] ->',
      drive(boot.build_credit, {'BAMLH0A0HYM2': rows(('2026-10-13', '2.59'), ('2026-10-10', 'ND'), ('2026-10-09', '2.59'))}, ('HY OAS',)))
print('M9 Reserves newest ND + parseable row with NO date key ->',
      drive(boot.build_domestic, {'WRESBAL': rows(('2026-10-08', 'ND'), (None, '2900000'))}, ('Reserves',)))
