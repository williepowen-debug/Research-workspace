"""Round-2 counterexamples for the L796 pin fix pass. Disposable repos only; repo tools imported read-only."""
import hashlib, json, os, shutil, subprocess, sys, tempfile
from pathlib import Path
from unittest.mock import patch
sys.dont_write_bytecode = True
sys.path.insert(0, '/home/willi/Research-workspace/PROME/tools')
import argus_scope as sc, argus_contract as ac

SCR = '/tmp/claude-1000/-home-willi-Research-workspace-PROME/21f2c037-44fb-44e2-b95b-80eb222ec9a7/scratchpad/l796-pin-read2/repos'
PERIM = Path('/home/willi/Research-workspace/PROME/state/AUDIT_PERIMETER.tsv').read_text()
GITIGNORE = Path('/home/willi/Research-workspace/.gitignore').read_text()
HDR = 'pattern\tclass\treason\n'
OBS = lambda base: {'owner': 'OTTO', 'reason': 'not relied on', 'basis': {'path': 'OWNER.md', 'commit': base},
                    'quote': 'OTTO owns the unrelated analysis', 'not_relied_on': True}

class Fx:
    def __init__(self):
        self.tmp = tempfile.mkdtemp(prefix='pin2_', dir=SCR)
        self.root = Path(self.tmp)
        self.p = patch.object(sc, 'ROOT', self.root); self.p.start()
        self.git('init', '-q', '-b', 'master'); self.git('config', 'user.email', 'f@x.test'); self.git('config', 'user.name', 'fx')
        self.write(sc.PERIMETER_FILE, PERIM); self.write('.gitignore', GITIGNORE)
        self.write('OWNER.md', 'OTTO owns the unrelated analysis.\n')
        self.write('PROME/old', 'baseline'); self.write('PROME/tracked.md', 'owned tracked\n')
        self.write('memory/auto/MEMORY.md', 'idx\n'); self.write('CLAUDE.md', 'root\n')
        self.base = self.commit('baseline fixture', sc.PERIMETER_FILE, '.gitignore', 'OWNER.md', 'PROME/old',
                                'PROME/tracked.md', 'memory/auto/MEMORY.md', 'CLAUDE.md')
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
    def verify(self, **kw): return sc.verify_review(**kw)
    def perim(self, rows): self.write(sc.PERIMETER_FILE, self.read(sc.PERIMETER_FILE).replace(HDR, HDR + rows, 1))
    def close(self): self.p.stop(); shutil.rmtree(self.tmp)

def tryfreeze(fx):
    try:
        fx.freeze(); return 'freeze OK'
    except ValueError as e:
        return f'freeze REFUSED: {str(e)[:230]}'

def run(name, fn):
    fx = Fx()
    try:
        out = fn(fx)
    except Exception as e:
        out = f'EXCEPTION {type(e).__name__}: {e}'
    finally:
        fx.close()
    print(f'### {name}\n{out}\n', flush=True)

# ---------------- (1) re-verify the two ❌ with own fixtures
def v_c1(fx):
    fx.perim('PROME/state/AUDIT_PERIMETER.tsv\tSHARED\tx\nPROME/state/HANDOFF_X.md\tEXCLUDED\tx\n')
    fx.commit('WALTER: perimeter row for board files', sc.PERIMETER_FILE)
    r1 = tryfreeze(fx)
    w1 = (fx.root / sc.REVIEW_FILE).exists()
    # observed attempt on the committed-only perimeter
    fx.plan['observed'] = {sc.PERIMETER_FILE: OBS(fx.base)}
    r2 = tryfreeze(fx)
    fx.plan['observed'] = {}
    # control: unrelated committed-only SHARED desk path still auto-attributed alongside
    return f'non-PROME perimeter commit, not delivered: {r1}; manifest written? {w1}\n+ declared observed: {r2}'

def v_c1_control_no_change(fx):
    fx.write('memory/auto/f.md', 'd'); fx.commit('BRENT: memory', 'memory/auto/f.md')
    m = fx.freeze()
    return f'perimeter untouched; freeze OK; auto={sorted(m["attributed_by_commit"])}; pin sha == file: {m["perimeter"]["sha256"] == hashlib.sha256((fx.root/sc.PERIMETER_FILE).read_bytes()).hexdigest()}'

def v_o(fx):
    fx.perim('PROME/state/HANDOFF_X.md\tEXCLUDED\tx\n')
    fx.plan['observed'] = {sc.PERIMETER_FILE: OBS(fx.base)}
    r1 = tryfreeze(fx)
    fx.plan['delivered'][sc.PERIMETER_FILE] = 'PROME row'
    r2 = tryfreeze(fx)
    return f'pending perimeter observed-only: {r1}\ndelivered AND observed: {r2}'

