# Broker capture — TRANSCRIPTION · 2026-09-30 (Wed) POST-CLOSE · Fidelity Traditional IRA *****1326
**Transcribed by PROME (`prome-94`) 2026-09-30 18:3x ET from two screenshots Will posted 18:31 ET (① positions view · ② Activity & Orders, Sep-30-2026 rows). Every cell as shown; nothing derived unless labelled DERIVED. Verified to the cent (§ ④). Comparison base for deltas = `git show HEAD:FORGE/STATUS.md` (the 9/29 13:4x intraday reconcile), never a view.**

## ① Positions view (Fidelity; the header row was not in the crop — account INFERRED = the same Traditional IRA *****1326 as the Activity view, by position-set match)
**As-of:** the 9/30 SESSION, captured POST-CLOSE (stock "last" cells equal the 9/30 closes to the cent — USO 145.66 · TBT 42.49 · AAPL 333.02 · GLD 380.84 · VLO 387.61 · APD 278.23 per `fetch.py price` 17:3x ET; "Today's gain/loss" populated for 9/30). Option marks are Fidelity's post-close marks — ⚠️ the three KRE Dec puts show $0.01 (−98% on the day) against KRE −0.56%: a bid-based after-hours mark, NOT a valuation; the 9/29 intraday marks were ~$0.46–0.53.

Columns: Symbol · Last · Today $ chg · Today's gain $ · Today's gain % · Total gain $ · Total gain % · Current value · % of account · Qty · Avg cost/share · Cost basis total

| Symbol | Last | Today $ | Today gain $ | Today gain % | Total gain $ | Total gain % | Value | % acct | Qty | Avg cost | Basis |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Cash (held in money market) | — | — | — | — | — | — | $18,102.04 | 49.75% | — | — | — |
| QQQ 740 Put Oct-01-2026 [NE] | $2.97 | −$2.33 | +$939.03 | +54.15% | +$939.03 | +54.15% | $2,673.00 | 7.35% | 9 | $1.93 | $1,733.97 |
| QQQ 735 Put Oct-05-2026 [NE] | $3.52 | −$1.41 | +$391.68 | +28.62% | +$391.68 | +28.62% | $1,760.00 | 4.84% | 5 | $2.74 | $1,368.32 |
| TLT 82 Put Oct-16-2026 | $4.60 | +$0.45 | +$45.00 | +10.84% | +$292.33 | +174.34% | $460.00 | 1.26% | 1 | $1.68 | $167.67 |
| USO (stock) | $145.66 | +$2.31 | +$85.47 | +1.61% | +$865.15 | +19.12% | $5,389.42 | 14.81% | 37 | $122.28 | $4,524.27 |
| TBT (stock) | $42.49 | +$0.46 | +$4.60 | +1.09% | +$78.44 | +22.64% | $424.90 | 1.17% | 10 | $34.65 | $346.46 |
| AAPL (stock) | $333.02 | +$3.62 | +$36.20 | +1.09% | +$3,093.75 | +1,308.41% | $3,330.20 | 9.15% | 10 | $23.65 | $236.45 |
| VLO (stock) | $387.61 | −$0.11 | −$0.11 | −0.03% | −$24.39 | −5.92% | $387.61 | 1.07% | 1 | $412.00 | $412.00 |
| APD (stock) [D badge] | $278.23 | −$0.96 | −$1.92 | −0.35% | −$33.11 | −5.62% | $556.46 | 1.53% | 2 | $294.79 | $589.57 |
| GLD (stock) | $380.84 | −$2.05 | −$34.85 | −0.54% | +$103.78 | +1.62% | $6,474.28 | 17.79% | 17 | $374.74 | $6,370.50 |
| USO 150 Call Oct-09-2026 | $2.84 | +$0.26 | −$31.33 | −5.23% | −$31.33 | −5.23% | $568.00 | 1.56% | 2 | $3.00 | $599.33 |
| APO 95 Put Dec-18-2026 | $1.20 | −$0.15 | −$15.00 | −11.12% | −$1,064.67 | −89.88% | $120.00 | 0.33% | 1 | $11.85 | $1,184.67 |
| HBAN 16 Put Oct-16-2026 | $0.70 | −$0.35 | −$70.00 | −33.34% | −$51.34 | −26.84% | $140.00 | 0.38% | 2 | $0.96 | $191.34 |
| KRE 60 Put Dec-18-2026 | $0.01 | −$0.52 | −$156.00 | −98.12% | −$875.02 | −99.66% | $3.00 | 0.01% | 3 [M] | $2.93 | $878.02 |
| KRE 60 Put Dec-18-2026 | $0.01 | −$0.52 | −$104.00 | −98.12% | −$511.34 | −99.62% | $2.00 | 0.01% | 2 | $2.57 | $513.34 |
| KRE 65 Put Dec-31-2026 | $0.01 | −$1.53 | −$335.33 | −99.41% | −$335.33 | −99.41% | $2.00 | 0.01% | 2 | $1.69 | $337.33 |
| Pending activity | — | — | — | — | — | — | −$4,007.98 | — | — | — | — |
| **Account total** | — | — | **+$753.44** | **+2.11%** | **+$2,837.63** | **+14.59%** | **$36,384.93** | — | — | — | — |

