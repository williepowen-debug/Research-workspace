"""Reproduce CARL's September 16 calculations from retained source vintages."""
import json
import re
from pathlib import Path

p = Path(__file__).resolve().parent
raw = json.loads((p / 'sources.json').read_text())
data = {s: {x['date']: float(x['value']) for x in v['observations']
            if 'date' in x and x['value'] != '.'}
        for s, v in raw['series'].items()}
out = {}
for date in ['2026-07-01', '2026-08-01']:
    prior = date[:4] + '-' + str(int(date[5:7])-1).zfill(2) + '-01'
    year = '2025' + date[4:]
    row = {}
    for name, sales, prices in [('grocery_proxy', 'RSDBS', 'CUSR0000SAF11'),
                                ('restaurants', 'RSFSDP', 'CUSR0000SEFV'),
                                ('apparel', 'RSCCAS', 'CPIAPPSL')]:
        row[name] = {basis: 100*((data[sales][date]/data[sales][base]) /
                                (data[prices][date]/data[prices][base])-1)
                     for basis, base in [('mom', prior), ('yoy', year)]}
    row['gm_share'] = {d: 100*data['RSGMS'][d]/data['RSXFS'][d]
                       for d in [date, prior, year]}
    out[date] = row
for basis in ['nominal', 'real']:
    html = (p / f'wallethub_{basis}.html').read_text()
    values = dict(json.loads(re.search(r'arrayToDataTable\((\[.*?\])\);', html).group(1))[1:])
    out['wallethub_'+basis] = {k: values[k] for k in ['2022 Q4', '2025 Q4', '2026 Q1']}
    out['wallethub_'+basis]['q4_change_pct'] = 100*(values['2025 Q4']/values['2022 Q4']-1)
# Census CB26-153 Table 1, seasonally adjusted $millions; independently
# checked against retained retail_august.pdf, matching PROME's transcription.
sales = {'total': [773947, 764462, 768587], 'auto': [142379, 141565, 144140],
         'gas': [62303, 60455, 60586], 'building': [42227, 42318, 42380],
         'restaurants': [105070, 103824, 103340], 'nonstore': [141339, 137772, 140207]}
sales['control'] = [sales['total'][i]-sum(sales[k][i] for k in
                      ['auto', 'gas', 'building', 'restaurants']) for i in range(3)]
sales['control_ex_nonstore'] = [sales['control'][i]-sales['nonstore'][i] for i in range(3)]
out['retail'] = {k: {'aug_jul_jun_millions': v, 'aug_mom_pct': 100*(v[0]/v[1]-1),
                    'jul_mom_pct': 100*(v[1]/v[2]-1), 'aug_vs_june_pct': 100*(v[0]/v[2]-1)}
                 for k, v in sales.items()}
(p / 'derived.json').write_text(json.dumps(out, indent=2)+'\n')
print(json.dumps(out, indent=2))
