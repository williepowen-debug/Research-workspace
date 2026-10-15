# Iran full sweep 10/14 — LEG B: Gulf energy infrastructure / production (FAL-01 class) / Saudi–Houthi

**Executor:** read-only verify-research helper for WALTER · **Written:** 2026-10-15T01:12:26Z (stamp from `date -u` in the writing command) · **Window:** EVENT dates 2026-10-08 → 10-15 (last full sweep 10/08 ~12:20Z). All dates 2026; times UTC unless marked local (AST = UTC+3).
**Read first (owner records):** anchor `IRAN_WAR.md` whole · `IRAN_WAR_GUARDS.md` whole (428 lines, 27 blocks) · 10/08 sweep · FALCON STATUS (last write **10/10 12:17 ET**, `71131f580`), FALCON `reports/2026-10-09`, `STRIKES.tsv` header (swept to 10/10, 0 new rows) · BOARD -1010-002, -1011-006, -1012-003, -1013-008, -1014-002, -1014-003, -1014-025 · WALTER helper notes 10/11, 10/12, 10/13 energy, 10/14 morning + evening. **FALCON owner state = 10/10; 14 WALTER handoffs 10/11-002 → 10/14-026 sit unconsumed in `AGENTS/FALCON/inbox/WALTER/`.** FALCON grades; this file reports facts.
**Guards applied:** 2019 Abqaiq/Khurais trap; Petroline 2019; KILL ① (capacity ≠ loss, applied to the 7 / 5 / 10 / 12 mb/d figures); ADD#24 ATTACKED/SHUT/DAMAGED split; intercepted→struck; ADD#25 force majeure; FAL-01 production-only (offices, airports, gas plants, refineries OUT); ADD#15 FIRMS/imagery never counts; ADD#22 artefact authentication (imagery is unauthenticated); Houthi claims CLAIM-ONLY; ADD#13 name collision; Ras Tanura 3/2 merge hazard; ADD#22 Kharg dates; METHOD NOTE (the Abqaiq item was searched as a possibly real event, not waved off).

## §0 Unreachable / partial primaries

