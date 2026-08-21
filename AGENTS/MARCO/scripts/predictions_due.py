#!/usr/bin/env python3
"""
MARCO Predictions / Expected-Signals Due Scan
Resolves the free-text Timeframe on every OPEN prediction (and the "Expected By"
on every active expected-signal) to an END date, then flags anything whose window
has passed (DUE for resolution) or is about to pass (DUE SOON).

This is the boot-time guard against a prediction sitting OPEN-but-stale past its
window. It FAILS LOUD: any timeframe it cannot parse is printed as UNPARSEABLE
rather than silently skipped — a skipped prediction is exactly the failure mode
this tool exists to kill.

Scans:
  thesis/PREDICTIONS.tsv  — rows where Status == OPEN
  EXPECTED_SIGNALS.md     — active table rows (Status not RESOLVED)

Usage:
  .venv/bin/python3 AGENTS/MARCO/scripts/predictions_due.py
  .venv/bin/python3 AGENTS/MARCO/scripts/predictions_due.py --soon 14   # DUE-SOON window
"""

import calendar
import re
import sys
from datetime import datetime, date
from pathlib import Path
import sys as _sys
_sys.path.insert(0, str(Path(__file__).resolve().parent))
from tsvutil import read_tsv_numbered  # noqa: E402

MARCO_DIR = Path(__file__).resolve().parent.parent
PREDICTIONS_TSV = MARCO_DIR / "thesis" / "PREDICTIONS.tsv"
EXPECTED_SIGNALS_MD = MARCO_DIR / "EXPECTED_SIGNALS.md"

DEFAULT_SOON = 21  # days: a window closing within this many days = DUE SOON

MONTHS = {m.lower(): i for i, m in enumerate(calendar.month_abbr) if m}
MONTHS.update({m.lower(): i for i, m in enumerate(calendar.month_name) if m})

QUARTER_END = {1: (3, 31), 2: (6, 30), 3: (9, 30), 4: (12, 31)}
HALF_END = {1: (6, 30), 2: (12, 31)}


def _eom(year, month):
    return date(year, month, calendar.monthrange(year, month)[1])


def parse_timeframe(s):
    """Resolve a free-text timeframe to the END date of its window.
    Returns a date, or None if unparseable. Normalizes en-dash to hyphen."""
    if not s:
        return None
    t = s.strip().replace("–", "-").replace("—", "-")
    tl = t.lower()

    # "NOW" / "immediate"
    if tl in ("now", "immediate", "imminent"):
        return date.today()

    # Explicit date: "By Mar 21 2026" / "Mar 21 2026" / "Jun 10"
    # (?!\d) stops the day from swallowing the first 2 digits of a bare year,
    # e.g. "May 2026" must NOT parse as May-20.
    m = re.search(r"([a-z]{3,9})\.?\s+(\d{1,2})(?!\d)(?:,?\s*(\d{4}))?", tl)
    if m and m.group(1) in MONTHS:
        mon = MONTHS[m.group(1)]
        day = int(m.group(2))
        yr = int(m.group(3)) if m.group(3) else date.today().year
        try:
            return date(yr, mon, day)
        except ValueError:
            pass

    # Year extraction (needed by the period forms below)
    ym = re.search(r"(20\d{2})", tl)
    year = int(ym.group(1)) if ym else date.today().year

    # Quarter range "Q2-Q3 2026" → end of the LATER quarter
    m = re.search(r"q([1-4])\s*-\s*q([1-4])", tl)
    if m:
        q = max(int(m.group(1)), int(m.group(2)))
        mo, dy = QUARTER_END[q]
        return date(year, mo, dy)

    # Single quarter "Q2 2026" / "Through Q2 2026"
    m = re.search(r"q([1-4])", tl)
    if m:
        mo, dy = QUARTER_END[int(m.group(1))]
        return date(year, mo, dy)

    # Half "H2 2026"
    m = re.search(r"h([12])", tl)
    if m:
        mo, dy = HALF_END[int(m.group(1))]
        return date(year, mo, dy)

    # Fiscal year "FY 2026" → federal FY ends Sep 30
    if re.search(r"fy\s*20\d{2}", tl) or re.search(r"fy\s*'?\d{2}", tl):
        return date(year, 9, 30)

    # "2025 FINAL" / "2025 final" → calendar year end
    if re.search(r"20\d{2}\s*final", tl) or tl.strip() == str(year):
        return date(year, 12, 31)

    # Month range "Mar-May 2026" / "Aug-Sep 2026" → end of later month
    m = re.search(r"([a-z]{3,9})\s*-\s*([a-z]{3,9})\s*20?\d{0,2}", tl)
    if m and m.group(1) in MONTHS and m.group(2) in MONTHS:
        return _eom(year, MONTHS[m.group(2)])

    # Single month "Mar 2026" / "Dec 2026"
    m = re.search(r"\b([a-z]{3,9})\b", tl)
    if m and m.group(1) in MONTHS:
        return _eom(year, MONTHS[m.group(1)])

    return None


