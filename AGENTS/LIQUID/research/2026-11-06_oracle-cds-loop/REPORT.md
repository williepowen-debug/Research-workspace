# Oracle CDS against Microsoft and SoftBank: LIQUID's leg

**Date:** 2026-11-06, written 16:00 ET, on files published to that time. **Authority:** Will in PROME's chat 15:40 ET; `inbox/2026-11-06_from-PROME_Oracle-CDS-loop.md`. **Scope:** LIQUID's leg only; PROME synthesizes. SAM owns SoftBank funding and VULCAN owns the Microsoft and capex mechanism.

**Labels.** FILE = SEC filing or public data file read here (DTCC, Treasury, State Street, Nasdaq). RELAY = someone else's report of a source I did not read. INFERENCE = my reading. All $0, no paid data, no login.

## Answer

On what I can measure, these are **two stories sharing one AI-financing tape, not one proven funding loop.** Oracle CDS moves most on Oracle's own financing news and on AI-sector days. The Microsoft report barely registered: about +6 to +8 bp on Oracle 5Y by the close of November 6, against a −6.2% five-minute stock drop. SoftBank's widening came first that day, so the report cannot have caused it. Nothing here shows a dollar passing between them. **That is absence on a partial view.** I cannot see buyers, sellers, net positions, swap spreads or the loans themselves.

⚠️ **My earlier line was wrong.** I said the "3.25%" Oracle CDS level was unsupported through November 5. I had tested only November files. Oracle 5Y traded through 325 on October 20, with a disseminated 342.5. That line reached WALTER's card 037 and two PROME packets. Corrected in §7.

## 1. Oracle 5Y CDS history, one named basis

**Basis [FILE].** DTCC SEC public dissemination, 234 daily files December 15, 2025 to November 5, 2026, plus about 550 same-day slices for November 6. Series: on-the-run 5Y contract, new trades only, cancelled rows removed, corrections applied, packages excluded. Data: `oracle_5y_dtcc_daily.tsv` here. Disseminated spreads are the named basis; they print on only about half of days, so converted medians fill the gaps and are always marked "conv".

**Calibration [FILE].** Rows carrying both a spread and an upfront show conv runs 4 bp under disseminated at 250 bp and wider (n=19, −5.0 to +3.3). A bare conv figure therefore understates the disseminated basis slightly.

| Date | Contract | Disseminated | Conv median | Conv range | Note |
|---|---|---:|---:|---:|---|
| December 17, 2025 | Dec 2030 | 153 to 156 | 151 | 145 to 154 | |
| February 2, 2026 | Dec 2030 | 127 to 129 | 126.5 | 122 to 130 | Largest one-day fall in the series, −29.5, on the day Oracle priced its February notes |
| March 27 | Jun 2031 | 199 | 201 | | |
| July 24 | Jun 2031 | 214 to 217 | 213 | 212 to 216 | |
| September 28 | Dec 2031 | 249 to 251 | 249 | 247 to 253 | |
| October 13 | Dec 2031 | 264 | 260 | 257 to 261 | |
| **October 15** | Dec 2031 | **302** | 295 | 279 to 313 | "288" is not a DTCC figure, see below |
| October 19 | Dec 2031 | none | 304 | 297 to 319 | |
| **October 20** | Dec 2031 | **342.5**, 13:36Z | 333 | 305 to 346 | **High of the whole file window** |
| October 21 | Dec 2031 | **315** | 312 | 306 to 316 | |
| October 22 | Dec 2031 | 314 | 316 | 313 to 316 | |
| October 28 | Dec 2031 | 276 to 280 | 258 | 251 to 285 | |
| **October 30** | Dec 2031 | **293** | 287 | 280 to 294 | Your point confirmed |
| November 2 | Dec 2031 | none | 294 | 290 to 296 | Notes priced |
| **November 3** | Dec 2031 | **300** | 294 | 293 to 295 | Your point confirmed |
| November 4 | Dec 2031 | 292.5 | 294 | 288 to 297 | Notes and equity closed |
| November 5 | Dec 2031 | 305 | 304 | 290 to 311 | |
| November 6, to about 15:50 ET | Dec 2031 | 305 in a package only | 312 | 306 to 314 | Partial. Full file about 20:15 ET |

⚠️ Each roll raises the series, because the new contract is longer: on November 6, Jun 2031 printed about 288 and Dec 2031 about 306 [FILE]. So December 2025 and November 2026 are not one contract. September 21's 145 conv is a roll-day artifact and is not a level; disseminated rows the next day read 212 to 215.

