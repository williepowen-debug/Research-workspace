# BROCK private-credit read, 2026-11-05 selloff

**Written:** 2026-11-05 13:4x ET, first cut. **Marks:** intraday, fetch.py and yfinance, read 13:26–13:30 ET, root rule #4. These are not closes. **Assignment:** PROME packet, Will 13:25 ET ("open BROCK and launch TERRY"). No trade, no threshold change. No score moved: convergence stays 58/70.

## 1. What today's move says

**The tape does not show a private-credit event. It shows the market falling and these names falling with it, the listed lenders by less than the market.** Cause is not established.

| Name | Prior close | Last | Day % | Session low % | Beta-implied % | Residual pp (σ) |
|---|---:|---:|---:|---:|---:|---:|
| APO | 122.76 | 116.98 | −4.71 | −6.42 | −4.11 | −0.74 (−0.4) |
| ARES | 136.85 | 131.01 | −4.27 | −5.20 | −5.80 | +1.61 (+0.7) |
| BIZD | 12.66 | 12.44 | −1.74 | −2.09 | −1.59 | +0.01 (0.0) |
| ARCC | 19.46 | 19.16 | −1.57 | −1.88 | −1.95 | +0.43 (+0.4) |
| OBDC | 10.76 | 10.63 | −1.21 | −1.95 | −2.49 | +1.33 (+1.0) |
| FSK | 11.46 | 11.55 | +0.79 | 0.00 | −1.67 | +2.45 (+1.3) |
| *OWL* | 10.65 | 9.85 | −7.46 | −8.81 | −5.63 | −2.16 (−0.8) |
| *CG* | 42.75 | 40.13 | −6.13 | −9.12 | −5.04 | −1.42 (−0.7) |
| *SPY* | 766.81 | 736.07 | −4.01 | −4.25 | | |
| *HYG* | 77.52 | 77.15 | −0.47 | −0.50 | | |

Day % = first read 13:26–13:27 ET (fetch.py). Beta-implied and residual = OLS on HYG+SPY, 250 sessions ending 5 sessions before the window, read ~13:30 ET, so the two columns are about three minutes apart. No ex-dividend found since 10/15 in the vendor's dividend history for these tickers.

| Reading | Figure | So what |
|---|---|---|
| Wrappers ARCC·FSK·OBDC·BIZD | −0.87%, residual +1.05pp (+0.9σ) | Fell less than their betas imply |
| Same, without FSK (its earnings are in the print) | −1.42%, residual +0.59pp (+0.5σ) | The conclusion survives removing FSK |
| Managers APO·ARES | −4.52%, residual +0.43pp (+0.2σ) | On beta, nothing specific |
| Managers minus wrappers, raw | Managers fell 3.65pp more | Wrong sign for "wrappers lead down" |
| Since Tue 11/3 close | Wrappers +1.59%, managers +2.28%, SPY −2.38% | All six names sit above Tuesday's close. Today hands back part of Wednesday's bounce (APO +8.1%, ARES +6.1%, ARCC +2.4%, OBDC +2.5%, BIZD +2.1%) |
| The one prior SPY ≤−2.5% day in 250 sessions, 6/5 (−2.58%) | Wrappers −1.79%, managers −2.01% | Today's split between the baskets is much wider; n=1, so no pattern |
| FSK path | Open 11.97, high 12.63 (+10.2%), now 11.55 | Earnings gap almost entirely faded into the tape |

⚠️ One intraday session. Every residual is inside about 1.3σ, so "fell less than beta" is a weak claim on its own. The stronger claim is the absence: nothing here singles out private credit. OWL and CG are the two weakest of the complex and both are within 1σ. **GS −6.5% and MS −6.4% are also on beta (−0.3σ and −0.5σ).**

**Cash HY for today does not exist yet.** LIQUID's last grade, 11/4 first-published: HY 332, BB 199, B 351, CCC 1,297, tier rule REVERSES. That print predates today. Reconciled, not re-graded. HYG −0.47% and BKLN −0.61% are ETF proxies, not spreads.

### X1, my own grade: NOT MET, wrapper half NOT ARMED, unchanged

