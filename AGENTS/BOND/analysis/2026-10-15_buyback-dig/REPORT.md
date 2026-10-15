# BOND — 2026-10-15 buyback dig: what the 10/15 op (and the stepped-up program) tells us

**Asked by Will 14:41 ET: "investigate this — what more can we determine?"** Inputs: FiscalData `buybacks_operations` (229 ops) and `buybacks_security_details` (5,626 rows since 2024), MSPD table 3 (9/30), NY Fed SOMA by CUSIP (10/7), TreasuryDirect auctioned bonds, Treasury par curves 2025–26, Yahoo ^TNX/^TYX op-window bars. Code `dig.py` → `derived.json`; ranking in `cumulative_retirement.txt`. All pulls 2026-10-15.

## Findings

| # | Finding | Figures |
|---|---|---|
| 1 | **Treasury is NOT paying up — the apparent narrowing was a timing artifact.** Against the *prior* close, the yield Treasury paid over the interpolated par curve looked like it collapsed (10–20Y: +18→+19→+6→+1bp; 20–30Y: +12→+2bp). But September ops ran on days yields rose before 13:40 and October ops on days they fell. Corrected to the op window, the spread is **flat**. | 10–20Y op-window-adjusted: **+12.6 (7/1) · +11.5 (9/10) · +11.9 (10/1) · +11.4 (10/15)**; same-day-close bracket +14.3 / +7.8 / +10.8 / tonight. 20–30Y: **+6.8 (9/24) · +6.9 (10/8)**; same-day +3.9 / +8.6 |
| 2 | **Off-the-run cheapness is stable → no sign of dealer balance-sheet strain in old long bonds.** If dealers were choking on inventory, old bonds would cheapen vs the curve; they haven't. | ~11–13bp (10–20Y) and ~7bp (20–30Y) on the op-window basis, July→October |
| 3 | **Buybacks offset about 30% of new long-bond interest-rate risk since the cap rose.** | Since 9/10: $27.27B par retired (market value $17.80B), DV01 $23.28M/bp vs 20Y/30Y auctions $57B par, DV01 $77.42M/bp |
| 4 | **The offer surge is specific to 10–20Y, not a general long-end exit.** | 10–20Y offered $46.4B (10/1) and $40.8B (10/15) = the **two largest of 28 ops since 2024** (median $20.0B). 20–30Y offered $10.5B (9/24) and $14.9B (10/8), **below** its $20.9B median despite a 3× larger cap |
| 5 | **Single-bond blocks dominate the 10–20Y fills.** Pattern consistent with one or a few large holders offering big blocks of specific 2041–42 bonds (Treasury takes the cheapest offers). Seller identity is NOT observable in any Treasury release. | 10/1: $4.95B of 912810TH1 (82.5%). 10/15: $5.58B of 912810TC2 (93.0%) = **9.2% of TC2's non-Fed float** in one op (outstanding $68.48B − SOMA $7.63B = $60.85B, 9/30–10/7) |
| 6 | **Some old issues are now heavily retired.** | 912810TH1 (3.25% 2042): **$14.07B = 28.2% of issued**; 912810RV2 17.0%; 912810SY5 13.8%; 912810TC2 10.9% (cross-check: MSPD 9/30 redeemed −$2,150M for TC2 = FiscalData cumulative through 9/10, exact) |

## What it means for BOND

- **F2 / "is Treasury quietly supporting the long end?":** No, on two independent legs: (a) purchases are off-the-run (5/5 ops), and now (b) prices paid are not rich to the curve on a timing-correct basis. Treasury is harvesting cheap old bonds at a steady discount.
- **Dealer absorption (VX-BND-04/16):** finding #2 is mild counter-evidence to dealer strain; score unchanged at 2.
- **Supply:** a ~30% DV01 offset is material but leaves ~70% of new long-end duration for the market; the 20Y-R on 10/21 ($13B) is still the next real demand test.

## Caveats (travel with every finding)

- **Selected sample:** accepted prices are the *cheapest* offers Treasury chose, not market mids; the spread LEVEL is biased cheap and partly structural (low-coupon/deep-discount bonds vs a par curve). Only the CHANGE over time is interpretable.
- **Op-window adjustment uses vendor ^TNX/^TYX moves** (5-min mean 13:40–13:55; 7/1 uses a 1-hour bar) as a proxy for the 14–19y and 21–25y sectors; 10–20Y uses the ^TNX/^TYX average. Same-day official close brackets it; the 10/15 same-day close publishes tonight.
- DV01 uses street-convention yields from accepted clean prices; issued DV01 uses TreasuryDirect auction price/coupon/maturity. The 10–20Y retirements are compared against 20Y/30Y supply only (10Y note supply excluded by choice).
- Finding #5's "few large holders" is an inference from concentration; no source identifies sellers.

## Owed check (dated)

- **FR2004 as-of 10/7 (publishes 10/15 ~16:15 ET)** covers the 10/1 op settlement (10/2). If the 11–21Y dealer coupon bucket fell by a similar size to the $6B op, dealers were likely sellers; if not, the blocks came from end-investors. Weak test (dealers intermediate), recorded so it is not over-read either way.
