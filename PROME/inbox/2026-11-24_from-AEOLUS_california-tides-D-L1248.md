# AEOLUS -> PROME: California tides, Tue 11/24 read and Wed 11/25 outlook (D:L1248)

**From:** AEOLUS (session aeolus-desk-agent-2026-11-24, Claude Code, Opus 5.5) · **Written:** 2026-11-24 23:33 ET · **Woken on:** Will's word 23:22 ET, via PROME prome-77
**Row:** D:L1248 (read was owed before 12:00 ET 11/24; fleet offline; read now, after Tuesday's tide and before Wednesday's).
**Findings:** `AGENTS/AEOLUS/workbook/KB.tsv` KB-AEO-326 to 329 · raw pulls `AGENTS/AEOLUS/sources/2026-11-24_california-tides/`. All water levels in feet above MLLW (mean lower low water), CO-OPS data PRELIMINARY (quality flag p), not verified by NOAA.

## For Will, in plain words

**What happened Tuesday.** The year's highest tides (the "king tides") arrived on a Pacific that has been running about a foot and a quarter above normal since late summer because of the very strong El Nino, and a storm on the north coast added roughly another two-thirds of a foot there. At Arena Cove (the Mendocino coast gauge) the water reached 8.86 ft at 12:24 ET, **the highest in that gauge's record on NOAA's own monthly table**. ⚠️ That record has a hole: the gauge has no data from 1983 to 1990, so it does not include the January 1983 storm, which still holds the records at San Francisco and Crescent City. At Humboldt Bay (North Spit) it reached 10.16 ft at 13:18 ET, **the second highest since the gauge started in 1977**, behind this January's 10.36, and over the Weather Service's "major flood" level of 10.0. San Francisco reached 8.23 ft at 13:06 ET, **0.43 ft under its record of 8.66 ft (27 January 1983, NOAA's station table)**.

**What flooded.** King Salmon, a small bayside neighbourhood south of Eureka with about 281 residents, was under an evacuation order from 7:03 AM Pacific Tuesday. The Sheriff (William Honsal) declared the emergency on Monday and the county board ratifies it Wednesday. Many residents stayed. People were wading in the streets and a railroad levee on the Samoa peninsula was overtopped. Fields Landing next door (about 275 people) is under a warning. ⚠️ This comes from local news, not the county's own notice, and the local paper warns that AI-faked King Salmon flood videos are circulating. I found no report of San Francisco Bay flooding Tuesday, which is a search gap, not evidence that nothing flooded.

**Wednesday, times in ET.** San Francisco is forecast to reach **8.5 ft at 13:49 ET**, which the Weather Service calls "approaching the highest tide ever recorded". That forecast includes up to 1.5 ft of storm surge on top of the tide. Thursday's high is 8.0 ft at 14:38 ET. Humboldt Bay is forecast at **10.0 to 10.4 ft between 12:00 and 16:00 ET**, right around January's 10.36 record. Waves of 20 to 30 ft are forecast on the San Francisco coast and up to 25 ft on the north coast. Southern California warnings say Orange and San Diego counties will likely break the records set in late October.

**Is anything of economic consequence exposed?** **Not on tonight's evidence.** This is a flood of shoreline roads, parks and a few small neighbourhoods. No power plant, port, refinery, airport or treatment plant has been reported affected. What exists is preparation: a temporary flood barrier and a closed shoulder at the westbound Bay Bridge toll plaza, and the state is watching Doolittle Drive next to Oakland airport, the Posey Tube and Highway 37. The Humboldt Bay power plant and the old nuclear plant's spent-fuel vault sit at King Salmon. Secondary sources put the vault about 44 ft above sea level, and studies show the site exposed only under about 3 ft of future sea-level rise with its barriers breached. I could not check that at PG&E or the NRC tonight. **Insurance:** tidal flooding is not covered by homeowners policies or by the California FAIR Plan, which is fire cover. Only federal flood insurance applies, and the exposed population is in the hundreds. Insured losses are immaterial. **No score moves, and nothing went to TERRY, WATT or SHADE**, because nothing met the row's bar.

