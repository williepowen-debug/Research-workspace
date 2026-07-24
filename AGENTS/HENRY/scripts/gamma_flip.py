#!/usr/bin/env python3
"""
gamma_flip.py — compute the SPX dealer-gamma flip (zero-gamma level) from the
LIVE ^SPX options chain via yfinance + Black-Scholes gamma. No paywalled
provider (SpotGamma/FlashAlpha) required — a FREE-TIER estimator (validated
2026-07-17 vs FlashAlpha/zerogex: flip within 20-34pts, walls exact-match).

boot.py imports compute_gamma_flip() for its (b) GAMMA section (14d horizon,
fast); run this script standalone for the definitive 35d read.

Method
------
- Pull ^SPX option chains for all expirations <= HORIZON_DAYS (near-term gamma
  dominates the flip); filter OI>0, sane IV (0.03-2.5), strikes within band of spot.
- BSM gamma per contract (r=4.5%, q=1.3% SPX div yield), gamma from yfinance IV.
- Dealer convention (standard SpotGamma-style naive): dealers LONG call gamma (+),
  SHORT put gamma (-). Net GEX(S) = sum_calls - sum_puts, in $ per 1% move.
- Zero-gamma FLIP = spot where Net GEX(S) crosses zero (grid + linear interp).
- Call/put walls = strikes with max gamma-weighted OI.

CAVEAT (state when citing): the ABSOLUTE $B depends on the dealer-positioning
assumption (real books differ; vendors apply proprietary adjustments — this is a
FREE-TIER proxy, NOT SpotGamma-grade). The FLIP LEVEL and the SIGN are the robust
reads; don't trust the exact level within ~30-40pts of a crossing.

Usage: .venv/bin/python3 AGENTS/HENRY/scripts/gamma_flip.py [--days N] [--asof YYYY-MM-DD]
"""
import sys, math
from datetime import date, datetime
from collections import defaultdict

# A healthy <=35d ^SPX pull is thousands of contracts (6,206 on 7/17, 4,900 at 14d).
# Below this the chain is too degraded to locate a flip — see the thin-chain guard.
MIN_CONTRACTS = 400


def _isnan(x):
    """True for NaN. Note `x or 0` does NOT catch NaN (NaN is truthy) — the 7/23 bug."""
    try:
        return math.isnan(float(x))
    except (TypeError, ValueError):
        return True

R, Q = 0.045, 0.013
HORIZON_DAYS = 35


def npdf(x):
    return math.exp(-0.5 * x * x) / math.sqrt(2 * math.pi)


def bsm_gamma(S, K, T, sig):
    if T <= 0 or sig <= 0 or S <= 0 or K <= 0:
        return 0.0
    d1 = (math.log(S / K) + (R - Q + 0.5 * sig * sig) * T) / (sig * math.sqrt(T))
    return math.exp(-Q * T) * npdf(d1) / (S * sig * math.sqrt(T))


