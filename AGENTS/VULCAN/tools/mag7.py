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


# ---------------------------------------------------------------------------
# THE SECTOR-WITHIN-INDEX LEG (added 2026-08-27) — contribution decomposition.
#
# THE QUESTION IT ANSWERS: "how much of the index's move IS the AI-hardware
# layer?" — carried as an open VULCAN item since 2026-08-24, when the S2 call
# turned on exactly this arithmetic done BY HAND ("AI-compute fell HARDER than
# QQQ, so it is a bloc rotation, not a memory-cycle lead").
#
# ⚠️ IT IS THE S&P 500, NOT QQQ, AND THAT IS A SUBSTITUTION — SAY SO.
#   The open item named QQQ. Invesco returns HTTP 406 on every path tried
#   (holdings CSV, product page, download endpoint) — a domain-wide bot wall —
#   and api.nasdaq.com's ETF holdings route 404s. So QQQ constituent weights are
#   PUBLIC-BUT-UNFETCHED, not unavailable: three endpoints, two issuers, one
#   session. Classified rather than assumed [ZHAO precedent 2026-08-21: unchecked
#   is not unavailable, and this desk got that wrong once already].
#   The SPY file is ALREADY FETCHED by this tool, is issuer-primary, and is the
#   basis S1's OWN registered band grades on (Mag-7 share of S&P 500). So the
#   substitution moves the leg TOWARD S1's threshold, not away from it — but the
#   two indices are NOT interchangeable: QQQ is ~60% tech vs the S&P's ~35%, so
#   an AI-hardware share computed here is STRUCTURALLY SMALLER than the QQQ
#   figure the item asked for. Never quote one as the other.
#
# THE PRIMARY OUTPUT IS THE CONTRIBUTION IN pp, NOT THE SHARE — deliberately.
#   "What % of the move was AI-hardware?" is a RATIO, and a ratio whose
#   denominator is an index return is unstable exactly when the index is quiet:
#   if the layer adds +0.50pp while everything else subtracts -0.48pp, the index
#   moves +0.02pp and the "share" reads 2500%. That is not a large number, it is
#   a small denominator. So: contribution in pp is always reported; the SHARE is
#   reported ONLY when |index move| >= SHARE_FLOOR_PP and is UNGRADEABLE
#   otherwise — never silently rendered
#   [`finding_spread_metric_blind_to_common_mode`: report component LEVELS beside
#    any ratio; `finding_output_shape_implies_more_than_the_measurement`].
#   ⚠️ BASE-RATED BEFORE SHIPPING so the ungradeable rate is known in advance
#   rather than discovered as a surprise. MEASURED over 2003-05-01..2026-08-27
#   (5,869 SPY total-return bars), |SPY return| clears the 1.0pp floor on:
#        1d  25.2% of windows   (median |ret| 0.50pp)
#        5d  57.8%              (median 1.22pp)
#       21d  82.3%              (median 2.77pp)
#       63d  91.9%              (median 5.32pp)
#   ⇒ THE 1-DAY SHARE IS EXPECTED TO BE UNGRADEABLE ABOUT THREE DAYS IN FOUR.
#   That is the instrument working, not failing.
#   ⚠️ These were MEASURED, and the measurement mattered: the first draft of this
#   comment ASSERTED 33.2/65.9/82.4/88.6 from intuition and was wrong on three of
#   the four windows (1d by 8pp, 5d by 8pp) — in the direction that made the
#   instrument look more gradeable than it is
#   [`finding_adoption_is_not_validation`; a plausible base rate written into a
#    docstring is never re-checked by anyone].
#
# MEMBERSHIP IS A JUDGMENT CALL, SO IT IS DECLARED, FROZEN, AND REPORTED NESTED.
#   A single hand-picked "AI-hardware" set is a free parameter wearing a name
#   [`finding_crosscheck_with_free_parameter_validates_nothing`]. Tiers are
#   NESTED (T1 ⊂ T2 ⊂ T3) so the reader sees how much of the answer is the
#   definition rather than the data. PLATFORM and LEGACY are reported ALONGSIDE,
#   not inside, because they are different mechanisms:
#     T1 AI-compute silicon  — the accelerator/custom-silicon layer
#     T2 = T1 + the S2 production chain (memory + semicap)
#     T3 = T2 + the physical datacenter build layer (S3 adjacency)
#     PLATFORM  — the hyperscalers, i.e. the capex SPENDERS (S1's own root)
#     LEGACY    — analog/legacy semis: a DIFFERENT cycle, carried as a CONTRAST
#   🔑 PLATFORM-vs-T1 is the S1 mechanism question in one line: on a given move,
#   is the index being driven by the capex SPENDERS or the capex RECIPIENTS?
#
# VALIDATION — zero free parameters, and it doubles as the weight-drift meter.
#   Sum EVERY priced holding's w_i x r_i and compare to SPY's own return over the
#   same window. Nothing is fitted. The residual is reported per window, and it
#   IS the measure of how far end-of-window weights have drifted from the weights
#   that actually applied during the window — so the approximation's cost is
#   visible per row instead of being argued about in a comment.
# ---------------------------------------------------------------------------

