#!/usr/bin/env python3
"""coordination_scorecard.py — DOCKET L239 weekly coordination-value scorecard.

Owner: DAEDALUS. Raw input: PROME/state/ORCH_LOG.tsv (+ git for the delivery leg).

*** DESCRIPTIVE ONLY. NO SUCCESS THRESHOLD IS SET, AND NONE MAY BE SET BEFORE >=4 ***
*** RENDERS EXIST (L239's own constraint). Every number here is a COUNT of what      ***
*** happened, never a grade of whether it was worth it. A scorecard that grades on   ***
*** render 1 has invented its own baseline (finding_ranked_head_sample_is_not_the_    ***
*** population): the first weeks of any orchestration era are unrepresentative by     ***
*** construction, because the backlog being drained accumulated under a different     ***
*** regime.                                                                           ***

Declared perimeter (printed with every render):
  - ORCH_LOG rows are written at PROME's CONSUMPTION of a delivery, not at the desk's
    delivery, so `delivered` lags by minutes and an IN-FLIGHT row lags a death
    indefinitely. IN-FLIGHT is NOT a liveness signal (the ledger's own header says so).
  - `drained` counts inbox items INTEGRATED, which is a desk's self-report.
  - A desk with NO row is never-orchestrated OR spawned-before-logging. ABSENCE PROVES
    NOTHING (the ledger's ABSENT-ROW clause).
  - The 8/23 wave-1 rows mix model= values across a mid-flight swap. DO NOT POOL them
    and read NOTHING about model quality from this pilot.

rc: 0 rendered · 2 cannot render (ledger missing/unparseable).
"""
import subprocess
import sys
from collections import Counter, defaultdict

ROOT = subprocess.run(["git", "rev-parse", "--show-toplevel"],
                      capture_output=True, text=True, check=True).stdout.strip()
LEDGER = f"{ROOT}/PROME/state/ORCH_LOG.tsv"
COLS = ["date", "desk", "tier", "touch", "trigger", "drained", "delivered",
        "zero_capital", "notes", "brief_defects"]


def load():
    try:
        raw = open(LEDGER, encoding="utf-8").read().split("\n")
    except OSError as e:
        print(f"rc=2 CANNOT-RENDER: {e}")
        sys.exit(2)
    rows = []
    for ln in raw:
        if not ln.strip() or ln.startswith("#"):
            continue
        f = ln.split("\t")
        if f[0] == "date":
            continue
        d = dict(zip(COLS, f + [""] * (len(COLS) - len(f))))
        rows.append(d)
    if not rows:
        print("rc=2 CANNOT-RENDER: no data rows")
        sys.exit(2)
    return rows


def as_int(s):
    s = (s or "").strip()
    return int(s) if s.lstrip("-").isdigit() else None


