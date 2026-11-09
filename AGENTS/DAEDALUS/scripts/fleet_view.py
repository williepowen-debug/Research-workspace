#!/usr/bin/env python3
"""WQ-655: generated evidence view; no authority, boot hook or source writes.

Run from any cwd. Default prints exceptions; --full appends the same collection's
roster. --output explicitly selects the sole file written. No output means stdout.
"""
import sys
sys.dont_write_bytecode = True
import argparse
import os
import datetime as dt
import re
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[3]
sys.path[:0] = [str(ROOT / 'PROME/tools'), str(ROOT / 'scripts')]
import desk_activity as activity
import docket_view
import fleet_dashboard as dashboard
import inbox_census
import orch_log
import session_bridge
import spawn_list as sl
import spawn_slate as slate


def git(root, *args):
    return activity.git(root, *args).decode('utf-8', 'replace').strip()


def owned(owner, path):
    base = activity.desk_path(owner) + '/'
    return path.startswith(base) and not path.startswith(base + 'inbox/')


def commits(root, head, limit=2000):
    raw = git(root, 'log', head, '--no-merges', '-n', str(limit),
              '--format=%x1e%H%x09%cI%x09%s', '--name-only')
    result = []
    for header, paths in sl.parse_log_records(raw):
        sha, stamp, subject = header.split('\t', 2)
        result.append(dict(sha=sha, stamp=stamp, subject=subject, paths=paths))
    return result


def attribution(owner, history):
    for row in history:
        # The donor accepts strong prefixes even with foreign-only paths. Require
        # an actual owned path here, and do not promote an inbound packet to work.
        paths = [p for p in row['paths'] if owned(owner, p)]
        if paths and re.match(rf'^{re.escape(owner)}(?:\s*:|\s*→|\s*->)', row['subject']) and sl.attributed(owner, row['subject'], row['paths']):
            substantive = [p for p in paths if Path(p).name == 'STATUS.md' or p.endswith('.tsv')]
            return dict(sha=row['sha'], stamp=row['stamp'], paths=paths,
                        substantive=substantive)
    return None


def scaffold(path):
    if path.name not in ('PROTOCOL.md', 'RECEIPT.md'):
        return False
    first = path.read_text().splitlines()[0:1]
    return bool(first and (path.name == 'PROTOCOL.md' and first[0] == '# Mail Processing Protocol'
                          or path.name == 'RECEIPT.md' and first[0].startswith('# Inbox Processing Receipt')))


def inbox(root, owner):
    _, top, lanes = inbox_census.census(owner)
    if top is None:
        raise ValueError('inbox absent')
    base = Path(activity.desk_path(owner)) / 'inbox'
    paths = [base / p for p in top] + [base / lane / p for lane, names in lanes.items() for p in names]
    # Donor's contract is one lane deep. Refuse a false-empty result for deeper mail.
    deeper = [p for p in (root / base).glob('*/*/') if p.is_dir() and 'processed' not in p.relative_to(root / base).parts]
    if deeper:
        raise ValueError('nested inbox beyond one lane: coverage UNKNOWN')
    return [str(p) for p in paths if not scaffold(root / p)]


