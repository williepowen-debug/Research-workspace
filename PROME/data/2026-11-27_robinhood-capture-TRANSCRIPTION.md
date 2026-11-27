# Robinhood Individual capture, 2026-11-27 after the half-day close

**Source:** one screenshot and one pasted "Recent" activity list, both posted by Will in PROME's chat 17:06 ET Fri 2026-11-27 (NYSE closed 13:00 ET; options closed 13:15 ET). Transcribed by PROME 2026-11-27 17:07 ET (`date`). Account number not shown. Quantity is shown on each card ("1 Buy", "2 Buys"); mark and cost are not shown, so cost and value in § ① are DERIVED from P/L ÷ P/L%. No clock on the capture; marks read as the 11/27 session end, not a verified settle. No stock list, no pending-orders panel and no cash line shown.

## ① Screenshot (account "Individual", 1W chart selected)

**Account value $2,305.45 · +$992.01 (+75.53%) Past week · Buying power $1,760.45.**
Start of the week DERIVED: $2,305.45 − $992.01 = $1,313.44; $992.01 / $1,313.44 = 75.53%, ties. ⚠️ The week's ledger (§ ②) carries a −$1,000.00 withdrawal (11/27) and a +$126.00 deposit (11/24); whether Robinhood's "Past week" figure is net of transfers is NOT SHOWN.

Options panel, in the order shown (the panel ends at KRE; the next panel is "Lists"):

| Option | Expiry | Side, qty as shown | P/L $ as shown | % shown | Cost DERIVED | Value DERIVED |
|---|---|---|---:|---:|---:|---:|
| CRWV $41 Put | 12/4 | 1 Buy | −$127.00 | −43.49% | $292.02 (ledger: $292.00) | $165.00 |
| USO $139 Call | 12/4 | 1 Buy | +$12.00 | +4.78% | $251.05 (ledger: $251.00) | $263.00 |
| HYG $76 Put | 1/15/2027 | 2 Buys | −$38.00 | −25.00% | $152.00 (ledger: $152.00) | $114.00 |
| KRE $25 Put | 1/15/2027 | 1 Buy | −$52.00 | −98.11% | $53.00 | $1.00 |

**Tie: DOES NOT TIE, short by $2.00.** Values $165 + $263 + $114 + $1 = $543.00; $543.00 + buying power $1,760.45 = $2,303.45 against the account value $2,305.45. The $2.00 is unexplained: cash is taken as buying power (the card shows no cash line), the P/L basis is not labelled, the −$1,000.00 withdrawal is 5 hours old and its settlement state is not shown, and no stock list is shown. Costs on three of the four lines reproduce the ledger's fills to within the rounding of the shown %.

Not on the options panel, against the mirror's 11/10 Robinhood section (`git show HEAD:FORGE/STATUS.md`): QQQ $675P Nov-10, QQQ $669P Nov-10, KRE $71.5P Nov-13 ×2, WAL $70P Nov-20, UNG $10.5C Dec-24. None of the five appears in § ② either, as far as that list reaches.

## ② "Recent" activity list, as pasted (newest first; relative times as shown at 17:06 ET 11/27; the list is cut inside 11/20)

