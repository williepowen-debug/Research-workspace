"""Counterexample fixtures for the L796 perimeter-pin repair. Disposable repos only; repo tools imported read-only."""
import hashlib, json, shutil, subprocess, sys, tempfile
from pathlib import Path
from unittest.mock import patch
sys.dont_write_bytecode = True
sys.path.insert(0, '/home/willi/Research-workspace/PROME/tools')
import argus_scope as sc, argus_contract as ac

SCR = '/tmp/claude-1000/-home-willi-Research-workspace-PROME/21f2c037-44fb-44e2-b95b-80eb222ec9a7/scratchpad/l796-pin-read/repos'
PERIM = Path('/home/willi/Research-workspace/PROME/state/AUDIT_PERIMETER.tsv').read_text()
GITIGNORE = Path('/home/willi/Research-workspace/.gitignore').read_text()
HDR = 'pattern\tclass\treason\n'

class Fx:
    def __init__(self):
        self.tmp = tempfile.mkdtemp(prefix='pin_', dir=SCR)
        self.root = Path(self.tmp)
        self.p = patch.object(sc, 'ROOT', self.root); self.p.start()
        self.git('init', '-q', '-b', 'master'); self.git('config', 'user.email', 'f@x.test'); self.git('config', 'user.name', 'fx')
        self.write(sc.PERIMETER_FILE, PERIM)
        self.write('.gitignore', GITIGNORE)
        self.write('OWNER.md', 'OTTO owns the unrelated analysis.\n')
        self.write('PROME/old', 'baseline'); self.write('memory/auto/MEMORY.md', 'idx\n'); self.write('CLAUDE.md', 'root\n')
        self.base = self.commit('baseline fixture', sc.PERIMETER_FILE, '.gitignore', 'OWNER.md', 'PROME/old', 'memory/auto/MEMORY.md', 'CLAUDE.md')
        sc.record_baseline(self.base)
        self.write('PROME/result', 'reviewed result')
        self.plan = {'delivered': {'PROME/result': 'PROME bounded repair'}, 'evidence': [], 'observed': {}}
    def git(self, *a):
        return subprocess.run(['git', *a], cwd=self.root, check=True, capture_output=True, text=True).stdout.strip()
    def write(self, path, v):
        t = self.root / path; t.parent.mkdir(parents=True, exist_ok=True); t.write_text(v)
    def read(self, path): return (self.root / path).read_text()
    def commit(self, msg, *paths):
        self.git('add', '--', *paths); self.git('commit', '-qm', msg, '--', *paths); return self.git('rev-parse', 'HEAD')
    def freeze(self): return ac.freeze(sc, self.plan)
    def manifest(self): return json.loads((self.root / sc.REVIEW_FILE).read_text())
    def save(self, d): (self.root / sc.REVIEW_FILE).write_text(json.dumps(d))
    def verify(self, **kw): return sc.verify_review(**kw)
    def close(self): self.p.stop(); shutil.rmtree(self.tmp)

def run(name, fn):
    fx = Fx()
    try:
        out = fn(fx)
    except Exception as e:
        out = f'EXCEPTION {type(e).__name__}: {e}'
    finally:
        fx.close()
    print(f'### {name}\n{out}\n')

# ---------- CE-G1: root .gitignore edited post-freeze hides an OWNED arrival; the .gitignore edit is advisory
def ce_g1(fx):
    fx.freeze()
    fx.write('.gitignore', fx.read('.gitignore') + '\nPROME/state/HANDOFF_X.md\n')
    fx.write('PROME/state/HANDOFF_X.md', 'PROME owned post-freeze write\n')
    st = fx.git('status', '--porcelain', '-uall')
    return f'porcelain: {st!r}\nworking-tree gate: {fx.verify()}'

# ---------- CE-G2: same but a NESTED self-ignoring .gitignore inside PROME/ (OWNED, untracked) -> no trace at all
def ce_g2(fx):
    fx.freeze()
    fx.write('PROME/state/scratch/.gitignore', '*\n')
    fx.write('PROME/state/scratch/HANDOFF_Y.md', 'PROME owned post-freeze write\n')
    st = fx.git('status', '--porcelain', '-uall')
    return f'porcelain: {st!r}\nworking-tree gate: {fx.verify()}'

