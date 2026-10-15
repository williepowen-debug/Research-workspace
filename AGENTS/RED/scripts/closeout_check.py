#!/usr/bin/env python3
"""RED closeout check — the cross-surface consistency gate. READ-ONLY.

WHY THIS EXISTS (built 2026-10-15, S54, on Will's 14:46 ET word; spec
`research/2026-10-15_CLOSEOUT_CHECK_BUILD_SPEC.md`). Every RED check before this
one was per-file: schema_check reads one TSV, review_debt reads the workbook,
read_cap_check reads sizes. Nothing asked whether STATUS, the TSVs, CALENDAR and the
NEXUS brief AGREED. Measured at the S53 boot (commit 75e1b12b3): STATUS showed 10
open challenges against 6 in canon; three prediction tallies disagreed; FT-10 read
four ways; and RED's own 10:33 addendum skipped two mandatory steps (A2 SCRATCH,
A4->W3 CHANGELOG) with no instrument noticing. A cold reader did.

CHECKS (letters are the spec's):
  a  STATUS open-challenge table == the non-RESOLVED rows of workbook/CHALLENGES.tsv
     (ID set, lead grade token, status token, re-review M/D)
  b  prediction tally (CORRECT / WRONG / ACTIVE) derived from workbook/PREDICTIONS.tsv
     == every LIVE tally asserted on STATUS, CALENDAR and NEXUS_BRIEF
  c  registry `state` lead token + N-of-M beside its row in the STATUS trigger table;
     header "FT-NN n of m" claims == registry
  d  SCRATCH carries a stamp within 60 min of STATUS's newest stamp (addendum floor A2)
  e  if registry state / VX_HISTORY / STATUS weights changed vs the base ->
     thesis/CHANGELOG.md changed vs the base with its top entry dated today (A4->W3),
     and OUTBOX.md changed vs the base with its newest entry dated today (A4->W8)
  f  NEXUS_BRIEF and CALENDAR headers carry the same HOLD / net-bear as STATUS
  g  the existing instruments, delegated: schema_check · gen_trigger_scan --check ·
     read_cap_check --agent RED · STATUS <= 200 lines · review_debt --quiet ·
     claim_check weekday · ledger_staleness --nudge RED · memory_index_check (--slug)

VINTAGES. Default = the working tree, base = HEAD (what this session changed).
`--at <commit>` reads every surface from that commit and uses its parent as the base;
delegated instruments cannot run on a past vintage and are reported SKIPPED, never
silently omitted. This is how the gate is falsified: `--at 75e1b12b3` must FAIL on
a/b/c/d/e; `--at HEAD` after the repairs must be clean (test_closeout_check.py).

EXIT  0 clean · 1 findings · 2 INCOMPLETE (a check could not run — never a pass).

WHAT A PASS DOES NOT MEAN. It says the mirrors agree with canon and the floor steps
left their marks. It does not say a weight was right, a challenge was well graded, a
CHANGELOG entry explains anything, or the push landed (the safe-push receipt line is
the only proof of that). The MANUAL list is printed every run so it cannot be skipped
silently; a step not run is reported SKIPPED in the closeout message and the
headline is PARTIAL (charter § WRITE-BACK).

Never parse RED's TSVs with the csv module — split on tab (literal quotes in cells).
"""
import argparse
import datetime as dt
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
RED = 'AGENTS/RED'

STATE_TOKENS = ('FIRING-BANKED', 'FIRED-BANKED', 'UN-FIRED', 'ARMED', 'FIRED', 'BLOCKED')
GRADE_LEAD = re.compile(r'^(WEAK-MOD|WEAK|MODERATE-STRONG|MODERATE|STRONG|COMPELLING|CRITICAL|FAIL|PARTIALLY)\b')
STATUS_TOKEN = re.compile(r'^(ACTIVE|LIVE|RE-TARGETED|SUPERSEDED)[A-Z-]*$')
STAMP = re.compile(r'(\d{4}-\d{2}-\d{2})\s+(\d{1,2}):(\d[\dx])')
TALLY_LONG = re.compile(r'(\d+)\s*(CORRECT|WRONG|ACTIVE)\s*[/·]\s*(\d+)\s*(CORRECT|WRONG|ACTIVE)'
                        r'(?:\s*[/·]\s*(\d+)\s*(CORRECT|WRONG|ACTIVE))?')
