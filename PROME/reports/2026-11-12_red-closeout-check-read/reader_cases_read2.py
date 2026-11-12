#!/usr/bin/env python3
"""Reviewer's own counterexamples for closeout_check e (commit 71f7d26586). Throwaway repos only."""
import os, subprocess, sys, tempfile
from pathlib import Path

SCRIPT = os.environ.get('UNDER') or str(Path(__file__).resolve().parent / 'AGENTS/RED/scripts/closeout_check.py')
ns = {'__name__': 'rev', '__file__': SCRIPT}
exec(compile(open(SCRIPT).read(), 'closeout_check.py', 'exec'), ns)

TODAY = '2026-11-12'
P_REG, P_CL = 'AGENTS/RED/registry/FALSIFICATION_TRIGGERS.tsv', 'AGENTS/RED/thesis/CHANGELOG.md'
REG0 = 'trigger_id\tstate\nRED-FT-01\tARMED; 0-of-3\n'
REG1 = 'trigger_id\tstate\nRED-FT-01\tFIRED 2026-11-12; exit armed\n'
CL0 = '# CHANGELOG\n\n## 2026-11-12 S63 morning\nold view -> new view\n'
CL1 = '# CHANGELOG\n\n## 2026-11-12 S64 afternoon\nFT-01 ARMED -> FIRED\n\n## 2026-11-12 S63 morning\nold\n'
STATUS_FX = '# RED STATUS\n\n## CURRENT ASSESSMENT\n\n| Hypothesis | Prob |\n|---|:--:|\n| Stag | 32% |\n'
INBOX = 'PROME/inbox/'
PROC = 'PROME/inbox/processed/'
MORNING = '2026-11-12_from-RED_closeout.md'
MORNING_BYTES = 'S63 packet: FT-06 run broke, net-bear 68 to 67\n'


def sh(d, *a, env=None):
    r = subprocess.run(['git', '-c', 'user.name=f', '-c', 'user.email=f@invalid', '-c', 'commit.gpgsign=false', *a],
                       cwd=d, capture_output=True, text=True, env=env)
    if r.returncode:
        raise RuntimeError('git %s: %s' % (a, r.stderr))
    return r.stdout.strip()


def put(d, rel, text, append=False):
    p = Path(d) / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    with open(p, 'a' if append else 'w', encoding='utf-8', newline='') as fh:
        fh.write(text)


def change_state(d):
    put(d, P_REG, REG1); put(d, P_CL, CL1)


def base_repo(d, packets):
    sh(d, 'init', '-q')
    put(d, P_REG, REG0); put(d, P_CL, CL0)
    put(d, 'AGENTS/RED/STATUS.md', STATUS_FX)
    put(d, 'AGENTS/RED/OUTBOX.md', '# OUTBOX - FROZEN 2026-11-12\n')
    put(d, INBOX + 'README.md', 'inbox\n')
    for rel, text in packets.items():
        put(d, rel, text)
    sh(d, 'add', '-A'); sh(d, 'commit', '-q', '-m', 'base')


def grade(d, at=None, today=TODAY):
    ns['ROOT'] = Path(d)
    F = []
    try:
        note = ns['check_state_change'](ns['Vintage'](at), F, today)
    except Exception as exc:
        return 'RAISED', repr(exc)
    es = [f for f in F if f[0] == 'e']
    w8 = [f for f in es if 'PROME/inbox' in f[2] or f[1] == 'UNKNOWN']
    got = 'UNKNOWN' if any(f[1] == 'UNKNOWN' for f in es) else ('FAIL' if w8 else 'PASS')
    return got, (w8[0][2] if w8 else note or '')[:160]


results = []


def case(name, packets, setup, want, today=TODAY):
    with tempfile.TemporaryDirectory() as d:
        base_repo(d, packets)
        at = setup(d)
        got = grade(d, at if isinstance(at, str) else None, today)
    ok = got[0] == want
    results.append(ok)
    print('%s  %-78s want %-7s got %s | %s' % ('OK ' if ok else 'BAD', name, want, got[0], got[1]))