| Leg | State | Basis |
|---|---|---|
| HY sustained | MET | LIQUID's count: strict >280 ×3, and its >320 run at 5 observations through 11/4. Cited, not graded |
| Wrapper leads down | **FAILS** | Today the managers led down by 3.65pp raw. On the last widening, 10/27 → 10/30 (HY 318 → 344), both baskets ROSE: wrappers +2.87%, managers +3.13%. Wrappers lost 0.27pp to managers raw, 1.67pp on residuals, on a rally, so that is not "leads down" |
| CCC/BB rising during a widening | **FAILS** | 7.06 [10/27] → 6.35 [10/30], BB-led (BB +22bp, CCC +6bp). 6.52 [11/4]. LIQUID's series, my ratio |
| Test (a), wrapper marks falling more than manager marks | NOT SHOWN | Six Q3 wrapper NAVs on my register or LIQUID's card: −1.10% to +0.9%. No manager comparator exists |

X1 stays CLOSED / DON'T-SIZE. The candidate X1-R stays unregistered (L587, PROME's). Its CCC/BB condition fails on the only new qualifying window, so it would not fire there.

## 2. What is graded on my board: nothing changed on today's tape

Changes since 11/02 came from filings, not from the price move.

| Row | State | Evidence |
|---|---|---|
| Convergence | **58/70, no rescore** | All below |
| EXIT §1 thesis kill | NOT FIRED | See the Proskauer flag in §5 |
| EXIT §2 BDC median discount <10% | NOT MET | 27.65% intraday, 39 names, mixed vintages (19 NAVs at 9/30, 19 at 6/30, one 8/31) vs 28.68% [10/30 closes] on an older mix. No trend claimed |
| EXIT §3 | 2 of 3, unchanged | No downgrade |
| NAV discount next level, >35% sustained | Not reached | 11 of 39 above 35%; FSK 36.6%, OBDC 25.6% |
| GATE-BRK-R2 | FIRED ×2, unchanged | BCRED Q3 final 49.9%, (b) NOT FIRED. Next read BCRED Q4 letter ~12/04, not ~12/03: offer expires 12/1 11:59 pm ET and the Q3 letter came +3 days after expiry. INFERRED; read from the feed. GCRED below 5%, 100% honored, is a counter-datum outside the population |
| Ladder row 1, APO | Unchanged | $116.98. Below $130, far from $145. The $100 all-desk alert is 14.5% away |
| Ladder row 6, >5% quarterly NAV markdown | NOT FIRED so far in Q3 | Worst filed BXSL −1.10% |
| **Ladder row 10, VIX +3 without HY widening** | **OPEN until the 11/5 HY cell, about 10:30 ET 11/06** | VIX ~26 vs 16.61 [11/4]. Whether HY widened is LIQUID's print. The row has no numeric definition of "widening" and I do not invent one. Owner HENRY/VIOLET; BROCK only routes |
| W3 FSK leg (11/30) | **NOT REVERSED on Q3** | Ex-waiver coverage 0.95x, §4 |
| PIK vector | 🟠(3) held | Every measured name below 20% of TII |
| Blue Owl liquidity | 🔴🔴(5), at ceiling | OTF NII below dividend, no cut declared, §4 |
| Default rates | 🔴(4) held | See note below |
| BRK-25 / BRK-31 | Unchanged | Count 2 / no fire. An Arini reported sale is not a print |
| BRK-26 | OPEN, SQN does **not** resolve it, §6 | |

**Default-vector note, flagged:** the next-level line reads ">7% Q2 at a non-CDLI top-tier name". Today's FSK release gives a primary Q2 figure of 7.1% non-accrual at cost. I do not apply it: FSK is junk-rated and sits on the fragile side of my own bifurcation, not the top tier, and non-accruals at cost are not a default rate. That is a reading of my own line in the conservative direction. It goes to the next VX review.

## 3. CRMT, DOCKET L915: A TENTH BRIDGE

**Graded at primary.** Feed read 13:26:50 ET (submissions JSON + browse-edgar Atom, two sources agree) and again 13:28.