**What I expect.** Wednesday most likely looks like Tuesday. At Humboldt Bay my working estimate is about 10.3 ft, close to the January record either way. Arena Cove likely sets a new high again, near 8.9 to 9.0 ft. San Francisco most likely comes in around 8.3 to 8.5 ft, under the 8.66 record. I put roughly a one-in-five chance on a San Francisco record Wednesday: it needs about 0.35 ft more surge than Tuesday carried. **The bigger forward point is Christmas.** The astronomical tide at San Francisco on 12/24 is 0.16 ft higher than Wednesday's. If the El Nino anomaly holds, the 23 to 25 December king tides reach about 8.4 ft before any storm, so a modest storm would put the 1983 record within reach. The next windows after that are 21 to 22 January. **What would change my mind:** the anomaly fading (San Francisco's daily excess over the tide table falling below about +0.8 ft by mid-December), or no storm on the December tides.

> **ATTENTION** 🟡 — NOAA's tide-data service (CO-OPS) began refusing this machine at about 23:27 ET (HTTP 403) after my own fast scan, about 300 requests in a few minutes. I stopped and did not change anything to get around it. The Weather Service's own gauge feed (NWPS, `api.water.noaa.gov`) serves the same readings and matches NOAA to 0.01 ft at four California gauges, so Wednesday's read does not depend on it. WALTER's flood check uses CO-OPS and may hit the same refusal. If it persists past Wednesday, Will may want to know that CO-OPS is unusable from this box (CME-class block). Whether it is a short rate limit or a standing block is UNKNOWN.

## Evidence

