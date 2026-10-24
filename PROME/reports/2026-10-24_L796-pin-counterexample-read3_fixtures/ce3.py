"""Round-3 counterexamples for the L796 pin fix pass 2. Disposable repos only; repo tools imported read-only."""
import hashlib, json, os, shutil, subprocess, sys, tempfile
from pathlib import Path
sys.dont_write_bytecode = True
D = '/tmp/claude-1000/-home-willi-Research-workspace-PROME/21f2c037-44fb-44e2-b95b-80eb222ec9a7/scratchpad/l796-pin-read3'
os.environ['TMPDIR'] = D + '/tmp'; os.makedirs(D + '/tmp', exist_ok=True); tempfile.tempdir = D + '/tmp'
from unittest.mock import patch
sys.path.insert(0, '/home/willi/Research-workspace/PROME/tools')
import argus_scope as sc, argus_contract as ac

SCR = D + '/repos'
PERIM = Path('/home/willi/Research-workspace/PROME/state/AUDIT_PERIMETER.tsv').read_text()
GITIGNORE = Path('/home/willi/Research-workspace/.gitignore').read_text()
HDR = 'pattern\tclass\treason\n'
OBS = lambda base: {'owner': 'OTTO', 'reason': 'not relied on', 'basis': {'path': 'OWNER.md', 'commit': base},
                    'quote': 'OTTO owns the unrelated analysis', 'not_relied_on': True}

class Fx:
    def __init__(self):
        self.tmp = tempfile.mkdtemp(prefix='pin3_', dir=SCR)
        self.root = Path(self.tmp)
        self.p = patch.object(sc, 'ROOT', self.root); self.p.start()
        self.git('init', '-q', '-b', 'master'); self.git('config', 'user.email', 'f@x.test'); self.git('config', 'user.name', 'fx')
        self.write(sc.PERIMETER_FILE, PERIM); self.write('.gitignore', GITIGNORE)
        self.write('OWNER.md', 'OTTO owns the unrelated analysis.\n')
        self.write('PROME/old', 'baseline'); self.write('PROME/tracked.md', 'owned tracked\n')
        self.write('memory/auto/MEMORY.md', 'idx\n'); self.write('CLAUDE.md', 'root\n')
        self.write('.claude/agents/argus.md', 'argus def\n'); self.write('AGENTS/BRENT/STATUS.md', 's\n')
        self.base = self.commit('baseline fixture', sc.PERIMETER_FILE, '.gitignore', 'OWNER.md', 'PROME/old',
                                'PROME/tracked.md', 'memory/auto/MEMORY.md', 'CLAUDE.md', '.claude/agents/argus.md',
                                'AGENTS/BRENT/STATUS.md')
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
    def save(self, m): (self.root / sc.REVIEW_FILE).write_text(json.dumps(m, indent=2) + '\n')
    def verify(self, **kw): return sc.verify_review(**kw)
    def perim(self, rows): self.write(sc.PERIMETER_FILE, self.read(sc.PERIMETER_FILE).replace(HDR, HDR + rows, 1))
    def porc(self): return self.git('status', '--porcelain', '-uall')
    def close(self): self.p.stop(); shutil.rmtree(self.tmp)

def short(r):
    rc, lines = r
    return (rc, [l[:150] for l in lines])

def tryfreeze(fx):
    try:
        fx.freeze(); return 'freeze OK'
    except ValueError as e:
        return f'freeze REFUSED: {str(e)[:220]}'

def tryobserve(fx, adds, ref=None):
    try:
        ac.observe(sc, adds, ref=ref); return 'observe ACCEPTED'
    except ValueError as e:
        return f'observe REFUSED: {str(e)[:160]}'

def run(name, fn):
    fx = Fx()
    try:
        out = fn(fx)
    except Exception as e:
        import traceback; out = f'EXCEPTION {type(e).__name__}: {e}\n{traceback.format_exc()[-600:]}'
    finally:
        fx.close()
    print(f'### {name}\n{out}\n', flush=True)

