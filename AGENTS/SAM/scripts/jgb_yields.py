#!/usr/bin/env python3
"""
SAM JGB Yield Monitor
Fetches daily JGB yield curve from MOF's authoritative CSV.

Sources (TWO, deliberately):
  PRIMARY  https://www.mof.go.jp/english/policy/jgbs/reference/interest_rate/jgbcme.csv
           CURRENT MONTH ONLY. On the 1st of a month it holds a single row.
  HISTORY  https://www.mof.go.jp/jgbs/reference/interest_rate/data/jgbcm_all.csv
           Full series since 1974 (Japanese, CP932, Reiwa/Heisei/Showa dates).
           Lags the current-month file by ~1 publication.

Format: Date, 1Y, 2Y, 3Y, ..., 10Y, 15Y, 20Y, 25Y, 30Y, 40Y (all in %)
Update cadence: MOF publishes with ~1 business day lag. Friday data posts Monday.

🔴 MONTH-BOUNDARY GAP (found 2026-09-01, fixed same day)
   The primary CSV is scoped to the CURRENT MONTH. If no session runs between the
   last business day of month M and the first of month M+1, every close in the tail
   of M is lost PERMANENTLY: the primary no longer serves them and this script had
   no other source. Measured instance: SAM was dark 8/27 -> 9/1 and 2026-08-27,
   08-28 and 08-31 were never captured.

   ⚠️ The failure is SILENT BY CONSTRUCTION. There is no error, no flag and no wrong
   value -- the TSV simply has no rows, so every downstream count, streak and
   "N consecutive closes" figure computes cleanly off an incomplete series.

   FIX: after parsing the primary, compare the last stored date against the earliest
   date the primary can serve. Any business day between them is a gap the primary
   CANNOT fill, so fall back to the history file for exactly those dates.

   ⛔ The history file is NOT trusted on sight. It is a different file, a different
   language and a different encoding, so it is BASIS-CONTROLLED first: it must
   reproduce already-stored overlapping rows EXACTLY before one gap row is written.
   Fails closed -- on a control failure nothing is appended and the gap is reported.

Appends to workbook/JGB_YIELDS.tsv (one row per date).
⛔ Existing rows are NEVER modified -- they are the first-print audit trail and past
   grades must stay reproducible. New dates are INSERTED and the file re-sorted; a
   byte-identity guard proves no stored line changed.

Checks thresholds:
  🔴 10Y ≥ 2.40% (stress crossover)
  🔴 30Y ≥ 4.00% (severe insurer stress)
  🔴 40Y ≥ 4.00% (extreme long-end stress)

Appends to workbook/JGB_YIELDS.tsv (one row per date).

Usage:
  .venv/bin/python3 AGENTS/SAM/scripts/jgb_yields.py
  .venv/bin/python3 AGENTS/SAM/scripts/jgb_yields.py --history 10   # show last 10 days
  .venv/bin/python3 AGENTS/SAM/scripts/jgb_yields.py --verify-history
        # run the basis control against the history file and report; write nothing
  .venv/bin/python3 AGENTS/SAM/scripts/jgb_yields.py --backfill-from 2026-01-01
        # deliberate deeper fill from the history file (still basis-controlled)
"""

import re
import sys
import urllib.request
from datetime import datetime
from pathlib import Path

SAM_DIR = Path(__file__).resolve().parent.parent
WORKBOOK = SAM_DIR / "workbook"
JGB_TSV = WORKBOOK / "JGB_YIELDS.tsv"

MOF_CSV_URL = "https://www.mof.go.jp/english/policy/jgbs/reference/interest_rate/jgbcme.csv"
# Full series since 1974. Japanese-language, CP932, era-prefixed dates. Lags the
# current-month file by ~1 publication, so the two are COMPLEMENTARY, not redundant.
MOF_HISTORY_CSV_URL = "https://www.mof.go.jp/jgbs/reference/interest_rate/data/jgbcm_all.csv"

HEADERS = {"User-Agent": "Mozilla/5.0 (SAM-Research)"}

# Japanese era -> Gregorian offset. Showa 49 = 1974 (first data), Heisei 1 = 1989,
# Reiwa 1 = 2019. Verified against the file's own first row (S49.9.24) and last (R8.*).
ERA_OFFSET = {"S": 1925, "H": 1988, "R": 2018}
ERA_RE = re.compile(r"^([SHR])(\d+)\.(\d+)\.(\d+)$")

