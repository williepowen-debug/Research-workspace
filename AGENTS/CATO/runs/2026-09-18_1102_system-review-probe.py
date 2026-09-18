"""Isolated CATO review probes. No owner writes, network calls, or production gates."""
import contextlib
import datetime
import importlib.util
import io
import json
from pathlib import Path
import runpy
import subprocess
import sys
import tempfile
import types
from unittest.mock import patch
from urllib.parse import parse_qs, urlparse

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[3]
SNAPSHOT = '1b1de7d0723cdcfb3cdb5984b2fade234a76ab17'


def source(rel):
    return subprocess.check_output(['git', 'show', SNAPSHOT + ':' + rel], cwd=ROOT, text=True)


def load(name, rel):
    mod = types.ModuleType(name)
    mod.__file__ = str(ROOT / rel)
    exec(compile(source(rel), mod.__file__, 'exec'), mod.__dict__)
    return mod


guard = load('subject_guard', 'PROME/tools/hooks/commit_subject_guard.py')
cmd = 'echo git commit -m "' + 'x' * 101 + '"'
print('HOOK harmless echo:', guard.diagnose(cmd)[0])
assert guard.diagnose(cmd)[0] == 'block'
buf = io.StringIO()
with contextlib.redirect_stderr(buf):
    rc = guard._handle({'tool_name': 'Bash', 'tool_input': {'command': 'git commit -m "$MSG"'}})
print('HOOK runtime subject: rc=', rc, 'advisory=', repr(buf.getvalue()))
assert rc == 0 and not buf.getvalue()

grader = ROOT / 'AGENTS/BOND/analysis/2026-09-17_grade_BND-25_BND-26_on_the_9-16_H15_cells.py'
realdate = datetime.date
class Date(realdate):
    @classmethod
    def today(cls):
        return cls(2026, 9, 23)


def grade(days):
    def pull(url, **kwargs):
        series = parse_qs(urlparse(url).query)['id'][0]
        # Three non-breach sessions, with the rest not yet published.
        rows = ['DATE,' + series] + [f'{d},4.00' for d in days]
        return io.BytesIO(('\n'.join(rows) + '\n').encode())
    out = io.StringIO()
    with patch('urllib.request.urlopen', pull), patch('datetime.date', Date), contextlib.redirect_stdout(out):
        exec(compile(source(str(grader.relative_to(ROOT))), str(grader), 'exec'), {'__name__': '__main__', '__file__': str(grader)})
    result = [line.strip() for line in out.getvalue().splitlines() if '⇒ BND-26' in line or '⇒ VOID-INSUFFICIENT' in line]
    print('BOND on 9/23 with', len(days), 'published sessions:', result)
    return result

assert any('= TRUE' in x for x in grade(['2026-09-16', '2026-09-17', '2026-09-18']))
assert any('VOID-INSUFFICIENT' in x for x in grade(['2026-09-16', '2026-09-17']))

gate = load('daedalus_gate', 'AGENTS/DAEDALUS/scripts/daedalus_gate.py')
with tempfile.TemporaryDirectory(prefix='cato-system-review-') as td:
    repo = Path(td) / 'repo'
    (repo / 'AGENTS/DAEDALUS/runs').mkdir(parents=True)
    (repo / 'PROME').mkdir()
    (repo / 'PROME/DOCKET.tsv').write_text('initial checked input\n')
    log = repo / 'AGENTS/DAEDALUS/runs/GATE_LOG.tsv'
    log.write_text('date_utc\tmode\thead\trc\tcounts\treceipt_sha8\n')
    def git(*args):
        subprocess.run(['git', '-C', str(repo), *args], check=True, capture_output=True)
    git('init', '-q', '-b', 'master')
    git('config', 'user.name', 'CATO isolated probe')
    git('config', 'user.email', 'probe@example.invalid')
    git('add', 'AGENTS/DAEDALUS/runs/GATE_LOG.tsv', 'PROME/DOCKET.tsv')
    git('commit', '-qm', 'fixture')
    ctx = {'root': str(repo), 'today': '2026-09-18', 'args': None}
    step = (gate.Step('T0', 'fixture clean', lambda ctx: (gate.CLEAN, 'fixture', '', 0)), ['fixture'])
    receipts = Path(td) / 'receipts'
    gate.run('probe', [step], ctx, str(receipts), log_row=True)
    rp = next(receipts.glob('*.json'))
    rc = gate.verify_receipt(str(rp), root=str(repo))
    print('GATE immediately after default log append: verify rc=', rc)
    assert rc == 1
    fp_before, _ = gate.fingerprint(str(repo))
    (repo / 'PROME/DOCKET.tsv').write_text('changed checked input\n')
    fp_after, _ = gate.fingerprint(str(repo))
    print('GATE checked PROME/DOCKET input mutation changes fingerprint:', fp_before != fp_after)
    assert fp_before == fp_after
    class Args:
        no_superseded = False
        superseded = [('old', 'new')]
        no_memory = True
        slug = []
        rule_declared = 'none'
        complete_since = None
    ctx['args'] = Args()
    registry = {s.sid: s for s, _ in gate.closeout_registry(ctx)}
    with patch.object(gate, 'sh', return_value=(127, 'fixture child failed')):
        result = registry['C2'].fn(ctx)
    print('GATE consumer child rc 127:', result[:2], 'reported rc=', result[3])
    assert result[0] == gate.CLEAN and result[3] == 0
print('All independent counterexamples reproduced; these are defects, not passing acceptance tests.')

oracle = load('oracle', 'AGENTS/ORACLE/scripts/polymarket.py')
dead = {'question': 'low rung', 'resolved': True, 'yes': 1.0}
live = {'question': 'higher rung', 'resolved': False, 'yes': 0.6}
assert oracle._select_event_leg([dead, live])[0] is live
assert oracle._select_event_leg([dead])[0] is dead
assert oracle._select_event_leg([])[0] is None
print('ORACLE isolated selector checks PASS: mixed ladder chooses live; all-resolved retained; empty handled.')
