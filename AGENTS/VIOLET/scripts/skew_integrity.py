#!/usr/bin/env python3
"""`^SKEW` mirror integrity — run AT THE MOMENT OF USE, record the verdict WITH the claim.

WHY THIS EXISTS, AND WHY IT IS NOT A BOOT CHECK
-----------------------------------------------
Two findings, four days apart, and the second one killed the first one's remedy.

**KB-VIO-221 (2026-09-04) — the defect HEALS.** On 9/2 yfinance's `^SKEW` history
omitted the 2026-08-28 bar and a grade was computed across the hole. On 9/4 the
same query — `period='20d'`, the exact call the 9/2 pull used — returned the bar
at 149.77. Same query, different answer two days apart, no error either time.
⇒ **A self-healing defect passes every LATER audit.** A grade computed during one
is silently wrong *and unfalsifiable afterwards*, so verification-after-the-fact
is not a control for it. **A boot-time check run before the work is not a control
either** — the gap can open between boot and use. The check has to run at the
moment the value is consumed, and its result has to be recorded beside the claim.

**KB-VIO-236 (2026-09-04, RED) — and there are TWO modes, not one.** RED
base-rated the full trailing year (253 sessions) where I had looked at 10:

    omitted session       2026-08-28   CBOE 149.77   yfinance absent
    value disagreement    2025-12-24   CBOE 161.30   yfinance 160.53

**Instrument-defect rate 2/253 = 0.79% of sessions.**

🔑 **The completeness check I originally proposed — count bars against the trading
calendar — CATCHES THE OMISSION AND IS BLIND TO THE WRONG VALUE.** A gapped series
announces itself; a wrong one does not. So this tool compares **values**, cell by
cell, and treats a bar-count match as necessary but nowhere near sufficient.

WHAT IT IS AND IS NOT
---------------------
✅ It answers: *for the dates I am about to use, does the mirror agree with the
   publisher of record, to the cent?*
⛔ It is NOT a vintage archive check. Neither endpoint retains first-published
   values and CBOE rewrites its CSV daily carrying current values for all history,
   so **which 2025-12-24 value was first published is UNKNOWABLE from here** — RED
   marked that UNKNOWN rather than papering over it, and so does this.
⛔ It cannot bound a hole that has already healed. It bounds THIS read, at THIS
   instant, which is the only thing any instrument can honestly bound here.

Exit codes: 0 = clean over the window; 1 = defect found (omission or disagreement);
2 = could not reach an endpoint (fails CLOSED — an unreachable publisher is not a
pass, it is an unknown, and an unknown must not be quoted as agreement).
"""
from __future__ import annotations
import argparse, io, sys, urllib.request
from datetime import date, datetime, timedelta

CBOE_URL = "https://cdn.cboe.com/api/global/us_indices/daily_prices/SKEW_History.csv"
UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                    "(KHTML, like Gecko) Chrome/125 Safari/537.36"}
TOL = 0.005  # published to 6dp; anything past half a cent is a real disagreement


def fetch_cboe(timeout: int = 30) -> dict[date, float]:
    raw = urllib.request.urlopen(
        urllib.request.Request(CBOE_URL, headers=UA), timeout=timeout).read()
    out: dict[date, float] = {}
    for line in io.StringIO(raw.decode("utf-8", "replace")):
        parts = line.strip().split(",")
        if len(parts) < 2:
            continue
        try:
            d = datetime.strptime(parts[0].strip(), "%m/%d/%Y").date()
            out[d] = float(parts[1])
        except (ValueError, IndexError):
            continue          # header and any malformed row
    return out


def fetch_yf(period: str = "3mo") -> dict[date, float]:
    import yfinance as yf
    h = yf.Ticker("^SKEW").history(period=period)
    return {i.date(): float(c) for i, c in zip(h.index, h["Close"])}