# Tenors SAM cares about (CSV has 1Y-40Y; we track these)
TRACKED_TENORS = ["2Y", "5Y", "10Y", "20Y", "30Y", "40Y"]

# Threshold levels (from THESIS.md KEY THRESHOLDS table)
THRESHOLDS = {
    "10Y": (2.40, "Stress crossover"),
    "30Y": (4.00, "Severe insurer stress"),
    "40Y": (4.00, "Extreme long-end stress"),
}

TSV_HEADER = "Date\t2Y\t5Y\t10Y\t20Y\t30Y\t40Y\tSource\n"


def fetch_mof_csv():
    """Fetch MOF JGB yield CSV. Returns raw text or None on failure."""
    try:
        req = urllib.request.Request(MOF_CSV_URL, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=15) as resp:
            return resp.read().decode("utf-8", errors="replace")
    except Exception as e:
        print(f"  ERROR fetching MOF CSV: {e}")
        return None


def parse_mof_csv(text):
    """
    Parse MOF CSV. Returns list of dicts ordered by date ascending.
    Structure:
      Line 1: "Interest Rate (Month Year),..."
      Line 2: "Date,1Y,2Y,3Y,4Y,5Y,6Y,7Y,8Y,9Y,10Y,15Y,20Y,25Y,30Y,40Y"
      Lines 3+: "YYYY/M/D,1.xxx,1.xxx,..."
      Trailer: empty lines + encoding warning
    """
    lines = text.splitlines()
    if len(lines) < 3:
        return []

    # Header is line 2 (index 1)
    header = [h.strip() for h in lines[1].split(",")]
    if header[0] != "Date":
        # Shouldn't happen, but bail cleanly
        return []

    # Map tenor name to column index
    tenor_idx = {name: i for i, name in enumerate(header)}

    rows = []
    for line in lines[2:]:
        parts = [p.strip() for p in line.split(",")]
        if not parts[0] or "/" not in parts[0]:
            continue
        try:
            # MOF format: 2026/4/9
            d = datetime.strptime(parts[0], "%Y/%m/%d").date()
        except ValueError:
            continue

        row = {"date": d.strftime("%Y-%m-%d")}
        for tenor in TRACKED_TENORS:
            idx = tenor_idx.get(tenor)
            if idx is not None and idx < len(parts):
                val = parts[idx]
                try:
                    row[tenor] = float(val) if val else None
                except ValueError:
                    row[tenor] = None
            else:
                row[tenor] = None
        rows.append(row)

    return rows


def fetch_mof_history_csv():
    """Fetch MOF's full-history CSV (CP932, Japanese). Returns text or None."""
    try:
        req = urllib.request.Request(MOF_HISTORY_CSV_URL, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=40) as resp:
            return resp.read().decode("cp932", errors="replace")
    except Exception as e:
        print(f"  ERROR fetching MOF history CSV: {e}")
        return None


def parse_mof_history_csv(text):
    """
    Parse MOF's full-history CSV into the SAME row shape as parse_mof_csv().

    Dates are era-prefixed: 'R8.8.31' = Reiwa 8 = 2026-08-31. Missing values are '-'.
    Column ORDER matches the English file (date,1Y..10Y,15Y,20Y,25Y,30Y,40Y) but the
    header is Japanese, so columns are taken POSITIONALLY against a verified layout
    rather than by name.
    """
    # Positional layout, asserted below against the file's own header width.
    col = {"2Y": 2, "5Y": 5, "10Y": 10, "20Y": 12, "30Y": 14, "40Y": 15}
    rows = []
    for line in text.splitlines():
        parts = [x.strip() for x in line.split(",")]
        if not parts or not parts[0]:
            continue
        m = ERA_RE.match(parts[0])
        if not m:
            continue
        era, y, mo, dy = m.group(1), int(m.group(2)), int(m.group(3)), int(m.group(4))
        off = ERA_OFFSET.get(era)
        if off is None or len(parts) < 16:
            continue
        try:
            d = datetime(off + y, mo, dy).date()
        except ValueError:
            continue
        row = {"date": d.strftime("%Y-%m-%d")}
        for tenor, idx in col.items():
            val = parts[idx]
            try:
                row[tenor] = float(val) if val and val != "-" else None
            except ValueError:
                row[tenor] = None
        rows.append(row)
    rows.sort(key=lambda r: r["date"])
    return rows


