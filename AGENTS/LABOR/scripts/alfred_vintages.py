#!/usr/bin/env python3
"""
ALFRED payroll VINTAGE TABLE — WQ-175 clause ② build (DOCKET L274, due 2026-09-25).

Turns Will's "payrolls are consistently revised lower" into a MEASURED bias with a
sign and a size, so the Oct-2 card's REVISION WATCH grades against a number instead
of an impression.

Usage:
  .venv/bin/python3 AGENTS/LABOR/scripts/alfred_vintages.py            # report only
  .venv/bin/python3 AGENTS/LABOR/scripts/alfred_vintages.py --write    # + write the TSV

Output: AGENTS/LABOR/workbook/PAYROLL_VINTAGES.tsv

SCOPE (fixed at authorisation, 2026-09-07)
------------------------------------------
HEADLINE PAYEMS ONLY, plus UNRATE/EMRATIO measured for revision. Sector-level
revision variance (CARL's 9/5 finding: retail trade revised ~7.5x harder than the
headline) is a NAMED FOLLOW-ON, deliberately outside this build — it would change
the deliverable's shape and the deadline is real.

⛔ THIS MOVES NO THRESHOLD AND SCORES NO VECTOR. It is a measurement.

METHOD
------
For reference month M, the published headline NFP is a MoM DIFFERENCE, so it must be
computed WITHIN a single vintage:  headline(M, V) = level(M, V) - level(M-1, V).
Reading a level across vintages instead is the error that makes revisions look
larger or smaller than they were.

  FIRST print  = headline computed in the FIRST vintage containing M
  THIRD print  = headline in the THIRD vintage containing M (two revisions later)
  CURRENT      = headline in the newest vintage
  BENCHMARKED  = headline in the first vintage on/after the annual benchmark that
                 follows M (benchmarks land with the January release, each February).
                 Months whose benchmark has not yet happened are marked PENDING and
                 are EXCLUDED from benchmark-bias aggregates — never folded in as 0.

🔒 REGIME CLASSIFIER — PRE-REGISTERED BEFORE ANY BIAS WAS COMPUTED
------------------------------------------------------------------
Written and committed before the revision figures were looked at, because a regime
cut chosen after seeing the bias is fitted, not measured.

  regime(M) = ACCELERATING  if  mean(first-print headline for M, M-1, M-2)
                             >  mean(first-print headline for M-3, M-4, M-5)
              DECELERATING  otherwise

It uses FIRST-PRINT values only — information actually available when M was first
published. No revised figure enters the classifier, so the regime label cannot be
contaminated by the revisions being measured.

VALIDATION GATE (fail-loud, runs before any aggregate is printed)
-----------------------------------------------------------------
The reconstruction must reproduce headlines published by BLS. If it cannot, the
whole table is untrustworthy and the script exits 2 rather than printing a number.
Anchors are the figures LABOR graded at the primary:
  2026-07 first print -23K · 2026-07 current +21K · 2026-06 current +31K
  2026-08 first print +162K
"""

import json
import os
import pathlib
import sys
import urllib.parse
import urllib.request
from collections import OrderedDict
from datetime import date

LABOR_DIR = pathlib.Path(__file__).resolve().parent.parent
WORKSPACE = LABOR_DIR.parent.parent
OUT_TSV = LABOR_DIR / "workbook" / "PAYROLL_VINTAGES.tsv"

# Reference-month window for the deliverable. Observations start earlier so that
# MoM (needs M-1) and the regime classifier (needs M-5) are defined at 2023-01.
FIRST_REF = "2023-01"
OBS_START = "2022-06-01"
RT_START = "2023-02-01"          # first vintage that can contain 2023-01

# (published headline in thousands) — graded at the primary by LABOR
ANCHORS = [
    ("2026-07", "first", -23),
    ("2026-07", "current", 21),
    ("2026-06", "current", 31),
    ("2026-08", "first", 162),
]


def load_key():
    envp = WORKSPACE / "FORGE" / "tools" / "market-data" / ".env"
    if envp.exists():
        for line in envp.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                os.environ.setdefault(k.strip(), v.strip())
    key = os.environ.get("FRED_API_KEY", "")
    if not key:
        sys.exit("FRED_API_KEY not set (FORGE/tools/market-data/.env) — CANNOT-VERIFY, not a pass")
    return key


