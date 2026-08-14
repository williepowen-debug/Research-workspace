#!/usr/bin/env python3
"""
SEVERITY-DIVERGENCE TEST (SDT) — the Secondary-thesis ("Invisible Exit") falsifier.

WHY THIS EXISTS
---------------
The Secondary thesis's previous falsifier was:

    "Q2 2026 NY Fed HDC shows auto transition-to-90+ accelerating in line with
     ABS-level stress"

That test RAN on 2026-08-11 and did not fire — but the finding that mattered was
that **it never could have fired in the confirming direction.** A skip cohort
measured in tens of thousands of loans cannot move a $1.713T national aggregate.
It could only ever fail-to-contradict. A one-sided instrument is not a test, and
carrying one is how a thesis becomes quietly unfalsifiable.
(auto-memory: finding_cohort_too_small_to_move_the_index)

This replaces it with a test measured INSIDE the pools where the cohort sits, at
a magnitude that clears a measured noise floor, and with a REFUTE branch that can
actually fire.

THE DISCRIMINATOR
-----------------
Separate FREQUENCY from SEVERITY. They respond differently to the two competing
explanations, which is the whole point:

    ordinary credit deterioration  ->  MORE defaults      (frequency UP)
                                       same collateral     (severity FLAT)

    skip-default / Invisible Exit  ->  vehicle is GONE     (severity UP)
                                       no 30/60/90 roll    (frequency FLAT)

So the joint condition **severity rising while frequency is flat** is the
mechanical fingerprint of skip. Ordinary credit deterioration CANNOT produce it:
more bad borrowers necessarily means more delinquency.

    Severity  S = 100 - recovery_pct     (loss given default, pp)
    Frequency F = dq_60plus_pct          (60+ delinquency, pp)

INSTRUMENT (named in full — a claim that names no instrument gets graded on
whatever number is in front of the reader; see OTTO-10, 2026-08-14)
------------------------------------------------------------------
  source     SEC EDGAR Form 10-D, Exhibit 99.1 monthly servicer reports
  issuer     Exeter Finance (EART shelf) ONLY
             *** Exeter is the ONLY public subprime shelf that discloses a
             recovery rate. Verified 2026-08-14 against the panel: exeter 20/20
             rows carry recovery, santander 0/15, bridgecrest 0/10. Severity is
             therefore unobservable for SDART and BLAST, and no cross-issuer
             control on severity is available. ***
  deals      EART 2022-2, 2022-3, 2023-1, 2024-1
  fields     recovery_pct (severity), dq_60plus_pct (frequency)
  unit       percentage points. recovery = % of defaulted balance recovered;
             dq_60plus = % of CURRENT pool balance. DIFFERENT DENOMINATORS —
             never combine them into one ratio, only compare their CHANGES.
  cadence    monthly (Exeter files ~end of month)
  ledger     workbook/PANEL_10D.tsv  (written by scripts/panel_10d.py)
  control    Manheim Used Vehicle Value Index, YoY % — the common-mode driver of
             recovery. A used-car crash lowers recovery for every pool with no
             skip involved at all, so an uncontrolled severity move is
             uninterpretable. (auto-memory: finding_spread_metric_blind_to_common_mode)

BASE RATE — measured BEFORE the thresholds were chosen, not after
-----------------------------------------------------------------
Pooled monthly recovery SD across the four Exeter deals (2026-03..07) = 2.12 pp.
Baseline blended recovery R0 = 27.05%.

    window n   SE of mean   2*SE      min detectable skip-share change
         5        0.95      1.90                  7.0%
        12        0.61      1.23                  4.5%
        24        0.43      0.87                  3.2%

A skip share s among defaults drags blended recovery to R0*(1-s), so a 2.0pp
recovery move == a ~7.4pp change in the skip share of defaults. That is the
magnitude this test is tuned to see. BELOW the floor it returns NO VERDICT
rather than a false negative — an effect under the detection floor is no
evidence, not weak evidence. (auto-memory: finding_effect_below_instrument_detection_floor)

PRE-REGISTERED VERDICT BOUNDARY — numbers, with an explicit NO-VERDICT band
--------------------------------------------------------------------------
Window: WINDOW_MONTHS consecutive monthly filings, >= MIN_DEALS deals reporting
both fields at both ends.

  CONFIRM   panel-mean dS >= +2.00 pp  AND  panel-mean dF <= +0.50 pp
            AND |Manheim YoY| <= 3.0%
            => severity rose materially while delinquency did not. Skip channel
               growing. Secondary thesis SUPPORTED.

  REFUTE    panel-mean dS <= +0.50 pp  AND  panel-mean dF >= +1.00 pp
            AND |Manheim YoY| <= 3.0%
            => deterioration is arriving as ordinary delinquency at stable
               collateral severity. The Invisible-Exit channel is NOT what is
               driving losses. Secondary thesis WEAKENED.

  NO VERDICT  everything else, including: fewer than MIN_DEALS deals; fewer than
              WINDOW_MONTHS observations; |Manheim YoY| > 3% (common-mode
              contaminated IN EITHER DIRECTION — a crash fakes a CONFIRM by depressing
              recovery, a rally fakes a REFUTE by lifting it and masking skip growth).

THE REFUTE BRANCH IS THE POINT. It fires on a common, plausible world-state, and
it is what the NY Fed test lacked.

SCOPE LIMIT — STATED UP FRONT, NOT BURIED
-----------------------------------------
Exeter is deep subprime. It is NOT known to be immigrant-concentrated. This test
measures the MECHANISM (collateral-less default), NOT the COHORT. Tricolor's own
deals were 144A with no public performance reporting, so the cohort-identified
test is GENUINELY IMPOSSIBLE with public data — not merely unfetched.
(auto-memory: finding_unfetched_is_not_unavailable — classified, and this one is
genuinely unavailable.)

=> A CONFIRM supports "skip-type loss is growing in deep subprime," which is the
   mechanism's fingerprint. It does NOT by itself establish the immigrant
   channel. Do not report it as if it does.

Usage:
    .venv/bin/python3 AGENTS/OTTO/scripts/severity_divergence.py
    ... --window 12       override the window length
    ... --manheim -1.8    supply the Manheim YoY reading for the window
    ... --self-test       run the positive control only
"""
import csv
import statistics as S
import sys
from pathlib import Path

