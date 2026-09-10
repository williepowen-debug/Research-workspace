#!/usr/bin/env python3
"""
BOND — MISSING-WATCHER CHECKS  (built 2026-08-20, Will-directed)

WHY THIS EXISTS
---------------
On 2026-08-20 three independent reviews (BOND's own boot, PROME's oversight
pass, DAEDALUS's Will-directed structure review) each found a different defect,
and all four instances turned out to be ONE class:

    a state change with NO PUBLISHER.

A LEVEL gate announces itself, because something recomputes it every boot.
Nothing was watching:

  * a fired TRIGGER against its vector's registered text   VX-BND-16   1 day
  * a CALENDAR against a position's expiry                 60-DTE     19 days
  * a RETIREMENT against the cells still citing it         VX-01 tail 23 days
  * a LEVEL FIX against the distances derived from it      33/88/71bp weeks

boot_recompute covers only the first kind of input (levels). This module adds
the three tractable watchers. The fourth (fired trigger vs vector text) needs
event semantics and is deliberately NOT attempted here — it is DAEDALUS's
shared check. It was also the CHEAPEST of the four, which is the whole point:
tractability and cost are unrelated.

SCOPE — READ BEFORE TRUSTING A CLEAN PASS
-----------------------------------------
Watchers A and B are REGISTRY-DRIVEN. They see exactly what is declared in
WATCH_DATES.tsv and RETIRED_TOKENS.tsv and NOTHING else. An undeclared expiry
or an unregistered retirement is invisible BY CONSTRUCTION — which is the same
failure mode as the missing docket row that let the August refunding run
ungraded. A clean pass means "nothing DECLARED has fired", never "nothing has
fired". Adding the registry row IS the work; the check is the cheap part.

rc: 0 clean · 1 finding (NOT a pass) — a finding is a prompt to LOOK.
"""
import re
import sys
import csv
from datetime import date, datetime
from pathlib import Path

HERE = Path(__file__).resolve().parent
AGENT = HERE.parent

# Live surfaces. Deliberately excludes analysis/, domain/sources/, inbox/,
# outbox/ and archive/ -- those are DATED RECORDS and correcting them destroys
# history (learned 2026-08-20 on a July pre-registration snapshot).
LIVE = ["STATUS.md", "TRADE.md", "NEXUS_BRIEF.md", "SCRATCH.md", "THESIS.md",
        "PROTOCOL.md", "thesis/THESIS.md", "workbook/VX.tsv", "workbook/FLOW.tsv",
        "monitors/AUCTION_HEALTH.md", "monitors/DEALER_CAPACITY.md",
        "monitors/CDX_CASH_BASIS.md", "monitors/CREDIT_PRIMARY_MARKET.md"]


def _live_files():
    for rel in LIVE:
        p = AGENT / rel
        if p.exists():
            yield rel, p.read_text(encoding="utf-8", errors="replace")


# Supersession is a BLOCK property, not a line property. A retained-verbatim
# table row under a "SUPERSEDED" banner carries no guard words of its own, but
# it is plainly not a live claim. Found on this checker's FIRST live run
# (2026-08-20) -- the doc was right and the check was wrong.
BLOCK_GUARD = ("superseded", "retained verbatim", "retained]", "historical",
               "not live", "archive", "as published", "prior version",
               "kill-on-sight", "record of how", "no longer current")


def _guarded_block_lines(text):
    """Line numbers (1-based) sitting under a heading that marks the block dead."""
    out, dead = set(), False
    for i, line in enumerate(text.splitlines(), 1):
        stripped = line.lstrip("> ").rstrip()
        if stripped.startswith("#"):
            dead = any(g in stripped.lower() for g in BLOCK_GUARD)
        elif dead:
            out.add(i)
    return out


def _rows(name):
    p = HERE / name
    if not p.exists():
        return []
    with p.open(encoding="utf-8") as f:
        return list(csv.DictReader(f, delimiter="\t"))


