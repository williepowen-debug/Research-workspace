#!/usr/bin/env python3
"""
Predictions-due scanner — the boot backstop for OPEN predictions whose Timeframe
has passed (or is imminent). Prevents the silent OPEN-but-stale miss (e.g. BRT-09
Q1-Q2 2026 sat unresolved past Q2-close until caught mid-session Jul-1).

Reads thesis/PREDICTIONS.tsv, parses each OPEN row's Timeframe into a best-effort
END date, and flags:
  🔴 DUE     — end date <= today (resolve at closeout: resolve / re-arm / push-date)
  🟠 SOON    — end date within the next 7 days
Event-conditional / open-ended timeframes ("Within X of <event>", "Ongoing") have
no fixed event date. Explicit OUTER BOUND dates are monitored without assuming the precondition occurred.

Run standalone or via boot.py. Exit 2 for due/unparseable or unresolved sub-obligation findings; 0 otherwise.
"""
import io
import re
import sys
from datetime import date, timedelta
from pathlib import Path

PRED = Path(__file__).resolve().parent.parent / "thesis" / "PREDICTIONS.tsv"

MONTHS = {
    "jan": 1, "feb": 2, "mar": 3, "apr": 4, "may": 5, "jun": 6,
    "jul": 7, "aug": 8, "sep": 9, "oct": 10, "nov": 11, "dec": 12,
}
Q_END = {1: (3, 31), 2: (6, 30), 3: (9, 30), 4: (12, 31)}


