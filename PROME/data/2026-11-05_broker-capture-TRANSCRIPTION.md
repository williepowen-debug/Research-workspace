# Broker capture — 2026-11-05 Thu, INTRADAY ~10:0x ET — Fidelity Traditional IRA •1326 (last four only; the repo is public, WQ-455)

**Transcribed by:** PROME (prome-98, desktop) from two screenshots Will posted in the PROME window 10:01 ET Thu 2026-11-05 (session images 1.png and 2.png). The account number is blacked out on the capture; •1326 is carried from the prior record, on the basis that the account name, the positions and the running cash all continue from it. **As-of:** the November 5 session, INTRADAY. "Today's gain/loss" is populated; the quote clock is not displayed; not a close, not settles.

**Ties to the cent (PROME, python):** Σ position values $12,669.59 + cash $28,218.18 + pending $3,953.67 = $44,841.44 ✓ · every row value = last × qty × (100 for options) ✓ · every row Total G/L $ = value − basis ✓ · Σ Total G/L = −$6,422.38 ✓ · Σ Today's G/L = −$957.21 ✓ · Σ cost basis $19,091.97 · pending = the three November 5 fills $2,882.28 + $366.67 + $704.72 ✓

## ① Positions view (19 rows + cash)

| # | Symbol | Last | Last chg | Today $ | Today % | Total G/L $ | Total G/L % | Current value | % acct | Qty | Avg cost | Cost basis | Badge / note |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| — | Cash (held in money market) | | | | | | | $28,218.18 | 62.93% | | | | |
| 1 | GLD | $376.53 | +$4.04 | +$72.72 | +1.08% | +$46.87 | +0.69% | $6,777.54 | 15.11% | 18 | $373.93 | $6,730.67 | 52wk $354.67–$509.70 |
| 2 | USO | $147.325 | +$1.915 | +$57.45 | +1.31% | +$747.74 | +20.36% | $4,419.75 | 9.86% | 30 | $122.40 | $3,672.01 | 52wk $65.99–$171.82 |
| 3 | USO 170 Call Nov-20-2026 | $1.46 | +$0.14 | +$14.00 | +10.60% | −$481.66 | −76.74% | $146.00 | 0.33% | 1 | $6.28 | $627.66 | |
| 4 | VLO | $368.15 | +$2.81 | +$5.62 | +0.76% | −$148.43 | −16.78% | $736.30 | 1.64% | 2 | $442.37 | $884.73 | 52wk $159.90–$461.52 |
| 5 | VLY 12 Put Dec-18-2026 | $0.10 | $0.00 | $0.00 | 0.00% | −$5.66 | −36.15% | $10.00 | 0.02% | 1 | $0.16 | $15.66 | |
| 6 | OZK 40 Put Nov-20-2026 | $0.05 | $0.00 | $0.00 | 0.00% | −$302.65 | −93.81% | $20.00 | 0.04% | 4 | $0.81 | $322.65 | |
| 7 | FLG 10 Put Mar-19-2027 | $0.30 | −$0.16 | −$16.00 | −34.79% | −$40.66 | −57.55% | $30.00 | 0.07% | 1 | $0.71 | $70.66 | |
| 8 | KRE 60 Put Dec-18-2026 (lot 1) | $0.08 | −$0.08 | −$16.00 | −50.00% | −$497.34 | −96.89% | $16.00 | 0.04% | 2 | $2.57 | $513.34 | |
| 9 | KRE 66 Put Nov-20-2026 | $0.07 | −$0.06 | −$18.00 | −46.16% | −$112.99 | −84.33% | $21.00 | 0.05% | 3 | $0.45 | $133.99 | |
| 10 | USO 172 Call Nov-11-2026 | $0.36 | −$0.20 | −$20.00 | −35.72% | −$496.66 | −93.25% | $36.00 | 0.08% | 1 | $5.33 | $532.66 | NE badge |
| 11 | KRE 60 Put Dec-18-2026 (lot 2) | $0.08 | −$0.08 | −$24.00 | −50.00% | −$854.02 | −97.27% | $24.00 | 0.05% | 3 | $2.93 | $878.02 | M (margin) |
| 12 | KRE 70 Put Nov-27-2026 | $0.24 | −$0.25 | −$50.00 | −51.03% | −$233.33 | −82.94% | $48.00 | 0.11% | 2 | $1.41 | $281.33 | |
| 13 | ZION 62.5 Put Nov-20-2026 | $0.20 | −$0.25 | −$50.00 | −55.56% | −$395.33 | −90.82% | $40.00 | 0.09% | 2 | $2.18 | $435.33 | |
| 14 | KRE 65 Put Dec-31-2026 | $0.26 | −$0.26 | −$52.00 | −50.00% | −$285.33 | −84.59% | $52.00 | 0.12% | 2 | $1.69 | $337.33 | |
| 15 | APO 95 Put Dec-18-2026 | $0.15 | −$0.79 | −$79.00 | −84.05% | −$1,169.67 | −98.74% | $15.00 | 0.03% | 1 | $11.85 | $1,184.67 | E badge |
| 16 | KRE 67 Put Nov-27-2026 | $0.12 | −$0.27 | −$108.00 | −69.24% | −$462.65 | −90.61% | $48.00 | 0.11% | 4 | $1.28 | $510.65 | |
| 17 | WAL 70 Put Dec-18-2026 | $0.45 | −$0.62 | −$124.00 | −57.95% | −$461.33 | −83.68% | $90.00 | 0.20% | 2 | $2.76 | $551.33 | |
| 18 | WAL 65 Put Dec-18-2026 | $0.15 | −$0.35 | −$140.00 | −70.00% | −$622.65 | −91.22% | $60.00 | 0.13% | 4 | $1.71 | $682.65 | |
| 19 | KRE 68 Put Nov-27-2026 | $0.08 | −$0.41 | −$410.00 | −83.68% | −$646.63 | −89.00% | $80.00 | 0.18% | 10 | $0.73 | $726.63 | |
| — | Pending activity | | | | | | | $3,953.67 | | | | | |
| — | **Account total** | | | | | | | **$44,841.44** | | | | | Today −$957.21 (−2.09%) · Total −$6,422.38 (−33.64%) |

