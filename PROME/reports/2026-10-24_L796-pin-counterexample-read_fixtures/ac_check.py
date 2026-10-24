"""Independent AC1-AC8 checks (my own code), plus pre-fix counterfactual using HEAD's argus_contract."""
import hashlib, importlib.util, json, sys
sys.dont_write_bytecode = True
sys.argv = [sys.argv[0], '__none__']
exec(open('ce.py').read().split("for n, f in [")[0])
spec = importlib.util.spec_from_file_location('old_ac', 'old/argus_contract_head.py'); old = importlib.util.module_from_spec(spec); spec.loader.exec_module(old)

def both(fx):
    d = fx.manifest(); return f'NEW {sc.verify_review()}\n  OLD(HEAD) {old.verify(sc, d)}'

def ac1(fx):
    m = fx.freeze(); d = fx.manifest()
    return (f'rules==loaded: {[tuple(r) for r in d["perimeter"]["rules"]] == sc.load_perimeter()}; '
            f'sha==file: {d["perimeter"]["sha256"] == hashlib.sha256((fx.root/sc.PERIMETER_FILE).read_bytes()).hexdigest()}; '
            f'perimeter not in contract: {"perimeter" not in d["contract"]}; contract_sha ok: {ac.digest(d["contract"]) == d["contract_sha256"]}; '
            f'contract keys {sorted(d["contract"])}')
def ac2(fx):
    fx.freeze()
    fx.write(sc.PERIMETER_FILE, fx.read(sc.PERIMETER_FILE).replace(HDR, HDR + 'PROME/state/AUDIT_PERIMETER.tsv\tEXCLUDED\tx\nPROME/state/HANDOFF_X.md\tEXCLUDED\tx\n', 1))
    fx.write('PROME/state/HANDOFF_X.md', 'x'); return both(fx)
def ac3(fx):
    fx.freeze()
    fx.write(sc.PERIMETER_FILE, fx.read(sc.PERIMETER_FILE).replace('memory/auto/**\tSHARED', 'memory/auto/**\tEXCLUDED', 1))
    fx.write('memory/auto/x.md', 'x'); return both(fx)
def ac4(fx):
    fx.freeze(); fx.write('FORGE/x.md', 'd'); fx.commit('BRENT: forge', 'FORGE/x.md')
    fx.write(sc.PERIMETER_FILE, fx.read(sc.PERIMETER_FILE).replace('FORGE/**\tOWNED', 'FORGE/**\tEXCLUDED', 1)); return both(fx)
def ac5a(fx):
    fx.freeze(); d = fx.manifest(); del d['perimeter']; fx.save(d); fx.write('AGENTS/BROCK/new.md', 'x')
    # also: legacy committed-only foreign path loses attribution
    fx.write('AGENTS/BRENT/c.md', 'c'); fx.commit('BRENT: c', 'AGENTS/BRENT/c.md')
    return f'{sc.verify_review()}'
def ac5b(fx):
    fx.freeze(); d = fx.manifest(); d['perimeter']['rules'][0][1] = 'OWNEDX'; fx.save(d); return f'{sc.verify_review()}'
def ac6(fx):
    fx.freeze(); fx.write('AGENTS/BROCK/new.md', 'x'); return f'{sc.verify_review()}'
def ac6b(fx):
    fx.freeze(); fx.write('AGENTS/BROCK/new.md', 'x'); fx.write(sc.PERIMETER_FILE, HDR + 'foo\tBOGUS\tr\n'); return both(fx)
def ac7(fx):
    fx.freeze(); (fx.root/'AGENTS/ZED').mkdir(parents=True); fx.git('mv', 'PROME/old', 'AGENTS/ZED/old'); return f'{sc.verify_review()}'
def ac8(fx):
    fx.freeze()
    for p in ['memory/auto/finding_prome_new_lesson.md', 'AGENTS/FALCON/inbox/data/2026-10-24_FIRMS.csv', 'NEWROOTFILE.md',
              'PROME/inbox/processed/2026-10-24_from-WALTER_x.md', 'CLAUDE.md']:
        fx.write(p, 'PROME wrote\n')
    return f'{sc.verify_review()}'
for n, f in [('AC1', ac1), ('AC2', ac2), ('AC3', ac3), ('AC4', ac4), ('AC5a', ac5a), ('AC5b', ac5b), ('AC6', ac6), ('AC6b', ac6b), ('AC7', ac7), ('AC8', ac8)]:
    run(n, f)
