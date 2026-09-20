#!/usr/bin/env python3
"""Read-only SAM closeout check — enumerate every closeout obligation, and
mechanically verify the ones that can be verified.

WHY THIS EXISTS (2026-09-19). SAM's closeout obligations live in TWO documents
under TWO framings that never cross-reference each other:

  * root CLAUDE.md  -> "**At session end:**"  steps 1, 1b, 1c, 1c-bis, 1d, 1e, 2, 3
                       — every one of these already has a script.
  * AGENTS/SAM/CLAUDE.md -> "### Write-back" steps 9-14, sitting inside
                       "## SPAWN PROTOCOL" between "### Execute" and "### Git",
                       and NEVER described there as a closeout
                       — none of these had a script.

On 2026-09-19 a grading session ran all 7 instrumented steps correctly and
skipped write-back step 10 (update the docket; keep CALENDAR and CATALYSTS in
sync). Four resolved Sep-18 rows were left in the FORWARD table, one still
reading "SAM-28 and SAM-31 remain OPEN" — and boot step 3 sends the next session
to read exactly those rows. Re-syncing then exposed a SECOND divergence from a
PRIOR session: CATALYSTS.tsv still held five 2026-09-16/17 rows CALENDAR had
already pruned. Nothing detected either one; a human question did.

The split is the mechanism, and it is worth stating because it predicts the next
miss: the docket-pruning duty is actually written in BOOT step 3 ("undated/past
rows are pruned at closeout"), ~49 lines away from write-back step 10 that owns
it. An obligation stated in the read phase and owed in the write phase is
discoverable at neither.

⛔ WHAT A PASS DOES *NOT* MEAN. This checks structure, not judgement. A PASS says
the docket is internally consistent and the derived counts agree — NOT that the
right events were added, that a thesis change was correctly declined, that the
brief says anything true, or that the session's analysis was sound. Steps marked
MANUAL below are unverifiable here by construction and are printed every run so
they cannot be silently skipped.

Usage:
  python3 AGENTS/SAM/scripts/closeout_check.py            # full run, exit 1 on failure
  python3 AGENTS/SAM/scripts/closeout_check.py --list     # enumerate steps only
  python3 AGENTS/SAM/scripts/closeout_check.py --no-delegate   # self-checks only
  python3 AGENTS/SAM/scripts/closeout_check.py --pre-commit    # early advisory: skips F and G

⛔ RUN ORDER. The full run belongs AFTER your final commit and BEFORE safe-push:
check G wants a clean tree and check F reads committed history, so running it with
work still uncommitted can only ever fail. Use --pre-commit for an early look.
"""
import csv
import json
import hashlib
import io
import re
import subprocess
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SAM = ROOT / 'AGENTS' / 'SAM'

# (step, where it is written, one-line duty, how it is covered here)
STEPS = [
    ('9',        'SAM §Write-back', 'Write results back to STATUS.md',                      'DELEGATED read_cap_check.py (size only; content is MANUAL)'),
    ('10',       'SAM §Write-back', 'Update docket/; prune past; CALENDAR<->CATALYSTS sync', 'CHECKED A/B/C'),
    ('11',       'SAM §Write-back', 'THESIS if thesis-level change + CHANGELOG',            'CHECKED D (count only); thesis judgement is MANUAL'),
    ('12',       'SAM §Write-back', 'TIMELINE if an event resolves + CHANGELOG',            'MANUAL'),
    ('12a',      'SAM §Write-back', 'Consider spawning METSUKE for TRADE/STRATEGY drift',   'MANUAL'),
    ('13',       'SAM §Write-back', 'Research detail -> research/outputs/',                 'MANUAL'),
    ('13a',      'SAM §Write-back', 'Refresh NEXUS_BRIEF LAST (ordering constraint)',       'CHECKED F'),
    ('14',       'SAM §Write-back', 'Update MEMORY.md (handoff)',                           'CHECKED H  (the fleet-idx delegation is a DIFFERENT file, not this step)'),
    ('root 1',   'root §Session end', 'Commit your files locally',                          'CHECKED G'),
    ('root 1b',  'root §Session end', 'Orphan check',                                       'DELEGATED orphan_check.sh (CATO 2026-09-19: was LISTED but never called)'),
    ('root 1c',  'root §Session end', 'Consumer check on superseded figures',               'MANUAL (needs --old/--new; series+unit judgement)'),
    ('root 1c-bis', 'root §Session end', 'Ledger staleness nudge',                          'DELEGATED ledger_staleness.py'),
    ('root 1d',  'root §Session end', 'Memory-index check (if an auto-memory was written)', 'MANUAL (needs --slug)'),
    ('root 1e',  'root §Session end', 'Claim check (weekday-vs-date)',                      'DELEGATED claim_check.py'),
    ('root 2',   'root §Session end', 'Auto-push via safe-push.sh + CONFIRMED receipt',     'MANUAL (the receipt line is the proof)'),
]

