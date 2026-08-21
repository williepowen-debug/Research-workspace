#!/usr/bin/env python3
"""
mag7.py — VULCAN S1 instrument: retain a PRIMARY-sourced Mag-7 index-weight series.

WHY THIS EXISTS (2026-08-21): the Mag-7 weight was carried at "~32.5%, aggregator-
sourced, ~July vintage" for SIX WEEKS across 8 references in 4 files, while being
(a) S1's banded threshold input and (b) the instrument for THESIS-KILL leg 2. It was
self-flagged as "the weakest instrument on this rail" on 7/12 and never re-pulled,
because nothing pulled it. A load-bearing number with no instrument decays silently
(`finding_owned_surface_without_a_ledger_destroys_history`). The 8/21 primary pull
came in at 32.98% — 0.5pp higher, and AT the 33% yellow line the stale figure read as
comfortably below.

SOURCE — and why this one:
  State Street's own daily holdings file for SPDR S&P 500 ETF Trust (SPY), the
  full-replication trust tracking the index. This is an ISSUER-PUBLISHED PRIMARY.
  ⚠️ It is NOT the S&P DJI index file — spglobal.com is gated (403) and the committee
  does not publish free constituent weights. So this is a FUND weight, not an INDEX
  weight, and the difference is real but small (cash + timing). The row records BOTH
  the raw fund weight and the equity-normalized figure; quote the basis, always.

⚠️ THE PERIMETER TRAP THIS TOOL EXISTS TO PREVENT — read before editing MAG7:
  ALPHABET HAS TWO SHARE CLASSES IN THE INDEX (GOOGL class A + GOOG class C) AND BOTH
  COUNT. Dropping GOOG understates the Mag-7 by ~2.4pp (30.55% vs 32.98% on 8/20 data)
  — larger than the entire distance to the yellow threshold. Any "Mag-7 weight" that
  omits one class is wrong by more than the number it is being compared against.

VALIDATION (runs every invocation, no free parameters):
  Anchor the scale on ONE name, then predict the other seven from shares x close.
  Zero unknowns => a real test, not a fit (`finding_crosscheck_with_free_parameter_
  validates_nothing`). Worst-case error must be <1%; otherwise the row is not written.

THE BREADTH LEG (added 2026-08-21, same day, closing a defect in this tool's first
version): VULCAN's S1 RED band is a CONJUNCTION — "Mag-7 >=40% AND breadth collapse."
v1 measured LEVEL ONLY, so the red band was UNTRIPPABLE BY CONSTRUCTION — a banded
threshold with no metric surface for one of its legs
(`finding_banded_threshold_with_no_metric_surface_is_untrippable`). Now measured.

  Metric: RSP/SPY total-return ratio, 63-trading-day (~3mo) relative return, in pp.
          Equal-weight vs cap-weight — the SAME breadth instrument KB-066 already
          uses. Deliberately not a rival definition.
  Threshold: <= -7.5pp = BREADTH-COLLAPSE.
  ⚠️ BASE-RATED BEFORE SHIPPING, not chosen to look decisive
     (`finding_base_rate_the_threshold_before_building_it`). Over 2003-05..2026-08
     (5,865 sessions), de-clustered into DISTINCT episodes (>90d gap = new episode,
     per `finding_overlapping_window_inflates_the_base_rate` — raw overlapping day
     counts inflate exceedances ~Nx):
        -5.0pp  -> 217 days (3.74%), 10 episodes  = too loose to mean "collapse"
        -7.5pp  ->  85 days (1.47%),  5 episodes  = ~1 per 4.7 years   <-- CHOSEN
       -10.0pp  ->  10 days (0.17%),  2 episodes  = at the sample floor (p0.1=-10.30)
       -12.5pp  ->   0 days                       = NEVER occurred in 23 years;
                                                    picking it would have re-created
                                                    the exact untrippable defect.
  ⚠️ CONJUNCTION NOTE: Mag-7 >=40% has never occurred either (32.98% at build). The
     two legs are POSITIVELY correlated BY CONSTRUCTION — megacap leadership both
     raises Mag-7 weight and makes equal-weight underperform — so the joint gate is
     far more satisfiable than multiplying two marginals suggests. That coupling is
     STRUCTURAL (near-definitional), NOT measured: no Mag-7 weight history exists to
     test it on, and this tool's own series is the thing that will eventually provide
     one. Do not present it as an empirical finding.

WHAT IT RECORDS -> workbook/MAG7_SERIES.tsv (append-only, one row per run)
  asof + per-name weights + Mag-7 total + the ex-GOOG trap value + NVDA's share of
  the group + band state. Vintage is CONTENT-derived (`asof` from the file's own
  header), NEVER mtime (`finding_mtime_is_corrupted_by_git_sync`).

FAILS LOUD: any leg that breaks writes ERR:<reason> and exits nonzero. Never a blank,
never a stale carry-forward. A partial run is a FAILED run, not a degraded one [L-16].

USAGE
  python3 AGENTS/VULCAN/tools/mag7.py            # fetch + validate + append
  python3 AGENTS/VULCAN/tools/mag7.py --dry-run  # print, do not write
  python3 AGENTS/VULCAN/tools/mag7.py --show 10  # last N retained rows

EXIT: 0 = ok · 1 = partial/validation failed (no row written) · 2 = total failure
"""

