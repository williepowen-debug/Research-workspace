"""One-off arithmetic on visually checked issuer tables and captured source quotes.

Not a monitor or a forecast grader. Reads only the saved Treasury capture.
"""
import csv
import hashlib
import json
from decimal import Decimal as D
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]

def pct(a, b):
    return float((D(str(a)) / D(str(b)) - 1) * 100)

metals = {}
for name, q3, q2, nine, h1, low, high, pace in [
    ('palladium', 736, 590, 1934, 1199, 2415, 2465, 634),
    ('platinum', 192, 145, 472, 281, 616, 636, 178),
]:
    residual = nine - h1
    metals[name] = {
        'unit': 'thousand troy ounces (koz)',
        'q3_reported': q3, 'q2_reported': q2, 'nine_month_reported': nine,
        'h1_original_issuer': h1, 'q3_from_rounded_totals': residual,
        'reported_minus_residual': q3 - residual,
        'qoq_percent': pct(q3, q2),
        'guidance_2026': [low, high],
        'q4_required': [low - nine, high - nine],
        'registered_upper_pace_boundary': pace,
        'both_methods_above_registered_pace': q3 > pace and residual > pace,
        'guidance_change': 'UNCHANGED',
    }
    assert q3 - residual == 1
    assert metals[name]['both_methods_above_registered_pace']

with (HERE / 'treasury_real.csv').open() as f:
    rates = {r['Date']: D(r['10 YR']) for r in csv.DictReader(f)}
gold = []
for date, price in [('10/22/2026', '4060.40'), ('10/23/2026', '4007.90')]:
    p = D(price)
    gold.append({
        'date': date, 'contract': 'COMEX gold December 2026 (GCZ26)',
        'reported_settlement_usd_per_oz': float(p),
        'source_status': 'MIRROR, Hammerstone commentary hosted by eOption; not certified',
        'primary_treasury_real_10y_percent': float(rates[date]),
        'price_minus_4050_usd_per_oz': float(p-D('4050')),
        'numerical_conjunction_if_certified': p < D('4050') and rates[date] >= D('2.40'),
        'certified_grade': 'UNRESOLVED',
    })
assert gold[0]['numerical_conjunction_if_certified'] is False
assert gold[1]['numerical_conjunction_if_certified'] is True

preserved = {}
for name in [
    'workbook/PREDICTIONS.tsv', 'CLAUDE.md',
    'palladium/research/2026-10-23_nornickel-9M-read-setup.md',
    'gold/research/2026-10-23_WQ451-decomposition-letter.md',
]:
    p = ROOT / 'AGENTS/MIDAS' / name
    preserved[name] = hashlib.sha256(p.read_bytes()).hexdigest()

result = {'nornickel': metals, 'gold': gold,
          'gold_contract_identity': {'date': '2026-10-22',
             'october_contract_last_usd_per_oz': 4042.80,
             'december_contract_last_usd_per_oz': 4060.40,
             'source': 'AP table hosted by Raymond James/Barchart; column Last, not settlement certification'},
          'preserved_sha256': preserved}
(HERE / 'calculations.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
