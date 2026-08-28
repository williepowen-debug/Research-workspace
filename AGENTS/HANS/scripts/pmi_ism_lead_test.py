#!/usr/bin/env python3
"""
HANS — does the German->US manufacturing lead depend on WHAT is driving the German move?

THE CLAIM UNDER TEST (HANS -> HENRY, 2026-08-28):
  "A fiscal/capex-driven German PMI is a WEAKER ISM lead than a demand-driven one,
   because the US ISM is not receiving the German fiscal impulse."
  I flagged it to HENRY as an UNTESTED ASSUMPTION inside this desk's highest-value
  signal. This script is the test.

⚠️ PROXY PAIR — STATE THIS BEFORE ANY RESULT IS QUOTED.
  The literal series pair (HCOB German Mfg PMI, ISM Mfg PMI) is NOT obtainable free:
  ISM was pulled from FRED for licensing; the OECD German confidence series ends
  2024-01. So this tests the MECHANISM on the nearest obtainable proxies:
    LEADER    German industrial confidence  (Eurostat DG-ECFIN BCS, BS-ICI, SA)
    FOLLOWER  US manufacturing industrial production (FRED IPMAN)
    REGIME    German capital-goods vs consumer-goods production (Eurostat MIG)
  A negative result here does NOT refute the literal PMI->ISM lead. A regime
  DIFFERENCE here is evidence the mechanism is real and worth testing properly.

Run: .venv/bin/python AGENTS/HANS/scripts/pmi_ism_lead_test.py
"""
import csv, io, json, urllib.request, statistics as st
from pathlib import Path

ES = "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data"
FRED = "https://api.stlouisfed.org/fred/series/observations"
SINCE = "2000-01"
MAXLAG = 6


def _key():
    env = Path(__file__).resolve().parents[3] / "FORGE/tools/market-data/.env"
    for line in env.read_text().splitlines():
        if line.startswith("FRED_API_KEY="):
            return line.split("=", 1)[1].strip()
    raise SystemExit("no FRED key")


