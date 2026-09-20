"""Guards for SAM's closeout_check.

Written with the checker (2026-09-19). Each test proves a check FIRES on a
defect — a checker whose checks have never been seen to fail is an assertion,
not an instrument. Checks A and B are additionally proven against the REAL
pre-repair commit in test_catches_the_actual_incident.

Run: python3 scripts/tests/test_closeout_check.py
"""
import importlib.util
import pathlib
import subprocess
import sys
import tempfile

_SAMDIR = pathlib.Path(__file__).resolve().parents[2]   # AGENTS/SAM
_ROOT = _SAMDIR.parents[1]                              # repo root (parents[3] was AGENTS/)
_SPEC = importlib.util.spec_from_file_location(
    'closeout_check', pathlib.Path(__file__).resolve().parents[1] / 'closeout_check.py')
cc = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(cc)

class Skipped(Exception):
    """Raised when a test CANNOT run (e.g. the git history is unreachable).

    ⛔ It is reported as SKIP, never as PASS. Found 2026-09-19: these tests were
    written with a bare `return` on an unreachable commit, so in a sandbox without
    the repo the end-to-end test printed PASS while executing nothing — 'a check
    that cannot be performed reads the same as one that passed'."""


TODAY = '2026-09-19'

CAL_HEAD = "# SAM CALENDAR\n\n| Date | Event |\n|---|---|\n"
CAL_RESOLVED = "\n## ✅ RESOLVED\n\n| Date | Event |\n|---|---|\n| Wed Sep 16 2026 | done |\n"
# Event text must MATCH across both files: since 2026-09-19 the docket check
# verifies event IDENTITY, not just counts, so placeholder names ('x' vs 'ev')
# correctly trip C2. The old fixture was unrealistic, not the check wrong.
_EV = 'JGB auction fixture event'
CAT_HEAD = "date\tevent\twhat_to_check\tthreshold_signal\tpriority\twho_cares\tnotes\ttype\n"


def _fixture(cal_rows, cat_dates):
    d = pathlib.Path(tempfile.mkdtemp())
    (d / 'docket').mkdir()
    (d / 'docket' / 'CALENDAR.md').write_text(
        CAL_HEAD + ''.join('| %s | %s |\n' % (r, _EV) for r in cal_rows) + CAL_RESOLVED, encoding='utf-8')
    (d / 'docket' / 'CATALYSTS.tsv').write_text(
        CAT_HEAD + ''.join('%s\t%s\tw\tt\t●\tSAM\tn\ttype\n' % (x, _EV) for x in cat_dates), encoding='utf-8')
    return d


def _run_docket(cal_rows, cat_dates):
    old, cc.SAM = cc.SAM, _fixture(cal_rows, cat_dates)
    try:
        p = []
        cc.check_docket(p, TODAY)
        return p
    finally:
        cc.SAM = old


def test_clean_docket_passes():
    p = _run_docket(['Tue Sep 29 2026', 'Thu Oct 08 2026'], ['2026-09-29', '2026-10-08'])
    assert p == [], p


def test_A_fires_on_past_row_in_catalysts():
    p = _run_docket(['Tue Sep 29 2026'], ['2026-09-18', '2026-09-29'])
    assert any(x.startswith('A ') for x in p), p
    assert '2026-09-18' in ' '.join(p)


def test_B_fires_on_past_row_in_calendar_forward_table():
    p = _run_docket(['Fri Sep 18 2026', 'Tue Sep 29 2026'], ['2026-09-29'])
    assert any(x.startswith('B ') for x in p), p


def test_B_does_not_fire_on_the_RESOLVED_block():
    """Rows below the RESOLVED heading are a dated record and SHOULD hold past
    dates. A checker that flagged them would train its reader to ignore it."""
    p = _run_docket(['Tue Sep 29 2026'], ['2026-09-29'])
    assert not any(x.startswith('B ') for x in p), p


def test_C_fires_when_the_two_files_diverge():
    p = _run_docket(['Tue Sep 29 2026'], ['2026-09-29', '2026-10-08'])
    assert any(x.startswith('C ') for x in p), p
    assert '2026-10-08' in ' '.join(p)


def test_C_quiet_when_both_hold_the_same_forward_set():
    p = _run_docket(['Tue Sep 29 2026', 'Thu Oct 08 2026'], ['2026-09-29', '2026-10-08'])
    assert not any(x.startswith('C ') for x in p), p


