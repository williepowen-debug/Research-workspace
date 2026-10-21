#!/usr/bin/env python3
"""Read-only calendar/DOCKET candidate correspondence, not semantic or delivery proof.

Production acceptance: builds/calendar_coverage_2026-10-20/production.json.
Contract: design/2026-10-20_CALENDAR_COVERAGE_ACCEPTANCE.md.
Default includes DAEDALUS; explicit --ledger narrows scope and prints that fact.
rc 0 complete nonempty correspondence; 1 unmatched candidates; 2 cannot assess.
Baseline and wiring disposition: builds/calendar_coverage_2026-10-20/RESULT.md.
"""
import argparse
import csv
import datetime as dt
import hashlib
import io
import json
import re
import sys
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / 'scripts'))
import docket_view

PATTERNS = ('AGENTS/*/CALENDAR.md', 'AGENTS/*/docket/CATALYSTS.tsv',
            'AGENTS/*/data/CATALYSTS.tsv', 'AGENTS/*/workbook/CATALYSTS.tsv')
STOP = set('the a an of in on at and or for to by with from as is are will next first '
           'last new q1 q2 q3 q4 fy report release results earnings quarterly annual '
           'quarter year review read check session follow up update date event calendar '
           'scheduled expected confirmed am pm et utc jst est edt after before close '
           'october november december january february march april may june july august '
           'september oct nov dec jan feb mar apr jun jul aug sep sept '
           'monday tuesday wednesday thursday friday saturday sunday '
           'mon tue tues wed thu thur thurs fri sat sun'.split())
TERMINAL = re.compile(r'^(?:RESOLVED|DONE|CLOSED|CANCELLED|CANCELED|OCCURRED|FIRED|SUPERSEDED|ARCHIVED)(?:\b|[-_])', re.I)
DATEISH = re.compile(r'\d{4}-\d{1,2}|\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s*\d|\b\d{1,2}/\d{1,2}\b', re.I)
RELATIVE = re.compile(r'\b(?:today|tomorrow|yesterday|tonight|(?:next|this|last)[ -](?:week|month|quarter|year|session|Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday))\b', re.I)


def plain(s):
    return re.sub(r'[*`]', '', s).strip()


def point_date(s):
    s = plain(s)
    m = re.fullmatch(r'(\d{4}-\d{2}-\d{2})(?:\s+\((?:Mon|Tue|Wed|Thu|Fri|Sat|Sun)[a-z]*\))?(?:\s+\d{1,2}:\d{2}(?:\s*[APap][Mm])?(?:\s+[A-Z]{2,4})?)?', s)
    if not m:
        raise ValueError('unsupported date shape (only explicit ISO point dates, optional weekday/time)')
    return dt.date.fromisoformat(m.group(1))


def terms(s, desk):
    return {t for t in re.findall(r'[a-z][a-z0-9]*(?:-[a-z0-9]+)*', s.lower())
            if len(t) > 1 and t not in STOP and t != desk.lower()}


def owners(s):
    # Parenthetical rationale is not owner identity. Repeat handles nested pairs.
    while re.search(r'\([^()]*\)', s):
        s = re.sub(r'\([^()]*\)', '', s)
    return set(re.findall(r'\b[A-Z][A-Z0-9_-]+\b', s))


def md_cells(line):
    return [c.strip().replace(r'\|', '|') for c in re.split(r'(?<!\\)\|', line.strip().strip('|'))]


def header(cells):
    names = [plain(c).lower().strip() for c in cells]
    dates = [i for i, n in enumerate(names) if n in ('date', 'when', 'date / check-by', 'date / window')]
    events = [i for i, n in enumerate(names) if n in ('event', 'what', 'catalyst', 'existing event')]
    if len(dates) == len(events) == 1 and len(set(names)) == len(names):
        return dates[0], events[0], names.index('status') if 'status' in names else None
    return None