def collect(root=ROOT, now=None, inventory=None):
    root = Path(root).resolve()
    now = now or dt.datetime.now(dt.timezone.utc)
    today = now.astimezone(ZoneInfo('America/New_York')).date()
    stamp = now.isoformat(timespec='seconds')
    data = dict(stamp=stamp, head=git(root, 'rev-parse', 'HEAD'), desks={},
                due=[], returns=[], blockers=[], conflicts=[], unknown=[], coverage=[])
    source_text = {}
    def read(path):
        text = (root / path).read_text()
        source_text[path] = text
        return text
    def row(section, message, source, when=stamp):
        data[section].append(dict(message=message, source=source, stamp=when))
    old = dashboard.read, inbox_census.root, sl.ROOT
    dashboard.read = read
    inbox_census.root = lambda: str(root)
    sl.ROOT = root
    try:
        try:
            roster = read('PROME/ROSTER.md')
            classes = slate.roster_classes(roster)
            parsed = dashboard.parse_roster()
            for group, label in zip(parsed, ('ACTIVE', 'TIER-2', 'DORMANT')):
                for name, _ in group:
                    classes.setdefault(name, label)
            if not classes or not any(parsed):
                raise ValueError('roster parser found no core roster')
        except (OSError, ValueError) as exc:
            classes = {}
            row('unknown', f'ROSTER UNKNOWN: {exc}', 'PROME/ROSTER.md')
        try:
            history = commits(root, data['head'])
            row('coverage', f'Git attribution scans {len(history)} most recent non-merge commits at pinned HEAD; older work UNKNOWN. STATUS/TSV touches are path evidence only, semantic substance UNKNOWN.', data['head'])
        except (OSError, ValueError) as exc:
            history = []
            row('unknown', f'Git history UNKNOWN: {exc}', 'HEAD')
        for owner, cls in sorted(classes.items()):
            base = activity.desk_path(owner)
            desk = dict(cls=cls, commit=attribution(owner, history), inbox=None, sessions=[], orch=[], brief='header date UNKNOWN', pending=None)
            data['desks'][owner] = desk
            # Archived/tool/off-fleet entries remain visible without inventing inbox obligations.
            if cls not in ('ACTIVE', 'TIER-2', 'SPECIAL'):
                continue
            try:
                desk['inbox'] = inbox(root, owner)
                for path in desk['inbox']:
                    row('returns', f'{owner}: pending consumption candidate (presence, not unread proof)', path)
            except (OSError, ValueError) as exc:
                row('unknown', f'{owner}: inbox UNKNOWN: {exc}', base + '/inbox/')
            try:
                desk['pending'] = activity.pending(root, base)
            except (OSError, ValueError) as exc:
                row('unknown', f'{owner}: working-tree coverage UNKNOWN: {exc}', base)
            brief = base + '/NEXUS_BRIEF.md'
            if (root / brief).is_file():
                try:
                    text = read(brief)
                    for n, line in enumerate(text.splitlines()[:20], 1):
                        if re.match(r'^\*?\*?(?:As of|Updated|Date|Last [Uu]pdated)\b', line, re.I):
                            date = re.search(r'20\d\d-\d\d-\d\d', line)
                            if date:
                                desk['brief'] = f'{date[0]} header only; scope/freshness UNKNOWN ({brief}:{n})'
                            break
                except (OSError, ValueError):
                    pass
        # Due work includes covered rows; coverage never discharges an obligation.
        docket = gates = ''
        due_rows = []
        try:
            docket = read('PROME/DOCKET.tsv')
            docket_view.load_docket(root / 'PROME/DOCKET.tsv', source_text=docket)
            for r in sl.open_records(docket, today):
                source = f"PROME/DOCKET.tsv:{r['line']}"
                if r['status'] == 'undated':
                    row('unknown', f"{r['key']} {r['owner_cell']}: open obligation, due date UNKNOWN", source)
                elif r['status'] in ('today', 'overdue'):
                    due = dt.date.fromisoformat(r['due'])
                    due_rows.append((sl.Row(r['key'], r['due'], (today-due).days, r['owner_token'], 'UNKNOWN', '', '', ''), source, r['owner_cell'], r['covered']))
                if re.match(r'^\s*(?:PENDING|★).*?\bBLOCKED\b', r['state_cell'], re.I):
                    row('blockers', f"{r['key']} {r['owner_cell']}: source marks BLOCKED; read row for dependency", source)
        except (OSError, ValueError, docket_view.DocketError) as exc:
            row('unknown', f'DOCKET UNKNOWN: {exc}', 'PROME/DOCKET.tsv')
        try:
            gates = read('PROME/GATES.tsv')
            diagnostics = []
            gate_rows = dashboard.parse_gates(today, diagnostics=diagnostics)
            if diagnostics:
                raise ValueError('; '.join(diagnostics))
            raw = [(n, l.split('\t')) for n, l in enumerate(gates.splitlines(), 1) if l.strip() and not l.startswith('#')]
            header = raw[0][1]
            cells = {c[0]: (n, dict(zip(header, c))) for n, c in raw[1:]}
            for r in gate_rows:
                n, c = cells[r['gate']]
                source = f'PROME/GATES.tsv:{n}'
                if r['kind'] == 'crit':
                    row('blockers', f"{r['gate']} {r['owner']}: FIRED-UNEXECUTED", source)
                if r['kind'] != 'live':
                    continue
                date = re.match(r'\d{4}-\d{2}-\d{2}', c.get('review_by', ''))
                if not date:
                    row('unknown', f"{r['gate']} {r['owner']}: LIVE review date UNKNOWN", source)
                elif dt.date.fromisoformat(date[0]) <= today:
                    due_rows.append((sl.Row('G:'+r['gate'], date[0], (today-dt.date.fromisoformat(date[0])).days, sl.owner_token(r['owner']), 'UNKNOWN', '', '', ''), source, r['owner'], False))
        except (OSError, ValueError, KeyError, IndexError) as exc:
            row('unknown', f'GATES UNKNOWN: {exc}', 'PROME/GATES.tsv')
        ev = slate.Evidence(data['head'], None)
        for r, source, owners, covered in due_rows:
            try:
                detail = slate.details([r], docket, gates)[0]
                # No ID is assumed unique: only exact row-key citations qualify here.
                from collections import Counter
                counts = Counter()
                for text in (docket, gates):
                    for pattern in slate.ID_PATTERNS:
                        counts.update(re.findall(pattern, text))
                token, notes, artifact = slate.precheck(detail, ev, counts)
                if token == 'UNCHECKED' or any('CANNOT-EVALUATE' in n or 'older returns' in n for n in notes):
                    token += ' (coverage incomplete: UNKNOWN)'
                row('due', f'{r.key} · {owners} · due {r.due} · covered={covered} · {token}; first-owner prefix-based citation; owned-work attribution UNKNOWN, never completion', source + (f'; {artifact}' if artifact else ''))
            except (OSError, ValueError, IndexError, KeyError) as exc:
                row('due', f'{r.key} · {owners} · due {r.due} · citation UNKNOWN: {exc}', source)
        # ORCH ledger claims are events, never inferred present activity.
        try:
            text = read('PROME/state/ORCH_LOG.tsv')
            lines = [(n, l.split('\t')) for n, l in enumerate(text.splitlines(), 1) if l.strip() and not l.startswith('#')]
            if lines[0][1] != orch_log.COLS:
                raise ValueError('ORCH header mismatch')
            rows = []
            for n, fields in lines[1:]:
                problems = orch_log.validate_line(fields, n)
                if problems:
                    raise ValueError('; '.join(problems))
                rows.append(fields)
            closed = orch_log._closed_inflight(rows)
            historical = []
            for i, (n, fields) in enumerate(lines[1:]):
                date, owner, _, touch = fields[:4]
                source = f'PROME/state/ORCH_LOG.tsv:{n}'
                if owner in data['desks'] and date == today.isoformat():
                    data['desks'][owner]['orch'].append(f'{date} {touch} ({source})')
                if orch_log._is_inflight(fields) and i not in closed:
                    if date < today.isoformat():
                        historical.append(source)
                    else:
                        row('unknown', f'{owner}: unreconciled ORCH in-flight claim, event {date}/{touch}; actual activity UNKNOWN', source)
            if historical:
                row('unknown', f'{len(historical)} historical unreconciled ORCH in-flight claims before {today}; not current activity. Inspect canonical ledger; first/last pointers supplied.', historical[0] + '; ' + historical[-1])
            row('coverage', 'ORCH events retained with date/key; canonical in-flight closure matching reused. CLOSE is a recorded claim, not a current-session verdict.', 'PROME/state/ORCH_LOG.tsv')
        except (OSError, ValueError, IndexError) as exc:
            row('unknown', f'ORCH UNKNOWN: {exc}', 'PROME/state/ORCH_LOG.tsv')
        try:
            inv = inventory() if inventory else session_bridge.inventory()
            for process in inv.get('processes', []):
                for owner, desk in data['desks'].items():
                    if process.get('cwd') == str(root / activity.desk_path(owner)):
                        desk['sessions'].append(f"{process.get('runtime')} process observed {inv.get('observed_at', stamp)}")
            for session in inv.get('claude', []) if isinstance(inv.get('claude'), list) else []:
                for owner, desk in data['desks'].items():
                    if session.get('cwd') == str(root / activity.desk_path(owner)):
                        desk['sessions'].append(f"Claude session {session.get('id') or session.get('sessionId')} observed {inv.get('observed_at', stamp)}")
            row('unknown', f"Current turn activity UNKNOWN for all desks. Session discovery: {inv.get('coverage', 'UNKNOWN')}; Claude inventory {'unavailable: '+inv['error'] if inv.get('error') else 'observed'}; Codex native inventory {inv.get('codex', {}).get('state', 'UNKNOWN')}. Absence is not inactivity.", 'PROME/tools/session_bridge.py', inv.get('observed_at', stamp))
        except (OSError, ValueError) as exc:
            row('unknown', f'Session discovery UNKNOWN: {exc}', 'PROME/tools/session_bridge.py')
        # Bounded same-day foreign-path changes are coordination candidates.
        for c in history:
            match = re.match(r'^([A-Z][A-Z0-9]+)(?:\s*:|\s*->|\s*→)', c['subject'])
            if not match or dt.datetime.fromisoformat(c['stamp']).astimezone(ZoneInfo('America/New_York')).date() != today:
                continue
            author = match[1]
            foreign = [p for p in c['paths'] if re.match(r'^AGENTS/[^/]+/', p) and not p.startswith(activity.desk_path(author) + '/')]
            if foreign:
                names = git(root, 'show', '--format=', '--name-status', '--find-renames', c['sha'])
                renames = [l for l in names.splitlines() if l.startswith('R') and any(p in l.split('\t')[1:] for p in foreign)]
                if renames:
                    row('conflicts', f'{author}: foreign-desk rename(s), coordination candidate; permission/intent UNKNOWN: ' + '; '.join(renames), c['sha'], c['stamp'])
        row('coverage', 'Inbox presence includes committed and untracked packets, one lane deep; processed/, dotfiles, README* and recognized FERT protocol/receipt scaffolds excluded. Presence is not proof of unread state.', 'PROME/tools/inbox_census.py')
        row('coverage', 'BOARD dispatch/consumption remains a separate surface; no board receipt is inferred from inbox presence. Positions, conviction, market prose, roster launch permissions and boot policy are not projected.', 'PROME/tools/board_scan.py; PROME/ROSTER.md')
        row('coverage', 'Due citations reuse spawn_slate (bounded 200 owner commits, first owner); RETURN FOUND is only a pointer, NO CITING RETURN is limited to that search. Working tree inputs and pinned committed evidence may differ.', 'PROME/tools/spawn_slate.py')
        for path, before in source_text.items():
            try:
                if (root / path).read_text() != before:
                    row('unknown', 'Source changed during collection; mixed snapshot UNKNOWN', path)
            except OSError:
                row('unknown', 'Source disappeared during collection; consistency UNKNOWN', path)
        if git(root, 'rev-parse', 'HEAD') != data['head']:
            row('unknown', 'HEAD changed during collection; Git evidence stays pinned, working-tree consistency UNKNOWN', data['head'])
        # Recheck inbox listings and pending paths, not file mtimes as activity.
        for owner, desk in data['desks'].items():
            if desk['inbox'] is not None:
                try:
                    if inbox(root, owner) != desk['inbox'] or activity.pending(root, activity.desk_path(owner)) != desk['pending']:
                        row('unknown', f'{owner}: inbox/worktree changed during collection; consistency UNKNOWN', activity.desk_path(owner))
                except (OSError, ValueError):
                    row('unknown', f'{owner}: consistency recheck unavailable', activity.desk_path(owner))
    finally:
        dashboard.read, inbox_census.root, sl.ROOT = old
    return data


