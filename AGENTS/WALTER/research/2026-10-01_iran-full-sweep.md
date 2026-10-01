# Iran-theater verify sweep — 2026-10-01

**Executor:** read-only verify-research subagent for WALTER · **Written:** 2026-10-01T15:10Z (stamp from `date -u`) · **Scope:** 7 claims sourced so far only to ZeroHedge 9/30, the No1 Daily Digest Substack 10/01, @HormuzLetter and MenchOsint.
**Method:** owners first (UKMTO, SPA/MoE/Aramco, ADNOC/WAM, CENTCOM, IRNA, State), then named wires, then OSINT. Event-date window 2026-09-29..10-01 enforced; date-trap rejects listed in §9.
**Guards applied (`IRAN_WAR_GUARDS.md`):** KILL-ON-SIGHT ① (Abqaiq "~7 mb/d", "5–7% of global supply"), ADD#15 (FIRMS not a confirmation), ADD#20 ("ceasefire"), ADD#24 (ATTACKED / SHUT / DAMAGED kept as separate states; capacity ≠ loss), ADD#26 ("unknown projectile" is a phrase, not an event ID), ADD#23 (front-month roll), syndication ≠ corroboration.

## 0. Unreachable primaries (stated up front)

| Source | Result |
|---|---|
| ukmto.org `/recent-incidents`, home, and the indexed PDF `20260930-ukmto_warning-146-26.pdf` | **403** (WebFetch and curl with a browser user agent). The PDF's existence and date (2026-09-30, warning **146/26**) come from its indexed URL only; **contents unread** |
| axios.com (10/01 scoop; 9/29 piece) | 403 — content taken from verbatim relays (Kurdistan24, Saudi Gazette/Anadolu, investingLive) |
| Seatrade Maritime, Al Arabiya, US News (Reuters wire), IranWire, inkl, EgyptToday | 403 or timeout |
| x.com posts | 402. Post times decoded from the snowflake IDs (exact to the millisecond) |
| SPA, Saudi MoD, Aramco newsroom, ADNOC/WAM, CENTCOM | Searched: **no statement found** for 9/29..10/01 on any of the claims below. This is absence-of-finding through search, not a read of each newsroom |
| NASA FIRMS | No own pull (no MAP_KEY; FALCON hit `Invalid MAP_KEY` too). Coordinates are **secondhand** (ZeroHedge) |

## 1. Per-claim verdicts

| # | Claim | Verdict | One-line basis |
|---|---|---|---|
| 1 | Abqaiq-area fire 9/30 | **CORRECTED-FRAMING** | A **fire was observed** by satellite (several instruments, all relayed by OSINT accounts). The OSINT's own measurement puts the origin **~45 km WEST of Abqaiq, in the North Ghawar / Ain Dar area, not the Abqaiq plant**. **Attack, damage and production effect: NOT established.** No Saudi, Aramco, CENTCOM or wire confirmation found |
| 2 | ADNOC Bu Hasa "143 MW fire" | **INDETERMINATE** | Only one OSINT account plus one blog. No ADNOC, WAM or wire confirmation. Cause unknown. "Iran appears to have struck" is the account's own inference |
| 3 | UKMTO 9/29: three tankers struck | **CONFIRMED (event) / CORRECTED (details)** | UKMTO late reports: **3 tankers struck by unknown projectiles 9/29, plus a 4th (Kuwait-flagged AL FUNTAS) 9/28 with a fire, extinguished.** No casualties and **no sinking**. The names come from third parties, not UKMTO. "All UAE-owned/managed" is **wrong**: SINBAD is managed by Anglo-Eastern. AL RUWAIS's vessel type and flag **conflict** across sources |
| 4 | Iran received the US counter-proposal | **CONFIRMED** (Iranian side) | Mohajerani, Wed **9/30**: received through Qatari mediators. Araghchi got it in **Doha on the evening of Tue 9/29**. Contents undisclosed. Reuters: **sequencing** is the sticking point. **No on-record US confirmation found** |
| 5 | Rubio ordered the Iranian delegation out | **CONFIRMED AS A REPORT** (anonymous US officials). **Iran DENIES it** | Axios scoop (URL dated 10/01, out late 9/30 ET). The **order is dated Mon 9/28 evening**. The delegation flew NY→Doha at 01:20 local on Tue 9/29. Iran's UN mission: the departure followed a schedule given to State on 9/17. No State Dept on-record statement found |
| 6 | Yanbu / Petroline; Hormuz transit counts since 9/22 | **UPDATED** (see §7) | Reuters 9/29: Aramco **notified customers on 9/28 of its October Yanbu loading schedule** (one Asian refining source). Kpler: pipeline throughput ~2.65 mb/d. Yanbu loadings ~2 mb/d (two trade sources). Transit counts still disagree by an order of magnitude: **PortWatch 1 (9/27) vs Windward 16 (9/28) and 17 (9/29)** |
| 7 | Dec Brent ~$99.94, +1.9% | **EXPLAINED (wire)** | CNBC 10/01: Brent +1.8% to $99.81. Driver: a **Reuters report that PetroChina cancelled some October gasoline/jet exports** (multiple unnamed sources). **No wire ties the move to Abqaiq, Bu Hasa or the tankers** |

