import contextlib, io, pathlib, subprocess, sys, tempfile, types
# Independent observations against current runner; all mutations are inside a temporary repo.
SOURCE = pathlib.Path(__file__).resolve().parents[3] / 'AGENTS/BOND/monitors/closeout_run.py'
m = types.ModuleType('bond_runner'); m.__file__ = str(SOURCE)
exec(compile(SOURCE.read_text(), str(SOURCE), 'exec'), m.__dict__)
original_sh, original_digest = m.sh, m.tree_digest

def capture(fn):
    out = io.StringIO()
    with contextlib.redirect_stdout(out): rc = fn()
    return rc, out.getvalue()

with tempfile.TemporaryDirectory(prefix='cato-bond-v2-') as folder:
    root = pathlib.Path(folder); bond = root / 'AGENTS/BOND'; (bond / 'registry').mkdir(parents=True)
    def git(*args):
        return subprocess.run(['git', *args], cwd=root, check=True, capture_output=True, text=True).stdout
    git('init', '-q'); git('config', 'user.email', 'fixture@example.invalid'); git('config', 'user.name', 'CATO fixture')
    for name in ['STATUS.md', 'NEXUS_BRIEF.md', 'TRADE.md', 'SCRATCH.md']:
        (bond / name).write_text('original\n')
    (bond / 'chart.bin').write_bytes(b'\x00original')
    git('add', 'AGENTS/BOND/STATUS.md', 'AGENTS/BOND/NEXUS_BRIEF.md', 'AGENTS/BOND/TRADE.md', 'AGENTS/BOND/SCRATCH.md', 'AGENTS/BOND/chart.bin')
    git('commit', '-qm', 'fixture baseline')
    m.REPO, m.BOND, m.LOG = root, bond, bond / 'registry/CLOSEOUT_LOG.tsv'
    def real_sh(cmd, cwd=None, timeout=600):
        return original_sh(cmd, cwd=root if cwd is None else cwd, timeout=timeout)
    m.sh = real_sh; m.tree_digest = lambda: original_digest(root)
    def changes(path, first, second):
        path.parent.mkdir(parents=True, exist_ok=True); path.write_bytes(first)
        before = m.tree_digest(); path.write_bytes(second)
        return m.tree_digest() != before
    print('untracked content edit detected:', changes(bond/'new.md',b'a',b'b'))
    print('outgoing convention packet edit detected:', changes(root/'PROME/inbox/2026-09-29_from-BOND_fixture.md',b'a',b'b'))
    print('tracked text edit detected:', changes(bond/'STATUS.md',b'a',b'b'))
    print('already modified tracked binary edit detected:', changes(bond/'chart.bin',b'\x00first',b'\x00second'))
    m.LOG.write_text('timestamp\ttier\thead\toverall\tsteps\tdigest\nfixture\tstandard\tHEAD\tFAILED\tfailing-step\t'+m.tree_digest()+'\n')
    print('verify after FAILED run rc:',capture(m.verify)[0])
    real_ordering=m.check_ordering
    (bond/'SCRATCH.md').write_text('new handoff\n')
    print('STATUS+SCRATCH changed, TRADE unchanged, brief declared no-op:',real_ordering({'NEXUS_BRIEF.md':'no consumed state changed'})[0])
    m.check_ordering = lambda noops: ('RAN','fixture ordering clean'); m.inbox_scan=lambda:'fixture empty inbox'
    self_output='''🔴 STALE ON A LIVE SURFACE — send the owner a packet (1)
        AGENTS/BOND/STATUS.md:42 [14/35]
           old figure still live
🔴 1 stale reference(s) on YOUR OWN surfaces. Fix them in place.
'''
    def mock_sh(cmd, cwd=None, timeout=600):
        if cmd[0]=='git': return real_sh(cmd,cwd,timeout)
        if 'scripts/consumer_check.py' in cmd:
            return (1,self_output) if '--self' in cmd else (0,'clean cross-agent')
        return 0,'fixture clean'
    m.sh=mock_sh
    sys.argv=['runner','--tier','standard','--superseded','14/35','15/35']
    rc,output=capture(m.main)
    print('unacknowledged self stale result rc:',rc)
    print('stale path visible in stdout or log:', 'AGENTS/BOND/STATUS.md:42' in output+m.LOG.read_text())
    sys.argv += ['--consumer-ack','PROME packeted']
    rc,output=capture(m.main)
    print('self still stale, cross-agent ack present, runner rc:',rc)
    print('ack note retained in log:', 'PROME packeted' in m.LOG.read_text())
    print('verify after acknowledged self-stale run rc:',capture(m.verify)[0])
    def mutate_sh(cmd,cwd=None,timeout=600):
        if cmd[0]=='git': return real_sh(cmd,cwd,timeout)
        if 'scripts/claim_check.py' in cmd: (bond/'STATUS.md').write_text('changed during checks\n')
        return 0,'fixture clean'
    m.sh=mutate_sh; sys.argv=['runner','--tier','standard']
    print('tracked mutation during run rc:',capture(m.main)[0])
    print('verify after mutation run rc:',capture(m.verify)[0])
    m.sh=lambda *a,**kw:(128,'fatal: fixture Git read failure')
    try: print('Git read failure produces digest instead of refusing:',isinstance(m.tree_digest(),str))
    except Exception as e: print('Git read failure refused:',type(e).__name__)