def parse_ledger(text, path):
    """Return row records including explicit exclusions and failures; no silent data drops."""
    lines = text.splitlines()
    if not lines:
        return [{'line': 0, 'issue': 'empty ledger'}]
    if re.match(r'^#?\s*FROZEN\b', lines[0], re.I):
        return [{'line': 1, 'excluded': 'FROZEN first-line banner'}]
    out = []
    if path.suffix.lower() == '.tsv':
        # Feed physical lines; csv.reader reports ending line, so start line is retained.
        reader = csv.reader(io.StringIO(text), delimiter='\t', strict=True)
        h = None
        width = None
        previous = 0
        try:
            for cells in reader:
                n = previous + 1
                previous = reader.line_num
                if not cells or (len(cells) == 1 and (not cells[0].strip() or cells[0].startswith('#'))):
                    continue
                if h is None:
                    h = header(cells)
                    if h is None:
                        out.append({'line': n, 'issue': 'unsupported TSV header'})
                        return out
                    width = len(cells)
                    continue
                if len(cells) != width:
                    out.append({'line': n, 'issue': f'ragged TSV: {len(cells)} cells, expected {width}'})
                else:
                    out.append(row(cells, h, n))
        except csv.Error as exc:
            out.append({'line': previous + 1, 'issue': f'CSV parse error: {exc}'})
        return out or [{'line': 0, 'issue': 'no data rows'}]
    h = None
    width = None
    history_level = None
    for n, line in enumerate(lines, 1):
        heading = re.match(r'^(#{1,6})\s+(.+)', line)
        if heading:
            level = len(heading[1])
            if history_level is not None and level <= history_level:
                history_level = None
            if re.match(r'^(RESOLVED|HISTORY|HISTORICAL|ARCHIVE|COMPLETED)\b', plain(heading[2]), re.I):
                history_level = level
            h = None
            if DATEISH.search(heading[2]) or RELATIVE.search(heading[2]):
                out.append({'line': n, 'excluded': 'dated heading in resolved/history section'} if history_level is not None
                           else {'line': n, 'issue': 'dated or relative heading outside supported tables'})
            continue
        if line.lstrip().startswith('|'):
            cells = md_cells(line)
            if all(re.fullmatch(r':?-+:?', c.replace(' ', '')) for c in cells):
                continue
            found = header(cells)
            if found:
                h, width = found, len(cells)
                continue
            if history_level is not None:
                out.append({'line': n, 'excluded': 'resolved/history section'})
            elif h is None:
                out.append({'line': n, 'issue': 'unsupported Markdown table/header'})
            elif len(cells) != width:
                out.append({'line': n, 'issue': f'ragged Markdown: {len(cells)} cells, expected {width}'})
            else:
                out.append(row(cells, h, n))
        else:
            h = None
            if DATEISH.search(line) or RELATIVE.search(line):
                if history_level is not None:
                    out.append({'line': n, 'excluded': 'dated prose in resolved/history section'})
                elif not re.match(r'^\s*(?:\*\*)?(?:Created|Updated|Last Updated|Sources?):', line, re.I):
                    out.append({'line': n, 'issue': 'dated prose outside supported tables'})
    return out or [{'line': 0, 'issue': 'no supported calendar data'}]


def row(cells, h, n):
    di, ei, si = h
    r = {'line': n, 'date_text': cells[di], 'event': plain(cells[ei])}
    if si is not None and TERMINAL.match(plain(cells[si])):
        r['excluded'] = f'terminal Status: {cells[si]}'
        return r
    try:
        r['date'] = point_date(cells[di]).isoformat()
        if not r['event']:
            raise ValueError('empty event')
    except ValueError as exc:
        r['issue'] = str(exc)
    return r