TALLY_SHORT = re.compile(r'(\d+)\s*([CWA])\s*/\s*(\d+)\s*([CWA])(?:\s*/\s*(\d+)\s*([CWA]))?\b')
HISTORY_CUES = ('read ', 'said', 'lagged', 'was ', 'prior', 'old ', 'folded', 'superseded',
                'stale', 'uncounted', 'corrected', 'used to', 'formerly')
N_OF_M = re.compile(r'\b(\d+)[- ]of[- ](\d+)\b')
ID_CHG = re.compile(r'CHG-RED-\d{3}')


def git(*args):
    r = subprocess.run(['git', *args], cwd=ROOT, capture_output=True, text=True)
    return r.returncode, r.stdout


class Vintage:
    """One snapshot of RED's surfaces: the working tree, or a commit."""

    def __init__(self, at=None):
        self.at = at

    @property
    def label(self):
        return 'working tree' if self.at is None else self.at

    @property
    def base(self):
        return 'HEAD' if self.at is None else self.at + '^'

    def read(self, rel):
        p = f'{RED}/{rel}'
        if self.at is None:
            f = ROOT / p
            return f.read_bytes().decode('utf-8', 'replace') if f.exists() else None
        rc, out = git('show', f'{self.at}:{p}')
        return out if rc == 0 else None

    def read_base(self, rel):
        rc, out = git('show', f'{self.base}:{RED}/{rel}')
        return out if rc == 0 else None

    def today(self):
        if self.at is None:
            return dt.date.today().isoformat()
        rc, out = git('log', '-1', '--format=%ad', '--date=short', self.at)
        return out.strip() if rc == 0 else dt.date.today().isoformat()


def tsv(text):
    """header list + list of dict rows; split on TAB only."""
    lines = [l for l in text.replace('\r\n', '\n').split('\n') if l.strip()]
    lines = [l for l in lines if not l.startswith('#')]
    hdr = lines[0].split('\t')
    rows = []
    for l in lines[1:]:
        cells = l.split('\t')
        rows.append({hdr[i]: (cells[i] if i < len(cells) else '') for i in range(len(hdr))})
    return hdr, rows


def section(text, heading_prefix):
    """Body of the first '## <heading_prefix>…' section, up to the next '## '."""
    m = re.search(r'^## +' + re.escape(heading_prefix) + r'.*$', text, flags=re.M)
    if not m:
        return None
    rest = text[m.end():]
    n = re.search(r'^## ', rest, flags=re.M)
    return rest[:n.start()] if n else rest


def top_block(text):
    n = re.search(r'^## ', text, flags=re.M)
    return text[:n.start()] if n else text


def table_rows(body):
    for line in body.split('\n'):
        if line.startswith('|') and not re.match(r'^\|[\s\-:|]+\|$', line):
            cells = [c.strip() for c in line.strip().strip('|').split('|')]
            yield line, cells


def clean(cell):
    return cell.replace('**', '').replace('`', '').strip()


