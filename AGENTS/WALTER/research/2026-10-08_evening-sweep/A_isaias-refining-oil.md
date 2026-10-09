# Evening sweep A: Hurricane Isaias, US Gulf refining/ports, oil

**Window:** 2026-10-08 16:20 ET (20:20Z) to sweep close, 2026-10-08 20:31 ET (2026-10-09 00:31Z; `date` at close).
**Scope:** Isaias, Gulf refining and ports, and oil. Iran/Gulf-war items are excluded (another agent has them).
**Baseline:** 45 routed titles in `today_titles.txt`. Isaias items are `-001`, `-019`, `-035` and `-042`. I grepped their BOARD bodies before grading anything as new.
**Labels:** PRIMARY = the agency or operator itself. SECONDARY-READ = article body fetched. SNIPPET-ONLY = search summary only.
**Verdicts:** NEW-ESTABLISHED · NEW-UNVERIFIED · CHANGE-TO-ROUTED (`-NNN`) · NOTHING-NEW.

---

## (a) NHC advisories after 1 PM CDT

| # | Item | Verdict | Label / source / time |
|---|---|---|---|
| a1 | **Advisory 9 (4 PM CDT / 21Z):** Isaias is now **100 mph (85 kt), Category 2**, up from 85 mph in 8A. Pressure **975 mb** (unchanged). Position 24.4N 89.3W, moving NE (50°) at 12 mph. Headline: *"HURRICANE HUNTERS FIND THAT ISAIAS NOW HAS 100 MPH WINDS"*. Tropical-storm-force winds now extend **125 mi** from the center (8A: 90 mi). Hurricane-force winds extend 15 mi. **Watches/warnings: "CHANGES WITH THIS ADVISORY: None."** | CHANGE-TO-ROUTED (`-019`/`-035`: 85 mph, 975 mb) | PRIMARY. https://www.nhc.noaa.gov/archive/2026/al09/al092026.public.009.shtml, issued 400 PM CDT Thu Oct 08 2026 (21:00Z) |
| a2 | **Discussion 9 (4 PM CDT):** forecast **peak still 95 kt / 110 mph, but now at 12h (09/06Z, ~1 AM CDT Fri)**. Discussion 8 had it at 24h (09/12Z). Then **85 kt / 100 mph at 09/18Z at 28.2N 87.4W** (offshore), and **65 kt / 75 mph INLAND at 10/06Z, 31.0N 87.2W**. Discussion 8 had 85 kt at 10/00Z at 29.6N 87.4W, still just offshore. NHC quotes: *"The official forecast is nudged slightly eastward"*; *"some decrease in intensity is indicated as Isaias approaches the coast"*; *"Isaias is expected to remain a dangerous hurricane through landfall"*; shear *"is expected to increase substantially during the next 36 hours."* Also: *"this is the first eye noted on satellite pictures in the Atlantic basin during the 2026 Hurricane Season."* | CHANGE-TO-ROUTED (`-019` carried Disc 8's ~110 mph peak around 12Z Fri and ~100 mph near 29.6N 87.4W at 00Z Sat) | PRIMARY. https://www.nhc.noaa.gov/text/MIATCDAT4.shtml (Discussion 9, 400 PM CDT, Forecaster Pasch). Forecast advisory: https://www.nhc.noaa.gov/archive/2026/al09/al092026.fstadv.009.shtml (21:00Z) |
| a3 | **Landfall intensity: my derivation, not an NHC figure.** No 00Z Sat forecast point exists any more. Between 85 kt offshore at 18Z Fri and 65 kt inland at 06Z Sat, landfall would interpolate to roughly 70–80 kt, a high-end Cat 1 to low Cat 2. ⚠️ This is arithmetic on two forecast points, not NHC's statement. NHC says only "some decrease" before landfall. | DERIVED (flagged) | From a2 |
| a4 | **NHC wind-speed probabilities, #8 (15Z) → #9 (21Z), cumulative, by site.** **Pensacola:** hurricane-force (64 kt) **14% → 6%**; 50 kt 44% → 41%; 34 kt 84% → 88%. **Mobile:** 64 kt **6% → 1%**; 50 kt 22% → 11%; 34 kt 59% → 52%. **Gulfport:** 34 kt 25% → 15%. **Buras LA:** 34 kt 8% → 3%. **Offshore points:** grid 29.0N 87.0W 64 kt 48% → 41%; grid 28.0N 89.0W 64 kt 9% → 1%. Pascagoula is **not a listed site**. | NEW-ESTABLISHED (not in any routed item) | PRIMARY. https://www.nhc.noaa.gov/archive/2026/al09/al092026.wndprb.008.shtml and `.wndprb.009.shtml` |
| a5 | **Intermediate Advisory 9A (7 PM CDT / 00Z):** **100 mph, 974 mb** (down 1 mb), 24.9N 88.8W, NE at 13 mph, **290 mi S of the mouth of the Mississippi River**. *"Additional strengthening is expected through early Friday."* Landfall *"within the warning area late Friday or early Saturday."* NOAA buoy 42001 reported sustained winds of 38 mph, gusting 42. **Watch/warning changes: "None."** | CHANGE-TO-ROUTED (minor: pressure and position) | PRIMARY. https://www.nhc.noaa.gov/text/MIATCPAT4.shtml (WTNT34 KNHC 082351, issued 700 PM CDT Thu Oct 08 2026, Forecaster Reinhart) |
| a6 | **Warnings stand as routed (unchanged in 9 and 9A):** Hurricane Warning from Ocean Springs MS to the Bay/Gulf County line FL. Storm Surge Warning from the mouth of the Mississippi to the Suwannee River. Tropical Storm Warnings from the Jefferson/Plaquemines Parish line to west of Ocean Springs, and from east of the Bay/Gulf line to the Aucilla River. Storm Surge Watch from the Suwannee River to Yankeetown. **Surge (unchanged):** 5–7 ft from Ocean Springs to Indian Pass and in Mobile Bay; 3–5 ft from the mouth of the Mississippi to Ocean Springs. Discussion 9, Key Message 3: inland Tropical Storm and High Wind watches/warnings *"may be required for portions of [central/northern AL, extreme eastern MS, western/northern GA] later tonight."* | NOTHING-NEW (warnings); NEW (inland-warnings flag) | PRIMARY. Advisory 9 / 9A / Discussion 9 |
| a7 | **Advisory 10 (10 PM CDT / 03Z) was not issued at sweep close.** At 00:31Z, CurrentStorms.json shows `advNum 009a`. | UNESTABLISHED | PRIMARY. https://www.nhc.noaa.gov/CurrentStorms.json |

**So what (no thesis grade):** NHC's 4 PM package pulls the peak earlier and offshore. It nudges the track east and explicitly weakens the storm before landfall. Hurricane-force probabilities fell at every listed coastal site between 15Z and 21Z. The 15-mile hurricane-force radius makes a direct refinery-level hit a narrow-band event. ⚠️ **The 125-mi tropical-storm wind field grew.** Port and terminal disruption is driven by gale-force winds, not hurricane-force winds.

---

## (b) BSEE / MMA shut-in update after 11:00 CDT

| # | Item | Verdict | Label / source / time |
|---|---|---|---|
| b1 | **No newer release.** The BSEE RSS feed, fetched 00:19Z 10/9, lists the latest Isaias item as `mma-monitors-gulf-response-isaias2`, pubDate **Thu, 08 Oct 2026 16:56:00 +0000**. That release carries data *"as of 11:00 a.m. CDT today"*: **1,282,879 b/d oil (62.89%)**, **1,127 MMcf/d gas (57.35%)**, **121 of 371** platforms evacuated, **5 of 11** non-DP rigs evacuated, **4 of 17** DP rigs moved off location. `…isaias3` returns 404. The release says MMA *"will update evacuation and shut-in statistics daily at 1 p.m. CDT, as appropriate."* **Next expected: ~1 PM CDT Fri 10/9.** | NOTHING-NEW (`-035` stands) | PRIMARY. https://www.bsee.gov/rss.xml ; https://www.bsee.gov/newsroom/latest-news/statements-and-releases/press-releases/mma-monitors-gulf-response-isaias2 |
| b2 | **Basis note.** The figures are operator-reported precautionary shut-ins (*"a standard procedure conducted by industry for safety and environmental reasons"*), not damage. Maritime Executive's *"About 60 percent of all Gulf oil and gas production"* (19:25 ET) blends the oil (62.89%) and gas (57.35%) shares. Cite the split figures. | NOTHING-NEW | SECONDARY-READ. https://maritime-executive.com/article/hurricane-isaias-prompts-shut-ins-for-60-percent-of-gulf-oil-production (datePublished 2026-10-08T19:25:56-04:00) |

---

## (c) Refinery shutdowns, rate cuts and preparedness statements

| # | Item | Verdict | Label / source / time |
|---|---|---|---|
| c1 | **No refinery shutdown or rate cut announced in the window.** I checked the Chevron newsroom (latest items 10/8 "Powering what's next…", 10/6 Hess Midstream divestiture; no storm item). I also checked the pascagoula.chevron.com pages (JS-only, no text), the BOE Report Reuters feed for 10/8 (no refinery item after the 63% shut-in story), the NBC live blog (entries 4:20–7:58 PM EDT, none on refineries), and targeted searches for PBF Chalmette, Valero Meraux, Vertex Mobile and Shell Norco (results were 2012/2020/2021 storms only). | NOTHING-NEW (`-042`'s "no cut announced" extends from 15:17 ET to ~20:30 ET) | Absence over the sources listed. This is a gap, not a clear. Refiners often do not announce rate cuts. |
| c2 | **Chevron's onshore statement, now read in an article body:** Chevron *"is monitoring the storm's development and track and making 'appropriate preparations' at onshore facilities, the company said."* Pascagoula *"was on the western edge of the National Hurricane Center's projected storm path as of Oct. 8."* **Vertex Energy, Mobile AL (88 kb/d)**, is *"directly in the storm's projected path"*; *"Vertex didn't immediately respond."* **Hunt Refining, Tuscaloosa AL (50 kb/d)**: *"further inland but is under a tropical storm watch"*; *"Hunt didn't immediately respond."* ⛔ This is a preparedness statement, not a shutdown or rate cut. | CHANGE-TO-ROUTED (`-042`; the laptop-evening verify had Chevron's wording SNIPPET-ONLY) | SECONDARY-READ, Transport Topics (Bloomberg syndication). https://www.ttnews.com/articles/isaias-threat-us-fuel-market, published 2026-10-08T15:15:00-04:00, modified 15:39:09-04:00. ⚠️ **Pre-window** (before 16:20 ET). The state did not change; only the sourcing improved. |
| c3 | **Pascagoula capacity basis conflict.** Chevron's own 2026 fact sheet: *"The refinery can process approximately 394,000 barrels per day of crude oil"* (also *"Makes up more than 90% of the refining capacity in MS"*). Bloomberg/TT: **356,000**. ZeroHedge, used in `-042`: **369,000**. Energy Intelligence (SNIPPET-ONLY): a permit filing for ~10% expansion to 394 kb/d. ⇒ The `-042` figure of 369 kb/d is one of three bases. **The company's current figure is 394 kb/d.** Capacity is exposure, not loss. | CHANGE-TO-ROUTED (`-042`, capacity basis) | PRIMARY (company PDF). https://chevronadvocacynetwork.com/wp-content/uploads/2026/07/Pascagoula-Refinery-Fact-Sheet-2026-2.pdf (uploaded 2026/07; page date not stated). Fetched and text-extracted. |
| c4 | **A different path-capacity figure exists. Do not add it to Energy Aspects.** Andy Lipow (Lipow Oil Associates): *"About 2.7 million barrels per day, or 14%, of America's refining capacity, lie within or near the projected of the path of the storm"* (sic). He *"expects at least some refineries in the New Orleans/Baton Rouge and Mississippi/Alabama regions will have to slow down."* That is **"within or near,"** a wider perimeter than Energy Aspects' ~0.5 mb/d **"in the path"**, and it predates the eastward nudge in a2. It is a forecast of cuts, not an announced cut. | NEW-UNVERIFIED as a fleet item (pre-window; not found on BOARD by grep) | SECONDARY-READ, CNN (Matt Egan), published Oct 8 2026 5:30 AM ET, updated 2:04 PM ET. https://www.cnn.com/2026/10/08/economy/isaias-oil-refineries-gulf-coast-hurricanes. Also NBC: https://www.nbcnews.com/business/energy/gas-prices-hurricane-isaias-gulf-mexico-rcna602258 (modified 22:15Z), where the note is dated Wednesday. |
| c5 | GasBuddy's De Haan: refineries in the path *"are likely to see flooding that could take them offline for up to 10 days."* | NEW-UNVERIFIED (commentary, not a state change) | SECONDARY-READ, NBC (as c4) |

---

## (d) Ports and infrastructure

| # | Item | Verdict | Label / source / time |
|---|---|---|---|
| d1 | **USCG Sector Mobile, all five ports at YANKEE:** **Gulfport, Mobile, Panama City, Pascagoula and Pensacola** each read *"Open / YANKEE / See MSIB 122-26 / Last Changed 2026-10-08."* Yankee closes a port to inbound vessels over 500 GT without COTP permission; it is not a closure. **No ZULU set.** | CHANGE-TO-ROUTED. The afternoon sweep A (row 18) had X-Ray (set Wed) for these ports and Yankee only "expected" at Mobile. `-035` carried Mobile's noon berth stop. | PRIMARY. https://www.navcen.uscg.gov/port-status?zone=MOBILE (fetched 00:2xZ 10/9). ⚠️ The table gives a **date only, no time**. The supporting rows below show at least Mobile and Gulfport were at Yankee in the morning, so this is likely **pre-window**. MSIB 122-26 itself was not found. |
| d2 | **Mobile:** *"The U.S. Coast Guard has established Port Condition YANKEE for the Port of Mobile… vessels may enter the port only with Coast Guard permission. Vessels seeking to depart must arrange immediate departure."* The Alabama Port Authority suspended vessel operations at public berths at **noon CDT Thu 10/8**. *"Terminal operations are scheduled to be suspended at the close of business today."* | Confirms d1 (the noon stop was already in `-035`) | PRIMARY (port authority). https://alports.com/news/tropical-storm-isaias-latest-updates-on-port-of-mobile-operations/, *"Last updated: Thursday, October 8, at 9:29 a.m. CDT"* (dateModified 14:44Z). No later update. |
| d3 | **Gulfport:** *"the U.S. Coast Guard (USCG) Captain of the Port (COTP) has ordered Port Status YANKEE for the Port of Gulfport."* | Confirms d1 | PRIMARY (MS State Port Authority). https://shipmspa.com/weather-updates/, modified 2026-10-08T14:24:53Z |
| d4 | **New Orleans / Lower Mississippi, Houma / Port Fourchon / LOOP:** the NAVCEN tables for Sector New Orleans and MSU Houma are **stale** (last changed 2024-09-12 to 2025-03-28). They show "Open" rows, including **LOOP and LOOP PLATFORM "Open, MSIB 048-24, 2024-09-12"**, which **cannot be used as current status**. A search summary says the Sector New Orleans COTP set **WHISKEY at 0700 on 10/7**, port open. The Greater Lafourche Port Commission (Port Fourchon) site carries no Isaias notice. **loopllc.com is JS-only** and no LOOP operational notice was found in any source. Geography: the Tropical Storm Warning starts at the Jefferson/Plaquemines Parish line, so Port Fourchon (Lafourche) is outside the warnings. Buras LA 34-kt probability is 3% at #9. | **UNESTABLISHED** (current New Orleans condition, LOOP, Fourchon) | NAVCEN PRIMARY (stale): https://www.navcen.uscg.gov/port-status?zone=NEW%20ORLEANS , `?zone=HOUMA`. Port Fourchon: https://portfourchon.com/weather-and-storm-info/. WHISKEY: SNIPPET-ONLY. USCG Atlantic Area port-condition pages returned **403** to both curl and WebFetch. |
| d5 | **Pipelines and terminals:** no Colonial, Products (SE)/Plantation or terminal shutdown notice found for the 2026 storm. Search results were 2020 Isaias (East Coast) and Ida 2021. | NOTHING-NEW / UNESTABLISHED | Searches only |
| d6 | Maritime Executive (19:25 ET) relays that **Coast Guard Heartland** warned SAR capacity *"will be reduced in the run-up to the hurricane's arrival"* while it repositions forces. Operational context only. | NEW-UNVERIFIED (minor; USCG release not read) | SECONDARY-READ, maritime-executive.com (as b2) |

---

## (e) Oil after the 10/8 settle

**Named-contract evening levels.** Source: Yahoo `.NYM` 5-minute bars, labelled by bar start in ET, pulled 20:2x ET. ⛔ **All bars after the 18:00 ET reopen belong to the Fri 10/9 session.** ⚠️ The vendor's date-labelled 10/8 *daily* bar has already been replaced by evening-session data. For CLX26 it shows a close of 91.12 on volume 3,786. That is **not the settle**, so do not use it.

| Contract | 10/8 settle (routed) | Evening (10/9 session) level | Evening range 18:00–20:15 ET | Change vs settle |
|---|---|---|---|---|
| **CLX26** (WTI Nov) | **$91.49** (+$3.21); vendor daily bar for 10/7 = 88.28, consistent | **$91.11** (20:10 ET bar close); $91.12 on the in-progress 20:15 bar | $90.93–$91.41 | **−$0.37** (~−0.4%), against a settle I did not re-verify here |
| **BZZ26** (NYMEX Brent BZ, Dec; *not* the ICE contract) | **ICE settle UNESTABLISHED.** A snippet says $104.28. investinglive says *"closed up around $4 near $104."* | **$103.80** (20:10 ET); $103.78 on the 20:15 bar | $103.64–$104.09 | **Not computed** (no verified settle) |
| RBX26 (RBOB Nov) | not obtained | $3.3040 (20:10 ET) | — | not computed |
| HOX26 (ULSD Nov) | not obtained | $4.8408 (20:10 ET) | — | not computed |

- **Post-settle dip, 10/8 session (before 17:00 ET), cause UNESTABLISHED.** CLX26 fell from $91.10 (15:55 bar) to a **$90.53 low (16:10 bar)**, then recovered to $91.18 by 16:55. BZZ26 went from $103.81 to a $103.16 low over the same bars. I found no Isaias, refinery or SPR item that times to it. The Iran items (`-034`, plus investinglive's late-session Fars/Hormuz report) are **out of my scope**, and I do not attribute the move. Source: Yahoo `.NYM` 5-minute bars.
- **Settle report:** *"Brent crude futures closed up around $4 near $104 a barrel, while US West Texas Intermediate rose circa 3.5% to settle around $91.50."* Peaks: *"Brent near $106 and WTI around $93."* SECONDARY-READ, investinglive, page stamp *"08/10/2026 at 08:54 PM"* (timezone not stated; day/month order inferred). No contract months named. https://investinglive.com/commodities/oil-settles-circa-4-higher-as-two-supply-threats-collide-iran-strike-fears-and-hurricane-isaias/ → **NOTHING-NEW** (consistent with the routed $91.49).

**Material oil news after 16:20 ET (non-Iran):**

| Item | Verdict | Source |
|---|---|---|
| **OPEC+:** nothing after 10/4. The 10/4 meeting kept November targets unchanged; next meeting Nov 1. | NOTHING-NEW | SNIPPET-ONLY (CNBC / The National / World Oil, 10/4) |
| **SPR / DOE:** the DOE newsroom's 10/8 releases are Genesis Mission awards, a fellowship and Early Career awards. **No SPR exchange or hurricane-related release.** | NOTHING-NEW | PRIMARY. https://www.energy.gov/newsroom (fetched 00:2xZ 10/9) |
| **Saudi OSPs (November):** not verified for 2026. The only "Nov 2026" figure found (Arab Light Asia −$5.00 vs Oman/Dubai) came from an uncorroborated site. Nothing new in the window. | NOTHING-NEW (the Nov OSP itself is UNESTABLISHED) | SNIPPET-ONLY |
| **EPA fuel waivers / DOE CESER Isaias situation report:** none found for 2026. | NOTHING-NEW | Searches only |

---

## Date-trap log (discipline 1)

- "Isaias" returns **2020 Isaias** (East Coast) results: USCG Zulu bulletins for Miami, Canaveral and Charleston; Maryland port closures; DOE CESER situation reports; Colonial context. **All 2020, all excluded.**
- Chevron Pascagoula "shut down ahead of storm" results are **Katrina 2005**, **Alberto 2018** and **Ian 2022**. PBF Chalmette and Valero Meraux results are **Ida 2021**. Excluded.
- The ZeroHedge/Yahoo "U.S. Gulf Energy Hub Braces for Category 2 Hurricane" is a **Wed 10/7 18:00Z** item, not new.

## Unknowns that gate decisions

1. Whether any refiner, Chevron Pascagoula above all, cuts runs before landfall. Not announced as of ~20:30 ET, and refiners often do not announce.
2. **The current Sector New Orleans port condition and LOOP status.** The NAVCEN tables are stale and LOOP's site is unreadable.
3. **The exact ICE Brent Dec 10/8 settle.**
4. Advisory 10 (10 PM CDT) and the 10/9 ~1 PM CDT MMA shut-in update, both after this sweep.
