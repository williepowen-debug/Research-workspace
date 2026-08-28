#!/usr/bin/env python3
"""
LIQUID — T3 / Test A decoupling dry-run (DOCKET 2026-09-01).

FROZEN LETTER (FORUM/2026-08-10_financial-conditions/04_synthesis/06_HENRY_joint-synthesis-FINAL.md, T3):
  "Regress 20-sess dHY and dVIX on dDXY; correlate residuals.
   <0.15 => shared factor is the dollar; >=0.45 => ~1.5 near the ceiling"
  Test design LIQUID / numeric bands HENRY. Flagged UNDER-POWERED (~9 of 12 windows).

This is a DRY RUN. It grades NOTHING. It reports the interim value, its uncertainty, and
whether 20 sessions can support the letter's own bands.

BASIS (declare when citing): HY OAS = FRED BAMLH0A0HYM2 (EOD, T+1). VIX = FRED VIXCLS
(EOD close, NOT intraday). Dollar = BOTH tested: FRED DTWEXBGS (Nominal Broad Dollar,
daily) and yfinance DX-Y.NYB (the actual ICE DXY the letter names). Deltas are first
differences of daily closes on the COMMON trading-day index of all three series.
"""
import sys, math, argparse, statistics
sys.path.insert(0, "FORGE/tools/market-data")
from fetch import fred_fetch

def fred(sid, n=800):
    out = {}
    for x in fred_fetch(sid, limit=n):
        v = x.get("value")
        if v in (".", "", None):
            continue
        out[x["date"]] = float(v)
    return out

def yf_close(tkr, n=800):
    try:
        import yfinance as yf
        h = yf.Ticker(tkr).history(period="3y", auto_adjust=False)
        return {d.strftime("%Y-%m-%d"): float(c) for d, c in h["Close"].items()}
    except Exception as e:
        print(f"  [warn] {tkr} unavailable: {e}", file=sys.stderr)
        return {}

def ols_resid(y, x):
    """Residuals of y regressed on x with an intercept."""
    n = len(y); mx = sum(x)/n; my = sum(y)/n
    sxx = sum((xi-mx)**2 for xi in x)
    b = (sum((xi-mx)*(yi-my) for xi, yi in zip(x, y))/sxx) if sxx > 0 else 0.0
    a = my - b*mx
    return [yi - (a + b*xi) for xi, yi in zip(x, y)], b

def corr(a, b):
    n = len(a); ma = sum(a)/n; mb = sum(b)/n
    va = sum((x-ma)**2 for x in a); vb = sum((x-mb)**2 for x in b)
    if va <= 0 or vb <= 0: return float("nan")
    return sum((x-ma)*(y-mb) for x, y in zip(a, b))/math.sqrt(va*vb)

def fisher_ci(r, n, k=1, conf=0.95):
    """CI for a PARTIAL correlation controlling k variables: se = 1/sqrt(n-3-k)."""
    df = n - 3 - k
    if df <= 0 or abs(r) >= 1: return (float("nan"), float("nan"), float("nan"))
    z = 0.5*math.log((1+r)/(1-r)); se = 1/math.sqrt(df)
    zc = 1.959963985
    return (math.tanh(z-zc*se), math.tanh(z+zc*se), se)

def power_at(rho, n, k=1, alpha=0.05):
    """Power to reject rho=0 at |rho|=rho, partial correlation, two-sided."""
    df = n - 3 - k
    if df <= 0: return 0.0
    se = 1/math.sqrt(df); z = 0.5*math.log((1+rho)/(1-rho))
    zc = 1.959963985
    # P(|Z| > zc) with Z ~ N(z/se, 1)
    lam = z/se
    Phi = lambda t: 0.5*(1+math.erf(t/math.sqrt(2)))
    return (1 - Phi(zc - lam)) + Phi(-zc - lam)

ap = argparse.ArgumentParser()
ap.add_argument("--window", type=int, default=20)
ap.add_argument("--through", default=None, help="last obs date (default: latest)")
a = ap.parse_args()

hy = fred("BAMLH0A0HYM2"); vix = fred("VIXCLS"); dxb = fred("DTWEXBGS")
dxy = yf_close("DX-Y.NYB")

for dollar_name, dollar in (("DX-Y.NYB (the ICE DXY the letter names)", dxy),
                            ("FRED DTWEXBGS (Nominal Broad Dollar)", dxb)):
    if not dollar:
        print(f"\n=== DOLLAR LEG: {dollar_name} — UNAVAILABLE, skipped ==="); continue
    dates = sorted(set(hy) & set(vix) & set(dollar))
    if a.through: dates = [d for d in dates if d <= a.through]
    W = a.window
    if len(dates) < W+1:
        print(f"\n=== {dollar_name}: only {len(dates)} common obs, need {W+1} ==="); continue
    win = dates[-(W+1):]
    dHY  = [ (hy[win[i]]-hy[win[i-1]])*100 for i in range(1, len(win)) ]
    dVIX = [ vix[win[i]]-vix[win[i-1]]     for i in range(1, len(win)) ]
    dDX  = [ dollar[win[i]]-dollar[win[i-1]] for i in range(1, len(win)) ]
    n = len(dHY)
    rHY, bHY   = ols_resid(dHY, dDX)
    rVIX, bVIX = ols_resid(dVIX, dDX)
    r  = corr(rHY, rVIX)
    raw = corr(dHY, dVIX)
    lo, hi, se = fisher_ci(r, n, k=1)
    print(f"\n=== T3 / Test A — DRY RUN (grades nothing) ===")
    print(f"  dollar leg      : {dollar_name}")
    print(f"  window          : {W} sessions of DELTAS, {win[1]} -> {win[-1]}  (n={n})")
    print(f"  raw corr(dHY,dVIX)                   = {raw:+.3f}")
    print(f"  PARTIAL corr of residuals on dDXY    = {r:+.3f}   <-- the letter's statistic")
    print(f"  95% CI (Fisher, df=n-4={n-4})          = [{lo:+.3f}, {hi:+.3f}]   (se_z={se:.3f})")
    print(f"  dDXY betas: dHY {bHY:+.3f} bp/unit · dVIX {bVIX:+.4f} pts/unit")
    band = ("<0.15  => SHARED FACTOR IS THE DOLLAR" if r < 0.15
            else ">=0.45 => ~1.5 NEAR THE CEILING" if r >= 0.45
            else "0.15-0.45 => INTERMEDIATE, letter names no verdict here")
    print(f"  interim band    : r={r:+.3f} -> {band}")
    print(f"  -- POWER, the question actually asked --")
    for rho in (0.15, 0.30, 0.45):
        print(f"     power to reject rho=0 if TRUE rho={rho:.2f}: {power_at(rho,n)*100:5.1f}%")
    print(f"     CI WIDTH = {hi-lo:.3f} — spans {'BOTH' if (lo<0.15 and hi>=0.45) else 'not both'} bands")
