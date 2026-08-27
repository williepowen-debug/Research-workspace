#!/usr/bin/env python3
"""
boot.py — VULCAN boot instrument. Ledger staleness + predictions-due, one verdict.

Built by DAEDALUS 2026-07-10 (VULCAN build). cwd-proof + self-locating: lives at
AGENTS/VULCAN/boot.py -> parents[2] == repo root; finds scripts/ledger_staleness.py
regardless of launch cwd.

Boot step 4 in CLAUDE.md. SEVEN legs:
  1. ledger staleness — workbook/*.tsv AND TRADE.md vs STATUS mtime (shared script).
  2. predictions-due  — workbook/PREDICTIONS.tsv rows past resolve_date still OPEN.
  3. S2 series age    — workbook/S2_SERIES.tsv vintage, CONTENT-derived from the
     row's own asof_utc (never mtime — git sync restamps mtime and the check would
     fail false-negative). Advisory only: it prompts you to run tools/semi_watch.py,
     it does NOT fetch (boot stays fast and offline-safe).
  4. MAG7 series age  — workbook/MAG7_SERIES.tsv vintage, CONTENT-derived from the
     row's own holdings_asof. Added 2026-08-21 the same day the instrument was built,
     because building the tool that fixes six-week rot WITHOUT the alarm that reports
     rot leaves the same hole one level down. Cadence is deliberately SLOWER than S2's
     (index weights move slowly; SPY publishes daily but the number does not move
     daily) — see MAG7_MAX_AGE_DAYS.

  5. S4 series age    — workbook/S4_SERIES.tsv vintage, CONTENT-derived from the row's
     own revenue_month. Added 2026-08-21. ⚠️ Its bound is derived from TSMC's PUBLICATION
     CADENCE, not inherited: TSMC files a 6-K ~the 10th for the PRIOR month, so the leg
     computes which month SHOULD be on file today and compares — it does not count days.
     Why S4 first among the three uninstrumented channels: on 2026-08-21 S4 was found 35
     DAYS STALE ON A MONTHLY SERIES, and the same audit found that the only two channels
     that stayed clean all day were the two that had instruments.
  6. catalyst countdown — scripts/catalyst_countdown.py: ONE reader over docket/
     CATALYSTS.tsv + PREDICTIONS.resolve_date + PROME/DOCKET rows VULCAN OWNS, plus a
     read-only scan of NEIGHBOURS' registries for rows naming VULCAN. Added 2026-08-21
     because boot's only date leg read PREDICTIONS.tsv, which by design holds VULCAN-NN
     MARKET forecasts — so 7 of 10 dated commitments had NO surfacing mechanism at all.

  7. workbook schema — scripts/validate_workbook.py --boot: enforces SCHEMA.tsv against
     ALL EIGHT ledgers. Added 2026-08-21. Until that day SCHEMA.tsv described KB.tsv ONLY
     (9 rows for 1 of 8 ledgers) while CLAUDE.md said "read before writing" — a ritual with
     no mechanism. First run found 2 genuine defects among 18 raw flags: a confidence cell
     carrying TWO tiers as prose (matched no filter, invisible to every scan) and a
     compound value in FLOW's channel enum.

⚠️ S3 and S5 STILL HAVE NO SERIES INSTRUMENT, and that is a DECISION, not an omission:
   both channels' registered thresholds are EVENT-triggered (a cleared new-issue vs talk,
   a collateral posting, a FERC order), not cadence-sampled. Building a daily price proxy
   for them would resolve something other than the concept the threshold names
   (`finding_registry_names_a_concept_tool_resolves_an_instrument`). They are covered by
   leg 6 instead — dated-event coverage, which is the shape their evidence actually has.

Combined exit: 0 = quiet · 1 = REVIEW (stale ledger or prediction due) · 2 = a leg failed.
"""

