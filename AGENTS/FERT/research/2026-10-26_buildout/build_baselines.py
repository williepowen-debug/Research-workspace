"""Offline extraction of the saved 2026-10-26 research snapshots; no scheduler.

Run with repository .venv/bin/python. Source table locators are zero-based
pandas table/row numbers, bound to the hashed HTML snapshots in this directory.
"""
from pathlib import Path
import csv
import io
import json
import re
import zipfile
import pandas as pd

HERE = Path(__file__).resolve().parent
DESK = HERE.parents[1]
SRC = HERE / 'sources'
DATE = '2026-10-26'


def write(relative, rows):
    path = DESK / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('w') as f:
        f.write(f'# Last real data refresh: {DATE}\n')
        f.write('# Maintenance: DATA_ROUTES.md; source observation dates are row-specific.\n')
        writer = csv.DictWriter(f, fieldnames=list(rows[0]), delimiter='\t', lineterminator='\n')
        writer.writeheader()
        writer.writerows(rows)
    print(relative, len(rows), 'rows')


def number(row, column):
    vals = {str(x).strip() for x in row.iloc[column:column+3] if pd.notna(x)} - {'$', '%'}
    assert len(vals) == 1, (column, vals)
    token = vals.pop()
    if token == '—':
        return 0.0
    assert re.fullmatch(r'\(?-?\d+(?:\.\d+)?\)?', token), token
    return float(token.strip('()')) * (-1 if token.startswith('(') else 1)


cf = []
for quarter, release in [('q1', '2026-05-06'), ('q2', '2026-08-05')]:
    filename = f'cf_{quarter}_2026.html'
    tables = pd.read_html(io.StringIO((SRC / filename).read_text()))
    periods = [('2026-Q1', 3), ('2025-Q1', 9)] if quarter == 'q1' else [
        ('2026-Q2', 3), ('2025-Q2', 9), ('2026-H1', 15), ('2025-H1', 21)]
    # Exact row labels, rather than shifting physical row positions.
    mappings = {
        2: ('Consolidated', {
            'Net sales': ('net_sales', 'USD million'),
            'Cost of sales': ('cost_of_sales', 'USD million'),
            'Gross margin': ('gross_margin', 'USD million'),
            'Gross margin percentage': ('gross_margin_percent', 'percent'),
            'Net earnings attributable to common stockholders': ('net_earnings_common', 'USD million'),
            'Net earnings per diluted share': ('diluted_eps', 'USD/share'),
            'EBITDA(1)': ('ebitda', 'USD million'),
            'Adjusted EBITDA(1)': ('issuer_adjusted_ebitda', 'USD million'),
            'Sales volume by product tons (000s)': ('sales_volume', 'thousand product short tons'),
            'Natural gas costs in cost of sales(2)': ('gas_before_realized_hedges', 'USD/MMBtu'),
            'Realized derivatives gain in cost of sales(3)': ('gas_realized_derivative_effect', 'USD/MMBtu'),
            'Cost of natural gas used for production in cost of sales': ('gas_in_cost_of_sales_including_realized_hedges', 'USD/MMBtu'),
            'Average daily market price of natural gas at the Henry Hub': ('period_average_henry_hub', 'USD/MMBtu'),
            'Depreciation and amortization': ('depreciation_amortization', 'USD million'),
            'Capital expenditures(4)': ('capital_expenditures', 'USD million'),
            'Ammonia(5)': ('ammonia_production', 'thousand product short tons'),
            'Granular urea': ('granular_urea_production', 'thousand product short tons'),
            'UAN (32%)(6)': ('uan_32pct_production', 'thousand product short tons'),
            'AN': ('an_production', 'thousand product short tons'),
        }),
        11: ('Consolidated', {
            'Net cash provided by operating activities': ('operating_cash_flow', 'USD million'),
            'Contributions from noncontrolling interests': ('noncontrolling_contributions', 'USD million'),
            'Distributions to noncontrolling interests': ('noncontrolling_distributions_signed', 'USD million'),
            'Purchases of treasury stock': ('treasury_stock_cash_flow_signed', 'USD million'),
        }),
    }
    segment_map = {
        'Net sales': ('net_sales', 'USD million'),
        'Cost of sales': ('cost_of_sales', 'USD million'),
        'Gross margin': ('gross_margin', 'USD million'),
        'Gross margin percentage': ('gross_margin_percent', 'percent'),
        'Sales volume by product tons (000s)': ('sales_volume', 'thousand product short tons'),
        'Average selling price per product ton': ('realized_selling_price', 'USD/product short ton'),
    }
    for ti, segment in [(3, 'Ammonia'), (4, 'Granular urea'), (5, 'UAN'), (6, 'AN'), (7, 'Other')]:
        mappings[ti] = (segment, segment_map)
    for ti, (segment, mapping) in mappings.items():
        seen = set()
        for ri, row in tables[ti].iterrows():
            label = str(row.iloc[0])
            if label not in mapping or label in seen:
                continue
            seen.add(label)
            metric, unit = mapping[label]
            for period, column in periods:
                cf.append(dict(period=period, segment=segment, metric=metric,
                               value=number(row, column), unit=unit, state='MEASURED',
                               published=release, source=filename,
                               locator=f'table[{ti}]/row[{ri}] {label}',
                               note='CF June 30 10-Q, Item 2 opening: tons are short tons. Product, not nutrient, weight; do not sum gross ammonia and upgraded-product output.' if 'ton' in unit else ''))
        assert seen == set(mapping), (filename, ti, set(mapping)-seen)
    # Balance sheets compare quarter-end to preceding December 31, never YoY.
    for ri, row in tables[10].iterrows():
        label = str(row.iloc[0])
        if label not in ('Cash and cash equivalents', 'Long-term debt'):
            continue
        cf.append(dict(period='2026-03-31' if quarter == 'q1' else '2026-06-30',
                       segment='Consolidated', metric='cash' if label.startswith('Cash') else 'long_term_debt',
                       value=number(row, 3), unit='USD million', state='MEASURED',
                       published=release, source=filename, locator=f'table[10]/row[{ri}] {label}',
                       note='Point-in-time balance, not a period flow; cash includes consolidated JV cash.'))

