"""Source-derived operator attention. No ticker-only coverage joins or trade execution."""
import csv
import datetime as dt
import hashlib
import html
from pathlib import Path
import re

FIELDS = ('account', 'ticker', 'instrument', 'expiry', 'owner', 'review', 'approval',
          'order', 'fill', 'action', 'complete_when', 'gate_ids', 'source', 'source_sha256', 'checked')
ROOT = Path(__file__).resolve().parents[2]


def clean(text):
    return re.sub(r'\*\*|~~|`', '', text).strip()


def link(path, label=None):
    # Pages live in PROME/artifacts; native relative links work in local artifacts.
    target = '../../' + path
    return f'<a href="{html.escape(target, quote=True)}">{html.escape(label or path)}</a>'


def source_digest(root, path):
    p = (root / path).resolve()
    if not p.is_relative_to(root.resolve()) or not p.is_file():
        raise ValueError('missing or invalid evidence: ' + path)
    return hashlib.sha256(p.read_bytes()).hexdigest()


def expiry_date(text, year):
    m = re.search(r'\b(20\d\d)-\d\d-\d\d\b', text)
    if m:
        return dt.date.fromisoformat(m[0]).isoformat()
    m = re.search(r'\b([A-Z][a-z]{2})-(\d{1,2})(?:-(20\d\d))?\b', text)
    if m:
        return dt.datetime.strptime(f'{m[1]}-{m[2]}-{m[3] or year}', '%b-%d-%Y').date().isoformat()
    m = re.search(r'\b(\d{1,2})/(\d{1,2})/(20\d\d)\b', text)
    if m:
        return dt.date(int(m[3]), int(m[1]), int(m[2])).isoformat()
    return ''


def instrument_name(text):
    # Keep every strike/type leg of a spread; never collapse to the underlying.
    text = re.sub(r'\b[A-Z][a-z]{2}-\d{1,2}(?:-20\d\d)?\b', '', text)
    m = re.search(r'\$?\d+(?:\.\d+)?[CP]?(?:/\$?\d+(?:\.\d+)?[CP]?)+(?:\s+(?:call|put)\s+spread)?|\$?\d+(?:\.\d+)?[CP]\b', text, re.I)
    return re.sub(r'\s+', ' ', m[0]).strip() if m else 'Stock'


def holdings(root=ROOT):
    source = root / 'FORGE/STATUS.md'
    text = source.read_text()
    stamp = re.search(r'\*\*Updated:\*\*\s*(\d{4}-\d\d-\d\d)', text)
    vintage = stamp[1] if stamp else 'UNKNOWN'
    year = int(vintage[:4]) if stamp else None
    rows, errors, cols, account, ticker = [], [], None, '', ''
    for line_no, ln in enumerate(text.splitlines(), 1):
        s = ln.strip()
        if s.startswith('## '):
            account = 'Fidelity' if s.startswith('## Fidelity') else ('Robinhood' if s.startswith('## Robinhood') else '')
            cols, ticker = None, ''
        elif s.startswith('### '):
            m = re.match(r'###\s+\*{0,2}([A-Z]{1,6})\b', s)
            ticker, cols = (m[1] if m else ''), None
        elif account and s.startswith('|'):
            raw = [c.strip() for c in s.strip('|').split('|')]
            cells = [clean(c) for c in raw]
            if 'Qty' in cells and any(c in cells for c in ('Ticker', 'Strike', 'Position')):
                cols = {c.split()[0]: i for i, c in enumerate(cells) if c}
                continue
            if cols is None or all(re.fullmatch(':?-+:?', c or '-') for c in cells):
                continue
            if len(cells) <= max(cols.values()):
                errors.append(f'FORGE line {line_no}: malformed holding row')
                continue
            get = lambda name: cells[cols[name]] if name in cols else ''
            if any('~~' in raw[cols[n]] for n in ('Ticker', 'Strike', 'Type', 'Position', 'Qty') if n in cols):
                continue
            state = ' '.join(get(n) for n in ('P&L', 'Outcome', 'State'))
            if re.fullmatch(r'0(?:\.0+)?', get('Qty')) or any(re.match(r'^(?:✅\s*)?(CLOSED|EXPIRED|ASSIGNED|EXERCISED|REALIZED)\b', get(n), re.I) for n in ('P&L', 'Outcome', 'State')):
                continue
            identity = get('Ticker') or get('Position') or ticker
            m = re.match(r'([A-Z]{1,6})\b', identity)
            if not m:
                errors.append(f'FORGE line {line_no}: instrument identity unknown')
                continue
            tick = m[1]
            pos = instrument_name(get('Strike') or get('Type') or get('Position'))
            exp = expiry_date(get('Expiry') or get('Type'), year) if year else ''
            if pos != 'Stock' and not exp:
                errors.append(f'FORGE line {line_no}: option expiry unknown')
            note = ' '.join(get(n) for n in ('Note', 'Owner', 'P&L', 'State'))
            observation = f'{vintage} broker positions; expiry year from this dated book where omitted'
            if account == 'Robinhood':
                observation = 'Not captured September 3; August 28 / operator-supplied records; current holdings unverified'
            if 'screenshot received September 9' in note:
                observation = 'Screenshot received September 9, 2026; capture timestamp and account header absent; Fidelity attribution inferred from context'
            qty = get('Qty')
            if not re.match(r'^\d+(?:\.\d+)?(?:\s|$)', qty):
                errors.append(f'FORGE line {line_no}: quantity unknown')
            pl = re.search(r'[+\-−]\s?\$?[\d,]+(?:\.\d+)?%?(?:\s*/\s*[+\-−][\d.]+%)?', get('P&L'))
            rows.append(dict(account=account, ticker=tick, instrument=pos, expiry=exp,
                             qty=qty, pl=pl[0] if pl else '—', observation=observation,
                             note=note, line=line_no, source='FORGE/STATUS.md'))
    if not rows:
        errors.append('FORGE holdings parsed to zero rows')
    return rows, errors