from __future__ import annotations

import argparse
import datetime as _dt
import os
import subprocess
import sys

# --- re-exec under the repo venv if deps are missing [L-16: fix at the TOOL, because
#     the next reader invokes from memory, a spawn packet, or a boot script] ---
if os.environ.get("_MAG7_REEXEC") != "1":
    try:
        import openpyxl  # noqa: F401
        import yfinance  # noqa: F401
    except ImportError:
        _root = subprocess.run(["git", "rev-parse", "--show-toplevel"],
                               capture_output=True, text=True).stdout.strip()
        _vpy = os.path.join(_root, ".venv", "bin", "python")
        if os.path.exists(_vpy):
            os.environ["_MAG7_REEXEC"] = "1"
            os.execv(_vpy, [_vpy, os.path.abspath(__file__)] + sys.argv[1:])

SPY_URL = ("https://www.ssga.com/us/en/intermediary/library-content/products/"
           "fund-data/etfs/us/holdings-daily-us-en-spy.xlsx")
UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126 Safari/537.36")

# Alphabet appears TWICE by design. Do not "deduplicate" it.
MAG7 = ["AAPL", "MSFT", "GOOGL", "GOOG", "AMZN", "NVDA", "META", "TSLA"]

COLS = ["asof_utc", "holdings_asof", "mag7_pct", "mag7_pct_normalized",
        "mag7_ex_goog_pct", "nvda_pct", "nvda_share_of_group_pct",
        "total_file_weight", "n_holdings", "breadth_rsp_spy_63d_pp", "breadth_pctile",
        "breadth_state", "band", "per_name_pct", "validation", "source"]

BREADTH_COLLAPSE_PP = -7.5   # base-rated: 5 distinct episodes in 23.3yr (~1/4.7yr)
BREADTH_WINDOW = 63          # trading days ~ 3 months


def _root() -> str:
    return subprocess.run(["git", "rev-parse", "--show-toplevel"],
                          capture_output=True, text=True).stdout.strip()


def band(p: float, breadth_pp) -> str:
    """VULCAN's registered S1 band, with BOTH legs of the red conjunction measured.

    RED = Mag-7 >= 40% AND breadth collapse (<= BREADTH_COLLAPSE_PP). v1 of this tool
    measured level only and could never fire red; that is now fixed. If the breadth
    leg is unavailable the red band reports UNGRADEABLE rather than silently
    downgrading to orange — an unmeasurable leg must fail LOUD, not fail benign.
    """
    collapsed = (breadth_pp is not None) and (breadth_pp <= BREADTH_COLLAPSE_PP)
    if p >= 40.0:
        if breadth_pp is None:
            return "RED-UNGRADEABLE(level>=40 but breadth leg unavailable)"
        return ("RED" if collapsed
                else f"level>=40 but breadth {breadth_pp:+.2f}pp > {BREADTH_COLLAPSE_PP}pp — RED NOT met")
    if p >= 37.0:
        return "ORANGE"
    if p >= 33.0:
        return "YELLOW"
    return "below-yellow"


