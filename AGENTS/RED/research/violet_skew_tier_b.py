"""
RED Tier B: Classify each SKEW-divergence fire by credit-state context.

VIOLET's v3.1 thesis: HY OAS leads VIX in low-vol regimes IF the shock is
credit-led. VIOLET's analog library already notes positioning-led VIX
spikes are transient (Feb 2018, Aug 2024). So the question is: what
fraction of past SKEW-divergence fires were credit-led, and how does
the base rate differ by credit state? The current setup (Apr 13) has
credit TIGHTENING hard (HY OAS 346→285 in 3 weeks) — which cohort
should we map it to?

Uses VIOLET's workbook/hy_oas_fred.csv (FRED BAMLH0A0HYM2, daily 1996-).
"""

import pandas as pd
import numpy as np

from violet_skew_recheck import (
    load_data, find_fire_days, cluster_into_episodes,
    episode_skew_peak, forward_window, sustained_above,
    peak_intraday, peak_close,
)

HY = "/home/willi/Research-workspace/AGENTS/VIOLET/workbook/hy_oas_fred.csv"


def load_hy():
    df = pd.read_csv(HY, parse_dates=["observation_date"])
    df = df.rename(columns={"observation_date": "Date", "BAMLH0A0HYM2": "HY_PCT"})
    df = df.dropna().sort_values("Date").reset_index(drop=True)
    # Convert % to bps
    df["HY_BPS"] = df["HY_PCT"] * 100
    return df


def hy_at(hy, d):
    """HY OAS bps at or closest-before date d."""
    sub = hy[hy["Date"] <= d]
    if not len(sub):
        return np.nan
    return float(sub.iloc[-1]["HY_BPS"])


def hy_window_stats(hy, fire_date):
    """HY OAS stats around the 20d window leading to fire:
       - hy_at_fire: level on fire date
       - hy_20d_prior: level 20 calendar days before
       - hy_chg_20d: change in bps
       - hy_peak_in_window: peak level in [fire-25, fire]
       - hy_trend: 'WIDENING', 'TIGHTENING', 'FLAT'
    """
    hy_at_fire = hy_at(hy, fire_date)
    hy_20d_prior = hy_at(hy, fire_date - pd.Timedelta(days=20))
    chg = hy_at_fire - hy_20d_prior

    # Peak in 25 calendar days prior (covers ~17-20 trading days)
    window = hy[(hy["Date"] >= fire_date - pd.Timedelta(days=25)) & (hy["Date"] <= fire_date)]
    hy_peak = window["HY_BPS"].max() if len(window) else np.nan
    hy_trough = window["HY_BPS"].min() if len(window) else np.nan

    if chg >= 25:
        trend = "WIDENING"
    elif chg <= -25:
        trend = "TIGHTENING"
    else:
        trend = "FLAT"
    return {
        "hy_at_fire": round(hy_at_fire, 0),
        "hy_20d_prior": round(hy_20d_prior, 0),
        "hy_chg_20d": round(chg, 0),
        "hy_peak_25d": round(hy_peak, 0),
        "hy_trough_25d": round(hy_trough, 0),
        "hy_trend": trend,
    }


