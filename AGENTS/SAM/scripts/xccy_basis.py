#!/usr/bin/env python3
"""JPY cross-currency basis PROXY — CIP residual from CME JPY futures.

WHY: RED's constructive item from the CHG-RED-048 blind pass (2026-08-20). A ~$400B-class
swap-funded yen carry book is INVISIBLE to CFTC but NOT to its funding market: on a genuine
unwind the JPY cross-currency basis should move; on a "nothing really unwound" day it should
not. That is the nearest thing to a DISCRIMINATING daily observation for the rival mechanism
K1 exposed -- and it is the metric surface CFTC-keyed killers lack.

⛔⛔ THIS IS NOT THE CROSS-CURRENCY BASIS. READ THIS BEFORE CITING ANY NUMBER BELOW. ⛔⛔
The true 3m JPY xccy basis needs 3m USDJPY forward points, a 3m USD OIS rate and a 3m JPY
OIS/TONA rate. Of those, the 3m JPY leg is NOT reachable from any primary this desk has
proven (MOF's JGB curve starts at 1Y; JBA TIBOR and FRED are both unreachable from this box
-- FRED timed out on every attempt 2026-08-27). So:
  * the forward leg is the CME Sep->Dec JPY futures SPREAD (a genuine fixed ~3m tenor,
    chosen over spot-vs-front precisely to avoid [[finding_continuous_front_ticker_rolls_so_deltas_lie]]);
  * the USD leg is the Treasury 3m par yield (a BILL yield, not OIS -- a real substitution);
  * the JPY leg is an ASSUMPTION (BOJ policy rate), not a measurement.
⇒ The LEVEL printed here carries the JPY-leg assumption and the bill-vs-OIS substitution and
  is worth AT BEST an order of magnitude. Do not quote it as "the basis".
⇒ The CHANGES are the usable part: a wrong-but-CONSTANT JPY assumption cancels in first
  differences, which is why this file reports d(residual) and grades on it.
⇒ If it cannot discriminate the test dates, SAY SO rather than dress it up. That is the whole
  reason the instrument exists.
"""
import sys, csv, urllib.request, warnings
from pathlib import Path
from datetime import datetime, date
warnings.filterwarnings("ignore")

SAM = Path(__file__).resolve().parent.parent
OUT = SAM / "workbook" / "XCCY_BASIS.tsv"
UST_URL = ("https://home.treasury.gov/resource-center/data-chart-center/interest-rates/"
           "daily-treasury-rates.csv/{yr}/all?type=daily_treasury_yield_curve"
           "&field_tdr_date_value={yr}&page&_format=csv")
HEADERS = {"User-Agent": "Mozilla/5.0 (SAM-Research)"}

NEAR, FAR = "6JU26.CME", "6JZ26.CME"          # Sep-2026, Dec-2026
NEAR_EXP, FAR_EXP = date(2026, 9, 14), date(2026, 12, 14)
LEG_DAYS = (FAR_EXP - NEAR_EXP).days
BOJ_POLICY = 1.00      # ASSUMPTION for the JPY leg -- not a measurement
TEST_DATES = ["2026-08-07", "2026-08-19"]      # RED's two named days

def ust_3m(years):
    out = {}
    for yr in years:
        txt = urllib.request.urlopen(urllib.request.Request(UST_URL.format(yr=yr), headers=HEADERS),
                                     timeout=45).read().decode("utf-8-sig", errors="replace")
        for r in csv.DictReader(txt.splitlines()):
            try:
                out[datetime.strptime(r["Date"].strip(), "%m/%d/%Y").strftime("%Y-%m-%d")] = float(r["3 Mo"])
            except (ValueError, KeyError, TypeError):
                continue
    return out

