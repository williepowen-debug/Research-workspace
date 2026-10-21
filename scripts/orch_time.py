#!/usr/bin/env python3
"""L748 append-only UNKNOWN time invalidation and attributed Git upper-bound audit.

Not receipt authentication, original append-time proof, or fleet liveness.
Use `invalidate --target KEY --reason EVIDENCE` only with owner authorization.
"""
import argparse
import datetime as dt
import hashlib
import json
from pathlib import Path
import subprocess
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
MARKER = 'time_correction_v1='
CLOSEOUT = 'closeout_v1='
ET = ZoneInfo('America/New_York')


def key(row):
    return hashlib.sha256(json.dumps(row[:5], ensure_ascii=True, separators=(',', ':')).encode()).hexdigest()


def stamp(value):
    if not isinstance(value, str):
        raise ValueError('timestamp absent')
    result = dt.datetime.fromisoformat(value.replace('Z', '+00:00'))
    if result.tzinfo is None:
        raise ValueError('timestamp lacks timezone')
    return result


def payload(row, marker):
    if row[8].count(marker) != 1:
        raise ValueError('missing or duplicate structured marker')
    result = json.loads(row[8].split(marker, 1)[1])
    if not isinstance(result, dict):
        raise ValueError('payload must be object')
    return result


def validate_correction(row, prior, now):
    data = payload(row, MARKER)
    if CLOSEOUT in row[8]:
        raise ValueError('correction cannot mix lifecycle evidence markers')
    if row[3] != 'CLOSE' or row[6] != 'TIME-CORRECTION (original time UNKNOWN)':
        raise ValueError('correction must be CLOSE with fixed delivery token')
    if any(row[i] for i in (5, 10, 11, 12)):
        raise ValueError('correction cannot claim quantitative activity')
    if data.get('replacement') != 'UNKNOWN':
        raise ValueError('only UNKNOWN replacement is authorized')
    if not isinstance(data.get('reason'), str) or not data['reason'].strip():
        raise ValueError('correction needs evidence/reason')
    recorded = stamp(data.get('recorded_at'))
    if recorded > now or recorded.astimezone(ET).date().isoformat() != row[0]:
        raise ValueError('correction date mismatch or future record')
    matches = [r for r in prior if key(r) == data.get('target')]
    if len(matches) != 1:
        raise ValueError('target must identify exactly one earlier original')
    original = matches[0]
    identity = payload(original, CLOSEOUT)
    if original[3] == 'CLOSE' or MARKER in original[8] or identity.get('resolves') is not None:
        raise ValueError('target is not an original touch')
    if (row[1], data.get('owner'), data.get('session_id')) != (
            original[1], identity.get('owner'), identity.get('session_id')):
        raise ValueError('correction identity mismatch')
    if data.get('owner') not in ('PROME', 'WILL') or not isinstance(data.get('session_id'), str) or not data['session_id'].strip():
        raise ValueError('original identity unavailable')
    return data


def apply_invalidations(touches, results, issues, now):
    """After lifecycle reconciliation; a receipt can never restore invalidated time."""
    prior, removed, invalidated, invalid = [], set(), {}, {}
    for event_key, row in touches:
        if MARKER in row[8]:
            try:
                data = validate_correction(row, prior, now)
                removed.add(event_key)
                invalidated.setdefault(data['target'], []).append((event_key, data['reason']))
            except (ValueError, TypeError, KeyError) as exc:
                issues.append(f'time correction {event_key}: {exc}; UNKNOWN')
                invalid[event_key] = str(exc)
        prior.append(row)
    out = [r for r in results if r['key'] not in removed]
    for row in out:
        if row['key'] in invalid:
            row.update(state='UNKNOWN', detail=invalid[row['key']])
        if row['key'] in invalidated:
            row.update(state='UNKNOWN', time_status='INVALIDATED-UNKNOWN',
                       detail='historical touch time invalidated; ' + repr(invalidated[row['key']]))
    return out, issues


def rotation_problem(rows, moving):
    """Pin both sides; malformed correction evidence refuses rotation conservatively."""
    pins, prior = set(), []
    for row in rows:
        if MARKER in row[8]:
            try:
                data = validate_correction(row, prior, dt.datetime.now(dt.timezone.utc))
                target = data['target']
                if not isinstance(target, str) or len(target) != 64:
                    raise ValueError('invalid target')
                pins.update((key(row), target))
            except (ValueError, TypeError, KeyError):
                return 'malformed time correction; preserve readable evidence'
        prior.append(row)
    if any(key(row) in pins for row in moving):
        return 'time correction/original pinned in hot ledger; UNKNOWN debt cannot age away'
    return None