[NE] = Fidelity "new" badge on the two QQQ lines (as shown). ABSENT from this view (present on the 9/29 mirror): QQQ 730P Sep-30 · USO 159C Sep-30 · TLT 77P Sep-30 · KRE 60P Sep-30 — see ② and § ③.

## ② Activity & Orders — Sep-30-2026, Traditional IRA *****1326 (14 rows, top→bottom as shown; fill TIMES not shown — the D-61 class)
| # | Action | Contract | Order type | Status | Amount |
|---|---|---|---|---|---|
| 1 | Sell to Close | 2 KRE Sep 30 2026 60 Puts | Net Debit Limit $1.67 (Day) | Filled at $0.01 | $1.87 |
| 2 | Buy to Open | 2 KRE Dec 31 2026 65 Puts | Net Debit Limit $1.67 (Day) | Filled at $1.68 | $337.33 |
| 3 | Sell to Close | 2 KRE Sep 30 2026 60 Puts | Net Debit Limit $1.63 (Day) | Verified Canceled | — |
| 4 | Buy to Open | 2 KRE Dec 31 2026 65 Puts | Net Debit Limit $1.63 (Day) | Verified Canceled | — |
| 5 | Sell to Close | 2 USO Sep 30 2026 159 Calls | Net Debit Limit $2.98 (Day) | Filled at $0.01 | $1.87 |
| 6 | Buy to Open | 2 USO Oct 9 2026 150 Calls | Net Debit Limit $2.98 (Day) | Filled at $2.99 | $599.33 |
| 7 | Sell to Close | 2 KRE Sep 30 2026 60 Puts | Net Debit Limit $1.55 (Day) | Verified Canceled | — |
| 8 | Buy to Open | 2 KRE Dec 31 2026 65 Puts | Net Debit Limit $1.55 (Day) | Verified Canceled | — |
| 9 | Sell to Close | 10 TLT Sep 30 2026 77 Puts | Limit $0.01 (Day) | Filled at $0.01 | $9.37 |
| 10 | Sell to Close | 9 QQQ Sep 30 2026 730 Puts | Net Debit Limit $1.91 (Day) | Filled at $0.01 | $8.43 |
| 11 | Buy to Open | 9 QQQ Oct 1 2026 740 Puts | Net Debit Limit $1.91 (Day) | Filled at $1.92 | $1,733.97 |
| 12 | Sell to Close | 5 TLT Sep 30 2026 77 Puts | Limit $0.02 (Day) | Filled at $0.02 | $9.43 |
| 13 | Buy to Open | 5 QQQ Oct 5 2026 735 Puts | Limit $2.73 (Day) | Filled at $2.73 | $1,368.32 |
| 14 | Buy to Open | 5 QQQ Oct 5 2026 735 Puts | Limit $2.52 (Day) | Verified Canceled | — |

Rows 1+2, 5+6, 10+11 are the legs of three net-debit ROLL orders (the canceled 3+4 / 7+8 pairs are earlier attempts at lower net debits). Rows 9, 12, 13 (and the canceled 14) are single-leg limit orders. **Will's word 18:27 ET: *"I rolled the puts."***

## ③ Activity ledger — as ② (the 9/30 rows ARE the ledger for this pass; no running-balance column in this view)
Signed cash effect of the filled rows (DERIVED from the Amount column; sells +, buys −): +1.87 −337.33 +1.87 −599.33 +9.37 +8.43 −1,733.97 +9.43 −1,368.32 = **−$4,007.98** = the positions view's Pending activity, to the cent ✓.