# ---------------------------------------------------------------- watcher A
def check_dates(today=None, rows=None):
    """DATE-GATE: a checkpoint fires on the CALENDAR and nothing watches it."""
    today = today or date.today()
    rows = rows if rows is not None else _rows("WATCH_DATES.tsv")
    out = []
    for r in rows:
        try:
            d = datetime.strptime(r["Date"].strip(), "%Y-%m-%d").date()
        except (ValueError, KeyError):
            out.append(("BAD-ROW", r.get("Label", "?"), "unparseable Date"))
            continue
        off = int(r.get("Checkpoint_Offset_Days") or 0)
        days = (d - today).days
        if off and not (r.get("Serviced_On") or "").strip():
            cp = date.fromordinal(d.toordinal() - off)
            if today >= cp:
                out.append(("CHECKPOINT-CROSSED", r["Label"],
                            f"{off}-day checkpoint fell {cp} ({(today-cp).days}d ago); "
                            f"{days}d to {d}"))
        if 0 <= days <= 3:
            out.append(("IMMINENT", r["Label"], f"{days}d away ({d})"))
        elif days < 0:
            out.append(("PASSED", r["Label"], f"{-days}d ago ({d}) — resolve or retire the row"))
    return out


# ---------------------------------------------------------------- watcher B
def check_retired(files=None, rows=None):
    """RETIREMENT: retiring a metric is a side effect nothing announces."""
    rows = rows if rows is not None else _rows("RETIRED_TOKENS.tsv")
    files = files if files is not None else list(_live_files())
    out = []
    for r in rows:
        tok = r["Token"].strip().lower()
        guards = [g.strip().lower() for g in (r.get("Guard_Words") or "").split(";") if g.strip()]
        for rel, text in files:
            dead = _guarded_block_lines(text)
            for i, line in enumerate(text.splitlines(), 1):
                low = line.lower()
                if tok not in low:
                    continue
                if i in dead:
                    continue          # the whole BLOCK is marked superseded
                if any(g in low for g in guards):
                    continue          # the line is ABOUT the retirement
                out.append(("RETIRED-TOKEN-LIVE", f"{rel}:{i}",
                            f'"{r["Token"]}" (retired {r["Retired_On"]}) — {r["Reason"][:90]}'))
    return out


# ---------------------------------------------------------------- watcher C
# A stated distance is a DERIVED figure. It does not inherit a fix to the level
# beneath it, so it must be recomputed, never read.
DIST = re.compile(r"(\d+(?:\.\d+)?)\s*bp\s+(?:away|from|short of|below|above)", re.I)
CMP = re.compile(r"[<>≤≥]\s*$|above\s*$|below\s*$")   # a comparator means THRESHOLD, not mark
DGUARD = ("was ", "read \"", "carried", "until 8/", "corrected", "stale", "prior",
          "retract", "supersed", "no longer", "never inherit", "recomputed",
          "this cell", "this read", "this line", "off a stale", "off the 8/")


def check_distances(gates, files=None, tol=0.6):
    """gates: {label_substr: true_distance_bp}. Flag a stated distance that disagrees."""
    files = files if files is not None else list(_live_files())
    out = []
    for rel, text in files:
        dead = _guarded_block_lines(text)
        for i, line in enumerate(text.splitlines(), 1):
            low = line.lower()
            if i in dead:
                continue
            if any(g in low for g in DGUARD):
                continue
            for m in DIST.finditer(line):
                pre = line[:m.start()]
                if CMP.search(pre):
                    continue
                stated = float(m.group(1))
                for lab, true in gates.items():
                    if lab.lower() not in low:
                        continue
                    if abs(stated - true) > tol:
                        out.append(("DERIVED-DISTANCE-STALE", f"{rel}:{i}",
                                    f'says "{m.group(0).strip()}" for {lab}; '
                                    f"recomputed = {true:.0f}bp"))
                    break
    return out


def report(findings, title):
    print(f"\n   -- {title} --")
    if not findings:
        print("      ok  (nothing DECLARED fired — not a certificate; see module docstring)")
        return 0
    for kind, where, why in findings:
        print(f"      {kind:24} {where}")
        print(f"         {why}")
    return len(findings)


