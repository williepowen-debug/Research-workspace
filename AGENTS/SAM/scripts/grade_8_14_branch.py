#!/usr/bin/env python3
"""
SAM — 2026-08-14 COT branch grader (forum-4 frozen letter).

Grades the Aug-11 JPY COT vintage against the branch table pre-registered in
  FORUM/2026-08-10_positioning-exhaustion/03_falsifiers/04_SAM_falsifiers.md §2.1
on the CORRECTED basis R = -188,077 [2007-06-26, n=1,354].

⚠️ THE BOUNDARIES BELOW ARE THE FROZEN LETTER. Do not re-tune at scoring time.
   That refusal is the whole point of the 8/7 precedent (SAM-40 was graded on the
   letter and FAILED on the letter). Any edit to these constants after the print
   invalidates the grade.

Independent leg: pulls raw deafut.txt and hand-parses it, so the grade never rests
on cftc_jpy.py alone (the 8/7 dual-source standard, which matched to the contract).

Usage:
  .venv/bin/python3 AGENTS/SAM/scripts/grade_8_14_branch.py
  .venv/bin/python3 AGENTS/SAM/scripts/grade_8_14_branch.py --net -50000 --oi 420000  # dry-run
"""

import argparse
import re
import sys
import urllib.request

# ---------------------------------------------------------------- FROZEN LETTER
R_CORRECTED = -188_077          # full-record extremum, 2007-06-26, OI 352,299, n=1,354
BASE_NET = -45_473              # 8/4 vintage
BASE_OI = 419_393
MEDIAN_WEEK = 12_160            # median |dnet|, trailing 104 week-pairs
MEDIAN_DOI = 10_872             # median |dOI|, trailing 104
LEG1_LINE = -112_846            # corrected 60%-of-R leg-1 invalidation line
KILL1_BUILD = 67_373            # KILL SPEC #1 cumulative-build leg
KILL1_DOI = 21_744              # KILL SPEC #1 OI leg (2 median weeks)
EXPECTED_REPORT_DATE = "2026-08-11"

# (label, lo, hi, prior) — half-open [lo, hi); None = unbounded
BRANCHES = [
    ("B1  RE-BUILD >=2 median wks",      None,      -69_793,  0.08),
    ("B2  MILD RE-BUILD 1-2 wks",        -69_793,   -57_633,  0.14),
    ("B0  NO-VERDICT BAND (+/-1 wk)",    -57_633,   -33_313,  0.52),
    ("B3  FURTHER COVER 1-2 wks",        -33_313,   -21_153,  0.14),
    ("B4  NEAR-FLAT / NET LONG >=2 wks", -21_153,   None,     0.10),
]

CFTC_URL = "https://www.cftc.gov/dea/newcot/deafut.txt"
JPY = "JAPANESE YEN - CHICAGO MERCANTILE EXCHANGE"
UA = {"User-Agent": "Mozilla/5.0 (SAM-Research)"}


def pull_raw():
    """Independent hand-parse of deafut.txt — the second source."""
    req = urllib.request.Request(CFTC_URL, headers=UA)
    with urllib.request.urlopen(req, timeout=20) as r:
        text = r.read().decode("utf-8", errors="replace")
    for line in text.splitlines():
        if JPY in line:
            f = [x.strip() for x in line.split(",")]
            date = f[2].strip()
            oi, nc_long, nc_short = int(f[7]), int(f[8]), int(f[9])
            return {"report_date": date, "oi": oi, "long": nc_long,
                    "short": nc_short, "net": nc_long - nc_short, "raw_fields": f}
    return None


