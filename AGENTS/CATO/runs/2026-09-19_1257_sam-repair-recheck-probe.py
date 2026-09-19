#!/usr/bin/env python3
"""Pinned repair review: controls and remaining counterexamples; no owner edits."""
import contextlib
import io
from pathlib import Path
import subprocess
import sys
import tempfile
import types
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[3]
REV = '003e7b14e4e96d5c79ac01608b88e914432dac6a'


def source(path):
    return subprocess.check_output(['git', 'show', REV + ':' + path], cwd=ROOT, text=True)


cc = types.ModuleType('sam_repair_review')
cc.__file__ = str(ROOT / 'AGENTS/SAM/scripts/closeout_check.py')
exec(compile(source('AGENTS/SAM/scripts/closeout_check.py'), cc.__file__, 'exec'), cc.__dict__)

print('Pinned SAM revision:', REV)
with tempfile.TemporaryDirectory(prefix='cato-sam-recheck-') as tmp:
    cc.SAM = Path(tmp) / 'fixture'
    for rel in ('docket/CALENDAR.md', 'docket/CATALYSTS.tsv', 'thesis/PREDICTIONS.tsv'):
        dest = cc.SAM / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(source('AGENTS/SAM/' + rel))
    thesis = cc.SAM / 'thesis/THESIS.md'

    def scoreboard(text):
        thesis.write_text(text)
        problems = []
        derived, _ = cc.check_scoreboard(problems)
        assert derived == (16, 16, 1, 1)
        return problems

    assert scoreboard('PREDICTIONS.tsv: 4 OPEN.')
    print('CLOSED reproduction: unquoted lone stale OPEN count detected')
    assert not scoreboard('PREDICTIONS.tsv: 4 OPEN')
    print('REMAINING: unquoted stale count at end of line is skipped; empty string matches quote-character test')
    stale = subprocess.check_output(['git', 'show', '22e55db36^:AGENTS/SAM/thesis/THESIS.md'], cwd=ROOT, text=True)
    assert scoreboard(stale)
    print('CLOSED reproduction: actual full pre-repair THESIS now detected')
    assert not scoreboard('PREDICTIONS.tsv currently has `4 OPEN`.')
    print('REMAINING: live backticked 4 OPEN claim suppressed as if historical')
    assert not scoreboard('PREDICTIONS.tsv: 4 OPEN. Scoreboard 16 CONFIRMED / 16 FAILED / 1 special.')
    print('REMAINING: correct 3-part scoreboard suppresses incorrect separate OPEN count on same line')
    assert not scoreboard('PREDICTIONS.tsv: this line read "4 OPEN as of August" until corrected.')
    print('CONTROL: genuine quoted correction history is quiet')

    cal = cc.SAM / 'docket/CALENDAR.md'
    original = cal.read_text()

    def docket():
        problems = []
        cc.check_docket(problems, '2026-09-19')
        return problems

    assert not docket()
    print('CONTROL: current docket passes; parsed rows:', sum(cc._calendar_forward_counts(original).values()))
    lines = original.splitlines(keepends=True)
    selected = [l for l in lines if l.startswith('|') and 'Sep 30 2026' in l and '2Y' in l]
    assert len(selected) == 1
    cal.write_text(''.join(l for l in lines if l not in selected))
    assert any(p.startswith('C ') for p in docket())
    print('CLOSED reproduction: deleted September 30 JGB 2Y event now detected')
    cal.write_text(original.replace(selected[0], selected[0].replace('2Y', '99Y')))
    assert not docket()
    print('REMAINING: replace JGB 2Y with different event JGB 99Y, same date/count; C passes')
    cal.write_text(original.replace('## ✅ RESOLVED', '| TBD | Extra undated live event |\n\n## ✅ RESOLVED', 1))
    assert not docket()
    print('REMAINING: undated CALENDAR forward event silently ignored')
    cal.write_text(original)

    cc._assert_table_matches_delegations()
    no_orphan = [(label, cmd) for label, cmd in cc.DELEGATED if label != 'root 1b']
    with patch.object(cc, 'DELEGATED', no_orphan):
        try:
            cc._assert_table_matches_delegations()
        except ValueError:
            print('CLOSED reproduction: removing declared orphan delegation raises')
        else:
            raise AssertionError('table/list mismatch accepted')

    # Obtain a REAL orphan advisory from an isolated repository, not a fabricated rc.
    sandbox = Path(tmp) / 'orphan-repo'
    sandbox.mkdir()
    subprocess.run(['git', 'init', '-q', str(sandbox)], check=True, capture_output=True)
    subprocess.run(['git', '-C', str(sandbox), 'config', 'status.showUntrackedFiles', 'all'], check=True)
    packet = sandbox / 'AGENTS/PROME/inbox/2026-09-19_from-SAM_probe.md'
    packet.parent.mkdir(parents=True)
    packet.write_text('Temporary fixture only.\n')
    orphan_script = Path(tmp) / 'orphan_check.sh'
    orphan_script.write_text(source('scripts/orphan_check.sh'))
    actual = subprocess.run(['bash', str(orphan_script), 'SAM'], cwd=sandbox, capture_output=True, text=True)
    assert actual.returncode == 0 and '[likely YOURS]' in actual.stdout, (actual.returncode, actual.stdout, actual.stderr)

    def fake_child(cmd, **kwargs):
        if 'scripts/orphan_check.sh' in cmd:
            return actual
        return subprocess.CompletedProcess(cmd, 0, '', '')

    with patch.object(cc.subprocess, 'run', fake_child):
        receipts = cc.run_delegated()
    receipt = next(r for r in receipts if r[0] == 'root 1b')
    assert receipt[2] == 0 and receipt[3] == ''
    print('REMAINING: real rc=0 orphan advisory identifies likely SAM packet; wrapper discards it and reports ok')

    with contextlib.ExitStack() as stack:
        for name in ('check_docket', 'check_sidecar', 'check_sam_memory', 'check_brief_ordering', 'check_tree_clean'):
            stack.enter_context(patch.object(cc, name, lambda *args: None))
        stack.enter_context(patch.object(cc, 'check_scoreboard', lambda p: ((16, 16, 1, 1), ['SAM-33'])))
        stack.enter_context(patch.object(cc, 'run_delegated', lambda: [('root 1b', 'bash scripts/orphan_check.sh', 'ERROR', 'timeout')]))
        stack.enter_context(patch.object(sys, 'argv', ['closeout_check.py']))
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            rc = cc.main()
    assert rc == 0 and 'CLOSEOUT-CHECK PASS' in output.getvalue()
    print('REMAINING: failed child execution is displayed ERROR but still exits 0/PASS; self-check scope caveat remains')

print('Repair verification completed; no owner files changed.')
