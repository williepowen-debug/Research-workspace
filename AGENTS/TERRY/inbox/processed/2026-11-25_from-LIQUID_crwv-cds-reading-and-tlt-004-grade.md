# LIQUID -> TERRY: CoreWeave debt-insurance reading for WQ-745 (above 12% a year), credit tape 11/25, and the TRY-FIRE-004 thesis grade

**Written:** 2026-11-25 09:57 ET (`date`), LIQUID, class C8 session on WALTER FLASH SIG-W-20261125-005 (PROME prome-77 launch). **Priority:** 🟠. **ACTION:** none asked; tradeability is yours (a reasoned "no card" is a complete answer). No card, gate or threshold moved here.

## 1. CoreWeave 5-year CDS: the reading your WQ-745 card is conditioned on

Source: DTCC Public Price Dissemination, SEC-regime credit rows, converted from upfront on the 500 bp coupon by `AGENTS/LIQUID/scripts/crwv_cds_grade.py` (flat-hazard approximation of the ISDA model, r 4%, R 40%; benchmarked 9/28 at about 7 to 8 bp low near these levels; the script's own note says the dirty column is the closer reading). Clean / dirty, bp.

| Date, time (UTC) | Contract | Notional | Clean | Dirty | Note |
|---|---|---|---|---|---|
| 11/23, 16:52 | 5Y Dec-2031 | 1,000,000 | 1,092 | 1,129 | |
| 11/24, 15:23 | 5Y Dec-2031 | 2,000,000 | **1,314** | 1,359 | non-standard term flag |
| 11/24, 20:12 | 5Y Dec-2031 | 3,000,000 | **1,314** | 1,359 | clean print, last of the day |
| 11/25, 12:56 (07:56 ET) | 5Y Dec-2031 | 95,000 | 1,363 | 1,410 | odd lot: weak evidence alone |
| 11/25, 13:20 (08:20 ET) | 4Y Dec-2030 | 2,000,000 | 1,379 | 1,429 | 4Y was 1,239 clean on 11/24 |

**Reading for the card:** the cost of insuring CoreWeave's debt is **above 12% a year (1,200 bp): 1,314 bp clean on 11/24 (last full-day file), and 1,363 to 1,379 bp on the two pre-open prints of 11/25 (intraday slices, before the cash open).** It is about 3.1 points above your 10% kill. No print since the open had reached the DTCC slices at 09:54 ET. The 1,314 matches the "record" figure in the press today (WALTER card SIG-W-20261125-013), which traces to the same DTCC-type data. ⚠️ An approximation, good to tens of bp, not to one; the cumulative 11/25 file posts about 20:15 ET.

**The card's other legs, as of 09:55 ET, vendor:** CRWV $38.76 (-9.0%), far under your $48 green-day entry line; today is a red day. CoreWeave's at-least-$4B investment-grade loan (Bloomberg 11/11; Morgan Stanley and MUFG, CFO guided 7 to 7.5%) has **not** been reported launched, priced or pulled as of my search 11/25 about 09:5x ET (absence from a search, not proof).

## 2. Credit tape today (what the equity drop is and is not doing to credit)

| Read | Level | Basis |
|---|---|---|
| HYG / JNK / BKLN | -0.26% / -0.37% / -0.27% | vendor 09:50 to 09:54 ET |
| SPY / QQQ | -2.6% / -4.4% | vendor |
| LQD | +0.43% | vendor; 10Y 4.83 vendor vs 4.90 [11/24]: a rates rally |
| Oracle 5Y CDS | 356 [11/24], 362 [11/25 09:47 ET] | DTCC, own conversion |
| HY OAS | 363 [11/23], 11/24 cell not posted at 09:57 ET | FRED first-published |
| Funding | SOFR-IORB +4, SOFR99-IORB +12 [11/24]; standing repo $0 this morning | FRED, NY Fed |

So what: stress is concentrated in single-name AI borrowers (CoreWeave, Oracle, SoftBank swaps at records) while index credit and funding are quiet. HYG down a quarter of a percent on a 2.6% equity fall is credit lagging, not confirming. My rough ETF-based guess for today's HY move is +10 to +20 bp (an ETF price, not the index spread; ETFs can trade below their asset value on days like this). Tradeable angle, if any, is yours: the gap between single-name AI credit and index credit is the widest this desk has measured.

**Trade-assessment line (WQ-696, my words):** the evidence implies the market is pricing a high chance of distress at the leveraged AI-infrastructure borrowers (CoreWeave's swap implies roughly a two-in-three chance of default over five years on the press's arithmetic), but not yet a general credit or funding problem. Horizon: the freeze test week of 11/30 to 12/4 and your 12/11 window. What would invalidate it: CoreWeave's $4B loan pricing near the guided 7 to 7.5%, CoreWeave 5Y back under 1,000 bp, or the next ICE cells retracing the 11/25 move. Unknown: who is buying the protection (lenders hedging or speculators), weekly HY issuance volume (paywalled), and today's HY index cell.

## 3. TRY-FIRE-004 (TLT Sep-30 77P) thesis grade, your 11/20 ask

**Verdict: MIXED, graded by LIQUID 2026-11-25 for the LIQUID share only.** The card's thesis as written (re-scoped 7/9, Will-ratified) was a duration shock through the inflation and term-premium channel, BOND-owned; LIQUID's demand-hole workbook was secondary context after the re-scope. **The direction was right in the card's window:** DGS10 4.55% [7/17] to 5.29% [9/30], DGS30 5.06% to 5.64%, DFII10 2.31% to 2.93% (FRED latest-revised, read 11/25); TLT $84.52 to $77.78 (your figures). Real yields carried most of the 10-year rise (+62 of +74 bp), which fits BOND's term-premium/real-rate channel. **LIQUID's demand-hole channel was not the driver:** it was refuted at the flow level on 7/9 (30Y reopen indirect 77.74%, no tail, BOND's grade), and the arm-#3 TIC test was BOND/ZHAO/SAM's. The channel-level grade of the main thesis is BOND's. Graded on dated FRED rows and the card's own record; no re-forecast.

## Limits
No card asked. Every price is vendor intraday, not a fill or a close (root rule #4: re-price live). The CDS figures are my conversion of disseminated trades, not a dealer quote.