HIDE = '\nPROME/state/HANDOFF_X.md\n'

# ---------- (1) ❌A / ❌B closure
def a1_post_freeze_committed_root_gitignore(fx):
    fx.freeze()
    fx.write('.gitignore', fx.read('.gitignore') + HIDE); fx.commit('WALTER: ignore board cache', '.gitignore')
    fx.write('PROME/state/HANDOFF_X.md', 'owned post-freeze\n')
    wt = fx.verify()
    A = fx.commit('PROME: closeout', 'PROME/result')
    s10 = fx.verify(ref=A, paths=['PROME/result'])
    return f'HANDOFF_X visible in porcelain? {"HANDOFF_X" in fx.porc()}\nworking-tree gate: {short(wt)}\nstep10 --ref: {short(s10)}'

def a2_pre_freeze_committed_root_gitignore(fx):
    fx.write('.gitignore', fx.read('.gitignore') + HIDE); fx.commit('WALTER: ignore board cache', '.gitignore')
    fx.write('PROME/state/HANDOFF_X.md', 'owned pending\n')
    r = tryfreeze(fx)
    fx.plan['observed'] = {'.gitignore': OBS(fx.base)}
    r2 = tryfreeze(fx)
    return f'not delivered: {r}\ndeclared observed: {r2}'

def a3_post_freeze_committed_root_gitattributes(fx):
    fx.freeze(); fx.write('.gitattributes', '* -text\n'); fx.commit('WALTER: attrs', '.gitattributes')
    wt = fx.verify(); A = fx.commit('PROME: closeout', 'PROME/result')
    return f'wt: {short(fx.verify())}\nstep10: {short(fx.verify(ref=A, paths=["PROME/result"]))}'

def b1_observe_perimeter_and_root_gitignore(fx):
    fx.freeze()
    fx.perim('PROME/state/HANDOFF_X.md\tEXCLUDED\tx\n'); fx.commit('WALTER: perimeter row', sc.PERIMETER_FILE)
    fx.write('.gitignore', fx.read('.gitignore') + '\nfoo.tmp\n'); fx.commit('WALTER: ignore', '.gitignore')
    o1 = tryobserve(fx, {sc.PERIMETER_FILE: OBS(fx.base)})
    o2 = tryobserve(fx, {'.gitignore': OBS(fx.base)})
    A = fx.commit('PROME: closeout', 'PROME/result')
    o3 = tryobserve(fx, {sc.PERIMETER_FILE: OBS(fx.base)}, ref=A)
    o4 = tryobserve(fx, {'.gitignore': OBS(fx.base)}, ref=A)
    return (f'observe perimeter (wt): {o1}\nobserve root .gitignore (wt): {o2}\nobserve perimeter ref=A: {o3}\n'
            f'observe .gitignore ref=A: {o4}\ngate wt: {short(fx.verify())}\nstep10: {short(fx.verify(ref=A, paths=["PROME/result"]))}')

def b2_hand_inserted_observed(fx):
    fx.freeze()
    fx.perim('PROME/state/HANDOFF_X.md\tEXCLUDED\tx\n'); fx.commit('WALTER: perimeter row', sc.PERIMETER_FILE)
    fx.write('.gitignore', fx.read('.gitignore') + HIDE); fx.commit('WALTER: ignore', '.gitignore')
    m = fx.manifest(); seen = ac.inventory(sc, m['contract']['baseline'], fx.git('rev-parse', 'HEAD'))
    out = []
    for p in (sc.PERIMETER_FILE, '.gitignore'):
        mm = json.loads(json.dumps(m))
        mm['observed'][p] = [ac.observation(sc, p, OBS(fx.base), seen[p])]
        fx.save(mm)
        out.append(f'hand-inserted observed {p}: wt {short(fx.verify())}')
    A = fx.commit('PROME: closeout', 'PROME/result')
    out.append(f'  same, step10: {short(fx.verify(ref=A, paths=["PROME/result"]))}')
    out.append(f'  mark_reviewed: {sc.mark_reviewed("x")}')
    return '\n'.join(out)