def test_D_fires_on_a_scoreboard_that_contradicts_the_file():
    """The derived count must beat any asserted one. This is the defect that let
    THESIS carry '4 OPEN as of 2026-08-27' for 23 days across two resolutions."""
    d = pathlib.Path(tempfile.mkdtemp())
    (d / 'thesis').mkdir()
    hdr = '\t'.join(cc.PRED_FIELDS)
    rows = [hdr,
            '\t'.join(['SAM-01', '2026-01-01', 'p', '50%', 't', 'CONFIRMED', '2026-02-01', 'TRUE', 'n']),
            '\t'.join(['SAM-02', '2026-01-01', 'p', '50%', 't', 'FAILED', '2026-02-01', 'FALSE', 'n']),
            '\t'.join(['SAM-03', '2026-01-01', 'p', '50%', 't', 'OPEN', '—', '—', 'n'])]
    (d / 'thesis' / 'PREDICTIONS.tsv').write_text('\n'.join(rows) + '\n', encoding='utf-8')
    (d / 'STATUS.md').write_text('Scoreboard 9 CONFIRMED / 9 FAILED / 9 special / 9 OPEN\n', encoding='utf-8')
    old, cc.SAM = cc.SAM, d
    try:
        p = []
        res = cc.check_scoreboard(p)
        assert res is not None
        derived, open_ids = res
        assert derived == (1, 1, 0, 1), derived
        assert open_ids == ['SAM-03'], open_ids
        assert any(x.startswith('D ') for x in p), p
    finally:
        cc.SAM = old


def test_E_fires_when_sidecar_holds_a_resolved_row():
    """boot.py hash-checks ONLY rows whose Status is OPEN, so a resolved row left
    in the sidecar is never verified again — the reason this check exists."""
    d = pathlib.Path(tempfile.mkdtemp())
    (d / 'thesis').mkdir()
    (d / 'docket').mkdir()
    hdr = '\t'.join(cc.PRED_FIELDS)
    rows = [hdr,
            '\t'.join(['SAM-03', '2026-01-01', 'p', '50%', 't', 'OPEN', '—', '—', 'n']),
            '\t'.join(['SAM-04', '2026-01-01', 'p', '50%', 't', 'FAILED', '2026-02-01', 'FALSE', 'n'])]
    (d / 'thesis' / 'PREDICTIONS.tsv').write_text('\n'.join(rows) + '\n', encoding='utf-8')
    (d / 'docket' / 'PREDICTION_SCHEDULE.json').write_text(
        '{"schema_version":1,"predictions":{"SAM-03":{"condition_sha256":"x"},'
        '"SAM-04":{"condition_sha256":"y"}}}', encoding='utf-8')
    old, cc.SAM = cc.SAM, d
    try:
        p = []
        cc.check_sidecar(p, ['SAM-03'])
        assert any('sidecar keys' in x for x in p), p
        assert any('hash for SAM-03' in x for x in p), p
    finally:
        cc.SAM = old


def test_catches_the_actual_incident():
    """End-to-end against the REAL pre-repair commit (7c956d29e). If this ever
    stops firing, the checker has been broken, not the history."""
    broken = '22e55db36^'
    d = pathlib.Path(tempfile.mkdtemp())
    (d / 'docket').mkdir()
    for name in ('CALENDAR.md', 'CATALYSTS.tsv'):
        r = subprocess.run(['git', 'show', '%s:AGENTS/SAM/docket/%s' % (broken, name)],
                           cwd=_ROOT, capture_output=True, text=True)
        if r.returncode:
            raise Skipped('commit %s not reachable' % broken)
        (d / 'docket' / name).write_text(r.stdout, encoding='utf-8')
    old, cc.SAM = cc.SAM, d
    try:
        p = []
        cc.check_docket(p, TODAY)
        assert any(x.startswith('A ') for x in p), p
        assert any(x.startswith('B ') for x in p), p
        assert '2026-09-18' in ' '.join(p)
        assert '2026-09-16' in ' '.join(p), 'must also catch the PRIOR session\'s divergence'
    finally:
        cc.SAM = old




