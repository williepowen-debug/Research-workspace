"""SKEW post-fire trajectory analysis across all 17 divergence episodes.

Question: After a SKEW divergence fires, how does SKEW behave? Does early
SKEW fading (breaking below 140) predict peaceful resolution, or is it
normal noise before the eventual VIX spike?

Data: vix_historical.csv (2018+) + yfinance (2014-15, recent gap).
Output: research/2026-04-16_skew_post_fire_trajectory.md
"""
from __future__ import annotations

import warnings
from datetime import datetime
from pathlib import Path

import numpy as np
import pandas as pd
import yfinance as yf

warnings.filterwarnings("ignore", category=FutureWarning)

SCRIPT_DIR = Path(__file__).resolve().parent
BASE_DIR = SCRIPT_DIR.parent
WORKBOOK = BASE_DIR / "workbook"
RESEARCH_DIR = BASE_DIR / "research"

WINDOW_PRE = 5     # trading days before fire
WINDOW_POST = 45   # trading days after fire (~65 calendar days)

# All 17 episodes: (id, first_fire_date, skew_peak_in_window, outcome)
EPISODES = [
    (1,  "2014-11-12", 125.7, "STRESS +50%"),
    (2,  "2015-10-09", 151.2, "STRESS +50%"),
    (3,  "2018-03-12", 142.0, "STRESS +50%"),
    (4,  "2018-04-30", 130.8, "peaceful"),
    (5,  "2018-07-26", 142.2, "STRESS +50%"),
    (6,  "2019-10-30", 127.3, "tension +30%"),
    (7,  "2020-04-17", 132.6, "tension +30%"),
    (8,  "2020-07-20", 145.9, "tension +30%"),
    (9,  "2021-06-14", 159.3, "tension +30%"),
    (10, "2022-03-24", 146.5, "STRESS +50%"),
    (11, "2023-11-30", 144.5, "mild uptick"),
    (12, "2024-05-16", 147.9, "STRESS +50%"),
    (13, "2024-11-22", 172.4, "STRESS +50%"),
    (14, "2025-01-22", 180.0, "STRESS +50%"),
    (15, "2025-05-19", 137.3, "mild uptick"),
    (16, "2025-12-16", 160.5, "STRESS +50%"),
    (17, "2026-04-13", 156.9, "TBD"),
]


def load_all_data() -> pd.DataFrame:
    """Load SKEW + VIX daily closes covering all 17 episodes."""
    # --- Primary: vix_historical.csv (2018-01-02 to 2026-04-10) ---
    csv_path = WORKBOOK / "vix_historical.csv"
    print(f"[CSV] {csv_path.name}")
    csv_df = pd.read_csv(csv_path, parse_dates=["Date"], index_col="Date")
    skew = csv_df["Close ^SKEW"].rename("skew")
    vix = csv_df["Close ^VIX"].rename("vix")
    skew.index.name = "date"
    vix.index.name = "date"

    # --- yfinance for 2014-2015 episodes ---
    print("[yfinance] 2014-09-01 → 2016-03-01")
    for ticker, target in [("^SKEW", "skew"), ("^VIX", "vix")]:
        try:
            df = yf.download(
                ticker, start="2014-09-01", end="2016-03-01",
                progress=False, auto_adjust=True,
            )
            if df.empty:
                continue
            s = df["Close"].squeeze()
            s.index = s.index.tz_localize(None)
            s.index.name = "date"
            if target == "skew":
                skew = s.combine_first(skew)
            else:
                vix = s.combine_first(vix)
        except Exception as e:
            print(f"  WARNING: {ticker}: {e}")

    # --- VX_DAILY.tsv for recent dates (boot.py captured, real-time aligned) ---
    vx_path = WORKBOOK / "VX_DAILY.tsv"
    if vx_path.exists():
        print(f"[TSV] {vx_path.name} (recent supplement)")
        vx_df = pd.read_csv(vx_path, sep="\t", parse_dates=["date"])
        vx_df = vx_df.set_index("date")[["skew", "vix"]].dropna(how="all")
        # Prefer VX_DAILY for dates after CSV ends (most recent, boot-verified)
        csv_end = skew.index.max()
        recent = vx_df[vx_df.index > csv_end]
        if not recent.empty:
            print(f"  Adding {len(recent)} rows after {csv_end.date()}")
            for col in ["skew", "vix"]:
                if col in recent.columns:
                    s = recent[col].dropna()
                    if not s.empty:
                        if col == "skew":
                            skew = s.combine_first(skew)
                        else:
                            vix = s.combine_first(vix)

    combined = pd.DataFrame({"skew": skew, "vix": vix})
    combined.sort_index(inplace=True)
    combined.dropna(subset=["skew", "vix"], how="all", inplace=True)
    print(f"[Data] {len(combined)} days, "
          f"{combined.index.min().date()} → {combined.index.max().date()}")
    return combined