def compare(cboe: dict[date, float], yfd: dict[date, float],
            lo: date, hi: date) -> tuple[list, list, list]:
    """Returns (omissions, disagreements, agreements) over [lo, hi] on CBOE dates.

    CBOE is the publisher of record, so ITS date set defines what should exist.
    A date yfinance has and CBOE does not is not a mirror defect — it is out of
    scope for this instrument and is deliberately not reported as one.
    """
    omissions, disagreements, agreements = [], [], []
    for d in sorted(k for k in cboe if lo <= k <= hi):
        if d not in yfd:
            omissions.append((d, cboe[d]))
        elif abs(cboe[d] - yfd[d]) > TOL:
            disagreements.append((d, cboe[d], yfd[d], cboe[d] - yfd[d]))
        else:
            agreements.append(d)
    return omissions, disagreements, agreements


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--days", type=int, default=30,
                    help="trailing calendar-day window to verify (default 30)")
    ap.add_argument("--since", help="verify from this ISO date instead of --days")
    ap.add_argument("--period", default="3mo",
                    help="yfinance history period; must span the window (default 3mo)")
    ap.add_argument("--quiet", action="store_true",
                    help="print only the one-line verdict meant to be pasted beside the claim")
    a = ap.parse_args(argv)

    try:
        cboe = fetch_cboe()
    except Exception as e:                                    # noqa: BLE001
        print(f"⛔ SKEW-INTEGRITY UNKNOWN — CBOE unreachable ({type(e).__name__}: {e}). "
              f"FAILING CLOSED: an unreachable publisher is not agreement. "
              f"Do NOT quote a ^SKEW value as verified on this run.")
        return 2
    try:
        yfd = fetch_yf(a.period)
    except Exception as e:                                    # noqa: BLE001
        print(f"⛔ SKEW-INTEGRITY UNKNOWN — yfinance mirror unreachable "
              f"({type(e).__name__}: {e}). FAILING CLOSED. CBOE alone cannot "
              f"establish mirror agreement; grade from CBOE and say the mirror was unchecked.")
        return 2

    hi = max(cboe)
    lo = date.fromisoformat(a.since) if a.since else hi - timedelta(days=a.days)
    om, dis, ag = compare(cboe, yfd, lo, hi)
    n = len(om) + len(dis) + len(ag)
    stamp = datetime.now().astimezone().strftime("%Y-%m-%d %H:%M %Z")

    if not a.quiet:
        print(f"^SKEW MIRROR INTEGRITY  •  {lo} .. {hi}  •  {n} CBOE session(s)  •  {stamp}")
        print(f"  publisher of record : CBOE SKEW_History.csv ({len(cboe):,} rows, "
              f"{min(cboe)} .. {max(cboe)})")
        print(f"  mirror              : yfinance ^SKEW  period={a.period}")
        print(f"  tolerance           : |Δ| > {TOL} counts as disagreement")
        print("─" * 78)
        if om:
            print(f"  🔴 OMITTED FROM MIRROR — {len(om)}:")
            for d, v in om:
                print(f"     {d}  CBOE {v:.6f}  ·  yfinance ABSENT")
        if dis:
            print(f"  🔴 VALUE DISAGREEMENT — {len(dis)}  (the mode a bar-count check cannot see):")
            for d, c, y, delta in dis:
                print(f"     {d}  CBOE {c:.6f}  ·  yfinance {y:.6f}  ·  Δ {delta:+.6f}")
        if not om and not dis:
            print(f"  ✅ {len(ag)} session(s) agree to within {TOL} — no omission, no disagreement.")
        print("─" * 78)

    # The one line that is meant to travel WITH the claim.
    if om or dis:
        verdict = (f"[SKEW-INTEGRITY {stamp}] 🔴 DEFECT over {lo}..{hi}: "
                   f"{len(om)} omission(s), {len(dis)} disagreement(s) across {n} CBOE sessions. "
                   f"GRADE FROM CBOE ONLY; the mirror is not usable for this window.")
    else:
        verdict = (f"[SKEW-INTEGRITY {stamp}] ✅ CBOE and yfinance agree on all {n} "
                   f"sessions {lo}..{hi} (|Δ| ≤ {TOL}). Verified AT TIME OF USE — "
                   f"this bounds THIS read only, not any earlier one.")
    print(verdict)
    return 1 if (om or dis) else 0


if __name__ == "__main__":
    raise SystemExit(main())
