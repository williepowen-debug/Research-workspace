"""
RED Tier C: Out-of-sample validation of VIOLET's SKEW-divergence pattern.

Uses yfinance pull covering 2007-01 to 2026-04 (VVIX constraint).
OOS period: 2007-01-03 to 2017-12-31 (pre-VIOLET-sample).
IN-sample: 2018-01-01 onward (matches VIOLET's file).

Reuses pattern definition and forward-window logic from violet_skew_recheck.
"""

import pandas as pd
import numpy as np

from violet_skew_recheck import (
    find_fire_days, cluster_into_episodes,
    episode_skew_peak, forward_window, sustained_above,
    peak_intraday, peak_close,
)

DATA = "/home/willi/Research-workspace/AGENTS/RED/research/skew_vix_vvix_full.csv"


def load_full():
    df = pd.read_csv(DATA, parse_dates=["Date"])
    df = df.rename(columns={
        "Close_SKEW": "SKEW",
        "Close_VIX": "VIX",
        "Close_VVIX": "VVIX",
        "High_VIX": "VIX_HIGH",
    })
    df = df[["Date", "SKEW", "VIX", "VVIX", "VIX_HIGH"]].dropna()
    df = df.sort_values("Date").reset_index(drop=True)
    return df


def classify_episodes(df, label):
    fires = find_fire_days(df)
    episodes = cluster_into_episodes(fires)
    print(f"\n{'='*90}\n{label}: {df['Date'].min().date()} to {df['Date'].max().date()} (n={len(df)} rows)")
    print(f"Fire days: {len(fires)}   Distinct episodes: {len(episodes)}\n{'='*90}")

    rows = []
    for i, (start, end) in enumerate(episodes, 1):
        skew_peak = episode_skew_peak(df, start, end)
        vix_at_start = df.loc[df["Date"] == start, "VIX"].iloc[0]
        fwd60 = forward_window(df, start, 60)
        fwd36 = forward_window(df, start, 36)
        rows.append({
            "ep": i,
            "start": start.date(),
            "end": end.date(),
            "skew_peak": round(skew_peak, 1),
            "vix_at_start": round(vix_at_start, 2),
            "intra_peak_60": round(peak_intraday(fwd60), 2),
            "close_peak_60": round(peak_close(fwd60), 2),
            "intra_peak_36": round(peak_intraday(fwd36), 2),
            "close_peak_36": round(peak_close(fwd36), 2),
            "sust_25_5d_60": sustained_above(fwd60, 25, 5),
            "sust_25_3d_60": sustained_above(fwd60, 25, 3),
            "sust_25_3d_36": sustained_above(fwd36, 25, 3),
            "sust_25_5d_36": sustained_above(fwd36, 25, 5),
            "sust_30_3d_60": sustained_above(fwd60, 30, 3),
            "intra_25_36": (peak_intraday(fwd36) >= 25) if len(fwd36) else False,
            "intra_25_60": (peak_intraday(fwd60) >= 25) if len(fwd60) else False,
        })
    return pd.DataFrame(rows)


def print_rates(out, label):
    n = len(out)
    if n == 0:
        print(f"  {label}: n=0")
        return
    def pct(col):
        v = out[col].sum()
        return f"{v}/{n} ({v/n*100:.0f}%)"
    print(f"\n  {label} (n={n})")
    print(f"    Intraday peak VIX >=25, 60d:          {pct('intra_25_60')}")
    print(f"    Intraday peak VIX >=25, 36d:          {pct('intra_25_36')}")
    print(f"    Sustained close >=25 for 3d, 60d:     {pct('sust_25_3d_60')}")
    print(f"    Sustained close >=25 for 5d, 60d:     {pct('sust_25_5d_60')}")
    print(f"    Sustained close >=25 for 3d, 36d:     {pct('sust_25_3d_36')}")
    print(f"    Sustained close >=25 for 5d, 36d:     {pct('sust_25_5d_36')}")
    print(f"    Sustained close >=30 for 3d, 60d:     {pct('sust_30_3d_60')}")


def main():
    df = load_full()

    # Split OOS (pre-2018) from IN-sample
    oos = df[df["Date"] < pd.Timestamp("2018-01-01")].reset_index(drop=True)
    ins = df[df["Date"] >= pd.Timestamp("2018-01-01")].reset_index(drop=True)

    oos_ep = classify_episodes(oos, "OOS (2007-01 to 2017-12)")
    print(oos_ep.to_string(index=False))

    ins_ep = classify_episodes(ins, "IN-SAMPLE (2018-01 to 2026-04, VIOLET's published data)")
    print(ins_ep.to_string(index=False))

    full_ep = classify_episodes(df, "POOLED (2007-01 to 2026-04)")
    print(full_ep.to_string(index=False))

    print("\n" + "=" * 90)
    print("HEADLINE BASE RATES — OOS vs IN-SAMPLE vs POOLED")
    print("=" * 90)
    print_rates(oos_ep, "OOS 2007-2017")
    print_rates(ins_ep, "IN-SAMPLE 2018-2026")
    print_rates(full_ep, "POOLED 2007-2026")

    # Exclude 2024-26 cluster from pooled for a fair OOS+pre-cluster read
    pre_cluster = full_ep[pd.to_datetime(full_ep["start"]) < pd.Timestamp("2024-01-01")]
    print_rates(pre_cluster, "POOLED ex-2024-26 cluster (2007-2023)")

    out_path = "/home/willi/Research-workspace/AGENTS/RED/research/violet_skew_tier_c_results.csv"
    full_ep.to_csv(out_path, index=False)
    print(f"\nPooled episode table written to {out_path}")


if __name__ == "__main__":
    main()
