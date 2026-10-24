import sys, subprocess
sys.argv = [sys.argv[0], 'zz-none']
exec(open(__file__.replace('ce3b.py', 'ce3.py')).read())
def c4_bound(fx):
    fx.freeze()
    fx.write('.claude/agents/newdef.md', 'PROME new agent def, unreviewed\n')
    fx.write('.claude/.gitignore', 'agents/newdef.md\n'); fx.commit('BRENT: harness ignore', '.claude/.gitignore')
    r = subprocess.run(['git', 'add', '--', '.claude/agents/newdef.md'], cwd=fx.root, capture_output=True, text=True)
    fx.git('add', '-f', '--', '.claude/agents/newdef.md', 'PROME/result'); fx.git('commit', '-qm', 'PROME: closeout')
    A = fx.git('rev-parse', 'HEAD')
    return f'plain git add rc={r.returncode} {r.stderr.strip()[:90]!r}\nforce-added commit, step10: {short(fx.verify(ref=A, paths=["PROME/result"]))}'
def c4_existing_tracked_owned(fx):
    # does a .claude/.gitignore hide an edit to a TRACKED OWNED file? (gitignore never hides tracked paths)
    fx.freeze(); fx.write('.claude/.gitignore', 'agents/\n'); fx.write('.claude/agents/argus.md', 'edited\n')
    return f'tracked OWNED edit under .claude/.gitignore agents/: {short(fx.verify())}'
run('c4_bound', c4_bound); run('c4_existing_tracked_owned', c4_existing_tracked_owned)
