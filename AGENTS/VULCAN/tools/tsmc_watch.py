#!/usr/bin/env python3
"""
tsmc_watch.py — VULCAN S4 instrument: retain a PRIMARY-sourced TSMC monthly-revenue series.

WHY THIS EXISTS (2026-08-21): S4 (supply-chain / geopolitics) is scored on TSMC's monthly
revenue line, and on 2026-08-21 that read was found **35 DAYS STALE ON A MONTHLY SERIES** —
it still carried the June print while July had filed on 8/10. Nothing pulled it, so nothing
noticed. Same root cause as the Mag-7 six-week rot that produced `tools/mag7.py`: a
load-bearing number with no instrument decays silently, and the desk's own freshness checks
all pass because they check the files, not the world.

⚠️ THE MEASURED PATTERN, worth more than either tool: on the 2026-08-21 audit, **the only
   two channels that stayed clean all day were the two that had instruments.** S3, S4 and S5
   had none. That is not a coincidence about carefulness.

SOURCE — and why this one:
  SEC EDGAR, TSMC's own Form 6-K monthly revenue release. CIK 0001046179.
  ISSUER-PRIMARY, free, no auth, stable JSON index. This is the same accession STATUS
  already cites by number (e.g. 0001046179-26-000471 for the July print), so the tool and
  the narrative provably read the SAME artifact rather than two sources that agree.
  Selector: form == "6-K" AND primaryDocument matches `tsm-revenue<YYYYMMDD>.htm`.
  ⚠️ The revenue MONTH comes from EDGAR's own `reportDate` (a month-end), NEVER from the
     filename date or from counting back from today. TSMC files ~the 10th for the PRIOR
     month; inferring the month from the filing date is off-by-one every single time.

VALIDATION (every run, ZERO free parameters — `finding_crosscheck_with_free_parameter_
validates_nothing`): the filing states BOTH the raw NT$ million figures AND the computed
percentages. Recompute all three from the raw figures and compare to the stated ones:
     MoM%   from month / prior-month
     YoY%   from month / year-ago-month
     YTD%   from cumulative / prior-year cumulative
  Three independent checks, no unknowns, tolerance 0.1pp (the filing rounds to 0.1).
  ANY mismatch ⇒ the row is NOT written. A parse that silently half-works is worse than a
  crash, because the half that breaks is the half carrying the newest evidence [L-16].

BANDING — and the one judgement call in this file, stated openly:
  VULCAN's THRESHOLDS table reads "TSMC monthly revenue (YoY): decel / flat / decline".
  `flat` and `decline` are unambiguous and are graded on the MONTHLY YoY.
  `decel` is NOT, and grading it on the monthly YoY would fire constantly on base effects —
  this desk has already been burned twice by exactly that (June-2026's +67.9% YoY was a
  base artifact off the June-2025 trough, and STATUS's standing instruction is therefore
  "CITE THE CUMULATIVE"). So `decel` is graded on the CUMULATIVE Jan-to-date YoY falling
  versus the prior month's cumulative YoY. The cumulative is the smoothed series; a decel
  in it is a real inflection, a decel in the monthly is usually arithmetic.
  ⚠️ Consequence, stated so it is not mistaken for a bug: `decel` CANNOT be graded on the
     first row of the series (no prior cumulative). It reports UNGRADEABLE, never a silent
     downgrade to no-stress — the `mag7.py` breadth-leg rule, applied here.

Usage:
  .venv/bin/python AGENTS/VULCAN/tools/tsmc_watch.py [--dry-run] [--backfill N] [--show N]
"""

import argparse
import csv
import gzip
import html
import json
import os
import re
import sys
import tempfile
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

TOOLS = Path(__file__).resolve().parent
VULCAN = TOOLS.parent
REPO = VULCAN.parent.parent
SERIES = VULCAN / "workbook" / "S4_SERIES.tsv"