def key(row):
    return tuple(row[f] for f in FIELDS[:4])


def coverage(root=ROOT):
    rows, errors = holdings(root)
    metadata = {}
    try:
        with (root / 'FORGE/position_management.tsv').open() as f:
            reader = csv.DictReader(f, delimiter='\t')
            if tuple(reader.fieldnames or ()) != FIELDS:
                raise ValueError('management schema changed')
            for m in reader:
                k = key(m)
                if k in metadata:
                    raise ValueError('duplicate management key: ' + str(k))
                if None in m or any(v is None for v in m.values()):
                    raise ValueError('malformed management row')
                dt.date.fromisoformat(m['checked'])
                if m['approval'] not in ('APPROVED', 'NOT_RECORDED', 'NOT_APPLICABLE') or m['order'] not in ('UNKNOWN', 'PLACED', 'NOT_APPLICABLE') or m['fill'] not in ('UNKNOWN', 'FILLED', 'NOT_APPLICABLE'):
                    raise ValueError('invalid approval/order/fill state')
                try:
                    m['valid'] = source_digest(root, m['source']) == m['source_sha256']
                except (OSError, ValueError):
                    m['valid'] = False
                if not m['valid']:
                    errors.append('Management evidence changed/missing: ' + '/'.join(k))
                metadata[k] = m
    except (OSError, ValueError, TypeError) as exc:
        errors.append('Management registry unavailable: ' + str(exc))
        metadata = {}
    gate_rows = {}
    try:
        for r in csv.reader((root / 'PROME/GATES.tsv').read_text().splitlines(), delimiter='\t'):
            if r and r[0].startswith('GATE-') and len(r) >= 8:
                gate_rows[r[0]] = r
    except OSError:
        errors.append('GATES unavailable; linked gate state unknown')
    for r in rows:
        m = metadata.get(key(r))
        r['management'] = m if m and m['valid'] else None
        r['gates'] = []
        if r['management']:
            for gid in filter(None, m['gate_ids'].split(',')):
                g = gate_rows.get(gid)
                r['gates'].append((gid, g[5] if g else 'UNKNOWN — gate missing', g[6] if g else 'UNKNOWN'))
                if not g:
                    errors.append('Mapped gate missing: ' + gid)
    return rows, errors


def pending_work(root=ROOT, today=None):
    today = today or dt.date.today()
    rows = []
    for no, ln in enumerate((root / 'PROME/DOCKET.tsv').read_text().splitlines(), 1):
        r = ln.split('\t')
        if len(r) < 6 or not re.match(r'PENDING\b|OVERDUE-ANNOTATED\b', r[3]) or not re.search(r'\bPROME\b', r[2]):
            continue
        end = r[0].split('..')[-1]
        if end.startswith('next-'):
            continue  # session-keyed row (DOCKET canon: `next-<DESK>-session` etc.) — not dated pending work, never an error (2026-09-10; L314 blocked the state write since 9/9)
        try:
            d = dt.date.fromisoformat(end)
        except ValueError:
            raise ValueError(f'DOCKET L{no}: unparseable pending date')
        if d > today + dt.timedelta(days=7):
            continue
        rows.append(dict(line=no, due=end, title=r[1], owner=r[2], state=r[3], evidence=r[4], next=r[5],
                         timing='OVERDUE' if d < today else ('TODAY' if d == today else 'UPCOMING')))
    return sorted(rows, key=lambda r: (r['due'], r['line']))


def confirmed_receipts(root=ROOT):
    # Discover receipts linked by the holdings mirror; only explicit confirmed sales qualify.
    text = (root / 'FORGE/STATUS.md').read_text()
    paths = sorted(set(re.findall(r'\]\(\.\./(PROME/reports/[^)]+sale-receipt\.md)\)', text)))
    receipts = []
    for path in paths:
        body = (root / path).read_text()
        if '**Execution confirmed by Will and his pasted broker receipt.**' not in body:
            raise ValueError('Receipt confirmation missing: ' + path)
        fields = {}
        for ln in body.splitlines():
            if ln.startswith('|'):
                c = [clean(v) for v in ln.strip('|').split('|')]
                if len(c) == 2:
                    fields[c[0]] = c[1]
        if not all(fields.get(k) for k in ('Date', 'Symbol', 'Contracts', 'Price', 'Net amount', 'Settlement')):
            raise ValueError('Incomplete receipt: ' + path)
        receipts.append((path, fields))
    return receipts


