#!/usr/bin/env python3
"""base_rate_review.py — recompute every registry row's rolling base rate and flag drift.

Born from CHG-RED-051 (2026-08-27): base rates were computed once at registration
(S30) and never recomputed, so FT-01 (published 21.8%) silently became a 48.3%/120s
regime descriptor and FT-07 (32.5%) an 84.2% one — while the published figures
REPRODUCED on the original sample. Staleness, not error: a correction pass could
not have caught it, only a scheduled recomputation can. This script is that
schedule's instrument (the `[[finding_mechanize_the_cap_not_the_ritual]]` class:
a deferrable review wants a boot check, not a remembered ritual).

What it does (read-only, ~10s, network for FRED/yfinance history):
  - For every mappable registry row: recompute the sustain-adjusted base rate on
    the full fetched sample, the last 120 observations, and the last 60.
  - Compare the 120-obs rate against the rate recorded in the row's
    `rolling_base_rate` cell (leading `NN.N%` token). Drift ratio >= 2.0x prints
    a RED flag, >= 1.5x an ORANGE one. A missing/MANUAL cell prints as such.
  - FT-11 special case: its "threshold" is a 5-session CHANGE on DGS30 (bp), not
    a level sustain. The script computes the rolling precondition rate AND prints
    the CURRENT 5-session change so the manual classifier's mappable half is
    surfaced at every run (the S34 open item).
  - `--candidate METRIC OP VALUE SUSTAIN` computes a base rate for a line that is
    NOT yet registered (used to base-rate FT-12 before registering it — the FT-10
    discipline: base-rate the threshold BEFORE building it).

Exit codes: 0 always (advisory), unless --strict, then 1 if any RED flag.
Methodology (matches S30/S35): a window at index i counts as satisfied when all
of obs[i-s+1..i] meet the condition; rate = satisfied windows / (n - s + 1).
TSVs are split on tab, never csv (ML-RED-168).

Wired as boot step 9d (2026-08-27, S37). Base-rate review is now scheduled: the
gap CHG-051 measured was not detection capability but invocation.
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from decimal import Decimal, InvalidOperation
from datetime import date
from pathlib import Path

REPO = Path(subprocess.run(
    ["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True, check=True
).stdout.strip())
RED = REPO / "AGENTS" / "RED"
REGISTRY = RED / "registry" / "FALSIFICATION_TRIGGERS.tsv"


def _ensure_venv():
    try:
        import yfinance  # noqa: F401
        return
    except ImportError:
        pass
    venv_py = REPO / ".venv" / "bin" / "python3"
    if venv_py.exists() and Path(sys.executable) != venv_py:
        import os
        os.execv(str(venv_py), [str(venv_py)] + sys.argv)
    sys.exit("yfinance unavailable and no repo venv at .venv/ — cannot continue")


_ensure_venv()
sys.path.insert(0, str(REPO / "FORGE" / "tools" / "market-data"))
import fetch  # noqa: E402

# metric -> (source, series/ticker, scale). Scale converts the raw series into
# the registry's units (bps for OAS, K for claims, level otherwise).
HISTORY_MAP = {
    "HY-OAS": ("fred", "BAMLH0A0HYM2", 100.0),
    "CCC-OAS": ("fred", "BAMLH0A3HYC", 100.0),
    "BRENT-PAPER": ("yf", "BZ=F", 1.0),
    "INITIAL-CLAIMS": ("fred", "ICSA", 0.001),
    # FT-06's canonical basis is FRED VIXCLS (the registry row's own disclosure,
    # ML-RED-176) — history therefore comes from VIXCLS, not ^VIX live bars.
    "VIX": ("fred", "VIXCLS", 1.0),
    "BREAKEVEN-5Y5Y": ("fred", "T5YIFR", 1.0),
    "SKEW-CBOE": ("yf", "^SKEW", 1.0),
    # CORE-CPI-3MO-ANN: unmapped BY DESIGN (release-derived compound, no series;
    # failing loud is correct for it — boot.py carries the same note).
}
FT11_METRIC = "UST-30Y-RALLY-ATTRIBUTION"
FRED_LIMIT = 800  # ~3y of daily obs; full-sample rates are labeled with their n


def rows(path: Path):
    lines = path.read_text().splitlines()
    head = lines[0].split("\t")
    out = []
    for ln in lines[1:]:
        if not ln.strip():
            continue
        f = ln.split("\t")
        out.append(dict(zip(head, f)))
    return out


def series_asc(metric: str) -> list[float]:
    src, key, scale = HISTORY_MAP[metric]
    if src == "fred":
        obs = fetch.fred_fetch(key, limit=FRED_LIMIT)
        # Exact decimal scaling — see boot.py scaled(): float("9.30")*100 = 930.0000000000001,
        # which is > 930 and silently counted 5 historical ties as FT-07 fires (DOCKET L258).
        vals = [_scaled(o["value"], scale) for o in reversed(obs) if "value" in o]
    else:
        import yfinance as yf
        h = yf.Ticker(key).history(period="3y")
        vals = [_scaled(v, scale) for v in h["Close"].dropna().tolist()]
    return vals


def _scaled(published, scale):
    """Scale a PUBLISHED value in exact decimal, never binary float (DOCKET L258).

    The base-rate path must use the SAME arithmetic as the live path in boot.py, or the
    published base rate describes a threshold the tool does not actually evaluate. Before
    this fix the two agreed only because BOTH were wrong in the same direction.
    
    ⛔ NO FALLBACK BRANCH. A try/except here that returns `float(published) * float(scale)`
    RESTORES THE EXACT L258 DEFECT THIS FUNCTION EXISTS TO REMOVE: forced, it returns
    930.0000000000001, which fires RED-FT-07's `> 930` STRICT band that the letter says
    must not fire. And it buys nothing - it re-raises on the very inputs it was written
    for (None -> TypeError, "" -> ValueError), so behaviour on bad input is IDENTICAL
    with or without it. All it can ever do is convert a loud failure into a silent wrong
    number. Removed 2026-09-14 (S45) after DAEDALUS forced the branch and demonstrated the
    restoration; the twin fallback in ft11_delta5() was removed the same session for the
    same reason, caught there by this repair's own acceptance test rather than by review.
    ⚠️ An error handler whose fallback is the PRE-REPAIR behaviour is invisible in review
    BECAUSE A try/except READS AS CAUTION (DAEDALUS PAT-171). Bad input must raise here.
    """
    return float(Decimal(str(published)) * Decimal(str(scale)))


def cond(op: str, threshold: float):
    return {
        "<": lambda v: v < threshold,
        ">": lambda v: v > threshold,
        "<=": lambda v: v <= threshold,
        ">=": lambda v: v >= threshold,
    }[op]


def base_rate(vals: list[float], op: str, threshold: float, sustain: int, window: int | None = None):
    """Fraction of sustain windows satisfied. window=None -> full sample."""
    if window:
        vals = vals[-(window + sustain - 1):]
    n = len(vals)
    if n < sustain:
        return None, 0
    c = cond(op, threshold)
    hits = [c(v) for v in vals]
    total = n - sustain + 1
    sat = sum(1 for i in range(sustain - 1, n) if all(hits[i - sustain + 1: i + 1]))
    return sat / total, total


def ft11_delta5(vals_pct: list[float]) -> list[float]:
    """5-session changes in bp on a percent-quoted series (DGS30), in EXACT DECIMAL.

    WHY (S45 2026-09-14, closing the item SCRATCH carried from S44 and DAEDALUS's
    DOCKET L258 packet): this differenced in raw binary float.

    ⚠️ THE FIRST MEASUREMENT OF THIS WAS WRONG IN RED'S OWN FAVOUR AND IS CORRECTED
    HERE. S44's note, and this repair's own first draft, recorded FT-11 as "benign by
    luck" - allegedly 0 decision flips under leg (iv)'s REGISTERED NON-STRICT `<=-4`
    and flips only under a hypothetical STRICT `<`. That is FALSE. Swept properly over
    the realistic fly range (-1.00..+1.00 pct, 2dp), the raw path flips the decision
    on the REGISTERED operator at 80 distinct levels, e.g.:

        fly -0.93 -> -0.97 : raw = -3.9999999999999925  ->  <= -4 is FALSE
                             exact = -4.0               ->  <= -4 is TRUE

    i.e. the raw path REJECTED A LEG-(iv) SATISFACTION THAT THE LETTER ACCEPTS - a
    live FALSE NEGATIVE on a registered precondition, not a hypothetical. The float
    error is SIGN-VARYING with operand magnitude (at fly -1.00 it drifts to
    -4.0000000000000036 and benignly accepts; at -0.93 it drifts the other way and
    wrongly rejects), which is exactly why "the drift is always in the safe
    direction" was an unsafe thing to have believed.

    The precondition leg IS benign: Delta5(DGS30) <= -10.2bp over DGS30 3.00-6.50
    flips 0 decisions, because that cut sits OFF the 1bp publication grid. Only the
    on-grid -4bp leg was exposed.

    NO PAST GRADE MOVES: S44 graded leg (iv) at -2.0bp, nowhere near the boundary,
    and its Delta5(DGS30) 5.25 -> 5.37 = +12.0bp reproduces exactly. The exposure was
    live and unfired, not retrospective.

    conformance repair, not a threshold change - identical in kind to scaled().

    ⚠️ NO FLOAT FALLBACK, DELIBERATELY. A first draft of this repair wrapped the
    Decimal conversion in try/except and fell back to raw float. That fallback was
    worthless and dangerous: it crashed on exactly the inputs (None, "") that make
    the Decimal path fail, so it added no robustness, and on any input where it HAD
    worked it would have silently restored the corrupted arithmetic this function
    exists to remove - a guard that fails OPEN into the defect it guards. Caught by
    this repair's own acceptance test, not in review. Bad input must fail loudly here.
    """
    return [
        float((Decimal(str(vals_pct[i])) - Decimal(str(vals_pct[i - 5]))) * 100)
        for i in range(5, len(vals_pct))
    ]


def parse_recorded_rate(cell: str) -> float | None:
    tok = cell.strip().split("%")[0].strip() if cell else ""
    try:
        return float(tok)
    except ValueError:
        return None


def _arm_date_note(row):
    """Arm-date note DERIVED from the registry row, never hardcoded.

    Reads instrument_basis_operative (the operative cell) and returns the FIRST
    'precondition live from <date>' match, which is the CURRENT date; later matches
    in that cell are dated corrections quoting SUPERSEDED text and must not win.
    Falls back to the state cell, then to silence. Fails to SILENT, never to a
    stale literal: a hardcoded 2026-09-09 lived here and kept printing the old arm
    date after the registry was corrected to 2026-09-10 (S43 2026-09-10) - the tool
    asserted a date independently of the file it reports on.
    """
    import re as _re
    for cell in ("instrument_basis_operative", "state"):
        m = _re.search(r"precondition live from (\d{4}-\d{2}-\d{2})", row.get(cell, "") or "")
        if m:
            return f" (live from {m.group(1)})"
    return ""


def flag(ratio: float | None) -> str:
    if ratio is None:
        return "  "
    # L546 (DAEDALUS 2026-10-08, fixed S51 2026-10-09): ratio = r120*100/recorded is a float
    # quotient, so an exact-on-edge tie could land on either side (33/120*100/55.0 =
    # 0.5000000000000001 missed 🔴; 2/120*100/2.5 = 0.6666666666666667 missed 🟠 against
    # 1/1.5 = 0.6666666666666666). Round to 6dp BEFORE comparing; edges are typed literals.
    ratio = round(ratio, 6)
    if ratio >= 2.0 or ratio <= 0.5:
        return "🔴"
    if ratio >= 1.5 or ratio <= 0.666667:
        return "🟠"
    return "🟢"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--strict", action="store_true", help="exit 1 on any 🔴 drift flag")
    ap.add_argument("--candidate", nargs=4, metavar=("METRIC", "OP", "VALUE", "SUSTAIN"),
                    help="base-rate an UNREGISTERED line (e.g. HY-OAS '<' 260 3)")
    args = ap.parse_args()

    today = date.today().isoformat()
    red_flags = 0

    if args.candidate:
        m, op, val, s = args.candidate
        vals = series_asc(m)
        full, nf = base_rate(vals, op, float(val), int(s))
        r120, _ = base_rate(vals, op, float(val), int(s), 120)
        r60, _ = base_rate(vals, op, float(val), int(s), 60)
        print(f"CANDIDATE {m} {op} {val} s={s}  [{today}]")
        print(f"  full sample (n={nf}): {full * 100:.1f}%   last 120: {r120 * 100:.1f}%   last 60: {r60 * 100:.1f}%")
        return 0

    print(f"BASE-RATE REVIEW — registry vs live series  [{today}]  (CHG-051 instrument; methodology = S30/S35)")
    print(f"{'id':<10} {'line':<24} {'recorded':>9} {'full(n)':>14} {'last120':>8} {'last60':>7}  drift")
    for r in rows(REGISTRY):
        tid, metric = r["trigger_id"], r["metric"]
        recorded = parse_recorded_rate(r.get("rolling_base_rate", ""))
        line = f"{metric} {r['threshold_op']} {r['threshold_value']} s={r['sustain_window']}"
        if metric == FT11_METRIC:
            src_vals = fetch.fred_fetch("DGS30", limit=FRED_LIMIT)
            pct = [float(o["value"]) for o in reversed(src_vals) if "value" in o]
            d5 = ft11_delta5(pct)
            thr = float(r["threshold_value"])
            full = sum(1 for v in d5 if v <= thr) / len(d5)
            r120 = sum(1 for v in d5[-120:] if v <= thr) / min(120, len(d5))
            cur = d5[-1]
            ratio = (r120 * 100 / recorded) if recorded else None
            fl = flag(ratio)
            if fl == "🔴":
                red_flags += 1
            print(f"{tid:<10} {'Δ5(DGS30)<=' + str(thr) + 'bp':<24} {recorded or '—':>9} "
                  f"{full * 100:>10.1f}%({len(d5)}) {r120 * 100:>7.1f}% {'':>7}  {fl}  "
                  f"CURRENT Δ5 = {cur:+.1f}bp -> precondition {'WOULD FIRE' if cur <= thr else 'clear'}"
                  f"{_arm_date_note(r)}")
            continue
        if metric not in HISTORY_MAP:
            print(f"{tid:<10} {line:<24} {'MANUAL':>9} {'—':>14} {'—':>8} {'—':>7}  ⚪ release-derived, review at each print")
            continue
        vals = series_asc(metric)
        thr = float(r["threshold_value"])
        s = int(r["sustain_window"])
        full, nf = base_rate(vals, r["threshold_op"], thr, s)
        r120, _ = base_rate(vals, r["threshold_op"], thr, s, 120)
        r60, _ = base_rate(vals, r["threshold_op"], thr, s, 60)
        ratio = (r120 * 100 / recorded) if (recorded and r120 is not None) else None
        fl = flag(ratio)
        if fl == "🔴":
            red_flags += 1
        rec_s = f"{recorded:.1f}%" if recorded is not None else "—"
        print(f"{tid:<10} {line:<24} {rec_s:>9} {full * 100:>10.1f}%({nf}) {r120 * 100:>7.1f}% {r60 * 100:>6.1f}%  {fl}"
              + (f"  {ratio:.1f}x vs recorded" if ratio else ""))

    print("\n  🔴 = rolling(120) >= 2x or <= 0.5x the recorded rate — the row's selectivity credential is stale;")
    print("       re-review it (do NOT auto-edit thresholds; bear-relevant re-cuts go to a scheduled window).")
    if args.strict and red_flags:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
