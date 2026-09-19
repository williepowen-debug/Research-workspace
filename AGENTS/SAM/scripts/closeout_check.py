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
    ('14',       'SAM §Write-back', 'Update MEMORY.md (handoff)',                           'DELEGATED check_memory_length.sh'),
    ('root 1',   'root §Session end', 'Commit your files locally',                          'CHECKED G'),
    ('root 1b',  'root §Session end', 'Orphan check',                                       'DELEGATED orphan_check.sh'),
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


def _catalysts():
    with open(SAM / 'docket' / 'CATALYSTS.tsv', encoding='utf-8') as f:
        return [r for r in csv.DictReader(f, delimiter='\t') if r.get('date')]


def _calendar_forward_dates(text):
    """Dates in CALENDAR's FORWARD table only — everything above the first
    '## ✅ RESOLVED' heading. Rows below it are a dated record and are SUPPOSED
    to hold past dates."""
    head = re.split(r'^## .*RESOLVED', text, maxsplit=1, flags=re.M)[0]
    out = set()
    for line in head.split('\n'):
        if not line.startswith('|'):
            continue
        m = re.search(r'\b(\w{3}) (\w{3}) (\d{1,2}) (\d{4})\b', line)
        if m:
            mon = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'].index(m.group(2)) + 1
            out.add('%s-%02d-%02d' % (m.group(4), mon, int(m.group(3))))
    return out


def check_docket(problems, today):
    cat = _catalysts()
    past = sorted({r['date'] for r in cat if r['date'] < today})
    if past:
        problems.append('A [step 10] CATALYSTS.tsv holds %d row(s) dated before today: %s '
                        '— resolved rows belong in CALENDAR\'s RESOLVED block, not the feed'
                        % (len(past), ', '.join(past)))

    cal_text = (SAM / 'docket' / 'CALENDAR.md').read_text(encoding='utf-8')
    cal_fwd = _calendar_forward_dates(cal_text)
    cal_past = sorted(d for d in cal_fwd if d < today)
    if cal_past:
        problems.append('B [step 10] CALENDAR.md FORWARD table holds past-dated row(s): %s '
                        '— boot step 3 reads exactly these rows, so a stale one misinforms the next session'
                        % ', '.join(cal_past))

    cat_fwd = {r['date'] for r in cat if r['date'] >= today}
    only_cat = sorted(cat_fwd - cal_fwd)
    only_cal = sorted(d for d in cal_fwd - cat_fwd if d >= today)
    if only_cat or only_cal:
        problems.append('C [step 10] CALENDAR and CATALYSTS forward sets DIVERGE (the charter says '
                        'they must not): only in CATALYSTS %s | only in CALENDAR %s'
                        % (only_cat or 'none', only_cal or 'none'))


PRED_FIELDS = ['Pred_ID', 'Date_Made', 'Prediction', 'Confidence', 'Timeframe',
               'Status', 'Date_Resolved', 'Outcome', 'Notes']
CONFIRM_CLASS = {'CONFIRMED', 'RESOLVED', 'RESOLVED CONFIRMED',
                 'RESOLVED CONFIRMED — TRUE-IN-LETTER / FALSE-IN-SPIRIT'}
SPECIAL_CLASS = {'RESOLVED — TRUE-IN-LETTER / FALSE-IN-SPIRIT'}


def _pred_rows():
    text = (SAM / 'thesis' / 'PREDICTIONS.tsv').read_text(encoding='utf-8')
    lines = [l for l in text.splitlines() if l.strip() and not l.startswith('#')]
    return list(csv.DictReader(io.StringIO('\n'.join(lines)), delimiter='\t'))


def check_scoreboard(problems):
    rows = _pred_rows()
    conf = [r for r in rows if r['Status'].strip() in CONFIRM_CLASS]
    fail = [r for r in rows if r['Status'].strip() == 'FAILED']
    spec = [r for r in rows if r['Status'].strip() in SPECIAL_CLASS]
    opn = [r for r in rows if r['Status'].strip() == 'OPEN']
    if len(conf) + len(fail) + len(spec) + len(opn) != len(rows):
        unk = {r['Status'].strip() for r in rows} - CONFIRM_CLASS - SPECIAL_CLASS - {'FAILED', 'OPEN'}
        problems.append('D [step 11] PREDICTIONS.tsv has unclassified Status value(s): %s '
                        '— the derived scoreboard cannot be trusted' % sorted(unk))
        return None
    derived = (len(conf), len(fail), len(spec), len(opn))

    # any LIVE surface asserting a scoreboard must match the derivation
    pat = re.compile(r'(\d+)\s*CONFIRMED\s*/\s*(\d+)\s*FAILED\s*/\s*(\d+)\s*special\s*/\s*(\d+)\s*OPEN')
    for rel in ('STATUS.md', 'STATUS_REFERENCE.md', 'NEXUS_BRIEF.md',
                'thesis/THESIS.md', 'MEMORY.md', 'TRADE.md', 'STRATEGY.md'):
        f = SAM / rel
        if not f.exists():
            continue
        for m in pat.finditer(f.read_text(encoding='utf-8')):
            got = tuple(int(g) for g in m.groups())
            if got != derived:
                problems.append('D [step 11] %s asserts scoreboard %d/%d/%d/%d but the file derives '
                                '%d/%d/%d/%d — re-derive, never carry a count forward' % ((rel,) + got + derived))
    return derived, [r['Pred_ID'] for r in opn]


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
    ('step 9',     ['python3', 'scripts/read_cap_check.py', '--agent', 'SAM']),
    ('step 14',    ['bash', 'scripts/check_memory_length.sh']),
    ('root 1c-bis', ['python3', 'scripts/ledger_staleness.py', '--nudge', 'SAM']),
]


def run_delegated():
    out = []
    for label, cmd in DELEGATED:
        try:
            r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, timeout=120)
            out.append((label, ' '.join(cmd[:2]), r.returncode))
        except Exception as exc:                                        # noqa: BLE001
            out.append((label, ' '.join(cmd[:2]), 'ERROR %s' % exc))
    return out


def main():
    argv = sys.argv[1:]
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
    check_brief_ordering(problems)
    check_tree_clean(problems)

    if '--no-delegate' not in argv:
        print('\n  DELEGATED (existing fleet instruments, exit codes):')
        for label, cmd, rc in run_delegated():
            mark = 'ok' if rc == 0 else 'rc=%s' % rc
            print('    %-12s %-34s %s' % (label, cmd, mark))
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
    print('  ✅ CLOSEOUT-CHECK PASS — structural checks only (docket sync, derived counts,')
    print('     sidecar, brief ordering, tree clean). This does NOT certify that the right')
    print('     events were added, that a thesis change was correctly declined, or that any')
    print('     figure is true. The MANUAL steps above remain yours.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
