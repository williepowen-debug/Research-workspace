#!/usr/bin/env python3
r"""
CARL Brier / calibration audit — scores CARL's own prediction record.

Deferred since v2.5.1 (2026-05-01); first run 2026-07-24 at Will's direction.

WHAT IT MEASURES
  Brier score   BS = mean( (forecast - outcome)^2 ).  Lower is better.
                0.00 = perfect · 0.25 = what you get always saying 50%.
  Skill vs climatology  BSS = 1 - BS / BS_climatology, where climatology is
                "always forecast the base rate".  NEGATIVE skill means the
                forecasts are worse than knowing nothing but the base rate —
                the single most important number in this report.
  Calibration   binned forecast-vs-actual.
  Decomposition Murphy: BS = Reliability - Resolution + Uncertainty.

THE METHODOLOGICAL PROBLEM, STATED UP FRONT
  `PREDICTIONS.tsv` Confidence holds the CURRENT/at-resolution value, not the
  ex-ante one.  CARL re-marks confidence as evidence arrives (CRL-03 ran
  90 -> 72 before resolving MISSED; CRL-11 85 -> 83).  Scoring the at-resolution
  number therefore **FLATTERS** the record: losers were trimmed before they
  resolved.  Where an earlier mark is recoverable from Notes, this script scores
  BOTH bases and reports the gap.  Treat the as-recorded score as a CEILING on
  true skill, not an estimate of it.

CONVENTIONS
  CONFIRMED -> 1.0 · MISSED -> 0.0 · MIXED -> 0.5 (stated, not obvious).
  "Legacy confirmed (pre-TSV)" bullets are EXCLUDED — no ex-ante probability was
  ever recorded, so including them would be pure survivorship (only the winners
  were written down).

Usage:
  .venv/bin/python3 AGENTS/CARL/scripts/brier_audit.py
  .venv/bin/python3 AGENTS/CARL/scripts/brier_audit.py --tsv <path>
"""

import argparse
import csv
import re
import sys
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent
CARL_DIR = SCRIPTS_DIR.parent
DEFAULT_TSV = CARL_DIR / "thesis" / "PREDICTIONS.tsv"

OUTCOME = {"CONFIRMED": 1.0, "MISSED": 0.0, "MIXED": 0.5}
PCT = re.compile(r"(\d+)\s*%")
# "90% -> 72%" / "90->72" / "was 75"
ARROW = re.compile(r"(\d{2})\s*%?\s*(?:->|→)\s*(\d{2})\s*%?")
WAS = re.compile(r"was\s+(\d{2})")


def load(path):
    rows = list(csv.reader(path.open(newline="", encoding="utf-8"), delimiter="\t"))
    hdr = rows[0]
    idx = {k: i for i, k in enumerate(hdr)}
    out = []
    for r in rows[1:]:
        if len(r) <= idx["Status"]:
            continue
        st = r[idx["Status"]].strip().upper()
        if st not in OUTCOME:
            continue
        conf_cell = r[idx["Confidence"]]
        m = PCT.search(conf_cell)
        if not m:
            continue
        notes = r[idx["Notes"]] if len(r) > idx["Notes"] else ""
        # earliest recoverable mark: the largest LEFT-hand side of any "a -> b",
        # or any "was N" — both indicate a prior, pre-trim confidence.
        cands = [int(a) for a, _ in ARROW.findall(notes)] + [int(x) for x in WAS.findall(notes)]
        recorded = int(m.group(1))
        exante = max(cands) if cands else None
        out.append({
            "id": r[0], "status": st, "o": OUTCOME[st],
            "f_recorded": recorded / 100.0,
            "f_exante": (exante / 100.0) if exante is not None else None,
            "made": r[idx["Date_Made"]], "resolved": r[idx["Date_Resolved"]],
            "pred": r[idx["Prediction"]][:70],
        })
    return out


def brier(fs, os_):
    return sum((f - o) ** 2 for f, o in zip(fs, os_)) / len(fs)


def decompose(fs, os_, bins):
    """Murphy decomposition: BS = REL - RES + UNC."""
    n = len(fs)
    base = sum(os_) / n
    unc = base * (1 - base)
    rel = res = 0.0
    for lo, hi in bins:
        grp = [(f, o) for f, o in zip(fs, os_) if lo <= f < hi]
        if not grp:
            continue
        k = len(grp)
        fbar = sum(f for f, _ in grp) / k
        obar = sum(o for _, o in grp) / k
        rel += k * (fbar - obar) ** 2
        res += k * (obar - base) ** 2
    return rel / n, res / n, unc, base


