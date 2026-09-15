#!/usr/bin/env python3
"""Validate a reviewed signal companion; never refresh hashes automatically.

Checks byte identity, approval receipt, date and fleet budget, not semantic truth.
--read emits the same validated companion bytes only after every check passes.
"""
import argparse
from datetime import date, datetime, timezone
import hashlib
import importlib.util
import json
from pathlib import Path
import re

REPO = Path(__file__).resolve().parents[3]
REGISTRY = 'AGENTS/WALTER/registry/signal_read_companions.json'


def budget():
    spec = importlib.util.spec_from_file_location('fleet_read_cap', REPO / 'scripts/read_cap_check.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.BUDGET_BYTES


def checked_path(repo, value, prefix):
    if not isinstance(value, str):
        raise ValueError('path must be text')
    path = Path(value)
    if path.is_absolute() or '..' in path.parts or not value.startswith(prefix):
        raise ValueError('path outside allowed source/companion/review scope')
    resolved = (repo / path).resolve()
    if not resolved.is_relative_to((repo / prefix).resolve()):
        raise ValueError('resolved path outside allowed scope')
    return resolved


def validate(signal_id, repo=REPO, today=None, byte_budget=None):
    """Return (record, validated body). Raise on any missing/unreviewed/stale input."""
    today = today or datetime.now(timezone.utc).date()
    byte_budget = budget() if byte_budget is None else byte_budget
    if not re.fullmatch(r'SIG-W-\d{8}-\d{3}', signal_id):
        raise ValueError('invalid exact signal ID')
    registry = json.loads((repo / REGISTRY).read_text())
    record = registry[signal_id]
    if record['status'] != 'reviewed':
        raise ValueError('companion not independently approved')
    reviewed = date.fromisoformat(record['reviewed_on'])
    due = date.fromisoformat(record['review_due'])
    if not reviewed <= today < due:
        raise ValueError('review future-dated or due; re-review required')
    blobs = {}
    for key, prefix in [('source', 'BOARD/'), ('companion', 'AGENTS/WALTER/reading/'),
                        ('review', 'AGENTS/WALTER/research/')]:
        raw = checked_path(repo, record[key], prefix).read_bytes()
        if hashlib.sha256(raw).hexdigest() != record[key + '_sha256']:
            raise ValueError(f'{key} bytes changed; re-review required')
        raw.decode('utf-8')  # Reject malformed bytes before any PASS or companion output.
        blobs[key] = raw
    if not re.search(r'^signal_id: ' + re.escape(signal_id) + r'\s*$',
                     blobs['source'].decode(), re.MULTILINE):
        raise ValueError('source signal ID mismatch')
    if Path(record['companion']).name != signal_id + '.md':
        raise ValueError('companion filename does not match ID')
    if not re.search(r'^Verdict: APPROVED\s*$', blobs['review'].decode(), re.MULTILINE):
        raise ValueError('review lacks explicit approval')
    if not blobs['companion'] or len(blobs['companion']) >= byte_budget:
        raise ValueError('companion empty or over fleet read budget')
    return record, blobs['companion']


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('signal_id')
    parser.add_argument('--read', action='store_true')
    args = parser.parse_args()
    try:
        record, body = validate(args.signal_id)
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(f'PARTIAL: {args.signal_id}: {exc}. No companion authorized; use source and re-review.')
        return 1
    print(f'PASS: {args.signal_id}: source/companion/review hashes match; {len(body)} B; '
          f'review due {record["review_due"]}. Identity/coverage receipt, not primary verification.')
    if args.read:
        print(body.decode(), end='')
    else:
        print(f'Read WHOLE: {record["companion"]}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
