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

⚠️ REGIME CLASSIFIER — DECLARED BEFORE THE BIAS WAS COMPUTED **IN-SESSION**, BUT THERE IS NO RECEIPT.
   🔧 Corrected 2026-09-07 (DAEDALUS): this header read "PRE-REGISTERED", and pre-registration is a
   claim about ORDER that only a commit can establish. This file and its results
   (`workbook/PAYROLL_VINTAGES.tsv`) were committed TOGETHER in `e96453b45`, so nothing external
   proves the classifier predates the numbers. The claim may be true; it is not EVIDENCED, and an
   unevidenced order claim is worth what "falsified before adoption" was worth earlier today.
   ⇒ FORWARD-ONLY RULE: commit the spec in its own commit BEFORE computing the result.
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

# Validation anchors, PINNED TO EXPLICIT VINTAGE DATES.
# ⚠️ These were originally written as ("2026-07", "current", 21) — a fixed number
# compared against WHATEVER IS CURRENT WHEN THE SCRIPT RUNS. Because the fetch runs
# through 9999-12-31, the next legitimate revision to July would have made the gate
# exit 2 and blocked the build. A validation anchor must name a FIXED historical
# release; "current" is not a fixed object. (CODEX review, 2026-09-07.)
# (ref_month, vintage_date, published headline in thousands)
ANCHORS = [
    ("2026-07", "20260807", -23),    # July first print, as published 2026-08-07
    ("2026-07", "20260904", 21),     # July as revised at the Aug release
    ("2026-06", "20260904", 31),     # June as revised at the Aug release
    ("2026-08", "20260904", 162),    # August first print
    ("2026-06", "20260702", 57),     # June first print — a second FIRST-stage anchor
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

    # --- RELEASE-STAGE INTEGRITY -------------------------------------------
    # `vs[2]` is the THIRD AVAILABLE VINTAGE, which equals BLS's THIRD ESTIMATE only
    # when the publication schedule was normal. It was not in late 2025: the 2025-10
    # and 2025-11 reference months BOTH first appear in the SAME 2025-12-16 vintage,
    # and 2025-09 first appears 2025-11-20 (~7 weeks late) — the lapse-in-
    # appropriations disruption. For those months the first AVAILABLE observation is
    # not BLS's first estimate, so "first→third available" and "first→third estimate"
    # are DIFFERENT MEASUREMENTS and must not be pooled silently.
    # Detection is structural, not a hardcoded date list:
    #   (a) a vintage that introduces MORE THAN ONE reference month, or
    #   (b) a first vintage landing >45 days after the reference month ends.
    # Flagged months are reported SEPARATELY and excluded from the headline
    # first→third aggregate. (CODEX review, 2026-09-07.)
    introduces = {}
    for ref in refs:
        vs = list(pay[ref].keys())
        if vs:
            introduces.setdefault(vs[0], []).append(ref)

    def disrupted(ref, first_v):
        if len(introduces.get(first_v, [])) > 1:
            return "MULTI-MONTH-RELEASE"
        y, m = int(ref[:4]), int(ref[5:7])
        eom = date(y + (m == 12), 1 if m == 12 else m + 1, 1)
        fv = date(int(first_v[:4]), int(first_v[4:6]), int(first_v[6:8]))
        return "LATE-FIRST-RELEASE" if (fv - eom).days > 45 else ""

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
            "third_available": headline(pay, ref, third_v) if third_v else None,
            "bench_vintage": bench_v or "",
            "benchmarked": headline(pay, ref, bench_v) if bench_v else None,
            "current_vintage": cur_v,
            "current": headline(pay, ref, cur_v),
            "n_vintages": len(vs),
            "stage_flag": disrupted(ref, first_v) or "OK",
        })

    # --- regime, from FIRST PRINTS ONLY (declared above; order NOT receipted) ---
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
            None if r["third_available"] is None or r["first_print"] is None
            else r["third_available"] - r["first_print"])
        r["rev_first_to_current"] = (
            None if r["current"] is None or r["first_print"] is None
            else r["current"] - r["first_print"])
        r["rev_first_to_bench"] = (
            None if r["benchmarked"] is None or r["first_print"] is None
            else r["benchmarked"] - r["first_print"])
        r["bench_status"] = "BENCHMARKED" if r["benchmarked"] is not None else "PENDING"
    return pay, rows


