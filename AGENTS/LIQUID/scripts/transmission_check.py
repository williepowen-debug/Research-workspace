#!/usr/bin/env python3
"""Credit-transmission persistence check + funding pairing + quarter-end base rate.

Built 2026-09-25 for PROME's Will-directed item 3 ("does credit transmission persist?").
Re-run after each FRED ICE BofA publication (~16:15 ET, T+1) to grade the next obs.

  Ladder  : FRED ICE BofA OAS (latest-revised basis) IG/BBB/BB/B/CCC/HY. d/d and 15-session
            changes, each percentile-ranked against its OWN history since 2023-10 (KB-LIQ-128
            method: rank the CHANGE, never the level).
  Funding : FRED SOFR/SOFR75/SOFR99/TGCR vs IORB, date-matched (KB-LIQ-126: no cross-date
            pairs); RRPONTSYD; RPONTTLD (SRF take-up, all collateral legs); WRESBAL/WTREGEN by as-of Wednesday.
  Q-end   : every quarter-end since 2024-Q1. Baseline = median of the 10 business days ending
            5 business days before the Q-end date; excess = print - baseline.
Usage: transmission_check.py [--asof YYYY-MM-DD]
"""
import sys, statistics, pathlib
from datetime import date
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "FORGE" / "tools" / "market-data"))
from fetch import fred_fetch

LADDER = [("IG", "BAMLC0A0CM"), ("BBB", "BAMLC0A4CBBB"), ("BB", "BAMLH0A1HYBB"),
          ("B", "BAMLH0A2HYB"), ("CCC", "BAMLH0A3HYC"), ("HY", "BAMLH0A0HYM2")]
START = "2023-10-01"

def series(sid, limit=2000):
    rows = fred_fetch(sid, limit=limit)
    if rows and "error" in rows[0]:
        raise SystemExit(f"FRED error {sid}: {rows[0]['error']}")
    return {r["date"]: float(r["value"]) for r in rows}

def pct_rank(x, hist):
    return 100.0 * sum(1 for h in hist if h <= x) / len(hist), sum(1 for h in hist if h >= x)

def ladder(asof):
    data = {k: series(s) for k, s in LADDER}
    dates = sorted(set.intersection(*(set(v) for v in data.values())))
    dates = [d for d in dates if d >= START and (asof is None or d <= asof)]
    i = len(dates) - 1
    print(f"== LADDER (bp, FRED latest-revised) latest obs {dates[i]} | prior {dates[i-1]} | 15-sess base {dates[i-15]} | history {dates[0]}..{dates[i]}")
    print(f"{'tier':5}{'level':>7}{'d/d':>6}{'d/d pct':>9}{'>=':>6}{'15s':>6}{'15s pct':>9}{'>=':>6}  n_dd/n_15")
    out = {}
    def row(name, v):
        dd = [v[j] - v[j-1] for j in range(1, len(v))]
        f15 = [v[j] - v[j-15] for j in range(15, len(v))]
        x1, x15 = dd[-1], f15[-1]
        p1, c1 = pct_rank(x1, dd); p15, c15 = pct_rank(x15, f15)
        print(f"{name:5}{v[-1]:7.0f}{x1:+6.0f}{p1:8.1f}%{c1:6d}{x15:+6.0f}{p15:8.1f}%{c15:6d}  {len(dd)}/{len(f15)}")
        out[name] = dict(level=v[-1], dd=x1, p1=p1, f15=x15, p15=p15)
    for k, _ in LADDER:
        row(k, [data[k][d] * 100 for d in dates[:i+1]])
    row("CCC-B", [(data["CCC"][d] - data["B"][d]) * 100 for d in dates[:i+1]])
    row("B-BB", [(data["B"][d] - data["BB"][d]) * 100 for d in dates[:i+1]])
    print("last 6 obs:", ", ".join(f"{d}: " + "/".join(f"{data[k][d]*100:.0f}" for k, _ in LADDER) for d in dates[i-5:i+1]), "(IG/BBB/BB/B/CCC/HY)")
    return out

def funding():
    s = {k: series(k, 1500) for k in ("SOFR", "SOFR75", "SOFR99", "TGCRRATE", "IORB", "RRPONTSYD", "RPONTTLD")}
    print("\n== FUNDING (date-matched to IORB of the same date; bp)")
    ds = sorted(d for d in s["SOFR"] if d in s["IORB"])[-8:]
    for d in ds:
        ib = s["IORB"][d]
        f = lambda k: f"{(s[k][d]-ib)*100:+4.0f}" if d in s[k] else "  na"
        print(f"{d} SOFR {s['SOFR'][d]:.2f} IORB {ib:.2f} | SOFR-IORB {f('SOFR')} SOFR75-IORB {f('SOFR75')} SOFR99-IORB {f('SOFR99')} TGCR-IORB {f("TGCRRATE")}"
              f" | RRP ${s['RRPONTSYD'].get(d, float('nan')):.2f}B SRF ${s["RPONTTLD"].get(d, float('nan')):.3f}B")
    for k in ("WRESBAL", "WTREGEN"):
        w = series(k, 6); print(k, " ".join(f"{d}:{w[d]:,.1f}" for d in sorted(w)))
    return s

def qend(s):
    import calendar
    print("\n== QUARTER-END TURNS (excess over pre-window baseline, bp; SRF $B on Q-end date)")
    days = sorted(d for d in s["SOFR"] if d in s["IORB"] and d in s["SOFR99"])
    sp = {d: round((s["SOFR"][d] - s["IORB"][d]) * 100) for d in days}   # whole bp: DAEDALUS #5 rounding order
    s99 = {d: round((s["SOFR99"][d] - s["IORB"][d]) * 100) for d in days}
    print(f"{'Q-end':11}{'base':>6}{'QE-1':>6}{'QE':>6}{'QE+1':>6}{'QE+2':>6}{'QE+3':>6}{'QE+5':>6} | {'99base':>7}{'99QE':>6}{'99+1':>6}{'99+2':>6} | days>+2 after | SRF QE")
    for y in (2024, 2025, 2026):
        for m in (3, 6, 9, 12):
            qe = date(y, m, calendar.monthrange(y, m)[1]).isoformat()
            prior = [d for d in days if d <= qe]
            if not prior or prior[-1] < qe[:8] + "25": continue
            qd = prior[-1]; k = days.index(qd)
            if k + 5 >= len(days): continue
            base = statistics.median(sp[d] for d in days[k-15:k-5])
            b99 = statistics.median(s99[d] for d in days[k-15:k-5])
            ex = lambda j: sp[days[k+j]] - base
            ex99 = lambda j: s99[days[k+j]] - b99
            n_after = 0
            for j in range(1, 11):
                if ex(j) > 2: n_after += 1
                else: break
            print(f"{qd:11}{base:+6.0f}{ex(-1):+6.0f}{ex(0):+6.0f}{ex(1):+6.0f}{ex(2):+6.0f}{ex(3):+6.0f}{ex(5):+6.0f} | {b99:+7.0f}{ex99(0):+6.0f}{ex99(1):+6.0f}{ex99(2):+6.0f} | {n_after:3d}           | {s["RPONTTLD"].get(qd, 0):.2f}")

if __name__ == "__main__":
    asof = sys.argv[sys.argv.index("--asof") + 1] if "--asof" in sys.argv else None
    ladder(asof); qend(funding())