CIK = 1046179
SUB_URL = f"https://data.sec.gov/submissions/CIK{CIK:010d}.json"
ARCH = f"https://www.sec.gov/Archives/edgar/data/{CIK}"
# SEC requires a descriptive UA with contact. Declared, not spoofed.
UA = "VULCAN-research (Research-workspace agent; contact williepowen@gmail.com)"
REV_DOC = re.compile(r"^tsm-revenue(\d{8})\.htm$", re.I)
TOL_PP = 0.1          # the filing rounds percentages to 0.1
FLAT_BAND_PCT = 2.0   # |YoY| under this = "flat"
# consecutive months of CUMULATIVE-YoY decline required to call "decel".
# Base-rated on the 20-month backfill before shipping — see band().
DECEL_MIN_RUN = 2

COLS = ["asof_utc", "revenue_month", "filed", "accession",
        "rev_ntd_mn", "prior_month_ntd_mn", "mom_pct", "yoy_pct",
        "year_ago_ntd_mn", "ytd_ntd_mn", "ytd_prior_ntd_mn", "ytd_yoy_pct",
        "ytd_yoy_prev_month_pct", "decel_run_mo", "ytd_is_month", "band", "validation", "source"]


def _get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA,
                                               "Accept-Encoding": "gzip, deflate"})
    d = urllib.request.urlopen(req, timeout=45).read()
    if d[:2] == b"\x1f\x8b":
        d = gzip.decompress(d)
    return d


def _text(url):
    raw = _get(url).decode("utf-8", "replace")
    t = re.sub(r"<[^>]+>", " ", raw)
    return re.sub(r"\s+", " ", html.unescape(t)).strip()


def revenue_filings(limit):
    """[(reportDate, filingDate, accession, docname)] newest-first, monthly-revenue 6-Ks only."""
    j = json.loads(_get(SUB_URL))
    r = j["filings"]["recent"]
    out = []
    for form, fdate, acc, doc, rdate in zip(r["form"], r["filingDate"],
                                            r["accessionNumber"], r["primaryDocument"],
                                            r["reportDate"]):
        if form == "6-K" and REV_DOC.match(doc or ""):
            out.append((rdate, fdate, acc, doc))
    return out[:limit]


def _num(x):
    """Accounting notation: '(1.1)' means -1.1. See PARSE DEFECT note in parse()."""
    x = x.strip().replace(",", "")
    if x.startswith("(") and x.endswith(")"):
        return -float(x[1:-1])
    return float(x)


# One number cell: plain, signed, or parenthesised-negative.
_N = r"\(?-?[\d,]+\.?\d*\)?"


