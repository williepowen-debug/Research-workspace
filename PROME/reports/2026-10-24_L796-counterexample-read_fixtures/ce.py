"""Counterexample fixtures for DOCKET L796 — disposable git repos only; imports repo tools read-only."""
import json, shutil, subprocess, sys, tempfile
from pathlib import Path
from unittest.mock import patch
sys.dont_write_bytecode = True
sys.path.insert(0, '/home/willi/Research-workspace/PROME/tools')
import argus_scope as sc, argus_contract as ac

PERIM = Path('/home/willi/Research-workspace/PROME/state/AUDIT_PERIMETER.tsv').read_text()

class Fx:
    def __init__(self):
        self.tmp = tempfile.mkdtemp(prefix='l796_', dir='/tmp/claude-1000/-home-willi-Research-workspace-PROME/59ab405d-868c-429b-a040-0cbdbacff64e/scratchpad/l796')
        self.root = Path(self.tmp)
        self.p = patch.object(sc, 'ROOT', self.root); self.p.start()
        self.git('init', '-q', '-b', 'master'); self.git('config', 'user.email', 'f@x.test'); self.git('config', 'user.name', 'fx')
        self.write('PROME/state/AUDIT_PERIMETER.tsv', PERIM)
        self.write('OWNER.md', 'OTTO owns the unrelated analysis.\n')
        self.write('PROME/old', 'baseline'); self.write('memory/auto/MEMORY.md', 'idx\n')
        self.write('CLAUDE.md', 'root\n')
        self.base = self.commit('baseline fixture', 'PROME/state/AUDIT_PERIMETER.tsv', 'OWNER.md', 'PROME/old', 'memory/auto/MEMORY.md', 'CLAUDE.md')
        sc.record_baseline(self.base)
        self.write('PROME/result', 'reviewed result')
        self.plan = {'delivered': {'PROME/result': 'PROME bounded repair'}, 'evidence': [], 'observed': {}}
    def git(self, *a):
        return subprocess.run(['git', *a], cwd=self.root, check=True, capture_output=True, text=True).stdout.strip()
    def write(self, path, v):
        t = self.root / path; t.parent.mkdir(parents=True, exist_ok=True); t.write_text(v)
    def commit(self, msg, *paths):
        self.git('add', '--', *paths); self.git('commit', '-qm', msg, '--', *paths); return self.git('rev-parse', 'HEAD')
    def freeze(self): return ac.freeze(sc, self.plan)
    def verify(self, **kw): return sc.verify_review(**kw)
    def close(self): self.p.stop(); shutil.rmtree(self.tmp)

def run(name, fn):
    fx = Fx()
    try:
        out = fn(fx)
        print(f'### {name}\n{out}\n')
    finally:
        fx.close()

def ce1(fx):
    """Step 10: foreign post-freeze pending arrival still blocks the --ref delivery verify."""
    fx.freeze()
    fx.write('AGENTS/REGINALD/decks/img1.png', 'deck image')   # foreign desk, after freeze
    wt = fx.verify()
    A = fx.commit('PROME: closeout delivery', 'PROME/result')
    step10 = fx.verify(ref=A, paths=['PROME/result'])
    return f'working-tree gate: {wt}\nstep-10 --ref {A[:9]} --paths PROME/result: {step10}'

def ce2(fx):
    """Wrong owner: PROME's own post-freeze writes in SHARED / UNATTRIBUTED / EXCLUDED lanes w/o filename evidence."""
    fx.freeze()
    fx.write('memory/auto/finding_prome_new_lesson.md', 'PROME wrote this after the freeze\n')
    fx.write('AGENTS/FALCON/inbox/data/2026-10-24_FIRMS.csv', 'PROME carve-out packet body\n')
    fx.write('CLAUDE.md', 'root\nPROME post-freeze edit\n')
    fx.write('NEWROOTFILE.md', 'PROME stray\n')
    fx.write('PROME/inbox/processed/2026-10-24_from-WALTER_x.md', 'consumed by PROME\n')
    return f'working-tree gate: {fx.verify()}'

def ce3(fx):
    """Over-block (safe direction): a desk CONSUMES a PROME packet during the closeout window (git mv to processed/)."""
    fx.write('AGENTS/CARL/inbox/2026-10-24_from-PROME_gap.md', 'packet\n')
    fx.commit('PROME -> CARL: gap', 'AGENTS/CARL/inbox/2026-10-24_from-PROME_gap.md')
    fx.plan['delivered']['AGENTS/CARL/inbox/2026-10-24_from-PROME_gap.md'] = 'PROME packet'
    fx.freeze()
    (fx.root/'AGENTS/CARL/inbox/processed').mkdir(parents=True, exist_ok=True)
    fx.git('mv', 'AGENTS/CARL/inbox/2026-10-24_from-PROME_gap.md', 'AGENTS/CARL/inbox/processed/2026-10-24_from-PROME_gap.md')
    r1 = fx.verify()
    return f'desk consumes delivered PROME packet: {r1}'

