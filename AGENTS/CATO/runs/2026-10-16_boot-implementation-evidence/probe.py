"""Read-only producer/consumer probes pinned to PROME's boot implementation.

Run from repository root: python3 <this-file> SNAPSHOT_DIRECTORY
Snapshot must contain the relevant files from git archive 1684ae0d7.
No gate execution, network, market calls or live state writes.
"""
import ast
import contextlib
import csv
import datetime as dt
import importlib.util
import io
import json
import math
from pathlib import Path
import re
import runpy
import subprocess
import sys
import tempfile
import types

REV = '1684ae0d7920c66faedb60c7643f4dcbef9a17d0'
snap = Path(sys.argv[1]).resolve()
sys.dont_write_bytecode = True
sys.path.insert(0, str(snap / 'PROME/tools'))

def show(path, rev=REV):
    return subprocess.check_output(['git', 'show', f'{rev}:{path}'], text=True)

def load(name):
    spec = importlib.util.spec_from_file_location(name, snap / f'PROME/tools/{name}.py')
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module

out = {'revision': REV}
orch = load('orch_closeout')
rows = list(csv.reader(io.StringIO(show('PROME/state/ORCH_LOG.tsv')), delimiter='\t', quoting=csv.QUOTE_NONE))
cruise = [r for r in rows if len(r) > 8 and r[0] == '2026-10-16' and 'agent-tool:desk:cruise-1016' in r[8]]
assert len(cruise) == 1
row = cruise[0]
state, detail = orch.disposition(row, dt.datetime(2026, 10, 16, 17, tzinfo=dt.timezone.utc))
assert state == 'UNKNOWN' and 'missing required evidence' in detail, (state, detail)
data = json.loads(row[8].split(orch.MARKER, 1)[1])
out['cruise_actual_record'] = {'source': 'PROME/state/ORCH_LOG.tsv', 'structured': data, 'state': state, 'detail': detail}
fixed = row.copy()
data_fixed = dict(data, receipt=data['ask'].split('RECEIPT ', 1)[1])
fixed[8] = row[8].split(orch.MARKER, 1)[0] + orch.MARKER + json.dumps(data_fixed)
assert orch.disposition(fixed, dt.datetime(2026, 10, 16, 17, tzinfo=dt.timezone.utc))[0] == 'ASKED_RECEIPT'
out['cruise_positive_control'] = 'ASKED_RECEIPT after adding the separate receipt field in an in-memory copy'

w = load('willq_view')
with tempfile.TemporaryDirectory(prefix='cato-willq-order-') as d:
    q, s = Path(d) / 'queue.md', Path(d) / 'scratch.md'
    original = show('PROME/WILL_QUEUE.md')
    q.write_text(original)
    s.write_text(w.render(w.parse_open(original), dt.date(2026, 10, 16)))
    capture = io.StringIO()
    with contextlib.redirect_stdout(capture):
        before = w.do_check(s, q)
        # Model a private ruling closing an actually open producer row; no actual ruling is asserted.
        changed, n = re.subn(r'(?m)^\| 450 \|', '| 450 | CLOSED ', original, count=1)
        assert n == 1
        q.write_text(changed)
        after = w.do_check(s, q)
        w.do_write(s, q, dt.date(2026, 10, 16), False)
        repaired = w.do_check(s, q)
    assert (before, after, repaired) == (0, 1, 0)
    out['post_gate_ruling_fixture'] = {'producer': 'pinned real WILL_QUEUE row 450; hypothetical close in temp copy', 'before': before, 'after_private_mutation': after, 'after_existing_view_regeneration': repaired, 'log': capture.getvalue().replace(d, '<temp>')}

config = runpy.run_path(str(snap / 'FORGE/tools/market-data/config.py'))
tree = ast.parse((snap / 'FORGE/tools/market-data/dashboard.py').read_text())
names = {'finite_value', 'available', '_weekdays_between', 'fetch_all'}
pure = ast.Module(body=[n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name in names], type_ignores=[])
env = {'math': math, 'datetime': dt, 'time': types.SimpleNamespace(strftime=lambda _: '2026-10-16'), 'VOL_MARKS': set(), 'VOL_ZERO_EPS': .005}
for name in ['classify', 'get_emoji', 'format_value']:
    env[name] = config[name]
exec(compile(pure, 'pinned_dashboard_functions', 'exec'), env)
series = next(s for s in config['SERIES'] if s['id'] == 'APO')
out['dashboard_fixtures'] = []
for label, payload in [('dated_today', {'price': 100, 'prev': 99, 'asof': '2026-10-16'}), ('dated_yesterday', {'price': 100, 'prev': 99, 'asof': '2026-10-15'}), ('missing_date', {'price': 100, 'prev': 99}), ('error', {'error': 'synthetic unavailable feed'})]:
    env['price_fetch'] = lambda tickers, p=payload: {'APO': p}
    result = env['fetch_all']([series])[0]
    out['dashboard_fixtures'].append({'case': label, 'available': env['available'](result), 'flags': result['flags'], 'date': result['date']})
assert out['dashboard_fixtures'][1]['available'] and '⚠stale' in out['dashboard_fixtures'][1]['flags']
assert not out['dashboard_fixtures'][3]['available']

unchanged = ['CLAUDE.md', 'PROME/CLAUDE.md', 'PROME/ACTIVE_DECISIONS.md', 'HEARTBEAT.md', 'PROME/tools/prome_gate.py', 'PROME/tools/boot_session.py', 'PROME/tools/table_check.py']
assert all(show(p) == show(p, REV + '^') for p in unchanged)
out['unchanged_vs_parent'] = unchanged
assert show('.claude/skills/boot/SKILL.md') == show('PROME/.claude/skills/boot/SKILL.md')
out['boot_skill_parity'] = True
def modes(txt):
    return [(r['reader'], r['path'], r['mode']) for r in csv.DictReader((line for line in txt.splitlines() if line and not line.startswith('#')), delimiter='\t')]
assert modes(show('PROME/registry/READS.tsv')) == modes(show('PROME/registry/READS.tsv', REV + '^'))
out['all_reads_modes_unchanged'] = True
def harvested_reads(boot):
    seq = boot.split('## Boot Sequence', 1)[-1].split('## Conditional Modules')[0]
    return sorted({path for line in seq.splitlines() if re.search(r'\bRead\b', line)
                   for path in re.findall(r'`((?:PROME/)?[A-Z][A-Za-z_]+\.(?:md|tsv))`', line)})
assert harvested_reads(show('PROME/BOOT.md')) == harvested_reads(show('PROME/BOOT.md', REV + '^'))
out['symmetry_reads'] = harvested_reads(show('PROME/BOOT.md'))
table = load('table_check')
out['table_perimeter'] = [str(p.relative_to(snap)) for p in table.perimeter()]
assert 'PROME/ACTIVE_DECISIONS.md' in out['table_perimeter']
assert 'HEARTBEAT.md' in out['table_perimeter']
for needle in ['**⚡ ONE-SHOT GATE', '**Reading those five verdicts']:
    before = [s for s in show('PROME/BOOT.md', REV + '^').splitlines() if needle in s]
    after = [s for s in show('PROME/BOOT.md').splitlines() if needle in s]
    assert before and before == after, needle
out['gate_and_five_verdict_bullets_unchanged'] = True
print(json.dumps(out, indent=2, ensure_ascii=False))
