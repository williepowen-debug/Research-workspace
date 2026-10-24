import importlib.util, sys
sys.dont_write_bytecode = True
exec(open('ce.py').read().split("for n, f in [")[0])
spec = importlib.util.spec_from_file_location('old_ac', 'old/argus_contract_head.py'); old = importlib.util.module_from_spec(spec); spec.loader.exec_module(old)
def g1_old(fx):
    old.freeze(sc, fx.plan)
    fx.write('.gitignore', fx.read('.gitignore') + '\nPROME/state/HANDOFF_X.md\n'); fx.write('PROME/state/HANDOFF_X.md', 'x')
    return f'{old.verify(sc, fx.manifest())}'
def c1_old(fx):
    t = fx.read(sc.PERIMETER_FILE).replace(HDR, HDR + 'PROME/state/AUDIT_PERIMETER.tsv\tSHARED\tx\nPROME/state/HANDOFF_X.md\tEXCLUDED\tx\n', 1)
    fx.write(sc.PERIMETER_FILE, t); fx.commit('WALTER: perimeter row', sc.PERIMETER_FILE)
    m = old.freeze(sc, fx.plan); fx.write('PROME/state/HANDOFF_X.md', 'x')
    return f'auto={sorted(m["attributed_by_commit"])}; {old.verify(sc, fx.manifest())}'
def g1_add_attempt(fx):
    fx.freeze(); fx.write('.gitignore', fx.read('.gitignore') + '\nPROME/state/HANDOFF_X.md\n'); fx.write('PROME/state/HANDOFF_X.md', 'x')
    r = subprocess.run(['git', 'add', '--', 'PROME/state/HANDOFF_X.md'], cwd=fx.root, capture_output=True, text=True)
    return f'git add rc {r.returncode}: {r.stderr.strip()[:120]}'
run('G1 at HEAD code', g1_old); run('C1 at HEAD code', c1_old); run('G1 git add of ignored file', g1_add_attempt)