OTTO = Path(__file__).resolve().parent.parent
LEDGER = OTTO / "workbook" / "PANEL_10D.tsv"

DEALS = ["EART 2022-2", "EART 2022-3", "EART 2023-1", "EART 2024-1"]
WINDOW_MONTHS = 12
MIN_DEALS = 3

CONFIRM_DS, CONFIRM_DF = 2.00, 0.50
REFUTE_DS,  REFUTE_DF  = 0.50, 1.00
MANHEIM_BAND = 3.0   # two-sided: |Manheim YoY| > this => common-mode contaminated


def num(x):
    try:
        return float(str(x).strip())
    except (TypeError, ValueError):
        return None


def load():
    """Read the panel, dedup on (deal, filing_date) keeping the LAST row."""
    if not LEDGER.exists():
        return {}
    rows = list(csv.DictReader(LEDGER.open(encoding="utf-8"), delimiter="\t"))
    seen = {}
    for r in rows:
        if r.get("status") not in (None, "", "OK"):
            continue                                   # never score an INVALID run
        seen[(r["deal"], r["filing_date"])] = r
    out = {}
    for (deal, fdate), r in seen.items():
        s, f = num(r.get("recovery_pct")), num(r.get("dq_60plus_pct"))
        if s is None or f is None:
            continue                                   # severity unobservable -> excluded
        out.setdefault(deal, []).append((fdate, 100.0 - s, f))
    for d in out:
        out[d].sort()
    return out


