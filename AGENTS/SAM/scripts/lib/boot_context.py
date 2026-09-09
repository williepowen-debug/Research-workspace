"""Read-only prediction reminders and bounded orientation extraction for SAM."""
import csv
import hashlib
import io
import json
import re
from datetime import date, datetime
from pathlib import Path
from zoneinfo import ZoneInfo

FIELDS = ['Pred_ID', 'Date_Made', 'Prediction', 'Confidence', 'Timeframe', 'Status', 'Date_Resolved', 'Outcome', 'Notes']
STATUSES = {'OPEN', 'FAILED', 'CONFIRMED', 'RESOLVED', 'RESOLVED CONFIRMED',
            'RESOLVED — TRUE-IN-LETTER / FALSE-IN-SPIRIT',
            'RESOLVED CONFIRMED — TRUE-IN-LETTER / FALSE-IN-SPIRIT'}
CHUNK_BYTES = 14000


class ContextError(ValueError):
    pass


def require(condition, message):
    if not condition:
        raise ContextError(message)


def digest(text):
    return hashlib.sha256(text.encode()).hexdigest()


def row_hash(row):
    return digest(json.dumps({k: row[k] for k in ('Prediction', 'Timeframe', 'Notes')},
                             ensure_ascii=False, sort_keys=True, separators=(',', ':')))


def predictions(sam):
    text = (sam/'thesis/PREDICTIONS.tsv').read_text()
    lines = [line for line in text.splitlines() if line.strip() and not line.startswith('#')]
    try:
        reader = csv.DictReader(io.StringIO('\n'.join(lines)), delimiter='\t', strict=True)
        require(reader.fieldnames == FIELDS, 'Prediction schema mismatch')
        rows = list(reader)
    except csv.Error as exc:
        raise ContextError(f'Malformed predictions TSV: {exc}') from exc
    seen = set()
    for row in rows:
        require(set(row) == set(FIELDS) and all(v is not None for v in row.values()), 'Malformed prediction row')
        ident = row['Pred_ID']
        require(re.fullmatch(r'SAM-\d+', ident) and ident not in seen, f'Invalid/duplicate prediction ID: {ident}')
        require(row['Status'] in STATUSES, f'Unknown prediction status for {ident}: {row["Status"]}')
        require(all(row[k].strip() for k in ('Prediction', 'Timeframe', 'Notes')), f'Incomplete conditions: {ident}')
        seen.add(ident)
    require(rows, 'No prediction rows found')
    return rows


def prediction_report(sam, now=None):
    now = now or datetime.now(ZoneInfo('America/New_York'))
    require(now.tzinfo is not None, 'Reminder clock must include timezone')
    rows = predictions(sam)
    opened = [row for row in rows if row['Status'] == 'OPEN']
    try:
        schedule = json.loads((sam/'docket/PREDICTION_SCHEDULE.json').read_text())
        require(isinstance(schedule, dict) and schedule.get('schema_version') == 1
                and isinstance(schedule.get('predictions'), dict), 'Schedule schema mismatch')
    except (OSError, ValueError) as exc:
        schedule = {'predictions': {}}
        schedule_error = f'SCHEDULING GAP: {exc}'
    else:
        schedule_error = None
    issues = [schedule_error] if schedule_error else []
    result = [f'PREDICTIONS: {len(opened)} OPEN from {len(rows)} validated rows (preamble counts ignored).',
              'Read-only reminders; no activation, resolution or grade performed.']
    by_id = {r['Pred_ID']: r for r in rows}
    for ident in schedule['predictions']:
        if ident not in by_id:
            issues.append(f'SCHEDULING GAP: unknown scheduled ID {ident}')
    for row in opened:
        ident = row['Pred_ID']
        result += ['', f'{ident} — OPEN', 'Timeframe: '+row['Timeframe'],
                   'Prediction: '+row['Prediction'], 'Notes: '+row['Notes']]
        try:
            item = schedule['predictions'].get(ident)
            require(isinstance(item, dict), f'SCHEDULING GAP: missing schedule for {ident}')
            require(item.get('condition_sha256') == row_hash(row), f'SCHEDULING GAP: changed conditions for {ident}')
            due = date.fromisoformat(item['due_date'])
            zone = ZoneInfo(item['timezone'])
            require(isinstance(item.get('boundary_rule'), str) and bool(item['boundary_rule'].strip()),
                    f'SCHEDULING GAP: no boundary rule for {ident}')
            delta = (due-now.astimezone(zone).date()).days
            state = f'{delta} calendar days remaining' if delta > 0 else 'review due today; observe boundary below' if delta == 0 else f'review overdue by {-delta} calendar days'
            result.append(f'Reminder: {state}; {due} [{item["timezone"]}]; {item["boundary_rule"]}')
        except (ContextError, KeyError, ValueError, TypeError) as exc:
            issues.append(f'{ident}: {exc}')
    result += ['', *issues]
    return '\n'.join(result).rstrip()+'\n', issues


def heading_blocks(text):
    matches = list(re.finditer(r'^## (.+)$', text, re.M))
    titles = [m[1] for m in matches]
    require(len(titles) == len(set(titles)), 'Duplicate second-level heading')
    blocks = [(m[1], text[m.start():matches[i+1].start() if i+1<len(matches) else len(text)]) for i,m in enumerate(matches)]
    return text[:matches[0].start()] if matches else text, blocks


def choose(blocks, prefix):
    found = [(title, body) for title,body in blocks if title.startswith(prefix)]
    require(len(found) == 1, f'Required section missing/ambiguous: {prefix}')
    return found[0]


