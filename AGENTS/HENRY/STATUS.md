# HENRY STATUS

**Last owner update:** 2026-11-25 16:36 ET, D:L1271 close check (Will's window henry-7d; Will's word 16:15 ET via PROME prome-77; Claude Code, Opus 5.5 `claude-opus-5-5`, laptop). **S&P 7,182.78 (−0.25%): red 7,037.04 NOT FIRED (145.74 over), YELLOW (17.22 under 7,200). RSP 215.74, +0.83%, so 11/25 cannot be a broadening day. VIX 28.29 (vendor stamp 16:15:01): ORANGE. All vendor, PROVISIONAL until FRED.** Record `research/2026-11-25_close-check/CLOSE.md`.

## VIEW — WED 11/25 AFTER THE CLOSE

**The selloff reversed inside the day and the average stock finished up; options did not believe it.** Low 6,970.11 at 09:45, last one-minute close under 7,037.04 at 12:00, high 7,199.31 at 14:32; cause not established. RSP +0.83%, IWM +0.65%, KRE +0.10%, HYG +0.12%, SMH −1.01%, NVDA −3.91%. VIX rose 1.93 on a −0.25% day and VIX3M/VIX is 0.929, inverted. Standing read unchanged: equities and credit are on two clocks (HY about +100bp since 9/21 while equal-weight is flat; `research/2026-11-24_credit-equity-read/READ.md`); stress is AI equity and single-name AI credit. CoreWeave: no valid 11/25 five-year swap to 11:45 ET, 5Y 1,314 [11/24] (WALTER 022). Mortgage-servicer bonds do NOT show broadening: Freedom alone is wide (LIQUID b2d692e862, evaluated prices, two dates, none for 11/25).

**Own midday read graded:** "close under red today about 65%" (unscored) MISSED; the 7,000 pin held 10:15–11:48 and released upward, which the read did not name; "equal-weight on light volume" superseded (RSP 1.20× its median for the day). October PCE split stands (goods-led, ML-HEN-247).

**PROJECTION, 16:36 ET 11/25 (unscored; moves nothing; HEN-65 letter frozen at 0.40):** Friday close under 7,037.04 about **8%**, under 7,200 about **55%** · close under 7,037.04 by 12/4 about **40%** (was 80) · HEN-65 (≤6,700 by 12/4) about **6%** (was 12) · range 7,000–7,450 / credit-led broadening / V repair **50 / 30 / 20** to 12/4–12/9. Alternative: the 09:45 low was a wash-out (VIX under 26, HY ≤363). Toward broadening: HY over 376 on a day RSP falls, KRE under $65, HYG under $75.50, a close under 6,970. Toward repair: a close over 7,200 with RSP up and HY ≤350. **December hike:** HEN-63 0.70 registered, not re-marked; futures ≈93% at 11:30 ET.

## GAMMA MAP — LAST PUBLISHED 11/19 12:17 ET (`gamma_flip.py --both --spot <vendor live> --publish`; chain asof 11/19 = 11/18 open interest)

| Chain (Cboe) | Spot | Flip 14d / 35d | Net gamma 14d / 35d ($B per 1%) | Put wall | Call wall |
|---|---|---|---|---|---|
| **SPX 11/19 12:17 ET (PUBLISHED)** | 7,203.64 (vendor; Cboe feed 7,247.84) | **7,498 / 7,517** | **NEGATIVE −58.6 / −85.7** (trough −87.2 at 7,150) | **⛔ WITHHELD:** put = call at 7,000 at both horizons | **7,000** published as the DOMINANT TWO-SIDED STRIKE, 204 points UNDER spot, not resistance; largest 11/20 open interest |
| **QQQ 11/19 12:17 ET (PUBLISHED)** | 648.76 (vendor) | **668 / 669** | **NEGATIVE −2.4 / −3.5** | **650**, near-tie BAND 640–650 at both: quote the band; spot inside it | **⛔ WITHHELD:** 14d 665 vs 35d 700; supersedes 680 [10:05] |
| SPX 11/25 16:17 ET, after the close, vendor chain (NOT PUBLISHED: non-Cboe) | 7,182.89 | **~7,357 / ~7,399** | **NEGATIVE −19.0 / −43.9** | 7,000 at both horizons (14d near-tie band 7,000–7,150); not published | WITHHELD: 14d 7,200 vs 35d 7,400 |

