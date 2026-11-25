import json
ro="Will's X bookmarks, scan 2026-11-25T17:48:42Z (Will 12:48 ET), BM-20261125-09"
b=lambda **k: dict(dict(safety_net="clear",event_window="open",route_origin=ro),**k)
C=[b(id="SIG-W-20261125-024",slug="CoreWeave-Oct-2031-bonds-74.23-yield-17.91-June-2030-record-low-76.55-Tradeweb-via-Reuters-Nov-25-and-CCC-effective-yield-18.66-Nov-24-FRED-three-year-window-high",
title="CoreWeave bonds Nov 25 morning (Tradeweb via Reuters, secondary): Oct 2031 notes 74.23 cents, 17.91% yield; June 2030 notes a record low 76.55; CCC effective yield 18.66% [11/24, FRED], the 2020 crisis-peak comparison is a monthly-chart claim FRED's window cannot test; stock has since bounced to 40.22",
origin=["X 2125610724885950960 @DeItaone","X 2125624903496040617 @DarioCpx (quoted post read)","X 2125394343477612548 @fxevolution (image read)"],signal_type="indicator",
body="""# CoreWeave cash bonds and the CCC yield

| Object | Read | Basis |
|---|---|---|
| CoreWeave Oct 2031 notes | down 1.92 to **74.23 cents, 17.91%**; Newsquawk carried the yield at 10:22 ET | Tradeweb via Reuters as relayed by MLQ (read) and @DeItaone; Reuters not read; intraday |
| CoreWeave June 2030 notes | down 3.79 to **76.55, a record low** | same |
| Debt, 10-Q for 9/30 | $41.6B recourse, $5.3B non-recourse; **$11.0B principal due in 2027** | MLQ citing the 10-Q; VULCAN holds the filing |
| Stock | 40.22 at 12:51 ET (-4.7%), from a 37.40 low; -10% at the time of the bond read | vendor; the bonds have not been re-read since the bounce |
| CCC effective yield | **18.66% [11/24]**, 18.48 [11/23], 18.61 [11/20], 18.32 [11/19]: the high of FRED's available window (from 11/2023) | FRED BAMLH0A3HYCEY 12:50 ET |
| 'Above the 2020 crisis peak, highest since 2016' | chart read: 18.48 live monthly bar against a dotted 2020 line; **monthly points, not daily peaks**; FRED here starts 2023-11-27 | UNTESTED. A daily 2020 high may be above it |

- **Killed as an inference:** 'shares are already worth close to zero as far as the credit market is concerned' (@DarioCpx). 74 cents is a distressed price, not a zero-equity mark; it is one commentator's reading.
- **Do not add as independent confirmation of the swaps:** bonds and LIQUID's swap reading (5Y 1,314 clean [11/24], card 022) are two instruments on one name; the 11/25 five-year swap trade was cancelled.
- Outright yield includes the Treasury level; the CCC spread was 1,405 bp [11/24] (card 022).
- **So what:** the cash bonds fell with the swaps in the morning, which fits single-name stress. The test is whether they recover with the stock. WQ-745's conditions are TERRY's; no change is asserted here.""",
source="mlq.ai (helper read 12:52 ET); FRED; X posts and one image; roic.ai refused (403)",action=["LIQUID","VULCAN","BROCK","TERRY"],info=["SAM","HENRY","REGINALD","NEXUS","VIOLET","RED","PROME"],precedence="PRIORITY",confidence=0.75,confidence_language="reports: one Reuters and Tradeweb chain, secondary; FRED at source",cluster="AI_INFRA_CAPEX",domain="AI_CAPEX",entities=["CoreWeave","CCC","Tradeweb","FRED"],
dispatch_note="PRIORITY. ACTION LIQUID (bond against swap basis), VULCAN (issuer), BROCK (combo:BROCK/ai-financing). TERRY BOARD-only (WQ-745 condition context). RED, PROME by BOARD diff.",route_summary="CoreWeave bonds 74.23, CCC yield 18.66"),
b(id="SIG-W-20261125-025",slug="Small-items-Will-bookmarks-Nov-25-Thanksgiving-high-wind-warnings-mid-Atlantic-PE-exit-backlog-300B-claim-WSJ-unread-Iowa-detonation-done-SocGen-Oracle-debt-Kalshi-93-others-repeats",
title="Small items, Will's bookmarks Nov 25: Thanksgiving high-wind warnings from North Carolina to New York; private-equity backlog and $300B 2028-29 debt (WSJ via post, unread; PitchBook August read); Iowa detonation done, zero airborne lead (preliminary); banks selling data-center loans mostly carded; Kalshi December hike 93%; repeats listed",
origin=["X 2125516586434113702 @NWS_MountHolly","X 2125599639013367920 @unusual_whales","X 2125226505936515500 @ABC","X 2125562424111596003 @DeItaone","X 2125584140900683877 @DeItaone","X 2125446309603680298 @pelositracker"],signal_type="development",
body="""# Small items (combo tags as shown)

| # | Item | Read | State and owner |
|---|---|---|---|
| 1 | Thanksgiving wind | NWS Mount Holly (image read, issued 03:15 ET): gusts 55 to 60 Philadelphia and Trenton, 60 to 65 Dover and Toms River, 65 to 70 Atlantic City, Cape May, Bethany; 4 AM to 11 PM Thursday by area. 28 High Wind Warnings live at 12:49 ET, NC Outer Banks to New York City and Long Island, tonight through 01:00 ET Friday | PRIMARY, forecast. AEOLUS; WATT (PJM and NYISO outages on a holiday load). Onshore wind with today's tides: not assessed here. combo:none |
| 2 | Private-equity exit backlog | post relaying WSJ: about $300B of PE-backed debt due 2028 and 2029; 30% of holdings held six years or more, a record (PitchBook) | WSJ UNREAD. PitchBook 'Zombie Problem' (Aug 17, 2026, text read in part): 2,536 US companies past the 5-to-7-year window; nonsoftware **BDC holdings alone** $65B due 2028, $67B due 2029; its over-five-years count is given as 4,568 (33.8%) AND 3,905 (28.9%) in the same paper. The $300B and 30% are NOT in what I read. BROCK. combo:none |
| 3 | Iowa Army plant lead azide | detonated about 10:00 ET Nov 25; 68 barrels, about 9,700 lb; EPA 'zero' airborne lead, preliminary; dust guidance covers 148 sq mi; no effect on munitions supply reported | ABC Nov 25 (read). Closes 20261123-018 item 7. combo:none |
| 4 | Banks selling data-center loans | Breakingviews column via post: ING $500M, HSBC $300M in the mid-80s, SocGen seeking buyers for $300M Oracle-related debt; ECB: data centers 1.2% of bank corporate exposure | REPEAT for ING (20261106-004, 20261123-008) and HSBC (20261117-009). **New to the BOARD by my search: SocGen $300M** (FT via search summary: Lighthouse WI and Frontier TX, quoted above 90 cents; page refused) and the ECB 1.2% (column, unread). combo:BROCK/ai-financing |
| 5 | December Fed | Kalshi 25 bp hike 93%, hold 4%, larger 4% (image read; volume $27.1M) | ORACLE owns this price; HENRY read futures at about 93% at 11:30 ET |
| 6 | Outage list | two weeks of US outages and breaches strung together (@pelositracker); its own last line says officials call many 'not cyberattacks' | KILL as a pattern claim. CIA, ODNI and FinCEN legs carded (20261124-018, -020, -021); other legs not checked. CYPHER informed |
| 7 | Repeats | FinCEN (20261124-020); PCE, GDP, claims and durables screenshots (three images read) agree with 007 and 020; one figure not on 007: Q3 GDP price index 1.9% against 2.3% survey (screenshot only, BEA not re-read; HENRY); SOFR +4 over IORB [11/24] (018, LIQUID) | DUP |""",
source="NWS Mount Holly image; api.weather.gov 12:49 ET; abcnews.com 138425051 (helper); PitchBook PDF Aug 17 2026; X posts and images; fourweekmba refused (403)",action=["AEOLUS","WATT","BROCK"],info=["CYPHER","ORACLE","LIQUID","HENRY","REGINALD","RED","PROME"],precedence="ROUTINE",confidence=0.75,confidence_language="reports: NWS primary; others secondary as stated per row",cluster="CLIMATE_MACRO",domain="CLIMATE_MACRO",entities=["NWS","PitchBook","Iowa Army Ammunition Plant","Societe Generale","Kalshi"],
dispatch_note="ROUTINE small items. ACTION AEOLUS and WATT (item 1), BROCK (items 2, 4). RED, PROME by BOARD diff.",route_summary="small items, bookmarks Nov 25")]
json.dump(C,open('AGENTS/WALTER/research/2026-11-25_bookmarks/cards-024.json','w'),indent=1)