# Also verified here because nothing else does, though not its own charter step:
#   E  PREDICTION_SCHEDULE.json keys == the OPEN set, and its condition hashes still match.


def git(*args):
    r = subprocess.run(['git', *args], cwd=ROOT, capture_output=True, text=True)
    if r.returncode:
        raise ValueError('git unavailable: ' + ' '.join(args[:3]))
    return r.stdout.strip()


def _catalysts_all():
    """EVERY row, including blank-date ones — filtering them here is what hid them."""
    with open(SAM / 'docket' / 'CATALYSTS.tsv', encoding='utf-8') as f:
        return list(csv.DictReader(f, delimiter='\t'))


def _calendar_forward_counts(text):
    """Dates in CALENDAR's FORWARD table only — everything above the first
    '## ✅ RESOLVED' heading. Rows below it are a dated record and are SUPPOSED
    to hold past dates."""
    head = re.split(r'^## .*RESOLVED', text, maxsplit=1, flags=re.M)[0]
    out = {}
    for line in head.split('\n'):
        if not line.startswith('|'):
            continue
        m = re.search(r'\b(\w{3}) (\w{3}) (\d{1,2}) (\d{4})\b', line)
        if m:
            mon = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'].index(m.group(2)) + 1
            d = '%s-%02d-%02d' % (m.group(4), mon, int(m.group(3)))
            out[d] = out.get(d, 0) + 1       # COUNT, not set membership
    return out


# ⛔ SINGLE QUOTES ARE DELIBERATELY ABSENT. Probing this check on 2026-09-19 (after
# CATO's round 2, before shipping) found that two ordinary apostrophes — a possessive
# and a contraction, e.g. "SAM's 9 OPEN rows aren't final" — form a spurious span that
# swallowed a LIVE claim. English prose is full of apostrophes, so single quotes are
# unusable as a retirement marker here. Retired values in this repo are quoted with
# double quotes; that is what is matched.
QUOTE_PAIRS = [('"', '"'), ('\u201c', '\u201d')]


def _quoted_spans(line):
    """Character ranges inside QUOTE marks.

    ⚠️ Replaces a single-character adjacency test that CATO broke three ways on
    2026-09-19:
      * `'' in '"\'`'` is TRUE in Python, so a match at the START or END of a line
        produced an empty neighbour and was auto-suppressed — an unquoted
        "… 4 OPEN" ending a line escaped silently.
      * BACKTICKS were treated as quoting, so a LIVE claim written as `9 OPEN`
        was suppressed. Backticks are formatting, not a retirement marker, and are
        deliberately NOT included here.
    Span containment fixes all three: a figure inside quotes is a record of a
    retired value; a bare one is a claim.
    """
    spans = []
    for op, cl in QUOTE_PAIRS:
        idx = [i for i, ch in enumerate(line) if ch == op] if op == cl else None
        if idx is not None:
            for a, b in zip(idx[::2], idx[1::2]):
                spans.append((a, b))
        else:
            stack = []
            for i, ch in enumerate(line):
                if ch == op:
                    stack.append(i)
                elif ch == cl and stack:
                    spans.append((stack.pop(), i))
    return spans


# ⛔ THE ASSUMPTION THAT BROKE (CATO round 3, 2026-09-19): quotes were treated as
# marking a RETIRED value. Quotes mark QUOTATION, which is equally used for a LIVE
# claim — CATO's counterexample is plain English:
#     PREDICTIONS.tsv currently reports "9 OPEN"; use that count today.
# Suppressing on quoting alone silenced it. Quoting is now NECESSARY BUT NOT
# SUFFICIENT: the line must ALSO carry positive evidence that the figure is being
# reported as history. Default is to FLAG; silence must be earned.
HISTORY_CUES = (
    'it read', 'read "', 'this line said', 'said "', 'until', 'superseded',
    'retired', 'no longer', 'previously', 'formerly', 'stale', 'false positive',
    'was wrong', 'corrected', 'match inside', 'matched inside', 'used to',
)


