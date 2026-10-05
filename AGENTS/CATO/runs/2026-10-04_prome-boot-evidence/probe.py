"""Replay the reviewed presentation without booting or altering operational state."""
from collections import Counter
import hashlib
import json
from pathlib import Path
import subprocess
import tempfile
import types

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
PIN = '5f7233fb7c5c1473d232ded65c1320affd3d06ea'
source = subprocess.check_output(
    ['git', 'show', PIN + ':PROME/tools/boot_read.py'], cwd=ROOT, text=True)
reader = types.ModuleType('reviewed_boot_reader')
exec(compile(source, 'reviewed_boot_reader', 'exec'), reader.__dict__)
path = HERE / 'orchestration-original.txt'
original = path.read_text()
compact, groups = reader.compact_orch(original)
gaps = [line for line in original.splitlines(keepends=True)
        if line.endswith(': ' + reader.GAP_REASON + '\n')]
matches = [line for line in gaps if reader.GAP_ROW.fullmatch(line)]
page_counts = {}
for view in ['full', reader.ORCH_VIEW]:
    offset, digest, parts = 0, None, []
    while True:
        page = reader.page(path, offset, digest, view)
        parts.append(page['text'])
        if page['eof']:
            break
        offset, digest = page['next_offset'], page['sha256']
    assert ''.join(parts) == (original if view == 'full' else compact)
    page_counts[view] = len(parts)

header = original.splitlines(keepends=True)[0]
fixtures = {}
for desk in ['VIOLET', "VIOLET (Will's session, directed)"]:
    identities = [f'2026-10-03 {desk} touch {i}-DOORBELL [' +
                  hashlib.sha256(str(i).encode()).hexdigest() + ']'
                  for i in [1, 2]]
    body = header + ''.join('UNKNOWN: ' + identity + ': ' + reader.GAP_REASON + '\n'
                            for identity in identities)
    rendered, grouped = reader.compact_orch(body)
    fixtures[desk] = {'groups': grouped,
                      'all_identities_preserved': all(x in rendered for x in identities)}
assert fixtures['VIOLET']['groups'] == 1
assert fixtures["VIOLET (Will's session, directed)"]['groups'] == 0
with tempfile.TemporaryDirectory(prefix='cato-prome-boot-measure-') as tmp:
    rendered_path = Path(tmp) / 'compact.txt'
    rendered_path.write_text(compact)
    measures = json.loads(subprocess.check_output(
        ['python3', 'PROME/tools/measure.py', '--json', str(path), str(rendered_path)],
        cwd=ROOT, text=True))
    for item, label in zip(measures, ['original', 'compact']):
        item['path'] = label
result = {'pinned_reader': PIN, 'groups': groups, 'repeated_gap_rows': len(gaps),
          'regex_matches': len(matches), 'not_matched': len(gaps)-len(matches),
          'dates': dict(sorted(Counter(x.split()[1] for x in gaps).items())),
          'pages': page_counts, 'measures': measures, 'fixture_results': fixtures,
          'meaning': 'Presentation-cost limitation; data preserved. No live boot or receipt repair.'}
print(json.dumps(result, indent=2))
