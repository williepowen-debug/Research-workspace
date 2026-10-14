"""One-off preservation checks for the approved October14 maintenance; no live grades."""
from pathlib import Path
import csv
import hashlib
import io
import json
import re
import subprocess
import zlib

HERE = Path(__file__).resolve().parent
DESK = HERE.parents[1]
ROOT = DESK.parents[1]
ARCHIVE = DESK / 'archive/2026-10-14_operational-followups'
checks = {}

def check(name, condition, detail):
    checks[name] = {'pass': bool(condition), 'detail': detail}

def sha(body):
    return hashlib.sha256(body).hexdigest()

manifest = json.loads((ARCHIVE / 'manifest.json').read_text())
for name, record in manifest['files'].items():
    body = (DESK / record['before_image']).read_bytes()
    check('archive:' + name, len(body) == record['bytes'] and sha(body) == record['sha256']
          and f'{zlib.crc32(body):08x}' == record['crc32'], record)
for record in manifest['rotated_blocks']:
    original = (DESK / manifest['files'][record['file']]['before_image']).read_bytes()
    block = original[record['original_start_utf8']:][:record['bytes']]
    check('rotated:' + record['name'], sha(block) == record['sha256'], record)

def records(body):
    return list(csv.DictReader(io.StringIO(''.join(line for line in body.splitlines(True)
                                                if not line.startswith('#'))), delimiter='\t'))

before_registry = (ARCHIVE / 'REGISTRY.tsv').read_bytes()
after_registry = (DESK / 'workbook/REGISTRY.tsv').read_bytes()
noncomments = lambda body: b''.join(line for line in body.splitlines(True) if not line.startswith(b'#'))
check('registry_rows_unchanged', noncomments(before_registry) == noncomments(after_registry),
      'Byte comparison of all non-comment rows; no numerical/status/date/probe change.')
before = records((ARCHIVE / 'INCIDENTS.tsv').read_text())
after = records((DESK / 'refinery_damage/INCIDENTS.tsv').read_text())
changed = [a['id'] for a, b in zip(after, before) if a != b]
preserved = len(before) == len(after) and all(
    {k: v for k, v in a.items() if k != 'notes'} == {k: v for k, v in b.items() if k != 'notes'}
    for a, b in zip(after, before))
check('incident_identity_and_fields', preserved, {'rows': len(after), 'notes_changed': changed})
check('incident_scope_six', {re.sub(r'[^0-9]', '', x).lstrip('0') for x in changed}
      == {'8', '16', '18', '22', '39', '44'}, changed)

original = (ARCHIVE / 'TRACKER.md').read_bytes()
live = (DESK / 'demand_destruction/TRACKER.md').read_text()
retained = json.loads((HERE / 'tracker-retained-blocks.json').read_text())
for record in retained['retained_exact_slices']:
    block = original[record['start_utf8']:][:record['bytes']]
    unchanged = sha(block) == record['sha256']
    expected = block.decode()
    for replacement in [retained['changed_live_line']] + retained['reader_annotations']:
        expected = expected.replace(replacement['before'], replacement['after'])
    check('tracker_slice:' + record['name'], unchanged and expected in live, record)
for i in range(1, 12):
    old = next(x for x in original.decode().splitlines() if x.startswith(f'> | {i} |'))
    new = next(x for x in live.splitlines() if x.startswith(f'> | {i} |'))
    check(f'alert_line_{i}', new == (retained['changed_live_line']['after'] if i == 4 else old),
          'Only line4 observation changes; thresholds preserved.')
for name in ['HOARDING.md', 'MATRIX_REVIEW.md', 'TRANSITION_MATRIX.md']:
    check('historical_body:' + name,
          (DESK / 'demand_destruction' / name).read_bytes().endswith((ARCHIVE / name).read_bytes()),
          'Historical original is an unchanged byte suffix behind a new scope banner.')
old_fastow = (ARCHIVE / 'FASTOW_MEMORY.md').read_text()
new_fastow = (DESK / 'docket/FASTOW_MEMORY.md').read_text()
def pending_to_hints(text):
    return text[text.index('\n## PENDING\n'):text.index('\n## NEXT RUN HINTS\n')]