def _is_historical_quote(line, start, end):
    """True only when the figure is BOTH inside quotes AND the line says it is old."""
    if not any(a < start and end <= b for a, b in _quoted_spans(line)):
        return False
    low = line.lower()
    return any(c in low for c in HISTORY_CUES)


TENOR_RE = re.compile(r'^\d{1,2}y$')     # 2y 5y 10y 20y 30y 40y — the auction discriminator

STOP = {'the', 'a', 'an', 'of', 'and', 'or', 'for', 'to', 'in', 'on', 'at', 'by',
        'vs', 'is', 'its', 'no', 'not', 'day', 'date', 'jst', 'et', 'am', 'pm'}


def _tokens(text):
    """Significant lowercase word/number tokens, for EVENT IDENTITY matching."""
    return {w for w in re.findall(r'[a-z0-9]+', text.lower()) if w not in STOP and len(w) > 1}


def _calendar_forward_rows(text):
    head = re.split(r'^## .*RESOLVED', text, maxsplit=1, flags=re.M)[0]
    return [l for l in head.split('\n')
            if l.startswith('|') and not l.startswith('|--') and '| Date |' not in l
            and '| When |' not in l]


DATE_RE = r'\b(\w{3}) (\w{3}) (\d{1,2}) (\d{4})\b'


def _row_date(line):
    m = re.search(DATE_RE, line)
    if not m:
        return None
    mon = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
           'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'].index(m.group(2)) + 1
    return '%s-%02d-%02d' % (m.group(4), mon, int(m.group(3)))


def _calendar_forward_events(text):
    out = {}
    for line in _calendar_forward_rows(text):
        d = _row_date(line)
        if d:
            cells = [c.strip() for c in line.strip('|').split('|')]
            out.setdefault(d, []).append(cells[1] if len(cells) > 1 else line)
    return out


def _calendar_undated_rows(text):
    return [l.strip() for l in _calendar_forward_rows(text) if not _row_date(l)]