def cfval(period, segment, metric):
    selected = [r['value'] for r in cf if (r['period'], r['segment'], r['metric']) == (period, segment, metric)]
    assert len(selected) == 1, (period, segment, metric)
    return selected[0]

assert len({(r['period'], r['segment'], r['metric']) for r in cf}) == len(cf)
for period in ['2025-Q1','2026-Q1','2025-Q2','2026-Q2','2025-H1','2026-H1']:
    for metric in ['net_sales','gross_margin','sales_volume']:
        assert sum(cfval(period,s,metric) for s in ['Ammonia','Granular urea','UAN','AN','Other']) == cfval(period,'Consolidated',metric)
for year in ['2025','2026']:
    for segment in ['Consolidated','Ammonia','Granular urea','UAN','AN','Other']:
        for metric in ['net_sales','gross_margin','sales_volume']:
            assert cfval(year+'-Q1',segment,metric)+cfval(year+'-Q2',segment,metric)==cfval(year+'-H1',segment,metric)
    for metric in ['issuer_adjusted_ebitda','operating_cash_flow','capital_expenditures','ammonia_production','granular_urea_production','uan_32pct_production','an_production']:
        assert cfval(year+'-Q1','Consolidated',metric)+cfval(year+'-Q2','Consolidated',metric)==cfval(year+'-H1','Consolidated',metric)
write('companies/CF/OPERATING_HISTORY.tsv', cf)

trade = json.loads((SRC/'ams_imports_2025_2026.json').read_text())
assert len(trade) < 10000  # not a truncated Socrata page
rows = [dict(month=r['date'][:7], hs=r['hs'], product=r['tfi_name'], nutrient=r['nutrient'],
             value=r['nutrient_short_tons'], unit='nutrient-equivalent short tons (AMS/TFI convention)',
             direction='Import', trade_type='Consumption', geography='United States; all countries and customs districts',
             state='MEASURED', source='ams_imports_2025_2026.json',
             note='Converted by AMS/TFI; not product weight. Preserve separate N/P components; phosphorus elemental-versus-oxide convention not independently verified.') for r in trade]
assert len({(r['month'],r['hs'],r['nutrient']) for r in rows}) == len(rows)
write('data/US_FERTILIZER_IMPORTS.tsv', rows)