def compute_gamma_flip(asof=None, horizon=HORIZON_DAYS, band=0.25):
    """Compute the SPX dealer-gamma flip from the live ^SPX chain.

    Returns a dict {spot, flip, flips, gex_at_spot, regime, call_wall, put_wall,
    n_contracts, horizon, band, asof} — or {'error': msg} on any failure (never
    raises, so boot.py can degrade gracefully).
    """
    try:
        import yfinance as yf
    except Exception as e:  # noqa: BLE001
        return {"error": f"yfinance import failed: {e}"}
    today = datetime.strptime(asof, "%Y-%m-%d").date() if asof else date.today()
    try:
        t = yf.Ticker("^SPX")
        spot = t.fast_info["lastPrice"]
        exps = t.options
    except Exception as e:  # noqa: BLE001
        return {"error": f"chain fetch failed: {e}"}
    if not spot or not exps:
        return {"error": "no spot/expirations from yfinance"}

    opts = []
    for exp in exps:
        y, m, d = map(int, exp.split("-"))
        T = (date(y, m, d) - today).days / 365.0
        if T <= 0 or T > horizon / 365.0:
            continue
        try:
            ch = t.option_chain(exp)
        except Exception:  # noqa: BLE001
            continue
        for df, typ in ((ch.calls, "C"), (ch.puts, "P")):
            for _, r in df.iterrows():
                K = r["strike"]; oi = r["openInterest"] or 0; iv = r["impliedVolatility"] or 0
                # NaN guard (7/23 bug): `x or 0` does NOT catch NaN — NaN is truthy, and
                # `NaN <= 0` is False, so NaN OI used to survive this filter and poison the
                # GEX sum. A NaN g0 then read as POSITIVE in boot.py (`g0 < 0`) and NEGATIVE
                # in the CLI (`g0 > 0`) — same number, opposite labels — while max() over an
                # all-NaN wall dict returned an arbitrary strike (put wall above call wall).
                # Fail loud on missing data; never emit a confident number built on NaN.
                if _isnan(K) or _isnan(oi) or _isnan(iv):
                    continue
                if oi <= 0 or not (0.03 < iv < 2.5):
                    continue
                if not ((1 - band) * spot < K < (1 + band) * spot):
                    continue
                opts.append((K, T, iv, oi, typ))
    if not opts:
        return {"error": "no usable contracts after filtering"}
    # Thin-chain guard (7/23): a healthy <=35d pull is thousands of contracts (6,206 on
    # 7/17). yfinance intermittently returns NaN IV for most of the chain, which the IV
    # filter correctly drops — leaving a residue too thin to locate a flip. Refuse to
    # emit rather than publish a number off a degraded feed.
    if len(opts) < MIN_CONTRACTS:
        return {"error": f"chain too thin: {len(opts)} usable contracts "
                         f"(< {MIN_CONTRACTS}); yfinance IV/OI feed degraded — "
                         f"no gamma read this run"}

    def net_gex(S):
        g = 0.0
        for K, T, iv, oi, typ in opts:
            gam = bsm_gamma(S, K, T, iv) * oi * 100 * S * S * 0.01
            g += gam if typ == "C" else -gam
        return g

    g0 = net_gex(spot)
    if _isnan(g0):
        return {"error": "net GEX computed as NaN — refusing to emit a regime call"}
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

    return {
        "spot": spot,
        "flip": flips[0] if flips else None,
        "flips": flips,
        "gex_at_spot": g0,
        "regime": "NEGATIVE" if g0 < 0 else "POSITIVE",
        "call_wall": max(cg, key=cg.get) if cg else None,
        "put_wall": max(pg, key=pg.get) if pg else None,
        "n_contracts": len(opts),
        "horizon": horizon,
        "band": band,
        "asof": today.isoformat(),
    }


def _flag(name, default):
    if name in sys.argv:
        return sys.argv[sys.argv.index(name) + 1]
    return default


def main():
    horizon = int(_flag("--days", HORIZON_DAYS))
    asof = _flag("--asof", None)
    r = compute_gamma_flip(asof=asof, horizon=horizon)
    if "error" in r:
        print(f"gamma_flip: {r['error']}")
        return 1

    spot, flips = r["spot"], r["flips"]
    print(f"===== SPX GAMMA FLIP  (asof {r['asof']}, <= {horizon}d, {r['n_contracts']} contracts) =====")
    print(f"  SPX spot        {spot:,.2f}")
    print(f"  Net GEX @ spot  {r['gex_at_spot']/1e9:+.1f} $B/1%   -> "
          f"{'POSITIVE (dealers dampen)' if r['gex_at_spot'] > 0 else 'NEGATIVE (dealers AMPLIFY)'}")
    print(f"  Zero-gamma FLIP {'  '.join(f'~{f:,.0f}' for f in flips) if flips else 'none in +/-10% band'}")
    if flips:
        rel = spot - flips[0]
        print(f"                  spot is {rel:+,.0f} pts {'BELOW (neg-gamma)' if rel < 0 else 'ABOVE (pos-gamma)'} the flip")
    cw, pw = r["call_wall"], r["put_wall"]
    print(f"  Call wall       {cw:,.0f}")
    print(f"  Put wall        {pw:,.0f}  {'<- SPX BELOW put wall (intensified downside feedback)' if pw and spot < pw else ''}")
    print("  (FREE-TIER proxy: absolute $B assumes long-call/short-put dealer gamma; the FLIP + sign are the robust reads)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