def main():
    rows = load()
    dates = sorted({r["date"] for r in rows})
    print("# COORDINATION-VALUE SCORECARD — DOCKET L239")
    print(f"\n**Renderer:** `AGENTS/DAEDALUS/scripts/coordination_scorecard.py` · "
          f"**Source:** `PROME/state/ORCH_LOG.tsv` ({len(rows)} touch rows, "
          f"{dates[0]} → {dates[-1]})")
    print("\n⛔ **DESCRIPTIVE ONLY — no success threshold is set, and none may be set "
          "before >=4 renders exist.** Every figure below is a count of what happened. "
          "None of them says whether an orchestrated touch was WORTH its cost; that "
          "question needs a baseline this ledger is too young to supply.\n")

    # --- volume by day ---
    print("## 1. Touch volume by day\n")
    print("| Date | Touches | Desks | Drained (items) | Deliveries recorded | IN-FLIGHT |")
    print("|---|---|---|---|---|---|")
    for d in dates:
        rr = [r for r in rows if r["date"] == d]
        dr = sum(as_int(r["drained"]) or 0 for r in rr)
        inflight = sum(1 for r in rr if "IN-FLIGHT" in r["delivered"].upper())
        deliv = sum(1 for r in rr if r["delivered"].strip()
                    and "IN-FLIGHT" not in r["delivered"].upper())
        print(f"| {d} | {len(rr)} | {len({r['desk'] for r in rr})} | {dr} | "
              f"{deliv} | {inflight} |")

    # --- per desk ---
    print("\n## 2. Per-desk touches (whole ledger)\n")
    per = defaultdict(lambda: {"n": 0, "dr": 0, "days": set(), "inflight": 0})
    for r in rows:
        p = per[r["desk"]]
        p["n"] += 1
        p["dr"] += as_int(r["drained"]) or 0
        p["days"].add(r["date"])
        if "IN-FLIGHT" in r["delivered"].upper():
            p["inflight"] += 1
    print("| Desk | Touches | Days touched | Items drained | IN-FLIGHT rows |")
    print("|---|---|---|---|---|")
    for k in sorted(per, key=lambda x: (-per[x]["n"], x)):
        p = per[k]
        print(f"| {k} | {p['n']} | {len(p['days'])} | {p['dr']} | {p['inflight']} |")

    # --- the leg that actually measures coordination VALUE ---
    print("\n## 3. Brief-defect rate — the one leg that measures coordination QUALITY\n")
    bd = [as_int(r["brief_defects"]) for r in rows]
    scored = [b for b in bd if b is not None]
    withdef = [b for b in scored if b > 0]
    print(f"- Rows with a scored `brief_defects` cell: **{len(scored)} of {len(rows)}** "
          f"({100*len(scored)/len(rows):.0f}%)")
    print(f"- Rows reporting >=1 false premise in the spawn brief: **{len(withdef)}**"
          + (f" ({100*len(withdef)/len(scored):.0f}% of scored)" if scored else ""))
    print(f"- Total defects recorded: **{sum(scored)}**")
    print("\n> This column exists because *the trigger cell records what the brief SAID "
          "and this cell records whether it was TRUE.* It is the only column that can "
          "falsify the coordination layer rather than describe its volume. "
          f"**{len(rows)-len(scored)} unscored rows are the number to watch** — an "
          "unscored cell is not a zero, and reading it as one would manufacture a "
          "clean record (`finding_silent_blank_evades_review`).")

    # --- zero-capital ---
    print("\n## 4. Zero-capital discipline\n")
    zc = Counter((r["zero_capital"] or "").strip().upper() or "(blank)" for r in rows)
    for k, v in zc.most_common():
        print(f"- `{k}` — {v}")

    # --- zero-drain touches (leg-3b input rule) ---
    zd = [r for r in rows if (as_int(r["drained"]) or 0) == 0]
    print(f"\n## 5. Zero-drain touches: **{len(zd)}** of {len(rows)}\n")
    print("> Per the ledger's LEG-3b INPUT RULE (my own F4, 8/23), a zero-drain touch "
          "does NOT reset a desk's cadence clock. These rows are real orchestration "
          "cost that buys no inbox progress — the honest denominator for any future "
          "value question, and the reason this render counts them separately rather "
          "than folding them into touch volume.")

    print("\n## Perimeter (travels with every verdict)\n")
    print("- Rows are written at PROME's CONSUMPTION, not at the desk's delivery: "
          "`delivered` lags by minutes, IN-FLIGHT lags a death indefinitely. "
          "**IN-FLIGHT is not a liveness instrument.**")
    print("- `drained` is the desk's self-report of items integrated.")
    print("- **A desk with no row proves nothing** (ABSENT-ROW clause): never-orchestrated "
          "and spawned-before-logging are indistinguishable here.")
    print("- **The 8/23 wave-1 rows straddle a mid-flight model swap — do not pool them, "
          "and read nothing about model quality from this pilot** (the ruling was "
          "cost-based, explicitly).")
    print(f"\n**Renders so far: this is #1. A success threshold may be proposed at #4 "
          f"(earliest ~2026-09-25 at a weekly cadence), not before.**")
    return 0


if __name__ == "__main__":
    sys.exit(main())