def read_tsv_rows():
    """Stored rows as {date: {tenor: float|None}}. Empty dict if the TSV is absent."""
    out = {}
    if not JGB_TSV.exists():
        return out
    with open(JGB_TSV) as f:
        next(f, None)
        for line in f:
            parts = line.rstrip("\n").split("\t")
            if not parts or not parts[0]:
                continue
            rec = {}
            for i, tenor in enumerate(TRACKED_TENORS, start=1):
                v = parts[i] if i < len(parts) else ""
                try:
                    rec[tenor] = float(v) if v else None
                except ValueError:
                    rec[tenor] = None
            out[parts[0]] = rec
    return out


def verify_history_basis(hist_rows, stored, primary_rows):
    """
    🔴 BASIS CONTROL — the history file must PROVE it agrees with what we already
    trust before a single gap row is written from it.

    Two independent controls, both on overlapping dates only:
      (a) vs the stored TSV      -- our own first-print audit trail
      (b) vs the primary CSV     -- the authoritative current-month source

    🔴 A control with NO overlapping dates is NOT a failure -- it is NOT APPLICABLE.
    The two MOF files are COMPLEMENTARY BY CONSTRUCTION (history lags the primary by
    ~1 publication), so on the 1st of a month they share no dates at all. Requiring
    BOTH to pass made the control unsatisfiable at exactly the month boundary it exists
    to protect -- i.e. the guard's own v1 failed closed on every real gap. Caught by
    running it rather than reasoning about it.

    Passing therefore requires:
      * at least ONE control with genuine overlap (never write on zero proof), AND
      * ZERO mismatches in every control that HAS overlap.

    Returns (ok: bool, report: list[str]). A single mismatched tenor on a single
    overlapping date fails the whole control -- this tests BASIS IDENTITY, not
    approximate agreement.
    """
    hist = {r["date"]: r for r in hist_rows}
    report = []
    ok = True
    proven = False        # a control passed CLEANLY on real overlap
    had_overlap = False   # a control had overlap at all (clean or not)

    for label, ref in (("stored TSV", stored),
                       ("primary CSV", {r["date"]: r for r in primary_rows})):
        shared = sorted(set(hist) & set(ref))
        if not shared:
            report.append(f"    {label:<12} ⚪ no overlapping dates — N/A "
                          f"(complementary coverage, not a failure)")
            continue
        had_overlap = True
        checked = mism = 0
        first_bad = None
        for d in shared:
            for tenor in TRACKED_TENORS:
                a, b = hist[d].get(tenor), ref[d].get(tenor)
                if a is None and b is None:
                    continue
                checked += 1
                if a is None or b is None or abs(a - b) > 1e-9:
                    mism += 1
                    if first_bad is None:
                        first_bad = f"{d} {tenor}: history {a} vs {label} {b}"
        if mism:
            ok = False
            report.append(f"    {label:<12} 🔴 {mism}/{checked} MISMATCH over "
                          f"{len(shared)} date(s) — first: {first_bad}")
        else:
            proven = True
            report.append(f"    {label:<12} ✅ {checked} value(s) identical over "
                          f"{len(shared)} date(s) [{shared[0]} … {shared[-1]}]")

    if not proven:
        ok = False
        # Distinguish "nothing to compare" from "compared and disagreed" — saying the
        # former when the latter happened is a message asserting a property the
        # situation lacks, which is the exact defect class this guard exists to catch.
        report.append(
            "    🔴 A control OVERLAPPED and DISAGREED — refusing." if had_overlap
            else "    🔴 NO control had overlapping dates — zero proof, refusing.")
    return ok, report


def find_gap_dates(stored, primary_rows, backfill_from=None):
    """
    Dates the PRIMARY cannot serve and we do not have.

    The primary is scoped to the current month, so its earliest row is a hard floor:
    anything before it is unreachable from that source forever.

    🔴 The test is NOT "is our latest row older than the floor". Once the current
    month's row is stored, the desk's newest date sits AT or AFTER the floor while the
    hole still gapes behind it -- the first version of this check compared max(stored)
    to the floor and reported NO GAP on the very series it was written to repair.
    The gap is a HOLE, not a tail, so we compare the last stored date STRICTLY BEFORE
    the floor against the floor itself.

    Weekends make an exact business-day test impossible without a calendar, so the
    trigger is a >3 day span (Fri->Mon is 3). A long public holiday can therefore
    trigger a harmless extra history fetch that finds nothing missing -- deliberately
    biased toward OVER-fetching, because the failure being prevented is silent.

    Returns (floor, cutoff); the caller pulls history rows in (cutoff, floor).
    """
    if not primary_rows:
        return None, None
    floor = min(r["date"] for r in primary_rows)
    if backfill_from:
        return floor, backfill_from
    if not stored:
        # First run: take only what the primary serves. A new TSV should not
        # silently drag in fifty years of history.
        return floor, None
    before = [d for d in stored if d < floor]
    if not before:
        return floor, None
    prior = max(before)
    span = (datetime.strptime(floor, "%Y-%m-%d") - datetime.strptime(prior, "%Y-%m-%d")).days
    if span > 3:
        return floor, prior
    return floor, None


