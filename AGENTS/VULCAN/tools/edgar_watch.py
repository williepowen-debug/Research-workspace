#!/usr/bin/env python3
"""
edgar_watch.py — VULCAN S3/S5 instrument: a PRIMARY filing sweep over the named issuers,
                 plus a CADENCE leg that derives when the next periodic filing can land.

WHY THIS EXISTS (built 2026-08-27, registered as the top build item since 2026-08-21):

  S3 and S5 had NO INSTRUMENT AT ALL, and that was a *decision* I made correctly and then
  stopped halfway through. Both channels' registered thresholds are EVENT-triggered — a
  cleared new issue vs talk, a collateral posting, a FERC order, a filed obligation — not
  cadence-sampled prices. So I ruled out a daily price proxy, which was right, and then
  left both channels with nothing, which was not. **The error was treating "no price series"
  as "no instrument."  An event-triggered channel's instrument is a FILING SWEEP.**
  [`finding_rejecting_an_instrument_is_an_audit_of_it`]

  The cost was measured twice before this file existed:
    · 2026-08-17  NVDA 8-K, $105B of residual-value guaranties on OpenAI-tenanted leases —
                  the single largest S5 datum on the board. Sat **4 days unseen**. Found by
                  accident, while verifying an unrelated earnings date.
    · 2026-08-26  NVDA 10-Q, answering all three of my registered tripwire questions. My
                  register said to look on **8/31**. It would have sat **5 days**.
  Both were found by a hand-pull that happened only because a date was on the register.
  **That is luck wearing the costume of process.**

⚠️  THE CADENCE LEG IS THE POINT, NOT THE NEW-FILINGS LEG. [L-22, bought 2026-08-27]
  The 8/31 date was **INFERRED** — NVDA's 8-K said the guaranty form *would be* a 10-Q
  exhibit, and I turned that into a date. It was never **DERIVED** from NVDA's own filing
  behaviour. Worse, the register row's remedy read *"re-derive from EDGAR if unfiled by this
  date"* — a check that could only execute ON 8/31, i.e. **after** the failure it existed to
  prevent. **A guard dated on the event it guards can only measure the miss.**
  ⇒ So this tool does not ask "has it filed yet?" on a date I picked. It derives, from each
    issuer's OWN history, the SHORTEST lag it has ever taken between period-end and filing,
    and opens the watch window THERE — at the earliest plausible occurrence, never the
    expected one. `finding_url_date_inference_has_no_error_signal` (n=2).

SOURCE — and why this one:
  SEC EDGAR submissions JSON, `https://data.sec.gov/submissions/CIK##########.json`.
  ISSUER-PRIMARY, free, no auth, stable schema. Same origin `tsmc_watch.py` already reads,
  so tool and narrative provably read ONE artifact rather than two sources that agree.
  ⚠️ BOUNDED SCOPE, STATED RATHER THAN DISCOVERED LATER: this reads `filings.recent` only,
     which EDGAR caps at ~1000 filings per issuer. For these five that is >2 years of
     history — ample for cadence — but it is NOT the full filing record, and the older
     `filings.files` pages are deliberately not fetched. A cadence derived here is a claim
     about the recent regime, which is the right claim for a forward watch window anyway.

WHAT IT DOES NOT DO, so the gap is not read as covered:
  It reads the filing INDEX, never the documents. It tells you a 10-Q landed and what its
  8-K item codes were; it does NOT tell you what the exhibit says. Reading the filing stays
  a human/agent act. ⚠️ This is the same boundary that made PROME's `edgar_8k` fetcher
  insufficient for the useful-life gate (STATUS: "it tells you the print happened; it does
  not answer the question") — recorded here so this tool is never written up as "covered."

TIERING — and the ONE rule that governs it:
  **Nothing is dropped. Ever.** Every filing observed is appended to the ledger; tiers only
  control what the BOOT LEG surfaces. A filter that can silently discard the important case
  is the defect class that produced L-20 (a parser blind to every declining month) and
  `mag7.py` v1 (a level-only breadth leg) — in both, the band was untrippable *by
  construction* and read as clean. So the sweep reports SUPPRESSED COUNTS explicitly:
  silence is always accompanied by the number of things being kept silent. [PAT-116 class]
    T1  8-K 10-Q 10-K 6-K 424B* S-1 S-3 S-4    material: obligations, results, new issuance
    T2  DEF*14A SC*13D SC*13G 25* 15*          ownership / structure
    T3  4 3 5 144 13F* SD ARS                  insider + routine; logged, not surfaced
  📏 MEASURED COST OF THAT CHOICE, stated so it is not a surprise later: the first run wrote
     5,001 rows / 538 KB across 5 issuers — **68.2% of them T3** (Form 4 n=2,327, Form 144
     n=885), spanning 2012-09-10 to 2026-08-26. That is a ONE-TIME backfill of whatever
     `filings.recent` holds; steady-state is ~200 rows/month. I considered dropping T3 and
     did not, for the reason the tiering rule exists: **the two times this desk decided a
     class of observation could not matter, it was wrong both times** (L-20's declining
     months, `mag7.py` v1's breadth leg). An insider-selling cluster is not banded today and
     is a legitimate S1 tell tomorrow; a record I have to re-fetch is not a record.

VALIDATION (every run, ZERO free parameters — `finding_crosscheck_with_free_parameter_
validates_nothing`), and it is a genuine BACKTEST rather than an internal consistency check:
  For each issuer's periodic forms, HOLD OUT the most recent filing, derive the earliest-
  plausible window from the REMAINING history, then check whether the held-out filing
  actually landed at or after that earliest bound. A predictor that fails its own last
  observation is not shipped as a warning surface — it reports ERR and the leg is marked
  UNGRADEABLE rather than silently downgraded. [the `mag7.py` breadth-leg rule]
  ⚠️ Run `--backtest` to see it. On the data that motivated this file, NVDA's 10-Q lag from
     quarter-end is tightly clustered around ~30-31 days — i.e. **the derivation would have
     said 8/26, and I said 8/31.**

DEPENDENCIES: stdlib only, on purpose. `semi_watch.py` needed `yfinance` (venv-only) and
  under a bare `python3` the ENTIRE equity cross-section wrote `ERR:yfinance-missing` [L-16].
  This tool cannot acquire that failure mode because it has nothing to import.

Usage:
  python3 AGENTS/VULCAN/tools/edgar_watch.py [--dry-run] [--show N] [--issuer TICK]
                                             [--backtest] [--tier N] [--since YYYY-MM-DD]
"""