# ---------------------------------------------------------------------------
# CATO counterexamples, 2026-09-19. Every one of these PASSED against the first
# version of the checker. They are written from CATO's actual probes, not from
# fixtures I invented — finding 1 escaped precisely because my own test for
# check D used a synthetic FOUR-part scoreboard, so it confirmed my assumption
# instead of the artifact.
# ---------------------------------------------------------------------------

def _preds(d, states):
    (d / 'thesis').mkdir(exist_ok=True)
    hdr = '\t'.join(cc.PRED_FIELDS)
    rows = [hdr] + ['\t'.join(['SAM-0%d' % n, '2026-01-01', 'p', '50%', 't', st, 'x', 'y', 'n'])
                    for n, st in enumerate(states, 1)]
    (d / 'thesis' / 'PREDICTIONS.tsv').write_text('\n'.join(rows) + '\n', encoding='utf-8')


def _scoreboard(thesis_text, states=('CONFIRMED', 'FAILED', 'OPEN')):
    d = pathlib.Path(tempfile.mkdtemp())
    _preds(d, list(states))
    (d / 'thesis' / 'THESIS.md').write_text(thesis_text, encoding='utf-8')
    old, cc.SAM = cc.SAM, d
    try:
        p = []
        cc.check_scoreboard(p)
        return p
    finally:
        cc.SAM = old


def test_CATO1_three_part_scoreboard_is_caught():
    """The REAL stale form: a 3-part scoreboard with the open count stated apart.
    The 4-part-only regex could not see it, so the checker missed the very defect
    it was built for."""
    p = _scoreboard('Scoreboard **14 CONFIRMED / 14 FAILED / 1 special**.\n')
    assert any('3-part' in x for x in p), p


def test_CATO1_lone_open_count_on_a_predictions_line_is_caught():
    p = _scoreboard('Canonical source: PREDICTIONS.tsv - 4 OPEN as of 2026-08-27.\n')
    assert any('4 OPEN' in x for x in p), p


def test_CATO1_real_pre_repair_thesis_text():
    """End-to-end against the actual committed stale text."""
    r = subprocess.run(['git', 'show', '22e55db36^:AGENTS/SAM/thesis/THESIS.md'],
                       cwd=_ROOT, capture_output=True, text=True)
    if r.returncode:
        raise Skipped('commit 22e55db36^ not reachable')
    i = r.stdout.index('## PREDICTIONS')
    assert _scoreboard(r.stdout[i:i + 700]) != [], 'real stale THESIS text must be caught'


def test_lone_open_does_not_fire_on_a_QUOTED_retired_value():
    """A correction note quoting a retired figure is a record, not a claim. The
    quote-guard was added after this check's FIRST live run fired on my own
    THESIS and MEMORY correction notes — the same failure that made
    consumer_check 51-of-51 false and trained its reader to skim."""
    p = _scoreboard('PREDICTIONS.tsv: this line read "4 OPEN as of 2026-08-27" until 2026-09-19.\n')
    assert p == [], p


def test_lone_open_does_not_fire_on_an_unrelated_series():
    p = _scoreboard('RED rail state: 3 OPEN (CH-009 CH-012 CH-017) and 12 CLOSED.\n')
    assert p == [], p


def test_CATO2_dropped_event_on_a_shared_date_is_caught():
    """Two events share 2026-09-30; deleting one from CALENDAR left the DATE
    present, so a date-set comparison passed."""
    p = _run_docket(['Wed Sep 30 2026'], ['2026-09-30', '2026-09-30'])
    assert any(x.startswith('C ') for x in p), p


def test_CATO2_undated_catalyst_row_is_caught():
    """_catalysts() filtered on a truthy date, so blank-date rows vanished from
    every date-keyed check."""
    d = pathlib.Path(tempfile.mkdtemp())
    (d / 'docket').mkdir()
    (d / 'docket' / 'CALENDAR.md').write_text(
        CAL_HEAD + '| Tue Sep 29 2026 | x |\n' + CAL_RESOLVED, encoding='utf-8')
    (d / 'docket' / 'CATALYSTS.tsv').write_text(
        CAT_HEAD + '2026-09-29\tx\tw\tt\tp\tc\tn\tt\n\tUNDATED\tw\tt\tp\tc\tn\tt\n', encoding='utf-8')
    old, cc.SAM = cc.SAM, d
    try:
        p = []
        cc.check_docket(p, TODAY)
        assert any(x.startswith('A2') for x in p), p
    finally:
        cc.SAM = old