**So what:** spot 174–216 under the flip band; dealers still amplify both ways until about 7,360–7,400. Compare flips, not $B, across days. The 11/19 rows remain the last PUBLISHED map. Earlier unpublished rows: `STATUS_COLD.md` § ROT-11/25.

**Levels (SPX, 11/25 vendor basis, own calc):** 200-day 7,352.49 · 50-day 7,602.53 · yellow 7,200 · orange 7,100 · red 7,037.04 (−10% from the 10/6 peak 7,818.93, WQ-609 A).

## VOL REGIME / TAPE INPUTS — THROUGH THE 11/25 CLOSE (VIX = FRED VIXCLS where posted, else vendor; Cboe blocked since 11/20; VIX9D and VIX3M vendor closes; VIOLET grades the broadcast)

| Session | SPX close | VIX settle | VIX9D | VIX3M | Term structure |
|---|---:|---:|---:|---:|---|
| 11/19 | 7,175.83 (−2.02%, FRED SP500 11/19) | 28.44 (FRED VIXCLS 11/19; Cboe settle proof unavailable 11/20, blocked) | 29.26 | 27.03 | inverted (0.950) |
| **11/20 close** | **6,910.39 (−3.70%; FRED SP500 11/20)** | **35.89 (FRED VIXCLS 11/20, confirms the vendor bar)** | 40.72 | 30.94 | **inverted, steep (0.862)** |
| **11/23 close** | **7,237.17 (+4.73%; FRED SP500 11/23)** | **26.62 (FRED VIXCLS 11/23)** | 27.76 | 25.50 | inverted (0.958) |
| **11/24 close** | **7,201.09 (−0.50%; FRED SP500 11/24, read 11:39 ET 11/25, = vendor bar)** | **26.36 (FRED VIXCLS 11/24 = vendor bar;** pre-open vendor prints 30.00–30.40 at 08:13–08:20 ET, regular-session high 29.57, WALTER 20261124-001) | 26.68 | 25.47 | inverted (0.966) |
| **11/25 close (PROVISIONAL)** | **7,182.78 (−0.25%; vendor bar; FRED unposted 16:34 ET)**, low 6,970.11 | **28.29 (vendor, stamp 16:15:01, read 16:34 ET)**, high 34.95 at 09:45 | 29.61 | 26.29 | inverted (0.929) |

**Cascade conditions:** vol-control (VIX over 23–24) met on every settle 11/17–11/25 (28.29); short-term CTA (SPX under its 50-day, 7,602.53) met; S&P under its 200-day (7,352.49) on every close since 11/17 (11/25 about 2.3% under); medium and long triggers have no sourced level and the dollar sizes are unsourced; GEX NEGATIVE (§ GAMMA MAP). VVIX 115.38 (vendor 11/25); SKEW 139.16 (vendor 11/24, 11/25 stale).

## CREDIT EARLY-WARNING MONITOR — FRED THROUGH 11/24 (read 11:39 ET 11/25)

| Series | 11/17 | 11/18 | 11/19 | 11/20 | 11/23 | 11/24 |
|---|---:|---:|---:|---:|---:|---:|
| HY OAS | 343bp | 347bp | 352bp | 376bp | 363bp | **372bp** |
| BB OAS | 204bp | 205bp | 210bp | 229bp | 219bp | **225bp** |
| CCC OAS | 1,329bp | 1,353bp | 1,361bp | 1,402bp | 1,387bp | **1,405bp** |
| CCC−BB | 1,125bp | 1,148bp | 1,151bp | 1,173bp | 1,168bp | **1,180bp** |