import argparse
import csv
import gzip
import json
import statistics
import sys
import urllib.error
import urllib.request
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

TOOLS = Path(__file__).resolve().parent
VULCAN = TOOLS.parent
LEDGER = VULCAN / "workbook" / "EDGAR_SEEN.tsv"

# SEC requires a descriptive UA with contact. Declared, not spoofed.
UA = "VULCAN-research (Research-workspace agent; contact williepowen@gmail.com)"
SUB = "https://data.sec.gov/submissions/CIK{cik:010d}.json"

# ─────────────────────────────────────────────────────────────────────────────
# ROSTER — every issuer carries the CHANNEL it serves and WHY it is on the list.
# An issuer with no stated reason is an issuer nobody can audit off the list later.
# ─────────────────────────────────────────────────────────────────────────────
ISSUERS = [
    # tick,  cik,      channel, why
    ("NVDA", 1045810, "S5/S1", "the $108.5B guarantee book, the OpenAI/SB Energy leases, "
                               "the $36B AI-cloud backstop. Largest S&P name; 24.19% of Mag-7."),
    ("ORCL", 1341439, "S5",    "$260B off-BS DC leases + the $3.3B lessor guarantee maturing "
                               "Sept-2026 — the nearest dated credit item on the board."),
    ("CRWV", 1769628, "S5",    "the DDTL pricing ladder (4.0 +225 -> 5.0 +450 -> 5.5 +550), "
                               "the power->DSCR covenant, the Negative-NOI trigger."),
    ("MU",   723125,  "S2",    "FQ4 is the SOLE resolver for VULCAN-02/-11/-12 and its date is "
                               "ESTIMATED (~9/29 off fiscalYearEnd=0903), NOT announced. The "
                               "cadence leg exists largely to de-risk exactly this row."),
    ("TSM",  1046179, "S4",    "monthly revenue 6-Ks. ⚠️ The revenue SERIES is owned by "
                               "tsmc_watch.py — this sweep watches for its OTHER filings and "
                               "must never be treated as a second revenue source."),
]