import csv
import subprocess
import sys
from datetime import date, datetime, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
STALENESS = ROOT / "scripts" / "ledger_staleness.py"
PREDICTIONS = HERE / "workbook" / "PREDICTIONS.tsv"
S2_SERIES = HERE / "workbook" / "S2_SERIES.tsv"
S2_MAX_AGE_DAYS = 7  # S2 is a score-3 channel; a week-old series is a stale channel
MAG7_SERIES = HERE / "workbook" / "MAG7_SERIES.tsv"
# 21d, and the bound is set from the CADENCE of what it measures, not inherited:
# index weights drift slowly, so a daily bound would cry wolf. But it must be well
# inside the 6-WEEK rot that made this instrument necessary — 21d catches that class
# twice over. (`finding_inherited_default_threshold_is_a_silent_decision`)
MAG7_MAX_AGE_DAYS = 21
EDGAR_SEEN = HERE / "workbook" / "EDGAR_SEEN.tsv"
S4_SERIES = HERE / "workbook" / "S4_SERIES.tsv"
# TSMC files the monthly revenue 6-K around the 10th for the PRIOR month. The leg
# therefore reasons in MONTHS, never in days: a day-count bound on a monthly series is
# either permanently noisy or permanently asleep.
S4_FILING_DAY = 12  # by this day of the month, the prior month should be on file
CATALYST_SCRIPT = HERE / "scripts" / "catalyst_countdown.py"
VALIDATOR = HERE / "scripts" / "validate_workbook.py"


def run(cmd):
    try:
        return subprocess.run([sys.executable, *cmd], cwd=str(ROOT)).returncode
    except Exception as e:  # noqa: BLE001
        print(f"  boot.py: FAILED to launch {cmd[0]}: {e}", file=sys.stderr)
        return 2


def run_alert(cmd):
    """Run the shared ledger_staleness check. rc contract REVISED 2026-08-17
    (DAEDALUS shared-script fix, PROME-approved, CHECK_STANDARD §8 rule 3):
    0 clean · 1 stale FINDINGS · 2 CANNOT-CERTIFY (MISCONFIGURED /
    LEDGERS-OUTSIDE-GLOB / usage) — the old 'always 0' alert contract is
    retired; rc now AGREES with the ⚠️/🔴 markers instead of contradicting
    them. Verdict = rc 1 OR marker-present (§8 rule 5 keeps the marker channel
    authoritative; still never bare output-nonempty — the 8/11→8/16 scope-line
    false-REVIEW stays fixed; CHECKS.tsv ledger_staleness row = contract home).
    rc 2 → leg failure (enforcement silently absent = never assume quiet).
    Returns 0 quiet · 1 REVIEW · 2 failure/cannot-certify."""
    try:
        p = subprocess.run([sys.executable, *cmd], cwd=str(ROOT),
                           capture_output=True, text=True)
    except Exception as e:  # noqa: BLE001
        print(f"  boot.py: FAILED to launch {cmd[0]}: {e}", file=sys.stderr)
        return 2
    out = (p.stdout or "").strip()
    err = (p.stderr or "").strip()
    if out:
        print(out)
    if err:
        print(err, file=sys.stderr)
    if p.returncode not in (0, 1):
        return 2
    return 1 if (p.returncode == 1 or "⚠️" in out or "🔴" in out) else 0


def predictions_due():
    """(n_due, rows) for PREDICTIONS.tsv rows past resolve_date still OPEN/ACTIVE.
    Tolerant of a newborn/empty ledger."""
    if not PREDICTIONS.exists():
        return 0, []
    today = date.today()
    due = []
    try:
        with PREDICTIONS.open(encoding="utf-8") as f:
            reader = csv.DictReader(f, delimiter="\t")
            cols = {c.lower(): c for c in (reader.fieldnames or [])}
            dcol = cols.get("resolve_date") or cols.get("resolves") or cols.get("resolve")
            scol = cols.get("status")
            if not dcol or not scol:
                return 0, []
            for r in reader:
                if (r.get(scol) or "").strip().upper() not in ("OPEN", "ACTIVE", "PENDING"):
                    continue
                raw = (r.get(dcol) or "").strip()
                try:
                    when = datetime.strptime(raw[:10], "%Y-%m-%d").date()
                except ValueError:
                    continue
                if when <= today:
                    due.append(f"{r.get(cols.get('id', 'id'), '?')} due {raw}")
    except Exception as e:  # noqa: BLE001
        print(f"  boot.py: predictions scan error: {e}", file=sys.stderr)
        return 2, []
    return len(due), due



