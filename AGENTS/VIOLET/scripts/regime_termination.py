"""Analyze what ended historical elevated SKEW regimes.

Question: When long SKEW regimes end, does the VIX event come before
(regime persisted through it), during (coincident), or after (regime
collapse was a precursor)?

Output: research/2026-04-16_regime_termination_analysis.md
"""
from __future__ import annotations

import sys
import warnings
from datetime import datetime
from pathlib import Path

import numpy as np
import pandas as pd

warnings.filterwarnings("ignore", category=FutureWarning)

SCRIPT_DIR = Path(__file__).resolve().parent
BASE_DIR = SCRIPT_DIR.parent
WORKBOOK = BASE_DIR / "workbook"
RESEARCH_DIR = BASE_DIR / "research"

sys.path.insert(0, str(SCRIPT_DIR))
from skew_trajectory import load_all_data

REGIME_THRESHOLD = 140
ROLLING_WINDOW = 20
MIN_REGIME_DAYS = 10
VIX_WINDOW = 60       # ±60 trading days for VIX peak search
POST_WINDOW = 30       # 30 td after regime ends


def load_data() -> pd.DataFrame:
    """Load SKEW + VIX closes + VIX intraday highs."""
    base = load_all_data()  # columns: skew, vix

    # Add High ^VIX from CSV
    csv_path = WORKBOOK / "vix_historical.csv"
    csv_df = pd.read_csv(csv_path, parse_dates=["Date"], index_col="Date")
    vix_high = csv_df["High ^VIX"].rename("vix_high")
    vix_high.index.name = "date"
    base = base.join(vix_high, how="left")
    # Pre-2018: no intraday data — use close as fallback
    base["vix_high"] = base["vix_high"].fillna(base["vix"])

    # Forward-fill SKEW NaN (up to 3 days) to prevent false regime breaks
    nan_before = base["skew"].isna().sum()
    base["skew"] = base["skew"].ffill(limit=3)
    nan_after = base["skew"].isna().sum()
    print(f"[NaN] Forward-filled {nan_before - nan_after} SKEW NaN values "
          f"({nan_after} remain)")

    # Compute 20d rolling average
    base["skew_20d"] = base["skew"].rolling(ROLLING_WINDOW, min_periods=15).mean()
    return base


def identify_regimes(df: pd.DataFrame) -> list[dict]:
    """Find contiguous periods where 20d avg SKEW >= threshold."""
    above = df["skew_20d"] >= REGIME_THRESHOLD
    regimes = []
    in_regime = False
    start = None

    for dt, val in above.items():
        if val and not in_regime:
            in_regime = True
            start = dt
        elif not val and in_regime:
            in_regime = False
            end_dt = df.index[df.index.get_loc(dt) - 1]
            dur = len(df.loc[start:end_dt])
            if dur >= MIN_REGIME_DAYS:
                peak = float(df.loc[start:end_dt, "skew"].max())
                regimes.append({
                    "start": start, "end": end_dt, "duration": dur,
                    "peak_skew": round(peak, 1), "ongoing": False,
                })

    # Check if final regime is ongoing
    if in_regime:
        end_dt = df.index[-1]
        dur = len(df.loc[start:end_dt])
        if dur >= MIN_REGIME_DAYS:
            peak = float(df.loc[start:end_dt, "skew"].max())
            regimes.append({
                "start": start, "end": end_dt, "duration": dur,
                "peak_skew": round(peak, 1), "ongoing": True,
            })

    # Number them
    for i, r in enumerate(regimes, 1):
        r["id"] = i
    return regimes