def fetch() -> tuple[dict, str, float, int]:
    import io
    import urllib.request
    import openpyxl
    req = urllib.request.Request(SPY_URL, headers={"User-Agent": UA})
    raw = urllib.request.urlopen(req, timeout=90).read()
    if len(raw) < 10_000 or raw[:2] != b"PK":
        raise RuntimeError(f"not-an-xlsx (got {len(raw)}B, likely a bot wall)")
    wb = openpyxl.load_workbook(io.BytesIO(raw))
    rows = list(wb.active.iter_rows(values_only=True))
    asof = ""
    for r in rows[:6]:
        if r and r[0] and "Holdings" in str(r[0]) and r[1]:
            asof = str(r[1]).replace("As of ", "").strip()
    if not asof:
        raise RuntimeError("holdings as-of header not found")
    h = {}
    for r in rows[5:]:
        if r and r[1] and r[4] not in (None, ""):
            try:
                h[str(r[1]).strip()] = (float(r[4]), float(r[6]))
            except (TypeError, ValueError):
                continue
    if len(h) < 450:
        raise RuntimeError(f"only {len(h)} holdings parsed, expected ~500")
    return h, asof, sum(v[0] for v in h.values()), len(h)


def breadth(asof: str):
    """The second leg of the RED conjunction: equal-weight vs cap-weight.

    Returns (rel_pp, percentile, state) or (None, None, "ERR:<reason>").
    Measured AS-OF the holdings date so both legs of the band share one clock —
    the same time-alignment bug that made this tool's first validator report a
    4.188% error on a perfect file.
    """
    import yfinance as yf
    try:
        d = _dt.datetime.strptime(asof, "%d-%b-%Y").date()
    except ValueError:
        return None, None, f"ERR:unparseable-asof-{asof}"
    try:
        px = yf.download(["RSP", "SPY"], start="2003-05-01",
                         end=d + _dt.timedelta(days=1),
                         progress=False, auto_adjust=True)["Close"].dropna()
        if len(px) < BREADTH_WINDOW + 250:
            return None, None, f"ERR:insufficient-history-{len(px)}"
        rel = px["RSP"] / px["SPY"]
        series = (rel / rel.shift(BREADTH_WINDOW) - 1.0) * 100.0
        series = series.dropna()
        cur = float(series.iloc[-1])
        pctile = float((series < cur).mean() * 100.0)
        state = "COLLAPSE" if cur <= BREADTH_COLLAPSE_PP else "no-collapse"
        return cur, pctile, state
    except Exception as e:  # noqa: BLE001
        return None, None, f"ERR:{type(e).__name__}"


