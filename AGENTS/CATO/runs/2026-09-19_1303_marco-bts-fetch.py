#!/usr/bin/env python3
"""Independent BTS read-only retrieval; writes only this review's evidence JSON."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re

from bs4 import BeautifulSoup
import requests

URL = 'https://transtats.bts.gov/Data_Elements.aspx?Data=1'
OUT = Path(__file__).with_name('2026-09-19_1303_marco-bts-primary.json')

def retrieve(pair):
    airport, carrier = pair
    s = requests.Session()
    s.headers['User-Agent'] = 'Mozilla/5.0'
    r = s.get(URL, timeout=45)
    r.raise_for_status()
    form = BeautifulSoup(r.text, 'html.parser')
    payload = {name: form.find(id=name)['value'] for name in
               ('__VIEWSTATE', '__VIEWSTATEGENERATOR', '__EVENTVALIDATION')}
    payload.update({'__EVENTTARGET':'', '__EVENTARGUMENT':'',
                    'CarrierList':carrier, 'AirportList':airport, 'Submit':'Submit'})
    r = s.post(URL, data=payload, timeout=60)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, 'html.parser')
    selected = {}
    for name, expected in [('AirportList', airport), ('CarrierList', carrier)]:
        item = soup.find(id=name).find('option', selected=True)
        selected[name] = {'value': item.get('value'), 'label': item.get_text(' ', strip=True)}
        assert selected[name]['value'] == expected, selected
    rows, omitted = [], []
    for tr in soup.find_all('tr'):
        cells = [x.get_text(' ', strip=True).replace(',', '')
                 for x in tr.find_all(['td', 'th'], recursive=False)]
        if len(cells) < 5 or not re.fullmatch(r'(19|20)\d{2}', cells[0]):
            continue
        if not re.fullmatch(r'\d{1,2}', cells[1]):
            continue
        y, m = int(cells[0]), int(cells[1])
        assert 1 <= m <= 12
        if not all(re.fullmatch(r'\d+', x) for x in cells[2:5]):
            omitted.append({'period':f'{y}-{m:02d}', 'cells':cells[2:5]})
            continue  # Missing source cells are recorded, never converted to zero.
        domestic, international, total = map(int, cells[2:5])
        assert domestic + international == total
        rows.append({'period': f'{y}-{m:02d}', 'domestic':domestic,
                     'international':international, 'total':total})
    assert rows and len(rows) == len({r['period'] for r in rows})
    return {'airport':airport, 'carrier':carrier, 'selected':selected,
            'response_sha256':hashlib.sha256(r.content).hexdigest(),
            'retrieved_utc':datetime.now(timezone.utc).isoformat(),
            'omitted_missing_cells':omitted, 'rows':rows}

if __name__ == '__main__':
    pairs = [(ap, carrier) for ap in ['MCO', 'FLL', 'MIA'] for carrier in ['All','NK']]
    with ThreadPoolExecutor(max_workers=3) as pool:
        data = list(pool.map(retrieve, pairs))
    OUT.write_text(json.dumps({'url':URL, 'results':data}, indent=2)+'\n')
    for result in data:
        rows = result['rows']
        print(result['airport'], result['carrier'], len(rows),
              'range', min(r['period'] for r in rows), max(r['period'] for r in rows),
              'selected', result['selected'])
        print([r for r in rows if r['period'] in ('2025-05','2025-06','2026-04','2026-05','2026-06')])
    print('Evidence:', OUT)
