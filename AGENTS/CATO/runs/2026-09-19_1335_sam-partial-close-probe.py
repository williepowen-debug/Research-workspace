#!/usr/bin/env python3
"""Bounded independent follow-up against SAM 93d39d1cf. No owner writes."""
import contextlib
import io
from pathlib import Path
import subprocess
import sys
import tempfile
import types
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[3]
REV = '93d39d1cf'


def source(rel):
    return subprocess.check_output(['git', 'show', REV + ':AGENTS/SAM/' + rel], cwd=ROOT, text=True)


cc = types.ModuleType('sam_final_pass')
cc.__file__ = str(ROOT / 'AGENTS/SAM/scripts/closeout_check.py')
exec(compile(source('scripts/closeout_check.py'), cc.__file__, 'exec'), cc.__dict__)
print('Pinned revision:', REV)
with tempfile.TemporaryDirectory(prefix='cato-sam-final-') as tmp:
    cc.SAM = Path(tmp)
    for rel in ('thesis/PREDICTIONS.tsv', 'docket/CALENDAR.md', 'docket/CATALYSTS.tsv'):
        dest = cc.SAM / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(source(rel))

    def score(text):
        (cc.SAM / 'thesis/THESIS.md').write_text(text)
        problems = []
        result = cc.check_scoreboard(problems)
        assert result[0] == (16, 16, 1, 1)
        return problems

    for text in ['PREDICTIONS.tsv: 4 OPEN', 'PREDICTIONS.tsv currently has `4 OPEN`.',
                 'PREDICTIONS.tsv: 4 OPEN. Scoreboard 16 CONFIRMED / 16 FAILED / 1 special.',
                 "PREDICTIONS.tsv SAM's 9 OPEN rows aren't final"]:
        assert score(text), text
    print('VERIFIED: end-of-line, backtick, adjacent correct scoreboard and apostrophe cases detected')
    assert not score('PREDICTIONS.tsv used to read "4 OPEN"; that count is retired.')
    print('CONTROL: actual historical quoted statement stays quiet')
    assert score('PREDICTIONS.tsv currently reports "9 OPEN"; use that count today.')
    print('VERIFIED: explicitly current quoted count is detected')
    text = 'PREDICTIONS.tsv currently reports \"9 OPEN\"; use that count until the next update.'
    assert not score(text)
    print('REMAINS: adding prospective until to a current claim suppresses it:', text)

    def docket():
        problems = []
        cc.check_docket(problems, '2026-09-19')
        return problems

    assert not docket()
    cal = cc.SAM / 'docket/CALENDAR.md'
    original = cal.read_text()
    rows = original.splitlines(keepends=True)
    targets = [l for l in rows if l.startswith('|') and 'Oct 08 2026' in l and 'JGB 30Y' in l]
    assert len(targets) == 1, targets
    old_row = targets[0]
    changed = old_row.replace('JGB 30Y', 'JGB 20Y')
    cal.write_text(original.replace(old_row, changed))
    assert any(x.startswith('C3 ') for x in docket())
    a = cc._tokens(old_row.split('|')[2])
    b = cc._tokens(changed.split('|')[2])
    print('VERIFIED: actual October 8 long-title JGB 30Y -> 20Y swap caught; Jaccard=', len(a & b) / len(a | b))
    cal.write_text(original)

    warnings = '\n'.join('[likely YOURS] AGENTS/PROME/inbox/probe-%d.md' % n for n in range(1, 9))
    with patch.object(cc.subprocess, 'run', lambda cmd, **kw: subprocess.CompletedProcess(cmd, 0, warnings, '')):
        receipt = cc.run_delegated()[0]
    assert 'probe-1.md' in receipt[3]
    assert 'probe-7.md' not in receipt[3] and 'probe-8.md' not in receipt[3]
    assert '2 MORE' in receipt[3] and 'run ' in receipt[3]
    print('PARTIAL: hidden warning count and rerun command now shown; original complete output not saved')
    long_warning = '[likely YOURS] AGENTS/PROME/inbox/' + 'x'*150 + '.md'
    with patch.object(cc.subprocess, 'run', lambda cmd, **kw: subprocess.CompletedProcess(cmd, 0, long_warning, '')):
        receipt = cc.run_delegated()[0]
    assert long_warning not in receipt[3] and 'NOT SHOWN' not in receipt[3]
    print('REMAINS: one long actionable path truncated with no notice')

    with contextlib.ExitStack() as stack:
        for name in ('check_docket', 'check_sidecar', 'check_sam_memory', 'check_brief_ordering', 'check_tree_clean'):
            stack.enter_context(patch.object(cc, name, lambda *args: None))
        stack.enter_context(patch.object(cc, 'check_scoreboard', lambda p: ((16,16,1,1), ['SAM-33'])))
        stack.enter_context(patch.object(cc, 'run_delegated', lambda: [('root 1b', 'bash scripts/orphan_check.sh', 'ERROR', 'timeout')]))
        stack.enter_context(patch.object(sys, 'argv', ['closeout_check.py']))
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            rc = cc.main()
    assert rc == 1 and 'CLOSEOUT-CHECK PASS' not in out.getvalue()
    print('VERIFIED: delegated ERROR now returns rc=1 without PASS')

    with contextlib.ExitStack() as stack:
        for name in ('check_docket', 'check_sidecar', 'check_sam_memory', 'check_brief_ordering', 'check_tree_clean'):
            stack.enter_context(patch.object(cc, name, lambda *args: None))
        stack.enter_context(patch.object(cc, 'check_scoreboard', lambda p: ((16,16,1,1), ['SAM-33'])))
        crash = 'Traceback (most recent call last):\n  File \"child.py\", line 1, in <module>\nRuntimeError: probe crash\n'
        stack.enter_context(patch.object(cc.subprocess, 'run', lambda cmd, **kw: subprocess.CompletedProcess(cmd, 1, '', crash)))
        stack.enter_context(patch.object(sys, 'argv', ['closeout_check.py']))
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            rc = cc.main()
    assert rc == 0 and 'CLOSEOUT-CHECK PASS' in out.getvalue() and 'RuntimeError' in out.getvalue()
    print('REMAINS: child traceback/rc1 travels through actual run_delegated into parent rc0/PASS')
print('Bounded pass complete; no owner mutations.')
