#!/usr/bin/env python3
"""HHDC grade lookup for the 2026-11-10 Q3 release (CARL, written 2026-11-09).

Usage (from repo root, isolated mode, data files passed as arguments):
  .venv/bin/python3 -I AGENTS/CARL/research/2026-11-09_HHDC_prep/hhdc_lookup.py \
      --prior AGENTS/CARL/research/2026-11-09_HHDC_prep/raw/HHD_C_Report_2026Q2.xlsx \
      --new   AGENTS/CARL/research/2026-11-09_HHDC_prep/raw/HHD_C_Report_2026Q3.xlsx \
      --quarter 26:Q3

Prints, from the NEW vintage only (single-vintage rule), the cells each registered
letter reads, then a revision diff against the PRIOR vintage (the card's §2 rule:
a revision check that reads only the new file is circular). Verdicts are mechanical
restatements of the frozen letters; CARL still writes the card by hand.

Letters encoded (verbatim sources):
  CRL-33  PREDICTIONS.tsv: Page 14 CC 26:Q3 > 6.97 at two decimals = YES; < = NO;
          exactly 6.97 = NO-VERDICT; series discontinued/re-based = NO-VERDICT.
  CRL-30  PREDICTIONS.tsv: Page 14 CC >= 7.50 in any release through 27:Q2 = fires;
          invalidation: < 6.50 in two consecutive releases.
  §1 AS-WRITTEN (superseded v2.6.5): Page 12 CC QoQ direction; Q2 was decline #1 of 2.
  §1 RE-SPEC (live v2.6.6): Page 14 CC falls 2 consecutive quarters AND cumulative
          decline across those two quarters >= 100bp.
  CRL-04  basis note only (CONFIRMED row): Page 12 STUDENT LOAN share, absolute 10% bar.
"""
import argparse
import sys

import openpyxl


def load(path):
    return openpyxl.load_workbook(path, read_only=True, data_only=True)


def series(wb, sheet, col):
    rows = list(wb[sheet].iter_rows(values_only=True))
    hdrs = [r for r in rows if r and r[0] is None and col in r]
    if not hdrs:
        raise SystemExit(f"STOP: column {col!r} not found on {sheet!r} - layout changed, read by hand")
    i = hdrs[0].index(col)
    out = {}
    for r in rows:
        if r and isinstance(r[0], str) and ":Q" in r[0] and len(r) > i and r[i] is not None:
            out[r[0].strip()] = float(r[i])
    return out