def test_CATO3_orphan_check_is_actually_delegated():
    """It was listed in the STEPS table as DELEGATED and never called."""
    assert any('orphan_check.sh' in ' '.join(cmd) for _, cmd in cc.DELEGATED)


def test_CATO3_sam_handoff_has_its_own_cap_check():
    """Step 14 was 'covered' by check_memory_length.sh, which measures the FLEET
    index memory/auto/MEMORY.md — a different file. SAM's handoff had no check."""
    assert hasattr(cc, 'check_sam_memory')
    d = pathlib.Path(tempfile.mkdtemp())
    (d / 'MEMORY.md').write_text('x\n' * 140, encoding='utf-8')
    old, cc.SAM = cc.SAM, d
    try:
        p = []
        cc.check_sam_memory(p)
        assert any(x.startswith('H ') for x in p), p
    finally:
        cc.SAM = old


def test_CATO4_pre_commit_mode_exists_and_is_documented():
    """The charter said run it BEFORE committing while G demanded a clean tree and
    F read committed history — the documented invocation could never pass."""
    src = (pathlib.Path(cc.__file__).read_text(encoding='utf-8')
           if getattr(cc, '__file__', None) else '')
    assert '--pre-commit' in src
    charter = (_SAMDIR / 'CLAUDE.md').read_text(encoding='utf-8')
    assert 'AFTER your final commit' in charter, 'charter must not tell you to run it pre-commit'




# ---------------------------------------------------------------------------
# CATO round 2, 2026-09-19 — counterexamples against the FIRST repair. Each of
# these PASSED against that repair, which is why "all five fixed" was premature.
# ---------------------------------------------------------------------------

def test_CATO2_1a_unquoted_open_at_end_of_line():
    """`'' in '"\'`'` is True in Python, so a match at line START or END produced
    an empty neighbour and the adjacency guard auto-suppressed it."""
    assert '' in '"\'`', 'the Python trap this test exists for'
    assert _scoreboard('PREDICTIONS.tsv scoreboard: 4 OPEN') != []


def test_CATO2_1b_wrong_open_beside_a_correct_scoreboard():
    """The old code did `continue` when the line held a valid 3- or 4-part
    scoreboard, so a WRONG open count beside a CORRECT one was never examined —
    and that is exactly the shape the real THESIS line had."""
    assert _scoreboard('PREDICTIONS.tsv Scoreboard 1 CONFIRMED / 1 FAILED / 0 special. Also 9 OPEN rows.') != []


def test_CATO2_1c_backticks_do_not_suppress_a_live_claim():
    """Backticks are formatting, not a retirement marker."""
    assert _scoreboard('PREDICTIONS.tsv scoreboard is `9 OPEN` right now.') != []


def test_CATO2_quoted_value_is_still_suppressed():
    """The fix must not simply delete the guard: a genuinely quoted retired value
    is a record, not a claim."""
    assert _scoreboard('PREDICTIONS.tsv: this line read "4 OPEN as of 2026-08-27" until 9/19.') == []


def test_CATO2_correct_scoreboard_stays_quiet():
    assert _scoreboard('PREDICTIONS.tsv Scoreboard 1 CONFIRMED / 1 FAILED / 0 special / 1 OPEN') == []


def _docket(cal_rows, cat_rows):
    d = pathlib.Path(tempfile.mkdtemp())
    (d / 'docket').mkdir()
    (d / 'docket' / 'CALENDAR.md').write_text(CAL_HEAD + cal_rows + CAL_RESOLVED, encoding='utf-8')
    (d / 'docket' / 'CATALYSTS.tsv').write_text(CAT_HEAD + cat_rows, encoding='utf-8')
    old, cc.SAM = cc.SAM, d
    try:
        p = []
        cc.check_docket(p, TODAY)
        return p
    finally:
        cc.SAM = old


def test_CATO2_same_date_event_swap_is_caught():
    """Counts still matched, so replacing one event with a different one on the
    same date passed a count-only comparison."""
    p = _docket('| Wed Sep 30 2026 | JGB 2Y auction |\n',
                '2026-09-30\tSOMETHING ENTIRELY DIFFERENT\tw\tt\tp\tc\tn\tt\n')
    assert any(x.startswith('C2') for x in p), p