def ce3b(fx):
    """Desk consumes an OLDER PROME packet (committed before baseline? no: in window, not delivered, auto-attrib refused by PROME subject)."""
    fx.write('AGENTS/CARL/inbox/2026-10-24_from-PROME_gap.md', 'packet\n')
    c = fx.commit('PROME -> CARL: gap', 'AGENTS/CARL/inbox/2026-10-24_from-PROME_gap.md')
    fx.plan['observed'] = {}
    # PROME separately committed it in the window; must deliver or observe it. Deliver it.
    fx.plan['delivered']['AGENTS/CARL/inbox/2026-10-24_from-PROME_gap.md'] = 'PROME packet'
    fx.freeze()
    # a relay by WALTER named via-PROME, desk-written, arrives after freeze
    fx.write('AGENTS/WALTER/inbox/2026-10-24_relay_via-PROME_note.md', 'walter relay\n')
    return f'desk-written via-PROME relay: {fx.verify()}'

def ce4(fx):
    """Overlap: SHARED path committed in window by a FOREIGN desk, then PROME edits it pending after freeze."""
    fx.write('memory/auto/finding_desk.md', 'desk v1\n')
    fx.commit('BRENT: memory', 'memory/auto/finding_desk.md')
    fx.freeze()   # committed-only foreign => attributed_by_commit
    fx.write('memory/auto/finding_desk.md', 'desk v1\nPROME extends n+1 after freeze\n')
    return f'PROME pending edit over desk-committed shared memory: {fx.verify()}'

def ce5(fx):
    """Rename out of OWNED lane after freeze by a foreign hand (staged git mv of an OWNED file)."""
    fx.write('PROME/notes.md', 'x\n'); fx.commit('PROME: notes', 'PROME/notes.md')
    fx.plan['delivered']['PROME/notes.md'] = 'PROME notes'
    fx.freeze()
    (fx.root/'AGENTS/ZED').mkdir(parents=True, exist_ok=True)
    fx.git('mv', 'PROME/old', 'AGENTS/ZED/old')
    return f'OWNED file git-mv into AGENTS/: {fx.verify()}'

def ce6(fx):
    """mark-reviewed promotion now succeeds over a post-freeze pending arrival (scope of change)."""
    fx.freeze()
    fx.write('AGENTS/BROCK/new.md', 'x')
    return f'mark_reviewed: {sc.mark_reviewed("ce6")}'

def ce7(fx):
    """Missing information: perimeter unreadable after freeze => strict (expect UNCLASSIFIED)."""
    fx.freeze()
    fx.write('AGENTS/BROCK/new.md', 'x')
    (fx.root / 'PROME/state/AUDIT_PERIMETER.tsv').write_text('pattern\tclass\treason\nfoo\tBOGUS\tr\n')
    return f'malformed perimeter: {fx.verify()}'

def ce8(fx):
    """Perimeter edited after freeze to reclassify memory/auto as EXCLUDED; the perimeter file is OWNED so it must self-flag."""
    fx.freeze()
    p = fx.root / 'PROME/state/AUDIT_PERIMETER.tsv'
    p.write_text(p.read_text().replace('memory/auto/**\tSHARED', 'memory/auto/**\tEXCLUDED'))
    fx.write('memory/auto/x.md', 'x')
    return f'perimeter edited post-freeze: {fx.verify()}'

def ce9(fx):
    """Step 10 with --observe of the foreign arrival: confirms the documented remedy is an observe round per arrival."""
    fx.freeze()
    fx.write('AGENTS/REGINALD/decks/img1.png', 'deck image')
    A = fx.commit('PROME: closeout delivery', 'PROME/result')
    fx.write('AGENTS/REGINALD/decks/img2.png', 'deck image 2')  # second arrival between gate and step 10
    return f'step-10 with two arrivals: {fx.verify(ref=A, paths=["PROME/result"])}'

for n, f in [('CE3 desk consumes PROME packet', ce3),
             ('CE3b desk-written via-PROME relay', ce3b), ('CE4 overlap', ce4), ('CE5 rename OWNED out', ce5),
             ('CE6 mark-reviewed', ce6), ('CE7 malformed perimeter', ce7), ('CE8 perimeter edited', ce8), ('CE9 step-10 two arrivals', ce9)]:
    run(n, f)

def ce8b(fx):
    """Self-exempting perimeter edit: a pending edit inserts an EXCLUDED row above PROME/** covering the perimeter file
    and PROME/state/**; then PROME edits an OWNED state file post-freeze."""
    fx.write('PROME/state/GATES.tsv', 'g\n'); fx.commit('PROME: gates', 'PROME/state/GATES.tsv')
    fx.plan['delivered']['PROME/state/GATES.tsv'] = 'gates'
    fx.write('PROME/state/DOCKET.tsv', 'd\n')
    fx.plan['delivered']['PROME/state/DOCKET.tsv'] = 'docket'
    fx.freeze()
    p = fx.root / 'PROME/state/AUDIT_PERIMETER.tsv'
    s = p.read_text().replace('pattern\tclass\treason\n', 'pattern\tclass\treason\nPROME/state/AUDIT_PERIMETER.tsv\tEXCLUDED\tx\nPROME/state/HANDOFF_X.md\tEXCLUDED\tx\n', 1)
    p.write_text(s)
    fx.write('PROME/state/HANDOFF_X.md', 'PROME owned post-freeze write\n')
    wt = fx.verify()
    return f'self-exempting perimeter edit: {wt}'

for n, f in [('CE8b self-exempting perimeter', ce8b)]:
    run(n, f)
