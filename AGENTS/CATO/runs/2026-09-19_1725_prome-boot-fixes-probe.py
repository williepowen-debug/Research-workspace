"""Read-only counterexample and queue census; prints revision and source hashes."""
import contextlib
import datetime as dt
import hashlib
import io
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.dont_write_bytecode = True
sys.path.insert(0, str(ROOT / 'PROME/tools'))
import spawn_list as s
import session_presence as p
import docket_view as d

print('HEAD:', subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip())
for name in ('PROME/tools/spawn_list.py', 'PROME/tools/session_presence.py',
             'PROME/tools/prome_gate.py', 'PROME/DOCKET.tsv',
             'AGENTS/TERRY/scripts/positions_from_forge.py'):
    print(hashlib.sha256((ROOT / name).read_bytes()).hexdigest(), name)

class NoGit:
    def last_self_commit(self, owner):
        return None

now = dt.datetime(2026, 9, 19, 20, tzinfo=dt.timezone.utc)
data = {'host': 'fixture', 'observed_at': now.isoformat()}
rows = s.collect('2026-09-19\tSample obligation\tPROME\tPENDING\tx\ty\n',
                 '', now.date(), 0, NoGit())
for label, supplied, snapshot in [('empty valid', [], data),
                                   ('empty stale', [], {**data, 'observed_at': '2026-09-18T20:00:00+00:00'}),
                                   ('actual producer row', rows, data)]:
    output = io.StringIO()
    try:
        with contextlib.redirect_stdout(output):
            rc = p.report(supplied, snapshot, now, 'fixture')
        result = f'rc={rc}'
    except Exception as exc:
        result = f'{type(exc).__name__}: {exc}'
    print(label, result, 'complete_marker=', 'Full due-row view complete' in output.getvalue())
print('producer width:', len(rows[0]))
live = [r for r in d.load_docket(ROOT / 'PROME/DOCKET.tsv') if d.state_kind(r['state']) == 'PENDING']
print('live:', len(live), 'PROME named:', sum('PROME' in r['owners'] for r in live),
      'PROME first:', sum(s.owner_token(r['owners']) == 'PROME' for r in live))
today = [r for r in live if r['end'] == now.date()]
print('dated today:', len(today), 'PROME first:', sum(s.owner_token(r['owners']) == 'PROME' for r in today))
