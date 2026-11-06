# C9 answer: IDEA-ORCL-PUTSPREAD-OCT23 after the Microsoft report

**Written:** 2026-11-06 16:08 EST, TERRY. **Commission:** `inbox/2026-11-06_from-PROME_C9-ORCL-card-after-Microsoft.md`. **Card changed:** no. **No order.**
**Reads:** ORCL $116.05 +0.77%, green, `fetch.py` 16:06 ET, final daily bar not read. Chain about 16:07 ET, after the close, vendor SCREENING marks (finding 5b), not broker quotes. CDS: `AGENTS/LIQUID/research/2026-11-06_oracle-cds-loop/REPORT.md` § 1.

## 1. Does the $120 leg still serve the card? Yes, as a price guard. It never measured the gap.
$120 keeps the entry near the $4.40 limit on these strikes. The debit limit does the same job, so at $116.05 lowering $120 would change nothing:

| Line | Card | Now | State |
|---|---|---:|---|
| T1 CDS 5Y, DTCC disseminated | ≥ 350 | 305 [11/5]. 11/6 partial, to about 15:50 ET: conv 306-314, best print about 318 on the disseminated basis. Full file about 20:15 ET | NOT FIRED, 32 to 45 bp short |
| T2 ORCL | ≥ $120.00 at T1 | $116.05 | fails if read now |
| Debit 115/100P | ≤ $4.40, no chase > $5.00 | $5.95 (10.65 − 4.70) | over both |
| FQ2 date, Oracle IR verified (WQ-518 A) | written on the card before entry | not verified; web search 11/6 finds no announcement, calendars project 12/10, unconfirmed | blocks entry |
| Void: CDS ≤ 280, close ≥ $145 | | no | NOT VOIDED |

Four independent blocks. Removing T2 alone fills nothing.

**The commission's framing needs one correction.** "Lapses while its thesis strengthens" holds for Oracle's financing story, not for this card. The card's thesis is a gap: credit wide, equity not following. Since the card: ORCL $126.16 [10/23 close] to $116.05, −8.0%. CDS 314 [10/22] to 305 [11/5] and about 306-318 [11/6 partial]. Credit is flat and the equity followed. The gap closed from the equity side. A lapse on 11/20 is the card working, on current reads.

**One case where $120 costs something:** CDS ≥ 350 with ORCL under $120. That would be credit leading again, and T2 would block it. The fix there is a new structure and Will's word, not a lower line on these strikes.

**Correction to the card's frame, not written on the card:** the card says "36 bp away" from 314 [10/22]. LIQUID's file shows 342.5 disseminated on 10/20, 7.5 bp under 350, three sessions before the card was written. So 350 is less remote than the card read, and the card's 11/5 line "DTCC 300 [11/3] is the newest read found" is also stale: 292.5 [11/4], 305 [11/5]. No fire was missed; the card dates from 10/23.

## 2. Would TERRY bring a NOT-FIRED idea to Will? No.
Checked so the "no" can be graded. Dec-18, ×1, outer debit, screening marks, not proposed:

| Structure | Debit | Max loss | Max gain | Breakeven | Payoff |
|---|---:|---:|---:|---:|---:|
| 115/100P, the card | $5.95 | $596.30, over the $500 default | $903.70 | $109.05 | 1.52 : 1 |
| 110/95P | $4.95 | $496.30 | $1,003.70 | $105.05, −9.5% | 2.02 : 1 |
| 105/90P, the card's distance from spot | $3.92 | $393.30 | $1,106.70 | $101.08, −12.9% | 2.81 : 1 |

Why no:
1. **Evidence.** Bloomberg's body is unread, the Microsoft-Oracle contract size is unknown, and nothing shows financing refused (LIQUID 11/6).
2. **The market did not confirm.** CDS about +6 to +8 bp by the 11/6 close against a −6.2% five-minute stock drop (LIQUID); ORCL closed +0.77%. LIQUID's read is two stories on one tape, not one proven loop, and it says that is absence on a partial view.
3. **Entry quality.** ORCL is at the low of its 30-day range, $115.16-144.54, −12.16% in 30 days. The card itself rejected a price-break trigger because it fires after the equity has moved. A new put spread here is that trade.
4. **The clock.** The likely FQ2 print falls after the card's 12/4 time stop. Holding only to 12/4 needs a fast 13% move. Holding past it is a bet on an unverified print date, and WQ-518 A bars estimated-date entry on the card.
5. **Book.** The HYG hedge is unfilled and covers overlapping AI-financing and credit risk. A second downside line before the first exists adds a view, not protection. Mirror check only: no ORCL line in `FORGE/STATUS.md`.

**What would reopen it, evidence and not levels:** the contract size and the Bloomberg body read; a filing or primary report of financing refused or repriced; an Oracle-verified FQ2 date. This sets no gate. Any idea would be a new NOT-FIRED card for Will under root rule #5.