def main():
    import yfinance as yf
    px = {}
    for sym in (NEAR, FAR):
        h = yf.Ticker(sym).history(start="2026-07-01", end="2026-08-28")
        if h.empty:
            print(f"  🔴 {sym} returned NO DATA — NO VERDICT (never substitute the continuous front)"); return 1
        px[sym] = {d.strftime("%Y-%m-%d"): float(c) for d, c in zip(h.index, h["Close"])}
    try:
        us = ust_3m(sorted({d[:4] for d in px[NEAR]}))
    except Exception as e:
        print(f"  🔴 US leg fetch FAILED ({type(e).__name__}) — NO VERDICT"); return 1

    dates = sorted(set(px[NEAR]) & set(px[FAR]) & set(us))
    rows = []
    for d in dates:
        n, f = px[NEAR][d], px[FAR][d]
        implied = (f / n - 1.0) * (365.0 / LEG_DAYS) * 100.0     # ann. %, USD-JPY fwd-fwd diff
        cash = us[d] - BOJ_POLICY                                 # ann. %, ASSUMED JPY leg
        rows.append((d, n, f, implied, cash, (implied - cash) * 100.0))   # residual in bp

    print(f"\n{'='*74}\n  JPY XCCY BASIS **PROXY** (CIP residual)   {datetime.now():%Y-%m-%d %H:%M}\n{'='*74}")
    print(f"  ⛔ NOT THE BASIS. JPY leg is an ASSUMPTION (BOJ {BOJ_POLICY:.2f}%), USD leg is a BILL")
    print(f"     yield not OIS. LEVEL is order-of-magnitude only; the CHANGES are the usable part.")
    print(f"  Tenor: {NEAR}→{FAR} spread = fixed {LEG_DAYS}d (no roll, no spot-timing mismatch)")

    # UNIT ANCHOR — hard stop, same discipline as bis_gli.py
    last = rows[-1]
    if not (0.0 < last[3] < 8.0):
        print(f"  🔴 UNIT ANCHOR FAILED: implied differential {last[3]:.2f}% outside 0-8% — "
              f"refusing to write a figure wrong by 10^n."); return 1
    print(f"  ✅ unit anchor: implied diff {last[3]:.2f}% is a plausible USD-JPY differential")

    print(f"\n  {'Date':<12}{'implied%':>10}{'cash%':>9}{'resid bp':>10}{'d resid':>9}")
    prev = None
    for d, n, f, imp, cash, res in rows[-10:]:
        dr = "" if prev is None else f"{res-prev:+8.1f}"
        print(f"  {d:<12}{imp:>10.3f}{cash:>9.3f}{res:>10.1f}{dr:>9}")
        prev = res

    resid = {r[0]: r[5] for r in rows}
    ds = [r[0] for r in rows]
    chg = {ds[i]: resid[ds[i]] - resid[ds[i-1]] for i in range(1, len(ds))}
    vals = sorted(abs(v) for v in chg.values())
    med = vals[len(vals)//2]; p90 = vals[int(0.9*len(vals))]
    print(f"\n  RESIDUAL DAILY |Δ| over {len(chg)} obs: median {med:.1f}bp · p90 {p90:.1f}bp")

    print(f"\n  🔴 RED'S TEST — did the funding market move on the days the tape did?")
    for t in TEST_DATES:
        if t in chg:
            v = chg[t]; rank = sum(1 for x in chg.values() if abs(x) <= abs(v)) / len(chg)
            verdict = "MOVED (top decile)" if abs(v) >= p90 else ("moved" if abs(v) > med else "QUIET")
            print(f"    {t}: Δresidual {v:+.1f}bp — {verdict}, {100*rank:.0f}th pct of daily moves")
        else:
            print(f"    {t}: no observation")

    with open(OUT, "w") as fh:
        fh.write("Date\tNear_Px\tFar_Px\tImplied_Diff_pct\tCash_Diff_pct\tResidual_bp\n")
        for d, n, f, imp, cash, res in rows:
            fh.write(f"{d}\t{n:.7f}\t{f:.7f}\t{imp:.4f}\t{cash:.4f}\t{res:.2f}\n")
    print(f"\n  → {OUT.name} ({len(rows)} rows)")
    print(f"  ⚠️  {len(rows)} observations is a SHORT window and one regime. A percentile here is")
    print(f"     descriptive, not calibrated. This instrument fires NOTHING on its own.\n")
    return 0

if __name__ == "__main__":
    sys.exit(main())
