"""Read-only calendar adapters. Source records remain authoritative."""
import ast
import hashlib
import json
import re
import subprocess
import sys
from datetime import date, datetime
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[5]
HERE = Path(__file__).resolve().parent
ECON = 'AGENTS/HENRY/domain/ECON_CALENDAR.md'
DOCKET = 'PROME/DOCKET.tsv'
GATES = 'PROME/GATES.tsv'
REGISTRY = 'PROME/tools/prome_gate.py'
ISO = r'\d{4}-\d{2}-\d{2}'
LIMIT = 3_000_000


def digest(text):
    return hashlib.sha256(text.encode()).hexdigest()


def read(root, path):
    target = (root / path).resolve()
    if not target.is_relative_to(root.resolve()) or not target.is_file():
        raise ValueError('Source missing or outside workspace')
    if target.stat().st_size > LIMIT:
        raise ValueError('Source exceeds reader size limit')
    return target.read_text(encoding='utf-8')


def registry(text):
    for node in ast.parse(text).body:
        if isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id == 'SUMMONS_LEDGERS' for t in node.targets):
            value = ast.literal_eval(node.value)
            if not isinstance(value, dict) or not all(isinstance(k, str) and isinstance(v, str) and re.fullmatch(r'AGENTS/[A-Z]+/(?:docket|workbook)/CATALYSTS.tsv', v) for k, v in value.items()):
                raise ValueError('Unsupported catalyst registry')
            return value
    raise ValueError('Catalyst registry unavailable')


def record(path, text, line, excerpt):
    return dict(path=path, line=line, excerpt=excerpt, label=path, sha256=digest(text))


def timing(cell, today):
    dates = re.findall(ISO, cell)
    try:
        for value in dates:
            date.fromisoformat(value)
    except ValueError:
        return '', '', 'uncertain'
    if not dates:
        return '', '', 'undated'
    if len(dates) > 2 or (len(dates) == 2 and dates[0] > dates[1]):
        return '', '', 'uncertain'
    start, end = dates[0], dates[-1]
    if re.search(r'~|TBD|ESTIMAT|MODELED|TENTATIVE|APPROX', cell, re.I):
        return start, end if start != end else '', 'uncertain'
    if end < today.isoformat():
        return start, end if start != end else '', 'overdue'
    return start, end if start != end else '', 'window' if start != end else 'date'


def event(path, text, line, raw, title, owner, cell, layer, today, **extra):
    start, end, lane = timing(cell, today)
    value = dict(id=path + ':' + digest(raw)[:16], title=title, owner=owner,
                 date=start, end=end, lane=lane, time='', when=cell or 'No date recorded',
                 layer=layer, why='', work='', link='', note='', verification='',
                 confidence='Source record; not independently reverified',
                 sources=[record(path, text, line, raw)])
    value.update(extra)
    return value


def tsv(text, required):
    lines = [(i, line) for i, line in enumerate(text.splitlines(), 1) if line.strip() and not line.startswith('#')]
    if not lines:
        raise ValueError('Empty source; no schema header')
    header = lines[0][1].split('\t')
    if not set(required) <= set(header) or len(set(header)) != len(header):
        raise ValueError('Unsupported source columns')
    rows = []
    errors = []
    for number, raw in lines[1:]:
        cells = raw.split('\t')
        if len(cells) != len(header):
            errors.append(f'Line {number}: malformed row; not placed on calendar')
        else:
            rows.append((number, raw, dict(zip(header, cells))))
    return rows, errors


def catalysts(path, text, owner, today):
    rows, errors = tsv(text, ['date', 'event', 'notes'])
    events = []
    for line, raw, row in rows:
        cell = row['date']
        # The source's date class can qualify an otherwise exact-looking date.
        explicit = re.search(r'\bdate_class\s+([A-Z-]+)', row['notes'])
        cls = row.get('date_class', '') or (explicit[1] if explicit else '')
        value = event(path, text, line, raw, row['event'], owner, cell, 'followup', today,
                      why=row.get('threshold_signal', row.get('expected_vol_impact', '')),
                      work=row.get('what_to_check', ''), note=row['notes'],
                      confidence=cls or 'Date class not separately recorded')
        if re.search(r'ESTIMAT|MODELED|TENTATIVE|APPROX', cls, re.I):
            value['lane'] = 'uncertain'
        events.append(value)
    return events, errors