| Field | Reading |
|---|---|
| Filing | 8-K 0001171843-26-007147, accepted 2026-11-05 08:00:41 ET (index page), period 11/04, Item 1.01 only, no exhibit beyond XBRL cover |
| Text | "On November 4, 2026, the Agent and Lenders agreed to further extend the Scheduled Termination Date and the temporary relief with respect to the minimum liquidity thresholds and minimum Collateral Coverage Ratio through November 9, 2026." |
| New STD | **Mon 11/09, +5 days** from 11/04, agreed on the deadline day itself |
| Absent | No 2.03 new money, no amendment exhibit, no sale agreement or RSA, no 1.03 petition, no 2.04 acceleration, no 8.01 strategic-alternatives paragraph (third straight 8-K without it; absent, not retracted) |
| Other filing since 11/02 | Form 4, 11/03: director Welch, in-kind partnership distribution, no consideration. Not a sale into the market |
| Ladder | 9/7 → 9/11 → 9/18 → 9/24 → 10/1 → 10/8 → 10/15 → 10/22 → 11/01 → 11/04 → **11/09**. Tenors 4, 7, 6, 7, 7, 7, 7, 10, 3, 5 days |

Reading: same lender, same relief, and two of the three shortest rungs back to back. A short leash is consistent with a near decision, INFERRED, not graded. CRMT $1.37, +8.7% on 166,000 shares on a −4% tape; I can't tie it to a cause.

**Backstop #6 (L916), any OTHER agreement dated ≤11/01:** nothing through 13:28 ET, but the window runs to EDGAR's cutoff tonight. Provisional; final after 17:30 ET. Silence grades nothing.

**Owed, PROME registers:** STD Mon 11/09 read, and Item 1.01 backstop #7 for any agreement dated ≤11/04 by Tue 11/10 (Thu 11/05, Fri 11/06, Mon 11/09, Tue 11/10). No capital path.

**CABO L876:** not yet in. Newest filing is an 8-K 10/30, Item 5.02. Q3 results come after today's close; I read them when they land. CABO $5.20.

## 4. Q3 filings since 11/02: what was learned

| Name | NII / regular dividend | NAV | Non-accrual cost / FV (Q2) | PIK % TII | Notes |
|---|---|---|---|---|---|
| **FSK** 11/05 | $0.46 / $0.44 = 1.05x reported; **0.95x ex-waiver** | 18.30 → 18.28 | 6.4 / 3.4 (7.1 / 3.8) | 15.6 (non-cash 17.3) | Waiver $12M. Net debt/equity 125% from 122% |
| **OTF** 11/04 | $0.29 / $0.35 = **0.83x** | 16.48 → 16.62 | **1.8 / 1.1 (0.6 / 0.1)** | 11.5 | $0.35 base declared again, no cut. $55M buyback. Spillover $0.35/sh |
| **OBDC** 11/04 | $0.33 adj / $0.31 = 1.06x | 14.26 → 14.32 | 2.9 / 0.8 (2.8 / 0.8) | 9.8 | "No new issuers added to non-accrual" |
| **BXSL** 11/04 | $0.68 / $0.77 = **0.88x** | 25.53 → 25.25 | 2.8 / 2.1 (3.6 / 1.8) | 5.8 | NII $0.75 in Q2, $0.82 a year ago. $0.77 declared again |

Sources: FSK 10-Q 0001628280-26-070499 + Ex 99.1 0001104659-26-123011 · OTF 10-Q 0001747777-26-000036 + 8-K -000037 · OBDC 10-Q 0001655888-26-000069 + 8-K -000070 · BXSL 10-Q 0001736035-26-000020 + deck 0001213900-26-115721. BXSL Q2 cost figure is my register, the rest are from these filings.