def analyze_termination(df: pd.DataFrame, regime: dict) -> dict:
    """Compute termination metrics for a completed regime."""
    end = regime["end"]
    end_pos = df.index.get_loc(end)
    start_pos = df.index.get_loc(regime["start"])

    m = {**regime}

    # Terminal 10 td behavior
    t10_start = max(start_pos, end_pos - 9)
    t10 = df.iloc[t10_start:end_pos + 1]
    m["skew_at_end"] = round(float(t10["skew"].iloc[-1]), 1)
    m["skew_20d_at_end"] = round(float(t10["skew_20d"].iloc[-1]), 1)
    m["vix_at_end"] = round(float(t10["vix"].iloc[-1]), 2)

    # Rate of change of 20d avg in final 5 td
    if len(t10) >= 5:
        final5 = t10["skew_20d"].iloc[-5:]
        slope = float(final5.iloc[-1] - final5.iloc[0])
        m["final_5d_slope"] = round(slope, 1)
    else:
        m["final_5d_slope"] = None

    # Classify terminal behavior
    if m["final_5d_slope"] is not None and m["final_5d_slope"] < -3:
        m["terminal_pattern"] = "sudden_drop"
    else:
        m["terminal_pattern"] = "gradual_fade"

    # VIX peak in ±60 td window
    win_start = max(0, end_pos - VIX_WINDOW)
    win_end = min(len(df), end_pos + VIX_WINDOW + 1)
    window = df.iloc[win_start:win_end]

    peak_close_idx = window["vix"].idxmax()
    peak_high_idx = window["vix_high"].idxmax()

    m["vix_peak_close"] = round(float(window["vix"].max()), 2)
    m["vix_peak_close_date"] = peak_close_idx
    m["vix_peak_high"] = round(float(window["vix_high"].max()), 2)
    m["vix_peak_high_date"] = peak_high_idx

    # Temporal lag (trading days): positive = VIX peaked before regime ended
    peak_pos = df.index.get_loc(peak_close_idx)
    lag_td = end_pos - peak_pos
    m["lag_td"] = lag_td

    # Classification
    vix_spike = m["vix_peak_close"] > m["vix_at_end"] * 1.3
    if abs(lag_td) <= 5:
        m["classification"] = "COINCIDENT"
    elif lag_td > 5:
        m["classification"] = "POST_EVENT_PERSIST"
    elif lag_td < -5 and vix_spike:
        m["classification"] = "PRE_EVENT_FADE"
    else:
        m["classification"] = "GRADUAL_FADE"

    # Post-regime VIX (30 td after end)
    post_start = end_pos + 1
    post_end = min(len(df), end_pos + POST_WINDOW + 1)
    if post_start < len(df):
        post = df.iloc[post_start:post_end]
        m["post_30d_vix_peak"] = round(float(post["vix"].max()), 2) if len(post) > 0 else None
        m["post_30d_vix_mean"] = round(float(post["vix"].mean()), 2) if len(post) > 0 else None
        m["post_30d_vix_high"] = round(float(post["vix_high"].max()), 2) if len(post) > 0 else None

        # Post-regime behavior
        if m["post_30d_vix_peak"] and m["post_30d_vix_peak"] > m["vix_at_end"] * 1.5:
            m["post_behavior"] = "SPIKE"
        elif m["post_30d_vix_peak"] and m["post_30d_vix_peak"] > m["vix_at_end"] * 1.2:
            m["post_behavior"] = "ELEVATED"
        else:
            m["post_behavior"] = "CALM"
    else:
        m["post_30d_vix_peak"] = None
        m["post_30d_vix_mean"] = None
        m["post_30d_vix_high"] = None
        m["post_behavior"] = "N/A"

    return m


def analyze_ongoing(df: pd.DataFrame, regime: dict) -> dict:
    """Partial metrics for the current ongoing regime."""
    m = {**regime}
    end_pos = df.index.get_loc(regime["end"])

    m["skew_at_end"] = round(float(df.iloc[end_pos]["skew"]), 1)
    m["skew_20d_at_end"] = round(float(df.iloc[end_pos]["skew_20d"]), 1)
    m["vix_at_end"] = round(float(df.iloc[end_pos]["vix"]), 2)

    # Intermediate VIX events during regime
    regime_data = df.loc[regime["start"]:regime["end"]]
    vix_peak_idx = regime_data["vix"].idxmax()
    m["mid_vix_peak"] = round(float(regime_data["vix"].max()), 2)
    m["mid_vix_peak_date"] = vix_peak_idx

    # Current 20d avg trajectory (final 10 td)
    t10 = regime_data.iloc[-10:]
    if len(t10) >= 5:
        final5 = t10["skew_20d"].iloc[-5:]
        m["final_5d_slope"] = round(float(final5.iloc[-1] - final5.iloc[0]), 1)
    else:
        m["final_5d_slope"] = None

    return m


# ── Markdown builder ────────────────────────────────────────────────