def parse(txt):
    r"""Pull the raw figures + stated percentages out of the 6-K table.

    The release carries the numbers TWICE — once in prose ("approximately NT$467.58
    billion, an increase of 5.6 percent...") and once in an exact NT$ million table.
    We parse the TABLE (exact) and never the prose, which is rounded to 2 significant
    figures — a 2-sig-fig figure cannot support a band call.

    🔴 PARSE DEFECT FOUND AND FIXED 2026-08-21, ON THIS TOOL'S FIRST BACKFILL — recorded
       because the CLASS matters more than the fix:
       v1's number pattern was `-?[\d.]+`. TSMC renders negative percentages in
       ACCOUNTING PARENTHESES — `(1.1)`, not `-1.1`. So v1 failed to parse EVERY MONTH IN
       WHICH REVENUE FELL, and reported those months as `ERR:table-row-not-matched`.
       ⚠️ Why this was worse than an ordinary bug: **S4's RED band is "decline."** An
          instrument that cannot represent a decline, grading a channel whose red band IS
          decline, is UNTRIPPABLE BY CONSTRUCTION
          (`finding_banded_threshold_with_no_metric_surface_is_untrippable`) — the same
          defect mag7.py v1 had on its breadth leg, here on the SIGN rather than a leg.
       ⚠️ And the failure was DIRECTIONAL: it discarded precisely the bearish observations
          while writing every benign one. That is L-16 with a sharper edge — a partial run
          is not merely incomplete, it is BIASED TOWARD PRESERVING PRIORS. 8 of 16 months
          failed; the tool still wrote 8 clean-looking rows and returned a series that
          would have read as uninterrupted growth.
       ⇒ Any future band/threshold parser on this desk gets a test on a NEGATIVE period
         before it is trusted. Absence of a bearish print is not evidence of its absence.

    SECOND CAUSE, benign: JANUARY filings carry no cumulative columns — January IS the
    year-to-date, so TSMC prints no "January to January" block. The cumulative group is
    therefore OPTIONAL, and for a January row the cumulative legs equal the monthly ones.
    """
    m = re.search(
        r"Net Revenue\s+(" + _N + r")\s+(" + _N + r")\s+(" + _N + r")\s+"
        r"(" + _N + r")\s+(" + _N + r")"
        r"(?:\s+(" + _N + r")\s+(" + _N + r")\s+(" + _N + r"))?", txt)
    if not m:
        return None, "ERR:table-row-not-matched"
    g = m.groups()
    try:
        d = dict(rev=_num(g[0]), prior=_num(g[1]), mom=_num(g[2]),
                 yago=_num(g[3]), yoy=_num(g[4]))
        if g[5] is not None:
            d.update(ytd=_num(g[5]), ytd_prior=_num(g[6]), ytd_yoy=_num(g[7]))
            d["ytd_is_month"] = False
        else:
            # January: the month IS the cumulative. Marked, never silently synthesised.
            d.update(ytd=d["rev"], ytd_prior=d["yago"], ytd_yoy=d["yoy"])
            d["ytd_is_month"] = True
    except ValueError:
        return None, "ERR:non-numeric-in-table"
    if not (d["rev"] > 0 and d["prior"] > 0 and d["yago"] > 0 and d["ytd_prior"] > 0):
        return None, "ERR:non-positive-figure"
    # range validation — TSMC monthly revenue has been NT$100bn-NT$1tn for years.
    if not (50_000 <= d["rev"] <= 2_000_000):
        return None, f"ERR:rev-out-of-range({d['rev']:.0f}NT$mn)"
    return d, None


def validate(d):
    """THREE independent recomputations, zero free parameters. All must agree."""
    checks = [("MoM", (d["rev"] / d["prior"] - 1) * 100, d["mom"]),
              ("YoY", (d["rev"] / d["yago"] - 1) * 100, d["yoy"]),
              ("YTD", (d["ytd"] / d["ytd_prior"] - 1) * 100, d["ytd_yoy"])]
    worst, bad = 0.0, []
    for name, calc, stated in checks:
        err = abs(calc - stated)
        worst = max(worst, err)
        if err > TOL_PP:
            bad.append(f"{name}(calc {calc:.2f} vs stated {stated:.2f})")
    if bad:
        return None, "ERR:validation-failed:" + ";".join(bad)
    return f"OK:3-recomputed-from-raw,worst-err={worst:.3f}pp", None


