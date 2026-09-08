#!/usr/bin/env python3
"""Verify retained September 8 owner extraction; no network or liability calculation."""
import json
import re
from collections import Counter
from pathlib import Path

base = Path(__file__).parent
sources = json.loads((base / '2026-09-08_canada_source-lines.json').read_text())
finance = []
pending = ''
for n, text in sorted((int(k), v) for k, v in sources['finance'].items()):
    if n < 45:
        continue
    if re.match(r'\d{4}\.\d{2}\.\d{2}\s*\|', text):
        assert not pending, ('unfinished Finance row', pending)
        pending = text
    elif pending:
        pending += ' ' + text
    match = re.search(r'\|\s*(15|25|50)\s*$', pending)
    if match:
        finance.append((pending[:10], int(match[1])))
        pending = ''
legal = []
for name, lower, upper in [('0785', 108, 786), ('0786', 65, 673)]:
    rate = None
    for n, text in sorted((int(k), v) for k, v in sources[name].items()):
        if not lower <= n < upper:
            continue
        match = re.search(r'Goods Subject to (15|25|50)% Surtax', text)
        if match:
            rate = int(match[1])
        if re.fullmatch(r'\s*\d{4}\.\d{2}\.\d{2}\s*', text):
            assert rate is not None, (name, n)
            legal.append((text.strip(), rate))
for rows in (finance, legal):
    assert len(rows) == len(dict(rows)) == 629, 'incomplete or duplicate commodity extraction'
assert dict(finance) == dict(legal), 'commodity scope/rate mismatch'
assert Counter(dict(finance).values()) == Counter({15: 21, 25: 195, 50: 413})
print(json.dumps({'items': 629, 'rates': dict(Counter(dict(finance).values())),
                  'missing_each_direction': 0, 'rate_mismatches': 0,
                  'scope': 'owner re-extraction, commodity schedules only; not remission, import weights or registration'}))
