#!/usr/bin/env python3
"""Read-only WALTER closeout check. No fetch, writes, or owner-state inference.

Checks the explicit receipt in LAST_COMPLETION and duplicate status claims.
A pass is scoped to these checks and the local origin ref, not arbitrary prose,
remote freshness, semantic owner integration, or all obligations being complete.
"""
import csv
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[3]
BASE = 'AGENTS/WALTER/'
START = '<!-- CLOSEOUT_RECEIPT_JSON\n'
END = '\nEND_CLOSEOUT_RECEIPT -->'


def git(repo, *args):
    result = subprocess.run(['git', *args], cwd=repo, capture_output=True, text=True)
    if result.returncode:
        raise ValueError('git check unavailable: ' + ' '.join(args[:2]))
    return result.stdout.strip()


def inspect(repo=ROOT):
    problems = []
    last = (repo / BASE / 'LAST_COMPLETION.md').read_text()
    status = (repo / BASE / 'STATUS.md').read_text()
    if last.count(START) != 1 or last.count(END) != 1:
        raise ValueError('need exactly one explicit closeout receipt')
    receipt = json.loads(last.split(START)[1].split(END)[0])
    if receipt['schema'] != 1:
        raise ValueError('unsupported receipt schema')
    asof = datetime.fromisoformat(receipt['as_of'].replace('Z', '+00:00'))
    if asof.tzinfo is None or asof > datetime.now(timezone.utc):
        raise ValueError('receipt needs a non-future timezone-aware observation time')
    datetime.strptime(receipt['next_review'], '%Y-%m-%d')
    for heading in ('FOLLOW-UP', 'OPEN DESIGN DECISIONS', 'WILL_NEEDS'):
        if last.count('## '+heading+'\n') != 1:
            problems.append('missing/duplicate obligation section: '+heading)
    if 'LAST_COMPLETION.md' not in status:
        problems.append('STATUS must link to the canonical obligation list')
    # This surface must not restate volatile publication/delivery/dated task state.
    rules = [r'\b(?:pending[- ]push|await(?:s|ing) (?:safe )?(?:sync|push)|uncommitted|local.only)\b',
             r'\bon origin\b|\b(?:commit|repair|implementation|work|closeout|handoff)[^\n.]{0,90}\b(?:pushed|published)\b',
             r'\b(?:handoffs?|deliveries|copies)\b[^\n.]{0,90}\b(?:held|delivered|pending|await)\b',
             r'\b\d+\s*(?:of\s*|/)\s*\d+\s*(?:handoffs?|deliver)',
             r'\b(?:remaining work|next review|follow.up)\s*:',
             r'\b(?:commit|implementation)[^\n.]{0,35}\bis local\b']
    for number, line in enumerate(status.splitlines(), 1):
        if any(re.search(rule, line, re.I) for rule in rules):
            problems.append(f'STATUS:{number}: duplicate volatile claim; move to LAST_COMPLETION/dated receipt')
    origin = git(repo, 'rev-parse', 'origin/master')
    commits = receipt['publication']
    if not commits:
        raise ValueError('publication scope must name at least one commit')
    for item in commits:
        commit = item['commit']
        if not re.fullmatch(r'[0-9a-f]{7,40}', commit):
            raise ValueError('publication requires an exact commit hash')
        git(repo, 'rev-parse', '--verify', commit+'^{commit}')
        rc = subprocess.run(['git','merge-base','--is-ancestor',commit,origin],cwd=repo).returncode
        if rc not in (0,1): raise ValueError('ancestry unavailable')
        if item['state'] not in ('published','pending'):
            raise ValueError('publication state must be published or pending')
        actual = 'published' if rc == 0 else 'pending'
        if actual != item['state']:
            problems.append(f'{commit}: claimed {item["state"]}, origin proves {actual}')
    delivery = receipt['delivery']
    day = delivery['signal_date']
    datetime.strptime(day, '%Y%m%d')
    with (repo / BASE / 'routed/delivery_log.tsv').open() as handle:
        reader = csv.DictReader(handle, delimiter='\t')
        rows = list(reader)
    if any(None in r or None in r.values() for r in rows):
        raise ValueError('delivery ledger malformed')
    selected = [r for r in rows if r['signal_id'].startswith('SIG-W-'+day+'-')]
    pairs = [(r['signal_id'],r['recipient']) for r in selected]
    if len(pairs) != len(set(pairs)):
        raise ValueError('duplicate selected signal/recipient pair')
    tree = set(git(repo,'ls-tree','-r','--name-only',origin).splitlines())
    proven = 0
    for row in selected:
        path = row['handoff_path']
        seen = path in tree or bool(git(repo,'log',origin,'-1','--format=%H','--',path))
        if seen: proven += 1
        if seen != (row['written_state'] == 'delivered'):
            problems.append(f'{row["signal_id"]}/{row["recipient"]}: ledger/origin disagree; reconcile or investigate')
    if type(delivery['total']) is not int or type(delivery['delivered']) is not int:
        raise ValueError('delivery counts must be integers')
    if (len(selected),proven) != (delivery['total'],delivery['delivered']):
        problems.append(f'delivery receipt mismatch: actual {proven}/{len(selected)}')
    # Review evidence is not an automated inference that an owner acted.
    if receipt['owner_review']['scope'] != 'manual evidence review; no automatic completion':
        raise ValueError('owner review must explicitly retain manual semantic review')
    evidence = receipt['owner_review']['evidence']
    if not evidence: raise ValueError('owner evidence pointers required')
    for item in evidence:
        path = Path(item['path'])
        if path.is_absolute() or '..' in path.parts:
            raise ValueError('owner evidence must be a repo-relative path')
        raw = (repo/path).read_bytes()
        if hashlib.sha256(raw).hexdigest() != item['sha256']:
            problems.append(f'owner evidence changed: {path}; reassess carried obligations')
    return problems, {'as_of':receipt['as_of'],'origin_ref':origin,
                      'delivery_scope':day,'delivered':proven,'total':len(selected),
                      'next_review':receipt['next_review'],
                      'limits':'Local origin ref only; fetch separately. Owner semantics and unstructured prose require human review.'}


if __name__ == '__main__':
    try:
        findings, result = inspect()
        print(json.dumps({'status':'REVIEW' if findings else 'PASS','findings':findings,**result},indent=2))
        raise SystemExit(bool(findings))
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print('UNKNOWN: closeout evidence unavailable: '+str(exc))
        raise SystemExit(2)
