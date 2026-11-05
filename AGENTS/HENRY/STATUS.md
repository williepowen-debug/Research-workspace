# HENRY STATUS

**Last owner update:** 2026-11-05 from 09:39 ET, boot then Will's 09:42 ET catch-up word via PROME (packet `inbox/processed/2026-11-05_from-PROME_catch-up-to-live-data.md`; Claude Code, Opus 5.5, `claude-opus-5-5`). Changed: everything above § THESIS re-based to 11/4 closes and an 11/5 morning intraday read; the 10/30 and 11/02 sections rotated verbatim to `STATUS_COLD.md` § ROT-11/05. Pre-session copy: `research/2026-11-05_catchup/STATUS-before.md`.

## VIEW

**11/5 09:52 ET, intraday, not a close: dealer gamma is NEGATIVE at both horizons on SPX, QQQ and NDX, and index mechanics are amplifying a second concentrated chip sell-off.** SPX 7,577.69 (−1.44%), QQQ 668.64 (−3.37%), NDX 27,462.64 (−3.43%), while RSP is −0.35% and KRE +1.0% (vendor 1-minute bars). SMH −5.59% at 09:45 ET, AMD −10.73%, QCOM −9.13%, TSLA −8.28%, MU −8.23%, NVDA −4.02%. QQQ traded through the 680 put wall I published 11/2 within two minutes of the open and NDX is under 28,000. SPX is under 7,600, inside the 7,500–7,600 band. The profile says SPX amplification keeps deepening to about 7,350–7,400 with no second flip above 7,100 (35d; shape only, dollars are assumption-dependent), while QQQ is already at its trough (675). HYG −0.15%: **not a credit move this morning.** Reported drivers, none established: Qualcomm's profit forecast, post-election rotation, AI-regulation talk (secondary press, premarket).

**The week so far:** 11/2 fell into the map's put band and QQQ spent the session between its two walls (grade below). 11/4 was the relief: Democrats reported winning both chambers (AP/Reuters; not certified), Brent settled $94.62 (−8.7%, CNBC), SPX +1.58% to 7,688.62, VIX −20.26% to 16.61, yet chips fell that day too (SOXX −3.14%, NVDA −3.17%). SPX closed 4 points under its 50-day (7,693.0, own calc) and under the flip. No deal, reopening or transit recovery is established (WALTER SIG-W-20261104-078). **Credit had not relaxed through 11/3 (11/4 not posted):** HY 326/344/343/340 (10/29–11/3), LIQUID's >320 persistence MET 11/2, tiers BROADENS.

No probability, threshold, prediction or trade changed.

## GAMMA MAP — 11/5 INTRADAY (`gamma_flip.py --both --spot <live> --publish`, 09:48 ET)

| Chain (Cboe; spot passed in live) | Flip 14d / 35d | Net GEX per 1% 14d / 35d | Put wall | Call wall |
|---|---:|---:|---|---|
| SPX (3,330 / 7,585 contracts), spot 7,581 | ~7,693 / ~7,696 | **−$32.4B / −$53.3B** | **7,600 at both** (35d near-tie, carry band 7,500–7,600) | WITHHELD: 7,650 vs 7,700 |
| QQQ (1,575 / 2,506), spot 669.70 | ~702 / ~706 | −$3.7B / −$6.4B | WITHHELD: 675 clean vs 680 near-tie, band 675–680 | **700 at both** |
| NDX (1,907 / 3,183), spot 27,527 | ~28,495 / ~28,566 | −$1.0B / −$2.0B | **28,000 at both** | WITHHELD: 28,500 vs 29,675 |

**Flips since 11/2:** SPX 7,706–7,711 → 7,693–7,696 · QQQ 718–721 → 702–706 · NDX 28,779–28,913 → 28,495–28,566. **35d profile, $B per 1% by spot:** SPX 7,750 +34 · 7,700 +4 · 7,650 −23 · 7,600 −46 · 7,550 −62 · 7,500 −72 · 7,400 −81 (trough) · 7,300 −78 · 7,100 −65. QQQ 710 +2.0 · 700 −1.2 · 690 −4.5 · 680 −6.3 · 675 −6.6 (trough) · 670 −6.4 · 660 −5.6 · 650 −4.7 · 620 −2.9.

**Put open interest, 11/2 map → 11/5 chain:** QQQ Nov-20 680 89,505 → 94,326 · 670 52,149 → 44,870 · 700 41,161 → 38,603 · 690 39,216 → 37,607; QQQ Nov-06 680 34,980 → 36,088. SPX Nov-06 7,550 7,330 → 6,874 · 7,400 8,009 → 6,380. Opening versus closing is unknown.

