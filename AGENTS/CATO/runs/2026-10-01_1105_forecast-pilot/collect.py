#!/usr/bin/env python3
"""Capture committed first-call records for CATO's bounded pilot; never grade.

No network, owner writes, scheduling, staging or commits. Default is preview.
--write atomically replaces only capture.json beside the frozen config.
"""
import argparse
import csv
import fcntl
import datetime as dt
import hashlib
import io
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile

HERE = Path(__file__).resolve().parent


def git(repo, *args):
    return subprocess.check_output(['git', '-C', str(repo), *args], text=True,
                                   stderr=subprocess.PIPE)


def rows(text, path):
    data = [r for r in csv.reader(io.StringIO(text), delimiter='\t')
            if r and any(r) and not r[0].startswith('#')]
    if not data:
        raise ValueError(f'empty ledger: {path}')
    header = data[0]
    names = [x.strip().lower() for x in header]
    if len(names) != len(set(names)):
        raise ValueError(f'duplicate columns: {path}')
    id_col = next((names.index(x) for x in ('pred_id', 'id') if x in names), None)
    if id_col is None:
        raise ValueError(f'no ID column: {path}')
    result = {}
    for fields in data[1:]:
        if len(fields) <= id_col or not fields[id_col].strip():
            raise ValueError(f'unidentifiable row: {path}')
        key = path.split('/')[1] + '/' + fields[id_col].strip()
        if key in result:
            raise ValueError(f'duplicate ID: {path}: {key}')
        result[key] = {'header': header, 'fields': fields,
                       'valid': len(header) == len(fields)}
    return result


def probability(row, interpretations=()):
    """Candidate detection only; no tiers, ranges or embedded narrative odds."""
    names = [s.strip().lower() for s in row['header']]
    if 'confidence' not in names:
        return None
    value = row['fields'][names.index('confidence')].strip()
    match = re.fullmatch(r'(\d{1,3}(?:\.\d+)?)\s*%', value)
    if match and 0 <= float(match[1]) <= 100:
        return float(match[1]) / 100
    # Numeric-looking annotations need a human decision before later slots fill.
    if re.search(r'\d', value):
        matches = [d for d in interpretations
                   if d['key'] == row['key'] and d['commit'] == row['commit']]
        if matches:
            if len(matches) != 1:
                raise ValueError('duplicate probability interpretations')
            decision = matches[0]
            leading = re.match(r'^(\d{1,3}(?:\.\d+)?)(?:%\s+[\[(]|pct$)', value)
            if (decision['blob'] != row['blob'] or decision['confidence'] != value
                    or not decision.get('reason') or not decision.get('evidence')
                    or not leading or not 0 <= float(leading[1]) <= 100
                    or decision['p'] != float(leading[1]) / 100):
                raise ValueError('probability interpretation evidence/value mismatch')
            row['probability_interpretation'] = decision
            return decision['p']
        raise ValueError(f'ambiguous numeric confidence: {value!r}')
    return None