# ---------- (2) ⚠️C scoping
def c1_research_gitignore(fx):
    fx.freeze()
    fx.write('AGENTS/BROCK/research/2026-10-24_x/.gitignore', '*.csv\n')
    wt = fx.verify()
    fx.commit('BROCK: research ignore', 'AGENTS/BROCK/research/2026-10-24_x/.gitignore')
    return f'pending: {short(wt)}\ncommitted (BROCK subject): {short(fx.verify())}'

def c2_guarded_dirs(fx):
    fx.freeze(); out = []
    for p in ('PROME/.gitignore', 'FORGE/.gitignore', '.gitignore', 'AGENTS/BRENT/inbox/.gitignore',
              'AGENTS/WALTER/inbox/WILL/.gitignore', 'memory/auto/.gitignore', 'newtop/.gitignore',
              'PROME/inbox/.gitignore', '.claude/.gitignore', 'AGENTS/BRENT/.gitignore', 'AGENTS/.gitignore',
              'scripts/.gitignore', '.claude/agents/.gitignore'):
        out.append(f'{p:40s} never_advisory={ac.never_advisory(sc, p, ac.pinned_rules(fx.manifest()))}')
    return '\n'.join(out)

def c3_pending_each(fx):
    out = []
    fx.freeze()
    for p in ('PROME/.gitignore', 'FORGE/.gitignore', 'AGENTS/BRENT/inbox/.gitignore', 'memory/auto/.gitignore'):
        fx.write(p, 'zz.tmp\n'); r = fx.verify(); (fx.root / p).unlink()
        out.append(f'pending {p}: rc {r[0]} {r[1][0][:90]}')
    fx.write('.gitignore', fx.read('.gitignore') + '\nzz\n'); out.append(f'pending root .gitignore: {short(fx.verify())[0]}')
    return '\n'.join(out)

def c4_claude_gitignore_hides_owned(fx):
    fx.freeze()
    fx.write('.claude/agents/newdef.md', 'PROME new agent def, unreviewed\n')
    ctl = fx.verify()
    fx.write('.claude/.gitignore', 'agents/newdef.md\n')
    wt = fx.verify()
    vis = fx.porc()
    fx.commit('BRENT: harness ignore', '.claude/.gitignore')
    wt2 = fx.verify()
    A = fx.commit('PROME: closeout', 'PROME/result')
    s10 = fx.verify(ref=A, paths=['PROME/result'])
    ign = fx.git('status', '--porcelain', '--ignored', '-uall', '--', '.claude')
    return (f'control (no ignore file): {short(ctl)}\npending .claude/.gitignore: {short(wt)}\nporcelain: {vis!r}\n'
            f'committed under BRENT subject: {short(wt2)}\nstep10: {short(s10)}\nignored under .claude: {ign!r}')

def c4b_claude_gitignore_observe_and_prefreeze(fx):
    fx.write('.claude/.gitignore', 'agents/newdef.md\n'); fx.commit('BRENT: harness ignore', '.claude/.gitignore')
    fx.write('.claude/agents/newdef.md', 'PROME new agent def, unreviewed\n')
    r = tryfreeze(fx)
    m = fx.manifest() if (fx.root / sc.REVIEW_FILE).exists() else {}
    return f'pre-freeze desk commit of .claude/.gitignore + OWNED pending: {r}; auto={sorted(m.get("attributed_by_commit", {}))}; gate {short(fx.verify())}'

def c5_desk_root_gitignore_hides_prome_packet(fx):
    fx.freeze()
    pk = 'AGENTS/BRENT/inbox/2026-10-24_from-PROME_task.md'
    fx.write(pk, 'PROME carve-out 1 packet, uncommitted\n')
    ctl = fx.verify()
    fx.write('AGENTS/BRENT/.gitignore', 'inbox/*from-PROME*\n')
    wt = fx.verify()
    return f'control: {short(ctl)}\nwith pending AGENTS/BRENT/.gitignore: {short(wt)}'

