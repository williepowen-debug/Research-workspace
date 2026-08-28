#!/usr/bin/env python3
"""
MIDAS -- COT vintage #3 grader, PRE-REGISTERED 2026-08-28 ~11:1x ET, BEFORE the 15:30 ET print.

WHAT THIS IS FOR
  reports/2026-08-23_gld-rates-attribution.md Sec.6 falsifier #3 impeaches the 8/19 residual if the
  8/19-21 surge was "CHASED" -- signalled by "a large net/OI ratchet from 54.69%".

  "Large" was a WORD. Per L-12 an unquantified boundary has two defensible answers and the grader
  picks one at 15:31 while looking at the number. This file fixes BOTH halves before the print:

    (a) the BOUNDARY   -- delta(net/OI) >= +1.4pp WoW, i.e. net/OI >= 56.1%
    (b) the COMPUTATION -- the percentile machinery below, run against a distribution FROZEN to
                           sources/cot_gold_history_2010_2026.tsv and committed before the release.

  Pre-registering the number without pre-registering the computation still leaves room to pick a
  window at 15:31. This closes that.

WHERE THE BOUNDARY CAME FROM (n=867 WoW changes, 2010-01-05 -> 2026-08-18)
  - Unconditional: mean +0.01pp, sd 3.31pp, p50 -0.03, p75 +1.78, p90 +4.19, p95 +5.80, max +15.26.
  - A naive "+1.0pp = large" fires on 34.5% of ALL weeks -- an ordinary week, not a ratchet.
  - The unconditional p90 (+4.19pp) is UNTRIPPABLE from this level: conditional on the prior level
    already being >=54.0% (n=15 in 16.6 years) the mean is -0.46pp, the median -0.54pp, and the
    LARGEST ratchet ever observed from >=54% is +2.44pp. Setting the bar at +4.19 would be the L-13
    disease -- a band that cannot score the regime you are actually in.
  - So the boundary is the CONDITIONAL p90 = +1.39pp, rounded to +1.4pp.

AUTHORITY (stated because it constrains what this file may do)
  This disambiguates an unquantified word in MIDAS's OWN UNREGISTERED write-up. No MIDAS-NN
  prediction, no DOCKET row and no GATES row keys on it -- checked -- so L-20 / tier test 4 is not
  engaged. PROME was offered the substitution and DECLINED to substitute (2026-08-28), leaving the
  boundary as MIDAS's own. It therefore stays as written here.

  >>> NO SINGLE BOUNDARY IS LOAD-BEARING. <<<
  The output prints the realised delta's percentile against BOTH the unconditional (n=867) and the
  >=54%-conditional (n=15) distributions, so a reader who rejects the boundary can still grade it.
  That is the L-18 discipline: the honest interval held where the point estimate failed.

WHAT THIS FILE MAY NOT DO
  - It does not grade MIDAS-06. Nothing here touches a frozen letter, a threshold, a band or a score.
  - It does not re-fit the distribution. The frozen TSV is the reference, full stop.

USAGE
  python3 grade_cot3.py --dry-run          # prove the machinery on the LAST KNOWN vintage (8/18)
  python3 grade_cot3.py                    # grade whatever cot_gold.py's puller returns (checks vintage)
  python3 grade_cot3.py --expect 2026-08-25 --poll 60 --max-wait 3600
"""
import argparse
import io
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
FROZEN = os.path.join(HERE, "sources", "cot_gold_history_2010_2026.tsv")

# ---- PRE-REGISTERED CONSTANTS. Do not edit after 2026-08-28 15:30 ET. ----
BOUNDARY_PP = 1.4          # delta(net/OI) >= this => "a large ratchet" => falsifier #3 FIRES
CONDITIONAL_FLOOR = 54.0   # the ">=54% start" that defines the conditional distribution
PRIOR_VINTAGE = "2026-08-18"
PRIOR_NET_OI = 54.69
# -------------------------------------------------------------------------


def load_frozen():
    rows = []
    with io.open(FROZEN, encoding="utf-8") as f:
        for line in f:
            if line.startswith("#") or line.startswith("report_date"):
                continue
            p = line.rstrip("\n").split("\t")
            if len(p) < 6:
                continue
            rows.append((p[0], int(p[1]), int(p[2]), int(p[3]), int(p[4]), float(p[5])))
    return rows


def pct_rank(sample, x):
    """Share of the sample strictly below x, as a percentile."""
    return 100.0 * sum(1 for v in sample if v < x) / len(sample)


