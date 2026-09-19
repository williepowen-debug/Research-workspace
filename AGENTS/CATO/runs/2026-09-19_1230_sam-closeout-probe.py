#!/usr/bin/env python3
"""Offline review counterexamples, pinned to SAM's reported build; no owner writes."""
import contextlib
import io
from pathlib import Path
import subprocess
import sys
import tempfile
import types
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[3]
REV = '12c399ce5735977ca36b29f939a2e29553743322'
PREFIX = 'AGENTS/SAM/'


def source(path, rev=REV):
    return subprocess.check_output(['git', 'show', rev + ':' + PREFIX + path],
                                   cwd=ROOT, text=True)


cc = types.ModuleType('sam_closeout_review')
cc.__file__ = str(ROOT / PREFIX / 'scripts/closeout_check.py')
exec(compile(source('scripts/closeout_check.py'), cc.__file__, 'exec'), cc.__dict__)


def docket():
    problems = []
    cc.check_docket(problems, '2026-09-19')
    return problems


print('Pinned revision:', REV)
with tempfile.TemporaryDirectory(prefix='cato-sam-closeout-') as tmp:
    cc.SAM = Path(tmp)
    for rel in ('docket/CALENDAR.md', 'docket/CATALYSTS.tsv',
                'thesis/PREDICTIONS.tsv', 'thesis/THESIS.md'):
        dest = cc.SAM / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(source(rel))
    assert docket() == []
    print('CONTROL: pinned current docket produces no problems')

    cal = cc.SAM / 'docket/CALENDAR.md'
    original = cal.read_text()
    lines = original.splitlines(keepends=True)
    removed = [line for line in lines if line.startswith('|') and
               'Sep 30 2026' in line and '2Y' in line]
    assert len(removed) == 1, removed
    cal.write_text(''.join(line for line in lines if line not in removed))
    result = docket()
    assert result == [], result
    print('COUNTEREXAMPLE: deleted September 30 JGB 2Y calendar event; A/B/C still pass')
    cal.write_text(original)

    cat = cc.SAM / 'docket/CATALYSTS.tsv'
    original_cat = cat.read_text()
    cat.write_text(original_cat + '\tUNDATED TEST EVENT\tcheck\tthreshold\tLOW\tSAM\tnote\texternal\n')
    result = docket()
    assert result == [], result
    print('COUNTEREXAMPLE: added undated catalyst row; A/B/C still pass')
    cat.write_text(original_cat)

    thesis = cc.SAM / 'thesis/THESIS.md'
    thesis.write_text(source('thesis/THESIS.md', '22e55db36^'))
    assert '4 OPEN as of 2026-08-27' in thesis.read_text()
    problems = []
    derived, _ = cc.check_scoreboard(problems)
    assert derived == (16, 16, 1, 1), derived
    assert problems == [], problems
    print('COUNTEREXAMPLE: actual stale pre-repair THESIS (4 OPEN, 14/14/1) escapes D; derived=', derived)
    thesis.write_text('99 CONFIRMED / 99 FAILED / 99 special / 99 OPEN')
    problems = []
    cc.check_scoreboard(problems)
    assert any(p.startswith('D ') for p in problems)
    print('CONTROL: full-format incorrect scoreboard is detected')

    calls = []

    def fake_run(cmd, **kwargs):
        calls.append(cmd)
        return subprocess.CompletedProcess(cmd, 2, 'CRITICAL_DIAGNOSTIC_MARKER', '')

    with patch.object(cc.subprocess, 'run', fake_run):
        receipts = cc.run_delegated()
    assert len(calls) == 4
    assert not any('scripts/orphan_check.sh' in c for c in calls)
    assert all('CRITICAL_DIAGNOSTIC_MARKER' not in repr(r) for r in receipts)
    print('COUNTEREXAMPLE: advertised orphan_check.sh never called; all delegate diagnostic text discarded')

    # Wiring test only: isolate successful self-checks from failing child tools.
    with contextlib.ExitStack() as stack:
        for name in ('check_docket', 'check_sidecar', 'check_brief_ordering', 'check_tree_clean'):
            stack.enter_context(patch.object(cc, name, lambda *args: None))
        stack.enter_context(patch.object(cc, 'check_scoreboard', lambda p: ((16, 16, 1, 1), ['SAM-33'])))
        stack.enter_context(patch.object(cc.subprocess, 'run', fake_run))
        stack.enter_context(patch.object(sys, 'argv', ['closeout_check.py']))
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            rc = cc.main()
    assert rc == 0 and 'CLOSEOUT-CHECK PASS' in output.getvalue()
    assert 'CRITICAL_DIAGNOSTIC_MARKER' not in output.getvalue()
    print('COUNTEREXAMPLE: all four child checks return rc=2 with diagnostic; main exits 0/PASS, diagnostic hidden')
    print('LIMIT: PASS text explicitly scopes itself to self-checks; this is not proof SAM actually ignored a child failure')

    with patch.object(cc, 'git', lambda *args: ' M AGENTS/SAM/STATUS.md'):
        problems = []
        cc.check_tree_clean(problems)
    assert len(problems) == 1 and problems[0].startswith('G ')
    print('WORKFLOW: legitimate pending STATUS edit fails G, although charter step 15 says run before final commit')

print('All review expectations reproduced. Counterexamples demonstrate gaps, not repairs.')