def c6_agents_gitignore(fx):
    fx.freeze()
    fx.write('AGENTS/BRENT/inbox/2026-10-24_from-PROME_task.md', 'packet\n')
    fx.write('AGENTS/.gitignore', '*/inbox/*from-PROME*\n')
    return f'pending AGENTS/.gitignore hiding a from-PROME packet: {short(fx.verify())}'

def c7_terry_real_shape(fx):
    # TERRY's real desk-root .gitignore ignores inbox/WILL/* (a SHARED lane); a post-freeze edit is advisory
    fx.freeze()
    fx.write('AGENTS/TERRY/.gitignore', 'inbox/WILL/*\n')
    fx.write('AGENTS/TERRY/inbox/WILL/x.csv', 'raw\n')
    return f'TERRY-shape desk-root ignore of a SHARED inbox lane: {short(fx.verify())}; porcelain {fx.porc()!r}'

# ---------- (3) further counterexamples
def d1_root_dotfile_row_disarms_root_guard(fx):
    fx.perim('.*\tEXCLUDED\ttop-level harness dotfiles (.mcp.json, .env)\n')
    fx.plan['delivered'][sc.PERIMETER_FILE] = 'PROME perimeter row for harness dotfiles'
    fx.freeze()
    A0 = fx.commit('PROME: closeout', 'PROME/result', sc.PERIMETER_FILE)
    g = ac.never_advisory(sc, '.gitignore', ac.pinned_rules(fx.manifest()))
    fx.write('.gitignore', fx.read('.gitignore') + HIDE)
    fx.write('PROME/state/HANDOFF_X.md', 'owned post-freeze\n')
    wt = fx.verify()
    fx.commit('WALTER: ignore', '.gitignore'); wt2 = fx.verify()
    return f'root .gitignore guarded under pin? {g}\npending root .gitignore hiding OWNED: {short(wt)}\ncommitted by WALTER: {short(wt2)}'

def d2_gitattributes_changes_porcelain(fx):
    fx.write('PROME/tracked.md', 'owned tracked\n$Id$\n'); fx.commit('base2', 'PROME/tracked.md')
    sc.record_baseline(fx.git('rev-parse', 'HEAD'))
    fx.freeze()
    fx.write('.claude/.gitattributes', '* ident\n')  # unguarded location, but scope is .claude/ only
    fx.write('.gitattributes', 'PROME/tracked.md ident\n')
    fx.git('add', '--renormalize', '--dry-run', '.') if False else None
    fx.write('PROME/tracked.md', 'owned tracked\n$Id: SECRET EDIT $\n')
    p = fx.porc()
    r = fx.verify()
    (fx.root / '.gitattributes').unlink()
    p2 = fx.porc()
    return f'with ident attr, porcelain: {p!r}\ngate: {short(r)}\nwithout attr, porcelain: {p2!r}'

def d3_guarded_path_removed_before_freeze(fx):
    fx.git('rm', '-q', '.gitignore'); fx.git('commit', '-qm', 'WALTER: drop gitignore')
    r = tryfreeze(fx)
    fx.plan['delivered']['.gitignore'] = 'reviewed: deletion of root ignore'
    r2 = tryfreeze(fx)
    m = fx.manifest(); A = fx.commit('PROME: closeout', 'PROME/result')
    return f'deleted root .gitignore not delivered: {r}\ndelivered deletion: {r2}; sha={m["contract"]["delivered"][".gitignore"]["sha256"]}\nstep10: {short(fx.verify(ref=A, paths=["PROME/result"]))}'

def d3b_perimeter_removed_before_freeze(fx):
    fx.git('rm', '-q', sc.PERIMETER_FILE); fx.git('commit', '-qm', 'WALTER: drop perimeter')
    r = tryfreeze(fx)
    fx.plan['delivered'][sc.PERIMETER_FILE] = 'reviewed deletion'
    r2 = tryfreeze(fx); m = fx.manifest()
    fx.write('AGENTS/BROCK/new.md', 'x')
    return f'not delivered: {r}\ndelivered: {r2}; pin={m["perimeter"]}\nforeign arrival under null pin: {short(fx.verify())}'

