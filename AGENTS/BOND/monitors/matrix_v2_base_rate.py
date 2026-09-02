#!/usr/bin/env python3
"""MATRIX_V2 per-tenor base-rating of the `I'` composition-failure test.

Owed 2026-09-04 (Will-ruled 2026-08-20 / 2026-08-27, `PROME/proposals/2026-08-27_matrix-v2-kill-scope-RULED.md`).
Built 2026-09-02 by BOND.

WHAT IT REPORTS, PER TENOR, NEVER POOLED (KB-BND-174: one rule, three effective strictnesses):

  A. FROZEN BAR for the next print — trailing-12 SAME-TENOR SAME-TIPS auctions strictly prior
     to --asof, indirect as % of COMPETITIVE ACCEPTED, 15th percentile by LINEAR interpolation
     (numpy default; the 8/27 7Y = 57.24 reproduces under this method). Also printed: the
     %-of-OFFERING figure (MATRIX_V2 §3d's own convention), the trailing-12 MIN (the OLD bar),
     the median, and bar − min. For tenors where the tool's term key POOLS reopenings with
     new issues (10Y/20Y/30Y — `grade_auction.bench` keys on originalSecurityTerm), the
     REOPENING-ONLY trailing-12 bar is printed beside it as a disclosed alternative.

  B. HISTORICAL BASE RATE (rolling, strictly out-of-sample): for every nominal coupon auction
     in the held history with >=12 same-tenor priors, the bar is recomputed from ITS OWN
     trailing-12 and `I'` fires iff indirect% < bar. Reported: realized fire rate (the
     in-construction expectation is ~15%, but a trailing window on an autocorrelated series
     does not have to deliver it), OLD conjunctive-test fire count (ind < min AND dlr > max)
     and OLD min-only fire count, so the difficulty shift Will ruled on is measured, not
     asserted.

  C. OUTCOME SEPARATION (the MATRIX_V2 draft's own yardstick): TLT close-to-close return over
     the 5 sessions AFTER the auction date (auction 1PM ET, so the auction-day close already
     carries the print). hit = TLT down (yields up). Reported for fires vs non-fires vs all,
     with N — a hit rate off N<6 is printed but flagged THIN.

Reads: data/auction_history_v2_prome-spawned.csv via grade_auction.load() (TA_WS overlay for
prints newer than the corpus), TLT via yfinance (run under .venv). No fitted parameters.
rc 0 = table printed · rc 2 = a required input failed (NOT a pass).
"""
from __future__ import annotations

import argparse
import datetime as dt
import statistics as st
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import grade_auction as ga  # noqa: E402

TENORS = ["2-Year", "3-Year", "5-Year", "7-Year", "10-Year", "20-Year", "30-Year"]
SHORT = {t: t.replace("-Year", "Y") for t in TENORS}
N_WIN = 12
PCT = 15
THIN = 6


def p15(vals):
    return float(np.percentile(vals, PCT))  # linear interpolation (numpy default)


def frozen_bar(recs, term, asof, reopen_only=None):
    h = [x for x in recs if x["term"] == term and not x["tips"] and x["date"] < asof]
    if reopen_only is not None:
        h = [x for x in h if x["reopening"] == reopen_only]
    h = h[-N_WIN:]
    if len(h) < THIN:
        return None
    ind = [x["ind"] for x in h]
    # of-offering: indirect accepted / offering. ind% of comp * comp / offering
    off = [x["ind"] * x["comp"] / x["offering"] for x in h if x["offering"]]
    return {"n": len(h), "from": h[0]["date"], "to": h[-1]["date"],
            "bar": p15(ind), "bar_off": p15(off) if len(off) == len(h) else None,
            "min": min(ind), "med": st.median(ind), "max": max(ind),
            "dlr_max": max(x["dlr"] for x in h), "dlr_med": st.median(x["dlr"] for x in h),
            "within1pp": sum(1 for v in ind if abs(v - p15(ind)) <= 1.0)}