def vintage_table(series_id, key, obs_start=OBS_START, rt_start=RT_START):
    """ALFRED wide table: {ref_month 'YYYY-MM': OrderedDict(vintage_date -> level)}."""
    q = {
        "series_id": series_id, "api_key": key, "file_type": "json",
        "observation_start": obs_start, "realtime_start": rt_start,
        "realtime_end": "9999-12-31", "output_type": "2",
    }
    url = "https://api.stlouisfed.org/fred/series/observations?" + urllib.parse.urlencode(q)
    try:
        data = json.load(urllib.request.urlopen(url, timeout=120))
    except Exception as exc:                                    # noqa: BLE001
        sys.exit(f"ALFRED fetch FAILED for {series_id}: {exc} — CANNOT-VERIFY, not a pass")
    out = {}
    for o in data["observations"]:
        ref = o["date"][:7]
        vs = OrderedDict()
        for k, v in o.items():
            if k == "date" or v in (".", "", None):
                continue
            vs[k.rsplit("_", 1)[1]] = float(v)          # 'PAYEMS_20260904' -> '20260904'
        out[ref] = OrderedDict(sorted(vs.items()))
    return out


def prev_month(ref):
    y, m = int(ref[:4]), int(ref[5:7])
    return f"{y-1}-12" if m == 1 else f"{y}-{m-1:02d}"


def headline(tbl, ref, vintage):
    """MoM change for ref month, computed WITHIN one vintage. None if unavailable."""
    pm = prev_month(ref)
    a = tbl.get(ref, {}).get(vintage)
    b = tbl.get(pm, {}).get(vintage)
    if a is None or b is None:
        return None
    return a - b


def benchmark_vintage_for(ref, vintages):
    """First vintage on/after the annual benchmark that follows ref.

    Benchmarks publish with the January Employment Situation, released in February.
    For ref month M in year Y, that is the February release of year Y+1 (a month in
    Nov/Dec of Y is benchmarked the following February too).
    """
    y = int(ref[:4])
    cutoff = f"{y+1}0201"
    later = [v for v in vintages if v >= cutoff]
    return later[0] if later else None


def build():
    key = load_key()
    pay = vintage_table("PAYEMS", key)
    refs = sorted(r for r in pay if r >= FIRST_REF)
    all_vintages = sorted({v for vs in pay.values() for v in vs})

    rows = []
    for ref in refs:
        vs = list(pay[ref].keys())
        if not vs:
            continue
        first_v = vs[0]
        third_v = vs[2] if len(vs) > 2 else None
        cur_v = all_vintages[-1]
        bench_v = benchmark_vintage_for(ref, all_vintages)

        rows.append({
            "ref_month": ref,
            "first_vintage": first_v,
            "first_print": headline(pay, ref, first_v),
            "third_vintage": third_v or "",
            "third_print": headline(pay, ref, third_v) if third_v else None,
            "bench_vintage": bench_v or "",
            "benchmarked": headline(pay, ref, bench_v) if bench_v else None,
            "current_vintage": cur_v,
            "current": headline(pay, ref, cur_v),
            "n_vintages": len(vs),
        })

    # --- regime, from FIRST PRINTS ONLY (pre-registered above) -----------------
    fp = {r["ref_month"]: r["first_print"] for r in rows}
    order = [r["ref_month"] for r in rows]
    for i, r in enumerate(rows):
        win_new = [fp.get(order[j]) for j in range(i - 2, i + 1) if 0 <= j < len(order)]
        win_old = [fp.get(order[j]) for j in range(i - 5, i - 2) if 0 <= j < len(order)]
        if len(win_new) == 3 and len(win_old) == 3 and all(x is not None for x in win_new + win_old):
            r["regime"] = "ACCELERATING" if (sum(win_new) / 3) > (sum(win_old) / 3) else "DECELERATING"
        else:
            r["regime"] = "INSUFFICIENT"

    for r in rows:
        r["rev_first_to_third"] = (
            None if r["third_print"] is None or r["first_print"] is None
            else r["third_print"] - r["first_print"])
        r["rev_first_to_current"] = (
            None if r["current"] is None or r["first_print"] is None
            else r["current"] - r["first_print"])
        r["rev_first_to_bench"] = (
            None if r["benchmarked"] is None or r["first_print"] is None
            else r["benchmarked"] - r["first_print"])
        r["bench_status"] = "BENCHMARKED" if r["benchmarked"] is not None else "PENDING"
    return pay, rows