def v_g1(fx):
    fx.freeze()
    fx.write('.gitignore', fx.read('.gitignore') + '\nPROME/state/HANDOFF_X.md\n')
    fx.write('PROME/state/HANDOFF_X.md', 'PROME owned post-freeze write\n')
    return f'porcelain: {fx.git("status","--porcelain","-uall")!r}\ngate: {fx.verify()}'

def v_d(fx):
    fx.perim('AGENTS/BRENT/**\tOWNED\tnew\n')
    fx.plan['delivered'][sc.PERIMETER_FILE] = 'PROME perimeter row'
    m = fx.freeze()
    newrow = ('AGENTS/BRENT/**', 'OWNED', 'new') in ac.pinned_rules(m)
    shaok = m['perimeter']['sha256'] == m['contract']['delivered'][sc.PERIMETER_FILE]['sha256']
    wt0 = fx.verify()
    A = fx.commit('PROME: closeout', 'PROME/result', sc.PERIMETER_FILE)
    s10 = fx.verify(ref=A, paths=['PROME/result', sc.PERIMETER_FILE])
    fx.write('AGENTS/BRENT/x.md', 'desk\n'); fx.write('AGENTS/BROCK/y.md', 'desk\n')
    wt1 = fx.verify()
    s10b = fx.verify(ref=A, paths=['PROME/result', sc.PERIMETER_FILE])
    return (f'pin has delivered row: {newrow}; pin sha == delivered sha: {shaok}\nwt gate clean: {wt0}\nstep10 clean: {s10}\n'
            f'wt gate + BRENT (new pin OWNED) + BROCK arrivals: {wt1}\nstep10 same: {s10b}')

# ---------------- (2) new counterexamples against the fix
def n1_committed_gitignore_post_freeze(fx):
    fx.freeze()
    fx.write('.gitignore', fx.read('.gitignore') + '\nPROME/state/HANDOFF_X.md\n')
    fx.commit('WALTER: ignore board cache', '.gitignore')
    fx.write('PROME/state/HANDOFF_X.md', 'PROME owned post-freeze write\n')
    wt = fx.verify()
    A = fx.commit('PROME: closeout', 'PROME/result')
    s10 = fx.verify(ref=A, paths=['PROME/result'])
    vis = fx.git('status', '--porcelain', '-uall')
    ign = fx.git('status', '--porcelain', '--ignored', '-uall', '--', 'PROME')
    return f'working-tree gate: {wt}\nstep10 --ref: {s10}\nporcelain: {vis!r}\nignored under PROME/: {ign!r}'

def n1_control_prome_subject(fx):
    fx.freeze()
    fx.write('.gitignore', fx.read('.gitignore') + '\nPROME/state/HANDOFF_X.md\n')
    fx.commit('PROME: ignore', '.gitignore')
    fx.write('PROME/state/HANDOFF_X.md', 'x\n')
    return f'PROME-subject .gitignore commit post-freeze: {fx.verify()}'

def n1c_committed_gitignore_pre_freeze(fx):
    fx.write('.gitignore', fx.read('.gitignore') + '\nPROME/state/HANDOFF_X.md\n')
    fx.commit('WALTER: ignore board cache', '.gitignore')
    fx.write('PROME/state/HANDOFF_X.md', 'PROME owned pending write, never delivered\n')
    m = fx.freeze()
    return f'freeze OK; auto={sorted(m["attributed_by_commit"])}; HANDOFF_X in inventory? {"PROME/state/HANDOFF_X.md" in m["inventory"]}; gate: {fx.verify()}'

def n1d_committed_gitattributes_post_freeze(fx):
    fx.freeze()
    fx.write('.gitattributes', '* -text\n'); fx.commit('WALTER: attrs', '.gitattributes')
    return f'committed .gitattributes post-freeze: {fx.verify()}'