def tlt_history():
    import pandas as pd  # noqa
    import yfinance as yf
    df = yf.download("TLT", start="2022-12-01", progress=False, auto_adjust=False)
    if df is None or len(df) == 0:
        raise RuntimeError("yfinance returned no TLT rows")
    close = df["Close"]
    if hasattr(close, "columns"):
        close = close.iloc[:, 0]
    s = close.dropna()
    s.index = [d.strftime("%Y-%m-%d") for d in s.index]
    return s


def fwd5(tlt, date):
    """Close-to-close TLT return, auction-day close -> 5 sessions later. None if not resolvable."""
    idx = list(tlt.index)
    if date not in tlt.index:
        # auction on a day TLT did not trade? take the first session >= date
        later = [d for d in idx if d >= date]
        if not later:
            return None
        date = later[0]
    i = idx.index(date)
    if i + 5 >= len(idx):
        return None
    return float(tlt.iloc[i + 5] / tlt.iloc[i] - 1.0)


def rolling(recs, term, tlt):
    h = [x for x in recs if x["term"] == term and not x["tips"]]
    rows = []
    for i in range(N_WIN, len(h)):
        w = h[i - N_WIN:i]
        x = h[i]
        ind = [y["ind"] for y in w]
        bar = p15(ind)
        mn, dmax = min(ind), max(y["dlr"] for y in w)
        r = fwd5(tlt, x["date"])
        rows.append({"date": x["date"], "cusip": x["cusip"], "reopen": x["reopening"],
                     "ind": x["ind"], "dlr": x["dlr"], "bar": bar, "margin": x["ind"] - bar,
                     "fire": x["ind"] < bar, "old_min": x["ind"] < mn,
                     "old_conj": x["ind"] < mn and x["dlr"] > dmax, "ret5": r})
    return rows


def stats(rows):
    rs = [r["ret5"] for r in rows if r["ret5"] is not None]
    if not rs:
        return {"n": 0, "hit": None, "med": None}
    return {"n": len(rs), "hit": sum(1 for v in rs if v < 0) / len(rs), "med": st.median(rs)}


def fmt_pct(v):
    return "—" if v is None else f"{100*v:.1f}%"