def append_tsv(rows):
    """
    Insert rows for dates not already stored, keeping the file DATE-SORTED.

    ⛔ Existing lines are preserved BYTE-IDENTICALLY and never rewritten -- they are
    the first-print audit trail, and past grades must stay reproducible. Backfilled
    dates land in the middle of the file, so a plain append would leave it unsorted;
    we re-sort and then PROVE by set-identity that every stored line survived unchanged.
    Returns (appended, backfilled).
    """
    if not JGB_TSV.exists():
        with open(JGB_TSV, "w") as f:
            f.write(TSV_HEADER)

    with open(JGB_TSV) as f:
        lines = f.read().split("\n")
    header = lines[0]
    body = [ln for ln in lines[1:] if ln.strip()]
    existing_dates = {ln.split("\t")[0] for ln in body}

    last_before = max(existing_dates) if existing_dates else None
    new_lines, appended, backfilled = [], 0, 0
    for r in rows:
        if r["date"] in existing_dates:
            continue
        values = [r["date"]]
        for tenor in TRACKED_TENORS:
            v = r.get(tenor)
            values.append(f"{v:.3f}" if v is not None else "")
        values.append("MOF")
        new_lines.append("\t".join(values))
        existing_dates.add(r["date"])
        appended += 1
        if last_before is not None and r["date"] < last_before:
            backfilled += 1

    if not new_lines:
        return 0, 0

    merged = sorted(body + new_lines, key=lambda ln: ln.split("\t")[0])

    # AUDIT-TRAIL GUARD: every pre-existing line must appear unchanged in the output.
    lost = set(body) - set(merged)
    if lost:
        raise RuntimeError(
            f"REFUSING TO WRITE: {len(lost)} stored line(s) would be lost or altered. "
            f"First: {sorted(lost)[0][:60]}"
        )

    with open(JGB_TSV, "w") as f:
        f.write(header + "\n" + "\n".join(merged) + "\n")
    return appended, backfilled


def check_thresholds(row):
    """Return list of threshold breaches for the given row."""
    breaches = []
    for tenor, (level, label) in THRESHOLDS.items():
        v = row.get(tenor)
        if v is not None and v >= level:
            dist = ((v - level) / level) * 100
            breaches.append((tenor, v, level, label, dist))
    return breaches


