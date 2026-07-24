#!/usr/bin/env python3
"""
GATE-LIQ-079 false-positive backtest (KB-LIQ-079 R4 / Rank-3, deferred 2026-07-18).

Purpose: replace "thresholds illustrative" with an independently-derived FP rate for the
acute arm leg -- SOFR99 - IORB >= +30bps AND non-calendar -- and answer the R4 regime
question: is the current RRP-drained regime actually unprecedented in-sample?

Basis discipline:
  - SOFR99 = FRED SOFR99 (99th pctile of SOFR distribution). SOFR starts 2018-04-03.
  - Ceiling = IORB spliced to IOER at the 2021-07-28/29 seam (per spec section 5).
  - All dates are FRED observation dates (the rate's effective date), not publication dates.
Run: .venv/bin/python3 AGENTS/LIQUID/scripts/fp_backtest_079.py
"""
import json, os, sys, urllib.request, urllib.parse
import datetime as dt

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

def fred_key():
    for p in [os.path.join(ROOT, "FORGE/tools/market-data/.env"), os.path.join(ROOT, ".env")]:
        if os.path.exists(p):
            for line in open(p).read().splitlines():
                if line.strip().startswith("FRED") and "=" in line:
                    return line.split("=", 1)[1].strip().strip('"').strip("'")
    return os.environ.get("FRED_API_KEY")

KEY = fred_key()

def fred(series, start="2018-01-01"):
    u = "https://api.stlouisfed.org/fred/series/observations?" + urllib.parse.urlencode(
        {"series_id": series, "api_key": KEY, "file_type": "json",
         "observation_start": start})
    d = json.load(urllib.request.urlopen(u, timeout=60))
    out = {}
    for o in d["observations"]:
        if o["value"] not in (".", ""):
            out[o["date"]] = float(o["value"])
    return out

# ---------- calendar filter ----------
def is_business_day(d):
    return d.weekday() < 5

def bd_offset(d, n):
    """move n business days from d (n may be negative)"""
    step = 1 if n > 0 else -1
    left = abs(n)
    cur = d
    while left:
        cur += dt.timedelta(days=step)
        if is_business_day(cur):
            left -= 1
    return cur

def calendar_dates(years):
    """Set of dates within +/-2 business days of month-end, quarter-end, or Apr-15."""
    flagged = set()
    anchors = []
    for y in years:
        for m in range(1, 13):
            # last calendar day of month -> roll back to last business day
            if m == 12:
                last = dt.date(y, 12, 31)
            else:
                last = dt.date(y, m + 1, 1) - dt.timedelta(days=1)
            while not is_business_day(last):
                last -= dt.timedelta(days=1)
            anchors.append(last)
        # Apr-15 tax date
        a = dt.date(y, 4, 15)
        while not is_business_day(a):
            a += dt.timedelta(days=1)
        anchors.append(a)
    for a in anchors:
        for k in range(-2, 3):
            flagged.add(bd_offset(a, k) if k else a)
    return flagged