def fmt_ret(v):
    return "—" if v is None else f"{100*v:+.2f}%"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--asof", default=dt.date.today().isoformat(),
                    help="bars frozen from auctions STRICTLY BEFORE this date")
    ap.add_argument("--no-tlt", action="store_true", help="skip the outcome leg (offline)")
    a = ap.parse_args()

    try:
        recs = ga.load()
    except Exception as e:  # noqa: BLE001
        print(f"[base_rate] 🔴 auction history failed: {e}", file=sys.stderr)
        return 2
    recs = [x for x in recs if not x["tips"] and x["term"] in TENORS]
    newest = max(x["date"] for x in recs)
    print(f"[base_rate] run {dt.datetime.now():%Y-%m-%d %H:%M} local · asof {a.asof} · "
          f"nominal coupon records {len(recs)} · newest {newest} · window trailing-{N_WIN} · "
          f"P{PCT} linear interpolation · % of COMPETITIVE ACCEPTED unless labelled")

    tlt = None
    if not a.no_tlt:
        try:
            tlt = tlt_history()
            print(f"[base_rate] TLT closes {tlt.index[0]} -> {tlt.index[-1]} n={len(tlt)} (yfinance, unadjusted close)")
        except Exception as e:  # noqa: BLE001
            print(f"[base_rate] 🔴 TLT history failed: {e} — outcome leg NOT run (rc=2, not a pass)", file=sys.stderr)
            return 2

    # ---- A. frozen bars --------------------------------------------------------------
    print(f"\n== A · FROZEN `I'` BARS — trailing-{N_WIN} same-tenor same-TIPS, strictly prior to {a.asof} ==")
    print(f"{'tenor':<6}{'n':>3}  {'window':<25}{'I bar P15':>10}{'of-offer':>10}{'OLD min':>9}{'median':>8}{'bar-min':>9}{'≤1pp of bar':>12}{'dlr max':>9}")
    frozen = {}
    for t in TENORS:
        b = frozen_bar(recs, t, a.asof)
        frozen[t] = b
        if not b:
            print(f"{SHORT[t]:<6}  THIN — no bar")
            continue
        print(f"{SHORT[t]:<6}{b['n']:>3}  {b['from']}→{b['to']}  {b['bar']:>9.2f}{(b['bar_off'] or float('nan')):>10.2f}"
              f"{b['min']:>9.2f}{b['med']:>8.2f}{b['bar']-b['min']:>+9.2f}{b['within1pp']:>12d}{b['dlr_max']:>9.2f}")
    print("\n   reopening-only alternative (the tool's term key POOLS reopenings with new issues; the 9/9 10Y-R and 9/10 30Y-R are reopenings):")
    for t in ("10-Year", "20-Year", "30-Year"):
        b = frozen_bar(recs, t, a.asof, reopen_only=True)
        if b:
            print(f"   {SHORT[t]:<6} reopen-only n={b['n']:>2} {b['from']}→{b['to']}  bar {b['bar']:.2f} | min {b['min']:.2f} | median {b['med']:.2f}"
                  f"   vs pooled bar {frozen[t]['bar']:.2f}  (Δ {b['bar']-frozen[t]['bar']:+.2f}pp)")
        else:
            print(f"   {SHORT[t]:<6} reopen-only THIN")

    # ---- B/C. rolling out-of-sample fire rate + outcome -------------------------------
    print(f"\n== B/C · ROLLING OUT-OF-SAMPLE BASE RATE — bar recomputed from each auction's OWN trailing-{N_WIN}; outcome = TLT close(t)→close(t+5) ==")
    hdr = (f"{'tenor':<6}{'N':>4}{'I fires':>8}{'rate':>7}{'OLDmin':>7}{'OLDconj':>8} | "
           f"{'hit|fire':>9}{'med5|fire':>10}{'n':>3} | {'hit|nofire':>11}{'med5|nofire':>12} | {'hit|all':>8}{'med5|all':>9}")
    print(hdr)
    allrows = []
    per = {}
    for t in TENORS:
        rows = rolling(recs, t, tlt if tlt is not None else None) if tlt is not None else rolling(recs, t, _NoTLT())
        per[t] = rows
        allrows += rows
        if not rows:
            print(f"{SHORT[t]:<6}   —")
            continue
        f = [r for r in rows if r["fire"]]
        nf = [r for r in rows if not r["fire"]]
        sf, snf, sa = stats(f), stats(nf), stats(rows)
        thin = " THIN" if sf["n"] < THIN else ""
        print(f"{SHORT[t]:<6}{len(rows):>4}{len(f):>8}{fmt_pct(len(f)/len(rows)):>7}{sum(r['old_min'] for r in rows):>7}{sum(r['old_conj'] for r in rows):>8} | "
              f"{fmt_pct(sf['hit']):>9}{fmt_ret(sf['med']):>10}{sf['n']:>3} | {fmt_pct(snf['hit']):>11}{fmt_ret(snf['med']):>12} | "
              f"{fmt_pct(sa['hit']):>8}{fmt_ret(sa['med']):>9}{thin}")
    f = [r for r in allrows if r["fire"]]
    nf = [r for r in allrows if not r["fire"]]
    sf, snf, sa = stats(f), stats(nf), stats(allrows)
    print(f"{'ALL':<6}{len(allrows):>4}{len(f):>8}{fmt_pct(len(f)/len(allrows)):>7}{sum(r['old_min'] for r in allrows):>7}{sum(r['old_conj'] for r in allrows):>8} | "
          f"{fmt_pct(sf['hit']):>9}{fmt_ret(sf['med']):>10}{sf['n']:>3} | {fmt_pct(snf['hit']):>11}{fmt_ret(snf['med']):>12} | "
          f"{fmt_pct(sa['hit']):>8}{fmt_ret(sa['med']):>9}   ⚠️ pooled row is CONTEXT ONLY — the ruling is per tenor")

    print("\n== fired windows (every out-of-sample `I'` fire in the held history) ==")
    for r in sorted(f, key=lambda r: r["date"]):
        print(f"   {r['date']}  {r['cusip']:<10} ind {r['ind']:6.2f} < bar {r['bar']:6.2f} (margin {r['margin']:+.2f}pp)  dlr {r['dlr']:5.2f}"
              f"  {'reopen' if r['reopen'] else 'new   '}  TLT5 {fmt_ret(r['ret5'])}  {'OLDconj' if r['old_conj'] else ('OLDmin' if r['old_min'] else '')}")
    print("\n== MARGIN TIERS among fires (a candidate CONFIRMATION leg, base-rated here so it is never proposed bare) ==")
    print(f"{'tier':<16}{'N':>4}{'share of all':>13}{'hit':>7}{'med TLT5':>10}")
    for lab, lo in (("margin < 0 (all)", 0.0), ("margin ≤ −1pp", -1.0), ("margin ≤ −2pp", -2.0), ("margin ≤ −3pp", -3.0), ("margin ≤ −5pp", -5.0)):
        sub = [r for r in f if r["margin"] <= lo] if lo < 0 else f
        ss = stats(sub)
        print(f"{lab:<16}{len(sub):>4}{fmt_pct(len(sub)/len(allrows)):>13}{fmt_pct(ss['hit']):>7}{fmt_ret(ss['med']):>10}{'  THIN' if ss['n'] < THIN else ''}")
    oc = [r for r in allrows if r["old_conj"]]
    om = [r for r in allrows if r["old_min"]]
    print(f"{'OLD min-only':<16}{len(om):>4}{fmt_pct(len(om)/len(allrows)):>13}{fmt_pct(stats(om)['hit']):>7}{fmt_ret(stats(om)['med']):>10}")
    print(f"{'OLD conjunctive':<16}{len(oc):>4}{fmt_pct(len(oc)/len(allrows)):>13}{fmt_pct(stats(oc)['hit']):>7}{fmt_ret(stats(oc)['med']):>10}{'  THIN' if stats(oc)['n'] < THIN else ''}")
    rates = {t: (sum(1 for r in per[t] if r['fire']) / len(per[t])) if per[t] else None for t in TENORS}
    r3, r10, r30 = rates["3-Year"], rates["10-Year"], rates["30-Year"]
    if None not in (r3, r10, r30):
        print(f"\n   P(≥1 `I'` fire across the 9/8 3Y · 9/9 10Y-R · 9/10 30Y-R) at the per-tenor rolling rates, independence assumed: "
              f"{100*(1-(1-r3)*(1-r10)*(1-r30)):.0f}%  (3Y {100*r3:.1f}% · 10Y {100*r10:.1f}% · 30Y {100*r30:.1f}%)")
    print("\n== margin distribution of NON-fires (how close the tenor runs to its bar) ==")
    for t in TENORS:
        m = [r["margin"] for r in per[t] if not r["fire"]]
        if m:
            print(f"   {SHORT[t]:<4} n={len(m):>3}  margin min {min(m):+.2f}  P25 {np.percentile(m,25):+.2f}  median {st.median(m):+.2f}pp")
    print("\n⚠️ A hit rate is a SAMPLE statistic over TLT, not a truth about auctions; N<6 rows are printed and labelled THIN.")
    print("⚠️ The rolling bar is OUT-OF-SAMPLE by construction (each auction graded on priors only); the frozen bars in A are what the 9/8–9/10 prints grade on.")
    return 0


class _NoTLT:
    index = []
    def __contains__(self, x):
        return False


if __name__ == "__main__":
    sys.exit(main())