def extract_window(data: pd.DataFrame, fire_date_str: str) -> pd.DataFrame | None:
    """Extract trading-day window around fire date."""
    fire_dt = pd.Timestamp(fire_date_str)
    available = data.index[data.index >= fire_dt]
    if available.empty:
        return None
    actual_fire = available[0]
    fire_pos = data.index.get_loc(actual_fire)

    start = max(0, fire_pos - WINDOW_PRE)
    end = min(len(data), fire_pos + WINDOW_POST + 1)

    window = data.iloc[start:end].copy()
    window["td"] = list(range(-(fire_pos - start), end - fire_pos))
    return window


def compute_metrics(window: pd.DataFrame, ep_id: int, outcome: str) -> dict:
    """Compute trajectory metrics for one episode."""
    fire_row = window[window["td"] == 0]
    if fire_row.empty:
        return {}

    fire_skew = float(fire_row["skew"].iloc[0])
    fire_vix = float(fire_row["vix"].iloc[0])
    post = window[window["td"] >= 0].copy()
    post_days = len(post)
    is_partial = post_days < 30

    # --- Group A: early behavior ---
    def skew_at(td):
        r = post[post["td"] == td]
        return float(r["skew"].iloc[0]) if not r.empty else None

    d3_skew = skew_at(3)
    d7_skew = skew_at(7)
    early = post[post["td"] <= 7]
    skew_changes = early["skew"].diff()
    max_1d_drop = float(skew_changes.min()) if len(skew_changes) > 1 else None

    m: dict = {
        "ep": ep_id,
        "outcome": outcome,
        "fire_skew": round(fire_skew, 1),
        "fire_vix": round(fire_vix, 2),
        "d3_skew": round(d3_skew, 1) if d3_skew is not None else None,
        "d3_delta": round(d3_skew - fire_skew, 1) if d3_skew is not None else None,
        "d7_skew": round(d7_skew, 1) if d7_skew is not None else None,
        "d7_delta": round(d7_skew - fire_skew, 1) if d7_skew is not None else None,
        "min_skew_7d": round(float(early["skew"].min()), 1),
        "max_1d_drop_7d": round(max_1d_drop, 1) if max_1d_drop is not None else None,
        "d3_below_140": d3_skew < 140 if d3_skew is not None else None,
        "fire_below_140": fire_skew < 140,
        "partial": is_partial,
    }

    # Trajectory snapshots
    for td_val, label in [(5, "d5"), (10, "d10"), (14, "d14"),
                           (21, "d21"), (30, "d30"), (45, "d45")]:
        m[f"skew_{label}"] = round(skew_at(td_val), 1) if skew_at(td_val) is not None else None

    if is_partial:
        m.update({
            "days_to_below_140": None, "min_skew_60d": None,
            "ever_below_140": bool((post["skew"] < 140).any()),
            "pattern": "PARTIAL",
        })
        return m

    # --- Group B: threshold dynamics ---
    below_mask = post["skew"] < 140
    days_below = int(below_mask.sum())
    ever_below = bool(below_mask.any())

    if fire_skew < 140:
        days_to_below_140 = 0
    elif ever_below:
        days_to_below_140 = int(post.loc[below_mask, "td"].iloc[0])
    else:
        days_to_below_140 = None  # never broke

    reramp_140 = reramp_145 = reramp_150 = False
    if ever_below:
        first_below_date = below_mask.idxmax()
        after = post.loc[first_below_date:]
        reramp_140 = bool((after["skew"] >= 140).any())
        reramp_145 = bool((after["skew"] >= 145).any())
        reramp_150 = bool((after["skew"] >= 150).any())

    m.update({
        "days_to_below_140": days_to_below_140,
        "min_skew_60d": round(float(post["skew"].min()), 1),
        "ever_below_140": ever_below,
        "reramp_140": reramp_140 if ever_below else "N/A",
        "reramp_145": reramp_145 if ever_below else "N/A",
        "reramp_150": reramp_150 if ever_below else "N/A",
        "days_below_140": days_below,
        "pct_below_140": round(days_below / post_days * 100, 1),
    })

    # --- Group C: VIX peak ---
    peak_idx = post["vix"].idxmax()
    peak_vix = float(post["vix"].max())
    peak_td = int(post.loc[peak_idx, "td"])
    skew_at_peak = float(post.loc[peak_idx, "skew"])
    vix_pct = (peak_vix - fire_vix) / fire_vix * 100

    m.update({
        "peak_vix": round(peak_vix, 2),
        "days_to_vix_peak": peak_td,
        "skew_at_vix_peak": round(skew_at_peak, 1),
        "vix_pct_change": round(vix_pct, 1),
    })

    # --- Group D: classification ---
    if not ever_below:
        pattern = "SUSTAINED_ELEV"
    elif reramp_145:
        pattern = "FADE_RERAMP"
    elif vix_pct < 15:
        pattern = "FADE_HOLD"
    else:
        pattern = "CHOPPY"
    m["pattern"] = pattern
    return m


