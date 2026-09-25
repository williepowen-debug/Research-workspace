#!/usr/bin/env python3
"""MIDAS band base-rate study — SLV / PPLT / PALL (+ GLD reference, CPER for corr).

Read-only research instrument. Pulls yfinance daily bars (auto_adjust=False, Close),
drops any bar dated today if run before 16:30 ET (partial intraday bar), and computes:
  1. distance from 200d SMA (%)       — percentiles, threshold fractions, today's rank
  2. rolling 63-session return (%)     — same, down + up
  3. drawdown from running 252d high   — same
  4. 200dma episodes (cross < -12 / -20, end on recovery > -5) + upside episodes
  5. 2026 first-crossing dates
  6. daily-return correlations (2020+, last 120 sessions)
  7. upside spikes (200dma distance > +20/+30/+40)
Outputs: band_stats.md (+ raw CSV cache) next to this script.

Run: /home/willi/Research-workspace/.venv/bin/python band_stats.py
"""
import datetime as dt
import os
import sys
from zoneinfo import ZoneInfo

import numpy as np
import pandas as pd
import yfinance as yf

OUT = os.path.dirname(os.path.abspath(__file__))
TICKERS = ["SLV", "PPLT", "PALL", "GLD", "CPER"]
STUDY = ["SLV", "PPLT", "PALL", "GLD"]
PCTS = [1, 5, 10, 25, 50, 75, 90, 95, 99]
WINDOWS = {"full": None, "2020+": "2020-01-01"}


def load():
    now_et = dt.datetime.now(ZoneInfo("America/New_York"))
    closes, vols, notes = {}, {}, []
    for t in TICKERS:
        d = yf.download(t, period="max", auto_adjust=False, progress=False)
        if isinstance(d.columns, pd.MultiIndex):
            d.columns = d.columns.get_level_values(0)
        d = d[["Close", "Volume"]].dropna(subset=["Close"])
        last = d.index[-1].date()
        if last == now_et.date() and now_et.time() < dt.time(16, 30):
            notes.append(f"{t}: dropped partial intraday bar {last} (run at {now_et:%Y-%m-%d %H:%M} ET)")
            d = d.iloc[:-1]
        d.to_csv(os.path.join(OUT, f"raw_{t}.csv"))
        closes[t] = d["Close"]
        vols[t] = d["Volume"]
    return pd.DataFrame(closes), pd.DataFrame(vols), notes, now_et


def data_quality(px, vol):
    rows = []
    for t in TICKERS:
        s = px[t].dropna()
        v = vol[t].reindex(s.index)
        r = s.pct_change().dropna()
        gaps = s.index.to_series().diff().dt.days
        big = r[r.abs() > 0.15]
        zero_v = int((v == 0).sum())
        # missing vs the union NYSE calendar across the other tickers (after inception)
        cal = px.index[px.index >= s.index[0]]
        missing = int(px[t].reindex(cal).isna().sum())
        first_yr = v[v.index < s.index[0] + pd.Timedelta(days=365)]
        sp = yf.Ticker(t).splits
        splits = ", ".join(f"{d.date()} {x:g}:1" for d, x in sp.items()) or "none"
        rows.append(dict(t=t, splits=splits, start=s.index[0].date(), end=s.index[-1].date(), n=len(s),
                         max_gap_days=int(gaps.max()), missing_vs_union=missing,
                         zero_vol=zero_v, med_vol_first_yr=int(first_yr.median()),
                         med_vol_last_yr=int(v.iloc[-252:].median()),
                         jumps=", ".join(f"{d.date()} {x:+.1%}" for d, x in big.items()) or "none"))
    return pd.DataFrame(rows)


def metrics(s):
    sma = s.rolling(200, min_periods=200).mean()
    d200 = (s / sma - 1) * 100
    r63 = (s / s.shift(63) - 1) * 100
    hi = s.rolling(252, min_periods=252).max()
    dd = (s / hi - 1) * 100
    return pd.DataFrame({"px": s, "sma200": sma, "d200": d200, "r63": r63, "dd252": dd})


def win(x, w):
    return x if WINDOWS[w] is None else x[x.index >= WINDOWS[w]]


def rank(series, v):
    series = series.dropna()
    return 100.0 * (series <= v).mean()


def fmt(x, nd=1):
    return "—" if pd.isna(x) else f"{x:.{nd}f}"