def validate(pay, rows):
    bad = []
    print("  VALIDATION GATE — reconstruction vs BLS headlines, at PINNED vintages")
    for ref, vintage, want in ANCHORS:
        h = headline(pay, ref, vintage)
        got = None if h is None else round(h)
        mark = "✅" if got == want else "❌"
        print(f"    {mark} {ref} @ vintage {vintage}  reconstructed {got if got is None else format(got,'+')}K"
              f"   published {want:+}K")
        if got != want:
            bad.append(f"{ref} @ {vintage}: reconstructed {got}, BLS published {want}")
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
        ("first→third (stage OK)", lambda r: r["stage_flag"] == "OK", "rev_first_to_third"),
        ("first→third INCL disrupted", lambda r: True, "rev_first_to_third"),
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
            lo, hi = diff - 1.96 * se_d, diff + 1.96 * se_d
            # ⚠️ WORDING IS THE FINDING. "no difference detected" != "no difference
            # exists". n=13 vs 24 with an interval this wide leaves economically
            # large effects unresolved; an equivalence claim would need a declared
            # margin and precision enough to exclude it. Earlier drafts of this
            # build said "the split does not exist in this data" — withdrawn.
            verdict = ("NOT DETECTED (not the same as absent)" if abs(t) < 2
                       else "separated")
            print(f"\n    REGIME TEST {lbl}: ACC {acc[1]:+.1f}K (n={acc[0]}) vs DEC {dec[1]:+.1f}K (n={dec[0]})"
                  f"  ⇒ diff {diff:+.1f}K, SE {se_d:.1f}K, t = {diff:+.1f}/{se_d:.1f} = {t:+.2f}"
                  f"\n      95% interval on the difference ≈ [{lo:+.0f}K, {hi:+.0f}K]  ⇒ {verdict}")

    # RED-23 asked for exactly this distribution and declared its own confidence
    # UNCALIBRATED for want of it. July-2026's place in it is the answer.
    # ⚠️ RED-23 resolves on August's THIRD PRINT, so the relevant distribution is
    # first→THIRD. An earlier version of this block ranked July on first→CURRENT and
    # reported "44/44, the most upward-revised month" as if it calibrated RED-23.
    # That mixes horizons: older months have absorbed annual revisions July has not,
    # and JULY HAS NO first→third VALUE AT ALL (only 2 vintages exist). On the
    # correct cut, +74K (2023-12), +67K (2024-12) and +49K (2023-07) all exceed
    # July's +44K. Corrected 2026-09-07 (CODEX review) — the packet built on the
    # wrong version went to RED and was retracted.
    jul = next((r for r in rows if r["ref_month"] == "2026-07"), None)
    ft3 = sorted(r["rev_first_to_third"] for r in rows
                 if r["rev_first_to_third"] is not None and r["stage_flag"] == "OK")
    cur = sorted(r["rev_first_to_current"] for r in rows if r["rev_first_to_current"] is not None)
    if jul:
        print(f"\n    RED-23 / 2026-07 — REPORTED ON BOTH CUTS, LABELLED:")
        v = jul["rev_first_to_current"]
        rank = sum(1 for x in cur if x <= v)
        print(f"      first→CURRENT: {jul['first_print']:+.0f}K → {jul['current']:+.0f}K = {v:+.0f}K, "
              f"rank {rank}/{len(cur)} — largest upward move on THIS cut, but July sits at its "
              f"2nd estimate while older months carry annual revisions. NOT RED's horizon.")
        if jul["rev_first_to_third"] is None:
            top = sorted(ft3, reverse=True)[:3]
            print(f"      first→THIRD (RED's horizon): 2026-07 HAS NO VALUE — only "
                  f"{jul['n_vintages']} vintages exist; its third estimate is unpublished.")
            print(f"      Upward tail on that cut exceeds July's +44K: "
                  f"{', '.join(f'{x:+.0f}K' for x in top)} (n={len(ft3)}, stage-OK only).")

    pend = sum(1 for r in rows if r["bench_status"] == "PENDING")
    print(f"\n    PENDING benchmark (excluded from the benchmark cut, never counted as 0): {pend}")
    return res


def write_tsv(rows):
    cols = ["ref_month", "regime", "stage_flag", "first_vintage", "first_print",
            "third_vintage", "third_available", "bench_vintage", "benchmarked",
            "bench_status", "current_vintage", "current", "rev_first_to_third",
            "rev_first_to_bench", "rev_first_to_current", "n_vintages"]
    OUT_TSV.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT_TSV, "w") as f:
        f.write(f"# ALFRED payroll vintage table — PAYEMS headline (MoM, thousands), "
                f"reference months {rows[0]['ref_month']}..{rows[-1]['ref_month']}\n")
        f.write(f"# Last real data refresh: {date.today().isoformat()}\n")
        f.write("# Built by scripts/alfred_vintages.py (WQ-175 clause 2 / DOCKET L274). "
                "Headline = level(M) - level(M-1) computed WITHIN one vintage. "
                "Regime from FIRST PRINTS ONLY, declared before the bias was computed in-session — but spec and results share commit e96453b45, so this order claim has NO receipt (DAEDALUS 2026-09-07). "
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
