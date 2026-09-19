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

_ROOT = pathlib.Path(__file__).resolve().parents[3]
_SPEC = importlib.util.spec_from_file_location(
    'closeout_check', pathlib.Path(__file__).resolve().parents[1] / 'closeout_check.py')
cc = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(cc)

TODAY = '2026-09-19'

CAL_HEAD = "# SAM CALENDAR\n\n| Date | Event |\n|---|---|\n"
CAL_RESOLVED = "\n## ✅ RESOLVED\n\n| Date | Event |\n|---|---|\n| Wed Sep 16 2026 | done |\n"
CAT_HEAD = "date\tevent\twhat_to_check\tthreshold_signal\tpriority\twho_cares\tnotes\ttype\n"


def _fixture(cal_rows, cat_dates):
    d = pathlib.Path(tempfile.mkdtemp())
    (d / 'docket').mkdir()
    (d / 'docket' / 'CALENDAR.md').write_text(
        CAL_HEAD + ''.join('| %s | x |\n' % r for r in cal_rows) + CAL_RESOLVED, encoding='utf-8')
    (d / 'docket' / 'CATALYSTS.tsv').write_text(
        CAT_HEAD + ''.join('%s\tev\tw\tt\t●\tSAM\tn\ttype\n' % x for x in cat_dates), encoding='utf-8')
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
            print('   SKIP test_catches_the_actual_incident (commit not reachable)')
            return
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


if __name__ == '__main__':
    fails = 0
    for name, fn in sorted(globals().items()):
        if name.startswith('test_') and callable(fn):
            try:
                fn()
                print('PASS', name)
            except AssertionError as e:
                fails += 1
                print('FAIL', name, '--', str(e)[:160])
    print('\n%d failure(s)' % fails)
    sys.exit(1 if fails else 0)