def run(gates=None, today=None):
    # IMMINENT rows are printed as a heads-up but do NOT count toward rc=1: a
    # gate that is 0-3 days away is exactly the state the registry exists to
    # produce, not a finding. (Until 2026-09-09 they were counted, so the boot
    # returned "unguarded drift" on the eve of every registered auction.)
    n = 0
    dates = check_dates(today=today)
    report(dates, "A · DATE-GATES (calendar vs a declared checkpoint)")
    n += len([f for f in dates if f[0] != "IMMINENT"])
    n += report(check_retired(), "B · RETIRED TOKENS (a retirement has no publisher)")
    if gates:
        n += report(check_distances(gates), "C · DERIVED DISTANCES (a distance never inherits a level fix)")
    return n


# ---------------------------------------------------------------- selftest
# Every fixture is a REAL defect this desk shipped, per the desk's convention.
def selftest():
    ok = True

    def chk(name, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print(f"   {'PASS' if good else 'FAIL':4}  {name}   (got {got}, want {want})")

    # A -- the 60-DTE miss: Sep-30 expiry, 60d checkpoint, graded on 8/20.
    rows = [{"Kind": "OPTION", "Label": "004", "Date": "2026-09-30",
             "Checkpoint_Offset_Days": "60", "Note": ""}]
    chk("A crossed checkpoint fires (60-DTE, 19d late)",
        len([f for f in check_dates(date(2026, 8, 20), rows) if f[0] == "CHECKPOINT-CROSSED"]), 1)
    chk("A same row silent BEFORE the checkpoint (7/16)",
        len(check_dates(date(2026, 7, 16), rows)), 0)

    # B -- VX-01's RED cell carried the retired tail for 23 days.
    tr = [{"Token": "tail >2", "Retired_On": "2026-07-28", "Reason": "unscoreable",
           "Guard_Words": "retired;unscoreable;history"}]
    chk("B retired tail in a live threshold cell fires",
        len(check_retired([("workbook/VX.tsv", "Th_R: BTC <2.3 with dealer spike, tail >2bps")], tr)), 1)
    chk("B the retirement ANNOUNCEMENT itself is guarded",
        len(check_retired([("STATUS.md", "the tail >2bp leg is RETIRED as unscoreable")], tr)), 0)

    tr2 = [{"Token": "series high", "Retired_On": "2026-08-20",
            "Reason": "no window stated", "Guard_Words": "retracted;wrong;correct label"}]

    # C -- TRADE.md said "7bp away" when DFII10 was 9bp off the 2.50 gate.
    g = {"DFII10": 9.0}
    chk("C stale distance fires (7bp stated, 9bp true)",
        len(check_distances(g, [("TRADE.md", "(a) DFII10 >2.5 sustained — the nearest gate, 7bp away;")])), 1)
    chk("C correct distance is silent",
        len(check_distances(g, [("STATUS.md", "DFII10 2.41 — 9bp away from the 2.50 add-gate")])), 0)
    chk("C a CORRECTION note about the stale figure is guarded",
        len(check_distances(g, [("TRADE.md", 'this cell read "7bp away" until 8/20; recomputed 9bp')])), 0)
    chk("C a THRESHOLD (comparator-preceded) is not a mark",
        len(check_distances({"DFII10": 9.0}, [("STATUS.md", "fires when DFII10 sits < 2bp away")])), 0)
    # BLOCK guard -- the first live run's own false positive (2026-08-20).
    sup = ("## SUPERSEDED LAYER - 7/24 vintage, NOT LIVE\n"
           "| DFII10 | 2.43 SERIES HIGH | 7bp from the 2.5 re-arm gate |\n")
    chk("BLOCK a retained row under a SUPERSEDED heading is guarded (retired token)",
        len(check_retired([("NEXUS_BRIEF.md", sup)], tr2)), 0)
    chk("BLOCK same row guarded for derived distance",
        len(check_distances({"DFII10": 9.0}, [("NEXUS_BRIEF.md", sup)])), 0)
    live = ("## Live rates state\n"
            "| DFII10 | 2.43 SERIES HIGH | 7bp from the 2.5 re-arm gate |\n")
    chk("BLOCK the SAME row under a LIVE heading still fires",
        len(check_distances({"DFII10": 9.0}, [("NEXUS_BRIEF.md", live)])), 1)

    print("\n   selftest:", "PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(selftest())
    sys.exit(1 if run(gates=None) else 0)