def s2_series_age():
    """Leg 3 — S2 memory-cycle series vintage, derived from CONTENT (asof_utc).

    Returns (rc, message). rc 0 = fresh · 1 = stale/absent (REVIEW) · 2 = unreadable.
    Deliberately does NOT fetch: boot must stay fast and work offline. It tells you
    to run tools/semi_watch.py; running it is the session's job.
    """
    if not S2_SERIES.exists():
        return 1, ("  S2 series ABSENT — run: python3 AGENTS/VULCAN/tools/semi_watch.py\n"
                   "    (S2 is at score 3 with no retained history; the live read is a point, not a trend.)")
    try:
        rows = list(csv.DictReader(S2_SERIES.open(encoding="utf-8"), delimiter="\t"))
        if not rows:
            return 1, "  S2 series is header-only — run tools/semi_watch.py"
        stamp = rows[-1].get("asof_utc", "")
        vintage = datetime.strptime(stamp[:10], "%Y-%m-%d").date()
    except Exception as e:  # noqa: BLE001
        return 2, f"  S2 series UNREADABLE ({type(e).__name__}) — inspect workbook/S2_SERIES.tsv"

    age = (date.today() - vintage).days
    n_err = sum(1 for k, v in rows[-1].items() if str(v).startswith("ERR:"))
    err_note = f"  ⚠️ last row has {n_err} ERR field(s) — do not read them as data." if n_err else ""
    if age > S2_MAX_AGE_DAYS:
        return 1, (f"  S2 series STALE {age}d (last {vintage}, {len(rows)} rows) — "
                   f"run: python3 AGENTS/VULCAN/tools/semi_watch.py{err_note}")
    return (1 if n_err else 0), f"  \u2713 S2 series fresh ({age}d, {len(rows)} rows, last {vintage}){err_note}"


def mag7_series_age():
    """Leg 4 — S1 concentration series vintage, derived from CONTENT (holdings_asof).

    Returns (rc, message). rc 0 = fresh · 1 = stale/absent (REVIEW) · 2 = unreadable.
    Like leg 3 it does NOT fetch — it tells you to run tools/mag7.py.

    Why it exists: the Mag-7 weight sat aggregator-sourced and six weeks stale while
    serving as BOTH S1's banded threshold input AND thesis-kill leg 2's instrument.
    An instrument with no staleness alarm is the same failure one level down.
    """
    if not MAG7_SERIES.exists():
        return 1, ("  MAG7 series ABSENT — run: python3 AGENTS/VULCAN/tools/mag7.py\n"
                   "    (S1's band input and thesis-kill leg 2 both read this number.)")
    try:
        rows = list(csv.DictReader(MAG7_SERIES.open(encoding="utf-8"), delimiter="\t"))
        if not rows:
            return 1, "  MAG7 series is header-only — run tools/mag7.py"
        last = rows[-1]
        vintage = datetime.strptime(last.get("holdings_asof", ""), "%d-%b-%Y").date()
    except Exception as e:  # noqa: BLE001
        return 2, f"  MAG7 series UNREADABLE ({type(e).__name__}) — inspect workbook/MAG7_SERIES.tsv"

    age = (date.today() - vintage).days
    notes = []
    if str(last.get("validation", "")).startswith("ERR"):
        notes.append("⚠️ last row failed validation — do not read it as data")
    band = str(last.get("band", ""))
    if band and band != "below-yellow":
        notes.append(f"⚠️ BAND = {band}")
    # proximity warning: the whole point of the 8/21 pull was that 32.98% sat 0.019pp
    # under the line while the files said "comfortably below".
    try:
        pct = float(last.get("mag7_pct", "nan"))
        if 32.0 <= pct < 33.0:
            notes.append(f"⚠️ {pct:.2f}% is inside 1pp of the 33% yellow line — AT it, not below it")
    except (TypeError, ValueError):
        pass
    note = ("\n    " + " · ".join(notes)) if notes else ""

    if len(rows) < 2:
        note += "\n    ⚠️ n=1 — a LEVEL, not a trend (breadth IS measured; there is just no history of it yet)."
    if age > MAG7_MAX_AGE_DAYS:
        return 1, (f"  MAG7 series STALE {age}d (holdings as-of {vintage}, {len(rows)} rows) — "
                   f"run: python3 AGENTS/VULCAN/tools/mag7.py{note}")
    return 0, f"  \u2713 MAG7 series fresh ({age}d, {len(rows)} rows, holdings as-of {vintage}){note}"