⚠️ **Vintage:** OI is 11/4-trade vintage INFERRED from OCC's morning post; the pre-open proof (`research/2026-11-02_L888/oi_vintage_check.py`) was not run today. Option marks and IV are about 15 minutes delayed. Free-tier proxy: sign and flip robust, $B assumption-dependent. QQQ is American-style and only part of Nasdaq-100 gamma. **These walls are morning reads on a falling tape; regrade at the close.**

⚠️ **Void read, disclosed:** a 09:44 ET run read SPX POSITIVE with flip ~7,641. Cboe's payload carried IV = 0 on all 29,440 contracts for the first ~15 minutes after the open, so the script fell through to the vendor chain and only the `src=` label said so. Nothing was published from it. Fixed in `scripts/gamma_flip.py` today (prints the reason, refuses `--publish`; tested). Any read before ~09:47 ET on a session is suspect; the pre-open payload is unaffected. `boot.py`'s 09:41 ET Cboe read (flip ~7,695, spot 7,688.62 = the 11/4 close) came through clean.

## GRADE OF THE 11/2 PRE-OPEN MAP (vendor daily bars)

| Line | 11/2 | 11/3 | 11/4 | 11/5 by 09:52 ET | Grade |
|---|---|---|---|---|---|
| SPX flip 7,706–7,711 | high 7,662.23 | high 7,594.61 | high 7,715.57, close 7,688.62 | under | Every close stayed under the flip; traded through 11/4 intraday only |
| SPX put band 7,500–7,600 | low 7,539.38, close 7,541.40 | low 7,545.39 | low 7,635.81 | ~7,578 | Band held on closes; lows stopped 39 points above its floor |
| QQQ put wall 680 | low **680.33**, close 681.09 | low 683.18 | low 687.87 | through in 2 minutes, low so far ~668 | **Held three sessions by $0.33 at the tightest, BROKEN intraday 11/5** |
| QQQ call wall 700 | high **699.43** | high 688.69 | high 701.45, close 691.95 | — | Held on every close; traded $1.45 through 11/4 |

The two QQQ walls bracketed a full session within $0.90 on 11/2. Levels on a four-session sample, not a hit rate. My note carried over from 10/30: a trough is where amplification peaks, not a support line.

## VOL REGIME / TAPE INPUTS — 11/4 CLOSE (vendor; VIX confirmed FRED VIXCLS)

| Session | SPX | VIX | VIX9D | VIX3M | VVIX | SKEW | Term structure |
|---|---:|---:|---:|---:|---:|---:|---|
| 11/2 | 7,541.40 (−0.51%) | 21.15 | 22.46 | 21.60 | 110.47 | 152.78 | **inverted** (9D > 3M) |
| 11/3 | 7,568.92 (+0.36%) | 20.83 | 21.96 | 21.27 | 107.40 | 150.01 | **inverted** |
| 11/4 | **7,688.62 (+1.58%)** | **16.61 (−20.26%)** | 15.19 | 18.80 | 90.41 | 150.90 | contango |

**11/5 morning (Cboe, delayed, last trade ~09:33 ET):** VIX 17.50, VIX9D 16.65, VIX3M 19.40, VVIX 92.48; contango. ⚠️ Not current with the 09:52 tape; a vendor VIX of 17.07 at boot was a pre-open bar. KRE $74.13 [11/4], USD/JPY 158.47 [11/4]. Cascade proxy (own calc, closes): SPX 50-day 7,693.0 through 11/4, layer-2 proxy MET on the 11/4 close by 4 points; layer 1 (VIX > 23–24) not met. VIOLET owns the vol broadcast. Files: `research/2026-11-05_catchup/`.

## CREDIT EARLY-WARNING MONITOR — FRED LATEST VINTAGE THROUGH 11/3 (pulled 09:46 ET 11/5)

| Series | 10/28 | 10/29 | 10/30 | 11/2 | 11/3 |
|---|---:|---:|---:|---:|---:|
| HY OAS | 314bp | 326bp | **344bp** | 343bp | **340bp** |
| BB OAS | 184bp | 194bp | 209bp | 206bp | 203bp |
| CCC OAS | 1,307bp | 1,325bp | 1,327bp | 1,319bp | 1,316bp |
| CCC−BB | 1,123bp | 1,131bp | 1,118bp | 1,113bp | 1,113bp |

