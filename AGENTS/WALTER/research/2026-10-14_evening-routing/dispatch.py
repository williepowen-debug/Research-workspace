"""Evening routing 2026-10-14 (walter-dc, Claude Code / Opus 5.5).

Applies one reviewed plan file (JSON list of signals) create-only:
BOARD file, per-recipient inbox/WALTER handoffs, route_log + delivery_log rows,
then regenerates BOARD/INDEX.md. No commit, push, pull, or recipient-state edit.

Usage: python3 dispatch.py PLAN.json            # dry run: prints what it would write
       python3 dispatch.py PLAN.json --apply    # writes (refuses on any collision)
"""
from pathlib import Path
import csv
import datetime
import json
import re
import subprocess
import sys

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[3]
DESK = ROOT / 'AGENTS/WALTER'
EXEMPT = {'CARL', 'RED', 'PROME', 'TERRY'}  # pull-complete: INFO via BOARD ID-diff only
NO_LANE = {'TERRY'}                          # TERRY lane closed 2026-09-14 (BOARD ID-diff even for ACTION)


def recipients(sig):
    for r in dict.fromkeys(sig['action'] + sig['info']):
        if r in NO_LANE:
            continue
        if r in EXEMPT and r not in sig['action']:
            continue
        yield r, ('ACTION' if r in sig['action'] else 'INFO')


def board_text(sig, stamp):
    q = lambda xs: '[' + ', '.join(json.dumps(x) for x in xs) + ']'
    hdr = [
        '---',
        f"signal_id: {sig['id']}",
        f"date: {sig['id'][6:10]}-{sig['id'][10:12]}-{sig['id'][12:14]}",  # ET signal date, matching the ID
        f"timestamp: {stamp}",
        f"dispatched: {stamp}",
        'source: WALTER',
        f"origin: {q(sig['origin'])}",
        f"domain: {sig['domain']}",
        f"cluster: {sig['cluster']}",
        f"entities: {q(sig['entities'])}",
        f"precedence: {sig['precedence']}",
        f"action: {q(sig['action'])}",
        f"to: {q(sig['action'])}",
        f"info: {q(sig['info'])}",
        f"confidence: {sig['confidence']}",
        f"confidence_language: {sig['confidence_language']}",
        'resources: 1',
        f"signal_type: {sig['signal_type']}",
        'safety_net: clear',
        'event_window: closed',
        f"word_count: {len(sig['body'].split())}",
        f"dispatch_note: {json.dumps(sig['dispatch_note'])}",
    ]
    for k in ('corrects', 'narrative_channel', 'anchor_unverified_as_of', 'cluster_secondary', 'case'):
        if sig.get(k):
            hdr.append(f"{k}: {sig[k] if isinstance(sig[k], str) else json.dumps(sig[k])}")
    hdr.append('---')
    src = '\n'.join(f'- {s}' for s in sig['sources'])
    return ('\n'.join(hdr) + f"\n\n# {sig['title']}\n\n{sig['body']}\n\n## Source / read scope\n\n{src}\n\n"
            f"Evidence: AGENTS/WALTER/research/2026-10-14_evening-routing/. Source date governs, not dispatch time.\n\n"
            f"## Requested action\n\n{sig['ask']}\n")


def handoff_text(sig, board_rel, stamp, recipient, role):
    ask = sig['ask'] if role == 'ACTION' else 'Information only; no recipient-directed task or new research commission.'
    why = sig.get('why', {}).get(recipient) or f"{recipient} is on the {sig['domain']} routing line for this item."
    return (f"# WALTER handoff — {sig['id']}\n\n**BOARD:** `{board_rel}`\n**Priority:** {sig['precedence']}\n"
            f"**Role:** {role}\n**From:** WALTER\n**Date:** {stamp}\n\n## Kernel\n\n{sig['title']}. {sig['body']}\n\n"
            f"## Why you got this\n\n{why}\n\n## Requested action\n\n{ask}\n\n## Confidence / caveats\n\n"
            f"Confidence {sig['confidence']:.2f}; source and measurement limits are in the kernel and the BOARD source section. "
            f"Only the recipient owner integrates and files this packet; a read-only helper must not consume or move it.\n")


def main():
    plan_path = Path(sys.argv[1])
    apply = sys.argv[2:] == ['--apply']
    plan = json.loads(plan_path.read_text())
    stamp = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    existing = {p.name[:18] for p in (ROOT / 'BOARD').glob('SIG-W-*.md')}
    writes, route, delivery = [], [], []
    for sig in plan:
        assert re.fullmatch(r'SIG-W-\d{8}-\d{3}', sig['id']), sig['id']
        assert sig['id'] not in existing, f"ID collision {sig['id']}"
        board = ROOT / 'BOARD' / f"{sig['id']}-{sig['slug']}.md"
        writes.append((board, board_text(sig, stamp)))
        route.append([stamp, sig['id'], '; '.join(sig['origin']), sig['title'], sig['precedence'],
                      ','.join(sig['action']), ','.join(sig['info']), f"{sig['confidence']:.2f}"])
        for r, role in recipients(sig):
            hp = ROOT / f"AGENTS/{r}/inbox/WALTER/{sig['id']}.md"
            writes.append((hp, handoff_text(sig, board.relative_to(ROOT), stamp, r, role)))
            delivery.append([stamp, sig['id'], r, role, 'CLAUDE_CODE', sig['precedence'], str(hp.relative_to(ROOT)),
                             'written_not_delivered_pending_push',
                             'walter-dc Claude Code/Opus 5.5; create-only; no recipient state edits. Delivered != consumed.'])
    collisions = [str(p) for p, _ in writes if p.exists()]
    assert not collisions, f'create-only collision: {collisions}'
    for p, _ in writes:
        print(('WRITE ' if apply else 'would write ') + str(p.relative_to(ROOT)))
    print(f'{len(plan)} signals, {len(delivery)} handoffs, stamp {stamp}')
    if not apply:
        return
    for p, text in writes:
        p.parent.mkdir(parents=True, exist_ok=True)
        with p.open('x') as f:
            f.write(text)
    for name, rows in (('route_log.tsv', route), ('delivery_log.tsv', delivery)):
        with (DESK / 'routed' / name).open('a', newline='') as f:
            csv.writer(f, delimiter='\t', lineterminator='\n').writerows(rows)
    r = subprocess.run(['python3', 'AGENTS/WALTER/tools/gen_board_index.py', '--write', 'BOARD/INDEX.md', '--cutover'],
                       cwd=ROOT, capture_output=True, text=True)
    print(r.stdout[-400:], r.stderr[-400:], 'index rc', r.returncode)
    (OUT / f'written-{plan_path.stem}.json').write_text(json.dumps(
        {'stamp': stamp, 'paths': [str(p.relative_to(ROOT)) for p, _ in writes]}, indent=2))


if __name__ == '__main__':
    main()
