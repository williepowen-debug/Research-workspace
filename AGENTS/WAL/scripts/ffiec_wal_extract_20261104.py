"""Reproduce WAL's bounded Q3 extraction from CATO's verified complete sources.

No network, credentials, grading writer, weight changes, or peer-bank study.
Uses the existing approved 70-field mapping; total assets is the MI3 ledger's
existing auxiliary field. Full source bytes and receipt are preserved by WAL.
"""
import csv
import hashlib
import io
import json
from datetime import datetime, timezone
from decimal import Decimal
from pathlib import Path

from ffiec_wal_analyze_20261014 import DIRECT, SCHEDULES

WAL = Path(__file__).resolve().parents[1]
ROOT = WAL.parents[1]
PROVIDER = ROOT / 'AGENTS/CATO/runs/2026-11-04_ffiec-access'
RAW = WAL / 'sources/ffiec_2026-11-04_verified'
OUT = WAL / 'research/2026-11-04_Q3-extraction'
MAPPING = {**DIRECT, 'total_assets_K': 'RCON2170'}


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def ratio(a, b):
    return None if a is None or b is None or b == 0 else Decimal(100) * a / b


def add(values):
    return None if any(v is None for v in values) else sum(values)


def serial(value):
    if isinstance(value, Decimal):
        return int(value) if value == value.to_integral_value() else float(value)
    raise TypeError(type(value).__name__)