PRED_SCHEMA_WARNINGS = []


def load_predictions():
    """Read PREDICTIONS.tsv by HEADER NAME (never by position).

    ⚠️ The right-pad below is a *tolerance*, and tolerance is what let a schema
    defect rot for two months (MAINTENANCE T1-D, fixed 2026-07-31): 10 of 16 rows
    were 8 columns against a 9-column header. Padding put those rows' NOTES text
    under the `Outcome` key and left `Notes` empty, silently — a reader asking for
    an outcome got notes and never knew. It also made hand-editing hazardous: a
    single dropped field during a confidence re-rate is invisible to a padding parser.

    So the pad stays (it must not crash boot) but it now ANNOUNCES itself via
    PRED_SCHEMA_WARNINGS, which main() prints. A tolerant reader that stays quiet
    is how a malformed file passes review forever.
    """
    if not PREDICTIONS_TSV.exists():
        return None
    rows = []
    PRED_SCHEMA_WARNINGS.clear()
    # Banner-tolerant (PAT-044), and TRUE file line numbers are preserved because
    # every warning below cites one — a re-based number sends the operator to an
    # innocent row, which is worse than no warning. See scripts/tsvutil.py.
    header, data = read_tsv_numbered(PREDICTIONS_TSV)
    nc = len(header)
    for ln, parts in data:
        if len(parts) < 2:
            continue
        if len(parts) != nc:
            PRED_SCHEMA_WARNINGS.append(
                f"line {ln} ({parts[0]}): {len(parts)} fields vs {nc}-col header "
                f"— padded to parse; fields after the gap sit under the WRONG key")
        row = dict(zip(header, parts + [""] * (nc - len(parts))))
        # An OPEN prediction cannot have an outcome; a resolved one must.
        st = row.get("Status", "").strip().upper()
        has_out = bool(row.get("Outcome", "").strip())
        if st == "OPEN" and has_out:
            PRED_SCHEMA_WARNINGS.append(
                f"line {ln} ({parts[0]}): Status=OPEN but Outcome is populated "
                f"— usually means notes landed in the Outcome column")
        elif st and st != "OPEN" and not has_out:
            PRED_SCHEMA_WARNINGS.append(
                f"line {ln} ({parts[0]}): Status={st} but Outcome is EMPTY "
                f"— a resolved prediction with no recorded outcome cannot be scored")
        if any('""' in v for v in parts):
            PRED_SCHEMA_WARNINGS.append(
                f'line {ln} ({parts[0]}): doubled quotes — CSV-quoting artifact '
                f'leaked into a TSV; collapse "" to "')
        rows.append(row)
    return rows


def load_expected_signals():
    """Parse the Active table of EXPECTED_SIGNALS.md → list of dicts.
    Stops at the '## Resolved' heading."""
    if not EXPECTED_SIGNALS_MD.exists():
        return None
    rows = []
    with open(EXPECTED_SIGNALS_MD) as f:
        for line in f:
            if line.strip().lower().startswith("## resolved"):
                break
            if line.lstrip().startswith("| ES-MARCO-"):
                cells = [c.strip() for c in line.strip().strip("|").split("|")]
                if len(cells) >= 4:
                    rows.append({
                        "id": cells[0], "signal": cells[1],
                        "expected_by": cells[2], "status": cells[3],
                    })
    return rows