def main():
    df = load_data()
    hy = load_hy()
    print(f"VIX data: {df['Date'].min().date()} to {df['Date'].max().date()}")
    print(f"HY OAS data: {hy['Date'].min().date()} to {hy['Date'].max().date()}\n")

    fires = find_fire_days(df)
    episodes = cluster_into_episodes(fires)
    print(f"Episodes: {len(episodes)}\n")

    rows = []
    for i, (start, end) in enumerate(episodes, 1):
        skew_peak = episode_skew_peak(df, start, end)
        vix_at_start = df.loc[df["Date"] == start, "VIX"].iloc[0]
        fwd = forward_window(df, start, 60)
        fwd36 = forward_window(df, start, 36)
        hy_ctx = hy_window_stats(hy, start)

        rows.append({
            "ep": i,
            "start": start.date(),
            "skew_peak": round(skew_peak, 1),
            "vix_at_start": round(vix_at_start, 2),
            "hy_at_fire": hy_ctx["hy_at_fire"],
            "hy_20d_prior": hy_ctx["hy_20d_prior"],
            "hy_chg_20d": hy_ctx["hy_chg_20d"],
            "hy_peak_25d": hy_ctx["hy_peak_25d"],
            "hy_trend": hy_ctx["hy_trend"],
            "sust_25_5d_60": sustained_above(fwd, 25, 5),
            "sust_25_3d_60": sustained_above(fwd, 25, 3),
            "sust_25_3d_36": sustained_above(fwd36, 25, 3),
            "intra_peak_60": round(peak_intraday(fwd), 2),
            "close_peak_60": round(peak_close(fwd), 2),
            "in_2024_26": pd.Timestamp(start) >= pd.Timestamp("2024-01-01"),
        })

    out = pd.DataFrame(rows)
    print("=" * 130)
    print("EPISODE TABLE — with HY OAS credit-state classification")
    print("=" * 130)
    print(out.to_string(index=False))

    print("\n" + "=" * 100)
    print("B1 — BASE RATES BY CREDIT STATE")
    print("=" * 100)

    for trend in ["WIDENING", "FLAT", "TIGHTENING"]:
        sub = out[out["hy_trend"] == trend]
        n = len(sub)
        if n == 0:
            print(f"\n  {trend}: n=0 (no historical episodes in this state)")
            continue
        s25_5_60 = sub["sust_25_5d_60"].sum()
        s25_3_60 = sub["sust_25_3d_60"].sum()
        s25_3_36 = sub["sust_25_3d_36"].sum()
        print(f"\n  {trend}: n={n}")
        print(f"    Episodes: {list(sub['ep'])}, start dates: {list(sub['start'])}")
        print(f"    HY OAS change 20d range: {sub['hy_chg_20d'].min():.0f} to {sub['hy_chg_20d'].max():.0f} bps")
        print(f"    Sustained close >=25 5d (60d horizon):    {s25_5_60}/{n} ({s25_5_60/n*100:.0f}%)")
        print(f"    Sustained close >=25 3d (60d horizon):    {s25_3_60}/{n} ({s25_3_60/n*100:.0f}%)")
        print(f"    Sustained close >=25 3d (36d horizon):    {s25_3_36}/{n} ({s25_3_36/n*100:.0f}%)")

    # Additional: split by "HY OAS near recent peak vs not"
    print("\n" + "=" * 100)
    print("B1 BONUS — HY OAS at fire vs peak in prior 25d")
    print("=" * 100)
    out["hy_off_peak_bps"] = out["hy_peak_25d"] - out["hy_at_fire"]
    out["hy_post_peak"] = out["hy_off_peak_bps"] > 15  # credit tightened >15bps off its recent high
    for label, sub in [("POST-PEAK (credit tightening from recent high)", out[out["hy_post_peak"]]),
                       ("NOT POST-PEAK (credit flat or still widening)", out[~out["hy_post_peak"]])]:
        n = len(sub)
        if n == 0:
            continue
        s25_5_60 = sub["sust_25_5d_60"].sum()
        s25_3_36 = sub["sust_25_3d_36"].sum()
        print(f"\n  {label}: n={n}")
        print(f"    Episodes: {list(sub['ep'])}")
        print(f"    Sustained close >=25 5d (60d horizon): {s25_5_60}/{n} ({s25_5_60/n*100:.0f}%)")
        print(f"    Sustained close >=25 3d (36d horizon): {s25_3_36}/{n} ({s25_3_36/n*100:.0f}%)")

    # Current-state lookup
    print("\n" + "=" * 100)
    print("CURRENT STATE — Apr 13 2026 fire")
    print("=" * 100)
    current_fire = pd.Timestamp("2026-04-13")
    # For Apr 13 we probably don't have HY OAS yet — use latest available
    latest_hy = hy.iloc[-1]
    print(f"  Latest HY OAS: {latest_hy['Date'].date()} = {latest_hy['HY_BPS']:.0f} bps")
    hy_ctx = hy_window_stats(hy, current_fire)
    print(f"  HY OAS at fire (Apr 13 proxy, latest avail): {hy_ctx['hy_at_fire']:.0f} bps")
    print(f"  HY OAS 20d prior (~Mar 24):                  {hy_ctx['hy_20d_prior']:.0f} bps")
    print(f"  HY OAS 20d change:                           {hy_ctx['hy_chg_20d']:+.0f} bps")
    print(f"  HY OAS peak in prior 25d:                    {hy_ctx['hy_peak_25d']:.0f} bps")
    print(f"  HY OAS trough in prior 25d:                  {hy_ctx['hy_trough_25d']:.0f} bps")
    print(f"  Classification:                              {hy_ctx['hy_trend']}")
    if hy_ctx['hy_peak_25d'] and hy_ctx['hy_at_fire']:
        print(f"  Off peak:                                    -{hy_ctx['hy_peak_25d'] - hy_ctx['hy_at_fire']:.0f} bps (post-peak = credit-tightened)")

    out.to_csv("/home/willi/Research-workspace/AGENTS/RED/research/violet_skew_tier_b_results.csv", index=False)
    print("\nFull table written to research/violet_skew_tier_b_results.csv")


if __name__ == "__main__":
    main()