# ---------- CE-G2c control: same nested ignore BEFORE the 10/22 branch existed would also be invisible (pre-existing)
# (shown by G2: no advisory line, the path is simply absent from inventory)

# ---------- CE-C1: a non-PROME-subject commit of the perimeter BEFORE the freeze self-exempts it from review
#           (attributed_by_commit has no PERIMETER_FILE hard-code) and the pin then carries those unreviewed rules
def ce_c1(fx):
    t = fx.read(sc.PERIMETER_FILE).replace(HDR, HDR + 'PROME/state/AUDIT_PERIMETER.tsv\tSHARED\tx\nPROME/state/HANDOFF_X.md\tEXCLUDED\tx\n', 1)
    fx.write(sc.PERIMETER_FILE, t)
    fx.commit('WALTER: perimeter row for board files', sc.PERIMETER_FILE)
    m = fx.freeze()
    pinned_self = sc.classify(sc.PERIMETER_FILE, ac.pinned_rules(m))
    fx.write('PROME/state/HANDOFF_X.md', 'PROME owned post-freeze write\n')
    return (f'freeze OK; attributed_by_commit keys: {sorted(m["attributed_by_commit"])}\n'
            f'perimeter delivered? {sc.PERIMETER_FILE in m["contract"]["delivered"]}; observed? {sc.PERIMETER_FILE in m["observed"]}\n'
            f'pinned class of perimeter file: {pinned_self}\nworking-tree gate after OWNED-under-baseline write: {fx.verify()}')

# ---------- CE-C1-control: same commit with a PROME subject -> evidence -> must be classified
def ce_c1_control(fx):
    t = fx.read(sc.PERIMETER_FILE).replace(HDR, HDR + 'PROME/state/AUDIT_PERIMETER.tsv\tSHARED\tx\n', 1)
    fx.write(sc.PERIMETER_FILE, t)
    fx.commit('PROME: perimeter row', sc.PERIMETER_FILE)
    return f'freeze: {fx.freeze()}'

# ---------- CE-T1: pin is trusted, never re-derived: hand edit of the pin (outside contract) passes validate
def ce_t1(fx):
    fx.freeze(); d = fx.manifest()
    d['perimeter']['rules'].insert(0, ['PROME/state/HANDOFF_X.md', 'EXCLUDED', 'x'])  # sha256 left as-is
    fx.save(d)
    fx.write('PROME/state/HANDOFF_X.md', 'PROME owned post-freeze write\n')
    return f'tampered pin, digest unchanged: {fx.verify()}'

# ---------- CE-T2: digest/rules consistency never checked: sha256 null with rules present; random sha256
def ce_t2(fx):
    fx.freeze(); d = fx.manifest()
    d['perimeter']['sha256'] = None; fx.save(d); r1 = fx.verify()
    d['perimeter']['sha256'] = 'a' * 64; fx.save(d); r2 = fx.verify()
    live = hashlib.sha256((fx.root / sc.PERIMETER_FILE).read_bytes()).hexdigest()
    return f'sha256=None,rules present: rc {r1[0]}\nsha256=aaaa…: rc {r2[0]} (live file digest {live[:12]}, untouched)'

# ---------- CE-V: validate shape bypass attempts
def ce_v(fx):
    fx.freeze(); d0 = fx.manifest(); out = []
    cases = {
        'rules=[]': {'sha256': None, 'rules': []},
        'rules tuple-ish 4 cells': {'sha256': None, 'rules': [['PROME/**', 'OWNED', 'r', 'x']]},
        'pattern int': {'sha256': None, 'rules': [[1, 'OWNED', 'r']]},
        'class UNATTRIBUTED': {'sha256': None, 'rules': [['**', 'UNATTRIBUTED', 'r']]},
        'extra key': {'sha256': None, 'rules': None, 'x': 1},
        'pin = []': [],
        'pin = false': False,
        'pin = {}': {},
        'rules = dict': {'sha256': None, 'rules': {'a': 1}},
        'rules=None (explicit strict)': {'sha256': None, 'rules': None},
        'pattern with trailing space (valid shape)': {'sha256': None, 'rules': [['PROME/** ', 'OWNED', 'r']] + d0['perimeter']['rules']},
        'empty-string pattern/reason': {'sha256': None, 'rules': [['', 'OWNED', '']] + d0['perimeter']['rules']},
    }
    fx.write('AGENTS/BROCK/new.md', 'x')
    for k, pin in cases.items():
        d = json.loads(json.dumps(d0)); d['perimeter'] = pin; fx.save(d)
        rc, lines = fx.verify(); out.append(f'{k}: rc {rc} {lines[0][:110]!r}')
    d = json.loads(json.dumps(d0)); d['perimeter'] = None; fx.save(d)
    rc, lines = fx.verify(); out.append(f'pin = null (JSON): rc {rc} {lines[0][:110]!r}')
    return '\n'.join(out)