def build_markdown(completed: list[dict], ongoing: dict | None) -> str:
    L: list[str] = []

    L.append("# SKEW Regime Termination Analysis\n")
    L.append("**Question:** When historical elevated SKEW regimes ended, "
             "did the VIX event come **before** the regime ended (regime "
             "persisted through it), **during** (coincident), or **after** "
             "(regime collapse preceded the event)?\n")
    L.append("**Motivation:** The current regime (206+ td, second longest "
             "in 19-year history) saw SKEW dip to 139.2 on Apr 16. If "
             "regimes typically collapse BEFORE the VIX event, this dip "
             "could signal the event is imminent. If they persist THROUGH "
             "events, the dip is noise.\n")
    L.append("---\n")

    # Method
    L.append("## Method\n")
    L.append("- **Regime definition:** 20-day rolling avg SKEW >= 140, "
             "minimum 10 trading days.")
    L.append("- **NaN handling:** Forward-filled SKEW gaps (up to 3 days) "
             "before computing rolling avg to prevent false terminations.")
    L.append("- **VIX peak:** Searched ±60 trading days around regime end. "
             "Used both daily close and intraday high (`High ^VIX`).")
    L.append("- **Temporal lag:** regime_end_date minus vix_peak_date in "
             "trading days. Positive = VIX peaked first (regime outlasted "
             "event). Negative = VIX peaked after (regime ended before event).")
    L.append("- **Data:** 2014-2026 (yfinance + vix_historical.csv + "
             "VX_DAILY.tsv).\n")
    L.append("---\n")

    all_regimes = completed + ([ongoing] if ongoing else [])
    all_regimes.sort(key=lambda x: x["duration"], reverse=True)

    # Table 1: Master inventory
    L.append("## Table 1: Master Regime Inventory\n")
    L.append("| # | Start | End | Duration | Peak SKEW | Status |")
    L.append("|--:|:------|:----|:--------:|----------:|:-------|")
    for r in all_regimes:
        status = "**ONGOING**" if r["ongoing"] else "ended"
        L.append(f"| {r['id']} | {r['start'].date()} | {r['end'].date()} "
                 f"| {r['duration']} td | {r['peak_skew']} | {status} |")
    L.append(f"\n{len(all_regimes)} regimes >= 10 td identified.\n")
    L.append("---\n")

    # Table 2: Termination detail
    L.append("## Table 2: Termination Detail\n")
    L.append("| # | End Date | Dur | SKEW @ End | VIX @ End "
             "| VIX Peak Close | VIX Peak Date | Lag (td) "
             "| Post-30d Peak | Classification |")
    L.append("|--:|:---------|----:|-----------:|----------:"
             "|---------------:|:-------------|--------:"
             "|--------------:|:-------------|")
    for r in sorted(completed, key=lambda x: x["duration"], reverse=True):
        L.append(
            f"| {r['id']} | {r['end'].date()} | {r['duration']} "
            f"| {r['skew_at_end']} | {r['vix_at_end']} "
            f"| {r['vix_peak_close']} | {r['vix_peak_close_date'].date()} "
            f"| {r['lag_td']:+d} "
            f"| {r.get('post_30d_vix_peak', '—')} "
            f"| {r['classification']} |"
        )
    L.append("\n**Lag sign:** positive = VIX peaked before regime ended "
             "(regime outlasted event); negative = VIX peaked after "
             "(regime ended before event).\n")
    L.append("---\n")

    # Finding 1: Temporal lag distribution
    L.append("## Finding 1: Temporal Lag Distribution\n")

    pre_event = [r for r in completed if r["classification"] == "PRE_EVENT_FADE"]
    coincident = [r for r in completed if r["classification"] == "COINCIDENT"]
    post_event = [r for r in completed if r["classification"] == "POST_EVENT_PERSIST"]
    gradual = [r for r in completed if r["classification"] == "GRADUAL_FADE"]

    L.append("| Classification | Count | Regimes | Meaning |")
    L.append("|:---------------|------:|:--------|:--------|")

    def _ids(lst):
        return ", ".join("R" + str(r["id"]) for r in lst) or "—"

    L.append(f"| PRE_EVENT_FADE | {len(pre_event)} "
             f"| {_ids(pre_event)} "
             f"| Regime ended, then VIX spiked |")
    L.append(f"| COINCIDENT | {len(coincident)} "
             f"| {_ids(coincident)} "
             f"| VIX peak ±5 td of regime end |")
    L.append(f"| POST_EVENT_PERSIST | {len(post_event)} "
             f"| {_ids(post_event)} "
             f"| Regime survived past VIX peak |")
    L.append(f"| GRADUAL_FADE | {len(gradual)} "
             f"| {_ids(gradual)} "
             f"| No major VIX event in window |")
    L.append("")

    # Lag statistics
    lags = [r["lag_td"] for r in completed]
    L.append(f"**Lag statistics:** mean {np.mean(lags):+.1f} td, "
             f"median {np.median(lags):+.1f} td, "
             f"range {min(lags):+d} to {max(lags):+d}\n")

    # Highlight key cases
    L.append("**Key cases by duration:**\n")
    for r in sorted(completed, key=lambda x: x["duration"], reverse=True)[:5]:
        L.append(f"- **R{r['id']}** ({r['duration']} td): ended {r['end'].date()}, "
                 f"VIX peaked {r['vix_peak_close']} on "
                 f"{r['vix_peak_close_date'].date()} → "
                 f"lag **{r['lag_td']:+d} td** ({r['classification']})")
    L.append("")
    L.append("---\n")

    # Finding 2: Terminal SKEW behavior
    L.append("## Finding 2: Terminal SKEW Behavior\n")
    L.append("How did SKEW behave in the final days of each regime?\n")
    L.append("| # | Duration | SKEW @ End | 20d Avg @ End | Final 5d Slope | Pattern |")
    L.append("|--:|---------:|-----------:|--------------:|---------------:|:--------|")
    for r in sorted(completed, key=lambda x: x["duration"], reverse=True):
        slope = f"{r['final_5d_slope']:+.1f}" if r["final_5d_slope"] is not None else "—"
        L.append(f"| {r['id']} | {r['duration']} | {r['skew_at_end']} "
                 f"| {r['skew_20d_at_end']} | {slope} "
                 f"| {r['terminal_pattern']} |")
    L.append("")

    sudden = [r for r in completed if r["terminal_pattern"] == "sudden_drop"]
    gradual_term = [r for r in completed if r["terminal_pattern"] == "gradual_fade"]
    L.append(f"**Sudden drops (final 5d slope < -3):** {len(sudden)}")
    L.append(f"**Gradual fades:** {len(gradual_term)}\n")
    L.append("---\n")

    # Finding 3: Post-regime VIX
    L.append("## Finding 3: Post-Regime VIX Behavior\n")
    L.append("What happened to VIX in the 30 trading days after the regime ended?\n")
    L.append("| # | Duration | VIX @ End | Post-30d Peak | Post-30d Mean | Behavior |")
    L.append("|--:|---------:|----------:|--------------:|--------------:|:---------|")
    for r in sorted(completed, key=lambda x: x["duration"], reverse=True):
        pp = r.get("post_30d_vix_peak", "—")
        pm = r.get("post_30d_vix_mean", "—")
        L.append(f"| {r['id']} | {r['duration']} | {r['vix_at_end']} "
                 f"| {pp} | {pm} | {r.get('post_behavior', '—')} |")
    L.append("")

    spikes = [r for r in completed if r.get("post_behavior") == "SPIKE"]
    calms = [r for r in completed if r.get("post_behavior") == "CALM"]
    L.append(f"**Post-regime spikes (VIX > 1.5x end level):** {len(spikes)} of {len(completed)}")
    L.append(f"**Post-regime calm:** {len(calms)} of {len(completed)}\n")
    L.append("---\n")

    # Finding 4: Current regime
    if ongoing:
        L.append("## Finding 4: Current Regime in Context\n")
        L.append(f"**Duration:** {ongoing['duration']} td (ongoing)")
        L.append(f"**SKEW at latest:** {ongoing['skew_at_end']}")
        L.append(f"**20d avg at latest:** {ongoing['skew_20d_at_end']}")
        L.append(f"**Final 5d slope:** {ongoing.get('final_5d_slope', '—')}")
        L.append(f"**Intermediate VIX event:** {ongoing['mid_vix_peak']} on "
                 f"{ongoing['mid_vix_peak_date'].date()} "
                 f"(regime persisted through it)\n")

        # Compare to completed regimes
        L.append("**Trajectory comparison (final 5d slope):**\n")
        L.append("| Regime | Duration | Final 5d Slope | What Followed |")
        L.append("|:-------|:---------|:--------------|:-------------|")
        for r in sorted(completed, key=lambda x: x["duration"], reverse=True)[:5]:
            slope = f"{r['final_5d_slope']:+.1f}" if r["final_5d_slope"] is not None else "—"
            L.append(f"| R{r['id']} | {r['duration']} td | {slope} "
                     f"| VIX {r['vix_peak_close']} ({r['classification']}) |")
        slope = f"{ongoing['final_5d_slope']:+.1f}" if ongoing.get("final_5d_slope") is not None else "—"
        L.append(f"| **Current** | **{ongoing['duration']} td** | **{slope}** "
                 f"| **TBD** |")
        L.append("")
    L.append("---\n")

    # Actionable summary
    L.append("## Actionable Summary\n")

    # Synthesize the key finding
    n_pre = len(pre_event)
    n_post = len(post_event)
    n_coin = len(coincident)
    n_grad = len(gradual)
    total = len(completed)

    L.append(f"**Of {total} completed regimes:**")
    L.append(f"- {n_pre} ({n_pre/total*100:.0f}%) — regime ended BEFORE "
             f"VIX event (PRE_EVENT_FADE)")
    L.append(f"- {n_coin} ({n_coin/total*100:.0f}%) — regime ended "
             f"WITH VIX event (COINCIDENT)")
    L.append(f"- {n_post} ({n_post/total*100:.0f}%) — regime OUTLASTED "
             f"VIX event (POST_EVENT_PERSIST)")
    L.append(f"- {n_grad} ({n_grad/total*100:.0f}%) — no significant "
             f"VIX event (GRADUAL_FADE)")
    L.append("")

    L.append("**For the VIX May 19 25C position:**\n")
    if n_pre + n_coin > n_post + n_grad:
        L.append("The dominant pattern is that VIX events come **at or after** "
                 "the regime ends. If our regime is truly ending, the VIX "
                 "event may still be ahead — **regime collapse is a precursor, "
                 "not an all-clear.** This paradoxically supports the position "
                 "even as SKEW fades.")
    elif n_post > n_pre:
        L.append("The dominant pattern is that regimes **persist through** "
                 "VIX events and collapse afterward. If our regime is still "
                 "intact (which the within-cycle bounce pattern suggests), "
                 "the position remains well-supported.")
    else:
        L.append("The pattern is mixed — no single dominant relationship. "
                 "SKEW regime termination alone is not a reliable signal "
                 "for VIX event timing.")
    L.append("")

    L.append("---\n")
    L.append(f"*Generated {datetime.now().strftime('%Y-%m-%d %H:%M')} "
             f"by VIOLET `scripts/regime_termination.py`*")
    L.append("*Data: yfinance + vix_historical.csv + VX_DAILY.tsv*")
    return "\n".join(L)


