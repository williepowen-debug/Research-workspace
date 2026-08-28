#!/usr/bin/env python3
"""
PREDICTIONS DUE CHECK — the Resolve_By column, actually read.

WHY THIS EXISTS
---------------
On 2026-08-28 WAL-01 and WAL-02 had been OPEN for 126 DAYS and NOTHING on this
desk could flag them. The ledger's only date fields were:
  * Date_Made     -- never changes
  * Timeframe     -- FREE TEXT ("Q2-Q3 2026"), unparseable
  * Date_Resolved -- populated only AFTER resolution
So no field could ever go overdue. The gap was invisible by construction, not
by neglect: every check this desk owns passed clean while two live predictions
aged four months. (finding_dated_carry_item_has_no_expiry_check --
a carried assertion is a string; reading the file never evaluates it.)

Resolve_By was added the same day. This script is the half that reads it --
without a reader the column is just a longer string, and the row-counting
audits still pass. (finding_banded_threshold_with_no_metric_surface_is_untrippable.)

WHAT IT DOES NOT DO
-------------------
It never grades, resolves, or edits a row. An OVERDUE flag is a prompt to LOOK.
A prediction can be legitimately overdue -- a print slips, an instrument goes
dark -- and the correct response may be to re-pin Resolve_By WITH A REASON, not
to force a verdict. Forcing a grade to clear a flag is the failure this guards.

BLANKS ARE REPORTED AS THEIR OWN CLASS, never folded into "fine". KB.tsv's
Stale_By carries 41 blank ACTIVE rows that its checker can neither expire nor
certify, so its headline understates the real position. Same mistake is not
repeated here. (finding_silent_blank_evades_review.)

Advisory. Exit 0 unless --strict.
"""
import argparse, csv, datetime, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
LEDGER = os.path.normpath(os.path.join(HERE, '..', 'workbook', 'PREDICTIONS.tsv'))
# A row in one of these statuses is closed; Resolve_By is history, not a deadline.
CLOSED = {'RESOLVED', 'RESOLVED-FAILED', 'RESOLVED-CONFIRMED', 'INVALIDATED',
          'RETIRED', 'VOID', 'SUPERSEDED'}


def load(path):
    with open(path, encoding='utf-8') as fh:
        rows = [l for l in fh.read().split('\n') if l.strip() and not l.startswith('#')]
    rdr = csv.DictReader(rows, delimiter='\t')
    return list(rdr), rdr.fieldnames


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--quiet', action='store_true')
    ap.add_argument('--strict', action='store_true', help='exit 1 if any OPEN row is overdue or blank')
    ap.add_argument('--asof', default=None, help='YYYY-MM-DD (default: today)')
    a = ap.parse_args()

    if not os.path.exists(LEDGER):
        print(f'predictions-due: ledger not found at {LEDGER}', file=sys.stderr)
        return 0

    today = (datetime.date.fromisoformat(a.asof) if a.asof else datetime.date.today())
    rows, cols = load(LEDGER)

    if 'Resolve_By' not in (cols or []):
        print('⚠️  predictions-due: no Resolve_By column — nothing to read (add it, or this check is a no-op)')
        return 0

    overdue, blank, ok, closed = [], [], [], []
    for r in rows:
        pid = (r.get('Pred_ID') or '').strip()
        if not pid:
            continue
        status = (r.get('Status') or '').strip().upper()
        rb = (r.get('Resolve_By') or '').strip()
        if status in CLOSED:
            closed.append(pid); continue
        if not rb:
            blank.append(pid); continue
        try:
            due = datetime.date.fromisoformat(rb)
        except ValueError:
            blank.append(f'{pid} (unparseable "{rb}")'); continue
        age = (today - datetime.date.fromisoformat(r['Date_Made'])).days if r.get('Date_Made') else None
        (overdue if due < today else ok).append((pid, due, (today - due).days, age))

    hdr = f'PREDICTIONS DUE CHECK — Resolve_By, as of {today}'
    if a.quiet:
        if overdue or blank:
            bits = []
            if overdue:
                worst = max(overdue, key=lambda t: t[2])
                bits.append(f'{len(overdue)} OVERDUE (worst {worst[0]} by {worst[2]}d)')
            if blank:
                bits.append(f'{len(blank)} with NO Resolve_By')
            print(f'⚠️  predictions due: {"; ".join(bits)} — LOOK, do not force a grade')
        return 1 if (a.strict and (overdue or blank)) else 0

    print(hdr); print('=' * len(hdr))
    print(f'  open rows checked: {len(overdue)+len(blank)+len(ok)}   closed (skipped): {len(closed)}')
    for pid, due, late, age in sorted(overdue, key=lambda t: -t[2]):
        print(f'  🔴 {pid:<10} due {due}  OVERDUE {late}d   (open {age}d)')
    for pid in blank:
        print(f'  🟠 {pid:<10} NO Resolve_By — cannot be evaluated, and a blank is not a pass')
    for pid, due, late, age in sorted(ok, key=lambda t: t[1]):
        print(f'  🟢 {pid:<10} due {due}  in {-late}d   (open {age}d)')
    if overdue or blank:
        print('\n  ⚠️  An OVERDUE flag is a prompt to LOOK, never an instruction to grade.')
        print('     Legitimate responses: resolve it, or RE-PIN Resolve_By WITH A REASON.')
        print('     Forcing a verdict to clear the flag is the failure this check guards against.')
    else:
        print('\n  ✓ every open prediction carries a Resolve_By and none is past it')
    return 1 if (a.strict and (overdue or blank)) else 0


if __name__ == '__main__':
    sys.exit(main())