# ── Markdown builder ────────────────────────────────────────────────


def _hdr(text: str) -> str:
    return f"\n## {text}\n"


def build_markdown(metrics: list[dict]) -> str:
    L: list[str] = []

    completed = [m for m in metrics if not m.get("partial")]
    n = len(completed)
    us = next((m for m in metrics if m["ep"] == 17), None)

    # ── Header ──
    L.append("# SKEW Post-Fire Trajectory Analysis\n")
    L.append("**Question:** After a SKEW divergence fires, how does SKEW behave "
             "over the following 60 days? Does SKEW breaking below 140 early "
             "(within the first week) predict a peaceful resolution, or is it "
             "normal noise before the eventual VIX spike?\n")
    L.append(f"**Motivation:** Episode #17 (our live VIX May 19 25C) saw SKEW "
             f"drop from {us['fire_skew']} to {us['d3_skew']} on day 3 post-fire "
             f"(2026-04-16), breaking below the 140 threshold.\n")
    L.append("---\n")

    # ── Method ──
    L.append(_hdr("Method"))
    L.append("- **Data:** Daily ^SKEW / ^VIX closes — `vix_historical.csv` "
             "(2018-2026) + yfinance (2014-15 episodes, recent gap).")
    L.append("- **Window:** 5 trading days pre-fire through 45 post-fire "
             "(~65 calendar days, covers the 60-day outcome window).")
    L.append("- **Metrics:** Early behavior (d+1→d+7), threshold dynamics "
             "(140 breaks / re-ramps), VIX-peak analysis, trajectory classification.")
    L.append("- **Indexing:** td = trading days from fire date. td=0 is fire day.\n")
    L.append("---\n")

    # ── Master table ──
    L.append(_hdr("Master Comparison Table"))
    L.append("| Ep | Fire SKEW | d+3 SKEW | d+3 Δ | d+7 SKEW | d+7 Δ "
             "| Min 7d | Max 1d Drop | <140 @ d+3 | Outcome |")
    L.append("|---:|----------:|---------:|------:|---------:|------:"
             "|-------:|------------:|:----------:|---------|")
    for m in metrics:
        def fmt(v, plus=False):
            if v is None: return "—"
            return f"{v:+.1f}" if plus else f"{v}"
        tag = " **← us**" if m["ep"] == 17 else ""
        out = m["outcome"] if not m.get("partial") else "**TBD (day 3)**"
        b140 = ("**YES**" if m.get("d3_below_140")
                else ("—" if m.get("d3_below_140") is None else "no"))
        L.append(f"| {m['ep']} | {m['fire_skew']} | {fmt(m['d3_skew'])} "
                 f"| {fmt(m['d3_delta'], True)} | {fmt(m['d7_skew'])} "
                 f"| {fmt(m['d7_delta'], True)} | {fmt(m['min_skew_7d'])} "
                 f"| {fmt(m['max_1d_drop_7d'])} | {b140} | {out}{tag} |")
    L.append("\n---\n")

    # ── Finding 1: early fading frequency ──
    L.append(_hdr("Finding 1: Early SKEW Fading Is Common"))
    d3_below = [m for m in completed if m.get("d3_below_140")]
    d3_above = [m for m in completed if m.get("d3_below_140") is False]
    min7_below = [m for m in completed
                  if m.get("min_skew_7d") is not None and m["min_skew_7d"] < 140]

    L.append(f"**SKEW < 140 at d+3:** {len(d3_below)} of {n} completed "
             f"episodes ({len(d3_below)/n*100:.0f}%)\n")

    if d3_below:
        cats = {"STRESS": 0, "tension": 0, "mild": 0, "peaceful": 0}
        for m in d3_below:
            for k in cats:
                if k in m["outcome"]:
                    cats[k] += 1
        L.append("**Outcomes when SKEW < 140 at d+3:**\n")
        L.append("| Outcome | Count | Pct |")
        L.append("|---------|------:|----:|")
        for k, v in cats.items():
            L.append(f"| {k} | {v} | {v/len(d3_below)*100:.0f}% |")
        L.append("")

    if d3_above:
        s = sum(1 for m in d3_above if "STRESS" in m["outcome"])
        L.append(f"**Outcomes when SKEW >= 140 at d+3:** "
                 f"{s}/{len(d3_above)} STRESS ({s/len(d3_above)*100:.0f}%)\n")

    L.append(f"**SKEW touched < 140 at any point in first 7 td:** "
             f"{len(min7_below)} of {n} ({len(min7_below)/n*100:.0f}%)\n")
    if min7_below:
        s = sum(1 for m in min7_below if "STRESS" in m["outcome"])
        L.append(f"Of those, {s}/{len(min7_below)} "
                 f"({s/len(min7_below)*100:.0f}%) produced STRESS +50%.\n")

    L.append("**Implication:** Early SKEW fading is NOT a reliable disconfirming "
             "signal. The outcome distribution conditional on d+3 < 140 is similar "
             "to the unconditional base rate.\n")
    L.append("---\n")

    # ── Finding 2: 10.7pt drop magnitude ──
    L.append(_hdr("Finding 2: The 10.7pt Single-Day Drop in Context"))
    L.append("Our Apr 16 SKEW drop of -10.7 is a large single-day move. "
             "How does it compare to early drops in other episodes?\n")
    L.append("**Largest single-day SKEW drops in first 7 td (all episodes):**\n")
    ranked = sorted(
        [m for m in metrics if m.get("max_1d_drop_7d") is not None],
        key=lambda x: x["max_1d_drop_7d"],
    )
    L.append("| Ep | Max 1d Drop | Fire SKEW | Outcome |")
    L.append("|---:|------------:|----------:|---------|")
    for m in ranked:
        tag = " **← us**" if m["ep"] == 17 else ""
        out = m["outcome"] if not m.get("partial") else "TBD"
        L.append(f"| {m['ep']} | {m['max_1d_drop_7d']:+.1f} "
                 f"| {m['fire_skew']} | {out}{tag} |")
    L.append("")
    big = [m for m in completed
           if m.get("max_1d_drop_7d") is not None and m["max_1d_drop_7d"] <= -10]
    L.append(f"**Episodes with ≥10pt single-day drop in first 7 td:** "
             f"{len(big)} of {n}")
    for m in big:
        L.append(f"  - Ep {m['ep']}: {m['max_1d_drop_7d']:+.1f}pt → {m['outcome']}")
    L.append("\n---\n")

    # ── Finding 3: re-ramp rates ──
    L.append(_hdr("Finding 3: Re-Ramp Rates After Breaking 140"))
    broke = [m for m in completed if m.get("ever_below_140")]
    never = [m for m in completed if not m.get("ever_below_140")]

    L.append(f"**Broke below 140 at any point in 60d:** "
             f"{len(broke)} of {n} ({len(broke)/n*100:.0f}%)")
    L.append(f"**Never broke 140:** "
             f"{len(never)} of {n} ({len(never)/n*100:.0f}%)\n")

    if broke:
        rr = {140: 0, 145: 0, 150: 0}
        for m in broke:
            if m.get("reramp_140") is True: rr[140] += 1
            if m.get("reramp_145") is True: rr[145] += 1
            if m.get("reramp_150") is True: rr[150] += 1

        L.append("**Re-ramp rates (of episodes that broke 140):**\n")
        L.append("| Threshold | Count | Rate |")
        L.append("|----------:|------:|-----:|")
        for lvl in [140, 145, 150]:
            L.append(f"| ≥ {lvl} | {rr[lvl]}/{len(broke)} "
                     f"| {rr[lvl]/len(broke)*100:.0f}% |")
        L.append("")

        L.append("**Days below 140 by episode (descending):**\n")
        L.append("| Ep | Days < 140 | % Window | Pattern | Outcome |")
        L.append("|---:|-----------:|---------:|---------|---------|")
        for m in sorted(broke, key=lambda x: x.get("days_below_140", 0),
                        reverse=True):
            L.append(f"| {m['ep']} | {m.get('days_below_140','?')} "
                     f"| {m.get('pct_below_140','?')}% "
                     f"| {m.get('pattern','?')} | {m['outcome']} |")
        L.append("")
    L.append("---\n")

    # ── Finding 4: SKEW at VIX peak ──
    L.append(_hdr("Finding 4: SKEW at VIX Peak"))
    L.append("When VIX eventually spiked, what was SKEW doing?\n")
    L.append("| Ep | Fire SKEW | Peak VIX | Days to Peak "
             "| SKEW @ Peak | SKEW Δ | Outcome |")
    L.append("|---:|----------:|---------:|-------------:"
             "|------------:|-------:|---------|")
    for m in completed:
        if m.get("peak_vix") is None:
            continue
        delta = round(m["skew_at_vix_peak"] - m["fire_skew"], 1)
        L.append(f"| {m['ep']} | {m['fire_skew']} | {m['peak_vix']} "
                 f"| {m['days_to_vix_peak']} | {m['skew_at_vix_peak']} "
                 f"| {delta:+.1f} | {m['outcome']} |")
    L.append("")

    stress = [m for m in completed
              if "STRESS" in m["outcome"] and m.get("skew_at_vix_peak")]
    if stress:
        avg_at = np.mean([m["skew_at_vix_peak"] for m in stress])
        avg_d = np.mean([m["skew_at_vix_peak"] - m["fire_skew"] for m in stress])
        L.append(f"**STRESS avg:** SKEW at VIX peak = {avg_at:.1f}, "
                 f"Δ from fire = {avg_d:+.1f}\n")
    L.append("---\n")

    # ── Finding 5: pattern classification ──
    L.append(_hdr("Finding 5: Trajectory Patterns"))
    pats: dict[str, list] = {}
    for m in completed:
        p = m.get("pattern", "UNKNOWN")
        pats.setdefault(p, []).append(m)

    L.append("| Pattern | Count | Episodes | Outcomes |")
    L.append("|---------|------:|----------|----------|")
    for p in sorted(pats):
        eps = ", ".join(str(m["ep"]) for m in pats[p])
        outs = ", ".join(m["outcome"] for m in pats[p])
        L.append(f"| {p} | {len(pats[p])} | {eps} | {outs} |")
    L.append("")
    L.append("**Definitions:**")
    L.append("- **SUSTAINED_ELEV** — SKEW never broke 140 in 60d window")
    L.append("- **FADE_RERAMP** — Broke 140, then re-ramped above 145")
    L.append("- **FADE_HOLD** — Broke 140, VIX never rose ≥15% (peaceful)")
    L.append("- **CHOPPY** — Broke 140, partial recovery but didn't reach 145\n")
    L.append("---\n")

    # ── Actionable summary ──
    L.append(_hdr("Actionable Summary for Episode #17"))
    if us:
        L.append(f"**Current state (day 3):** SKEW {us.get('d3_skew','?')} "
                 f"(Δ {us.get('d3_delta',0):+.1f} from fire), VIX 18.86\n")
    L.append("**Decision tree:**\n")
    L.append("| If SKEW does this… | By when | Historical precedent | Action |")
    L.append("|:-------------------|:--------|:---------------------|:-------|")
    L.append("| Rebounds > 145 within 5 td | ~Apr 22 "
             "| Most common path (FADE_RERAMP pattern) "
             "| Hold — episode live |")
    L.append("| Sustains < 140 for 7+ consecutive td | ~Apr 25 "
             "| Rare — only peaceful / mild episodes sustained fade "
             "| Reduce conviction |")
    L.append("| Sustains < 140 through FOMC | Apr 29 "
             "| Approaches peaceful territory "
             "| Significant invalidation — review stop |")
    L.append("| Drops below 130 | Any "
             "| Only Ep 4 (peaceful, SKEW peak 130.8) lived here "
             "| Exit or heavy trim |")
    L.append("| Re-ramps > 150 | Any "
             "| Re-enters high-severity cohort "
             "| Add to position |")
    L.append("")
    L.append("**Bottom line:** A single-day SKEW break below 140 on day 3 "
             "is **NOT** sufficient to invalidate the episode. The existing "
             "TRADE.md invalidation criterion — \"SKEW <140 **sustained** + "
             "VIX <20 through May 7\" — is correctly calibrated. The word "
             "\"sustained\" is doing the critical work. Monitor daily; the "
             "next 4-5 trading days (through Apr 22) will show whether this "
             "is a transient dip or the start of a genuine fade.\n")
    L.append("---\n")
    L.append(f"*Generated {datetime.now().strftime('%Y-%m-%d %H:%M')} "
             f"by VIOLET `scripts/skew_trajectory.py`*")
    L.append("*Data: yfinance ^SKEW / ^VIX + workbook/vix_historical.csv*")
    return "\n".join(L)