def _last_day(y, m):
    return (date(y + (m // 12), (m % 12) + 1, 1) - timedelta(days=1)).day


def parse_end_date(tf):
    """Best-effort LATEST resolvable end-date from a free-text timeframe. None if none."""
    s = tf.lower()
    cands = []

    # Explicit month day, year  e.g. "By Jul 3 2026", "By Jul 3, 2026"
    for m, d, y in re.findall(r"(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*\.?\s+(\d{1,2})(?:st|nd|rd|th)?,?\s+(\d{4})", s):
        try:
            cands.append(date(int(y), MONTHS[m], min(int(d), _last_day(int(y), MONTHS[m]))))
        except ValueError:
            pass

    # Quarters (incl. ranges "Q1-Q2 2026", "end-Q3 2026") — year attaches to the group
    for ym in re.finditer(r"((?:q[1-4][\s\-–to]*)+)\s*(\d{4})", s):
        yr = int(ym.group(2))
        qs = [int(q) for q in re.findall(r"q([1-4])", ym.group(1))]
        if qs:
            mm, dd = Q_END[max(qs)]
            cands.append(date(yr, mm, dd))

    # Halves "H2 2026", "H1 2027"
    for h, y in re.findall(r"h([12])\s*(\d{4})", s):
        cands.append(date(int(y), 6, 30) if h == "1" else date(int(y), 12, 31))

    # Month range "May-June 2026" / "May–Jun 2026" (no day) -> end of 2nd month
    for m1, m2, y in re.findall(r"(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*[\s\-–to]+(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*\s+(\d{4})", s):
        yr, mm = int(y), MONTHS[m2]
        cands.append(date(yr, mm, _last_day(yr, mm)))

    # Single "Month YYYY" (no day) -> end of month
    for m, y in re.findall(r"(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*\s+(\d{4})", s):
        yr, mm = int(y), MONTHS[m]
        cands.append(date(yr, mm, _last_day(yr, mm)))

    # ⛔ ADDED 2026-09-07 (CODEX review, Will-approved). ISO `YYYY-MM-DD` had NO pattern here,
    # so the MOST EXPLICIT timeframe form was the one the parser could not read: `By 2026-09-30`
    # (BRT-29) and `By 2026-10-26` (BRT-30) both returned None and were silently skipped, while
    # the FUZZY form `By end-Q3 2026` (BRT-26) parsed fine. A scanner that handles "end-Q3 2026"
    # and not "2026-09-30" is inverted: precision was being punished.
    # supersedes: none — EXTENDS parse_end_date.
    for y, mo, d in re.findall(r"(\d{4})-(\d{2})-(\d{2})", s):
        try:
            cands.append(date(int(y), int(mo), int(d)))
        except ValueError:
            pass

    return max(cands) if cands else None


# Event-conditional timeframes are gated by a PRECONDITION, not a calendar — the docstring says
# they are skipped BY DESIGN. Separating them from genuinely-unparseable rows matters: a guard
# that reports a deliberate design choice as a defect cries wolf every single boot, and a guard
# that is always red is read as noise and then ignored — which would re-create the blindness
# this scanner exists to remove. [[finding_loosening_a_check_to_kill_a_false_alarm_inverts_the_failure_direction]]
EVENT_CONDITIONAL_RE = re.compile(
    r"within\s+\d+|within\s+(?:days|weeks|months)|ongoing|of\s+\w+ing\b|upon\b|when\b|if\b",
    re.IGNORECASE)


def scan(today=None, debug=False):
    today = today or date.today()
    soon = today + timedelta(days=7)
    due, upcoming, unparsed, event_cond = [], [], [], []
    with io.open(PRED, "r", encoding="utf-8", newline="\n") as f:
        for ln in f:
            if ln.startswith("#") or ln.startswith("Pred_ID"):
                continue
            fx = ln.rstrip("\n").split("\t")
            if len(fx) < 6 or not fx[0].startswith("BRT-"):
                continue
            pid, tf, status = fx[0], fx[4], fx[5]
            # ⛔⛔ FIXED 2026-09-07 (CODEX review). THIS READ `if status != "OPEN": continue` —
            # an EXACT string match. Every OPEN row that had been ANNOTATED was therefore
            # dropped: BRT-07 ("OPEN — re-dated 2026-08-13; OUTER BOUND 2027-03-06") and BRT-12
            # ("OPEN — re-dated, resolves 2026-09-30") never reached the parser at all.
            # ★ THE INVERSION IS THE POINT: annotating a status to make it MORE informative —
            # exactly what closeout step 8 tells this desk to do when it re-dates a row —
            # REMOVED that row from the backstop scan. The better-documented rows were the
            # invisible ones. Combined with the ISO-date gap above, 4 of 5 OPEN predictions
            # were unscanned while boot printed "✅ ran cleanly, no alerts".
            # [[finding_scan_keyed_on_naming_reads_local_form_as_absence]]
            if not status.upper().startswith("OPEN"):
                continue
            end = parse_end_date(tf)
            outer = re.search(r"OUTER BOUND\s+(\d{4}-\d{2}-\d{2})", status, re.I)
            if outer:
                bound = parse_end_date(outer.group(1))
                if bound:
                    end = min(end, bound) if end else bound
                    tf += f" [explicit outer bound {bound}; event precondition not inferred]"
            if debug:
                print(f"    {pid}: tf={tf!r} -> end={end}")
            if end is None:
                # ⛔ WAS a bare `continue` — an unparseable timeframe on an OPEN prediction
                # vanished with no signal, which is the precise shape of the miss this whole
                # script exists to prevent. Now it is reported.
                if EVENT_CONDITIONAL_RE.search(tf):
                    event_cond.append((pid, tf, status))
                else:
                    unparsed.append((pid, tf, status))
                continue
            if end <= today:
                due.append((pid, tf, end))
            elif end <= soon:
                upcoming.append((pid, tf, end))
    return due, upcoming, unparsed, event_cond


def sub_obligations(today=None):
    """Surface the existing unresolved BRT-29 M obligation, not a final grade.

    Extends this scanner; supersedes the silent Timeframe-only treatment of M.
    Date comes from the registered claim; current unresolved state from Notes.
    No additional deadline/state ledger is created.
    """
    today = today or date.today()
    findings = []
    for line in PRED.read_text().splitlines():
        fields = line.split("\t")
        if len(fields) < 10 or fields[0] != 'BRT-29' or not fields[5].upper().startswith('OPEN'):
            continue
        if not re.search(r'\bM unresolved\b', fields[-1], re.I):
            continue
        claim = fields[2]
        part = claim.split('(M)', 1)[-1].split('(T)', 1)[0]
        match = re.search(r'by\s+(Aug)[- ](\d{1,2})', part, re.I)
        end = parse_end_date(f'{match.group(1)} {match.group(2)}, {fields[1][:4]}') if match else None
        if end is None or end <= today + timedelta(days=7):
            findings.append((fields[0], 'M evidence review; final prediction window unchanged', end))
    return findings


def main():
    debug = "--debug" in sys.argv
    print("  ⏳ Predictions-Due Scan...")
    due, upcoming, unparsed, event_cond = scan(debug=debug)
    obligations = sub_obligations()
    for pid, label, end in obligations:
        print(f"      ⚠️ SUB-OBLIGATION REVIEW: {pid} {label}; deadline {end or 'UNPARSEABLE'}; remains unresolved")
    # ⛔ UNPARSED IS REPORTED BEFORE THE CLEAN VERDICT, and it BLOCKS the clean verdict. An OPEN
    # prediction whose timeframe this parser cannot read is NOT evidence of "no alerts" — it is
    # evidence that the backstop did not cover that row. Printing ✅ over it is the silent-green
    # class. [[finding_lenient_parser_reports_unparseable_as_a_behavior]]
    if event_cond:
        print("      ⚪ EVENT-CONDITIONAL (skipped BY DESIGN — a precondition gates these, not a"
              " calendar). Listed so the exclusion is never silent:")
        for pid, tf, status in event_cond:
            print(f"      ⚪ {pid}  timeframe={tf!r}; no dated outer bound parsed")
    if unparsed:
        print("      🔴 UNPARSEABLE TIMEFRAME on an OPEN prediction — the scan DID NOT COVER these:")
        for pid, tf, status in unparsed:
            print(f"      🔴 {pid}  timeframe={tf!r}  status={status[:40]!r}")
        print("         ⇒ fix the Timeframe cell or extend parse_end_date. Until then these rows"
              " can NEVER come due, exactly like the STUCK-row blindness the boot doc warns of.")
    if not due and not upcoming:
        if unparsed or obligations:
            print("      ⚠️  no DUE/SOON rows AMONG THE ROWS THAT PARSED — check SUB-OBLIGATION/UNPARSEABLE findings above.")
            return 2
        print("      ✅ no OPEN predictions past (or within 7d of) their timeframe")
        return 0
    if due:
        print("      🔴 DUE — resolve at closeout (resolve / re-arm-with-reason / push-date-with-reason):")
        for pid, tf, end in due:
            print(f"      🔴 {pid}  (timeframe {tf!r} ended {end})")
    if upcoming:
        print("      🟠 SOON (≤7d) — pre-stage resolution:")
        for pid, tf, end in upcoming:
            print(f"      🟠 {pid}  (timeframe {tf!r} ends {end})")
    return 2 if (due or unparsed or obligations) else 0


if __name__ == "__main__":
    sys.exit(main())