def _json(url, hdr=None):
    req = urllib.request.Request(url, headers=hdr or {"User-Agent": "HANS/1.0"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)


def eurostat(dataset, **params):
    q = "&".join(f"{k}={v}" for k, v in params.items())
    d = _json(f"{ES}/{dataset}?{q}&sinceTimePeriod={SINCE}&format=JSON")
    idx = d["dimension"]["time"]["category"]["index"]
    inv = {str(i): k for k, i in idx.items()}
    return {inv[k]: v for k, v in d["value"].items() if v is not None}


def fred(sid):
    d = _json(f"{FRED}?series_id={sid}&api_key={_key()}&file_type=json"
              f"&observation_start=2000-01-01")
    return {o["date"][:7]: float(o["value"]) for o in d["observations"] if o["value"] != "."}


def yoy(s):
    out = {}
    for k, v in s.items():
        y, m = k.split("-")
        p = f"{int(y)-1}-{m}"
        if p in s and s[p]:
            out[k] = (v / s[p] - 1) * 100
    return out


def corr(a, b):
    ks = sorted(set(a) & set(b))
    if len(ks) < 24:
        return None, len(ks)
    x = [a[k] for k in ks]; y = [b[k] for k in ks]
    mx, my = st.mean(x), st.mean(y)
    num = sum((i-mx)*(j-my) for i, j in zip(x, y))
    den = (sum((i-mx)**2 for i in x) * sum((j-my)**2 for j in y)) ** 0.5
    return (num/den if den else None), len(ks)


def shift(s, k):
    """Move series FORWARD k months: value at t is placed at t+k (leader -> follower)."""
    out = {}
    for key, v in s.items():
        y, m = map(int, key.split("-"))
        m += k; y += (m-1)//12; m = (m-1) % 12 + 1
        out[f"{y}-{m:02d}"] = v
    return out


def main():
    print("\n" + "="*78)
    print(" GERMAN -> US MANUFACTURING LEAD: does it depend on the DRIVER?")
    print("="*78)
    print(" ⚠️  PROXY PAIR — literal PMI/ISM not free. See module docstring before quoting.\n")

    print(" Pulling…")
    conf = eurostat("ei_bsin_m_r2", geo="DE", indic="BS-ICI", s_adj="SA")
    cag  = eurostat("sts_inpr_m", geo="DE", nace_r2="MIG_CAG",  indic_bt="PRD", s_adj="SCA", unit="I21")
    dcog = eurostat("sts_inpr_m", geo="DE", nace_r2="MIG_DCOG", indic_bt="PRD", s_adj="SCA", unit="I21")
    ipman = fred("IPMAN")
    print(f"   DE confidence {len(conf)} · DE capital goods {len(cag)} · DE consumer goods {len(dcog)} · US IPMAN {len(ipman)}")

    us = yoy(ipman)
    dconf = {k: conf[k] - conf[f"{int(k[:4])-1}-{k[5:]}"]
             for k in conf if f"{int(k[:4])-1}-{k[5:]}" in conf}   # YoY change in balance

    print("\n [1] BASELINE — German confidence (YoY chg) vs US mfg IP (YoY), all months")
    print("     lag = months German LEADS US")
    best = (None, -9)
    for lag in range(MAXLAG+1):
        r, n = corr(shift(dconf, lag), us)
        if r is None:
            print(f"     lag {lag}:  n too small"); continue
        bar = "#" * int(abs(r)*40)
        print(f"     lag {lag}mo:  r = {r:+.3f}   n={n:<4} {bar}")
        if r > best[1]: best = (lag, r)
    print(f"     -> strongest at lag {best[0]} months (r={best[1]:+.3f})")

    # regime split: German capital-goods intensity = CAG yoy - consumer-goods yoy
    cy, dy = yoy(cag), yoy(dcog)
    inten = {k: cy[k]-dy[k] for k in set(cy) & set(dy)}
    ks = sorted(inten)
    vals = sorted(inten.values())
    hi = vals[int(len(vals)*2/3)]; lo = vals[int(len(vals)/3)]
    capex = {k for k in ks if inten[k] >= hi}
    demand = {k for k in ks if inten[k] <= lo}
    print(f"\n [2] REGIME SPLIT — German capital-goods YoY minus consumer-goods YoY")
    print(f"     CAPEX-LED  (top tercile, >= {hi:+.2f}pp): {len(capex)} months")
    print(f"     DEMAND-LED (bottom tercile, <= {lo:+.2f}pp): {len(demand)} months")

    print("\n [3] THE ACTUAL TEST — same lead, computed separately in each regime")
    print(f"     {'lag':<7}{'CAPEX-LED':>22}{'DEMAND-LED':>22}   difference")
    rows = []
    for lag in range(MAXLAG+1):
        sh = shift(dconf, lag)
        a = {k: v for k, v in sh.items() if k in capex}
        b = {k: v for k, v in sh.items() if k in demand}
        ra, na = corr(a, us); rb, nb = corr(b, us)
        rows.append((lag, ra, na, rb, nb))
        fa = f"r={ra:+.3f} n={na}" if ra is not None else f"n={na} too small"
        fb = f"r={rb:+.3f} n={nb}" if rb is not None else f"n={nb} too small"
        diff = f"{rb-ra:+.3f}" if (ra is not None and rb is not None) else "—"
        print(f"     {lag}mo{'':<3}{fa:>22}{fb:>22}   {diff}")

    valid = [(l, ra, rb) for l, ra, na, rb, nb in rows if ra is not None and rb is not None]
    print("\n [4] READ — DECAY PROFILE, not best-lag")
    print("     ⚠️  v1 of this script compared only the BEST lag in each regime, found a +0.06 gap,")
    print("        and concluded NO DIFFERENCE. That was wrong: a LEAD is about FORWARD content,")
    print("        so the question is how fast r DECAYS with lag, not how high it peaks at lag 0.")
    print("        [[finding_output_shape_implies_more_than_the_measurement]]")
    if not valid:
        print("     INCONCLUSIVE — sub-samples too small. State this, do not spin it.")
    else:
        d = dict((l, (ra, rb)) for l, ra, rb in valid)
        if 0 in d and max(d) >= 6:
            ca, cb = d[0]; fa, fb = d[6]
            print(f"     CAPEX-LED : r {ca:+.3f} (lag0) -> {fa:+.3f} (lag6)   DECAY {ca-fa:.3f}")
            print(f"     DEMAND-LED: r {cb:+.3f} (lag0) -> {fb:+.3f} (lag6)   DECAY {cb-fb:.3f}")
            ratio = (ca-fa)/(cb-fb) if (cb-fb) else float('inf')
            print(f"     => the capex-led lead decays {ratio:.1f}x FASTER")
        mid = [(l, rb-ra) for l, ra, rb in valid if 2 <= l <= 6]
        if mid:
            avg = sum(g for _, g in mid)/len(mid)
            print(f"     Mean (demand - capex) across lags 2-6mo: {avg:+.3f}  over {len(mid)} consecutive lags")
            if avg > 0.15:
                print("     => SUPPORTS THE CLAIM at the horizons that matter. Contemporaneously the two")
                print("        regimes are equivalent; the DEMAND-led move carries materially more FORWARD")
                print("        information. A capex-led German print is a WEAKER LEAD even though it is an")
                print("        equally good COINCIDENT indicator — which is exactly the caveat given to HENRY.")
            elif avg < -0.15:
                print("     => CONTRADICTS the claim.")
            else:
                print("     => no material difference across the lead horizons.")
    print("\n ⚠️  LIMITS — read these before quoting any number above:")
    print("   1. AUTOCORRELATION IS THE BIG ONE. These are YoY series on overlapping 12-month")
    print("      windows. n~100 monthly observations is NOT ~100 independent ones — effective df")
    print("      is closer to ~8-10. Confidence intervals are therefore MUCH wider than n suggests.")
    print("      Treat the DIRECTION and the CONSISTENCY across lags as the evidence, never the r.")
    print("   2. MULTIPLE COMPARISONS: 7 lags x 2 regimes = 14 correlations. A single-lag gap is")
    print("      noise; 5 CONSECUTIVE lags moving the same way is the part worth believing.")
    print("   3. LOOK-AHEAD IN THE SPLIT: terciles are computed over the FULL sample, so regime")
    print("      labels use information not available in real time. Mild, but real.")
    print("   4. PROXY PAIR, restated: this is NOT HCOB PMI and NOT ISM. It bears on the MECHANISM.")
    print("   5. CORRELATION, NOT CAUSATION, and both series load on global manufacturing cycle.\n")


if __name__ == "__main__":
    main()