def audit(root, ledger, revision):
    """Compare committed structured times to attributed line commit metadata only."""
    def git(*args):
        return subprocess.check_output(['git', '-C', str(root), *args], text=True, stderr=subprocess.PIPE)
    import orch_log
    if orch_log.check(str(ledger), quiet=True)[0]:
        raise ValueError('invalid ledger schema/header: population UNKNOWN')
    revision = git('rev-parse', '--verify', revision + '^{commit}').strip()
    relative = ledger.resolve().relative_to(root.resolve()).as_posix()
    if git('rev-parse', '--is-shallow-repository').strip() != 'false':
        raise ValueError('shallow history: provenance UNKNOWN')
    committed = git('show', f'{revision}:{relative}')
    if ledger.read_bytes() != committed.encode():
        raise ValueError('working ledger differs from pinned revision: provenance UNKNOWN')
    blamed = git('blame', '--line-porcelain', revision, '--', relative)
    metadata, commits = {}, []
    for line in blamed.splitlines():
        if line.startswith('\t'):
            commits.append(dict(metadata)); metadata = {}
        elif line.startswith('committer-time '):
            metadata['time'] = int(line.split()[1])
        elif line == 'boundary':
            metadata['boundary'] = True
        elif len(line.split()) >= 3 and len(line.split()[0]) == 40:
            metadata['commit'] = line.split()[0]
    lines = committed.splitlines()
    if len(lines) != len(commits):
        raise ValueError('blame population mismatch')
    output = []
    for n, (line, provenance) in enumerate(zip(lines, commits), 1):
        if not line.strip() or line.startswith('#') or line.startswith('date\t'):
            continue
        row = line.split('\t')
        if len(row) != 13:
            raise ValueError(f'line {n}: malformed ledger')
        marker = MARKER if MARKER in row[8] else CLOSEOUT
        if marker not in row[8]:
            continue
        result = dict(line=n, key=key(row), attributed_commit=provenance.get('commit'), state='UNKNOWN')
        try:
            data = payload(row, marker)
            touched = stamp(data.get('recorded_at' if marker == MARKER else 'touch_at'))
            if provenance.get('boundary') or 'time' not in provenance or 'commit' not in provenance:
                raise ValueError('boundary or missing attributed commit metadata')
            committed_at = dt.datetime.fromtimestamp(provenance['time'], dt.timezone.utc)
            result.update(attributed_commit_at=committed_at.isoformat(),
                          state='INVALID-FUTURE' if touched > committed_at else 'UPPER-BOUND-CONSISTENT')
        except (ValueError, TypeError) as exc:
            result['reason'] = str(exc)
        output.append(result)
    if not output:
        raise ValueError('no structured timestamp population: NOT-ASSESSED')
    return dict(revision=revision, rows=output, limits='Attributed line-changing commit metadata, not original append time or authenticated event time. Earlier placeholders can pass.')


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('mode', choices=['audit', 'invalidate'])
    ap.add_argument('--ledger', type=Path, default=ROOT/'PROME/state/ORCH_LOG.tsv')
    ap.add_argument('--view-path', type=Path, default=ROOT/'PROME/state/ORCH_INFLIGHT.md')
    ap.add_argument('--revision', default='HEAD')
    ap.add_argument('--target')
    ap.add_argument('--reason')
    ap.add_argument('--acknowledge-unobserved', type=int)
    args = ap.parse_args()
    try:
        if args.mode == 'audit':
            result = audit(ROOT, args.ledger, args.revision)
            print(json.dumps(result, indent=2))
            return 2 if any(r['state'] != 'UPPER-BOUND-CONSISTENT' for r in result['rows']) else 0
        import orch_log
        rc, rows = orch_log.check(str(args.ledger), quiet=True)
        if rc: raise ValueError('ledger malformed')
        targets = [r for r in rows if key(r) == args.target]
        if len(targets) != 1: raise ValueError('target must identify exactly one row')
        identity = payload(targets[0], CLOSEOUT)
        now = dt.datetime.now(dt.timezone.utc)
        data = dict(target=args.target, owner=identity.get('owner'), session_id=identity.get('session_id'),
                    replacement='UNKNOWN', recorded_at=now.isoformat(), reason=args.reason)
        values = {c: '' for c in orch_log.COLS}
        values.update(date=now.astimezone(ET).date().isoformat(), desk=targets[0][1], tier=targets[0][2],
                      touch='CLOSE', trigger=f'time invalidation {args.target} at {now.isoformat()}',
                      delivered='TIME-CORRECTION (original time UNKNOWN)', notes=MARKER+json.dumps(data))
        return orch_log.append(argparse.Namespace(**values, acknowledge_unobserved=args.acknowledge_unobserved),
                               str(args.ledger), str(args.view_path))
    except (OSError, ValueError, TypeError, subprocess.SubprocessError) as exc:
        print(f'UNKNOWN: {exc}')
        return 2

if __name__ == '__main__':
    raise SystemExit(main())
