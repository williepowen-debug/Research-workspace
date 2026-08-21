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


def check_fr2004() -> int:
    """FR2004 dealer-stock vintage drift across live surfaces.

    WHY THIS EXISTS. On 2026-08-21 a boot-doc audit found the 8/12 as-of had
    landed on STATUS's dashboard and VX-04 while FOUR surfaces still read
    "current through the 8/05 as-of" -- TRADE.md, STATUS's exit block, the
    CATALYSTS row, and DEALER_CAPACITY's BODY sitting beneath a fresh 8/12
    HEADER. Both boot and closeout had returned rc=0 that morning.

    They were right to: the drift checker covers the FRED set, and FR2004 is
    the NY FED api. A load-bearing series that no check covers rots silently
    and reports clean -- so coverage, not diligence, was the gap.
    """
    import re
    here = Path(__file__).resolve().parent.parent
    try:
        sys.path.insert(0, str(here / "monitors"))
        import fr2004_fetch as fr
        sb = fr.current_seriesbreak(dt.date.today())
        series = {label: fr.fetch(k, sb) for k, label in fr.BUCKETS}
        dates = sorted(set.intersection(*(set(v) for v in series.values())))
    except Exception as e:                                    # noqa: BLE001
        print(f"\n   \u26a0\ufe0f  FR2004 vintage check DID NOT RUN ({e}) — that is a GAP, not a pass")
        return 1
    if not dates:
        print("\n   \u26a0\ufe0f  FR2004 returned no common as-of dates — GAP, not a pass")
        return 1
    latest = dates[-1]
    lm, ld = int(latest[5:7]), int(latest[8:10])
    findings = 0
    pat = re.compile(r"as[- ]of[^0-9]{0,24}(?:\*\*)?(20\d{2}-\d{2}-\d{2}|(\d{1,2})/(\d{1,2}))"
                     r"|through the (?:\*\*)?(\d{1,2})/(\d{1,2})(?:\*\*)? as-of", re.I)
    surfaces = ([here / f for f in ("STATUS.md", "TRADE.md", "NEXUS_BRIEF.md",
                                    "SCRATCH.md", "docket/CATALYSTS.tsv")]
                + sorted((here / "monitors").glob("*.md")))
    for f in surfaces:
        if not f.exists():
            continue
        for i, l in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
            if "ASSERTION_CHECK: LIVE-REGION-ENDS" in l:
                break          # explicitly superseded region -- same sentinel
            if "fr2004" not in l.lower() and "dealer" not in l.lower() and "as-of" not in l.lower():
                continue
            low = l.lower()
            # NARROW guard, not the shared GUARD list. The shared list contains
            # "✅", and two of the four surfaces this check exists to catch
            # carried a ✅ for an UNRELATED clause on the same line ("✅ FIRED
            # 7/28", "✅ GAP CLOSED") -- the full list would have skipped the
            # exact defect. Only an explicit RETRACTION marker suppresses here.
            if any(g in low for g in ("this read", "this line read", "read \"",
                                      "until 2026-", "corrected 2026-", "prior:")):
                continue
            for m in pat.finditer(l):
                g1, a, b, c, d = m.groups()
                # g1 captures the WHOLE alternation, so a slash match lands in
                # it too -- discriminate on shape, not on which group is set.
                if g1 and len(g1) == 10 and g1[4] == "-":
                    mo, da = int(g1[5:7]), int(g1[8:10])
                elif a and b:
                    mo, da = int(a), int(b)
                elif c and d:
                    mo, da = int(c), int(d)
                else:
                    continue
                if (mo, da) == (lm, ld):
                    continue
                if (mo, da) > (lm, ld):
                    continue                       # a future/expected as-of, fine
                print(f"\n   \U0001F534 FR2004 VINTAGE DRIFT — {f.name}:{i} names as-of "
                      f"{mo}/{da:02d}; latest published is {latest}")
                print(f"      {re.sub(r'  +', ' ', l).strip()[:150]}")
                findings += 1
                break
    if not findings:
        print(f"\n   \u2705 FR2004 vintage consistent across live surfaces (latest as-of {latest})")
    return findings