def gates(text, today):
    rows, errors = tsv(text, ['gate_id', 'state', 'review_by', 'owner', 'condition'])
    events = []
    for line, raw, row in rows:
        state = re.split(r'\s|/|—|:|\(', row['state'].strip(), maxsplit=1)[0]
        if state in {'RESOLVED', 'LAPSED', 'RETIRED'}:
            continue
        if state not in {'LIVE', 'FIRED-UNEXECUTED'}:
            errors.append(f'Line {line}: unrecognized gate state; inspect source')
            continue
        # Owner contract: leading review_by date is the review clock; prose can contain other dates.
        match = re.match(ISO, row['review_by'])
        cell = match[0] if match else ''
        events.append(event(GATES, text, line, raw, row['gate_id'] + ' · review', row['owner'], cell,
                            'followup', today, why=row['condition'], note='Review date, not a forecast of a gate firing. ' + row['review_by'],
                            link=row.get('definition_surface', '') + '\n' + row.get('consumed_by', ''),
                            confidence=row['state']))
    return events, errors


def economic(text, today):
    window = re.search(r'Window verified:\*\*\s*(' + ISO + r')\s*→\s*(' + ISO + ')', text)
    if not window:
        raise ValueError('No explicit calendar verification window; year inference refused')
    lo, hi = map(date.fromisoformat, window.groups())
    rebuild = re.search(r'Rebuild this window before (' + ISO + ')', text)
    warnings = ['Only the NEXT 30 DAYS table is loaded; prose beyond the window and recurring patterns are not expanded.']
    if today > hi or (rebuild and today >= date.fromisoformat(rebuild[1])):
        warnings.append('STALE: HENRY’s stated calendar refresh deadline has passed.')
    header = next((l for l in text.splitlines() if 'Window verified:' in l), '')
    result = []
    in_table = False
    for line, raw in enumerate(text.splitlines(), 1):
        if raw.startswith('| Date | Time |'):
            in_table = True
            continue
        if not in_table:
            continue
        if not raw.startswith('|'):
            break
        cells = [s.strip().replace('**', '') for s in raw.strip('|').split('|')]
        if raw.startswith('|---'):
            continue
        if len(cells) != 6:
            warnings.append(f'Line {line}: unsupported economic row')
            continue
        dated, clock, title, period, source, why = cells
        match = re.search(r'\b([A-Z][a-z]{2}) (\d{1,2})(?:[–-](\d{1,2}))?\b', dated)
        candidates = []
        if match:
            for year in range(lo.year, hi.year + 1):
                try:
                    start = datetime.strptime(f'{year} {match[1]} {match[2]}', '%Y %b %d').date()
                    end = start.replace(day=int(match[3])) if match[3] else start
                    if lo <= start <= end <= hi:
                        candidates.append((start, end))
                except ValueError:
                    pass
        cell = ' → '.join(dict.fromkeys(d.isoformat() for d in candidates[0])) if len(candidates) == 1 else ''
        value = event(ECON, text, line, raw, title, 'HENRY', cell, 'market', today,
                      why=why, note=f'Data for: {period}. Source: {source}', verification=header,
                      when=f'{dated} · {clock} ET', confidence='Schedule as recorded by HENRY')
        if not cell:
            value['lane'] = 'uncertain'
        elif re.fullmatch(r'\d{1,2}:\d{2}', clock) and value['lane'] == 'date':
            hour, minute = map(int, clock.split(':'))
            if hour < 24 and minute < 60:
                value.update(lane='timed', time=f'{hour:02}:{minute:02}')
        result.append(value)
    if not in_table:
        raise ValueError('Economic table missing')
    return result, warnings


def docket(root, text, today):
    command = [sys.executable, '-B', str(root / 'PROME/tools/spawn_list.py'), '--open', '--json', '--as-of', today.isoformat()]
    completed = subprocess.run(command, cwd=root, capture_output=True, text=True, timeout=20)
    if completed.returncode or len(completed.stdout) > 8_000_000:
        raise ValueError('Open-docket export failed or exceeded output limit')
    doc = json.loads(completed.stdout)
    if (doc.get('schema') != 'spawn_list.open' or doc.get('version') != 1 or doc.get('error')
            or doc.get('as_of') != today.isoformat() or doc.get('source_sha256') != digest(text)
            or not isinstance(doc.get('rows'), list) or doc.get('count') != len(doc['rows'])):
        raise ValueError('Open-docket export changed during read or has unsupported contract; refresh')
    lines = text.splitlines()
    events = []
    for row in doc['rows']:
        number = row['line']
        if type(number) is not int or not 1 <= number <= len(lines):
            raise ValueError('Export has invalid source line')
        raw = lines[number - 1]
        cells = raw.split('\t')
        if len(cells) < 4 or cells[:4] != [row['date_cell'], row['catalyst'], row['owner_cell'], row['state_cell']]:
            raise ValueError('Export does not match captured source row')
        events.append(event(DOCKET, text, number, raw, row['catalyst'], row['owner_cell'], row['date_cell'],
                            'unclassified', today, work=row['notes'], confidence=row['state_cell'],
                            note='Open obligation; not evidence that an agent should start or that work is unfinished in every owner record. ' + row['coverage']))
    return events, []


