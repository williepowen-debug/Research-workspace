#!/usr/bin/env python3
"""YURI due-date check; read-only, own directory IN.

CHECK_STANDARD perimeter: row dates and YUR-004 registered checkpoints only.
No source access, grading, messaging, inbox consumption or body-text verification.
Production cases: workbook/INTENT_LEDGER.tsv at pre-2026-10-12 HEAD, evaluated
2026-10-02 (clean) and 2026-10-12 (missed 10/09 checkpoint). Acceptance record:
research/2026-10-12_BOOT_CHECK_ACCEPTANCE.md. Baseline 4 rows / 1 missed checkpoint.
rc 0 no work due; 1 due; 2 cannot certify. Missing information biases to 2.
"""
import argparse
import csv
from datetime import date, datetime
from pathlib import Path
import re
import sys
from zoneinfo import ZoneInfo

DESK = Path(__file__).resolve().parents[1]


def assess(ledger, letter, today):
    raw = ledger.read_text()
    lines = [line for line in raw.splitlines() if line and not line.startswith('#')]
    reader = csv.DictReader(lines, delimiter='\t')
    required = {'id', 'registered', 'resolve_by', 'reading', 'status'}
    if not reader.fieldnames or not required <= set(reader.fieldnames):
        raise ValueError('ledger header missing required fields')
    rows = list(reader)
    if not rows or len({r['id'] for r in rows}) != len(rows):
        raise ValueError('empty ledger or duplicate row id')
    due = []
    for row in rows:
        if None in row or any(value is None for value in row.values()):
            raise ValueError('ragged row ' + row['id'])
        registered = date.fromisoformat(row['registered'])
        end = date.fromisoformat(row['resolve_by'])
        if end < registered:
            raise ValueError('resolve_by precedes registration: ' + row['id'])
        token = row['status'].split(' ', 1)[0]
        if token not in {'OPEN', 'HIT', 'MISS', 'VOID', 'STUCK'}:
            raise ValueError('unknown status: ' + row['id'])
        if token != 'OPEN':
            continue
        if registered > today:
            raise ValueError('future registration: ' + row['id'])
        if end <= today:
            due.append(row['id'] + ' final date ' + end.isoformat())
        if row['id'] == 'YUR-004':
            text = letter.read_text()
            section = text.split('**4. Checkpoints and grading cadence.**', 1)[1].split('**5.', 1)[0]
            weekly = section.split('**Weekly reads on Fridays:**', 1)[1].split('\n', 1)[0]
            checkpoints = [date(registered.year, int(m), int(d))
                           for m, d in re.findall(r'(\d{2})/(\d{2})', weekly)]
            stamps = re.findall(r'(?:YURI (\d{4}-\d{2}-\d{2}) review|First read (\d{4}-\d{2}-\d{2}))', row['reading'])
            if not checkpoints or not stamps:
                raise ValueError('YUR-004 calendar or row review date missing')
            reviewed = max(date.fromisoformat(a or b) for a, b in stamps)
            if reviewed > today or reviewed < registered:
                raise ValueError('YUR-004 review date outside observed range')
            due.extend('YUR-004 checkpoint ' + d.isoformat()
                       for d in checkpoints if reviewed < d <= today)
    return len(rows), due


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--ledger', type=Path, default=DESK / 'workbook/INTENT_LEDGER.tsv')
    parser.add_argument('--letter', type=Path, default=DESK / 'research/2026-10-02_YUR-004_REGISTERED.md')
    parser.add_argument('--as-of', type=date.fromisoformat)
    args = parser.parse_args()
    now = datetime.now(ZoneInfo('America/New_York'))
    print(now.strftime('⏰ WALL CLOCK: %Y-%m-%d %H:%M:%S %Z'))
    today = args.as_of or now.date()
    print('PERIMETER: YURI row dates and YUR-004 checkpoints; as-of ' + today.isoformat())
    print('NOTE: no source verification, grading, messaging or inbox-consumption certification.')
    try:
        count, due = assess(args.ledger, args.letter, today)
    except (OSError, ValueError, IndexError, KeyError) as error:
        print('UNKNOWN: YURI must repair or inspect input: ' + str(error))
        return 2
    if due:
        for item in due:
            print('DUE: YURI must review ' + item)
        return 1
    print('PASS: no dates due among ' + str(count) + ' rows; proves only this date perimeter.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
