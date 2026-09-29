import contextlib, io, pathlib, subprocess, sys, tempfile, types
# Observation probe; temporary Git repository and stubbed checks, no production writes.
SOURCE = pathlib.Path(__file__).resolve().parents[3] / 'AGENTS/BOND/monitors/closeout_run.py'
m = types.ModuleType('bond_runner'); m.__file__ = str(SOURCE)
exec(compile(SOURCE.read_text(), str(SOURCE), 'exec'), m.__dict__)
original_sh = m.sh

def capture(fn):
    out = io.StringIO()
    with contextlib.redirect_stdout(out):
        rc = fn()
    return rc, out.getvalue()

with tempfile.TemporaryDirectory(prefix='cato-bond-probe-') as folder:
    root = pathlib.Path(folder); bond = root / 'AGENTS/BOND'
    (bond / 'registry').mkdir(parents=True)
    def git(*args):
        return subprocess.run(['git', *args], cwd=root, check=True, capture_output=True, text=True).stdout
    git('init', '-q'); git('config', 'user.email', 'fixture@example.invalid'); git('config', 'user.name', 'CATO fixture')
    for name in ['STATUS.md', 'NEXUS_BRIEF.md', 'TRADE.md', 'SCRATCH.md']:
        (bond / name).write_text('original\n')
    git('add', 'AGENTS/BOND/STATUS.md', 'AGENTS/BOND/NEXUS_BRIEF.md', 'AGENTS/BOND/TRADE.md', 'AGENTS/BOND/SCRATCH.md')
    git('commit', '-qm', 'fixture baseline')
    m.REPO, m.BOND, m.LOG = root, bond, bond / 'registry/CLOSEOUT_LOG.tsv'
    def real_sh(cmd, cwd=None, timeout=600):
        return original_sh(cmd, cwd=root if cwd is None else cwd, timeout=timeout)
    m.sh = real_sh
    new = bond / 'new_note.md'; new.write_text('checked version\n')
    before = m.tree_digest(); new.write_text('different version\n')
    print('untracked-content edit detected:', m.tree_digest() != before)
    before = m.tree_digest(); (bond / 'STATUS.md').write_text('tracked change\n')
    print('tracked-content edit detected (positive control):', m.tree_digest() != before)
    packet = root / 'AGENTS/TERRY/inbox/from-BOND.md'; packet.parent.mkdir(parents=True); packet.write_text('packet v1\n')
    before = m.tree_digest(); packet.write_text('packet v2\n')
    print('outside-BOND packet edit detected:', m.tree_digest() != before)
    m.LOG.write_text('timestamp\ttier\thead\toverall\tsteps\tdigest\nfixture\tstandard\tHEAD\tFAILED\tfailing-step\t' + m.tree_digest() + '\n')
    rc, output = capture(m.verify)
    print('verify after FAILED run:', rc, output.strip())
    # Simulate root tool failures/results; all other checks return clean.
    m.check_ordering = lambda: ('RAN', 'fixture ordering clean')
    m.inbox_scan = lambda: 'fixture inbox empty'
    def mock_sh(cmd, cwd=None, timeout=600):
        if cmd[0] == 'git': return real_sh(cmd, cwd, timeout)
        if 'scripts/orphan_check.sh' in cmd: return 127, 'ORPHAN_COMMAND_FAILED'
        if 'scripts/ledger_staleness.py' in cmd: return 1, 'LEDGER_TRACEBACK'
        if 'scripts/consumer_check.py' in cmd: return 0, 'STALE_FIXTURE AGENTS/OTHER/STATUS.md:42'
        return 0, 'fixture clean'
    m.sh = mock_sh; sys.argv = ['runner', '--tier', 'standard', '--superseded', 'OLD', 'NEW']
    rc, output = capture(m.main)
    print('runner with orphan rc127 + ledger rc1 overall:', rc)
    print('consumer stale path visible:', 'STALE_FIXTURE' in output)
    print('orphan failure detail visible:', 'ORPHAN_COMMAND_FAILED' in output)
    print('log preserves consumer path:', 'STALE_FIXTURE' in m.LOG.read_text())
    for line in output.splitlines():
        if 'root 1b ' in line or 'root 1c-bis ' in line: print(line.strip())
    # Mutation after content checker but before digest is recorded.
    def mutate_sh(cmd, cwd=None, timeout=600):
        if cmd[0] == 'git': return real_sh(cmd, cwd, timeout)
        if 'scripts/claim_check.py' in cmd: (bond / 'STATUS.md').write_text('changed after content checks\n')
        return 0, 'fixture clean'
    m.sh = mutate_sh; sys.argv = ['runner', '--tier', 'standard']
    rc, _ = capture(m.main); verify_rc, verify_output = capture(m.verify)
    print('mutation during run: run rc / verify rc:', rc, verify_rc)
    print(verify_output.strip())
    # Actual git-backed ordering: STATUS is dirty but unchanged TRADE is valid.
    m.sh = real_sh
    print('dirty STATUS vs unchanged TRADE ordering:', m.vintage('TRADE.md') < m.vintage('STATUS.md'))