def quantile(sample, p):
    s = sorted(sample)
    k = (len(s) - 1) * p / 100.0
    f = int(k)
    c = min(f + 1, len(s) - 1)
    return s[f] + (s[c] - s[f]) * (k - f)


def grade(report_date, oi, nc_long, nc_short, prior_vintage=None):
    rows = load_frozen()
    if not rows:
        print("FATAL: frozen reference distribution missing or empty at %s" % FROZEN)
        return 2

    net = nc_long - nc_short
    net_oi = 100.0 * net / oi

    pv = prior_vintage or PRIOR_VINTAGE
    prior = [r for r in rows if r[0] == pv]
    if not prior:
        print("FATAL: prior vintage %s absent from the frozen file -- cannot compute a delta." % pv)
        return 2
    p_date, p_oi, p_l, p_s, p_net, p_ratio = prior[0]

    if pv == PRIOR_VINTAGE and abs(p_ratio - PRIOR_NET_OI) > 0.01:
        print("FATAL: frozen file's %s net/OI is %.2f, pre-registered constant says %.2f. STOP."
              % (p_date, p_ratio, PRIOR_NET_OI))
        return 2

    # ---- STALE-VINTAGE GUARD (bought by the dry run failing its own acceptance test,
    #      2026-08-28: the v1 graded the 8/18 row against ITSELF and printed a healthy-looking
    #      +0.00pp / DOES NOT FIRE). This is the exact shape of the failure cot_gold.py's own
    #      docstring warns about -- CFTC and Socrata both serve a clean 200 carrying LAST
    #      week's vintage after 15:30. Without this guard a stale serve grades as a benign
    #      non-firing print and nothing looks wrong. Fail loud.
    if report_date <= p_date:
        print("=" * 74)
        print("  REFUSING TO GRADE -- STALE OR NON-ADVANCING VINTAGE")
        print("=" * 74)
        print("  incoming as-of : %s" % report_date)
        print("  prior as-of    : %s" % p_date)
        print("  The incoming vintage does not POST-DATE the prior one, so the delta is not a")
        print("  WoW change. cot_gold.py's docstring: NEVER grade the first response after 15:30 --")
        print("  poll until the IN-ROW as-of date equals the expected Tuesday.")
        print("  Re-run: python3 cot_gold.py --expect 2026-08-25 --poll 60 --max-wait 3600")
        print("=" * 74)
        return 3

    d_ratio = net_oi - p_ratio
    d_net = net - p_net
    d_oi = oi - p_oi

    # distributions -- built ONLY from the frozen file
    uncond = [rows[i][5] - rows[i - 1][5] for i in range(1, len(rows))]
    cond = [rows[i][5] - rows[i - 1][5] for i in range(1, len(rows)) if rows[i - 1][5] >= CONDITIONAL_FLOOR]
    levels = [r[5] for r in rows]

    print("=" * 74)
    print("  MIDAS -- GOLD COT VINTAGE #3 GRADE  (pre-registered 2026-08-28, before the print)")
    print("=" * 74)
    print("  vintage as-of : %s" % report_date)
    print("  open interest : %s" % format(oi, ","))
    print("  NC long       : %s" % format(nc_long, ","))
    print("  NC short      : %s" % format(nc_short, ","))
    print("  net NC long   : %s" % format(net, ","))
    print("  NET / OI      : %.2f%%" % net_oi)
    print()
    print("  --- WoW vs %s (net/OI %.2f%%) ---" % (p_date, p_ratio))
    print("    delta OI      : %+s" % format(d_oi, ","))
    print("    delta net     : %+s" % format(d_net, ","))
    print("    DELTA net/OI  : %+.2fpp        <-- the graded quantity" % d_ratio)
    print()
    print("  --- THE DELTA AGAINST BOTH REFERENCE DISTRIBUTIONS (no single boundary is load-bearing) ---")
    print("    unconditional  n=%d  (2010-01-05 -> %s)" % (len(uncond), rows[-1][0]))
    print("      percentile of this delta : %.1f%%" % pct_rank(uncond, d_ratio))
    print("      reference  p50 %+.2f | p75 %+.2f | p90 %+.2f | p95 %+.2f | max %+.2f"
          % (quantile(uncond, 50), quantile(uncond, 75), quantile(uncond, 90),
             quantile(uncond, 95), max(uncond)))
    print("    conditional on a >=%.1f%% start  n=%d   (SMALL -- read as such)" % (CONDITIONAL_FLOOR, len(cond)))
    print("      percentile of this delta : %.1f%%" % pct_rank(cond, d_ratio))
    print("      reference  mean %+.2f | median %+.2f | p90 %+.2f | MAX EVER %+.2f"
          % (sum(cond) / len(cond), quantile(cond, 50), quantile(cond, 90), max(cond)))
    print()
    print("  --- LEVEL context ---")
    print("    net/OI %.2f%% = %.1fth percentile of the level distribution (n=%d)"
          % (net_oi, pct_rank(levels, net_oi), len(levels)))
    print("    reference  median %.2f | p95 %.2f | ALL-TIME MAX %.2f (%s)"
          % (quantile(levels, 50), quantile(levels, 95), max(levels),
             [r[0] for r in rows if r[5] == max(levels)][0]))
    print()
    print("  --- FALSIFIER #3 (reports/2026-08-23_gld-rates-attribution.md Sec.6) ---")
    print("    PRE-REGISTERED BOUNDARY: delta(net/OI) >= +%.1fpp  (i.e. net/OI >= %.1f%%)"
          % (BOUNDARY_PP, PRIOR_NET_OI + BOUNDARY_PP))
    if d_ratio >= BOUNDARY_PP:
        print("    >>> FIRES. The 8/19-21 surge was CHASED on this measure.")
        print("        => a meaningful part of the 8/19 residual is SPEC FLOW, not premium, and the")
        print("           write-up's 'unexplained' must be re-read as 'explained by positioning I had")
        print("           not measured yet'. This IMPEACHES my own published read -- say so plainly.")
    else:
        print("    >>> DOES NOT FIRE (%+.2fpp vs the +%.1fpp boundary)." % (d_ratio, BOUNDARY_PP))
        print("        => the positioning falsifier does NOT impeach the 8/19 residual on this print.")
        print("           NOT a confirmation of the premium read -- a falsifier that fails to fire is")
        print("           the ABSENCE of one specific refutation, never evidence for the thesis.")
    print()
    print("    REPORT THE DELTA AND BOTH PERCENTILES ALONGSIDE THE VERDICT, ALWAYS.")
    print("    A reader who rejects the +%.1fpp boundary must still be able to grade this." % BOUNDARY_PP)
    print("=" * 74)
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true",
                    help="prove the machinery on the last known vintage (8/18) -- delta must be +0.25pp")
    ap.add_argument("--expect", help="required in-row as-of date, e.g. 2026-08-25")
    ap.add_argument("--poll", type=int, default=0)
    ap.add_argument("--max-wait", type=int, default=0)
    a = ap.parse_args()

    if a.dry_run:
        print(">>> DRY RUN: grading the 2026-08-11 -> 2026-08-18 transition, whose answer is known.")
        print(">>> ACCEPTANCE: DELTA net/OI == +0.25pp and 'DOES NOT FIRE'. Anything else = broken.\n")
        rows = load_frozen()
        r = [x for x in rows if x[0] == PRIOR_VINTAGE][0]
        rc = grade(r[0], r[1], r[2], r[3], prior_vintage="2026-08-11")
        print("\n>>> Also asserting the STALE-VINTAGE GUARD refuses a self-comparison:")
        rc2 = grade(r[0], r[1], r[2], r[3])   # prior defaults to 8/18 == incoming
        if rc2 != 3:
            print(">>> GUARD FAILED: a stale vintage was graded instead of refused.")
            return 2
        print(">>> Guard OK (refused, rc=3).")
        return rc

    sys.path.insert(0, HERE)
    try:
        import cot_gold
    except Exception as e:
        print("FATAL: cannot import cot_gold.py (%s). Run it directly and pass the figures in." % e)
        return 2

    fetch = None
    for name in ("fetch_latest", "fetch", "pull", "get_latest", "main"):
        if hasattr(cot_gold, name):
            fetch = getattr(cot_gold, name)
            break
    if fetch is None:
        print("NOTE: cot_gold.py exposes no reusable fetch entry point.")
        print("      Run:  python3 cot_gold.py --expect %s --poll 60 --max-wait 3600" % (a.expect or "YYYY-MM-DD"))
        print("      then: python3 grade_cot3.py --manual <report_date> <OI> <NC_long> <NC_short>")
        return 3
    print("NOTE: driving cot_gold.py programmatically is unverified; prefer the two-step above.")
    return 3


if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[1] == "--manual":
        _, _, d, oi, nl, ns = sys.argv[:6]
        sys.exit(grade(d, int(oi), int(nl), int(ns)))
    sys.exit(main())