def band(d, prev_ytd_yoy, decel_run=0):
    """decline / flat = MONTHLY YoY. decel = CUMULATIVE YoY falling for N+ CONSECUTIVE months.

    ⚠️ BASE-RATED ON THE 20-MONTH BACKFILL BEFORE SHIPPING, not chosen to look decisive
       (`finding_base_rate_the_threshold_before_building_it`). v1 fired `decel` on a SINGLE
       month-over-month fall in the cumulative, and measured that way it fired **10/20
       months = 50%**. A yellow band that is lit half the time carries no information.
       The cause was visible in the series: 2025 was a genuine 8-month deceleration run
       (cum YoY 43.5 -> 31.6) while 2026 OSCILLATES (36.8, 29.9, 35.1, 29.9, 30.0, 35.6,
       37.0), so a 1-month comparison fires on every down-tick of a choppy series and
       conflates "decelerating trend" with "noisy month".

         N>=1 : 10/20 (50%)  — 2025: 8 · 2026: 2   <- v1; both 2026 fires are runs of ONE
         N>=2 :  7/20 (35%)  — 2025: 7 · 2026: 0   <- CHOSEN
         N>=3 :  6/20 (30%)  — 2025: 6 · 2026: 0

       N=2 removes BOTH 2026 false fires while retaining 7 of the 8 months of the real 2025
       decel — clean separation on this sample. ⚠️ And N=2 is PRINCIPLED, not fitted: this
       desk's own standing discipline reads "'sustained' always carries N+ sessions", and
       `decel` is a TREND word — a trend claim on a single observation is not a trend. N=2
       is the minimum defensible value for any trend claim, so it was not selected by
       scanning for the prettiest number.
       ⚠️ 35% is still high for a "watch" band. It is honest about what it measures — TSMC
          spent most of 2025 genuinely decelerating — but do NOT read yellow as a signal to
          act. Yellow is "look"; the ACTIONABLE bands are flat and decline.

    ⚠️ RED (`decline`, monthly YoY < 0) has occurred **0 times in these 20 months**. That is
       reported, not hidden: the band is REACHABLE (proven by fixture test 2026-08-21) but
       unobserved in-sample, so it carries no base rate and must not be presented as one.
    """
    if d["yoy"] < 0:
        return "red-decline"
    if d["yoy"] < FLAT_BAND_PCT:
        return "orange-flat"
    if prev_ytd_yoy is None:
        return "no-stress(decel-UNGRADEABLE:no-prior-cumulative)"
    if d["ytd_yoy"] < prev_ytd_yoy:
        if decel_run + 1 >= DECEL_MIN_RUN:
            return f"yellow-decel(cum {prev_ytd_yoy:.1f}->{d['ytd_yoy']:.1f}, run {decel_run+1}mo)"
        return (f"no-stress(cum ticked down {prev_ytd_yoy:.1f}->{d['ytd_yoy']:.1f} but run=1 "
                f"<{DECEL_MIN_RUN}mo — a trend claim needs {DECEL_MIN_RUN}+ observations)")
    return "no-stress"