---

## 2. Claim 1 — the Abqaiq-area fire, 2026-09-30

### Timeline (UTC; X times decoded from post IDs)
| Time (Z) | Source | Content | Weight |
|---|---|---|---|
| ~06:45–07:15 | EUMETSAT Meteosat (per HormuzLetter); MenchOsint "visible by satellite starting from 07h15 UTC" | Black smoke plume, **~90 km long**, visible **7+ h** until sunset | Instrument reading, **relayed by OSINT** |
| 14:33:46 | MenchOsint `2105305106874822855` | "Plume of black smoke erupting from an oil facility in Saudi Arabia's Abqaiq" | OSINT |
| 15:26:08 | HormuzLetter `2105318283024961949` | "Houthis **appear** to have struck the Abqaiq oil processing facility … handling around **5 to 7% of global oil supply**" | ⛔ **KILL-ON-SIGHT ①**: an Abqaiq capacity share presented as if at risk |
| 15:34:44 | @hey_itsmyturn / sh1n.org `2105320448934236599` | "Aramco **pumping station west of Abqaiq** on fire at ~0700Z … no statements by [Houthis]" | OSINT |
| 17:25:57 | HormuzLetter `2105348436576944410` | "First ground-level image … smoke rising from Saudi Aramco's **North Ghawar production facility** … plume origin roughly **45 km west of Abqaiq, at Ghawar rather than the Abqaiq stabilization plant**" | **The account corrects its own 15:26 post** |
| 9/30 (time n/a) | ZeroHedge, "Signs Of Fresh Houthi Attack On Saudi Aramco Facilities" ([link](https://www.zerohedge.com/geopolitical/iran-says-it-received-official-us-counter-offer-ending-war)) | **NASA FIRMS coordinates 25°50'21.3"N 49°13'36.3"E**, "near a **processing facility south of the Ayn Dar oil field**, not the main Abqaiq facility". IRNA, citing **anonymous** sources: Houthis attacked "Abqaiq oil city" on Wednesday afternoon. "No official confirmation" | Secondhand FIRMS; Iranian state media citing anonymous sources = **not a primary for the event** |
| 10/01 | No1 Daily Digest ([link](https://no1sdailydigest.substack.com/p/daily-digest-2026-10-01)) | Adds "smoke at North Ghawar and at Ain Dar, near the East-West pipeline" (OSINTWarfare, MenchOsint). Dissent: "**OilPrice.com saw only routine flaring at Abqaiq**" (via OilandEnergy) | Aggregator. The OilPrice dissent is **itself unverified**: I found no OilPrice article saying it |

**Own geometry check:** the FIRMS point lies **45.5 km WSW of the Abqaiq plant** (great-circle distance; Abqaiq plant taken as ≈25.93N 49.67E). That matches HormuzLetter's "~45 km west". So the two OSINT measurements agree with each other, and **both place the origin away from the Abqaiq stabilization plant.** I could not identify the facility at those coordinates (no facility GIS layer was reachable).

### State table (ADD#24: separate states)
| State | Status | Basis |
|---|---|---|
| **FIRE / SMOKE OBSERVED** | **Supported**: satellite plume + FIRMS + one "ground-level image" | All relayed by OSINT accounts (one channel under syndication ≠ corroboration). **The instrument readings are real types of evidence, but none was pulled by us or by a named wire** |
| **ATTACKED** | **NOT established** | No Saudi MoD, SPA, Aramco, CENTCOM or wire statement. No Houthi (Saree) claim found as of the reports. Only IRNA's anonymous-sources line |
| **DAMAGED** | **NOT established** | No operator statement and no damage imagery analysis |
| **PRODUCTION / FLOW AFFECTED** | **NOT established** | Nothing found. CNBC's 10/01 oil-market piece **does not mention it at all**. It cites the Yanbu restart easing supply worries |
| **WHICH FACILITY** | **NOT established** | Candidates in circulation: Abqaiq plant (contradicted by the plume geometry) · "pumping station west of Abqaiq" (would be TRANSPORT, i.e. Petroline's origin) · "North Ghawar production facility" / "processing facility south of Ayn Dar" (would be PRODUCTION, a GOSP-class asset) |

**FAL-01 relevance (for FALCON, not graded here):** this is the subtle part. If the origin really is a **Ghawar/Ain Dar GOSP**, then this is the **production-asset class FAL-01 watches**, which matters more than an Abqaiq processing headline would. If it is a **pumping station**, it is transport (like Petroline 9/11). Neither an attack nor a facility is established, so **FAL-01 stays NOT FIRED on this evidence.** Also live: the "routine flaring" alternative. Large flares register in FIRMS, but a 90 km black plume lasting 7+ h is not typical flaring. Neither reading is settled.

**Wire check:** searches of Reuters, Bloomberg and AP surfaced **no** 9/30–10/01 item on an Eastern Province fire. Every "Abqaiq fire" hit from wires or mainstream outlets was a date trap (§9).

---

## 3. Claim 2 — ADNOC Bu Hasa (UAE)

| Item | Finding |
|---|---|
| Origin | HormuzLetter `2105353196432679349`, **2026-09-30T17:44:52Z**: "Iran **appears** to have struck ADNOC's Bu Hasa facility … Sentinel-3 imagery … black smoke plume roughly **50 km** … NASA FIRMS recorded a fire radiative power of **143 megawatts** … VIIRS mid-infrared channel reading **367 Kelvin**, the absolute ceiling". Also "Flights near Abu Dhabi were disrupted earlier today" (unsourced) |
| Echo | coreinsightsintl.com blog, 9/30 ([link](https://www.coreinsightsintl.com/post/iran-hits-bu-hasa-oil-facility-in-united-arab-emirates-only-route-around-strait-of-hormuz-now-burn)): "smashed and burning". Cites **no** official statement. Same data as the X post = **same channel** |
| ADNOC / WAM / UAE MoD | **Nothing found** for 9/29–10/01. WAM search returned only Feb–May 2026 interception statements |
| Wires | Nothing found |
| Cause | **Unknown.** Attribution to Iran is inference |

**Caveats that travel with it:** (a) **143 MW FRP is a single-pixel radiative reading, not a damage or loss measure.** Large gas flares at oil fields register routinely in FIRMS, and VIIRS I4 saturation (~367 K) is common for flares, so "hotter than the data shows" is not evidence of an attack. (b) ⛔ "Bu Hasa feeds Habshan–Fujairah, the UAE's only Hormuz bypass" is **geography, not an impact**. It must not become a "UAE bypass offline" claim (ADD#24 capacity ≠ loss). **Verdict: INDETERMINATE.**

---

## 4. Claim 3 — UKMTO, tankers struck 9/28–9/29

### Per-vessel table
| Vessel | Event date | UKMTO description (via relays) | Type / flag / manager | Identified by | Damage / casualties | Sunk? |
|---|---|---|---|---|---|---|
| **AL FUNTAS** | **9/28** (Mon evening) | Struck by unknown projectile, **fire, later extinguished**; "vessel is underway" | Kuwait-flagged crude tanker | IMO tracking (per DataPortuaria) | Crew safe | **No** |
| **MERSIN PROSPERITY** | **9/29** | "Crude oil tanker that was struck on its **port side**" | 2008-built VLCC, 299,319 dwt. **Flag conflict: Liberian** (Maritime Executive, Reuters) **vs Vanuatu** (DataPortuaria). Manager **ADNOC L&S** | Vanguard Tech; IMO tracking | No casualties reported. Damage extent not stated | **No** |
| **SINBAD** | **9/29** | "**Inbound** tanker that was struck by an unknown projectile" | Aframax, 115,949 dwt, Liberian. Manager **Anglo-Eastern Tanker Management** (not UAE). Loaded products at Jubail in early September. Last reported at Fujairah | IMO tracking; Marisks | None reported | **No** |
| **AL RUWAIS** | **9/29** | UKMTO: "an **LNG tanker** was struck by an unknown projectile on September 29th" (Newsquawk headline, **9/30 09:40 UTC**) | **CONFLICT:** Vanguard Tech names the UKMTO LNG ship as AL RUWAIS, **Bahamas-flagged LNG**. Reuters/Marisks list AL RUWAIS as an **oil-products tanker, Liberian, ADNOC L&S**, discharging diesel after an STS transfer off Sohar | Vanguard Tech / Marisks | "No damage, crew safe, no pollution" (DataPortuaria relay) | **No** |

**Sources:** Maritime Executive, 2026-09-30 14:56 ([link](https://maritime-executive.com/article/three-vessels-struck-in-strait-of-hormuz-as-iran-s-grip-loosens)) · Reuters wire syndicated via MarineLink 10/01 ([link](https://www.marinelink.com/news/three-oil-tankers-fire-strait-hormuz-543387)), Baird Maritime 10/01 ([link](https://www.bairdmaritime.com/security/incidents/three-tankers-transiting-strait-of-hormuz-hit-by-projectiles)) and OilPrice 10/01 ([link](https://oilprice.com/Latest-Energy-News/World-News/Three-Tankers-Struck-by-Unknown-Projectiles-in-Strait-of-Hormuz.html)), all **one wire**. In it: "Three Liberian-flagged oil tankers were struck by unknown projectiles when transiting the Strait of Hormuz on Tuesday". Marisks: AIS transponders off. ADNOC L&S and Anglo-Eastern declined or did not respond · DataPortuaria ([link](https://dataportuaria.com/en/internacional/current-affairs/attacks-on-four-tankers-reported-in-strait-of-hormuz-transit-eb3796)) · TASS 9/30 ([link](https://tass.com/world/2195113)): UKMTO "no reports of casualties"; UKMTO did not name the vessels · Seatrade, "Four vessels struck in Hormuz in 24 hours" (403; snippet: "UKMTO released four late reports … from 28 and 29 September") · Newsquawk ([link](https://www.newsquawk.com/headlines/ukmto-says-that-an-lng-tanker-was-struck-by-an-unknown-projectile-on-september-29th)).

**Established:** four UKMTO late reports, 9/28 (1) and 9/29 (3). Unknown projectiles, attacker unnamed, no casualties reported, **no sinking, no mine**. **Not established:** UKMTO positions (primary 403), which corridor ("southern corridor" is OSINT framing), the attacker (a social-media attribution to Iran is unconfirmed per UKMTO relays), the actual vessel type/flag of AL RUWAIS, and Mersin Prosperity's flag. **Correction:** "UAE-owned or UAE-managed SINBAD, MERSIN PROSPERITY and AL RUWAIS" overstates it. Two of the three are ADNOC L&S-managed; SINBAD is Anglo-Eastern. ADD#26: same day ≠ same event. Keep four separate events.

**GATE 2 / losses:** unchanged at 3. No hull lost.

---

## 5. Claim 4 — Iran received the US response

| Item | Finding | Source |
|---|---|---|
| Statement | Government spokesperson **Fatemeh Mohajerani, Wednesday 2026-09-30**: Tehran "has received Washington's proposal responding to Iran's proposed seven-day initiative". Araghchi presented the US response to Pezeshkian **at a Cabinet meeting** (to IRNA) | Xinhua, 2026-09-30 22:10:16 UTC ([link](https://english.news.cn/20260930/6a245773450245dfad2da3d99a5f4a00/c.html)) · ZeroHedge 9/30 quoting IRNA · Reuters via US News 9/30 ([link](https://www.usnews.com/news/world/articles/2026-09-30/iran-receives-us-feedback-on-seven-day-trust-building-plan), timed out) |
| Handover | Araghchi received the US feedback **from Qatari mediators in Doha on Tuesday evening, 9/29** | Reuters via search relays; Voice of Emirates 9/30 |
| Reuters substance | Seven-day plan "aimed at building trust". **Sequencing is the main sticking point**, not the components. Sourcing: "a senior Iranian official" / "a briefed official". HNGN gloss: Iran front-loads US concessions, while Washington wants nuclear steps first | Kurdistan24 ([link](https://www.kurdistan24.net/en/story/942944/iran-receives-us-response-to-seven-day-hormuz-proposal-gap-is-over-sequencing-not-substance)) · HNGN 9/30 ([link](https://www.hngn.com/articles/273398/20260930/iran-gets-formal-us-answer-hormuz-plan-sequencing-splits-sides.htm)) |
| Contents | **Not disclosed** by Iran | All sources |
| Pezeshkian | Any deal must be "win-win". Iran is "making every possible effort to ensure the success of the Islamabad Memorandum of Understanding" (ISNA) | hathalyoum / EgyptToday relays |
| **US side** | **No on-record White House or State confirmation found.** Context: Axios 9/28 headline "Trump willing to ease sanctions and unfreeze assets in exchange for Iran nuclear concessions" · Axios 9/29 "U.S.-Iran talks yield little, raising odds of renewed combat" (headlines only, 403) · **Trump, Wed 9/30:** "Maybe I will blow 'em up … We will blow 'em up or make a deal. But the time is c[oming]" (Kurdistan24 relay) | |

**Exact Persian wording: not obtained** (English renderings only). ⛔ Some secondaries (straits.live) call it a "**ceasefire** counterproposal". **Do NOT carry that** (ADD#20). **MEDIATED ≠ BILATERAL:** the channel is Qatar.

---

## 6. Claim 5 — "Rubio ordered the Iranian delegation out of New York"

| Item | Finding |
|---|---|
| Primary report | **Axios scoop**, "Rubio ordered Iranian delegation to leave the country, U.S. official says", URL `axios.com/2026/10/01/rubio-iran-unga-delegation-kicked-out` (403). First relays: Washington Examiner **9/30 23:06 ET**; Iran International EN post `2105452727396356297` = **2026-10-01T00:20Z** ("Axios reported Wednesday") |
| **Event date** | **Order: Monday 2026-09-28 evening.** The US mission to the UN told Iran's mission, "at Rubio's orders", that the delegation had to leave "immediately". Delegation incl. Araghchi boarded **NY→Doha at 1:20 a.m. Tuesday 9/29** (05:20 GMT) |
| Sourcing | **One US official** + a "second source familiar" (Axios). Anadolu: "two US officials" (Saudi Gazette 10/01). Quote (US official): "Secretary Rubio kicked out the Iranian delegation who had overstayed their welcome. The UN General Assembly was over, so it was time for them to go." The **second source said Araghchi was already scheduled to return Monday night** |
| Iran response | Iran's UN mission: "The Iranian delegation left New York on Monday evening, in accordance with the schedule that had also been communicated to the US Department of State in advance on September 17 … Having achieved nothing, the State Department has resorted to propagating baseless and worthless news" (Saudi Gazette/Anadolu, 10/01 12:44 ([link](https://saudigazette.com.sa/article/665016/world/iran-rejects-expulsion-claim-after-rubio-orders-araghchis-delegation-to-leave-new-york))) |
| State Dept on record | **None found** |
| Talks | Axios: by late afternoon Mon 9/28 talks were "stalemate[d]". **Qatari mediators continue** on a compromise proposal |

**Order vs report:** what is established is a **report, from anonymous US officials, that an order was given**, and it is **disputed** by Iran's mission. **Sequence matters:** the order (9/28) came **before** Iran received the US response in Doha (9/29). So "expelled" and "received counter-proposal" are **not contradictory**: the mediated channel kept running after the New York leg ended. Kurdistan24 relay ([link](https://www.kurdistan24.net/en/story/943142/rubio-orders-iranian-delegation-to-leave-us-after-talks-stall-axios-reports)) · investingLive 10/01 00:19 ([link](https://investinglive.com/commodities/rubio-orders-iranian-delegation-out-of-new-york-after-talks-stall-axios-reports/)).

---

## 7. Claim 6 — Yanbu / Petroline, and Hormuz transit counts

### Yanbu / East–West line (all event dates 9/27–9/28)
| Figure | Object | Source / date | Sourcing quality |
|---|---|---|---|
| **Aramco "notified customers on Monday evening [9/28] of its October loading schedule from Yanbu"** | Operational notice (not a public statement) | Reuters (Tan/Liu/Yap, Singapore) 2026-09-29 via MarineLink ([link](https://www.marinelink.com/news/yanbu-oil-loadings-resume-pipeline-543342)) and Baird ([link](https://www.bairdmaritime.com/shipping/ports/saudi-crude-flows-again-from-red-sea-port-of-yanbu-as-key-pipeline-restarts)) | **One** Asian refining source. Aramco "did not immediately respond" |
| Yanbu crude loadings **~2 mb/d "since last week"** | Loadings | Same Reuters | Two trade sources |
| Pipeline throughput **~2.65 mb/d**, expected **3–4 mb/d** in coming days; **~5.5 mb/d pre-attack rate could take another month** | Line FLOW | Same Reuters, Kpler | Vendor estimate |
| ~3.5 mb/d flow | Line FLOW | Bloomberg 9/28 (already in the anchor) | One person |
| ~10M bbl loading at Yanbu + Al Muajjiz, 40 tankers | Imagery, **9/27** | TankerTrackers (ESA imagery) via Reuters | Vendor/visual |
| ~10M bbl loaded at Yanbu **Mon 9/28**; Saudi loadings **8.5 mb/d 7-day average** ("highest of the war") | Loadings | AGBI 2026-09-30 07:11, Kpler ([link](https://www.agbi.com/analysis/oil-and-gas/2026/09/saudi-oil-exports-hit-wartime-high-as-pipeline-flows-resume/)) | Vendor |
| **7 mb/d** | **NAMEPLATE CAPACITY**, never a loss or flow | Reuters, AGBI | ⛔ ADD#24 |

**Two FLOW figures, two sources:** Kpler 2.65 vs Bloomberg 3.5 mb/d. They are different estimates of the same object; carry both with attribution and do not average them. **Still no Aramco or MoE public statement; "line struck/damaged" is still confirmed by nobody.** ⛔ The digest's "East-West bypass appears to still be shut, judging by Polymarket odds" (JustDario) is **REJECTED**: the Reuters/Kpler vessel data contradicts it, and prediction-market odds are not a flow instrument.

### Hormuz transit prints since 9/22 (all FLOORS, not levels; anchor's denominator is 88/day)
| Print | Date | Source | Note |
|---|---|---|---|
| **55 AIS-visible transits, 9/16–9/23** (~94% below ~910/week prewar) | 9/16–23 | Windward blog 2026-09-29 ([link](https://windward.ai/blog/is-iran-losing-its-grip-on-strait-of-hormuz-traffic/)) | AIS-only. Windward says the true count is higher (dark tankers) |
| **16** (11 in / 5 out; 11 AIS + 5 dark) | 24h ending 9/28 | Windward via search relay | |
| **17** (6 in / 11 out; 7 dark, 6 of them tankers; 5 of the 7 dark used the northern corridor) | 9/29 | Windward via Maritime Executive 9/30 | |
| Southern corridor = **39%** of traffic since 9/7 (vs 17% Jul–Aug) | since 9/7 | Windward | |
| **1 transit** | 9/27 | IMF PortWatch via straits.live 9/29–9/30 ([link](https://straits.live/briefs/2026-09-29)) | straits.live quotes an **85/day** baseline. ⛔ the canonical figure is **88** |
| ~**10 mb/d** average through the strait in September vs ~16 prewar; +~6 mb/d via bypasses; Gulf crude exports ~**85% of prewar** | Sept avg | NYT/Kpler via Iran International 9/30 ([link](https://www.iranintl.com/en/202609308224)) | Volume, not a count |
| September volumes "at least **16.5 mbd**", ~two-thirds via STS | Sept | Kpler via Maritime Executive | Appears to be **total incl. bypass** (≈10 + 6). Do not set it against the 10 mb/d strait figure |
| 7-day average **14.3 mb/d**, "still about 4MM short" | n/a | @ericnuttall via digest | X, unverified |

**The order-of-magnitude disagreement persists** (PortWatch 1/day vs Windward 16–17/day), as in the 9/24 sweep. ⛔ **No LEVEL from any one source.** Ladder #6 (transit recovery): the volume data (Kpler/NYT ~85% of prewar Gulf exports) points to **recovery in BARRELS through dark/STS shuttling, not in counted transits.** That is a framing question for FALCON/BRENT, not a ladder fire WALTER can call.

---

## 8. Claim 7 — the oil price on 10/01

| Item | Finding |
|---|---|
| Wire | **CNBC, published 10/01 01:17 EDT, updated ~2h before 09:45 ET** ([link](https://www.cnbc.com/2026/10/01/oil-prices-today-wti-brent.html), fetched via curl): "Oil prices reversed earlier losses to jump more than 2% on Thursday, with Brent topping $100". "Brent crude … 1.8% higher at **$99.81**", WTI +0.5% to **$90.87** |
| Stated driver | "**Reuters reported that China's state oil major PetroChina canceled a handful of gasoline and jet fuel shipments that were planned for October, citing multiple unnamed sources** … CNBC could not independently verify". Energy Intelligence 10/01 headline: "**China Halts Refined Products Exports**" |
| Offsetting | The Yanbu loadings resumption had "eased" crude supply worries (UOB; Trade Nation's Morrison). Rubio/delegation story cited as background risk |
| **Not cited** | **No mention of Abqaiq, Ghawar, Bu Hasa or the 9/29 tankers.** So any read that "the market priced the Abqaiq fire" has **no wire support** |
| Cross-check | GlobalSecurity Day-216 (Trading Economics): Brent $100.22, +2.24% on 10/01. ⚠️ Same compendium quotes "Fox News $103.50 settlement 9/30". That is **not reconcilable** with Dec Brent ~$98 and is not carried |
| Roll caution (ADD#23) | **November Brent expired 9/30, so the front month is now December.** Any continuous-ticker (`BZ=F`/`LCO.1`) delta spanning 9/30→10/01 is a roll artifact. Use the **named contract (BZZ26)** only. Our vendor's BZZ26 $99.94 +1.9% is consistent with CNBC's $99.81 +1.8% |

---

## 9. Date traps rejected (event date outside 9/29–10/01)

| Item | Real event date | Why it surfaced |
|---|---|---|
| HormuzLetter "Abqaiq refinery has been struck by drones … East-West Pumping Station … NASA FIRMS confirms" (`2081737513983467753`) | **2026-07-27** (decoded) | Search hit for "Abqaiq fire". **The JULY-27 trap**: drones intercepted per the Saudi MoD (guard corpus) |
| Energy Intelligence "Strikes Target Saudi Oil and Gas Facilities" (Abqaiq smoke; "main facilities … escaped damage") | Published **7/28**, event **Mon 7/27** | "Monday" reads like 9/28 |
| Powergame.gr, ESA imagery of Abqaiq + Hawiyah flaring | **7/27** | Same |
| Türkiye Today, satellite smoke at Abqaiq | **2026-04-08** | Search hit |
| Saudi Gazette / Gulf News / Al Jazeera / Ahram: "drone attacks cause fire at two Aramco facilities" | **2019-09-14** | The 2019 Abqaiq/Khurais trap |
| Al Jazeera / CNBC / NPR, Jizan refinery fire | **2026-08-09** | |
| Kuwait condemns "Iranian attack on UAE oil tankers in Hormuz" (KUNA/WAM) | **2026-07-14** | Looks like a reaction to the 9/29 ADNOC hulls. **It is not** |
| Misbar fact-check (2026-09-28): video shared 9/24 as a "fire at Aramco Yanbu" | Video is from **August 2026** | Misleading recirculation |

---

## 10. WHAT CHANGED vs the anchor (`IRAN_WAR.md`, last full sweep 9/24)

| # | Change | Strength |
|---|---|---|
| 1 | **9/30 OSINT hypothesis (anchor L11) gets MORE specific but NOT confirmed.** The plume origin is measured ~45 km WEST of Abqaiq (North Ghawar / Ain Dar), not the Abqaiq plant. FIRMS coordinates are now published (25.8393N 49.2268E, secondhand). The candidate facility is a **production-class** asset (GOSP), which raises FAL-01 relevance *if* ever confirmed. Attack / damage / production: **nobody** | OSINT-only. No owner, no wire |
| 2 | **New theater (UAE onshore): Bu Hasa fire claim**, 9/30 ~17:45Z | Single OSINT account. INDETERMINATE |
| 3 | **Hormuz hits resume after the anchor's "UKMTO reports no attacks since 9/23" (L10):** AL FUNTAS 9/28 (fire, extinguished) + 3 tankers 9/29 (MERSIN PROSPERITY, SINBAD, AL RUWAIS) | UKMTO (via relays) + Reuters/Marisks names. **No sinking. Losses stay at 3** |
| 4 | **Diplomacy:** the US **response to the 7-day plan was delivered** (Doha, 9/29) and Iran confirmed receipt (9/30). The gap is **sequencing** (Reuters). This supersedes the anchor's 9/27 "nothing conveyed by mediators yet" | Iranian government on record + Reuters. US silent on record |
| 5 | **Rubio ordered the delegation out (9/28)**, reported by Axios 9/30–10/01 and **denied by Iran** | Anonymous US officials |
| 6 | **Trump 9/30: "We will blow 'em up or make a deal"** | POTUS channel: tape, not information |
| 7 | **Petroline export leg strengthened:** Aramco **notified customers of an October Yanbu loading schedule (9/28)**. Kpler throughput 2.65 mb/d. Yanbu loadings ~2 mb/d. Saudi 7-day loadings 8.5 mb/d (Kpler). **Still not operator-confirmed publicly; "struck/damaged" is still confirmed by nobody** | Reuters (one source for the notice) + vendor |
| 8 | Transit prints since 9/22: Windward 16 (9/28), 17 (9/29); PortWatch 1 (9/27); Kpler/NYT September ~10 mb/d through the strait | FLOORS, disagreeing |
| 9 | **Out of scope, flagged for the anchor:** the anchor's "9/23 bulk carrier ADRIFT, on fire" is **MV CAPE DAO**: **two torpedoes, one Indian seafarer killed**, ~2.5 nm off Musandam (The National 9/23–24 with Reuters image; Gulf News; gCaptain "Seafarer killed in Hormuz attack"). The anchor does not carry the **torpedo mechanism or the fatality**. Also: the Wikipedia ship list describes Kylo/Riesco as sinking "after US strike". Unverified here; FALCON owns that adjudication | Named outlets; not re-verified in depth |

---

## 11. NOT ESTABLISHED

- **That anything in Saudi Arabia was ATTACKED on 9/30.** No Saudi MoD, SPA, Aramco, CENTCOM or named-wire statement. No Houthi claim found. IRNA's anonymous sources are not a primary.
- **Which facility is burning:** Abqaiq plant vs a pumping station vs a North Ghawar / Ain Dar GOSP. Nor whether it is **production or transport**.
- **Any DAMAGE or PRODUCTION/FLOW impact** at the 9/30 Saudi site, or at Bu Hasa.
- **Bu Hasa: cause, attacker, and whether it is more than a flare** (FRP and VIIRS saturation do not distinguish them).
- **That OilPrice saw "routine flaring"** (the dissent is itself second-hand; no OilPrice article found).
- **UKMTO positions, corridor and attacker** for the 9/28–29 strikes. **AL RUWAIS's true type and flag** (LNG/Bahamas vs products/Liberia). **MERSIN PROSPERITY's flag** (Liberia vs Vanuatu).
- **The content of the US response** to the 7-day plan, and **any on-record US confirmation** that it was sent.
- **That Iran was "expelled"**: reported by anonymous US officials and denied by Iran's UN mission. No State Dept on-record statement.
- **A Hormuz transit LEVEL.** Vendors disagree ~17×.
- **Aramco/MoE public confirmation** of the Yanbu restart. The customer notice is one source.
- ⛔ **Not carried (guard kills):** "5 to 7% of global oil supply" (Abqaiq capacity share, KILL ①) · "7 mb/d" as anything but nameplate capacity · "Houthis struck the Abqaiq plant" · "ceasefire counterproposal" (ADD#20) · "UAE's only bypass now burning" as an impact claim · Polymarket odds as pipeline evidence · "Fox $103.50 settlement" · "UAE-owned/managed" for all three hulls.