def validate(h: dict, holdings_asof: str) -> str:
    """Zero-free-parameter check: anchor on ONE name, predict the other seven.

    ⚠️ MUST price on the HOLDINGS FILE'S OWN as-of date, not 'latest'. The first
    version of this used the most recent close and failed at 4.188% on a file that
    was in fact perfect — because it compared 8/20 holdings against 8/21 prices.
    A validator misaligned in TIME reports a data error that does not exist, which
    is the expensive direction: it discredits a good instrument.
    """
    import yfinance as yf
    missing = [t for t in MAG7 if t not in h]
    if missing:
        return f"ERR:missing-{','.join(missing)}"
    try:
        d = _dt.datetime.strptime(holdings_asof, "%d-%b-%Y").date()
    except ValueError:
        return f"ERR:unparseable-asof-{holdings_asof}"
    px = yf.download(MAG7, start=d, end=d + _dt.timedelta(days=1),
                     progress=False, auto_adjust=False)["Close"].dropna()
    if px.empty:
        return f"ERR:no-close-for-{d}"
    px = px.iloc[0]
    mv = {t: h[t][1] * float(px[t]) for t in MAG7}
    k = h["NVDA"][0] / mv["NVDA"]
    worst = max(abs(mv[t] * k - h[t][0]) / h[t][0] * 100 for t in MAG7)
    return (f"OK:priced-{d},anchored-on-NVDA,7-independent-predictions,worst-err={worst:.3f}%"
            if worst < 1.0 else f"ERR:inconsistent-at-{d}-worst-err={worst:.3f}%")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--show", type=int, metavar="N")
    a = ap.parse_args()

    out = os.path.join(_root(), "AGENTS", "VULCAN", "workbook", "MAG7_SERIES.tsv")

    if a.show:
        if not os.path.exists(out):
            print("  no series yet")
            return 0
        lines = open(out).read().rstrip("\n").split("\n")
        print("  " + "\n  ".join([lines[0]] + lines[1:][-a.show:]))
        return 0

    print("=" * 72)
    print("  VULCAN mag7 — S1 index-concentration series (SPY holdings, issuer-primary)")
    print("=" * 72)
    try:
        h, asof, tot, n = fetch()
    except Exception as e:
        print(f"  ERR:fetch — {e}")
        print("  NO ROW WRITTEN. A partial run is a FAILED run [L-16].")
        return 2

    v = validate(h, asof)
    b_pp, b_pct, b_state = breadth(asof)
    per = {t: h[t][0] for t in MAG7}
    s = sum(per.values())
    ex = s - per["GOOG"]
    norm = s / tot * 100

    print(f"  holdings as-of      {asof}   ({n} holdings, total weight {tot:.4f})")
    for t in MAG7:
        print(f"    {t:<6} {per[t]:8.4f}")
    print(f"  MAG-7               {s:.4f}%   (normalized {norm:.4f}%)")
    print(f"  ex-GOOG (THE TRAP)  {ex:.4f}%   <- wrong by {s-ex:.2f}pp; never quote this")
    print(f"  NVDA share of group {per['NVDA']/s*100:.2f}%")
    if b_pp is None:
        print(f"  BREADTH (RSP-SPY)   {b_state}   ⚠️ red band is UNGRADEABLE without it")
    else:
        print(f"  BREADTH (RSP-SPY)   {b_pp:+.2f}pp over {BREADTH_WINDOW}d "
              f"(pctile {b_pct:.1f}) -> {b_state}   [collapse at <= {BREADTH_COLLAPSE_PP}pp]")
    print(f"  BAND                {band(s, b_pp)}")
    print(f"  validation          {v}")

    if v.startswith("ERR"):
        print("  NO ROW WRITTEN — validation failed.")
        return 1
    if a.dry_run:
        print("\n  --dry-run: nothing written.")
        return 0

    row = [_dt.datetime.now(_dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), asof,
           f"{s:.4f}", f"{norm:.4f}", f"{ex:.4f}", f"{per['NVDA']:.4f}",
           f"{per['NVDA']/s*100:.2f}", f"{tot:.4f}", str(n),
           (f"{b_pp:.4f}" if b_pp is not None else b_state),
           (f"{b_pct:.1f}" if b_pct is not None else "ERR"),
           b_state, band(s, b_pp),
           ";".join(f"{t}:{per[t]:.4f}" for t in MAG7), v,
           "SSGA SPY daily holdings xlsx (issuer-primary; FUND weight, not S&P DJI index weight)"]
    new = not os.path.exists(out)
    with open(out, "a") as f:
        if new:
            f.write("\t".join(COLS) + "\n")
        f.write("\t".join(row) + "\n")
    print(f"\n  appended -> workbook/MAG7_SERIES.tsv")
    return 0


if __name__ == "__main__":
    sys.exit(main())
