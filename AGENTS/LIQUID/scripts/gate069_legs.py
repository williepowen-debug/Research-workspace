#!/usr/bin/env python3
"""
LIQUID — GATE-LIQ-069 (AI-HY cohort re-arm) leg instrumentation.

Registry letter: "ANY ONE of 5 legs: BB>220-while-CCC-flat · CoreWeave 5Y CDS re-widen
>100bp · AI-infra HY new-issue concessions widening · cohort equity (CRWV,IREN,APLD,NBIS)
-15%/session w/ credit underperforming · ORCL fallen-angel ladder."

This tool grades L1 and L4. L2 is graded by `scripts/crwv_cds_grade.py` (DTCC PPD converted
quotes; FIRED 2026-09-26). L3 is NO_INSTRUMENT. L5 is ratings, SECONDARY-SOURCED: its primary
re-verification was re-registered NO_INSTRUMENT by DOCKET L345 on 2026-09-29.

L1/L4 sub-thresholds are ADOPTED LETTER (WQ-114, Will-ruled 2026-09-01, prospective from 9/1):
"CCC flat" = |5-session CCC OAS change| <= 15bp · "credit underperforming" = HY OAS >= +5bp on
the session. (Until 2026-09-29 this file still called them "PROPOSED, not adopted": CATO 9/29.)

⛔ SESSION SELECTION, 2026-09-29 (CATO 9/29 counterexample, runs/2026-09-29_0853_liquid-gate069-probe.py):
the previous version took BOTH the L4 equity session and the HY session change from the dates
COMMON to BB, CCC and HY. One missing CCC observation (a series L4 never reads) therefore dropped
a date from the intersection and silently stretched the "session" across TWO days: two -10% / +3bp
days became one -19% / +6bp "session" and L4 printed FIRED. Each leg now reads ITS OWN series:
L4's HY change comes from HY's own consecutive published obs, each stock's change from that stock's
own previous bar, and the two "previous" dates MUST be equal or the leg fails CLOSED.
Run `--selftest` (offline) before trusting a change here.
"""
import sys, argparse

CCC_FLAT_BP = 15      # WQ-114 letter: |CCC 5-session change| <= 15bp == "flat"
CRED_UNDER_BP = 5     # WQ-114 letter: HY OAS widened >= 5bp on the session == "credit underperforming"
BB_LINE = 220
EQ_LINE = -15.0
TICK = ["CRWV", "IREN", "APLD", "NBIS"]


def grade_l1(bb, ccc):
    """PURE. bb/ccc = {date: bp}. L1 = BB > 220 while CCC flat, on ONE observation date.
    CCC's 5-session change is taken on CCC's OWN published observations."""
    if not bb or not ccc:
        return {"state": "INSTRUMENT-FAULT", "why": "BB or CCC series empty"}
    lb, lc = max(bb), max(ccc)
    if lb != lc:
        return {"state": "INSTRUMENT-FAULT", "why": f"latest BB {lb} != latest CCC {lc}; not one observation"}
    cd = sorted(ccc)
    if len(cd) < 6:
        return {"state": "INSTRUMENT-FAULT", "why": "fewer than 6 CCC observations"}
    chg = ccc[cd[-1]] - ccc[cd[-6]]
    bb_hit, flat = bb[lb] > BB_LINE, abs(chg) <= CCC_FLAT_BP
    return {"state": "FIRED" if (bb_hit and flat) else "NOT FIRED", "obs": lb, "bb": bb[lb],
            "ccc": ccc[lc], "ccc_chg": chg, "ccc_from": cd[-6], "bb_hit": bb_hit, "flat": flat}