def report(rows, label, key):
    fs = [r[key] for r in rows]
    os_ = [r["o"] for r in rows]
    n = len(fs)
    bs = brier(fs, os_)
    base = sum(os_) / n
    bs_clim = sum((base - o) ** 2 for o in os_) / n
    bss = 1 - bs / bs_clim if bs_clim > 0 else float("nan")
    mean_f = sum(fs) / n

    print(f"\n{'=' * 74}\n  {label}   (N = {n})\n{'=' * 74}")
    print(f"  Brier score              {bs:.4f}   (0 perfect · 0.25 = always saying 50%)")
    print(f"  Climatology (base-rate)  {bs_clim:.4f}   'always forecast {base:.0%}'")
    print(f"  BRIER SKILL SCORE        {bss:+.3f}   {'*** NEGATIVE — worse than knowing only the base rate ***' if bss < 0 else ''}")
    print(f"  Mean forecast            {mean_f:.1%}")
    print(f"  Actual hit rate          {base:.1%}")
    print(f"  OVERCONFIDENCE           {mean_f - base:+.1%}   (mean forecast minus actual)")

    bins = [(0.0, 0.55), (0.55, 0.65), (0.65, 0.75), (0.75, 0.85), (0.85, 1.01)]
    rel, res, unc, _ = decompose(fs, os_, bins)
    print(f"\n  Murphy decomposition:  BS = REL - RES + UNC")
    print(f"    Reliability (lower=better, 0=perfectly calibrated)  {rel:.4f}")
    print(f"    Resolution  (higher=better, discrimination)         {res:.4f}")
    print(f"    Uncertainty (base-rate variance, irreducible)       {unc:.4f}")
    print(f"    check: {rel:.4f} - {res:.4f} + {unc:.4f} = {rel - res + unc:.4f}")

    print(f"\n  CALIBRATION BY BAND")
    print(f"    {'band':<12} {'n':>2}  {'mean fcst':>9}  {'actual':>7}  {'gap':>7}   ids")
    for lo, hi in bins:
        grp = [r for r in rows if lo <= r[key] < hi]
        if not grp:
            continue
        mf = sum(r[key] for r in grp) / len(grp)
        ao = sum(r["o"] for r in grp) / len(grp)
        flag = "  <-- worst" if abs(mf - ao) > 0.5 else ""
        print(f"    {int(lo*100)}-{int(hi*100)}%{'':<5} {len(grp):>2}  {mf:>8.0%}  {ao:>7.0%}  {mf-ao:>+7.0%}   "
              f"{','.join(r['id'] for r in grp)}{flag}")
    return bs, bss, mean_f, base


def main():
    ap = argparse.ArgumentParser(description="CARL Brier / calibration audit.")
    ap.add_argument("--tsv", default=str(DEFAULT_TSV))
    args = ap.parse_args()
    path = Path(args.tsv)
    rows = load(path)
    if not rows:
        raise SystemExit("no resolved predictions found")

    print(f"\nCARL BRIER AUDIT — source {path}")
    print(f"Resolved predictions scored: {len(rows)}")
    print(f"Convention: CONFIRMED=1.0 · MISSED=0.0 · MIXED=0.5 · legacy pre-TSV EXCLUDED (survivorship)")

    print(f"\n  {'ID':8} {'STATUS':10} {'f(rec)':>7} {'f(ex-ante)':>11} {'outcome':>8}   prediction")
    for r in sorted(rows, key=lambda x: x["id"]):
        ea = f"{r['f_exante']:.0%}" if r["f_exante"] is not None else "  —"
        print(f"  {r['id']:8} {r['status']:10} {r['f_recorded']:>7.0%} {ea:>11} {r['o']:>8.1f}   {r['pred']}")

    bs_r, bss_r, mf_r, base = report(rows, "BASIS A — AS RECORDED (confidence at/near resolution)", "f_recorded")

    ex = [dict(r) for r in rows]
    n_rec = sum(1 for r in ex if r["f_exante"] is not None)
    for r in ex:
        if r["f_exante"] is None:
            r["f_exante"] = r["f_recorded"]
    bs_e, bss_e, mf_e, _ = report(
        ex, f"BASIS B — BEST-RECOVERABLE EX-ANTE ({n_rec}/{len(ex)} recovered from Notes; rest fall back to recorded)",
        "f_exante")

    print(f"\n{'=' * 74}\n  THE GAP\n{'=' * 74}")
    print(f"  Brier as-recorded {bs_r:.4f}  vs  ex-ante {bs_e:.4f}   ({bs_e - bs_r:+.4f})")
    print(f"  Mean forecast     {mf_r:.1%}      vs  {mf_e:.1%}")
    print(f"  Actual hit rate   {base:.1%}")
    print(f"\n  If ex-ante is WORSE, the recorded score is flattered by mid-life trimming:")
    print(f"  losers were marked down before they resolved. Treat BASIS A as a CEILING")
    print(f"  on true skill. Only {n_rec} of {len(ex)} ex-ante marks are recoverable, so B is")
    print(f"  itself a partial reconstruction, not the true ex-ante record.\n")
    print(f"  ⚠️  N = {len(rows)}. TERRY's paper-book spec sets N>=10 as the MINIMUM before")
    print(f"      scoring acts on anything. This is directional, not significant.\n")


if __name__ == "__main__":
    sys.exit(main())
