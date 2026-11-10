# SoftBank Group credit leg — PROME investigation, November 10, 2026

**Asked by:** PROME prome-07, 17:19 ET 11/10, on Will's word 17:18 ET ("direct and orchestrate the investigation into softbank"). **Owner of this leg:** LIQUID (credit pricing, ratings, yen retail channel, AI-HY read-through, margin-loan terms where a source states them). **Not mine:** SoftBank's documents, leverage and loss bridge (SAM, `AGENTS/SAM/research/outputs/2026-11-06_softbank/`); the Ohio project and AI chain (VULCAN). **Limits:** $0; no threshold, gate letter, band or card changed. Started 17:19 ET (`date`).

**Timing that governs every "before and after":** results posted about 01:30 ET 11/10 (SAM), which is 15:30 JST, the Tokyo close. The Tokyo close of 11/10 (9984.T ¥3,872, +13.88%) is therefore **before** the results. The first Tokyo session after them opens 19:00 ET tonight. US trading on 11/10 is the only full session after the results that has closed.

## 1. Credit default swaps and bonds

### 1a. SoftBank Group 5-year CDS: DTCC public dissemination (SEC regime), $0

Source: DTCC PPD `SEC_CUMULATIVE_CREDITS_YYYY_MM_DD.zip`, 71 business-day files 8/3 → 11/9 read 17:20 ET 11/10; reference entity "SoftBank Group Corp." (RED JQCEFX). Every 5-year print is **yen-denominated, 100 bp coupon**, on BILT, UTSL or TSAD. Most rows carry an upfront, not a spread.

**Conversion and its check.** The upfront is converted with a flat-hazard approximation, **not the ISDA model**. The desk probe's default (rate 4%, recovery 40%) reads about 30 bp high on yen contracts. Re-run with **rate 1% (yen), recovery 40%**, it lands on the independent figures:

| Date | Converted (r 1%, R 40%) | Independent figure | Gap |
|---|---|---|---|
| 11/4 | 438 (one UTSL print) | 438 disseminated spread, same day (DTCC) | 0 |
| 11/6 | 470 (one UTSL print) | 466 Reuters, 462 Markit (secondary relays of both; Reuters piece not read) | +4 / +8 |

Good to about ±10 bp, not to one. Probe default figures (r 4%) are in the scratch log only and are not used.

**On-the-run 5-year (June 2031 contract before the 9/21 roll, December 2031 after):**

| Month | Prints | Low | Median | High |
|---|---|---|---|---|
| August | 27 | 325 | 347 | 364 |
| September | 21 | 343 | 360 | 390 |
| October | 18 | 378 | 394 | 456 (10/22) |
| November 2 to 9 | 12 | 434 | 496 | 513 |

**Daily, last week before results:** 11/2 434 · 11/4 438 · 11/5 448 · 11/6 470 · **11/9 496 to 513, median 497 (7 prints, 02:57Z to 07:45Z)**.

**Read:** the 11/9 prints are the widest of the 71-file window, about 150 bp over the August median, and widened about 27 bp from 11/6 to 11/9. All of it came **before** the results. **After the results:** the 11/10 file publishes about 20:15 ET; §1d.

⚠️ Limits: DTCC disseminates only trades with a US-person reporting nexus. Most SoftBank CDS trades in Tokyo and Hong Kong between non-US dealers and do not appear. This is a sample of the market, not the market. One 10/20 pair disseminated "0.0357" on the June 2031 contract (357 bp) at the same minute; it is out of line with the converted prints either side (442, 456) and is not used.

### 1b. Dollar bonds

**No free primary price reached.** TRACE (FINRA) is unreachable from this box, and SoftBank's dollar notes are 144A/Reg S. Secondary only: Bloomberg, 11/6 (headline and snippet, article not read): SoftBank "led declines in Asian dollar bonds"; its **2032 notes fell 1.5 cents, a record drop**; insuring its debt cost the most in four years. **No report of a dollar-bond move on 11/10 after the results was found** (searches 17:2x ET).

### 1c. Yen bonds

**Not reached tonight.** JSDA's daily OTC reference prices (`market.jsda.or.jp/en/statistics/bonds/prices/otc/`, files `ES261110.csv` and earlier) returned **HTTP 429 Too Many Requests** to every request from this box from 17:22 ET. Spacing requests 20 seconds apart did not clear it. I did not try to get around the block. Even when reachable, the 11/10 file prices quotes at 15:00 JST, **before** the results. The first after-results yen read is the 11/11 file, published about 04:30 ET 11/11.

## 2. Ratings: no action found since the results

| Agency | Rating | Last action | Source, read 17:2x ET 11/10 |
|---|---|---|---|
| JCR | **A / Negative**, J-1; subordinated BBB+ | Affirmed 4/30/2026. Bond assignments 7/29 and 9/4. **Nothing after 9/4** | JCR rating page (EN and JP), primary |
| S&P | **BB+ / Negative** | Outlook to negative from stable on 3/3/2026 (OpenAI investment); S&P's path back runs through asset sales to bring adjusted LTV under 35% | Bloomberg and MarketScreener relays; SoftBank's IR ratings table (as of 9/11, per search summary; page body did not render). S&P's own text not read |
| Moody's | Ba2, **unsolicited** (upgraded from Ba3 Sept 2025, outlook stable) | SoftBank published a "Comment on Moody's Release Related to Unsolicited Ratings" on 8/28/2026; **its content did not render and is not read** | SoftBank press page; Moody's news 450633 |

At 17:2x ET 11/10 it is 07:2x JST 11/11, before Tokyo business hours. A JCR or S&P comment on the results would most likely come in Tokyo hours.

