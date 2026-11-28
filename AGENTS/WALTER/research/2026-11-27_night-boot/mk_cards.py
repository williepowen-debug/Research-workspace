import json
RO = "WALTER night boot 2026-11-27 (Will 'Hi WALTER please boot up', 22:30 ET); step 7j flood check and step 7e lane batch data/2026-11-27/news.json (collector 23:29Z, rewritten after the evening mark)"
cards = []

cards.append(dict(
 id="SIG-W-20261127-017",
 slug="St-Johns-at-Sanford-official-forecast-now-9.0-ft-above-the-8.96-ft-record-issued-Nov-28-01-22Z-observed-8.91-DeLand-6.28-observed-vs-6.33-record-forecast-6.5-this-weekend-6.6-to-Dec-4",
 safety_net="clear", event_window="open", route_origin=RO,
 origin=["NWPS api.water.noaa.gov SNFF1 and DLAF1 stageflow and gauge records, read 2026-11-28T03:35:45Z", "api.weather.gov alerts FL, Flood Warnings sent 20:34 to 20:58 ET 11/27, read 2026-11-28T03:35:32Z"],
 signal_type="threshold-crossed",
 title="St. Johns at Sanford: the official NWS forecast issued 20:22 ET Fri Nov 27 now crests at 9.0 ft (Sat Nov 28 07:00 ET), ABOVE the 8.96 ft record (Oct 9, 2022), then 8.9 to 9.0 through early next week; observed 8.91 ft at 21:30 ET, 0.05 ft under it. DeLand observed 6.28 ft (record 6.33), forecast 6.5 ft this weekend and 6.6 ft to Fri Dec 4. Sanford becomes the second gauge forecast above its record",
 body="""# Florida flood check, Fri Nov 27 night (update to 20261127-003)

| Gauge | Observed (NWPS) | Official forecast (issued 01:22Z Nov 28 = 20:22 ET Nov 27) | Record (NWPS crest history) | Change since 20261127-003 |
|---|---|---|---|---|
| **Sanford (SNFF1)** | **8.91 ft at 02:30Z (21:30 ET)**, the highest in the observed series returned | **9.0 ft at 12:00Z Sat Nov 28 (07:00 ET)**; NWS warning 20:47 ET: crest 9.0 ft, then steady 8.9 to 9.0 'through at least early next week'; 8.8 by Dec 5 | **8.96 ft (2022-10-09)** | forecast 8.9 to **9.0, above the record** (NEW); observed 8.86 to 8.91 |
| DeLand (DLAF1) | 6.27 to 6.28 ft, 01:45Z to 02:30Z | 6.3 overnight; NWS 20:52 ET: 6.5 ft late this weekend, 6.6 ft early next week, steady into mid-week; series maximum 6.6, last point 6.5 at 00:00Z Dec 5 | 6.33 ft (2022-10-11) | observed 6.25 to 6.28; forecast timing earlier (6.5 this weekend) |
| Astor (ASTF1) | 4.4 ft at 20:30 ET (NWS); 24-hour max 4.5 | steady 4.3 to 4.4 through early next week | 4.81 ft (2024-10-12, as carried on 003) | small fall |
| Above Lake Harney | 13.1 ft at 19:30 ET, above its old record | very slow decline from this weekend | | continuing state |
| Cocoa 9W | 18.2 ft at 19:15 ET, above its old record | very slow decline to 17.8 ft | | continuing state |

- **Why IMMEDIATE:** card 003 registered it: 'an official Sanford forecast at or above 8.96 is a new IMMEDIATE' (ROUTING_TABLE CLIMATE_MACRO, an officially forecast record river level). This forecast is 9.0 at one decimal; the NWPS series carries one decimal on this gauge, so the margin over the record is 0.04 ft and inside forecast error.
- **Limits:** a forecast, not an observation. Sanford has not observed a record; observed is 0.05 ft under it. DeLand has not observed one either (0.05 ft under). Record values read tonight from the NWPS gauge records (crest history), matching 003.
- **So what:** two Seminole and Volusia reach gauges are now forecast at or above records for most of next week, with Lake Harney and Cocoa already above theirs upstream. Sanford's 9.0 ft impact line: 'flooding becomes more significant to the Sanford waterfront area'. Disaster-declaration coverage of Volusia and Seminole was last read by AEOLUS 11/25 (KB-AEO-331) and by CORAL 00:13Z 11/28 (no DR-4956 amendment); not re-read here.""",
 source="api.water.noaa.gov/nwps/v1/gauges/SNFF1/stageflow and /DLAF1/stageflow (read 2026-11-28T03:35:45Z); api.water.noaa.gov/nwps/v1/gauges/SNFF1 and DLAF1 (crest history); api.weather.gov/alerts/active?area=FL (read 03:35:32Z)",
 action=["CORAL"], info=["AEOLUS","SHADE","HOMER","REGINALD","MARCO","RED","PROME"],
 precedence="IMMEDIATE", confidence=0.95,
 confidence_language="confirmed: NWS and NWPS primary read directly; the record crossing is a forecast",
 cluster="CLIMATE_MACRO", domain="CLIMATE_MACRO",
 entities=["St. Johns River","Sanford","DeLand","Astor","Lake Harney","Cocoa","Seminole County","Volusia County","NWS","NWPS"],
 dispatch_note="IMMEDIATE by step 7j and card 003's registered line (official Sanford forecast at or above 8.96). Florida: CORAL action, AEOLUS info; other recipients as 003. RED, PROME by BOARD diff.",
 route_summary="Sanford official forecast 9.0 ft above the 8.96 record; DeLand 6.28 obs vs 6.33"))