# ─────────────────────────────── a ───────────────────────────────
def check_challenges(v, F):
    canon = v.read('workbook/CHALLENGES.tsv')
    status = v.read('STATUS.md')
    if canon is None or status is None:
        F.append(('a', 'UNKNOWN', 'CHALLENGES.tsv or STATUS.md unreadable'))
        return
    _, rows = tsv(canon)
    open_rows = {r['CHG_ID']: r for r in rows if not r['Status'].startswith('RESOLVED')}
    body = section(status, 'OPEN CHALLENGES')
    if body is None:
        F.append(('a', 'FAIL', 'STATUS has no "## OPEN CHALLENGES" section'))
        return
    mirror = {}
    for line, cells in table_rows(body):
        m = ID_CHG.search(cells[0]) if cells else None
        if m:
            mirror[m.group(0)] = cells
    if set(mirror) != set(open_rows):
        F.append(('a', 'FAIL', 'open-challenge table lists %d row(s) %s but canon has %d non-RESOLVED row(s) %s'
                  % (len(mirror), sorted(mirror), len(open_rows), sorted(open_rows))))
    for cid in sorted(set(mirror) & set(open_rows)):
        cells = [clean(c) for c in mirror[cid]]
        r = open_rows[cid]
        canon_grade = GRADE_LEAD.match(r['Grade'].strip())
        canon_grade = canon_grade.group(1) if canon_grade else r['Grade'].split()[0]
        grade_cell = next((c for c in cells[1:] if GRADE_LEAD.match(c)), None)
        if grade_cell is None:
            F.append(('a', 'FAIL', '%s: no cell in its STATUS row starts with a grade token (canon %s)' % (cid, canon_grade)))
        elif GRADE_LEAD.match(grade_cell).group(1) != canon_grade:
            F.append(('a', 'FAIL', '%s: STATUS grade %r vs canon %r' % (cid, grade_cell[:30], canon_grade)))
        status_cell = next((c for c in cells[1:] if STATUS_TOKEN.match(c)), None)
        if status_cell is None:
            F.append(('a', 'FAIL', '%s: no cell in its STATUS row is a bare status token (canon %s)' % (cid, r['Status'])))
        elif status_cell != r['Status'].strip():
            F.append(('a', 'FAIL', '%s: STATUS status %r vs canon %r' % (cid, status_cell, r['Status'].strip())))
        d = re.match(r'(\d{4})-(\d{2})-(\d{2})', r['Resolved_Date'].strip())
        if d:
            want = '%d/%d' % (int(d.group(2)), int(d.group(3)))
            date_cells = [c for c in cells[1:] if re.fullmatch(r'\d{1,2}/\d{1,2}', c)]
            if not date_cells:
                F.append(('a', 'FAIL', '%s: STATUS row carries no bare re-review M/D cell (canon %s)' % (cid, want)))
            elif want not in date_cells:
                F.append(('a', 'FAIL', '%s: STATUS re-review %s vs canon %s' % (cid, date_cells[0], want)))


# ─────────────────────────────── b ───────────────────────────────
def derive_tally(pred_text):
    _, rows = tsv(pred_text)
    c = w = a = 0
    active, unk = [], []
    for r in rows:
        st = r['Status'].strip()
        if st == 'ACTIVE':
            a += 1
            active.append(r['Pred_ID'])
        elif st == 'RESOLVED':
            m = re.search(r'\b(CORRECT|WRONG)\b', r['Outcome'])
            if not m:
                unk.append(r['Pred_ID'])
            elif m.group(1) == 'CORRECT':
                c += 1
            else:
                w += 1
        else:
            unk.append(r['Pred_ID'])
    return (c, w, a), active, unk, len(rows)


def live_tallies(text):
    """(lineno, {C:n,W:n,A:n}, snippet) for every tally that is a LIVE claim."""
    out = []
    for i, line in enumerate(text.split('\n'), 1):
        for pat, short in ((TALLY_LONG, False), (TALLY_SHORT, True)):
            for m in pat.finditer(line):
                # A history cue on EITHER side retires the figure: "the 9/18 line read 9W/12C/1A"
                # puts it before, "(9W/12C/1A) lagged canon" puts it after. Falsified on NEXUS
                # vS52 line 31 at 75e1b12b3, which the before-only window flagged.
                around = (line[max(0, m.start() - 70):m.start()] + ' ' + line[m.end():m.end() + 40]).lower()
                if any(c in around for c in HISTORY_CUES):
                    continue
                g = m.groups()
                parts = {}
                for k in (0, 2, 4):
                    if g[k] is None:
                        continue
                    key = g[k + 1][0].upper()
                    parts[key] = int(g[k])
                if len(parts) < 2 or len(parts) != len([x for x in g[1::2] if x]):
                    continue
                out.append((i, parts, m.group(0)))
    return out


