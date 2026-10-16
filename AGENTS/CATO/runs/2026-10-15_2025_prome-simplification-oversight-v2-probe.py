"""V2 design evidence: real perimeter witness and isolated fake-push handoff."""
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import types

repo = Path(__file__).resolve().parents[3]
pin = '31062bfc61b3376172775064ada60e3d0bbb024d'
real_git = shutil.which('git')
def git(root, *args):
    return subprocess.check_output([real_git, '-c', 'core.hooksPath=/dev/null', '-c', 'user.name=CATO fixture', '-c', 'user.email=cato-fixture@example.invalid', *args], cwd=root, stderr=subprocess.PIPE).decode().strip()
def source(path):
    return subprocess.check_output([real_git, 'show', f'{pin}:{path}'], cwd=repo).decode()
results = {'pin': pin, 'limit': 'No v2 implementation exists. Receipt interleaving is a design simulation; classifier and safe-push are pinned production code. Network/push operations are substituted.'}
with tempfile.TemporaryDirectory(prefix='cato-wq448-v2-') as tmp:
    root = Path(tmp)
    mod = types.ModuleType('argus_v2_evidence')
    mod.__file__ = str(repo/'PROME/tools/argus_scope.py')
    exec(compile(source('PROME/tools/argus_scope.py'), mod.__file__, 'exec'), mod.__dict__)
    perimeter = root/'AUDIT_PERIMETER.tsv'
    perimeter.write_text(source('PROME/state/AUDIT_PERIMETER.tsv'))
    rules = mod.load_perimeter(perimeter)
    witness = '46299b920dc188b71ce86d83b8b9b590dfa8012b'
    paths = git(repo, 'show', '--format=', '--name-only', witness).splitlines()
    classified = {p: mod.classify(p, rules)[0] for p in paths}
    assert set(classified.values()) == {'SHARED', 'EXCLUDED'}
    results['real_dewey_witness'] = {'commit': witness, 'classes': classified, 'v2_result': 'mixed => refusal, although this is DEWEY work; re-running does not change the classes'}

    sandbox = root/'sandbox'
    (sandbox/'scripts').mkdir(parents=True)
    git(sandbox, 'init', '-q', '-b', 'master')
    (sandbox/'example.md').write_text('base\n')
    git(sandbox, 'add', 'example.md')
    git(sandbox, 'commit', '-qm', 'fixture base')
    base = git(sandbox, 'rev-parse', 'HEAD')
    git(sandbox, 'update-ref', 'refs/remotes/origin/master', base)
    (sandbox/'example.md').write_text('checked\n')
    git(sandbox, 'commit', '-qam', 'fixture checked candidate')
    checked = git(sandbox, 'rev-parse', 'HEAD')
    # An edit after the relevant check, before an end-of-gate receipt snapshot.
    checked_hash = hashlib.sha256((sandbox/'example.md').read_bytes()).hexdigest()
    (sandbox/'example.md').write_text('not checked\n')
    end_hash = hashlib.sha256((sandbox/'example.md').read_bytes()).hexdigest()
    results['end_snapshot_interleaving'] = {'checked_hash': checked_hash, 'receipt_end_hash': end_hash, 'receipt_matches_later_bytes': end_hash == hashlib.sha256((sandbox/'example.md').read_bytes()).hexdigest(), 'matches_checked_bytes': checked_hash == end_hash}
    assert checked_hash != end_hash
    git(sandbox, 'commit', '-qam', 'fixture concurrent followup')
    advanced = git(sandbox, 'rev-parse', 'HEAD')
    (sandbox/'scripts/install-git-hooks.sh').write_text('#!/bin/sh\nexit 0\n')
    (sandbox/'scripts/safe-push.sh').write_text(source('scripts/safe-push.sh'))
    shimdir = root/'bin'
    shimdir.mkdir()
    shim = shimdir/'git'
    shim.write_text('#!/bin/sh\ncase "$1" in\n fetch) exit 0;;\n push) "$CATO_REAL_GIT" rev-parse HEAD > "$CATO_PUSH_LOG"; exit 1;;\n *) exec "$CATO_REAL_GIT" "$@";;\nesac\n')
    shim.chmod(0o700)
    log = root/'fake-push-tip.txt'
    env = dict(os.environ, PATH=str(shimdir)+os.pathsep+os.environ['PATH'], CATO_REAL_GIT=real_git, CATO_PUSH_LOG=str(log))
    run = subprocess.run(['bash', 'scripts/safe-push.sh'], cwd=sandbox, env=env, capture_output=True, text=True)
    observed = log.read_text().strip()
    assert observed == advanced and observed != checked
    results['handoff_after_validation'] = {'validated_tip': checked, 'later_tip': advanced, 'fake_push_received_tip': observed, 'safe_push_rc': run.returncode, 'real_push_executed': False}
print(json.dumps(results, indent=2))
