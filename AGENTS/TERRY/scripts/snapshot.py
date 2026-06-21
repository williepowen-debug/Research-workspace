#!/usr/bin/env python3
"""
TERRY Snapshot — price/relative-strength context for trade construction.

Purpose: give Terry enough deterministic market context to discuss entries,
levels, relative strength, and data freshness without pretending to have a full
charting terminal or option chain.

Examples:
  python3 AGENTS/TERRY/scripts/snapshot.py WAL KRE --benchmark KRE --days 30 --stress
  python3 AGENTS/TERRY/scripts/snapshot.py TLT FXY --benchmark SPY --days 60
  python3 AGENTS/TERRY/scripts/snapshot.py --selftest

Notes:
- Prices/history come from FORGE/tools/market-data/fetch.py (yfinance wrapper).
- FRED stress values are dated observations, not live prints.
- Option-chain data is NOT fetched here; Terry must use POSITION_INTAKE / chain fields.
"""

from __future__ import annotations

import argparse
import math
import sys
from datetime import datetime
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent
TERRY_DIR = SCRIPTS_DIR.parent
WORKSPACE = SCRIPTS_DIR.parents[2]
FETCH_DIR = WORKSPACE / "FORGE" / "tools" / "market-data"
sys.path.insert(0, str(FETCH_DIR))

try:
    from fetch import fred_fetch, price_fetch, price_history
except Exception as e:  # pragma: no cover
    print(f"FATAL: cannot import FORGE market-data fetch.py from {FETCH_DIR}: {e}")
    sys.exit(2)

DEFAULT_BENCHMARKS = {
    "WAL": "KRE", "OZK": "KRE", "KRE": "SPY", "XLF": "SPY",
    "HYG": "SPY", "JNK": "SPY", "BIZD": "SPY", "APO": "SPY", "ARES": "SPY",
    "TLT": "SPY", "FXY": "SPY", "BZ=F": "USO", "CL=F": "USO",
}

FRED_STRESS = [
    ("BAMLH0A0HYM2", "HY OAS", 100, "bps"),
    ("BAMLH0A3HYC", "CCC OAS", 100, "bps"),
    ("DGS10", "10Y", 1, "%"),
]


def fmt_pct(x):
    if x is None or (isinstance(x, float) and math.isnan(x)):
        return "N/A"
    return f"{x:+.2f}%"


def hist_stats(rows):
    """Rows are chronological from fetch.price_history; compute simple chart stats."""
    if not rows:
        return {}
    closes = [float(r["close"]) for r in rows if r.get("close") is not None]
    if not closes:
        return {}
    first, last = closes[0], closes[-1]
    high, low = max(closes), min(closes)
    ret = ((last - first) / first * 100) if first else None
    # simple location within range: 0=low, 100=high
    loc = ((last - low) / (high - low) * 100) if high != low else 50.0
    ma20 = sum(closes[-20:]) / min(20, len(closes))
    ma50 = sum(closes[-50:]) / min(50, len(closes))
    return dict(first=first, last=last, high=high, low=low, return_pct=ret, range_loc=loc, ma20=ma20, ma50=ma50)


def marker_for_location(loc):
    if loc is None:
        return "?"
    if loc >= 80:
        return "near range high"
    if loc <= 20:
        return "near range low"
    return "mid-range"


def stress_rows():
    out = []
    for sid, label, mult, unit in FRED_STRESS:
        obs = fred_fetch(sid, limit=2)
        if not obs or "error" in obs[0]:
            out.append((label, "ERR", "", obs[0].get("error", "no data") if obs else "no data"))
            continue
        try:
            val = float(obs[0]["value"]) * mult
            disp = f"{val:.0f}{unit}" if unit == "bps" else f"{val:.2f}{unit}"
        except Exception:
            disp = str(obs[0].get("value"))
        out.append((label, disp, obs[0]["date"], "FRED observation date"))
    return out