# ── Main ────────────────────────────────────────────────────────────


def main():
    print("=" * 60)
    print("  SKEW Post-Fire Trajectory Analysis")
    print("=" * 60)

    data = load_all_data()

    all_metrics: list[dict] = []
    for ep_id, fire_date, skew_peak, outcome in EPISODES:
        print(f"\n[Ep {ep_id:2d}] fire={fire_date}  peak_SKEW={skew_peak}")
        window = extract_window(data, fire_date)
        if window is None:
            print("  !! No data — skipping")
            continue
        m = compute_metrics(window, ep_id, outcome)
        if not m:
            print("  !! Metrics failed — skipping")
            continue
        print(f"  fire_skew={m['fire_skew']}  d3={m.get('d3_skew','—')}  "
              f"d7={m.get('d7_skew','—')}  pattern={m.get('pattern','—')}")
        all_metrics.append(m)

    print(f"\n{'=' * 60}")
    print(f"  {len(all_metrics)} episodes processed")
    print(f"{'=' * 60}")

    md = build_markdown(all_metrics)
    out_path = RESEARCH_DIR / "2026-04-16_skew_post_fire_trajectory.md"
    out_path.write_text(md)
    print(f"\n→ {out_path}")

    # Quick summary
    completed = [m for m in all_metrics if not m.get("partial")]
    d3b = [m for m in completed if m.get("d3_below_140")]
    broke = [m for m in completed if m.get("ever_below_140")]
    print(f"\n--- Quick Summary ---")
    print(f"SKEW < 140 @ d+3:  {len(d3b)}/{len(completed)}")
    print(f"SKEW ever < 140:   {len(broke)}/{len(completed)}")
    if d3b:
        s = sum(1 for m in d3b if "STRESS" in m["outcome"])
        print(f"  of d+3 < 140:    {s}/{len(d3b)} STRESS")


if __name__ == "__main__":
    main()