## ② Orders panel, November 5

| Date | Order | Status | Amount |
|---|---|---|---|
| Nov-05-2026 | Sell to Close 1 contract QQQ Nov 20 2026 690 Put, Limit $28.83 (Day) | Filled at $28.83 | $2,882.28 |
| Nov-05-2026 | Sell 1 share of VLO at Market (Day) | Filled at $366.665 | $366.67 |
| Nov-05-2026 | Sell 2 shares of AAPL at Market (Day) | Filled at $352.37 | $704.72 |

## ③ Activity, Past 30 days, as visible (newest first; the view ends at the October 30 USO row)

| Date | Description | Amount | Cash balance |
|---|---|---|---|
| Nov-05-2026 | YOU SOLD CLOSING TRANSACTION PUT QQQ Nov 20 26 $690 (Margin) | +$2,882.28 | Processing |
| Nov-05-2026 | YOU SOLD VLO (Cash) | +$366.67 | Processing |
| Nov-05-2026 | YOU SOLD AAPL (Cash) | +$704.72 | Processing |
| Nov-05-2026 | EXPIRED PUT QQQ Nov 04 26 $680 as of 2026-11-04 (Cash) | -- | Processing |
| Nov-04-2026 | YOU SOLD CLOSING TRANSACTION CALL AAPL Nov 04 26 $345 (Cash) | +$776.32 | $28,218.18 |
| Nov-03-2026 | EXPIRED CALL GLD Nov 02 26 $375 as of 2026-11-02 (Cash) | -- | $27,441.86 |
| Nov-03-2026 | YOU BOUGHT OPENING TRANSACTION PUT QQQ Nov 04 26 $680 (Cash) | −$464.66 | $27,441.86 |
| Nov-02-2026 | YOU SOLD CLOSING TRANSACTION PUT QQQ Nov 05 26 $685 (Cash) | +$1,202.31 | $27,906.52 |
| Nov-02-2026 | YOU BOUGHT OPENING TRANSACTION PUT QQQ Nov 04 26 $680 (Cash) | −$649.66 | $26,704.21 |
| Nov-02-2026 | YOU SOLD CLOSING TRANSACTION PUT QQQ Nov 04 26 $680 (Cash) | +$777.32 | $27,353.87 |
| Nov-02-2026 | YOU BOUGHT OPENING TRANSACTION CALL AAPL Nov 04 26 $345 (Cash) | −$440.66 | $26,576.55 |
| Nov-02-2026 | YOU SOLD CLOSING TRANSACTION PUT QQQ Nov 02 26 $680 (Cash) | +$52.34 | $27,017.21 |
| Nov-02-2026 | YOU SOLD CLOSING TRANSACTION PUT QQQ Nov 02 26 $715 (Cash) | +$2,069.29 | $26,964.87 |
| Nov-02-2026 | YOU BOUGHT OPENING TRANSACTION PUT QQQ Nov 06 26 $680 (Cash) | −$1,141.33 | $24,895.58 |
| Nov-02-2026 | YOU SOLD CLOSING TRANSACTION PUT QQQ Nov 06 26 $680 (Cash) | +$882.32 | $26,036.91 |
| Nov-02-2026 | YOU SOLD CLOSING TRANSACTION PUT QQQ Nov 06 26 $680 (Cash) | +$1,105.31 | $25,154.59 |
| Nov-02-2026 | YOU SOLD GLD (Cash) | +$1,814.51 | $24,049.28 |
| Nov-02-2026 | YOU SOLD GLD (Cash) | +$1,818.46 | $22,234.77 |
| Nov-02-2026 | YOU SOLD AAPL (Cash) | +$337.22 | $20,416.31 |
| Nov-02-2026 | YOU SOLD APD (Cash) | +$637.04 | $20,079.09 |
| Oct-30-2026 | YOU BOUGHT OPENING TRANSACTION CALL USO Nov 11 26 $172 (Cash) | −$532.66 | $19,397.62 |

**Running-balance check (PROME):** every step from $20,079.09 up to $28,218.18 ties row by row. ❌ **One gap, $44.43:** $19,397.62 + $637.04 = $20,034.66 against the displayed $20,079.09. Figures re-read at 2× zoom. No row in view explains it. Nothing is inferred about its cause.

## ④ Not in this capture

- Activity before the October 30 USO row, including whatever closed the second QQQ Nov-20 690P and opened the QQQ Nov-02 680P and QQQ Nov-05 685P lines and the Nov-06 680P contracts sold November 2.
- Share counts on the stock sales in the Activity rows. GLD 28→18 and AAPL 3→2→0 are implied by the positions, not displayed per row.
- Robinhood.