cards.append(dict(
 id="SIG-W-20261127-018",
 slug="CORRECTION-of-20261127-007-item-5-France-recession-verdict-withdrawn-Reuters-says-INSEE-Nov-27-detailed-release-shows-technical-recession-INSEE-page-not-read-and-S-and-P-affirms-A-plus-outlook-to-negative",
 safety_net="clear", event_window="open", route_origin=RO,
 origin=["France 24 with Reuters, 'S&P revises France's outlook from stable to negative', issued 27/11/2026 23:00 (page read by helper)", "INSEE IR263 first estimate 30 October 2026, insee.fr/en/statistiques/9113712 (read by helper)", "FT title 'S&P cuts France outlook to negative' 2026-11-27 22:45Z (lane; ft.com refused fetch)", "Reuters via investing.com 5053881 and whtc.com (search summary)"],
 signal_type="correction",
 title="CORRECTION of 20261127-007 item 5: its verdict that '-0.2% and recession' were unsupported rested on INSEE's Oct 30 FLASH (-0.1%, Q2 0.0%) while the Nov 27 DETAILED release was not read; Reuters (via France 24, 23:00) says 'the French economy entered a technical recession, according to INSEE figures released Friday', and the FT titled it 'shrinks 0.2%'. Verdict WITHDRAWN to UNVERIFIED at INSEE (page not found by WALTER). Also Nov 27: S&P affirmed France A+/A-1 and cut the outlook to negative from stable, so all three big agencies now carry a negative outlook",
 body="""# Correction of SIG-W-20261127-007, item 5, and the S&P action on France

| Card 007 line | Was | Now | Direction |
|---|---|---|---|
| Item 5 (France Q3) | 'INSEE first estimate (10/30): Q3 -0.1%, Q2 0.0% ... **CORRECTED-FRAMING: -0.2% and recession unsupported by the flash**; the 11/27 detailed estimate not retrieved' | The flash is the wrong release to test a Nov 27 claim. INSEE scheduled the Q3 detailed figures for **27 November 2026, 08:45** (IR263's own 'next publication' line). **Reuters, relayed by France 24 (issued 27/11/2026 23:00):** 'the French economy entered a technical recession, according to INSEE figures released Friday.' FT 11:38Z title (card 002 item 6): 'French economy shrinks 0.2% in third quarter'. **INSEE's 27 November page was not found or read** (English listing did not render; French search returned only the flash) | Verdict **WITHDRAWN**: the bookmark claim is now **REPORTED by two tier-1 outlets, UNVERIFIED at INSEE**. A technical recession needs Q2 revised below zero as well; the revised Q2 figure is not in hand |

## Also new: S&P on France, Fri Nov 27 (after the European close)

| Item | Detail | Source |
|---|---|---|
| Rating | **A+/A-1 affirmed**; outlook **negative from stable** | France 24 with Reuters, 23:00 11/27 (read); FT title 22:45Z |
| Reasons (as relayed) | rising public debt against moderate growth prospects; need for fiscal consolidation; high risk that political fragmentation persists after the 2027 presidential election; interest costs rising through 2029; medium-term downgrade threat raised | France 24 with Reuters (read) |
| Figures (search summary of Reuters relays, page not read) | deficit 5.3% of GDP in 2027; growth 0.6% next year | Reuters via investing.com 5053881 (not opened) |
| Peers (search summary) | Fitch A+, outlook negative since Oct 30; Moody's Aa3, negative | Euronews 10/31; relays |

- **So what:** France's rating is unchanged but every major agency now warns of a cut, on the day INSEE's detailed accounts reportedly showed a technical recession. HANS-T-10 (France-Germany 10Y spread above 100 bp and OAT above 4.50) is the registered line this can move; Monday 11/30 is the first OAT session after the action. Not graded here.
- **Not read:** S&P's own release (spglobal.com not tried), INSEE's 27 November release, ft.com (refused automated fetch).
- **Why 007 slipped:** the verdict tested a claim about the 11/27 release against the 10/30 release (wrong referent; MEMORY finding 73's class: a 'not supported' needs the release it is about).""",
 source="france24.com/en/france/20261127-s-p-revises-france-s-outlook-from-stable-to-negative (helper read); insee.fr/en/statistiques/9113712 (helper read, the 30 Oct first estimate); ft.com/content/4e16110a-9604-4455-8557-4edece5df01a (title only; fetch refused); investing.com/news/economy-news/sp-revises-france-outlook-to-negative-on-mounting-budget-pressures-weak-growth-5053881 (search summary)",
 action=["HANS"], info=["CARL","ISHM","REGINALD","HENRY","LIQUID","LABOR","CORAL","BOND","RED","PROME"],
 precedence="PRIORITY", confidence=0.75,
 confidence_language="reports: Reuters relay read for S&P; INSEE detailed release not read",
 cluster="MISC", domain="EUROPE_MACRO",
 entities=["France","INSEE","S&P Global Ratings","Fitch","Moody's","OAT","HANS-T-10","technical recession"],
 dispatch_note="PRIORITY: correction direction matters (a 'not supported' verdict withdrawn) and a sovereign outlook action. HANS action (EUROPE_MACRO owner; HANS-T-10); BOND info as EUROPE_MACRO backup; recipients of 007 kept on info. R1 COR-20261127-05 same commit; banner on 007. RED, PROME by BOARD diff.",
 route_summary="Correction of 007 item 5 (France recession verdict withdrawn); S&P France outlook negative, A+ kept",
 extra_fm={"corrects":["SIG-W-20261127-007"],
  "corrects_direction":"007 item 5 CORRECTED-FRAMING verdict WITHDRAWN to UNVERIFIED: Reuters reports INSEE's 11/27 detailed release shows a technical recession; the flash used for the verdict was the wrong release",
  "kill_strings":["-0.2% and 'recession' unsupported by the flash","not -0.2% recession"]}))

