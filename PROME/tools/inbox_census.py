#!/usr/bin/env python3
"""inbox_census.py — count a desk's UNCONSUMED inbox items the way the desk counts them (WQ-178, 2026-09-04).

Usage: python3 PROME/tools/inbox_census.py LABOR [SAM ...]     (repo-root or PROME/ cwd both fine)

Counts FILES only (never directory entries), at the top level of AGENTS/<DESK>/inbox/ and separately per lane
subdirectory (e.g. WALTER/), excluding any `processed/` directory at either level. PROME's own surface is
PROME/inbox/ at the repo root (never AGENTS/PROME/). rc 0 always; the numbers are the output.
Origin: 9/4 doorbells quoted every desk one high because `ls | grep -v processed | wc -l` counted the WALTER/ lane
directory as an item (BOND 3→2, VIOLET 7→6, LABOR 2→1+2-lane, SAM 1→0).
"""
import os, sys, subprocess

def root():
    return subprocess.run(["git","rev-parse","--show-toplevel"],capture_output=True,text=True).stdout.strip()

def census(desk):
    base = os.path.join(root(), "PROME", "inbox") if desk.upper()=="PROME" else os.path.join(root(), "AGENTS", desk.upper(), "inbox")
    if not os.path.isdir(base):
        return desk, None, {}
    top = sorted(f for f in os.listdir(base) if os.path.isfile(os.path.join(base,f)))
    lanes = {}
    for d in sorted(os.listdir(base)):
        dp = os.path.join(base,d)
        if os.path.isdir(dp) and d != "processed":
            lanes[d] = sorted(f for f in os.listdir(dp) if os.path.isfile(os.path.join(dp,f)))
    return desk, top, lanes

def main(argv):
    if not argv:
        print(__doc__); return 0
    for desk in argv:
        d, top, lanes = census(desk)
        if top is None:
            print(f"{d.upper():<10} inbox: NOT FOUND"); continue
        lane_s = " · ".join(f"{k}/ {len(v)}" for k,v in lanes.items()) or "no lanes"
        print(f"{d.upper():<10} top-level {len(top):>3} · {lane_s}   (files only; processed/ excluded)")
        for f in top: print(f"           - {f}")
        for k,v in lanes.items():
            for f in v: print(f"           - {k}/{f}")
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