# R1: PROME files the earlier packet with git mv AND appends a consumption stamp (observed practice:
#     R075-R095 renames into processed/ on 2026-10-16). Shared working tree, uncommitted.
def r1(d):
    change_state(d)
    Path(d, PROC).mkdir(parents=True, exist_ok=True)
    sh(d, 'mv', INBOX + MORNING, PROC + MORNING)
    put(d, PROC + MORNING, '\n-- consumed by PROME 14:40 ET\n', append=True)
case('R1 earlier packet git-mv\'d + stamped by PROME (wt), no new packet', {INBOX + MORNING: MORNING_BYTES}, r1, 'FAIL')


# R1b: same, but in --at form: PROME's move+stamp and RED's state change land in one commit
#      (e.g. a shared-index sweep). Base = at^ holds the packet in the inbox.
def r1b(d):
    r1(d); sh(d, 'add', '-A'); sh(d, 'commit', '-q', '-m', 'x'); return sh(d, 'rev-parse', 'HEAD')
case('R1b same as R1, --at form', {INBOX + MORNING: MORNING_BYTES}, r1b, 'FAIL')


# R1c: PROME annotates the earlier packet in place (no move), RED never writes a new one.
def r1c(d):
    change_state(d); put(d, INBOX + MORNING, '\n-- PROME read 14:40 ET\n', append=True)
case('R1c earlier packet annotated in place by someone else, no new packet', {INBOX + MORNING: MORNING_BYTES}, r1c, 'FAIL')


# R2: genuine new packet whose filename collides with a same-day packet already filed in processed/.
def r2(d):
    change_state(d); put(d, INBOX + MORNING, 'S64 packet: FT-01 ARMED -> FIRED, net-bear 67 -> 70\n')
case('R2 NEW packet reusing the name of a filed same-day packet', {PROC + MORNING: MORNING_BYTES}, r2, 'PASS')


# R3: genuine new packet whose BYTES equal an earlier same-day packet (template / re-send).
def r3(d):
    change_state(d); put(d, INBOX + '2026-11-12_from-RED_S64.md', MORNING_BYTES)
case('R3 new file, identical bytes to the earlier packet (copy/template)', {PROC + MORNING: MORNING_BYTES}, r3, 'FAIL')


# R4: an OLD packet from yesterday renamed to today's date (same bytes) -> base set is filtered by
#     today's date, so the old blob is not "old".
def r4(d):
    change_state(d)
    sh(d, 'mv', PROC + '2026-11-11_from-RED_x.md', INBOX + '2026-11-12_from-RED_x.md')
case('R4 yesterday\'s packet renamed to today\'s date, same bytes', {PROC + '2026-11-11_from-RED_x.md': 'yesterday\n'}, r4, 'FAIL')


# R5: packet committed separately BEFORE the state change (carve-out 1 commit first), check on wt.
def r5(d):
    put(d, INBOX + '2026-11-12_from-RED_S64.md', 'S64 packet: FT-01 fired\n')
    sh(d, 'add', '-A'); sh(d, 'commit', '-q', '-m', 'RED -> PROME packet')
    change_state(d)
case('R5 new packet committed first, state change still uncommitted (wt)', {PROC + MORNING: MORNING_BYTES}, r5, 'FAIL')


# R6: --at with a packet committed in the commit BEFORE the state-change commit.
def r6(d):
    r5(d); sh(d, 'add', '-A'); sh(d, 'commit', '-q', '-m', 'state'); return sh(d, 'rev-parse', 'HEAD')
case('R6 --at state commit whose parent added the packet', {PROC + MORNING: MORNING_BYTES}, r6, 'FAIL')


# R7: --at across midnight: commit authored 00:05 on 11-13 carrying the state change and a packet
#     written at 23:58 dated 11-12. today = author date 11-13.
def r7(d):
    change_state(d); put(d, INBOX + '2026-11-12_from-RED_S64-late.md', 'late packet\n')
    put(d, P_CL, CL1.replace('## 2026-11-12 S64', '## 2026-11-13 S64'))
    sh(d, 'add', '-A')
    env = dict(os.environ, GIT_AUTHOR_DATE='2026-11-13T00:05:00-05:00', GIT_COMMITTER_DATE='2026-11-13T00:05:00-05:00')
    sh(d, 'commit', '-q', '-m', 'state', env=env)
    return sh(d, 'rev-parse', 'HEAD')
