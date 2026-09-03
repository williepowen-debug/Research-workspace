#!/usr/bin/env python3
"""
⛔ RETIRED 2026-09-02 — DO NOT WIRE THIS INTO THE BOOT SEQUENCE.

Disposition of DAEDALUS's 2026-08-28 wiring-sweep item 3 ("orphaned tool,
PAT-108 writer-with-no-reader, boot edition") and CREED SCRATCH deferred
item 10. The choice offered was wire / fix the keying / retire with a note.
RETIRE, for one reason that is a rule and not a preference:

  Its staleness checks key on os.path.getmtime. Root CLAUDE.md § Data Hygiene
  says NEVER key a NEW freshness mechanism on mtime — git sync restamps it, so
  it fails FALSE-NEGATIVE (reads FRESH after a pull). Wiring it would install a
  known-broken freshness check into the boot path, which is worse than the
  orphan it currently is.

Every check it performed is already done, correctly keyed, elsewhere in
CLAUDE.md's boot sequence:
  · workbook staleness  -> boot step 7's `find -mtime` (advisory, and the
    content-vintage authority is scripts/ledger_staleness.py, which reads the
    PAT-044 "Last real data refresh:" header FIRST)
  · prediction resolve dates -> boot step 4b
  · threshold/band scan      -> boot step 4c, scripts/threshold_scan.py
  · corrections register     -> boot step 7b
This file is kept for its source trail only. It is not run and must not be
cited as a check that ran.
"""

"""
CREED Boot Check — the mechanical half of the boot sequence.

CREED is Tier-2 spawn-on-need: sessions are far apart and the expensive failure
is not "stale data" (that is the expected steady state) but *not knowing what
went stale while CREED was dark*. This script answers that in ~1 second.

Deliberately does NOT pull market data. Prices must be live and pulled at the
moment of use (root CLAUDE.md rule 4) — baking a price into a boot script
invites citing a cached level. Use FORGE/tools/market-data/fetch.py for that.

Usage:
  python3 AGENTS/CREED/scripts/boot.py

Adopted 2026-07-27 from REGINALD/scripts/boot.py (orchestrator pattern), scoped
down to what a spawn-on-need agent actually needs at wake.
"""

import csv
import io
import os
import subprocess
import sys
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
CREED = os.path.dirname(HERE)
ROOT = os.path.dirname(os.path.dirname(CREED))

VX_STALE_DAYS = 14          # matches the CLAUDE.md boot staleness rule
STATUS_CAP = 320            # matches the CLAUDE.md split trigger

RED, YEL, GRN, DIM, RST = "\033[31m", "\033[33m", "\033[32m", "\033[2m", "\033[0m"
if not sys.stdout.isatty():
    RED = YEL = GRN = DIM = RST = ""

findings = []   # (severity, message) — severity: 2=act, 1=note, 0=ok


def add(sev, msg):
    findings.append((sev, msg))


def age_days(path):
    try:
        return (datetime.now() - datetime.fromtimestamp(os.path.getmtime(path))).days
    except OSError:
        return None


def hdr(t):
    print(f"\n{t}\n" + "-" * len(t))


# ---------------------------------------------------------------- 1. workbook
def check_workbook():
    hdr("1. WORKBOOK STALENESS")
    wb = os.path.join(CREED, "workbook")
    stale = []
    for f in sorted(os.listdir(wb)):
        if not f.endswith(".tsv"):
            continue
        d = age_days(os.path.join(wb, f))
        mark = f"{RED}STALE{RST}" if d is not None and d > VX_STALE_DAYS else f"{GRN}ok{RST}"
        print(f"  {f:24s} {d:>4}d  {mark}")
        if d is not None and d > VX_STALE_DAYS:
            stale.append(f"{f} ({d}d)")
    if stale:
        add(2, "VX stale: " + ", ".join(stale) +
               " — refresh the latest monthly CMBS/SS print + REIT tape BEFORE citing any workbook value.")
    else:
        print(f"  {DIM}(Tier-2 note: staleness between spawns is the expected steady state, "
              f"not neglect. The alert exists to force a refresh before citing.){RST}")


