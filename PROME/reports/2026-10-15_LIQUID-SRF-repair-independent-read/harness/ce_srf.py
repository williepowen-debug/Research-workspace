"""Reader-devised SRF counterexamples. Usage: python ce_srf.py <ws-root>. No network (mocked fetch), no writes."""
import sys, io, contextlib
from decimal import Decimal
from pathlib import Path
from unittest import mock
WS = Path(sys.argv[1]).resolve()
sys.path.insert(0, str(WS / 'AGENTS/LIQUID/scripts'))
import boot, sofr_dispersion

def domestic(t_obs, m_obs):
    """Drive the REAL build_domestic through fred_series with raw FRED-shaped rows for both SRF legs."""
    def ff(sid, limit=5):
        if sid == 'RPONTSYD': return t_obs
        if sid == 'RPONMBSD': return m_obs
        return [{'error': 'synthetic unavailable'}]
    boot.RESULTS.clear()
    with mock.patch.object(boot, 'fred_fetch', side_effect=ff), \
         mock.patch.object(boot, 'fred_pairs', return_value=([], 'synthetic unavailable')), \
         mock.patch.object(sofr_dispersion, '_load', return_value=[]):
        with contextlib.redirect_stdout(io.StringIO()):
            boot.build_domestic()
    return [r for r in boot.RESULTS if r['label'] == 'SRF usage']

# CE5: exact-threshold ties. Every 3-decimal split of exactly $50.000B must grade NOT above 50 (strict >).
bad = []
for i in range(0, 50001):
    a = Decimal(i) / 1000; b = Decimal(50) - a
    rows = domestic([{'date': '2026-10-13', 'value': str(a)}], [{'date': '2026-10-13', 'value': str(b)}])
    if rows[0]['marker'] != '🟢': bad.append((str(a), str(b), rows[0]['display'], rows[0]['marker']))
print('CE5 tie sweep: 50,001 splits of exactly $50.000B through build_domestic; graded above 50 ->', len(bad), bad[:3])
r = domestic([{'date': '2026-10-13', 'value': '25.001'}], [{'date': '2026-10-13', 'value': '25.000'}])[0]
print('CE5b smallest-above tie (25.001+25.000=50.001):', r['display'], r['marker'], r['note'])

# CE6: newest row of one leg present but non-numeric (not FRED's "." which fetch.py drops). fred_series keeps
# obs[0]'s DATE but the first PARSEABLE value (an older row's) -> value/date misattribution before the guard sees it.
rows = domestic([{'date': '2026-10-13', 'value': 'ND'}, {'date': '2026-10-10', 'value': '30.000'}],
                [{'date': '2026-10-13', 'value': '30.000'}])
print('CE6 T newest unparseable (10-13), older 10-10 = 30; MBS 10-13 = 30 ->', [(x['display'], x['marker'], x['asof'], x['note']) for x in rows])

# CE7: non-publication day on one leg — T leg's latest is the prior business day (10-10), MBS published 10-13.
rows = domestic([{'date': '2026-10-10', 'value': '30.000'}], [{'date': '2026-10-13', 'value': '30.000'}])
print('CE7 mismatched (holiday on one leg) ->', [(x['display'], x['marker'], x['asof'], x['note']) for x in rows])