def grade_l4(hy, eq):
    """PURE. hy = {date: bp}; eq = {ticker: {date: raw close}}. L4 = ANY ONE cohort name <= -15% on
    the session AND HY OAS >= +5bp on the SAME session. The session is HY's latest published obs
    and its OWN previous obs; every stock must have bars on exactly those two dates as ITS latest
    bar at-or-before the session and ITS previous bar. Any mismatch => INSTRUMENT-FAULT, never a grade."""
    hd = sorted(hy)
    if len(hd) < 2:
        return {"state": "INSTRUMENT-FAULT", "faults": ["fewer than 2 HY observations"], "rows": []}
    last, hprev = hd[-1], hd[-2]
    hy_chg = hy[last] - hy[hprev]
    faults, rows, worst = [], [], None
    for t in TICK:
        c = eq.get(t)
        if not c:
            faults.append(f"{t} no series"); continue
        if last not in c:
            faults.append(f"{t} bar missing for {last}"); continue
        before = [d for d in c if d < last]
        if not before:
            faults.append(f"{t} no bar before {last}"); continue
        ep = max(before)
        if ep != hprev:
            faults.append(f"{t} session mismatch: equity prev bar {ep} vs HY prev obs {hprev}"); continue
        chg = (c[last] / c[ep] - 1) * 100
        rows.append((t, c[last], chg, ep))
        if worst is None or chg < worst[1]:
            worst = (t, chg)
    newer = sorted({d for c in eq.values() if c for d in c if d > last})
    out = {"last": last, "hprev": hprev, "hy_chg": hy_chg, "rows": rows, "faults": faults,
           "worst": worst, "newer": newer, "cr": hy_chg >= CRED_UNDER_BP}
    if faults:
        out["state"] = "INSTRUMENT-FAULT"
    else:
        out["state"] = "FIRED" if (worst[1] <= EQ_LINE and out["cr"]) else "NOT FIRED"
    return out


