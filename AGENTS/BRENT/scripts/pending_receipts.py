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

⇒ The check: for every EXECUTION LOG row still marked PENDING/⏳, look the ticker up in the
FORGE mirror and report when FORGE shows closure language the pending row has not absorbed.

FAIL-CLOSED: if FORGE is unreadable, that is FINDINGS, not OK -- an unreadable mirror is
exactly when a stale PENDING row is most dangerous. A check that certifies clean when its
own input is missing is the silent-fallback-green class boot.py exists to kill.

⚠️ WHAT THIS CANNOT DO, so nobody reads a clean run as an all-clear: it compares TEXT in two
files. It cannot see a fill that reached NEITHER surface, it cannot price or date anything,
and a clean run means "FORGE does not contradict my pending rows" -- never "my pending rows
are true." Only the broker settles that. [[finding_freshness_check_cannot_catch_a_fresh_lie]]

Exit: 0 = no contradiction found · 2 = FINDINGS · 1 = check itself broke (desk convention).
"""
import re
import sys
from pathlib import Path

BRENT = Path(__file__).resolve().parent.parent
ROOT = BRENT.parent.parent
TRADE = BRENT / "TRADE.md"
FORGE = ROOT / "FORGE" / "STATUS.md"

PENDING_RE = re.compile(r"PENDING|⏳", re.I)
# ⛔ v1 OF THIS CHECK FAILED ON ITS FIRST LIVE RUN, both ways, and the fixes are below.
# [[finding_test_the_guard_not_just_the_guarded]] — a guard's own v1 fails on first RUN.
#
# ① A RESOLVED row that NARRATES its own former pendingness re-triggered the scanner: my
#    corrected XLE row contains the sentence "the row sat PENDING for three days". Prose
#    MENTIONING the marker reclassified the row.
#    [[finding_marker_word_in_prose_disables_the_scanner_that_reads_for_it]]
RESOLVED_RE = re.compile(
    r"RESOLVED|RECEIPT IN HAND|\bFILLED\b|DISCHARGED|✅", re.I)
# Closure language a mirror uses. Deliberately broad: a FALSE POSITIVE costs one lookup,
# a FALSE NEGATIVE costs what the XLE row cost.
CLOSED_RE = re.compile(r"\bSOLD\b|\bCLOSED\b|\bFLAT\b|×0|\bx0\b|qty\s*0\b|\b0\s*—\s*SOLD", re.I)
# Tickers this desk can own. Explicit allowlist beats a regex that harvests every capital word.
TICKERS = ("USO", "XLE", "XOP", "STNG", "EOG", "VLO", "MPC", "OXY", "CVX", "XOM", "BNO", "LNG")


def rows_with_pending(text):
    out = []
    for ln in text.splitlines():
        if not ln.lstrip().startswith("|"):
            continue
        if PENDING_RE.search(ln) and not RESOLVED_RE.search(ln):
            out.append(ln)
    return out


def main():
    if not TRADE.exists():
        print("🔴 FAIL: TRADE.md not found", file=sys.stderr)
        return 1
    trade = TRADE.read_text(encoding="utf-8")

    pend = rows_with_pending(trade)
    if not pend:
        print("  ✅ PENDING-RECEIPTS: no EXECUTION LOG row is marked PENDING/⏳.")
        print("     ⚠️  Clean here means FORGE does not CONTRADICT this surface — never that")
        print("        the surface is true. Only the broker settles a position.")
        return 0

    if not FORGE.exists():
        print(f"  🔴 FINDINGS: {len(pend)} PENDING row(s) and the FORGE mirror is UNREADABLE at {FORGE}.")
        print("     Fail-closed by design: an unreadable mirror is exactly when a stale PENDING")
        print("     row is most dangerous. Verify each row at the broker before trusting it.")
        return 2
    forge = FORGE.read_text(encoding="utf-8")

    findings = []
    for row in pend:
        for tic in TICKERS:
            if not re.search(rf"\b{tic}\b", row):
                continue
            for fl in forge.splitlines():
                # ② v1 matched FORGE's long PROSE banners, which contain tickers and the word
                #    "SOLD" in narrative. Require an actual TABLE ROW: pipe-delimited with
                #    enough cells to be a position row, not a paragraph that starts with ">".
                if not fl.lstrip().startswith("|") or fl.count("|") < 4:
                    continue
                if re.search(rf"\b{tic}\b", fl) and CLOSED_RE.search(fl):
                    findings.append((tic, row.strip()[:150], fl.strip()[:200]))
                    break

    if not findings:
        print(f"  ✅ PENDING-RECEIPTS: {len(pend)} PENDING row(s); FORGE shows no closure "
              f"language for any of their tickers.")
        print("     ⚠️  NOT an all-clear — a fill that reached neither surface is invisible here.")
        return 0

    print(f"  🔴 PENDING-RECEIPTS — FINDINGS ({len(findings)}): FORGE contradicts a PENDING row.")
    print("     ⛔ Do NOT 'reaffirm' these. Resolve each at the artifact FORGE names, or at the broker.")
    for tic, row, fl in findings:
        print(f"\n     ── {tic} ──")
        print(f"        TRADE.md (still PENDING): {row}")
        print(f"        FORGE mirror says       : {fl}")
    print("\n     ⚠️  FORGE is a MIRROR, not the broker. It can itself be stale; it is evidence")
    print("        that the two surfaces disagree, never a fill receipt on its own.")
    return 2


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as exc:  # noqa: BLE001 - a broken check must never read as OK
        print(f"🔴 FAIL: pending_receipts.py raised {type(exc).__name__}: {exc}", file=sys.stderr)
        sys.exit(1)