| Source | Result | Used instead |
|---|---|---|
| iea.org OMR (10/14) | 403 / Cloudflare (WebFetch + curl; WALTER's saved `iea.html` is the challenge page) | TT News, CNBC, The National, Morocco World (fetched). Saudi Sept 8.3 mb/d = **search snippet of the IEA table only, not read** |
| opec.org MOMR (10/13) | not fetched | Reuters via The Edge Malaysia, Anadolu (fetched); Commodity Context public summary |
| SPA (spa.gov.sa) | JS shell; article N2698973 returns title only | MoE Dhahran text via Saudi Gazette (SPA relay, 10/14 00:51 local), Türkiye Today, Al Jazeera |
| moenergy.gov.sa; Saudi MoE/MoD on X | connection failed / not attempted (x.com 402 last sweep) | wire relays |
| aramco.com newsroom | JS-limited (one Aug item renders) | CEO 10/12 WPC speech page **fetched (WebFetch)** |
| Saba (saba.ye), Tasnim | not fetched | YPA (Houthi-run, fetched) for Saree text; Newsquawk headline for Tasnim |
| CENTCOM | not attempted (403 last sweep) | GlobalSecurity Day-229 aggregator (fetched) |
| WAM/ADNOC, KUNA/KPC, QatarEnergy, Iraqi oil ministry/SOMO, JODI | not fetched; search only | **SEARCH-NOT-FOUND** for any window event (coverage gap, not a negative) |
| Kpler/Vortexa weekly Saudi/Yanbu loadings for w/c 10/05, 10/12 | no print found; Kpler tracker URLs for 10/8–10/15 404 | Kpler blogs 10/06, 10/07 (fetched) |
| Bloomberg originals; Platts/Argus | paywalled | Bloomberg wire via Rigzone (10/14), Investing.com (10/09, per BOARD -002) |
| France24 live, Gulf Business | 403; Palestine Chronicle 429; Local10 (AP) headline only | Reuters/AFP/Bloomberg copies |

## §1 Incident table (event 10/08–10/15; energy/strategic infrastructure; hulls excluded — other leg)

| Event (date) | Asset · class | Claimant | Confirmer | ATTACKED / SHUT / DAMAGED | Counting source for a production-class hit? |
|---|---|---|---|---|---|
| **Abqaiq + "Tanjib gas plant" smoke (10/08)** — 🆕 **not in FALCON KB or BOARD** | Abqaiq = crude **stabilisation (IN-class on FALCON §2a)** · Tanajib = gas plant (class of the "oil facility" unresolved) | No Saree claim found (YPA search: only 2019 Abqaiq items + this media piece). Media: Soar Atlas imagery "dated Oct 8" (Newsquawk 10/08 09:07Z); Tasnim "massive fire" (Newsquawk 10/09 07:02Z); YPA 10/08 21:01 local "infrared" images, "two fires", "destroyed fuel storage tank" | **None.** Energy News Beat 10/09 06:40 CT: "no Saudi, Aramco, coalition, Reuters, AP or Bloomberg confirmation"; "flaring may be precautionary". Nothing later found | ATTACKED: unestablished · SHUT: none stated · DAMAGED: imagery/claimant only | **NO** — imagery + Iranian/Houthi media never count. Abqaiq is the one IN-class asset in this window's claim set → **FOR FALCON** |
| Shedgum + Hawiyah heat (10/09 night →); "Ghawar BM" (RIA 10/10) | gas plants (OUT); field-level claim | RIA via 1news.az; no Saree text | none | heat only | NO — FALCON 10/10: OUT; unchanged |
| **Shedgum ("Shuqaiq") gas + "Tanajib oil facility" (Saree, 10/11, "past 24h")** | gas plant (OUT) · Tanajib class INDETERMINATE (Aramco 2/26 primary: Tanajib **Gas** Plant, Marjan/Zuluf associated gas) | Saree via YPA 408069 (10/11 19:32 local) + TASS: "led to break out fires" | **none** (no Aramco/MoE/SPA/coalition word found through 10/14; House of Saud 10/12: silence) | claim only | NO. ⚠️ **Name collision (ADD#13 class):** YPA writes "**Shuqaiq** gas facility"; TASS/Saree-EN = **Shedgum** (شدقم). Shuqaiq is also a Jazan-coast town with a power/desal plant. Both readings are OUT of FAL-01 |
| **Haradh (10/13)** | locality in southern Ghawar (Al-Ahsa) — target not named | Houthi BM | **Coalition (al-Maliki, X; via Anadolu/MEMO 10/13, Saudi Gazette)**: BM toward "Haradh Center in Al-Ahsa Governorate" **intercepted and destroyed** | ATTACKED (attempted) · intercepted · no damage reported | NO (intercepted ≠ struck). **FOR FALCON:** a state-acknowledged shot at a Ghawar production locality |
| **Aramco HQ, Dhahran (10/13 evening)** | **office/administrative tower** (houses an operations-management centre) — OUT | Saree 10/14 (YPA 408411): "Aramco in Dhahran… destruction and fires" | **MoE official (SPA relay):** "administrative building… targeted, resulting in a limited fire"; no injuries/deaths | ATTACKED ✅ (MoE) · SHUT: building partly (staff WFH; some functions shifted abroad — Reuters/Bloomberg sources) · DAMAGED ✅ (extent contested, below) | NO — office class. Bloomberg 10/14 (one person): "Oil production operations haven't been affected" |
| Dhahran BM (10/13) | — | Houthi | Coalition: BM toward Dhahran intercepted; **fragments fell in a residential area** | intercepted | — (does not settle direct-hit vs debris at the tower) |
| Aramco Riyadh refinery (claim 10/14) | refinery — OUT | Saree 10/14 statement + 10/13 target map | **none found** (Civil Defense: debris of 2 intercepted cruise missiles → 4 injured, 15 homes, Riyadh 10/13) | claim only | NO (refining OUT; no confirmation) |
| "Ras Tanura refinery" (10/14) | refinery — OUT | Iran International rendering of the 10/14 Houthi claim (via GlobalSecurity) | none | — | **UNSUPPORTED:** the YPA text of the statement names "the Aramco refinery **in Riyadh**", not Ras Tanura; Ras Tanura = 3/2 merge hazard |
| KKIA Riyadh (10/08, 10/10, 10/11, 10/14 claim) · KFIA Dammam (10/11) | airports — OUT | Saree | GACA (see §6) | ATTACKED ✅ | NO |
| UAE (Fujairah, Ruwais, Jebel Ali), Kuwait, Bahrain, Qatar (Ras Laffan), Iraq (Basra, Kurdistan) onshore | — | — | — | **no window event found** (search-only; WAM/KUNA/QatarEnergy/SOMO unread) | — |
| Qatar Emir (10/13) "direct damage to some Ras Laffan energy sites" | LNG | — | Emir (via Khaleej Times live / National) | — | **Not new:** the damage is **March 2026** (2 of 14 trains, ~17% of capacity). Date-trap, §9 |
| Iran: Kharg, South Pars, Bandar Abbas, Abadan | — | — | — | no window event found (§7) | — |

**Dhahran — resolved as far as the evidence goes:**

| Point | Official (MoE via SPA, 10/14 00:51 local) | Anonymous sources | Verdict |
|---|---|---|---|
| Asset | "administrative building affiliated with Saudi Aramco" | office tower in HQ complex; holds an operations centre overseeing rigs, refineries, terminals, pipelines (Reuters) / "operations management office" (Bloomberg) | **Agreed: an office. OUT of FAL-01 and the production rung whatever the extent** |
| Extent | "limited fire" | Reuters 10/14 (3 people, direct knowledge; Rashad/Azhari): "extensive damage"; fire began 9th floor south wing, spread 6th–10th; top three floors (CEO Nasser's office) "severely damaged", ceiling partly caved in, windows/doors blown out; a 4th person: still burning early 10/14. Bloomberg (people familiar): ~3 floors damaged; staff WFH. AP (two regional officials): executive offices incl. CEO office | **UNRESOLVED in degree.** The only on-record account is "limited"; every damage specific is anonymous. They are not contradictory in kind (one building, fire, no casualties) |
| Mechanism | "targeted" | Reuters company source: BM hit the tower; AFP: two employees say a tower was hit, a third source confirms; CNN: unclear if direct hit or debris | Direct hit better supported (three independent anonymous source sets) than debris; **not state-confirmed** |
| Casualties | none | none | 0 |
| Production | not addressed | Reuters (2 people): operations at the complex "continued normally"; Bloomberg (1 person): "Oil production operations haven't been affected" | **No production effect asserted by anyone** |

## §2 FAL-01 / production-class verdict

**FIRM-NEGATIVE HOLDS** (fact basis for FALCON; FALCON grades). No counting source (state, operator, CENTCOM or a named wire on the record) confirms a hostile strike on a Gulf-ally crude **production-class** facility for event dates 10/08–10/15. Every confirmed hit in the window is OUT by class (an office at Dhahran; airports). Every IN-class-capable item is claim- or imagery-only (Abqaiq 10/08; Tanajib 10/08 + 10/11) or was intercepted (Haradh 10/13).

**Production rung D 85→92 (FALCON §2a: counting source + hostile strike + Gulf-ally crude production-class facility, on/after 9/29): ARMED, NOT FIRED on this evidence.** For FALCON:
1. **Abqaiq 10/08 imagery + Tasnim + YPA**: this is the only IN-class candidate in the window, and FALCON has not seen it (no KB row; FALCON's last write was 10/10). A counting confirmation would fire the rung; none was found by 10/14. Treat it as a check-the-world item, not as noise, and not as a hit.
2. **Haradh 10/13**: the coalition confirms a BM aimed at a southern-Ghawar production locality was intercepted. Intent datum only.
3. **Tanajib**: asset identity is still INDETERMINATE (gas plant vs a crude-side unit; -1012-003).
4. **Saree 10/14** forward line: operations "will continue… targeting Saudi enemy airports and oil facilities". A declaration, no target or date. Saba "dispose of Aramco shares" (10/14) is the same.

## §3 Petroline (East-West) / Yanbu

| Item | Finding | Source (date · read) |
|---|---|---|
| New attack on the line or Yanbu, 10/08–10/15 | **None found** | search-based; MoE/SPA newsroom unreadable |
| Bloomberg 10/09: full November volumes to European refiners after Petroline "returned to operation" | Still **unnamed sources only**; **no Aramco/SPA/buyer primary found** | Investing.com/Report.az copies (relayed via BOARD -002); Aramco CEO 10/12 speech (fetched) does not mention Petroline, Yanbu or customers' allocations |
| Minister, WPC Riyadh, **Mon 10/12** | Plan to raise E-W capacity to **10 mb/d within 2–3 years**. ⚠️ Gulf News body says capacity "previously expanded to **five** million" vs the anchor's 7 mb/d nameplate; its headline says "by 2026". **All three are capacity or plan figures, none is a flow (KILL ①)** | Gulf News 10/12 (fetched); Asharq Al-Awsat headline |
| Throughput | No new metered figure. Kpler 10/07 renders the minister's 10/06 "5.8" **as "5.8 Mbd"**, and ENB 10/09 quotes "5.8mn b/d". **The minister's own words were not read; the unit is still not established at the primary** (10/08 sweep) | Kpler blog 10/07, ENB 10/09 (fetched) |
| Restart date | Kpler 10/07 repeats "operations resumed five to six days after the pipeline was hit" (the minister). The IEA (10/14, via The National) dates the "bombing" to **9/11**; the anchor carries attacks 9/10 and the shutdown 9/11. Record question, FALCON's | — |
| Yanbu loadings since 10/08 | **No vendor print found** for w/c 10/05 or 10/12. Latest: Kpler, Saudi loadings **9.1 Mbd w/c 9/21** (post-COVID high); MEG loadings **+3.2 to 4.1 Mbd in Sept**; Kpler 10/06 expects Yanbu barrels "returning", with both corridors kept open | Kpler 10/06, 10/07 (fetched) |
| Bloomberg 10/14 context | "A cross-country pipeline… was temporarily shut last month following an attack." Consistent, nothing new | Rigzone (Bloomberg wire, 10/14 15:25 GMT update) |

## §4 Force majeure (ADD#25: primary words only)

| Company | 10/08–10/15 declaration? | Basis |
|---|---|---|
| Aramco | **None found** | CEO 10/12 speech (fetched): no FM mention; the Europe November restoration (Bloomberg 10/09, unnamed) reverses the October zero allocation, an operational state |
| ADNOC, KPC, SOMO | **None found** (search-only) | KPC CEO 10/05 (Bloomberg/gCaptain relay): meeting crude supply commitments; all refineries operational |
| QatarEnergy | **No new declaration.** The existing LNG FM (declared March) was reported **extended "until at least early December"** (Informed Comment 10/05, relaying OilPrice/Bloomberg traders) | Pre-window extension of an LNG FM; **not crude; not FAL-05 route (a)** |

⇒ No FM state change.

## §5 Supply prints (each with date and basis)

| Print | Figure | Basis / caveat |
|---|---|---|
| **IEA OMR, 10/14** | World supply **+2.5 mb/d m/m to 102.3 mb/d (Sept)**; OPEC+ **+2.1 mb/d, led by Saudi**; "UAE drove the non-OPEC+ increase"; **Gulf crude exports +4.4 to 13.9 mb/d (>75% of prewar)**; Hormuz oil flows **10.9 mb/d**; 2026 supply −5.8 mb/d to 100.7; "renewed attacks in the Gulf leave the recovery fragile"; ME + Russia net gasoil exports 820 kb/d (−1.3 mb/d y/y); observed stocks 509 mb below prewar (end-Sept) | Public highlights via TT News, CNBC, The National (fetched); iea.org 403. **Saudi Sept supply 8.3 mb/d (vs 5.97 Aug) = search snippet of the IEA table only; NOT read.** No Gulf shut-in figure recovered |
| **OPEC MOMR, 10/13** | OPEC+ **39.07 mb/d** (+~903 kb/d); OPEC 25.1 mb/d (+~920 kb/d). **Saudi secondary sources +744 kb/d to ~8.0 mb/d; Saudi direct communication 8.372 mb/d** (+>2 mb/d). Iraq +386 to 3.9 · UAE +86 to 3.9 · **Kuwait −140 to ~1.8** · Iran −99 to ~2.0 | Reuters via The Edge (fetched); Anadolu (fetched; figures read as secondary sources, not stated explicitly). **Two bases (secondary vs direct); never merge** |
| Commodity Context (10/13, public summary) | ME shut-ins **4–6 MMbpd** latest; ~2 MMbpd ex-Iran (~4 incl. Iran) at the Sept low; cumulative loss >2.3 bn bbl (early Oct); Iraq 94% of prewar | Export-implied estimate, analyst |
| Kpler, 10/07 | ~**5 Mbd** ME crude + condensate offline vs Feb (as of 10/06, large share Iran); Saudi supply expected **~9 Mbd in October**; total ME exports ≈ prewar | Vendor model (fetched) |
| Aramco CEO, **10/05** (pre-window) | "Our system is intact"; **12 mb/d maximum sustainable capacity "available within days"** | Reuters via BOE. **A capacity claim, not production (KILL ①).** The National 10/14 re-carries it as "this month" |
| Aramco CEO, **10/12** WPC (primary, fetched) | No asset named, no damage assessment; restoration "in hours and days, not weeks and months"; "studying additional crude export routes"; overseas storage | **Not a counting source** |
| US Energy Sec. Wright, 10/12 WPC | Hormuz oil flows 80–90% of pre-conflict; products 25–35% | Official statement, not a print (Gulf News) |
| KPC CEO, 10/05 (pre-window) | Kuwait ~2 mb/d vs ~2.6 prewar (~75%) | Bloomberg/gCaptain relay |
| Kpler/Vortexa Saudi exports for October; JODI September | **not found / not yet published** | gap |
| Market tell (BRENT's lane) | TASI −1.7%, Aramco −1.6% on 10/14 (Reuters via YPA; Bloomberg "as much as" −1.8 / −1.6) | context only |

## §6 Houthi campaign 10/08–10/15 (claims vs Saudi confirmations)

| Event date | Houthi claim (source) | Saudi / coalition statement | Class | State |
|---|---|---|---|---|
| 10/08 | Warning to "experts, engineers" at all Saudi oil facilities (YPA 407708) + KKIA | **GACA: two attacks on KKIA, 3 Saudis killed incl. a Saudia pilot** | threat; airport | threat · airport CONFIRMED |
| 10/10 | KKIA (claimed per Al Jazeera) | **GACA: 12 killed, 309 injured; 13 after an Indian national died (Indian Embassy)** | airport | CONFIRMED |
| 10/11 | Saree: KKIA ×3 waves; "Shuqaiq/Shedgum gas facility"; "Tanajib oil facility"; KFIA Dammam (YPA 408069, TASS) | **GACA: KKIA T4 hit, 1 killed (Pakistani), 11 injured**; KFIA "came under attack"; coalition intercepted a cruise missile near KKIA. **No word on Shedgum/Tanajib** | airport ✅ / energy CLAIM | — |
| 10/12 | — | Coalition: 2 BMs toward Khamis Mushait + 1 toward Riyadh intercepted (Fox live) | — | intercepted |
| 10/13 | Saree publishes target maps: KKIA, Aramco Riyadh refinery, Aramco Dhahran (YPA 408344) after the coalition's Sanaa al-Sabaha strike | **MoE: Dhahran admin building, limited fire, 0 casualties**; coalition: BMs toward Dhahran and Haradh intercepted; 3 cruise missiles + 3 drones (Riyadh/south); Civil Defense: 4 injured, 15 homes (Riyadh debris) | office ✅ | ATTACKED + DAMAGED (extent contested) |
| 10/14 | Saree (YPA 408411): "Aramco in Dhahran", KKIA, "Aramco refinery in Riyadh", "destruction and fires"; ops "will continue… airports and oil facilities"; later BM on KKIA "hit directly" (YPA 408478). Saba military source: "advise Aramco shareholders to dispose of their shares" (YPA 408425) | Coalition: BM toward Riyadh intercepted; Riyadh/Al-Kharj alerts; one resident hurt by debris in Riyadh (Saudi Gazette sidebar). **No statement on the Riyadh refinery** | refinery CLAIM; airport CLAIM | — |

- **Saudi-confirmed deaths, 10/08–10/11:** 3 + 12 (+1 per the Indian Embassy) + 1 = **17**. Bloomberg 10/14: "at least 18 killed… over the past week" (window not stated). Never merge the tallies.
- 🔴 **FOR FALCON (casualty ratchet):** FALCON's 10/10 STATUS carried KKIA 10/10 as "dozens injured, NOT state-confirmed" and set the RATE-STEP lighting bar at **12 confirmed killed** (rolling 30d: 7). GACA has since confirmed **12 killed / 309 injured (10/10) and 1 killed / 11 injured (10/11)**. On FALCON's own stated bar the rolling count would appear to cross; **FALCON grades this; it is unconsumed in -1011-006.**
- Shareholder line: unnamed Saba "military source", not Saree; names no target or date. A threat statement.

## §7 Kharg / Iranian energy assets

| Item | Finding | Basis |
|---|---|---|
| Kharg seizure | **None found** | search-based |
| Kharg strike / terminal damage, 10/08–10/15 | **None found**. Anchor dates hold: 3/13 and 4/7, both military-only | search-based. GlobalSecurity 10/14: no US/Israeli strike on Iranian territory 13–14 Oct |
| Kharg loadings | No October print. Latest: zero Iranian crude loadings in Sept (Bloomberg 10/01, prior sweep); Kharg loadings "inactive" 9/18–10/03 (Maritime News); Iran output ~2.0 mb/d (−99 kb/d, OPEC secondary, Sept). Blockade-caused, not strike-caused | relays |
| South Pars, Bandar Abbas, Abadan | Nothing in window. Abadan blast ~9/25 (pre-window; "technical failure" per state media, contested) | search |
| Other | Drone hit a Sirik fishing boat (Hormozgan), 3 injured, no attribution (Reuters via JPost) — not energy | GlobalSecurity |

## §8 Ladder items touched

| # | Item | Status | Basis |
|---|---|---|---|
| **1** | FAL-01-class production hit | **NOT FIRED** | §2. FOR FALCON: Abqaiq 10/08 imagery (IN-class, unconfirmed, unseen by FALCON); Haradh interception |
| **4** | Kharg seizure executed | **NOT FIRED** | §7 (search-based) |
| **3** | Grid/power strikes on Iran | **NOT FIRED** | No executed strike on Iranian territory found 10/08–10/15. POTUS 10/08 "no attack before the midterms" (11/3) = tape; blockade "full force" |
| — | Force majeure (re-verify trigger) | **No change** | §4 |
| — | Petroline: line itself struck? restart notice? | **No new statement** | §3 |
| FOR FALCON | Casualty ratchet; Tanajib identity; Dhahran (OUT, logged); 14 unconsumed handoffs | — | §6, §1 |

## §9 Date-trap and merge rejects

| Item | Real date / object | Why it surfaced |
|---|---|---|
| YPA "Abqaiq" search: "NASA images… Abqaiq refineries", "Abqaiq and Khurais… 10 drones", minister on Abqaiq/Khurais | **2019-09-14 → 09-18** | 2019 trap, alongside the 10/08 item |
| Fox "Iran-linked drone attack… satellite images"; The National 10/14 "Abqaiq and Khurais… ~50% of crude" | **2019** | Abqaiq queries |
| Türkiye Today "Satellite image shows smoke, fire at Abqaiq" (3217739) | **April 2026** (ESA image, per search summary) | Abqaiq October query |
| HormuzLetter X "Abqaiq struck… East-West Pumping Station… FIRMS"; ZeroHedge "Abqaiq targeted" | **~7/27** | same |
| The National 10/14 photo "fire at the Aramco refinery south of Riyadh"; Türkiye Today "Flames… south of Riyadh on October 3" | **10/03** (FALCON KB-242) | Dhahran coverage |
| "Aramco HQ Dhahran missile" results (shrapnel near Dhahran; Dammam debris) | **2021-03-07 / 2021-09-04–05** | Dhahran query |
| Ras Tanura as a 10/14 Houthi target; "Houthi strikes on refineries at Ras Tanura" (The National, House of Saud) | Ras Tanura = **3/2/2026, Iran** (Wikipedia "2026 Aramco refinery attack") | merge + actor error |
| Bernama / Yeni Şafak "Houthis claim strikes on Saudi airports, Aramco refinery" | **10/05–06 (Rabigh)** | Saree October query |
| Qatar Emir 10/13 Ras Laffan damage | **March 2026** damage | LNG query |
| OilPrice "Qatar Extends Force Majeure" | **8/28**; Informed Comment extension 10/05 | FM query |
| gCaptain/Bloomberg "Iran resumes Kharg loadings"; "Kharg has no tankers loading" | **6/20; 5/18** cycles | Kharg query |
| Fujairah strikes; Ruwais; Mina al-Ahmadi; Basra/Rumaila; Bapco FM; Kuwait airport | **Mar–Jul 2026** | Gulf queries |
| S&P "Asian refiners receive full Saudi term allocations for November" | **2020-10-13** | Aramco November query |
| Aramco CEO "12 mb/d within days / system intact" | **10/05** (London), re-carried 10/14 as "this month" | capacity quote |
| TradeWinds "New Houthi attack targets Yanbu port" | **10/01** event, already BOARD -1002-014/-016 | Yanbu query |

## §10 What changed since 10/08

The production gate did not move, but the Houthi campaign on Saudi Arabia escalated in reach and in target type. **Saudi authorities confirmed a hit on Aramco's Dhahran headquarters on 10/13** (MoE: "limited fire", no casualties). Three anonymous source sets (Reuters, AP and AFP, plus Bloomberg) describe a direct missile hit with several floors burned, including the CEO's floor, while operations and oil production continued. It is an office, so it is OUT of FAL-01 and of the production rung whatever the extent. The airport campaign became the deadliest of the war on Saudi soil: GACA confirms **12 killed and 309 injured at KKIA on 10/10** (13 after a later death) and 1 killed on 10/11. FALCON's 10/10 casualty ratchet predates both. Saree's claims also widened to Shedgum, Tanajib, KFIA (10/11) and the Riyadh refinery (10/14), and he says "oil facilities" are next. None of these is confirmed. The coalition confirms an interception toward **Haradh** in southern Ghawar (10/13). **One IN-class candidate that FALCON has not seen:** satellite smoke at **Abqaiq on 10/08** (Soar Atlas imagery, Tasnim, YPA). No counting source exists for it, so FAL-01 stays **firm-negative** and the D 85→92 rung stays armed and unfired. Supply moved the other way. The IEA (10/14) has Gulf crude exports up 4.4 to 13.9 mb/d in September. OPEC secondary sources (10/13) have Saudi output up 744 kb/d to ~8.0 mb/d; Riyadh's own figure is 8.372. Kpler expects ~9 mb/d in October, and Bloomberg (unnamed, 10/09) says Aramco is restoring full November volumes to Europe. There is still no operator primary for Petroline's flow unit, no October Yanbu print, no force majeure, no new attack on the line, and no Kharg seizure or strike. **Coverage limits that matter:** IEA, OPEC, SPA, the MoE and the Gulf state agencies were not read at source, and FALCON's owner state is four days old with 14 handoffs unconsumed.