# ---------- CE-R: TOCTOU inside pin_perimeter (file changes between load_perimeter and read_bytes)
def ce_r(fx):
    orig = sc.load_perimeter
    def racing(path=None):
        r = orig(path)
        fx.write(sc.PERIMETER_FILE, fx.read(sc.PERIMETER_FILE) + 'ZZZ/**\tEXCLUDED\trace\n')
        return r
    with patch.object(sc, 'load_perimeter', racing):
        try:
            fx.freeze(); res = 'freeze SUCCEEDED'
        except ValueError as e:
            res = f'freeze REFUSED: {str(e)[:200]}'
    return res + f'; manifest written? {(fx.root / sc.REVIEW_FILE).exists()}'

# ---------- CE-R2: race where the perimeter was DELIVERED (pending at freeze) and moves between delivered sha and pin
def ce_r2(fx):
    fx.write(sc.PERIMETER_FILE, fx.read(sc.PERIMETER_FILE) + 'NEW/**\tEXCLUDED\tnew row\n')
    fx.plan['delivered'][sc.PERIMETER_FILE] = 'PROME perimeter row'
    orig = ac.pin_perimeter
    def racing(s):
        fx.write(sc.PERIMETER_FILE, fx.read(sc.PERIMETER_FILE) + 'PROME/state/HANDOFF_X.md\tEXCLUDED\trace\n')
        return orig(s)
    with patch.object(ac, 'pin_perimeter', racing):
        try:
            fx.freeze(); res = 'freeze SUCCEEDED'
        except ValueError as e:
            res = f'freeze REFUSED: {str(e)[:200]}'
    return res

# ---------- CE-D: perimeter pending AND delivered at the freeze -> pin = the delivered (new) rules; later edits block
def ce_d(fx):
    fx.write(sc.PERIMETER_FILE, fx.read(sc.PERIMETER_FILE).replace(HDR, HDR + 'AGENTS/BRENT/**\tOWNED\tnew\n', 1))
    fx.plan['delivered'][sc.PERIMETER_FILE] = 'PROME perimeter row'
    m = fx.freeze()
    a = ('AGENTS/BRENT/**', 'OWNED', 'new') in ac.pinned_rules(m)
    fx.write('AGENTS/BRENT/x.md', 'desk\n')
    wt = fx.verify()
    A = fx.commit('PROME: closeout', 'PROME/result', sc.PERIMETER_FILE)
    s10 = fx.verify(ref=A, paths=['PROME/result', sc.PERIMETER_FILE])
    # second variant: revert after freeze
    return f'pin has new row: {a}\nwt gate with BRENT pending (pinned OWNED): {wt}\nstep10: {s10}'

# ---------- CE-S10: step 10 committed side: desk commits FORGE/x.md after delivery; then perimeter edited pending to EXCLUDE FORGE
def ce_s10(fx):
    fx.freeze()
    A = fx.commit('PROME: closeout', 'PROME/result')
    fx.write('AGENTS/BRENT/n.md', 'n'); fx.commit('BRENT: note', 'AGENTS/BRENT/n.md')
    r0 = fx.verify(ref=A, paths=['PROME/result'])
    fx.write('FORGE/x.md', 'desk wrote\n'); fx.commit('BRENT: forge note', 'FORGE/x.md')
    fx.write(sc.PERIMETER_FILE, fx.read(sc.PERIMETER_FILE).replace('FORGE/**\tOWNED', 'FORGE/**\tEXCLUDED', 1))
    r1 = fx.verify(ref=A, paths=['PROME/result'])
    return f'step10, foreign EXCLUDED commit after delivery: {r0}\nstep10, + FORGE commit + live perimeter edit: {r1}'

