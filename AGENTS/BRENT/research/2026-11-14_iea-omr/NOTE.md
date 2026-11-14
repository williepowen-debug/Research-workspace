# November 14: IEA November OMR graded at secondaries; FAA ground stop against jet demand; inbox drain (PROME prome-fe commission, C9 / WQ-538 A)

Session started 11:25 EST, note written 11:29–11:4x EST (from `date`). Brief from PROME (prome-fe), not Will's own words. $0, no trade construction, no change to any level, operator, instrument or consequence.

## 0. Access, stated first

| Source | Result | What I did |
|---|---|---|
| iea.org (the report) | Not attempted. WALTER got HTTP 403 from this machine on 11/14 | No evasion. Graded on secondaries only |
| aninews.in, benzinga.com | HTTP 403 (web-fetch, 11/14) | Not retried |
| BNN Bloomberg (Reuters, Alex Lawler, 11/13 07:53 EST); Energy News Beat (11/14); The Edge Kuwait (11/13); IndexBox (11/14); Xinhua Paris (11/13 19:41) | HTTP 200, read by a web-fetch reader | Figures below. Every overlapping figure agrees across pages; no numerical contradiction |
| FRED DCOILBRENTEU, DJFUELUSGULF | HTTP 200, curl from this machine 11:28 EST; newest 11/11 | Saved here as CSV |
| tsa.gov passenger volumes | curl from this machine: **HTTP 403**. One WebFetch read (Anthropic's fetch service, a different client, not a header trick) returned the page | ⚠️ Disclosed: the 11/12 figure is a small-model extraction, single source |
| OPEC November MOMR demand | Argus via search summary only; Argus page not opened | Labelled [EST secondary, search summary] |

## 1. IEA November OMR: what "surplus" means

**Answer in one line:** the 1.7 mb/d "surplus" is a **forecast** for the Q4 2026 average. The **observed** fact is October: world observed stocks rose **+52 mb** (about +1.7 mb/d over 31 days, own arithmetic), the first rise since June. But oil on water rose **+86 mb** in the same month, so **stocks on land fell by about 34 mb** (own arithmetic, 52 − 86) to the lowest since at least 2016 (IEA via Energy News Beat and The Edge). The October surplus is barrels at sea on longer routes, not barrels in tanks near buyers.

Guardian's "returns" and WSJ's "set to return" are both defensible: October's build is observed, the Q4 surplus is forecast.

| IEA figure (11/13 OMR) | Value | Kind | Pages carrying it |
|---|---|---|---|
| Q4-26 world supply | 105 mb/d | forecast | Reuters/BNN; ENB as Reuters |
| Q4-26 supply minus forecast demand | **+1.7 mb/d** | **forecast** ("will return to a surplus in the fourth quarter") | Reuters/BNN; ENB as Reuters |
| Implied Q4-26 demand | about 103.3 mb/d | own arithmetic, 105 − 1.7 | none |
| October world supply | 105.4 mb/d, +2.3 m/m, +5.3 since August, −2.9 y/y | observed estimate | ENB, Edge, IDX, Xinhua |
| October observed stocks | **+52 mb**, first rise since June | observed estimate | ENB, Edge, Xinhua |
| October oil on water | **+86 mb** | observed estimate | ENB, Edge |
| Stocks on land | lowest since at least 2016; cumulative draw since the war began −462 mb | observed estimate | ENB (level), ENB and Edge (−462) |
| Gulf exports excluding Oman, October | 18.4 mb/d, 26% below pre-war; crude 15 mb/d; products and LPG about half of pre-war | observed estimate | ENB, Edge (crude 15: Edge only) |
| 2026 demand | −2.7 mb/d to 102.3 mb/d; Q3 −3.8, Q4 −2.7 y/y | forecast | BNN, ENB, Edge, IDX |
| 2026 / 2027 supply | −4.8 mb/d / +6.6 mb/d to 108.1 | forecast | BNN, ENB, Edge, IDX |
| 2027 surplus | about 3.8 mb/d (3.94 last month) | forecast | Reuters/BNN only |
| Refinery runs | October 81.3 mb/d (−1.3), December 84.7 | estimate / forecast | Edge only |
| Diesel | "overriding concern"; European diesel 77% above pre-war; about $180/bbl (ENB only) | observed | ENB, Edge |
| Dated Brent | $136 high early October to "around $93" at writing | observed | ENB, Edge |

## 2. Grade against EIA and OPEC

| Item | IEA OMR 11/13 | EIA STEO 11/10 (forecast completed 11/5) [CONF API, my 11/10 note § 3] | OPEC MOMR 11/11 | Read |
|---|---|---|---|---|
| Q4-26 supply | 105.0 | 105.14 | not in my records | **agree within 0.14** |
| Q4-26 demand | ~103.3 (derived) | 103.67 | not in my records | IEA about 0.37 lower |
| **Q4-26 balance** | **+1.7 build (forecast)** | **+1.47 build (forecast)** | no balance figure reached | **two agencies agree on a Q4 build of 1.5–1.7 mb/d; IEA about 0.23 larger** |
| October stock change | +52 mb observed (≈ +1.68 mb/d) | −1.69 in EIA's sign convention = 1.69 build (modelled history) | — | **agree to 0.01 mb/d** |
| 2026 demand growth | −2.7 mb/d | −2.0 mb/d (text) | **+0.18 mb/d to 105.72** [EST Argus via search summary, unchanged from October] | **OPEC is the outlier by about 2.9 mb/d on growth.** Levels are not comparable across agencies (different perimeters) |
| Saudi / Middle East October | Gulf exports 18.4 ex-Oman, −26% vs pre-war | ME shut-ins 2.5 mb/d | Saudi secondary 9.194 | different perimeters; all three say supply rose in October; **never summed** |
| **Spare capacity, January 2027** | **NOT FOUND on any readable page** | COPS_OPEC 0.01 | Saudi self-report implies about 1.2–1.3 room (production 10.563 vs supply 9.203) | **still CONTESTED; the IEA did not adjudicate it in anything I could read** |

**Verdict.** On the Q4 balance, the second agency confirms the first: EIA and IEA both have a Q4 build near 1.5–1.7 mb/d, driven by supply (Gulf restart, Russia), with demand still down year on year. OPEC disagrees through demand, not supply (its 2026 demand still grows). The IEA adds one thing EIA's balance cannot show: **where the October surplus sits**. It is on the water, and land stocks are at a ten-year low.

## 3. The physical side moved too: Dated is now under the futures

FRED DCOILBRENTEU (Dated/North Sea spot, EIA via FRED; pulled 11:28 EST, newest 11/11) [CONF]:

| Date | Dated Brent | BZF27 settle basis [EST vendor proxy, my records] | Dated minus future |
|---|---|---|---|
| 11/3 | 107.03 | about 103.60 (vendor row, 11/3 combo note) | about +3.4 |
| 11/4 | 91.84 | — | — |
| 11/9 | 91.03 | 92.57 (THESIS 11/10) | **−1.54** |
| 11/11 | 92.14 | 92.76 (SCRATCH 11/13) | **−0.62** |

The physical premium over paper that STATUS carried as "Dated $107.03 on 11/3" collapsed on 11/4 (−$15.19 in one print) and has stayed **at or below the future** since. My 11/8, 11/10 and 11/11 notes called Dated "newest $107.03 (11/3)"; that was FRED's newest when pulled (11/11 08:52 EST), and the 11/4–11/11 prints have posted since. **That claim is overtaken**; corrected here, not silently.

## 4. What it does to my rows (letters unchanged)

| Row | Effect |
|---|---|
| combo:paper-physical-gap (what_to_check: "Dated minus the pinned future under $2 on the same date, **or** a stock build in the November STEO or IEA report") | **Both conditions now met** (Dated −0.62 on 11/11; IEA observed October build +52 mb). Logging only: it moves no score, band, gate or trigger (WQ-622 A). Counter-member logged beside it: the build is at sea and land stocks are at a ten-year low, so the prompt physical market can stay tight while the balance is in surplus. The theme's answer leans to **"the paper surplus is real on the water; the gap that remains is location, not existence."** |
| combo:gulf-flow-basis | Member: IEA Gulf exports ex-Oman 18.4 mb/d October, 26% below pre-war, crude 15 (single page). Different perimeter from Kpler Hormuz 10.5 and Kpler Gulf crude incl. bypass 16.7 (WALTER 11/11); not summed |
| combo:diesel-buffer | Member: IEA calls diesel the "overriding concern"; European diesel 77% above pre-war; October runs 81.3 mb/d. Supports the theme; no figure on US stocks |
| BRT-33 (F-a, M1−M3 under +3.50 by 11/27) | Direction-supportive (a surplus and Dated under futures argue for flatter spreads), but the 11/13 window read was +4.9903 and steepened on 11/12. **No re-mark** |
| BRT-34 (US distillate under 95M) | IEA diesel tightness is consistent; no US figure in it. No re-mark |
| BRT-07, BRT-32, BG-02 | Untouched: no Hormuz reopening, no Yanbu loading statement |
| MKT-BZ-F-BELOW-85 | Not crossed (BZF27 about 95.8 on 11/13, vendor) |
| 11/29 OPEC+ January letter | The Q4 build now has two agencies. Spare stays **CONTESTED** (EIA 0.01 against Saudi's implied 1.2–1.3); the IEA figure is the missing piece |
| THESIS v5.13 (crude loosening, products tight) | Confirmed by a second agency in the same split ("Oil swings back to surplus, diesel doesn't"). Path A record-only (no registered grader, WQ-331 P4). **No version change** |

## 5. Figures still missing, and where Will's browser could read them

| Missing figure | Where |
|---|---|
| IEA effective spare capacity (Saudi, OPEC+), October and January | The OPEC+ crude supply table of the full report (paid). The free page `https://www.iea.org/reports/oil-market-report-november-2026` (Highlights) may state it in prose |
| Russia October output change (the "+210 kb/d" relay is unverified) | Same free Highlights page, or CNBC 11/13 12:05Z "Russian crude production rebounds after Trump diesel deal" |
| IEA Q4 demand level and Q4 stock change as printed (I derived 103.3) | Highlights page balance chart; full report Table 1 |
| Iran output (Iran International: "below pre-war domestic needs") | Highlights page or full report Table 4 |
| OPEC's call on OPEC+ crude and its implied balance | OPEC November MOMR Table 11-1 (Will downloaded the PDF 11/11; WALTER holds pages 54–55 only) |

## 6. FAA ground stop and jet demand (card SIG-W-20261114-001)

| Item | Figure | Source |
|---|---|---|
| Ground stop | 15:54 EST to about 20:15 EST Fri 11/13, about 4 h 21 min | Wikipedia/CBS, Duffy per search summary; one report says lifted about 19:30 |
| Cause, as stated | FAA: "communication issues impacting multiple Air Route Traffic Control Centers". Bedford (FAA Administrator, Sat): "an equipment issue", "zero evidence of anything nefarious". Duffy (Sat, ABC): a contractor replacing copper with fibre at a remote FAA site; a router "started flooding other routers"; "contractor error or a faulty piece of equipment"; Duffy says L3Harris "owns that network" | ABC and Yahoo live blogs. **Not an FAA finding.** **Nothing links Peraton** (card 007 item 2 stays context) |
| Friday cancellations / delays | **9,132 / 7,030** (FlightAware, final, reported 06:52 EST 11/14) | ABC. The earlier "nearly 8,000 / 8,500" is an intraday snapshot; do not mix |
| Saturday cancellations | 3,374 at 06:52 EST; more than 4,000 at 10:50 EST; Bedford expects 4,000–5,000 of about 41,000 scheduled | ABC, Yahoo |
| TSA checkpoint | Thu 11/12 **2,484,345**; **Fri 11/13 and Sat 11/14 NOT POSTED** at about 11:27 EST | tsa.gov via WebFetch extraction, single source (⚠️ section 0) |
| US jet fuel product supplied | 4-week average 1.777 mb/d, week to 11/6, +1.8% y/y | [CONF EIA WPSR, read 11/12] |
| Gulf Coast jet spot | 4.035 $/gal on 11/11; **11/12 and 11/13 not posted** | FRED DJFUELUSGULF, pulled 11:28 EST |

**Size of the dent (own arithmetic, upper bound):** 9,132 of about 41,000 daily flights is about 22% of one day. 22% of 1.777 mb/d is about **0.39 mb of jet fuel**, about **0.056 mb/d** averaged over the week to 11/13 and about 0.014 mb/d on the 4-week average. Saturday's 4,000–5,000 cancellations (about 10–12%) land in the week to 11/20, about 0.03 mb/d. It is an upper bound: cancellations skew to smaller regional aircraft, and 3,500 aircraft already airborne at the order flew on. **This sits inside ordinary weekly noise in EIA's jet series; the 11/18 WPSR will not be able to show it as a signal.** It is a one-day airline revenue and operations event, not a demand-destruction datum, and it is not fuel-price-driven, so it is **not BRT-09 / airline-capacity evidence**.

**Not posted yet:** TSA 11/13 and 11/14 (TSA updates Monday to Friday by 9 a.m.; expect by Monday 11/16); EIA WPSR week to 11/13 (Wednesday 11/18, modelled, verify at eia.gov); FRED Gulf jet 11/12–11/13; airline cost or revenue estimates (none found).

## 7. Inbox drain (both lanes)

| Card | Disposition | Note |
|---|---|---|
| SIG-W-20261114-004 IEA OMR | acted | Sections 1–5 |
| SIG-W-20261114-001 FAA ground stop | acted | Section 6 |
| SIG-W-20261114-003 Trump-Putin-Xi trilateral (Shenzhen, late week of 11/16; Xi bilateral Thu 11/19) | noted | Iran "may" come up is BBC's line, not the White House's. No BRENT row moves; the Russian diesel import deal it cites is HAWK/OSPREY context. Watch only for a Hormuz or Iran-export statement out of it |
| SIG-W-20261114-006 small items | noted | Item 6 (Bloomberg: Ukraine's ninth Russian refinery hit in November; "Russian diesel exports drop") logged on combo:diesel-buffer as a member, against the 11/12 "Russian diesel exports double" headlines; OSPREY owns the strike record. Item 1 (polar vortex; heating oil +59% y/y in Maine, CNBC) logged on diesel-buffer as context. Item 10 (New Orleans collision, Mississippi traffic shut during rescue, reopening not stated): no refinery or crude-flow figure; record only. Rest outside domain |
| SIG-W-20261114-007 Will's bookmarks | noted | Item 2 (Peraton): context only, section 6. Item 3 (Volgograd second partisan witness): still UNVERIFIED, added to the existing diesel-buffer member. Others outside domain |
| Top-level inbox | empty | No MSG-* files |

## 8. For TERRY (via PROME), material only

The fleet mirror shows held USO shares and VLO lines (FORGE mirror, 11/10 intraday; positions are TRADE's and Will's). Material for a tradeability read, not a construction:
1. Two agencies now forecast a Q4 crude surplus of 1.5–1.7 mb/d, and the observed October build is real but at sea.
2. Dated Brent has traded at or under the front future since 11/4 (−0.62 on 11/11), so the physical premium is gone.
3. The front spread is still backwardated (+4.99 M1−M3 on 11/13, vendor), so a long-futures holder still earns roll yield while it lasts.
4. Products stay tight on both agencies' reads (refiner margin side).
5. The ground stop is not an oil signal.
