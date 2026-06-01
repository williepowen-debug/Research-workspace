"""Diet coiled-spring backtest.

KB-VIO-036 STRICT signature (per research/2026-04-15_skew_divergence_episodes.md):
    20d window where ΔSKEW ≥ +10  AND  ΔVIX ≤ -5  AND  ΔVVIX ≤ -15
    19-yr backtest 2007-2026 → 46 trigger days / 17 episodes.

KB-VIO-062 DIET hypothesis (the 5/20→5/29 2026 window):
    Directional signature intact (ΔSKEW +11.87 ✅, ΔVIX -2.54, ΔVVIX -10.39)
    but VIX/VVIX magnitudes FALL SHORT of strict thresholds.
    Hypothesis: in GEX-suppressed regimes, the formal magnitude floor can't
    fire because realized vol cannot move enough; SKEW still expresses the
    tail bid because it measures option-price relative-cost, not magnitude.
    If true, KB-VIO-036's 94% hit rate has a LOWER effective magnitude floor
    in current regime.

This script tests the hypothesis. For each 20d window in 2007-2026:
    - Compute ΔSKEW / ΔVIX / ΔVVIX
    - Classify: STRICT_FIRE / DIET_FIRE / NEITHER
    - For each fire, compute forward 30d/60d VIX % change + peak

DIET threshold (KB-VIO-062 example-calibrated to just-include the 5/20-5/29 case):
    ΔSKEW ≥ +10  AND  ΔVIX ≤ -2  AND  ΔVVIX ≤ -10  AND  NOT STRICT

Outputs:
    workbook/DIET_COILED_SPRING.csv — every fire date with forward returns
    stdout summary — counts, base rates, forward distributions
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd
import yfinance as yf

ROOT = Path(__file__).resolve().parent.parent
OUT_CSV = ROOT / "workbook" / "DIET_COILED_SPRING.csv"

START = "2007-01-01"
END = "2026-06-02"
WINDOW = 20
FWD_30 = 30
FWD_60 = 60

STRICT_SKEW = 10.0
STRICT_VIX = -5.0
STRICT_VVIX = -15.0

DIET_SKEW = 10.0
DIET_VIX = -2.0
DIET_VVIX = -10.0


def pull() -> pd.DataFrame:
    tickers = {"^VIX": "vix", "^VVIX": "vvix", "^SKEW": "skew"}
    frames = []
    for t, c in tickers.items():
        print(f"[yfinance] {t}")
        df = yf.download(t, start=START, end=END, progress=False, auto_adjust=True)
        s = df["Close"].squeeze()
        s.name = c
        s.index = s.index.tz_localize(None)
        frames.append(s)
    out = pd.concat(frames, axis=1).dropna()
    print(f"  rows: {len(out)}  span: {out.index.min().date()} → {out.index.max().date()}")
    return out


def classify(df: pd.DataFrame) -> pd.DataFrame:
    """For each day t, compute window-end deltas (t vs t-WINDOW) and classify."""
    df = df.copy()
    df["d_skew"] = df["skew"] - df["skew"].shift(WINDOW)
    df["d_vix"] = df["vix"] - df["vix"].shift(WINDOW)
    df["d_vvix"] = df["vvix"] - df["vvix"].shift(WINDOW)

    strict = (df["d_skew"] >= STRICT_SKEW) & (df["d_vix"] <= STRICT_VIX) & (df["d_vvix"] <= STRICT_VVIX)
    diet_raw = (df["d_skew"] >= DIET_SKEW) & (df["d_vix"] <= DIET_VIX) & (df["d_vvix"] <= DIET_VVIX)
    diet_only = diet_raw & ~strict

    df["class"] = "NEITHER"
    df.loc[diet_only, "class"] = "DIET"
    df.loc[strict, "class"] = "STRICT"
    return df


def forward_returns(df: pd.DataFrame) -> pd.DataFrame:
    """Forward 30d / 60d VIX % change + peak VIX from each day."""
    df = df.copy()
    vix = df["vix"].values
    n = len(df)
    f30, f60, peak30, peak60 = [], [], [], []
    for i in range(n):
        if i + FWD_30 < n:
            f30.append((vix[i + FWD_30] / vix[i] - 1.0) * 100.0)
            peak30.append(float(vix[i + 1 : i + FWD_30 + 1].max()))
        else:
            f30.append(np.nan)
            peak30.append(np.nan)
        if i + FWD_60 < n:
            f60.append((vix[i + FWD_60] / vix[i] - 1.0) * 100.0)
            peak60.append(float(vix[i + 1 : i + FWD_60 + 1].max()))
        else:
            f60.append(np.nan)
            peak60.append(np.nan)
    df["fwd30_vix_pct"] = f30
    df["fwd60_vix_pct"] = f60
    df["fwd30_vix_peak"] = peak30
    df["fwd60_vix_peak"] = peak60
    df["fwd60_vix_peak_pct"] = (df["fwd60_vix_peak"] / df["vix"] - 1.0) * 100.0
    return df


def cluster_episodes(fire_dates: pd.DatetimeIndex, gap_td: int = 21) -> list[list[pd.Timestamp]]:
    """Group fire dates into episodes (consecutive trading-day clusters).

    Two fires within `gap_td` trading days = same episode.
    """
    if len(fire_dates) == 0:
        return []
    dates = sorted(fire_dates)
    eps = [[dates[0]]]
    for d in dates[1:]:
        if (d - eps[-1][-1]).days <= gap_td * 1.5:
            eps[-1].append(d)
        else:
            eps.append([d])
    return eps


def summarize(df: pd.DataFrame, label: str) -> dict:
    sub = df[df["class"] == label].dropna(subset=["fwd60_vix_pct"])
    if len(sub) == 0:
        return {"label": label, "n": 0}
    f30 = sub["fwd30_vix_pct"]
    f60 = sub["fwd60_vix_pct"]
    peak = sub["fwd60_vix_peak_pct"]
    return {
        "label": label,
        "n_fire_days": len(sub),
        "n_episodes": len(cluster_episodes(sub.index)),
        "f30_mean": float(f30.mean()),
        "f30_median": float(f30.median()),
        "f30_pct_pos": float((f30 > 0).mean() * 100),
        "f60_mean": float(f60.mean()),
        "f60_median": float(f60.median()),
        "f60_pct_pos": float((f60 > 0).mean() * 100),
        "f60_peak_mean": float(peak.mean()),
        "f60_peak_median": float(peak.median()),
        "f60_peak_gt_30": float((peak > 30).mean() * 100),
        "f60_peak_gt_50": float((peak > 50).mean() * 100),
        "f60_peak_gt_100": float((peak > 100).mean() * 100),
    }


def fmt_pct(v: float) -> str:
    return f"{v:+.1f}%" if not pd.isna(v) else "n/a"


def main() -> None:
    df = pull()
    df = classify(df)
    df = forward_returns(df)

    fires = df[df["class"].isin(["STRICT", "DIET"])].copy()
    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    fires.to_csv(OUT_CSV, index_label="date")

    print()
    print("=" * 72)
    print("  DIET COILED-SPRING BACKTEST  •  2007-01 → 2026-06")
    print("=" * 72)
    print(f"  Window:       {WINDOW} td")
    print(f"  STRICT:       ΔSKEW ≥ +{STRICT_SKEW}  ΔVIX ≤ {STRICT_VIX}  ΔVVIX ≤ {STRICT_VVIX}")
    print(f"  DIET:         ΔSKEW ≥ +{DIET_SKEW}  ΔVIX ≤ {DIET_VIX}  ΔVVIX ≤ {DIET_VVIX}  (and NOT STRICT)")
    print(f"  Forward:      VIX % change at +{FWD_30}td and +{FWD_60}td  +  peak VIX in next {FWD_60}td")
    print()

    valid = df.dropna(subset=["fwd60_vix_pct"])
    base_n = len(valid)
    print(f"  Universe (with valid fwd60):  {base_n} days")
    print()

    for label in ("STRICT", "DIET"):
        s = summarize(df, label)
        if s["n"] == 0 if "n" in s else False:
            print(f"  {label:7s}  no fires"); continue
        n = s["n_fire_days"]
        eps = s["n_episodes"]
        print(f"  {label:7s}  fires: {n:3d} days / {eps:2d} episodes  ({n/base_n*100:.2f}% of universe)")
        print(f"    fwd30 VIX %:    mean {fmt_pct(s['f30_mean']):>7s}  median {fmt_pct(s['f30_median']):>7s}  pct_pos {s['f30_pct_pos']:.0f}%")
        print(f"    fwd60 VIX %:    mean {fmt_pct(s['f60_mean']):>7s}  median {fmt_pct(s['f60_median']):>7s}  pct_pos {s['f60_pct_pos']:.0f}%")
        print(f"    fwd60 peak %:   mean {fmt_pct(s['f60_peak_mean']):>7s}  median {fmt_pct(s['f60_peak_median']):>7s}")
        print(f"    fwd60 peak hit-rate:  >+30% {s['f60_peak_gt_30']:.0f}%   >+50% {s['f60_peak_gt_50']:.0f}%   >+100% {s['f60_peak_gt_100']:.0f}%")
        print()

    # Base rate comparison for non-fire days
    neither = df[df["class"] == "NEITHER"].dropna(subset=["fwd60_vix_pct"])
    if len(neither):
        f60_n = neither["fwd60_vix_pct"]
        peak_n = neither["fwd60_vix_peak_pct"]
        print(f"  NEITHER  base rate: n={len(neither)}")
        print(f"    fwd60 VIX %:    mean {fmt_pct(float(f60_n.mean())):>7s}  median {fmt_pct(float(f60_n.median())):>7s}  pct_pos {(f60_n>0).mean()*100:.0f}%")
        print(f"    fwd60 peak %:   mean {fmt_pct(float(peak_n.mean())):>7s}  median {fmt_pct(float(peak_n.median())):>7s}")
        print(f"    fwd60 peak hit-rate:  >+30% {(peak_n>30).mean()*100:.0f}%   >+50% {(peak_n>50).mean()*100:.0f}%   >+100% {(peak_n>100).mean()*100:.0f}%")
        print()

    print(f"  Written: {OUT_CSV.relative_to(ROOT.parent.parent)}")
    print()

    # Episode tables for transparency
    for label in ("STRICT", "DIET"):
        sub = df[df["class"] == label]
        eps = cluster_episodes(sub.index)
        print(f"  {label} episodes (gap≤21td):  {len(eps)}")
        for i, e in enumerate(eps, 1):
            start = e[0].date()
            end = e[-1].date()
            row_at_end = df.loc[e[-1]]
            f60 = row_at_end.get("fwd60_vix_pct", np.nan)
            peak = row_at_end.get("fwd60_vix_peak_pct", np.nan)
            print(f"    {i:2d}. {start} → {end}  ({len(e)}d)  fwd60: {fmt_pct(float(f60)):>7s}  peak: {fmt_pct(float(peak)):>7s}")
        print()


if __name__ == "__main__":
    main()