def check_docket(problems, today):
    """⚠️ CATO 2026-09-19 found this comparing bare DATE SETS. Two events sharing a
    date meant deleting one from CALENDAR still passed, and rows with a blank date
    vanished from the comparison entirely. It now compares the COUNT OF EVENTS PER
    DATE — which catches a dropped event without needing the two files' prose to
    match word-for-word — and flags undated rows explicitly."""
    rows = _catalysts_all()
    undated = [r for r in rows if not (r.get('date') or '').strip()]
    if undated:
        problems.append('A2 [step 10] CATALYSTS.tsv has %d row(s) with a BLANK date: %s '
                        '— catalyst_countdown.py cannot surface them and every date-keyed check '
                        'skips them silently'
                        % (len(undated), ', '.join((r.get('event') or '?')[:40] for r in undated[:4])))
    dated = [r for r in rows if (r.get('date') or '').strip()]

    past = sorted({r['date'] for r in dated if r['date'] < today})
    if past:
        problems.append('A [step 10] CATALYSTS.tsv holds %d row(s) dated before today: %s '
                        '— resolved rows belong in CALENDAR\'s RESOLVED block, not the feed'
                        % (len(past), ', '.join(past)))

    cal_text = (SAM / 'docket' / 'CALENDAR.md').read_text(encoding='utf-8')
    cal_counts = _calendar_forward_counts(cal_text)
    undated_cal = _calendar_undated_rows(cal_text)
    if undated_cal:
        problems.append('B2 [step 10] CALENDAR.md FORWARD table has %d row(s) with no parseable date: %s '
                        '— invisible to every date-keyed check, including this one before 2026-09-19'
                        % (len(undated_cal), ' | '.join(r[:55] for r in undated_cal[:3])))
    cal_past = sorted(d for d in cal_counts if d < today)
    if cal_past:
        problems.append('B [step 10] CALENDAR.md FORWARD table holds past-dated row(s): %s '
                        '— boot step 3 reads exactly these rows, so a stale one misinforms the next session'
                        % ', '.join(cal_past))

    # ⚠️ CATO 2026-09-19 (second pass): this compared EVENT COUNTS per date, so
    # REPLACING one event with a different one on the same date passed cleanly.
    # Counts are kept (they localise a miscount) and EVENT IDENTITY is now checked
    # on top, by significant-token overlap — the two files word things differently
    # by design, so exact string equality would be noise.
    cal_events = _calendar_forward_events(cal_text)
    cat_events = {}
    for r in dated:
        if r['date'] >= today:
            cat_events.setdefault(r['date'], []).append(r.get('event') or '')

    for d in sorted(set(cat_events) | set(cal_events)):
        a, b = len(cat_events.get(d, [])), len(cal_events.get(d, []))
        if a != b:
            problems.append('C [step 10] %s: CATALYSTS has %d event(s), CALENDAR forward table has %d '
                            '— the charter says the two must not diverge' % (d, a, b))
            continue
        pool = list(cal_events.get(d, []))
        for ev in cat_events.get(d, []):
            # ⚠️ A bare overlap floor of >=2 let a TENOR SWAP through: "JGB 10Y auction"
            # vs "JGB 2Y auction" share {jgb, auction} and this desk tracks many
            # auctions differing only by tenor. Jaccard uses the DIFFERENCES too.
            # Measured on live data 2026-09-19: every true pair scores 1.00 and the
            # tenor-swap decoy scores 0.50, so 0.6 has margin on both sides.
            et = _tokens(ev)
            best, score = None, 0.0
            for cand in pool:
                ct = _tokens(cand)
                j = len(et & ct) / len(et | ct) if (et | ct) else 0.0
                if j > score:
                    best, score = cand, j
            # ⛔ THE SECOND ASSUMPTION THAT BROKE: that a similarity THRESHOLD can
            # stand in for identity. CATO round 3 swapped the tenor in the LIVE
            # October-8 row — "JGB 30Y auction — THE NEXT TEST THE FROZEN BARS
            # ACTUALLY APPLY TO" -> 20Y — and scored 0.80, clearing the bar. My decoy
            # had used SHORT names (0.50); a long title DILUTES the one token that
            # carries the meaning. A ratio over all tokens cannot weight the
            # discriminator, so the discriminator is now compared DIRECTLY and the
            # ratio is kept only as a backstop.
            tenor_a = {t for t in et if TENOR_RE.match(t)}
            tenor_b = {t for t in _tokens(best)} if best else set()
            tenor_b = {t for t in tenor_b if TENOR_RE.match(t)}
            if best is not None and tenor_a != tenor_b:
                problems.append('C3 [step 10] %s: CATALYSTS event %r names tenor(s) %s but its closest '
                                'CALENDAR row %r names %s. A TENOR SWAP inside a long title scores high '
                                'on any similarity ratio (live example: 0.80) — the discriminator is '
                                'compared directly, not diluted into an average.'
                                % (d, ev[:44], sorted(tenor_a) or 'none', best[:44], sorted(tenor_b) or 'none'))
                pool.remove(best)
                continue
            if score < 0.6:
                problems.append('C2 [step 10] %s: CATALYSTS event %r has no matching CALENDAR row '
                                '(best similarity %.2f, need 0.60). Same-date EVENT SWAPS — including '
                                'a TENOR SWAP that shares most words — are invisible to a count-only '
                                'or overlap-only comparison.' % (d, ev[:60], score))
            elif best is not None:
                pool.remove(best)


PRED_FIELDS = ['Pred_ID', 'Date_Made', 'Prediction', 'Confidence', 'Timeframe',
               'Status', 'Date_Resolved', 'Outcome', 'Notes']
CONFIRM_CLASS = {'CONFIRMED', 'RESOLVED', 'RESOLVED CONFIRMED',
                 'RESOLVED CONFIRMED — TRUE-IN-LETTER / FALSE-IN-SPIRIT'}
SPECIAL_CLASS = {'RESOLVED — TRUE-IN-LETTER / FALSE-IN-SPIRIT'}
# ⚠️ Added 2026-09-19 PM with SAM-28's regrade. THIS FILE KEEPS ITS OWN STATUS
# VOCABULARY, SEPARATE FROM scripts/lib/boot_context.py STATUSES — the new token was
# added there first and check D failed here on the same run, which is the only reason
# the split was noticed. Two guards over one fact, and updating one does not update
# the other. ⛔ ANY future status token must be added in BOTH places.
QUALIFIED_CLASS = {'RESOLVED — QUALIFIED / NO-VERDICT'}


