#!/usr/bin/env python3
"""BASIS attestation check — boot 9f (built S54 2026-10-15, SCRATCH 6b).

`registry/basis-hashes.json` records the sha256 of every surface RED's boot and closeout
run on (its own charter and scripts, the root charter, WALTER's consumption spec, the
market-data CLI, the fleet correction/staleness instruments). Between RED's 9/14
attestation and 10/15, FIVE of those fleet surfaces changed and the attestation did not
move — nothing compared the file to the hash. This does.

USAGE
  basis_check.py --check                 compare live sha256 to the declared hashes;
                                         rc 0 all match · rc 1 CHANGED/MISSING (read the
                                         diff: `git log -p -- <path>`) · rc 2 cannot run
  basis_check.py --rehash --note "<why>" re-attest every path (+ any --add PATH), stamp
                                         declared_on = today, append a history entry.
                                         The ONLY writing path. A bare call, --help or an
                                         unknown flag refuses (argparse) and writes nothing.
A CHANGED surface is information, not an error: read what changed, decide whether a boot
step or a rule moved with it, then re-attest. Re-attesting without reading is the failure
this exists to catch (finding_header_edit_is_the_edit_most_mistaken_for_maintenance).
"""
import argparse
import datetime as dt
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
REG = ROOT / 'AGENTS' / 'RED' / 'registry' / 'basis-hashes.json'


def sha(path):
    p = ROOT / path
    return hashlib.sha256(p.read_bytes()).hexdigest() if p.exists() else None


def main():
    ap = argparse.ArgumentParser(description='RED BASIS hash attestation (boot 9f).')
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument('--check', action='store_true')
    g.add_argument('--rehash', action='store_true')
    ap.add_argument('--note', help='required with --rehash: why the attestation moves')
    ap.add_argument('--add', action='append', default=[], metavar='PATH', help='with --rehash: add a surface')
    a = ap.parse_args()
    if not REG.exists():
        print('BASIS 2 CANNOT RUN: %s missing' % REG.relative_to(ROOT))
        return 2
    reg = json.loads(REG.read_text(encoding='utf-8'))
    hashes = reg.get('hashes', {})
    if a.check:
        changed, missing = [], []
        for path, want in sorted(hashes.items()):
            got = sha(path)
            if got is None:
                missing.append(path)
            elif got != want:
                changed.append(path)
        print('BASIS declared %s — %d surface(s): %d match · %d CHANGED · %d MISSING'
              % (reg.get('declared_on', '?'), len(hashes), len(hashes) - len(changed) - len(missing), len(changed), len(missing)))
        for p in changed:
            print('  CHANGED  %s   (git log -p -- %s)' % (p, p))
        for p in missing:
            print('  MISSING  %s' % p)
        if changed or missing:
            print('BASIS 1 DRIFT — read each diff, then `basis_check.py --rehash --note "<why>"` at write-back')
            return 1
        print('BASIS 0 OK')
        return 0
    if not a.note or not a.note.strip():
        print('BASIS 2 REFUSED: --rehash needs --note "<why>" (a re-attestation without a reason is a header edit)')
        return 2
    for p in a.add:
        if sha(p) is None:
            print('BASIS 2 REFUSED: --add %s does not exist' % p)
            return 2
        hashes[p] = None
    today = dt.date.today().isoformat()
    moved = []
    for path in sorted(hashes):
        got = sha(path)
        if got is None:
            print('BASIS 2 REFUSED: %s missing — remove it from the registry by hand with a reason, never silently' % path)
            return 2
        if hashes[path] != got:
            moved.append(path)
        hashes[path] = got
    reg['hashes'] = dict(sorted(hashes.items()))
    reg['declared_on'] = today
    reg.setdefault('history', []).append({'date': today, 'note': a.note.strip(), 'moved': moved})
    REG.write_text(json.dumps(reg, indent=2, ensure_ascii=False, sort_keys=False) + '\n', encoding='utf-8')
    print('BASIS re-attested %s — %d surface(s), %d moved: %s' % (today, len(hashes), len(moved), ', '.join(moved) or 'none'))
    return 0


if __name__ == '__main__':
    sys.exit(main())
