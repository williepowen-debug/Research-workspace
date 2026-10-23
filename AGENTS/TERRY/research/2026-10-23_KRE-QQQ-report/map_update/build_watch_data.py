"""Datasets for the divergence map's daily watch (TERRY, 2026-10-23).
kre_qqq_daily.csv  — KRE, QQQ (dividend-adjusted), ^TNX; daily % moves; 10y change in bp; 20-session corr;
                     rolling 20/60-session slope of KRE daily % on 10y daily bp change, as % KRE per +10 bp.
watch_refs.csv     — sourced constants: REGINALD's carried fit, FOMC date, thresholds TERRY defined.
episodes_2006.csv  — completed KRE/QQQ see-saw episodes since 2006 (../episode_study/episodes.csv).
Run: .venv/bin/python -I build_watch_data.py
"""
import os, time
import pandas as pd
import yfinance as yf
HERE = os.path.dirname(os.path.abspath(__file__)); UP = os.path.dirname(HERE)
for i in range(4):
    try:
        px = yf.download(["KRE", "QQQ", "^TNX"], start="2023-06-01", interval="1d", auto_adjust=True, progress=False)["Close"]; break
    except Exception:
        if i == 3: raise
        time.sleep(5 * (i + 1))
px = px.dropna(subset=["KRE", "QQQ"]); px["^TNX"] = px["^TNX"].ffill()
d = pd.DataFrame(index=px.index)
d["kre"] = px["KRE"].round(4); d["qqq"] = px["QQQ"].round(4); d["ten_year"] = px["^TNX"].round(3)
kr = px["KRE"].pct_change() * 100; qr = px["QQQ"].pct_change() * 100; tb = px["^TNX"].diff() * 100
d["kre_ret_pct"] = kr.round(3); d["qqq_ret_pct"] = qr.round(3); d["ten_chg_bp"] = tb.round(1)
d["corr20"] = kr.rolling(20).corr(qr).round(4)
for n in (20, 60):
    d[f"kre_per_10bp_{n}"] = (kr.rolling(n).cov(tb) / tb.rolling(n).var() * 10).round(3)
d = d[d.index >= "2024-01-02"]; d.index.name = "date"; d.index = d.index.strftime("%Y-%m-%d")
d.to_csv(os.path.join(HERE, "kre_qqq_daily.csv"))
print("daily rows", len(d), d.index[0], "->", d.index[-1]); print(d.tail(3).to_string())

refs = pd.DataFrame([
    ("reginald_beta", "KRE per +10 bp in the 10-year, carried figure", -0.72, "%", "REGINALD 57-session joint fit with HY, 2026-08-04 to 2026-10-22, R² 0.13 (weak); packet 012e5c08c"),
    ("reginald_r2", "Fit quality (R²) of the carried figure", 0.13, "", "REGINALD packet 012e5c08c"),
    ("signal_date", "See-saw signal: 20-day correlation first at or below -0.24", "2026-10-22", "date", "TERRY episode_study (corr -0.2357 at the 10/22 close)"),
    ("median_runway", "Median sessions until correlation back above 0, 13 past episodes since 2006", 16, "sessions", "TERRY episode_study/RESULTS.md"),
    ("fomc_date", "Fed decision (FOMC), 14:00 ET", "2026-10-28", "date", "PROME DOCKET L773 (Fed calendar, read 10/21)"),
    ("ratio_rollover_pct", "Ratio rolling over: KRE/QQQ at least this far below its peak since Oct 6", 3, "%", "TERRY definition (10/23 break list)"),
    ("joint_day_pct", "Joint down day: both KRE and QQQ at or below this daily move", -1, "%", "TERRY definition (10/23 break list)"),
    ("ten_up_bp", "10-year turning up: rise over 5 sessions at least", 15, "bp", "TERRY definition (sent to REGINALD 10/23 as alarm 2)"),
    ("alarm_ten_bp", "Alarm: KRE closes down on a session the 10-year falls at least", -5, "bp", "TERRY proposal to REGINALD 10/23 (ae7d13dc1); REGINALD's answer governs"),
], columns=["key", "label", "value", "unit", "source"])
refs.to_csv(os.path.join(HERE, "watch_refs.csv"), index=False)

ep = pd.read_csv(os.path.join(UP, "episode_study", "episodes.csv"))
ep = ep[ep["signal"] < "2026-10-22"][["signal", "dir", "class20", "joint_fall40", "joint_rally40", "sessions_to_corr_above0", "KRE+40", "QQQ+40"]]
ep.columns = ["signal", "leader", "class_at_20", "both_fell_5pct_40d", "both_rose_5pct_40d", "runway_sessions", "kre_40d", "qqq_40d"]
ep["leader"] = ep["leader"].str.replace("KRE over QQQ", "banks").str.replace("QQQ over KRE", "tech")
ep["kre_40d"] = (ep["kre_40d"] * 100).round(1); ep["qqq_40d"] = (ep["qqq_40d"] * 100).round(1)
ep.to_csv(os.path.join(HERE, "episodes_2006.csv"), index=False)
print(ep.to_string())
