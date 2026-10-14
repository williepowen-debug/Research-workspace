"""Reproduce a dated WAL-only FFIEC research extraction. No grades or live rules."""
import csv
import hashlib
import json
from pathlib import Path

WAL = Path(__file__).resolve().parents[1]
RAW = WAL / 'sources/ffiec_2026-10-14'
OUT = WAL / 'research'
SCHEDULES = {'RCCI', 'RCN', 'RCL', 'RCP', 'RCM', 'RIBI', 'RIBII', 'RIC',
             'RCRI', 'RCRII', 'RCS', 'RCV', 'RI', 'RC', 'RCK'}
DIRECT = {
    'ndfi_funded_K': 'RCONJ454', 'ndfi_mortgage_K': 'RCONPV05',
    'ndfi_business_K': 'RCONPV06', 'ndfi_PE_K': 'RCONPV07',
    'ndfi_consumer_K': 'RCONPV08', 'ndfi_other_K': 'RCONPV09',
    'ndfi_unused_K': 'RCONPV11', 'ndfi_unused_mortgage_K': 'RCONPV12',
    'ndfi_unused_business_K': 'RCONPV13', 'ndfi_unused_PE_K': 'RCONPV14',
    'ndfi_unused_consumer_K': 'RCONPV15', 'ndfi_unused_other_K': 'RCONPV16',
    'ndfi_PD30_K': 'RCONPV23', 'ndfi_PD90_K': 'RCONPV24',
    'ndfi_nonaccrual_K': 'RCONPV25', 'MI3_K': 'RCON2746',
    'CI_K': 'RCON1766', 'loans_total_K': 'RCON2122', 'HFI_K': 'RCONB528',
    'modified_performing_K': 'RCONHK25', 'modified_PD30_K': 'RCONHK26',
    'modified_PD90_K': 'RCONHK27', 'modified_nonaccrual_K': 'RCONHK28',
    'CRE_NOO_modified_performing_K': 'RCONK162',
    'CRE_NOO_modified_nonaccrual_K': 'RCONK119',
    'nonaccrual_total_K': 'RCON1403', 'PD30_total_K': 'RCON1406',
    'PD90_total_K': 'RCON1407', 'GNMA_PD30_K': 'RCONK042',
    'GNMA_PD90_K': 'RCONK043', 'GNMA_nonaccrual_K': 'RCONK044',
    'HFS_nonaccrual_K': 'RCONC226', 'HFS_PD30_K': 'RCONC240',
    'HFS_PD90_K': 'RCONC241', 'government_nonaccrual_K': 'RCONK038',
    'nonaccrual_additions_6mo_K': 'RCONC410', 'nonaccrual_sales_6mo_balance_K': 'RCONC411',
    'C_and_LD_nonaccrual_K': 'RCONF173', 'CRE_NOO_nonaccrual_K': 'RCONF183',
    'ACL_HFI_K': 'RIAD3123', 'ACL_offbalance_K': 'RCONB557',
    'gross_CO_YTD_K': 'RIAD4635', 'recoveries_YTD_K': 'RIAD4605',
    'provision_HFI_YTD_K': 'RIAD4230', 'transfers_writedown_YTD_K': 'RIAD5523',
    'MI3_CO_YTD_K': 'RIAD5409', 'MI3_recovery_YTD_K': 'RIAD5410',
    'mortgage_sales_quarter_K': 'RCONFT04', 'mortgage_HFS_trading_K': 'RCONFT05',
    'mortgage_retail_originations_quarter_K': 'RCONHT81',
    'mortgage_wholesale_originations_purchases_quarter_K': 'RCONHT82',
    'mortgage_income_quarter_K': 'RIADHT85', 'mortgage_repurchases_quarter_principal_K': 'RCONHT86',
    'mortgage_warranty_reserves_K': 'RCONM288', 'MSA_carrying_K': 'RCON3164',
    'MSA_FV_K': 'RCONA590', 'servicing_no_recourse_UPB_K': 'RCONB805',
    'servicing_foreclosure_UPB_K': 'RCONF699', 'asset_sales_recourse_UPB_K': 'RCONB790',
    'asset_sales_recourse_max_exposure_K': 'RCONB797',
    'bank_CET1_K': 'RCOAP859', 'bank_RWA_K': 'RCOAA223',
    'bank_CET1_reported_pct': 'RCOAP793', 'MSA_threshold_deduction_K': 'RCOALB59',
    'bank_AOCI_K': 'RCOAB530', 'AOCI_optout': 'RCOAP838',
    'SSFA_other_onbalance_exposure_K': 'RCONS490',
    'SSFA_other_onbalance_RWA_K': 'RCONS493',
    'SSFA_offbalance_exposure_K': 'RCONS495', 'SSFA_offbalance_RWA_K': 'RCONS498',
}


def number(row):
    if row is None or row['Value'] == '':
        return None
    try:
        return float(row['Value'].removesuffix('%'))
    except ValueError:
        return None


def total(values):
    return None if any(v is None for v in values) else sum(values)


def ratio(a, b):
    return None if a is None or b is None or b == 0 else 100 * a / b