LAYER_T1 = ["NVDA", "AVGO", "AMD", "MRVL"]
LAYER_MEMORY = ["MU", "WDC", "STX", "SNDK"]
LAYER_SEMICAP = ["AMAT", "LRCX", "KLAC", "TER"]
LAYER_DCBUILD = ["ANET", "VRT", "SMCI", "DELL", "HPE"]
LAYER_PLATFORM = ["MSFT", "GOOGL", "GOOG", "AMZN", "META"]
LAYER_LEGACY = ["INTC", "TXN", "QCOM", "ADI", "NXPI", "MCHP", "ON", "MPWR",
                "SWKS", "QRVO"]

LAYER_T2 = LAYER_T1 + LAYER_MEMORY + LAYER_SEMICAP
LAYER_T3 = LAYER_T2 + LAYER_DCBUILD

# STRUCTURAL INVARIANT, checked at import rather than in a test file because it is a
# property of the DEFINITIONS, not of a run: `rest_pp` is computed as
# total - T3 - PLATFORM - LEGACY, which is only correct if those three are pairwise
# DISJOINT. A ticker added to two lists would be counted twice in the layer figures
# and once in `rest`, and every number would still look plausible — the silent-
# arithmetic class this desk keeps finding. Fails LOUD at import, before any fetch.
_l_groups = {"T3": LAYER_T3, "PLATFORM": LAYER_PLATFORM, "LEGACY": LAYER_LEGACY}
for _a in _l_groups:
    for _b in _l_groups:
        if _a < _b:
            _dupe = set(_l_groups[_a]) & set(_l_groups[_b])
            assert not _dupe, f"layer overlap {_a}/{_b}: {sorted(_dupe)} — rest_pp would double-count"
assert len(LAYER_T3) == len(set(LAYER_T3)), "duplicate ticker inside the nested tiers"
assert set(LAYER_T1) <= set(LAYER_T2) <= set(LAYER_T3), "tiers are not nested"

LAYER_WINDOWS = [1, 5, 21, 63]   # 21 = the rolling-1mo basis S2/VULCAN-16 grade on
SHARE_FLOOR_PP = 1.0             # below this the ratio measures cancellation, not attribution

LAYER_COLS = ["asof_utc", "holdings_asof", "window_days", "index_ret_pp",
              "index_ret_arith_pp",
              "t1_pp", "t2_pp", "t3_pp", "platform_pp", "legacy_pp", "rest_pp",
              "t1_share_pct", "t2_share_pct", "t3_share_pct", "platform_share_pct",
              "share_state", "recon_err_pp", "n_priced", "excluded_weight_pct",
              "t1_weight_pct", "platform_weight_pct", "validation", "source"]


def _yf_ticker(t: str) -> str:
    """SSGA writes class shares with a dot; yfinance wants a dash (BRK.B -> BRK-B)."""
    return t.replace(".", "-")