def test_CATO2_matching_events_with_different_prose_stay_quiet():
    """The two files word things differently by design — identity is matched on
    significant-token overlap, not string equality, or this becomes noise."""
    p = _docket('| Wed Sep 30 2026 | BOJ Oct-Dec 2026 JGB purchase schedule (17:00 JST) |\n',
                '2026-09-30\tBOJ Oct-Dec 2026 JGB purchase schedule\tw\tt\tp\tc\tn\tt\n')
    assert p == [], p


def test_CATO2_undated_calendar_row_is_caught():
    p = _docket('| TBD | undated forward event |\n', '')
    assert any(x.startswith('B2') for x in p), p


def test_CATO2_delegated_warnings_survive_a_zero_exit():
    """orphan_check.sh DELIBERATELY exits 0 while printing '[not yours]' warnings.
    Keeping child output only for non-zero exits discarded all 12 of them — exit
    code is not the signal for an advisory tool, the TEXT is."""
    src = pathlib.Path(cc.__file__).read_text(encoding='utf-8')
    assert 'r.returncode or warned' in src
    assert 'exit 0, but it WARNED' in src


def test_CATO2_live_docket_has_no_false_positives():
    """The identity check must be quiet on the REAL files, or it is noise."""
    real = _SAMDIR
    if not (real / 'docket' / 'CATALYSTS.tsv').exists():
        raise Skipped('real docket not present (sandbox run)')
    old, cc.SAM = cc.SAM, real
    try:
        p = []
        cc.check_docket(p, TODAY)
        assert p == [], p
    finally:
        cc.SAM = old




# ---------------------------------------------------------------------------
# SELF-FOUND, 2026-09-19, by adversarially probing the round-2 repair BEFORE
# reporting it as done. Both escaped every test written up to that point.
# ---------------------------------------------------------------------------

def test_apostrophes_do_not_form_a_quoted_span():
    """Two ordinary apostrophes — a possessive and a contraction — formed a
    spurious 'quoted' span that swallowed a LIVE claim. English prose is full of
    apostrophes, so single quotes are unusable as a retirement marker."""
    line = "PREDICTIONS.tsv SAM's 9 OPEN rows aren't final"
    assert cc._quoted_spans(line) == [], cc._quoted_spans(line)
    assert _scoreboard(line) != []
    assert _scoreboard("PREDICTIONS.tsv scoreboard isn't right: 9 OPEN per PROME's ledger") != []


def test_double_quotes_still_suppress():
    """The apostrophe fix must not gut the guard."""
    assert _scoreboard('PREDICTIONS.tsv: read "4 OPEN as of 2026-08-27" until 9/19.') == []


def test_tenor_swap_is_caught():
    """'JGB 10Y auction' and 'JGB 2Y auction' share {jgb, auction}, so a bare
    overlap floor of >=2 passed a swap between them — and this desk tracks many
    auctions differing only by tenor. Jaccard uses the DIFFERENCES too."""
    p = _docket('| Tue Oct 06 2026 | JGB 10Y auction |\n',
                '2026-10-06\tJGB 2Y auction\tw\tt\tp\tc\tn\tt\n')
    # C2 = no plausible match at all; C3 = matched, but the TENOR discriminator
    # differs. Since the round-3 fix this case is correctly the more specific C3.
    assert any(x.startswith(('C2', 'C3')) for x in p), p


def test_similarity_threshold_has_margin_on_live_data():
    """Measured 2026-09-19: every live true pair scores 1.00 and the tenor-swap
    decoy scores 0.50, so 0.6 has margin both ways. If a future wording change
    pushes a true pair near the line, this test says so before it becomes noise."""
    real = _SAMDIR
    if not (real / 'docket' / 'CATALYSTS.tsv').exists():
        raise Skipped('real docket not present')
    cal = cc._calendar_forward_events((real / 'docket' / 'CALENDAR.md').read_text(encoding='utf-8'))
    cat = {}
    old, cc.SAM = cc.SAM, real
    try:
        rows = [r for r in cc._catalysts_all() if (r.get('date') or '').strip() >= TODAY]
    finally:
        cc.SAM = old
    for r in rows:
        cat.setdefault(r['date'], []).append(r.get('event') or '')
    worst = 1.0
    for d, evs in cat.items():
        pool = list(cal.get(d, []))
        for ev in evs:
            if not pool:
                continue
            def j(c):
                a, b = cc._tokens(ev), cc._tokens(c)
                return len(a & b) / len(a | b) if (a | b) else 0.0
            best = max(pool, key=j)
            worst = min(worst, j(best))
            pool.remove(best)
    assert worst >= 0.75, 'live true pairs down to %.2f — too close to the 0.60 bar' % worst




