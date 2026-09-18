#!/usr/bin/env python3
"""Pinned offline review probes. Reproduces historical behavior, not repair acceptance."""
import contextlib, datetime as dt, io, subprocess, types, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
REV="a2522254c"
sys.dont_write_bytecode=True
m=types.ModuleType("review_roll")
m.__file__=str(ROOT/"AGENTS/SAM/scripts/oil_roll_check.py")
exec(compile(subprocess.check_output(["git","show",REV+":AGENTS/SAM/scripts/oil_roll_check.py"],cwd=ROOT),m.__file__,"exec"),m.__dict__)
a,b,c,d=[dt.date(2026,9,x) for x in (15,16,17,18)]
nov={a:100.,b:101.,c:102.,d:103.}
dec={a:90.,b:91.,c:92.,d:93.}
for label,cont,expected in [
 ("complete_no_roll",nov,0),
 ("complete_roll",{a:100.,b:101.,c:92.,d:93.},2),
 ("missing_end_hides_roll",{a:100.,b:101.},0),
 ("single_observation",{a:100.},0),
 ("missing_middle",{a:100.,d:103.},0),
]:
 fixtures={"BZ=F":cont,"BZX26.NYM":nov,"BZZ26.NYM":dec}
 m.closes=lambda symbol,start,end: fixtures.get(symbol,{})
 out=io.StringIO()
 with contextlib.redirect_stdout(out): rc=m.check("BZ=F",a,d)
 print(label,"requested",a,d,"rc",rc)
 print(out.getvalue().strip())
 assert rc==expected
h=types.ModuleType("review_hook");h.__file__=str(ROOT/"PROME/tools/hooks/commit_subject_guard.py")
exec(compile(subprocess.check_output(["git","show",REV+":PROME/tools/hooks/commit_subject_guard.py"],cwd=ROOT),h.__file__,"exec"),h.__dict__)
for prefix in ["","echo ","command -v ","env printf %s ","timeout 1 echo "]:
 verdict=h.diagnose(prefix+'git commit -m "'+'x'*101+'"')[0]
 print("HOOK",repr(prefix),verdict)
 assert verdict==("allow" if prefix=="echo " else "block")
print("Historical counterexamples reproduced; exit zero is NOT repair acceptance.")
