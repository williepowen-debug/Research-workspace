#!/usr/bin/env python3
"""Check WALTER's reviewed boot basis against current bytes, including dirty edits.

Read-only. Exit 1 on a missing/changed/undeclared basis; re-attestation requires
reviewing the changed operation and updating READS plus the hash record manually.
This checks declared coverage, not whether a boot or market scan was executed.
"""
import hashlib
import json
import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]


def check(repo=REPO):
    try:
        manifest = repo / 'PROME/registry/READS.tsv'
        paths = {f[2] for line in manifest.read_text().splitlines()
                 if len(f := line.split('\t')) >= 3 and f[:2] == ['BASIS', 'WALTER']}
        hashes = json.loads((repo / 'AGENTS/WALTER/registry/boot_basis_hashes.json').read_text())
        if not isinstance(hashes, dict) or any(
                not isinstance(path, str) or not isinstance(value, str)
                or not re.fullmatch(r'[0-9a-f]{64}', value)
                for path, value in hashes.items()):
            return ['BASIS UNAVAILABLE: expected a path-to-SHA256 object'], 0
        failures = [f'BASIS SET MISMATCH: {p}' for p in sorted(paths ^ hashes.keys())]
        for path in sorted(paths & hashes.keys()):
            p = repo / path
            if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest() != hashes[path]:
                failures.append(f'REVIEW REQUIRED: {path}')
        if not paths:
            failures.append('EMPTY BASIS: coverage unavailable')
        return failures, len(paths)
    except (OSError, ValueError, TypeError) as exc:
        return [f'BASIS UNAVAILABLE: {exc}'], 0


if __name__ == '__main__':
    failures, count = check()
    print('\n'.join(failures) if failures else f'BOOT BASIS MATCH: {count} declared paths; execution not certified')
    raise SystemExit(bool(failures))