def self_test():
    """
    POSITIVE CONTROL — tests the ARITHMETIC, never the WORLD.

    The s017 lesson, in this script's own design: the 10-D panel's original
    control pinned a fixed value and compared it against WHATEVER THE NEWEST
    FILING RETURNED, so the arrival of new data — the one event the instrument
    exists to detect — necessarily failed the control. This control instead
    feeds SYNTHETIC series with known answers through the real verdict function.
    It must keep passing forever; if it fails, the code changed, not the market.
    """
    cases = [
        # name,               dS,    dF,   manheim, expected
        ("clean CONFIRM",     3.00,  0.10,   0.0,   "CONFIRM"),
        ("clean REFUTE",      0.10,  2.00,   0.0,   "REFUTE"),
        ("boundary dS just under CONFIRM", 1.99, 0.10, 0.0, "NO VERDICT"),
        ("boundary dF just over CONFIRM",  3.00, 0.51, 0.0, "NO VERDICT"),
        ("both move (ambiguous)",          3.00, 2.00, 0.0, "NO VERDICT"),
        ("CONFIRM shape but Manheim crash", 3.00, 0.10, -8.0, "NO VERDICT"),
        ("REFUTE shape but Manheim rally",  0.10, 2.00,  8.0, "NO VERDICT"),
        ("Manheim just inside band",        0.10, 2.00,  2.9, "REFUTE"),
        ("Manheim just outside band",       0.10, 2.00,  3.1, "NO VERDICT"),
        ("nothing moves",                  0.10, 0.10,  0.0, "NO VERDICT"),
    ]
    ok = True
    print("  POSITIVE CONTROL (synthetic — tests the arithmetic, not the world)")
    for name, ds, df, man, exp in cases:
        got = verdict(ds, df, man, n_deals=4, n_months=WINDOW_MONTHS)[0]
        flag = "ok " if got == exp else "FAIL"
        if got != exp:
            ok = False
        print(f"    [{flag}] {name:<34} dS={ds:+5.2f} dF={df:+5.2f} manheim={man:+5.1f}%  -> {got}")
    print(f"  CONTROL: {'PASS' if ok else '**FAIL**'}")
    return ok


def verdict(ds, df, manheim, n_deals, n_months):
    """Pure function of the pre-registered boundary. Returns (verdict, why)."""
    if n_deals < MIN_DEALS:
        return "NO VERDICT", f"only {n_deals} deal(s) reporting both fields; need {MIN_DEALS}"
    if n_months < WINDOW_MONTHS:
        return ("NO VERDICT",
                f"window is {n_months} month(s); the pre-registered window is {WINDOW_MONTHS}. "
                f"At n={n_months} the minimum detectable skip-share change is worse than the "
                f"threshold this test is tuned to — NOT ARMED")
    if manheim is not None and abs(manheim) > MANHEIM_BAND:
        # TWO-SIDED, and it has to be. The first draft of this gate only blocked a
        # used-car CRASH, which protects the CONFIRM branch (a crash lowers recovery
        # with no skip involved) and leaves the REFUTE branch wide open: a strong
        # used-car RALLY mechanically LIFTS recovery, so "severity flat" could be a
        # rising skip share being masked by a rising market. Same contamination,
        # opposite sign, and the one-sided version would have called that REFUTE.
        # Caught 2026-08-14 while taking the first live reading.
        direction = "decline" if manheim < 0 else "rally"
        masks = ("depresses recovery with no skip involved — would fake a CONFIRM"
                 if manheim < 0 else
                 "lifts recovery and can MASK a rising skip share — would fake a REFUTE")
        return ("NO VERDICT",
                f"Manheim YoY {manheim:+.1f}% outside ±{MANHEIM_BAND}% — common-mode "
                f"contaminated. A used-car {direction} {masks}")
    if ds >= CONFIRM_DS and df <= CONFIRM_DF:
        return ("CONFIRM",
                f"severity +{ds:.2f}pp (>= {CONFIRM_DS}) while frequency {df:+.2f}pp "
                f"(<= {CONFIRM_DF}) — loss severity rose without a delinquency precursor")
    if ds <= REFUTE_DS and df >= REFUTE_DF:
        return ("REFUTE",
                f"severity {ds:+.2f}pp (<= {REFUTE_DS}) while frequency +{df:.2f}pp "
                f"(>= {REFUTE_DF}) — deterioration is ordinary delinquency at stable severity")
    return ("NO VERDICT",
            f"dS={ds:+.2f} dF={df:+.2f} falls in the deliberate dead band between "
            f"CONFIRM and REFUTE")