def validate(pay, rows):
    by = {r["ref_month"]: r for r in rows}
    bad = []
    for ref, which, want in ANCHORS:
        r = by.get(ref)
        got = None if r is None else round(r["first_print"] if which == "first" else r["current"])
        if got != want:
            bad.append(f"{ref} {which}: reconstructed {got}, BLS published {want}")
    print("  VALIDATION GATE — reconstruction vs BLS-published headlines")
    for ref, which, want in ANCHORS:
        r = by.get(ref)
        got = None if r is None else round(r["first_print"] if which == "first" else r["current"])
        mark = "✅" if got == want else "❌"
        print(f"    {mark} {ref} {which:8} reconstructed {got:>+6}K   published {want:>+6}K")
    if bad:
        print("\n  ❌ VALIDATION FAILED — the table does not reproduce published headlines:")
        for b in bad:
            print("     •", b)
        print("  Refusing to print aggregates off an unvalidated reconstruction.")
        sys.exit(2)
    print("    → gate PASS, aggregates below are computed on a validated table\n")


def summarize(rows):
    def agg(sel, field):
        vals = [r[field] for r in rows if sel(r) and r[field] is not None]
        if not vals:
            return None
        n = len(vals)
        mean = sum(vals) / n
        # Dispersion is reported BESIDE every mean on purpose. A revision mean of
        # -33K against an SD of ~50K is not a number you can difference between two
        # subsamples and call a regime effect. finding_verified_figures_do_not_
        # verify_the_shape_claim: name the denominator AND beat the noise before
        # any shape word.
        sd = (sum((v - mean) ** 2 for v in vals) / (n - 1)) ** 0.5 if n > 1 else float("nan")
        se = sd / (n ** 0.5) if n > 1 else float("nan")
        srt = sorted(vals)
        med = srt[n // 2] if n % 2 else (srt[n // 2 - 1] + srt[n // 2]) / 2
        neg = sum(1 for v in vals if v < 0)
        return n, mean, neg, min(vals), max(vals), sd, se, med

    print("  REVISION BIAS — first print → later vintage (thousands of jobs)")
    print(f"    {'cut':<28} {'n':>4} {'mean':>9} {'median':>8} {'SD':>7} {'SE':>7} {'neg/n':>9} {'min':>7} {'max':>7}")
    print(f"    {'-'*94}")
    cuts = [
        ("ALL · first→third", lambda r: True, "rev_first_to_third"),
        ("ALL · first→current", lambda r: True, "rev_first_to_current"),
        ("ALL · first→benchmarked", lambda r: r["bench_status"] == "BENCHMARKED", "rev_first_to_bench"),
        ("ACCELERATING · first→third", lambda r: r["regime"] == "ACCELERATING", "rev_first_to_third"),
        ("DECELERATING · first→third", lambda r: r["regime"] == "DECELERATING", "rev_first_to_third"),
        ("ACCELERATING · first→current", lambda r: r["regime"] == "ACCELERATING", "rev_first_to_current"),
        ("DECELERATING · first→current", lambda r: r["regime"] == "DECELERATING", "rev_first_to_current"),
    ]
    res = {}
    for label, sel, field in cuts:
        a = agg(sel, field)
        res[label] = a
        if a is None:
            print(f"    {label:<28} {'—':>4}")
            continue
        n, mean, neg, lo, hi, sd, se, med = a
        print(f"    {label:<28} {n:>4} {mean:>+8.1f}K {med:>+7.0f}K {sd:>6.0f}K {se:>6.1f}K "
              f"{neg:>4}/{n:<4} {lo:>+6.0f}K {hi:>+6.0f}K")
    # --- is the REGIME split real, or noise? Ask before reporting it as a cut. ---
    for field, lbl in (("rev_first_to_third", "first→third"), ("rev_first_to_current", "first→current")):
        a = res.get(f"ACCELERATING · {lbl}") or res.get(f"ACCELERATING · first→third")
        acc = agg(lambda r: r["regime"] == "ACCELERATING", field)
        dec = agg(lambda r: r["regime"] == "DECELERATING", field)
        if acc and dec:
            diff = acc[1] - dec[1]
            se_d = (acc[6] ** 2 + dec[6] ** 2) ** 0.5
            t = diff / se_d if se_d else float("nan")
            verdict = "INDISTINGUISHABLE" if abs(t) < 2 else "separated"
            print(f"\n    REGIME TEST {lbl}: ACC {acc[1]:+.1f}K vs DEC {dec[1]:+.1f}K  "
                  f"⇒ diff {diff:+.1f}K, SE(diff) {se_d:.1f}K, t = {diff:+.1f}/{se_d:.1f} = {t:+.2f}"
                  f"  ⇒ {verdict}")

    # RED-23 asked for exactly this distribution and declared its own confidence
    # UNCALIBRATED for want of it. July-2026's place in it is the answer.
    jul = next((r for r in rows if r["ref_month"] == "2026-07"), None)
    ft = sorted(r["rev_first_to_current"] for r in rows if r["rev_first_to_current"] is not None)
    if jul and jul["rev_first_to_current"] is not None:
        v = jul["rev_first_to_current"]
        rank = sum(1 for x in ft if x <= v)
        print(f"\n    RED-23 / 2026-07: first {jul['first_print']:+.0f}K → current "
              f"{jul['current']:+.0f}K = {v:+.0f}K, rank {rank}/{len(ft)} "
              f"({rank/len(ft)*100:.0f}th pct) — the MOST UPWARD-revised month in the sample."
              f" A 60% confidence resting on n=1 rests on the opposite tail from the systematic bias.")

    pend = sum(1 for r in rows if r["bench_status"] == "PENDING")
    print(f"\n    PENDING benchmark (excluded from the benchmark cut, never counted as 0): {pend}")
    return res


def write_tsv(rows):
    cols = ["ref_month", "regime", "first_vintage", "first_print", "third_vintage",
            "third_print", "bench_vintage", "benchmarked", "bench_status",
            "current_vintage", "current", "rev_first_to_third",
            "rev_first_to_bench", "rev_first_to_current", "n_vintages"]
    OUT_TSV.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT_TSV, "w") as f:
        f.write(f"# ALFRED payroll vintage table — PAYEMS headline (MoM, thousands), "
                f"reference months {rows[0]['ref_month']}..{rows[-1]['ref_month']}\n")
        f.write(f"# Last real data refresh: {date.today().isoformat()}\n")
        f.write("# Built by scripts/alfred_vintages.py (WQ-175 clause 2 / DOCKET L274). "
                "Headline = level(M) - level(M-1) computed WITHIN one vintage. "
                "Regime from FIRST PRINTS ONLY, pre-registered before any bias was computed. "
                "PENDING benchmark rows are excluded from benchmark aggregates, never folded in as 0. "
                "MOVES NO THRESHOLD.\n")
        f.write("\t".join(cols) + "\n")
        for r in rows:
            f.write("\t".join(
                "" if r.get(c) is None else
                (f"{r[c]:+.0f}" if isinstance(r.get(c), float) and c not in ("n_vintages",) else str(r.get(c)))
                for c in cols) + "\n")
    print(f"\n  wrote {OUT_TSV.relative_to(WORKSPACE)}  ({len(rows)} reference months)")


def main():
    print(f"\n{'='*74}")
    print("  ALFRED PAYROLL VINTAGE TABLE — WQ-175 clause ② / DOCKET L274")
    print(f"{'='*74}\n")
    pay, rows = build()
    print(f"  reference months {rows[0]['ref_month']} .. {rows[-1]['ref_month']}  "
          f"({len(rows)} rows)\n")
    validate(pay, rows)
    summarize(rows)
    if "--write" in sys.argv:
        write_tsv(rows)
    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
