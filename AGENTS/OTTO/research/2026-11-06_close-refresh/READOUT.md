# OTTO close refresh, data through Friday 2026-11-06

**Session:** s043, Claude Code, Opus 5.5. PROME relay of Will's 17:08 ET word. Bounded: no new thread, no spawn, no trade. Written 2026-11-06 ET.

**Result:** no score, band, gate, threshold or prediction moved. Convergence stays 32/50. Three dated records were stale and are corrected: the Tricolor auction row, the Hertz watch row, and the Chu and James docket notes.

## 1. Tricolor vehicle auction, the dashboard row was six months old

The hot row read "$39.5M on 5,857 sold (~62%)", a figure first logged 5/21. The auctioneer files a sworn monthly application and the trustee files a quarterly Form 1, so the row could have been refreshed all along.

| Measure | Value | Source |
|---|---|---|
| Vehicles sold, 1/11 to 10/31 | **9,082** | Sum of ten Holman applications, `HOLMAN_MONTHLY.tsv` |
| Net sale proceeds, 1/11 to 10/31 | **$63,089,785.80** | Same sum |
| October alone | 834 vehicles, $6,772,639.58 net | Dkt 1494 ¶13, filed 11/06, sha256 172154693c6bcfb3... |
| Trustee, car auction proceeds received at 9/30 | **$53,783,885.63** against an estimated **$65,000,000.00** | Dkt 1482 Form 1 asset 52, filed 10/28, sha256 f18da33743b77f2f... |
| Trustee, total estate receipts at 9/30 | $80,695,488.67 | Dkt 1482 Form 1 totals |
| Trustee, cars left | "approximately 2,000 cars remain to be sold" | Dkt 1482, status narrative |
| Vehicle Sales Deadline | **11/30/2026**, effective 10/15 | Dkt 1467 ¶2, entered 10/16, sha256 6d1fd6f0215f752e... |

**Tie-out, positive control:** the applications sum to exactly 5,857 vehicles and $39,500,061.19 through April 30, the old row to the dollar. So the method reproduces the old number, and the old number was April's.

**Unreconciled:** Holman's cumulative through 9/30 is $56,317,146.22; the trustee shows $53,783,885.63 received at 9/30. The $2,533,260.59 gap (4.5%) is not explained in what was read. Timing or setoffs are plausible `[EST]`, not established. The two are different bases and are not added or averaged.

**Recovery:** $63.09M over about $2B of debt is 3.2% realized. "~3%" stands. If 2,000 is a 9/30 count, about 1,170 remain; at October's $8,121 per vehicle the total would reach about $72.6M, 3.6%, above the trustee's $65.0M `[EST]`. The report's "as of the date of this report" leaves the count's date unclear (9/30 or 10/28), and the tail includes no-title vehicles (Dkt 1484), so that is a rough upper case, not a forecast.

**Old "~62%" retired.** Its ~9,500 base no longer fits: 9,082 sold plus about 1,170 left is about 10,250 `[EST]`.

**Tail quality, logged not scored:** vehicles that did not cover their sale costs ran 1.4–1.8% of sales in Feb–Apr and 5.8–7.4% in Jul–Oct; October's 62 of 834 (7.4%) is the highest. Average net per vehicle is noisy, $4,428 in June and $8,121 in October, so it says more about mix than about the used market.

**Colour:** 🔴🔴 unchanged. The downgrade condition is recovery above 35%.

## 2. Hertz fleet watch, the Q3 10-Q is read

Source: 10-Q 0001657853-26-000086, filed 11/05, period 9/30, sha256 957d7d0e9461ee5b...; prior 10-Q 0001657853-26-000046 for 6/30.

| Row item | 6/30 | 9/30 |
|---|---|---|
| HVF III Series 2021-2, expected final 12/2026 | $2,000M | **$1,000M** |
| 4.63% Senior Notes due 12/2026 | $200M (12/31/25) | **$199M**, not yet paid |
| HVF III 2021-A Remaining Capacity | $1,893M | $2,363M |
| HVF III 2021-A Availability Under Borrowing Base | $0 | **$0** |

**Correction to the row:** the "$1,893M VFN availability" it carried was Remaining Capacity. Availability under the borrowing base was zero then and now; capacity needs collateral.