| # | When shown | Entry | Amount | Detail |
|---|---|---|---:|---|
| 1 | 2h | Buy QQQ $646 Put 11/30 | Canceled | |
| 2 | 4h | Buy USO $139 Call 12/4 | $251.00 | 1 contract at $2.51 |
| 3 | 5h | Withdrawal from individual to an external bank account (name not recorded: the repo is public) | −$1,000.00 | |
| 4 | Nov 25 | Buy CRWV $41 Put 12/4 | $292.00 | 1 contract at $2.92 |
| 5 | Nov 25 | Buy QQQ $627 Put 11/27 | $432.00 | 1 contract at $4.32 |
| 6 | Nov 25 | Buy QQQ $625 Put 11/27 | $366.00 | 1 contract at $3.66 |
| 7 | Nov 25 | Sell QQQ $640 Call 11/25 | $2.00 | 1 contract at $0.02 |
| 8 | Nov 25 | Buy HYG $76 Put 1/15/2027 | $152.00 | 2 contracts at $0.76 |
| 9 | Nov 25 | Buy QQQ $610 Put 11/25 | $411.00 | 1 contract at $4.11 |
| 10 | Nov 25 | Sell QQQ $635 Put 11/25 | $2,240.00 | 1 contract at $22.40 |
| 11 | Nov 25 | QQQ $610 Put Expiration | $0.00 | |
| 12 | Nov 24 | Buy QQQ $635 Put 11/25 | $501.00 | 1 contract at $5.01 |
| 13 | Nov 24 | Buy QQQ $640 Call 11/25 | $384.00 | 1 contract at $3.84 |
| 14 | Nov 24 | Sell QQQ $634 Put 11/24 | $35.00 | 1 contract at $0.35 |
| 15 | Nov 24 | Sell QQQ $636 Call 11/24 | $315.00 | 1 contract at $3.15 |
| 16 | Nov 24 | Buy QQQ $636 Call 11/24 | $188.00 | 1 contract at $1.88 |
| 17 | Nov 24 | Buy QQQ $634 Put 11/24 | $299.00 | 1 contract at $2.99 |
| 18 | Nov 24 | Sell NVDA $160 Put 11/25 | $900.00 | 1 contract at $9.00 |
| 19 | Nov 24 | Sell QQQ $650 Put 11/24 | $1,597.00 | 1 contract at $15.97 |
| 20 | Nov 24 | Deposit to individual from an external bank account (name not recorded: the repo is public) | +$126.00 | |
| 21 | Nov 23 | Sell QQQ $649 Put 11/23 | $12.00 | 1 contract at $0.12 |
| 22 | Nov 23 | Buy QQQ $650 Put 11/24 | $572.00 | 1 contract at $5.72 |
| 23 | Nov 23 | Buy NVDA $160 Put 11/25 | $385.00 | 1 contract at $3.85 |
| 24 | Nov 23 | Buy QQQ $649 Put 11/23 | $419.00 | 1 contract at $4.19 |
| 25 | Nov 20 | Sell KRE $69 Put 11/20 | $35.00 | 1 contract at $0.35 |
| 26 | Nov 20 | Sell KRE $69 Put 11/20 | Canceled | |
| 27 | Nov 20 | Sell QQQ $620 Put 11/20 | $1,024.00 | 1 contract at $10.24 |
| 28 | Nov 20 | Sell QQQ $627 Call 11/20 | $17.00 | 1 contract at $0.17 |
| 29 | Nov 20 | Sell QQQ $627 Call 11/20 | Canceled | |
| 30 | Nov 20 | Buy QQQ $620 Put 11/20 | $279.00 | 1 contract at $2.79 |
| 31 | Nov 20 | Buy QQQ $627 Call 11/20 | $277.00 | 1 contract at $2.77 |
| 32 | Nov 20 | Sell QQQ $635 Put 11/20 | $1,106.00 | detail line CUT OFF (the paste ends here) |

**Reading limits (PROME's, for the clerk to check, not to copy):**
- The dates "Nov 23" and "Nov 25" are as shown. 11/23 was a Monday and 11/26 was Thanksgiving; row 21 to 24 dates are the list's own.
- Rows 5 and 6 (QQQ $627P and $625P, both dated 11/27, bought 11/25) have NO sell row and NO expiration row in the list, and neither is on the options panel. Disposition NOT SHOWN; an expiration entry may not have posted by 17:06 ET. Nothing is inferred.
- Row 9 buys a QQQ $610 Put 11/25 on Nov 25 and row 11 is its expiration at $0.00 the same day, as the list shows it.
- Row 32's contract count and price are cut off; the buy of that QQQ $635 Put 11/20 and the buy of the KRE $69 Put 11/20 (row 25) are before the list's reach.
- Fees are not shown on any row; amounts are as displayed.
- The list is Robinhood only. No Fidelity view was supplied on 11/27; the Fidelity section of the mirror stays at its 11/18 intraday vintage.