def _expected_revenue_month(today):
    """Which month-end SHOULD be on file today, given TSMC's ~10th-of-month cadence."""
    y, m = today.year, today.month
    back = 1 if today.day >= S4_FILING_DAY else 2
    for _ in range(back):
        m -= 1
        if m == 0:
            m, y = 12, y - 1
    nxt = date(y + (m == 12), (m % 12) + 1, 1)
    return date(y, m, 1), (nxt - timedelta(days=1))


def s4_series_age():
    """Leg 5 — S4 TSMC monthly-revenue series, CONTENT-derived from revenue_month.

    Returns (rc, message). rc 0 = fresh · 1 = a print is missing (REVIEW) · 2 = unreadable.
    Like legs 3-4 it does NOT fetch; it tells you to run tools/tsmc_watch.py.
    """
    if not S4_SERIES.exists():
        return 1, ("  S4 series ABSENT — run: .venv/bin/python AGENTS/VULCAN/tools/tsmc_watch.py\n"
                   "    (S4 is S1's cleanest INDEPENDENT root and had no retained history at all.)")
    try:
        rows = list(csv.DictReader(S4_SERIES.open(encoding="utf-8"), delimiter="\t"))
        if not rows:
            return 1, "  S4 series is header-only — run tools/tsmc_watch.py"
        latest = max(r["revenue_month"] for r in rows)
        have = datetime.strptime(latest, "%Y-%m-%d").date()
    except Exception as e:  # noqa: BLE001
        return 2, f"  S4 series UNREADABLE ({type(e).__name__}) — inspect workbook/S4_SERIES.tsv"

    _, want = _expected_revenue_month(date.today())
    if have < want:
        missed = (want.year - have.year) * 12 + (want.month - have.month)
        return 1, (f"  S4 series BEHIND by {missed} month(s) — have {have:%b %Y}, "
                   f"{want:%b %Y} should be filed by now.\n"
                   f"    run: .venv/bin/python AGENTS/VULCAN/tools/tsmc_watch.py\n"
                   f"    ⚠️ S4 rotted 35d on this exact series once, because nothing pulled it.")
    last = sorted(rows, key=lambda r: r["revenue_month"])[-1]
    note = ""
    if str(last.get("band", "")).startswith(("red", "orange")):
        note = f"\n    🔴 last band = {last['band']} — S4's revenue line is NOT clean; read it."
    return 0, (f"  ✓ S4 series current ({len(rows)} rows, latest {have:%b %Y}, "
               f"cum YoY {last['ytd_yoy_pct']}%, band {last['band']}){note}")


def catalyst_countdown():
    """Leg 6 — dated commitments across CATALYSTS + PREDICTIONS + DOCKET + neighbours."""
    if not CATALYST_SCRIPT.exists():
        return 2, "  🔴 scripts/catalyst_countdown.py MISSING — every dated commitment is unsurfaced"
    py = ROOT / ".venv" / "bin" / "python"
    cmd = [str(py if py.exists() else sys.executable), str(CATALYST_SCRIPT)]
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=90)
    except Exception as e:  # noqa: BLE001
        return 2, f"  🔴 catalyst countdown FAILED to run ({type(e).__name__})"
    out = (r.stdout or "").rstrip("\n")
    # the script prints its own header; strip it so boot owns the numbering
    out = "\n".join(l for l in out.splitlines() if not l.startswith("--- 5."))
    if r.returncode == 2:
        return 2, out + "\n  🔴 countdown reported a BLIND registry — do not read as quiet"
    return (1 if r.returncode == 1 else 0), out