# ---------- CE-L: legacy schema-1 manifest (no --contract) still classifies with the LIVE perimeter
def ce_l(fx):
    lanes, _ = sc.build_scope(fx.base, sc.load_perimeter())
    sc.record_review([e['path'] for e in lanes['OWNED'] + lanes['SHARED'] + lanes['UNATTRIBUTED']])
    fx.write(sc.PERIMETER_FILE, fx.read(sc.PERIMETER_FILE).replace(HDR, HDR + 'PROME/state/AUDIT_PERIMETER.tsv\tEXCLUDED\tx\nPROME/state/HANDOFF_X.md\tEXCLUDED\tx\n', 1))
    fx.write('PROME/state/HANDOFF_X.md', 'PROME owned post-freeze write\n')
    return f'legacy working-tree gate: {fx.verify()}\nmark_reviewed: {sc.mark_reviewed("x")}'

# ---------- CE-M: mark_reviewed + observe preserve the pin; observe after a perimeter edit
def ce_m(fx):
    fx.freeze()
    rc = sc.mark_reviewed('ok'); d = fx.manifest()
    keep1 = d.get('perimeter') is not None and d['verdict']
    fx.write('AGENTS/BROCK/new.md', 'x')
    ac.observe(sc, {'AGENTS/BROCK/new.md': {'owner': 'OTTO', 'reason': 'unrelated', 'basis': {'path': 'OWNER.md', 'commit': fx.base},
                                              'quote': 'OTTO owns the unrelated analysis', 'not_relied_on': True}})
    d2 = fx.manifest()
    fx.write(sc.PERIMETER_FILE, fx.read(sc.PERIMETER_FILE) + 'X/**\tEXCLUDED\tx\n')
    r = fx.verify()
    return f'mark_reviewed {rc}; pin kept after mark: {keep1}; pin kept after observe: {d2["perimeter"] == d["perimeter"]}\nverify after live edit: {r}\nmark_reviewed now: {sc.mark_reviewed("y")}'

# ---------- CE-O: observed-only classification of a PENDING perimeter edit at freeze -> pin carries unreviewed rules
def ce_o(fx):
    fx.write(sc.PERIMETER_FILE, fx.read(sc.PERIMETER_FILE).replace(HDR, HDR + 'PROME/state/HANDOFF_X.md\tEXCLUDED\tx\n', 1))
    fx.plan['observed'] = {sc.PERIMETER_FILE: {'owner': 'OTTO', 'reason': 'not relied on', 'basis': {'path': 'OWNER.md', 'commit': fx.base},
                                               'quote': 'OTTO owns the unrelated analysis', 'not_relied_on': True}}
    m = fx.freeze()
    fx.write('PROME/state/HANDOFF_X.md', 'PROME owned post-freeze write\n')
    return f'freeze OK with perimeter observed-only; pinned has HANDOFF row: {("PROME/state/HANDOFF_X.md","EXCLUDED","x") in ac.pinned_rules(m)}\ngate: {fx.verify()}'

# ---------- CE-X: ORDINARY: pin present and a PROME commit lands post-freeze in FORGE (OWNED) -> blocks
def ce_x(fx):
    fx.freeze()
    fx.write('memory/auto/finding_x.md', 'desk\n'); fx.commit('BRENT: memory', 'memory/auto/finding_x.md')
    return f'committed-only SHARED by desk after freeze (pinned): {fx.verify()}'

for n, f in [('CE-G1 root .gitignore hides OWNED arrival', ce_g1), ('CE-G2 nested self-ignoring .gitignore', ce_g2),
             ('CE-C1 foreign-subject perimeter commit pre-freeze', ce_c1), ('CE-C1 control PROME subject', ce_c1_control),
             ('CE-T1 tampered pin', ce_t1), ('CE-T2 digest never checked', ce_t2), ('CE-V validate shapes', ce_v),
             ('CE-R TOCTOU in pin_perimeter', ce_r), ('CE-R2 race delivered perimeter', ce_r2),
             ('CE-D delivered perimeter pinned', ce_d), ('CE-S10 step-10 committed side', ce_s10),
             ('CE-L legacy schema-1 live perimeter', ce_l), ('CE-M mark_reviewed/observe keep pin', ce_m),
             ('CE-O observed-only perimeter at freeze', ce_o), ('CE-X committed-only SHARED after freeze', ce_x)]:
    if len(sys.argv) == 1 or any(a in n for a in sys.argv[1:]):
        run(n, f)
