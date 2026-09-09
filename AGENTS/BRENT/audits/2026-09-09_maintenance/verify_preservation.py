"""One-time maintenance evidence; supersedes none, not a new boot check."""
import ast
import csv
import hashlib
import io
import json
from pathlib import Path
import re
import subprocess
import zlib

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
BRENT = ROOT / 'AGENTS/BRENT'
BASE = '7b8461779'


def before(path):
    return subprocess.check_output(['git', 'show', f'{BASE}:AGENTS/BRENT/{path}'], cwd=ROOT)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def rows(raw):
    return list(csv.DictReader(io.StringIO('\n'.join(
        x for x in raw.decode().splitlines() if x and not x.startswith('#'))), delimiter='\t'))


report = {'base_commit': BASE, 'unchanged': {}, 'rotations': [], 'bytes': {}}
frozen = ['TRADE.md', 'thesis/PREDICTIONS.tsv', 'thesis/THESIS.md', 'thesis/CHANGELOG.md',
          'refinery_damage/INCIDENTS.tsv', 'board_log.tsv', 'docket/CATALYSTS.tsv',
          'LESSONS.md', 'workbook/LESSONS_INDEX.tsv', 'scripts/data/refiner_ratios.tsv',
          'workbook/KB.tsv', 'workbook/VX.tsv', 'workbook/FLOW.tsv']
frozen += [str(p.relative_to(BRENT)) for p in sorted((BRENT / 'setups').glob('SPECS_*.md'))]
for name in frozen:
    raw = (BRENT / name).read_bytes()
    assert raw == before(name), name
    report['unchanged'][name] = sha(raw)

old, new = rows(before('workbook/REGISTRY.tsv')), rows((BRENT / 'workbook/REGISTRY.tsv').read_bytes())
assert len(old) == len(new) == 49
changes = []
for x, y in zip(old, new):
    for key in x:
        if x[key] != y[key]:
            assert x['test_id'] == y['test_id'] == 'TANKER-LIVENESS'
            assert key in ('probe', 'probe_scope', 'consumer_scripts', 'notes'), key
            changes.append(key)
report['registry'] = {'rows': len(new), 'only_changed_row': 'TANKER-LIVENESS', 'fields': changes}

for entry in json.loads((HERE / 'rotation-manifest.json').read_text())['rotations']:
    dest = entry['destination'].split('#')[0]
    raw = (BRENT / dest).read_bytes()
    source = entry['source'].split(' ')[0]
    original = before(source)
    if dest.startswith('archive/'):
        assert raw in original, source
        assert sha(raw) == entry['sha256'], dest
        assert f'{zlib.crc32(raw):08x}' == entry['crc32'], dest
    else:
        # Rationale fragments are whole source lines, except the moved parenthesis.
        fragments = original.splitlines(keepends=True)
        fragments += [m.group().encode() + b'\n' for m in re.finditer(
            r'\*\(Corrected 2026-07-30:.*?\)\*', original.decode())]
        matched = [b for b in fragments if sha(b) == entry['sha256']]
        assert len(matched) == 1 and matched[0] in raw, entry['source']
    report['rotations'].append({'destination': dest, 'sha256': entry['sha256'], 'verified': True})

old = before('docket/FASTOW_MEMORY.md').decode()
new = (BRENT / 'docket/FASTOW_MEMORY.md').read_text()
assert old.split('\n## PENDING\n')[0] == new.split('\n## PENDING\n')[0]
assert old[old.index('\n## STANDING MONITORS'):old.index('\n## NEXT RUN HINTS\n')] in new
report['fastow_history_and_ownership_preserved'] = True

def executable(raw):
    tree = ast.parse(raw)
    tree.body = tree.body[1:]  # module docstring only was corrected
    return ast.dump(tree, include_attributes=False)

assert executable(before('scripts/cot_grade.py')) == executable((BRENT / 'scripts/cot_grade.py').read_bytes())
report['cot_executable_unchanged'] = True
for name in ['CLAUDE.md', 'STATUS.md', 'SCRATCH.md', 'NEXUS_BRIEF.md']:
    size = (BRENT / name).stat().st_size
    assert size < 32550, name
    report['bytes'][name] = {'before': len(before(name)), 'after': size, 'headroom': 32550 - size}

# Alert cells retain their own vintages; a maintenance annotation cannot refresh them.
def alerts(raw):
    return re.findall(r'^> \| (?:[1-9]|1[01]) \|.*$', raw.decode(), re.M)

assert len(alerts(before('demand_destruction/TRACKER.md'))) == 11
assert alerts(before('demand_destruction/TRACKER.md')) == alerts((BRENT / 'demand_destruction/TRACKER.md').read_bytes())
report['tracker_alert_rows_unchanged'] = 11
print(json.dumps(report, indent=2))
