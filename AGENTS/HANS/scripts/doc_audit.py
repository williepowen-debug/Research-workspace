#!/usr/bin/env python3
"""HANS documentation audit — catches the drift classes that have actually bitten this desk.

WHY THIS EXISTS (2026-09-05). Every documentation defect this desk has had was found
FROM OUTSIDE (WALTER x2, DAEDALUS x5) on a surface HANS had just written and therefore
trusted. The 9/5 session added two more of the same shape: a stale value-mirror deleted
from STATUS.md while its TWIN in CLAUDE.md was left standing, and three PMI FLASH values
carried as settled after the finals had published. Neither is subtle; both are invisible
without a mechanism, because a surface you just wrote reads as correct.

Checks, each tied to the incident that motivated it:
  C1 SPEC-MIRROR    CLAUDE.md's threshold table must carry BANDS, never live LEVELS.
  C2 SUPERSEDED     No value retired in workbook/PUBLISHED.tsv may appear in a
                    CURRENT-VALUE POSITION (registry current_value / VX Current_Value).
                    SERIES-QUALIFIED via PUBLISHED.tsv's `vectors` column — a bare-value
                    match flagged UK CPI 2.9% against EA HICP 2.9% on the first run.
  C3 REG-VS-VX      Mapped registry rows and their VX metric surfaces must agree,
                    PER LEG for compound two-leg rows.
  C4 DISPATCH       Every fired-log dispatch_artifact resolves AND lives in a RECIPIENT tree.
  C5 TSV            No ragged rows (a short row silently shifts every later column).
  C6 CAPS           STATUS.md within BOTH its line cap and the read-cap BYTE budget.
  C7 PATHS          Every `path/like/this` referenced in a boot-read surface resolves.
  C8 KB-STALE       No ACTIVE KB fact asserts a value retired for a metric it declares.

Exit 0 clean · 1 findings. Run at closeout and after any edit to a boot-read surface.
"""
import csv, re, sys
from pathlib import Path

HANS = Path(__file__).resolve().parent.parent
ROOT = HANS.parent.parent
STATUS_LINE_CAP, STATUS_BYTE_BUDGET = 250, 32_550

# Registry row -> its VX metric surface. Keep in sync with registry/README.md.
REG_VX = {
    'HANS-T-01': 'VX-HANS-8.06', 'HANS-T-02': 'VX-HANS-8.06',
    'HANS-T-05': 'VX-HANS-3.05', 'HANS-T-06': 'VX-HANS-3.06',
    'HANS-T-07': 'VX-HANS-8.01', 'HANS-T-08': 'VX-HANS-8.07',
    # COMPOUND rows carry a tuple, one surface PER LEG in registry order
    # ("spread / level"). T-09's level leg had NO surface until doc_audit C3 found it
    # on 2026-09-05 — the README's "every row names a metric surface" check maps ROWS,
    # not LEGS [[finding_relative_threshold_cannot_be_graded_by_a_one_sided_instrument]].
    'HANS-T-09': ('VX-HANS-3.01', 'VX-HANS-3.09'),
    'HANS-T-10': ('VX-HANS-3.02', 'VX-HANS-3.07'),
    'HANS-T-11': 'VX-HANS-2.01', 'HANS-T-13': 'VX-HANS-3.08',
}
# HANS-T-04 is deliberately absent: its as_of is the DECISION date (when the ECB set the
# rate) while VX Last_Updated is the VERIFICATION date. Different semantics, not a skew.

# Paths a boot-read surface names to say they DO NOT exist. Flagging these inverts the
# doc's meaning, so they are excluded by design, not by convenience.
KNOWN_ABSENT = {'archive/STATUS_PRE_REVIVAL_2026-06-22.md'}

def tsv(p):
    return list(csv.DictReader(open(HANS / p), delimiter='\t'))

def published():
    """PUBLISHED.tsv -> {metric: (current, [superseded])}, '#' lines skipped.
    Tie-break within a date is APPEND ORDER (matches scripts/consumer_check.read_ledger)."""
    raw = [l for l in (HANS / 'workbook/PUBLISHED.tsv').read_text().strip().split('\n')
           if l.strip() and not l.lstrip().startswith('#')]
    hdr = [h.strip().lower() for h in raw[0].split('\t')]
    im, iv, ia = hdr.index('metric'), hdr.index('value'), hdr.index('asof')
    ivec = hdr.index('vectors') if 'vectors' in hdr else None
    by, vecs = {}, {}
    for idx, l in enumerate(raw[1:]):
        r = l.split('\t')
        if len(r) <= max(im, iv, ia):
            continue
        by.setdefault(r[im], []).append((r[ia], idx, r[iv]))
        if ivec is not None and len(r) > ivec and r[ivec].strip():
            vecs.setdefault(r[im], set()).update(
                x.strip() for x in r[ivec].split(',') if x.strip())
    out = {}
    for m, e in by.items():
        e.sort()
        out[m] = (e[-1][2], [v for _, _, v in e[:-1]], sorted(vecs.get(m, ())))
    return out

