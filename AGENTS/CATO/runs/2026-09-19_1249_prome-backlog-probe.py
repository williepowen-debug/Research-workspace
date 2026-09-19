#!/usr/bin/env python3
"""Read-only reproduction of PROME backlog counts and two hidden obligations."""
import datetime as dt
import importlib.util
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[3]
REV = '45b99d158d3143d1ec7a7ba2a6cb0fad6edc83f5'
TODAY = dt.date(2026, 9, 19)


def pinned(path):
    return subprocess.check_output(['git', 'show', REV + ':' + path], cwd=ROOT, text=True)


# The canonical parser is used, not a substring reconstruction of PENDING.
# Refuse changed code so this receipt cannot silently become a repair test.
for path in ('PROME/tools/spawn_list.py', 'scripts/docket_view.py'):
    assert (ROOT / path).read_text() == pinned(path), 'Parser changed; rebase this probe explicitly'
spec = importlib.util.spec_from_file_location('spawn_list_review', ROOT / 'PROME/tools/spawn_list.py')
sl = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sl)
text = pinned('PROME/DOCKET.tsv')
rows = sl.list_open(text, TODAY)
involved = [r for r in rows if 'PROME' in r[2]]
primary = [r for r in rows if sl.owner_token(r[2]) == 'PROME']
today_rows = [r for r in involved if r[1] == TODAY.isoformat()]
future = [r for r in involved if sl.DATE.findall(r[1]) and
          '2026-09-20' <= sl.DATE.findall(r[1])[-1] <= '2026-09-26']
print('Snapshot:', REV)
print('Canonical PENDING, PROME anywhere in owner cell:', len(involved))
print('Canonical PENDING, PROME first owner:', len(primary))
print('Due September 19, PROME involved:', len(today_rows))
print('Due September 19, PROME first owner:', sum(r[1] == '2026-09-19' for r in primary))
print('Next seven days Sep20-26, PROME involved, range END used:', len(future))
print('Today line numbers:', [r[0] for r in today_rows])
for n in (291, 292, 333, 441, 444):
    cols = text.splitlines()[n - 1].split('\t')
    kind = sl.state_kind(cols[3])
    print('L%d: %s; date=%s; state-prefix=%r' % (n, kind, cols[0], cols[3][:90]))
    assert kind == 'TERMINAL'
    if n in (441, 444):
        assert 'PENDING' in cols[3]
        assert n not in {r[0] for r in rows}
        print('  COUNTEREXAMPLE: unfinished obligation with buried PENDING absent from list_open')
print('September 12 to September 19:', (TODAY - dt.date(2026, 9, 12)).days, 'days old')
print('Canonical >7-day stale condition:', (TODAY - dt.date(2026, 9, 12)).days > 7)
print('Pinned SCRATCH bytes:', len(pinned('PROME/SCRATCH.md').encode()))
print('Read-cap:', 32550)
print('No queue mutations or owner sends.')
