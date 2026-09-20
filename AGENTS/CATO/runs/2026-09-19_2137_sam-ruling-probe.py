"""Read-only evidence for the SAM ruling review; no owner writes or market fetches."""
import collections
import csv
import hashlib
import importlib.util
import io
from pathlib import Path
import subprocess
import types

ROOT = Path(__file__).resolve().parents[3]
PIN = 'ed18776ae9528f836d5f7ce8906b07b296a8659b'
SAM = ROOT / 'AGENTS/SAM'


def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT, text=True)


def rows(text):
    return list(csv.DictReader(io.StringIO('\n'.join(
        line for line in text.splitlines() if line and not line.startswith('#'))), delimiter='\t'))


paths = [
    'CLAUDE.md', 'STATUS.md', 'MEMORY.md', 'NEXUS_BRIEF.md',
    'docket/2026-09-19_CATO-R4-RULING.md',
    'docket/2026-09-18_SAM28_SAM31_REVIEW.md',
    'thesis/PREDICTIONS.tsv', 'scripts/lib/boot_context.py',
    'scripts/closeout_check.py', 'scripts/tests/test_closeout_check.py',
]
print('Review pin:', PIN)
for rel in paths:
    live = (SAM / rel).read_bytes()
    pinned = subprocess.check_output(['git', 'show', f'{PIN}:AGENTS/SAM/{rel}'], cwd=ROOT)
    assert live == pinned, f'Source changed since review pin: {rel}'
    print('PIN MATCH', hashlib.sha256(live).hexdigest(), rel)

current = rows((SAM / 'thesis/PREDICTIONS.tsv').read_text())
old = {r['Pred_ID']: r for r in rows(git('show', '36f24db95^:AGENTS/SAM/thesis/PREDICTIONS.tsv'))}
print('Exact status counts:', dict(collections.Counter(r['Status'] for r in current)))
for row in current:
    changed = [key for key in row if row[key] != old[row['Pred_ID']][key]]
    if changed:
        print('Changed fields:', row['Pred_ID'], changed)
    for field in ('Prediction', 'Confidence', 'Timeframe', 'Date_Made'):
        assert row[field] == old[row['Pred_ID']][field]
print('All registered term fields unchanged.')

print('\nCURRENT OWNER TEST SUITE')
testpath = SAM / 'scripts/tests/test_closeout_check.py'
run = subprocess.run(['python3', '-B', str(testpath)], cwd=ROOT, text=True, capture_output=True)
print(run.stdout, run.stderr, 'exit:', run.returncode)
assert run.returncode == 0

spec = importlib.util.spec_from_file_location('sam_tests', testpath)
tests = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tests)
prior = types.ModuleType('pre_fix_closeout')
prior.__file__ = str(SAM / 'scripts/closeout_check.py')
exec(compile(git('show', '986b1039c^:AGENTS/SAM/scripts/closeout_check.py'), prior.__file__, 'exec'), prior.__dict__)
tests.cc = prior
print('\nTHREE NEW TESTS AGAINST PRE-FIX CODE')
for name in sorted(n for n in vars(tests) if n.startswith('test_QUAL_')):
    try:
        getattr(tests, name)()
    except AssertionError as exc:
        print('FAILS PRE-FIX AS EXPECTED:', name, str(exc))
    else:
        raise AssertionError('Unexpected pre-fix pass: ' + name)

print('\nCURRENT STRUCTURAL CHECK (delegation explicitly skipped)')
run = subprocess.run(['python3', '-B', str(SAM / 'scripts/closeout_check.py'), '--no-delegate'],
                     cwd=ROOT, text=True, capture_output=True)
for line in run.stdout.splitlines():
    if any(token in line for token in ('DERIVED from', 'CLOSEOUT-CHECK', 'This does NOT')):
        print(line)
print('exit:', run.returncode)
if run.stderr:
    print(run.stderr)
assert run.returncode == 0
derived = next(line for line in run.stdout.splitlines() if 'DERIVED from' in line)
assert 'qualified' not in derived.lower()
print('OUTPUT DEFECT REPRODUCED: qualified row exists but is absent from the derived summary.')

print('\nEARLIER OWNER EPISODE SCREEN (not primary-market certification)')
screen = list(csv.DictReader((SAM / 'research/outputs/2026-09-09_followthrough/episode-screen.csv').open()))
for row in sorted(screen, key=lambda r: float(r['vix_delta']), reverse=True)[:4]:
    print(row['date'], 'delta VIX', row['vix_delta'], 'FXY daily', row['fxy_vendor_daily_pct'])

print('\nNEXT TWO STORED DATED ITEMS')
for row in list(csv.DictReader((SAM / 'docket/CATALYSTS.tsv').open(), delimiter='\t'))[:2]:
    print(row['date'], row['event'])
