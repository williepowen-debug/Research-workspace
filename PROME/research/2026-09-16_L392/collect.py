#!/usr/bin/env python3
"""Bounded L392 observations; never changes STALE_S or grades a contract.

--schedule captures six declared windows today; --once captures a setup sample.
Every sample runs contract_probe in a fresh process (no inherited quote cache).
"""
import argparse
import datetime as dt
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import time
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent
ET = ZoneInfo('America/New_York')
DAY = dt.date(2026, 9, 16)
SLOTS = [('preclose', 16, 5), ('preclose', 16, 25), ('preclose', 16, 45),
         ('evening', 20, 5), ('evening', 20, 25), ('evening', 20, 45)]


def worker():
    path = ROOT / 'FORGE/tools/market-data/fetch.py'
    spec = importlib.util.spec_from_file_location('market_fetch', path)
    module = importlib.util.module_from_spec(spec)
    sys.path.insert(0, str(path.parent))
    spec.loader.exec_module(module)
    print(json.dumps(module.contract_probe('BZ'), sort_keys=True))


def sample(window, planned=None):
    started = dt.datetime.now(dt.timezone.utc)
    code = ROOT / 'FORGE/tools/market-data/fetch.py'
    record = {'window': window, 'planned_at': planned.isoformat() if planned else None,
              'started_at': started.isoformat(), 'fetch_sha256': hashlib.sha256(code.read_bytes()).hexdigest(),
              'root': 'BZ', 'horizon': 5, 'exchange': 'NYM', 'policy_change': False}
    try:
        result = subprocess.run([sys.executable, str(Path(__file__).resolve()), '--worker'],
                                capture_output=True, text=True, timeout=100, cwd=ROOT)
        record.update(returncode=result.returncode, stdout=result.stdout, stderr=result.stderr)
        try:
            record['probe'] = json.loads(result.stdout)
        except ValueError:
            record['error'] = 'worker output is not JSON'
    except subprocess.TimeoutExpired as exc:
        record.update(error='worker timeout', returncode=None)
    record['finished_at'] = dt.datetime.now(dt.timezone.utc).isoformat()
    name = started.strftime('%Y%m%dT%H%M%S%fZ') + '-' + window + '.json'
    with (OUT / name).open('x') as f:
        json.dump(record, f, indent=2); f.write('\n')
    print(json.dumps({'file': name, 'window': window, 'verdict': record.get('probe', {}).get('verdict'),
                      'error': record.get('error')}), flush=True)
    return record


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    group = ap.add_mutually_exclusive_group(required=True)
    group.add_argument('--worker', action='store_true')
    group.add_argument('--once', action='store_true')
    group.add_argument('--schedule', action='store_true')
    group.add_argument('--plan', action='store_true')
    args = ap.parse_args()
    if args.worker:
        worker(); return
    if args.once:
        sample('setup-only'); return
    slots = [(label, dt.datetime.combine(DAY, dt.time(hour, minute), ET)) for label, hour, minute in SLOTS]
    if args.plan:
        print('\n'.join(f'{label}\t{stamp.isoformat()}' for label, stamp in slots)); return
    for label, stamp in slots:
        now = dt.datetime.now(ET)
        if (now - stamp).total_seconds() > 120:
            print(f'MISSED {label} {stamp.isoformat()}; not backfilled', flush=True)
            continue
        while (remaining := (stamp - dt.datetime.now(ET)).total_seconds()) > 0:
            time.sleep(min(remaining, 30))
        sample(label, stamp)
    print('Bounded observation schedule finished; no calibration or policy change performed.', flush=True)


if __name__ == '__main__':
    main()
