"""Bounded documentation recount of saved evidence; no network or live grading.

Run from the repository root. Uses the unchanged dispersion instrument's pure
analyze function. Frozen probabilities, thresholds and live verdict are untouched.
"""
import gzip
import hashlib
import json
import sys
from datetime import date
from decimal import Decimal
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / 'AGENTS/LIQUID/scripts'))
import sofr_dispersion as sd

SOURCE = ROOT / 'AGENTS/LIQUID/research/2026-10-14_credit-funding-refresh/evidence-full.json.gz'
raw = json.load(gzip.open(SOURCE, 'rt'))
s = {k: {r['date']: Decimal(r['value']) for r in rows}
     for k, rows in raw['latest_revised'].items()}
ice = sorted(set(s['BAMLH0A2HYB']) & set(s['BAMLH0A3HYC']))
sofr = sorted(s['SOFR'])
listed = ['2024-08-06', '2025-03-10', '2025-04-07', '2025-10-14',
          '2025-11-18', '2026-02-12', '2026-03-16']
run = 0
reset_triggers = []
for i, d in enumerate(ice):
    if i < 15 or d > '2026-09-23':
        continue
    b = round(s['BAMLH0A2HYB'][d] * 100) - round(s['BAMLH0A2HYB'][ice[i-15]] * 100)
    c = round(s['BAMLH0A3HYC'][d] * 100) - round(s['BAMLH0A3HYC'][ice[i-15]] * 100)
    run = run + 1 if b >= 28 and c >= 0 else 0
    if run == 3:
        reset_triggers.append(d)

pairs = [(date.fromisoformat(d), float((s['SOFR75'][d] - s['IORB'][d]) * 100))
         for d in sorted(set(s['SOFR75']) & set(s['IORB']))
         if not sd.is_qe(date.fromisoformat(d))]
zs = {p[0].isoformat(): sd.analyze(pairs[:i+1]) for i, p in enumerate(pairs)}
windows = []
for t in sorted(set(listed) | set(reset_triggers)):
    for label, dates in [('ICE', ice), ('SOFR', sofr)]:
        i = dates.index(t)
        lo, hi = dates[i-10], dates[i+10]
        witnesses = [{'date': d, 'z': round(a['z'], 6)}
                     for d, a in zs.items()
                     if lo <= d <= hi and a and a['z'] is not None and a['z'] >= 4]
        srfs = [(d, float(v)) for d, v in s['RPONTTLD'].items() if lo <= d <= hi]
        s99s = [(d, float((s['SOFR99'][d] - s['IORB'][d]) * 100))
                for d in sorted(set(s['SOFR99']) & set(s['IORB'])) if lo <= d <= hi]
        max_srf = max(v for _, v in srfs)
        max99 = max(v for _, v in s99s)
        # No historical ARM replay: its operative exclusion-list perimeter is later.
        # Positive windows already qualify on z. Other windows cannot reach ARM
        # because even their unfiltered maximum is below its necessary 30bp line.
        eligible = bool(witnesses) or max_srf >= 50
        if not eligible and max99 >= 30:
            raise RuntimeError('Historical ARM membership unresolved: no negative classification allowed')
        windows.append({'trigger': t, 'list': label, 'start': lo, 'end': hi,
                        'published_date_list': dates[i-10:i+11],
                        'listed_in_original': t in listed, 'z_witnesses': witnesses,
                        'srf_max_b': max_srf, 'sofr99_iorb_max_bp': round(max99, 6),
                        'strict_funding_present': eligible})

qualifying = sorted({r['trigger'] for r in windows if r['strict_funding_present']})
out = {'source': str(SOURCE.relative_to(ROOT)), 'source_sha256': hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
       'source_retrieved_at': raw['retrieved_at'], 'basis': 'October14 saved latest-revised history; not original September25 vintage',
       'ice_available_start': ice[0], 'historical_cutoff': '2026-09-23',
       'original_listed_triggers': listed, 'run_reset_convention': 'one trigger on the third qualifying consecutive published observation; any failed observation resets run to zero',
       'run_reset_triggers': reset_triggers, 'qualifying_trigger_dates': qualifying,
       'listed_window_count': {'numerator': len(set(qualifying) & set(listed)), 'denominator': len(listed)},
       'reset_window_count': {'numerator': len(set(qualifying) & set(reset_triggers)), 'denominator': len(reset_triggers)},
       'windows': windows,
       'limits': ['No original seven-trigger reset/deduplication code recovered.',
                  'Rolling history now starts October16,2023, versus October2 in the original reference sample; earliest lost observations cannot be reconstructed here.',
                  'No thresholds, probabilities, episode-independent rates or live grades recalculated.',
                  'No historical ARM replay outside its current exclusion-list perimeter; z alone establishes both positive windows.',
                  'Loose original 3-of-7 accompaniment criterion undefined; not reconstructed or reusable.']}
Path(__file__).with_name('historical-counts.json').write_text(json.dumps(out, indent=2) + '\n')
print('Original listed windows:', out['listed_window_count'], 'run-reset windows:', out['reset_window_count'])
print('Qualifying dates:', qualifying)
