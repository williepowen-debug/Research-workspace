#!/usr/bin/env python3
"""Read the existing ORCH_LOG closeout evidence; never infer native liveness.

Evidence is an attributed record, not authentication of the referenced receipt.
No messaging, file mutation, or closeout-blocking authority is provided here.
"""
import argparse
import csv
import datetime as dt
import hashlib
import json
import re
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[2]
HEADER = ['date', 'desk', 'tier', 'touch', 'trigger', 'drained', 'delivered',
          'zero_capital', 'notes', 'brief_defects', 'inbox_before', 'inbox_after',
          'brief_defect_count']
LABELS = {'ASKED_RECEIPT': 'ASKED → receipt', 'ASKED_WORKING': 'ASKED → still working',
          'ALREADY_CLOSED': 'ALREADY CLOSED OUT', 'DARK_BEFORE_ASK': 'WENT DARK BEFORE THE ASK'}
ET = ZoneInfo('America/New_York')
MARKER = 'closeout_v1='


def touch_key(row):
    return hashlib.sha256(json.dumps(row[:5], ensure_ascii=True,
                                    separators=(',', ':')).encode()).hexdigest()


def read_touches(path, day):
    rows = []
    header = False
    seen = set()
    for line_no, line in enumerate(Path(path).read_text().splitlines(), 1):
        if not line.strip() or line.startswith('#'):
            continue
        fields = next(csv.reader([line], delimiter='\t', quoting=csv.QUOTE_NONE))
        if not header:
            if fields != HEADER:
                raise ValueError(f'line {line_no}: expected ORCH_LOG 13-column header')
            header = True
            continue
        if len(fields) != len(HEADER):
            raise ValueError(f'line {line_no}: expected 13 columns, found {len(fields)}')
        try:
            row_day = dt.date.fromisoformat(fields[0])
        except ValueError as exc:
            raise ValueError(f'line {line_no}: invalid touch date') from exc
        if fields[3] != 'CLOSE' and not re.fullmatch(r'[1-9][0-9]*(?:[A-Za-z][A-Za-z0-9_-]*|-[A-Za-z0-9_-]+)?', fields[3]):
            raise ValueError(f'line {line_no}: invalid TOUCH/CLOSE token {fields[3]!r}')
        if row_day != day or fields[3] == 'CLOSE':
            continue
        key = touch_key(fields)
        if key in seen:
            raise ValueError(f'line {line_no}: duplicate touch key {key}')
        seen.add(key)
        rows.append((key, fields))
    if not header:
        raise ValueError('ORCH_LOG header missing; population UNKNOWN')
    return rows


def timestamp(value):
    if not isinstance(value, str):
        raise ValueError('timestamp absent')
    stamp = dt.datetime.fromisoformat(value.replace('Z', '+00:00'))
    if stamp.tzinfo is None:
        raise ValueError('timestamp has no timezone')
    return stamp


def disposition(row, now):
    notes = row[8]
    if notes.count(MARKER) != 1:
        return 'UNKNOWN', 'missing or duplicate structured closeout evidence'
    try:
        data = json.loads(notes.split(MARKER, 1)[1])
        if not isinstance(data, dict):
            raise ValueError('evidence must be an object')
        owner = data.get('owner')
        if owner not in ('PROME', 'WILL'):
            raise ValueError('touch ownership UNKNOWN')
        if not isinstance(data.get('session_id'), str) or not data['session_id'].strip():
            raise ValueError('session identity missing')
        touched, observed = timestamp(data.get('touch_at')), timestamp(data.get('observed_at'))
        if touched.astimezone(ET).date().isoformat() != row[0] or not touched <= observed <= now:
            raise ValueError('observation predates touch, is future, or touch date mismatches')
        if owner == 'WILL':
            return 'OUT_OF_SCOPE', 'explicit WILL-owned session; not a PROME spawn obligation'
        state = data.get('state')
        if state not in LABELS:
            raise ValueError('closeout disposition UNKNOWN')
        required = {'ASKED_RECEIPT': ('ask', 'receipt'), 'ASKED_WORKING': ('ask',),
                    'ALREADY_CLOSED': ('receipt',), 'DARK_BEFORE_ASK': ('presence',)}[state]
        if any(not isinstance(data.get(k), str) or not data[k].strip() for k in required):
            raise ValueError(f'{state}: missing required evidence {required}')
        if state == 'DARK_BEFORE_ASK' and data.get('ask'):
            raise ValueError('DARK_BEFORE_ASK contradicts recorded ask')
        detail = ' | '.join(f'{k}: {data[k]}' for k in required)
        if state == 'ASKED_WORKING':
            detail += ' | pending; no completion receipt established'
        return state, detail
    except (ValueError, TypeError) as exc:
        return 'UNKNOWN', str(exc)


def evaluate(path, day, expected=(), inventory_complete=False, now=None):
    now = now or dt.datetime.now(dt.timezone.utc)
    rows = read_touches(path, day)
    actual = {key for key, _ in rows}
    expected = set(expected)
    issues = []
    if not inventory_complete:
        issues.append('spawn inventory coverage UNKNOWN; ledger absence cannot prove no spawns')
    for key in sorted(expected - actual):
        issues.append(f'known spawn absent from ORCH_LOG: {key}; UNKNOWN')
    if inventory_complete:
        for key in sorted(actual - expected):
            issues.append(f'ledger touch absent from declared complete inventory: {key}; UNKNOWN')
    results = []
    for key, row in rows:
        state, detail = disposition(row, now)
        results.append({'key': key, 'desk': row[1], 'touch': row[3], 'state': state, 'detail': detail})
    return results, issues


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--ledger', type=Path, default=ROOT / 'PROME/state/ORCH_LOG.tsv')
    ap.add_argument('--date', type=dt.date.fromisoformat, default=dt.datetime.now(ET).date())
    ap.add_argument('--expected-key', action='append', default=[])
    ap.add_argument('--inventory-complete', action='store_true',
                    help='attest expected keys cover the actual selected-day tool/spawn record; not fleet liveness')
    args = ap.parse_args(argv)
    try:
        rows, issues = evaluate(args.ledger, args.date, args.expected_key, args.inventory_complete)
    except (OSError, ValueError) as exc:
        print(f'UNKNOWN: cannot enumerate {args.ledger}: {exc}')
        return 2
    if not rows and not issues:
        return 0
    print(f'ORCH_LOG closeout evidence — {args.date}; attributed records, not native receipt authentication')
    for state, label in LABELS.items():
        matching = [r for r in rows if r['state'] == state]
        print(f'{label}: {len(matching)}')
        for row in matching:
            print(f"  {row['desk']} touch {row['touch']} [{row['key']}]: {row['detail']}")
    for row in rows:
        if row['state'] not in LABELS:
            print(f"{row['state']}: {row['desk']} touch {row['touch']} [{row['key']}]: {row['detail']}")
    for issue in issues:
        print(f'UNKNOWN: {issue}')
    return 1 if issues or any(r['state'] == 'UNKNOWN' for r in rows) else 0


if __name__ == '__main__':
    raise SystemExit(main())