def collect(repo, config, pin, interpretations=()):
    base = config['baseline_commit']
    pin = git(repo, 'rev-parse', pin + '^{commit}').strip()
    git(repo, 'merge-base', '--is-ancestor', base, pin)
    if git(repo, 'rev-list', '--min-parents=2', f'{base}..{pin}').strip():
        raise ValueError('merge in pilot range; review ancestry before collection')
    paths = config['paths']
    seen = set(config['baseline_keys'])
    current = {}
    for path in paths:
        current[path] = rows(git(repo, 'show', base + ':' + path), path)
    selected, skipped, versions = [], [], []
    selected_keys = set()
    cutoff = dt.datetime.fromisoformat(config['enrollment_ends_utc'])
    commits = git(repo, 'rev-list', '--reverse', f'{base}..{pin}', '--', *paths).splitlines()
    for commit in commits:
        timestamp = git(repo, 'show', '-s', '--format=%cI', commit).strip()
        in_window = dt.datetime.fromisoformat(timestamp) <= cutoff
        changed = git(repo, 'diff-tree', '--no-commit-id', '--name-only', '-r', commit,
                      '--', *paths).splitlines()
        occurrences = {}
        deleted = []
        for path in changed:
            text = git(repo, 'show', commit + ':' + path)  # missing path is a coverage failure
            blob = git(repo, 'rev-parse', commit + ':' + path).strip()
            new_rows = rows(text, path)
            for key, row in new_rows.items():
                if key in seen and key not in selected_keys:
                    continue
                if not row['valid']:
                    raise ValueError(f'malformed candidate/selected row: {commit}:{path}: {key}')
                entry = {'key': key, 'commit': commit, 'committed_at': timestamp,
                         'path': path, 'blob': blob, **row}
                if key in occurrences:
                    raise ValueError(f'same-commit duplicate across ledgers: {key}')
                if key not in current[path] or row != current[path][key]:
                    occurrences[key] = entry
            for key in current[path].keys() - new_rows.keys():
                if key in selected_keys:
                    deleted.append({'key': key, 'commit': commit, 'committed_at': timestamp,
                                    'path': path, 'deleted_from_observed_path': True})
            current[path] = new_rows
        for key, entry in sorted(occurrences.items()):
            if key in selected_keys:
                versions.append(entry)
                continue
            seen.add(key)
            if not in_window or len(selected) >= config['limit']:
                continue
            p = probability(entry, interpretations)
            if p is None:
                skipped.append({**entry, 'reason': 'NO_NUMERIC_PROBABILITY_AT_FIRST_APPEARANCE'})
            else:
                selected.append({**entry, 'slot': len(selected) + 1, 'p_original_candidate': p,
                                 'review': 'PENDING'})
                selected_keys.add(key)
        versions.extend(deleted)
    # Detect a missing ledger even if no usable commit was returned.
    for path in paths:
        git(repo, 'cat-file', '-e', pin + ':' + path)
    return {'baseline_commit': base, 'through_commit': pin,
            'config_sha256': hashlib.sha256(json.dumps(config, sort_keys=True).encode()).hexdigest(),
            'selected': selected, 'later_versions': versions, 'nonnumeric_new_rows': skipped,
            'limits': 'Candidate capture only. Manual registration, eligibility and outcome review required.'}


def write_capture(path, result, repo):
    # Lock the directory itself: no stale lock-file cleanup or concurrent overwrite.
    lock = os.open(path.parent, os.O_RDONLY)
    temp = None
    try:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        if path.exists():
            previous = json.loads(path.read_text())
            git(repo, 'merge-base', '--is-ancestor', previous['through_commit'],
                result['through_commit'])
            if previous['config_sha256'] != result['config_sha256']:
                raise ValueError('frozen config changed; refusing overwrite')
            for field in ('selected', 'later_versions', 'nonnumeric_new_rows'):
                old = previous[field]
                if result[field][:len(old)] != old:
                    raise ValueError(f'capture history would change or shrink: {field}')
        fd, temp = tempfile.mkstemp(prefix='.capture-', dir=path.parent)
        with os.fdopen(fd, 'w') as out:
            out.write(json.dumps(result, indent=2) + '\n')
        os.replace(temp, path)
    finally:
        if temp and os.path.exists(temp):
            os.unlink(temp)  # only our own failed temporary output
        os.close(lock)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--pin', default='HEAD')
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args()
    try:
        repo = Path(git(HERE, 'rev-parse', '--show-toplevel').strip())
        config = json.loads((HERE / 'config.json').read_text())
        decision_path = HERE / 'probability_interpretations.json'
        interpretations = json.loads(decision_path.read_text()) if decision_path.exists() else []
        result = collect(repo, config, args.pin, interpretations)
        if args.write:
            write_capture(HERE / 'capture.json', result, repo)
        print(json.dumps({'through_commit': result['through_commit'],
                          'selected': len(result['selected']), 'target': config['limit'],
                          'updates': len(result['later_versions']),
                          'nonnumeric_new_rows': len(result['nonnumeric_new_rows']),
                          'written': args.write,
                          'next': 'Review new candidates or due cases during CATO sessions; no background job.'}, indent=2))
    except (ValueError, subprocess.CalledProcessError, OSError, KeyError) as error:
        print(f'CANNOT-EVALUATE: {error}', file=sys.stderr)
        return 2
    return 0


if __name__ == '__main__':
    sys.exit(main())
