#!/usr/bin/env python3
"""Replay real source extracts against the complete canonical docket at their pin.

Missing Git objects are UNKNOWN rc2, not a passing production test.
"""
import datetime as dt
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[4]
spec = importlib.util.spec_from_file_location('coverage_check', ROOT / 'AGENTS/DAEDALUS/scripts/calendar_docket_coverage.py')
c = importlib.util.module_from_spec(spec)
spec.loader.exec_module(c)


def main():
    data = json.loads(Path(__file__).with_name('production.json').read_text())
    try:
        raw = subprocess.check_output(['git', 'show', data['revision'] + ':' + data['docket']], cwd=ROOT)
        for case in data['cases']:
            original = subprocess.check_output(['git', 'show', data['revision'] + ':' + case['source']], cwd=ROOT).decode().splitlines()
            if original[0] != case['header'] or original[case['line'] - 1] != case['row']:
                raise ValueError('production extract does not match pinned source: ' + case['id'])
    except (subprocess.CalledProcessError, ValueError, IndexError) as exc:
        print('UNKNOWN: production source unavailable or changed:', exc)
        return 2
    failed = 0
    with tempfile.TemporaryDirectory(prefix='calendar-production-') as temp:
        root = Path(temp)
        docket = root / data['docket']
        docket.parent.mkdir(parents=True)
        docket.write_bytes(raw)
        for case in data['cases']:
            path = root / case['source']
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(case['header'] + '\n' + case['row'] + '\n')
            r = c.assess(root, docket, [path], dt.date.fromisoformat(data['as_of']), 14, True)
            states = [row['status'] for row in r['records']]
            ok = states == [case['expected']]
            failed += not ok
            print(f"{'PASS' if ok else 'FAIL'} {case['id']}: {case['source']}:{case['line']} -> {states}, rc={r['rc']}")
            if case['expected'] == 'MATCHED':
                print('CLEAN: nonempty real row has candidate correspondence; not semantic or delivery proof.')
            else:
                print(case['expected'] + ': ' + r['records'][0]['reason'])
    return 1 if failed else 0


if __name__ == '__main__':
    sys.exit(main())