**LIQUID 11/4 (owner adjudication, SIG-W-20261104-076):** renewed >320 persistence MET 11/2, fourth observation 11/3; existing tier rule BROADENS (IG 94/94/93 fails strict >94). Price repricing is demonstrated; a generalized funding restriction is not (funding NOT ARMED through 11/3). REGINALD's strict >350 ×3 stays 0 of 3. HY tightened only 4bp from the 10/30 peak through 11/3, and the 11/4 relief session is not yet posted (HYG +0.70% that day); `credit_monitor.py` 09:41 ET: gap +257bp over ~3 months, HYG $77.39, HYG/LQD 5-session −0.4%, no fund-flow flag. 11/4 FRED not posted at the pull.

## RELEASES SINCE 11/2

| Release | Actual | Consensus | Prior | Market reaction | Read |
|---|---:|---:|---:|---|---|
| ISM manufacturing Oct (11/2) | 55.5; orders 55.5, employment 52.4, prices 75.2 | UNKNOWN | 54.5 | SPX −0.51% that day; overlapped | Activity holds, prices stay RED observation; inventory and precautionary demand limit breadth (ISHM) |
| S&P manufacturing final Oct (11/2) | 54.9 | flash 56.0 | 55.9 | — | Components unverified (portal 403) |
| JOLTS Sep (11/3) | openings 7,523K; hires−separations +83K | UNKNOWN | +96K rev | — | LABOR owns |
| ADP Oct (11/4) | +86K | UNKNOWN | +86K rev | — | Not CES; does not grade HEN-59 |
| ISM services Oct (11/4) | 54.5; orders 55.9, employment 51.4, prices 73.0 | UNKNOWN | 54.9 | SPX +1.58%; overlapped by oil and election | Demand softer but above 50; prices remain high: the two legs stay separate |
| Productivity Q3 prelim (11/5) | output per hour +3.5% annualized; unit labor costs −0.7% annualized | UNKNOWN | — | not separable from the open | ⚠️ My annualization of FRED OPHNFB/ULCNFB index levels; BLS page 403, release text unread |

Sources: WALTER SIG-W-20261104-003/-004/-005 and ISHM L899 (ISM primaries read there, not re-read by HENRY). KB ML-HEN-195.

**Election (SIG-W-20261104-038):** HENRY held no election scenario to reconcile; nothing to grade (search with positive control in `board_log.tsv`). Reaction logged KB ML-HEN-196, cause not established.

**Positioning leads (SIG-W-20261102-005), qualified, not upgraded:** "hedge funds selling at an all-time pace" (Kalshi) and "~$1B into a 3x Nasdaq ETF after 10/30" (MacroEdge). Neither names a source, window or ticker. QQQ short interest: latest published still 82,001,618 at the 10/15 settlement (Nasdaq API 09:51 ET 11/5); the 10/30 settlement is not posted.