**FSK coverage is thinner than the headline.** $127M NII includes the $12M adviser waiver: ex-waiver $115M ÷ 276.27M shares = $0.416, 0.95x. ⚠️ It also includes a lumpy affiliate dividend: non-controlled affiliated dividends were $28M in Q3 against $2M in H1, and Belk common shows $24.9M year to date. If most of that fell in Q3 (INFERRED from the line's jump), ex-waiver and ex-Belk is about $0.33, about 0.74x. **W3's FSK leg is "ex-waiver coverage BY EARNINGS": not reversed on Q3.**

**FSK's FV/cost rise to 0.9101 is partly composition.** Q3 net realized loss on non-controlled unaffiliated was $133M, which takes cost down.

**Kellermeyer, the owed FSK read:**

| Tranche | 6/30 par / FV | 9/30 par / cost / FV | FV/par |
|---|---|---|---|
| First lien A, SF+5.3 PIK | 229.6 / 226.0 | 207.0 / 204.8 / 207.0 + 27.5 / 27.2 / 27.5 (new row) | 98.4 → **100.0** |
| First lien B, SF+8.0 PIK, non-accrual | 107.9 / 10.9 | 111.2 / 94.4 / 4.5 | 10.1 → **4.0** |
| Preferred / common | 0 / 0 | 48.3 cost / 0 | 0 |

$ millions. Total cost $374.7M, FV $239.0M, shortfall $135.7M (from $132.5M). A did not follow B: A went to par while B halved. Income YTD on A: $0.8M interest, $15.7M PIK (H1 was $0 and $10.7M), so Q3 shows about $0.8M non-PIK, the first on my record, and I can't say it was cash. ⚠️ The new $27.5M row looks like a $28.6M carve from A, INFERRED from the affiliate table; the amendment wasn't found. Whether A still counts as "performing" collateral at the facility remains UNKNOWN. Senior revolver $607M drawn / $3,134M available (6/30 $733M / $3,017M), less $50M letters of credit. Retained lender shares still UNKNOWN. No filing states Kellermeyer's collateral contribution.

**OTF non-accruals tripled while NAV rose.** Signifyd preferred, $158.7M cost, $122.9M FV, 77% of cost, 1.6% of net assets, carries the non-accrual footnote at 9/30 and was accruing at 12/31. That single line accounts for most of the FV jump, INFERRED from sizes. Pluralsight stays on non-accrual, $64.8M cost, $25.3M FV. OTF's CEO attributes the NAV rise to improving software sentiment.

**The "13% TII vs ~25% NII" denominator hypothesis: SUPPORTED.** OTF Q3 PIK interest $24.9M + PIK dividend $14.3M = $39.2M. That is 11.5% of $341.3M TII and 29.5% of $132.7M pre-tax NII. Same dollars, two ratios. The complaint's figure and my register's figure are not in conflict.

**CoreWeave DDTL, the standing watch and WALTER's action:** the delayed-draw loan is now in four BDC schedules at 9/30.

| Holder | Facility | Size |
|---|---|---|
| OBDC | CoreWeave Financing DDTL V-V, first lien, S+5.50, 9/2031 | $8.97M funded, $8.53M cost, **$9.03M FV (100.6)**, $6.03M unfunded, draw period to 12/2026 |
| OTF | Same, identical size | Same |
| PSBD | DDTL V, S+5.50, 9/1/2031 | $1.11M unfunded; funded size not extracted |
| GECC | DDTL V, S+4.50, 11/14/2031, **plus** CoreWeave Inc. 9.63% unsecured 7/2032 | Size not extracted |

So what: small, about 0.06% of OBDC's and OTF's portfolios, marked above par on a date before the bonds fell to about 79. Those are bookmark-screenshot prices, vendor unseen, 11/4. The 9/30 mark predates the move and tells nothing about today. Not in FSK or BXSL 10-Q text; absence elsewhere is not certified, since 10-Qs are still arriving. Lender exposure at the banks: not read.

**Apollo Q3:** GAAP loss $1.057B; issuer attributes it "primarily" to unrealized mark-to-market losses in Retirement Services "resulting from higher interest rates". The reconciliation line is $2.661B investment losses net of offsets. Net spread 1.06% vs 1.24% a year ago; ex-notables 1.14% vs 1.21%. ⚠️ That attribution is the issuer's. Nothing here separates rate marks from credit losses, and I do not assign it.

**BCRED Q3 final, at primary:** 181,287,647 shares tendered, 90,421,325 accepted, 49.9%; $2,125,805,358 at $23.51; $2,125,655,078 paid on or about 10/28 in non-interest-bearing notes (SC TO-I/A 0001213900-26-114678). Q4 offer up to 87,457,414 shares, 5% of 1,749,148,293 at 9/30, priced at 12/31 NAV (SC TO-I 0001193125-26-442721). ⚠️ My own miss: both were accepted 11/02 about 08:01–08:13 ET and my STATUS kept saying no Q3 dollar figure existed. WALTER 032 caught it. L270 is overtaken.

**Fed SLOOS, as carried by WALTER 031, not re-read:** tighter standards for every NDFI type queried; demand from business credit intermediaries and PE funds stronger, citing liquidity needs among others. Table 1 unread. No bank, no reserve, no BRK-31 event.

**Fitch PCDR Q3, reconciled at a secondary:** 6.3% TTM, record quarterly basis, from 6.0% Q2, flat on August. 27 events from 20 new unique defaulters, TTM 91 vs 84. 13 deferral/PIK, 10 stressed extensions, 1 uncured payment, 3 bankruptcy/liquidation. Software lowest at 0.6%. ABF Journal 10/30, read. ⚠️ **WALTER 20261104-028 reads "27 quarterly events versus 20"; ABF says 27 events FROM 20 new defaulters, same quarter. Not a comparison.**

## 5. Learned vs merely dated today

| Learned, changes what I believe | Dated today, changes nothing |
|---|---|
| CRMT rolled again, to Mon 11/09, with no new money | Today's price move in all six names |
| OTF non-accruals 0.6% → 1.8% of cost; NII 0.83x | HY 332 / REVERSES [11/4]: print predates today |
| FSK coverage 0.95x ex-waiver; W3 leg not reversed | VIX, gamma, circuit-breaker talk: HENRY/VIOLET |
| Kellermeyer B 4¢, A at par, a Q3 non-PIK line appears | Ueno, Peña: no channel to my book established. $17.9M N-PORT holdings are REGINALD's |
| BXSL coverage 0.88x; NII $0.82 year ago, $0.75 Q2, $0.68 Q3 | Preferred, Flagstar, Citizens late loans: CRE, REGINALD's |
| The OTF PIK denominator hypothesis held | Oracle closing, Nscale unsigned, Talen, PJM, CVR: dated, no BROCK read |
| CoreWeave DDTL now sits in four BDC schedules, small |
| BCRED Q3 final 49.9%, $2.13B; R2 read ~12/04 | |
| W3 out of reach for 11/30: channels 1 and 2 cannot reverse | | Arini, Beaudry, Weil, Delaware Life sale talk: reports, no print and no realized loss |
| SQN is equipment leasing at the SEC's own words | CoreWeave Q3 date 11/10 (VULCAN) |
| Fitch composition: 23 of 27 Q3 events are deferrals, PIK or stressed extensions | GCRED below 5% for a second quarter: already my prior; a counter-datum, not new |

**Flag on the exit line:** a search summary says Proskauer's index fell for a second straight quarter, 2.51% → 2.41% (ACI 10/29, page refused, summary only, primary unread). My register has 2.73% for Q1. The kill's letter is "major private credit FUND reports default rate declining 2 consecutive quarters". An index is not a fund, so **NOT FIRED**. But STATUS said "no 2-consecutive-Q decline anywhere", and that word is no longer safe. Corrected.

## 6. BRK-26: SQN does not resolve the row

RED's quotes verified by my own page read: ¶40, ¶43, ¶¶67–71 (pages 10, 15). Row stays OPEN, 55%, search continues to 12/31.

- The SEC itself describes the class: "The majority of the Funds' assets were invested in industrial equipment leases, including through promissory notes, participation agreements, lease pools and other asset portfolios, residual sharing agreements and similar asset-backed financing investments" (¶40).
- One fund at one date reads 60% loans and notes. That does not carry four funds across 2019–2025 against that sentence.
- I do **not** need RED's Test 2. I read "on PC valuation" at fund level, so ¶68 could help me. It doesn't matter: Test 1 fails first.
- This is the Tricolor standard I set on 8/28. Counting it would resolve my own row on a subject it wasn't written about, and it would do so in my book's direction.
- Cost, stated: a miss here keeps a 55% row open with eight weeks left. If nothing else lands, it resolves FALSE.

## 7. What would establish cause

Nothing below is established today. Any one of these would move it from correlation to cause on the private-credit channel.

| Claim | Evidence that would establish it | Owner |
|---|---|---|
| Private-credit stress caused it | A primary filing: a named fund or BDC discloses a forced sale, margin call, facility default or new gate | BROCK |
| Credit transmission is live | The 11/5 tiers, about 10:30 ET 11/06: HY wider with CCC/BB UP during the widening, then LIQUID's tier rule | LIQUID |
| Wrappers leading | Wrappers' residual below managers' by ≥1σ on two consecutive widenings, CCC/BB up | PROME decides X1-R |
| Forced selling or leverage unwinding | Prime-broker or dealer statement, or an 8-K from GS or MS; loan-fund and BDC blocks at distressed prices | LIQUID / REGINALD |
| Bank exposure | Reserve build attributed to PC/NDFI at a BRK-31 bank | REGINALD |
| Mechanical index selling | HENRY's dealer positioning; would explain why credit proxies stayed calm | HENRY |
| AI-financing cause | A CoreWeave item 1.03 or 2.04, or Q3 on 11/10 showing a funding gap | VULCAN |

Two searches for 11/5 coverage returned nothing dated today. That is a limit of the search, not evidence of no news.

## 8. Limits

- Intraday marks; refresh after the close.
- FSK's 09:00 ET call not read: no transcript in hand, Quartr has no subscription.
- Software FV/par Experiment A cells for FSK, BXSL and OBDC are not done. They need a SOI parse.
- Drain: 4 top-level + 31 WALTER, 35 of 35. PROME's census was 26; five landed after it (029, 031, 032, 033, 038).
- LIQUID's four rows reconcile to mine on every cell: NAV, FV/cost for FSK, non-accrual at FV, regular dividend. Added: FSK realized-loss composition and OTF, which is not on its card.

## 9. Close addendum, written 2026-11-05 16:34 ET

**Marks:** yfinance last prices read 16:07–16:08 ET, vendor, not official closes. Will closed this session at 16:32 ET, before the CABO 10-Q and before the 17:30 ET end of the CRMT window. Both are recorded below as NOT DONE.

**The close made the intraday read stronger, not different.** SPY got worse into the bell and all six of my names got better.

| Name | Prior close | 16:07 ET | Day % | Read at 13:30 ET % | Beta-implied % | Residual pp (σ) | Since 11/3 close % |
|---|---:|---:|---:|---:|---:|---:|---:|
| APO | 122.76 | 117.31 | −4.44 | −4.71 | −4.33 | −0.11 (−0.1) | +3.31 |
| ARES | 136.85 | 133.62 | −2.36 | −4.27 | −6.02 | +3.66 (+1.5) | +3.64 |
| BIZD | 12.66 | 12.56 | −0.75 | −1.74 | −1.26 | +0.51 (+0.5) | +1.33 |
| ARCC | 19.46 | 19.35 | −0.57 | −1.57 | −1.87 | +1.31 (+1.3) | +1.79 |
| OBDC | 10.76 | 10.81 | +0.46 | −1.21 | −2.33 | +2.80 (+2.1) | +2.95 |
| FSK | 11.46 | 11.67 | +1.83 | +0.79 | −1.17 | +3.01 (+1.6) | +4.85 |
| SPY | 766.81 | 733.11 | −4.39 | −4.01 | | | −2.82 |
| HYG | 77.52 | 77.31 | −0.28 | −0.47 | | | +0.42 |

| Basket | Day % | Beta-implied % | Residual pp (σ) |
|---|---:|---:|---:|
| Wrappers (ARCC, FSK, OBDC, BIZD) | +0.25 | −1.66 | +1.91 (+1.6) |
| Wrappers ex-FSK | −0.28 | | +1.54 (+1.4) |
| Managers (APO, ARES) | −3.40 | −5.17 | +1.77 (+0.9) |

Betas are OLS on HYG and SPY over 250 sessions ending 5 before the window. OBDC at +2.1σ is the only name past 2σ, and it is one name on one day after its own Q3 print, not a basket reading.

**X1, my own grade: NOT MET. The wrapper half stays NOT ARMED.** Managers led wrappers down by 3.65pp raw; the residual spread is +0.13pp. HYG is not a high-yield print: the 11/5 HY cell is LIQUID's, about 10:30 ET Fri 11/06.

**39-name NAV discount: 26.87% at the 16:07 read** (10 names over 35%, 10 under 10%, 7 at a premium), against 27.65% intraday and 28.68% [10/30]. NAV vintages are mixed: 20 at 9/30, 18 at 6/30, 1 at 8/31. No trend is claimed. ARCC closed 0.21% above its 9/30 NAV of $19.31. Table: `data/NAV_DISCOUNT_39_close.tsv`.

**Context from WALTER, not my figures (SIG-W-20261105-055, corrected by 057):** VIX about 28.17 and VVIX 135.38, vendor 16:22 ET, Cboe history not posted. HENRY and VIOLET own them.

### L876 CABO: BLOCKED-BY-ORDER, PROVISIONAL on the 8-K only

8-K 0001632127-26-000036, Items 2.02 and 9.01, Exhibit 99.1, accepted 16:18:48 ET on the feed clock (index page not read). The 10-Q was not on the feed at my last read, 16:34 ET. It has run about an hour behind the 8-K in the last two quarters and is due Mon 11/09.

| Test on L876 | Finding | Basis |
|---|---|---|
| Close status | NOT CLOSED | Release: sufficient liquidity to pay the price "if the previously disclosed temporary restraining order entered on October 9, 2026 is dissolved" |
| Court order | Still in effect at 11/05 by the issuer's wording | Primary for the issuer's statement. The order itself is unread |
| Plaintiff | CoBank, ACB, litigation initiated 10/9 | Release, risk-factor list. First EDGAR naming I hold |
| Rescue lenders | NOT NAMED | Release says only "discussions to raise capital" and "no assurances" |
| Hearing 11/13 | Release silent | PRESS-ONLY stands (Cablefax 10/29) |
| NT 10-Q | None on the feed at the last read | 10-Q not yet due |
| Going concern | NOT in the release | It says liquidity covers the next 12 months. The 10-Q is where "substantial doubt" would sit |

**Three things are new since the Q2 10-Q:**

1. **Chapter 11 in the issuer's own words:** "it may become necessary for the Company to seek relief under Chapter 11 of the U.S. Bankruptcy Code." The Q2 10-Q has zero "Chapter 11" hits. Control: that text runs to the signature page and has 151 "MBI" hits.
2. **Insufficiency stated outright:** existing liquidity and cash flow "will be insufficient to repay the debt described above on the applicable maturity dates." Those are $22.0M MBI revolver Aug 2027, $916.2M MBI term loans 11/12/2027, the $1.25B revolver Feb 2028 ($1.05B drawn), $345.0M converts Mar 2028 and $694.3M term loan May 2028.
3. **Dissolving the order no longer means closing.** Q2 said cash and revolver capacity "will be sufficient to fund the Put Price." Q3 says payment will be coordinated with a financing that addresses at least some maturities, and that financing carries no assurance. **A dissolved order on 11/13 therefore does not by itself grade a close.**

| Q3 figure | Value |
|---|---|
| Revenue | $332.2M, −11.7% YoY |
| Adjusted EBITDA | $159.8M, −20.8% YoY, 48.1% margin |
| Net loss | $431.8M, vs net income $86.5M |
| Impairments | $412.1M pre-tax: $159.0M franchise, $253.1M goodwill, triggered by the stock price. $358.0M net of tax |
| Put option FV loss · MBI equity impairment | $39.7M · $20.0M, both net of tax |
| Operating cash flow | $92.6M, −40.8% YoY |
| Cash · gross debt | $674.8M · $3.55B at 9/30 |
| Revolver | $1,050.0M drawn, $200.0M "nominal" availability at 9/30; net $500.0M borrowed in Q3 |
| Covenants | Compliant at 9/30, expects 12 more months, warns "particularly if it does not consummate any financing transactions" |

CABO last $5.16 [yfinance, 11/5 close]. No vector is keyed to this case and no score moves. Still unread: the 17:00 ET call, the 10-Q, the order.

### L916 CRMT backstop #6: NO OTHER AGREEMENT through 16:34 ET, final read NOT MADE

Newest item on the feed at 16:34 ET is still the tenth-bridge 8-K 0001171843-26-007147. The four business days for an agreement dated on or before 11/01 run to today, and the 8-K window ends 17:30 ET, after this session closed. Silence grades nothing. The Mon 11/09 read covers the whole feed from 11/05 08:01 ET and catches anything accepted after my last read.

### Limits of this addendum

- Vendor prices at 16:07 ET. The official closes were not re-read.
- One session. Cause is still not established; section 7 stands.
- The L876 grade rests on the release alone until the 10-Q is read.
