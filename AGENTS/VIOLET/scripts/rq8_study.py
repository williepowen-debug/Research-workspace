"""
RQ #8 — Rates-vol → equity-vol base-rate study.

Cohort:    MOVE 2d change >= 30%, 3-day de-dup keeping first.
Horizons:  T+0, T+1, T+3, T+5, T+10.
Metrics:   VIX / VIX3M/VIX ratio / VVIX per event per horizon,
           plus percent change vs T-1.
Baseline:  unconditional distribution of same forward-k VIX % changes.

Pre-registration is `research/2026-09-24_RQ-8_move-2d-jump-forward-vix.md` §1.
Report writer fills §2-6.

Usage:  python3 scripts/rq8_study.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd
import yfinance as yf


HORIZONS = [0, 1, 3, 5, 10]
COHORT_THRESHOLD = 0.30
DEDUP_WINDOW_TD = 3


def pull_series() -> pd.DataFrame:
    tickers = ["^MOVE", "^VIX", "^VIX3M", "^VVIX"]
    frames = {}
    for t in tickers:
        h = yf.Ticker(t).history(period="max")
        if h.empty:
            print(f"WARN: no data for {t}", file=sys.stderr)
            continue
        s = h["Close"].copy()
        s.index = pd.to_datetime(s.index).tz_localize(None).normalize()
        frames[t] = s
    df = pd.DataFrame(frames)
    df = df.dropna(subset=["^MOVE"])
    return df


def identify_cohort(df: pd.DataFrame) -> pd.DataFrame:
    """Events where MOVE 2d pct_change >= COHORT_THRESHOLD, then 3-td de-dup."""
    move = df["^MOVE"]
    pct2 = move.pct_change(2)
    raw_events = pct2[pct2 >= COHORT_THRESHOLD]
    idx = raw_events.index.tolist()

    # 3-td de-dup: keep first, drop any within 3 trading days of a prior kept event
    dates = df.index.tolist()
    date_to_pos = {d: i for i, d in enumerate(dates)}
    kept: list[pd.Timestamp] = []
    last_kept_pos = -10**9
    for d in idx:
        p = date_to_pos[d]
        if p - last_kept_pos > DEDUP_WINDOW_TD:
            kept.append(d)
            last_kept_pos = p

    cohort = pd.DataFrame(
        {
            "event_date": kept,
            "move_t_minus_2": [move.shift(2).loc[d] for d in kept],
            "move_t_minus_1": [move.shift(1).loc[d] for d in kept],
            "move_t0": [move.loc[d] for d in kept],
            "move_2d_pct": [pct2.loc[d] for d in kept],
        }
    )
    return cohort


def forward_paths(df: pd.DataFrame, cohort: pd.DataFrame) -> pd.DataFrame:
    """For each event, extract VIX/VIX3M-ratio/VVIX at T+0 through T+10."""
    dates = df.index.tolist()
    date_to_pos = {d: i for i, d in enumerate(dates)}
    rows = []
    for _, ev in cohort.iterrows():
        d0 = ev["event_date"]
        p0 = date_to_pos[d0]
        if p0 - 1 < 0:
            continue
        # T-1 baseline (session before the 2d window began = T-2 relative to T0)
        d_baseline = dates[p0 - 1]
        vix_tm1 = df["^VIX"].iloc[p0 - 1]

        for k in HORIZONS:
            p = p0 + k
            if p >= len(dates):
                break
            d = dates[p]
            vix_val = df["^VIX"].iloc[p] if "^VIX" in df.columns else float("nan")
            v3m_val = df["^VIX3M"].iloc[p] if "^VIX3M" in df.columns else float("nan")
            vvix_val = df["^VVIX"].iloc[p] if "^VVIX" in df.columns else float("nan")
            ratio = v3m_val / vix_val if pd.notna(v3m_val) and pd.notna(vix_val) and vix_val > 0 else float("nan")
            rows.append(
                dict(
                    event_date=d0,
                    horizon=f"T+{k}",
                    k=k,
                    session_date=d,
                    vix=vix_val,
                    vix3m_over_vix=ratio,
                    vvix=vvix_val,
                    vix_pct_vs_tm1=(vix_val / vix_tm1 - 1) * 100 if pd.notna(vix_tm1) and vix_tm1 > 0 else float("nan"),
                )
            )
    return pd.DataFrame(rows)


def unconditional_baseline(df: pd.DataFrame) -> pd.DataFrame:
    """Distribution of forward-k VIX percent changes across all sessions."""
    rows = []
    for k in HORIZONS:
        if k == 0:
            pct = pd.Series(0.0, index=df.index)
        else:
            pct = df["^VIX"].pct_change(k).shift(-k) * 100
        s = pct.dropna()
        rows.append(
            dict(
                horizon=f"T+{k}",
                k=k,
                n=len(s),
                median=s.median(),
                p25=s.quantile(0.25),
                p75=s.quantile(0.75),
                std=s.std(),
            )
        )
    return pd.DataFrame(rows)


def cohort_summary(forward: pd.DataFrame) -> pd.DataFrame:
    """Per-horizon cohort summary."""
    rows = []
    for k in HORIZONS:
        sub = forward[forward["k"] == k]
        rows.append(
            dict(
                horizon=f"T+{k}",
                k=k,
                n_events=sub["event_date"].nunique(),
                vix_median=sub["vix"].median(),
                vix_pct_median=sub["vix_pct_vs_tm1"].median(),
                vix_pct_p25=sub["vix_pct_vs_tm1"].quantile(0.25),
                vix_pct_p75=sub["vix_pct_vs_tm1"].quantile(0.75),
                ratio_median=sub["vix3m_over_vix"].median(),
                ratio_below_110_pct=(sub["vix3m_over_vix"] < 1.10).mean() * 100,
                vvix_median=sub["vvix"].median(),
                vvix_above_100_pct=(sub["vvix"] > 100).mean() * 100,
            )
        )
    return pd.DataFrame(rows)


def cluster_check(cohort: pd.DataFrame) -> str:
    """Detect if >60% of events fall within any 30-td window."""
    if len(cohort) < 2:
        return "n<2, cluster check not run"
    dates = pd.to_datetime(cohort["event_date"]).sort_values().reset_index(drop=True)
    # For each event, count events within +/- 30 calendar days
    windows = []
    for i, d in enumerate(dates):
        lo = d - pd.Timedelta(days=45)  # ~30 td
        hi = d + pd.Timedelta(days=45)
        n_in_window = ((dates >= lo) & (dates <= hi)).sum()
        windows.append(n_in_window)
    max_cluster = max(windows)
    pct = max_cluster / len(dates) * 100
    return f"largest 30-td cluster contains {max_cluster}/{len(dates)} events = {pct:.0f}%"


def main() -> None:
    print("### PULL")
    df = pull_series()
    for c in df.columns:
        s = df[c].dropna()
        print(f"  {c}: {len(s)} rows, {s.index.min().date()} → {s.index.max().date()}")

    # Cross-check MOVE against my ledger
    my = pd.read_csv("AGENTS/VIOLET/workbook/MOVE.tsv", sep="\t")
    my["date"] = pd.to_datetime(my["date"])
    latest = my.iloc[-1]
    yf_val = df["^MOVE"].get(latest["date"])
    print(f"\n### CROSS-CHECK MOVE latest ledger row")
    print(f"  ledger 9/24: {latest['close']}   yfinance 9/24: {yf_val}")

    cohort = identify_cohort(df)
    print(f"\n### COHORT")
    print(f"  n events after 3-td de-dup: {len(cohort)}")
    print(f"  cluster check: {cluster_check(cohort)}")
    print(f"  first 5 events + last 5:")
    print(cohort.head(5).to_string(index=False))
    print("  ...")
    print(cohort.tail(5).to_string(index=False))

    forward = forward_paths(df, cohort)
    summary = cohort_summary(forward)
    print(f"\n### COHORT SUMMARY (forward paths)")
    print(summary.to_string(index=False, float_format=lambda x: f"{x:.2f}"))

    baseline = unconditional_baseline(df)
    print(f"\n### UNCONDITIONAL VIX baseline (all sessions)")
    print(baseline.to_string(index=False, float_format=lambda x: f"{x:.2f}"))

    # Save artifacts
    out_dir = Path("AGENTS/VIOLET/research")
    cohort.to_csv(out_dir / "rq8_cohort.csv", index=False)
    forward.to_csv(out_dir / "rq8_forward.csv", index=False)
    summary.to_csv(out_dir / "rq8_cohort_summary.csv", index=False)
    baseline.to_csv(out_dir / "rq8_baseline.csv", index=False)
    print(f"\nartifacts saved to {out_dir}/rq8_*.csv")


if __name__ == "__main__":
    main()