def workbook_schema():
    """Leg 7 — enforce SCHEMA.tsv across every declared ledger."""
    if not VALIDATOR.exists():
        return 2, "  🔴 scripts/validate_workbook.py MISSING — SCHEMA.tsv is unenforced"
    py = ROOT / ".venv" / "bin" / "python"
    try:
        r = subprocess.run([str(py if py.exists() else sys.executable), str(VALIDATOR), "--boot"],
                           capture_output=True, text=True, timeout=60)
    except Exception as e:  # noqa: BLE001
        return 2, f"  🔴 workbook validator FAILED to run ({type(e).__name__})"
    return (2 if r.returncode == 2 else (1 if r.returncode == 1 else 0)), (r.stdout or "").rstrip("\n")


def edgar_sweep():
    """Leg 8 — S3/S5 filing sweep: sweep staleness + OPEN filing windows.

    Like legs 3-5 this is ADVISORY and does NOT fetch — boot stays fast and offline-safe.
    But unlike them it can do real work offline: the cadence windows are computed from the
    RETAINED LEDGER (form / filed / report_date are all in it), so an open filing window
    surfaces at boot with zero network calls.

    STALENESS BOUND = 3 DAYS, and the number is DERIVED, not inherited
    [`finding_inherited_default_threshold_is_a_silent_decision`]. What this instrument
    measures is 8-K material events, which are unscheduled and can land on any business day,
    so there is no natural period to key on. The bound therefore comes from the two MEASURED
    misses that caused this tool to be built: the 2026-08-17 $105B guaranty 8-K sat 4 days,
    and the 2026-08-26 10-Q would have sat 5. **3 days sits strictly below both, so the
    guard would have caught each of them** — which is the only calibration claim worth making.
    """
    if not EDGAR_SEEN.exists():
        return 1, ("  EDGAR ledger ABSENT — run: python3 AGENTS/VULCAN/tools/edgar_watch.py"
                   "\n    (S3/S5 are EVENT-triggered channels; the filing sweep IS their "
                   "instrument.)")
    try:
        rows = list(csv.DictReader(EDGAR_SEEN.open(encoding="utf-8"), delimiter="\t"))
        if not rows:
            return 1, "  EDGAR ledger is header-only — run tools/edgar_watch.py"
        # CONTENT vintage: the newest observation stamp in the file, never mtime.
        last_run = max(r["first_seen_utc"] for r in rows)[:10]
        age = (date.today() - datetime.strptime(last_run, "%Y-%m-%d").date()).days
    except Exception as e:  # noqa: BLE001
        return 2, f"  EDGAR ledger UNREADABLE ({type(e).__name__}) — inspect EDGAR_SEEN.tsv"

    out, rc = [], 0
    if age > 3:
        rc = 1
        out.append(f"  🔴 EDGAR sweep {age}d STALE (last {last_run}; bound 3d, derived from "
                   f"the 4d and 5d misses that built this tool)"
                   f"\n    run: python3 AGENTS/VULCAN/tools/edgar_watch.py")
    else:
        out.append(f"  ✓ EDGAR sweep fresh ({age}d, {len(rows)} rows, last swept {last_run})")

    # ── OPEN filing windows, computed offline from the retained ledger ──
    try:
        sys.path.insert(0, str(HERE / "tools"))
        import edgar_watch as EW  # noqa: PLC0415
        today = date.today()
        by = {}
        for r in rows:
            by.setdefault(r["tick"], []).append(
                {"form": r["form"], "filed": r["filed"],
                 "report_date": r["report_date"], "items": r["items"]})
        for tick, fl in sorted(by.items()):
            fy = sorted({EW._d(x["report_date"]) for x in fl
                         if x["form"] in ("10-K", "20-F", "40-F") and x["report_date"]})
            for form in sorted({x["form"] for x in fl} & EW.PERIODIC):
                hist = EW.lags(fl, form)
                if EW.backtest(hist)[0] != "PASS":
                    continue
                nw = EW.next_window(hist, today, fy, form)
                if not nw or nw.get("stale"):
                    continue
                if nw["earliest"] <= today <= nw["latest"]:
                    rc = max(rc, 1)
                    out.append(f"    🔔 {tick} {form} WINDOW OPEN since {nw['earliest']} "
                               f"(typical {nw['typical']}, latest {nw['latest']}) — CHECK EDGAR")
            ec = EW.earnings_cadence(fl, today)
            if ec and ec["earliest"] <= today <= ec["latest"]:
                rc = max(rc, 1)
                lbl = "FQ4" if ec["is_q4"] else "Q"
                out.append(f"    🔔 {tick} {lbl} EARNINGS window OPEN since {ec['earliest']} "
                           f"(typical {ec['typical']}) — CHECK")
    except Exception as e:  # noqa: BLE001
        # FAIL LOUD. A window leg that silently no-ops is the defect this tool exists to kill.
        out.append(f"    🔴 window leg FAILED ({type(e).__name__}: {str(e)[:70]}) — windows "
                   f"NOT evaluated this boot. Do NOT read the quiet as clean.")
        rc = 2
    return rc, "\n".join(out)