def selftest():
    """Offline. Includes CATO's 9/29 counterexample as a permanent regression case."""
    ok = True
    def check(label, got, want):
        nonlocal ok
        ok &= got == want
        print(f"  {'✓' if got == want else '✗'} {label}: got {got!r}, want {want!r}")
    D = ["2026-09-16", "2026-09-17", "2026-09-18", "2026-09-21", "2026-09-22", "2026-09-23", "2026-09-24", "2026-09-25"]
    hy = {d: {"2026-09-24": 273.0, "2026-09-25": 276.0}.get(d, 270.0) for d in D}
    px = {d: {"2026-09-24": 90.0, "2026-09-25": 81.0}.get(d, 100.0) for d in D}   # two consecutive -10% days
    eq = {t: dict(px) for t in TICK}
    r = grade_l4(hy, eq)
    check("complete data: -10%/+3bp → NOT FIRED", (r["state"], round(r["worst"][1], 2), r["hy_chg"]), ("NOT FIRED", -10.0, 3.0))
    # CATO counterexample: an unrelated CCC gap must not touch L4 at all (L4 never reads CCC)
    ccc_gap = {d: 800.0 for d in D if d != "2026-09-24"}
    r = grade_l4(hy, eq)
    check("CATO: CCC missing 9/24 cannot stretch the L4 session", (r["state"], r["hprev"]), ("NOT FIRED", "2026-09-24"))
    # missing HY 9/24 itself: HY's own prev is 9/23; equity prev is 9/24 -> mismatch, fail closed
    hy_gap = {d: v for d, v in hy.items() if d != "2026-09-24"}
    r = grade_l4(hy_gap, eq)
    check("HY obs missing → session mismatch → INSTRUMENT-FAULT (never a stretched grade)",
          (r["state"], any("session mismatch" in f for f in r["faults"])), ("INSTRUMENT-FAULT", True))
    # missing equity bar on the session
    eq_gap = {t: {d: v for d, v in px.items() if d != "2026-09-25"} for t in TICK}
    check("equity bar missing on the session → INSTRUMENT-FAULT", grade_l4(hy, eq_gap)["state"], "INSTRUMENT-FAULT")
    # a genuine fire: one name -16% and HY +5 on the same session
    eq_fire = {t: dict(px) for t in TICK}; eq_fire["CRWV"]["2026-09-25"] = 90.0 * 0.84
    hy_fire = dict(hy); hy_fire["2026-09-25"] = 278.0
    check("one name -16% with HY +5bp same session → FIRED", grade_l4(hy_fire, eq_fire)["state"], "FIRED")
    check("HY +4bp (under the ≥5 line) → NOT FIRED", grade_l4({**hy_fire, "2026-09-25": 277.0}, eq_fire)["state"], "NOT FIRED")
    check("exactly -15.00% is <= -15 → FIRED", grade_l4(hy_fire, {**eq_fire, "CRWV": {**px, "2026-09-25": 90.0 * 0.85}})["state"], "FIRED")
    # L1
    bb = {d: 230.0 for d in D}; ccc = {d: 800.0 for d in D}
    check("L1: BB 230 + CCC flat → FIRED", grade_l1(bb, ccc)["state"], "FIRED")
    check("L1: CCC +16 over 5 sessions → NOT FIRED", grade_l1(bb, {**ccc, "2026-09-25": 816.0})["state"], "NOT FIRED")
    check("L1: CCC latest date missing → FAULT, not a stale-date grade", grade_l1(bb, {d: v for d, v in ccc.items() if d != "2026-09-25"})["state"], "INSTRUMENT-FAULT")
    check("L1: CCC gap mid-window uses CCC's own 6th-latest obs",
          grade_l1(bb, ccc_gap)["ccc_from"], "2026-09-17")
    # DAEDALUS #2 ties, on values as FRED publishes them (percent strings) — through bp(), the read path
    check("tie: BB published 2.20 (=220bp) does NOT meet strict >220",
          grade_l1({d: bp("2.20") for d in D}, {d: bp("8.00") for d in D})["state"], "NOT FIRED")
    check("tie: BB published 2.21 meets >220",
          grade_l1({d: bp("2.21") for d in D}, {d: bp("8.00") for d in D})["state"], "FIRED")
    check("tie: CCC 5-session change of exactly 15bp IS flat (<=)",
          grade_l1({d: bp("2.30") for d in D}, {**{d: bp("8.00") for d in D}, D[-1]: bp("8.15")})["flat"], True)
    hy_tie = {d: bp("2.50") for d in D}; hy_tie[D[-1]] = bp("2.55")
    check("tie: HY 2.50 → 2.55 (+5bp exactly) IS credit underperforming (>=)", grade_l4(hy_tie, eq_fire)["cr"], True)
    print(f"\n  SELFTEST: {'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


def ser(sid, n=30):
    from fetch import fred_fetch
    out = {}
    for x in fred_fetch(sid, limit=n):
        v = x.get("value")
        if v in (".", "", None): continue
        # DAEDALUS #2 precision (2026-09-29): FRED publishes 0.01 pct, i.e. WHOLE bp. Round at read time, once.
        # Unrounded, 2.20*100 = 220.00000000000003 > 220 (a FALSE L1 fire at exactly the line) and
        # 2.55*100 - 2.50*100 = 4.999… < 5 (a MISSED L4 credit leg at exactly +5bp).
        out[x["date"]] = bp(v)
    return out


def bp(pct):
    """FRED percent string/float → whole basis points (exact for 2-decimal published values)."""
    return round(float(pct) * 100)


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--selftest", action="store_true"); a = ap.parse_args()
    if a.selftest:
        return selftest()
    sys.path.insert(0, "FORGE/tools/market-data")
    print("=" * 96)
    print("  GATE-LIQ-069 — L1 / L4 graded here · L2 → scripts/crwv_cds_grade.py · L3 NO_INSTRUMENT · L5 secondary-sourced")
    print(f"  ADOPTED letter (WQ-114, 9/1): 'CCC flat' = |5-sess CCC delta| <= {CCC_FLAT_BP}bp · "
          f"'credit underperforming' = HY OAS +{CRED_UNDER_BP}bp or more on the session")
    print("=" * 96)

    bb, ccc, hy = ser("BAMLH0A1HYBB"), ser("BAMLH0A3HYC"), ser("BAMLH0A0HYM2")
    g1 = grade_l1(bb, ccc)
    print(f"\n  L1  BB>220 while CCC flat")
    if g1["state"] == "INSTRUMENT-FAULT":
        print(f"      => L1 🔴 INSTRUMENT-FAULT — {g1['why']}. NOT graded.")
    else:
        print(f"      BB {g1['bb']:.0f}bps [obs {g1['obs']}] -> BB>220? {'YES' if g1['bb_hit'] else 'NO'}   ({BB_LINE - g1['bb']:+.0f}bp to the line)")
        print(f"      CCC {g1['ccc']:.0f}bps, 5-sess change {g1['ccc_chg']:+.0f}bp (vs {g1['ccc_from']}, CCC's own obs) -> flat? {'YES' if g1['flat'] else 'NO'}")
        print(f"      => L1 {'🔴 FIRED' if g1['state'] == 'FIRED' else '🟢 NOT FIRED'}   (conjunctive; BB is the binding half)")

    print(f"\n  L4  cohort equity -15%/session with credit underperforming (ANY ONE name, WQ-170)")
    # ⚠️ F1 IDENTITY GUARD (KB-LIQ-117): pass a LIST of tickers and verify the returned keys.
    eq, fetch_faults = {}, []
    hd = sorted(hy)
    try:
        import yfinance as yf, warnings; warnings.filterwarnings("ignore")
        px = yf.download(TICK, start=hd[-6] if len(hd) >= 6 else None, end=None, auto_adjust=False, progress=False)["Close"]
        px.index = [i.strftime("%Y-%m-%d") for i in px.index]
        extra = [k for k in px.columns if k not in TICK]
        if extra: fetch_faults.append(f"UNREQUESTED tickers returned {extra} — identity mismatch")
        for t in TICK:
            if t in px.columns:
                eq[t] = {d: float(v) for d, v in px[t].dropna().items()}
    except Exception as e:
        fetch_faults.append(f"fetch failed: {type(e).__name__}")
    g4 = grade_l4(hy, eq)
    faults = fetch_faults + g4["faults"]
    for t, close, chg, ep in g4["rows"]:
        print(f"      {t:<6} {close:>10.2f}  {chg:+.2f}%   [session {g4['last']} vs {ep}, raw close]")
    if g4.get("newer"):
        print(f"      ⏳ equity sessions after the latest HY obs {g4['newer']}: UNGRADEABLE-PENDING-PUBLICATION (not graded)")
    if "hy_chg" in g4:
        print(f"      HY OAS session change {g4['hy_chg']:+.0f}bp [obs {g4['last']} vs {g4['hprev']}, HY's own obs] "
              f"-> credit underperforming? {'YES' if g4['cr'] else 'NO'}")
    if faults:
        # ⛔ NEVER report NOT FIRED off an unmeasured leg — that is the dead-quiet failure.
        print(f"      => L4 🔴 INSTRUMENT-FAULT — {'; '.join(faults)}")
        print(f"         NOT graded. An unmeasured leg is UNMEASURED, never NOT FIRED.")
    else:
        w = g4["worst"]
        print(f"      worst name: {w[0]} {w[1]:+.2f}%  -> <=-15%? {'YES' if w[1] <= EQ_LINE else 'NO'}")
        print(f"      => L4 {'🔴 FIRED' if g4['state'] == 'FIRED' else '🟢 NOT FIRED'}   (conjunctive)")
    print(f"\n  ↪ L2 CoreWeave 5Y CDS  — graded by scripts/crwv_cds_grade.py (DTCC PPD converted quotes; FIRED 9/26)")
    print(f"  ⛔ L3 AI-infra new-issue concessions — NO_INSTRUMENT (dealer/terminal primary)")
    print(f"  ⚠️  L5 ORCL fallen-angel ladder — SECONDARY-SOURCED (≥2 independent outlets); primary re-verification NO_INSTRUMENT (L345, 9/29)")
    print("=" * 96)
    return 0


if __name__ == "__main__":
    # Exit ONLY on a non-zero code: an unconditional sys.exit() ends any harness that runs this file
    # via runpy (CATO's probe) after the first scenario, and the harness then reports rc 0 on
    # nothing — a silent false-clean, caught 2026-09-29.
    _rc = main()
    if _rc:
        sys.exit(_rc)
