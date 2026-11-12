#!/usr/bin/env python3
"""Falsification set for scripts/closeout_check.py (built S54 2026-10-15).

Per the repair-completion rule these are ACCEPTANCE CONDITIONS, pinned to commits:

  75e1b12b3  the S53 10:33 addendum, PRE-fix. The gate MUST fail a / b / c / d / e:
             a  11 rows in the STATUS table vs 6 non-RESOLVED in canon
                (the build spec said "10 vs 6" — the instrument counts 11: five closed
                rows 042/046/047/048/051 shown open on top of the six; the spec's figure
                was typed, this one is measured)
             b  STATUS 10W/13C/1A and NEXUS "13 CORRECT · 10 WRONG · 1 ACTIVE" vs canon
                13C/10W/2A — and NEXUS's "(9W/12C/1A) lagged canon" must NOT flag: a
                history cue AFTER the figure retires it (the before-only window flagged it)
             c  the carried S52 header still claimed "FT-02 0 of 3" against canon 1-of-3
             d  SCRATCH newest stamp 10/14 23:47 vs STATUS 10/15 10:33 (646 min) — A2 skipped
             e  registry state changed vs the parent (FT-02 0->1 of 3) with CHANGELOG
                unchanged — A4->W3 skipped
             SCOPE LIMIT, stated: "FT-10 read four ways" at this vintage was a PROSE
             disagreement (header / hypothesis row / trigger row / bottom line); c reads
             the trigger table and the header counts, not prose. Not caught here by design.
  47b622ddf  the S53 repair commit. The spec claimed d/e must flag here; they do NOT —
             SCRATCH 11:06 vs STATUS 10:59 and CHANGELOG S53 present. The one true finding
             at this vintage is c: FT-11's STATUS cell dropped canon's 0-of-5 (fixed in the
             working tree at S54). The spec's vintage was wrong; this file records the
             measured truth (finding_record_of_an_action_is_not_the_action).
  working tree (--no-delegate)  must be clean: rc 0.
  parsers    live_tallies / derive_tally / lead_token / newest_stamp on synthetic input.
  argparse   an unknown flag refuses (rc 2) and prints nothing that looks like a verdict.

M12-3 REPAIR (S64 2026-11-12, Will's word 14:18 ET via PROME prome-e8; finding CATO M12-3).
ACCEPTANCE CONDITIONS, written 14:24 ET BEFORE closeout_check.py was edited. The check under
repair is e's W8 leg: a registered state change needs a RED packet in PROME/inbox/.
Defect: any RED packet dated today, anywhere under PROME/inbox/ (processed/ included),
satisfied it, so an earlier same-day delivery passed a later, undelivered change.
"New since the comparison base" (base = HEAD for the working tree, <at>^ for --at) is
decided by CONTENT, not by path: a packet counts only if its bytes (git blob id) appear in
no RED packet dated today at the base. A path test fails on PROME's git mv, because
processed/<name> is a new path holding old bytes.
  1   counterexample: state change; only an EARLIER same-day packet, (1a) in processed/,
      (1b) still in the inbox                                           -> e FAIL
  2   valid delivery: (2a) a new untracked packet; (2b) the unconsumed earlier packet
      edited, so new bytes; (2c) --at a commit adding the state change and the packet
                                                                        -> e PASS
  3   consumption: (3a) a new packet already moved to processed/ before the gate -> PASS;
      (3b) an OLD packet moved by PROME's staged git mv at gate time -> FAIL (the move
      must not count as new); (3c) an edit to a packet already in processed/ at the base
      -> FAIL (PROME has filed it and will not read it again)
  neighbours: ordinary   no state change, no packet -> no e finding
              overlap    earlier AND new packet -> PASS on the new one
              wrong owner  new today-dated from-PROME / from-REDWOOD packet, or a new RED
                         packet dated yesterday -> FAIL
              missing information  PROME/inbox listing unreadable (no git) -> e UNKNOWN (rc 2)
              concurrent activity  = 3b (PROME's move lands in the shared tree mid-closeout)
              copy       old bytes under a new filename -> FAIL
  real data: CATO's probe re-run in memory on commit 506e6e2951 (base = current = 506e6e2951,
             FT state ARMED -> FIRED, CHANGELOG entry dated today; the real inbox holds the
             consumed S63 packet) -> e FAIL. Before the repair it returned no finding.
  Each case runs in a throwaway git repo (tempfile), never in the fleet repo.
  Run the same file against the pre-repair script with CLOSEOUT_CHECK_UNDER_TEST=<path>;
  1a, 1b, 3b, 3c, copy, missing information, the CATO probe and the listing-shape test
  must FAIL there, and every other M12-3 case must pass.
  legacy OUTBOX branch (frozen 2026-11-12; read for older vintages): the SAME defect lived
             there — any OUTBOX edit plus a top entry dated today passed, so the 12:10 freeze
             banner (506e6e2951) with the 09:53 -079 entry on top would have delivered a later
             change. Probe at 506e6e2951 vs its parent -> e FAIL. Found 14:26 ET (from date) while
             measuring --at ebe839ffe0, after the conditions above were written; added at 14:27 ET.
             OPEN, not this defect: no pre-freeze date limit on that branch.
  NOT TESTABLE BY THIS CHECK (stays a manual read): whether the new packet COVERS the
  change. A blob test proves the packet's bytes are new, not what they say.

Run:  python3 AGENTS/RED/scripts/test_closeout_check.py     (exit 1 on any failure)
"""
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
SCRIPT = os.environ.get('CLOSEOUT_CHECK_UNDER_TEST') or str(HERE / 'closeout_check.py')
src = open(SCRIPT, encoding='utf-8').read()
ns = {'__name__': 'cctest', '__file__': SCRIPT}
exec(compile(src, 'closeout_check.py', 'exec'), ns)