def check_tally(v, F):
    pred = v.read('workbook/PREDICTIONS.tsv')
    if pred is None:
        F.append(('b', 'UNKNOWN', 'PREDICTIONS.tsv unreadable'))
        return None
    derived, active, unk, n = derive_tally(pred)
    if unk:
        F.append(('b', 'FAIL', 'PREDICTIONS.tsv rows with no CORRECT/WRONG token or unknown Status: %s' % unk))
    want = {'C': derived[0], 'W': derived[1], 'A': derived[2]}
    for rel in ('STATUS.md', 'CALENDAR.md', 'NEXUS_BRIEF.md'):
        text = v.read(rel)
        if text is None:
            F.append(('b', 'UNKNOWN', '%s unreadable' % rel))
            continue
        found = live_tallies(text)
        if not found:
            F.append(('b', 'FAIL', '%s carries no live prediction tally (derived %dC/%dW/%dA)' % ((rel,) + derived)))
        for ln, parts, snip in found:
            bad = {k: (parts[k], want[k]) for k in parts if parts[k] != want[k]}
            if bad:
                F.append(('b', 'FAIL', '%s:%d asserts "%s" but canon derives %dC/%dW/%dA'
                          % ((rel, ln, snip.strip()) + derived)))
    return derived, active, n


# ─────────────────────────────── c ───────────────────────────────
def registry_states(text):
    _, rows = tsv(text)
    return {r['trigger_id']: r['state'].strip() for r in rows}


def lead_token(state):
    for t in STATE_TOKENS:
        if state.startswith(t):
            return t
    return state.split(';')[0].split()[0] if state else ''


def check_triggers(v, F):
    reg = v.read('registry/FALSIFICATION_TRIGGERS.tsv')
    status = v.read('STATUS.md')
    if reg is None or status is None:
        F.append(('c', 'UNKNOWN', 'registry or STATUS unreadable'))
        return
    states = registry_states(reg)
    body = section(status, 'FALSIFICATION CRITERIA')
    if body is None:
        F.append(('c', 'FAIL', 'STATUS has no "## FALSIFICATION CRITERIA" section'))
        return
    cells_by_id = {}
    for line, cells in table_rows(body):
        first = clean(cells[0])
        ids = re.findall(r'FT-(\d\d)', first)
        ids += re.findall(r'/\s*(\d\d)\b', first)
        if not ids or len(cells) < 2:
            continue
        for n in ids:
            cells_by_id['RED-FT-' + n] = clean(cells[1]) + ' | ' + clean(cells[2] if len(cells) > 2 else '')
    for tid, st in sorted(states.items()):
        tok = lead_token(st)
        cell = cells_by_id.get(tid)
        if cell is None:
            F.append(('c', 'FAIL', '%s (canon %r) has no row in the STATUS trigger table' % (tid, st)))
            continue
        if not re.search(r'\b' + re.escape(tok) + r'\b(?!-)', cell):
            F.append(('c', 'FAIL', '%s: STATUS cell %r lacks canon lead token %r' % (tid, cell[:60], tok)))
        m = N_OF_M.search(st)
        if m:
            want = re.compile(r'\b%s[- ]of[- ]%s\b' % (m.group(1), m.group(2)))
            if not want.search(cell):
                F.append(('c', 'FAIL', '%s: canon count %s-of-%s absent from STATUS cell %r'
                          % (tid, m.group(1), m.group(2), cell[:60])))
    head = top_block(status)
    for m in re.finditer(r'FT-(\d\d)\W{0,40}?\b(\d+) of (\d+)\b', head):
        tid = 'RED-FT-' + m.group(1)
        st = states.get(tid, '')
        c = N_OF_M.search(st)
        if not c:
            F.append(('c', 'FAIL', 'STATUS header claims %s "%s of %s" but canon state %r carries no count'
                      % (tid, m.group(2), m.group(3), st)))
        elif (c.group(1), c.group(2)) != (m.group(2), m.group(3)):
            F.append(('c', 'FAIL', 'STATUS header claims %s "%s of %s" but canon says %s-of-%s'
                      % (tid, m.group(2), m.group(3), c.group(1), c.group(2))))


