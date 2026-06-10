#!/usr/bin/env python3
"""convexity_read.py — Convexity-Pricing Rubric (Packet #2, v0 2026-06-09).

Answers the EXPRESSION question, not the forecast question:
is the tail cheap or rich, decomposed by what you'd actually be buying,
and given a view, which structure is the cheapest way to express it.

Forecast/conviction lives in the L1-L4 stack (Packet #1 / VIX_THESIS).
This rubric NEVER sizes: sizing = stack conviction x structure unit, Will-gated.

Components priced as PERCENTILES vs trailing history, never absolute levels:
  - Term-structure shape: event-kink vs sustained stress; belly slope
  - Vol-of-vol (VVIX): unconditional AND VIX-bucket-conditional percentile
  - Tail skew (SKEW): OTM tail cost
  - Implied-realized spread: VIX vs 10d/20d realized, close-to-close AND
    Parkinson (CC >> Parkinson = gap-risk tape; CC ~= Parkinson = grind)

Usage:  .venv/bin/python3 AGENTS/VIOLET/scripts/convexity_read.py [--json]
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import numpy as np
import pandas as pd
import yfinance as yf

ET = ZoneInfo("America/New_York")
SCRIPT_DIR = Path(__file__).resolve().parent
DAILY_LOG = SCRIPT_DIR.parent / "workbook" / "VX_DAILY.tsv"

TACTICAL_WIN = 252      # 1yr trading days
STRUCTURAL_WIN = 1260   # 5yr trading days
CHEAP_PCT = 25.0
RICH_PCT = 75.0
# VIX buckets mirror MEMORY.md regime definitions
VIX_BUCKETS = [(0, 15, "<15"), (15, 20, "15-20"), (20, 30, "20-30"), (30, 999, ">30")]


def pct_rank(series: pd.Series, value: float) -> float:
    s = series.dropna()
    if len(s) == 0:
        return float("nan")
    return float((s < value).mean() * 100)


def verdict(p: float) -> str:
    if math.isnan(p):
        return "n/a"
    if p <= CHEAP_PCT:
        return "CHEAP"
    if p >= RICH_PCT:
        return "RICH"
    return "NEUTRAL"


def normalize_dates(s: pd.Series) -> pd.Series:
    """yfinance returns ^VIX in America/Chicago but ^VVIX/^SKEW in
    America/New_York — joining on raw timestamps silently drops rows.
    Re-key everything to plain dates."""
    s = s.copy()
    s.index = pd.to_datetime(s.index).date
    return s[~pd.Index(s.index).duplicated(keep="last")]


def fetch_history(ticker: str, days: int) -> pd.Series:
    h = yf.Ticker(ticker).history(period=f"{max(days + 30, 260)}d")
    return normalize_dates(h["Close"].dropna()) if not h.empty else pd.Series(dtype=float)


def latest(series: pd.Series) -> float:
    return float(series.iloc[-1]) if len(series) else float("nan")


def realized_vols(spx: pd.DataFrame) -> dict:
    out = {}
    logret = np.log(spx["Close"] / spx["Close"].shift(1)).dropna()
    hl = np.log(spx["High"] / spx["Low"]).dropna()
    for win in (10, 20):
        cc = float(logret.tail(win).std(ddof=1) * math.sqrt(252) * 100)
        park = float(
            math.sqrt((hl.tail(win) ** 2).mean() / (4 * math.log(2))) * math.sqrt(252) * 100
        )
        out[win] = {"cc": round(cc, 2), "parkinson": round(park, 2)}
    return out


def m1m2_from_ledger() -> tuple[float | None, str]:
    """Latest M1:M2 adjusted contango from VX_DAILY.tsv (with its date)."""
    if not DAILY_LOG.exists():
        return None, ""
    try:
        df = pd.read_csv(DAILY_LOG, sep="\t")
        df = df[pd.to_numeric(df["m1m2_adj_pct"], errors="coerce").notna()]
        if df.empty:
            return None, ""
        row = df.iloc[-1]
        return float(row["m1m2_adj_pct"]), str(row["date"])
    except Exception:
        return None, ""


def build() -> dict:
    # --- live-ish quotes (last close / intraday last) ---
    vix_h = normalize_dates(yf.Ticker("^VIX").history(period=f"{STRUCTURAL_WIN + 60}d")["Close"].dropna())
    vvix_h = normalize_dates(yf.Ticker("^VVIX").history(period=f"{STRUCTURAL_WIN + 60}d")["Close"].dropna())
    skew_h = normalize_dates(yf.Ticker("^SKEW").history(period=f"{STRUCTURAL_WIN + 60}d")["Close"].dropna())
    vix9d = latest(fetch_history("^VIX9D", 10))
    vix3m = latest(fetch_history("^VIX3M", 10))
    vix6m = latest(fetch_history("^VIX6M", 10))
    # 450 calendar days ≈ 300 trading days: covers TACTICAL_WIN (252)
    # + 20d rolling warm-up so the "1yr percentile" label is honest
    spx = yf.Ticker("^GSPC").history(period="450d")

    vix, vvix, skew = latest(vix_h), latest(vvix_h), latest(skew_h)
    rv = realized_vols(spx)
    m1m2, m1m2_date = m1m2_from_ledger()

    # --- term shape classification ---
    kink_front = vix9d > vix if not math.isnan(vix9d) else False
    contango_belly = vix3m > vix and vix6m > vix3m
    if kink_front and contango_belly:
        shape = "EVENT-KINK on contango belly (front prices a dated event; belly calm)"
    elif vix > vix3m and vix3m > vix6m:
        shape = "SUSTAINED STRESS (full backwardation)"
    elif vix > vix3m:
        shape = "FRONT INVERSION past 3M (stress building)"
    else:
        shape = "CLEAN CONTANGO (no near event premium)"

    # --- VVIX percentiles: tactical, structural, VIX-bucket-conditional ---
    vvix_tac = pct_rank(vvix_h.tail(TACTICAL_WIN), vvix)
    vvix_str = pct_rank(vvix_h.tail(STRUCTURAL_WIN), vvix)
    joint = pd.DataFrame({"vix": vix_h, "vvix": vvix_h}).dropna().tail(STRUCTURAL_WIN)
    bucket_label, vvix_cond = "n/a", float("nan")
    for lo, hi, label in VIX_BUCKETS:
        if lo <= vix < hi:
            bucket_label = label
            sub = joint[(joint["vix"] >= lo) & (joint["vix"] < hi)]["vvix"]
            if len(sub) >= 60:
                vvix_cond = pct_rank(sub, vvix)
            break

    # --- SKEW percentiles ---
    skew_tac = pct_rank(skew_h.tail(TACTICAL_WIN), skew)
    skew_str = pct_rank(skew_h.tail(STRUCTURAL_WIN), skew)

    # --- implied-realized spread (anchor: 20d CC), percentiled on 1yr ---
    # Date-keyed join, NOT positional: ^VIX trades on days SPX data can lag
    # (and vice versa on holidays — see MEMORY phantom-print caveat); a
    # positional subtraction shifts the whole spread history on any mismatch.
    spread20 = vix - rv[20]["cc"]
    logret = np.log(spx["Close"] / spx["Close"].shift(1)).dropna()
    rv20_series = normalize_dates(logret.rolling(20).std(ddof=1) * math.sqrt(252) * 100)
    spread_joined = pd.DataFrame({"vix": vix_h, "rv20": rv20_series}).dropna()
    spread_series = spread_joined["vix"] - spread_joined["rv20"]
    spread_pct = pct_rank(spread_series.tail(TACTICAL_WIN), spread20)
    gap_tell = ("GAP-RISK tape (CC >> Parkinson)" if rv[20]["cc"] > rv[20]["parkinson"] * 1.25
                else "GRIND tape (CC ~= Parkinson)")

    # --- event-premium curve location (refinement 4: hump isn't always front) ---
    locs = []
    if kink_front:
        locs.append(f"VIX9D kink (+{vix9d - vix:.2f} over spot)")
    if m1m2 is not None and m1m2 > 5.0:
        locs.append(f"M1:M2 hump (+{m1m2:.2f}% adj, as of {m1m2_date})")
    hump_loc = "; ".join(locs) if locs else "no pronounced event premium located"

    components = {
        "term_shape": {"desc": shape, "vix9d": vix9d, "vix": vix, "vix3m": vix3m,
                       "vix6m": vix6m, "m1m2_adj_pct": m1m2, "hump_location": hump_loc},
        "vol_of_vol": {"vvix": vvix, "pct_1yr": round(vvix_tac, 1),
                       "pct_5yr": round(vvix_str, 1),
                       "pct_cond_vix_bucket": round(vvix_cond, 1) if not math.isnan(vvix_cond) else None,
                       "vix_bucket": bucket_label,
                       "verdict_tactical": verdict(vvix_tac),
                       "verdict_conditional": verdict(vvix_cond)},
        "tail_skew": {"skew": skew, "pct_1yr": round(skew_tac, 1),
                      "pct_5yr": round(skew_str, 1), "verdict": verdict(skew_tac)},
        "implied_realized": {"vix": vix, "rv10": rv[10], "rv20": rv[20],
                             "spread_vs_rv20cc": round(spread20, 2),
                             "spread_pct_1yr": round(spread_pct, 1),
                             "verdict": verdict(spread_pct), "tape_tell": gap_tell},
    }

    # --- expression map ---
    vov_cheap = verdict(vvix_cond if not math.isnan(vvix_cond) else vvix_tac) == "CHEAP"
    skew_rich = verdict(skew_tac) == "RICH"
    expression = {
        "own_vertical_tail": (
            ("VIX calls / vol-of-vol structures — VVIX " +
             ("CHEAP" if vov_cheap else "NOT cheap") + " on conditional read")
            + ("; AVOID naked OTM index puts (SKEW rich)" if skew_rich
               else "; OTM puts acceptable (SKEW not rich)")),
        "fade_event_premium": (
            f"Sell the located hump [{hump_loc}] via calendar/ratio "
            "(short rich tenor vs long adjacent), NOT naked short-gamma through the event"),
        "cheap_downside": (
            "Put-spread / spread-collar (finance the rich skew)" if skew_rich
            else "Outright puts viable (skew not rich)"),
    }

    # --- carry/bleed flag (mandatory on any own-convexity call) ---
    carry = {
        "iv_rv_carry": f"Own-vol bleeds ~{spread20:+.1f} vol-pts of IV-RV spread "
                       f"({verdict(spread_pct)} at {spread_pct:.0f}th pct 1yr)",
        "curve_roll": (f"Long M2 rolls DOWN ~{m1m2:.1f}%/month toward M1 if curve static "
                       f"(seller of M2 COLLECTS this)" if m1m2 is not None and m1m2 > 0
                       else "Curve flat/inverted — roll-down not a bleed"),
        "note": "v0 has no live option-chain theta; per-structure theta lands with SPX/VIX chain in v1",
    }

    return {
        "asof": datetime.now(ET).strftime("%Y-%m-%d %H:%M ET"),
        "components": components,
        "expression": expression,
        "carry": carry,
        "handoff": "Conviction = L1-L4 stack (Packet #1). This rubric prices structure only. "
                   "Sizing = conviction x structure unit, Will-gated at FORGE.",
    }


def print_report(r: dict) -> None:
    c = r["components"]
    print(f"CONVEXITY READ  {r['asof']}")
    print("=" * 70)
    t = c["term_shape"]
    print(f"  TERM SHAPE   {t['desc']}")
    print(f"               9D {t['vix9d']:.2f} | spot {t['vix']:.2f} | 3M {t['vix3m']:.2f} "
          f"| 6M {t['vix6m']:.2f} | M1:M2 adj {t['m1m2_adj_pct'] if t['m1m2_adj_pct'] is not None else 'n/a'}%")
    print(f"               event premium located: {t['hump_location']}")
    v = c["vol_of_vol"]
    print(f"  VOL-OF-VOL   VVIX {v['vvix']:.2f} -> {v['pct_1yr']}th pct 1yr / {v['pct_5yr']}th 5yr "
          f"/ {v['pct_cond_vix_bucket']}th cond(VIX {v['vix_bucket']})")
    print(f"               verdict: {v['verdict_tactical']} tactical, {v['verdict_conditional']} conditional")
    s = c["tail_skew"]
    print(f"  TAIL SKEW    SKEW {s['skew']:.2f} -> {s['pct_1yr']}th pct 1yr / {s['pct_5yr']}th 5yr "
          f"-> {s['verdict']}")
    ir = c["implied_realized"]
    print(f"  IV-RV        VIX {ir['vix']:.2f} vs RV20 cc {ir['rv20']['cc']} / park {ir['rv20']['parkinson']} "
          f"(RV10 cc {ir['rv10']['cc']} / park {ir['rv10']['parkinson']})")
    print(f"               spread {ir['spread_vs_rv20cc']:+.2f} -> {ir['spread_pct_1yr']}th pct 1yr "
          f"-> {ir['verdict']} | {ir['tape_tell']}")
    print("-" * 70)
    print("  EXPRESSION")
    for k, val in r["expression"].items():
        print(f"    {k:22s} {val}")
    print("  CARRY/BLEED (mandatory)")
    for k, val in r["carry"].items():
        print(f"    {k:22s} {val}")
    print("-" * 70)
    print(f"  HANDOFF  {r['handoff']}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    try:
        report = build()
    except Exception as e:
        print(f"convexity_read failed: {e}", file=sys.stderr)
        sys.exit(1)
    if args.json:
        print(json.dumps(report, indent=2, default=str))
    else:
        print_report(report)