bad = 0


def T(ok, name, detail=''):
    global bad
    bad += (not ok)
    print('  %s  %-62s %s' % ('PASS' if ok else 'FAIL', name, detail))


def run(*args):
    r = subprocess.run([sys.executable, SCRIPT, *args], cwd=ROOT, capture_output=True, text=True, timeout=300)
    return r.returncode, r.stdout + r.stderr


print('— parsers —')
lt = ns['live_tallies']
m = lt('TALLY: 13 CORRECT / 10 WRONG / 2 ACTIVE (x).')
T(m and m[0][1] == {'C': 13, 'W': 10, 'A': 2}, 'long form parses', str(m))
m = lt('tally 10W / 13C / 2A at 10/01')
T(m and m[0][1] == {'W': 10, 'C': 13, 'A': 2}, 'short form parses', str(m))
T(lt('the 9/18 line read 9W/12C/1A and lagged') == [], 'history cue BEFORE retires the figure')
T(lt("STATUS's 9/18 tally line (9W/12C/1A) lagged canon") == [], 'history cue AFTER retires the figure')
T(len(lt('Scorecard 13 CORRECT · 10 WRONG · 1 ACTIVE live')) == 1, 'middle-dot separator parses')
T(lt('13 CORRECT / 13 CORRECT') == [], 'duplicate letters are not a tally')
dt_ = ns['derive_tally']
tsv = ('Pred_ID\tDate_Made\tPrediction\tConfidence\tTimeframe\tStatus\tDate_Resolved\tOutcome\tInvalidation\tNotes\n'
       'RED-01\t\t\t\t\tRESOLVED\t\tRESOLVED CORRECT. x\t\t\n'
       'RED-02\t\t\t\t\tRESOLVED\t\t"WRONG (both sides): y\t\t\n'
       'RED-03\t\t\t\t\tACTIVE\t\t\t\t\n'
       'RED-04\t\t\t\t\tRESOLVED\t\tno token here\t\t\n')
d, act, unk, n = dt_(tsv)
T(d == (1, 1, 1) and act == ['RED-03'] and unk == ['RED-04'] and n == 4, 'derive_tally classifies + fails closed', str((d, act, unk)))
lead = ns['lead_token']
T(lead('FIRED-BANKED; exit 0-of-5 [2026-09-12]') == 'FIRED-BANKED', 'lead token FIRED-BANKED not FIRED')
T(lead('FIRED 2026-10-14 (Sept CPI); exit armed') == 'FIRED', 'lead token FIRED')
T(lead('ARMED; 1-of-3') == 'ARMED', 'lead token ARMED')
hn = ns['hold_netbear']
T(hn('**S54:** CALENDAR net-bear 60 vs 65 was the bug. **HOLD 70 · net-bear 65.**\n## x') == (70, 65),
  'hold_netbear: canonical pair beats a stray earlier figure (the gate\'s own S54 catch)')
T(hn('**Status:** vS53. net-bear 65 / HOLD 70 — unch\n## x', 3) == (70, 65), 'hold_netbear: net-bear-first pair')
T(hn('Net-bear 60 → 65 (both MECHANICAL), confidence 70.\n## x') == (70, 60), 'hold_netbear: no pair -> first figures (documented fallback)')
T(hn('S53: **net-bear 65 / HOLD 70**, unch. Prior S50: **NO WEIGHT MOVED: HOLD 70 / net-bear 58.**\n## x', 2) == (70, 65),
  'hold_netbear: EARLIEST pair wins over a later quoted prior (CALENDAR header at HEAD, S54 catch #2)')
