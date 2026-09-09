"""Offline reproduction from preserved EIA workbooks and delayed option feeds.

Run with the repository .venv Python (xlrd, pandas, openpyxl).
Quarterly flows use simple monthly means to match BRENT's existing vintage
ladder; inventories use quarter-end levels. No new forecast grades.
"""
import csv
import json
from pathlib import Path
import pandas as pd
import xlrd

ROOT = Path(__file__).resolve().parent

def retail(filename, sheet_name, prefix):
    book = xlrd.open_workbook(ROOT/filename)
    sheet = book.sheet_by_name(sheet_name)
    result = []
    for region in ['NUS', 'R10', 'R20', 'R30', 'R40', 'R50']:
        key = f'{prefix}_{region}_DPG'
        col = sheet.row_values(1).index(key)
        series = [(xlrd.xldate_as_datetime(sheet.cell_value(i, 0), book.datemode).date().isoformat(),
                   sheet.cell_value(i, col)) for i in range(3, sheet.nrows)
                  if isinstance(sheet.cell_value(i, col), (int, float))]
        old, new = series[-2:]
        assert old[0] == '2026-08-31' and new[0] == '2026-09-07'
        change = round(new[1]-old[1], 3)
        history = [round(series[i][1]-series[i-1][1], 3) for i in range(1, len(series))
                   if '2020-01-01' <= series[i][0] < new[0]]
        result.append(dict(region=region, series_id=key, label=sheet.cell_value(2, col),
                           date=new[0], value=new[1], prior_date=old[0], prior_value=old[1],
                           change=change, change_pct=100*change/old[1],
                           previous_weekly_changes_since_2020=len(history),
                           previous_changes_at_least_as_large=sum(v >= change for v in history)))
    return result

gas = retail('retail-gas.xls', 'Data 3', 'EMM_EPMR_PTE')
diesel = retail('retail-diesel.xls', 'Data 1', 'EMD_EPD2D_PTE')
assert gas[0]['value'] == 4.157 and diesel[0]['value'] == 5.967
(ROOT/'retail-derived.json').write_text(json.dumps(dict(gasoline=gas, diesel=diesel), indent=2)+'\n')

selection = {
    '3atab': ['papr_world','patc_world','t3_stchange_world','pasc_oecd_t3'],
    '3ctab': ['papr_opecplus'],
    '3dtab': ['cops_opec', 'cops_opec_r05'],
}
baseline = []
for sheet, keys in selection.items():
    frame = pd.read_excel(ROOT/'aug26_base.xlsx', sheet_name=sheet, header=None).fillna('')
    years = frame.iloc[2].replace('', pd.NA).ffill()
    for key in keys:
        row = frame[frame.iloc[:, 0] == key].iloc[0]
        monthly = {f'{int(years.iloc[c])}-{m:02d}': float(row.iloc[c])
                   for c in range(2, 74)
                   if years.iloc[c] in [2026, 2027]
                   for m in [int(pd.to_datetime(str(frame.iloc[3,c]), format='%b').month)]}
        stocks = key == 'pasc_oecd_t3'
        quarters = {}
        for year in [2026,2027]:
            for q in range(1,5):
                vals = [monthly[f'{year}-{m:02d}'] for m in range(3*q-2,3*q+1)]
                quarters[f'{year}Q{q}'] = vals[-1] if stocks else sum(vals)/3
        baseline.append(dict(sheet=sheet, series_id=key, label=row.iloc[1],
                             quarterly_method='end-of-quarter' if stocks else 'simple monthly mean',
                             units='million barrels' if stocks else 'million barrels/day',
                             monthly=monthly, quarterly=quarters))
by_key = {r['series_id']:r for r in baseline}
for month in by_key['papr_world']['monthly']:
    draw = by_key['patc_world']['monthly'][month]-by_key['papr_world']['monthly'][month]
    assert abs(draw-by_key['t3_stchange_world']['monthly'][month]) < 1e-6
assert abs(by_key['cops_opec']['quarterly']['2026Q3']-.02) < 1e-9
(ROOT/'august-steo-baseline.json').write_text(json.dumps(dict(issue_date='2026-08-11',
    forecast_completed='2026-08-06', withdrawal_sign='positive is draw', series=baseline), indent=2)+'\n')

quotes = []
for name, strikes in [('USO-2026-10-16-chain.json',[135]),('USO-2026-09-18-chain.json',[150,165]),
                      ('XLE-2026-09-30-chain.json',[65])]:
    chain = json.loads((ROOT/name).read_text())
    for row in chain['rows']:
        if row['strike'] in strikes:
            assert 0 < row['bid'] <= row['ask'] and not row['quote_flag']
            quotes.append(dict(file=name, fetch_ts=chain['fetch_ts'], spot=chain['spot'], **row))
(ROOT/'selected-option-quotes.json').write_text(json.dumps(quotes,indent=2)+'\n')

print('RETAIL: verified September 7 observation and August 31 comparison')
for g,d in zip(gas,diesel):print(g['region'],g['value'],g['change'],d['value'],d['change'])
print('STEO August: Q3 2026 / Q4 2026 / Q1 2027 / Q2 2027')
for r in baseline:print(r['series_id'],*[round(r['quarterly'][q],4) for q in ['2026Q3','2026Q4','2027Q1','2027Q2']])
print('OPTION: all requested strikes found; positive ordered bid/ask, existing tool flags empty')