def cell(value):
    return str(value).replace('|', '\\|').replace('\n', ' ').replace('\r', ' ')


def render(data, full=False):
    out = ['# Fleet evidence view — generated, never hand-edit', '',
           f"Observed {data['stamp']}; Git snapshot `{data['head']}`. Read-only evidence, no authority or launch decisions.", '']
    for key, title in [('due', 'Due work'), ('returns', 'Pending consumption'), ('blockers', 'Recorded blockers'), ('conflicts', 'Coordination candidates'), ('unknown', 'Consequential unknowns'), ('coverage', 'Coverage')]:
        out += ['## ' + title, '', '| Observed / event time | Evidence | Source |', '|---|---|---|']
        for r in data[key]:
            out.append(f"| {cell(r['stamp'])} | {cell(r['message'])} | {cell(r['source'])} |")
        if not data[key]:
            out.append(f"| {data['stamp']} | No matches in checked inputs; see UNKNOWN and coverage before treating as clean | {data['head']}; PROME/DOCKET.tsv; PROME/GATES.tsv; PROME/state/ORCH_LOG.tsv |")
        out.append('')
    if full:
        out += ['## Full roster — same collection', '', '| Observed | Desk / class | Commit attribution / substance | Inbox / dirty paths | Session / ORCH evidence | Brief header | Source |', '|---|---|---|---|---|---|---|']
        for owner, d in data['desks'].items():
            c = d['commit']
            commit = f"{c['sha'][:12]} {c['stamp']} prefix + owned path; STATUS/TSV touches: {', '.join(c['substantive']) or 'none'}; semantic substance UNKNOWN" if c else 'No attributable commit in bounded scan; substantive work UNKNOWN'
            mail = 'UNKNOWN / not collected for class' if d['inbox'] is None else str(len(d['inbox'])) + ' pending candidates'
            dirty = 'UNKNOWN' if d['pending'] is None else str(len(d['pending']))
            sessions = '; '.join(d['sessions'] + d['orch']) or 'No observed session/event in covered sources'
            out.append('| ' + ' | '.join(map(cell, [data['stamp'], owner+' / '+d['cls'], commit, mail+'; dirty paths '+dirty, sessions+'; current activity UNKNOWN', d['brief'], 'PROME/ROSTER.md; '+activity.desk_path(owner)+(('; commit '+c['sha']) if c else '')])) + ' |')
    return '\n'.join(out) + '\n'


def write_output(path, result, root=ROOT):
    path = Path(path)
    allowed = {root / 'PROME/state/FLEET.md', root / 'PROME/state/FLEET_FULL.md'}
    if path.is_symlink() or path.resolve() not in allowed:
        raise ValueError('output must be a regular generated fleet Markdown path')
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_TRUNC | os.O_NOFOLLOW, 0o644)
    with os.fdopen(fd, 'w') as stream:
        stream.write(result)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--full', action='store_true')
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    # Prevent accidental source replacement: outputs must be generated fleet Markdown.
    if args.output and (args.output.resolve().parent != ROOT / 'PROME/state' or not re.fullmatch(r'FLEET(?:_FULL)?\.md', args.output.name)):
        parser.error('--output must be PROME/state/FLEET.md or FLEET_FULL.md')
    data = collect()
    result = render(data, args.full)
    if args.output:
        write_output(args.output, result)
    else:
        print(result, end='')
    return 0


if __name__ == '__main__':
    sys.exit(main())