**11/24 is the latest FRED cell; 11/25 posts about 11/26–27 (D:L1272).** HY 372 YELLOW, CCC 1,405 RED, CCC−BB Δ5d +55, ~3mo +302. HYG/LQD −1.36% over 5 sessions (15:34 ET 11/25). REG-T-04 fired 11/23 (REGINALD grades). H4: a quiet credit tape is no all-clear. Earlier notes: `STATUS_COLD.md` § ROT-11/25.

## RELEASES SINCE 11/2

| Release | Actual | Consensus | Prior | Market reaction | Read |
|---|---:|---:|---:|---|---|
| **PCE Oct (BEA 11/25, first published)** | **core +0.3% m/m (+0.2925%), 3.3% y/y (3.261%); headline +0.3% (+0.3175%), 3.8% y/y (3.845%); real PCE 0.0%; income +0.7%, real DPI +0.5% (Medicare rebate one-off); saving rate 4.1%. Split (table 2.4.4U, midday): core goods +0.35%, housing +0.29%, services ex energy and housing +0.27% (ML-HEN-247)** | **not sourced by HENRY**; core y/y 3.2 per a Newsquawk listing (WALTER 007, relay) | Sep core +0.3% (revised +0.317 → +0.325%), 3.1% y/y; Sep headline +0.49 → +0.50%; Aug core +0.262 → +0.274%; Sep saving rate 3.8 → 3.6 (ALFRED vintage 11/24) | ES 7,084.50 (08:29) → 7,068.50 (08:32), −0.23%, vendor 1-min (~10 min delayed); ZN +3/32 then back; the −2% morning is the chip selloff | **Core hot line (>0.3) NOT FIRED (0.29).** Steady 0.3 core, year rate up on a soft base, revisions up, real spending flat two months: hike side of the rate path holds (HEN-63 not re-marked), consumer weaker. Core 3-month annualized 3.63% (own calc). KB ML-HEN-245. Durable goods (Census) not read |
| **GDP Q3 second estimate (BEA 11/25)** | **real GDP +4.3% SAAR** (advance +3.4, revised up 0.9 on investment and consumer spending); real final sales to private domestic purchasers +5.8%; GDI +4.4%; gross domestic purchases prices +2.7% (from 3.0); Q3 PCE prices 2.1 / core 2.5, unrevised; corporate profits +$206.0B (Q2 +$384.0B) | not sourced | Q2 +2.2% | same 08:30 bar as PCE (above) | Q3 activity strong, so the hike case gains (HEN-63 not re-marked); October's flat real PCE is the first soft month of Q4. Source: bea.gov/data/gdp/gross-domestic-product and the 11/25 release page, read 09:1x ET |

October CPI (core +0.3%) and PPI (final demand +0.3%) rows: `STATUS_COLD.md` § ROT-11/25. Since 11/13, not mine to grade: FOMC minutes 11/18 ('almost all' see further hikes likely; KB ML-HEN-234), Philadelphia Fed 11/19 (prices received highest since June 2022, new orders −0.4; KB ML-HEN-235, ISHM grades), claims 11/19 (203K, continuing 1.763M; LABOR grades). Payrolls Oct row: `STATUS_COLD.md` § ROT-11/19. Older rows (ISM, S&P manufacturing, JOLTS, ADP, ISM services, productivity, 11/2-11/5), their sources, the election and breadth notes: § ROT-11/10-CLOSE.

## THESIS / INVALIDATION TRIAD

