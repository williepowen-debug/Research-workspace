#!/usr/bin/env python3
"""Cross-check TRADE.md's PENDING execution rows against the FORGE position mirror.

WHY THIS EXISTS (2026-09-14, Will-visible; supersedes: nothing — it MAKES EXECUTABLE the
boot step 6c PENDING-row guard that already existed in prose and passed as a no-op).

THE FAILURE IT IS BUILT FROM, stated plainly because it was mine:
  XLE Sep-30 65C x1 was SOLD 2026-09-11 ~10:07 ET at $1.51. TERRY held the verbatim Fidelity
  activity row and committed it the same day (bcc962bbd, 12:22 ET). FORGE/STATUS.md carried
  it from 9/11. NO packet was routed to BRENT, and BRENT's TRADE.md carried the position as
  OPEN with its receipt "PENDING" for three days -- through two full boots that ran step 6c.
  On 2026-09-14 I quoted Will a live bid/ask on that position and built guidance around it.
  WILL corrected it, with a broker screenshot.

⛔ THE DEFECT IN THE OLD GUARD WAS ITS VERB. "Resolve-OR-REAFFIRM every PENDING row" lets a
session discharge the step by re-reading its own label: I confirmed the row still SAID pending
instead of checking whether it still WAS. REAFFIRM has no evidentiary floor, so the guard
passes on the strength of the thing it is supposed to doubt.
[[finding_record_of_an_action_is_not_the_action]] -- check the TARGET artifact, never the record.
[[finding_dated_carry_item_has_no_expiry_check]] -- a carried assertion never self-evaluates.

★ THE STRUCTURAL POINT, which is the transmission problem in one line:
  position truth is PUSH-routed (packets) but it LIVES in a PULL surface (FORGE/STATUS.md).
  A desk that owns a leg does not read FORGE at boot -- it waits for a packet. So when no
  packet is sent, the desk's own surface rots silently while the correct value sits in a file
  it never opens. This check closes that loop from the READER's side, which is the only side
  this desk controls. It does not fix routing and does not pretend to.

September 15 extension: scan only EXECUTION LOG and POSITIONS (live). Explicit
receipt_status markers take precedence; outstanding receipts always produce findings.
FORGE closure text is a candidate for contract/account matching, never proof by ticker.
Positions with explicit expiry=YYYY-MM-DD and no terminal outcome also produce findings.

Scope: text-only checks cannot see fills absent from both files, infer expiry dates
from contract prose, or establish sale prices. Missing required inputs fail closed.
A clean run means no unresolved receipt or explicitly dated expired holding was found
within these sections; it does not certify broker holdings or profit/loss.

Exit: 0 = no scoped outstanding item · 2 = FINDINGS · 1 = check itself broke.

"""
import re
import sys
from pathlib import Path
from datetime import date

BRENT = Path(__file__).resolve().parent.parent
ROOT = BRENT.parent.parent
TRADE = BRENT / "TRADE.md"
FORGE = ROOT / "FORGE" / "STATUS.md"

# September 15: extends the existing receipt check; supersedes whole-file table
# scanning and false-green unresolved receipts. L20/L22/L27: falsify with real
# navigation, historical fill prose, a different contract, and a missing section.
PENDING_RE = re.compile(r"\bPENDING\b|\bUNRESOLVED\b|⏳", re.I)
CLOSED_RE = re.compile(r"\bSOLD\b|\bCLOSED\b|\bFLAT\b|×0|\bx0\b", re.I)
TICKERS = ("USO", "XLE", "XOP", "STNG", "EOG", "VLO", "MPC", "OXY", "CVX", "XOM", "BNO", "LNG")


def section_rows(text, title):
    """Read one exact level-2 section. Missing/empty perimeter cannot pass."""
    match = re.search(r"^## " + re.escape(title) + r"\s*$", text, re.M)
    if not match:
        raise ValueError(f"missing TRADE section: {title}")
    body = re.split(r"^## ", text[match.end():], maxsplit=1, flags=re.M)[0]
    rows = []
    for line in body.splitlines():
        if not line.lstrip().startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if cells[0] in ("Date", "Position") or all(re.fullmatch(r"[-: ]+", c) for c in cells):
            continue
        rows.append((line, cells))
    if not rows:
        raise ValueError(f"no data rows in TRADE section: {title}")
    return rows


