# HENRY STATUS

**Last owner update:** 2026-11-21 18:2x ET, PROME due-row wake launched LATE (prome-77 letter 18:02 ET 11/21; the laptop slept about 14:53 ET 11/20 to 17:50 ET 11/21, so the 16:05 ET 11/20 close read never ran; Claude Code, Opus 5.5 `claude-opus-5-5`, laptop). **S&P 500 closed 6,910.39 on Fri 11/20 (−3.70%; vendor bar, FRED Monday): 126.65 under the red line 7,037.04, −11.62% from peak. RED LINE FIRED → signal to WALTER for CARL and PROME. HEN-64 event YES (grades on FRED). HEN-65 registered 0.40.** Dealer gamma NEGATIVE and flat from about 6,400 to 7,100 on my rebuild (vendor chain, VIX-term volatility; vendor weekend IVs broken; Cboe 403), not published. Record `research/2026-11-21_close-read/CLOSE.md`. The 11/20 header and VIEW: `STATUS_COLD.md` § ROT-11/21.

## VIEW — 11/20 CLOSE, READ SAT 11/21 18:02–18:10 ET (record `research/2026-11-21_close-read/CLOSE.md`)

**The S&P closed through the red line on a chip-led day, with rates rallying and credit not yet following; dealers are short gamma at a flat rate from about 6,400 to 7,100, so Monday's moves get amplified in both directions.** Close 11/20 (vendor bars): S&P 6,910.39 (−3.70%; two sessions −5.64%), NDX −5.61%, SMH −10.60%, NVDA −14.01%, vs RSP −1.98%, IWM −2.88%, KRE −1.36%, HYG −0.26%. Treasury par 2Y 4.63 (−13bp), 10Y 4.92 (−12bp). VIX 35.89 PROVISIONAL (vendor; no Cboe settle proof, VIXCLS unposted), VIX9D 40.72 over VIX3M 30.94 (0.862). The red line broke before noon (7,024.16 at the 12:00 bar); Reuters' SEC-Nvidia report (14:16, zone not shown; VULCAN's evidence, unchecked) coincides with the last leg: NVDA −9.85% at the 14:15 bar, −14.01% at the close. **Map (rebuild):** NEGATIVE −52 to −57 $B per 1% at spot, flat 6,400–7,100, flip band about 7,420–7,680 (assumption-dependent). KRE beat IWM by 1.5 points while yields fell: not a bank-credit read, no REGINALD flag. **D:L823:** from 11/4, KRE −7.8%, QQQ −12.1%; UNRESOLVED to 2027-01-20/02-18. **H4:** credit lagging on Friday's ETF tape; FRED HY 11/20 posts Monday. ⚠️ Free-tier proxy; volatility is my assumption, not market IV; open interest excludes Friday's trades.

**PROJECTION (moves nothing; separate events, not one distribution):** **HEN-65** (close at or under 6,700 on any session 11/23–12/4) registered **0.40** (base rates 32–48%, own calc since 1990). A close back over 7,037.04 in the same window: about **65%**, unscored (base 68–75%). Monday 11/23: about 60% a higher close, about 1 in 3 a move over 2% either way, unscored. Changes my mind: downside, FRED HY 11/20 at or over about 370 with HYG under about $75.50, or KRE falling with QQQ; upside, a close over about 7,200 with VIX under 30.

## GAMMA MAP — LAST PUBLISHED 11/19 12:17 ET (`gamma_flip.py --both --spot <vendor live> --publish`; chain asof 11/19 = 11/18 open interest)

| Chain (Cboe) | Spot | Flip 14d / 35d | Net gamma 14d / 35d ($B per 1%) | Put wall | Call wall |
|---|---|---|---|---|---|
| **SPX 11/19 12:17 ET (PUBLISHED)** | 7,203.64 (vendor; Cboe feed 7,247.84) | **7,498 / 7,517** | **NEGATIVE −58.6 / −85.7** (trough −87.2 at 7,150) | **⛔ WITHHELD:** put = call at 7,000 at both horizons | **7,000** published as the DOMINANT TWO-SIDED STRIKE, 204 points UNDER spot, not resistance; largest 11/20 open interest |
| **QQQ 11/19 12:17 ET (PUBLISHED)** | 648.76 (vendor) | **668 / 669** | **NEGATIVE −2.4 / −3.5** | **650**, near-tie BAND 640–650 at both: quote the band; spot inside it | **⛔ WITHHELD:** 14d 665 vs 35d 700; supersedes 680 [10:05] |
| SPX 11/20 close, rebuilt Sat 11/21 18:0x ET (NOT PUBLISHED: vendor open interest through 11/19 trades, VIX-term volatility, Cboe 403) | 6,910.39 (vendor close) | **~7,420–7,680** (band across volatility assumptions; 11/20 midday vendor-IV map 7,422–7,440) | **NEGATIVE −52.0 / −55.0 / −56.5** (flat / skew 1 / skew 2, 35d) | largest put strike 7,000 (in the money); not published | largest call strike 8,000; not published |

**So what (11/21, for Monday):** dealers are short gamma across the whole plausible Monday range (flat about −50 to −57 from 6,400 to 7,100; thins above 7,200), so hedging sells into a fall and buys into a rebound; no cushion until about 6,400. VIX 36–41 implies about 2.3–2.6% a day. The 12/18 quarterly holds about 3.39 million of the roughly 6 million contracts within 35 days. The 11/19 rows remain the last PUBLISHED map. Superseded 11/20 rows: `STATUS_COLD.md` § ROT-11/21.

**Levels (SPX, 11/10 bar basis, own calc):** 200-day 7,331.08 · 50-day 7,672.91 · yellow 7,200 · orange 7,100 · red 7,037.04 (−10% from the 10/6 peak 7,818.93, WQ-609 A).

## VOL REGIME / TAPE INPUTS — THROUGH THE 11/20 CLOSE (VIX = FRED VIXCLS; Cboe settle proof unavailable 11/20, the feed is blocked; VIX9D and VIX3M vendor closes; VIOLET grades the broadcast)

| Session | SPX close | VIX settle | VIX9D | VIX3M | Term structure |
|---|---:|---:|---:|---:|---|
| 11/17 | 7,340.53 (−1.03%) | 25.46 | 26.70 | 24.98 | inverted (0.981; front over spot) |
| 11/18 | 7,323.63 (−0.23%) | 24.56 | 23.95 | 24.29 | VIX9D under VIX; VIX3M/VIX 0.989, still under 1 |
| 11/19 | 7,175.83 (−2.02%, vendor; FRED not posted) | 28.44 (FRED VIXCLS 11/19; Cboe settle proof unavailable 11/20, blocked) | 29.26 | 27.03 | inverted (0.950) |
| **11/20 close** | **6,910.39 (−3.70%, vendor; FRED Monday)** | **35.89 PROVISIONAL** (vendor bar; Cboe settle proof blocked; VIXCLS unposted) | 40.72 | 30.94 | **inverted, steep (0.862)** |

**Cascade conditions:** vol-control (VIX over 23–24) met on the 11/17, 11/18 and 11/19 settles and the 11/20 close (35.89, provisional); short-term CTA (SPX under its 50-day, 7,672.91 on the 11/10 basis, not recomputed) met; S&P under its 200-day (7,331.08, 11/10 basis) on every close since 11/17 (11/20 about 5.7% under); medium and long triggers have no sourced level and the dollar sizes are unsourced; GEX NEGATIVE and flat to about 6,400 (§ GAMMA MAP, rebuild). VVIX 138.03, SKEW 138.84 (vendor closes 11/20; SKEW last Cboe-confirmed 153.55 [11/6]; Cboe blocked since 11/20). 11/16 row and the 11/19 intraday rows: `STATUS_COLD.md` § ROT-11/20.

## CREDIT EARLY-WARNING MONITOR — FRED THROUGH 11/19 (read 11:35 ET 11/20)

| Series | 11/13 | 11/16 | 11/17 | 11/18 | 11/19 |
|---|---:|---:|---:|---:|---:|
| HY OAS | 323bp | 334bp | 343bp | 347bp | **352bp** |
| BB OAS | 186bp | 196bp | 204bp | 205bp | **210bp** |
| CCC OAS | 1,316bp | 1,310bp | 1,329bp | 1,353bp | **1,361bp** |
| CCC−BB | 1,130bp | 1,114bp | 1,125bp | 1,148bp | **1,151bp** |

**11/19 (FRED, read 11:35 ET 11/20; WALTER FLASH 20261120-001): HY 352, five sessions up and the 2026 high (2026 window; the series' last close at or above 352 was 353 on 2025-05-09), first 2026 close over 350: REGINALD's REG-T-04 day 1 of 3 (REGINALD grades; REG-37 is its projection row). BB 210, CCC 1,361 (RED), CCC−BB 1,151. HYG −0.26% on the 11/20 close while the S&P fell 3.70%: credit is following, not leading (H4 as amended 11/20). FRED 11/20 posts Mon 11/23.** The 11/17 note: `STATUS_COLD.md` § ROT-11/20.

## RELEASES SINCE 11/2

| Release | Actual | Consensus | Prior | Market reaction | Read |
|---|---:|---:|---:|---|---|
| **PPI Oct (11/13)** | **final demand +0.3% (+0.348%) SA; goods +0.5, services +0.2, foods +1.3, energy −0.1, less F&E +0.3, less F,E,trade +0.5; NSA y/y +6.5%** | 0.4 (press relay, unverified) | Sep +1.4 (revised from +1.3), y/y +6.3 | ES +24 pts on the 08:30 bar, vendor 10Y −3bp, both gone by 09:25; cash S&P open +0.32%, then −1.10% at 10:20 ET and a 7,499.40 print at 10:22 ET; vendor 10Y 5.15–5.17; chips led | **HEN-58 NONE; expectation HIT, graded ~1h50m late, disclosed.** Soft services did it. The market did not take the soft print as relief past the open. Figures: api.bls.gov index data; bls.gov release 403. `research/2026-11-13_ppi/` |
| **CPI Oct (11/10)** | **core +0.3% (+0.296%), headline +0.4% (+0.350%); energy +0.70%, gasoline +1.04%, food +0.47%, shelter +0.31%, core services +0.34%, core goods +0.16% (SA)** | core 0.22, headline 0.23 (Bloomberg survey, relay); Dow Jones 0.2 / 0.3 (press) | Sep core +0.3 (+0.335%), headline +0.6 (+0.648%) | ES −0.55% on the 08:30 bar, no extension; SPX −0.64% at 11:10 ET; ZQZ26 to 95.920 (hike fully priced plus about 13% of another 25bp); 10Y about +13bp; KRE and IWM −1.3% intraday; **close** SPX −0.38%, VIX −2.31%, 2Y par 4.73% (+17bp), 10Y par 4.98% (+10bp) | **HEN-57 NOT FIRED; expectation HIT on the verdict, 0.1 low on the level; graded late, disclosed.** Hot to consensus on both, third straight 0.3 core; supports the hike side of the path. Year-on-year not published by BLS for October (2025 shutdown gap, press). Figures: api.bls.gov index data; BLS one-decimal wording via press (bls.gov 403). `research/2026-11-10_cpi-grade/` |

Since 11/13, not mine to grade: FOMC minutes 11/18 ('almost all' see further hikes likely; KB ML-HEN-234), Philadelphia Fed 11/19 (prices received highest since June 2022, new orders −0.4; KB ML-HEN-235, ISHM grades), claims 11/19 (203K, continuing 1.763M; LABOR grades). Payrolls Oct row: `STATUS_COLD.md` § ROT-11/19. Older rows (ISM, S&P manufacturing, JOLTS, ADP, ISM services, productivity, 11/2-11/5), their sources, the election and breadth notes: § ROT-11/10-CLOSE.

## THESIS / INVALIDATION TRIAD

| Axis | Current judgment |
|---|---|
| Cyclical | Inflation pressure persists (October PPI final demand +0.3% m/m, +6.5% y/y, September revised to +1.4% [BLS 11/13, index data]; October CPI core +0.3%, third straight 0.3, headline +0.4% [BLS 11/10]; September CPI/PPI hot on energy; core PCE +0.3% m/m, 3.1% y/y [BEA 10/29]; ISM prices 75.2 manufacturing / 73.0 services [Oct]) while activity holds (ISM 55.5 / 54.5 [Oct]). October payrolls +165K with wages firm; LABOR stood its freeze thesis down on its own kill rule, a hiring read and not a layoffs read, 15K over the bar on a first print (WALTER 010). Read-through here: the labor leg no longer argues for an equity bid break, and it supports the hike side of the rate path. Brent January about $98.29 on 11/5 (BRENT mark, [EST]). Treasury par 11/10: 2Y 4.73%, 10Y 4.98%, 30Y 5.35% (11/9: 4.56%, 4.88%, 5.26%). December Fed meeting priced as a near-certain hike with about a 1-in-8 chance of a half point (ORACLE KB-ORC-133, 09:45 ET 11/11: Polymarket hold 3.5, +25bp 85.5, +50bp or more 11.8; fed funds futures about +28.9bp as cross-check; ORACLE owns this figure, WQ-671 A). FOMC minutes (11/18): 'almost all' participants see further increases likely; 'a couple' would consider more than 25bp in December if inflation is unfavorable (KB ML-HEN-234). |
| AI-capex | HEN-36 mechanism RESOLVED-CONFIRMED; class-wide de-rate expression FALSIFIED. Q3 hyperscaler cluster closed with **no capex cut** (VULCAN 10/30: AMZN held ~$220B for 2026, TTM FCF −$42.4B; §4b NO-VERDICT). The market sold the spend: GOOGL −12.64% (10/29), then on 10/30 SOXX −8.24%, INTC −28.58% on its results, NVDA −4.22%, QQQ −3.47% vs RSP −0.79% (VULCAN owns the capex grade; HEN-36 re-read: nothing in VULCAN's packet changes its resolution). **11/4–11/5 repeated the pattern without a capex event:** chips fell through the election relief and led 11/5 down; AMD beat its quarter on 11/3 (press) and closed −17.26% on 11/5, SMH −11.21% (vendor). |
| Structural credit | Tail stress persists (CCC 1,361bp RED, CCC−BB 1,151 [FRED 11/19]); broad HY **352bp [11/19]**, YELLOW, the 2026 high (over 348 [11/5]), up five sessions (323, 334, 343, 347, 352); REG-T-04 day 1 of 3 (REGINALD); **LIQUID's above-320 three-day rule MET 11/17, the whole ladder wider (SIG-W-20261118-010)**; funding not confirmed (LIQUID). Not AI-led on the rated CCC tier (DEWEY 10/23). H4 as amended 11/20 (`2beee94614`): credit does not reliably lead the equity break; a quiet credit tape is no all-clear. |

**Standing Will rule (8/10):** VIX < 15 AND HY < 260 on the SAME session, five consecutive; non-latching. **Joint count 0** (HY 352 [FRED 11/19] > 260; VIX 28.44 [FRED VIXCLS 11/19] > 15; 35.89 provisional 11/20).

## ACTIVE THRESHOLDS — ALL STANDING LEVELS UNCHANGED

| Metric | Current [source date] | Yellow / Orange / Red | State |
|---|---|---|---|
| ISM manufacturing PMI | 55.5 [ISM Oct] | <50 / <48 / <47 | NOT FIRED. **The <47 trigger is ISHM's since 2026-10-23 (WQ-507 A)** |
| ISM manufacturing employment | 52.4 [ISM Oct] | <47 / <45 / <43 | NOT FIRED |
| ISM manufacturing prices | 75.2 [ISM Oct] | >60 / >70 / >75 | RED observation (0.2 over) |
| PPI FD m/m | **+0.3% [BLS Oct, 11/13, index data; release text 403]**; Sep revised +1.4% (first print +1.3% [10/15]) | >0.4 / >0.5 / >0.6 | **NOT FIRED: HEN-58 RESOLVED NONE 11/13** (0.1 under the yellow line); next print December |
| Core PCE m/m | +0.3% [BEA Sep, 10/29] (unrounded +0.32%) | >0.3 hot | NOT FIRED |
| VIX | **35.89 [vendor close 11/20, PROVISIONAL]**; 28.44 [FRED VIXCLS 11/19]; 24.56 [11/18] | >23 / >28 / >30 sustained | **over 30 on one provisional close** (5.89 over); ORANGE close 11/19. Grade on FRED VIXCLS 11/20. VIOLET owns the broadcast |
| SPX | **6,910.39 [vendor close 11/20, −3.70%; FRED not posted]**; 7,175.83 [FRED 11/19] | <7,200 / <7,100 / **−10% from cycle peak** (7,037.04 at the 7,818.93 close of 10/6; recomputes at a new peak; WQ-609 A, Will 11/5) | **RED: FIRED on the 11/20 close** (126.65 under, −11.62%; first close under it); signal to WALTER for CARL and PROME 11/21. **HEN-64 event YES** (grades on FRED SP500 11/20). HEN-65 open. Walls: none published since 11/19 12:17 ET |
| KRE | **$68.32 [vendor close 11/20, −1.36%]**; $69.26 [11/19] | <$65 / <$62 / <$60 | NOT FIRED (3.32 over yellow) |
| 10Y | **4.92% [Treasury par 11/20, first published, read 18:03 ET 11/21; 2Y 4.63, 30Y 5.31]**; 5.04% [par 11/19]; 5.07% [11/18] | >4.5 / >4.8 / >5.0 | **ORANGE: first par close under 5.0 since 11/10 (4.98)**; six straight red closes 11/12–11/19 ended. WALTER routed the red cross as SIG-W-20261112-008 (ACTION BROCK) |
| 2Y / 30Y | **4.63% / 5.31% [Treasury par 11/20]**; 4.76% / 5.40% [par 11/19] | >4.25 / >4.40 / >4.60 · >5.0 / >5.25 / >5.50 | **2Y RED (3bp over 4.60, −13bp on the day); HEN-62 RESOLVED-HIT 11/10.** 30Y ORANGE (6bp over 5.25); 20Y 5.34% |
| HY OAS | **352bp [FRED 11/19; BB 210]**; 347 [11/18] | >320 / >400 / >500 | **YELLOW** (32 over 320); the 2026 high; REG-T-04 (over 350 ×3) day 1 of 3; LIQUID and REGINALD grade the HY rows |
| CCC OAS | **1,361bp [FRED 11/19], CCC−BB 1,151** | >900 / >1000 / >1100 | RED |
| USD/JPY | 158.72 [vendor 16:21 ET 11/10]; 158.74 [~11:09 ET] | absolute daily change ≥2%, SAM's call | NOT FIRED (+0.47% at 11:09 ET; vendor daily bar mis-dated, close change not computed) |
| SKEW | **153.55 [Cboe History 11/6]** (149.37 [11/5]) | >145 / >150 / >160 | **ORANGE on 11/6** (3.55 over 150, was YELLOW 11/5); RED-FT-10 owner grade separate |
| VIX kill leg | 28.44 [VIXCLS 11/19] | <17 / <16 / <15 one session | NOT FIRED (11.44 over 17) |
| HY kill observable | 352bp [FRED 11/19] | <290 / <270 / <260 ×5 | NOT FIRED |

## CROSS-DESK / CATALYST STACK / GAPS

- **11/21 late wake (prome-77 letter 18:02 ET 11/21):** (1) Boot 17.0 s; predictions due none (HEN-64 4d); corrections check rc 1 → COR-20261120-12 receipted NO-OP. (2) **WALTER lane 3 drained** (board_log, `git mv`): 20261120-005 Poland info-only, 012 correction noted, 013 Kansas City Fed noted (KB ML-HEN-241 combo). General inbox 1: TERRY's 11/20 ask (answered 11/20, now committed by TERRY) moved to processed. (3) **Close read:** red line FIRED, signal `AGENTS/WALTER/inbox/2026-11-21_from-HENRY_SPX-red-line-fired-11-20-close.md`; HEN-64 event YES, grades on FRED; HEN-65 registered 0.40; TERRY handoff `AGENTS/TERRY/inbox/2026-11-21_from-HENRY_red-line-close-and-negative-gamma-tradeability.md`. (4) **Map rebuilt, not published.** ⚠️ The boot kit's gamma step and one `gamma_flip.py` call each sent one ordinary request to Cboe on the script's default before I switched to the vendor source by hand; both 403, no workaround. (5) Scorer note: HEN-60 to HEN-64 confidences are each the YES probability as lettered.
- Rotated 11/21 18:1x ET to `STATUS_COLD.md` § ROT-11/21 (verbatim): the 11/20 header, VIEW and PROJECTION, the unpublished 11/20 gamma row, the 11/20 intraday vol row, the superseded VIX/SPX/KRE/10Y/2Y-30Y threshold rows, the 11/20 wake, hand-off and runtime bullets.
- **US–China trade clocks, moved from 11/10 to the January 9–11, 2027 cluster (WALTER SIG-W-20261109-010, ACTION HENRY; ZHAO read the primaries 11/9, WALTER relayed, HENRY did not re-read). One row per instrument, never one "1/10 cliff"; ZHAO owns the grades (L435/L437/L858):**
  - USTR s.301 ship fees and Annex V.A crane duties, further suspended (FR 2026-22867): end **11:59 p.m. ET 2027-01-09**.
  - USTR s.301 tech-transfer exclusions, all 178 extended (FR 2026-22925): end **11:59 p.m. ET 2027-01-09**.
  - BIS Affiliates Rule stay (FR 2026-22793, 91 FR 70789): "until January 10, 2027".
  - MOFCOM–GAC 公告**2026年**第58号 suspends the 2025 export-control package (2025 Nos. 55–58, 61, 62; scope of 公告2025年第70号): end **2027-01-10 Beijing**, first uncovered day 1/11. ⚠️ 公告2026年第58号 is the suspension; 公告2025年第58号 is the battery package it suspends.
  - MOFCOM 令2026年第4号, Hanwha Ocean US-unit countermeasures suspended 2 more months from 11/10: **about 2027-01-10** (a duration, not a date).
  - MoT special port fees on US ships (2025 No. 54) and its investigation (No. 55): **2027-01-10**, Chinese press quoting the text, MoT primary unread.
- **Diesel and refining (BRENT commission, DOCKET 11/20):** my crack estimate is BRENT's input; Russian producer ban through 1/31/2027 (SIG-W-20261031-001).
- **Still open:** Operating Dashboard REFRESHED 16:09 ET 11/12 on Will's go-ahead (version 6, same URL https://claude.ai/artifact/W7ALXXxkW4mGJHLHjrbeyr; 16:06 ET close, Treasury par 11/12 with the 10Y red cross, 16:06 ET gamma, put-wall wording corrected; version 5 at 12:1x ET was the midday tape); breadth rerun and options volume by strike not run; FRED SP500 and VIXCLS 11/6 not posted (Cboe confirms VIX 25.64); Brent and gas MARKET_DATA cells stay blank, BRENT owns the settle. Fleet consumer sweep timed out at boot again (180s). `PUBLISHED.tsv` now says none published with a `NONE` value row (QQQ walls 11/9); SPX `put_wall` resolves to 7,500 [11/9].
- **Next:** (1) **Mon 11/23:** FRED SP500 11/20 → grade HEN-64 (HIT if under 7,100; Brier 0.36) and confirm the red-line close; FRED VIXCLS 11/20 → VIX cell; FRED HY/BB/CCC 11/20 (REG-T-04 day 2, REGINALD grades) — my changes-my-mind marker is HY at or over about 370. (2) Monday close read: HEN-65 window opens (close at or under 6,700). (3) Cboe: refused since 11/20; do not retry around it; the boot kit's default still tries it first (a `--source` switch for `gamma_flip.py`/`boot.py` is a draft for PROME, not done). (4) HEN-64 resolves 11/25; FOMC 12/9 (HEN-63 0.70); D:L823 2027-01-20 to 02-18; dashboard v6 (11/12) stale; LESSONS.md rotation (76%); DAEDALUS K38–K52 at an ordinary wake. (5) NEXUS_BRIEF: figures changed this session (red line, HEN-64, HEN-65); rewrite at closeout (step 10).
- **Runtime (11/21 laptop):** Claude Code (Opus 5.5, `claude-opus-5-5`); SendMessage available as a deferred tool. Working: vendor quotes, bars and chains (chain IV fields broken on the weekend), FRED, Treasury par CSV, `corrections_boot_check.py`. **Blocked: Cboe delayed-quote API (403 since 11/20).** Absent on the laptop (PROME/MACHINE_LOCAL.md): Kalshi credentials, gh token, CourtListener token, none needed. Definite, MT Newswire and desktop-commander connectors failed to connect; not needed. Quartr not called.