def prev_q(q):
    yy, qq = q.split(":Q")
    yy, qq = int(yy), int(qq)
    return f"{yy:02d}:Q{qq-1}" if qq > 1 else f"{yy-1:02d}:Q4"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--prior", required=True)
    ap.add_argument("--new", required=True)
    ap.add_argument("--quarter", required=True, help="e.g. 26:Q3")
    a = ap.parse_args()
    q, q1 = a.quarter, prev_q(a.quarter)
    q2 = prev_q(q1)
    new, old = load(a.new), load(a.prior)

    cells = [("Page 14 Data", "CC", "flow into 90+ CC (CRL-33, CRL-30, RE-SPEC)"),
             ("Page 12 Data", "CC", "90+ stock share CC (AS-WRITTEN shadow)"),
             ("Page 13 Data", "CC", "flow into 30+ CC (context, same pipeline - not a second witness)"),
             ("Page 12 Data", "STUDENT LOAN", "90+ stock share student (CRL-04 basis note)"),
             ("Page 14 Data", "STUDENT LOAN", "flow into 90+ student (context)"),
             ("Page 12 Data", "AUTO", "90+ stock share auto (CARL-AUTO-OUTFLOW-01 re-check)"),
             ("Page 14 Data", "AUTO", "flow into 90+ auto (context)")]

    data = {}
    print(f"== NEW vintage: {a.new}\n== PRIOR vintage: {a.prior}\n== quarter graded: {q}\n")
    if q not in series(new, "Page 14 Data", "CC"):
        sys.exit(f"STOP: {q} absent from NEW file Page 14 CC - wrong file or year-trap; check the PDF header")
    print(f"{'series':58s} {q2:>8s} {q1:>8s} {q:>8s}   revision of {q1} (prior -> new)")
    for sheet, col, label in cells:
        sn, so = series(new, sheet, col), series(old, sheet, col)
        data[(sheet, col)] = sn
        v = [sn.get(x) for x in (q2, q1, q)]
        fmt = lambda x: f"{x:8.4f}" if x is not None else "     n/a"
        rev = so.get(q1)
        revs = "n/a" if rev is None or sn.get(q1) is None else (
            "unrevised" if round(rev, 4) == round(sn[q1], 4) else f"REVISED {rev:.4f} -> {sn[q1]:.4f}")
        print(f"{label:58s} {fmt(v[0])} {fmt(v[1])} {fmt(v[2])}   {revs}")
    # how many quarters revised anywhere in history, per key series
    for sheet, col in [("Page 14 Data", "CC"), ("Page 12 Data", "CC")]:
        sn, so = data[(sheet, col)], series(old, sheet, col)
        diff = [k for k in so if k in sn and round(so[k], 4) != round(sn[k], 4)]
        print(f"  history revised on {sheet} {col}: {len(diff)} quarter(s) {diff[:8]}")

    f = data[("Page 14 Data", "CC")]
    s = data[("Page 12 Data", "CC")]
    print("\n== VERDICTS (mechanical restatement of frozen letters; CARL writes the card)")
    v33 = round(f[q], 2)
    print(f"CRL-33  {q} flow = {f[q]:.4f} -> {v33:.2f} vs 6.97: " +
          ("YES (above)" if v33 > 6.97 else "NO (below)" if v33 < 6.97 else "NO-VERDICT (tie at precision)"))
    print(f"CRL-30  {q} flow {f[q]:.2f} vs 7.50 bar: " + ("FIRES (>=7.50)" if f[q] >= 7.50 else "not fired, stays OPEN") +
          ("; invalidation leg: below 6.50 this release (needs two consecutive)" if f[q] < 6.50 else "") +
          f"; same-quarter YoY: {q[:2]}->{int(q[:2])-1:02d}{q[2:]} " +
          (f"{f[q]:.2f} vs {f.get(f'{int(q[:2])-1:02d}{q[2:]}', float('nan')):.2f}"))
    d1, d2 = f[q1] - f[q2], f[q] - f[q1]
    cum = f[q2] - f[q]
    respec = d1 < 0 and d2 < 0 and cum >= 1.00 - 1e-9
    print(f"RE-SPEC {q2}->{q1}->{q}: {f[q2]:.4f} -> {f[q1]:.4f} -> {f[q]:.4f}; moves {d1:+.4f}, {d2:+.4f}; "
          f"cumulative decline {cum*100:+.1f}bp vs 100bp floor -> " + ("LEG 2 MET" if respec else "leg 2 NOT met"))
    ds = s[q] - s[q1]
    print(f"AS-WRITTEN {q1}->{q} CC 90+ share {s[q1]:.4f} -> {s[q]:.4f} ({ds*100:+.1f}bp): " +
          ("DECLINE -> with prior-quarter decline (same vintage below) = 2 consecutive -> LEG 2 MET" if ds < 0 and s[q1] < s[q2]
           else "decline, but prior quarter was not a decline on this vintage" if ds < 0 else "NOT a decline -> count resets"))
    print(f"           same-vintage {q2}->{q1}: {s[q2]:.4f} -> {s[q1]:.4f} ({(s[q1]-s[q2])*100:+.1f}bp)")
    asw = ds < 0 and s[q1] < s[q2]
    if asw != respec:
        print("\n!! §1 DIVERGENCE: the two rows disagree. Write both on the card and escalate to Will THIS SESSION (Rider 1).")
    else:
        print("\n§1 rows agree (" + ("both met" if asw else "neither met") + "). Leg 1 (claims) still recorded on the card.")
    st = data[("Page 12 Data", "STUDENT LOAN")]
    print(f"CRL-04 basis note: student 90+ share {q} = {st[q]:.2f} (bar 10.0%, row CONFIRMED; note only, no re-grade)")


if __name__ == "__main__":
    main()
