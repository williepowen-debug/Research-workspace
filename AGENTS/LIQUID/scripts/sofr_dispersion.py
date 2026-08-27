#!/usr/bin/env python3
"""SOFR dispersion — drift-robust successor to the dead `SOFR75-IORB >= 0` band.

WHY THIS EXISTS (KB-LIQ-106, 2026-08-27)
  The registered line "SOFR75-IORB >= 0 on 3 consecutive non-quarter-end days = broad
  pressure" was cleared by the MEDIAN DAY of 2026 and had been continuously satisfied for
  27 sessions while STATUS reported "1 print, needs 3". It did not die of bad construction
  -- it was ALIVE and never crossed at all in 2021-22 -- it died of a five-year REGIME
  MIGRATION (share of non-q-end days >= 0bp, by year: 0.0 / 0.0 / 7.6 / 32.9 / 55.6 / 89.5).

  ==> A DRIFTING SERIES HAS NO STATIONARY PERCENTILE. Any fixed replacement band (I had
  proposed p90/p95/p99 = +9/+13/+24 and withdrew it) re-dies on the same schedule.

DESIGN, and the one trap it is built to avoid
  Two questions must be answered SEPARATELY, because each is blind to the other:
    (1) DEVIATION  "is today unusual FOR THE CURRENT REGIME?"   -> robust rolling z-score
    (2) DRIFT      "is the REGIME ITSELF moving, and how fast?"  -> slope of the median
  A z-score ALONE would have hidden the exact finding that motivated this file: a slow
  sustained migration normalises into the rolling baseline and reads z~0 forever. A slope
  ALONE is blind to an acute one-day dislocation. Reporting one without the other rebuilds
  the failure in a new place, so both are always emitted.

  Robust stats (median / MAD) not mean/std: the series retains fat tails even after the
  quarter-end filter, and one +39bp print should not widen the band that judges it.

BASIS
  FRED SOFR75, SOFR, IORB. Pair is IORB-limited (IORB starts 2021-07-29; SOFR75 goes back
  to 2018-04-03 but IOER-vs-IORB is a basis splice and is NOT done here).
  Quarter-end windows (+/-4d around Mar/Jun/Sep/Dec ends and the first 3d of the next
  quarter) are EXCLUDED from every statistic -- Q-end turns print wide mechanically.

READ THE OUTPUT AS
  level  = where the 75th percentile sits vs the IORB ceiling, today (the raw datum)
  z      = deviation from the trailing regime      -> ACUTE stress candidate
  slope  = bp/yr the regime itself is moving       -> STRUCTURAL tightening/easing
Neither number alone is a verdict. Bands below are BASE-RATED (see --baserate), not guessed.
"""
import sys, statistics
from datetime import date, timedelta

WIN_Z     = 250   # trailing non-q-end sessions defining "the current regime"
WIN_SLOPE = 60    # sessions in each median used for the slope endpoints
QE_PAD    = 4

def is_qe(d):
    for m, last in ((3, 31), (6, 30), (9, 30), (12, 31)):
        if abs((d - date(d.year, m, last)).days) <= QE_PAD:
            return True
    for m in (1, 4, 7, 10):
        if 0 <= (d - date(d.year, m, 1)).days <= 3:
            return True
    return False

def _mad_sigma(xs):
    """Robust scale: 1.4826 * MAD. Returns None if degenerate (all-identical window)."""
    if len(xs) < 10:
        return None
    med = statistics.median(xs)
    mad = statistics.median([abs(x - med) for x in xs])
    s = 1.4826 * mad
    return s if s > 1e-9 else None

def analyze(pairs):
    """pairs: [(date, spread_bp)] ascending, ALREADY quarter-end filtered.
    Returns dict or None if too short. Pure -- no IO, no fetch (so --selftest can drive it)."""
    if len(pairs) < WIN_Z + WIN_SLOPE:
        return None
    vals = [v for _, v in pairs]
    cur, cur_date = vals[-1], pairs[-1][0]

    base = vals[-(WIN_Z + 1):-1]                 # trailing regime, EXCLUDING today
    med, sig = statistics.median(base), _mad_sigma(base)
    z = None if sig is None else (cur - med) / sig

    recent = statistics.median(vals[-WIN_SLOPE:])
    older  = statistics.median(vals[-(WIN_Z + WIN_SLOPE):-WIN_Z])
    slope  = (recent - older) * (252.0 / WIN_Z)   # bp per ~year

    return {"date": cur_date, "level": cur, "regime_median": med, "sigma": sig,
            "z": z, "slope_bp_yr": slope, "recent_med": recent, "older_med": older, "n": len(pairs)}