with tempfile.TemporaryDirectory() as d:
    base_repo(d, {})
    at = r7(d)
    ns['ROOT'] = Path(d)
    today7 = ns['Vintage'](at).today()
    g = grade(d, at, today7)
    print('INFO R7 midnight --at: today=%s -> %s | %s' % (today7, g[0], g[1]))


# R8: packet in a nested subdirectory of the inbox (e.g. inbox/RED/...) and packet name with spaces/unicode
def r8(d):
    change_state(d); put(d, INBOX + 'sub dir/2026-11-12_from-RED_S64 é.md', 'nested new\n')
case('R8 new packet in nested dir, name with space+unicode', {PROC + MORNING: MORNING_BYTES}, r8, 'PASS')


# R9: genuine new packet consumed by PROME's git mv (staged) before RED's gate runs -> must PASS (req 3)
def r9(d):
    change_state(d); put(d, INBOX + '2026-11-12_from-RED_S64.md', 'S64 new\n')
    sh(d, 'add', INBOX + '2026-11-12_from-RED_S64.md')
    Path(d, PROC).mkdir(parents=True, exist_ok=True)
    sh(d, 'mv', INBOX + '2026-11-12_from-RED_S64.md', PROC + '2026-11-12_from-RED_S64.md')
case('R9 new packet staged then git mv\'d to processed/ (req 3, wt)', {PROC + MORNING: MORNING_BYTES}, r9, 'PASS')


# R9b: req 3 in --at form: state change + packet in commit A; PROME moves it in a later commit; grade A.
def r9b(d):
    change_state(d); put(d, INBOX + '2026-11-12_from-RED_S64.md', 'S64 new\n')
    sh(d, 'add', '-A'); sh(d, 'commit', '-q', '-m', 'A'); a = sh(d, 'rev-parse', 'HEAD')
    Path(d, PROC).mkdir(parents=True, exist_ok=True)
    sh(d, 'mv', INBOX + '2026-11-12_from-RED_S64.md', PROC + '2026-11-12_from-RED_S64.md')
    sh(d, 'commit', '-q', '-m', 'PROME files'); return a
case('R9b --at state commit, packet later moved by PROME', {PROC + MORNING: MORNING_BYTES}, r9b, 'PASS')


# R10: CRLF working-tree packet with core.autocrlf=true whose LF form equals the earlier blob -> old
def r10(d):
    sh(d, 'config', 'core.autocrlf', 'true')
    change_state(d); put(d, INBOX + '2026-11-12_from-RED_S64.md', MORNING_BYTES.replace('\n', '\r\n'))
case('R10 CRLF copy of the earlier packet under autocrlf (old bytes after clean filter)', {PROC + MORNING: MORNING_BYTES}, r10, 'FAIL')


# R11: listing unreadable at base only: --at a root commit (no parent)
with tempfile.TemporaryDirectory() as d:
    sh(d, 'init', '-q'); put(d, P_REG, REG1); put(d, P_CL, CL1); put(d, INBOX + '2026-11-12_from-RED_a.md', 'a\n')
    sh(d, 'add', '-A'); sh(d, 'commit', '-q', '-m', 'root')
    print('INFO R11 --at root commit (base unreadable):', grade(d, sh(d, 'rev-parse', 'HEAD')))

# R12: inbox directory unreadable (chmod 000 processed/) in wt form, new packet lives there
def r12(d):
    change_state(d); put(d, PROC + '2026-11-12_from-RED_S64.md', 'new consumed\n')
    os.chmod(Path(d, PROC), 0o000)
with tempfile.TemporaryDirectory() as d:
    base_repo(d, {INBOX + MORNING: MORNING_BYTES})
    r12(d)
    g = grade(d)
    os.chmod(Path(d, PROC), 0o755)
    print('INFO R12 processed/ unreadable (chmod 000), new packet inside: %s | %s' % g)