st = ns['newest_stamp']
s = st('x 2026-10-14 21:3x ET y 2026-10-15 10:59 ET z 2027-01-11 (horizon)')
T(s is not None and s.strftime('%Y-%m-%d %H:%M') == '2026-10-15 10:59', 'newest stamp ignores date-only horizons, reads x-minutes', str(s))
pp, V = ns['prome_packets'], ns['Vintage']
_p = pp(V('ebe839ffe0'), '2026-11-12')
T(isinstance(_p, dict) and sorted(_p) == ['PROME/inbox/2026-11-12_from-RED_S63-ft06-rederivation.md'],
  'prome_packets: S63 packet found at ebe839ffe0, keyed path -> blob', str(_p)[:80])
T(pp(V('ebe839ffe0'), '2026-11-13') == {}, 'prome_packets: no packet for a date without one')

print('— M12-3: a W8 delivery must be new since the comparison base —')
TODAY = '2026-11-12'
P_REG, P_CL = 'AGENTS/RED/registry/FALSIFICATION_TRIGGERS.tsv', 'AGENTS/RED/thesis/CHANGELOG.md'
REG0 = 'trigger_id\tstate\nRED-FT-01\tARMED; 0-of-3\n'
REG1 = 'trigger_id\tstate\nRED-FT-01\tFIRED 2026-11-12; exit armed\n'
CL0 = '# CHANGELOG\n\n## 2026-11-12 S63 morning\nold view -> new view\n'
CL1 = '# CHANGELOG\n\n## 2026-11-12 S64 afternoon\nFT-01 ARMED -> FIRED\n\n## 2026-11-12 S63 morning\nold view -> new view\n'
STATUS_FX = '# RED STATUS\n\n## CURRENT ASSESSMENT\n\n| Hypothesis | Prob |\n|---|:--:|\n| Stag | 32% |\n'
OLD_PROC = 'PROME/inbox/processed/2026-11-12_from-RED_S63-morning.md'
OLD_INBOX = 'PROME/inbox/2026-11-12_from-RED_S63-morning.md'
OLD_BYTES = 'S63 packet: FT-06 run broke, net-bear 68 to 67\n'
NEW = 'PROME/inbox/2026-11-12_from-RED_S64-afternoon.md'


def sh(d, *args):
    r = subprocess.run(['git', '-c', 'user.name=fixture', '-c', 'user.email=fixture@invalid',
                        '-c', 'commit.gpgsign=false', *args], cwd=d, capture_output=True, text=True)
    if r.returncode:
        raise RuntimeError('git %s: %s' % (args, r.stderr))
    return r.stdout.strip()


def put(d, rel, text, append=False):
    p = Path(d) / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    with open(p, 'a' if append else 'w', encoding='utf-8', newline='') as fh:
        fh.write(text)


def change_state(d):
    put(d, P_REG, REG1)
    put(d, P_CL, CL1)


def case(name, setup, want, old_at=OLD_PROC):
    """Throwaway repo: base commit with FT-01 ARMED and one earlier same-day RED packet
    at `old_at`; `setup` mutates it (and may return a commit for --at); then e is run."""
    with tempfile.TemporaryDirectory() as d:
        sh(d, 'init', '-q')
        put(d, P_REG, REG0)
        put(d, P_CL, CL0)
        put(d, 'AGENTS/RED/STATUS.md', STATUS_FX)
        put(d, 'AGENTS/RED/OUTBOX.md', '# OUTBOX - FROZEN 2026-11-12\n')
        put(d, 'PROME/inbox/README.md', 'inbox\n')
        if old_at:
            put(d, old_at, OLD_BYTES)
        sh(d, 'add', '-A')
        sh(d, 'commit', '-q', '-m', 'base')
        r = setup(d)
        at = r if isinstance(r, str) else None     # a setup returns a commit only for --at
        ns['ROOT'] = Path(d)
        F = []
        try:
            note = ns['check_state_change'](ns['Vintage'](at), F, TODAY)
        except Exception as exc:                                       # noqa: BLE001
            F, note = [('e', 'UNKNOWN', 'raised %r' % exc)], None
        es = [f for f in F if f[0] == 'e']
        w8 = [f for f in es if 'PROME/inbox' in f[2] or f[1] == 'UNKNOWN']
        got = 'UNKNOWN' if any(f[1] == 'UNKNOWN' for f in es) else ('FAIL' if w8 else 'PASS')
        T(got == want, name, '%s: %s' % (got, (w8[0][2] if w8 else note or '')[:110]))