def main():
    RAW.mkdir(exist_ok=True)
    OUT.mkdir(exist_ok=True)
    receipt_copy = RAW / 'CATO_receipt.json'
    provider_receipt = (receipt_copy if receipt_copy.exists() else PROVIDER / 'receipt.json').read_bytes()
    receipt = json.loads(provider_receipt)
    existing = RAW / 'provenance.json'
    provenance = {
        'desk': 'WAL', 'retrieving_desk': 'CATO',
        'source_receipt': str((PROVIDER / 'receipt.json').relative_to(ROOT)),
        'source_receipt_sha256': sha(provider_receipt),
        'source_format': 'SDF', 'source_entity': 'Western Alliance Bank RSSD 3138146',
        'preserved_at_utc': (json.loads(existing.read_text())['preserved_at_utc']
                             if existing.exists() else datetime.now(timezone.utc).isoformat()),
        'records': [],
    }
    # Exact byte copies, never a CSV reserialization of the complete document.
    assert not receipt_copy.exists() or receipt_copy.read_bytes() == provider_receipt
    receipt_copy.write_bytes(provider_receipt)
    metrics, fields, schedules, checks = {}, [], [], []
    records = [r for r in receipt['records'] if 'path' in r]
    assert len(records) == 2
    for rec in records:
        upstream = ROOT / rec['path']
        retained = RAW / upstream.name
        original = retained if retained.exists() else upstream
        raw = original.read_bytes()
        assert rec['endpoint'] == 'https://ffieccdr.azure-api.us/public/RetrieveFacsimile'
        assert rec['http_status'] == 200 and rec['status'] == 'VERIFIED_SOURCE'
        assert sha(raw) == rec['sha256'] and len(raw) == rec['bytes']
        date = datetime.strptime(rec['period'], '%m/%d/%Y').strftime('%Y-%m-%d')
        assert date in ('2026-06-30', '2026-09-30')
        rows = list(csv.DictReader(io.StringIO(raw.decode('utf-8-sig')), delimiter=';'))
        assert len(rows) == rec['rows']
        assert all(r['Bank RSSD Identifier'] == '3138146' and
                   r['Call Date'] == date.replace('-', '') for r in rows)
        data = {r['MDRM #']: r for r in rows}
        assert len(data) == len(rows)
        assert data['RCON1766']['Value']
        target = RAW / upstream.name
        assert not target.exists() or target.read_bytes() == raw
        target.write_bytes(raw)
        provenance['records'].append({**rec, 'upstream_path': rec['path'],
                                      'path': str(target.relative_to(ROOT))})
        checks.append(date + ': source bytes/hash/row count/RSSD/period/unique MDRMs verified')
        if date == '2026-06-30':
            baseline = WAL / 'sources/ffiec_2026-10-14/WAL_2026-06-30.sdf'
            assert sha(baseline.read_bytes()) == sha(raw)
            checks.append('June source byte-identical to WAL accepted October 14 source')
        m = {'quarter': date}
        for key, code in MAPPING.items():
            row = data.get(code)
            value = None
            if row is None:
                status = ('NOT_EXPECTED_Q3_SEMIANNUAL' if date == '2026-09-30' and
                          code in ('RCONC410', 'RCONC411') else 'MISSING')
            elif not row['Value'].strip():
                status = 'REPORTED_BLANK'
            else:
                value = Decimal(row['Value'].replace(',', '').removesuffix('%'))
                status = 'REPORTED'
            m[key] = value
            fields.append({'quarter': date, 'field': key, 'MDRM': code,
                           'value': value, 'status': status,
                           'units': ('percent' if key == 'bank_CET1_reported_pct' else
                                     'election flag' if key == 'AOCI_optout' else 'USD thousands'),
                           'source_sha256': rec['sha256'],
                           'source_path': str(target.relative_to(ROOT)),
                           'schedule': row['Call Schedule'] if row else '',
                           'line': row['Line Number'] if row else '',
                           'definition': row['Short Definition'] if row else '',
                           'raw_value': row['Value'] if row else '',
                           'last_update': row['Last Update'] if row else ''})
        absent = {f['MDRM'] for f in fields if f['quarter'] == date and f['value'] is None}
        assert absent == ({'RCONC410', 'RCONC411'} if date == '2026-09-30' else set())
        for kind, parts in [('funded', ['mortgage', 'business', 'PE', 'consumer', 'other']),
                            ('unused', ['unused_mortgage', 'unused_business', 'unused_PE',
                                        'unused_consumer', 'unused_other'])]:
            subtotal = add([m['ndfi_' + part + '_K'] for part in parts])
            residual = subtotal - m['ndfi_' + kind + '_K']
            assert abs(residual) <= 1  # Existing October 14 $1K source-precision tolerance.
            m['ndfi_' + kind + '_subtype_residual_K'] = residual
            checks.append(f'{date}: NDFI {kind} subtype residual {residual}K; existing <=1K tolerance')
        m['MI3_pct_item4'] = ratio(m['MI3_K'], m['CI_K'])
        m['ndfi_pct_total_loans'] = ratio(m['ndfi_funded_K'], m['loans_total_K'])
        m['ndfi_pct_HFI'] = ratio(m['ndfi_funded_K'], m['HFI_K'])
        m['ndfi_nonaccrual_pct'] = ratio(m['ndfi_nonaccrual_K'], m['ndfi_funded_K'])
        m['ndfi_funded_plus_unused_face_K'] = add([m['ndfi_funded_K'], m['ndfi_unused_K']])
        m['modified_PD_or_nonaccrual_K'] = add([m[k] for k in
            ['modified_PD30_K', 'modified_PD90_K', 'modified_nonaccrual_K']])
        m['modified_combined_K'] = add([m['modified_performing_K'], m['modified_PD_or_nonaccrual_K']])
        m['PD90_excluding_GNMA_K'] = m['PD90_total_K'] - m['GNMA_PD90_K']
        m['NCO_YTD_K'] = m['gross_CO_YTD_K'] - m['recoveries_YTD_K']
        m['bank_CET1_computed_pct'] = ratio(m['bank_CET1_K'], m['bank_RWA_K'])
        assert abs(m['bank_CET1_computed_pct'] - m['bank_CET1_reported_pct']) < Decimal('.0001')
        checks.append(date + ': bank CET1 numerator/RWA ties reported ratio at existing tolerance')
        for row in rows:
            if row['Call Schedule'] in SCHEDULES:
                schedules.append({'quarter': date, **row})
        metrics[date] = m
    assert set(metrics) == {'2026-06-30', '2026-09-30'}
    a, b = metrics['2026-06-30'], metrics['2026-09-30']
    accepted = json.loads((WAL / 'research/2026-10-14_FFIEC-metrics.json').read_text())
    accepted_q2 = next(q for q in accepted['quarters'] if q['quarter'] == '2026-06-30')
    assert all(a[k] == Decimal(str(accepted_q2[k])) for k in DIRECT)
    checks.append('All 70 Q2 named fields reproduce accepted October 14 extraction')
    b['NCO_quarter_K'] = b['NCO_YTD_K'] - a['NCO_YTD_K']
    b['MI3_qoq_delta_pp'] = b['MI3_pct_item4'] - a['MI3_pct_item4']
    # Cross-check against the already-accepted issuer grade; this never re-grades it.
    assert round(b['NCO_quarter_K'] / 1000, 1) == Decimal('45.8')
    checks.append('Q3 bank NCO 45.797M reproduces accepted issuer 45.8M at printed precision')
    assert provenance['records'][1]['sha256'] == (
        '2e04cc7bf1a78e525a68059c358215c8ce9e3c24c3639d84ea74ccb8d69c60a4')
    checks.append('Q3 complete bytes also match WALTER original historical receipt')
    existing.write_text(json.dumps(provenance, indent=2) + '\n')
    limits = [
        'MI3 uses the existing WAL frozen item-4 denominator; not a cross-bank comparison basis.',
        'MI3 is CRE lending not secured by real estate; it does not identify the secured-office $99M loan.',
        'June/December nonaccrual additions/sales absent at Q3, not zero.',
        'NDFI commitments are face amounts, not funded draws, losses or a fixed-cohort utilization rate.',
        'No borrower attribution, NDFI-only loss attribution, or new score/weight interpretation.',
        'Modification stocks differ in population/window; not a loan-level migration bridge.',
        'GNMA residual excludes only rebooked GNMA, not every guarantee or insurance population.',
        'Bank mortgage income and bank capital are not parent income/EPS or parent capital.',
        'Recourse/SSFA populations can overlap NDFI and each other; never add blindly.',
        'Quarterly NCO is same-year Q3 YTD less Q2 YTD; no new issuer grade or fraud adjustment.',
    ]
    (OUT / 'metrics.json').write_text(json.dumps({'entity': provenance['source_entity'],
        'units': 'USD thousands except ratios/flags', 'quarters': list(metrics.values()),
        'validations': checks, 'limits': limits}, default=serial, indent=2) + '\n')
    for name, values in [('approved-fields.tsv', fields), ('supporting-schedules.tsv', schedules)]:
        with (OUT / name).open('w') as f:
            writer = csv.DictWriter(f, fieldnames=list(values[0]), delimiter='\t', lineterminator='\n')
            writer.writeheader()
            writer.writerows(values)
    (OUT / 'checks.json').write_text(json.dumps({'status': 'VERIFIED', 'checks': checks,
        'approved_named_fields': len(DIRECT), 'ledger_auxiliary_fields': 1,
        'quarters': 2, 'Q3_reported_named_fields': 68, 'Q3_not_expected_semiannual': 2,
        'supporting_schedule_rows': len(schedules)}, indent=2) + '\n')
    print(f'Verified two complete sources; {len(DIRECT)} approved fields + assets per quarter.')
    print(f'Q3 MI3 {b["MI3_pct_item4"]:.4f}%; delta {b["MI3_qoq_delta_pp"]:.4f}pp.')
    print(f'Q3 NDFI nonaccrual {b["ndfi_nonaccrual_K"]}K; Q3 NCO {b["NCO_quarter_K"]}K.')
    print(f'{len(checks)} validations; {len(schedules)} supporting schedule rows. No grading write.')


if __name__ == '__main__':
    main()