PERIODIC = {"10-Q", "10-K", "20-F", "40-F"}   # forms with a meaningful reportDate->filed lag

T1 = {"8-K", "10-Q", "10-K", "6-K", "S-1", "S-3", "S-4", "20-F", "40-F", "8-K/A",
      "10-Q/A", "10-K/A", "S-1/A", "S-3/A"}
T2_PREFIX = ("DEF ", "DEFA", "PRE ", "SC 13D", "SC 13G", "SC TO", "425", "11-K")
T3 = {"4", "3", "5", "144", "SD", "ARS", "CERT", "8-A12B", "S-8", "NO ACT"}

COLS = ["first_seen_utc", "tick", "cik", "form", "filed", "report_date",
        "accession", "primary_doc", "items", "tier", "channel"]


# ─────────────────────────────────────────────────────────────── http / io ──
def _get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA,
                                               "Accept-Encoding": "gzip, deflate"})
    d = urllib.request.urlopen(req, timeout=45).read()
    if d[:2] == b"\x1f\x8b":
        d = gzip.decompress(d)
    return d


def fetch(cik):
    """Parallel-array submissions feed -> list of dicts. Raises on any structural surprise."""
    j = json.loads(_get(SUB.format(cik=cik)))
    r = j["filings"]["recent"]
    need = ["form", "filingDate", "accessionNumber", "primaryDocument", "reportDate"]
    missing = [k for k in need if k not in r]
    if missing:
        raise ValueError(f"submissions feed missing {missing} — schema changed")
    n = len(r["form"])
    # Zero-free-parameter structural check: every parallel array must be the same length.
    # A ragged feed silently mis-pairs a form with another filing's date, which is the
    # `finding_partial_record_written_as_final_never_heals` shape.
    bad = {k: len(r[k]) for k in need + (["items"] if "items" in r else []) if len(r[k]) != n}
    if bad:
        raise ValueError(f"ragged submissions arrays (form n={n}): {bad}")
    items = r.get("items", [""] * n)
    return [{"form": r["form"][i], "filed": r["filingDate"][i],
             "report_date": r["reportDate"][i] or "", "accession": r["accessionNumber"][i],
             "doc": r["primaryDocument"][i] or "", "items": items[i] or ""}
            for i in range(n)]


def tier(form):
    f = (form or "").strip()
    if f in T1:
        return 1
    if f.startswith(T2_PREFIX) or f in ("15-12B", "25-NSE"):
        return 2
    if f in T3 or f.startswith("13F"):
        return 3
    return 2  # unknown forms default to SURFACED, never suppressed. Fail toward visibility.


def load_seen():
    if not LEDGER.exists():
        return set(), []
    with LEDGER.open(newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh, delimiter="\t"))
    return {r["accession"] for r in rows}, rows


def append(rows, dry):
    new_file = not LEDGER.exists()
    if dry:
        return
    LEDGER.parent.mkdir(parents=True, exist_ok=True)
    with LEDGER.open("a", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=COLS, delimiter="\t",
                           quoting=csv.QUOTE_MINIMAL, extrasaction="ignore")
        if new_file:
            w.writeheader()
        for r in rows:
            w.writerow(r)


# ────────────────────────────────────────────────────────────────  cadence ──
def _d(s):
    return datetime.strptime(s, "%Y-%m-%d").date()


def lags(filings, form):
    """[(report_date, filed, lag_days)] for one periodic form, oldest-first."""
    out = []
    for f in filings:
        if f["form"] != form or not f["report_date"]:
            continue
        try:
            rd, fd = _d(f["report_date"]), _d(f["filed"])
        except ValueError:
            continue
        if 0 <= (fd - rd).days <= 200:
            out.append((rd, fd, (fd - rd).days))
    return sorted(out)