# ── Main ────────────────────────────────────────────────────────────


def main():
    print("=" * 60)
    print("  SKEW Regime Termination Analysis")
    print("=" * 60)

    df = load_data()
    print(f"\n[Data] {len(df)} days, "
          f"{df.index.min().date()} → {df.index.max().date()}")

    regimes = identify_regimes(df)
    print(f"\n[Regimes] {len(regimes)} elevated SKEW regimes >= {MIN_REGIME_DAYS} td")

    completed = []
    ongoing_regime = None

    for r in regimes:
        tag = " (ONGOING)" if r["ongoing"] else ""
        print(f"  R{r['id']:2d}: {r['start'].date()} → {r['end'].date()} "
              f"({r['duration']} td, peak {r['peak_skew']}){tag}")

        if r["ongoing"]:
            ongoing_regime = analyze_ongoing(df, r)
        else:
            m = analyze_termination(df, r)
            print(f"        VIX peak {m['vix_peak_close']} on "
                  f"{m['vix_peak_close_date'].date()}, "
                  f"lag {m['lag_td']:+d} td → {m['classification']}")
            completed.append(m)

    print(f"\n{'=' * 60}")
    print(f"  {len(completed)} completed + "
          f"{'1 ongoing' if ongoing_regime else '0 ongoing'}")
    print(f"{'=' * 60}")

    md = build_markdown(completed, ongoing_regime)
    out_path = RESEARCH_DIR / "2026-04-16_regime_termination_analysis.md"
    out_path.write_text(md)
    print(f"\n→ {out_path}")

    # Quick summary
    print("\n--- Classification Summary ---")
    for cls in ["PRE_EVENT_FADE", "COINCIDENT", "POST_EVENT_PERSIST", "GRADUAL_FADE"]:
        count = sum(1 for r in completed if r["classification"] == cls)
        ids = [f"R{r['id']}" for r in completed if r["classification"] == cls]
        print(f"  {cls}: {count} ({', '.join(ids)})")


if __name__ == "__main__":
    main()