# ---------------------------------------------------------------------------
# BANDS. Every number below is BASE-RATED on the realised distribution, not chosen.
# Re-run `--baserate` after ANY edit here; the printed fire rates ARE the argument.
# Measured 2026-08-27 over 781 gradeable sessions (2022-12-09 -> obs 2026-08-26):
#   z >= 3.0 -> 10.37%   z >= 4.0 -> 4.87%   z >= 6.0 -> 1.28%
# Chosen so YELLOW is a look-at-it prompt, ORANGE is uncommon, RED is rare enough to route.
Z_YELLOW, Z_ORANGE, Z_RED = 3.0, 4.0, 6.0

# NOTE ON THE SLOPE — deliberately NOT banded.
# |slope| has a MEDIAN of 4.03bp/yr, so any binary "regime is moving" flag fires on most
# days: my first cut (>=4.0) fired 60.8% of sessions. That is the same dead-band failure
# this file exists to replace, rebuilt one level up. So the slope is reported as a VALUE
# plus its own percentile and never as an alert. The instrument therefore makes no
# un-base-rated claim anywhere. Percentiles measured with the fire rates above:
SLOPE_PCTL = [(4.03, 50), (6.05, 75), (7.06, 85), (8.06, 90), (10.08, 95), (11.09, 99)]

def slope_pctl(sl):
    """Percentile of |slope| against its own realised history. Context, not a threshold."""
    a = abs(sl)
    p = 0
    for cut, pc in SLOPE_PCTL:
        if a >= cut:
            p = pc
    return p

def classify(a):
    """DEVIATION drives the marker (base-rated). DRIFT is always reported, never banded."""
    if a is None:
        return "\u26aa", "insufficient history"
    z, sl = a["z"], a["slope_bp_yr"]
    if z is None:
        mk, note = "\u26aa", "degenerate scale (flat window) \u2014 no deviation read"
    elif z >= Z_RED:
        mk, note = "\U0001f534", f"z {z:+.1f} \u2014 ACUTE vs trailing regime (median {a['regime_median']:+.0f}bp)"
    elif z >= Z_ORANGE:
        mk, note = "\U0001f7e0", f"z {z:+.1f} \u2014 elevated vs trailing regime (median {a['regime_median']:+.0f}bp)"
    elif z >= Z_YELLOW:
        mk, note = "\U0001f7e1", f"z {z:+.1f} \u2014 mildly elevated vs trailing regime"
    elif z <= -Z_ORANGE:
        mk, note = "\U0001f7e1", f"z {z:+.1f} \u2014 unusually EASY vs trailing regime"
    else:
        mk, note = "\U0001f7e2", f"z {z:+.1f} \u2014 ordinary for the current regime"
    d = "tightening" if sl > 0 else "easing"
    drift = f"regime {d} {sl:+.1f}bp/yr (p{slope_pctl(sl)} of its own history)"
    return mk, f"{note} \u00b7 {drift}"

# ---------------------------------------------------------------- data / cli
def _load():
    sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parents[3]
                          / "FORGE" / "tools" / "market-data"))
    from fetch import fred_fetch
    s75 = {o["date"]: o["value"] for o in fred_fetch("SOFR75", limit=5000)}
    ior = {o["date"]: o["value"] for o in fred_fetch("IORB",   limit=5000)}
    out = []
    for d in sorted(set(s75) & set(ior)):
        try:
            dd = date.fromisoformat(d)
            if is_qe(dd):
                continue
            out.append((dd, (float(s75[d]) - float(ior[d])) * 100))
        except (ValueError, TypeError):
            continue
    return out