check('fastow_pending_standing_calibration_preserved', pending_to_hints(old_fastow) == pending_to_hints(new_fastow),
      'Exact comparison at anchored headings; entire PENDING/STANDING MONITORS/CALIBRATION block.')

receipts = json.loads((HERE / 'source-receipts.json').read_text())
for record in receipts + json.loads((HERE / 'public-source-receipts.json').read_text()):
    if 'stored_sha256' in record:
        suffix = '.json' if record['name'].startswith('util-') else '.txt'
        body = (HERE / (record['name'] + suffix)).read_bytes()
        check('stored_source:' + record['name'], sha(body) == record['stored_sha256']
              and len(body) == record['stored_bytes'], 'Stored-body hash, distinct from any redacted raw-body hash.')
util = json.loads((HERE / 'util-current-series.json').read_text())['response']['data'][0]
check('utilization_identity_and_vintage', all(util.get(k) == v for k, v in {
    'series': 'WPULEUS3', 'duoarea': 'NUS', 'process': 'YUP', 'units': '%',
    'period': '2026-10-02', 'value': '92.7'}.items()), util)
check('cftc_access_gap_retained', len([r for r in receipts if r['name'].startswith('cftc-')
                                    and r.get('http_status') == 403]) == 2, 'Two primary paths returned403; no current reissue check.')
for record in json.loads((HERE / 'routine-review.json').read_text())['saved_prompts']:
    check('saved_prompt:' + record['path'], sha((DESK / record['path']).read_bytes()) == record['sha256'],
          'Saved prompt only; not a live deployment receipt.')

hot = ['STATUS.md', 'SCRATCH.md', 'TRADE.md', 'thesis/THESIS.md',
       'demand_destruction/TRACKER.md', 'docket/FASTOW_MEMORY.md', 'NEXUS_BRIEF.md']
for name in hot:
    count = len((DESK / name).read_bytes())
    check('rotation_stop:' + name, count < 22785, {'bytes': count, 'strict_stop': 22785})
packet = 'SIG-W-20261014-014'
rows = records((DESK / 'board_log.tsv').read_text())
check('walter_intake_reconciled', sum(r.get('signal_id') == packet for r in rows) == 1
      and (DESK / f'inbox/WALTER/processed/{packet}.md').exists()
      and not (DESK / f'inbox/WALTER/{packet}.md').exists(), 'One logged row and one archived packet.')
frozen = ['workbook/KB.tsv', 'workbook/VX.tsv', 'workbook/FLOW.tsv', 'thesis/TIMELINE.md', 'GROUP_MAP.md']
dirty = subprocess.check_output(['git', 'diff', '--name-only', 'HEAD', '--', 'AGENTS/BRENT'], cwd=ROOT, text=True).splitlines()
check('frozen_untouched', not set('AGENTS/BRENT/' + p for p in frozen).intersection(dirty), frozen)

link_files = [DESK / p.removeprefix('AGENTS/BRENT/') for p in dirty if p.endswith('.md')
              and '/inbox/' not in p]
link_files += list(HERE.glob('*.md'))
missing = []
count = 0
for path in link_files:
    text = path.read_text()
    if path.name in ['HOARDING.md', 'MATRIX_REVIEW.md', 'TRANSITION_MATRIX.md']:
        text = text[:-len((ARCHIVE / path.name).read_text())]
    for target in re.findall(r'\]\(([^)]+)\)', text):
        target = target.strip('<>').split('#', 1)[0]
        if not target or '://' in target or target.startswith(('mailto:', 'app:')):
            continue
        count += 1
        if not (path.parent / target).exists() and not (path.parent / target).resolve() == HERE / 'validation.json':
            missing.append({'file': str(path.relative_to(DESK)), 'target': target})
check('local_markdown_links', not missing, {'checked': count, 'missing': missing,
      'scope': 'Changed live Markdown and audit reports; historical bodies/intake packet excluded.'})
result = {'scope': 'One-off preservation validation; supersedes:none. No live market, broker, remote scheduler or facility certification.',
          'all_pass': all(x['pass'] for x in checks.values()), 'checks': checks}
(HERE / 'validation.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps({'all_pass': result['all_pass'], 'checks': len(checks),
                  'failures': {k: v for k, v in checks.items() if not v['pass']}}, indent=2))
raise SystemExit(0 if result['all_pass'] else 1)
