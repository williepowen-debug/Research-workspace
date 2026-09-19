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
  C6 CAPS           STATUS.md within BOTH its line cap and the read-cap BYTE
                    budget, AND CLAUDE.md within the byte budget — the charter is
                    auto-loaded whole every session and the FLEET checker cannot
                    see it, because it reads the charter to find other files.
  C7 PATHS          Every `path/like/this` referenced in a boot-read surface resolves.
  C8 KB-STALE       No ACTIVE KB fact asserts a value retired for a metric it declares.
  C10 BAND-STATE    A live VX row's Status must EQUAL the band function of its own
                    Current_Value. The column looks derived and was typed by hand:
                    VX-HANS-1.05 read GREEN at 348.4 against a Yellow of 350.0 — France's
                    first band crossing — and a packet went out on that row still calling
                    it green (ML-HANS-461).
  C11 DIRECTION     Every registry threshold must have a VX surface whose bands run in
                    the SAME direction. ZHAO's case proves C10 cannot catch this: their
                    PBOC rows agree with their bands perfectly and would read green if the
                    PBOC did nothing, because both bands only face one way. Here it caught
                    VX-HANS-4.01 carrying a CUTTING-cycle sign while HANS-T-04 fires
                    upward — a threshold and its own surface in opposite directions
                    (ML-HANS-462).

  LIMIT, PRE-REGISTERED SO NOTHING HERE IS OVER-TRUSTED: C10 and C11 both test the
  INSTRUMENT against itself. Neither asks whether a band exists on the side that would
  FALSIFY the thesis the row serves. That is a judgement, and on this desk it had exactly
  one instance before 2026-09-18 (HANS-T-01/T-02, the only two-sided pair).

  C9  STATUS-SUPERSEDED  (band-suppressed — see the pre-registered limit in the code)
                    C2's perimeter stopped at the registry and VX. STATUS.md — the
                    desk's LARGEST current-value surface and the one the operator reads —
                    was never scanned, and a superseded HICP figure sat there 17 days while
                    C2 reported zero findings every run (owed #15 since 9/18).
                    ⚠️ WHY IT WAS HARD AND HOW IT IS SOLVED: STATUS legitimately quotes dated
                    historical values all over, so a bare-value scan floods. A flooding check
                    trains you to skim, which is worse than no check. Discriminator, borrowed
                    from consumer_check: a superseded value is CLEARED when the CURRENT value
                    of the same metric appears on the same line (a correction or comparison),
                    or when the line carries an explicit history marker. Only an orphaned
                    superseded value — old number, no new number, no marker — is a finding.
  C12 ID-UNIQUE     Every workbook/registry TSV's key column must be UNIQUE. C5 tests that
                    rows are SQUARE, which is a DIFFERENT PROPERTY, so ML.tsv carried 95 IDs
                    shared by 246 rows with different findings for seven months and passed
                    every audit (ML-HANS-473). A duplicate key makes every citation to it
                    ambiguous and no squareness test can see it.
  C14 NO-NARRATIVE  STATUS.md must carry no per-session heading. The 2026-09-19 hot/cold
                    split moved narrative to SESSION_LOG.md; a split is a one-time edit and
                    the file regrows without a guard (91%->75% in three passes, back to 85%
                    within the hour). The contract is ENFORCED, not written down and trusted
                    — the day it was written also showed a written lesson failing to
                    transfer four commits later.
  C13 SCALE         A live VX row whose |value| is >8x its largest band, or <1/8 its smallest,
                    is a REFERENT MISMATCH — the value and the bands describe different
                    objects. VX-HANS-5.01 held EURO STOXX 50 (~6,486) against bands built for
                    SX7E (~268), a 27x gap: it could not fire under any market outcome, and
                    C10 and C11 BOTH PASSED because each operand was internally valid
                    (ML-HANS-465). Calibrated 2026-09-19 on 38 live rows: worst legitimate
                    ratio 3.65x, so 8x separates cleanly with 2.2x headroom.

Exit 0 clean · 1 findings. Run at closeout and after any edit to a boot-read surface.
"""
import csv, re, subprocess, sys
from pathlib import Path

# Dead-state PREFIXES — ONE shared notion of "parked" across this desk's guards
# (boot.py is_dead() uses the same set). PREFIX, never exact membership: a status
# cell is a canonical token optionally followed by a date and free prose
# (AGENTS/DAEDALUS/BLUEPRINTS/STATE_VOCABULARY.md Class 1). Legacy bare tokens stay
# recognised under canon's grandfathering rule, which a prefix test gives for free.
# C13 scale limit — |value| more than this multiple outside its own bands means the two
# describe DIFFERENT QUANTITIES. Module-level on purpose: a calibrated constant must be
# inspectable by a test, or the calibration is a claim nothing can check.
# Calibrated 2026-09-19 across 38 live VX rows: worst LEGITIMATE ratio 3.65x
# (VX-HANS-11.03, itself a known construct mismatch, owed #14). The defect it is built for
# measured 27x. 8.0 separates them with 2.2x headroom on the legitimate side.
SCALE_LIMIT = 8.0

KB_DEAD_PREFIXES = ("FROZEN", "RETIRED", "SUPERSEDED", "UNREACHABLE",
                    "ARCHIVED", "HISTORICAL", "NOT CURRENT", "DO NOT CITE", "NOT MAINTAINED")

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
    # Added 2026-09-18 with the core-inflation falsifiers (ML-HANS-462).
    'HANS-T-16': 'VX-HANS-4.11', 'HANS-T-17': 'VX-HANS-4.12',
}
# HANS-T-04 is deliberately absent FROM REG_VX: its as_of is the DECISION date (when the
# ECB set the rate) while VX Last_Updated is the VERIFICATION date. Different semantics,
# not a skew.
#
# 🔴 BUT THAT EXCLUSION IS SCOPED TO C3, AND IT LEAKED. When C11 was added on 2026-09-18
# it iterated REG_VX and therefore inherited a C3-only exemption — silently dropping
# HANS-T-04, which is THE ROW THE DIRECTIONAL DEFECT WAS ON (VX-HANS-4.01 carried a
# cutting-cycle sign while T-04 fires upward). An exclusion written for one check had
# quietly scoped a later one, exactly like C8's allowlist and C2's perimeter
# [[finding_guard_correctness_and_wiring_are_independent]]. C11 now iterates its OWN map.
# Rule: a new check DECLARES its perimeter; it never borrows another check's.
REG_VX_DIR = dict(REG_VX)
REG_VX_DIR['HANS-T-04'] = 'VX-HANS-4.01'   # direction IS comparable even when dates are not

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

def _ever_existed(relpath):
    """Did ANY commit ever add a file at this path?

    C4 asks 'was this fire DISPATCHED?' — delivery is an EVENT, so it is a
    question about HISTORY, not about live state. A historical diff cannot rot:
    the recipient's later `git mv` is a different commit and cannot reach into
    the one that added the file. Testing `.exists()` instead made this guard
    inherit the RECIPIENT's workflow as a hidden dependency, and on 2026-09-10
    it fired C4-DEAD twice on packets that were dead BECAUSE DELIVERY SUCCEEDED
    (BRENT consumes inbound mail into inbox/processed/).

    ⚠️ Globbing `processed/` too would only PATCH that: it leaves the dependency
    in place and widens it, so the next directory the recipient invents breaks it
    again. Diff-scoping REMOVES the dependency.
    (DAEDALUS 2026-09-10, runs/2026-09-10_INBOX_DISPOSITIONS.md ⑦. The discriminator:
    'did I author this?' / 'was this delivered?' => history => read the diff;
    'is this here NOW?' => live state => glob both and order by commit time.
    Pairing the wrong remedy to the question gives a guard that LOOKS hardened.)
    """
    try:
        out = subprocess.run(
            ['git', 'log', '--diff-filter=A', '--format=%h', '--', relpath],
            cwd=ROOT, capture_output=True, text=True, timeout=20)
    except (OSError, subprocess.SubprocessError):
        return None          # git unavailable => UNKNOWN, never a silent pass
    if out.returncode != 0:
        return None
    return bool(out.stdout.strip())


def _audit_full():
    f = []
    info = []
    def bad(code, msg):
        f.append((code, msg))
    def note(code, msg):
        info.append((code, msg))

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
        if (r.get('Status') or '').upper().startswith(KB_DEAD_PREFIXES):
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
    # ⚠️ SCOPE TEST REWRITTEN 2026-09-18 — IT WAS AN ALLOWLIST OF ONE TOKEN.
    # The old line read `if Status != 'ACTIVE': continue`, whose COMMENT said it was
    # skipping dead rows but whose CODE skipped every row not spelled exactly ACTIVE.
    # Intent and implementation disagreed, and the gap was every live-but-differently-
    # labelled row: 2 CORRECTED + 2 CONFIRMED rows had never been checked, and on
    # 2026-09-18 this desk added 3 more by inventing EXPIRED-NOT-REFRESHED to describe
    # a stale row more precisely — which silently REMOVED it from this check.
    # Describing a row better must never desupervise it
    # [[finding_status_token_membership_test_desupervises_improved_rows]].
    # Now a DENYLIST of dead-state PREFIXES, matching boot.py's is_dead() and fleet
    # canon (STATE_VOCABULARY.md Class 1: canonical token, then free prose).
    # UNKNOWN TOKENS ARE CHECKED, not skipped — an unrecognised label must fail loud.
    for r in tsv('workbook/KB.tsv'):
        if (r.get('Status') or '').strip().upper().startswith(KB_DEAD_PREFIXES):
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
                    # print the ROW'S OWN status, not the word "ACTIVE": since
                    # 2026-09-18 this check supervises every non-dead row, so a
                    # hardcoded "is ACTIVE" would misdescribe a CORRECTED/CONFIRMED
                    # row and send the reader looking for a status it does not have.
                    bad('C8-KB-STALE', f"{r['ID']} is {(r.get('Status') or '?').strip()!s} and asserts {o!r} "
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
            if (ROOT / p).exists():
                continue
            # Missing NOW. That alone says nothing about delivery — ask history.
            ever = _ever_existed(p)
            if ever is None:
                bad('C4-UNKNOWN', f"{r['fire_id']}: {p} missing and git could not be "
                                  'consulted — UNKNOWN, not clean (fail closed)')
            elif ever:
                moved = sorted(x.relative_to(ROOT).as_posix()
                               for x in ROOT.glob(f'AGENTS/*/**/{Path(p).name}'))
                where = f' — now at {moved[0]}' if moved else ''
                note('C4-MOVED', f"{r['fire_id']}: {p} was DELIVERED (a commit added it) "
                                 f'and the recipient has since moved it{where}. Not a '
                                 'defect; re-point the ledger when convenient')
            else:
                bad('C4-DEAD', f"{r['fire_id']}: {p} was NEVER added in any commit — "
                               'not a moved file, an undelivered or wrong path')

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

    # ---- C6: BOTH caps on STATUS.md, AND the byte cap on CLAUDE.md ----------
    st = HANS / 'STATUS.md'
    nl, nb = len(st.read_text().split('\n')), len(st.read_bytes())
    if nl > STATUS_LINE_CAP:
        bad('C6-LINES', f'STATUS.md {nl} lines > {STATUS_LINE_CAP}')
    if nb > STATUS_BYTE_BUDGET:
        bad('C6-BYTES', f'STATUS.md {nb:,} B > {STATUS_BYTE_BUDGET:,} B read-cap budget '
                        '(the BYTE budget binds before the line cap — rewriting for '
                        'concision does not shrink it; rotate or split)')

    # CLAUDE.md, added 2026-09-18. The fleet checker scripts/read_cap_check.py OPENS
    # this file only to discover which OTHER surfaces to weigh, and never weighs it —
    # so the charter, which the harness loads WHOLE at every single session start, was
    # the one surface nothing measured. It stood at 32,961 B against a 32,550 B budget
    # and reported "1 file assessed, 0 over budget" all session
    # [[finding_instrument_reports_clean_against_the_wrong_reference]].
    # Checked HERE because scripts/ at the repo root is not this desk's to edit; the
    # fleet-level gap is flagged to PROME, not patched locally.
    cb = len((HANS / 'CLAUDE.md').read_bytes())
    if cb > STATUS_BYTE_BUDGET:
        bad('C6-CHARTER-BYTES', f'CLAUDE.md {cb:,} B > {STATUS_BYTE_BUDGET:,} B read-cap '
                                'budget, and it is auto-loaded WHOLE every session — a '
                                'stronger case for the cap than any boot-step read. '
                                'Rotate narrative to CHARTER_PROVENANCE.md; keep rules')
    elif cb > int(STATUS_BYTE_BUDGET * 0.75):
        note('C6-CHARTER-ROTATE', f'CLAUDE.md {cb:,} B is past 75% of the budget — '
                                  'rotate-tier. Stopping at the trigger is not finishing')

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
    # ---- C10: a VX Status must EQUAL the band function of its own value -----
    # The column is a FUNCTION of the four cells beside it and was maintained by hand.
    # Found because a PEER asked about an unrelated instrument [[ML-HANS-461]].
    # Rows whose status is a compound token or NA-WRONG-UNIT are exempt BY NAME, never
    # by silence: an exemption that is not enumerated is indistinguishable from a bug.
    # DELIBERATELY EMPTY. Two exemptions were written here on 2026-09-18 and BOTH were
    # removed within the hour, for the same reason: each named a defect and then excused
    # it. VX-HANS-3.05 was 'a compound token, not a plain band colour' — the token
    # overstated the fired tier and C10 was right. VX-HANS-1.04 was 'bands ordinally
    # broken... fixing it is a separate decision' — it was not a separate decision, it
    # was the fix, deferred 64 days. An exemption written to quiet a flag is how a defect
    # gets laundered [[finding_a_flag_resolved_in_the_wrong_direction_launders_the_defect]].
    # Anything added here must name a property of the SCHEMA, never of a row's content.
    BAND_EXEMPT = {}
    for r in tsv('workbook/VX.tsv'):
        vid = r['Vector_ID']
        st = (r.get('Status') or '').strip().upper()
        if st.startswith(KB_DEAD_PREFIXES) or st.startswith('NA-WRONG-UNIT'):
            continue
        if vid in BAND_EXEMPT:
            note('C10-EXEMPT', f'{vid}: {BAND_EXEMPT[vid]}')
            continue
        try:
            v, y, o_, rd = (float(r['Current_Value']), float(r['Yellow']),
                            float(r['Orange']), float(r['Red']))
        except (ValueError, KeyError):
            continue                      # non-numeric band => not gradeable here
        if y > o_ > rd:                   # descending: LOWER is worse
            exp = 'RED' if v <= rd else 'ORANGE' if v <= o_ else 'YELLOW' if v <= y else 'GREEN'
        elif y < o_ < rd:                 # ascending: HIGHER is worse
            exp = 'RED' if v >= rd else 'ORANGE' if v >= o_ else 'YELLOW' if v >= y else 'GREEN'
        else:
            bad('C10-NON-MONOTONE', f'{vid}: bands {y}/{o_}/{rd} are not monotone, so no '
                                    'state can be derived — the band is the defect')
            continue
        if not st.startswith(exp):
            bad('C10-BAND-STATE', f'{vid}: Status={st!r} but value {v} against bands '
                                  f'{y}/{o_}/{rd} is {exp}')

    # ---- C9: superseded values sitting in STATUS.md ------------------------
    # Owed since 2026-09-18. C2 covers registry + VX; STATUS.md is the biggest
    # current-value surface on the desk and was never scanned.
    # ⚠️ THE WHOLE DESIGN PROBLEM IS FALSE POSITIVES, not detection. STATUS quotes dated
    # history constantly and a bare-value scan would flood — and a flooding check gets
    # skimmed, which is strictly worse than no check
    # [[finding_a_check_that_only_advises_is_overridden_the_control_is_downstream]].
    # 🔴 v2, 2026-09-19, after CATO supplied four counterexamples against v1:
    #  · v1 MISSED ITS OWN MOTIVATING DEFECT — a current assertion of the retired 3.3%
    #    HICP passed, because a 'bare 2-sig-fig' noise floor excluded it. A filter written
    #    to cut noise had removed the exact class the check was built for.
    #  · a UNICODE MINUS (U+2212) slipped every match: '−19.7pp' invisible, '-19.7pp' caught.
    #  · ARROWS counted as history markers, so '... -19.7pp -> watch it' suppressed. An arrow
    #    is not a claim about time, and old→new is already covered by the current-value rule.
    #  · markers matched ANYWHERE on the line, so one 'was' 200 chars away silenced a live
    #    figure. Markers must now sit within PROX characters of the number.
    HIST_MARK = re.compile(
        r'supersed|corrected|correction|rotated|historical|\bwas\b|\bprior\b|previously|'
        r'\bformer\b|retired|\bcarried\b|\bhad\b|no longer|withdrawn', re.I)
    PROX = 60
    # A metric's unit is the only attribution prose offers. '85' matches any bp metric;
    # '85bp' does not. Suffix -> the unit that must follow the number.
    UNIT_OF = (('_PCT', '%'), ('_BP', 'bp'), ('_PP', 'pp'), ('_EUR_BN', 'bn'), ('_TWH', 'TWh'))
    # ⚠️ IRREDUCIBLE LIMIT, PRE-REGISTERED: C2 attributes a value to a metric via
    # PUBLISHED.tsv's `vectors` column. PROSE HAS NO SUCH COLUMN, so a SHORT number cannot
    # be attributed — on 2026-09-19 a live '2.9%' was GERMAN CPI, a different series that
    # happens to equal a retired EA/UK value. Short numbers therefore report as an ADVISORY
    # NOTE; only distinctive ones (>=3 significant digits) are blocking FINDINGS. Reporting
    # both as findings cries wolf; reporting neither is exactly what v1 did.
    # PERIMETER, STATED: the same boot-read set C7 walks, not STATUS.md alone. Scoping a
    # new check to the one file that motivated it is how C2's perimeter came to be wrong —
    # "a checker's PERIMETER is a claim about where drift can live" (C8's own docstring).
    # CHARTER_PROVENANCE.md joins the set because the 9/18 rotation moved live reasoning
    # into it, so it is now a place a stale figure can hide.
    C9_SURFACES = ['STATUS.md', 'CLAUDE.md', 'DISPATCH_LOG.md', 'CHARTER_PROVENANCE.md',
                   'LAST_COMPLETION.md']
    # A surface that DECLARES ITSELF a statement-time record is out of scope, and the
    # declaration is READ FROM THE FILE rather than hardcoded here — DISPATCH_LOG.md's own
    # header says "APPEND-ONLY, AND EVERY ROW IS A STATEMENT-TIME RECORD ... never
    # re-valued afterwards", which makes its old figures CORRECT HISTORY, exactly like a
    # dated ledger row under closeout 9c. Hardcoding the skip would rot the moment the file
    # changed character; reading its header cannot [[finding_read_the_artifacts_own_header_first]].
    # The skip is NOTED, never silent — an invisible exclusion is how a perimeter goes wrong.
    def _is_statement_time_record(txt):
        head = '\n'.join(txt.split('\n')[:15]).upper()
        return 'APPEND-ONLY' in head and 'STATEMENT-TIME' in head

    for _surface in C9_SURFACES:
      st_path = HANS / _surface
      if st_path.exists() and _is_statement_time_record(st_path.read_text(encoding='utf-8')):
          note('C9-SKIP-RECORD', f'{_surface}: self-declared APPEND-ONLY statement-time '
                                 f'record — old values are correct history, not drift')
      elif st_path.exists():
          pub9 = published()
          live_vx = {r['Vector_ID'] for r in tsv('workbook/VX.tsv')
                     if not (r.get('Status') or '').upper().startswith(KB_DEAD_PREFIXES)}
          # 🔴 BAND SUPPRESSION — added on C9's FIRST RUN, which produced exactly one hit and
          # it was FALSE. STATUS.md:85 '>4.50 level leg' is HANS-T-10's OAT trip line; it
          # matched only because BOE_BANK_RATE_PCT once stood at 4.50. In free prose there is
          # no `vectors` column to series-qualify against, so C2's discriminator is unavailable
          # and a bare number can belong to any metric.
          # The rule that resolves it is already this desk's canon: A BAND IS A LINE, NOT A
          # LEVEL (root CLAUDE.md: "A BAND belongs here; a LEVEL never does"), and PROME's
          # L441 sharpening says the same — FLAG THE YARDSTICK, NEVER THE LINE IT IS MEASURED
          # AGAINST. So a number that IS a registered band is never a stale reading.
          # ⚠️ PRE-REGISTERED LIMIT: if a genuinely stale LEVEL happens to equal a registered
          # BAND, C9 goes quiet on it. That is a real hole and it is named rather than
          # discovered later. It is bounded — such a value is by construction sitting exactly
          # on a trip line, where C10/C13 and the fired-log are already looking.
          band_nums = set()
          for _r in tsv('registry/THRESHOLDS.tsv'):
              band_nums.update(re.findall(r'-?\d+\.?\d*', _r.get('band', '') or ''))
          _txt = st_path.read_text(encoding='utf-8').replace('\u2212', '-')
          for ln, line in enumerate(_txt.split('\n'), 1):
              if not line.strip() or line.lstrip().startswith('|---'):
                  continue
              for metric, (cur, olds, vecs) in pub9.items():
                  # series-qualified exactly like C2: only metrics with a LIVE declared surface
                  if not vecs or not (set(vecs) & live_vx):
                      continue
                  _u = next((u for suf, u in UNIT_OF if metric.endswith(suf)), None)
                  for old in set(olds):
                      o = old.strip()
                      _mm = re.search(r'(?<![\d.])' + re.escape(o) + r'(?![\d])', line)
                      if not _mm:
                          continue
                      if re.search(r'(?<![\d.])' + re.escape(cur.strip()) + r'(?![\d])', line):
                          continue          # CLEARED: new value on the same line
                      if o.lstrip('-') in band_nums or o in band_nums:
                          continue          # CLEARED: it is a registered BAND, i.e. a LINE
                      # UNIT GATE: a metric's unit is the only attribution prose offers.
                      # '85' matches any bp metric; '85bp' does not.
                      if _u and not re.match(r'\s{0,2}' + re.escape(_u),
                                             line[_mm.end():_mm.end() + 6]):
                          continue          # CLEARED: no matching unit -> not this metric
                      # markers must sit NEAR the number: one 'was' 200 chars away had
                      # been silencing live figures.
                      if HIST_MARK.search(line[max(0, _mm.start() - PROX):_mm.end() + PROX]):
                          continue          # CLEARED: marked as history, near the number
                      _msg = (f'{_surface}:{ln} carries {o!r}, retired for {metric} '
                              f'(current {cur.strip()!r}) with no new value, no history marker')
                      if len(o.replace('-', '').replace('.', '').lstrip('0')) >= 3:
                          bad('C9-STATUS-SUPERSEDED', _msg)
                      else:
                          note('C9-SHORT-NUMBER', _msg + ' - SHORT number: prose cannot attribute '
                               'it to a metric (a live 2.9% was GERMAN CPI, not the retired '
                               'EA/UK value). LOOK, do not assume')

    # ---- C14: STATUS must not re-accumulate session narrative ---------------
    # The hot/cold split (owed #20, 2026-09-19) moved session narrative to SESSION_LOG.md.
    # 🔴 A SPLIT IS A ONE-TIME EDIT; WITHOUT A GUARD THE FILE JUST REGROWS — three rotation
    # passes that morning took STATUS 91% -> 75% and it was back to 85% within the hour.
    # Today also proved a WRITTEN contract does not transfer: the same defect recurred four
    # commits after I wrote it up. So the contract is enforced here rather than trusted.
    st = HANS / 'STATUS.md'
    if st.exists():
        for ln, line in enumerate(st.read_text(encoding='utf-8').split('\n'), 1):
            # ⚠️ v1 of this regex was `^#{2,3}\s.*\bSESSION\s*\d` and it FIRED FALSE on its
            # first run: the INBOX heading reads "(session 1; not re-processed s2–s4)", a
            # legitimate section that merely MENTIONS a session. The guard must test what a
            # heading IS ABOUT, not what it mentions — so the subject is read from the START
            # of the heading text, after stripping emoji and markers.
            # Second guard today whose v1 failed on first run (C9's first hit was also false)
            # [[finding_test_the_guard_not_just_the_guarded]].
            _h = re.match(r'^#{2,3}\s+(.*)$', line)
            _subj = re.sub(r'^[^0-9A-Za-z]+', '', _h.group(1)) if _h else ''
            if re.match(r'SESSIONS?\s*\d', _subj, re.I):
                bad('C14-STATUS-NARRATIVE',
                    f'STATUS.md:{ln} has a per-session heading — session narrative belongs '
                    f'in SESSION_LOG.md. STATUS carries STATE and decision-relevant caveats; '
                    f'a CARRY FORWARD block is fine, a session block is not: {line.strip()[:70]!r}')

    # ---- C12: a key column must be UNIQUE, which C5 does not test -----------
    # C5 asks "are the rows SQUARE". Squareness and key-uniqueness are different
    # properties, and the file that failed was square [[ML-HANS-473]].
    for rel, keycol in (('workbook/ML.tsv', 'Entry_ID'),
                        ('workbook/VX.tsv', 'Vector_ID'),
                        ('workbook/KB.tsv', 'ID'),
                        ('registry/THRESHOLDS.tsv', 'threshold_id')):
        fp = HANS / rel
        if not fp.exists():
            continue
        seen, dup = set(), []
        for r in tsv(rel):
            k = (r.get(keycol) or '').strip()
            if not k:
                continue
            (dup.append(k) if k in seen else seen.add(k))
        if dup:
            u = sorted(set(dup))
            # ML.tsv's Feb-2026 bulk load is a KNOWN, MEASURED, REGISTERED backlog (owed
            # #23). It is reported as a COUNT so it can never read as clean, and is not
            # re-listed row by row every run — but a NEW collision above the legacy ceiling
            # must still be loud, so the ceiling is asserted, never assumed.
            if rel == 'workbook/ML.tsv':
                # 🔴 WAS `>= 400`, WHICH AMNESTIED EVERY OLD ID RATHER THAN THE RECORDED
                # COLLISIONS. CATO counterexample 2026-09-19: duplicating the previously
                # UNIQUE ML-HANS-001 took the duplicate groups 95 -> 96 and produced NO
                # finding, because 001 < 400. An exemption must name the accepted FACTS,
                # never a range that happens to contain them (RULE #1d).
                _fz = HANS / 'registry/ML_LEGACY_DUP_IDS.txt'
                frozen = ({l.strip() for l in _fz.read_text().split('\n')
                           if l.strip() and not l.startswith('#')} if _fz.exists() else set())
                newdup = sorted(set(u) - frozen)
                if newdup:
                    bad('C12-ID-DUPLICATE',
                        f'{rel}: duplicate {keycol}(s) NOT in the frozen legacy set: {newdup}')
                elif u:
                    note('C12-LEGACY-DUP',
                         f'{rel}: {len(u)} duplicate {keycol}(s), all in the FROZEN set '
                         f'(registry/ML_LEGACY_DUP_IDS.txt) - owed #23, not renumbered')
            else:
                bad('C12-ID-DUPLICATE', f'{rel}: duplicate {keycol}(s): {u}')

    # ---- C13: value and bands that describe DIFFERENT OBJECTS ---------------
    # C10 and C11 compare a row's fields to EACH OTHER, so both pass when the pair is
    # internally consistent and jointly wrong. This asks a question neither can:
    # is the value even the same KIND of quantity as its bands? [[ML-HANS-465]]
    for r in tsv('workbook/VX.tsv'):
        if (r.get('Status') or '').upper().startswith(KB_DEAD_PREFIXES):
            continue
        try:
            v = abs(float(str(r.get('Current_Value', '')).replace(',', '').strip()))
            bands = [abs(float(r[c])) for c in ('Yellow', 'Orange', 'Red')]
        except (ValueError, TypeError, KeyError):
            continue                      # qualitative rows are not in scope
        nz = [b for b in bands if b]
        if not v or not nz:
            continue                      # a zero band or zero value is not a scale claim
        ratio = max(v / max(nz), min(nz) / v)
        if ratio > SCALE_LIMIT:
            bad('C13-SCALE',
                f"{r['Vector_ID']} value {v:g} is {ratio:.1f}x outside its own bands "
                f"{bands} — value and bands look like DIFFERENT QUANTITIES; the row "
                f"may be unable to fire under any outcome")

    # ---- C11: a threshold and its metric surface must face the SAME way -----
    # C10 passes a row that agrees with a band pointing the wrong way, so this is a
    # SEPARATE test, not a stricter one. ZHAO 2026-09-18 supplied the proof.
    def _band_dir(txt):
        """Direction a registry band fires in, from its own text. None = undecidable."""
        t = (txt or '')
        up, dn = ('>' in t), ('<' in t)
        return 'UP' if up and not dn else 'DOWN' if dn and not up else None
    DIR_EXEMPT = {
        'HANS-T-02': 'THE ONLY TWO-SIDED METRIC ON THIS DESK. T-01 (<47) and T-02 (>52) '
                     'both map to VX-HANS-8.06, whose bands serve the WEAKNESS leg; T-02 '
                     'is the KILL-side threshold and the three band columns cannot hold a '
                     'second direction. The flag is the SCHEMA LIMIT, not a defect — and '
                     'T-02 is MET, having correctly killed the ISM-weakness leg.',
        'HANS-T-08': 'registry states a MAGNITUDE (">15pp below norm") while the surface '
                     'carries a SIGNED value (currently -15.99). Same quantity, and the band '
                     'text now says so explicitly; a text parse cannot resolve magnitude vs '
                     'sign. NOTE the exemption is about the SCHEMA (magnitude vs sign), not '
                     'about any particular value — it must not be read as blessing a level.',
    }
    for tid, vids in REG_VX_DIR.items():
        if tid not in reg:
            continue
        if tid in DIR_EXEMPT:
            note('C11-EXEMPT', f'{tid}: {DIR_EXEMPT[tid]}')
            continue
        rdir = _band_dir(reg[tid]['band'])
        if rdir is None:
            continue                      # compound / qualitative band — not gradeable
        for vid in ((vids,) if isinstance(vids, str) else vids):
            vr = vx.get(vid)
            if not vr:
                continue
            try:
                y, o_, rd = float(vr['Yellow']), float(vr['Orange']), float(vr['Red'])
            except (ValueError, KeyError):
                continue
            vdir = 'DOWN' if y > o_ > rd else 'UP' if y < o_ < rd else None
            if vdir and vdir != rdir:
                bad('C11-DIRECTION', f'{tid} band {reg[tid]["band"]!r} fires {rdir} but its '
                                     f'surface {vid} has bands {y}/{o_}/{rd} running {vdir} '
                                     '— threshold and metric surface face opposite ways')

    return f, info


def audit():
    """Findings only — the historical signature. Five callers in test_hans.py
    unpack this as a flat list; changing it under them broke all five on
    2026-09-10, which is its own small lesson about interfaces. INFO states are
    NOT findings and are read via audit_full()."""
    return _audit_full()[0]

def main():
    f, info = _audit_full()
    print(f'HANS DOC AUDIT — {len(f)} finding(s)')
    print('=' * 72)
    for code, msg in f:
        print(f'  {code:18s} {msg}')
    for code, msg in info:
        print(f'  {code:18s} {msg}')   # INFO — a visible STATE, not a finding
    if not f:
        print('  ✅ clean — spec mirror band-only · no superseded value in a current-value '
              'position · registry==VX · dispatch paths in recipient trees · TSVs square · '
              'STATUS within BOTH caps · paths resolve')
    if info:
        print(f'  ({len(info)} informational state(s) above — not counted as findings)')
    return 1 if f else 0

if __name__ == '__main__':
    sys.exit(main())