def n2_observe_perimeter_after_freeze(fx):
    fx.freeze()
    fx.perim('PROME/state/HANDOFF_X.md\tEXCLUDED\tWALTER board handoff\n')
    fx.commit('WALTER: perimeter row for board handoffs', sc.PERIMETER_FILE)
    before = fx.verify()
    try:
        ac.observe(sc, {sc.PERIMETER_FILE: OBS(fx.base)}); obs = 'observe() ACCEPTED the perimeter'
    except ValueError as e:
        obs = f'observe() REFUSED: {e}'
    after = fx.verify()
    rc_mark = sc.mark_reviewed('ok')
    A = fx.commit('PROME: closeout', 'PROME/result')
    s10 = fx.verify(ref=A, paths=['PROME/result'])
    # next day: baseline advances to the delivery commit; a fresh freeze pins the WALTER rules with no delivery demanded
    sc.record_baseline(A)
    fx.write('PROME/result2', 'next day'); fx.plan = {'delivered': {'PROME/result2': 'next'}, 'evidence': [], 'observed': {}}
    m2 = fx.freeze()
    pinned_walter = ('PROME/state/HANDOFF_X.md', 'EXCLUDED', 'WALTER board handoff') in ac.pinned_rules(m2)
    fx.write('PROME/state/HANDOFF_X.md', 'PROME owned write\n')
    nd = fx.verify()
    return (f'gate before observe: {before}\n{obs}\ngate after observe: {after}\nmark_reviewed: {rc_mark}\nstep10: {s10}\n'
            f'next-day freeze pins WALTER rows without delivery: {pinned_walter}\nnext-day gate with OWNED-under-old-rules write: {nd}')

def n3_committed_and_pending_perimeter(fx):
    fx.perim('ZZ/**\tEXCLUDED\tcommitted\n'); fx.commit('BRENT: zz', sc.PERIMETER_FILE)
    fx.perim('YY/**\tEXCLUDED\tpending\n')
    r1 = tryfreeze(fx)
    fx.plan['delivered'][sc.PERIMETER_FILE] = 'PROME both rows'
    m = fx.freeze(); rules = ac.pinned_rules(m)
    has = (('ZZ/**', 'EXCLUDED', 'committed') in rules, ('YY/**', 'EXCLUDED', 'pending') in rules)
    A = fx.commit('PROME: closeout', 'PROME/result', sc.PERIMETER_FILE)
    s10 = fx.verify(ref=A, paths=['PROME/result', sc.PERIMETER_FILE])
    return f'undelivered: {r1}\ndelivered: pin has (committed,pending) rows {has}\nstep10: {s10}'

def n4_rm_and_mv(fx):
    out = []
    fx.git('rm', '-q', sc.PERIMETER_FILE)
    out.append(f'git rm at freeze, not delivered: {tryfreeze(fx)}')
    fx.plan['delivered'][sc.PERIMETER_FILE] = 'PROME removes perimeter'
    fx.write('memory/auto/f.md', 'd'); fx.commit('BRENT: memory', 'memory/auto/f.md')
    out.append(f'git rm at freeze, delivered (+ desk committed-only memory file): {tryfreeze(fx)}')
    return '\n'.join(out)

def n4b_mv_after_freeze(fx):
    fx.freeze()
    fx.git('mv', sc.PERIMETER_FILE, 'PROME/state/AUDIT_PERIMETER_v2.tsv')
    fx.write('AGENTS/BROCK/new.md', 'x')
    wt = fx.verify()
    fx.git('commit', '-qm', 'WALTER: rename perimeter')
    wt2 = fx.verify()
    return f'staged git mv after freeze: {wt}\ncommitted (WALTER subject): {wt2}'

def n5_nested_and_attributes(fx):
    fx.freeze(); out = []
    fx.write('.gitattributes', '*.md text\n'); out.append(f'pending root .gitattributes: {fx.verify()}')
    (fx.root / '.gitattributes').unlink()
    fx.write('AGENTS/BROCK/.gitignore', 'tmp/\n'); out.append(f'pending AGENTS/BROCK/.gitignore (cannot hide PROME files): {fx.verify()}')
    (fx.root / 'AGENTS/BROCK/.gitignore').unlink()
    fx.write('memory/auto/.gitignore', '*.tmp\n'); out.append(f'pending memory/auto/.gitignore: {fx.verify()}')
    return '\n'.join(out)

def n6_case_and_form(fx):
    fx.freeze(); out = []
    fx.write('.GITIGNORE', 'PROME/state/HANDOFF_X.md\n'); fx.write('PROME/state/HANDOFF_X.md', 'x\n')
    out.append(f'.GITIGNORE: porcelain {fx.git("status","--porcelain","-uall")!r}; gate {fx.verify()}')
    (fx.root / '.GITIGNORE').unlink()
    out.append(f'never_advisory forms: .gitignore={ac.never_advisory(sc, ".gitignore")} PROME//.gitignore={ac.never_advisory(sc, "PROME//.gitignore")} '
               f'./PROME/state/AUDIT_PERIMETER.tsv={ac.never_advisory(sc, "./PROME/state/AUDIT_PERIMETER.tsv")} .gitignore.bak={ac.never_advisory(sc, ".gitignore.bak")}')
    # symlinked .gitignore at root pointing to a file with the hiding rule
    (fx.root / 'PROME/state/HANDOFF_X.md').unlink()
    fx.write('AGENTS/BROCK/ign', 'PROME/state/HANDOFF_X.md\n')
    os.replace(fx.root / '.gitignore', fx.root / 'gi.bak')
    os.symlink('AGENTS/BROCK/ign', fx.root / '.gitignore')
    fx.write('PROME/state/HANDOFF_X.md', 'x\n')
    out.append(f'symlinked .gitignore: porcelain {fx.git("status","--porcelain","-uall")!r}; gate {fx.verify()}')
    return '\n'.join(out)