def run(args):
    tickers = [t.upper() for t in args.tickers]
    if not tickers:
        print("No tickers supplied. Try: snapshot.py WAL KRE --benchmark KRE")
        return 1

    benchmark = (args.benchmark or DEFAULT_BENCHMARKS.get(tickers[0]) or "SPY").upper()
    fetch_tickers = sorted(set(tickers + [benchmark]))

    print(f"TERRY snapshot — {datetime.now().strftime('%Y-%m-%d %H:%M local')}")
    print(f"Tickers: {', '.join(tickers)} | Benchmark: {benchmark} | Lookback: {args.days}d")
    print("Data: yfinance via FORGE fetch.py; option-chain NOT included.\n")

    prices = price_fetch(fetch_tickers)
    histories = price_history(fetch_tickers, days=args.days)
    bench_stats = hist_stats(histories.get(benchmark, {}).get("history", []))
    bench_ret = bench_stats.get("return_pct")

    print("PRICE / TAPE")
    print("Ticker     Price      Day chg   Lookback  Rel vs bench   Range loc     Key range")
    print("---------  ---------  --------  --------  -------------  ------------  ----------------")
    for t in tickers:
        p = prices.get(t, {})
        h = histories.get(t, {})
        if "error" in p or "error" in h:
            print(f"{t:<9}  ERROR     {str(p.get('error') or h.get('error'))[:70]}")
            continue
        st = hist_stats(h.get("history", []))
        ret = st.get("return_pct")
        rel = (ret - bench_ret) if ret is not None and bench_ret is not None and t != benchmark else None
        loc = st.get("range_loc")
        range_txt = f"{st.get('low', 0):.2f}–{st.get('high', 0):.2f}" if st else "N/A"
        price = p.get("price")
        price_txt = f"{price:.2f}" if isinstance(price, (int, float)) else "N/A"
        day = fmt_pct(p.get("change_pct"))
        print(f"{t:<9}  {price_txt:>9}  {day:>8}  {fmt_pct(ret):>8}  {fmt_pct(rel):>13}  {marker_for_location(loc):<12}  {range_txt}")

    if benchmark not in tickers:
        st = bench_stats
        print(f"\nBenchmark {benchmark}: {fmt_pct(bench_ret)} over {args.days}d; range {st.get('low', 0):.2f}–{st.get('high', 0):.2f}" if st else f"\nBenchmark {benchmark}: unavailable")

    print("\nTERRY READ PROMPTS")
    print("- Entry quality: avoid chasing if price is near range extreme without fresh catalyst.")
    print("- Invalidation: use nearby support/resistance or thesis/tape break; do not hide behind macro narrative.")
    print("- Options: chain still required (bid/ask, OI/volume, IV, delta, theta, expected move).")

    if args.stress:
        print("\nCREDIT / RATES BACKDROP")
        for label, val, d, note in stress_rows():
            print(f"- {label}: {val}" + (f" [{d}]" if d else "") + f" — {note}")
    return 0


def selftest():
    assert FETCH_DIR.exists(), f"missing fetch dir: {FETCH_DIR}"
    assert (FETCH_DIR / "fetch.py").exists(), "missing fetch.py"
    rows = fred_fetch("BAMLH0A0HYM2", limit=1)
    assert rows and "error" not in rows[0], f"FRED selftest failed: {rows}"
    print("snapshot.py SELFTEST: PASS")
    return 0


def main():
    ap = argparse.ArgumentParser(description="TERRY price/relative-strength snapshot")
    ap.add_argument("tickers", nargs="*", help="Tickers/instruments, e.g. WAL KRE TLT")
    ap.add_argument("--benchmark", "-b", help="Relative-strength benchmark (default inferred, often SPY/KRE)")
    ap.add_argument("--days", type=int, default=30, help="Lookback days for simple range/return stats")
    ap.add_argument("--stress", action="store_true", help="Include HY/CCC/10Y FRED backdrop")
    ap.add_argument("--selftest", action="store_true", help="Validate imports/FRED access")
    args = ap.parse_args()
    if args.selftest:
        return selftest()
    return run(args)


if __name__ == "__main__":
    raise SystemExit(main())