archive = zipfile.ZipFile(SRC/'ers_farm_20260903.zip')
df = pd.read_csv(archive.open(archive.namelist()[0]), encoding='cp1252')
keys = ['EXAUSIPFL--P','EXAUSIPPT--P','CRAUSCR--VAP','CRAUSSY--VAP','CRAUSWT--VAP','FIAUSNTFI--P','FBAUSCICSCRP','FBAUSCICSSPP','FBAUSCICSWTP']
selected = df[(df.State=='US') & df.Year.between(2023,2026) & df.artificialKey.isin(keys)]
assert len(selected) == len(keys)*4
rows=[]
for r in selected.itertuples():
    rows.append(dict(year=r.Year, key=r.artificialKey, measure=r.VariableDescriptionTotal,
                     value=r.Amount, unit=r.unit_desc.replace('\xa0',' ').strip(),
                     geography='United States', vintage='2026-09-03',
                     state='MEASURED', estimate_type='forecast' if r.Year==2026 else 'historical estimate',
                     source='ers_farm_20260903.zip/FarmIncome_WealthStatisticsData_September2026.csv',
                     note='MEASURED denotes the published estimate, not a realized outcome. Nominal annual estimates; crop-farm net cash income includes noncrop receipts; fertilizer expense includes lime/soil conditioner. Not per-acre margins.'))
write('data/FARM_ECONOMICS.tsv', rows)

rows=[]
for series, label in [('WPU01','Farm products'),('WPU02','Processed foods and feeds'),('WPU0651','Mixed fertilizers')]:
    j=json.loads((SRC/f'bls_{series}.json').read_text())
    assert j['status']=='REQUEST_SUCCEEDED' and len(j['Results']['series'])==1
    assert j['Results']['series'][0]['seriesID']==series
    for r in j['Results']['series'][0]['data']:
        if not re.fullmatch('M(0[1-9]|1[0-2])',r['period']):continue
        rows.append(dict(month=r['year']+'-'+r['period'][1:], series=series, measure=label,
                         value=r['value'], unit='index 1982=100; not seasonally adjusted',
                         state='MEASURED', preliminary='yes' if any(f.get('code')=='P' for f in r['footnotes']) else 'no',
                         source=f'bls_{series}.json',
                         note='Producer-price indexes; compare changes within series, not raw index levels across series; no fertilizer causation identified.'))
assert len({(r['month'],r['series']) for r in rows})==len(rows)
write('data/INTERMEDIATE_PRICES.tsv', rows)

write('data/CHINA_UREA_EXPORTS.tsv', [dict(
    month='2026-09', geography='China; all destinations', product='Urea',
    value=2450400, unit='metric product tons', state='MEASURED',
    source_authority='MIRROR-WALLED', published='2026-10-20; 2026-10-23',
    source='china_mysteel_20261020.html; china_sci_sina_20261023.html',
    locator='Longzhong opening export statistic; SCI opening September export statistic',
    note='Reported statistic, not primary-verified. 245.04 ten-thousand tons multiplied by 10000. Official Customs portal: requests TLS failure and browser timeout. Two publishers can share one Customs input. Not allocation, ship tracking, product destination arrival or verified YTD.')])

write('workbook/SUPPLY_EVENTS.tsv', [dict(
    event_id='CF-YAZOO', evidence_date=published, facility='Yazoo City, Mississippi',
    product='Ammonia and upgraded nitrogen products', event_kind='restart guidance',
    restart_window=window, affected_capacity='', capacity_unit='product short tons/year',
    capacity_state='UNKNOWN', source_authority='PRIMARY', source=source,
    locator='Operations overview; Yazoo City restart paragraph',
    note='One facility, two guidance vintages. No aggregate capacity loss inferred; available utilization excludes site. Latest dated guidance controls the expectation, not proof of actual restart.')
    for published,window,source in [
        ('2026-05-06','Late Q4 2026 at earliest','cf_q1_2026.html'),
        ('2026-08-05','First half 2027','cf_q2_2026.html')]])

relative=[]
for product,first,last,kb in [('Urea',678,674,'KB-FERT-001'),('DAP',917,937,'KB-FERT-008'),('MAP',959,981,'KB-FERT-008')]:
    for week,value,pub,source in [('2026-08-03/2026-08-07',first,'2026-08-12',kb),('2026-10-12/2026-10-16',last,'2026-10-21','KB-FERT-079')]:
        relative.append(dict(observation_week=week,published=pub,product=product,
                             benchmark='DTN US national average retail',value=value,
                             unit='USD/product ton as published by DTN',state='MEASURED',
                             indexed_to_first_observation=round(value/first*100,4),
                             percent_from_first_observation=round((value/first-1)*100,4),
                             source_authority='PRIMARY',source=source,
                             note='Existing source-located KB receipt; not a new live quote. Compare aligned within-series percent changes, not cross-product dollar spreads. No potash comparison.'))
write('data/RELATIVE_NUTRIENTS.tsv', relative)
print('PASS: unique keys, complete source mappings, segment reconciliation, quarterly/H1 additive checks.')