**Fleet consequence, OTTO's lane:** Q3 disposal proceeds $1,695M vs $1,720M a year earlier; nine months $6,778M vs $5,970M (+14%), Americas $5,947M vs $5,084M. Americas Q3 average vehicles 427,207 vs 425,268; depreciation per unit per month $280 vs $279. Management attributes the Americas depreciation rise to lower per-unit gains on fewer dispositions. Nothing here reads as forced supply into wholesale in Q3.

**Watch status:** not fired. "Amortization event", "early amortization" and "rapid amortization" appear nowhere in the filing text, a literal text search of this one filing. Close test not met: the notes and $1,000M of 2021-2 are still outstanding. "Series 2021-2" appears only in the debt table, so the filing does not say why $1,000M came off; August's $875M Series 2026-3 and 2026-4 issuance is a possible source, not a stated one.

**For LIQUID, credit read not graded here:** in November HVF III extended the 2021-A Class B to 11/2/2028 at 12.46% fixed (was 9.28%), and Class B cannot fund unless the 4.625% notes are paid in full before 12/31/2026. Corporate liquidity $946M vs $1,489M at 12/31/25, cash $531M vs $631M at 6/30. Corporate covenants in compliance at 9/30. Maturities remaining in 2026: vehicle $1,272M, non-vehicle $203M.

## 3. Court feeds through 11/06

| Case | New | Effect |
|---|---|---|
| James, 1:26-cr-00029 | ECF 161, memo endorsed 11/06 by Judge Caproni: redactions allowed; **government's response to the adjournment motion due Monday 11/09**. sha256 237b5eea94449f9e... | New dated row. No ruling on adjournment. The endorsement sits in an encoded font; decoded by hand and read in context |
| Chu, 1:25-cr-00579 | Sealed minute entry 11/06, contents unknown. Last numbered public entry ECF 190, 10/29 | No suppression ruling on the public feed through 11/06. Feed is newest 30 only (WQ-531) |
| First Brands, 25-90399 | Dkt 4052, Kingsbridge certificate of no objection on Dkt 3841, may take that item off the 11/18 hearing if an order enters. Dkt 4047 and 4048: objection and notice on compensation applications | No date moved |
| Tricolor Ch.7 | Dkt 1492/1494 above; Dkt 1490 Navarro Towing settlement approved. Dkt 1489 transcript restricted | Ares deadline 11/30 unchanged |

## 4. Filings and the auto line in G.19

- **10-D panel:** dry-run, both controls pass, no new filings. Newest are 10/15 (Santander, Bridgecrest) and 10/29 (Exeter), September collections.
- **Shelf probe:** dry-run only, ledger frozen. 7 of 8 shelves validated with no halt. CPS query errored, not counted as quiet, and a retry timed out; CPS last validated 10/25 at 2026-D. Exeter stops at 2026-4, window to 11/12.
- **CRMT:** no 8-K after 11/05. Bridge runs to Monday 11/09. BROCK grades.
- **Credit Acceptance:** Form ABS-15G filed 11/06 under Rule 15Ga-2 for Credit Acceptance Auto Loan Trust 2026-3, Grant Thornton report dated 11/06. A pre-sale step; no size, price or closing is read.
- **Federal Reserve G.19, first print, not seasonally adjusted (WALTER's saved page):** motor vehicle loans $1,589.8B at Q3, $1,574.6B at Q2, $1,559.7B at Q1, $1,560.7B a year ago. Up $15.2B (+0.97%) on the quarter after +$14.9B; +1.9% YoY. Perimeter differs from the NY Fed's $1.713T, so the two do not reconcile; carry the difference into the 11/10 check. No delinquency content.

## 5. Vendor bars, 2026-11-06, yfinance, not official closes

CVNA $73.57 (+2.07%, adjusted for the 5-for-1 split of 2026-05-08), ALLY $38.17 (−1.70%), CRMT $1.44 (−5.26%), CPSS $10.17 (+2.94%), CACC $529.56 (+1.34%), MTB $217.75 (−0.92%), OBK $53.24 (−1.46%), TFIN $61.23 (−1.61%).

## 6. Not read

Exhibit A-1 of Dkt 1494 (vehicle list), Dkt 1484 (no-title list), full body of the Hertz 10-Q beyond the row's checks, Hertz earnings release, CPS shelf leg, sealed Chu entry, First Brands Dkt 4047 body.