# R13: legacy OUTBOX: new top heading identical to an older heading lower down (same-day, generic heading)
def r13(d):
    change_state(d)
    put(d, 'AGENTS/RED/OUTBOX.md', '# OUTBOX\n\n## 20261112 RED -> PROME\nnew entry about FT-01\n\n## 20261112 RED -> PROME\nmorning\n')
with tempfile.TemporaryDirectory() as d:
    base_repo(d, {})
    put(d, 'AGENTS/RED/OUTBOX.md', '# OUTBOX\n\n## 20261112 RED -> PROME\nmorning\n'); sh(d, 'commit', '-qam', 'b2')
    r13(d); print('INFO R13 legacy: new OUTBOX entry with a heading identical to an older one:', grade(d))

# R14: legacy OUTBOX: old top heading edited by one char, no new entry -> passes?
with tempfile.TemporaryDirectory() as d:
    base_repo(d, {})
    put(d, 'AGENTS/RED/OUTBOX.md', '# OUTBOX\n\n## 20261112 -079 morning\nmorning\n'); sh(d, 'commit', '-qam', 'b2')
    change_state(d); put(d, 'AGENTS/RED/OUTBOX.md', '# OUTBOX\n\n## 20261112 -079 morning.\nmorning\n')
    print('INFO R14 legacy: old top heading edited by one char, no new entry:', grade(d))

print('\n%d/%d cases met the reviewer\'s expectation' % (sum(results), len(results)))

print('--- read 2: cases aimed at the changed condition ---')
# N1: RED appends an addendum to its unconsumed morning packet (a delivery by design, author 2b),
#     then PROME files it with a plain git mv before RED's gate runs (shared tree). Req 2 + req 3.
def n1(d):
    change_state(d)
    put(d, INBOX + MORNING, 'Addendum S64: FT-01 ARMED -> FIRED\n', append=True)
    Path(d, PROC).mkdir(parents=True, exist_ok=True)
    sh(d, 'mv', INBOX + MORNING, PROC + MORNING)
case('N1 RED-edited unconsumed packet (2b delivery), then plain git mv to processed/', {INBOX + MORNING: MORNING_BYTES}, n1, 'PASS')
def n1b(d):
    n1(d); sh(d, 'add', '-A'); sh(d, 'commit', '-q', '-m', 'x'); return sh(d, 'rev-parse', 'HEAD')
case('N1b same, --at form', {INBOX + MORNING: MORNING_BYTES}, n1b, 'PASS')

# N2: PROME files the OLD packet with a rename (observed R100 renames on 11-06) AND a stamp (observed 10-16).
def n2(d):
    change_state(d)
    Path(d, PROC).mkdir(parents=True, exist_ok=True)
    sh(d, 'mv', INBOX + MORNING, PROC + MORNING.replace('.md', '-filed.md'))
    put(d, PROC + MORNING.replace('.md', '-filed.md'), '\n-- consumed by PROME\n', append=True)
case('N2 OLD packet filed with rename + stamp, no new packet', {INBOX + MORNING: MORNING_BYTES}, n2, 'FAIL')

# N3: R2's genuine new packet (named like a filed one) is then consumed by PROME, overwriting processed/X.
def n3(d):
    change_state(d); put(d, INBOX + MORNING, 'S64 packet: FT-01 ARMED -> FIRED\n')
    sh(d, 'add', INBOX + MORNING)
    sh(d, 'mv', '-f', INBOX + MORNING, PROC + MORNING)
case('N3 R2\'s new same-named packet, then filed over processed/X by git mv -f', {PROC + MORNING: MORNING_BYTES}, n3, 'PASS')

# N4: new packet delivered while an old one (in inbox at base) is filed plainly — overlap, must PASS on the new.
def n4(d):
    change_state(d); put(d, INBOX + '2026-11-12_from-RED_S64.md', 'S64 new\n')
    Path(d, PROC).mkdir(parents=True, exist_ok=True)
    sh(d, 'mv', INBOX + MORNING, PROC + MORNING)
    put(d, PROC + MORNING, '\n-- consumed\n', append=True)
case('N4 overlap: old packet filed+stamped AND a new packet in the inbox', {INBOX + MORNING: MORNING_BYTES}, n4, 'PASS')
print('\n%d/%d (all cases) met expectation' % (sum(results), len(results)))