def main():
    soon = DEFAULT_SOON
    if "--soon" in sys.argv:
        i = sys.argv.index("--soon")
        if i + 1 < len(sys.argv):
            soon = int(sys.argv[i + 1])

    today = date.today()
    print(f"\n{'='*72}")
    print(f"  MARCO Predictions / Expected-Signals Due Scan — {datetime.now():%Y-%m-%d %H:%M}")
    print(f"{'='*72}")

    rc = 0

    # ---- PREDICTIONS ----
    preds = load_predictions()
    if preds is None:
        print(f"\n  ❌ ERROR: {PREDICTIONS_TSV} not found")
        rc = 1
    else:
        if PRED_SCHEMA_WARNINGS:
            print(f"\n  ⚠️  PREDICTIONS.tsv SCHEMA — {len(PRED_SCHEMA_WARNINGS)} issue(s):")
            for w in PRED_SCHEMA_WARNINGS:
                print(f"      · {w}")
            print("      (the parser padded these to keep running — the file is still wrong)")
        due, due_soon, unparsed = [], [], []
        for p in preds:
            if p.get("Status", "").strip().upper() != "OPEN":
                continue
            end = parse_timeframe(p.get("Timeframe", ""))
            if end is None:
                unparsed.append(p)
                continue
            delta = (end - today).days
            if delta < 0:
                due.append((end, delta, p))
            elif delta <= soon:
                due_soon.append((end, delta, p))

        print(f"\n  PREDICTIONS — {sum(1 for p in preds if p.get('Status','').strip().upper()=='OPEN')} OPEN")
        if due:
            print(f"\n  🔴 DUE for resolution — window passed ({len(due)}):")
            for end, delta, p in sorted(due, key=lambda r: r[0]):
                print(f"    {p['Pred_ID']:<8} window ended {end} ({-delta}d ago) | {p['Timeframe']}")
                print(f"         ↳ {p['Prediction'][:80]}")
        if due_soon:
            print(f"\n  🟠 DUE SOON — closes within {soon}d ({len(due_soon)}):")
            for end, delta, p in sorted(due_soon, key=lambda r: r[0]):
                print(f"    {p['Pred_ID']:<8} closes {end} (in {delta}d) | {p['Timeframe']}")
                print(f"         ↳ {p['Prediction'][:80]}")
        if not due and not due_soon:
            print("    ✓ no OPEN prediction past or near its window")
        if unparsed:
            rc = 1
            print(f"\n  ⚠️  UNPARSEABLE timeframe — {len(unparsed)} (fix or extend parser):")
            for p in unparsed:
                print(f"    {p['Pred_ID']:<8} Timeframe='{p.get('Timeframe','')}'")

    # ---- EXPECTED SIGNALS ----
    es = load_expected_signals()
    if es is None:
        print(f"\n  (EXPECTED_SIGNALS.md not found — skipped)")
    else:
        es_due, es_unparsed = [], []
        for s in es:
            st = s["status"].upper()
            if "RESOLVED" in st or "APPEARED" in st or "DID_NOT_APPEAR" in st:
                continue
            end = parse_timeframe(s["expected_by"])
            if end is None:
                es_unparsed.append(s)
                continue
            delta = (end - today).days
            if delta < 0:
                es_due.append((end, delta, s))

        print(f"\n  EXPECTED SIGNALS — {len(es)} active")
        if es_due:
            print(f"\n  🟠 PAST DEADLINE — assess APPEARED / DID_NOT_APPEAR ({len(es_due)}):")
            for end, delta, s in sorted(es_due, key=lambda r: r[0]):
                print(f"    {s['id']:<14} expected by {end} ({-delta}d ago) | status: {s['status'][:30]}")
                print(f"         ↳ {s['signal'][:80]}")
        else:
            print("    ✓ no active expected-signal past deadline")
        if es_unparsed:
            print(f"\n  ⚠️  UNPARSEABLE 'Expected By' — {len(es_unparsed)}:")
            for s in es_unparsed:
                print(f"    {s['id']:<14} expected_by='{s['expected_by']}'")

    print()
    return rc


if __name__ == "__main__":
    sys.exit(main())