# ─────────────────────────────── d ───────────────────────────────
def newest_stamp(text):
    best = None
    for m in STAMP.finditer(text):
        try:
            t = dt.datetime.strptime('%s %s:%s' % (m.group(1), m.group(2), m.group(3).replace('x', '0')),
                                     '%Y-%m-%d %H:%M')
        except ValueError:
            continue
        if best is None or t > best:
            best = t
    return best


def check_scratch(v, F):
    status, scratch = v.read('STATUS.md'), v.read('SCRATCH.md')
    if status is None or scratch is None:
        F.append(('d', 'UNKNOWN', 'STATUS or SCRATCH unreadable'))
        return
    s, c = newest_stamp(status), newest_stamp(scratch)
    if s is None or c is None:
        F.append(('d', 'FAIL', 'no parseable YYYY-MM-DD HH:MM stamp in %s' % ('STATUS' if s is None else 'SCRATCH')))
        return
    if c < s - dt.timedelta(minutes=60):
        F.append(('d', 'FAIL', 'SCRATCH newest stamp %s is %d min behind STATUS newest %s — the addendum floor (A2) was not written'
                  % (c.strftime('%Y-%m-%d %H:%M'), int((s - c).total_seconds() // 60), s.strftime('%Y-%m-%d %H:%M'))))


# ─────────────────────────────── e ───────────────────────────────
def weights_table(status):
    body = section(status, 'CURRENT ASSESSMENT') or ''
    out = {}
    for line, cells in table_rows(body):
        if len(cells) >= 2:
            m = re.match(r'(\d+)%', clean(cells[1]))
            if m and clean(cells[0]):
                out[clean(cells[0])] = int(m.group(1))
    return out


def check_state_change(v, F, today):
    changed = []
    reg_now, reg_base = v.read('registry/FALSIFICATION_TRIGGERS.tsv'), v.read_base('registry/FALSIFICATION_TRIGGERS.tsv')
    if reg_now is None:
        F.append(('e', 'UNKNOWN', 'registry unreadable'))
        return
    if reg_base is None or registry_states(reg_now) != registry_states(reg_base):
        changed.append('registry state')
    vx_now, vx_base = v.read('workbook/VX_HISTORY.tsv'), v.read_base('workbook/VX_HISTORY.tsv')
    if vx_now is not None and (vx_base is None or len(tsv(vx_now)[1]) != len(tsv(vx_base)[1])):
        changed.append('VX_HISTORY rows')
    st_now, st_base = v.read('STATUS.md'), v.read_base('STATUS.md')
    if st_now is not None and (st_base is None or weights_table(st_now) != weights_table(st_base)):
        changed.append('STATUS weights table')
    if not changed:
        return 'no registered state changed vs %s' % v.base
    cl_now, cl_base = v.read('thesis/CHANGELOG.md'), v.read_base('thesis/CHANGELOG.md')
    top = re.search(r'^## .*$', cl_now or '', flags=re.M)
    if cl_now is None or cl_now == cl_base or not top or today not in top.group(0):
        F.append(('e', 'FAIL', '%s changed vs %s but thesis/CHANGELOG.md %s (A4 -> W3 is mandatory)'
                  % (' + '.join(changed), v.base,
                     'is unchanged' if cl_now == cl_base else 'top entry is not dated %s: %r' % (today, (top.group(0)[:70] if top else '')))))
    ob_now, ob_base = v.read('OUTBOX.md'), v.read_base('OUTBOX.md')
    first = re.search(r'^## .*$', ob_now or '', flags=re.M)
    ymd = today.replace('-', '')
    if ob_now is None or ob_now == ob_base or not first or ymd not in first.group(0):
        F.append(('e', 'FAIL', '%s changed vs %s but OUTBOX.md %s (A4 -> W8 is mandatory; "they already know" is not routing)'
                  % (' + '.join(changed), v.base,
                     'is unchanged' if ob_now == ob_base else 'newest entry is not dated %s: %r' % (ymd, (first.group(0)[:70] if first else '')))))
    return 'changed vs %s: %s' % (v.base, ', '.join(changed))


# ─────────────────────────────── f ───────────────────────────────
PAIR_HN = re.compile(r'\bHOLD\s*(\d{2})\s*(?:[·/,]|and)\s*[Nn]et-bear\s*(\d{2})\b')
PAIR_NH = re.compile(r'\b[Nn]et-bear\s*(\d{2})\s*(?:[·/,]|and)\s*HOLD\s*(\d{2})\b')


def hold_netbear(text, n_lines=None):
    """The canonical PAIR ('HOLD 70 · net-bear 65' / 'net-bear 65 / HOLD 70') wins over a stray
    figure. Falsified on the gate's own first closeout (S54): the STATUS header line said
    'CALENDAR net-bear 60 vs 65 … HOLD 70 · net-bear 65' and first-match read 60."""
    head = top_block(text) if n_lines is None else '\n'.join(text.split('\n')[:n_lines])
    # EARLIEST pair in reading order wins: these headers put the newest claim first and quote
    # priors after it ("… net-bear 65 / HOLD 70 … Prior: … HOLD 70 / net-bear 58"). Trying the
    # HOLD-first form before the net-bear-first form read 58 off CALENDAR at HEAD (S54).
    pairs = [(m.start(), int(m.group(1)), int(m.group(2))) for m in PAIR_HN.finditer(head)]
    pairs += [(m.start(), int(m.group(2)), int(m.group(1))) for m in PAIR_NH.finditer(head)]
    if pairs:
        _, h, nb = min(pairs)
        return (h, nb)
    h = re.search(r'\b(?:HOLD|[Cc]onfidence)\s*(\d{2})\b', head)
    nb = re.search(r'\b[Nn]et-bear\s*(\d{2})\b', head)
    return (int(h.group(1)) if h else None, int(nb.group(1)) if nb else None)


def check_headers(v, F):
    status = v.read('STATUS.md')
    if status is None:
        F.append(('f', 'UNKNOWN', 'STATUS unreadable'))
        return None
    want = hold_netbear(status)
    if None in want:
        F.append(('f', 'FAIL', 'STATUS top block does not state both HOLD and net-bear (got %r)' % (want,)))
        return want
    for rel, n in (('NEXUS_BRIEF.md', 12), ('CALENDAR.md', 8)):
        text = v.read(rel)
        if text is None:
            F.append(('f', 'UNKNOWN', '%s unreadable' % rel))
            continue
        got = hold_netbear(text, n)
        if got != want:
            F.append(('f', 'FAIL', '%s header HOLD/net-bear %r vs STATUS %r' % (rel, got, want)))
    return want


# ─────────────────────────────── g ───────────────────────────────
def delegated(F, slugs):
    red = f'{RED}/'
    gates = [
        ('schema_check', ['python3', red + 'scripts/schema_check.py']),
        ('trigger_scan --check', ['python3', red + 'scripts/gen_trigger_scan.py', '--check']),
        ('read_cap RED', ['python3', 'scripts/read_cap_check.py', '--agent', 'RED']),
    ]
    if slugs:
        cmd = ['python3', 'scripts/memory_index_check.py', '--strict']
        for s in slugs:
            cmd += ['--slug', s]
        gates.append(('memory_index --slug', cmd))
    weekday_paths = [p for p in ('PROME/DOCKET.tsv', 'PROME/GATES.tsv', 'PROME/WILL_QUEUE.md',
                                 red + 'docket/CATALYSTS.tsv', red + 'CALENDAR.md', red + 'STATUS.md')
                     if (ROOT / p).exists()]
    advisory = [
        ('review_debt', ['python3', red + 'scripts/review_debt.py', '--quiet']),
        ('claim_check weekday', ['python3', 'scripts/claim_check.py', '--check', 'weekday', *weekday_paths]),
        ('ledger_nudge RED', ['python3', 'scripts/ledger_staleness.py', '--nudge', 'RED']),
        ('basis_check', ['python3', red + 'scripts/basis_check.py', '--check']),
    ]
    rows = []
    for kind, items in (('GATE', gates), ('ADVISORY', advisory)):
        for name, cmd in items:
            try:
                r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, timeout=180)
                out = (r.stdout + r.stderr).strip()
                rc = r.returncode
            except Exception as exc:                                   # noqa: BLE001
                out, rc = str(exc), 'ERROR'
            crashed = rc == 'ERROR' or 'Traceback (most recent call last)' in out
            lines = [l for l in out.split('\n') if l.strip()]
            if crashed:
                state = 'UNKNOWN'
                F.append(('g', 'UNKNOWN', '%s did not run cleanly (rc %s): %s' % (name, rc, (lines[-1] if lines else '')[:140])))
            elif rc == 0:
                state = 'PASS'
            elif kind == 'GATE':
                state = 'FAIL'
                F.append(('g', 'FAIL', '%s rc %s: %s' % (name, rc, ' | '.join(l[:110] for l in lines[-3:]))))
            else:
                state = 'ADVISORY'
            rows.append((kind, name, state, rc, lines))
    # STATUS line cap is RED's own rule (charter W1) — no instrument owns it elsewhere.
    n = len((ROOT / RED / 'STATUS.md').read_text(encoding='utf-8').split('\n'))
    rows.append(('GATE', 'STATUS <= 200 lines', 'PASS' if n <= 200 else 'FAIL', 'lines=%d' % n, []))
    if n > 200:
        F.append(('g', 'FAIL', 'STATUS.md is %d lines (cap 200, charter W1) — fold verbatim to reports/' % n))
    return rows


MANUAL = [
    ('W2', 'every DUE row dispositioned (boot.py §④ lists them); mechanism vs threshold kept separate'),
    ('W3', 'the CHANGELOG entry EXPLAINS old view -> new view (e only proves one exists)'),
    ('W6', 'workbook rows carry dated evidence; Flip_If graded against this session\'s data'),
    ('W7', 'transferable lesson -> memory/auto/ + index row (then re-run with --memory-slug)'),
    ('W8', 'OUTBOX content is routable; NEXUS_BRIEF refreshed LAST before the commit'),
    ('W9', 'any file/schema/tool/protocol change recorded in MAINTENANCE.md'),
    ('W10', 'safe-push receipt line "Pushed. CONFIRMED: HEAD <sha> is on origin/master (fresh fetch)." — the only proof of PUSHED'),
]


def main():
    ap = argparse.ArgumentParser(description='RED closeout check (read-only). Unknown flags refuse.')
    ap.add_argument('--at', metavar='COMMIT', help='check that commit\'s surfaces against its parent (delegated g SKIPPED)')
    ap.add_argument('--no-delegate', action='store_true', help='skip g (reported SKIPPED)')
    ap.add_argument('--memory-slug', action='append', default=[], help='auto-memory slug written this session (repeatable)')
    ap.add_argument('--quiet', action='store_true', help='findings and verdict only')
    a = ap.parse_args()

    v = Vintage(a.at)
    if a.at:
        rc, _ = git('rev-parse', '--verify', a.at + '^{commit}')
        if rc:
            print('CLOSEOUT-CHECK 2 CANNOT RUN: %r is not a commit' % a.at)
            return 2
    today = v.today()
    F = []
    if not a.quiet:
        print('=' * 76)
        print('  RED CLOSEOUT CHECK — vintage %s (base %s) — today %s' % (v.label, v.base, today))
        print('=' * 76)

    check_challenges(v, F)
    tally = check_tally(v, F)
    check_triggers(v, F)
    check_scratch(v, F)
    e_note = check_state_change(v, F, today)
    hb = check_headers(v, F)

    skipped = []
    g_rows = []
    if a.at or a.no_delegate:
        skipped.append('g delegated instruments (%s)' % ('--at vintage' if a.at else '--no-delegate'))
    else:
        g_rows = delegated(F, a.memory_slug)
    if not a.memory_slug and not a.at:
        skipped.append('g memory_index_check (no --memory-slug given — pass one per auto-memory written, or none were)')

    def state_of(letter):
        st = [s for l, s, _ in F if l == letter]
        return 'UNKNOWN' if 'UNKNOWN' in st else ('FAIL' if st else 'PASS')

    if not a.quiet:
        print('  a  challenge table == canon        %s' % state_of('a'))
        print('  b  prediction tally x3            %s%s' % (state_of('b'), '   derived %dC/%dW/%dA of %d rows, ACTIVE %s' % (tally[0] + (tally[2], ', '.join(tally[1]))) if tally else ''))
        print('  c  trigger states + header counts %s' % state_of('c'))
        print('  d  SCRATCH addendum floor         %s' % state_of('d'))
        print('  e  state change -> CHANGELOG+OUTBOX %s   %s' % (state_of('e'), e_note or ''))
        print('  f  NEXUS/CALENDAR HOLD, net-bear  %s%s' % (state_of('f'), '   STATUS HOLD %s / net-bear %s' % hb if hb else ''))
        if g_rows:
            print('  g  delegated instruments:')
            for kind, name, state, rc, lines in g_rows:
                print('     %-9s %-24s %-9s rc=%s' % (kind, name, state, rc))
                if state in ('ADVISORY', 'FAIL', 'UNKNOWN'):
                    for l in lines[-3:]:
                        print('        | ' + l[:140])
        if skipped:
            print('  SKIPPED (say so in the closeout message; the headline is then PARTIAL):')
            for s in skipped:
                print('     - ' + s)
        print('  MANUAL — unverifiable here, printed every run so they cannot be skipped silently:')
        for step, duty in MANUAL:
            print('     %-4s %s' % (step, duty))
        print()

    unknown = [f for f in F if f[1] == 'UNKNOWN']
    fails = [f for f in F if f[1] == 'FAIL']
    if F:
        print('  FINDINGS (%d):' % len(F))
        for letter, state, msg in F:
            print('    [%s] %s %s' % (letter, state, msg))
        print()
    if unknown:
        print('  ⛔ CLOSEOUT-CHECK 2 INCOMPLETE — %d check(s) could not run; an unrun check is not a pass.' % len(unknown))
        return 2
    if fails:
        print('  ❌ CLOSEOUT-CHECK 1 FAIL — %d finding(s). Fix at canon or regenerate the mirror; never edit the mirror by hand to match.' % len(fails))
        return 1
    scope = 'a-f' + (' + g' if g_rows else '')
    print('  ✅ CLOSEOUT-CHECK 0 PASS — scope %s on %s%s. A PASS certifies agreement and floor marks, not judgement.'
          % (scope, v.label, ('; SKIPPED: ' + '; '.join(skipped)) if skipped else ''))
    return 0


if __name__ == '__main__':
    sys.exit(main())
