#!/usr/bin/env python3
"""BOND — boot-time recompute of LOAD-BEARING DERIVED statistics.

WHY THIS EXISTS
---------------
On 2026-08-18 BOND made six method errors in one day. **Every one was a
CARRIED figure; none was a fresh computation.** The existing boot protocol
already said "pull load-bearing figures LIVE" -- and BOND did. The gap was
that the instruction covered LEVELS (30Y, DFII10, HY OAS) and not DERIVED
statistics (runs, counts, percentiles, gate distances), which is where all
six errors lived.

It also encodes three specific lessons from that day:

  1. **Declare the aggregation, not just the series.** A run computed
     per-year and a run computed whole-series differ by 57% on the same
     data. Every line below prints its own method.
  2. **Refresh the RELEASE, not the series you happen to be grading.**
     DFII10 and DGS30 publish on the same H.15 cycle; BOND re-pulled one
     and left the other, leaving a live add-gate distance stale for hours.
     This pulls the whole set.
  3. **Bust the cache.** A 5-minute TTL is invisible to a reader and makes
     "I pulled it live" false without any error surfacing.

USAGE
-----
    python3 monitors/boot_recompute.py

Prints a stamped block for pasting/checking against STATUS, plus TRADE.md's
gate table and a drift check on the boot-unread surfaces.
rc 0 clean; rc 1 unguarded drift found (NOT a pass); rc 2 fetch failure
(also NOT a pass).
"""
from __future__ import annotations

import datetime as dt
import glob
import os
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO / "FORGE" / "tools" / "market-data"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

# H.15 publishes these together -- always refresh as a SET.
H15_SET = ["DGS2", "DGS10", "DGS30", "DFII10", "T10YIE", "T5YIFR"]
CREDIT = ["BAMLH0A0HYM2", "BAMLH0A3HYC", "BAMLC0A0CM"]
GATES = {"DFII10": ("TLT add-gate", 2.50, "above"),
         "T5YIFR": ("inflation-unanchor red", 2.50, "above"),
         "DGS30": ("long-end level", 5.00, "above"),
         "DGS10": ("arm-#2 line", 4.50, "above")}


def bust_cache() -> int:
    n = 0
    for f in glob.glob(str(REPO / "FORGE/tools/market-data/.cache/fred_*.json")):
        try:
            os.remove(f); n += 1
        except OSError:
            pass
    return n


# ---------------------------------------------------------------------------
# UNREAD-SURFACE DRIFT CHECK  (added 2026-08-20, Will-approved)
#
# WHY: the 8/20 core-file sweep found every stale cluster living in TRADE.md,
# monitors/*.md and NEXUS_BRIEF.md -- the three surfaces the BOOT protocol does
# NOT read. STATUS is checked every boot and was nearly clean; the unread files
# rotted for weeks. The worst instance: TRADE.md described the ONLY live
# add-gate as "6bp away and closing" when DFII10 had backed off to 9bp and was
# WIDENING -- a decision number, pointing the wrong way, on the trade surface.
#
# This is wired into the TOOL rather than added as a boot instruction because
# the conditional steps ("update TRADE.md if state changed") are self-assessed,
# and today proved they get skipped. Detection was never the gap; invocation was.
# ---------------------------------------------------------------------------

GUARD = ("supersed", "was \"", "until 8/", "corrected", "retract", "prior",
         "historical", "re-pin", "8/18 block", "read \"", "no longer", "stale",
         "deliberately not", "→ `status.md`", "hand-derived", "not carried here")

ALIAS = {"DFII10": ("DFII10", "10Y real"), "DGS30": ("DGS30", "30Y"),
         "DGS10": ("DGS10", "10Y"), "DGS2": ("DGS2", "2Y")}


def _floats(text):
    import re
    return [float(x) for x in re.findall(r"(?<![\d.])\d+\.\d+(?![\d])", text)]