def read_series():
    if not SERIES.exists():
        return []
    with open(SERIES, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def write_series(rows):
    """Atomic + whole-file field-count check (`finding_partial_record_written_as_final_
    never_heals`): a ragged half-written ledger is permanent."""
    fd, tmp = tempfile.mkstemp(dir=str(SERIES.parent), suffix=".tmp")
    os.close(fd)
    with open(tmp, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=COLS, delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    lines = open(tmp, encoding="utf-8").read().rstrip("\n").split("\n")
    widths = {len(r) for r in csv.reader(lines, delimiter="\t")}
    if len(widths) != 1:
        os.unlink(tmp)
        raise SystemExit(f"REFUSING TO WRITE — ragged field counts {sorted(widths)}")
    os.replace(tmp, SERIES)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--backfill", type=int, default=1,
                    help="how many recent monthly 6-Ks to pull (default 1 = newest)")
    ap.add_argument("--show", type=int, default=0)
    a = ap.parse_args()

    existing = read_series()
    if a.show:
        for r in existing[-a.show:]:
            print(f"{r['revenue_month']}  NT${float(r['rev_ntd_mn']):>10,.0f}mn  "
                  f"MoM {r['mom_pct']:>6}%  YoY {r['yoy_pct']:>6}%  "
                  f"YTD {r['ytd_yoy_pct']:>6}%  {r['band']}")
        return 0

    have = {r["revenue_month"] for r in existing}
    try:
        filings = revenue_filings(a.backfill)
    except Exception as e:
        print(f"🔴 ERR: EDGAR submissions index unreachable ({type(e).__name__}: {e})")
        return 2
    if not filings:
        print("🔴 ERR: no monthly-revenue 6-K matched the selector — CHECK THE SELECTOR, "
              "do not assume TSMC stopped filing")
        return 2

    rows, added, failed = list(existing), 0, 0
    for rdate, fdate, acc, doc in sorted(filings):        # oldest-first so cum-decel works
        if rdate in have and not a.dry_run:
            continue
        url = f"{ARCH}/{acc.replace('-','')}/{doc}"
        try:
            txt = _text(url)
        except Exception as e:
            print(f"  🔴 {rdate}: fetch failed ({type(e).__name__}) — {url}")
            failed += 1
            continue
        d, err = parse(txt)
        if err:
            print(f"  🔴 {rdate}: {err} — NOT WRITTEN")
            failed += 1
            continue
        vs, verr = validate(d)
        if verr:
            print(f"  🔴 {rdate}: {verr} — NOT WRITTEN")
            failed += 1
            continue
        prev = None
        for r in sorted(rows, key=lambda x: x["revenue_month"]):
            if r["revenue_month"] < rdate and r["ytd_yoy_pct"]:
                # only the immediately-preceding month of the SAME calendar year:
                # a Jan cumulative is not comparable to the prior Dec's.
                if r["revenue_month"][:4] == rdate[:4]:
                    prev = float(r["ytd_yoy_pct"])
        run = 0
        hist = [r for r in sorted(rows, key=lambda x: x["revenue_month"])
                if r["revenue_month"] < rdate]
        for r in reversed(hist):
            if r["revenue_month"][:4] != rdate[:4]:
                break                      # runs do not cross the cumulative's year reset
            try:
                if r["ytd_yoy_prev_month_pct"] and \
                        float(r["ytd_yoy_pct"]) < float(r["ytd_yoy_prev_month_pct"]):
                    run += 1
                    continue
            except ValueError:
                pass
            break
        b = band(d, prev, run)
        row = dict(asof_utc=datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
                   revenue_month=rdate, filed=fdate, accession=acc,
                   rev_ntd_mn=f"{d['rev']:.0f}", prior_month_ntd_mn=f"{d['prior']:.0f}",
                   mom_pct=f"{d['mom']:.1f}", yoy_pct=f"{d['yoy']:.1f}",
                   year_ago_ntd_mn=f"{d['yago']:.0f}", ytd_ntd_mn=f"{d['ytd']:.0f}",
                   ytd_prior_ntd_mn=f"{d['ytd_prior']:.0f}", ytd_yoy_pct=f"{d['ytd_yoy']:.1f}",
                   ytd_yoy_prev_month_pct=("" if prev is None else f"{prev:.1f}"),
                   decel_run_mo=str(run + 1 if (prev is not None and d["ytd_yoy"] < prev) else 0),
                   ytd_is_month=("YES-january-no-cumulative-block" if d["ytd_is_month"] else ""),
                   band=b, validation=vs,
                   source=f"SEC 6-K {acc} (issuer-primary, EDGAR CIK {CIK:010d})")
        print(f"  ✓ {rdate}  NT${d['rev']:>10,.0f}mn  MoM {d['mom']:>6.1f}%  "
              f"YoY {d['yoy']:>6.1f}%  YTD {d['ytd_yoy']:>5.1f}%  [{b}]  {vs}")
        if rdate not in have:
            rows.append(row)
            added += 1

    if failed and not added:
        print(f"🔴 ALL {failed} attempted month(s) FAILED — treat as a FAILED RUN, not a "
              f"degraded one: the leg that breaks carries the newest evidence [L-16]")
        return 2
    if failed:
        print(f"🔴 PARTIAL: {added} written, {failed} FAILED — a partial run is a FAILED run")
    if a.dry_run:
        print(f"[dry-run] {added} new row(s) would be appended to {SERIES.relative_to(REPO)}")
        return 1 if failed else 0
    if added:
        rows.sort(key=lambda r: r["revenue_month"])
        write_series(rows)
        print(f"→ {added} row(s) appended · {SERIES.relative_to(REPO)} now {len(rows)} rows")
    else:
        print("→ no new months (series already current)")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