def grade(net, oi, report_date=None):
    out = []
    a = out.append
    a("=" * 74)
    a("  SAM 8/14 BRANCH GRADE — forum-4 frozen letter, corrected basis")
    a("=" * 74)

    if report_date and report_date != EXPECTED_REPORT_DATE:
        a(f"  report_date = {report_date!r} != {EXPECTED_REPORT_DATE}")
        a("  >>> B5  NO PUBLISH / WRONG VINTAGE — registered NO-READ (prior 2%)")
        a("  >>> Never grade last week's row as this week's.")
        return "\n".join(out), "B5"

    dnet = net - BASE_NET
    doi = oi - BASE_OI
    pct_R = 100.0 * net / R_CORRECTED
    net_oi = 100.0 * net / oi if oi else float("nan")

    a(f"  Vintage        : {report_date or 'n/a'}   (expected {EXPECTED_REPORT_DATE})")
    a(f"  Net noncomm    : {net:,}   (prior {BASE_NET:,},  WoW {dnet:+,})")
    a(f"  Open interest  : {oi:,}   (prior {BASE_OI:,},  WoW {doi:+,})")
    a(f"  % of R         : {pct_R:.1f}%   of corrected R = {R_CORRECTED:,}")
    a(f"                   (legacy -180,000 basis would read {100.0*net/-180000:.1f}% — RETIRED, do not cite)")
    a(f"  net/OI         : {net_oi:.2f}%")
    a(f"  WoW in median weeks: {dnet/MEDIAN_WEEK:+.2f}   (1 wk = {MEDIAN_WEEK:,})")
    a("")

    verdict = None
    a("  BRANCH TABLE (frozen; boundaries in CONTRACTS)")
    for label, lo, hi, prior in BRANCHES:
        lo_ok = (lo is None) or (net > lo)
        hi_ok = (hi is None) or (net < hi)
        # B1 is net <= -69,793 ; B2 upper bound inclusive ; B3 lower inclusive
        if label.startswith("B1"):
            hit = net <= -69_793
        elif label.startswith("B2"):
            hit = -69_793 < net <= -57_633
        elif label.startswith("B0"):
            hit = -57_633 < net < -33_313
        elif label.startswith("B3"):
            hit = -33_313 <= net < -21_153
        else:
            hit = net >= -21_153
        mark = " <<< FIRED" if hit else ""
        if hit:
            verdict = label.split()[0]
        a(f"    {label:<34} prior {prior:>5.0%}{mark}")
    a("")

    # ---- companion 1: open interest (MANDATORY)
    a("  COMPANION 1 — OPEN INTEREST (mandatory; bar |dOI| = %s)" % f"{MEDIAN_DOI:,}")
    covering = dnet > 0      # net rising toward zero = shorts covering
    building = dnet < 0      # net falling = shorts rebuilding
    if doi <= -MEDIAN_DOI and covering:
        oi_read = "LIQUIDATION — market shrinking as the crowd covers"
    elif doi >= MEDIAN_DOI and building:
        oi_read = "FRESH MONEY — new crowd entering (KILL SPEC #1 second leg)"
    elif abs(doi) < MEDIAN_DOI:
        oi_read = "FLAT — |dOI| under the bar: NO MECHANISM READ, state it as such"
    else:
        oi_read = f"dOI {doi:+,} does not pair with the net direction — report both, claim neither"
    a(f"    dOI {doi:+,}  ->  {oi_read}")
    a("")

    # ---- frame + kill spec
    a("  FRAME EFFECT")
    dist = LEG1_LINE - net
    a(f"    leg-1 line {LEG1_LINE:,};  this print is {abs(dist):,} contracts away "
      f"({abs(dist)/MEDIAN_WEEK:.2f} median weeks)")
    ks1_leg1 = net <= LEG1_LINE
    ks1_leg2 = doi >= KILL1_DOI
    a(f"    KILL SPEC #1 leg 1 (net through {LEG1_LINE:,}) : {'FIRED' if ks1_leg1 else 'NOT MET'}")
    a(f"    KILL SPEC #1 leg 2 (dOI >= {KILL1_DOI:,})       : {'FIRED' if ks1_leg2 else 'NOT MET'}")
    a(f"    => KILL SPEC #1 : {'FIRED' if (ks1_leg1 and ks1_leg2) else 'NOT FIRED (needs BOTH legs)'}")
    a("    => FRAME: LOW, unchanged. No branch of this print re-arms Channel 4.")
    a("")
    a("=" * 74)
    a(f"  VERDICT: {verdict}")
    if verdict == "B0":
        a("  B0 IS A NO-VERDICT. It is NOT confirmation of anything.")
        a("  The instrument is saying nothing, and that is the pre-registered modal outcome.")
    a("=" * 74)
    return "\n".join(out), verdict


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--net", type=int)
    p.add_argument("--oi", type=int)
    p.add_argument("--date", type=str)
    args = p.parse_args()

    if args.net is not None and args.oi is not None:
        txt, v = grade(args.net, args.oi, args.date or EXPECTED_REPORT_DATE)
        print(txt)
        return

    d = pull_raw()
    if not d:
        print("  FAIL — JPY row not found in deafut.txt. Do NOT grade. Treat as B5 pending re-pull.")
        sys.exit(1)
    print(f"  [raw deafut.txt hand-parse] date={d['report_date']} OI={d['oi']:,} "
          f"long={d['long']:,} short={d['short']:,} net={d['net']:,}")
    print()
    txt, v = grade(d["net"], d["oi"], d["report_date"])
    print(txt)


if __name__ == "__main__":
    main()