def main():
    argv = sys.argv
    window = int(argv[argv.index("--window") + 1]) if "--window" in argv else WINDOW_MONTHS
    manheim = float(argv[argv.index("--manheim") + 1]) if "--manheim" in argv else None

    print("=" * 78)
    print("  SEVERITY-DIVERGENCE TEST — Secondary-thesis ('Invisible Exit') falsifier")
    print("=" * 78)

    control_ok = self_test()
    if "--self-test" in argv:
        return 0 if control_ok else 1
    if not control_ok:
        print("\n  **CONTROL FAILED — the verdict function is broken. No reading taken.**\n")
        return 1

    data = load()
    if not data:
        print(f"\n  no usable rows in {LEDGER.name}\n")
        return 1

    print(f"\n  Ledger: {LEDGER.name}   window: {window} month(s)   "
          f"Manheim YoY: {f'{manheim:+.1f}%' if manheim is not None else 'NOT SUPPLIED'}")
    print(f"\n  {'deal':<14}{'n':>3}{'first':>12}{'last':>12}"
          f"{'dSeverity':>11}{'dFreq':>9}   signature")
    dss, dfs, spans = [], [], []
    for d in DEALS:
        obs = data.get(d, [])
        if len(obs) < 2:
            print(f"  {d:<14}{len(obs):>3}  — insufficient observations")
            continue
        use = obs[-(window + 1):]
        ds = use[-1][1] - use[0][1]
        df = use[-1][2] - use[0][2]
        dss.append(ds); dfs.append(df); spans.append(len(use) - 1)
        sig = ("SEVERITY-DIVERGENT" if ds >= CONFIRM_DS and df <= CONFIRM_DF
               else "ordinary-credit" if ds <= REFUTE_DS and df >= REFUTE_DF
               else "-")
        print(f"  {d:<14}{len(use):>3}{use[0][0]:>12}{use[-1][0]:>12}"
              f"{ds:>+11.2f}{df:>+9.2f}   {sig}")

    if not dss:
        print("\n  NO VERDICT — no deal had two usable observations\n")
        return 0

    mds, mdf = S.mean(dss), S.mean(dfs)
    n_months = min(spans)
    v, why = verdict(mds, mdf, manheim, len(dss), n_months)

    print(f"\n  panel mean:   dSeverity {mds:+.2f}pp    dFrequency {mdf:+.2f}pp    "
          f"deals={len(dss)}  window={n_months}mo")
    print(f"\n  {'='*74}\n  VERDICT: {v}\n  {'='*74}\n  {why}")

    if v == "NO VERDICT" and n_months < WINDOW_MONTHS:
        print(f"\n  ARMING GAP: {WINDOW_MONTHS - n_months} more monthly filing(s) needed.")
        print("  Backfill rather than wait — the full 10-D history is on EDGAR:")
        print("      .venv/bin/python3 AGENTS/OTTO/scripts/panel_10d.py --only EART --history 15")
    if manheim is None and v != "NO VERDICT":
        print("\n  ⚠ Manheim YoY was NOT supplied. The verdict above is UNCONTROLLED for the")
        print("    used-vehicle market. Re-run with --manheim <yoy%> before recording it.")
    print("\n  SCOPE: measures the MECHANISM (collateral-less default) in deep subprime.")
    print("         Does NOT identify the immigrant cohort — Tricolor's own deals were")
    print("         144A with no public performance data. Do not over-claim a CONFIRM.\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
