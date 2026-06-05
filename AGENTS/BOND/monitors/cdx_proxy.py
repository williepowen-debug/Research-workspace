"""
cdx_proxy.py — BOND free proxy for the CDX / cash-credit basis vector (VX-BND-06)
================================================================================

WHY THIS EXISTS
---------------
True CDX.HY / CDX.IG index levels are owned by S&P Global / Markit and are NOT
available from a free source. For weeks VX-BND-06 sat as "🟡 data gap" — one of
seven convergence vectors effectively dark. This script wires a DEFENSIBLE FREE
PROXY so the vector is monitorable, while being explicit about what it can and
cannot see.

WHAT IT MEASURES (and what it does NOT)
---------------------------------------
The decision question the vector serves: "Is cash-credit calm fake — is the
faster hedging/derivatives layer signaling stress that cash bonds haven't
repriced yet?"

Proxy construct:
  HYG/IEF ratio = HY credit ETF stripped of duration (IEF = 7-10Y UST ETF).
  This isolates the CREDIT component of HYG from the rates component.
  - HYG/IEF ROLLS OVER while cash HY OAS (FRED) stays tight  -> fast layer
    leading cash -> proxy for "synthetic/fast-money leading cash."
  - HYG/IEF and cash OAS move together                       -> no divergence.

LIMITATION (read this before citing it):
  HYG is CASH (an ETF holding bonds), not SYNTHETIC. So this is a
  faster-cash-vs-slower-cash lead/lag proxy, NOT the true synthetic-vs-cash
  basis. The genuinely synthetic, fast-money signal lives in HYG OPTIONS
  (put skew / implied vol) — which is VIOLET's domain. For the real synthetic
  read, request HYG option-skew from VIOLET. True CDX requires the S&P Global
  MCP connector (needs auth) or a paid Markit feed.

USAGE
-----
  source .venv/bin/activate && python3 AGENTS/BOND/monitors/cdx_proxy.py

Signals (printed):
  - HYG/IEF level vs 3-month range (rich = top, stressed = bottom)
  - 20-day z-score of the ratio (momentum of the credit-excess move)
  - 20-day % change
  - Cross-check line vs cash HY OAS (pull separately from FRED BAMLH0A0HYM2)
"""

from __future__ import annotations
import sys
import pandas as pd


def main() -> int:
    try:
        import yfinance as yf
    except ImportError:
        print("yfinance not available — run inside .venv")
        return 1

    px = yf.download(["HYG", "IEF", "JNK", "LQD"], period="3mo", progress=False)["Close"].dropna()
    if px.empty:
        print("no price data returned")
        return 1

    hy_ratio = px["HYG"] / px["IEF"]      # HY credit excess (duration-stripped)
    ig_ratio = px["LQD"] / px["IEF"]      # IG credit excess (cross-check)

    def z20(s: pd.Series) -> pd.Series:
        return (s - s.rolling(20).mean()) / s.rolling(20).std()

    out = pd.DataFrame({
        "HYG/IEF": hy_ratio,
        "HYG/IEF_z20": z20(hy_ratio),
        "LQD/IEF": ig_ratio,
        "LQD/IEF_z20": z20(ig_ratio),
    })

    print("=== BOND CDX-basis PROXY (free) — HYG/IEF credit-excess ===")
    print(out.tail(10).round(4).to_string())
    lo, hi, now = hy_ratio.min(), hy_ratio.max(), hy_ratio.iloc[-1]
    pctile = (hy_ratio <= now).mean() * 100
    print()
    print(f"HYG/IEF now {now:.4f} | 3mo range {lo:.4f}-{hi:.4f} | {pctile:.0f}th pctile of 3mo")
    print(f"20d chg: {(now/hy_ratio.iloc[-21]-1)*100:+.2f}% | z20 {out['HYG/IEF_z20'].iloc[-1]:+.2f}")
    print()
    print("READ: ratio near TOP of range = credit-excess RICH, no hidden stress.")
    print("      ratio breaking to BOTTOM while cash HY OAS stays tight = DIVERGENCE -> signal HENRY/LIQUID.")
    print("Cross-check vs cash: python3 FORGE/tools/market-data/fetch.py fred BAMLH0A0HYM2 --periods 5")
    print("Synthetic/options leg (not visible here): request HYG put-skew from VIOLET.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