def main():
    print("=" * 72)
    print("  VULCAN BOOT — staleness · predictions · series · catalysts · schema")
    print("=" * 72)
    rcs = []

    print("\n--- 1. ledger staleness (workbook + TRADE.md vs STATUS) ---")
    sw = run_alert([str(STALENESS), "VULCAN", "--quiet"])
    st = run_alert([str(STALENESS), "VULCAN", "--trade", "--quiet"])
    if sw == st == 0:
        print("  ✓ quiet (alert-contract: output only when stale/misconfigured)")
    rcs.append(2 if 2 in (sw, st) else (1 if 1 in (sw, st) else 0))

    print("\n--- 2. predictions-due scan ---")
    n_due, due = predictions_due()
    if due:
        for d in due:
            print(f"  DUE: {d}")
        rcs.append(1)
    elif n_due == 0:
        print("  none due (or newborn ledger)")
        rcs.append(0)
    else:
        rcs.append(2)

    print("\n--- 3. S2 memory-cycle series (content-vintage) ---")
    s2_rc, s2_msg = s2_series_age()
    print(s2_msg)
    rcs.append(s2_rc)

    print("\n--- 4. S1 Mag-7 concentration series (content-vintage) ---")
    m7_rc, m7_msg = mag7_series_age()
    print(m7_msg)
    rcs.append(m7_rc)

    print("\n--- 5. S4 TSMC monthly-revenue series (content-vintage) ---")
    s4_rc, s4_msg = s4_series_age()
    print(s4_msg)
    rcs.append(s4_rc)

    print("\n--- 6. catalyst countdown (dated commitments, all sources) ---")
    cc_rc, cc_msg = catalyst_countdown()
    print(cc_msg)
    rcs.append(cc_rc)

    print("\n--- 7. workbook schema conformance (all ledgers) ---")
    wb_rc, wb_msg = workbook_schema()
    print(wb_msg)
    rcs.append(wb_rc)

    print("\n--- 8. EDGAR filing sweep (S3/S5 event instrument) ---")
    eg_rc, eg_msg = edgar_sweep()
    print(eg_msg)
    rcs.append(eg_rc)

    print("\n" + "=" * 72)
    if 2 in rcs:
        print("  VULCAN boot: a leg FAILED — check manually, do NOT assume quiet.")
        return 2
    if 1 in rcs:
        print("  VULCAN boot: REVIEW — stale ledger or prediction due.")
        return 1
    print("  VULCAN boot: all quiet.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