def check_unread_surfaces(series) -> int:
    """Print TRADE.md's gate table and flag drift on boot-unread surfaces."""
    import re
    here = Path(__file__).resolve().parent.parent
    findings = 0

    # --- 1. THE GATE TABLE: print it, so it is actually READ at boot.
    trade = here / "TRADE.md"
    print("\n== GATE TABLE  (TRADE.md — printed here because boot never reads that file) ==")
    if not trade.exists():
        print("   ⚠️  TRADE.md not found"); return 1
    lines = trade.read_text(encoding="utf-8").splitlines()
    rows = [l for l in lines if re.match(r"\s*\|\s*\*{0,2}\(?[a-d]\)", l)]
    if not rows:
        print("   ⚠️  no gate rows matched — table renamed or restructured? CHECK MANUALLY.")
        findings += 1
    for l in rows:
        flat = re.sub(r"\s+", " ", l).strip()
        print("   " + (flat[:150] + ("…" if len(flat) > 150 else "")))

    # --- 2. DRIFT: an unguarded hardcoded LEVEL for the metric a gate row is about.
    #     Threshold-vs-mark discriminator: a number preceded by a comparator
    #     (>, <, >=, <=, above, below) IS the gate's own threshold and is never a
    #     drift candidate. A number introduced by the metric name or a bracket is
    #     a MARK, and marks do not belong on a posture surface at all.
    for l in rows:
        low = l.lower()
        if any(g in low for g in GUARD):
            continue
        # each gate row is about ONE metric: the alias appearing earliest in it
        hits = []
        for sid in ("DFII10", "DGS30", "DGS10", "DGS2"):
            for a in ALIAS[sid]:
                i = low.find(a.lower())
                if i >= 0:
                    hits.append((i, sid))
        if not hits:
            continue
        sid = min(hits)[1]
        if sid not in series:
            continue
        live = series[sid][-1][1]
        for m in re.finditer(r"(?<![\d.])(\d+\.\d+)(?![\d])", l):
            before = l[max(0, m.start() - 12):m.start()]
            if re.search(r"(>=|<=|>|<|\u2265|\u2264|above|below|over|under)\s*$", before, re.I):
                continue                       # a THRESHOLD, by construction
            f = float(m.group(1))
            if abs(f - live) < 5e-3:
                continue                       # already correct
            if abs(f - live) <= 0.60:          # in-band => reads as a level for this metric
                print(f"\n   \U0001F534 GATE DRIFT — TRADE.md carries a {sid} MARK of {f}; "
                      f"live is {live} [{series[sid][-1][0]}]")
                print(f"      {re.sub(r'  +', ' ', l).strip()[:150]}")
                findings += 1

    # --- 3. FROZEN-VINTAGE CLAIMS: "X is the freshest print" naming a stale date.
    newest = max(obs[-1][0] for obs in series.values())
    for f in sorted(list((here / "monitors").glob("*.md")) + [here / "NEXUS_BRIEF.md", trade]):
        for i, l in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
            if not re.search(r"freshest (confirmed )?print|is the freshest|no \S+ exists yet", l, re.I):
                continue
            if any(g in l.lower() for g in GUARD):
                continue
            print(f"\n   🔴 FROZEN VINTAGE — {f.name}:{i} names a fixed 'freshest print'; "
                  f"newest actual observation is {newest}")
            print(f"      {re.sub(r'  +', ' ', l).strip()[:150]}")
            findings += 1

    if findings == 0:
        print("\n   ✅ no unguarded drift on TRADE.md / monitors / NEXUS_BRIEF")
    return findings