cards.append(dict(
 id="SIG-W-20261127-019",
 slug="Small-items-Nov-27-night-lane-Al-Jazeera-blockade-item-likely-Pacific-Archer-HKD-six-month-high-Meituan-lower-2027-AI-capex-Carnival-CEO-grant-8-K-AT-and-T-PRT-appeal-Paraguay-bank-arrest-copper-jump",
 safety_net="clear", event_window="closed", route_origin=RO,
 origin=["Research-Intake data/2026-11-27/news.json (collector 2026-11-27T23:29Z), titles read before 2026-11-28T03:36:56Z (date command)", "EDGAR 8-K feed (CCL items 5.02, 9.01) via intake_scan"],
 signal_type="context",
 title="Small items, Nov 27 night lane (titles; folded by owner theme): Al Jazeera 22:23Z 'US military says it disabled merchant ship trying to breach Iran blockade' is most likely the Nov 26 Pacific Archer event on card 004 (page not read); Hong Kong dollar at a six-month high as funding costs jump; Meituan expects lower AI capex in 2027; Carnival amends CEO Weinstein's 2022 stock grant (8-K 5.02); both sides seek immediate appeal in the AT&T pension-risk-transfer case; Paraguay ex-minister arrested over a bank failure; copper's biggest jump since January",
 body="""# Small items, Nov 27 night lane (titles read; not scored)

| combo | Item (outlet, date) | Read | Owner |
|---|---|---|---|
| combo:FALCON/blockade | 'US military says it disabled merchant ship trying to breach Iran blockade' (Al Jazeera, 2026-11-27 22:23Z) | title; Google News redirect and aljazeera.com date path failed; a search found no other Nov 27 disabling. **Most likely the Pacific Archer (CENTCOM: disabled Nov 26, announced Nov 27; card 004 item 1).** Not confirmed as the same ship | FALCON |
| combo:ZHAO/hibor | 'Hong Kong Dollar Climbs to Six-month High as Funding Costs Jump' (Briefs Finance, 11/27 13:30Z) | title only; not found by my BOARD search (HIBOR, Hong Kong dollar) | ZHAO |
| combo:ZHAO/pboc | 'PBOC Warns of Rising Uncertainty, Pledges Ample Liquidity' (Bloomberg 11/27); 'China's central bank releases 2026 Financial Stability Report: mechanism to provide liquidity to non-bank institutions' (BigGo, 11/27) | titles only | ZHAO |
| combo:VULCAN/capex | 'Meituan expects lower AI capex in 2027 after a RMB2 billion quarterly profit' (Startup Fortune, 11/27); 'Magnificent 7 may fragment as AI capex growth slows, Synergy says' (InvestmentNews, 11/27); 'Micron CEO expects memory shortages to worsen in 2028, TrendForce sees prices falling' (Yahoo, 11/27) | titles only; Meituan is not a hyperscaler (no VULCAN gate implied) | VULCAN |
| combo:VULCAN/gpu-finance | 'How NVIDIA's new export restrictions could impact neoclouds like CoreWeave, Nebius' (Blockspace, 11/27); 'GPU-backed loan cuts slow data center builds' (Wisevoter, 11/26); 'CoreWeave eyes $4.5B loan, but bankruptcy odds rise to 21% on prediction markets' (Benzinga, 11/27) | TITLE ONLY; source not reviewed. The $4.5B loan is on 20261125-031, -035 and 010; prediction-market odds are ORACLE's to read | VULCAN, BROCK (ORACLE for the odds) |
| combo:CRUISE/governance | Carnival amends CEO Weinstein's 2022 stock grant, adjusts vesting (Investing.com 11/27); EDGAR 8-K items 5.02, 9.01 filed 11/27 | title and 8-K item codes; exhibit not opened | CRUISE |
| combo:SHADE/prt | 'Both sides request immediate appeal in AT&T PRT case' (plansponsor, 11/23) | title only; pension-risk-transfer litigation, PE-insurer channel | SHADE |
| combo:none | 'Paraguay ex-minister arrested in latest bank failure fallout' (Arab News, 11/27; lane alert) | title; Paraguay bank items on 20261120-006 and 20261121-003; no US channel seen | REGINALD (info) |
| combo:MIDAS/copper | 'Copper price jumps most since January as short sellers retreat' (Mining.com, 11/27) | title only | MIDAS |
| combo:BOND/long-end | 'Nasdaq leads market rebound as Treasury yields hit 5.29% at the long end' (TradingView, 11/27) | title only; the tenor is not stated in the title | BOND |
| combo:CORAL/fl-fiscal | 'Florida property tax cut prompts sheriff hiring freezes' (Yahoo, 11/26) | title only; repeat theme of 20261124-018 (FL property tax) | CORAL, CARL |

- **Repeats, not re-carded:** Russia jet fuel ban (11 titles; card 015, Resolution 1586); Novorossiysk and St. Petersburg drone attack (card 002); Commerzbank and the Treasury market (20261124-018); BoE report (20261126-005); SpaceX bond (20261126-005); Nvidia CEO resignation (stale, Nov 12 and 15); Huang testimony (20261123-018, 20261125-001); Jurf al-Sakhar (20261120-008); N-able (20261126-005); El Nino titles (no NOAA release found in them; ROUTING_TABLE v0.53 asks for the NOAA release itself).
- **NO-ACTION:** the other titles in the batch (declared in aggregate on batch manifest BM-20261128-01).""",
 source="/home/willi/Research-Intake data/2026-11-27/news.json (fingerprint d3691a8db965) and the intake_scan EDGAR leg; web search 2026-11-28 for the Al Jazeera item",
 action=["FALCON","ZHAO","VULCAN","CRUISE","SHADE"], info=["BROCK","ORACLE","REGINALD","MIDAS","BOND","CORAL","CARL","RED","PROME"],
 precedence="ROUTINE", confidence=0.5,
 confidence_language="titles: sources not read unless stated",
 cluster="MISC", domain="AI_CAPEX",
 entities=["CENTCOM","Pacific Archer","Hong Kong dollar","PBOC","Meituan","Micron","CoreWeave","Carnival","AT&T","Paraguay","copper"],
 dispatch_note="ROUTINE small-items fold (step 10.6). ACTION only for owners whose theme row is new; info for repeats and title-only folds. RED, PROME by BOARD diff.",
 route_summary="Small items Nov 27 night: blockade item likely Pacific Archer, HKD high, Meituan capex, CCL grant"))

json.dump([cards[0]], open("cards-017.json","w"), indent=1, ensure_ascii=False)
json.dump([cards[1]], open("cards-018.json","w"), indent=1, ensure_ascii=False)
json.dump([cards[2]], open("cards-019.json","w"), indent=1, ensure_ascii=False)
print("ok")