def assess(root, docket, paths, as_of, days, explicit=False):
    records, inputs = [], {}
    def read(path):
        data = path.read_bytes()
        inputs[str(path)] = hashlib.sha256(data).hexdigest()
        return data.decode('utf-8-sig')
    try:
        drs = docket_view.load_docket(str(docket), source_text=read(docket))
    except (OSError, UnicodeError, ValueError, docket_view.DocketError) as exc:
        return {'rc': 2, 'error': f'canonical docket unreadable: {exc}', 'records': [], 'inputs': inputs}
    if not paths:
        records.append({'path': str(root / 'AGENTS'), 'line': 0, 'status': 'UNASSESSED', 'reason': 'zero files in declared patterns'})
    for path in paths:
        try:
            rel = path.resolve().relative_to(root.resolve())
            if len(rel.parts) < 3 or rel.parts[0] != 'AGENTS':
                raise ValueError('ledger must be under root/AGENTS/<DESK>')
            desk = rel.parts[1]
            rows = parse_ledger(read(path), path)
        except (OSError, UnicodeError, ValueError) as exc:
            records.append({'path': str(path), 'line': 0, 'status': 'UNASSESSED', 'reason': str(exc)})
            continue
        for r in rows:
            r.update(path=str(rel), desk=desk)
            records.append(r)
            if 'issue' in r:
                r.update(status='UNASSESSED', reason=r.pop('issue'))
                continue
            if 'excluded' in r:
                r.update(status='EXCLUDED', reason=r.pop('excluded'))
                continue
            day = dt.date.fromisoformat(r['date'])
            if not as_of <= day <= as_of + dt.timedelta(days=days):
                r.update(status='OUTSIDE-WINDOW', reason='date outside inclusive window')
                continue
            keys = terms(r['event'], desk)
            if not keys:
                r.update(status='UNASSESSED', reason='no discriminating event term')
                continue
            matches, uncertain = [], []
            quarters = set(re.findall(r'\bQ[1-4]\b', r['event'], re.I))
            for d in drs:
                if desk not in owners(d['owners']):
                    continue
                shared = sorted(keys & terms(d['catalyst'], desk))
                if not shared:
                    continue
                if d['start'] is not None and not d['start'] <= day <= d['end']:
                    continue
                hit = {'line': d['line'], 'terms': shared, 'event': d['catalyst'], 'span': d['span']}
                dq = set(re.findall(r'\bQ[1-4]\b', d['catalyst'], re.I))
                # A multi-day carrier can mention excluded events in its long body.
                # Date containment alone cannot locate the event inside that carrier.
                if d['start'] is None or d['approx'] or d['start'] != d['end'] or (quarters and dq and {q.upper() for q in quarters}.isdisjoint(q.upper() for q in dq)):
                    uncertain.append(hit)
                else:
                    matches.append(hit)
            r['matches'], r['uncertain_matches'] = matches, uncertain
            if len(matches) == 1 and not uncertain:
                r.update(status='MATCHED', reason='candidate date/desk/key-term correspondence only')
            elif matches or uncertain:
                r.update(status='UNASSESSED', reason='ambiguous, range, approximate, symbolic or conflicting-quarter candidate')
            else:
                r.update(status='UNMATCHED', reason='no date/desk/key-term candidate; owner must verify wording before registration')
    # Conservative: mixed results remain rc2. Findings are retained, never folded into clean.
    for name, digest in inputs.items():
        try:
            if hashlib.sha256(Path(name).read_bytes()).hexdigest() != digest:
                raise ValueError('input changed during scan')
        except (OSError, ValueError) as exc:
            records.append({'path': name, 'line': 0, 'status': 'UNASSESSED', 'reason': str(exc)})
    counts = {s: sum(r['status'] == s for r in records) for s in ('MATCHED', 'UNMATCHED', 'UNASSESSED', 'EXCLUDED', 'OUTSIDE-WINDOW')}
    assessed = counts['MATCHED'] + counts['UNMATCHED']
    rc = 2 if counts['UNASSESSED'] or not assessed else (1 if counts['UNMATCHED'] else 0)
    return {'rc': rc, 'as_of': as_of.isoformat(), 'through': (as_of + dt.timedelta(days=days)).isoformat(),
            'scope': 'explicit ledgers' if explicit else list(PATTERNS), 'files': [str(p) for p in paths],
            'self_in_scope': 'DAEDALUS included by default patterns; explicit selection may narrow',
            'counts': counts, 'assessed': assessed, 'docket_rows': len(drs), 'records': records, 'inputs': inputs,
            'limits': 'Candidate correspondence only: no event identity, schedule truth, pending status, delivery or owner consumption proof. Unsupported shapes remain UNASSESSED. Per-file hashes are not an atomic fleet snapshot.'}


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--root', type=Path, default=ROOT)
    ap.add_argument('--docket', type=Path)
    ap.add_argument('--ledger', action='append', default=[])
    ap.add_argument('--as-of', type=dt.date.fromisoformat, default=dt.datetime.now(ZoneInfo('America/New_York')).date())
    ap.add_argument('--days', type=int, default=14)
    ap.add_argument('--json', action='store_true')
    a = ap.parse_args(argv)
    if a.days < 0:
        ap.error('--days must be nonnegative')
    root = a.root.resolve()
    paths = sorted({(root / p).resolve() for p in a.ledger}) if a.ledger else sorted({p for pat in PATTERNS for p in root.glob(pat)})
    result = assess(root, a.docket or root / 'PROME/DOCKET.tsv', paths, a.as_of, a.days, bool(a.ledger))
    if a.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print(f"CALENDAR-COVERAGE rc={result['rc']} window={a.as_of}..{a.as_of + dt.timedelta(days=a.days)} files={len(paths)}")
        print('PERIMETER:', result.get('scope', list(PATTERNS)), 'DAEDALUS included by default; no archive recursion')
        for p in paths:
            print('FILE', p)
        if 'error' in result:
            print('UNASSESSED:', result['error'])
        for r in result['records']:
            print(f"{r['status']} {r['path']}:{r['line']} {r.get('date_text', '')} {r.get('event', '')} — {r['reason']}")
            for m in r.get('matches', []) + r.get('uncertain_matches', []):
                print(f"  DOCKET L{m['line']} terms={','.join(m['terms'])} span={m['span']}")
        print('COUNTS', result.get('counts', {}))
        if result['rc'] == 0:
            print('CLEAN: nonempty supported rows have candidate correspondence; not event-identity or delivery proof.')
        elif not result.get('assessed', 0):
            print('UNASSESSED: zero assessed rows; no clean bill.')
        print('ACTION: PROME and named desk owners review UNMATCHED/UNASSESSED locations; the tool never writes DOCKET.')
        print(result.get('limits', 'Cannot assess canonical input.'))
    return result['rc']


if __name__ == '__main__':
    sys.exit(main())
