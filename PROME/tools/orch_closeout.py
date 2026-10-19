#!/usr/bin/env python3
"""Read the existing ORCH_LOG closeout evidence; never infer native liveness.

Evidence is an attributed record, not authentication of the referenced receipt.
No messaging, file mutation, or closeout-blocking authority is provided here.
Coverage includes the selected ET day and all unresolved prior-date touches.
Historical evidence gaps remain UNKNOWN until reconciled, never aged away.
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
    """Read candidate touches through day; closure filtering happens after validation."""
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
        if row_day > day or fields[3] == 'CLOSE':
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


def structured(row):
    if row[8].count(MARKER) != 1:
        raise ValueError('missing or duplicate structured identity')
    data = json.loads(row[8].split(MARKER, 1)[1])
    if not isinstance(data, dict):
        raise ValueError('evidence must be an object')
    return data


def reconcile(touches, now):
    """Resolve explicit event links only; retain each original obligation's identity.

    A resolution event is evidence about the named original touch, not another
    spawn. It may update WORKING to RECEIPT (or correct a disposition), but never
    guesses which earlier session a desk name meant.
    """
    originals, issues = {}, []
    for key, row in touches:
        state, detail = disposition(row, now)
        try:
            data = structured(row)
        except (ValueError, TypeError):
            data = {}
        targets = data.get('resolves')
        result = {'key': key, 'date': row[0], 'desk': row[1], 'touch': row[3],
                  'state': state, 'detail': detail, 'session_id': data.get('session_id'),
                  'owner': data.get('owner'), 'touch_at': data.get('touch_at'), 'events': []}
        if targets is None:
            originals[key] = (row, data, result)
            continue
        try:
            if not isinstance(targets, list) or not targets or len(set(targets)) != len(targets):
                raise ValueError('resolves must name distinct original touch keys')
            if state == 'UNKNOWN':
                raise ValueError(f'invalid resolution evidence: {detail}')
            checked = []
            for target in targets:
                if target not in originals:
                    raise ValueError(f'unknown/non-original target {target}')
                original, identity, previous = originals[target]
                if (row[1], data['owner'], data['session_id']) != (
                        original[1], identity.get('owner'), identity.get('session_id')):
                    raise ValueError(f'identity mismatch for {target}')
                touched = timestamp(identity.get('touch_at'))
                if touched.astimezone(ET).date().isoformat() != original[0]:
                    raise ValueError(f'original timestamp/date mismatch for {target}')
                if not touched <= timestamp(data['touch_at']) <= timestamp(data['observed_at']) <= now:
                    raise ValueError(f'resolution predates original touch {target}')
                last_at = previous.get('resolved_at', identity.get('observed_at'))
                if timestamp(data['observed_at']) <= timestamp(last_at):
                    raise ValueError(f'out-of-order or ambiguous tied correction for {target}')
                checked.append(previous)
            for previous in checked:
                previous.update(state=state, detail=f'{detail} | resolution event {key}',
                                resolved_at=data['observed_at'])
                previous['events'].append(key)
        except (ValueError, TypeError, KeyError) as exc:
            issues.append(f'resolution {key}: {exc}; UNKNOWN')
            result.update(state='UNKNOWN', detail=str(exc))
            originals[key] = (row, data, result)
    return [item[2] for item in originals.values()], issues


def evaluate(path, day, expected=(), inventory_complete=False, now=None, session_inventory=None):
    now = now or dt.datetime.now(dt.timezone.utc)
    reconciled, issues = reconcile(read_touches(path, day), now)
    results = [r for r in reconciled if r['date'] >= day.isoformat() or
               r['state'] not in ('ASKED_RECEIPT', 'ALREADY_CLOSED', 'OUT_OF_SCOPE')]
    if session_inventory is not None:
        inv = session_inventory
        if not isinstance(inv, dict) or inv.get('complete') is not True or not inv.get('session_ids'):
            raise ValueError('bounded inventory requires complete=true and session_ids')
        if (not isinstance(inv['session_ids'], list) or
                not all(isinstance(s, str) and s.strip() for s in inv['session_ids']) or
                len(set(inv['session_ids'])) != len(inv['session_ids'])):
            raise ValueError('inventory session identities must be distinct nonempty strings')
        if not isinstance(inv.get('evidence'), str) or not inv['evidence'].strip():
            raise ValueError('inventory requires actual runtime enumeration evidence')
        if not timestamp(inv.get('observed_at')) <= now:
            raise ValueError('inventory observation is in the future')
        if timestamp(inv['observed_at']).astimezone(ET).date() != day:
            raise ValueError('inventory observation must be on selected day')
        if not isinstance(inv.get('expected_keys'), list) or not all(
                isinstance(k, str) and re.fullmatch('[0-9a-f]{64}', k) for k in inv['expected_keys']):
            raise ValueError('inventory expected_keys must contain touch hashes')
        expected, inventory_complete = inv['expected_keys'], True
        # Keep historical debt in results. Only this explicitly bounded population
        # participates in current-session coverage, never a global green claim.
        current = [r for r in reconciled if r['session_id'] in inv['session_ids']]
        for row in current:
            if timestamp(row['touch_at']) > timestamp(inv['observed_at']):
                issues.append(f'inventory observation predates enumerated touch: {row["key"]}; UNKNOWN')
        current_keys = {r['key'] for r in current}
        results = [r for r in reconciled if r in results or r['key'] in current_keys]
        for row in results:
            row['population'] = 'current' if row['session_id'] in inv['session_ids'] else 'outside-inventory'
        actual = {r['key'] for r in current}
        known_sessions = {r['session_id'] for r in current}
        for session in set(inv['session_ids']) - known_sessions:
            issues.append(f'known session absent from ORCH_LOG: {session}; UNKNOWN')
    else:
        actual = {row['key'] for row in results}
    expected = set(expected)
    if not inventory_complete:
        issues.append('spawn inventory coverage UNKNOWN; ledger absence cannot prove no spawns')
    for key in sorted(expected - actual):
        issues.append(f'known spawn absent from ORCH_LOG: {key}; UNKNOWN')
    if inventory_complete:
        for key in sorted(actual - expected):
            issues.append(f'ledger touch absent from declared complete inventory: {key}; UNKNOWN')
    return results, issues


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--ledger', type=Path, default=ROOT / 'PROME/state/ORCH_LOG.tsv')
    ap.add_argument('--date', type=dt.date.fromisoformat, default=dt.datetime.now(ET).date())
    ap.add_argument('--expected-key', action='append', default=[])
    ap.add_argument('--inventory-complete', action='store_true',
                    help='attest expected keys cover selected-day touches and unresolved prior touches; not fleet liveness')
    ap.add_argument('--session-inventory', type=Path,
                    help='JSON: session_ids, expected_keys, observed_at, evidence, complete; historical debt stays separate')
    ap.add_argument('--json', action='store_true')
    args = ap.parse_args(argv)
    try:
        inv = json.loads(args.session_inventory.read_text()) if args.session_inventory else None
        rows, issues = evaluate(args.ledger, args.date, args.expected_key, args.inventory_complete,
                               session_inventory=inv)
    except (OSError, ValueError) as exc:
        print(f'UNKNOWN: cannot enumerate {args.ledger}: {exc}')
        return 2
    if args.json:
        print(json.dumps({'rows': rows, 'issues': issues,
                          'coverage': 'bounded-session' if inv else 'ledger-with-unresolved-history',
                          'historical_unknown': sum(r['date'] < str(args.date) and r['state'] == 'UNKNOWN' for r in rows),
                          'limits': 'Attributed records, not receipt authentication or fleet liveness.'}, indent=2))
        return 1 if issues or any(r['state'] == 'UNKNOWN' for r in rows) else 0
    if not rows and not issues:
        return 0
    print(f'ORCH_LOG closeout evidence — {args.date} + unresolved prior touches; attributed records, not native receipt authentication')
    for state, label in LABELS.items():
        matching = [r for r in rows if r['state'] == state]
        print(f'{label}: {len(matching)}')
        for row in matching:
            print(f"  {row['date']} {row['desk']} touch {row['touch']} [{row['key']}]: {row['detail']}")
    for row in rows:
        if row['state'] not in LABELS:
            print(f"{row['state']}: {row['date']} {row['desk']} touch {row['touch']} [{row['key']}]: {row['detail']}")
    for issue in issues:
        print(f'UNKNOWN: {issue}')
    return 1 if issues or any(r['state'] == 'UNKNOWN' for r in rows) else 0


if __name__ == '__main__':
    raise SystemExit(main())
