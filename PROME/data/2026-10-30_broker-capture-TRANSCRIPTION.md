# Broker capture — 2026-10-30 Fri, INTRADAY ~13:2x ET — Fidelity Traditional IRA •1326 (last four only; the repo is public, WQ-455)

**Transcribed by:** PROME (prome-c5, desktop) from two screenshots Will posted in the PROME window 13:21 ET Fri 2026-10-30 (images 3 and 4). **As-of:** the October30 session, INTRADAY — "Today's gain/loss" is populated and the capture time is ~13:2x ET, so every "Last price" is an intraday Fidelity last, NOT a close, NOT a settle, NOT an executable quote. Quote clock not displayed. **Account total $46,241.82** (Today +$789.92 / +1.74%; Total −$278.47 / −1.02%). **Cash (held in money market) $13,386.72 = 28.95%** (unchanged from the 10/29 capture — today's sales are still "Processing"). **Pending activity $5,927.58.**

**Ties to the cent (PROME, python):** Σ position values $26,927.52 + cash $13,386.72 + pending $5,927.58 = $46,241.82 ✓ · every row value = last × qty × (100 for options) ✓ · every row Total G/L $ = value − basis ✓ · Σ Today's G/L = +$789.92 ✓ · pending = today's six fills net $4,965.58 + the prior pending (margin credit balance) $962.00 ✓.

## ① Positions view (23 rows + cash)

| # | Symbol | Last | Last chg | Today $ | Today % | Total G/L $ | Total G/L % | Current value | % acct | Qty | Avg cost | Cost basis | Badge / note |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| — | Cash (money market) | | | | | | | $13,386.72 | 28.95% | | | | |
| 1 | QQQ 715 Put Nov-02-2026 | $25.41 | +$14.53 | +$1,453.00 | +133.54% | +$2,056.34 | +424.28% | $2,541.00 | 5.50% | 1 | $4.85 | $484.66 | NE |
| 2 | USO (United States Oil Fund LP) | $171.57 | +$3.38 | +$101.40 | +2.00% | +$1,475.09 | +40.17% | $5,147.10 | 11.13% | 30 | $122.40 | $3,672.01 | 52wk $65.99–$171.82 |
| 3 | AAPL | $346.95 | −$1.96 | −$5.88 | −0.57% | +$969.92 | +1,367.43% | $1,040.85 | 2.25% | 3 | $23.64 | $70.93 | E; 52wk $243.42–$351.73 |
| 4 | QQQ 690 Put Nov-20-2026 | $17.70 | +$7.85 | +$1,570.00 | +79.69% | +$860.67 | +32.12% | $3,540.00 | 7.66% | 2 | $13.40 | $2,679.33 | M (margin) |
| 5 | USO 170 Call Nov-20-2026 | $9.50 | +$1.70 | +$170.00 | +21.79% | +$322.34 | +51.35% | $950.00 | 2.05% | 1 | $6.28 | $627.66 | |
| 6 | APD | $314.21 | +$2.46 | +$4.92 | +0.78% | +$38.85 | +6.58% | $628.42 | 1.36% | 2 | $294.79 | $589.57 | 52wk $229.11–$315.73 |
| 7 | VLY 12 Put Dec-18-2026 | $0.05 | −$0.05 | −$5.00 | −50.00% | −$10.66 | −68.08% | $5.00 | 0.01% | 1 | $0.16 | $15.66 | |
| 8 | FLG 10 Put Mar-19-2027 | $0.55 | −$0.05 | −$5.00 | −8.34% | −$15.66 | −22.17% | $55.00 | 0.12% | 1 | $0.71 | $70.66 | |
| 9 | KRE 66 Put Nov-20-2026 | $0.26 | +$0.06 | +$18.00 | +30.00% | −$55.99 | −41.79% | $78.00 | 0.17% | 3 | $0.45 | $133.99 | |
| 10 | KRE 70 Put Nov-27-2026 | $1.02 | +$0.22 | +$44.00 | +27.50% | −$77.33 | −27.49% | $204.00 | 0.44% | 2 | $1.41 | $281.33 | |
| 11 | VLO | $394.065 | +$9.495 | +$28.48 | +2.46% | −$114.54 | −8.84% | $1,182.19 | 2.56% | 3 | $432.24 | $1,296.73 | 52wk $159.90–$461.52 |
| 12 | KRE 65 Put Dec-31-2026 | $0.75 | −$0.10 | −$20.00 | −11.77% | −$187.33 | −55.54% | $150.00 | 0.32% | 2 | $1.69 | $337.33 | |
| 13 | KRE 68 Put Nov-27-2026 | $0.50 | −$1.80 | −$1,800.00 | −78.27% | −$226.63 | −31.19% | $500.00 | 1.08% | 10 | $0.73 | $726.63 | ⚠️ "Last chg −$1.80" implies a prior last of $2.30 on a $0.73-basis put; a stale/odd prior print, transcribed as shown |
| 14 | OZK 40 Put Nov-20-2026 | $0.10 | $0.00 | $0.00 | 0.00% | −$282.65 | −87.61% | $40.00 | 0.09% | 4 | $0.81 | $322.65 | |
| 15 | WAL 70 Put Dec-18-2026 | $1.15 | −$0.60 | −$120.00 | −34.29% | −$321.33 | −58.29% | $230.00 | 0.50% | 2 | $2.76 | $551.33 | |
| 16 | ZION 62.5 Put Nov-20-2026 | $0.40 | −$0.19 | −$38.00 | −32.21% | −$355.33 | −81.63% | $80.00 | 0.17% | 2 | $2.18 | $435.33 | |
| 17 | KRE 67 Put Nov-27-2026 | $0.37 | −$0.17 | −$68.00 | −31.49% | −$362.65 | −71.02% | $148.00 | 0.32% | 4 | $1.28 | $510.65 | |
| 18 | KRE 60 Put Dec-18-2026 (lot 1) | $0.27 | +$0.07 | +$14.00 | +35.00% | −$459.34 | −89.49% | $54.00 | 0.12% | 2 | $2.57 | $513.34 | |
| 19 | WAL 65 Put Dec-18-2026 | $0.55 | −$0.20 | −$80.00 | −26.67% | −$462.65 | −67.78% | $220.00 | 0.48% | 4 | $1.71 | $682.65 | |
| 20 | GLD | $356.57 | −$12.00 | −$336.00 | −3.26% | −$505.57 | −4.82% | $9,983.96 | 21.59% | 28 | $374.63 | $10,489.53 | 52wk $356.14–$509.70 |
| 21 | GLD 375 Call Nov-02-2026 | $0.02 | −$0.51 | −$102.00 | −96.23% | −$647.33 | −99.39% | $4.00 | 0.01% | 2 | $3.26 | $651.33 | NE |
| 22 | KRE 60 Put Dec-18-2026 (lot 2) | $0.27 | +$0.07 | +$21.00 | +35.00% | −$797.02 | −90.78% | $81.00 | 0.18% | 3 | $2.93 | $878.02 | M |
| 23 | APO 95 Put Dec-18-2026 | $0.65 | −$0.55 | −$55.00 | −45.84% | −$1,119.67 | −94.52% | $65.00 | 0.14% | 1 | $11.85 | $1,184.67 | E |
| — | Pending activity | | | | | | | $5,927.58 | | | | | |
| — | **Account total** | | | **+$789.92** | **+1.74%** | **−$278.47** | **−1.02%** | **$46,241.82** | | | | | |

Σ basis of the 23 rows $27,205.99; Σ value $26,927.52. Badges: NE = Fidelity "new" marker; E = Fidelity badge (meaning not shown); M = margin.

## ② Orders — "Pending" panel (all dated Oct-30-2026; broker-verified)

| Order | Limit | Status | Amount |
|---|---|---|---|
| Sell to Close 1 QQQ Nov-20-2026 690 Put | $17.95 (Day) | **OPEN** (Cancel / Replace shown) | — |
| Sell 10 shares TBT | $38.57 (Day) | Filled at $38.57 | $385.70 |
| Sell to Close 1 QQQ Oct-30-2026 710 Put | $19.53 (Day) | Filled at $19.53 | $1,952.29 |
| Buy to Close 2 QQQ Nov-20-2026 670 Puts | $8.07 (Day) | Filled at $8.00 | $1,601.33 |
| Sell to Close 1 QQQ Oct-30-2026 711 Put | $17.64 (Day) | Filled at $17.67 | $1,766.30 |
| Sell to Close 1 QQQ Oct-30-2026 711 Put | $17.89 (Day) | Verified Canceled | — |
| Sell to Close 1 USO Oct-30-2026 163 Call | $8.00 (Day) | Filled at $8.01 | $800.32 |
| Sell to Close 1 USO Oct-30-2026 163 Call | $8.17 (Day) | Verified Canceled | — |
| Sell to Close 1 QQQ Oct-30-2026 711 Put | $16.30 (Day) | Filled at $16.63 | $1,662.30 |

## ③ Activity ledger — "Past 30 days" panel as visible (rows 10/23–10/30; older rows NOT visible in the capture — the panel may continue below)

| Date | Description (verbatim, condensed) | Amount | Cash balance |
|---|---|---|---|
| Oct-30-2026 | YOU SOLD PROSHARES ULTRASHORT 20+ YEAR TREASURY (TBT) (Cash) | +$385.70 | Processing |
| Oct-30-2026 | YOU SOLD CLOSING TRANSACTION PUT (QQQ) OCT 30 26 $710 (100 SHS) (Cash) | +$1,952.29 | Processing |
| Oct-30-2026 | YOU BOUGHT CLOSING TRANSACTION PUT (QQQ) NOV 20 26 $670 (100 SHS) (Margin) | −$1,601.33 | Processing |
| Oct-30-2026 | YOU SOLD CLOSING TRANSACTION PUT (QQQ) OCT 30 26 $711 (100 SHS) (Cash) | +$1,766.30 | Processing |
| Oct-30-2026 | YOU SOLD CLOSING TRANSACTION CALL (USO) OCT 30 26 $163 (100 SHS) (Cash) | +$800.32 | Processing |
| Oct-30-2026 | YOU SOLD CLOSING TRANSACTION PUT (QQQ) OCT 30 26 $711 (100 SHS) (Cash) | +$1,662.30 | Processing |
| Oct-27-2026 | YOU BOUGHT OPENING TRANSACTION PUT (QQQ) NOV 02 26 $715 (100 SHS) (Cash) | −$484.66 | $14,348.72 |
| Oct-27-2026 | YOU BOUGHT OPENING TRANSACTION CALL (USO) NOV 20 26 $170 (100 SHS) (Cash) | −$627.66 | $14,833.38 |
| Oct-27-2026 | YOU BOUGHT OPENING TRANSACTION PUT (QQQ) OCT 30 26 $711 (100 SHS) (Cash) | −$687.33 | $15,461.04 |
| Oct-26-2026 | YOU SOLD CLOSING TRANSACTION OPTION LIQUIDATION PUT (QQQ) OCT 26 26 $710 (100 SHS) (Cash) | +$4.74 | $16,148.37 |
| Oct-26-2026 | YOU SOLD CLOSING TRANSACTION OPTION LIQUIDATION PUT (QQQ) OCT 26 26 $705 (100 SHS) (Cash) | +$1.97 | $16,143.63 |
| Oct-26-2026 | YOU BOUGHT OPENING TRANSACTION PUT (QQQ) OCT 30 26 $710 (100 SHS) (Cash) | −$661.66 | $16,141.66 |
| Oct-23-2026 | EXPIRED CALL (QQQ) OCT 22 26 $717 as of 2026-10-22 (100 SHS) (Cash) | — | $16,803.32 |
| Oct-23-2026 | YOU SOLD UNITED STS OIL FD LP UNITS (USO) (Cash) | +$842.96 | $16,803.32 |
| Oct-23-2026 | YOU SOLD CLOSING TRANSACTION OPTION LIQUIDATION PUT (CRWV) OCT 23 26 $56 (100 SHS) (Cash) | +$88.34 | $15,960.36 |

Ledger arithmetic check (PROME): cash-balance column steps agree with the amounts from 10/23 $15,960.36 → 10/27 $14,348.72 (each row's balance = prior balance + amount, to the cent) ✓. The 10/29 capture's cash $13,386.72 vs the ledger's last settled balance $14,348.72 (10/27): a −$962.00 step not shown in this panel = the "pending (margin credit balance) $962.00" the 10/29 mirror carried; its row is not visible here.

Still UNSEEN after this capture (not in the visible rows): the GLD 25→28, AAPL 4→3, TBT 5→10 quantity changes; the USO Oct-28 165C, USO Oct-30 165C ×2 and CMG Oct-30 28P exits; any 10/22 rows (D-90 is only partly closed).
