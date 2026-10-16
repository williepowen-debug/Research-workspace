"""Independent bounded checks of b9d9ffc61; creates an isolated checkout.

The WQ-448 case models proposal D1, not an implemented gate.
Usage: python3 -B <this-script> --repo /path/to/Research-workspace
All test writes go to a new /tmp directory, printed with the results.
"""
import argparse
import datetime as dt
import hashlib
import importlib.util
import json
import subprocess
import sys
import tempfile
from pathlib import Path

ap = argparse.ArgumentParser()
ap.add_argument('--repo', type=Path, required=True)
args = ap.parse_args()
PIN = 'b9d9ffc61e84aecc6165e4412c69d41fb917b650'
ROOT = Path(tempfile.mkdtemp(prefix='cato-commits-proof-', dir='/tmp'))
for name in ('PROME/tools/decision_deck.py', 'PROME/tools/prome_gate.py',
             'PROME/tools/tests/test_deck_owed_digest_L738.py',
             'scripts/docket_view.py', 'PROME/DOCKET.tsv', 'PROME/SCRATCH.md'):
    dest = ROOT / name
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(subprocess.check_output(['git', '-C', str(args.repo), 'show', PIN + ':' + name]))
(ROOT / 'scripts/docket_view_old.py').write_bytes(subprocess.check_output(
    ['git', '-C', str(args.repo), 'show', '8ac3461de:scripts/docket_view.py']))
(ROOT / 'PROME/WILL_QUEUE.md').write_text('## OPEN\n')
subprocess.run(['git', 'init', '-q', str(ROOT)], check=True)
sys.path.insert(0, str(ROOT / 'PROME/tools/tests'))
import test_deck_owed_digest_L738 as F


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def cli_cases():
    fixture = F.OwedDigest()
    fixture.setUp()
    try:
        fixture.hosted_build()
        default = ROOT / 'PROME/artifacts/decision_deck.html'
        default.parent.mkdir(parents=True, exist_ok=True)
        default.write_bytes(fixture.out.read_bytes())
        downloaded = ROOT / 'downloaded-A.html'
        downloaded.write_bytes(default.read_bytes())
        alias = ROOT / 'local-render-alias.html'
        if not alias.exists():
            alias.symlink_to(default)
        state = ROOT / 'PROME/state/deck_owed_hosted.json'
        state.parent.mkdir(parents=True, exist_ok=True)
        state.write_text('{"sentinel":"previous publication"}\n')
        prior = state.read_bytes()
        script = ROOT / 'PROME/tools/decision_deck.py'
        def run(args):
            return subprocess.run([sys.executable, '-B', str(script),
                                   '--record-hosted-owed', 'v-test', *args],
                                  cwd=ROOT, text=True, capture_output=True)
        results = []
        for name, args in [
            ('omitted page', []),
            ('default local render', ['--page', str(default)]),
            ('symlink to local render', ['--page', str(alias)]),
            ('explicit custom output equals page', ['-o', str(downloaded), '--page', str(downloaded)]),
            ('missing page', ['--page', str(ROOT / 'absent.html')]),
        ]:
            r = run(args)
            assert r.returncode == 2 and state.read_bytes() == prior, (name, r.stdout, r.stderr)
            results.append({'case': name, 'rc': r.returncode, 'record_preserved': True})
        r = run(['--page', str(downloaded)])
        assert r.returncode == 0, (r.stdout, r.stderr)
        rec = json.loads(state.read_text())
        assert rec['fingerprints'] == F.D.page_receipt(downloaded)['fingerprints']
        assert rec['page_sha256'] == hashlib.sha256(downloaded.read_bytes()).hexdigest()
        results.append({'case': 'separate downloaded-copy fixture', 'rc': 0,
                        'page_receipt_and_hash_match': True})
        return results
    finally:
        fixture.doCleanups()


def docket_cases():
    old = load('old_docket', ROOT / 'scripts/docket_view_old.py')
    new = load('new_docket', ROOT / 'scripts/docket_view.py')
    day = dt.date(2026, 10, 16)
    rows = new.load_docket(ROOT / 'PROME/DOCKET.tsv')
    before = old.render(rows, day)
    after = new.render(rows, day)
    def line(text, prefix):
        return next(x for x in text.splitlines() if x.startswith(prefix))
    checks = {}
    for prefix in ('**⚠️ OVERDUE', '**UNDATED', '*Beyond'):
        checks[prefix] = line(before, prefix) == line(after, prefix)
    checks['counts'] = line(before, '*GENERATED').split('Rows cited')[0] == line(after, '*GENERATED').split('Rows cited')[0]
    forward_old = next(x for x in before.splitlines() if x.startswith('**FRI 10/16:**'))
    forward_new = next(x for x in after.splitlines() if x.startswith('**FRI 10/16:**'))
    # The final detailed day is 10/23. All daily groups preceding 10/24 must be identical.
    checks['whole_near_window'] = forward_old.split(' — **10/24:**')[0] == forward_new.split(' — **10/24:**')[0]
    scratch = (ROOT / 'PROME/SCRATCH.md').read_text()
    saved = scratch[scratch.index(new.BEGIN):scratch.index(new.END)+len(new.END)]
    checks['committed_generated_block_matches'] = saved.strip() == after.strip()
    assert all(checks.values()), checks
    (ROOT / 'docket-before.txt').write_text(before)
    (ROOT / 'docket-after.txt').write_text(after)
    return checks


def proposal_d1_trace():
    # D1's specified S0/S1 rule can certify X despite only checking Y.
    p = ROOT / 'proposal-input.txt'
    p.write_text('INVALID X\n')
    def snap():
        return {'proposal-input.txt': hashlib.sha256(p.read_bytes()).hexdigest()}
    s0 = snap()
    p.write_text('VALID Y\n')
    checked_bytes = p.read_text()
    passed = checked_bytes == 'VALID Y\n'
    p.write_text('INVALID X\n')
    s1 = snap()
    receipt_issued = passed and s0 == s1
    committed_bytes_pass = p.read_text() == 'VALID Y\n'
    assert receipt_issued and not committed_bytes_pass
    return {'kind': 'proposal model, no gate implementation', 'S0_equals_S1': s0 == s1,
            'check_passed_on_Y': passed, 'receipt_issued_for_X': receipt_issued,
            'X_would_fail_check': not committed_bytes_pass}


results = {'pin': PIN, 'isolated_directory': str(ROOT),
           'cli': cli_cases(), 'docket': docket_cases(), 'WQ448_D1': proposal_d1_trace()}
(ROOT / 'review-probe-results.json').write_text(json.dumps(results, indent=2) + '\n')
print(json.dumps(results, indent=2))
