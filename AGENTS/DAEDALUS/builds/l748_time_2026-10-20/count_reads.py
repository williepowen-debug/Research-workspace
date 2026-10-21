#!/usr/bin/env python3
"""L470 evidence extraction, not a freshness/coverage or strict-mode certificate."""
import csv
import datetime as dt
import hashlib
import json
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[4]
def git(*args):
    return subprocess.check_output(['git', '-C', str(ROOT), *args], text=True)

def snapshot(ref):
    roster = git('show', f'{ref}:PROME/ROSTER.md')
    manifest = git('show', f'{ref}:PROME/registry/READS.tsv')
    population, include = set(), False
    for line in roster.splitlines():
        if line.startswith('## '):
            include = line.startswith('## ACTIVE') or line.startswith('## TIER-2')
        if include and line.startswith('|'):
            name = line.split('|')[1].strip()
            if re.fullmatch('[A-Z][A-Z0-9_]+', name):
                population.add(name)
    rows = list(csv.DictReader([x for x in manifest.splitlines() if x and not x.startswith('#')], delimiter='\t'))
    if any(None in row or any(v is None for v in row.values()) for row in rows):
        raise ValueError('malformed manifest: cannot count')
    attestations = [r for r in rows if r['row_kind'] == 'ATTESTATION'
                    and r['reader'] == r['declared_by'] and r['mode'] == 'manifest-complete']
    names = {r['reader'] for r in attestations}
    return dict(revision=git('rev-parse',ref).strip(),
                manifest_sha256=hashlib.sha256(manifest.encode()).hexdigest(),
                roster_sha256=hashlib.sha256(roster.encode()).hexdigest(),
                active_tier2=sorted(population), population_count=len(population),
                signed_attestation_rows=len(attestations), signed_desks=sorted(names),
                eligible_signed_desks=sorted(names & population), eligible_count=len(names & population),
                outside_population=sorted(names-population),
                condition_met_even_using_all_signed_desks=len(names)>=30,
                limits='Presence upper bound only; duplicates, freshness, BASIS and read coverage not certified.')

if __name__ == '__main__':
    import argparse
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--head', required=True, help='fixed full commit id')
    args=ap.parse_args()
    cutoff=git('rev-list','-1','--before=2026-10-16T00:00:00-04:00',args.head).strip()
    print(json.dumps(dict(observed_at=dt.datetime.now(dt.timezone.utc).isoformat(),
        cutoff_method='Last reachable commit selected by git rev-list --before ET end October15; not an actual PR#8 receipt or authenticated wall-clock snapshot.',
        ruled_threshold=30, ruled_denominator=37,
        cutoff=snapshot(cutoff), current=snapshot(args.head)), indent=2))