def audit():
    f = []
    def bad(code, msg):
        f.append((code, msg))

    # ---- C1: the spec mirror carries bands, never levels -------------------
    claude = (HANS / 'CLAUDE.md').read_text()
    try:
        tbl = claude[claude.index('## KEY THRESHOLDS'):claude.index('## PMI → ISM')]
    except ValueError:
        tbl = ''
        bad('C1-STRUCT', 'CLAUDE.md: could not locate the KEY THRESHOLDS table')
    for i, line in enumerate(tbl.split('\n'), 1):
        if not line.startswith('|'):
            continue
        # A "(live: ...)" parenthetical is the exact form that went stale on 9/5.
        if re.search(r'\(live[:\s]', line, re.I):
            bad('C1-LIVE-VALUE', f'CLAUDE.md KEY THRESHOLDS row {i}: carries a live value — '
                                 'bands only; levels belong in registry/THRESHOLDS.tsv')

    # ---- C2: superseded values in a CURRENT-VALUE POSITION ------------------
    # SERIES-QUALIFIED, deliberately. Matching on the BARE VALUE flagged VX-HANS-4.08
    # (UK CPI 2.9%) against EA_FLASH_HICP_YOY_PCT 2.9% on its first run — two different
    # series, same digits. A check that cannot name the series is guessing
    # [[finding_unqualified_identifier_is_a_defect_waiting_for_a_reader]].
    pub, byvec = published(), {}
    for m, (_, olds, vecs) in pub.items():
        for v in vecs:
            byvec.setdefault(v, (m, set()))[1].update(o.strip() for o in olds)
    # registry: value_basis names the series, so threshold_id -> metric is 1:1 via REG_VX
    vx_of = REG_VX
    for r in tsv('registry/THRESHOLDS.tsv'):
        vid = vx_of.get(r['threshold_id'])
        if vid and vid in byvec:
            m, olds = byvec[vid]
            if r['current_value'].strip() in olds:
                bad('C2-SUPERSEDED', f"registry {r['threshold_id']}.current_value = "
                                     f"{r['current_value']!r}, retired for {m}")
    for r in tsv('workbook/VX.tsv'):
        if (r.get('Status') or '').upper().startswith(('FROZEN', 'RETIRED')):
            continue                      # parked rows keep their vintage BY DESIGN
        ent = byvec.get(r['Vector_ID'])
        if not ent:
            continue                      # no declared surface -> skip, never guess
        m, olds = ent
        if (r.get('Current_Value') or '').strip() in olds:
            bad('C2-SUPERSEDED', f"VX {r['Vector_ID']}.Current_Value = "
                                 f"{r['Current_Value']!r}, retired for {m}")

    # ---- C8: ACTIVE KB facts asserting a superseded value -------------------
    # PERIMETER GAP FOUND BY CODEX VIA PROME, 2026-09-05 — not by this script. C2 covered
    # registry and VX and stopped there, so three KB rows stayed ACTIVE asserting the PMI
    # flashes and a refuted "France stagnated" AFTER every headline surface was corrected,
    # with Stale_By dates weeks out so boot §[7] would not reach them either. A checker's
    # PERIMETER is a claim about where drift can live, and mine was wrong
    # [[finding_instrument_reports_clean_against_the_wrong_reference]].
    # Series-qualified the same way C2 is: a KB row is only checked against metrics whose
    # declared vector it names in its own Vectors cell.
    for r in tsv('workbook/KB.tsv'):
        if (r.get('Status') or '').strip().upper() != 'ACTIVE':
            continue                       # SUPERSEDED/RETIRED rows keep their text BY DESIGN
        vecs = {v.strip() for v in (r.get('Vectors') or '').split(',') if v.strip()}
        fact = r.get('Fact') or ''
        for vid in vecs & set(byvec):
            m, olds = byvec[vid]
            for o in olds:
                for hit in re.finditer(rf'(?<![\d.]){re.escape(o)}(?![\d.])', fact):
                    # MARKER-ADJACENCY, same discipline as scripts/consumer_check.py: a
                    # superseded value sitting next to a history word is a QUOTE, not an
                    # assertion, and quoting what you used to believe is exactly what a
                    # corrected row SHOULD do. Without this, C8 flags its own corrections.
                    ctx = fact[max(0, hit.start() - 60): hit.end() + 60].lower()
                    if re.search(r'flash|was |were |from |prior|previous|superseded|'
                                 r'corrected|retired|revised|earlier|until|\bold\b|'
                                 r'no longer|instead of|not \d', ctx):
                        continue
                    # DATE-ADJACENCY. "3.29% on 8/28" is a historical quote with no history
                    # WORD in it. Sound because the value is ALREADY on the superseded list:
                    # a retired value carrying its own date is by construction a citation of
                    # when it was true, not a claim that it still is.
                    tail = fact[hit.end(): hit.end() + 24]
                    if re.search(r'^\s*%?\s*(on|as of|at)?\s*[\[(]?\s*'
                                 r'(\d{1,2}/\d{1,2}|\d{4}-\d{2}-\d{2})', tail):
                        continue
                    bad('C8-KB-STALE', f"{r['ID']} is ACTIVE and asserts {o!r} "
                                       f"(retired for {m}, surface {vid})")

    # ---- C3: registry vs its metric surface ---------------------------------
    reg = {r['threshold_id']: r for r in tsv('registry/THRESHOLDS.tsv')}
    vx = {r['Vector_ID']: r for r in tsv('workbook/VX.tsv')}
    def eq(a, b):
        a, b = a.strip().rstrip('bp').strip(), b.strip().rstrip('bp').strip()
        try:
            return abs(float(a) - float(b)) < 1e-9
        except ValueError:
            return a == b
    for tid, vids in REG_VX.items():
        vids = (vids,) if isinstance(vids, str) else vids
        if tid not in reg:
            bad('C3-MISSING', f'{tid}: no registry row')
            continue
        legs = [x.strip() for x in reg[tid]['current_value'].split('/')]
        if len(legs) != len(vids):
            bad('C3-LEG-COUNT', f'{tid}: {len(legs)} leg(s) in current_value but '
                                f'{len(vids)} surface(s) mapped')
            continue
        for leg, vid in zip(legs, vids):
            if vid not in vx:
                bad('C3-MISSING', f'{tid} -> {vid}: no VX row')
            elif not eq(leg, vx[vid]['Current_Value']):
                bad('C3-REG-VS-VX', f'{tid} leg {leg!r} but {vid}={vx[vid]["Current_Value"]}')

    # ---- C4: dispatch records point INTO A RECIPIENT TREE and resolve -------
    for r in tsv('registry/HANS_T_FIRED_LOG.tsv'):
        da = (r.get('dispatch_artifact') or '').strip()
        if da in ('', 'none'):
            continue
        for p in [x.strip() for x in da.split(';') if x.strip()]:
            if p.startswith('AGENTS/HANS/'):
                bad('C4-SELF-DISPATCH', f"{r['fire_id']}: sender-tree path {p} — a dispatch "
                                        'record in your OWN tree can never be falsified')
            if not (ROOT / p).exists():
                bad('C4-DEAD', f"{r['fire_id']}: {p} does not exist")

    # ---- C5: ragged TSV rows -------------------------------------------------
    for name in ['registry/THRESHOLDS.tsv', 'registry/HANS_T_FIRED_LOG.tsv',
                 'workbook/KB.tsv', 'workbook/VX.tsv', 'workbook/FLOW.tsv',
                 'workbook/PREDICTIONS.tsv', 'workbook/ML.tsv', 'workbook/PUBLISHED.tsv']:
        rows = [l for l in (HANS / name).read_text().split('\n')
                if l.strip() and not l.lstrip().startswith('#')]
        n = len(rows[0].split('\t'))
        for i, l in enumerate(rows[1:], 2):
            if len(l.split('\t')) != n:
                bad('C5-RAGGED', f'{name} row {i}: {len(l.split(chr(9)))} cols vs header {n}')

    # ---- C6: BOTH caps on STATUS.md -----------------------------------------
    st = HANS / 'STATUS.md'
    nl, nb = len(st.read_text().split('\n')), len(st.read_bytes())
    if nl > STATUS_LINE_CAP:
        bad('C6-LINES', f'STATUS.md {nl} lines > {STATUS_LINE_CAP}')
    if nb > STATUS_BYTE_BUDGET:
        bad('C6-BYTES', f'STATUS.md {nb:,} B > {STATUS_BYTE_BUDGET:,} B read-cap budget '
                        '(the BYTE budget binds before the line cap — rewriting for '
                        'concision does not shrink it; rotate or split)')

    # ---- C7: referenced paths resolve ---------------------------------------
    pat = re.compile(r'`([A-Za-z0-9_][A-Za-z0-9_./-]*\.(?:md|tsv|py))`')
    for name in ['STATUS.md', 'CLAUDE.md', 'DISPATCH_LOG.md', 'registry/README.md']:
        base = (HANS / name).parent
        for m in pat.finditer((HANS / name).read_text()):
            p = m.group(1)
            if p in KNOWN_ABSENT or '/' not in p:   # bare filenames are prose shorthand
                continue
            if any((c / p).exists() for c in (base, HANS, ROOT)):
                continue
            bad('C7-DEAD-PATH', f'{name}: `{p}`')
    return f

def main():
    f = audit()
    print(f'HANS DOC AUDIT — {len(f)} finding(s)')
    print('=' * 72)
    for code, msg in f:
        print(f'  {code:18s} {msg}')
    if not f:
        print('  ✅ clean — spec mirror band-only · no superseded value in a current-value '
              'position · registry==VX · dispatch paths in recipient trees · TSVs square · '
              'STATUS within BOTH caps · paths resolve')
    return 1 if f else 0

if __name__ == '__main__':
    sys.exit(main())