def main() -> int:
    import fetch  # noqa: E402
    print(f"[boot_recompute] cache entries busted: {bust_cache()}")
    print(f"[boot_recompute] run {dt.datetime.now():%Y-%m-%d %H:%M} local\n")

    series = {}
    try:
        for sid in H15_SET + CREDIT:
            raw = fetch.fred_fetch(sid, limit=20000)
            obs = sorted((o["date"], float(o["value"])) for o in raw if "error" not in o)
            if not obs:
                raise RuntimeError(f"{sid} returned no observations")
            series[sid] = obs
    except Exception as e:
        print(f"[boot_recompute] FETCH FAILURE: {e}", file=sys.stderr)
        print("[boot_recompute] rc=2 — NOT a pass.", file=sys.stderr)
        return 2

    print("== LEVELS (latest published) ==")
    for sid, obs in series.items():
        d, v = obs[-1]
        print(f"   {sid:14} {v:>8.2f}   [{d}]   n={len(obs):,}  span {obs[0][0]}→{obs[-1][0]}")

    print("\n== GATE DISTANCES (the numbers that drive decisions) ==")
    for sid, (label, thr, direction) in GATES.items():
        d, v = series[sid][-1]
        gap = (thr - v) if direction == "above" else (v - thr)
        state = "🔴 BREACHED" if gap <= 0 else f"{gap*100:>5.0f}bp away"
        print(f"   {sid:8} {v:>6.2f} vs {thr:>5.2f}  {label:24} {state}   [{d}]")

    print("\n== DERIVED: 30Y regime statistics ==")
    print("   method: DGS30 · session closes · threshold ≥5.00 · MAXIMAL run · WHOLE-SERIES scan")
    obs = series["DGS30"]
    y = dt.date.today().year
    cur = [x for x in obs if x[0].startswith(str(y))]
    days = sum(1 for _, v in cur if v >= 5.00)
    best = run = 0
    for _, v in obs:
        run = run + 1 if v >= 5.00 else 0
        best = max(best, run)
    live = 0
    for _, v in reversed(obs):
        if v >= 5.00:
            live += 1
        else:
            break
    print(f"   {y} days ≥5.00      : {days}   (of {len(cur)} sessions)")
    print(f"   current run         : {live} consecutive")
    print(f"   longest run, series : {best}")
    print(f"   {y} max             : {max(cur, key=lambda x: x[1])}")
    print(f"   series max          : {max(obs, key=lambda x: x[1])}")

    print("\n== DERIVED: percentiles (method: full-series rank of the latest close) ==")
    for sid in ("DGS30", "DGS10", "DFII10"):
        obs = series[sid]
        v = [x[1] for x in obs]
        cv = obs[-1][1]
        post = [x for d, x in obs if d >= "2010-01-01"]
        p_full = 100 * sum(1 for x in v if x < cv) / len(v)
        p_post = 100 * sum(1 for x in post if x < cv) / len(post) if post else float("nan")
        print(f"   {sid:8} {cv:>6.2f}  full {p_full:5.1f}th (n={len(v):,}, from {obs[0][0]})"
              f"   post-2010 {p_post:5.1f}th")

    drift = check_unread_surfaces(series)

    # MISSING-WATCHER CHECKS (2026-08-20, Will-directed) -- wired in HERE rather
    # than shipped as a second command, because this desk's own lesson is that a
    # pass needing two invocations gets half-run on a busy session.
    try:
        import watchers
        gates = {}
        for sid, (lab, thr, side) in GATES.items():
            cur = series[sid][-1][1]
            gates[sid] = abs(thr - cur) * 100
        print("\n== MISSING-WATCHER CHECKS (date-gates - retirements - derived distances) ==")
        drift += watchers.run(gates=gates)
    except Exception as e:                      # never let a watcher break the boot pull
        print(f"\n[boot_recompute] WARNING: watchers did not run ({e}). "
              f"That is a GAP, not a pass.")
        drift += 1

    print("\n⚠️  Paste-check these against STATUS. Any figure on a BOND surface that is NOT")
    print("    in this block, or disagrees with it, is a CARRIED figure — recompute or drop it.")
    if drift:
        print(f"\n[boot_recompute] rc=1 — {drift} unguarded drift finding(s) on boot-unread "
              f"surfaces. NOT a pass: fix by PATTERN across the tree, never by the line list above.")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
