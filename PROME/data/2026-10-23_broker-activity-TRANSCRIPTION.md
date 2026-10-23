# Broker activity transcription — Fidelity IRA "Pending" view, 2026-10-23 (captured ~13:2x ET, Will's screenshot in the PROME window)

**Transcribed by:** PROME (prome-03 fresh context), 2026-10-23 13:2x ET from `date`. **Scope:** the Pending/activity list only — NOT a positions capture; FORGE positions are NOT reconciled from this file. Amounts are the broker's "Amount" column (fees included where the broker includes them); fill clocks not displayed. Derived P/L is TERRY's to compute, never PROME's.

| Date | Order | Status | Fill | Amount |
|---|---|---|---|---|
| 10/23 | Buy to Open 2 × QQQ Nov-20-2026 690P (net debit limit $4.67, Day) | FILLED | $13.39 | $2,679.33 |
| 10/23 | Sell to Open 2 × QQQ Nov-20-2026 670P (same spread order) | FILLED | $8.72 | $1,742.63 |
| 10/23 | Sell 1 share AAPL at market | FILLED | $346.635 | $346.64 |
| 10/23 | Sell 5 shares USO at market | FILLED | $168.595 | $842.96 |
| 10/23 | Sell to Close 1 × USO Oct-30-2026 165C (limit $7.15) | FILLED | $7.15 | $714.32 |
| 10/23 | Buy to Open 2 × QQQ Oct-26-2026 705P (limit $4.32) | FILLED | $4.30 | $861.33 |
| 10/23 | Buy to Open 4 × FLG Mar-19-2027 10P (limit $0.52) | **OPEN** (unfilled at capture) | — | — |
| 10/23 | Sell to Close 1 × USO Oct-23-2026 163C (limit $4.27) | FILLED | $4.36 | $435.34 |
| 10/23 | Sell to Close 1 × USO Oct-23-2026 163C (limit $4.50) | Verified Canceled | — | — |
| 10/22 | Sell to Close 1 × QQQ Oct-22-2026 717C at market | Verified Canceled | — | — |

**Net on the QQQ spread (derived, PROME arithmetic for the card only):** $2,679.33 − $1,742.63 = **$936.70** for 2 contracts (= $4.67 × 200 + fees). Card `IDEA-QQQ-PUTWALL-OCT22` fired by Will's hand at 2× the card's default size, BEFORE T1 (SPX cash close < 7,650) fired — S&P ~7,650 intraday at the fill, QQQ green (+0.12% at 13:17 ET preview). Day colour: green. Chase line ($5.00) respected.

**Book changes implied (positions capture owed to confirm; nothing inferred beyond the rows):** AAPL 4 → 3 · USO 35 → 30 · USO Oct-30 165C 2 → 1 · USO Oct-23 163C 1 → 0 · QQQ Oct-26 705P ×2 NEW · QQQ Nov-20 690/670P ×2 NEW · FLG Mar-2027 10P ×4 PENDING (open order).

**Consumers:** TERRY books (root rule #10; card FIRED, management lines live: harvest ≥ $10 mark · kill SPX close ≥ 7,750 ×2 · time stop 11/13) · ANVIL mirrors FORGE at the next positions capture (this file = post-snapshot events) · FLG desk informed of the open FLG put order (Will's own position idea on the Q3 miss; not a desk card).