| # | Claim | Source | Time | State |
|---|---|---|---|---|
| 1 | Arena Cove 8.862 ft at 9:24 AM PST 11/24, highest in the monthly table 1978-2026 (prior top 8.671, Feb 1998; 8.652, Jan 2026) | CO-OPS datagetter 6-min + monthly_mean "highest" | obs 17:24Z; read 23:25 ET | VERIFIED (preliminary obs) |
| 2 | Arena Cove has no data 1983 to 1990, so the Jan 1983 storm is missing | CO-OPS monthly_mean coverage | read 23:27 ET | VERIFIED |
| 3 | North Spit 10.162 at 10:18 AM PST, second to 10.359 (Jan 2026) since 1977; NWS major 10.0 | CO-OPS; NWPS HBYC1 flood categories | obs 18:18Z | VERIFIED |
| 4 | Crescent City 10.062 at 10:00 AM PST, 4th (record 10.663, Jan 1983) | CO-OPS monthly_mean | obs 18:00Z | VERIFIED |
| 5 | San Francisco 8.233 at 10:06 AM PST; record 8.659 to 8.663 MLLW, 27 Jan 1983 (datum-page max 14.639 STND minus MLLW 5.98) | CO-OPS mdapi datums + monthly_mean | obs 18:06Z | VERIFIED |
| 6 | Bay gauges under their records: Alameda 8.982 vs 9.645 (1983); Richmond 8.379 vs 8.675 (Jan 2026); Point Reyes 8.386 vs 8.553 (Jan 2026); Redwood City 10.712 vs listed 10.789 (Dec 1983, datum page only) | CO-OPS | 11/24 | VERIFIED (Redwood City record INFERRED: the datum-page max can be stale, as at North Spit) |
| 7 | Excess over predicted tide at the high: north coast +1.60 to +1.74, Bay +1.29 to +1.35 | CO-OPS obs minus predictions | 11/24 | VERIFIED |
| 8 | Background West Coast anomaly since August: SF Nov 1-22 mean +1.26, Crescent City +0.90 | KB-AEO-313 (CO-OPS hourly) | 11/23 | VERIFIED (earlier pull) |
| 9 | Storm share ~+0.7 ft north coast, ~0 at SF | residual arithmetic, rows 7 and 8 | — | INFERRED |
| 10 | Attribution: El Nino warm-water expansion and Kelvin waves, plus king tides and surge | KQED 11/13 (NWS Joe Merchant, Jan Null); Governor's release 11/24 | 11/13, 11/24 | VERIFIED as their attribution; not a formal NOAA attribution study |
| 11 | SF Wed 8.5 ft at 10:49 AM PST (13:49 ET), Thu 8.0 at 11:38 AM PST; includes up to 1.5 ft surge; "approaching the highest tide ever recorded"; up to 2.7 ft inundation; surf 20-30 ft | NWS San Francisco CFW / High Surf Warning | issued 13:42 PST 11/24 | VERIFIED |
| 12 | North Spit Wed 10.0-10.4, 9 AM-1 PM PST; up to 2 ft above HAT; Thu Coastal Flood Watch, up to 2.5 ft; surf up to 25 ft Wed | NWS Eureka CFW | issued 13:27 PST 11/24 | VERIFIED |
| 13 | Card 030's conflict: the NWPS series (8.54 Wed) is the astronomical tide only, with no anomaly; Tuesday it was 1.74 ft low and the forecaster's 10.3-11.0 was 0.14 to 0.84 ft high. **The forecaster's total is the number to use.** | NWPS HBYC1 stageflow (issued 00Z 11/25) vs CO-OPS obs | 11/24-25 | VERIFIED |
| 14 | Delta and Carquinez: Port Chicago 7.5 ft MLLW 1:01 PM PST Wed; Rio Vista 7.6 ft NAVD88; levee erosion possible (Solano shorelines, where the refineries sit) | NWS Sacramento Flood Warning | issued 13:20-13:24 PST 11/24 | VERIFIED (forecast); refinery impact UNKNOWN |
| 15 | SoCal: Orange/San Diego 7.9-8.3 ft, "likely breaking the all-time tidal records set back in late October"; SLO/SB 7.7-8.2, Ventura 8.0-8.4, surf to 22 ft | NWS San Diego 13:57 PST; NWS LA/Oxnard 17:51 PST | 11/24 | VERIFIED (forecast); SoCal 11/24 observations not read (CO-OPS refused) |
| 16 | King Salmon evacuation order, zone HUM-E091-B, ~281 people, in effect 7:03 AM PST 11/24; Sheriff Honsal emergency declaration 11/23; Board ratifies Wed 1:30 PM PST; Fields Landing warning, ~275 people, since 11/20 | Lost Coast Outpost evacuations page (county Genasys listing) and live blog | read 23:30 ET | INFERRED (secondary; county notice not read) |
| 17 | Flooding reported: King Salmon streets, a Samoa railroad levee overtopped, Freshwater Slough levees, Old Town Eureka waterfront | Lost Coast Outpost live blog (reader photos) | 11/24 | INFERRED (secondary) |
| 18 | State actions: I-80 WB toll-plaza barrier with shoulder closed; Doolittle Dr, Posey Tube, SR 37 named; state emergency since 9/21 | Governor's release 11/24 | 11/24 | VERIFIED |
| 19 | No report of Humboldt Bay Generating Station, spent-fuel vault, harbor, SFO, OAK, refineries, wastewater plants affected | web search, LoCO, Governor | 23:30 ET | SEARCH-NOT-FOUND |
| 20 | Spent-fuel vault ~44 ft above mean sea level; exposed only under 1 m of sea-level rise with barriers breached | Cal Sea Grant, Wikipedia, Coastal Commission 2015 report (via search summary) | — | INFERRED (not read at PG&E or NRC) |
| 21 | King tide windows: 11/24-26, 12/23-25 2026, 1/21-22 2027 (NorCal also 12/22, 1/20, 1/23) | California Coastal Commission King Tides Project (via search) | — | INFERRED (page not opened) |
| 22 | SF astronomical high 12/24 = 7.18 MLLW vs 7.02 on 11/25 | CO-OPS predictions (KB-313 pull, 11/23) | 11/23 | VERIFIED (earlier pull) |
| 23 | Predicted heights at North Spit and Arena Cove for Dec and Jan | CO-OPS refused | — | UNKNOWN |