def window(hist):
    """EARLIEST-plausible and typical lag from history. The L-22 rule lives here:
    the watch opens at min(), not at median()."""
    if len(hist) < 3:
        return None
    L = [h[2] for h in hist]
    return {"n": len(L), "min": min(L), "med": int(statistics.median(L)), "max": max(L)}


def backtest(hist):
    """ZERO-FREE-PARAMETER BACKTEST: hold out the newest filing, derive the window from the
    rest, ask whether the held-out filing landed at/after the earliest bound.
    Returns (verdict, detail). A predictor that fails here is NOT shipped as a warning."""
    if len(hist) < 4:
        return "UNGRADEABLE", "n<4 after hold-out"
    held, prior = hist[-1], hist[:-1]
    w = window(prior)
    ok = held[2] >= w["min"]
    return ("PASS" if ok else "FAIL",
            f"held-out {held[0]}->{held[1]} lag {held[2]}d vs earliest-bound {w['min']}d "
            f"(from n={w['n']}, med {w['med']}d, max {w['max']}d)")


def next_window(hist, today, fy_ends=None, form=""):
    """When can the NEXT filing of this form land? Derived, never inferred.

    ⚠️ TWO STRUCTURAL GUARDS, both found on this file's FIRST RUNS (2026-08-27) — recorded
    because each one produced a confident, wrong-looking-right answer:

    (1) A company that files a 10-K at fiscal year-end does NOT file a 10-Q for Q4.
        Projecting the 10-Q period series naively forward walks it into the FY end and
        predicts a 10-Q that structurally cannot exist. ⇒ for QUARTERLY forms only, if the
        projected period lands on a fiscal year-end, SKIP IT and project the following
        period instead. ⚠️ My first fix SUPPRESSED the window — which was wrong twice over:
        it silenced the 10-K rows too (the 10-K is exactly the form that DOES cover the FY
        end), and for ORCL it threw away a real Q1 prediction instead of stepping past the
        gap. **Suppressing is not the same as skipping, and I shipped the wrong one first.**

    (2) A projection whose window has already fully elapsed is stale, not silent — a quiet
        leg must never mean "the series stopped and I stopped with it".
        ⚠️ SPEC CORRECTED 2026-08-27 BY MY OWN FALSIFICATION TEST, and the correction is the
        interesting part. v1 said "roll forward until the window is in the future." The test
        showed it silently returned None on a 3-years-stale series (the loop bound was 8
        periods and it needed ~11). **The fix was NOT a bigger loop bound.** Rolling a dead
        series forward eleven periods manufactures a confident prediction out of a regime
        that has ended — which is a worse failure than the one it was solving, and a
        *quieter* one. ⇒ Roll forward at MOST 2 periods (a normal gap), and if the series is
        still behind, return STALE and REPORT it. **The staleness IS the finding.**
        📌 Recorded rather than quietly patched: I wrote the test to match my v1 intent, the
        test failed, and the right move was to change the SPEC — not to widen the constant
        until the test passed. Those two edits look identical in a diff."""
    w = window(hist)
    if not w:
        return None
    ends = [h[0] for h in hist]
    if len(ends) < 3:
        return None
    spacing = int(statistics.median([(ends[i + 1] - ends[i]).days
                                     for i in range(len(ends) - 1)]))
    if not 60 <= spacing <= 400:
        return None
    annual = form in ("10-K", "20-F", "40-F")

    def on_fy(d):
        if annual or not fy_ends:
            return False
        return any(abs((fe + timedelta(days=364 * k) - d).days) <= 12
                   for fe in fy_ends for k in range(0, 5))

    nxt = ends[-1] + timedelta(days=spacing)
    skipped, rolled = False, 0
    while True:
        if on_fy(nxt):                       # guard (1): step PAST the FY quarter
            nxt += timedelta(days=spacing)
            skipped = True
            continue
        if (nxt + timedelta(days=w["max"])) < today:   # guard (2): behind today
            if rolled >= 2:
                # STALE. Do NOT keep projecting — say so. See the spec note above.
                return {"stale": True, "last_period": ends[-1], "spacing": spacing,
                        "behind_days": (today - ends[-1]).days, **w}
            nxt += timedelta(days=spacing)
            rolled += 1
            continue
        break
    return {"period_end": nxt, "skipped_fy_quarter": skipped, "stale": False,
            "earliest": nxt + timedelta(days=w["min"]),
            "typical": nxt + timedelta(days=w["med"]),
            "latest": nxt + timedelta(days=w["max"]), **w}