def n7_skip_worktree(fx):
    fx.freeze()
    fx.git('update-index', '--skip-worktree', 'PROME/tracked.md')
    fx.write('PROME/tracked.md', 'owned tracked, edited after freeze\n')
    a = (fx.git('status', '--porcelain', '-uall'), fx.verify())
    fx.git('update-index', '--no-skip-worktree', 'PROME/tracked.md'); fx.git('update-index', '--assume-unchanged', 'PROME/tracked.md')
    b = (fx.git('status', '--porcelain', '-uall'), fx.verify())
    return f'skip-worktree: porcelain {a[0]!r}; gate {a[1]}\nassume-unchanged: porcelain {b[0]!r}; gate {b[1]}'

def n8_pin_not_bound_to_delivered_bytes(fx):
    fx.perim('NEW/**\tEXCLUDED\tdelivered row\n')
    fx.plan['delivered'][sc.PERIMETER_FILE] = 'PROME row'
    orig = sc.load_perimeter
    calls = {'n': 0}
    def other_read(path=None):  # simulates an A->B->A flip during pin_perimeter: rules read from B, file bytes A afterwards
        calls['n'] += 1
        return [('PROME/state/HANDOFF_X.md', 'EXCLUDED', 'B')] + orig(path)
    with patch.object(sc, 'load_perimeter', other_read):
        r = tryfreeze(fx)
    m = fx.manifest() if (fx.root / sc.REVIEW_FILE).exists() else None
    if not m:
        return r
    fx.write('PROME/state/HANDOFF_X.md', 'PROME owned write\n')
    return (f'{r}; pin sha == delivered sha: {m["perimeter"]["sha256"] == m["contract"]["delivered"][sc.PERIMETER_FILE]["sha256"]}; '
            f'pin rules == rules parsed from delivered bytes: {ac.pinned_rules(m) == orig()}\ngate: {fx.verify()}')

# ---------------- (4) regressions
def r1_ac6(fx):
    fx.freeze(); fx.write('AGENTS/BROCK/new.md', 'x'); return f'AC6: {fx.verify()}'

def r2_committed_shared(fx):
    fx.freeze()
    fx.write('memory/auto/finding_x.md', 'desk\n'); fx.commit('BRENT: memory', 'memory/auto/finding_x.md')
    fx.write('AGENTS/BRENT/STATUS.md', 'desk\n'); fx.commit('BRENT: status', 'AGENTS/BRENT/STATUS.md')
    wt = fx.verify()
    A = fx.commit('PROME: closeout', 'PROME/result')
    return f'committed-only SHARED + EXCLUDED desk files after freeze: {wt}\nstep10: {fx.verify(ref=A, paths=["PROME/result"])}'

def r3_owned_pending_blocks(fx):
    fx.freeze(); fx.write('PROME/state/HANDOFF_X.md', 'x'); return f'OWNED pending arrival: {fx.verify()}'

CASES = [('V-C1', v_c1), ('V-C1ctl', v_c1_control_no_change), ('V-O', v_o), ('V-G1', v_g1), ('V-D', v_d),
         ('N1 ', n1_committed_gitignore_post_freeze), ('N1ctl', n1_control_prome_subject), ('N1c', n1c_committed_gitignore_pre_freeze),
         ('N1d', n1d_committed_gitattributes_post_freeze), ('N2', n2_observe_perimeter_after_freeze),
         ('N3', n3_committed_and_pending_perimeter), ('N4 ', n4_rm_and_mv), ('N4b', n4b_mv_after_freeze),
         ('N5', n5_nested_and_attributes), ('N6', n6_case_and_form), ('N7', n7_skip_worktree), ('N8', n8_pin_not_bound_to_delivered_bytes),
         ('R1', r1_ac6), ('R2', r2_committed_shared), ('R3', r3_owned_pending_blocks)]
for n, f in CASES:
    if len(sys.argv) == 1 or any(n.strip() == a for a in sys.argv[1:]):
        run(n.strip(), f)