def enrich(events, texts, today):
    """Reuse reviewed joins/classifications only while every cited excerpt still matches."""
    context = json.loads((HERE.parent / 'week-sketch/snapshot.json').read_text())
    notes = []
    for saved in context['events']:
        sources = saved['sources']
        if not all(s['path'] in texts and s['excerpt'] in texts[s['path']] for s in sources):
            notes.append(saved['title'] + ': preview context not reused because a cited record changed or is unavailable.')
            continue
        matched = [e for e in events if any(e['sources'][0]['path'] == s['path'] and e['sources'][0]['excerpt'] == s['excerpt'] for s in sources)]
        if not matched or not any(e['date'] == saved['date'] for e in matched):
            continue
        # All represented primary rows must still be current; missing terminal docket rows are not revived.
        if any(s['path'] == DOCKET and not any(e['sources'][0]['excerpt'] == s['excerpt'] for e in matched) for s in sources):
            continue
        item = dict(saved)
        item['sources'] = [record(s['path'], texts[s['path']], texts[s['path']][:texts[s['path']].index(s['excerpt'])].count('\n') + 1, s['excerpt']) for s in sources]
        item['verification'] = 'Reviewed preview context from October 31, 2026; cited excerpts still match this refresh. ' + item.get('verification', '')
        item['note'] = item.get('note', '') + ' Context is dated; this refresh does not reverify external schedules or current holdings.'
        if (item.get('end') or item['date']) and (item.get('end') or item['date']) < today.isoformat() and item['lane'] in {'date', 'timed', 'window'}:
            item['lane'] = 'overdue'
        events = [e for e in events if e not in matched] + [item]
    return events, notes


def snapshot(root=ROOT, today=None):
    today = today or datetime.now(ZoneInfo('America/New_York')).date()
    texts, coverage, events = {}, [], []
    def load(path, label, parser):
        try:
            text = read(root, path)
            texts[path] = text
            rows, warnings = parser(text)
            events.extend(rows)
            coverage.append(dict(path=path, label=label, status='loaded', count=len(rows), warnings=warnings, sha256=digest(text)))
        except (OSError, ValueError, KeyError, TypeError, subprocess.SubprocessError) as error:
            coverage.append(dict(path=path, label=label, status='unavailable', count=0, warnings=[str(error)]))
    load(ECON, 'Economic schedule', lambda text: economic(text, today))
    load(DOCKET, 'Open desk obligations', lambda text: docket(root, text, today))
    load(GATES, 'Gate review dates', lambda text: gates(text, today))
    try:
        regtext = read(root, REGISTRY)
        texts[REGISTRY] = regtext
        registered = registry(regtext)
        for owner, path in registered.items():
            load(path, owner + ' catalysts', lambda text, p=path, o=owner: catalysts(p, text, o, today))
    except (OSError, ValueError, SyntaxError) as error:
        coverage.append(dict(path=REGISTRY, label='Catalyst registry', status='unavailable', count=0, warnings=[str(error)]))
    card = 'AGENTS/TERRY/setups/QQQ_nov20-690-670P_gamma-negative-putwall_2026-10-22.md'
    load(card, 'Dated preview position context (not holdings)', lambda text: ([], []))
    events, context_notes = enrich(events, texts, today)
    # Cross-file reads are sequential, not transactional. Refuse to describe a changed file as current.
    for item in coverage:
        if item['status'] == 'loaded':
            try:
                if digest(read(root, item['path'])) != item['sha256']:
                    raise ValueError('Source changed during refresh; refresh again')
            except (OSError, ValueError) as error:
                item.update(status='unavailable', warnings=item['warnings'] + [str(error)])
                events = [e for e in events if not any(s['path'] == item['path'] for s in e['sources'])]
    return dict(today=today.isoformat(), refreshed_at=datetime.now(ZoneInfo('America/New_York')).isoformat(),
                timezone='America/New_York', events=events, coverage=coverage, context_notes=context_notes,
                note='Live local files, not a sync with GitHub or an external schedule verification. No launch, reminder or write actions.')