def _pred_rows():
    text = (SAM / 'thesis' / 'PREDICTIONS.tsv').read_text(encoding='utf-8')
    lines = [l for l in text.splitlines() if l.strip() and not l.startswith('#')]
    return list(csv.DictReader(io.StringIO('\n'.join(lines)), delimiter='\t'))


def check_scoreboard(problems):
    rows = _pred_rows()
    conf = [r for r in rows if r['Status'].strip() in CONFIRM_CLASS]
    fail = [r for r in rows if r['Status'].strip() == 'FAILED']
    spec = [r for r in rows if r['Status'].strip() in SPECIAL_CLASS]
    qual = [r for r in rows if r['Status'].strip() in QUALIFIED_CLASS]
    opn = [r for r in rows if r['Status'].strip() == 'OPEN']
    if len(conf) + len(fail) + len(spec) + len(qual) + len(opn) != len(rows):
        unk = ({r['Status'].strip() for r in rows} - CONFIRM_CLASS - SPECIAL_CLASS
               - QUALIFIED_CLASS - {'FAILED', 'OPEN'})
        problems.append('D [step 11] PREDICTIONS.tsv has unclassified Status value(s): %s '
                        '— the derived scoreboard cannot be trusted' % sorted(unk))
        return None
    derived = (len(conf), len(fail), len(spec), len(opn))
    derived5 = (len(conf), len(fail), len(spec), len(qual), len(opn))

    # Any LIVE surface asserting a scoreboard must match the derivation.
    #
    # ⚠️ CATO 2026-09-19: this originally required the FOUR-part form
    #   "X CONFIRMED / Y FAILED / Z special / W OPEN"
    # and therefore could NOT see the very defect it was built for. THESIS carried
    #   "**4 OPEN as of 2026-08-27** ... Scoreboard **14 CONFIRMED / 14 FAILED / 1 special**"
    # — a THREE-part scoreboard with the open count stated SEPARATELY. It went stale
    # for 23 days across two resolutions and this check would have passed it.
    # My own test for D used a synthetic four-part fixture I wrote myself, so it
    # confirmed my assumption instead of the artifact. Three forms are matched now.
    # 5-part form, live since 2026-09-19 PM: "16 CONFIRMED / 15 FAILED / 1 special / 1 qualified / 1 OPEN".
    # ⛔ MUST be matched BEFORE `four`, and `four` must not match inside it: the 4-part
    # pattern cannot match this string anyway (a `qualified` term sits between `special`
    # and `OPEN`), which means that WITHOUT this pattern the check would have silently
    # stopped verifying the scoreboard on every live surface — passing, while checking
    # nothing. That is the failure direction this file has already shipped three times.
    five = re.compile(r'(\d+)\s*CONFIRMED\s*/\s*(\d+)\s*FAILED\s*/\s*(\d+)\s*special'
                      r'\s*/\s*(\d+)\s*qualified\s*/\s*(\d+)\s*OPEN')
    four = re.compile(r'(\d+)\s*CONFIRMED\s*/\s*(\d+)\s*FAILED\s*/\s*(\d+)\s*special\s*/\s*(\d+)\s*OPEN')
    three = re.compile(r'(\d+)\s*CONFIRMED\s*/\s*(\d+)\s*FAILED\s*/\s*(\d+)\s*special(?!\s*/)')
    lone = re.compile(r'(\d+)\s*OPEN\b')
    for rel in ('STATUS.md', 'STATUS_REFERENCE.md', 'NEXUS_BRIEF.md',
                'thesis/THESIS.md', 'MEMORY.md', 'TRADE.md', 'STRATEGY.md'):
        f = SAM / rel
        if not f.exists():
            continue
        text = f.read_text(encoding='utf-8')
        for m in five.finditer(text):
            got = tuple(int(g) for g in m.groups())
            if got != derived5:
                problems.append('D [step 11] %s asserts scoreboard %d/%d/%d/%d/%d but the file derives '
                                '%d/%d/%d/%d/%d — re-derive, never carry a count forward'
                                % ((rel,) + got + derived5))
        # A 4-part scoreboard is INCOMPLETE, not merely possibly-wrong, once any
        # qualified row exists: its four numbers can each be right while the row is
        # invisible and the parts no longer sum to the file.
        if qual:
            for m in four.finditer(text):
                problems.append('D [step 11] %s carries a 4-part scoreboard "%s" while %d qualified '
                                'row(s) exist — the qualified class is omitted, so the parts do not '
                                'sum to the file (%d rows). Use the 5-part form.'
                                % (rel, m.group(0).strip(), len(qual), len(rows)))
        for m in four.finditer(text):
            got = tuple(int(g) for g in m.groups())
            if got != derived:
                problems.append('D [step 11] %s asserts scoreboard %d/%d/%d/%d but the file derives '
                                '%d/%d/%d/%d — re-derive, never carry a count forward'
                                % ((rel,) + got + derived))
        for m in three.finditer(text):
            got = tuple(int(g) for g in m.groups())
            if got != derived[:3]:
                problems.append('D [step 11] %s asserts a 3-part scoreboard %d/%d/%d but the file '
                                'derives %d/%d/%d' % ((rel,) + got + derived[:3]))
        # A lone "N OPEN" counts as a scoreboard claim when the LINE it sits on is
        # talking about predictions. Otherwise every "3 OPEN" in prose trips it, and
        # a check that cries wolf gets skimmed (consumer_check: 51/51 false).
        #
        # ⚠️ CATO 2026-09-19 (second pass) broke the previous version two more ways:
        #   * it did `continue` whenever the line ALSO held a valid 3- or 4-part
        #     scoreboard, so a WRONG open count sitting beside a CORRECT scoreboard
        #     was never examined — and that is exactly the real THESIS shape.
        #   * the quote test used single-character adjacency, and `'' in '"...'` is
        #     True, so any match at line start/end was auto-suppressed.
        # Fixed by BLANKING the scoreboard spans and scanning what remains, and by
        # testing span containment instead of neighbouring characters.
        for line in text.split('\n'):
            low = line.lower()
            if not ('predictions.tsv' in low or 'scoreboard' in low):
                continue
            masked = line
            for m in list(five.finditer(line)) + list(four.finditer(line)) + list(three.finditer(line)):
                masked = masked[:m.start()] + ' ' * (m.end() - m.start()) + masked[m.end():]
            for m in lone.finditer(masked):
                if _is_historical_quote(line, m.start(), m.end()):
                    continue          # quoted AND explicitly flagged as historical
                if int(m.group(1)) != derived[3]:
                    problems.append('D [step 11] %s asserts "%s OPEN" on a predictions line but the '
                                    'file derives %d OPEN — this is the form THESIS carried stale '
                                    'for 23 days' % (rel, m.group(1), derived[3]))
    return derived, [r['Pred_ID'] for r in opn]