| Axis | Current judgment |
|---|---|
| Cyclical | Inflation pressure persists (October PPI final demand +0.3% m/m, +6.5% y/y, September revised to +1.4% [BLS 11/13, index data]; October CPI core +0.3%, third straight 0.3, headline +0.4% [BLS 11/10]; September CPI/PPI hot on energy; October core PCE +0.3% m/m (+0.29%), 3.3% y/y from 3.1, headline 3.8% y/y, real PCE flat [BEA 11/25]; ISM prices 75.2 manufacturing / 73.0 services [Oct]) while activity holds (ISM 55.5 / 54.5 [Oct]). October payrolls +165K with wages firm; LABOR stood its freeze thesis down on its own kill rule, a hiring read and not a layoffs read, 15K over the bar on a first print (WALTER 010). Read-through here: the labor leg no longer argues for an equity bid break, and it supports the hike side of the rate path. Brent January about $98.29 on 11/5 (BRENT mark, [EST]). Treasury par 11/10: 2Y 4.73%, 10Y 4.98%, 30Y 5.35% (11/9: 4.56%, 4.88%, 5.26%). December Fed meeting priced as a near-certain hike with about a 1-in-8 chance of a half point (ORACLE KB-ORC-133, 09:45 ET 11/11: Polymarket hold 3.5, +25bp 85.5, +50bp or more 11.8; fed funds futures about +28.9bp as cross-check; ORACLE owns this figure, WQ-671 A). FOMC minutes (11/18): 'almost all' participants see further increases likely; 'a couple' would consider more than 25bp in December if inflation is unfavorable (KB ML-HEN-234). |
| AI-capex | HEN-36 mechanism RESOLVED-CONFIRMED; class-wide de-rate expression FALSIFIED. Q3 hyperscaler cluster closed with **no capex cut** (VULCAN 10/30: AMZN held ~$220B for 2026, TTM FCF −$42.4B; §4b NO-VERDICT). The market sold the spend: GOOGL −12.64% (10/29), then on 10/30 SOXX −8.24%, INTC −28.58% on its results, NVDA −4.22%, QQQ −3.47% vs RSP −0.79% (VULCAN owns the capex grade; HEN-36 re-read: nothing in VULCAN's packet changes its resolution). **11/4–11/5 repeated the pattern without a capex event:** chips fell through the election relief and led 11/5 down; AMD beat its quarter on 11/3 (press) and closed −17.26% on 11/5, SMH −11.21% (vendor). |
| Structural credit | Tail stress persists (CCC 1,405bp RED, CCC−BB 1,180 [FRED 11/24]); broad HY **372bp [11/24]**, YELLOW, under the 2026 high 376 [11/20] (323, 334, 343, 347, 352, 376, 363, 372); CCC 1,405 [11/24]; **REG-T-04 FIRED on 11/23 (REGINALD grades)**; HY +97bp from 266 [9/21] while equal-weight equities are flat over the same window (`research/2026-11-24_credit-equity-read/READ.md`); **LIQUID's above-320 three-day rule MET 11/17, the whole ladder wider (SIG-W-20261118-010)**; funding not confirmed (LIQUID). Not AI-led on the rated CCC tier (DEWEY 10/23). H4 as amended 11/20 (`2beee94614`): credit does not reliably lead the equity break; a quiet credit tape is no all-clear. |

**Standing Will rule (8/10):** VIX < 15 AND HY < 260 on the SAME session, five consecutive; non-latching. **Joint count 0** (HY 372 [FRED 11/24] > 260; VIX 28.29 [vendor settle 11/25] > 15).

## ACTIVE THRESHOLDS — ALL STANDING LEVELS UNCHANGED

| Metric | Current [source date] | Yellow / Orange / Red | State |
|---|---|---|---|
| ISM manufacturing PMI | 55.5 [ISM Oct] | <50 / <48 / <47 | NOT FIRED. **The <47 trigger is ISHM's since 2026-10-23 (WQ-507 A)** |
| ISM manufacturing employment | 52.4 [ISM Oct] | <47 / <45 / <43 | NOT FIRED |
| ISM manufacturing prices | 75.2 [ISM Oct] | >60 / >70 / >75 | RED observation (0.2 over) |
| PPI FD m/m | **+0.3% [BLS Oct, 11/13, index data; release text 403]**; Sep revised +1.4% (first print +1.3% [10/15]) | >0.4 / >0.5 / >0.6 | **NOT FIRED: HEN-58 RESOLVED NONE 11/13** (0.1 under the yellow line); next print December |
| Core PCE m/m | **+0.3% [BEA Oct, 11/25] (unrounded +0.2925%)**; Sep revised +0.325% | >0.3 hot | NOT FIRED (0.0075 under on the unrounded figure); next print 12/23 |
| VIX | **28.29 [vendor settle stamp 16:15:01 11/25, PROVISIONAL]**; 26.36 [FRED VIXCLS 11/24]; 26.62 [11/23]; 35.89 [11/20] | >23 / >28 / >30 sustained | **ORANGE on 11/25** (0.29 over 28; was YELLOW 11/23–11/24). RED on one close (11/20), not sustained; 11/25 high 34.95 is not a close. VIOLET owns the broadcast |
| SPX | **7,182.78 [vendor close 11/25, −0.25%, PROVISIONAL]**; 7,201.09 [FRED 11/24]; 7,237.17 [FRED 11/23] | <7,200 / <7,100 / **−10% from cycle peak** (7,037.04 at the FRED 7,818.93 close of 10/6; recomputes at a new peak; WQ-609 A, Will 11/5) | **YELLOW on 11/25** (17.22 under); orange and red NOT FIRED (82.78 and 145.74 over). Red fired on the 11/20 close (SIG-W-20261121-004). HEN-65 open (3 of 9 sessions closed above 6,700). Walls: none published since 11/19 12:17 ET |
| KRE | **$69.83 [vendor close 11/25, +0.10%]**; $69.76 [11/24] | <$65 / <$62 / <$60 | NOT FIRED (4.83 over yellow) |
| 10Y | **4.85% [Treasury par 11/25, dated XML 16:19 ET]**; 4.91% [11/24] | >4.5 / >4.8 / >5.0 | **ORANGE** (5bp over 4.8, 15 under 5.0) |
| 2Y / 30Y | **4.61% / 5.24% [Treasury par 11/25]**; 4.63% / 5.30% [11/24] | >4.25 / >4.40 / >4.60 · >5.0 / >5.25 / >5.50 | **2Y RED (1bp over 4.60).** **30Y YELLOW (1bp under 5.25; was ORANGE 11/24)**; 20Y 5.28% |
| HY OAS | **372bp [FRED 11/24; BB 225]** (read 11:39 ET 11/25); 363 [11/23]; 376 [11/20] | >320 / >400 / >500 | **YELLOW** (52 over 320, 28 under 400); 2026 high 376 [11/20]; **REG-T-04 (over 350 ×3) FIRED 11/23**; LIQUID and REGINALD grade the HY rows |
| CCC OAS | **1,405bp [FRED 11/24], CCC−BB 1,180** | >900 / >1000 / >1100 | RED |
| USD/JPY | 158.72 [vendor 16:21 ET 11/10]; 158.74 [~11:09 ET] | absolute daily change ≥2%, SAM's call | NOT FIRED (+0.47% at 11:09 ET; vendor daily bar mis-dated, close change not computed) |
| SKEW | **153.55 [Cboe History 11/6]** (149.37 [11/5]) | >145 / >150 / >160 | **ORANGE on 11/6** (3.55 over 150, was YELLOW 11/5); RED-FT-10 owner grade separate |
| VIX kill leg | 28.29 [vendor settle 11/25]; 26.36 [VIXCLS 11/24] | <17 / <16 / <15 one session | NOT FIRED (11.29 over 17) |
| HY kill observable | 372bp [FRED 11/24] | <290 / <270 / <260 ×5 | NOT FIRED |

## CROSS-DESK / CATALYST STACK / GAPS

- **11/25 close check (D:L1271, 16:36 ET):** graded as in § VIEW; no WALTER signal (red not fired; yellow has no registered signal row). Boot at 15:34 ET: 12 WALTER cards and COR-20261125-22 (APPLIED), -23, -35, -36 (NO-OP) done (34ebb1ebf0). ⚠️ That boot ran on default `--source auto` (one Cboe request sent before the vendor fallback), the second time; use `--source vendor`. General inbox 2 of 2: FERT G5 cc (info-only), DAEDALUS byte headroom (acted: this rotation). WALTER 037 is NOT in HENRY's lane (addressed CORAL, AEOLUS, SHADE). Packets: PROME, TERRY. KB ML-HEN-250, -251.
- Rotated 11/25 to `STATUS_COLD.md` § ROT-11/25 (verbatim, 19,205 B).
- **US–China trade clocks, moved from 11/10 to the January 9–11, 2027 cluster (WALTER SIG-W-20261109-010, ACTION HENRY; ZHAO read the primaries 11/9, WALTER relayed, HENRY did not re-read). One row per instrument, never one "1/10 cliff"; ZHAO owns the grades (L435/L437/L858):**
  - USTR s.301 ship fees and Annex V.A crane duties, further suspended (FR 2026-22867): end **11:59 p.m. ET 2027-01-09**.
  - USTR s.301 tech-transfer exclusions, all 178 extended (FR 2026-22925): end **11:59 p.m. ET 2027-01-09**.
  - BIS Affiliates Rule stay (FR 2026-22793, 91 FR 70789): "until January 10, 2027".
  - MOFCOM–GAC 公告**2026年**第58号 suspends the 2025 export-control package (2025 Nos. 55–58, 61, 62; scope of 公告2025年第70号): end **2027-01-10 Beijing**, first uncovered day 1/11. ⚠️ 公告2026年第58号 is the suspension; 公告2025年第58号 is the battery package it suspends.
  - MOFCOM 令2026年第4号, Hanwha Ocean US-unit countermeasures suspended 2 more months from 11/10: **about 2027-01-10** (a duration, not a date).
  - MoT special port fees on US ships (2025 No. 54) and its investigation (No. 55): **2027-01-10**, Chinese press quoting the text, MoT primary unread.
- **Diesel and refining (BRENT commission, DOCKET 11/20):** my crack estimate is BRENT's input; Russian producer ban through 1/31/2027 (SIG-W-20261031-001).
- **Still open:** Operating Dashboard v6 is of 11/12, stale, same URL https://claude.ai/artifact/W7ALXXxkW4mGJHLHjrbeyr; breadth rerun not run; MARKET_DATA Brent, gas and USD/JPY cells blank (BRENT, SAM own); `PUBLISHED.tsv` QQQ walls NONE [11/9], SPX `put_wall` 7,500 [11/9].
- **Next:** (1) FRED SP500 and VIXCLS 11/25 confirm this close; FRED HY 11/25 is read for LEVEL only (D:L1272, Fri 11/27): RSP rose, so the marker cannot fire on 11/25. (2) Friday 11/27 closes 13:00 (options 13:15). (3) Boot and gamma on `--source vendor`; Cboe refused since 11/20, never work around it. (4) HEN-65 and payrolls 12/4; FOMC 12/9 (HEN-63); CPI 12/10; PPI 12/15; PCE November 12/23 (core goods y/y likely up on a −0.05 base); HEN-61 12/31; MOFCOM No. 59 2027-01-27; D:L823 2027-02-18. (5) LESSONS rotation (78%); DAEDALUS K38–K52; registering the broadening letter (enumerate the middle band).
- **Runtime (11/25, laptop):** Claude Code, Opus 5.5; SendMessage loaded. Working: vendor quotes, bars, chains; FRED CSV; Treasury XML (honest client name). Blocked: Cboe, cmegroup.com. Not used: Quartr, web search.
