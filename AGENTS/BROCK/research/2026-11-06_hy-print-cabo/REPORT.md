# BROCK, November 6, 2026: first HY print on the selloff, and Cable One's 10-Q and call

**Stamp:** Fri 2026-11-06 about 10:20 ET. **Task:** WQ-626 A, DOCKET L965; resume list in `PROME/inbox/processed/2026-11-05_from-BROCK_close-addendum-L876-cabo-L916.md`; WALTER SIG-W-20261106-004.
**Limits kept:** no level, operator, instrument or consequence changed on any gate, kill rule, band or frozen letter. No trade view. Scores unchanged, convergence 58/70.

## 1. The five things that matter

1. **The November 5 print carried the selloff, and it was broad, not a low-quality event.** HY 348 (+16 bp), BB 213 (+14), B 367 (+16), CCC 1,320 (+23). In percent, BB widened most (+7.0%) and CCC least (+1.8%).
2. **Ladder row 10 NOT FIRED on the letter.** VIX +11.57 points at the official close, but HY widened 16 bp on the same print.
3. **My CCC/BB condition did not fire, and the base rate says it almost never can on a widening.** The ratio fell 6.52 to 6.20. It fell on all 42 days HY widened 10 bp or more in the three-year FRED window.
4. **Cable One L876 is now BLOCKED-BY-ORDER on the 10-Q.** MBI not closed. The 10-Q adds a fact the WALTER card lacks: Cable One says it does not meet the NYSE listing standard, and its own risk factors trace delisting to a convertible put it may not be able to pay, then a cross-default.
5. **No going-concern language, but that is partly the calendar.** The 12-month window from the 10-Q ends about November 5, 2027; the MBI term loans mature November 12, 2027, and Cable One's own revolver in February 2028. The next 10-K's window will reach that revolver.

## 2. The print (FRED first-published request, read 10:10:44 ET November 6)

BB had posted by this read. ALFRED labels the first-published date as the observation date, so the label does not show arrival time (LIQUID KB-LIQ-151).

| Series | 10/28 | 10/29 | 11/04 | 11/05 | d/d bp | d/d % | 5-session bp (from 10/29) |
|---|---:|---:|---:|---:|---:|---:|---:|
| HY OAS | 314 | 326 | 332 | **348** | +16 | +4.8% | +22 |
| BB | 184 | 194 | 199 | **213** | +14 | +7.0% | +19 |
| B | 318 | 332 | 351 | **367** | +16 | +4.6% | +35 |
| CCC | 1,307 | 1,325 | 1,297 | **1,320** | +23 | +1.8% | −5 |
| IG | 86 | 89 | 91 | **93** | +2 | | +4 |
| BBB | 107 | 110 | 113 | **116** | +3 | | +6 |
| VIX close (VIXCLS, points) | 16.91 | 17.20 | 16.61 | **28.18** | +11.57 | +69.6% | +63.8% |
| CCC/BB (ratio of OAS) | 7.10 | 6.83 | 6.52 | **6.20** | −0.32 | | −0.63 |
| CCC−BB bp | 1,123 | 1,131 | 1,098 | **1,107** | +9 | | −24 |

HY +16 bp: 17 of 785 day-over-day changes were +16 or wider (2.2%), window 2023-11-07 to 2026-11-05. VIX +11.57 is the fourth-largest daily rise since August 2022, behind 2025-04-04 (+15.29), 2024-08-05 (+15.18) and 2024-12-18 (+11.75).

## 3. Ladder row 10: "VIX spike +3 without HY widening"

| Leg | Reading | Result |
|---|---|---|
| VIX spike +3 | +11.57, official close, FRED VIXCLS | MET |
| Without HY widening | HY +16 bp same print | NOT MET on any plain reading |
| Row | | **NOT FIRED** |

⚠️ The row has no numeric definition of widening and I invented none. Two facts bear on that gap:

- **A different row reads the same print the other way.** VIOLET's Will-approved definition for its own row calls credit flat at HY no wider than +25 bp over 5 sessions; HY is +22. That is VIOLET's row and VIOLET's grade. I did not import it.
- **Base rate.** On the 25 days VIX rose 3 or more points in the HY window, HY was unchanged or tighter on 2 (2024-12-18 −2, 2025-04-08 −4), +1 to +5 on 2, and +6 or wider on 21; median +11. A plain reading fires about 1 time in 12.

## 4. CCC/BB

**Grade: not my signal.** The STATUS condition is "CCC/BB turns UP DURING a widening". It fell 6.52 to 6.20, and fell 7.10 to 6.20 across the widening from 10/28.

**Do not read the fall as comfort.** BB is the denominator and it moves most in percent when the whole market reprices. CCC−BB in basis points rose 9 on the same day, so the two bases disagree on direction.

