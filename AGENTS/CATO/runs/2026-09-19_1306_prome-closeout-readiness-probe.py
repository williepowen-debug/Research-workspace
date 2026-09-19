#!/usr/bin/env python3
"""Targeted isolated checks; does not run PROME boot/closeout or write its outputs."""
import contextlib
import datetime as dt
import hashlib
import io
from pathlib import Path
import subprocess
import sys
import tempfile
import types
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[3]
REV = '7cc6bc5b3175bffc157387750661e0138d80ea5b'
sys.path.insert(0, str(ROOT / 'PROME/tools'))


def module(name, rel, revision=REV):
    src = subprocess.check_output(['git', 'show', revision + ':' + rel], cwd=ROOT, text=True)
    mod = types.ModuleType(name)
    mod.__file__ = str(ROOT / rel)
    sys.modules[name] = mod
    exec(compile(src, mod.__file__, 'exec'), mod.__dict__)
    return mod


gate = module('review_gate_new', 'PROME/tools/prome_gate.py')
old = module('review_gate_old', 'PROME/tools/prome_gate.py', REV + '^')
deck = module('review_deck', 'PROME/tools/decision_deck.py')
today = dt.date(2026, 9, 19)
header = '| # | Item | Type | Needed by | Since | PROME rec | Notes |\n'
row = '| {id} | A live ask | RULE | {due} | 9/19 | approve | notes |\n'

print('Pinned revision:', REV)
with tempfile.TemporaryDirectory(prefix='cato-prome-closeout-') as tmp:
    root = Path(tmp)
    (root / 'PROME').mkdir()
    queue = root / 'PROME/WILL_QUEUE.md'
    queue.write_text('**Last reconciled:** 2026-09-19\n## OPEN\n' + header +
                     row.format(id='1', due='2026-02-30') + row.format(id='2', due='2026-09-19'))
    for label, mod in [('before', old), ('after', gate)]:
        mod.ROOT = root
        mod.results.clear()
        mod.guard(mod.check_will_queue)
        rc = mod.aggregate_rc(mod.results, [])
        problems = mod.check_will_queue.last_problems
        print('F1', label, 'aggregate_rc=', rc, 'problems=', problems)
        if label == 'before':
            assert rc == 2 and any(r[0] == mod.ERROR for r in mod.results)
            print('  Before repair: explicit ERROR/UNKNOWN, not a passing production gate')
        else:
            assert any('IMPOSSIBLE DATE #1' in p for p in problems)
            assert any('DUE TODAY #2' in p for p in problems)
            assert rc == 0 and all(r[0] == mod.ADVISE for r in mod.results)
            print('  After repair: impossible row named; due sibling preserved')
            print('  REMAINING: invalid input is only ADVISE; rc 2 became rc 0, not fail-closed')

    deck.Q = queue
    with contextlib.ExitStack() as stack:
        stack.enter_context(patch.object(deck, 'load_explainers', lambda: {}))
        for name in ('parse_decided', 'parse_active', 'parse_docket'):
            stack.enter_context(patch.object(deck, name, lambda *args: []))
        for ident, wide in [('1', True), ('32b', False), ('32b', True)]:
            h = header.rstrip('\n') + ' Extra |\n' if wide else header
            queue.write_text('## OPEN\n' + h + row.format(id=ident, due='2026-09-19'))
            out = root / ('owed-' + ident + '-' + str(wide) + '.html')
            stderr = io.StringIO()
            with contextlib.redirect_stderr(stderr):
                try:
                    result = deck.build(today, out, reference_out=root / 'reference.html')
                except SystemExit as exc:
                    assert ident == '1' and wide and not out.exists()
                    print('F2 numeric-ID widened header: refused before write; control repaired')
                else:
                    contents = out.read_text()
                    if wide:
                        assert 'Nothing owed.' in contents
                        print('F2 REMAINS: supported lettered ID 32b + widened header builds Nothing owed over live ask')
                    else:
                        assert 'Nothing owed.' not in contents
                        print('F2 CONTROL: normal header accepts and renders supported lettered ID 32b')

data = (ROOT / 'FORGE/STATUS.md').read_bytes()
print('Reviewed working FORGE bytes:', len(data), 'over cap:', len(data) - 32550)
print('FORGE SHA256:', hashlib.sha256(data).hexdigest())
print('No owner mutations; hypothetical Deck outputs stayed in temporary directory.')
