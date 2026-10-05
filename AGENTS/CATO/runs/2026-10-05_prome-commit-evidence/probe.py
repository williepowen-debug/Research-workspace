"""Review reproduction: python3 -B probe.py /path/to/export/of/a441d4fa8."""
import sys, json, pathlib, tempfile, importlib.util, shutil
from unittest.mock import patch
ROOT = pathlib.Path(sys.argv[1]).resolve()
sys.path.insert(0, str(ROOT / 'PROME/tools'))
sys.path.insert(0, str(ROOT / 'PROME/tools/tests'))
import test_docket_row_cap as fixture
import boot_read
import prome_gate as gate

results = {}
for case in ('unset_unstaged', 'raised_unstaged', 'normal'):
    t = fixture.Repo('test_worktree_clean_and_flagged')
    t.setUp()
    try:
        config = t.repo / 'scripts/harness_caps.env'
        if case == 'unset_unstaged':
            config.write_text('# temporarily editing settings\n')
        elif case == 'raised_unstaged':
            config.write_text('DOCKET_ROW_CAP_BYTES=10000\n')
        t.docket.write_text(t.docket.read_text() + fixture.row(3, fixture.D + 50))
        p = t.git('commit', '-q', 'PROME/DOCKET.tsv', '-m', 'isolated cap probe', check=False)
        results[case] = {'commit_rc': p.returncode, 'stderr': p.stderr,
                         'committed_policy': t.git('show', 'HEAD:scripts/harness_caps.env').stdout,
                         'status': t.git('status', '--short').stdout}
    finally:
        t.doCleanups()

source = ROOT / 'AGENTS/CATO/runs/2026-10-04_prome-boot-evidence/orchestration-original.txt'
original = source.read_text()
compact, groups = boot_read.compact_orch(original)
lines = []
grouped = False
identities = 0
for line in compact.splitlines(keepends=True):
    if line == f'UNKNOWN (each entry): {boot_read.GAP_REASON}\n':
        grouped = True
        continue
    if grouped and line.startswith('  '):
        lines.append('UNKNOWN: ' + line[2:].rstrip('\n') + ': ' + boot_read.GAP_REASON + '\n')
        identities += 1
    else:
        grouped = False
        lines.append(line)
offset, sha, pages = 0, None, 0
while True:
    p = boot_read.page(source, offset, sha, boot_read.ORCH_VIEW)
    pages += 1
    if p['eof']: break
    offset, sha = p['next_offset'], p['sha256']
results['boot_replay'] = {'groups': groups, 'grouped_identities': identities,
                          'roundtrip_exact': ''.join(lines) == original, 'pages': pages}

spec = importlib.util.spec_from_file_location('firetime', ROOT / 'scripts/firetime_check.py')
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
results['artifact_parser'] = {s: m.split_artifact_cell(s) for s in (
    '.claude/agents/argus.md + .claude/agents/coldreader.md',
    'PROME/tools/prome_gate.py:312 (fired-unexecuted)',
    'PROME/DOCKET.tsv+PROME/GATES.tsv',
    '`PROME/a_handles+drift.md` · `AGENTS/BOND/STATUS.md`')}
t = fixture.Repo('test_worktree_clean_and_flagged')
t.setUp()
try:
    for name in ('memory_index_check.py', 'memory_index_paths.py', 'check_memory_length.sh', 'harness_caps.env'):
        shutil.copy2(ROOT / 'scripts' / name, t.repo / 'scripts' / name)
    mem = t.repo / 'memory/auto'
    mem.mkdir(parents=True)
    (mem / 'MEMORY.md').write_text('# Memory index\n')
    (mem / 'finding_cato_probe.md').write_text('# Untracked unindexed memory\n')
    gate.results.clear()
    with tempfile.TemporaryDirectory() as logs, patch.object(gate, 'ROOT', t.repo), patch.object(gate, 'LOG_DIR', pathlib.Path(logs)):
        gate.check_memory_declared(['finding_cato_probe'])
        results['untracked_unindexed_memory'] = {
            'aggregate_rc': gate.aggregate_rc(gate.results, []),
            'rows': gate.results,
            'checker_output': '\n'.join(p.read_text() for p in pathlib.Path(logs).glob('*memory-index*')),
            'tracked_memory': t.git('ls-files', 'memory/auto').stdout}
finally:
    t.doCleanups()
print(json.dumps(results, indent=2, ensure_ascii=False))
