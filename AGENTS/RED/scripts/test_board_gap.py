#!/usr/bin/env python3
"""Falsification set for boot.py section (5), the BOARD-disposition gap.

Written S44 2026-09-12 with the rebuild of that section, after the previous
implementation reported GREEN while 27 action-addressed signals sat unlogged
(oldest 154 days). Per the repair-completion rule the tests are the ACCEPTANCE
CONDITIONS, not a replay of the reproduction:

  routing forms  - both keys (`action:` and legacy `to:`) in all three value
                   forms the corpus actually uses (bracketed, bare, annotated)
  WRONG OWNER    - a signal addressed to another desk must not flag RED
  substring      - RED must match as a whole token, never inside REDACTED
  MISSING INFO   - a file with no routing key at all must not flag
  REGRESSION     - the header row must never be read as data (defect 1: the
                   literal "timestamp_read" sorts above every date and pinned
                   the gate green unconditionally)
  OVERLAP        - an id dispositioned only in a ROTATED ARCHIVE must count as
                   logged (defect 3: a live-file-only reader re-flags all 36)

  CONCURRENT ACTIVITY - N/A, justified: the section is read-only and a row
  appended by another session mid-run can only make the count stale by one,
  never wrong in direction.

Run:  python3 AGENTS/RED/scripts/test_board_gap.py     (exit 1 on any failure)
"""
import sys, re
src=open('/home/willi/Research-workspace/AGENTS/RED/scripts/boot.py').read()
src=src.replace('\n_ensure_venv()\n','\n\n')
ns={'__name__':'rbtest','__file__':'/home/willi/Research-workspace/AGENTS/RED/scripts/boot.py'}
exec(compile(src,'boot.py','exec'), ns)
f=ns['_red_addressed']
T=[('bracket quoted','action: ["RED", "VIOLET"]\n',True),
 ('bracket bare','action: [RED, VIOLET]\n',True),
 ('legacy to bracket','to: [RED]\n',True),
 ('legacy to bare','to: RED\n',True),
 ('annotated form','to: RED (counter-evidence), HENRY\n',True),
 ('WRONG OWNER only','action: ["VIOLET", "HENRY"]\n',False),
 ('substring REDACTED','action: [REDACTED]\n',False),
 ('substring REGINALD','action: ["REGINALD"]\n',False),
 ('info-only not action','info: ["RED"]\n',False),
 ('no routing key','entities: [RED-FT-10]\n',False),
 ('lowercase red','action: [red]\n',True)]
bad=0
for name,txt,exp in T:
    got=f(txt); ok=got==exp; bad+=(not ok)
    print(f"  {'PASS' if ok else 'FAIL'}  {name:22} -> {got} (expect {exp})")
ids,ledgers=ns['_logged_ids']()
r1 = not any('timestamp' in i for i in ids)
r2 = len(ledgers)==3
live=set(re.findall(r'SIG-W-\d{8}-\d{3}', open('/home/willi/Research-workspace/AGENTS/RED/board_log.tsv').read()))
r3 = bool(ids-live)
print(f"\n  {'PASS' if r1 else 'FAIL'}  REGRESSION: header row never enters the id set ({len(ids)} ids)")
print(f"  {'PASS' if r2 else 'FAIL'}  all three ledgers read (live + 2 archives)")
print(f"  {'PASS' if r3 else 'FAIL'}  OVERLAP: {len(ids-live)} ids logged ONLY in an archive count as logged")
bad += (not r1)+(not r2)+(not r3)
print(f"\n{'ALL PASS (14/14)' if bad==0 else str(bad)+' FAILURES'}")
sys.exit(1 if bad else 0)