def layer_contributions(h: dict, holdings_asof: str):
    """Decompose the index move into declared layers. Returns (rows, note).

    rows = list of dicts, one per window in LAYER_WINDOWS. On any failure returns
    ([], "ERR:<reason>") — no partial rows, no blanks
    [L-16: a partial run is a FAILED run, not a degraded one].
    """
    import yfinance as yf
    try:
        d = _dt.datetime.strptime(holdings_asof, "%d-%b-%Y").date()
    except ValueError:
        return [], f"ERR:unparseable-asof-{holdings_asof}"

    names = sorted(h.keys())
    tmap = {_yf_ticker(t): t for t in names}
    want = sorted(tmap.keys()) + ["SPY"]

    # ~250 calendar days back covers the 63-trading-day window with slack.
    start = d - _dt.timedelta(days=200)
    try:
        px = yf.download(want, start=start, end=d + _dt.timedelta(days=1),
                         progress=False, auto_adjust=True)["Close"]
    except Exception as e:  # noqa: BLE001
        return [], f"ERR:download-{type(e).__name__}"
    if px is None or px.empty or "SPY" not in px.columns:
        return [], "ERR:no-price-frame"
    px = px[px.index.date <= d]
    if len(px) < max(LAYER_WINDOWS) + 1:
        return [], f"ERR:insufficient-history-{len(px)}-rows"
    if px.index[-1].date() != d:
        return [], f"ERR:last-bar-{px.index[-1].date()}-not-holdings-asof-{d}"

    # A name is PRICED only if it has a clean close at both ends of the window.
    priced, excluded = {}, {}
    for yt, orig in tmap.items():
        if yt not in px.columns:
            excluded[orig] = h[orig][0]
            continue
        col = px[yt].dropna()
        if len(col) < max(LAYER_WINDOWS) + 1 or col.index[-1].date() != d:
            excluded[orig] = h[orig][0]
            continue
        priced[orig] = col
    if not priced:
        return [], "ERR:zero-priced-holdings"

    excl_w = sum(excluded.values())
    missing = {g: [t for t in grp if t not in priced]
               for g, grp in (("T1", LAYER_T1), ("T2", LAYER_T2), ("T3", LAYER_T3),
                              ("PLATFORM", LAYER_PLATFORM), ("LEGACY", LAYER_LEGACY))}
    miss_note = ";".join(f"{g}-missing:{','.join(v)}" for g, v in missing.items() if v)

    spy = px["SPY"].dropna()

    # --- DAILY-CHAINED weights [see WHY, above] -----------------------------
    # w_i,t is rebuilt each day from shares x close, so the weight PATH is used
    # rather than today's weight applied backwards.
    import pandas as _pd
    pxm = _pd.DataFrame({t: col for t, col in priced.items()}).dropna(how="all")
    pxm = pxm.ffill()
    shares = _pd.Series({t: h[t][1] for t in pxm.columns})
    mcap = pxm.mul(shares, axis=1)
    wts = mcap.div(mcap.sum(axis=1), axis=0) * 100.0     # percent, sums to 100
    rets = pxm.pct_change()
    dcontrib = wts.shift(1) * rets                        # START-of-day weight x that day's return
    spy_d = spy.pct_change() * 100.0

    out = []
    for w in LAYER_WINDOWS:
        seg = dcontrib.iloc[-w:]
        contrib = (seg.sum(axis=0)).to_dict()             # already in pp of index

        def grp(members):
            return sum(contrib.get(t, 0.0) for t in members)

        t1, t2, t3 = grp(LAYER_T1), grp(LAYER_T2), grp(LAYER_T3)
        plat, leg = grp(LAYER_PLATFORM), grp(LAYER_LEGACY)
        total = sum(contrib.values())
        rest = total - t3 - plat - leg
        idx = (float(spy.iloc[-1]) / float(spy.iloc[-1 - w]) - 1.0) * 100.0
        idx_arith = float(spy_d.iloc[-w:].sum())
        # LIKE-FOR-LIKE: contributions are an ARITHMETIC sum of daily w x r, so they
        # are validated against the ARITHMETIC sum of the index's daily returns, not
        # against the compounded move. Both are reported; the gap between them is
        # compounding, not error, and hiding either would misattribute one as the other.
        recon = total - idx_arith

        gradeable = abs(idx) >= SHARE_FLOOR_PP
        state = ("gradeable" if gradeable
                 else f"UNGRADEABLE:index-move-{idx:+.2f}pp-under-{SHARE_FLOOR_PP}pp-floor")

        def share(x):
            return f"{x / idx * 100.0:.1f}" if gradeable else "UNGRADEABLE"

        out.append({
            "window_days": w, "index_ret_pp": f"{idx:.4f}",
            "index_ret_arith_pp": f"{idx_arith:.4f}",
            "t1_pp": f"{t1:.4f}", "t2_pp": f"{t2:.4f}", "t3_pp": f"{t3:.4f}",
            "platform_pp": f"{plat:.4f}", "legacy_pp": f"{leg:.4f}",
            "rest_pp": f"{rest:.4f}",
            "t1_share_pct": share(t1), "t2_share_pct": share(t2),
            "t3_share_pct": share(t3), "platform_share_pct": share(plat),
            "share_state": state, "recon_err_pp": f"{recon:.4f}",
            "n_priced": str(len(contrib)),
            "excluded_weight_pct": f"{excl_w:.4f}",
            "t1_weight_pct": f"{sum(h[t][0] for t in LAYER_T1 if t in h):.4f}",
            "platform_weight_pct": f"{sum(h[t][0] for t in LAYER_PLATFORM if t in h):.4f}",
        })
    return out, (miss_note or "all-declared-members-priced")


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

    # --- sector-within-index leg (separate ledger, separate validation) ---
    print("\n  " + "-" * 68)
    print("  SECTOR-WITHIN-INDEX — contribution decomposition (S&P 500 via SPY)")
    print("  " + "-" * 68)
    lrows, lnote = layer_contributions(h, asof)
    if not lrows:
        print(f"  ERR — layer leg failed: {lnote}")
        print("  ⚠️ NO LAYER ROW WILL BE WRITTEN. The mag7 row is unaffected and is")
        print("     still written below — do NOT read that success as covering this leg.")
    else:
        print(f"  layer membership    {lnote}")
        print(f"  T1 weight {lrows[0]['t1_weight_pct']}%  ·  PLATFORM weight "
              f"{lrows[0]['platform_weight_pct']}%  ·  excluded weight "
              f"{lrows[0]['excluded_weight_pct']}%  ·  {lrows[0]['n_priced']} priced")
        print(f"  {'win':>4} {'index':>8} {'T1':>8} {'T2':>8} {'T3':>8} "
              f"{'PLATFM':>8} {'LEGACY':>8} {'REST':>8} {'recon':>7}  T1 share")
        for r in lrows:
            print(f"  {r['window_days']:>3}d {float(r['index_ret_pp']):>+8.2f} "
                  f"{float(r['t1_pp']):>+8.2f} {float(r['t2_pp']):>+8.2f} "
                  f"{float(r['t3_pp']):>+8.2f} {float(r['platform_pp']):>+8.2f} "
                  f"{float(r['legacy_pp']):>+8.2f} {float(r['rest_pp']):>+8.2f} "
                  f"{float(r['recon_err_pp']):>+7.2f}  "
                  + (f"{r['t1_share_pct']}%" if r['share_state'] == 'gradeable'
                     else "UNGRADEABLE"))
        print(f"  (all figures pp OF INDEX. share reported only when |index move| "
              f">= {SHARE_FLOOR_PP}pp;")
        print(f"   1d clears that on 25.2% of history — ungradeable is the EXPECTED "
              f"1d state, not a fault.)")

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

    if not lrows:
        print("  layer leg FAILED — workbook/LAYER_SERIES.tsv NOT written.")
        return 1
    lout = os.path.join(_root(), "AGENTS", "VULCAN", "workbook", "LAYER_SERIES.tsv")
    stamp = _dt.datetime.now(_dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    lnew = not os.path.exists(lout)
    with open(lout, "a") as f:
        if lnew:
            f.write("\t".join(LAYER_COLS) + "\n")
        for r in lrows:
            r = dict(r, asof_utc=stamp, holdings_asof=asof, validation=lnote,
                     source=("SSGA SPY daily holdings xlsx (issuer-primary) x yfinance "
                             "total-return closes; contributions = weight%% x return, "
                             "reconciled against SPY's own return"))
            f.write("\t".join(str(r[c]) for c in LAYER_COLS) + "\n")
    print(f"  appended -> workbook/LAYER_SERIES.tsv ({len(lrows)} rows, one per window)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