def check_sam_memory(problems):
    """H [step 14] — SAM's OWN handoff against its charter cap.
    ⚠️ CATO 2026-09-19: step 14 was 'covered' by check_memory_length.sh, which measures
    memory/auto/MEMORY.md (the FLEET index) — a different file. SAM's handoff had no
    check at all."""
    f = SAM / 'MEMORY.md'
    if not f.exists():
        problems.append('H [step 14] AGENTS/SAM/MEMORY.md missing')
        return
    n = len(f.read_text(encoding='utf-8').split('\n'))
    if n > 100:
        problems.append('H [step 14] AGENTS/SAM/MEMORY.md is %d lines, over its charter cap of 100 '
                        '("promote to thesis or auto-memory, never just accumulate")' % n)


def _row_hash(row):
    return hashlib.sha256(json.dumps({k: row[k] for k in ('Prediction', 'Timeframe', 'Notes')},
                                     ensure_ascii=False, sort_keys=True,
                                     separators=(',', ':')).encode()).hexdigest()


def check_sidecar(problems, open_ids):
    f = SAM / 'docket' / 'PREDICTION_SCHEDULE.json'
    if not f.exists():
        problems.append('E PREDICTION_SCHEDULE.json missing')
        return
    sched = json.loads(f.read_text(encoding='utf-8'))['predictions']
    by_id = {r['Pred_ID']: r for r in _pred_rows()}
    if set(sched) != set(open_ids):
        problems.append('E sidecar keys %s != OPEN set %s. NOTE: boot.py only hash-checks OPEN rows, '
                        'so a resolved row left here is never re-verified again'
                        % (sorted(sched), sorted(open_ids)))
    for pid in set(sched) & set(by_id):
        if sched[pid].get('condition_sha256') != _row_hash(by_id[pid]):
            problems.append('E sidecar hash for %s does not match its row — re-stamp ONLY after a '
                            'field-level git diff of Prediction/Timeframe/Confidence/Status' % pid)


