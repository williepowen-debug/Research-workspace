#!/usr/bin/env python3
"""Read-only staged WALTER archive guard; exact-byte moves only pass automatically.

Examines staged deletions without Git's rename heuristic. Each deleted WALTER
blob needs a same-blob staged addition within WALTER. A split/edited move needs
manual split_verify evidence and is deliberately reported for review, never
automatically waved through. Unstaged deletions and foreign paths are not covered.
"""
import subprocess
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]


def check(repo=REPO):
    def git(*args):
        return subprocess.check_output(['git', *args], cwd=repo)
    raw = git('diff', '--cached', '--no-renames', '--name-status', '-z').decode().split('\0')
    pairs = [(raw[i], raw[i + 1]) for i in range(0, len(raw) - 1, 2)]
    additions = [p for status, p in pairs if status == 'A' and p.startswith('AGENTS/WALTER/')]
    blobs = [git('rev-parse', ':' + p).strip() for p in additions]
    failures, checked = [], 0
    for status, path in pairs:
        if status != 'D' or not path.startswith('AGENTS/WALTER/'):
            continue
        checked += 1
        blob = git('rev-parse', 'HEAD:' + path).strip()
        if blob not in blobs:
            failures.append(path)
        else:
            blobs.remove(blob)  # Require a distinct addition for each deletion.
    return failures, checked


if __name__ == '__main__':
    try:
        failures, checked = check()
    except (OSError, subprocess.CalledProcessError, IndexError, UnicodeError) as exc:
        print(f'ARCHIVE CHECK UNAVAILABLE: {exc}')
        raise SystemExit(2)
    print(f'ARCHIVE CHECK: {checked} staged WALTER deletion(s), {len(failures)} need review')
    for path in failures:
        print(f'UNPAIRED OR EDITED: {path}; supply exact archive addition or split_verify proof')
    raise SystemExit(bool(failures))