# ------------------------------------------------------------- 2. predictions
def check_predictions():
    hdr("2. PREDICTIONS — resolve-date scan (run at BOOT, not closeout)")
    p = os.path.join(CREED, "workbook", "PREDICTIONS.tsv")
    today = datetime.now(timezone.utc).date()
    rows = [r for r in csv.DictReader(
        (l for l in io.open(p, encoding="utf-8") if not l.startswith("#")), delimiter="\t")]
    overdue = opened = 0
    for r in rows:
        if (r.get("Status") or "").strip().upper() != "OPEN":
            continue
        opened += 1
        tf = (r.get("Timeframe") or "").strip()
        due = None
        for tok in tf.replace("by ", "").split():
            try:
                due = datetime.strptime(tok, "%Y-%m-%d").date()
                break
            except ValueError:
                pass
        if due and due < today:
            overdue += 1
            add(2, f"{r['Pred_ID']} is PAST its timeframe ({tf}) and still Status=OPEN — "
                   f"grade it, or mark STUCK if the instrument is unavailable.")
            print(f"  {RED}OVERDUE{RST} {r['Pred_ID']}  {tf}")
        else:
            print(f"  {DIM}open   {r['Pred_ID']}  {tf}  -> {(r.get('Resolves_On') or '')[:58]}{RST}")
    print(f"\n  {opened} open, {overdue} overdue.")
    if overdue:
        add(1, "Reminder: update PREDICTIONS.tsv AND workbook/PREDICTIONS_SCOREBOARD.md "
               "in the SAME session — both writes, or neither counts.")


# ------------------------------------------------- 3. closeout-skip detector
def check_closeout_skew():
    hdr("3. CLOSEOUT-SKIP DETECTOR")
    s, lc = os.path.join(CREED, "STATUS.md"), os.path.join(CREED, "LAST_COMPLETION.md")
    ds, dl = age_days(s), age_days(lc)
    print(f"  STATUS.md          {ds:>4}d")
    print(f"  LAST_COMPLETION.md {dl:>4}d")
    if ds is not None and dl is not None and (dl - ds) > 2:
        add(2, f"LAST_COMPLETION.md is {dl - ds}d older than STATUS.md — A CLOSEOUT WAS SKIPPED. "
               "Treat every claim in it as UNKNOWN, not current. "
               "(This is the exact failure that let a 7/4 claim survive two sessions and reach Will.)")
        print(f"  {RED}SKEW: a closeout was skipped.{RST}")
    else:
        print(f"  {GRN}ok{RST}")


# ------------------------------------------------------------------- 4. mail
def check_mail():
    hdr("4. MAIL")
    total = 0
    for lane, path in (("inbox/", os.path.join(CREED, "inbox")),
                       ("inbox/WALTER/", os.path.join(CREED, "inbox", "WALTER"))):
        n = len([f for f in os.listdir(path) if f.endswith(".md")]) if os.path.isdir(path) else 0
        total += n
        print(f"  {lane:16s} {n} unprocessed")
    if total:
        add(2, f"{total} unprocessed mail item(s). Clear the inbox BEFORE new research — "
               "an unprocessed inbox routinely carries live state the canonical surfaces do not reflect. "
               "Log each to board_log.tsv at READ time.")
    else:
        print(f"  {GRN}both lanes clean{RST}")


# ----------------------------------------------------------------- 5. hygiene
def check_hygiene():
    hdr("5. HYGIENE")
    n = sum(1 for _ in io.open(os.path.join(CREED, "STATUS.md"), encoding="utf-8"))
    print(f"  STATUS.md {n} lines (target 300 / split trigger {STATUS_CAP})")
    if n > STATUS_CAP:
        add(1, f"STATUS.md is {n} lines, over the {STATUS_CAP} split trigger — when you add this "
               "session's catch-up section, archive the OLDEST one to archive/STATUS_CATCHUPS_*.md.")
    try:
        d = subprocess.run(["git", "status", "--short", "--", "AGENTS/CREED/"],
                           cwd=ROOT, capture_output=True, text=True, timeout=15).stdout.strip()
        print(f"  git: {'clean' if not d else str(len(d.splitlines())) + ' file(s) dirty'}")
        if d:
            for l in d.splitlines()[:12]:
                print(f"    {DIM}{l}{RST}")
            add(1, "Uncommitted CREED files present at boot — likely an interrupted session. "
                   "Read SCRATCH.md and reconcile before overwriting anything.")
    except Exception as e:
        print(f"  {DIM}git check skipped: {e}{RST}")


def main():
    print("=" * 72)
    print(f"CREED BOOT CHECK — {datetime.now():%Y-%m-%d %H:%M %Z} ({datetime.now():%A})")
    print("=" * 72)
    for fn in (check_workbook, check_predictions, check_closeout_skew, check_mail, check_hygiene):
        try:
            fn()
        except Exception as e:
            add(1, f"{fn.__name__} failed: {e}")
            print(f"  {RED}check failed: {e}{RST}")

    hdr("ACTION SUMMARY")
    act = [m for s, m in findings if s == 2]
    note = [m for s, m in findings if s == 1]
    if not act and not note:
        print(f"  {GRN}Nothing owed mechanically. Proceed to the rails.{RST}")
    for m in act:
        print(f"  {RED}[ACT] {RST}{m}")
    for m in note:
        print(f"  {YEL}[NOTE]{RST} {m}")
    print(f"\n{DIM}This script checks MECHANICS only. It does not read the rails and it does not"
          f"\npull prices — prices must be live at the moment of use. Boot order: SCRATCH.md ->"
          f"\nCLAUDE.md -> STATUS.md -> rails.{RST}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