**The three points in your brief.**

| Point | Finding |
|---|---|
| 293 [10/30] | Disseminated, confirmed [FILE] |
| 300 [11/3] | Disseminated, confirmed [FILE] |
| 288 [10/15] | **Different basis.** RELAY: WALTER SIG-W-20261016-005, Securitas citing S&P Global MI and LSEG, a vendor close, "record". DTCC that day: disseminated 302, trades 279 to 313, late prints 279 to 287 [FILE]. Consistent with a late-day close; it is not a DTCC print, and it stopped being the high within three sessions |

**The two claims.**

| Claim | Finding |
|---|---|
| "3.25%" | Source: an image post, in card 029; no date or vendor established [RELAY]. **As a level, supported:** October 20 had 12 trades, ranging 305 to 346 conv, ten of them at 323 or wider, with 342.5 disseminated [FILE]. **As November 6's level, not supported so far:** best conv print 314, about 318 on the disseminated basis, through about 15:50 ET [FILE]. **As a "record" on November 6, not supported:** October 20 stands higher on this file |
| "315 bp" | Undated [RELAY]. Matches a disseminated 315 on October 21, 18:02Z, and 314 on October 22 [FILE]. A match, not proof of what the report meant |

"Record" beyond this window: my file begins December 2025, so I cannot grade all-time. Relays call the level an 18-year high [RELAY].

## 2. What is driving it

| Channel | Evidence for | Evidence against or missing | Read |
|---|---|---|---|
| **Oracle's own financing news** | October 28: last print before the 8-K about 285 to 290 at 14:18 to 14:43Z; 8-K accepted 18:24:44Z; first print after it 256 to 261 at 18:34Z [FILE]. February 2: −29.5 on pricing day with ORCL −5.3% [FILE]. Both times credit improved on funding news whatever the stock did | n=2. On October 28 no trade printed for nearly four hours before the 8-K, so the move cannot be timed to it, and the press release time is not established. The October FOMC decision fell in the same gap [catalyst file]. ORCL rose 10.7% that day. The gain was fully lost by November 5, with the pledge intact | **Strongest evidence** [INFERENCE] |
| **Bond supply** | Spreads and CDS peaked before the deal. New 2031s priced +275 against about 115 in February [FILE]. Amazon went 79 to 100 and Alphabet 77 to 87 from October 28 to about November 4 to 5 disseminated, so supply pressure may be sector-wide [FILE; supply link INFERENCE] | CDS did not fall once the $20B was done. Nov 2 to Nov 5 it rose. New notes sat above reoffer | Partial |
| **Lender hedging** | October 19 to 20: 5Y +52 conv over two days while ORCL rose 1.1% and 1.2% and HY moved about +2 [FILE]. New notes held above reoffer while CDS widened [FILE]. Both fit a protection bid not matched by cash selling [INFERENCE] | **Cannot be seen.** DTCC shows no buyer, seller or net position. I found no primary or relay in the repo naming a lender hedging Oracle. Print counts mislead: one trade can appear as both a client and a clearing row | **Plausible, unproven.** Do not state it as fact |
| **Credit view** | Curve rises with maturity: about 140 Jun 2028, 272 Dec 2030, 288 Jun 2031, 306 Dec 2031 on November 6 [FILE]. No inversion means no near-term default pricing [INFERENCE]. Ratings Baa2 negative, BBB− stable, BBB stable, November 2 [FILE] | ORCL's −8.8% on November 2 moved CDS only about +7 | Present, slow, not the daily driver |
| **Sector tape** | October 16 to 20 Oracle +52, CoreWeave upfront 15.9 to 18.8 points, Meta 105 to 111 [October 19 to 20], Amazon 76 to 81 [FILE] | Daily HY explains little, below | Real, partial |

**How much the daily tape explains [FILE, my regression].** Daily change in 5Y conv median on ORCL's return and HY's change, roll days skipped:

| Window | n | R², stock | R², HY | R², both |
|---|---:|---:|---:|---:|
| December to August | 154 | 0.09 | 0.16 | 0.20 |
| September to November | 43 | 0.18 | 0.25 | 0.29 |

About 70% of daily moves are not explained by Oracle's stock and the index together [INFERENCE from the fit]. That residual is where name-specific financing and hedging flow would sit, but it also holds noise from thin prints, so it is not a measure of hedging.