def render(root=ROOT):
    rows, errors = coverage(root)
    esc = html.escape
    h = ["<section id='broker-actions'><h2>Broker actions — approval, orders and fills</h2>"]
    h.append("<p>Recorded actions only. A sale instruction does not establish an order or fill.</p>")
    actions = [r for r in rows if r['management'] and r['management']['action']]
    # One instruction per contract, not per tax lot.
    seen = set()
    for r in sorted(actions, key=lambda r: r['management']['review']):
        if key(r) in seen:
            continue
        seen.add(key(r)); m = r['management']
        h.append(f"<article class='decision'><b>{esc(r['account']+' · '+r['ticker']+' '+r['instrument']+' '+r['expiry'])}</b>"
                 f"<p>Approval: {esc(m['approval'])} · Order: {esc(m['order'])} · Fill: {esc(m['fill'])}</p>"
                 f"<p>{esc(m['action'])}</p><p>Owner: {esc(m['owner'])} · Review: {esc(m['review'])}</p>"
                 f"<p>Complete when: {esc(m['complete_when'])}</p><small>Checked {esc(m['checked'])} · {link(m['source'], 'Evidence')}</small></article>")
    if not actions:
        h.append('<p>No source-validated broker actions available; this is not an all-clear.</p>')
    h.append("</section><section id='management-coverage'><h2>Position management coverage</h2><p>Accounts and contracts are matched explicitly. Unrecorded coverage does not mean a position has no possible exit rule. Notes and marks retain their observation dates.</p><div class='tw'><table><tr><th>Account / instrument</th><th>Qty / expiry</th><th>Management / next review</th><th>Evidence</th></tr>")
    for r in rows:
        m = r['management']
        if m:
            management = f"{esc(m['owner'])} · next review {esc(m['review'])}<br>Complete when: {esc(m['complete_when'])}"
            source = link(m['source'], 'Management source') + ' · checked ' + esc(m['checked'])
        else:
            management = 'Management mapping UNRECORDED — PROME must verify the applicable rule and next review'
            source = 'No validated management mapping'
        for gid, state, checked in r['gates']:
            management += f'<details><summary>{esc(gid)}</summary><p>{esc(state)}</p><p>Gate evidence: {esc(checked)}</p>{link("PROME/GATES.tsv", "Gate record")}</details>'
        if not r['gates']:
            management += '<br>No explicit action-gate mapping verified'
        h.append(f"<tr><td>{esc(r['account'])}<br><b>{esc(r['ticker']+' '+r['instrument'])}</b></td><td>{esc(r['qty'])}<br>{esc(r['expiry'] or 'No expiry')}</td><td>{management}</td><td>{source}<br>{link(r['source'], 'Holding source')}<br>{esc(r['observation'])}<details><summary>Recorded position note</summary>{esc(r['note'])}</details></td></tr>")
    h.append('</table></div></section>')
    try:
        receipts = confirmed_receipts(root)
        h.append("<section id='confirmed-changes'><h2>Confirmed changes and settlement</h2>")
        for path, f in receipts:
            h.append(f"<p><b>{esc(f['Date']+' · '+f['Symbol'])}</b> · contracts {esc(f['Contracts'])} at {esc(f['Price'])}; net proceeds {esc(f['Net amount'])}; scheduled settlement {esc(f['Settlement'])}. {link(path, 'Broker receipt')}</p>")
        h.append('<p>Settlement date is not confirmation of settled cash. Account attribution follows the receipt caveat; no updated account total is inferred.</p></section>')
    except (OSError, ValueError) as exc:
        errors.append(str(exc))
    try:
        work = pending_work(root)
        h.append("<section id='prome-work'><h2>PROME work — overdue and next seven days</h2><p>Generated from the docket. Pending means not reconciled here; owner delivery may already exist. Items involving Will are identified by their recorded owner, with current approvals in Waiting on you.</p>")
        for r in work:
            h.append(f"<details><summary>{esc(r['timing']+' · '+r['due']+' · L'+str(r['line'])+' · '+r['title'].split('—')[0])}</summary><p>Owner: {esc(r['owner'])}</p><p>{esc(r['title'])}</p><p>Recorded state: {esc(r['state'])}</p><p>Next action / completion terms: {esc(r['next'])}</p><p>Evidence required: {esc(r['evidence'])}</p>{link('PROME/DOCKET.tsv', 'Docket record')}</details>")
        h.append('</section>')
    except (OSError, ValueError) as exc:
        errors.append(str(exc))
    warnings = ''.join(f"<div class='degraded'>⚠ {esc(e)}</div>" for e in errors)
    return warnings + '\n'.join(h), errors
