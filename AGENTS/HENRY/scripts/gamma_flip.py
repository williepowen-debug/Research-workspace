#!/usr/bin/env python3
"""
gamma_flip.py — compute the SPX dealer-gamma flip (zero-gamma level) from the
LIVE ^SPX options chain via yfinance + Black-Scholes gamma. No paywalled
provider (SpotGamma/FlashAlpha) required — resolves HENRY's persistent
"exact flip paywalled" GAP.

Method
------
- Pull ^SPX option chains for all expirations <= HORIZON_DAYS (near-term gamma
  dominates the flip); filter OI>0, sane IV (0.03-2.5), strikes within +/-25% of spot.
- BSM gamma per contract (r=4.5%, q=1.3% SPX div yield), gamma from yfinance IV.
- Dealer convention (standard SpotGamma-style naive): dealers LONG call gamma (+),
  SHORT put gamma (-). Net GEX(S) = sum_calls - sum_puts, in $ per 1% move.
- Zero-gamma FLIP = spot where Net GEX(S) crosses zero (grid + linear interp).
- Call/put walls = strikes with max gamma-weighted OI.

CAVEAT (state when citing): the ABSOLUTE $B depends on the dealer-positioning
assumption (real books differ; vendors apply proprietary adjustments). The FLIP
LEVEL and the SIGN of net gamma are robust — they are where gamma-weighted OI
balances. Greeks are BSM-from-IV, not vendor greeks.

Usage: .venv/bin/python3 AGENTS/HENRY/scripts/gamma_flip.py [--days N] [--asof YYYY-MM-DD]
"""
import sys, math
from datetime import date, datetime
import yfinance as yf
from collections import defaultdict

R, Q = 0.045, 0.013
HORIZON_DAYS = 35

def _flag(name, default):
    if name in sys.argv:
        return sys.argv[sys.argv.index(name) + 1]
    return default

def npdf(x):
    return math.exp(-0.5 * x * x) / math.sqrt(2 * math.pi)

def bsm_gamma(S, K, T, sig):
    if T <= 0 or sig <= 0 or S <= 0 or K <= 0:
        return 0.0
    d1 = (math.log(S / K) + (R - Q + 0.5 * sig * sig) * T) / (sig * math.sqrt(T))
    return math.exp(-Q * T) * npdf(d1) / (S * sig * math.sqrt(T))

def main():
    horizon = int(_flag("--days", HORIZON_DAYS))
    asof = _flag("--asof", None)
    today = datetime.strptime(asof, "%Y-%m-%d").date() if asof else date.today()

    t = yf.Ticker("^SPX")
    spot = t.fast_info["lastPrice"]

    opts = []
    for exp in t.options:
        y, m, d = map(int, exp.split("-"))
        T = (date(y, m, d) - today).days / 365.0
        if T <= 0 or T > horizon / 365.0:
            continue
        ch = t.option_chain(exp)
        for df, typ in ((ch.calls, "C"), (ch.puts, "P")):
            for _, r in df.iterrows():
                K = r["strike"]; oi = r["openInterest"] or 0; iv = r["impliedVolatility"] or 0
                if oi <= 0 or not (0.03 < iv < 2.5):
                    continue
                if not (0.75 * spot < K < 1.25 * spot):
                    continue
                opts.append((K, T, iv, oi, typ))

    def net_gex(S):
        g = 0.0
        for K, T, iv, oi, typ in opts:
            gam = bsm_gamma(S, K, T, iv) * oi * 100 * S * S * 0.01
            g += gam if typ == "C" else -gam
        return g

    g0 = net_gex(spot)
    lo, hi = int(spot * 0.90), int(spot * 1.10)
    vals = [(S, net_gex(S)) for S in range(lo, hi, 5)]
    flips = []
    for (S1, v1), (S2, v2) in zip(vals, vals[1:]):
        if v1 == 0 or (v1 < 0) != (v2 < 0):
            flips.append(S1 + (0 - v1) * (S2 - S1) / (v2 - v1))

    cg, pg = defaultdict(float), defaultdict(float)
    for K, T, iv, oi, typ in opts:
        w = bsm_gamma(spot, K, T, iv) * oi
        (cg if typ == "C" else pg)[K] += w
    callwall = max(cg, key=cg.get) if cg else float("nan")
    putwall = max(pg, key=pg.get) if pg else float("nan")

    print(f"===== SPX GAMMA FLIP  (asof {today}, <= {horizon}d, {len(opts)} contracts) =====")
    print(f"  SPX spot        {spot:,.2f}")
    print(f"  Net GEX @ spot  {g0/1e9:+.1f} $B/1%   -> {'POSITIVE (dealers dampen)' if g0 > 0 else 'NEGATIVE (dealers AMPLIFY)'}")
    print(f"  Zero-gamma FLIP {'  '.join(f'~{f:,.0f}' for f in flips) if flips else 'none in +/-10% band'}")
    if flips:
        f = flips[0]
        rel = spot - f
        print(f"                  spot is {rel:+,.0f} pts {'BELOW (neg-gamma)' if rel < 0 else 'ABOVE (pos-gamma)'} the flip")
    print(f"  Call wall       {callwall:,.0f}")
    print(f"  Put wall        {putwall:,.0f}  {'<- SPX BELOW put wall (intensified downside feedback)' if spot < putwall else ''}")
    print(f"  (caveat: absolute $B assumes long-call/short-put dealer gamma; FLIP + sign are the robust reads)")

if __name__ == "__main__":
    main()