def check_brief_ordering(problems):
    """Schema Amendment 10: the brief is the session's LAST write-back.
    Checkable form: brief commit time >= STATUS commit time."""
    b = git('log', '-1', '--format=%ct', '--', 'AGENTS/SAM/NEXUS_BRIEF.md')
    s = git('log', '-1', '--format=%ct', '--', 'AGENTS/SAM/STATUS.md')
    if not b or not s:
        problems.append('F [step 13a] cannot read commit times for NEXUS_BRIEF.md / STATUS.md')
        return
    if int(b) < int(s):
        problems.append('F [step 13a] NEXUS_BRIEF.md was committed BEFORE the last STATUS.md commit '
                        '(%s < %s) — the brief must be the LAST write-back, per schema Amendment 10'
                        % (b, s))


def check_tree_clean(problems):
    dirty = [l for l in git('status', '--porcelain', '--', 'AGENTS/SAM/').split('\n') if l.strip()]
    if dirty:
        problems.append('G [root 1] %d uncommitted file(s) under AGENTS/SAM/:\n      %s'
                        % (len(dirty), '\n      '.join(dirty)))


DELEGATED = [
    ('root 1e',    ['python3', 'scripts/claim_check.py', '--check', 'weekday',
                    'AGENTS/SAM/docket/CATALYSTS.tsv', 'AGENTS/SAM/docket/CALENDAR.md',
                    'AGENTS/SAM/STATUS.md']),
    ('9',          ['python3', 'scripts/read_cap_check.py', '--agent', 'SAM']),
    # measures memory/auto/MEMORY.md — the FLEET index, NOT SAM's handoff. Check H
    # covers the handoff. Kept because the fleet cap is real; labelled so the two
    # are never confused again (CATO 2026-09-19).
    ('fleet-idx',  ['bash', 'scripts/check_memory_length.sh']),  # NOT step 14 — different file

    ('root 1c-bis', ['python3', 'scripts/ledger_staleness.py', '--nudge', 'SAM']),
    # CATO 2026-09-19: this was in the STEPS table as DELEGATED and was never called.
    ('root 1b',    ['bash', 'scripts/orphan_check.sh', 'SAM']),
]


def run_delegated():
    """⚠️ CATO 2026-09-19: this discarded child stdout/stderr, so a non-zero exit
    arrived as a bare number with the diagnosis thrown away — the reader then had to
    re-run the tool by hand, which is how an advisory gets skipped."""
    out = []
    for label, cmd in DELEGATED:
        try:
            r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, timeout=120)
            # ⚠️ CATO 2026-09-19 (second pass): output was kept only for a NON-ZERO
            # exit, and orphan_check.sh DELIBERATELY exits 0 while printing warnings
            # ("[not yours]", "[likely YOURS]"). Its 12 warning lines vanished. Exit
            # code is not the signal for an advisory tool — the TEXT is.
            out_text = (r.stdout + r.stderr).strip()
            lines = [l for l in out_text.split('\n') if l.strip()]
            warned = any(k in out_text for k in
                         ('⚠', '🔴', '🟠', 'not yours', 'likely YOURS', 'WARNING',
                          'STALE', 'nudge:', 'FAIL'))
            tail = ''
            if r.returncode or warned:
                keep = [l for l in lines if any(k in l for k in
                        ('⚠', '🔴', '🟠', 'not yours', 'likely YOURS', 'WARNING',
                         'STALE', 'nudge:', 'FAIL'))] or lines[-4:]
                shown = keep[:6]
                tail = '\n'.join('        | ' + l[:150] for l in shown)
                if len(keep) > len(shown):
                    tail += ('\n        | ... %d MORE warning line(s) NOT SHOWN — run  %s  for the full log'
                             % (len(keep) - len(shown), ' '.join(cmd)))
                if r.returncode == 0 and warned:
                    tail = '        | (exit 0, but it WARNED — read it)\n' + tail
            out.append((label, ' '.join(cmd[:2]), r.returncode, tail))
        except Exception as exc:                                        # noqa: BLE001
            out.append((label, ' '.join(cmd[:2]), 'ERROR', '        | %s' % exc))
    return out