def rows_with_pending(text):
    out = []
    for line, cells in section_rows(text, "EXECUTION LOG"):
        if len(cells) != 3:
            raise ValueError("EXECUTION LOG row must have Date / Action / Detail")
        # An explicit marker wins; an entry fill elsewhere in the prose must
        # never suppress an outstanding exit receipt on the same row.
        explicit = re.search(r"receipt_status=(PENDING|RESOLVED)\b", line, re.I)
        if explicit:
            if explicit[1].upper() == "PENDING":
                out.append(line)
            continue
        detail = re.sub(r"[*`]|✅|⏳", "", cells[2]).strip()
        resolved = re.match(r"(?:RESOLVED\b|RECEIPT IN HAND\b|DISCHARGED\b)", detail, re.I)
        # The legacy closed-spread row uses an hourglass immediately qualified
        # by RESOLVED. Ignore that pair, not a separate PENDING in the same row.
        markers = re.sub(r"⏳\s*RESOLVED\b", "RESOLVED", line, flags=re.I)
        if PENDING_RE.search(markers) and not resolved:
            out.append(line)
    return out


def expired_without_outcome(text, today):
    out = []
    for line, cells in section_rows(text, "POSITIONS (live)"):
        if len(cells) != 4:
            raise ValueError("POSITIONS row must have four cells")
        # Examine identity/type/status only. A different historical sale in the
        # source cell does not close this position. Never infer a year from today.
        state = " ".join(cells[:3])
        if CLOSED_RE.search(state):
            continue
        expiry = re.search(r"expiry=(\d{4}-\d{2}-\d{2})\b", state)
        if expiry and date.fromisoformat(expiry[1]) < today:
            out.append(line)
    return out


def main():
    try:
        trade = TRADE.read_text(encoding="utf-8")
        pend = rows_with_pending(trade)
        expired = expired_without_outcome(trade, date.today())
    except (OSError, ValueError) as exc:
        print(f"  🔴 PENDING-RECEIPTS: CANNOT CERTIFY: {exc}")
        return 2

    if not pend and not expired:
        print("  ✅ PENDING-RECEIPTS: no unresolved execution receipts or elapsed explicit expiries.")
        print("     Scope: EXECUTION LOG markers and POSITIONS expiry=YYYY-MM-DD fields only.")
        print("     Broker truth and unrecorded trades remain outside this text check.")
        return 0

    print(f"  🔴 PENDING-RECEIPTS: {len(pend)} unresolved receipt(s); {len(expired)} elapsed expiry row(s).")
    for row in pend:
        print("     UNRESOLVED RECEIPT: " + row.strip())
    for row in expired:
        print("     EXPIRY OUTCOME REQUIRED: " + row.strip())
    try:
        forge = FORGE.read_text(encoding="utf-8")
    except OSError as exc:
        print(f"     FORGE unavailable: {exc}. Resolve at owner/broker; never reaffirm from the label.")
        return 2
    for row in pend + expired:
        for tic in TICKERS:
            if not re.search(rf"\b{tic}\b", row):
                continue
            candidates = [ln for ln in forge.splitlines()
                          if ln.lstrip().startswith("|") and ln.count("|") >= 4
                          and re.search(rf"\b{tic}\b", ln) and CLOSED_RE.search(ln)]
            if candidates:
                print(f"     {tic}: FORGE has closure CANDIDATES. Match contract/account before resolving:")
                for candidate in candidates:
                    print("       " + candidate.strip())
    print("     Absence of a FORGE contradiction does not resolve an owed receipt.")
    return 2


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as exc:  # noqa: BLE001 - a broken check must never read as OK
        print(f"🔴 FAIL: pending_receipts.py raised {type(exc).__name__}: {exc}", file=sys.stderr)
        sys.exit(1)