# ---------------------------------------------------------------------------
# CATO round 3, 2026-09-19. These do not just add counterexamples — each names
# the ASSUMPTION that failed, because the specific fixes were already correct
# and the assumptions behind them were not.
# ---------------------------------------------------------------------------

def test_R3_quoting_alone_does_not_prove_a_figure_is_retired():
    """ASSUMPTION THAT FAILED: 'quoted == retired'. Quotes mark QUOTATION, which is
    equally used for a LIVE claim. Suppression now requires quoting AND a positive
    history cue on the line; the default is to flag."""
    live = 'PREDICTIONS.tsv currently reports "9 OPEN"; use that count today.'
    assert _scoreboard(live) != [], 'a quoted LIVE claim must still be caught'
    hist = 'PREDICTIONS.tsv ... It read "4 OPEN as of 2026-08-27" until 2026-09-19'
    assert _scoreboard(hist) == [], 'a quoted HISTORICAL value must stay suppressed'


def test_R3_tenor_swap_inside_a_long_live_title():
    """ASSUMPTION THAT FAILED: that a similarity THRESHOLD can stand in for identity.
    A long title dilutes the one token carrying the meaning. My decoy used short
    names and scored 0.50; CATO used the LIVE Oct-8 row and scored 0.80, clearing
    the bar. Tenors are now compared directly instead of averaged away."""
    real = 'JGB 30Y auction \u2014 THE NEXT TEST THE FROZEN BARS ACTUALLY APPLY TO'
    swapped = real.replace('30Y', '20Y')
    a, b = cc._tokens(real), cc._tokens(swapped)
    assert len(a & b) / len(a | b) > 0.6, 'premise: the swap clears the similarity bar'
    p = _docket('| Thu Oct 08 2026 | %s |\n' % real,
                '2026-10-08\t%s\tw\tt\tp\tc\tn\tt\n' % swapped)
    assert any(x.startswith('C3') for x in p), p


def test_R3_matching_tenors_stay_quiet():
    real = 'JGB 30Y auction \u2014 THE NEXT TEST THE FROZEN BARS ACTUALLY APPLY TO'
    p = _docket('| Thu Oct 08 2026 | %s |\n' % real,
                '2026-10-08\t%s\tw\tt\tp\tc\tn\tt\n' % real)
    assert p == [], p


def test_R3_a_delegated_tool_that_could_not_run_fails_the_gate():
    """ASSUMPTION THAT FAILED: that printing a child's status is the same as acting
    on it. run_delegated results were never joined to `problems`, so a TIMEOUT
    printed 'ERROR' and the scoped PASS footer still appeared. A check that did not
    execute is not a check that passed."""
    import io as _io, contextlib as _c, sys as _sys
    saved = cc.run_delegated
    cc.run_delegated = lambda: [('root 1e', 'python3 scripts/claim_check.py', 'ERROR', '        | timed out')]
    argv = _sys.argv
    _sys.argv = ['x']
    try:
        buf = _io.StringIO()
        with _c.redirect_stdout(buf):
            rc = cc.main()
        out = buf.getvalue()
        assert rc == 1, 'a delegated timeout must fail the gate'
        assert 'could not run (timeout or crash)' in out
        assert 'CLOSEOUT-CHECK PASS' not in out
    finally:
        cc.run_delegated = saved
        _sys.argv = argv


def test_R3_truncated_warnings_say_how_many_were_hidden():
    """ASSUMPTION THAT FAILED: that showing SOME warnings is enough. Eight actionable
    lines became six displayed with no pointer, so the reader could not tell anything
    was missing."""
    saved = cc.DELEGATED
    cc.DELEGATED = [('root 1b', ['python3', '-c',
                                 'print(chr(10).join("\u26a0\ufe0f warn %d" % i for i in range(9)))'])]
    try:
        tails = [t for _l, _c2, _rc, t in cc.run_delegated()]
        assert 'MORE warning line(s) NOT SHOWN' in tails[0], tails[0]
        assert 'for the full log' in tails[0]
    finally:
        cc.DELEGATED = saved


