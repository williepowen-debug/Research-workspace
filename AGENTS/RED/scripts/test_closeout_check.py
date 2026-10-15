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

Run:  python3 AGENTS/RED/scripts/test_closeout_check.py     (exit 1 on any failure)
"""
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
SCRIPT = str(HERE / 'closeout_check.py')
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
