#!/usr/bin/env python3
"""VIOLET H3 test — does the FRONT VX BASIS invert BEFORE the VIX3M/VIX index ratio?

THE HYPOTHESIS (SCRATCH 7/29, thesis v3.8 "open, not tradeable"): stand-down (ii)
reads the CASH INDEX ratio VIX3M/VIX < 1.0. On 2026-07-29 the front VX basis
(spot - M1 settlement) inverted to -0.35 while that ratio still read 1.0407. If the
strip systematically leads the index ratio, then (ii) is a SYSTEMATICALLY LATE
peak-marker — the same instrument-mismatch family as KB-VIO-129 (the guard reads
one instrument, the position settles on another).

WHY THIS MATTERS BEYOND ONE GUARD: KB-VIO-034 established term-structure inversion
as a PEAK-marker (553 obs, 2.2% hit rate as an onset predictor, mean -5% forward) —
i.e. it is an EXIT-TIMING instrument. An exit-timing signal that fires late is
strictly worse than one that fires early, so the lead/lag is the whole value.

METHOD
  - Calendar = ^VIX trading days from yfinance.
  - M1 = nearest-expiry standard VX contract from CBOE's per-date settlement CSV.
  - front_basis = M1_settle - VIX_spot      ⚠️ SIGN CONVENTION: this matches STATUS.md
        ("spot 20.66 > VX/Q6 20.3094 = -0.35"). NEGATIVE = BACKWARDATION = spot above
        the front future = the stress shape. POSITIVE = contango = normal.
        ⚠️ v1 of this script used `spot - M1` and called negative "backwardation",
        which is exactly inverted. It fired on 85.9% of days with ZERO overlap with
        ratio-inversion — it was measuring CONTANGO, the normal state. Caught only by
        computing the base rate; the peak table alone looked like clean H3 support.
        A signal that fires 86% of the time has no discriminating power, and the
        zero-overlap anomaly is what exposed the sign error. Always base-rate a new
        instrument before reading its event table.
  - index_ratio = VIX3M / VIX               (below 1.0 = inverted)
  - Episode peaks = local VIX maxima over +/-PEAK_WIN td with VIX >= PEAK_MIN.
  - For each peak, look back LOOKBACK td and record the FIRST inversion date on each
    instrument; lead = (ratio_first_date - basis_first_date) in trading days.

⚠️ THE CONFOUND, HANDLED EXPLICITLY: as M1 approaches expiry it converges to spot
mechanically, so the basis tends toward 0 (and noisily through it) for reasons that
have nothing to do with stress. Rows with dte < MIN_DTE are therefore EXCLUDED, and
--min-dte lets you test the result's sensitivity to that choice. A finding that
survives only at one dte floor is an artifact of the floor.

⚠️ n IS SMALL BY CONSTRUCTION. CBOE serves settlement one HTTP request per date, so
a 20-year pull is ~5,000 requests. This runs a 2-year window (~500 requests, ~3 min)
covering the Aug-2024 carry unwind, Apr-2025 tariff spike, Mar-2026 stress episode
and the Jun-2026 NFP shock. That is a handful of episode peaks — enough for a
DIRECTIONAL read, NOT enough to promote H3 out of "open". Report n with the result.

Usage:
  .venv/bin/python3 AGENTS/VIOLET/scripts/h3_basis_lead.py --start 2024-07-01
  .venv/bin/python3 AGENTS/VIOLET/scripts/h3_basis_lead.py --min-dte 3 --peak-min 22
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import date, datetime
from pathlib import Path

WORKSPACE = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(WORKSPACE / "FORGE" / "tools" / "market-data"))

PEAK_WIN = 10      # td each side for the local-max test
PEAK_MIN = 20.0    # only grade peaks that reached a stress level worth exiting into
LOOKBACK = 30      # td before the peak to search for a first inversion
MIN_DTE = 5        # exclude M1 rows inside this many days of expiry (convergence)


def load_spot(start: str, end: str):
    import yfinance as yf
    out = {}
    for key, sym in (("vix", "^VIX"), ("vix3m", "^VIX3M")):
        h = yf.Ticker(sym).history(start=start, end=end, interval="1d")
        out[key] = {d.date(): float(v) for d, v in h["Close"].items() if v == v}
    return out


def load_m1(days, min_dte: int, verbose: bool = False):
    import vix_futures as vf
    m1 = {}
    for i, d in enumerate(days):
        try:
            rows = vf.fetch_settlement(d)
        except Exception:
            continue
        fut = sorted(
            [r for r in rows if r.get("expiration") and r.get("price")],
            key=lambda r: r["expiration"],
        )
        # nearest contract that still has real life left in it
        for r in fut:
            dte = (r["expiration"] - d).days
            if dte >= min_dte:
                m1[d] = {"price": float(r["price"]), "symbol": r["symbol"], "dte": dte}
                break
        if verbose and i % 50 == 0:
            print(f"    ... {i}/{len(days)} {d}", file=sys.stderr)
    return m1


def first_inversion(series, peak_i, lookback, pred):
    """First index in [peak_i-lookback, peak_i] where pred(value) holds."""
    lo = max(0, peak_i - lookback)
    for i in range(lo, peak_i + 1):
        v = series[i]
        if v is not None and pred(v):
            return i
    return None


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--start", default="2025-08-01")  # CBOE serves ~12mo rolling; see CBOE_EPOCH note
    ap.add_argument("--end", default=None)
    ap.add_argument("--min-dte", type=int, default=MIN_DTE)
    ap.add_argument("--peak-min", type=float, default=PEAK_MIN)
    ap.add_argument("--peak-win", type=int, default=PEAK_WIN)
    ap.add_argument("--lookback", type=int, default=LOOKBACK)
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args(argv)
    end = a.end or date.today().isoformat()

    spot = load_spot(a.start, end)
    days = sorted(spot["vix"])
    print(f"calendar: {len(days)} trading days {days[0]} -> {days[-1]}", file=sys.stderr)
    print(f"pulling CBOE settlement (1 request/date, ~0.3s each)...", file=sys.stderr)
    m1 = load_m1(days, a.min_dte, verbose=True)
    print(f"M1 resolved for {len(m1)}/{len(days)} days (min_dte={a.min_dte})", file=sys.stderr)

    rows = []
    for d in days:
        v = spot["vix"].get(d)
        v3 = spot["vix3m"].get(d)
        f = m1.get(d)
        rows.append({
            "date": d,
            "vix": v,
            "basis": (f["price"] - v) if (v is not None and f) else None,
            "ratio": (v3 / v) if (v and v3) else None,
            "m1": f["price"] if f else None,
            "dte": f["dte"] if f else None,
        })

    vix = [r["vix"] for r in rows]
    basis = [r["basis"] for r in rows]
    ratio = [r["ratio"] for r in rows]

    # local maxima
    peaks = []
    for i in range(a.peak_win, len(rows) - a.peak_win):
        v = vix[i]
        if v is None or v < a.peak_min:
            continue
        window = [x for x in vix[i - a.peak_win:i + a.peak_win + 1] if x is not None]
        if window and v == max(window):
            if peaks and (i - peaks[-1]) <= a.peak_win:
                if v > vix[peaks[-1]]:
                    peaks[-1] = i
                continue
            peaks.append(i)

    results = []
    for pi in peaks:
        bi = first_inversion(basis, pi, a.lookback, lambda x: x < 0)
        ri = first_inversion(ratio, pi, a.lookback, lambda x: x < 1.0)
        lead = None
        if bi is not None and ri is not None:
            lead = ri - bi          # >0 = basis inverted FIRST (H3 supported)
        results.append({
            "peak_date": str(rows[pi]["date"]),
            "peak_vix": round(vix[pi], 2),
            "basis_first": str(rows[bi]["date"]) if bi is not None else None,
            "ratio_first": str(rows[ri]["date"]) if ri is not None else None,
            "lead_td": lead,
        })

    supported = [r for r in results if r["lead_td"] is not None and r["lead_td"] > 0]
    tied = [r for r in results if r["lead_td"] == 0]
    against = [r for r in results if r["lead_td"] is not None and r["lead_td"] < 0]
    basis_only = [r for r in results if r["basis_first"] and not r["ratio_first"]]
    ratio_only = [r for r in results if r["ratio_first"] and not r["basis_first"]]
    neither = [r for r in results if not r["basis_first"] and not r["ratio_first"]]

    out = {
        "params": {"start": a.start, "end": end, "min_dte": a.min_dte,
                   "peak_min": a.peak_min, "peak_win": a.peak_win,
                   "lookback": a.lookback},
        "n_days": len(days), "n_m1_days": len(m1), "n_peaks": len(results),
        "both_inverted": len(supported) + len(tied) + len(against),
        "basis_led": len(supported), "tied": len(tied), "ratio_led": len(against),
        "basis_only": len(basis_only), "ratio_only": len(ratio_only),
        "neither": len(neither),
        "leads_td": [r["lead_td"] for r in results if r["lead_td"] is not None],
        "peaks": results,
    }
    if a.json:
        print(json.dumps(out, indent=1))
        return 0

    print()
    print("=" * 72)
    print(f"H3 — front VX basis vs VIX3M/VIX index ratio, as PEAK-markers")
    print("=" * 72)
    print(f"window {a.start} -> {end} | {len(days)} td | M1 on {len(m1)} | min_dte={a.min_dte}")
    print(f"peaks: local VIX max +/-{a.peak_win}td with VIX >= {a.peak_min}; lookback {a.lookback}td")
    print()
    print(f"{'peak':12s} {'VIX':>6s}  {'basis<0 first':>13s} {'ratio<1 first':>13s} {'lead(td)':>9s}")
    for r in results:
        lead = "—" if r["lead_td"] is None else f"{r['lead_td']:+d}"
        print(f"{r['peak_date']:12s} {r['peak_vix']:6.2f}  "
              f"{str(r['basis_first'] or '—'):>13s} {str(r['ratio_first'] or '—'):>13s} {lead:>9s}")
    print()
    print(f"  n peaks = {len(results)}")
    print(f"  both inverted   : {out['both_inverted']}  -> basis led {len(supported)} | tied {len(tied)} | ratio led {len(against)}")
    print(f"  basis ONLY      : {len(basis_only)}   (ratio never inverted — basis caught a peak the guard missed entirely)")
    print(f"  ratio ONLY      : {len(ratio_only)}")
    print(f"  neither         : {len(neither)}")
    if out["leads_td"]:
        L = sorted(out["leads_td"])
        med = L[len(L) // 2] if len(L) % 2 else (L[len(L)//2 - 1] + L[len(L)//2]) / 2
        print(f"  lead when both fired: median {med:+.1f} td, range {L[0]:+d}..{L[-1]:+d}")
    print()
    print("  ⚠️  n is small by construction. Directional read only — do NOT promote H3")
    print("      out of 'open' on this alone, and re-run with --min-dte 3 and 8 to")
    print("      confirm the sign is not an artifact of the expiry-convergence filter.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