def selftest():
    """Falsify the instrument before trusting it (the guard's own v1 fails on first run)."""
    ok = True
    def chk(label, got, want):
        nonlocal ok
        good = (got == want) if not isinstance(want, float) else abs(got - want) < 1e-6
        print(f"  {'PASS' if good else 'FAIL'}  {label}: got {got!r} want {want!r}")
        ok = good and ok
    d0 = date(2022, 1, 3)
    days = [d0 + timedelta(days=i) for i in range(WIN_Z + WIN_SLOPE + 10)]
    # 1) a FLAT series must read z~0 and slope 0 -- and must not crash on zero scale
    flat = [(d, 5.0) for d in days]
    a = analyze(flat)
    chk("flat: slope==0", round(a["slope_bp_yr"], 6), 0.0)
    chk("flat: sigma degenerate -> z None", a["z"], None)
    chk("flat: classify is neutral", classify(a)[0], "⚪")
    # 2) a pure RAMP must show slope>0 while z stays modest -- THE failure mode that
    #    motivated this file: drift must NOT hide inside the rolling baseline.
    ramp = [(d, i * 0.1) for i, d in enumerate(days)]
    a2 = analyze(ramp)
    chk("ramp: slope positive", a2["slope_bp_yr"] > 5, True)
    chk("ramp: drift is REPORTED not normalised away", "tightening" in classify(a2)[1].lower(), True)
    # the ramp must ALSO not scream on z — drift is not deviation, and conflating them
    # is exactly how a slow migration got missed for five years.
    chk("ramp: z stays sub-RED (drift != deviation)", a2["z"] < Z_RED, True)
    # 3) a flat series with ONE spike must read acute on z
    spike = [(d, 5.0 + (i % 7) * 0.3) for i, d in enumerate(days)]
    spike[-1] = (spike[-1][0], 40.0)
    a3 = analyze(spike)
    chk("spike: z is acute", a3["z"] > Z_RED, True)
    # 4) quarter-end filter actually excludes
    chk("qe filter: 2026-06-30 excluded", is_qe(date(2026, 6, 30)), True)
    chk("qe filter: 2026-08-26 kept",     is_qe(date(2026, 8, 26)), False)
    # 5) too-short input returns None rather than a wrong number
    chk("short input -> None", analyze(flat[:20]), None)
    print("\nSELFTEST", "PASS" if ok else "FAIL")
    return 0 if ok else 1

def baserate():
    """Print the REALISED fire rate of every band. Run this before trusting any line."""
    p = _load()
    fires = {"🟡": 0, "🟠": 0, "🔴": 0}
    slopes = []
    n = 0
    for i in range(WIN_Z + WIN_SLOPE, len(p) + 1):
        a = analyze(p[:i])
        if not a or a["z"] is None:
            continue
        n += 1
        if a["z"] >= Z_RED: fires["🔴"] += 1
        elif a["z"] >= Z_ORANGE: fires["🟠"] += 1
        elif a["z"] >= Z_YELLOW: fires["🟡"] += 1
        slopes.append(abs(a["slope_bp_yr"]))
    print(f"BASE RATE over {n} gradeable sessions ({p[WIN_Z+WIN_SLOPE-1][0]} -> {p[-1][0]}):")
    for k in ("🟡", "🟠", "🔴"):
        print(f"  {k} z-band fires : {fires[k]:4d}/{n} = {100*fires[k]/n:5.2f}%")
    slopes.sort()
    qs = lambda pc: slopes[min(len(slopes)-1, int(pc/100*len(slopes)))]
    print(f"  |slope| p50 {qs(50):.2f} · p75 {qs(75):.2f} · p85 {qs(85):.2f} · p90 {qs(90):.2f} · p95 {qs(95):.2f} bp/yr")
    print("  (slope is NOT banded — reported as value+percentile; a >=4bp/yr flag fired 60.8% of days)")
    print("\n  A band that fires on most days is dead. That is what this replaces —")
    print("  so these numbers, not the design, are the argument for the bands.")
    return 0

def main():
    if "--selftest" in sys.argv: return selftest()
    if "--baserate" in sys.argv: return baserate()
    p = _load()
    a = analyze(p)
    mk, note = classify(a)
    if a is None:
        print("⚪ SOFR dispersion — insufficient history"); return 0
    print(f"{mk} SOFR75-IORB  {a['level']:+.0f}bps  [{a['date']}]   {note}")
    print(f"   regime median {a['regime_median']:+.1f}bp (trailing {WIN_Z} non-q-end sessions), "
          f"scale {a['sigma']:.1f}bp" if a['sigma'] else "   scale degenerate")
    print(f"   regime drift  {a['older_med']:+.1f}bp -> {a['recent_med']:+.1f}bp "
          f"= {a['slope_bp_yr']:+.1f}bp/yr")
    return 0

if __name__ == "__main__":
    sys.exit(main())
