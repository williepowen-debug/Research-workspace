# G — What the market prices across the Ellison / AI-debt web, and what a retail account can touch

**Reader:** G (read-only research reader, spawned by PROME) · **Written:** 2026-10-22 evening ET (Thursday) · **Scope:** pricing and instruments only. **No trade recommendation.** TERRY builds cards; Will decides.
**Confidence tokens:** VERIFIED (checked at the artifact/tape) · INFERRED (supported, not directly established) · SEARCH-NOT-FOUND · UNKNOWN.

## 0. Method and what was actually read

| Source | What | Notes |
|---|---|---|
| DTCC Public Price Dissemination, SEC-regime cumulative credit files (`pddata.dtcc.com`, free) | Single-name CDS prints 10/01-10/22/2026 and 12/22/2025-01/22/2026 | Same source as `AGENTS/LIQUID/scripts/dtcc_cds_probe.py`. I re-parsed the raw CSVs myself (scratchpad only). 10/22 file was published 20:15 ET and is in hand. |
| DTCC CFTC-regime file | CDX.NA.IG / CDX.NA.HY index prints | Level derived from upfront + coupon; see sign caveat below. |
| FRED (`fredgraph.csv`) | ICE BofA OAS series, DGS5, DGS10 through 10/21 | VERIFIED; 10/22 value not yet published. |
| Yahoo (yfinance) | Closes, history, option chains (post-close snapshot ~20:40 ET 10/22) | PSKY series is BROKEN, see 2.1. |
| stockanalysis.com / marketchameleon.com (secondary) | PSKY closes, short interest, IV30, option volume | Secondary web; labelled where used. |
| Press (Bloomberg Law/IBTimes/Barron's via aggregators) | Paramount, CoreWeave, Oracle bond/CDS colour | Secondary; labelled. |

**CDS reading rules (apply to every CDS figure below).**
1. Levels are tape prints, not a vendor composite. "s" = disseminated spread field. "u" = my flat-hazard conversion of upfront + coupon (r 4%, R 40%, quarterly; not ISDA; good to tens of bp, not to one).
2. The DTCC upfront field is UNSIGNED and the notional is CAPPED at "5,000,000+". Where upfront is under about 1.5 points the sign is not knowable; I used only disseminated spreads for those names (AMZN, GOOGL, META, NVDA, MSFT, IBM, CSCO, CMCSA, DIS). Naive reading would have put AMZN and GOOGL near 120bp; the disseminated spreads are 82-83bp.
3. Prints repeating an identical upfront across 3+ unrelated names (e.g. 1.75pt across Oracle, Meta, Disney, IBM, Cisco on 10/22 19:50Z) are package/basket dissemination and were excluded.
4. Standard 5Y = Dec-2031 expiry now; Dec-2030 in January. ORCL 100bp coupon; CRWV 500bp coupon; Paramount Global 100bp coupon.
5. CDS is not retail-accessible (ISDA/ECP). Everything below in sections 1 and 4 is market information, not an instrument a retail account can hold.

## 1. Credit cross-section (5Y CDS, bp)

### 1.1 Single names: 1 Jan 2026 vs today

"Jan" = first two weeks of January (nearest dissemination to 1 Jan; 12/31 and 1/2 had almost no prints). "Today" = 10/22 tape unless noted.

| Name | Jan 2026 (date, source) | Latest (date) | Change | Token |
|---|---|---|---|---|
| **ORCL** (S&P BBB-, 7/9; Moody's Baa2 neg, Fitch BBB per secondary) | 143-149 (12/30: 146u; 1/5: 143u; 1/6: 145s; 1/13: 149s) | **314s** (10/22 18:07Z); 313-316u earlier; 10/21 315-320s; 10/20 342s | **+~167bp, 2.1x** | VERIFIED (tape) |
| MSFT (AAA) | UNKNOWN (no clean print in sampled January days) | 50-52s (10/1-10/9); 10/22 prints are capped/unsigned, no usable spread | n/a | latest clean = 10/9; staleness stated |
| IBM | UNKNOWN (1/5 print 168u has ambiguous sign: 168 or ~32) | 74s (10/20, 10/21); 68-71s (10/5-10/15) | n/a | VERIFIED latest |
| CSCO | 29s (1/13) | 48s (10/22 20:27Z) | +19 (1.7x) | VERIFIED |
| AMZN | 34s (1/16) | 83s (10/22 21:41Z); 80-81s (10/20) | +49 (2.4x) | VERIFIED |
| GOOGL | UNKNOWN | 82s (10/22, 5 prints) | n/a | VERIFIED latest |
| META | UNKNOWN | 116-118s (10/22); Markit "record 114.5" per LIQUID/Reuters 10/20-21 | n/a | VERIFIED |
| NVDA | UNKNOWN | 116-117s (10/22) | n/a | VERIFIED |
| **Paramount Global** (legacy PSKY credit; S&P BB 9/24, Fitch BB at close) | 182s (1/5, 1/9, 1/13) | **547s** (10/22 18:08Z, 3M); uncapped upfront prints 521-556u; 10/21 550s; 10/20 605u; 10/13 570s; press 577 on 10/13 and 268 on 9/17 (IBTimes) | **+~365bp, 3.0x** | VERIFIED (tape); reference entity is "Paramount Global", not "Paramount Skydance" |
| WBD | ~50s (1/13) | 52s (10/15; WBD acquired 10/6, reference-entity status UNKNOWN) | flat | INFERRED stale |
| DIS | 32s (1/8) | 36s (10/15) | +4 | VERIFIED |
| CMCSA | 58s (12/30) | 92s (10/20); 88-90s (10/15-10/16) | +34 (1.6x) | VERIFIED |
| FOXA | SEARCH-NOT-FOUND (no print in sampled days) | SEARCH-NOT-FOUND | n/a | |
| **CoreWeave** | 713-739u (1/6-1/12); 664-672u (1/15-1/16); ~730 center | **1,112u** (10/22 14:05Z, 3M uncapped); 1,144u (20:29Z, 2M, Jun-2031 expiry); 10/20 1,168u; 10/15 print 1,310u; ICE record **1,194.5** on 10/15 (press, single secondary source) | **+~380bp, 1.5x** | VERIFIED (tape); upfront conversions are approximations |
| SoftBank Group | 308-322u (1/15-1/20) | **489u** (10/22 09:27Z, 500M notional, single print); 452u (10/15); 426u (10/2) | +~175bp, 1.6x | INFERRED (single print/day) |
| Broadcom (AI context) | UNKNOWN | 156s (10/21-10/22) | n/a | VERIFIED |
| SpaceX (context) | UNKNOWN | 240s (10/21-10/22) | n/a | VERIFIED |

**Oracle curve on the tape, disseminated spreads:** 10/21: 1.2y 130-140, 3.2y 266-271, 5.2y 315-320, 9.2y 368. 10/22: 3.2y 260, 3.7y 272, 5.2y 314. Oracle 5Y path: ~245 (10/1) → 263 (10/8) → 264 (10/13) → ~300 (10/15) → 312 (10/19) → 342 (10/20 intraday high print) → 315 (10/21) → 314 (10/22). Matches the fleet anchors (320/315 on 10/21 VERIFIED).

### 1.2 Indices and cash benchmarks

| Series | 31 Dec 2025 / early Jan | Latest | Change | Source / token |
|---|---|---|---|---|
| ICE BofA US HY OAS | 281 (12/31) | **327** (10/21); 2026 range 260 (8/28) to 346 (3/30) | +46 | FRED, VERIFIED |
| ICE BofA US Corporate (IG) OAS | 79 | **88** (10/21); 2026 range 73-94 | +9 | FRED, VERIFIED |
| ICE BofA BB OAS | 169 | 198 (10/21) | +29 | FRED, VERIFIED |
| ICE BofA BBB OAS | 101 | 109 (10/21) | +8 | FRED, VERIFIED |
| ICE BofA CCC OAS | 885 | 1,307 (10/21); 1,327 (10/20) | +422 | FRED, VERIFIED |
| 5Y UST / 10Y UST | 3.73% / 4.18% | 4.95% / 5.13% (10/21) | +122bp / +95bp | FRED, VERIFIED. The risk-free base moved a lot; credit yields are not only credit spread. |
| CDX.NA.IG 5Y | ~48-50 (12/30, 1/5) | ~61-63 (10/21-10/22; disseminated spread field 62-63) | +~13 | DTCC CFTC regime; INFERRED (IG field agrees with upfront under the negative-sign reading) |
| CDX.NA.HY 5Y | ~301-304 (12/30, 1/5) | ~341-347 (10/21-10/22) | +~45 | DTCC CFTC regime; INFERRED (sign chosen so level matches HY OAS 327; the positive-sign reading gives ~675, rejected) |

### 1.3 ORCL against its cohorts

| Comparison | Level | Read |
|---|---|---|
| ORCL 5Y CDS vs CDX.NA.IG | 314 vs ~62 | ~5x the IG index. |
| ORCL 5Y CDS vs CDX.NA.HY | 314 vs ~347 | A BBB- name trades about 10% inside the HY index on CDS. INFERRED (two different instruments and constituents). |
| ORCL vs IG tech peers (CSCO 48, AMZN 83, GOOGL 82, META 116, NVDA 117, MSFT ~50 on 10/9, IBM 74) | 314 vs 48-117 | 2.7x to 6.5x the nearest peer. META (116) is the next widest of the AI hyperscalers. |
| ORCL vs other tape names near BBB-/BB+ | GM 111, Delta 116, Ally 145, Conagra 102, Kohl's 420 (10/21-10/22, 1 print each) | A thin, single-print cohort; ORCL sits above every IG-rated name found and below only Kohl's, Paramount, CRWV, SoftBank, Argentina in the scan. INFERRED; ratings of these names not re-verified. |
| ORCL vs ICE BB cash OAS | 314 (CDS) vs 198 (cash OAS, 10/21) | Different instruments (CDS includes the CDS-bond basis and no index composition); direction only. |
| ORCL vs its own cash bonds | 2046 6.55% YTM 8.11%, +247bp over 20Y UST 5.64% (10/2, Benzinga via Webull); 3.85% 2060 est. YTM 7.62%, ~+220bp over 5.42% UST (10/21, model estimate from fund valuations, therighttrader.com) | Long-bond spread +220 to +247 vs 10Y new-issue +145 on 2/2/2026 (BBB index +95 then) and secondary 2036 +205 / 2056 +263 in late July. Cash spreads are INFERRED to have widened roughly 60-100bp since February; no 10/22 cash print reached. |

### 1.4 Paramount: bonds

| Item | Data | Token |
|---|---|---|
| Financing package (priced 9/30, closed 10/5-10/6) | ~$52B total: $30B IG-rated first-lien notes, $12.4B high-yield second-lien, $9.46B loans (IBTimes 10/15). First-lien notes 6.30% 2028 to 8.90% 2066 ($3.5B to $1.25B each); second-lien $6B 8.25% 2031, EUR885M 7.00% 2031, $4B 8.875% 2034, $1.4B 9.125% 2036; USD TLB $8.5B at SOFR+275, 99.75 OID (company release 9/30) | VERIFIED (release); issue prices not disclosed |
| Ratings | S&P cut to BB from BB+ on 9/24; Fitch BB issuer, first-lien secured BBB- (investment grade) at completion | VERIFIED (IBTimes, secondary press) |
| Second-lien 9.125% 2036 | 100 at issue (9/30); **~91 on 10/13** (IBTimes) → approx. YTM **10.6%** (my calculation, 9.97y, semi-annual) | price VERIFIED secondary; yield INFERRED |
| 8-year USD junk notes | ~96 on 10/1 vs 100 at issue (Bloomberg Law) | secondary, truncated |
| Bonds after 10/13 | SEARCH-NOT-FOUND (TRACE/Bloomberg paywalled) | |
| Net debt at close | $84.3B per Debtwire (est.), after ~$5B cash (IBTimes) | secondary estimate |
| New-issue market context | New IG deals trailed JPM IG index by 27bp over the 10 days to 10/8; Skydance the main cause (IBTimes quoting JPM) | secondary |

### 1.5 CoreWeave and AI-infra high yield

| Item | Data | Token |
|---|---|---|
| CRWV bonds, HYG fund-evaluated, holdings file "as of 10/21" (LIQUID report 10/22) | 9.25% 6/2030: 85.76 / YTW 14.44%; 9.00% 2/2031: 81.75 / 14.91%; 9.75% 10/2031: 81.74 / 15.12%; 9.625% 7/2032: 80.04 / 14.91% | VERIFIED as LIQUID's receipt; vendor evaluations, not TRACE; 2030 line unchanged since 10/14 (stale risk) |
| Press peak | 2032 notes ~15-16% around 10/13-10/16; 2031s 79.9 / 15.6% and 78.65 / 16.2% (Reuters/Barron's via aggregators) | secondary |
| HY index yield for comparison | UST 5Y 4.95% + HY OAS 3.27% ≈ 8.2% (crude; the index is 3-4y duration) | INFERRED |
| CRWV spread to index | ~14.4-15.1% vs ~8.2% = roughly +620 to +690bp over the HY index yield; CDS 1,112 vs CDX.NA.HY ~347 = 3.2x | INFERRED |
| Applied Digital (APLD) | $1.59B 7.000% senior secured notes due 6/15/2031, priced at par June 2026 (company 8-K via search). Current price/yield SEARCH-NOT-FOUND. A $2.35B secured-note launch just before the sector sell-off is mentioned but date and pricing unconfirmed. | VERIFIED existence; level UNKNOWN |
| Nebius (NBIS) | Convertible notes only (0.50% 2030, 4.50% 2034; ~$5.75B raised in two series per press; $4.34B closed March 2026). No straight bonds found. Current price UNKNOWN. | secondary |
| IREN | Convertibles only per search; no bond pricing found. | SEARCH-NOT-FOUND |
| CDS for APLD / IREN / NBIS | No print on the 10/22 tape for these names (scanned by name). | SEARCH-NOT-FOUND |

## 2. Equity

### 2.1 Data-quality flag for PROME (act on this)

**`FORGE/tools/market-data/fetch.py price PSKY` returned $9.78 for 2026-10-22. That number is wrong.** It equals the 10/5/2026 close (9.775); Yahoo's own 10/22 row is a corrupted fragment (Open 9.26 = the 10/5 open, High = Low = 9.775, Close NaN). Yahoo also holds only about 15 PSKY bars (since 7/29) and its PSKY option chain has all bid/ask at 0 with last trades dated 10/1-10/5. The 10/22 close per stockanalysis.com (secondary) is **$7.79** (10/21 7.87, 10/20 7.10, 10/19 6.80, 10/16 6.91, 10/15 7.26, 10/14 7.06, 10/13 9.27). marketchameleon's PSKY page repeats the stale 9.77. INFERRED that 7.79 is correct (one independent secondary source; its 10/14-10/16 closes match Yahoo's and IBTimes' 10/14 7.06 exactly). Re-check at a broker quote before any PSKY figure is used on a card.

### 2.2 Table (closes 10/22/2026 unless noted)

| | ORCL | PSKY | CRWV | SoftBank (SFTBY ADR / 9984.T) | TSLA |
|---|---|---|---|---|---|
| Close 10/22 | **$125.54** (-2.78%) VERIFIED | **$7.79** (-1.0%) INFERRED (see 2.1) | **$55.60** (-10.06%) VERIFIED | SFTBY **$13.50** (-7.91%); 9984.T **¥4,305** (-6.9%) 10/22 JST close; ¥4,012 intraday 10/23 JST | **$374.58** (-3.08%) VERIFIED |
| 12/31/2025 close | $194.91 | ~$13.4 (derived: TIKR said "down 33% YTD at ~$9" on 3/27) INFERRED | $71.61 | SFTBY $14.18; 9984.T ¥4,400 | $449.72 |
| **YTD** | **-35.6%** | **~-42%** INFERRED | **-22.4%** | SFTBY -4.8%; 9984.T -2.2% | **-16.7%** |
| 2026 high (close) | $248.15 (6/1) | UNKNOWN pre-July (series unavailable); highest close seen 11.14 (9/16); 1-yr change -52.8% (stockanalysis) | $137.98 (5/6) | SFTBY $28.68 (6/1); 9984.T ¥8,632 (6/2) | $451.67 (1/5) |
| **Drawdown from 2026 high** | **-49.4%** | at least -30% from 11.14; about -42% or worse vs January level INFERRED | **-59.7%** (new low today; prior 2026 low $60.82) | SFTBY **-52.9%**; 9984.T **-50.1%** | **-17.1%** |
| 30-day implied vol (IV30) | **59.5%** (10/22; 56.7% on 10/21) | UNKNOWN (no usable live source; last found: Fintel 58-61% on 7/31, AlphaQuery ~55-60% on 7/6) | **109.8%** (98.5% on 10/21) | no US-listed options on SFTBY; 9984.T IV SEARCH-NOT-FOUND | **39.6%** (41.8% on 10/21) |
| IV30 52-week range / median | 40.7%-84.4% / 56.3% | UNKNOWN | 65.9%-122.7% / 89.2% | n/a | 36.5%-61.0% / 44.9% |
| Realized vol 20d / 1y | 58.2% / 55.7% | 11 sessions to 10/22: ~151% annualized incl. 10/14, ~67% excl. 10/14 (10/14 is -23.8% and includes the warrant-distribution adjustment). 1y UNKNOWN. | 92.7% / 92.2% | 9984.T 30d 76%, 1y 87% (yfinance, incl. 10/23 intraday) | 35.4% / 42.8% |
| IV30 / 1y realized | 1.07x | n/a | 1.19x | n/a | 0.93x |
| IV30 position in own 52w range | 43% | n/a | 77% | n/a | 13% (near low) |
| Skew at 1 month (11/20 expiry, 90% put vs ATM vs 110% call IV) | 61 / ~60 / 60: flat | UNKNOWN (stale chain) | 113 / ~112 / 113: flat | n/a | 43 / ~41 / 41: mild put skew |
| Option volume 10/22 (marketchameleon) | 489,136 (C 286,394 / P 202,742); P/C 0.71; 30d avg 423,254 | UNKNOWN | 939,674 (C 503,960 / P 435,714); P/C 0.86; 30d avg ~425,701 | n/a | 1,939,132; P/C 0.84; 30d avg 2,217,313 |
| Short interest (stockanalysis, date unstated) | 48.49M sh, 2.60% float, 1.42 days (prior month 44.60M) | 85.02M sh, 2.07% float, 8.32 days (prior 78.37M) | 59.95M sh, **18.26% float**, 2.08 days (prior 54.94M) | SEARCH-NOT-FOUND | 70.93M sh, 2.51% float, 1.79 days |
| Market cap / total debt (stockanalysis) | $380.6B / $169.1B | ~$39.3B at 7.79 (5.04B shares) / stockanalysis debt $16.2B is stale; Debtwire net debt $84.3B at close | $30.7B / $51.6B | n/a | $1.48T / $9.5B |

Notes: (a) Skew is read from Yahoo post-close chain snapshots (IV as the vendor computed it); it is a coarse 1-month read, and the ATM put IV sits 3-4 vol points below the ATM call IV in ORCL and CRWV, which is a parity/borrow artifact, not a forecast. The practical read is that puts 10% out of the money are not richer than at-the-money in ORCL or CRWV; the market is not charging a tail premium on top of already-high level vol. (b) The 5.04B PSKY share count is from stockanalysis and fits an ~$40B equity raise at ~$9; Yahoo shows 1.12B (stale). (c) SFTBY drop on 10/22 -7.9% and 9984.T a further ~-6.8% intraday on 10/23 JST: SoftBank is the node moving hardest right now.

### 2.3 AI-infra cohort equity, 10/22 close vs 12/31/2025 and 2026 high (VERIFIED, Yahoo / repo tool)

| | Close | YTD | From 2026 high | IV30 |
|---|---|---|---|---|
| NBIS | $159.17 (-7.23%) | +90% | -44.5% | n/a (chain ATM IV ~1.0 for 11/20) |
| IREN | $25.51 (-8.37%) | -32.5% | -62.4% | not pulled |
| APLD | $19.09 (-9.01%) | -22.1% | -61.5% | not pulled |
| Media/tech peers | DIS $113.13 (-0.6% YTD), CMCSA $22.84 (-18.5%), FOXA $68.27 (-6.6%), MSFT $521.08 (+7.7%), AMZN $250.38 (+8.5%), IBM $252.11 (-14.9%), CSCO $104.89 (+36.2%) | | | |

## 3. Instruments a retail options account can use

### 3.1 Listed options, 1-3 month tenors (Yahoo post-close snapshot 10/22 ~20:40 ET; bid/ask are closing quotes)

| Underlying | Expiry (dte) | ATM strike | ATM call bid/ask · OI | ATM put bid/ask · OI | Put as % of spot; put spread | Chain open interest, calls / puts |
|---|---|---|---|---|---|---|
| **ORCL** $125.54 | 11/20 (29) | 125 | 9.00/9.10 · 935 | 8.00/8.15 · 12,054 | 6.4%; 1.9% | 211,745 / 182,335 |
| | 12/18 (57) | 125 | 13.25/13.40 · 1,166 | 11.85/12.00 · 10,148 | 9.5%; 1.3% | 285,384 / 243,648 |
| | 1/15/27 (85) | 125 | 14.95/15.60 · 2,018 | 13.60/14.00 · 10,159 | 10.9%; 2.9% | 326,369 / 265,148 |
| ORCL 10%-out put | 11/20 / 12/18 / 1/15 | 115 | | 4.00/4.10 · 12,088 / 7.35/7.50 · 13,988 / 9.00/9.10 · 15,754 | 3.2% / 5.9% / 7.2% of spot | |
| **CRWV** $55.60 | 11/20 (29) | 55 | 7.25/7.50 · 2,172 | 6.40/6.65 · 15,525 | 11.7%; 3.8% | 216,565 / 221,072 |
| | 12/18 (57) | 55 | 9.05/9.35 · 439 | 8.15/8.30 · 11,714 | 14.8%; 1.8% | 168,774 / 220,118 |
| | 1/15/27 (85) | 55 | 10.55/10.75 · 525 | 9.40/9.60 · 9,768 | 17.0%; 2.1% | 284,899 / 328,408 |
| CRWV 10%-out put | 11/20 / 12/18 / 1/15 | 50 | | 4.20/4.30 · 15,859 / 5.75/5.90 · 10,990 / 6.90/7.20 · 38,769 | 7.6% / 10.4% / 12.4% | |
| **PSKY** $7.79 | all | 8 | **bid/ask 0/0 in the vendor feed; last trades 10/1-10/5** | OI only: 11/20 8P 5,832; 1/15 8P 74,450, 9P 27,142, 10P 44,534 | UNKNOWN | 11/20 38,017 / 14,806; 12/18 241,059 / 58,571; 1/15 265,018 / 293,813 |
| TSLA $374.58 (reference) | 11/20 | 375 | 17.45/17.75 · 4,456 | 16.00/16.85 · 2,848 | 4.3%; 5.3% | 233,172 / 228,147 |
| NBIS $159.17 (reference) | 11/20 | 160 | 18.05/18.25 · 402 | 18.30/18.55 · 2,651 | 11.5%; 1.4% | 86,627 / 101,688 |
| SFTBY | none | | | | | no listed options (Yahoo returns zero expiries) |

Liquidity read (VERIFIED as a vendor snapshot; confirm at the broker): ORCL and CRWV are deep. Dollar-wide round-lot spreads of 0.10-0.40 on 8-15 dollar premiums (1.3-3.8% of premium) at ATM, six-figure chain open interest, and 10,000-39,000-lot OI at the common put strikes. TSLA is deepest. The ORCL 11/27 expiry is thin (OI under 100 at ATM): use the monthly. **PSKY options exist and carry sizable open interest (1/15 8P 74k, 10C 54k), but I could not obtain a live bid/ask or IV: the feed is stale and 10/14's warrant distribution and share-count change may have adjusted contracts. Treat PSKY options liquidity as UNKNOWN until a broker chain is open.** SoftBank has no listed US options; the 9984.T Japanese options are outside a normal US retail account.

### 3.2 ETFs and funds

| Exposure | Instrument | Weight / note | Token |
|---|---|---|---|
| **Oracle alone, unlevered** | **none** | Confirmed no unlevered single-name ETF in the search. | SEARCH-NOT-FOUND |
| Oracle, 2x daily long | ORCX (Defiance Daily Target 2X Long ORCL, 1.29-1.36% ER, launched 2/6/2025); ORCU (Direxion Daily ORCL Bull 2X, 0.97% ER, launched 11/19/2025) | Daily-reset leverage, built for one-day holding; they fell far more than 2x ORCL over longer spans (ORCX ~$21 on 9/2/2026 per P&I, AUM ~$224M). Inverse ORCL ETF: SEARCH-NOT-FOUND. | VERIFIED existence (search) |
| CoreWeave, 2x daily long | CRWG (Leverage Shares, 0.75% ER, launched 8/11/2025); CRWU (T-REX 2X, 1.50% ER, 7/25/2025) | Same daily-reset caveat. Inverse CRWV ETF: not checked. | VERIFIED existence |
| Paramount | no single-name ETF found | | SEARCH-NOT-FOUND |
| Software basket with Oracle | IGV: ORCL 6.92% (also MSFT 8.50%) · SKYY (cloud): ORCL 3.20%, CRWV 2.97%, MSFT 3.51%, AMZN 3.33%, IBM 3.27% | Yahoo holdings, current vintage unconfirmed | INFERRED |
| Broad tech | XLK/VGT: ORCL not in the top 10 (CSCO 2.4% / 1.6%); MSFT 10.7% / 11.2% | | VERIFIED (Yahoo top holdings) |
| Comms/media | XLC top-10 still lists WBD 4.94%, DIS 4.48% | WBD was acquired 10/6 and last traded 10/5 ($30.95), so the holdings list is stale | VERIFIED stale |
| Credit beta (cash HY) | HYG $77.10 (+0.16% 10/22); LQD $104.28 (+1.04%) | HYG holds CRWV bonds (LIQUID used its holdings file) but at a small weight; HYG options are very deep: 11/20 chain OI 2.0M puts / 0.9M calls, ATM 77 put 0.55/0.64 (OI 364,868), 12/18 put 1.02/1.32, IV 8-11% | VERIFIED snapshot |
| CDS | CDX/CDS | Not retail-accessible: ISDA/ECP counterparties; shown only as a market signal | |

## 4. What the pricing implies

**Method.** Flat hazard λ = spread / (1 - 40% recovery). Cumulative default probability over 5 years = 1 - e^(-5λ). These are RISK-NEUTRAL probabilities: they include a premium for bearing the risk and for CDS-bond basis and liquidity, so true (physical) default odds are lower. The 40% standard recovery is a convention; it is probably too high for a CRWV-type asset-heavy issuer and may be too low for first-lien-secured Paramount debt.

| Name | Spread | λ per year | 1-year | **5-year** | Jan 2026 5-year (same method) |
|---|---|---|---|---|---|
| ORCL | 314 | 5.2% | 5.1% | **23%** | 11.5% (147) |
| Paramount Global | 547 | 9.1% | 8.7% | **37%** | 14.1% (182) |
| CoreWeave | 1,112 | 18.5% | 16.9% | **60%** | 45.6% (730) |
| SoftBank | 489 | 8.2% | 7.8% | **34%** | 22.8% (311) |
| CDX.NA.HY (index, INFERRED level) | 347 | 5.8% | 5.6% | 25% | 22.2% (~302) |
| META / AMZN / GOOGL / CSCO | 116 / 83 / 82 / 48 | 1.9 / 1.4 / 1.4 / 0.8% | | 9.2 / 6.7 / 6.6 / 3.9% | |
| MSFT (10/9) / IBM (10/21) | 50 / 74 | 0.8 / 1.2% | | 4.1 / 6.0% | |

**Does equity vol agree with credit?** A rough Merton-style cross-check (INFERRED; asset vol = equity IV30 x E/(E+D), D = stockanalysis total debt including leases, r 4.5%, 5-year horizon, ignoring debt maturities and asset-backed structure):

| Name | Equity | Debt | IV30 | Merton 5Y PD | CDS-implied 5Y (risk-neutral) | Read |
|---|---|---|---|---|---|---|
| ORCL | $381B | $169B | 59.5% | ~14% | 23% | Same order of magnitude; credit is wider than equity vol alone explains but not wildly. Equity vol is mid-range for its own year (43rd percentile of the 52w IV range) while CDS (314) sits far above the July 2026 press-reported record of ~203: credit has moved more than equity vol. |
| CRWV | $30.7B | $51.6B | 109.8% | ~38% | 60% | Credit says more distress than equity vol does. Equity IV is high (77th percentile of range) and the stock is -60% from its high, but option implied move is ±6.1% for the nearest expiry and skew is flat; the options market is pricing a violent equity, not an extra put premium for default. |
| PSKY | ~$39B (INFERRED share count) | Debtwire net debt $84.3B | UNKNOWN (RV ~67% ex 10/14) | not computed: share count and IV conflict | 37% | Cannot cross-check cleanly. The equity has fallen from ~$9.3 to ~$7.8 (-16%) since 10/13 while Paramount Global CDS went 570 → 547 (flat to slightly tighter). 5-year hazard of 9%/yr at BB with first-lien notes rated BBB- by Fitch suggests CDS is pricing second-lien/unsecured recovery risk more than the secured stack. INFERRED. |
| TSLA (reference) | | | 39.6% (near 52w low) | | no clean CDS | Equity vol near its yearly low; not part of the credit stress cluster. |

Cross-name conclusions (all INFERRED unless marked):
1. The market ranks credit stress CoreWeave (60%) > Paramount (37%) > SoftBank (34%) > Oracle (23%) on 5Y risk-neutral odds. The Ellison-linked pair (Oracle, Paramount) moved 2.1x and 3.0x against the HY index 1.1x and IG index 1.3x; neither is explained by the index.
2. Oracle's CDS (314) now equals the HY index (347) rather than IG peers (48-117). Rating is still BBB- (S&P). The CDS market prices Oracle as a high-yield credit while it is still an investment-grade issuer; if an agency moves it below BBB-, index-eligibility and forced-selling mechanics become the next question (LIQUID's GATE-LIQ-069 tracks the rating ladder; I did not find an October agency action).
3. Equity options are not signalling credit panic in ORCL: realized vol 55-58% vs implied 59.5%, flat 1-month skew, put/call 0.71 on 489k contracts. CRWV options are signalling extreme volatility but a symmetric one.
4. Paramount's bond market (second-lien 2036 at ~91, ~10.6% YTM; Paramount Global CDS ~547) disagrees more with a "deal done, de-risked" equity narrative than with a falling equity price: equity has been volatile (-23.8% on 10/14 with the warrant effect) while CDS widened through 10/14 and eased slightly since.
5. SoftBank (CDS 489, ADR -7.9% on 10/22, further -6.8% intraday on 10/23 JST, -50% from its June high) is the largest same-day mover; I found no listed option or bond-level data for it.

## 5. What I could not reach

| Gap | Why |
|---|---|
| MSFT, GOOGL, META, NVDA, IBM, FOXA 1 January 2026 CDS | Not printed in the ~20 sampled January trading days with usable disseminated spreads. |
| Any 10/22 MSFT clean spread | 10/22 MSFT prints are capped/unsigned/package; last clean disseminated 50bp on 10/9. |
| Cash-bond yields for ORCL (10/22), PSKY after 10/13, media peers, APLD, NBIS/IREN converts | TRACE/Bloomberg/ICE paywalled; press only. |
| PSKY live IV, skew, option bid/ask, IV history | Yahoo chain stale since 10/5; marketchameleon/Fintel pages empty or 403; vendor price feed corrupted (section 2.1). |
| PSKY 2026 high and exact YTD | Yahoo history ~15 bars; January level derived from a TIKR sentence. |
| SoftBank option/IV/short-interest | No US-listed options; no SEC short interest for an ADR; Japanese options not reached. |
| Moody's/Fitch primary actions on Oracle | Secondary only (Moody's Baa2 negative, Fitch BBB per Benzinga/fleet). |
| Short-interest settlement dates | stockanalysis does not state them. |
| Whether the DTCC "Paramount Global" CDS reference survives unchanged after the Skydance/WBD structure | UNKNOWN; relevant to deliverable obligations if a credit event were ever in question. |

## SUMMARY FOR PROME

- **Headline table (5Y CDS, tape 10/22 vs early Jan):** Oracle **314 vs ~147 (2.1x)**; Paramount Global **547 vs 182 (3.0x)**; CoreWeave **~1,112 vs ~730 (1.5x)**; SoftBank ~489 vs ~311; CDX.NA.IG ~62 vs ~49; CDX.NA.HY ~347 vs ~302 (INFERRED sign); HY OAS 327 vs 281, IG OAS 88 vs 79 (FRED, 10/21). IG tech peers: CSCO 48 (29 in Jan), AMZN 83 (34), GOOGL 82, META 116, NVDA 117, MSFT ~50 (10/9, last clean print), IBM 74. Media: CMCSA 92 (58), DIS 36 (32).
- **Oracle trades like high yield on CDS (314 vs HY index ~347, vs 5x the IG index) while still BBB-.** Implied 5Y risk-neutral default odds at 40% recovery: ORCL 23% (11% in Jan), Paramount 37%, CRWV 60%, SoftBank 34%.
- **DATA DEFECT:** the repo price tool shows PSKY $9.78 on 10/22; that is the 10/5 close. Secondary source shows **$7.79**. Yahoo's PSKY history and option chain are also stale/broken. Fix before any PSKY number reaches a card.
- **Equity (10/22):** ORCL $125.54, -35.6% YTD, -49.4% from 6/1 high; CRWV $55.60, -22.4% YTD, -59.7% from high; TSLA $374.58, -16.7% YTD; SFTBY $13.50, -52.9% from June high; PSKY ~$7.79, about -42% YTD (INFERRED).
- **Where credit and equity vol disagree:** ORCL IV30 59.5% is mid-range (43rd percentile of its year) and roughly equals realized (55.7%), skew flat, P/C 0.71 — equity options are calm relative to a CDS at a 2-year high. CRWV: credit (60% odds) is more distressed than a Merton-style read of equity vol (~38%); IV 109.8% is high but symmetric. TSLA IV 39.6% is near its 52w low, outside the stress cluster.
- **Instruments:** ORCL options deep (11/20 chain OI ~394k contracts; ATM spreads 0.15 on ~8-dollar puts; 12/18 and 1/15 similar); CRWV options deep (939k contracts 10/22; put OI 38,769 at the 1/15 50 strike); costs: ORCL 125 put 8.0-8.15 / 11.85-12.0 / 13.6-14.0 for 11/20 / 12/18 / 1/15; CRWV 55 put 6.4-6.65 / 8.15-8.3 / 9.4-9.6. **No unlevered Oracle-only ETF exists; 2x daily long ORCL funds do (ORCX, ORCU), as do 2x CRWV (CRWG, CRWU).** IGV holds ORCL 6.9%; SKYY holds ORCL 3.2% and CRWV 3.0%. HYG options are very deep (2M put OI on 11/20). CDS is not retail-accessible.
- **Could not reach:** PSKY live option quotes/IV (feed stale; OI large but liquidity UNKNOWN), PSKY bond prices after 10/13 (second-lien 2036 was ~91 / ~10.6% YTM on 10/13), Oracle cash-bond levels on 10/22 (10/2: 2046s 8.11%), APLD/NBIS/IREN bond prices, January CDS for MSFT/GOOGL/META/NVDA, SoftBank options.
- Files: report at `/home/willi/Research-workspace/PROME/reports/2026-10-22_ellison-financing-web/G-what-is-priced.md`. Raw DTCC/FRED pulls and parsers are in the session scratchpad only (`/tmp/claude-1000/-home-willi-Research-workspace-PROME/40ef6293-44ad-4b1b-be36-24f13a73e844/scratchpad/`).