## Forward view (unscored; no row registered)

- **Wed 11/25:** Humboldt ~10.3 (arithmetic: Wed tide 8.54 + Tue excess 1.74), within ±0.3 of the 10.36 record. Arena Cove ~8.96, likely a new high again. SF most likely 8.3-8.5; **record (>=8.67) about 20%**. Thursday is lower by about 0.5 ft at SF.
- **23-25 Dec:** the SF astronomical tide is higher than this week's. With background excess of about +1.2, the tide reaches about 8.4 before any storm. A Bay record is a live possibility if a storm lines up: **about 30%** (my estimate, unscored).
- **Alternative:** the El Nino excess fades faster than NWS expects (they say it holds until El Nino wanes in the new year), and December comes in near 8.0.
- **Would change my mind:** SF daily excess under +0.8 ft in mid-December (down from +1.26 in November), or CPC's 12/10 discussion showing rapid Nino-3.4 decay.
- **C4:** no band input; the flood leg stays live but local. The insurance (loss) leg does not move: flood is outside homeowners and FAIR Plan policies. Score held at 2.

## Second read owed

**Yes, Wed 11/25 at about 14:30 ET.** That is after San Francisco's 13:49 ET high and Humboldt's peak window of 12:00-16:00 ET (peak about 13:00-14:00 ET). The read covers the observed highs at San Francisco against 8.66, North Spit against 10.36, Arena Cove against 8.86, and Crescent City. Read through NWPS (`api.water.noaa.gov/nwps/v1/gauges/{FTPC1,HBYC1,ANVC1,CECC1}/stageflow`, MLLW) if CO-OPS still refuses, plus the Wednesday impact reports. Please register it (owner AEOLUS). A third check at the 23-25 Dec king tides belongs on the docket only if you judge it worth a row; I have not registered a prediction.

## Gaps

- CO-OPS refused after 23:27 ET. Not read: SoCal and Monterey observations for 11/24, North Coast predictions for December and January.
- No official county or PG&E statement read. King Salmon facts are from local news.
- No Bay Area 11/24 impact report found.
- Coastal Commission dates come from a search summary; the page was not opened.

## COMPLETION — AEOLUS — 2026-11-24
STATUS: ✅ DONE (items 1-5; item 6 follows in a second packet)
CHANGED: AGENTS/AEOLUS/workbook/KB.tsv (KB-AEO-326..329), AGENTS/AEOLUS/sources/2026-11-24_california-tides/*, PROME/inbox/2026-11-24_from-AEOLUS_california-tides-D-L1248.md
RESULT: Arena Cove 8.862 ft MLLW on 11/24 is the highest in its NOAA monthly record (1978-2026, with 1983-90 missing); North Spit 10.162 is 2nd since 1977; SF 8.233 is 0.43 under its 8.66 (1983) record. Wednesday: SF 8.5 at 13:49 ET, Humboldt 10.0-10.4. No asset of consequence affected and insured loss immaterial; no score moved, no packet routed.
GAPS: CO-OPS API returned HTTP 403 from 23:27 ET after my ~300-request scan; stopped, no evasion; NWPS is the fallback. County or PG&E statements and Bay impact reports were not found.
WILL_NEEDS: None (ATTENTION only: CO-OPS refusal, possibly affects WALTER).
FOLLOW-UP: Register AEOLUS second read Wed 11/25 ~14:30 ET (post-tide, NWPS fallback); D:L1248 can be marked read.
