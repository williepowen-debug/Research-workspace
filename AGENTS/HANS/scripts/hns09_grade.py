#!/usr/bin/env python3
"""
hns09_grade — grades prediction HNS-09 from workbook/HNS09_Q3_RESULTS.tsv.

HNS-09 (registered 2026-08-28, 70%): "At Q3-2026 European bank results, the sector shows
NII/earnings still holding with NO material rise in cost-of-risk."

WHY THIS IS A SCRIPT. The prediction was registered with no named bank set, no cost-of-risk
series and no number for "material" (DAEDALUS, 10/08 and 10/21). A grade written after the
results would choose those three things knowing the answer. This file fixes them BEFORE the
first result (BNP and Deutsche, 2026-10-28), and the tests in test_hans.py hold it to them.

THE RULES (frozen 2026-10-21, hans-1021, before any Q3 result in the set was published):
  BANK SET   the 9 large euro-area banks listed in the TSV. Fixed: a bank is never added or
             dropped after the fact. A bank that has not reported by 2026-11-30 is simply
             not counted.
  SOURCE     each bank's OWN Q3 release or results presentation. A row with an empty
             `source` cell does not count.
  EARNINGS   NII, Q3-2026 vs Q3-2025, as reported. HOLDING = Q3-26 >= 95% of Q3-25.
             NII, not net income, because net income carries one-offs (disposals, exits,
             M&A) that say nothing about the rate leg this prediction is about.
             Reported EUR figures only - constant-currency figures are NOT used (Santander and
             BBVA carry large FX effects; choosing the basis after seeing it would be a free parameter).
  CREDIT     cost of risk, Q3-2026 vs Q3-2025, AS REPORTED - never adjusted. MATERIAL RISE
             = +10bp or more (annualised, on the bank's own basis), OR the bank raises its
             full-year cost-of-risk guidance. If a bank gives CoR only in EUR, material =
             a rise of at least max(30% of |Q3-25|, EUR 50mn).
             ⛔ NO ONE-OFF ADJUSTMENT. Stripping a "one-off" out of cost of risk is the
             single move that would let this prediction pass a test it should fail.
             One-offs go in `notes`; the reported number is graded.
  SECTOR     needs >= 3 graded banks (otherwise CANNOT-GRADE; the registered anchor then
             extends past 11/30 until three have reported). MISS if AT LEAST ONE-THIRD of
             graded banks show a material CoR rise, OR at least one-third fail the NII test.
             Otherwise HIT. Ties fall on the MISS side, against the prediction.

A HIT is not reassurance: it means the credit leg has not turned YET (see the registered note).
"""
import csv, sys
from pathlib import Path

HANS = Path(__file__).resolve().parent.parent
TSV = HANS / "workbook/HNS09_Q3_RESULTS.tsv"
WINDOW_END = "2026-11-30"
NII_HOLD = 0.95
COR_BP_MATERIAL = 10.0
COR_EUR_PCT, COR_EUR_FLOOR = 0.30, 50.0
MIN_BANKS = 3


def _num(x):
    x = (x or "").strip()
    if not x:
        return None
    return float(x)          # a non-numeric cell RAISES: a typo must not read as "blank"


def read(path=TSV):
    lines = [l for l in Path(path).read_text(encoding="utf-8").split("\n")
             if l.strip() and not l.lstrip().startswith("#")]
    return list(csv.DictReader(lines, delimiter="\t"))


def grade_bank(r):
    """-> (state, nii_hold, cor_material, why). state is GRADED, PENDING or INCOMPLETE."""
    if (r.get("status") or "").strip().upper() != "REPORTED":
        return "PENDING", None, None, "not reported"
    if not (r.get("source") or "").strip():
        return "INCOMPLETE", None, None, "no source"
    if not (r.get("results_date") or "").strip():
        return "INCOMPLETE", None, None, "no results_date - the window cannot be checked"
    if r["results_date"].strip() > WINDOW_END:
        return "INCOMPLETE", None, None, f"reported after {WINDOW_END}"
    n26, n25 = _num(r.get("nii_q3_26_eur_mn")), _num(r.get("nii_q3_25_eur_mn"))
    if n26 is None or n25 is None or n25 <= 0:
        return "INCOMPLETE", None, None, "NII pair missing"
    nii_hold = n26 >= NII_HOLD * n25
    guide = (r.get("fy_cor_guidance_raised") or "").strip().upper() == "Y"
    b26, b25 = _num(r.get("cor_bp_q3_26")), _num(r.get("cor_bp_q3_25"))
    e26, e25 = _num(r.get("cor_eur_mn_q3_26")), _num(r.get("cor_eur_mn_q3_25"))
    if b26 is not None and b25 is not None:
        rise, basis = b26 - b25, "bp"
        cor_mat = rise >= COR_BP_MATERIAL
    elif e26 is not None and e25 is not None:
        rise, basis = e26 - e25, "EUR mn"
        cor_mat = rise >= max(COR_EUR_PCT * abs(e25), COR_EUR_FLOOR)
    else:
        return "INCOMPLETE", None, None, "CoR pair missing"
    cor_mat = cor_mat or guide
    why = (f"NII {n26:.0f}/{n25:.0f} = {n26 / n25 - 1:+.1%} · CoR {rise:+.1f} {basis}"
           + (" · FY guidance RAISED" if guide else ""))
    return "GRADED", nii_hold, cor_mat, why


def grade(rows):
    """-> (verdict, n_graded, n_cor_material, n_nii_fail, per_bank)."""
    per = [(r.get("bank", "?"),) + grade_bank(r) for r in rows]
    g = [p for p in per if p[1] == "GRADED"]
    n = len(g)
    cor = sum(1 for p in g if p[3])
    nii = sum(1 for p in g if not p[2])
    if n < MIN_BANKS:
        return "CANNOT-GRADE", n, cor, nii, per
    miss = cor * 3 >= n or nii * 3 >= n          # integer form of ">= one-third"
    return ("MISS" if miss else "HIT"), n, cor, nii, per


def main():
    verdict, n, cor, nii, per = grade(read())
    print("HNS-09 GRADER — Q3-2026 European bank results (rules frozen 2026-10-21)")
    for bank, state, nh, cm, why in per:
        flag = "" if state != "GRADED" else (" CoR-MATERIAL" if cm else "") + ("" if nh else " NII-FAIL")
        print(f"  {bank:18} {state:11} {why}{flag}")
    print(f"\n  graded {n} · CoR material {cor} · NII fail {nii} · threshold = one-third of graded")
    print(f"  VERDICT: {verdict}" + ("  (needs >= 3 graded banks)" if verdict == "CANNOT-GRADE" else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