def _assert_table_matches_delegations():
    """The STEPS table is output the reader trusts. CATO 2026-09-19 found it
    claiming 'DELEGATED orphan_check.sh' for a command that was never called, so
    the table is now checked against the list rather than maintained by hand."""
    labels = {l for l, _ in DELEGATED}
    bad = [(step, cover) for step, _w, _d, cover in STEPS
           if 'DELEGATED' in cover and step not in labels]
    if bad:
        raise ValueError('STEPS claims a delegation that never runs: %s' % bad)


def main():
    argv = sys.argv[1:]
    pre_commit = '--pre-commit' in argv
    _assert_table_matches_delegations()
    print('=' * 74)
    print('  SAM CLOSEOUT CHECK — %s' % date.today().isoformat())
    print('=' * 74)
    print('  %-9s %-18s %-46s' % ('STEP', 'WRITTEN IN', 'COVERAGE'))
    for step, where, duty, cover in STEPS:
        print('  %-9s %-18s %-46s' % (step, where, cover))
        print('  %-28s %s' % ('', duty))
    if '--list' in argv:
        return 0

    today = date.today().isoformat()
    problems = []
    check_docket(problems, today)
    sb = check_scoreboard(problems)
    if sb:
        derived, open_ids = sb
        check_sidecar(problems, open_ids)
        print('\n  DERIVED from PREDICTIONS.tsv: %d CONFIRMED / %d FAILED / %d special / %d OPEN  (OPEN: %s)'
              % (derived + (', '.join(open_ids) or 'none',)))
    check_sam_memory(problems)
    # ⚠️ CATO 2026-09-19: the charter said run this BEFORE committing, while G demands a
    # CLEAN tree and F reads COMMITTED history — so the documented invocation could never
    # pass. Resolved by making the mode explicit rather than by weakening either check.
    if pre_commit:
        print('\n  --pre-commit: SKIPPING F (brief-vs-STATUS commit order) and G (clean tree).')
        print('  These are only meaningful AFTER the final commit. Re-run with no flag before pushing.')
    else:
        check_brief_ordering(problems)
        check_tree_clean(problems)

    if '--no-delegate' not in argv:
        print('\n  DELEGATED (existing fleet instruments, exit codes):')
        for label, cmd, rc, tail in run_delegated():
            mark = 'ok' if rc == 0 else 'rc=%s' % rc
            print('    %-12s %-34s %s' % (label, cmd, mark))
            if tail:
                print(tail)
            # ⛔ CATO round 3: a delegated tool that TIMED OUT or crashed printed
            # 'ERROR' and the gate still returned PASS, because run_delegated results
            # were never joined to `problems`. A check that could not run is not a
            # check that passed — the whole point of the scoped footer.
            if rc == 'ERROR':
                problems.append('DELEG [%s] %s could not run (timeout or crash) — a check that did '
                                'not execute is NOT a pass; re-run it or state it as skipped'
                                % (label, cmd))
        print('    (non-zero is not automatically a closeout failure — read that tool\'s own output)')

    print('\n  MANUAL — unverifiable here, and printed every run so they cannot be skipped:')
    for step, where, duty, cover in STEPS:
        if cover.startswith('MANUAL'):
            print('    %-9s %s' % (step, duty))

    print()
    if problems:
        print('  ❌ CLOSEOUT-CHECK FAIL — %d problem(s):' % len(problems))
        for p in problems:
            print('    - %s' % p)
        print('\n  A FAIL is structural. A PASS is scoped to these checks and says nothing')
        print('  about whether the session\'s judgement was right.')
        return 1
    ran = 'docket sync, derived counts, sidecar, handoff cap'
    ran += ', brief ordering, tree clean' if not pre_commit else '  [F and G SKIPPED: --pre-commit]'
    print('  ✅ CLOSEOUT-CHECK PASS — structural checks only: %s.' % ran)
    print('     This does NOT certify that the right events were added, that a thesis change')
    print('     was correctly declined, or that any figure is true. The MANUAL steps above')
    print('     remain yours. A PASS naming checks it did not run is how a gate overstates')
    print('     itself — the scope line is generated from the mode, not typed.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