**Cannot see:** counterparties and direction; net or gross positions (DTCC's weekly Trade Information Warehouse data was not tested today); dealer inventory; loans and their hedges; Oracle-linked project debt prices; swap spreads; TRACE trades; anything before December 2025 on this basis.

## 3. Oracle bonds against CDS since the $20B closed

Method: State Street SPIB and SPBO holdings, as of November 5, market value over par [FILE, evaluated fund marks, not trades]. All five new notes are held, with identical marks where both funds overlap. Spread is yield less the interpolated Treasury CMT for November 5 [FILE]. Reoffer and pricing spreads from the November 2 term sheet [FILE].

| New note | Reoffer | Nov 5 mark | Change, points | Pricing spread | Nov 5 spread | Change, bp |
|---|---:|---:|---:|---:|---:|---:|
| 7.000% 2029 | 99.835 | 100.535 | +0.70 | +240 | +228 | −12 |
| 7.450% 2031 | 99.942 | 100.206 | +0.26 | +275 | +281 | +6 |
| 7.850% 2033 | 99.995 | 100.894 | +0.90 | +305 | +298 | −7 |
| 8.000% 2037 | 99.916 | 100.331 | +0.42 | +310 | about +310 | about 0 |
| 8.650% 2046 | 99.840 | 100.594 | +0.75 | +335 | +332 | −3 |

**So what.** All five notes stood above reoffer the day ORCL closed at 115.16, 0.7% under its offering price, and HY widened 16. Over November 2 to 5, 5Y CDS rose about 10 on conv medians (294 to 304), while the closest bond, the 2031, widened 6 and the others held or tightened. **Cash held better than CDS** [FILE; INFERENCE on meaning]. That leans toward a CDS bid rather than cash selling, on one date.

| Oracle 5Y date | Bond spread over Treasuries | CDS | CDS less bond |
|---|---:|---:|---:|
| February 2, pricing | +115 | about 127 | about +12 |
| November 2, pricing | +275 | about 294 | about +19 |
| November 5, mark | +281 | 305 | about +24 |

⚠️ **This is not a true basis.** CDS is priced off swaps, not Treasuries, and swap spreads are unreachable here. If 5Y swap spreads are negative, the real gap is smaller by that amount and could be near zero. The direction of the gap is usable, the level is not [INFERENCE]. Also: one date of marks; marks are vendor-evaluated; maturities differ slightly, November 2031 against December 2031; accrual treatment for older bonds is unverified, so I do not use them here.

Earlier-dated fund files are not available, so I cannot draw a daily line since November 4. The State Street file as of November 6 should post next business day, and that is the first real second point.

## 4. Does Microsoft's reassessment show in CDS?

**Barely, and only in Oracle.** Timing: ORCL's largest five-minute drop came at 17:35Z, 12:35 ET, 116.47 to 109.21 [FILE, Yahoo bars]. That this was the Bloomberg report is my inference; I have no timestamp for the report. Bloomberg's body is unread and Reuters' account of the larger reassessment is a relay of it [RELAY].

| Name, Dec 2031 | Before 12:35 ET | After | Read |
|---|---|---|---|
| Oracle | 306 conv, 14:41Z and 17:18Z | 305 at 17:37Z inside a curve package; 312 to 314 conv from 19:31Z | **+6 to +8**, and not at once |
| Oracle stock | 116.47 | 109.21 low, 115.64 at 20:46Z, Yahoo intraday | Most of the drop reversed |
| Microsoft | No November 6 print through about 15:50 ET; about 53 disseminated [November 4] | | **Cannot show anything yet** |
| Meta | Upfront 0.45 November 5 | 0.45 November 6 | Flat |
| Amazon, Alphabet | 0.17, 0.48 | 0.22, 0.53 November 6 | Small, direction not signed |
| CoreWeave | 21.86 points November 5 | 20.6 November 6 | Tighter on the day, time-of-day not tested |

All November 6 figures are same-day slices, thin, and can be corrected in the full file. So the market treated it, so far, as one Oracle contract and not a sector funding shock [INFERENCE]. **It does not test the wider reassessment.** A review with unknown size and direction would show later, if at all. Card 034's warning stands: do not read this as a contained older-chip event.

## 5. SoftBank's 466 bp

| Item | Finding |
|---|---|
| Source | Reuters, "as high as 466 bp, widest since October 2022", Markit, via WALTER card 003 [RELAY]. Reuters page returned 403 to SAM, so currency and whether it is a close or intraday high are **not established** |
| What DTCC holds | SoftBank single-name is **yen**: 575 of 589 trades. The last dollar rows are October 2 and 9, on shorter maturities, Dec 2027 and Jun 2028 [FILE] |
| Disseminated, yen, Dec 2031 | 458 [October 26], 435 [October 30], 438 [November 4] [FILE] |
| November 6 | One print, 08:39Z, 14.77 points upfront against 14.24 at the 438 print. My estimate about 451 [INFERENCE, scaled from November 4; the raw conversion of 468 runs high, and I have no row carrying both figures to calibrate it] |

**Can the two be compared? Level no, direction with care.** They differ in currency, in contract terms and likely recovery convention, and in trading hours, Tokyo against New York [INFERENCE on terms; FILE on currency and times]. A yen contract is expected to differ from a dollar contract on the same name, so 466 and 451 need not conflict.

Direction: Oracle peaked October 20 and SoftBank's disseminated high came October 26, so the same fortnight. Weekly changes correlate +0.34, n=38, on thin SoftBank data [FILE, weak]. **Sequence matters:** SoftBank's November 6 print was at 08:39Z, about 8 hours before ORCL's drop. So its widening that day follows the November 5 selloff and Tokyo's −5.96% session, not the Microsoft report [FILE on times; INFERENCE on cause].

## 6. What would prove a funding link

A shared tape is not a link. Proof means the same dollars. **Any one of these would count:**

1. A named filing showing SoftBank or OpenAI deferring or shortening a payment to Oracle.
2. Oracle disclosing a prepayment or vendor-financing shortfall tied to a named customer contract.
3. A named lender cutting, repricing or hedging both Oracle-linked project debt and SoftBank credit, on primary evidence.
4. CDS moving together on a SoftBank-only or Oracle-only funding event, with the AI tape flat that day.

**Would weigh against:** SoftBank's next yen retail bond clearing at a normal coupon; Oracle's remaining performance obligations intact with prepayments on schedule.

| Date | Test | Owner |
|---|---|---|
| Tonight, about 20:15 ET | DTCC November 6 full file: Oracle and Microsoft | LIQUID |
| About November 9 | State Street file as of November 6: new notes against reoffer, the second bond point | LIQUID |
| November 10, 01:30 ET | SoftBank results. ⛔ Headline leverage is as of September 30, not today's (card 036) | SAM |
| About November 13 | W1 as-of November 10, first print able to show a cover after November 5 | LIQUID |
| November 19 | ING data-centre loan bids [RELAY] | WALTER, LIQUID |
| Mid-December, not set | Oracle Q2 FY27 results and 10-Q: remaining performance obligations, prepayments, vendor financing. Any public raise beyond the pledge | VULCAN, LIQUID |
| December 31 | IREN GPU 2.0's undrawn $1.5B lapses [FILE]; a Microsoft-linked funding test | VULCAN, LIQUID |
| About January 1, 2027 | Oracle's 60-day company lock-up ends [FILE] | LIQUID |
| Late January, not set | Microsoft 10-Q: commitments and leases not yet commenced | VULCAN |

## 7. Corrections to my own record

| Where | What it said | Now |
|---|---|---|
| `REPORT.md` §15.8, STATUS §3, NEXUS brief, PROME W1 packet, WALTER packet, hence card 037 | "3.25%" unsupported through November 5 | **Wrong.** Tested only November. 5Y traded through 325 on October 20, disseminated 342.5 |
| Same | Sized CDS against 288 as the prior high | 288 is a vendor close on a different basis; DTCC high is 342.5 |
| Card 037, carried from me | "'Record' is not established either way" | Still true for all history. On the DTCC window, October 20 is the high, so November 5's 305 is not a record |
| `dtcc_cds_probe.py` | Reads NEWT only | Does not remove cancelled rows, and mis-scales or mis-signs some names. November 5's published range is unaffected: the one cancelled 309 had a live duplicate. Logged at KB-LIQ-150; tool fix owed |

## 8. Gates

No gate, band, score or letter moved, and none requires it. 069: L2 reads CoreWeave only, no Oracle line; L5 needs a rating action, none seen after November 2. 072: Oracle is the issuer already scored, so 342.5 is no new instance. 076, 079, HY-REKILL: unaffected. No gate letter keys on Oracle's CDS level. No card or position view here; TERRY owns those.

## Method notes

Scripts: `pull.py`, `ser.py`, `hist.py` here. Same-day DTCC slices (`ppd/api/report/intraday/sec/SEC_SLICE_CREDITS_YYYY_MM_DD_N.zip`) and the ticker are free and no-login, so a same-day read does not have to wait for 20:15 ET. Microsoft and other names below the 100 bp coupon must be read from disseminated rows: the conversion flips sign (KB-LIQ-150). SoftBank needs a yen discount rate, and some rows quote spread in bp, not decimals.