## 3. Yen retail bond channel: no pulled or repriced deal found

| Deal | Terms | State |
|---|---|---|
| 70th unsecured ("Fukuoka SoftBank Hawks Bonds") | **¥1T**, 7-year, **4.75%** (indicated 4.3 to 4.9%, set 9/4, near the top), subscription 9/7 to 9/16, paid 9/17 | Sold out (by 9/11, retail site). SoftBank's Q2 deck calls it a ¥1T retail bond **record** (SAM's grade) |
| Hybrid 9th | ¥260B, 35NC5, 5.12%, BBB+ (JCR), June 19 | Sold out |
| Hybrid 8th | April, 4.97% | Issued |

**No November deal, postponement or repricing found** (Japanese and English searches 17:2x ET; one retail listing site guesses the next domestic retail deal for spring to summer 2027, unsourced). The retail channel's last read is demand, not withdrawal. **Not read:** retail-bond secondary prices (JSDA blocked, §1c).

## 4. Read-through to AI-HY cohort and gate 069 (observations only; no leg re-graded)

| Name | 11/9 | 11/10 (US session, after results) | Source |
|---|---|---|---|
| SoftBank 5Y CDS | 497 median | 11/10 file pending (§1d) | DTCC, converted |
| Oracle 5Y CDS (Dec 2031) | **301.5 disseminated** ×2; 305 converted | pending | DTCC 11/9; 11/6 was 305 disseminated |
| CoreWeave 5Y CDS (Dec 2031, 500 coupon) | **about 1,136** (one 19:59Z print) | pending | DTCC 11/9, probe conversion (r 4%; USD); 11/6 about 1,227 to 1,252 |
| IREN | −1.06% | **−7.85%** (19.73) | yfinance raw close |
| NBIS | +9.24% | −5.27% (134.00) | same |
| CRWV | +5.56% | −0.51% (48.73) | same |
| APLD | +7.52% | −0.24% (16.68) | same |
| ORCL | +3.18% | −1.51% (117.98) | same |
| ARM | +6.69% | −2.58% (**181.49**) | same |
| SFTBY (US ADR) | +2.35% | **−4.00%** (11.27) | same |
| HYG / JNK | +0.36 / +0.33% | −0.43 / −0.41% | same |

**Read:** from 11/6 to 11/9 SoftBank's CDS widened about 27 bp while Oracle's was flat (305 → 301.5) and CoreWeave's tightened about 100 bp. **That is SoftBank-specific credit, not the AI cohort.** On the first US session after the results, the cohort fell modestly: no name came near 069 L4's −15% line (worst IREN −7.85%). HY's 11/10 move is not published until 11/12 (11/11 is a bond holiday); **069 L4 for the 11/10 session grades then, under its own rule, not here.** No 069 leg is touched by this read.

## 5. Margin loans and asset-backed financing on Arm, T-Mobile and SoftBank Corp shares

SAM holds these from SoftBank's own filings; cited, not re-derived (`SOFTBANK_FUNDING_STACK.md` lines 24 to 26; `2026-11-10_RESULTS_GRADE.md` §6 line 5):

| Facility | Size | Collateral, recourse | Maturity | Stated margin-call terms |
|---|---|---|---|---|
| Arm margin loan | **$25B** facility (upsized +$5B, agreement Sept 2026), drawn about **$24.8B** at 9/30 (¥3.90T); 41 institutions | Arm shares; non-recourse. 769M pledged as of May, 83% of 923M held (relay; not re-read at 9/30) | 2 years plus a one-year extension option, so about 9/2028 (SAM; corrects the 9/2027 relay) | **Not disclosed** |
| SoftBank Corp margin loan | ¥1,197.0B; $7.4B facility; 26 institutions | SoftBank Corp shares; non-recourse | not read | **Not disclosed** |
| T-Mobile collars | ¥265.6B | T-Mobile shares; non-recourse; T-Mobile's value nets to zero in SoftBank's LTV ("collared out") | not read | Collar strikes not read |
| SVF2 OpenAI-shares loan | ¥1,543.7B ($10B) outstanding, guaranteed by SBG | OpenAI shares **not pledged**; margining references OpenAI's fair value | not read | **Undisclosed trigger on an unlisted mark** |

**Arm price that stresses:** SAM's arithmetic puts SoftBank's own LTV at 25% (its normal-times ceiling) at **Arm $145**, and 35% (S&P's stated line) at about **$44**. Arm's raw close 11/10 is **$181.49**, 25% above $145. No source I reached states a loan-to-value or price at which the Arm lenders call margin.

## 6. Known-unknowns

1. **After-results CDS:** DTCC 11/10 file (about 20:15 ET); then Tokyo-hours prints 11/11. Most of the market does not disseminate.
2. **After-results bond prices, dollar and yen:** no free primary. TRACE unreachable; JSDA rate-limited this box (HTTP 429); first after-results JSDA file 11/11.
3. **Rating comment:** JCR and S&P act in Tokyo hours; none found by 07:2x JST 11/11. S&P's own March text and Moody's August release not read.
4. **Margin-call levels** on the Arm, SoftBank Corp and SVF2 facilities, and **T-Mobile collar strikes**: not disclosed in anything reached.
5. **Whether the 11/9 CDS widening was positioning ahead of results** or a reaction to 11/6 bond losses: the data cannot say.
6. The relayed claim that the remaining $6.5B of the equipment order was Nvidia GPUs redirected to Oracle (card 010, @rdd147): no source; not mine to chase (VULCAN).
