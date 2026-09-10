# XLE September 30 $65C — existing approved exit tracking
**Setup ID:** `TRY-EXIT-XLE65C`
**Updated:** 2026-09-09 21:1x ET (owner expiry-pass write-back; prior 2026-09-08T17:27:10-04:00)
**Terry verdict:** CONDITIONAL
**Tracking state:** STAGED — approved exit selected; execution unconfirmed.

This is owner write-back of WQ-168 §⑦, approved by Will September 3 at 12:45 ET. No new proposal or approval is requested. Full original expiry card: `PROME/inbox/processed/2026-09-03_from-TERRY_expiry-pass-Sep18-Sep30-seven-lines-007-grade-UNKNOWN-mirrors.md`. Its September 6 “Sat” labels are calendar errors: that date was Sunday. The date and approved rule are unchanged.

## Observed condition and consequence
XLE September 8 regular close **$64.77**, below **$66.50** by **$1.73**. Source: Yahoo **MIRROR**, daily bar and regular-close metadata agree, metadata September 8 16:00 ET; capture September 8 16:21:41 ET in PROME's preserved evidence, sha256 in `../outbox/2026-09-08_owner-market-evidence.json`. This is not an independently obtained exchange close.

The existing rule selects **sell to close both XLE September 30, 2026 $65 calls at the bid on the September 9 open**. Will checks the live Fidelity position and open orders first. The dated exit still binds on a red open; a September 9 rebound does not replace the September 8 test. No order submitted or fill claimed by TERRY. Current holdings/orders/executable bid/fill are **UNKNOWN**; `[POSITION_STATE_INCOMPLETE]`. Do not sell contracts no longer held or duplicate an existing order.

## 2026-09-09 21:1x ET — SELECTED at the 9/8 close; fill UNKNOWN pending Will's receipt

**Record, in the required form: SELECTED at the 9/8 close; fill UNKNOWN pending Will's receipt.** The 9/8 test ($64.77 < $66.50) selected the already-approved SELL BOTH at the 9/9 open. Execution is Will's hand at the broker; **the repo has no fill — quantity, price, time and account are all UNKNOWN.** No proceeds booked, no holdings removed, no re-approval requested.

⛔ **NOT re-litigated on the day's colour (Non-Negotiable #12).** For the record and *not* as a reason to revisit: **XLE closed $65.31 on 9/9, +0.83% — a GREEN day, and $0.54 above the $64.77 that selected the exit.** The dated test ran on the 9/8 close and is spent; a 9/9 rebound does not replace it and does not reopen it. The rule was ruled cold, before the print.

**Marks at 9/9 close (MOMENT properties, `RISK_RULES` #14 — recorded, not a proposal):** XLE Sep-30 **$65C bid `1.65` / ask `1.75` / mark `1.70`**, spread 5.88%, IV 25.51%, OI 7,380, vol 519, last trade 15:58 ET, no quote flag (`chain_fetch.py XLE 2026-09-30 --type call --no-cache --legs 65`, 21:07 ET). **If still held**, ×2 ⇒ ≈**$330 at bid / $340 at mark** vs **$456 basis** ($2.28 ×2) ⇒ **−$126 / −27.6%** at the bid. 21 DTE. **These are post-close quotes, not executable, and they do not establish that the position is still held.**

PROME L252 may consume this owner observation. **L253 remains open until an execution receipt** (actual quantity, price, time, account and remaining disposition). No sale proceeds or realized P/L estimated. Track as STAGED until execution is reported; “selected” does not mean “filled.” No add, roll, replacement threshold or new sizing.