## ④ Verification to the cent (PROME arithmetic on the shown cells)
- Σ position values 22,290.87 + cash 18,102.04 + pending −4,007.98 = **36,384.93** = Account total ✓.
- Every row: value = last × qty (× 100 for options) ✓ (15/15). Every total-gain cell = value − basis ✓ (15/15). Σ Today's gain $ = +753.44 = the account's today figure ✓.
- New-line bases = fill × qty × 100 + fees: QQQ 740P 1,728.00 + 5.97 = 1,733.97 ✓ · QQQ 735P 1,365.00 + 3.32 = 1,368.32 ✓ · USO 150C 598.00 + 1.33 = 599.33 ✓ · KRE 65P 336.00 + 1.33 = 337.33 ✓ (fees DERIVED as the difference).
- Cash $18,102.04 = the 9/29 mirror's cash (unchanged; today's net sits in Pending). D-63's +$2.27 bridge is untouched by this capture.

## ⑤ Deltas vs the mirror (`git show HEAD:FORGE/STATUS.md`, 9/29 13:4x intraday) — the ANVIL contract
| Line | Delta | Evidence |
|---|---|---|
| QQQ $730P Sep-30 ×9 | **GONE — SOLD TO CLOSE @ $0.01, net $8.43 (ledger row 10); NOT expired.** Realized vs the mirror's broker basis $2,237.97 = DERIVED −$2,229.54 | rolled into the 740P (row 11) |
| USO $159C Sep-30 ×2 | **GONE — SOLD TO CLOSE @ $0.01, net $1.87 (row 5); NOT expired.** Realized vs basis $921.33 = DERIVED −$919.46 | rolled into the Oct-9 150C (row 6) |
| TLT $77P Sep-30 ×15 | **GONE — SOLD TO CLOSE: 10 @ $0.01 net $9.37 (row 9) + 5 @ $0.02 net $9.43 (row 12) = $18.80; NOT held to expiry** — a THIRD hand-deviation from WQ-168 ④ / WQ-217 HOLD (9/10 · 9/28 · 9/30); recorded, not adjudicated. Realized vs the mirror's basis $173.44 = DERIVED −$154.64 | no replacement TLT line |
| KRE $60P Sep-30 ×2 | **GONE — SOLD TO CLOSE @ $0.01, net $1.87 (row 1); NOT lapsed** (WQ-168 ⑥ ruled LAPSE; sold instead — recorded). Realized = ANVIL from the mirror's basis | rolled into the Dec-31 65P (row 2) |
| QQQ $740P Oct-01-2026 ×9 | **NEW** — bought @ $1.92, basis $1,733.97 (row 11); mark $2.97 / $2,673.00 (+$939.03). ⚠️ **EXPIRES THU 10/01; ITM at the 9/30 close (QQQ 739.77 < 740)** — D-60's ITM leg, one session out; no card | WQ-347 (registered tonight) |
| QQQ $735P Oct-05-2026 ×5 | **NEW** — bought @ $2.73, basis $1,368.32 (row 13); mark $3.52 / $1,760.00 (+$391.68). Size ADDED vs the rolled nine (14 QQQ puts across two lines); no card | WQ-347 |
| USO $150C Oct-09-2026 ×2 | **NEW** — bought @ $2.99, basis $599.33 (row 6); mark $2.84 / $568.00 (−$31.33). New oil-call exposure on the book Will ruled "one oil bet" (WQ-297 A); no card | record |
| KRE $65P Dec-31-2026 ×2 | **NEW** — bought @ $1.68, basis $337.33 (row 2); mark $0.01 / $2.00 (⚠️ after-hours mark). Will's own KRE add (TERRY's conditional card 4ad672c43 read NOT constructible today); no card | record |
| AAPL 10 · GLD 17 · USO 37 · VLO 1 · APD 2 · TBT 10 · TLT $82P ×1 · KRE $60P Dec-18 3(M)+2 · APO $95P ×1 · HBAN $16P ×2 | **MARK ONLY** — quantities and bases unchanged; marks = 9/30 close (stocks) / Fidelity post-close (options) | — |
| Robinhood | **NOT CAPTURED tonight** — the 9/29 card stands (WAL $70P · KRE $25P · $295.15) | — |
| Cash | unchanged $18,102.04; **Pending −$4,007.98** = today's net; account total $36,384.93 (was $36,822.87 [9/29 13:4x intraday]) | — |