def earnings_cadence(filings, today):
    """THE HIGHEST-VALUE LEG, and it exists for one registered row.

    An earnings RELEASE (8-K item 2.02) is a DIFFERENT EVENT from the periodic filing that
    follows it — the distinction PROME made for NVDA on 8/21 (the call carries the capex
    guide; the 10-Q carries the disclosure text) and the same distinction that makes MU's
    date load-bearing here. `PREDICTIONS.tsv` calls VULCAN-12 *"the sharpest case on the
    book: MU FQ4 is its SOLE resolver on BOTH branches and MU's date is ESTIMATED
    (~9/29, EDGAR fiscalYearEnd=0903), not announced."*

    ⚠️ `fiscalYearEnd` in the submissions feed is a NOMINAL marker (MU: 0903), not the
       actual period end. MU runs a 52/53-week year whose end has been Aug 27 - Sep 1.
       Inferring an earnings date off the nominal marker is the L-22 error exactly.

    So: pair each earnings 8-K with the most recent period end that PRECEDES it (taken from
    the 10-Q/10-K reportDates the issuer itself filed), derive the lag distribution, and
    project. Zero free parameters — every input is a date the issuer filed.
    Q4 is kept SEPARATE from Q1-Q3 because the lags differ materially (MU: Q4 26-27d vs
    Q1/Q2 20-21d) and blending them would manufacture a false precision."""
    ends = sorted({_d(f["report_date"]) for f in filings
                   if f["form"] in PERIODIC and f["report_date"]}
                  | set())
    fy = sorted({_d(f["report_date"]) for f in filings
                 if f["form"] in ("10-K", "20-F", "40-F") and f["report_date"]})
    if len(ends) < 4 or not fy:
        return None
    pairs = []
    for f in filings:
        if f["form"] != "8-K" or "2.02" not in (f["items"] or ""):
            continue
        fd = _d(f["filed"])
        prior = [e for e in ends if 0 < (fd - e).days <= 75]
        if not prior:
            continue
        pe = max(prior)
        pairs.append((pe, fd, (fd - pe).days, pe in fy))
    if len(pairs) < 4:
        return None
    pairs.sort()
    q4 = [p for p in pairs if p[3]]
    nxt_end = ends[-1] + timedelta(days=91)
    is_q4 = any(abs((f_ + timedelta(days=364 * k) - nxt_end).days) <= 10
                for f_ in fy for k in range(0, 4))
    use = q4 if (is_q4 and len(q4) >= 2) else pairs
    L = [p[2] for p in use]
    return {"next_period_end": nxt_end, "is_q4": is_q4, "n": len(L),
            "min": min(L), "med": int(statistics.median(L)), "max": max(L),
            "earliest": nxt_end + timedelta(days=min(L)),
            "typical": nxt_end + timedelta(days=int(statistics.median(L))),
            "latest": nxt_end + timedelta(days=max(L)),
            "basis": "FQ4-only" if use is q4 else "all-quarters",
            "recent": pairs[-4:]}


