"""Read-only production-code probes; all Git mutations stay in temporary repos."""
import contextlib
import hashlib
import io
import json
import os
from pathlib import Path
import subprocess
import tempfile
import types

repo = Path(__file__).resolve().parents[3]
pin = '3880d83ed56ddf830bef7dcbb77de945846701b4'
sources = {name: subprocess.check_output(['git', 'show', f'{pin}:PROME/tools/{name}.py'], cwd=repo).decode() for name in ('commit_check', 'argus_scope')}

def git(root, *args):
    return subprocess.check_output(['git', '-c', 'core.hooksPath=/dev/null', '-c', 'user.name=CATO fixture', '-c', 'user.email=cato-fixture@example.invalid', *args], cwd=root, stderr=subprocess.PIPE).decode().strip()

def make_case(root):
    root.mkdir()
    git(root, 'init', '-q')
    (root/'PROME/state').mkdir(parents=True)
    (root/'PROME/example.md').write_text('original\n')
    git(root, 'add', 'PROME/example.md')
    git(root, 'commit', '-qm', 'fixture base')
    base = git(root, 'rev-parse', 'HEAD')
    os.chdir(root)
    modules = {}
    for name, source in sources.items():
        mod = types.ModuleType(name)
        mod.__file__ = str(repo/'PROME/tools'/f'{name}.py')
        exec(compile(source, mod.__file__, 'exec'), mod.__dict__)
        mod.ROOT = root
        modules[name] = mod
    modules['commit_check'].MANIFEST = root/'.git/prome_commit_intent.txt'
    (root/'PROME/state/argus_baseline.json').write_text(json.dumps({'sha': base}))
    (root/'PROME/state/argus_review.json').write_text(json.dumps({'baseline': base, 'verdict': 'REVIEWED', 'paths': {'PROME/example.md': hashlib.sha256(b'checked\n').hexdigest()}}))
    return base, modules['commit_check'], modules['argus_scope']

def intent_rc(cc):
    cc.MANIFEST.write_text('PROME/example.md\n')
    with contextlib.redirect_stdout(io.StringIO()):
        return cc.verify('HEAD', False)

results = {'pin': pin, 'scope': 'Current verifier functions only; proposed push command does not exist; no real gate or push run.'}
with tempfile.TemporaryDirectory(prefix='cato-wq448-') as tmp:
    try:
        root = Path(tmp)/'changed-content'
        base, cc, argus = make_case(root)
        # Simulate a successful receipt for the pre-edit state at base.
        receipt = {'tier': 'light', 'rc': 0, 'head': base, 'errored': []}
        (root/'PROME/example.md').write_text('later-unchecked\n')
        git(root, 'add', 'PROME/example.md')
        git(root, 'commit', '-qm', 'fixture later content')
        review_rc, lines = argus.verify_review(paths=['PROME/example.md'], ref='HEAD')
        results['changed_after_gate'] = {'receipt_base_matches': receipt['head'] == base, 'intent_rc': intent_rc(cc), 'review_rc': review_rc, 'review_lines': lines}
        assert results['changed_after_gate']['intent_rc'] == 0 and review_rc == 1

        root = Path(tmp)/'two-commits'
        base, cc, argus = make_case(root)
        (root/'PROME/unreviewed.md').write_text('never in review\n')
        git(root, 'add', 'PROME/unreviewed.md')
        git(root, 'commit', '-qm', 'fixture unreviewed earlier file')
        (root/'PROME/example.md').write_text('checked\n')
        git(root, 'add', 'PROME/example.md')
        git(root, 'commit', '-qm', 'fixture reviewed last file')
        head_paths = sorted(cc.commit_paths('HEAD'))
        range_paths = git(root, 'diff', '--name-only', f'{base}..HEAD').splitlines()
        head_rc, head_lines = argus.verify_review(paths=head_paths, ref='HEAD')
        range_rc, range_lines = argus.verify_review(paths=range_paths, ref='HEAD')
        results['earlier_unreviewed_file'] = {'intent_rc': intent_rc(cc), 'head_paths': head_paths, 'range_paths': range_paths, 'head_review_rc': head_rc, 'complete_range_review_rc': range_rc, 'complete_range_review_lines': range_lines}
        assert results['earlier_unreviewed_file']['intent_rc'] == 0 and head_rc == 0 and range_rc == 1
    finally:
        os.chdir(repo)
print(json.dumps(results, indent=2))