DRIFT_FIXTURES = [
    # Fixtures for the NUMERIC half of the closeout pass. Added 2026-08-21,
    # when a boot-doc audit found this checker had no selftest at all while
    # CLAUDE.md advertised that the combined pass "verifies the CHECKERS".
    # Each is a real shape from this desk's TRADE.md gate table.
    ("REAL 8/20 defect: a live MARK on the posture surface",
     "| **(a) DFII10 >2.5 sustained** | gap is 6bp and closing; DFII10 2.44 |",
     {"DFII10": 2.35}, [("DFII10", 2.44, 2.35)]),
    ("a THRESHOLD is never a drift candidate (>2.5 with live 2.35)",
     "| **(a) DFII10 >2.5 sustained** | LIVE — the only survivor |",
     {"DFII10": 2.35}, []),
    ("'below 2.50' is a threshold too, not a mark",
     "| (a) DFII10 | fires only if it closes below 2.50 |",
     {"DFII10": 2.35}, []),
    ("a correct mark does not fire",
     "| (a) DFII10 | DFII10 2.35 |", {"DFII10": 2.35}, []),
    ("out-of-band number is not a level for this metric (5.19 vs DFII10 2.35)",
     "| (a) DFII10 | unrelated figure 5.19 |", {"DFII10": 2.35}, []),
    ("GUARD-token row is skipped (already marked corrected)",
     "| (a) DFII10 | ⚠️ CORRECTED: this read DFII10 2.44 |",
     {"DFII10": 2.35}, []),
    ("earliest alias wins when a row names two metrics",
     "| (b) 30Y >5.0 / 10Y >4.6 | DGS30 5.11 |",
     {"DGS30": 5.19, "DGS10": 4.65}, [("DGS30", 5.11, 5.19)]),
    ("no tracked alias in the row => nothing to check",
     "| (c) Composition failure at the 7/28 7Y | printed 70.15% / 12.97% |",
     {"DFII10": 2.35}, []),
]


def drift_selftest() -> int:
    fails = 0
    print("[boot_recompute --selftest] NUMERIC half of the closeout pass\n")
    for label, row, live, expected in DRIFT_FIXTURES:
        got = gate_row_drift(row, live)
        ok = got == expected
        fails += 0 if ok else 1
        print(f"  {'PASS' if ok else 'FAIL'}  {label}")
        if not ok:
            print(f"        expected {expected!r}, got {got!r}")
    print(f"\n  {'ALL PASS' if not fails else str(fails) + ' FAILURE(S)'} — "
          f"{len(DRIFT_FIXTURES)} drift fixtures")
    return 1 if fails else 0


def gate_row_drift(l: str, live_by_sid: dict):
    """PURE predicate: MARKs in ONE gate row that disagree with the live level.

    Extracted 2026-08-21. It was inline inside check_unread_surfaces(), which
    does I/O and printing, so it could not be tested -- and `closeout_check
    --selftest` therefore verified only the ASSERTION checker while CLAUDE.md
    advertised that it "verifies the CHECKERS", plural. Half the combined pass
    had zero coverage and the doc said otherwise.

    Returns [(sid, found_value, live_value)].
    """
    import re
    low = l.lower()
    if any(g in low for g in GUARD):
        return []
    hits = []
    for sid in ("DFII10", "DGS30", "DGS10", "DGS2"):
        for a in ALIAS[sid]:
            i = low.find(a.lower())
            if i >= 0:
                hits.append((i, sid))
    if not hits:
        return []
    sid = min(hits)[1]                 # the row is about ONE metric: the earliest alias
    if sid not in live_by_sid:
        return []
    live = live_by_sid[sid]
    out = []
    for m in re.finditer(r"(?<![\d.])(\d+\.\d+)(?![\d])", l):
        before = l[max(0, m.start() - 12):m.start()]
        if re.search(r"(>=|<=|>|<|\u2265|\u2264|above|below|over|under)\s*$", before, re.I):
            continue                   # a THRESHOLD, by construction -- never a mark
        f = float(m.group(1))
        if abs(f - live) < 5e-3:
            continue                   # already correct
        if abs(f - live) <= 0.60:      # in-band => reads as a level for this metric
            out.append((sid, f, live))
    return out


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
        for sid, f, live in gate_row_drift(l, {k: v[-1][1] for k, v in series.items()}):
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

    # FR2004 vintage (2026-08-21). Wired in HERE, not shipped as a second
    # command, for the same reason as the watchers below: a pass needing two
    # invocations gets half-run. This series is the NY Fed api, not FRED, so
    # nothing above covers it -- which is why four surfaces sat a print behind
    # while both boot and closeout returned rc=0.
    drift += check_fr2004()

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