# ─────────────────────────────────────────────────────────────────── main ──
def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dry-run", action="store_true", help="fetch + report, write nothing")
    ap.add_argument("--show", type=int, metavar="N", help="show last N ledger rows, no fetch")
    ap.add_argument("--issuer", metavar="TICK", help="limit to one ticker")
    ap.add_argument("--backtest", action="store_true", help="show the cadence backtest detail")
    ap.add_argument("--tier", type=int, default=2,
                    help="surface tiers <= this (default 2). Suppressed rows are COUNTED, "
                         "never dropped — the ledger always gets everything.")
    ap.add_argument("--since", metavar="YYYY-MM-DD",
                    help="on a first run, only treat filings on/after this as NEW "
                         "(prevents a cold start reporting 1000 filings as news)")
    a = ap.parse_args()

    if a.show:
        _, rows = load_seen()
        if not rows:
            print("EDGAR_SEEN.tsv: empty (no run yet)")
            return 0
        print(f"{'filed':<11} {'tick':<5} {'form':<9} {'T':<2} {'report':<11} accession")
        for r in rows[-a.show:]:
            print(f"{r['filed']:<11} {r['tick']:<5} {r['form']:<9} {r['tier']:<2} "
                  f"{r['report_date'] or '-':<11} {r['accession']}")
        return 0

    seen, prior_rows = load_seen()
    cold = not prior_rows
    since = _d(a.since) if a.since else None
    if cold and not since:
        # Cold start with no floor would report the entire history as "new". Default to
        # 30 days and SAY SO — a silent default is a decision nobody can audit.
        since = date.today() - timedelta(days=30)
        print(f"ℹ️  cold start: no ledger yet. Treating filings on/after {since} as NEW "
              f"(default 30d floor; override with --since). Full history is still LOGGED.")

    roster = [i for i in ISSUERS if not a.issuer or i[0].upper() == a.issuer.upper()]
    if not roster:
        print(f"ERR: unknown issuer {a.issuer!r}; known: "
              f"{', '.join(i[0] for i in ISSUERS)}", file=sys.stderr)
        return 2

    today = date.today()
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    fresh, errors, suppressed, cadence_lines, bt_lines, earn_lines = [], [], 0, [], [], []

    for tick, cik, channel, _why in roster:
        try:
            filings = fetch(cik)
        except (urllib.error.URLError, ValueError, KeyError, json.JSONDecodeError) as e:
            # FAIL LOUD. A partial run is a FAILED run, never a degraded one [L-16] — the
            # leg that breaks carries the newest evidence, so silent partials are biased
            # toward preserving priors.
            errors.append(f"ERR:{tick}:{type(e).__name__}:{str(e)[:90]}")
            continue

        for f in filings:
            if f["accession"] in seen:
                continue
            t = tier(f["form"])
            row = {"first_seen_utc": stamp, "tick": tick, "cik": cik, "form": f["form"],
                   "filed": f["filed"], "report_date": f["report_date"],
                   "accession": f["accession"], "primary_doc": f["doc"],
                   "items": f["items"], "tier": t, "channel": channel}
            fresh.append(row)

        # ── cadence leg (the reason this file exists) ──
        fy_ends = sorted({_d(f["report_date"]) for f in filings
                          if f["form"] in ("10-K", "20-F", "40-F") and f["report_date"]})
        ec = earnings_cadence(filings, today)
        if ec:
            lbl = "FQ4" if ec["is_q4"] else "Q"
            d_open = (ec["earliest"] - today).days
            mark = "🔔" if d_open <= 0 else ("⏳" if d_open <= 45 else "  ")
            if d_open <= 45:
                earn_lines.append(
                    f"    {mark} {tick:<5} {lbl} EARNINGS 8-K (item 2.02) — period end "
                    f"~{ec['next_period_end']}, release window "
                    f"{ec['earliest']} … {ec['latest']} (typical {ec['typical']}); "
                    f"lag n={ec['n']} min {ec['min']}d med {ec['med']}d max {ec['max']}d, "
                    f"basis {ec['basis']}")
        for form in sorted({f["form"] for f in filings} & PERIODIC):
            hist = lags(filings, form)
            verdict, detail = backtest(hist)
            bt_lines.append(f"    {tick:<5} {form:<5} backtest {verdict:<11} {detail}")
            if verdict == "FAIL":
                errors.append(f"ERR:{tick}:{form}:cadence-backtest-FAILED — {detail}")
                continue
            if verdict == "UNGRADEABLE":
                cadence_lines.append(f"    {tick:<5} {form:<5} UNGRADEABLE — {detail} "
                                     f"(reported, NOT silently downgraded)")
                continue
            nw = next_window(hist, today, fy_ends, form)
            if not nw:
                continue
            if nw.get("stale"):
                cadence_lines.append(
                    f"    🔴 {tick:<5} {form:<5} SERIES STALE — last period end "
                    f"{nw['last_period']} is {nw['behind_days']}d behind today at ~"
                    f"{nw['spacing']}d spacing. NOT projecting forward: a dead series rolled "
                    f"forward manufactures a confident prediction. Check the issuer.")
                continue
            d_open = (nw["earliest"] - today).days
            if d_open <= 0 <= (nw["latest"] - today).days:
                cadence_lines.append(
                    f"    🔔 {tick:<5} {form:<5} WINDOW OPEN since {nw['earliest']} "
                    f"({-d_open}d) — typical {nw['typical']}, latest {nw['latest']}. "
                    f"Period end ~{nw['period_end']}. CHECK NOW.")
            elif 0 < d_open <= 21:
                cadence_lines.append(
                    f"    ⏳ {tick:<5} {form:<5} window opens {nw['earliest']} (in {d_open}d) "
                    f"— typical {nw['typical']}. Period end ~{nw['period_end']}"
                    f"{' (FY quarter skipped — covered by the annual report)' if nw['skipped_fy_quarter'] else ''}. "
                    f"⚠️ Watch from the EARLIEST date, not the typical one [L-22].")

    fresh.sort(key=lambda r: (r["filed"], r["tick"]), reverse=True)
    shown = [r for r in fresh
             if r["tier"] <= a.tier and (not since or _d(r["filed"]) >= since)]
    suppressed = len(fresh) - len(shown)

    print("=" * 78)
    print(f"  VULCAN edgar_watch — {len(roster)} issuer(s), {stamp}")
    print("=" * 78)

    if a.backtest:
        print("\n--- cadence backtest (hold-one-out, zero free parameters) ---")
        for l in bt_lines or ["    (none)"]:
            print(l)

    print(f"\n--- 1. NEW filings (tier <= {a.tier}) ---")
    if shown:
        for r in shown:
            it = f"  items={r['items']}" if r["items"] else ""
            rd = f"  period={r['report_date']}" if r["report_date"] else ""
            print(f"  🆕 {r['filed']}  {r['tick']:<5} {r['form']:<9} [{r['channel']}] "
                  f"{r['accession']}{rd}{it}")
            print(f"      {r['primary_doc']}")
    else:
        print("  ✓ none")
    # Silence always carries its own count. Never let a filter report an empty set as
    # "nothing happened" — that is how an untrippable band reads as clean.
    print(f"  ({suppressed} filing(s) logged but not surfaced at this tier/date floor"
          f"{' — raise --tier or lower --since to see them' if suppressed else ''})")

    print("\n--- 2. periodic-filing windows (derived from each issuer's OWN history) ---")
    for l in cadence_lines or ["  ✓ no periodic filing window open or opening within 21d"]:
        print(l)

    print("\n--- 3. EARNINGS-RELEASE windows (8-K item 2.02) ---")
    print("    ⚠️ A release is a DIFFERENT EVENT from the periodic filing that follows it.")
    for l in earn_lines or ["    ✓ none within 45d"]:
        print(l)

    if errors:
        print("\n--- 🔴 ERRORS — a partial run is a FAILED run [L-16] ---")
        for e in errors:
            print(f"  {e}")

    append(fresh, a.dry_run)
    if a.dry_run:
        print(f"\n[--dry-run] {len(fresh)} row(s) NOT written")
    elif fresh:
        print(f"\n→ {len(fresh)} row(s) appended to {LEDGER.relative_to(VULCAN.parent.parent)}")

    if errors:
        return 2
    return 1 if (shown or any("🔔" in l for l in cadence_lines + earn_lines)) else 0


if __name__ == "__main__":
    sys.exit(main())
