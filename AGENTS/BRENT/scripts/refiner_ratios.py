#!/usr/bin/env python3
"""Historical refiner/USO research code; CLI retired September 9, 2026.

Reference: research/archive/PRODUCT_SIDE_DECOUPLING_THESIS.md.
The executable entry point now only prints a retirement notice. It performs no
network retrieval or TSV write. Functions below preserve the old research
implementation and its historical interpretations, not current trade authority.
Recommissioning requires an identified current research reader and validated
observation basis; the July 1 TSV is historical.
"""

import os
import sys
from datetime import datetime, date
from pathlib import Path

try:
    import yfinance as yf
except ImportError:
    print("  ERROR: yfinance not installed.")
    sys.exit(1)

REFINERS = ["MPC", "PSX", "VLO", "DINO", "PBF"]
CRUDE_PROXY = "USO"
ALL_TICKERS = REFINERS + [CRUDE_PROXY]

SCRIPT_DIR = Path(__file__).resolve().parent
DATA_DIR = SCRIPT_DIR / "data"
TSV_PATH = DATA_DIR / "refiner_ratios.tsv"

Z_WARN = 1.0
Z_STRONG = 2.0


def fetch_history(period="6mo"):
    """Return dict ticker -> list of (date, close) tuples."""
    data = yf.download(
        ALL_TICKERS,
        period=period,
        interval="1d",
        auto_adjust=True,
        progress=False,
        group_by="ticker",
        threads=True,
    )
    out = {}
    for t in ALL_TICKERS:
        try:
            closes = data[t]["Close"].dropna()
            out[t] = [(idx.date(), float(v)) for idx, v in closes.items()]
        except Exception as e:
            print(f"  WARN: no history for {t}: {e}")
            out[t] = []
    return out


def compute_ratio_series(history):
    """Given history dict, return dict ticker -> list of (date, ratio) for refiners."""
    uso = dict(history[CRUDE_PROXY])
    series = {}
    for t in REFINERS:
        pairs = []
        for d, close in history[t]:
            uso_close = uso.get(d)
            if uso_close and uso_close > 0:
                pairs.append((d, close / uso_close))
        series[t] = pairs
    return series


def stats(values):
    """Mean + population stdev. Returns (mean, stdev)."""
    if not values:
        return (0.0, 0.0)
    n = len(values)
    m = sum(values) / n
    var = sum((v - m) ** 2 for v in values) / n
    return (m, var ** 0.5)


def analyze(ratio_series):
    """Compute per-ticker stats and today's z-score."""
    rows = []
    for t, pairs in ratio_series.items():
        if len(pairs) < 20:
            continue
        values = [v for _, v in pairs]
        mean, sd = stats(values)
        today_date, today_ratio = pairs[-1]
        prev_ratio = pairs[-2][1] if len(pairs) >= 2 else today_ratio
        z = (today_ratio - mean) / sd if sd > 0 else 0.0
        chg_1d = (today_ratio - prev_ratio) / prev_ratio * 100 if prev_ratio else 0.0
        rows.append({
            "ticker": t,
            "date": today_date,
            "ratio": today_ratio,
            "mean_6mo": mean,
            "sd_6mo": sd,
            "z": z,
            "chg_1d_pct": chg_1d,
        })
    return rows


def classify(z, chg_1d):
    """Mean-reversion interpretation: compressed ratio + rising = entry signal."""
    if z >= Z_WARN:
        return "🟠 EXHAUSTED"
    if z <= -Z_WARN and chg_1d >= 1.0:
        return "🟢 REVERTING"
    if z <= -Z_WARN:
        return "🟡 COMPRESSED"
    return "⚪ NORMAL"


def print_report(rows, as_of):
    print("=" * 78)
    print(f"  BRENT REFINER-CRUDE RATIO MONITOR   as of {as_of}")
    print("=" * 78)
    print(f"  Thesis: product-side decoupling (see PRODUCT_SIDE_DECOUPLING_THESIS.md)")
    print(f"  Baseline: 6-mo daily close-to-close ratio vs USO")
    print()
    print(f"  {'Ticker':<8}{'Ratio':>10}{'6mo μ':>10}{'6mo σ':>10}{'z-score':>10}{'1d Δ%':>10}  Signal")
    print(f"  {'-'*68}")
    rows_sorted = sorted(rows, key=lambda r: -r["chg_1d_pct"])
    for r in rows_sorted:
        print(
            f"  {r['ticker']:<8}{r['ratio']:>10.3f}{r['mean_6mo']:>10.3f}"
            f"{r['sd_6mo']:>10.3f}{r['z']:>+10.2f}{r['chg_1d_pct']:>+10.2f}"
            f"  {classify(r['z'], r['chg_1d_pct'])}"
        )
    print()

    reverting = [r for r in rows if r["z"] <= -Z_WARN and r["chg_1d_pct"] >= 1.0]
    exhausted = [r for r in rows if r["z"] >= Z_WARN]
    mean_chg = sum(r["chg_1d_pct"] for r in rows) / len(rows)

    if reverting:
        print("  🟢 DECOUPLING ENTRY FIRING (compressed + reverting):")
        for r in reverting:
            print(f"     {r['ticker']}  z={r['z']:+.2f}  1dΔ={r['chg_1d_pct']:+.1f}%")
    if exhausted:
        print("  🟠 REVERSION EXHAUSTED (consider exit):")
        for r in exhausted:
            print(f"     {r['ticker']}  z={r['z']:+.2f}  1dΔ={r['chg_1d_pct']:+.1f}%")

    agg_signal = "🟢 CONFIRMED" if mean_chg >= 1.0 else "⚪ quiet"
    print(f"  AGGREGATE 1d Δ across refiners: {mean_chg:+.2f}%  [{agg_signal}]")
    print()


def append_tsv(rows):
    DATA_DIR.mkdir(exist_ok=True)
    header = "date\tticker\tratio\tmean_6mo\tsd_6mo\tz\tchg_1d_pct\n"
    new_file = not TSV_PATH.exists()
    with open(TSV_PATH, "a") as f:
        if new_file:
            f.write(header)
        for r in rows:
            f.write(
                f"{r['date']}\t{r['ticker']}\t{r['ratio']:.5f}\t"
                f"{r['mean_6mo']:.5f}\t{r['sd_6mo']:.5f}\t{r['z']:.3f}\t"
                f"{r['chg_1d_pct']:.3f}\n"
            )
    print(f"  Appended {len(rows)} row(s) to {TSV_PATH.relative_to(SCRIPT_DIR.parent.parent.parent)}")


def main():
    # Supersedes the automatic fetch/write and obsolete entry/exit readout.
    # Preserve analysis functions as historical code; recommissioning requires
    # a current research reader and separately validated observation basis.
    print("RETIRED: this historical research entry point no longer fetches or writes data.")
    print("Reference: AGENTS/BRENT/research/archive/PRODUCT_SIDE_DECOUPLING_THESIS.md")
    print("Its historical z-score scheme is not a current entry/exit rule.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
