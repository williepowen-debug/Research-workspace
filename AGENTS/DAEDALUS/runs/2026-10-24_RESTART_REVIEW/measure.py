"""Read-only source measurement and disposable-repository closeout reproduction.

No fleet file is imported live or mutated. Git fixture commits stay under /tmp.
Usage: python3 -B measure.py REPO_ROOT OUTPUT_DIRECTORY [SOURCE_COMMIT]
"""
import hashlib
import importlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
from datetime import datetime, timezone

repo, output = map(Path, sys.argv[1:3])
output.mkdir(parents=True, exist_ok=True)

def git(root, *args):
    return subprocess.check_output(['git', *args], cwd=root)

head = git(repo, 'rev-parse', sys.argv[3] if len(sys.argv) > 3 else 'HEAD').decode().strip()

def blob(path):
    return git(repo, 'show', f'{head}:{path}')

common = ['CLAUDE.md', 'AGENTS.md', 'USER.md']
sets = {
    'DEWEY_boot_before_question': common + ['AGENTS/DEWEY/CLAUDE.md', 'AGENTS/DEWEY/CONTEXT.md'],
    'HANS_core_plus_status': common + ['AGENTS/HANS/CLAUDE.md', 'AGENTS/HANS/STATUS.md'],
    'OTTO_full_named_prose': common + [f'AGENTS/OTTO/{p}' for p in ['CLAUDE.md', 'STATUS.md', 'LAST_COMPLETION.md', 'MEMORY.md', 'LESSONS.md']],
    'OTTO_specific_task_named_prose': common + ['AGENTS/OTTO/CLAUDE.md', 'AGENTS/OTTO/STATUS.md'],
    'DAEDALUS_every_boot_named_prose': common + [f'AGENTS/DAEDALUS/{p}' for p in ['CLAUDE.md', 'OPERATIONS.md', 'STATUS.md', 'FLEET_DIRECTORY.md', 'PATTERNS_HOT.md']],
}
rows = {p: {'bytes': len(blob(p)), 'sha256': hashlib.sha256(blob(p)).hexdigest()} for p in sorted(set(sum(sets.values(), [])))}
measures = {k: {'paths': v, 'bytes': sum(rows[p]['bytes'] for p in v)} for k, v in sets.items()}
result = {'as_of': datetime.now(timezone.utc).isoformat(), 'head': head, 'method': 'UTF-8 Git blob byte sizes; named prose only, not full boot cost, actual tokens, runtime or avoidable waste. Excludes runtime-spec reads, conditional sources, inboxes and tool outputs.', 'files': rows, 'named_read_sets': measures, 'fixtures': []}
result['tool_source_hashes'] = {p: hashlib.sha256(blob(p)).hexdigest() for p in ['PROME/tools/argus_scope.py', 'PROME/tools/argus_contract.py', 'PROME/state/AUDIT_PERIMETER.tsv', '.gitignore']}

with tempfile.TemporaryDirectory(prefix='daedalus-restart-review-') as tmp:
    base = Path(tmp)
    modules = base/'modules'
    modules.mkdir()
    for name in ['argus_scope', 'argus_contract']:
        data = blob(f'PROME/tools/{name}.py')
        (modules/f'{name}.py').write_bytes(data)
    sys.path.insert(0, str(modules))
    sc = importlib.import_module('argus_scope')
    ac = importlib.import_module('argus_contract')
    for case in ['clean', 'foreign_pending', 'owned_pending', 'unreviewed_commit']:
        root = base/case
        root.mkdir()
        def write(path, data):
            p = root/path
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_bytes(data)
        def commit(subject, *paths):
            git(root, 'add', '--', *paths)
            git(root, 'commit', '-qm', subject, '--', *paths)
            return git(root, 'rev-parse', 'HEAD').decode().strip()
        git(root, 'init', '-q', '-b', 'master')
        git(root, 'config', 'user.name', 'DAEDALUS isolated fixture')
        git(root, 'config', 'user.email', 'fixture@example.invalid')
        git(root, 'config', 'commit.gpgsign', 'false')
        for p in ['PROME/state/AUDIT_PERIMETER.tsv', '.gitignore']:
            write(p, blob(p))
        initial = commit('fixture baseline', 'PROME/state/AUDIT_PERIMETER.tsv', '.gitignore')
        sc.ROOT = root
        sc.record_baseline(initial)
        write('PROME/result.md', b'reviewed delivery\n')
        ac.freeze(sc, {'delivered': {'PROME/result.md': 'bounded reviewed artifact'}, 'evidence': [], 'observed': {}})
        mark = sc.mark_reviewed('isolated reproduction; not a fleet review')
        if case == 'foreign_pending':
            write('AGENTS/REGINALD/unrelated.md', b'other desk work\n')
        elif case == 'owned_pending':
            write('PROME/unreviewed.md', b'new owner work\n')
        before = sc.verify_review()
        paths = ['PROME/result.md']
        if case == 'unreviewed_commit':
            write('PROME/unreviewed.md', b'new owner work\n')
            paths.append('PROME/unreviewed.md')
        target = commit('PROME: fixture delivery', *paths)
        after = sc.verify_review(ref=target, paths=paths)
        expected = {'clean': (0, 0), 'foreign_pending': (0, 1), 'owned_pending': (1, 1), 'unreviewed_commit': (0, 1)}[case]
        assert (before[0], after[0]) == expected, (case, before, after)
        if case == 'foreign_pending':
            assert any('UNCLASSIFIED: AGENTS/REGINALD/unrelated.md' in line for line in after[1])
        if case == 'unreviewed_commit':
            assert any('UNREVIEWED ACTUAL COMMIT PATH: PROME/unreviewed.md' in line for line in after[1])
        result['fixtures'].append({'case': case, 'mark_reviewed': mark, 'working_tree_verify': before, 'delivery_verify': after})

(output/'measurements.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps({'head': head, 'named_read_bytes': {k:v['bytes'] for k,v in measures.items()}, 'fixtures': result['fixtures']}, indent=2))