def main():
    print("=" * 78)
    print("GATE-LIQ-079 FP BACKTEST — acute leg SOFR99 - ceiling")
    print("=" * 78)
    if not KEY:
        print("NO FRED KEY — abort"); sys.exit(1)

    sofr99 = fred("SOFR99")
    sofr   = fred("SOFR")
    iorb   = fred("IORB")
    ioer   = fred("IOER")
    rrp    = fred("RRPONTSYD")
    effr   = fred("EFFR")

    print(f"pulled: SOFR99 {len(sofr99)}  SOFR {len(sofr)}  IORB {len(iorb)}  "
          f"IOER {len(ioer)}  RRP {len(rrp)}  EFFR {len(effr)}")
    if sofr99:
        ks = sorted(sofr99)
        print(f"SOFR99 span: {ks[0]} -> {ks[-1]}")

    # spliced ceiling
    ceiling = {}
    for d, v in ioer.items():
        if d < "2021-07-29":
            ceiling[d] = v
    for d, v in iorb.items():
        ceiling[d] = v
    print(f"spliced ceiling: {len(ceiling)} obs "
          f"(IOER<2021-07-29 -> IORB); seam check "
          f"IOER 2021-07-28={ioer.get('2021-07-28')} IORB 2021-07-29={iorb.get('2021-07-29')}")

    # spread series
    rows = []
    for d in sorted(sofr99):
        if d in ceiling:
            rows.append((d, round((sofr99[d] - ceiling[d]) * 100, 1)))
    print(f"spread obs: {len(rows)}  ({rows[0][0]} -> {rows[-1][0]})")

    years = sorted({int(d[:4]) for d, _ in rows})
    cal = calendar_dates(years)

    # ---------- threshold census ----------
    print("\n" + "-" * 78)
    print("THRESHOLD CENSUS (raw fire-days vs calendar-filtered)")
    print("-" * 78)
    print(f"{'thresh':>7} {'fire-days':>10} {'non-cal':>9} {'cal-artifact':>13} {'episodes(raw)':>14} {'episodes(non-cal)':>18}")

    def episodes(dates, gap=5):
        """cluster fire dates into episodes; new episode if >gap calendar days apart"""
        if not dates: return []
        eps, cur = [], [dates[0]]
        for d in dates[1:]:
            prev = dt.date.fromisoformat(cur[-1])
            now = dt.date.fromisoformat(d)
            if (now - prev).days > gap:
                eps.append(cur); cur = [d]
            else:
                cur.append(d)
        eps.append(cur)
        return eps

    census = {}
    for th in (10, 20, 30, 40, 50):
        fires = [d for d, s in rows if s >= th]
        noncal = [d for d in fires if dt.date.fromisoformat(d) not in cal]
        er, en = episodes(fires), episodes(noncal)
        census[th] = (fires, noncal, er, en)
        print(f"{th:>6}b {len(fires):>10} {len(noncal):>9} {len(fires)-len(noncal):>13} "
              f"{len(er):>14} {len(en):>18}")

    # ---------- +30 detail ----------
    print("\n" + "-" * 78)
    print("+30bps NON-CALENDAR EPISODES (the registered arm line) — detail")
    print("-" * 78)
    fires30, noncal30, eps30_raw, eps30 = census[30]
    if not eps30 or not noncal30:
        print("  NONE.")
    for e in eps30:
        peak = max(s for d, s in rows if d in e)
        rrp_at = None
        for d in e:
            if d in rrp: rrp_at = rrp[d]; break
        print(f"  {e[0]} -> {e[-1]}  days={len(e):<3} peak={peak:>6.1f}bp  "
              f"RRP@start={('%.1fB' % rrp_at) if rrp_at is not None else 'n/a':>9}")

    print("\n  RAW (unfiltered) +30 episodes, for the calendar-artifact check:")
    for e in eps30_raw:
        peak = max(s for d, s in rows if d in e)
        n_cal = sum(1 for d in e if dt.date.fromisoformat(d) in cal)
        tag = "ALL-CALENDAR" if n_cal == len(e) else f"{n_cal}/{len(e)} cal-days"
        print(f"  {e[0]} -> {e[-1]}  days={len(e):<3} peak={peak:>6.1f}bp  {tag}")

    # ---------- R4: regime split ----------
    print("\n" + "=" * 78)
    print("R4 REGIME QUESTION — is the RRP-drained regime unprecedented IN-SAMPLE?")
    print("=" * 78)
    # RRP regime: drained if RRP < $50B
    DRAIN = 50.0
    drained_days = [d for d in sorted(rrp) if rrp[d] < DRAIN]
    buffered_days = [d for d in sorted(rrp) if rrp[d] >= DRAIN]
    print(f"RRP < ${DRAIN:.0f}B ('drained'):  {len(drained_days)} obs")
    print(f"RRP >= ${DRAIN:.0f}B ('buffered'): {len(buffered_days)} obs")
    if drained_days:
        # contiguous drained spans
        spans, cur = [], [drained_days[0]]
        for d in drained_days[1:]:
            if (dt.date.fromisoformat(d) - dt.date.fromisoformat(cur[-1])).days > 7:
                spans.append(cur); cur = [d]
            else: cur.append(d)
        spans.append(cur)
        print("\n  Contiguous DRAINED spans (>30 obs shown):")
        for s in spans:
            if len(s) > 30:
                print(f"    {s[0]} -> {s[-1]}   ({len(s)} obs)")

    # spread behaviour by regime
    def stats(dates):
        vals = [s for d, s in rows if d in dates]
        if not vals: return None
        vals_sorted = sorted(vals)
        n = len(vals)
        return (n, sum(vals)/n, vals_sorted[int(n*0.95)] if n > 20 else max(vals), max(vals),
                sum(1 for v in vals if v >= 30))
    dset, bset = set(drained_days), set(buffered_days)
    print("\n  Acute-leg (SOFR99-ceiling) behaviour BY REGIME:")
    print(f"  {'regime':<12} {'n':>6} {'mean':>8} {'p95':>8} {'max':>8} {'days>=30':>9}")
    for nm, ds in (("DRAINED", dset), ("BUFFERED", bset)):
        st = stats(ds)
        if st:
            print(f"  {nm:<12} {st[0]:>6} {st[1]:>8.1f} {st[2]:>8.1f} {st[3]:>8.1f} {st[4]:>9}")

    # where do the +30 non-cal fires sit by regime?
    print("\n  +30 NON-CALENDAR fire-days by regime:")
    for nm, ds in (("DRAINED", dset), ("BUFFERED", bset)):
        k = [d for d in noncal30 if d in ds]
        print(f"    {nm:<10} {len(k):>4} fire-days" + (f"   e.g. {k[0]} .. {k[-1]}" if k else ""))
    unknown = [d for d in noncal30 if d not in dset and d not in bset]
    if unknown:
        print(f"    (no RRP obs for {len(unknown)} fire-days: {unknown[:5]})")

    # current state
    last = rows[-1]
    ld = sorted(rrp)[-1]
    print("\n" + "-" * 78)
    print(f"CURRENT: SOFR99-ceiling {last[1]:+.1f}bp [{last[0]}]  |  arm line +30  |  "
          f"gap {30-last[1]:.1f}bp")
    print(f"         RRP ${rrp[ld]:.3f}B [{ld}]  -> regime = "
          f"{'DRAINED' if rrp[ld] < DRAIN else 'BUFFERED'}")
    print("-" * 78)

if __name__ == "__main__":
    main()