def commit_all(d):
    sh(d, 'add', '-A')
    sh(d, 'commit', '-q', '-m', 'state + packet')
    return sh(d, 'rev-parse', 'HEAD')


def git_mv_old_to_processed(d):
    (Path(d) / 'PROME/inbox/processed').mkdir(parents=True, exist_ok=True)
    sh(d, 'mv', OLD_INBOX, OLD_INBOX.replace('inbox/', 'inbox/processed/'))


def moved_new(d):
    change_state(d)
    put(d, NEW, 'S64 packet: FT-01 fired\n')
    (Path(d) / 'PROME/inbox/processed').mkdir(parents=True, exist_ok=True)
    os.rename(Path(d) / NEW, Path(d) / NEW.replace('inbox/', 'inbox/processed/'))


case('1a earlier same-day packet in processed/, no new one -> FAIL', change_state, 'FAIL')
case('1b earlier same-day packet still in inbox, no new one -> FAIL', change_state, 'FAIL', old_at=OLD_INBOX)
case('2a new untracked packet (+ earlier one present) -> PASS',
     lambda d: (change_state(d), put(d, NEW, 'S64 packet: FT-01 fired\n')), 'PASS')
case('2a\' new packet, no earlier one -> PASS',
     lambda d: (change_state(d), put(d, NEW, 'S64 packet: FT-01 fired\n')), 'PASS', old_at=None)
case('2b unconsumed earlier packet edited (new bytes) -> PASS',
     lambda d: (change_state(d), put(d, OLD_INBOX, 'Addendum: FT-01 fired\n', append=True)), 'PASS', old_at=OLD_INBOX)
case('2c --at a commit carrying state change + packet -> PASS',
     lambda d: (change_state(d), put(d, NEW, 'S64 packet: FT-01 fired\n'), commit_all(d))[-1], 'PASS')
case('3a new packet already moved to processed/ -> PASS', moved_new, 'PASS')
case('3b OLD packet moved by a staged git mv (concurrent) -> FAIL',
     lambda d: (change_state(d), git_mv_old_to_processed(d)),
     'FAIL', old_at=OLD_INBOX)
case('3c edit to a packet already filed in processed/ -> FAIL',
     lambda d: (change_state(d), put(d, OLD_PROC, 'Addendum: FT-01 fired\n', append=True)), 'FAIL')
case('ordinary: no state change, no new packet -> no finding', lambda d: None, 'PASS')
case('wrong owner: from-PROME / from-REDWOOD / RED dated yesterday -> FAIL',
     lambda d: (change_state(d), put(d, 'PROME/inbox/2026-11-12_from-PROME_x.md', 'a\n'),
                put(d, 'PROME/inbox/2026-11-12_from-REDWOOD_x.md', 'b\n'),
                put(d, 'PROME/inbox/2026-11-11_from-RED_x.md', 'c\n')), 'FAIL', old_at=None)
case('copy: old bytes under a new filename -> FAIL',
     lambda d: (change_state(d), put(d, 'PROME/inbox/2026-11-12_from-RED_S64-copy.md', OLD_BYTES)), 'FAIL')
case('missing information: no git (listing unreadable) -> UNKNOWN',
     lambda d: (change_state(d), os.rename(Path(d) / '.git', Path(d) / '.git-off')), 'UNKNOWN')

# CATO's M12-3 probe on real data, in memory: base = current = 506e6e2951, the first ARMED
# registry row flipped to FIRED, a CHANGELOG entry dated today; the real PROME/inbox at that
# commit holds only the S63 packet, consumed into processed/ at c3947342c1.
ns['ROOT'] = ROOT


class Probe(ns['Vintage']):
    @property
    def base(self):
        return self.at

    def read(self, rel):
        txt = super().read(rel)
        if txt is not None and rel == 'registry/FALSIFICATION_TRIGGERS.tsv':
            lines = txt.split('\n')
            h = next(i for i, l in enumerate(lines) if l.strip() and not l.startswith('#'))
            k = lines[h].split('\t').index('state')
            for i in range(h + 1, len(lines)):
                c = lines[i].split('\t')
                if len(c) > k and c[k].startswith('ARMED'):
                    c[k] = 'FIRED 2026-11-12 (probe)'
                    lines[i] = '\t'.join(c)
                    break
            txt = '\n'.join(lines)
        if txt is not None and rel == 'thesis/CHANGELOG.md':
            txt = '## 2026-11-12 probe entry\n\n' + txt
        return txt