def main():
    metrics, fields, manifest, validations = [], [], [], []
    for path in sorted(RAW.glob('WAL_*.sdf')):
        quarter = path.stem.removeprefix('WAL_')
        rows = list(csv.DictReader(path.open(), delimiter=';'))
        assert all(r['Bank RSSD Identifier'] == '3138146' for r in rows)
        assert all(r['Call Date'] == quarter.replace('-', '') for r in rows)
        data = {r['MDRM #']: r for r in rows}
        assert len(data) == len(rows)
        manifest.append({'quarter': quarter, 'path': str(path.relative_to(WAL)),
                         'sha256': hashlib.sha256(path.read_bytes()).hexdigest(), 'rows': len(rows)})
        for row in rows:
            if row['Call Schedule'] in SCHEDULES:
                fields.append({'Quarter_End': quarter, **row})
        m = {'quarter': quarter, **{k: number(data.get(v)) for k, v in DIRECT.items()}}
        for name, parts in [('funded', ['mortgage', 'business', 'PE', 'consumer', 'other']),
                            ('unused', ['unused_mortgage', 'unused_business', 'unused_PE', 'unused_consumer', 'unused_other'])]:
            subtotal = total([m['ndfi_' + part + '_K'] for part in parts])
            if subtotal is not None:
                assert abs(subtotal - m['ndfi_' + name + '_K']) <= 1
                validations.append(quarter + ' NDFI ' + name + ' subtypes tie')
        m['ndfi_nonaccrual_pct'] = ratio(m['ndfi_nonaccrual_K'], m['ndfi_funded_K'])
        m['ndfi_funded_plus_unused_face_K'] = total([m['ndfi_funded_K'], m['ndfi_unused_K']])
        m['ndfi_aggregate_funding_ratio_pct'] = ratio(m['ndfi_funded_K'], m['ndfi_funded_plus_unused_face_K'])
        m['modified_nonperforming_or_PD_K'] = total([m['modified_PD30_K'], m['modified_PD90_K'], m['modified_nonaccrual_K']])
        m['modified_combined_reported_K'] = total([m['modified_performing_K'], m['modified_nonperforming_or_PD_K']])
        m['PD90_excluding_GNMA_K'] = (m['PD90_total_K'] - m['GNMA_PD90_K']
                                      if m['GNMA_PD90_K'] is not None else None)
        m['NCO_YTD_K'] = m['gross_CO_YTD_K'] - m['recoveries_YTD_K']
        m['NCO_quarter_K'] = (m['NCO_YTD_K'] if quarter[5:7] == '03' else
                              m['NCO_YTD_K'] - metrics[-1]['NCO_YTD_K']
                              if metrics and quarter[:4] == metrics[-1]['quarter'][:4] else None)
        m['bank_CET1_computed_pct'] = ratio(m['bank_CET1_K'], m['bank_RWA_K'])
        assert abs(m['bank_CET1_computed_pct'] - m['bank_CET1_reported_pct']) < .0001
        validations.append(quarter + ' CET1 numerator/RWA ties reported percentage')
        metrics.append(m)
    assert len(metrics) == 8 and metrics[-1]['quarter'] == '2026-06-30'
    # Existing accepted Q2 source is a stronger check than a self-consistency test.
    assert round(metrics[-1]['NCO_quarter_K'] / 1000, 1) == 55.0
    assert metrics[-1]['ndfi_funded_K'] == 15812034
    assert metrics[-1]['ACL_HFI_K'] == 487385
    assert abs(metrics[-1]['MSA_carrying_K'] - 1499649) < 1
    OUT.joinpath('2026-10-14_FFIEC-metrics.json').write_text(json.dumps({
        'entity': 'Western Alliance Bank RSSD3138146',
        'units': 'USD thousands except percentages and election flags; not parent EPS',
        'quarters': metrics, 'sources': manifest, 'validations': validations,
        'limits': ['Quarterly flows computed from YTD only within the same calendar year; first Q3-2024 NCO unavailable',
                   'NDFI subtype/nonaccrual fields absent September2024, not zero',
                   'Nonaccrual additions/sales are June/December semiannual fields',
                   'Modification stocks are not a loan-level migration cohort; definition vintages require caution',
                   'RC-P income is quarterly and not a substitute for parent mortgage revenue or EPS',
                   'Repurchases are principal/commitments, not losses; recourse columns can overlap other exposures',
                   'Q3-2026 retrieval HTTP500 does not prove absence of a filing']
    }, indent=2) + '\n')
    for name, records in [('2026-10-14_FFIEC-metrics.tsv', metrics),
                          ('2026-10-14_FFIEC-selected-fields.tsv', fields)]:
        with OUT.joinpath(name).open('w') as stream:
            writer = csv.DictWriter(stream, fieldnames=list(records[0]), delimiter='\t')
            writer.writeheader()
            writer.writerows(records)
    print(f'{len(metrics)} quarters; {len(DIRECT)} named fields; {len(fields)} schedule rows; {len(validations)} ties passed.')
    print('Q2 NCO reproduces accepted $55.0M at issuer printed precision; missing values preserved; no thesis grade changed.')


if __name__ == '__main__':
    main()