def pct_table(M, col, title):
    lines = [f"| metal | window | n | first | " + " | ".join(f"p{p}" for p in PCTS) + " | today | rank |",
             "|---|---|---|---|" + "---|" * (len(PCTS) + 2)]
    for t in STUDY:
        for w in WINDOWS:
            x = win(M[t][col], w).dropna()
            q = np.percentile(x, PCTS)
            today = M[t][col].dropna().iloc[-1]
            lines.append(f"| {t} | {w} | {len(x)} | {x.index[0].date()} | " + " | ".join(fmt(v) for v in q)
                         + f" | **{fmt(today)}** | **p{fmt(rank(x, today), 0)}** |")
    return f"### {title}\n\n" + "\n".join(lines) + "\n"


def frac_table(M, col, down, up, title):
    hdr = [f"< {d}%" for d in down] + [f"> +{u}%" for u in up]
    lines = ["| metal | window | n | " + " | ".join(hdr) + " |", "|---|---|---|" + "---|" * len(hdr)]
    for t in STUDY:
        for w in WINDOWS:
            x = win(M[t][col], w).dropna()
            cells = [f"{100 * (x < d).mean():.1f}" for d in down] + [f"{100 * (x > u).mean():.1f}" for u in up]
            lines.append(f"| {t} | {w} | {len(x)} | " + " | ".join(cells) + " |")
    return f"### {title} (% of days)\n\n" + "\n".join(lines) + "\n"


def episodes(x, trig, reset, direction="down"):
    """Episode starts on first cross beyond trig; ends when recovers past reset."""
    x = x.dropna()
    out, inep, st = [], False, None
    for d, v in x.items():
        hit = v < trig if direction == "down" else v > trig
        rec = v > reset if direction == "down" else v < reset
        if not inep and hit:
            inep, st = True, d
        elif inep and rec:
            seg = x[st:d]
            tr = seg.idxmin() if direction == "down" else seg.idxmax()
            out.append((st, tr, seg[tr], d, len(seg) - 1, False))
            inep = False
    if inep:
        seg = x[st:]
        tr = seg.idxmin() if direction == "down" else seg.idxmax()
        out.append((st, tr, seg[tr], None, len(seg) - 1, True))
    return out


def ep_block(M, t, trig, reset, direction):
    x = M[t]["d200"].dropna()
    eps = episodes(x, trig, reset, direction)
    yrs_full = (x.index[-1] - x.index[0]).days / 365.25
    x20 = x[x.index >= "2020-01-01"]
    yrs_20 = (x20.index[-1] - x20.index[0]).days / 365.25
    n20 = sum(1 for e in eps if e[0] >= pd.Timestamp("2020-01-01"))
    sym = "<" if direction == "down" else ">"
    rsym = ">" if direction == "down" else "<"
    head = (f"**{t} — 200dma distance {sym} {trig:+}% (reset {rsym} {reset:+}%)**: {len(eps)} episodes over "
            f"{yrs_full:.1f}y = **{len(eps) / yrs_full:.2f}/yr** (full, from {x.index[0].date()}); "
            f"{n20} over {yrs_20:.1f}y = **{n20 / yrs_20:.2f}/yr** (2020+)\n\n")
    lines = ["| # | start | px@start | trough/peak date | extreme % | end | sessions |", "|---|---|---|---|---|---|---|"]
    for i, (st, tr, tv, en, n, ongoing) in enumerate(eps, 1):
        lines.append(f"| {i} | {st.date()} | {M[t]['px'][st]:.2f} | {tr.date()} | {tv:+.1f} | "
                     f"{'ONGOING' if ongoing else en.date()} | {n} |")
    return head + ("\n".join(lines) if eps else "_none_") + "\n\n", len(eps) / yrs_full, n20 / yrs_20


def first_cross_2026(M, t):
    df = M[t]
    y = df[df.index >= "2026-01-01"]
    peak_d = y["px"].idxmax()
    res = {"ytd_high": (peak_d.date(), y["px"].max())}
    for col, ths in [("d200", [-5, -12, -20]), ("dd252", [-10, -20, -30]), ("r63", [-10, -20, -30])]:
        for th in ths:
            hit = y[y[col] < th]
            res[(col, th)] = (hit.index[0].date(), hit["px"].iloc[0], hit[col].iloc[0],
                              hit.index[0] == y.index[0]) if len(hit) else None
            post = y[y.index > peak_d]
            h2 = post[post[col] < th]
            res[("post", col, th)] = (h2.index[0].date(), h2["px"].iloc[0], h2[col].iloc[0],
                                      100 * (h2["px"].iloc[0] / y["px"].max() - 1),
                                      int(((y.index > peak_d) & (y.index <= h2.index[0])).sum())) if len(h2) else None
    for th in [20, 30, 40]:
        hit = y[y["d200"] > th]
        res[("d200up", th)] = (hit.index[0].date(), hit["px"].iloc[0], hit["d200"].iloc[0],
                               hit.index[0] == y.index[0]) if len(hit) else None
    return res