def d4_null_rules_observed_nested(fx):
    fx.write('AGENTS/BROCK/research/x/.gitignore', '*.csv\n'); fx.commit('PROME: oops', 'AGENTS/BROCK/research/x/.gitignore')
    fx.plan['observed'] = {'AGENTS/BROCK/research/x/.gitignore': OBS(fx.base)}
    r = tryfreeze(fx)
    m = fx.manifest()
    ok = short(fx.verify())
    m['perimeter'] = {'sha256': None, 'rules': None}; fx.save(m)
    nul = short(fx.verify())
    m.pop('perimeter'); fx.save(m)
    nokey = short(fx.verify())
    return f'PROME-subject nested research ignore observed at freeze: {r}; gate {ok}\nrules null: {nul}\nno pin key: {nokey}'

def d5_probe_name_collision(fx):
    # a delivered row for a real dotfile name the probe could collide with
    fx.perim('PROME/**/.ignore-probe\tEXCLUDED\tx\n')
    fx.plan['delivered'][sc.PERIMETER_FILE] = 'row'
    fx.freeze()
    return f'PROME/.gitignore guarded with colliding row? {ac.never_advisory(sc, "PROME/.gitignore", ac.pinned_rules(fx.manifest()))}'

def d6_gitignore_in_excluded_dir_with_shared_file_rows(fx):
    fx.freeze()
    fx.write('scripts/new_shared_tool.py', 'x')  # UNATTRIBUTED? no: scripts/** EXCLUDED
    fx.write('scripts/.gitignore', 'read_cap_check.py\n')
    fx.write('scripts/read_cap_check.py', 'PROME new file (SHARED row)\n')
    p = fx.porc()
    return f'scripts/.gitignore hides SHARED-row file: porcelain {p!r}; gate {short(fx.verify())}'

# ---------- (4) regression
def r1_ac6(fx):
    fx.freeze(); fx.write('AGENTS/BROCK/new.md', 'x'); return f'AC6: {short(fx.verify())}'

def r2_committed_shared(fx):
    fx.freeze(); fx.write('memory/auto/f.md', 'd'); fx.commit('BRENT: memory', 'memory/auto/f.md')
    wt = fx.verify(); A = fx.commit('PROME: closeout', 'PROME/result')
    return f'desk committed-only SHARED after freeze: {short(wt)}\nstep10: {short(fx.verify(ref=A, paths=["PROME/result"]))}'

def r3_delivered_perimeter_step10(fx):
    fx.perim('AGENTS/BRENT/**\tOWNED\tnew\n')
    fx.plan['delivered'][sc.PERIMETER_FILE] = 'PROME perimeter row'
    m = fx.freeze()
    sha_ok = m['perimeter']['sha256'] == m['contract']['delivered'][sc.PERIMETER_FILE]['sha256']
    rules_ok = ac.pinned_rules(m) == sc.load_perimeter()
    A = fx.commit('PROME: closeout', 'PROME/result', sc.PERIMETER_FILE)
    s10 = fx.verify(ref=A, paths=['PROME/result', sc.PERIMETER_FILE])
    fx.write('AGENTS/BRENT/x.md', 'desk'); wt = fx.verify()
    return f'pin sha==delivered: {sha_ok}; pin rules==parse of file: {rules_ok}\nstep10: {short(s10)}\nwt + AGENTS/BRENT arrival (OWNED under pin): {short(wt)}'

CASES = [(k, v) for k, v in list(globals().items()) if callable(v) and k[:2] in ('a1','a2','a3','b1','b2','c1','c2','c3','c4','c5','c6','c7','d1','d2','d3','d4','d5','d6','r1','r2','r3')]
sel = sys.argv[1:]
for k, v in CASES:
    if not sel or any(k.startswith(s) for s in sel):
        run(k, v)
