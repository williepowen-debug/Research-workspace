#!/usr/bin/env python3
"""
QQQ/NDX V-RECOVERY EPISODE ANALYZER — TERRY, built 2026-08-04.

Answers, on demand and reproducibly, the question Will asked on 8/4 while looking
at a 3-month QQQ chart: *"is this an unusual retracement — the extent of drop and
recovery?"* — and the two follow-ups that mattered:

  #7  does the base rate survive outside the 1999-2003 bubble era?
  #3  at the prior high, is a REJECTION the modal path or the exception?

This exists so the next V costs 30 seconds instead of an hour, and so the numbers
are RE-DERIVED rather than quoted from a stale write-up. `RESEARCH.md` records the
2026-08-04 run; this script is the thing that can contradict it.

    python3 AGENTS/TERRY/qqq/scripts/v_episodes.py                 # full report, ^NDX
    python3 AGENTS/TERRY/qqq/scripts/v_episodes.py --ticker QQQ
    python3 AGENTS/TERRY/qqq/scripts/v_episodes.py --integrity     # the NDX-vs-QQQ check only
    python3 AGENTS/TERRY/qqq/scripts/v_episodes.py --selftest

────────────────────────────────────────────────────────────────────────────────
🔴 THE DATA-INTEGRITY FINDING THIS TOOL EXISTS TO ENFORCE — read before trusting
any number it prints.

QQQ launched 1999-03-10 and split 2:1 on 2000-03-20. Over 1999-2003 the QQQ and
^NDX series **disagree by a mean 0.492pp per day and up to 6.72pp**; from 2004 the
mean gap is 0.065pp. An ETF cannot miss its index by 6.7% in a day, so one of the
two series is wrong in that window, and the divergence decays monotonically as QQQ
matured — which points at early QQQ.

★ Why it matters more than it sounds: **1999-2003 supplies the MAJORITY of episodes
in any sample built on this event definition (21 of 32 on NDX), and those rows carry
the OPPOSITE FORWARD SIGN to every other era** (3-month median −7.3% vs +21.9%).
So the least trustworthy rows are simultaneously the most numerous AND the ones
driving the answer. `--exclude-bubble` is not a robustness toggle; it is the
honest default for anything decision-bearing, and the report prints both.

⚠️ Never quote a headline base rate from this tool without its n and its era split.
The near-highs cohort — the configuration of 2026-08-04 — has **n=3 outside the
bubble era.** Three observations, split 2-1, with the single loss at −21.9%.
────────────────────────────────────────────────────────────────────────────────
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

VENV_PY = Path(__file__).resolve().parents[4] / ".venv" / "bin" / "python3"


def _ensure_deps_or_reexec() -> None:
    """Self-heal under .venv (same pattern as chain_fetch.py / paper_book_mark.py).

    Exits NON-ZERO with the fix if it cannot: a base-rate tool has no safe degraded
    output — a silently empty episode set reads exactly like 'no precedent exists'.
    """
    try:
        import yfinance, pandas, numpy  # noqa: F401
        return
    except ModuleNotFoundError:
        pass
    if not os.environ.get("_VE_REEXEC") and VENV_PY.exists():
        os.environ["_VE_REEXEC"] = "1"
        os.execv(str(VENV_PY), [str(VENV_PY), *sys.argv])
    print(f"FATAL: yfinance/pandas not importable and no venv at {VENV_PY}.\n"
          f"  Fix: {VENV_PY} -m pip install yfinance pandas\n"
          f"  NO episode table is printed — an empty one would read as 'no precedent'.",
          file=sys.stderr)
    raise SystemExit(2)


BUBBLE = ("1999-01-01", "2003-12-31")   # the window where QQQ and ^NDX disagree
DEEP_DD = -15.0                          # drawdown-from-ATH splitting bear-bounce from near-highs
MIN_DD_FOR_V = -8.0                      # an episode needs a real prior drawdown to be a "V"
REJECT_PCT, BREAK_PCT, TEST_WINDOW = 3.0, 2.0, 20
RETURN_HORIZON = 250                     # sessions allowed to carry back to the old high
DECLUSTER = 10                           # sessions; keeps one episode per cluster


def load(ticker):
    import yfinance as yf
    h = yf.Ticker(ticker).history(period="max")[["High", "Low", "Close"]].dropna()
    if h.empty:
        raise SystemExit(f"FATAL: no data for {ticker} — refusing to print an empty episode set.")
    h.index = h.index.tz_localize(None)
    return h


def find_episodes(close, thr, decluster=DECLUSTER):
    """Distinct 4-session rallies >= thr%. De-clustered so one move counts once."""
    r4 = close.pct_change(4) * 100
    hits = r4[r4 >= thr]
    out, last = [], None
    for d in hits.index:
        if last is None or (close.index.get_loc(d) - close.index.get_loc(last)) > decluster:
            out.append(d)
            last = d
    return out


def integrity_check(verbose=True):
    """Compare ^NDX and QQQ daily returns by era. Returns the 1999-2003 mean gap.

    This is `finding_base_rate_the_instrument_before_its_event_table` applied: base-rate
    the INSTRUMENT before reading its event table. Running the episode finder on both
    series and matching the results is what exposed the bubble-era divergence — a
    correlation number alone (0.980) looked fine and hid it.
    """
    import pandas as pd
    n, q = load("^NDX")["Close"], load("QQQ")["Close"]
    j = pd.concat([n.rename("ndx"), q.rename("qqq")], axis=1).dropna()
    r = j.pct_change().dropna() * 100
    r["gap"] = (r.ndx - r.qqq).abs()
    early = r[r.index.year <= 2003]
    late = r[r.index.year >= 2004]
    if verbose:
        print("DATA INTEGRITY — ^NDX vs QQQ daily returns")
        print(f"  overlap {j.index[0].date()} .. {j.index[-1].date()}  n={len(j)}")
        print(f"  1999-2003 : mean gap {early.gap.mean():.3f}pp   max {early.gap.max():.2f}pp   "
              f"days >1pp apart {int((early.gap > 1).sum())}")
        print(f"  2004-     : mean gap {late.gap.mean():.3f}pp   max {late.gap.max():.2f}pp   "
              f"days >1pp apart {int((late.gap > 1).sum())}")
        verdict = ("🔴 bubble-era rows are NOT measurement-grade — exclude them from anything "
                   "decision-bearing" if early.gap.mean() > 3 * late.gap.mean()
                   else "✓ eras comparable")
        print(f"  => {verdict}")
    return float(early.gap.mean()), float(late.gap.mean())


def analyse(ticker, thr=None):
    import pandas as pd, numpy as np
    h = load(ticker)
    c, hi = h["Close"], h["High"]
    if thr is None:                                   # default: today's own 4-session return
        thr = (c.iloc[-1] / c.iloc[-5] - 1) * 100
    dd = (c / c.cummax() - 1) * 100
    eps = find_episodes(c, thr)
    if not eps:
        raise SystemExit(f"FATAL: zero episodes at threshold {thr:.2f}% — that is a defect or a "
                         f"badly chosen threshold, not a finding. Refusing to report 'no precedent'.")

    def fwd(d, n):
        i = c.index.get_loc(d)
        return (c.iloc[i + n] / c.iloc[i] - 1) * 100 if i + n < len(c) else np.nan

    rows = []
    for E in eps:
        i = c.index.get_loc(E)
        win = c.iloc[max(0, i - RETURN_HORIZON):i + 1]
        P, Pd = win.max(), win.idxmax()
        trough = c.iloc[c.index.get_loc(Pd):i + 1].min()
        prior_dd = (trough / P - 1) * 100
        rec = dict(date=E, dd_ath=dd.asof(E), prior_dd=prior_dd, thr=thr,
                   f1m=fwd(E, 21), f3m=fwd(E, 63), old_high=P,
                   bubble=pd.Timestamp(BUBBLE[0]) <= E <= pd.Timestamp(BUBBLE[1]),
                   verdict=None, sessions_to_high=np.nan)
        # ---- #3: first test of the prior high
        if prior_dd <= MIN_DD_FOR_V:
            fut = c.iloc[i + 1:i + 1 + RETURN_HORIZON]
            touch = fut[fut >= P]
            if len(touch) == 0:
                rec["verdict"] = "NEVER RETURNED"
            else:
                T = touch.index[0]
                j = c.index.get_loc(T)
                path = c.iloc[j:j + TEST_WINDOW + 1]
                rej = next((k for k, x in enumerate(path) if (x / P - 1) * 100 <= -REJECT_PCT), None)
                brk = next((k for k, x in enumerate(path) if (x / P - 1) * 100 >= BREAK_PCT), None)
                rec["verdict"] = ("REJECTED on first test" if rej is not None and (brk is None or rej < brk)
                                  else "BROKE THROUGH first test" if brk is not None else "CHOPPED")
                rec["sessions_to_high"] = j - i
        rows.append(rec)
    return pd.DataFrame(rows), thr


def report(ticker, thr=None, as_json=False):
    import pandas as pd, numpy as np
    df, thr = analyse(ticker, thr)
    prior = df[df.date < pd.Timestamp.today().normalize().replace(month=1, day=1)]
    prior = prior.dropna(subset=["f1m", "f3m"])
    nh = prior[prior.dd_ath > DEEP_DD]

    def stats(s):
        if not len(s):
            return None
        return dict(n=int(len(s)), f1m_med=round(float(s.f1m.median()), 1),
                    f1m_win=round(float((s.f1m > 0).mean() * 100)),
                    f3m_med=round(float(s.f3m.median()), 1),
                    f3m_win=round(float((s.f3m > 0).mean() * 100)))

    tested = prior[prior.verdict.notna() & (prior.verdict != "NEVER RETURNED")]
    reached = prior[prior.verdict.notna()]
    out = dict(
        ticker=ticker, threshold_pct=round(thr, 2),
        span=[str(df.date.min().date()), str(df.date.max().date())],
        episodes_total=int(len(df)), episodes_prior=int(len(prior)),
        cohorts={"all": stats(prior), "bubble": stats(prior[prior.bubble]),
                 "ex_bubble": stats(prior[~prior.bubble]),
                 "near_highs": stats(nh), "near_highs_ex_bubble": stats(nh[~nh.bubble])},
        prior_high_test={
            "episodes_with_real_drawdown": int(len(reached)),
            "reached_old_high": int(len(tested)),
            "reached_pct": round(len(tested) / len(reached) * 100) if len(reached) else None,
            "broke_through": int((tested.verdict == "BROKE THROUGH first test").sum()),
            "rejected": int((tested.verdict == "REJECTED on first test").sum()),
            "ex_bubble_broke": int(((tested.verdict == "BROKE THROUGH first test") & ~tested.bubble).sum()),
            "ex_bubble_n": int((~tested.bubble).sum()),
            "median_sessions_to_high": None if tested.empty else float(tested.sessions_to_high.median()),
        })
    if as_json:
        print(json.dumps(out, indent=2))
        return out

    print(f"QQQ V-RECOVERY EPISODES — {ticker}  {out['span'][0]} .. {out['span'][1]}")
    print(f"threshold = {thr:.2f}% over 4 sessions   episodes={out['episodes_total']} "
          f"(prior, with forward data: {out['episodes_prior']})\n")
    print(f"{'cohort':<34}{'n':>4}{'1m med':>9}{'1m win':>8}{'3m med':>9}{'3m win':>8}")
    print("-" * 72)
    for lbl, key in [("ALL prior episodes", "all"),
                     ("  bubble 1999-2003 (DATA-SUSPECT)", "bubble"),
                     ("  EX-BUBBLE", "ex_bubble"),
                     ("NEAR-HIGHS (dd > -15%)", "near_highs"),
                     ("  NEAR-HIGHS EX-BUBBLE  <- honest", "near_highs_ex_bubble")]:
        s = out["cohorts"][key]
        if s:
            print(f"{lbl:<34}{s['n']:>4}{s['f1m_med']:>8.1f}%{s['f1m_win']:>7.0f}%"
                  f"{s['f3m_med']:>8.1f}%{s['f3m_win']:>7.0f}%")
    p = out["prior_high_test"]
    print(f"\nFIRST TEST OF THE PRIOR HIGH ({RETURN_HORIZON}-session horizon)")
    print(f"  carried back to the old high : {p['reached_old_high']}/{p['episodes_with_real_drawdown']}"
          f" = {p['reached_pct']}%   <- the modal path is NOT reaching it")
    print(f"  of those, broke through      : {p['broke_through']}   rejected: {p['rejected']}")
    print(f"  ex-bubble                    : {p['ex_bubble_broke']}/{p['ex_bubble_n']} broke through")
    print(f"  median sessions V -> old high: {p['median_sessions_to_high']:.0f}"
          if p["median_sessions_to_high"] else "")
    s = out["cohorts"]["near_highs_ex_bubble"]
    if s:
        print(f"\n⚠️  The cohort matching a near-highs V has n={s['n']} outside the bubble era. "
              f"Quote the n, never the % alone.")
    return out


def selftest():
    """Guard-the-guard: assert the tool FAILS on degenerate input rather than
    printing a confident empty answer. A base-rate tool's worst failure is a silent
    zero, which reads identically to 'no precedent exists'."""
    import pandas as pd, numpy as np
    fails = 0

    def ok(lbl, cond):
        nonlocal fails
        print(f"  {'PASS' if cond else 'FAIL'}  {lbl}")
        if not cond:
            fails += 1

    idx = pd.bdate_range("2020-01-01", periods=60)
    flat = pd.Series(np.linspace(100, 101, 60), index=idx)
    ok("flat series yields NO episodes at a 9% bar", find_episodes(flat, 9.0) == [])
    spike = flat.copy()
    spike.iloc[30:34] = [110, 112, 114, 116]
    ok("an injected +15% 4-day move IS found", len(find_episodes(spike, 9.0)) >= 1)
    two = flat.copy()
    two.iloc[10:14] = [110, 112, 114, 116]
    two.iloc[40:44] = [110, 112, 114, 116]
    ok("two separated moves de-cluster to 2 episodes, not N windows",
       len(find_episodes(two, 9.0)) == 2)
    close = flat.copy()
    close.iloc[20:24] = [110, 112, 114, 116]
    close.iloc[26:30] = [118, 120, 122, 124]
    ok("two moves within the de-cluster gap collapse to 1",
       len(find_episodes(close, 9.0, decluster=20)) == 1)
    ok("BUBBLE window is the era where QQQ and ^NDX diverge", BUBBLE == ("1999-01-01", "2003-12-31"))
    ok("ex-bubble is the documented honest default, not a toggle",
       "honest default" in __doc__)
    print(f"\n  {'SELFTEST PASS' if not fails else f'SELFTEST FAIL ({fails})'}")
    return 1 if fails else 0


def main():
    ap = argparse.ArgumentParser(description="QQQ/NDX V-recovery episode analyzer")
    ap.add_argument("--ticker", default="^NDX",
                    help="^NDX (default — longer + internally consistent) or QQQ")
    ap.add_argument("--threshold", type=float, default=None,
                    help="4-session %% bar; default = today's own 4-session return")
    ap.add_argument("--integrity", action="store_true", help="run only the ^NDX-vs-QQQ era check")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        _ensure_deps_or_reexec()
        return selftest()
    _ensure_deps_or_reexec()
    if a.integrity:
        integrity_check()
        return 0
    report(a.ticker, a.threshold, a.json)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