def fc_cell(v):
    if v is None:
        return "not crossed"
    tag = " [already beyond on 1st 2026 session]" if v[3] else ""
    return f"{v[0]} @ {v[1]:.2f} ({v[2]:+.1f}){tag}"


def ep_rate(x, trig, reset, direction):
    x = x.dropna()
    eps = episodes(x, trig, reset, direction)
    yf_ = (x.index[-1] - x.index[0]).days / 365.25
    x20 = x[x.index >= "2020-01-01"]
    y20 = (x20.index[-1] - x20.index[0]).days / 365.25
    n20 = sum(1 for e in eps if e[0] >= pd.Timestamp("2020-01-01"))
    return len(eps), len(eps) / yf_, n20, n20 / y20, (eps[-1][0].date() if eps else None)


def main():
    px, vol, notes, now_et = load()
    M = {t: metrics(px[t].dropna()) for t in TICKERS}
    md = []
    md.append("# MIDAS band base rates — SLV / PPLT / PALL (GLD reference)\n")
    md.append(f"Generated {now_et:%Y-%m-%d %H:%M} ET by `band_stats.py` (yfinance, `auto_adjust=False` Close, "
              f"no-roll ETFs). Last complete close used: "
              + ", ".join(f"{t} {M[t].index[-1].date()} = {M[t]['px'].iloc[-1]:.2f}" for t in TICKERS) + ".\n")
    md.append("Definitions: **d200** = close / SMA200 − 1; **r63** = 63-session return; **dd252** = close / "
              "rolling-252-session max − 1. Percentile rank = % of days in window with value ≤ today. "
              "Windows: *full* = from first valid metric day (inception + 200/63/252 sessions); *2020+* = from 2020-01-01. "
              "n = trading days with a valid value.\n")

    # --- data quality
    dq = data_quality(px, vol)
    md.append("## 0. Data problems\n")
    md.append("| ticker | first | last | n | max calendar gap (d) | missing vs union calendar | zero-volume days | median vol yr1 | median vol last 252 | single-day moves >15% | Yahoo split events (back-adjusted in Close) |")
    md.append("|---|---|---|---|---|---|---|---|---|---|---|")
    for _, r in dq.iterrows():
        md.append(f"| {r.t} | {r.start} | {r.end} | {r.n} | {r.max_gap_days} | {r.missing_vs_union} | {r.zero_vol} | "
                  f"{r.med_vol_first_yr:,} | {r.med_vol_last_yr:,} | {r.jumps} | {r.splits} |")
    md.append("")
    for n in notes:
        md.append(f"- {n}")
    md.append("")

    # --- 1-3 percentiles
    md.append("## 1. Distance from 200-day SMA (%)\n")
    md.append(pct_table(M, "d200", "Percentiles"))
    md.append(frac_table(M, "d200", [-5, -10, -12, -15, -20, -25, -30], [20, 30, 40], "Threshold fractions"))
    md.append("## 2. Rolling 63-session return (%)\n")
    md.append(pct_table(M, "r63", "Percentiles"))
    md.append(frac_table(M, "r63", [-5, -10, -12, -15, -20, -25, -30], [10, 20, 30, 40], "Threshold fractions"))
    md.append("## 3. Drawdown from running 252-session high (%)\n")
    md.append(pct_table(M, "dd252", "Percentiles"))
    md.append(frac_table(M, "dd252", [-10, -20, -30, -40, -50], [], "Threshold fractions"))

    # --- 4 episodes
    md.append("## 4. Episodes — 200dma distance (downside)\n")
    md.append("Episode = first close below trigger; ends on first close back above −5% (the Yellow line). "
              "Start price is the ETF close on the trigger day. Fires/yr = episodes ÷ years of valid d200 history.\n")
    rates = {}
    for trig in [-12, -20]:
        md.append(f"### Trigger {trig}%\n")
        for t in STUDY:
            blk, rf, r20 = ep_block(M, t, trig, -5, "down")
            rates[(t, trig)] = (rf, r20)
            md.append(blk)
    # -5% yellow rate only (episode counts, no table — reset at 0)
    md.append("### Trigger −5% (reset above 0%) — rate only\n")
    md.append("| metal | episodes full | /yr full | episodes 2020+ | /yr 2020+ |\n|---|---|---|---|---|")
    for t in STUDY:
        x = M[t]["d200"].dropna()
        eps = episodes(x, -5, 0, "down")
        yf_ = (x.index[-1] - x.index[0]).days / 365.25
        x20 = x[x.index >= "2020-01-01"]
        y20 = (x20.index[-1] - x20.index[0]).days / 365.25
        n20 = sum(1 for e in eps if e[0] >= pd.Timestamp("2020-01-01"))
        rates[(t, -5)] = (len(eps) / yf_, n20 / y20)
        md.append(f"| {t} | {len(eps)} | {len(eps) / yf_:.2f} | {n20} | {n20 / y20:.2f} |")
    md.append("")

    md.append("## 4b. Fire rates for every candidate threshold (episodes per year)\n")
    md.append("Episode rule: starts on first close beyond trigger; ends on first close back past the reset. Resets: "
              "d200 down → −5% (for the −5% trigger: 0%); d200 up → +5%; r63 → 0%; dd252 → half the trigger "
              "(e.g. −20% resets above −10%). Full window starts at the first valid metric day.\n")
    md.append("| metal | metric | trigger | reset | episodes full | /yr full | episodes 2020+ | /yr 2020+ | last start |")
    md.append("|---|---|---|---|---|---|---|---|---|")
    specs = ([("d200", th, (0 if th == -5 else -5), "down") for th in [-5, -10, -12, -15, -20, -25]]
             + [("d200", th, 5, "up") for th in [20, 30, 40]]
             + [("r63", th, 0, "down") for th in [-10, -15, -20, -30]]
             + [("r63", th, 0, "up") for th in [20, 30, 40]]
             + [("dd252", th, th / 2, "down") for th in [-10, -20, -30, -40]])
    for t in STUDY:
        for col, th, rs, dr in specs:
            n, rf, n20, r20, last = ep_rate(M[t][col], th, rs, dr)
            md.append(f"| {t} | {col} | {'<' if dr == 'down' else '>'} {th:+}% | {rs:+g}% | {n} | {rf:.2f} | {n20} | {r20:.2f} | {last or '—'} |")
    md.append("")

    # --- 5 2026 crossings
    md.append("## 5. 2026 first-crossing dates (first close in 2026 beyond threshold; ETF close that day)\n")
    cols = [("d200", -5), ("d200", -12), ("d200", -20), ("dd252", -10), ("dd252", -20), ("dd252", -30),
            ("r63", -10), ("r63", -20), ("r63", -30)]
    md.append("| metal | 2026 high (date, px) | " + " | ".join(f"{c} {th}%" for c, th in cols) + " |")
    md.append("|---|---|" + "---|" * len(cols))
    for t in STUDY:
        res = first_cross_2026(M, t)
        cells = [fc_cell(res[k]) for k in cols]
        md.append(f"| {t} | {res['ytd_high'][0]} {res['ytd_high'][1]:.2f} | " + " | ".join(cells) + " |")
    md.append("")
    md.append("**After the 2026 peak** — first close AFTER each metal's 2026 closing high beyond the threshold. "
              "Cell = date @ ETF close (metric value) · % below the 2026 high at that close · sessions after the high. "
              "This is the answer to 'would the band have caught the Jan→Sep collapse, and how late'.\n")
    md.append("| metal | 2026 high | " + " | ".join(f"{c} {th}%" for c, th in cols) + " |")
    md.append("|---|---|" + "---|" * len(cols))
    for t in STUDY:
        res = first_cross_2026(M, t)
        cells = []
        for k in cols:
            v = res[("post",) + k]
            cells.append("not crossed" if v is None else f"{v[0]} @ {v[1]:.2f} ({v[2]:+.1f}) · {v[3]:+.1f}% · s{v[4]}")
        md.append(f"| {t} | {res['ytd_high'][0]} {res['ytd_high'][1]:.2f} | " + " | ".join(cells) + " |")
    md.append("")
    md.append("Upside in 2026 (first close with d200 above threshold):\n")
    md.append("| metal | > +20% | > +30% | > +40% |\n|---|---|---|---|")
    for t in STUDY:
        res = first_cross_2026(M, t)
        md.append(f"| {t} | " + " | ".join(fc_cell(res[("d200up", th)]) for th in [20, 30, 40]) + " |")
    md.append("")
    # 2026 path table: monthly-end values of d200 / dd252 per metal
    md.append("2026 month-end path (d200 / dd252, %):\n")
    me = {t: M[t][M[t].index >= "2026-01-01"].resample("ME").last() for t in STUDY}
    md.append("| month-end | " + " | ".join(f"{t} px / d200 / dd252" for t in STUDY) + " |")
    md.append("|---|" + "---|" * len(STUDY))
    for d in me["SLV"].index:
        lab = f"{M['SLV'].index[-1].date()} (MTD, last close)" if d == me["SLV"].index[-1] else str(d.date())
        md.append(f"| {lab} | " + " | ".join(
            f"{me[t].loc[d, 'px']:.2f} / {me[t].loc[d, 'd200']:+.1f} / {me[t].loc[d, 'dd252']:+.1f}" for t in STUDY) + " |")
    md.append("")

    # --- 6 correlations
    md.append("## 6. Daily-return correlations (close-to-close, pairwise-complete)\n")
    rets = px[TICKERS].pct_change(fill_method=None)
    for label, sub in [("2020-01-01 → last close", rets[rets.index >= "2020-01-01"]),
                       ("last 120 sessions", rets.dropna().iloc[-120:])]:
        c = sub.corr()
        md.append(f"**{label}** (n = {len(sub.dropna())} common days, {sub.dropna().index[0].date()} → {sub.dropna().index[-1].date()})\n")
        md.append("| | " + " | ".join(TICKERS) + " |\n|---|" + "---|" * len(TICKERS))
        for a in TICKERS:
            md.append(f"| {a} | " + " | ".join(f"{c.loc[a, b]:.2f}" for b in TICKERS) + " |")
        md.append("")
    # co-firing: days where d200 < -12 on SLV, PPLT, PALL simultaneously
    D = pd.DataFrame({t: M[t]["d200"] for t in ["SLV", "PPLT", "PALL"]}).dropna()
    for th in [-12, -20]:
        b = D < th
        any_ = b.any(axis=1).sum()
        all3 = b.all(axis=1).sum()
        ge2 = (b.sum(axis=1) >= 2).sum()
        md.append(f"- Co-firing, d200 < {th}% (common window {D.index[0].date()} → {D.index[-1].date()}, n={len(D)}): "
                  f"any-of-3 {any_} days; ≥2 of 3 {ge2} days ({100 * ge2 / max(any_, 1):.0f}% of any-days); "
                  f"all 3 {all3} days ({100 * all3 / max(any_, 1):.0f}% of any-days).")
    md.append("")

    # --- 7 upside
    md.append("## 7. Upside spikes — 200dma distance\n")
    md.append("Episode = first close above trigger; ends on first close back below +5%.\n")
    md.append("| metal | trigger | episodes full | /yr full | episodes 2020+ | /yr 2020+ | most recent start | its peak (date, %) |")
    md.append("|---|---|---|---|---|---|---|---|")
    for t in STUDY:
        x = M[t]["d200"].dropna()
        yf_ = (x.index[-1] - x.index[0]).days / 365.25
        x20 = x[x.index >= "2020-01-01"]
        y20 = (x20.index[-1] - x20.index[0]).days / 365.25
        for th in [20, 30, 40]:
            eps = episodes(x, th, 5, "up")
            n20 = sum(1 for e in eps if e[0] >= pd.Timestamp("2020-01-01"))
            rates[(t, f"+{th}")] = (len(eps) / yf_, n20 / y20)
            last = eps[-1] if eps else None
            md.append(f"| {t} | > +{th}% | {len(eps)} | {len(eps) / yf_:.2f} | {n20} | {n20 / y20:.2f} | "
                      + (f"{last[0].date()} | {last[1].date()} {last[2]:+.1f}{' (ONGOING)' if last[5] else ''} |" if last else "— | — |"))
    md.append("")
    md.append("Upside episode detail, > +30%:\n")
    for t in STUDY:
        blk, _, _ = ep_block(M, t, 30, 5, "up")
        md.append(blk)

    with open(os.path.join(OUT, "band_stats_body.md"), "w") as f:
        f.write("\n".join(md))
    # machine-readable rates for the summary section
    pd.DataFrame([(k[0], k[1], v[0], v[1]) for k, v in rates.items()],
                 columns=["ticker", "trigger", "per_yr_full", "per_yr_2020"]).to_csv(os.path.join(OUT, "rates.csv"), index=False)
    print("ok", [(t, M[t].index[-1].date()) for t in TICKERS])


if __name__ == "__main__":
    sys.exit(main())