# ---------------------------------------------------------------------------
# 2026-09-19 PM — SAM-28 regraded to RESOLVED — QUALIFIED / NO-VERDICT.
# Counterexamples built from the LIVE wording that shipped that evening, not from
# a synthetic fixture — the composed-fixture trap this file has hit twice.
# Each test below was RUN AGAINST THE PRE-FIX CODE first; all three fail there.
# ---------------------------------------------------------------------------

def _qual_dir(status_line):
    """3 rows: one CONFIRMED, one FAILED, one QUALIFIED. No OPEN rows."""
    d = pathlib.Path(tempfile.mkdtemp())
    (d / 'thesis').mkdir()
    hdr = '\t'.join(cc.PRED_FIELDS)
    rows = [hdr,
            '\t'.join(['SAM-01', '2026-01-01', 'p', '50%', 't', 'CONFIRMED', '2026-02-01', 'TRUE', 'n']),
            '\t'.join(['SAM-02', '2026-01-01', 'p', '50%', 't', 'FAILED', '2026-02-01', 'FALSE', 'n']),
            '\t'.join(['SAM-28', '2026-06-22', 'p', '40%', 't',
                       'RESOLVED — QUALIFIED / NO-VERDICT', '2026-09-18', 'QUALIFIED', 'n'])]
    (d / 'thesis' / 'PREDICTIONS.tsv').write_text('\n'.join(rows) + '\n', encoding='utf-8')
    (d / 'STATUS.md').write_text(status_line, encoding='utf-8')
    return d


def _run_qual(status_line):
    d = _qual_dir(status_line)
    old, cc.SAM = cc.SAM, d
    try:
        p = []
        res = cc.check_scoreboard(p)
        return p, res
    finally:
        cc.SAM = old


def test_QUAL_new_status_token_is_classified():
    """PRE-FIX: 'unclassified Status value' and check_scoreboard returns None, so
    every downstream scoreboard comparison is skipped entirely."""
    p, res = _run_qual('Scoreboard 1 CONFIRMED / 1 FAILED / 0 special / 1 qualified / 0 OPEN\n')
    assert res is not None, 'the qualified token must not blind the whole check'
    assert not any('unclassified' in x for x in p), p
    assert not any(x.startswith('D ') for x in p), p


def test_QUAL_five_part_scoreboard_with_a_wrong_number_fires():
    """PRE-FIX: no 5-part pattern existed, so the assertion went unchecked.

    ⚠️ The first version of this test asserted only `startswith('D ')` and PASSED
    against the pre-fix code — the unclassified-status problem also starts with 'D ',
    so it passed for the WRONG REASON and discriminated nothing. Asserting on the
    mismatch MESSAGE is what makes it a real regression test."""
    p, _ = _run_qual('Scoreboard 1 CONFIRMED / 9 FAILED / 0 special / 1 qualified / 0 OPEN\n')
    hits = [x for x in p if x.startswith('D ') and 'asserts scoreboard' in x]
    assert hits, 'expected a 5-part scoreboard MISMATCH, got: %s' % p
    assert '1/9/0/1/0' in hits[0], hits


def test_QUAL_four_part_scoreboard_is_incomplete_once_a_qualified_row_exists():
    """The four numbers are each CORRECT here; the defect is the omitted class, so
    the parts no longer sum to the file. PRE-FIX this passed on both counts."""
    p, _ = _run_qual('Scoreboard 1 CONFIRMED / 1 FAILED / 0 special / 0 OPEN\n')
    assert any(x.startswith('D ') and 'qualified' in x for x in p), p


if __name__ == '__main__':
    fails = skips = 0
    for name, fn in sorted(globals().items()):
        if name.startswith('test_') and callable(fn):
            try:
                fn()
                print('PASS', name)
            except Skipped as e:
                skips += 1
                print('SKIP', name, '--', e)
            except AssertionError as e:
                fails += 1
                print('FAIL', name, '--', str(e)[:160])
    print('\n%d failure(s), %d skipped' % (fails, skips))
    if skips:
        print('⚠️  A SKIP is not a PASS. A skipped end-to-end test verified nothing.')
    sys.exit(1 if fails else 0)