**Breadth check (SIG-W-20261104-055):** the attributed "60% of S&P 500 in bear-market territory" (Goldman's Molavi via Bloomberg, 11/3) does not reproduce: **31.3%** of members sat 20%+ under their 252-session closing high on 11/3 (33.3% on intraday highs), 29.1% on 11/4; **56.4%** sat 10%+ under on 11/3, 50.6% on 11/4. Bloomberg's definition was not read, so the gap is unexplained. Members above 50-day / 200-day: 71.7% / 65.5% on 11/4. SPX was −3.2% from its 10/6 record on 11/3. Own calc, `research/2026-11-05_catchup/breadth_recheck.txt`, KB ML-HEN-197.

## MARKET BREADTH — L616 STUDY (Friday 10/30 closes; members from SSGA holdings as of 10/29; yfinance bars pulled 10/31 13:07–13:10 ET)

| Measure | 10/30 | Reference points |
|---|---|---|
| S&P 500 members above 50-day / 200-day | **60.2% / 59.2%** | 9/30 20.9% / 40.4% (2026 low for the 200-day) · 10/6 record close 29.5% / 46.6% (lowest of 2026's 28 record closes on both) · 8/13 record 68.7% / 73.6% |
| S&P 400 / S&P 600 members above 200-day | 49.8% / 51.8% | 8/13 72.2% / 74.7% |
| RSP/SPY relative (total return, ratio basis) | 1 day +1.00pp · 1 week +1.38 · October **+5.91** (99.5 pctile of 22-session windows since 2003) · 3 months +0.50 · YTD +3.26 | VULCAN 63-session leg on its own method: −0.50pp 10/29 → +0.94pp 10/30 (reproduced) |
| QQEW/QQQ relative | 1 day +0.22 · October −0.38 · YTD −5.59 | equal weight lags inside the Nasdaq-100 this year |
| Small / mid vs SPY, 3 months | IWM −5.17pp · IJR −4.56 · MDY −3.67 | October +1.44 / +4.07 / +2.78 |
| Friday: S&P 500 members down | **55.1%** (median member −0.32%) | SPY ≤ −1.3% days since 1/2025 (32): median 75.8%; Friday 4th narrowest of 33 |
| Friday: index arithmetic | Mag-7 −0.68pp + 18 other chip makers −0.76pp = **79%** of −1.82% | other 476 members −0.38pp (median −0.16%) |
| Friday: new 52-week highs / lows (intraday) | S&P 500 **42 / 5** · S&P 1500 87 / 19 | S&P 1500 weekly name-days: w/e 10/2 72 / 410 → w/e 10/30 282 / 112 |
| S&P 500 A/D line (cumulative from 2025-01-02) | 7,393 | peak 8,160 (8/14) · 5,946 (9/30) |

**Read:** concentrated at the 10/6 record, broadening since; Friday narrow at the index level and broad only inside tech (80% of S&P 500 IT members down; QQEW/QQQ an ordinary-breadth Nasdaq day); three-month small/mid damage only partly repaired. Constituent counts are computed from members' own closes (not the exchange A/D series, which was not reached); survivorship: today's members applied backwards. Not a threshold, monitor or prediction. Files `research/2026-10-31_L616_breadth/`; memo `PROME/inbox/2026-10-31_from-HENRY_L616-market-breadth.md`.

## THESIS / INVALIDATION TRIAD

| Axis | Current judgment |
|---|---|
| Cyclical | Inflation pressure persists (September CPI/PPI hot on energy; core PCE +0.3% m/m, 3.1% y/y [BEA 10/29]; ISM prices 75.2 manufacturing / 73.0 services [Oct]) while activity holds (ISM 55.5 / 54.5 [Oct]). Oil fell hard into 11/4 and rose back this morning (BZ=F bar 97.47, not a settle). Treasury par 11/4: 2Y 4.58%, 10Y 4.90%, 30Y 5.28%. |
| AI-capex | HEN-36 mechanism RESOLVED-CONFIRMED; class-wide de-rate expression FALSIFIED. Q3 hyperscaler cluster closed with **no capex cut** (VULCAN 10/30: AMZN held ~$220B for 2026, TTM FCF −$42.4B; §4b NO-VERDICT). The market sold the spend: GOOGL −12.64% (10/29), then on 10/30 SOXX −8.24%, INTC −28.58% on its results, NVDA −4.22%, QQQ −3.47% vs RSP −0.79% (VULCAN owns the capex grade; HEN-36 re-read: nothing in VULCAN's packet changes its resolution). **11/4–11/5 repeated the pattern without a capex event:** chips fell through the election relief and led 11/5 down; AMD beat its quarter on 11/3 (press) and traded −10.73% at 09:45 ET 11/5. |
| Structural credit | Tail stress persists (CCC 1,316bp RED, CCC−BB 1,113bp [FRED 11/3]); broad HY **340bp, four observations over 320**, tiers BROADENS (LIQUID 11/4). Funding not confirmed. Not AI-led on the rated CCC tier (DEWEY 10/23). |

**Standing Will rule (8/10):** VIX < 15 AND HY < 260 on the SAME session, five consecutive; non-latching. **Joint count 0** (HY 340 [11/3] > 260; VIX 16.61 [11/4] > 15).

## ACTIVE THRESHOLDS — ALL STANDING LEVELS UNCHANGED

| Metric | Current [source date] | Yellow / Orange / Red | State |
|---|---|---|---|
| ISM manufacturing PMI | 55.5 [ISM Oct] | <50 / <48 / <47 | NOT FIRED. **The <47 trigger is ISHM's since 2026-10-23 (WQ-507 A)** |
| ISM manufacturing employment | 52.4 [ISM Oct] | <47 / <45 / <43 | NOT FIRED |
| ISM manufacturing prices | 75.2 [ISM Oct] | >60 / >70 / >75 | RED observation (0.2 over) |
| PPI FD m/m | +1.3% [BLS Sep, 10/15] | >0.4 / >0.5 / >0.6 | RED observation; next print 11/13 |
| Core PCE m/m | +0.3% [BEA Sep, 10/29] (unrounded +0.32%) | >0.3 hot | NOT FIRED |
| VIX | **16.61 [FRED VIXCLS 11/4]**; 11/5 Cboe 17.50 delayed (~09:33 ET) | >23 / >28 / >30 sustained | NOT FIRED (6.39 below 23) |
| SPX | **7,688.62 [vendor 11/4]**; 7,577.69 intraday 09:52 ET 11/5 | <7,200 / <7,100 / <6,494 | NOT FIRED (378 above 7,200 intraday); gamma **NEGATIVE both**, flip 7,693–7,696 [11/5] |
| KRE | $74.13 [vendor 11/4] | <$65 / <$62 / <$60 | NOT FIRED |
| 10Y | **4.90% [Treasury par 11/4]** | >4.5 / >4.8 / >5.0 | ORANGE (10bp under red) |
| 2Y / 30Y | **4.58% / 5.28% [Treasury par 11/4]** | >4.25 / >4.40 / >4.60 · >5.0 / >5.25 / >5.50 | **2Y ORANGE (2bp under red; was RED 4.61 on 11/3)**; 30Y ORANGE (22bp under red) |
| HY OAS | **340bp [FRED 11/3]** | >320 / >400 / >500 | **YELLOW** (20bp over) |
| CCC OAS | 1,316bp [FRED 11/3] | >900 / >1000 / >1100 | RED |
| USD/JPY | 158.47 [vendor 11/4, +0.35%] | absolute daily change ≥2%, SAM's call | NOT FIRED |
| SKEW | 150.90 [vendor 11/4] | >145 / >150 / >160 | ORANGE (RED-FT-10 owner grade separate) |
| VIX kill leg | **16.61 [FRED VIXCLS 11/4]** | <17 / <16 / <15 one session | **YELLOW on the 11/4 close** (was NOT FIRED); leg only, the kill needs the HY leg too |
| HY kill observable | 340bp [FRED 11/3] | <290 / <270 / <260 ×5 | NOT FIRED |

## CROSS-DESK / CATALYST STACK / GAPS

- **Next:** HEN-59 October payrolls Fri 11/6 08:30 ET, L767 co-reader, frozen expectation FIRED (<100K); HEN-57 CPI Tue 11/10 (L775; expect NOT FIRED, +0.2); BIS and MOFCOM clocks 11/10 (L435/L437, co-owned); HEN-58 PPI Fri 11/13 (L776; expect NONE ≤0.4); PANW + bank-stock legs of CYPHER row 9 on 11/18; NVDA 11/19 (L322). Letter `research/2026-10-29_catchup/PREREG_nov-releases.md`.
- **Row 9 magnitude gap** (no number for "vector-vendor collapse") still with PROME/CYPHER; needed before 11/18.
- **VLO line (SIG-W-20261104-077):** $90.16 and the HOZ26×42 − CLZ26 basis confirmed to TERRY 11/5 (packet in its inbox). TERRY owns the gate; CME unread; no order implied. HEN-46 itself resolved 10/22, so "thesis-dead" is historical wording.
- **Diesel and refining (BRENT commission, DOCKET 11/20):** my crack estimate is BRENT's input; Russian producer ban through 1/31/2027 (SIG-W-20261031-001).
- **ISHM (11/4, two packets, read and filed):** Q3 core orders/shipments +3.638% / +3.939% nominal q/q (mixed vintages), Emerson underlying orders +14% ex-AspenTech, five October rail weeks positive y/y. Real buying better supported; breadth still qualified by hardware and weak Europe/China. Equity read: supports cyclical activity, does not offset chip repricing.
- **CYPHER 11/2 (read and filed):** COIN's 10/30 residual faded to −2.59pp (z −0.9) by the close; no name priced Binance venue risk beyond bitcoin-plus-Nasdaq beta. No HENRY line.
- **Instrument note:** SOXX printed 450.41 → ~141 on 11/5 with no vendor split record (SMH −5.6% implies a ratio near 3.2). Unconfirmed share-count change; quote no SOXX % for 11/5 until confirmed. Use SMH.
- **Inbox (11/5):** drained, 19 WALTER cards logged in `board_log.tsv` (8 acted, 3 noted, 8 info-only) and filed, 4 general packets filed. DOCKET L565 (WATCH_FOR, dated 11/3) names HENRY outstanding, but HENRY answered 10/2 (510b067c0) and the set never landed; current answer sent 11/5: land an empty HENRY list. `boot.py` due-scan: none overdue.
- **Still open:** PROME to land the empty WATCH_FOR list (L565); Operating Dashboard refresh; OI-vintage proof not run 11/5; consumer check for superseded flips at closeout.
- **Runtime:** Claude Code (Opus 5.5), terminal + web + cross-session messaging. MCP connectors Definite, MT Newswire and Desktop Commander failed to connect; none needed; Quartr not called. bls.gov 403 from this box; cmegroup.com not approached.