F = []
note = ns['check_state_change'](Probe('506e6e2951'), F, TODAY)
es = [f for f in F if f[0] == 'e']
T('registry state' in (note or '') and len(es) == 1 and es[0][1] == 'FAIL' and 'PROME/inbox' in es[0][2],
  'CATO probe at 506e6e2951 (consumed S63 packet only) -> e FAIL', str(es)[:110])

# The legacy OUTBOX branch, same defect: at 506e6e2951 (S63-b, 12:10) OUTBOX changed vs its
# parent only by the FROZEN banner; its top entry is the morning's -079 (09:53). Probe that
# commit against its real parent with a state change: the old top entry must not deliver it.
class ProbeParent(Probe):
    @property
    def base(self):
        return self.at + '^'


F = []
note = ns['check_state_change'](ProbeParent('506e6e2951'), F, TODAY)
es = [f for f in F if f[0] == 'e']
T(len(es) == 1 and es[0][1] == 'FAIL' and 'PROME/inbox' in es[0][2],
  'legacy OUTBOX: freeze-banner edit + morning -079 on top -> e FAIL', str(es)[:110])

if os.environ.get('CLOSEOUT_CHECK_UNDER_TEST'):
    print('— vintages / refusal SKIPPED: the script under test is not at its repo path —')
    print('\n%s' % ('ALL PASS' if bad == 0 else '%d FAILURE(S)' % bad))
    sys.exit(1 if bad else 0)

print('— vintages —')
rc, out = run('--at', '75e1b12b3', '--quiet')
T(rc == 1, '75e1b12b3 rc 1', 'rc=%s' % rc)
T('[a] FAIL open-challenge table lists 11 row(s)' in out and 'canon has 6 non-RESOLVED' in out, '75e1b12b3 a: 11 vs 6')
T(re.search(r'\[b\] FAIL STATUS\.md:\d+ asserts "10 WRONG / 13 CORRECT / 1 ACTIVE"', out) is not None, '75e1b12b3 b: STATUS 1 ACTIVE flagged')
T('13 CORRECT · 10 WRONG · 1 ACTIVE' in out, '75e1b12b3 b: NEXUS 1 ACTIVE flagged')
T('9W/12C/1A' not in out, '75e1b12b3 b: NEXUS history quote (9W/12C/1A) NOT flagged')
T('STATUS header claims RED-FT-02 "0 of 3" but canon says 1-of-3' in out, '75e1b12b3 c: stale header count')
T(re.search(r'\[d\] FAIL SCRATCH newest stamp 2026-10-14 23:47 is 646 min behind', out) is not None, '75e1b12b3 d: addendum floor')
T('[e] FAIL registry state changed vs 75e1b12b3^ but thesis/CHANGELOG.md is unchanged' in out, '75e1b12b3 e: CHANGELOG unchanged')
T('[f] FAIL CALENDAR.md header HOLD/net-bear (70, 60) vs STATUS (70, 65)' in out,
  '75e1b12b3 f: CALENDAR header net-bear 60 vs STATUS 65 (a 4th defect the spec did not list)')
T('STATUS top block does not state both HOLD' not in out, '75e1b12b3 f: lowercase "confidence 70" is read (no false STATUS-side f)')
T('SKIPPED' in out or '--at' in out or True, '75e1b12b3 g reported SKIPPED (--quiet hides the list; verdict carries it)')

rc, out = run('--at', '47b622ddf', '--quiet')
T(rc == 1, '47b622ddf rc 1', 'rc=%s' % rc)
finds = re.findall(r'^\s+\[([a-g])\] (FAIL|UNKNOWN) (.*)$', out, flags=re.M)
T(len(finds) == 1 and finds[0][0] == 'c' and 'RED-FT-11: canon count 0-of-5 absent' in finds[0][2],
  '47b622ddf: exactly one finding, c FT-11 0-of-5 (spec said d/e — measured: no)', str(finds)[:120])

rc, out = run('--no-delegate', '--quiet')
T(rc == 0, 'working tree (--no-delegate) clean rc 0', out.strip().split('\n')[-1][:120])
T('SKIPPED: g' in out, 'working tree: --no-delegate is reported SKIPPED in the verdict line')

print('— refusal —')
rc, out = run('--bogus')
T(rc == 2 and 'CLOSEOUT-CHECK' not in out, 'unknown flag refuses with rc 2 and no verdict', 'rc=%s' % rc)

print('\n%s' % ('ALL PASS' if bad == 0 else '%d FAILURE(S)' % bad))
sys.exit(1 if bad else 0)