**Instrument finding (FRED, 786 observations, 2023-11-07 to 2026-11-05; FRED's ICE history is about three years, so one cycle):**

| Test | n | Ratio rose | Ratio fell |
|---|---:|---:|---:|
| Days HY widened 10+ bp | 42 | **0** | 42 |
| Days HY widened at all | 328 | 46 | 281 |
| Days HY tightened | 372 | 314 | |
| 5-session HY +25 or more, non-overlapping | 12 | 0 | 12 |
| 10-session, non-overlapping | 15 | 2 | 13 |
| 15-session, non-overlapping | 14 | 1 | 13 |
| 20-session, non-overlapping | 13 | 3 | 10 |

Correlation of daily HY change with daily ratio change: −0.79. The ratio rises mainly in rallies: its 10/28 reading of 7.10 came at HY 314, and its window high of 7.17 on 9/11.

**So what:**

1. My condition (and X1 test (b), which needs it) is close to unreachable on a real widening. A zero count there comes from the ratio's arithmetic, not from credit quality. This is standing trap 7, panel depth. The 10/1 to 10/20 case in KB-BRK-360 was HY +9 only, below these tests.
2. **The FORUM-5 W3 reversal leg points the wrong way.** "CCC/BB ≤5.93" is written as a reversal of deterioration. 696 of 786 observations are at or below 5.93, and another selloff day like 11/05 (−0.32) would nearly reach it from 6.20 (needs −0.27). The leg can pass because BB widened, which is the opposite of a recovery. P2 line 58 already called this leg weak in both directions and not base-rated; this is that base rate.
3. **Consequence today: none.** W3 already cannot reach 3 of 4 by 11/30 (STATUS carried debts). P2 line 58 also reads "or CCC−BB ≤828, 2 consecutive WEEKLY observations", while line 154 and STATUS read "×2 observations". Both go to L186 before 11/30. No letter changed here.

## 5. Cable One 10-Q (0001632127-26-000038, accepted 11/05 17:15:50 ET, read at SEC; liquidity, notes, litigation and risk sections, not cover to cover)

**L876 grade: BLOCKED-BY-ORDER, FINAL on the 10-Q; MBI NOT CLOSED.** "temporarily prohibits the Company from consummating the MBI Acquisition"; "not obligated to close ... if and for so long as any legal restraint ... (including the TRO) is in effect". The order itself remains unread. The 11/13 hearing date is now issuer-stated, no longer press-only; its outcome is still unread until it happens.

| Item | Figure or words | Basis |
|---|---|---|
| Stockholders' equity | **−$86.3M** at 9/30, from +$1,433.6M at 12/31/25 | Balance sheet, book |
| Q3 net loss | −$431.8M; nine months −$1,560.6M | Asset impairments $412.1M Q3; MBI equity-investment impairments $26.7M Q3, $376.4M YTD, are a separate line |
| Cash | $674.8M at 9/30 | Includes the net $500M September revolver draw ($700M borrowed, $200M repaid) |
| Revolver | $1.05B drawn of $1.25B, $200M nominal availability | 9/30 |
| Put Price | about $480M for the remaining about 55% of MBI | 10-Q |
| MBI equity to be acquired | "of uncertain value" | Risk factor, 9/30 |
| Rescue lenders | **Unnamed.** "engaged in discussions" | No private-credit lender named, so the catalyst row's line is not met |
| "going concern" / "substantial doubt" | **0 hits each** | Whole document text |

**New since my 8-K read:**

| Finding | Evidence |
|---|---|
| **NYSE non-compliance, stated as fact** | "we are not in compliance with the continued listing standards under Section 802.01B": equity under $50M and 30-trading-day average market cap under $50M. Issuer "intend[s] to submit" a plan |
| **Independent check** | 5,680,440 shares (10/30 cover) × average of 30 vendor closes through 11/5 ($8.65) = $49.1M, ties to "less than $50 million" |
| **Hard floor** | Average market cap under $15M over 30 trading days means prompt delisting, no cure. $15M = $2.64 a share. $4.26 to $4.43 on 11/06 intraday (vendor, −14% to −17%) = about $24M to $25M |
| **The chain** | Delisting could "trigger a 'fundamental change'" under the convertible indenture ⇒ holders expected to put $345.0M at par ⇒ "we may be unable to satisfy the repurchase obligation" ⇒ event of default ⇒ cross-default under the credit agreement |
| **Second lender front** | A creditor group's counsel threatened claims "substantially similar" to CoBank's; even if the TRO is dissolved, CoBank or others "may pursue litigation" |
| **GTCR front** | 11/2 letter alleges failure to use reasonable best efforts; intervention "as soon as November 6"; issuer says without merit |
| **Trapped both ways** | If obligated to close and unable to address maturities, "it is possible that we will not consummate", which would be a breach exposing it to damages or specific performance |
| **Exchange offer dead** | MBI term loan exchange: about 34% accepted, not consummated |
| **Springing maturity, not in the insufficiency list** | Term Loan B-2/B-3 ($231.3M + $727.9M = $959.2M) mature 10/30/2029, but move to 5/3/2028 if more than $150M of Term Loan B-4 is outstanding that day |

**Maturity wall (9/30 principal):**

| Date | Debt | $M | Condition |
|---|---|---:|---|
| 8/11/2027 | MBI revolver | 22.0 | If MBI closes |
| 11/12/2027 | MBI term loans | 916.2 | If MBI closes |
| Feb 2028 | Revolver drawn | 1,050.0 | |
| Mar 2028 | 1.125% convertibles | 345.0 | Par put earlier if delisted |
| 5/3/2028 | Term Loan B-4 | 694.3 | |
| 5/3/2028 | Term Loan B-2/B-3 | 959.2 | Only if more than $150M of B-4 remains |
| 2030 | 4.00% senior notes | about 503 | Call figure, Koetje |

**Going-concern window (my inference; accounting judgment is management's and the auditor's).** The 10-Q's adequacy statement runs 12 months from filing, to about 11/5/2027. The first large maturity, MBI's, sits 7 days past that and only applies if MBI closes. Cable One's own first wall is 3 months past it. The issuer already writes that liquidity "will be insufficient" for these maturities. A FY2026 10-K filed from late February 2027 has a window reaching the February 2028 revolver. So today's absence of the words is weaker comfort than it sounds. Registered as BRK-38.

**Book equity is not a solvency finding (my inference).** A −$86.3M book figure and "of uncertain value" sit beside CoBank's constructive fraudulent transfer claim, but book value is not the legal test and the order is unread. I give no view on the 11/13 outcome.

## 6. Cable One call, November 5 (PARTIAL)

⚠️ **About 80% read.** Motley Fool transcript, secondary, verbatim to mid-answer in Koetje's reply to McHugh; the last about 20% and the operator's close are unread. Benzinga, MarketBeat, Seeking Alpha and GuruFocus all refused the automated fetch (403). Quartr not called, no subscription. Replay is listed to December 3; audio not read. The Fool page's own "risks" summary attributes Chapter 11 wording to Koetje, but that wording is not in the verbatim text read, so I do not attribute it to the call.

| Speaker | Words | So what |
|---|---|---|
| Koetje | "With respect to MBI, we continue to evaluate the appropriate next steps" and no updates "today" | No new MBI fact |
| Koetje | "actively evaluate a range of financing alternatives" | Softer than the 10-Q's "will be insufficient" |
| Koetje | "Our balance sheet continues to be supported by a substantial cash balance and strong operating liquidity" | Same; the 10-Q was filed 15 minutes after the call began |
| Koetje | Charges "do not impact our cash flow, liquidity, operating strategy or long-term growth initiatives" | Accounting framing |
| Holanda, asked by Williams (TD Cowen) on MBI timing and the balance sheet | "Item 17 under subsequent events lays out pretty much exactly where we are" | Management deflected to the filing; balance-sheet part unanswered in the text read |

In the text read, nobody mentions the order, CoBank, the hearing, GTCR, NYSE, covenants or going concern. That covers 80% of the call and proves nothing about the rest. **Grade for the resume item: call adds no fact beyond the 10-Q in the part read.**

## 7. Car-Mart L916 remainder

EDGAR submissions JSON and browse-edgar Atom agree at 10:15 ET November 6: newest filing is still the 8-K of 11/05 (0001171843-26-007147). **No other filing since 08:00:41 ET 11/05**, which covers the unread 17:30 ET window. Silence grades nothing. The Mon 11/09 STD read stands.

## 8. WALTER SIG-W-20261106-004 against my gates

Secondary and press, as the card says; nothing re-read at TRACE, ING or the Bank of England.

| Gate or row | Read |
|---|---|
| BRK-25 / ladder row 4 | **Does not count.** The instrument needs a loan held by a BDC. ING is a bank. Even a sub-90 clearing price on 11/19 would not move the count of 2 |
| BRK-07 | No write-down evidenced; CoreWeave delayed-draw lines in OBDC, OTF, PSBD and GECC are small at 9/30 (KB-BRK-425) |
| GATE-BRK-R2, X1, Cross-asset vector | Unaffected. Nothing here is a redemption or wrapper event |
| Bank warehouse / BRK-31 | ING is a non-US bank, not one of the 11 |

CoreWeave's unsecured bonds at 16% yields say nothing direct about a delayed-draw loan mark, but the 12/31 marks are the first place that shows. Logged under `combo:ai-financing-repricing`.

## 9. Not done, by limit

- **SIG-W-20261105-067 ACTION** (was any Ares-managed public vehicle among Tricolor's lenders?): DEFERRED, outside this bounded task.
- **GIBBS packet 11/06** (Goldman $368M provision, BRK-31; figure check before 11/16): direct packet, not processed on this spawn.

Reproduce: `ccc_bb_daily.py` and `ccc_bb_windows.py` in this directory, run from repo root.