def split_chunks(text, budget=CHUNK_BYTES):
    chunks, current = [], ''
    for line in text.splitlines(keepends=True):
        require(len(line.encode()) <= budget, 'Single line exceeds chunk budget; use smaller explicit source sections')
        if len((current+line).encode()) > budget:
            chunks.append(current); current = ''
        current += line
    if current:
        chunks.append(current)
    return chunks


def orientation(sam, now=None):
    """Build all content before printing anything; broken sections fail closed."""
    parts = []
    def add(path, section, body, source):
        require(body.strip(), f'Empty orientation section: {path} {section}')
        for index, chunk in enumerate(split_chunks(body), 1):
            parts.append(dict(path=path, section=section, piece=index, bytes=len(chunk.encode()),
                              source_sha256=digest(source), content_sha256=digest(chunk), content=chunk))
    path='thesis/THESIS.md'; text=(sam/path).read_text(); header,blocks=heading_blocks(text)
    # Exact structural boundary, not a byte/line slice of the long historical header.
    boundary='**Retirement record (as published; percentages later corrected in STATUS):**'
    require(header.count(boundary)==1, 'THESIS current-header boundary missing/ambiguous')
    add(path,'Current identity/version',header.split(boundary)[0],text)
    for prefix in ('PILLAR AUDIT', 'CARRY-UNWIND PROBABILITY METHOD', 'OIL-IN-YEN STRUCTURAL DYNAMIC', 'KEY THRESHOLDS'):
        title,body=choose(blocks,prefix); add(path,title,body,text)
    path='STATUS.md'; text=(sam/path).read_text(); header,blocks=heading_blocks(text)
    add(path,'Current header',header,text)
    dated=[(title,body) for title,body in blocks if re.match(r'\d{4}-\d{2}-\d{2}\b',title)]
    require(dated, 'STATUS missing current dated session')
    dates=[title[:10] for title,body in dated]
    require(dates==sorted(dates,reverse=True),'STATUS sessions not newest first')
    add(path,*dated[0],text)
    for prefix in ('LIVE MARKET DATA','CARRY UNWIND PROBABILITY','INTERVENTION STATUS','KEY THRESHOLDS','WHAT TO WATCH','POSITION','PREDICTIONS'):
        title,body=choose(blocks,prefix);add(path,title,body,text)
    path='docket/CALENDAR.md';text=(sam/path).read_text();header,blocks=heading_blocks(text)
    forward=[(title,body) for title,body in blocks if 'forward event set synchronized with CATALYSTS.tsv' in title]
    require(len(forward)==1,'Calendar forward table missing/ambiguous')
    # Forward section is maintained by owner; dates are not inferred from decorative text.
    # Reject explicit resolved rows instead of dropping them silently.
    require('✅' not in forward[0][1], 'Resolved item in forward calendar; reconcile owner section')
    add(path,*forward[0],text)
    title,body=choose(blocks,'🔭 BEYOND THE 6-WEEK HORIZON');add(path,title,body,text)
    path='thesis/timeline/TIMELINE.md';text=(sam/path).read_text();header,blocks=heading_blocks(text)
    dated=[(title,body) for title,body in blocks if re.match(r'\d{4}-\d{2}-\d{2}\b',title)]
    require(len(dated)>=2,'TIMELINE needs two ISO-dated latest blocks')
    require(dated[:2]==blocks[:2], 'TIMELINE latest blocks must have unambiguous ISO dates')
    require(dated[0][0][:10]>=dated[1][0][:10], 'TIMELINE order is not newest first')
    for title,body in dated[:2]:add(path,title,body,text)
    path='MEMORY.md';text=(sam/path).read_text()
    require('### NEXT SESSION' in text,'MEMORY handoff missing')
    add(path,'Whole memory (all chunks required)',text,text)
    path='thesis/PREDICTIONS.tsv';text=(sam/path).read_text()
    require(text.count('# HIGH-CONFIDENCE FAILURES')==1,'Calibration warning missing/ambiguous')
    warning=text[text.index('# HIGH-CONFIDENCE FAILURES'):]
    require('\nPred_ID\t' in warning,'Prediction header missing')
    add(path,'Calibration warning',warning.split('\nPred_ID\t')[0],text)
    report,issues=prediction_report(sam,now)
    add(path,'OPEN predictions and schedule diagnostics',report,text)
    # Sidecar hash travels alongside source-row hashes.
    schedule=sam/'docket/PREDICTION_SCHEDULE.json'
    schedule_hash=hashlib.sha256(schedule.read_bytes()).hexdigest() if schedule.exists() else 'MISSING'
    return parts,issues,schedule_hash


def emit_orientation(sam, part=None, now=None):
    parts,issues,schedule_hash=orientation(sam,now)
    if part is not None:
        require(1<=part<=len(parts), f'Part must be between 1 and {len(parts)}')
        item=parts[part-1]
        print(f'PART {part}/{len(parts)} | {item["path"]} | {item["section"]} | {item["bytes"]} B')
        print(f'Source SHA256 {item["source_sha256"]}; content SHA256 {item["content_sha256"]}')
        print(item['content'],end='')
        print(f'\nEND PART {part}/{len(parts)}')
    else:
        print(f'ORIENTATION INDEX: {len(parts)} parts; {sum(p["bytes"] for p in parts)} content bytes.')
        print('Index only: context NOT loaded. Read EVERY part using --orient --part N before reporting orientation complete.')
        print('No network, market writes, inbox actions or prediction grades. All clocks remain source clocks.')
        print('Schedule SHA256 '+schedule_hash)
        for i,item in enumerate(parts,1):
            print(f'{i}: {item["path"]} | {item["section"]} (piece {item["piece"]}) | {item["bytes"]} B | source={item["source_sha256"]} | content={item["content_sha256"]}')
        for issue in issues: print(issue)
    return int(bool(issues))