def main():
    history = 5
    if "--history" in sys.argv:
        idx = sys.argv.index("--history")
        if idx + 1 < len(sys.argv):
            history = int(sys.argv[idx + 1])
    verify_only = "--verify-history" in sys.argv
    backfill_from = None
    if "--backfill-from" in sys.argv:
        idx = sys.argv.index("--backfill-from")
        if idx + 1 < len(sys.argv):
            backfill_from = sys.argv[idx + 1]

    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    print(f"\n{'='*70}")
    print(f"  SAM JGB Yield Monitor — {now}")
    print(f"{'='*70}")

    text = fetch_mof_csv()
    if not text:
        print("\n  ERROR: MOF CSV fetch failed. Try again later.")
        return 1

    rows = parse_mof_csv(text)
    if not rows:
        print("\n  ERROR: MOF CSV parsed empty. Format may have changed.")
        return 1

    latest = rows[-1]
    print(f"\n  Source: MOF (authoritative)")
    print(f"  Latest publication: {latest['date']}")

    # Print latest snapshot
    print(f"\n  LATEST CURVE ({latest['date']})")
    print(f"  {'-'*60}")
    for tenor in TRACKED_TENORS:
        v = latest.get(tenor)
        if v is None:
            print(f"  {tenor:<4}  — no data")
            continue
        mark = ""
        if tenor in THRESHOLDS:
            level, _ = THRESHOLDS[tenor]
            if v >= level:
                mark = "  🔴 BREACHED"
            elif v >= level * 0.95:
                mark = "  ⚠️  near breach"
        print(f"  {tenor:<4}  {v:>6.3f}%{mark}")

    # Threshold breaches
    breaches = check_thresholds(latest)
    if breaches:
        print(f"\n  🔴 ACTIVE BREACHES")
        print(f"  {'-'*60}")
        for tenor, v, level, label, dist in breaches:
            print(f"  🔴 {tenor} at {v:.3f}%  (threshold {level:.2f}%, +{dist:.1f}%)  {label}")

    # History
    if len(rows) >= 2:
        print(f"\n  RECENT HISTORY (last {min(history, len(rows))} days)")
        print(f"  {'-'*60}")
        print(f"  {'Date':<12}  " + "  ".join(f"{t:>6}" for t in TRACKED_TENORS))
        for r in rows[-history:]:
            vals = "  ".join(
                f"{r[t]:>6.3f}" if r.get(t) is not None else "     —"
                for t in TRACKED_TENORS
            )
            print(f"  {r['date']:<12}  {vals}")

        # Week-over-week change (latest vs 5 business days ago if available)
        if len(rows) >= 6:
            prior = rows[-6]
            print(f"\n  5-DAY CHANGE ({prior['date']} → {latest['date']})")
            print(f"  {'-'*60}")
            for tenor in TRACKED_TENORS:
                cur = latest.get(tenor)
                old = prior.get(tenor)
                if cur is not None and old is not None:
                    delta_bp = (cur - old) * 100
                    arrow = "↑" if delta_bp > 0 else "↓" if delta_bp < 0 else "·"
                    print(f"  {tenor:<4}  {old:.3f}% → {cur:.3f}%  ({arrow}{abs(delta_bp):.1f}bp)")

    # ------------------------------------------------------------------
    # MONTH-BOUNDARY GAP CHECK — the primary is scoped to the current month,
    # so anything before its earliest row is unreachable from that source.
    # ------------------------------------------------------------------
    stored = read_tsv_rows()
    floor, cutoff = find_gap_dates(stored, rows, backfill_from)
    gap_rows = []

    if verify_only or cutoff:
        if cutoff:
            print(f"\n  🔴 MONTH-BOUNDARY GAP DETECTED")
            print(f"  {'-'*60}")
            print(f"  Last stored close:        {cutoff}")
            print(f"  Earliest the primary has: {floor}")
            print(f"  ⚠️  The primary CSV is CURRENT-MONTH ONLY and can never serve the")
            print(f"      dates in between. Falling back to the MOF history file.")
        else:
            print(f"\n  BASIS CONTROL (--verify-history; no gap to fill)")
            print(f"  {'-'*60}")

        htext = fetch_mof_history_csv()
        hist = parse_mof_history_csv(htext) if htext else []
        if not hist:
            print(f"  🔴 History fetch/parse FAILED — gap NOT filled, nothing written.")
            print(f"     The stored series remains INCOMPLETE between {cutoff} and {floor}.")
            return 1

        print(f"\n  BASIS CONTROL — history file must reproduce what we already trust")
        ok, report = verify_history_basis(hist, stored, rows)
        for ln in report:
            print(ln)

        if not ok:
            print(f"\n  ⛔ BASIS CONTROL FAILED — refusing to write a single history row.")
            print(f"     Fails closed by design: an unverified second source is exactly")
            print(f"     how a wrong basis enters a series that past grades depend on.")
            return 1
        print(f"  ✅ Basis control PASSED — history is same-basis as the primary.")

        if cutoff:
            gap_rows = [r for r in hist if cutoff < r["date"] < floor]
            print(f"\n  Gap rows recovered: {len(gap_rows)}"
                  + (f"  [{gap_rows[0]['date']} … {gap_rows[-1]['date']}]" if gap_rows else ""))

        if verify_only:
            print(f"\n  --verify-history: nothing written.\n")
            return 0

    # Append to TSV (primary rows + any recovered gap rows)
    appended, backfilled = append_tsv(gap_rows + rows)
    if appended > 0:
        note = f" ({backfilled} BACKFILLED into the gap)" if backfilled else ""
        print(f"\n  Appended {appended} row(s) to JGB_YIELDS.tsv{note}")
    else:
        print(f"\n  TSV already current (no new rows)")

    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
