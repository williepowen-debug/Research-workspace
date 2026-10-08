# Iran-theater FULL verify sweep — 2026-10-08

**Executor:** read-only verify-research subagent for WALTER · **Written:** 2026-10-08T12:20Z (stamp from `date -u` in the writing command) · **Window:** event dates 2026-10-01 → 2026-10-08, with emphasis on overnight 10/07 → 10/08. **Scope:** claims A–H (weekly full sweep due 10/08) + coordinator addendum I1–I8 (Will's X-bookmarks).
**Method:** owner records first (FALCON STATUS 10/07 22:31 ET, FALCON report `reports/2026-10-07_gate001-review-and-inbox-drain.md`, KB-FALCON-255; BRENT STATUS 10/07), then primaries (UKMTO, CENTCOM, SPA/MoE/Aramco, MMA/BSEE, IEA, IRNA/Fars), then named wires (Reuters, AP, AFP, Bloomberg), then OSINT. Every item is keyed to its EVENT date. Date-trap rejects are in §8. I do **not** re-grade FALCON's or BRENT's marks.
**Guard corpus:** `IRAN_WAR_GUARDS.md` read whole (428 lines). **27 blocks**, the count in the anchor's inventory heading. **Guards applied:** KILL-ON-SIGHT ① (capacity read as loss: the minister's "5.8 million barrels" vs 7 mb/d nameplate) and ③ (declaratory control: Naqdi's "illegal routes") · flagged source UANI (I2) · 'VESSEL SUNK' theater-check plus ADD#13 "which sea" (158-26 is off Qatar; 151-26 is in the Red Sea) · maritime clock collision (UKMTO times are UTC) · mediated ≠ bilateral, and "do not score a two-track contradiction as one side lying" (Iran "replied" vs mediators "still waiting") · POTUS channel = tape (Trump 10/6–10/7) · search-summary contamination (one summary merged ON PEACE into 158-26; OilPrice garbled the Reuters window and attribution) · METHOD NOTE (I4 was searched as a possible real event; it was not dismissed on the guard alone) · intercepted→struck (KKIA 10/8) · 7/25 2019 Abqaiq/Khurais trap (the Aramco CEO's 2019 reminiscence) · Petroline 2019/April traps · ⭐ HORMUZ DENOMINATOR (88 canonical vs Reuters' "~125 a day"; counts are FLOORS) · ROUTING-GUARDS FOLD ("energy facilities" in a target list is not a FAL-01 event) · ADD#14 Mecca pact naming · ADD#15 FIRMS is not confirmation · ADD#19 anti-theater-merge (Forties/Apache = North Sea; Isaias = Gulf of Mexico) · ADD#20 "ceasefire" (CNN 10/7 "US-Iran ceasefire unravelled", not carried) · ADD#22 Kharg date anchors · ADD#23 named contracts only · ADD#24 (a wire's geography is not a fix; SHUT ≠ HIT; capacity ≠ loss) · ADD#25 force majeure · ADD#26 five discriminators per UKMTO item · ADD#27 checked, not triggered (no in-port hull).

## 0. Unreachable primaries (stated up front)

| Source | Result |
|---|---|
| ukmto.org: home, `/recent-incidents`, indexed PDFs `20261005-ukmto_warning_154-26.pdf`, `20261006-ukmto_warning_157-26.pdf`, plus guessed `…158-26` and `…159-26` | **403** on curl (browser UA) and on WebFetch. Bright Data was **not** used: WQ-383 budget is PROME's call, and WALTER's 10/04 run showed the public feed renders a "0 reports" shell. **Every UKMTO fact below comes from relays.** Post times for 149/151/156-26 are decoded from UKMTO's X post IDs (accurate to the millisecond) |
| centcom.mil press releases | **403**. Absence of a strike on Iran is search-based (tracker plus wires), not a read of CENTCOM |
| iea.org/news | **403**. The 10/07 IEA statement comes via The National and CNN |
| axios.com | **403**. Axios content comes via Deccan Chronicle (fullest relay), Investing.com, Arab News and Daily Beirut |
| cnn.com | WebFetch **451**; curl 200 (read in full) |
| investing.com (Reuters copy) | curl 403; WebFetch OK. This is the Reuters 1041 GMT story |
| seatrade-maritime.com | 403 (snippet only) |
| x.com (Kemp; UKMTO posts) | 402. Times decoded from post IDs |
| FT (Aramco CEO) | Not retrieved. **The Aramco primary was used instead** (aramco.com speech page, via WebFetch; curl failed with an HTTP/2 error) |
| SPA / MoE / Aramco newsroom / MoD | Searched, **no statement found** on Khurais (10/04), Rabigh/Jeddah (10/05–06) or KKIA (10/08). Absence of finding through search, not a read of each newsroom |
| Fars / IRNA | Not fetched directly. Naqdi's words come via TASS citing Fars, plus CBS |
| Platts / Argus Forties assessment | Paywalled, not read (I6) |
| NHC advisory | Not read. The track is covered by BOARD `SIG-W-20261008-001` |

## 1. Per-claim verdicts

| # | Claim | Verdict | One-line basis (source, event date) |
|---|---|---|---|
| A | Overnight oil jump on "record tanker attacks" | **CONFIRMED (move) / CORRECTED-FRAMING ("record")** | Reuters (Dareen, London 10/08): Dec Brent futures **$105.20, +$5 / +4.99%, at 1041 GMT**, highest since 9/29; WTI $92.75. Own `fetch.py` **BZZ26.NYM $104.76, +4.55%, at 12:14Z**. "Record" = **Kpler: 10 tankers struck in the strait 9/28–10/04, against a prior weekly high of 6** (CNN 10/08). Other instruments, other windows: **Reuters (three unnamed maritime security sources): ≥12 attacks on oil/LNG/LPG tankers 9/28–10/05**; **IMO: 9 incidents** the same week; **UKMTO: "nine attacks this month"** (as of Tue 10/06). The wires name **three** drivers: tanker attacks, **Hurricane Isaias**, and the **Axios** report. **No new hull incident 10/07 ~1900Z → 10/08 ~12Z found**; the latest is 158-26 (§2) |
| B | "Just seven tankers transited Hormuz Tuesday, less than half the 7-day average" | **CONFIRMED (Kpler) / CORRECTED-FRAMING** | Kpler counted **7 commodity vessels** (not tankers only) on **Tue 10/06**, the lowest since **7/23** on its own series; **10 on Wed 10/07**; **>20 on Sun/Mon 10/04–05** (Reuters 10/07). LSEG: **8** on Tue (5 oil tankers + LNG carrier AL-MAFYAR), **14** Mon. **Kpler excludes AIS-dark ships ⇒ a FLOOR, never a level.** On the canonical denominator, 7/88 ≈ 8% (floor). ⛔ Reuters' "~125 large vessels a day prewar" is a different denominator; do not blend it with 88 |
| C | Axios: US preparing to "resume major combat operations" | **CONFIRMED AS A REPORT (anonymous officials) — PREPARATION, NOT EXECUTION** | Axios (Barak Ravid, also for N12), published **late Wed 10/07 ET**: the Pentagon told CENTCOM **"several days ago" to conclude preparations** for resuming major combat operations; **no date set; Trump has made no final decision**. Sources: US officials; US and Israeli officials on timing. Second Israeli official: chances before the midterms are "**not high**"; after them they "increase significantly". Unnamed Pentagon official: "The Department's job is to develop and present military options". Unnamed WH official: "all options available … the easy way or the hard way". Corroborating, also anonymous: NBC 10/07 (one US official + one person); The Atlantic 10/08 (WH asked the Pentagon to "prepare strike options" before the midterms). **No on-record denial.** Reuters "could not verify". **No strike on Iranian territory found 10/01–10/08** (§4) |
| D | Diplomacy since 10/01 | **UPDATED — NO FRAMEWORK** | **Sun 10/04, MFA spokesman Baghaei**: Iran conveyed an **initial** position through Qatar; "We are reviewing the details and will provide additional points on certain details to the U.S. side" (anewz 10/05). **Axios 10/07**: Qatari mediators are **still waiting** for Iran's response to the US counterproposal, which includes nuclear demands. This is two-track, not a contradiction (initial vs final). **Trump, San Antonio, 10/07**: "the deal isn't really something that I want to do" (POTUS tape). Iranian official 10/07: the blockade must lift **before** nuclear issues (CBS). **Oman channel: nothing found.** ⛔ Report.az's "effectively ruling out nuclear talks" is the outlet's gloss and is NOT carried |
| E | IEA agreed to accelerate stock releases (~10/07) | **CORRECTED-FRAMING** | **Wed 10/07**: members backed **accelerating the ~100 mb still undelivered from the March 400 mb action** (~325 mb released to date), **diesel first**. **No new volume** (CNN: members "would not add to the 400 million barrels"; ICE gasoil closed **+6%** on that). G7's 10/02 diesel-led 100 mb sits **inside** that ~100 mb (CNN). Members hold **~1.1 bn bbl**, incl. **>200 mb diesel**. Birol: "stands ready to release more … if and when required". Governing board meets next week. IEA primary 403 |
| F | US Gulf hurricane cutting offshore output | **CONFIRMED AT PRIMARY — NOT IRAN** | **Hurricane Isaias** (CNN misspells it "Isais"). **Marine Minerals Administration** (BSEE + BOEM, reunified 7/10/2026) release dated **Wed 10/07**, data as of **11:00 CDT**: **25.08% of Gulf oil and 16.37% of Gulf gas shut in**; 8 of 371 manned platforms evacuated (2.16%). The b/d figure (511,619) is from relays, not from the MMA text I read. Shell and Chevron curtailing (CNN). It feeds the **same** 10/08 price move |
| G | Saudi assets / FAL-01 | **GATE 1 FIRM-NEGATIVE HOLDS** | No counting source confirms a hostile hit on a production-class asset. Khurais (10/04) is unchanged (§5). The minister's 10/06 quotes carry **no daily unit** and a **restart-timing claim** that conflicts with the anchor (§5). The Aramco CEO (10/05) says Aramco is "restoring damaged infrastructure at pace" but **names no asset**. Rabigh (10/05) is still INDETERMINATE, and refining is OUT of class. I4 (Jeddah 10/06) is UNSUPPORTED |
| H | Re-verify ladder items | **NONE FIRED** | **Force majeure:** no declaration found (ADD#25). **Kharg seizure:** none found. **Mojtaba:** no verified October appearance (latest is an undated Mehr clip around 8/9). **Bab el-Mandeb closure order:** none; FALCON's event override was NOT TRIGGERED through 10/07. New context, not ladder fires: Naqdi's declaration (I1); B-1s pulled from Fairford (I3); Mecca pact **activated** 10/05; Houthi airport campaign (KKIA claim 10/08: intercepted "north of Riyadh" per the coalition) |
| I1 | "IRAN SAYS IT WILL SOON BLOCK 'ILLEGAL' ROUTES IN HORMUZ" | **CONFIRMED (statement) / CORRECTED-FRAMING** | Speaker: **Mohammad Reza Naqdi, adviser to the IRGC commander-in-chief**, via **Fars**, **Wed 10/07** (TASS; CBS 8:45 AM ET), hours after Rubio said Iran had "lost complete control". He is not the IRGC Navy and not the MFA. His definition: "Iranian forces will soon block several routes that violators created by blasting" rocky passages, used by small boats to move oil to tankers. **The Oman-coast-corridor reading is a reporter's inference, not his words.** This is a **declaration** (KILL ③: move on behavior). The nearest behavior datum is **UKMTO 152-26, 10/05 0827Z**: the IRGC hailed an inbound tanker ~11 nm N of Khasab, and it turned back |
| I2 | ZH 10/06 "50 Iranian tanker logjam … US naval blockade" | **CONFIRMED (blockade is executed policy) / CORRECTED-FRAMING** | The blockade is **not** ZH framing. The anchor history records it beginning **2026-04-13** (CENTCOM via Stars & Stripes; 91 ships redirected by 5/20), announced lifted **6/14**, and recorded "in full effect" **7/26–27**. A relay dates the reinstatement to "mid-July", unverified. It is current per Trump 10/06 ("Nobody's ever seen a blockade like that"), Bessent, and Iran's 10/07 demand that it be lifted. **Bloomberg 10/01 (preliminary; Kpler and Vortexa agree per relays): Iran loaded ZERO crude in September**, vs ~250 kb/d in August. ⚠️ The **"~50 tankers" count is UANI's** (Oct 5 snapshot, via Bloomberg), a **flagged advocacy source** with validation owed. ZH's "blockade **of the Strait of Hormuz**" names the wrong object: it is a blockade of Iranian ports and Iran-linked shipping, enforced in the Gulf of Oman |
| I3 | NYT 10/04: B-1s withdrawn from RAF Fairford; "10 of 12 left" | **CONFIRMED / CORRECTED ("10 of 12" → all)** | Withdrawal ~**Sun 10/04**. NYT (two anonymous US officials): **all 12 B-1s** withdrawn after warnings of an Iran-backed plot; ≥3 home by Sunday. An unnamed Department official told Fox/CNN (**10/04 20:32 EDT**): "all U.S. bombers that were deployed to RAF Fairford have re-deployed to their home stations". Trump **Mon 10/05**: "They would be linked to Iran". Rubio: "a foreign actor". **UK: no public Iran link.** Plot: 3 vehicles with fuel accelerants near the base ~9/27; 6 arrested, all bailed. **Attribution to Iran is US officials' claim, not established** |
| I4 | @DD_Geopolitics 10/06 22:05Z: "Ansarallah hits Aramco AGAIN, large fires in Jeddah" | **UNSUPPORTED (as a new 10/06 event)** | Searches keyed on Jeddah + Aramco + October found **no 10/06 Jeddah event**, no Saree claim naming Jeddah energy 10/06–10/08, and no Saudi confirmation. The Houthi claims in the window name **Riyadh/Khurais (10/03–04)**, **Rabigh (10/05)**, **Abha airport (10/06)** and **KKIA (10/07, 10/08)**. Most likely this is the **10/05 Rabigh claim**: Newsquawk 10/05 15:12Z labels Rabigh "in Jeddah", and that is BOARD `-015`. Date traps that surface: **North Jeddah Bulk Plant 2020-11-23 / 2021-03 / 2022-03-25** (§8). Rabigh is a refinery/petrochemical complex, OUT of FAL-01 |
| I5 | @live_ais_com 10/05: UKMTO "time-delayed reports", "14 security incidents in as many days", more 10/04 incidents | **CONFIRMED (late reports; the 10/04 incidents) / INDETERMINATE ("14")** | UKMTO's own phrase is "time-late report". **Three incidents on 10/04:** **151-26** at ~1650Z (**Red Sea**, near-miss), **153-26** at 1716Z (late, inbound LPG tanker), **154-26** at 1907Z (late, crude tanker, verified source). Seatrade (10/05): nine UKMTO reports in October through 10/05 (8 Hormuz, 1 Bab). **The "14 in 14 days" figure has no stated basis** (warnings, advisories, or strikes?). From ~9/21 to 10/05 the UKMTO numbering runs ~141→157, so it is plausible but unverifiable. Merged into §2 |
| I6 | ZH/Kemp 10/06: Forties spot "over $140/bbl, highest since the war began" | **CONFIRMED AS KEMP'S REPORT (single source) / CORRECTED-FRAMING** | Kemp's X post at **10/05 14:20Z** (decoded) extracts his newsletter: physical prices are "the highest since the **opening weeks** of the war". **His own record is Forties $147 on 4/09** (LSEG lifetime high $148.87 around 4/13), so "highest since the war began" is false. **Basis:** physical spot (a Platts/Argus assessment, not read) vs futures. Dec Brent futures were ~$100–101 on 10/05–07 (BRENT capture 10/07 16:15 ET: $101.04). **Local driver:** Unite's Apache strike mandate (ballot closed 10/01) threatens the Forties pipeline system (North Sea, ADD#19) |
| I7 | FT 10/05: Aramco CEO "scarily thin", "<6bn barrels … not practically available", two years to rebuild | **CONFIRMED AT ARAMCO PRIMARY** | Amin Nasser, **Energy Intelligence Forum, London, Mon 10/05** (aramco.com speech page): "the supply resilience cushion is scarily thin"; "less than 6 billion barrels of commercial inventories remain today, with the vast majority not practically available"; "replenishing inventories while meeting demand could take up to two years"; ~10 bn bbl at the start, "nearly 3 billion barrels of gross oil supply" lost, ">1 billion barrels" drawn; "Emergency reserves might buy us a winter". The FT text itself was not read. CBS carried it at 10/07 1:33 PM, a relay. ⚠️ The same speech says "our facilities at Abqaiq and Khurais had been attacked". **That is 2019** ("I will never forget 2019…"), the 2019 trap. **Do not clip it as a 2026 admission** |
| I8 | Bloomberg 10/06 "Iran ramps up ship attacks as oil and gas flows climb" vs CNN "seven tankers Tuesday" | **CONFIRMED — BOTH TRUE, DIFFERENT INSTRUMENTS AND DAYS** | Bloomberg 10/06: UKMTO counts **9 attacks in October so far** (≈ half of September's Hormuz + Gulf total). On flows, Bloomberg's Livingstone-Wallace says "pretty close now to prewar level", a qualitative barrel read. **Kpler (Reuters 10/07):** crude crossing the strait **fell 27% w/w to ≥10.1 mb/d (74% of prewar)**, mainly fewer STS transfers in the Gulf of Oman. Exports from the Gulf of Oman coast + Red Sea were **6.7 mb/d** (>2× prewar), so total Middle East crude exports ≈ prewar. **Kpler (CNBC 10/08):** Gulf ex-Iran + Saudi/UAE ~**18.5 mb/d ≈ prewar**. The Tuesday count is a **one-day vessel-count dip** after >20/day on 10/04–05. Bloomberg's piece predates it. Relay-only and unverified: Kpler 10.3 mb/d (week to 10/03, vs 13.5 prewar); Windward 9–10 mb/d (vs 14.5 prewar). ⛔ **Three different "prewar" bases (13.5 / 14.5 / ~16 mb/d); never blend them** |

---

## 2. Hull incidents 10/01 → 10/08, by UKMTO number (ADD#26: event date · vessel · direction · mechanism · position)

Owner record: FALCON KB-FALCON-255 / VI-0042..0055 (10/07). My relay checks are added. **UKMTO text was unread at the primary for every row (403).**

| UKMTO | EVENT (UTC) | Vessel | Dir. | Mechanism / damage | Position (per UKMTO relay) | Sea / GATE-2 note | Source of row |
|---|---|---|---|---|---|---|---|
| 147-26 | 10/01 1750Z | KAZIMAH III (Kuwaiti VLCC, KOTC), per trade press | — | struck; fire; crew evacuated; afloat, no CTL found | Hormuz | Hormuz; not a sinking | anchor 10/02 limb; FALCON VI-0042 |
| 148-26 | 10/02 1122Z (master) | unnamed tanker | outbound | unknown projectile; small fire + blackout; extinguished; underway; no casualties | inside the Strait | Hormuz | Regulas 10/03 (fetched) |
| 149-26 | 10/02 2142Z (UKMTO X post 10/02 23:15Z) | unnamed crude tanker | n/s | unknown projectile, port side; crew safe | ~4 nm E of Oman | Hormuz / Musandam | Regulas 10/03; X ID decoded |
| 150-26 | TBC (issued 10/04) | **INFERRED LIPSI** (FALCON) | n/s | engine room; no fire stated | area just N of the Musandam tip | Hormuz | FALCON 10/04 report. ⚠️ see conflict below |
| 151-26 | 10/04 ~1650Z (X post 18:54Z) | CHRYSTAL SKY (Marshall Is.; UAE-linked), per Vanguard | → Barcelona | **near-miss** airburst ~100 m; no damage | ~60 nm S of Al Mukha | **RED SEA / Bab el-Mandeb: not Hormuz, GATE-2 ineligible** | FALCON 10/07 |
| 152-26 | 10/05 0827Z (ADVISORY) | unnamed | inbound | **IRGC hail: "turn back or face being targeted"**; complied; **not a strike** | ~11 nm N of Khasab | Hormuz; first IRGC-attributed act since 9/28 | FALCON; Shafaq 10/05 |
| 153-26 | 10/04 1716Z (time-late) | unnamed LPG tanker | inbound | struck | Hormuz | Hormuz | **one blog numbers it** (Regulas). Weak |
| 154-26 | 10/04 1907Z (time-late) | unnamed crude tanker | n/s | "struck by unknown projectiles" (verified source) | Strait of Hormuz | Hormuz | UKMTO PDF indexed `20261005-…154-26` (text via search relay); Seatrade |
| 155-26 | 10/03 TBC (time-late) | unnamed crude tanker | n/s | struck above the waterline | Hormuz | **possible duplicate** of an earlier 10/03 report | FALCON |
| 156-26 | 10/05 1637Z (X post 18:07Z) | **LIPSI (Liberia, Dynacom), per Shafaq's "maritime security sources"** | n/s | unknown projectile; **engine-room fire**, crew fighting it; no casualties at the time | Strait of Hormuz | Hormuz | Shafaq 10/05 20:53Z (fetched); X ID decoded |
| 157-26 | 10/05 time TBC (issued 10/06) | unnamed oil tanker | **outbound** | unknown projectile; damage n/s | Strait of Hormuz | Hormuz | UKMTO PDF indexed `20261006-…157-26`; Iran International 10/06 13:23 BST |
| 158-26 | **10/07 ~1900Z** | unnamed tanker; flag/cargo unreleased | n/s | **"multiple projectiles"; crew casualties reported, count unknown**; no claim; Qatar no comment | **~51 nm (94 km) N of Madinat ash Shamal, Qatar** (Qatar EEZ) | **CENTRAL/WESTERN GULF, not the Strait.** First tanker attack in the western Gulf "in weeks" (Maritime Executive via AFP) | Al Jazeera/AFP-DPA 10/08; ANI; DeepDraft 10/08 |
| (unnumbered) | 10/05 or 10/06 | **ON PEACE** (Panama LR2, IMO 9893204; 19 crew, 17 Indian) | n/s | unknown projectile; **12 injured** (11 Indian), evacuated to Khasab | ~9 nm NE of Limah (FALCON), "transiting Hormuz" (India MEA, Tue 10/06) | Hormuz | India MEA via relays; **may be 156 or 157** |
| (unnumbered) | ~10/05 | MARAN GAS MYSTRAS (Greek LNG carrier) | outbound | near-waterline hit; sailed on | Hormuz | Hormuz | FALCON only; not re-verified here |
| 159-26 | — | — | — | **none found** to ~12:15Z 10/08 (DeepDraft 10/08: "none reported" for 10/08; FALCON's helper found none to 02:20Z) | — | — | — |

**Established:** ~10 strike reports (numbered + named) 10/01–10/07, one IRGC turn-back, and one Red Sea near-miss. **NO SINKING, NO MINE DETONATION ⇒ losses stay 3; GATE 2 untouched.** ⚠️ **Conflicts FALCON must resolve, not me:**
- **(a) LIPSI.** Shafaq ties LIPSI to **156-26** (10/05, engine-room fire). FALCON's VI-0045 infers LIPSI = **150-26** (issued 10/04, engine room, no fire). Both rows say "engine room". Either one hull was reported twice, or the identification is wrong on one. **Do not transfer the name across events.**
- **(b) ON PEACE vs 158-26.** A search-summary layer merged ON PEACE (Hormuz, 12 injured, MEA 10/06) into 158-26 (off Qatar, 10/07). These are **different events**: different day, position ~300+ km apart, different casualty report. ⛔ Do not merge (ADD#26, search-summary contamination).
- **(c) 156-26 casualties.** The initial advisory said no casualties; if ON PEACE = 156-26, the MEA's 12 injured supersede that.

**Weekly counts are different instruments over different windows; none is a level and none should be averaged:** Kpler 10 tankers struck (9/28–10/04) · Reuters' three sources ≥12 (9/28–10/05) · IMO 9 (same week; IMO verifies slowly) · UKMTO 9 "this month" (as of 10/06) · FALCON ledger 13–16 struck hulls (9/28–10/07). ⛔ OilPrice's "a dozen attacks between September 28 and October 2 … U.S. Navy-led outlet" is a **re-derivation error**. Reuters' window is to **10/05**, and the count is from three maritime security sources, not JMIC. JMIC's Sunday (10/04) note is about IRGC harassment (overflights, surveillance, VHF hailing): "These actions continue to demonstrate Iran's intent to assert presence along key transit lanes."

---

## 3. Claim A detail — the 10/08 oil move

| Item | Finding | Source |
|---|---|---|
| Reuters level | Dec Brent futures **$105.20, +$5.00 (+4.99%) at 1041 GMT**, highest since 9/29. WTI **$92.75, +$4.47 (+5.06%)**, highest since 10/02 | Reuters (Seher Dareen), London 10/08, via Investing.com 06:51 |
| CNN level | Brent **$105.46**, ">5%", "shortly after 7 a.m. ET". WTI **$92.82** | CNN Business, published 10/08 10:34Z, updated 11:26Z (curl, read whole) |
| OilPrice | Brent $105.02 (+4.81%) at 5:46 CDT | OilPrice (Slav) 10/08 |
| Own named contract (ADD#23) | **BZZ26.NYM $104.76, +4.55%, at 12:14:54Z**. CLX26.NYM $92.29, +4.54%. ⚠️ `contract_identity` printed UNKNOWN for BZZ26 (name-cut inference); the symbol is Dec-26 | `FORGE/tools/market-data/fetch.py` |
| Stated drivers | (1) tanker attacks: Kpler's record week, MST Marquee's Kavonic ("frequency … highest since the war began"). (2) **Hurricane Isaias**: Shell/Chevron curtailing; 25.08% of Gulf oil shut in. (3) Reuters adds the **Axios** report. The prior session (10/07) closed **lower** after the IEA acceleration (Reuters) | Reuters; CNN |
| Not the cause | No new hull incident overnight 10/07 → 10/08 found. 158-26 (10/07 ~1900Z) was the latest | §2 |

⇒ **Do not assign the 10/08 move to the tanker attacks alone.** Three drivers are named, and no wire weights them.

## 4. Claim C detail — US posture vs execution

| State | Status | Basis |
|---|---|---|
| **PREPARATION ordered** | Reported (anonymous) | Axios 10/07: CENTCOM told "several days ago" to conclude preparations; no date. NBC 10/07: the national security team discussed resuming large-scale operations "in the coming weeks". The Atlantic 10/08: WH asked for strike options before the midterms |
| **DECISION** | **NOT made** | Axios: "Trump has not made a final decision" |
| **TIMING** | Contested **within the same report** | "could take place before the US midterm elections (Nov 3)" vs the second Israeli official: chances before the elections are "not high … after the midterms … increase significantly" |
| **TARGETS (if resumed)** | "energy facilities, infrastructure and nuclear targets" (Axios, citing sources) | ⚠️ A target LIST is not an event. "Energy" on Iranian soil is **not** FAL-01 (Gulf-ally production) and is not a grid fire until executed (ROUTING-GUARDS FOLD) |
| **EXECUTED strike on Iranian territory, 10/01–10/08** | **NONE FOUND** | GlobalSecurity tracker through 10/05: "28th consecutive operational period" with no strike ashore. CBS 10/08: the US "hasn't announced strikes on Iran for weeks". FALCON: none since 9/08. The latest CENTCOM IRGC-target wave in results is ~9/01. **Search-based; CENTCOM 403** |
| Counter-signal | B-1s pulled from Fairford ~10/04 (I3). The Pentagon says the fleet can strike from CONUS | Fox 10/04; CBS 10/08 |
| Iran | Araghchi (~10/04–05): enemies choosing "military confrontation … will face a stronger response". Iranian army (10/07, CBS): may launch **preemptive** strikes on US positions (threat datum) | anewz; CBS |
| POTUS tape | 10/06 Sparrows Point: "If it doesn't have oil, we just sink the ship"; "the Hormuz Strait belongs to the United States Navy". 10/07: "the deal isn't really something that I want to do"; "It will be over very quickly" | Deccan Chronicle / CNBC relays. **Tape, not information** |

## 5. Claims G / D detail — Saudi assets and diplomacy

**Petroline / East-West line (event 10/06, Manama; Reuters / Al Jazeera 10/06):** Minister Abdulaziz bin Salman: "as of this morning we're back up to **5.8 million barrels**". **The quote carries no daily unit**; "a day / bpd" is the outlet's addition. Second quote: "**within five or six days, we began using the pipeline again after the major attack**". ⚠️ **This conflicts with the anchor's restart date of 9/22, which rests on unnamed sources.** Five or six days from 9/11 is ~9/16–17. That bears on the shut-duration record; FAL-05 already resolved FAILED 9/28 on **route (c), Yanbu loadings ≥72h**, and is FALCON's to adjudicate. ⛔ KILL ①: 5.8 is next to a **7 mb/d nameplate**; never write "7 mb/d" as a flow or a loss. **Yanbu loadings w/c 9/28 and 10/05: no vendor weekly print found** (agrees with FALCON's gap).

**Khurais (10/03–10/07):** unchanged from FALCON 10/07. AFP 10/05 (one unnamed source): a pump station was hit and the line "stopped again". Bloomberg and Reuters 10/05: flows uninterrupted. FALCON's own FIRMS shows heat 10/03–10/07, peak 504.6 MW on 10/06 (**heat never counts**, ADD#15). **No Aramco/MoE/SPA statement.** INDETERMINATE.

**Aramco CEO 10/05 (primary):** "restoring damaged infrastructure at pace". Attacks on land "including Aramco facilities" amplified the shock. **No asset is named and no volume is lost or quantified**, so this is **not** a counting confirmation of a production-class hit. Not new in kind: Aramco acknowledged minor Abqaiq damage on its 8/04 call.

**Riyadh refinery (10/03):** an AFP reporter saw crews fighting a blaze at the refinery south of Riyadh. Saree claimed it; the coalition called it "misleading". Refinery = OUT (FALCON KB-242).

**Rabigh (10/05):** BOARD `-015` stands. INDETERMINATE; refining is OUT.

**Houthi airport campaign:** Abha, **Tue 10/06**: 2 killed, 28 wounded (GACA). **KKIA, Wed 10/07**: 1 killed (Sudanese), 8 wounded (Saudi authorities, via CNN). **KKIA, Thu 10/08**: Houthi ballistic-missile CLAIM; the coalition (al-Maliki) says it **intercepted a missile "north of Riyadh"** and destroyed a launcher in Sana'a; repeated blasts were heard; diplomats were told to shelter in place (AFP). **Intercepted ≠ struck**; no damage confirmed. **No energy site is named 10/06–10/08.**

**Diplomacy:** Iran conveyed an **initial** response via Qatar (Baghaei, Sun 10/04: "reviewing the details … will provide additional points"; Gharibabadi: the final position will come "through the appropriate channels", Iran "simultaneously prepared for other scenarios"). Axios 10/07: mediators are **still waiting** for the Iranian response; talks have made "no progress". Vance 10/07: Iran must "do something meaningful on their enrichment capacity". Iranian official 10/07: lift the blockade before the nuclear file. Qatar's Emir passed proposals to Iran's Interior Minister Momeni ~10/05–06 (**Sputnik only**; single source). Putin to meet Pezeshkian Fri 10/09 in Turkmenistan (CBS). **No dated framework, no Oman development, no US accept/reject** ⇒ ladder #5 NOT fired. **MEDIATED ≠ BILATERAL** (Qatar).

**Regional:** Saudi Arabia, Turkey and Pakistan **activated** their defense pact at an emergency Riyadh meeting on Mon 10/05 (joint statement). Pakistan's ISPR chief confirmed troops in-kingdom on 10/07 (CNN exclusive). ⚠️ ADD#14 naming: the formal instrument is the **Mecca Joint Deterrence Agreement** (signed 8/07). Outlets now write "Mecca Joint Defense Agreement" or "Mecca Alliance". It is the same instrument; do not merge it with the 2025 Saudi–Pakistan bilateral or the 14-nation maritime coalition.

---

## 6. STATE CHANGES vs the anchor's 10/01 lead

| # | Item | 10/01 anchor | Now (event date · primary/basis) |
|---|---|---|---|
| 1 | **Losses** | 3 | **3, unchanged.** No sinking, no mine 10/01–10/08 (UKMTO relays; FALCON VX 10/07) |
| 2 | **Hull war** | Hits resumed 9/28–29 (4 hulls) | **Escalated in rate and in geography.** UKMTO 147–158 (10/01–10/07): ~10 strike reports + ON PEACE / MYSTRAS. **158-26 on 10/07 ~1900Z, ~51 nm N of Qatar: the first post-9/28 tanker attack in the central/western Gulf, with casualties.** Record week on Kpler's series (10 tankers, 9/28–10/04) and on Reuters' three sources (≥12, 9/28–10/05) |
| 3 | **GATE 1 / FAL-01** | FIRM-NEGATIVE | **FIRM-NEGATIVE, holds.** No counting source for a production-class hit. Khurais contested; Rabigh and the Riyadh refinery OUT; Jeddah 10/06 unsupported |
| 4 | **GATE 2** | Untouched (fired 9/5) | **Untouched.** ⚠️ 158-26 is a Gulf (not Strait) event; FALCON rules eligibility if it ever becomes a loss |
| 5 | **Diplomacy** | US response handed over 9/29; receipt confirmed 9/30 | **Iran conveyed an INITIAL position via Qatar on 10/04 (Baghaei); mediators await the final (Axios 10/07). No framework.** POTUS 10/07: deal "isn't really something that I want" (tape) |
| 6 | **Transit floor** | Windward 16–17 (9/28–29) vs PortWatch 1 (9/27) | **Kpler 7 commodity vessels Tue 10/06 (lowest since 7/23), 10 Wed 10/07, >20 Sun–Mon 10/04–05. LSEG 8 / 14. PortWatch 4 (10/04, FALCON script).** All FLOORS. Barrels: Kpler ≥10.1 mb/d through the strait (−27% w/w; 74% of prewar), while all-route Middle East exports ≈ prewar |
| 7 | **US posture** | No strike on Iranian territory | **Still no executed strike (10/01–10/08, search-based).** New: CENTCOM told to **conclude preparations** for major combat operations (Axios 10/07, anonymous; no date, no decision) + NBC + The Atlantic. B-1s withdrawn from Fairford ~10/04 |
| 8 | **Iran declaratory** | — | IRGC adviser Naqdi, 10/07 (Fars): will "soon block" smuggling "routes". Declaration only. Behavior: 152-26 IRGC turn-back, 10/05 |
| 9 | **Petroline** | Restart reported 9/22 (unnamed) | Minister, **10/06**: "back up to 5.8 million barrels" (no unit) and "within five or six days" of the attack (**conflicts with 9/22**) |
| 10 | **Saudi–Houthi** | Khurais claim 10/04, disputed | Airport campaign: Abha 10/06 and KKIA 10/07, **3 killed, 36 wounded** (GACA). KKIA claim 10/08, intercepted per the coalition. Mecca pact **activated** 10/05 |
| 11 | **Supply policy** | — | IEA 10/07: **accelerate** the remaining ~100 mb, diesel first, **no new volume**. Isaias: **25.08%** of Gulf oil shut in (MMA, 10/07 11:00 CDT) |

## 7. What each owner needs to adjudicate

**FALCON** (theater, marks, ladder):
- **158-26** (10/07 ~1900Z, off Qatar, casualties): hull identity, casualty count (CAS-023), Gulf-vs-Strait eligibility, and whether it re-prices Gulf war-risk (its WARRISK note already flags this).
- **LIPSI**: is it 150-26 (VI-0045, inferred) or 156-26 (Shafaq 10/05)? Also map **ON PEACE** to 156 or 157, and never to 158.
- **Weekly-count reconciliation**: Kpler 10 · Reuters ≥12 · IMO 9 · UKMTO 9-in-October vs its own 13–16 ledger. Name each instrument; do not average.
- **US-Iran direct-kinetic vector**: preparation reporting (Axios/NBC/The Atlantic) plus the Fairford withdrawal, with no executed strike. Does any registered rung read "preparation"?
- **Ladder #5**: the 10/04 "initial position" vs the 10/07 "still waiting" (two-track, mediated).
- **Naqdi declaration (I1)**: a perimeter question only (smuggling channels vs the Oman-coast corridor). 152-26 is the behavior datum.
- **Petroline shut-duration**: the minister's "five or six days" vs the 9/22 report. This is a record question; FAL-05 is already resolved on route (c).
- **Aramco CEO's "damaged infrastructure"**: no asset named, so it is not a production-rung counting source. Confirm.
- **I4**: no distinct 10/06 Jeddah event. Treat it as Rabigh (`-015`) recirculation.

**BRENT** (oil, prices, flows):
- **10/08 move attribution**: three drivers (attacks + Isaias + Axios), unweighted. Named contract only: BZZ26 $104.76 +4.55% at 12:14Z (own fetch); Reuters $105.20 at 1041 GMT.
- **Isaias**: MMA 25.08% oil / 16.37% gas shut in, as of 10/07 11:00 CDT; restart path. No Gulf Coast refinery shutdown found (a gap, not a clear).
- **IEA 10/07**: acceleration of the ~100 mb remainder, diesel first, no new volume. Gasoil +6% on "no addition" (CNN). The governing board meets next week.
- **Forties >$140** (Kemp 10/05, single source): physical vs futures basis (~$40 gap to Dec futures ~$100–101); Apache/Unite strike risk on the Forties system. "Highest since the war began" is false against Kemp's own $147 on 4/09.
- **Aramco CEO inventory figures** (10/05 primary): <6 bn bbl commercial, mostly "not practically available"; ~3 bn bbl gross supply lost; >1 bn bbl drawn; up to two years to rebuild.
- **Flows**: Kpler ≥10.1 mb/d through the strait (−27% w/w, 74% of prewar); 6.7 mb/d via the Gulf of Oman coast + Red Sea; ~18.5 mb/d combined ≈ prewar (CNBC/Kpler). Relay-only: Kpler 10.3 vs 13.5 prewar; Windward 9–10 vs 14.5 prewar. **Three prewar bases; do not blend them.** Transit denominator: Reuters' "~125/day" ≠ the canonical 88.
- **Iran blockade**: zero Iranian crude loadings in September (Bloomberg prelim; Kpler/Vortexa per relays); Kpler ~10 mb outside the blockade zone (vs 100 mb in July); ~70 mb onshore. The UANI "~50 tankers" count is flagged and unvalidated.
- **Petroline "5.8"** has no unit in the minister's words (the 10/06 record already carries this).

## 8. Date traps rejected (event date outside 10/01–10/08)

| Item | Real event date | Why it surfaced |
|---|---|---|
| Diari de Tarragona: "three incidents off Oman — IRGC fast boats opened fire on a tanker; container ship hit by a projectile" | **2026-04-18** | Ranked against "14 security incidents UKMTO October". Shape matches 152-26/156-26 |
| Argaam: "Forties spot nears record $150" / $148.87 lifetime high | **2026-04-13** (LSEG) | Forties >$140 query (I6) |
| Kemp: "Forties closed at a record $147 on April 9" | **2026-04-09** | Same. It refutes ZH's "highest since the war began" |
| Aramco CEO speech: "our facilities at Abqaiq and Khurais had been attacked" | **2019-09-14** (reminiscence inside a 10/05/2026 speech) | 2019 Abqaiq/Khurais trap, inside a genuine 2026 primary |
| North Jeddah Bulk Plant Houthi fires | **2020-11-23 · 2021-03 · 2022-03-25** | Jeddah + Aramco + fire query (I4) |
| Al Jazeera: "Saudi Arabia says key oil pipeline back to full capacity after attacks" | **2026-04-12** (April Petroline cycle) | Petroline restart query. Not the 10/06 statement |
| Reuters "oil jumps" results: Brent $114.44 (+5.8%) · $79.11 (+4%) · $97.47 | **2026-05-04 · 07-13 · 09-07** | "Oil jumps … Hormuz" query |
| WBUR/NPR: "Strait of Hormuz erupts as oil tops $100"; "US sank five Iranian oil tankers" | **2026-09-09** | Same |
| Gulf News: "Oil tops $100 as Iran attacks offset IEA stockpile release" | Undated in results; the March–April release cycle | IEA query. Not carried |
| Barchart: "IEA approves record 400 million barrel release" | **March 2026** (the base action) | IEA query. The 10/07 decision accelerates its remainder |
| The National: "Iranian tankers laden with oil have broken US blockade" | **2026-04-22** | Blockade query (I2). The first, porous blockade cycle |
| Kharg: "every military target obliterated"; explosions near Kharg | **2026-03-13 · 04-07 · early Sept**; AI video **8/30** (ADD#22) | Kharg seizure query. No October event |
| Mojtaba "first public appearance" / Mehr video | **~2026-08-09** (undated clip) | Mojtaba query. Not an October appearance |
| Aramco cuts European October term allocations to zero | **2026-09-18** | Force-majeure query. Operational, not a declaration (ADD#25) |
| UKMTO "unknown projectile" items (Al Jazeera 8/18; Oman "first tanker attacked" 3/01) | **2026-08-18 · 03-01** | UKMTO October query (ADD#26) |

## 9. NOT ESTABLISHED

- **Any UKMTO warning text at the primary** (403). The 153-26 number rests on one blog. The 155-26 duplicate question is open. 158-26's hull, flag and casualty count are unknown. There is no 159-26.
- **Which hull is LIPSI** (150-26 vs 156-26), and which numbered warning **ON PEACE** is.
- **Attacker attribution** for any 10/01–10/07 strike. Fars' 10/03 "targeted seven" names no hulls. The 152-26 hail is the only IRGC-attributed act.
- **That the US has decided, dated, or executed** a resumption of combat. The reporting is anonymous and is about preparation.
- **Iran's final response** to the US counterproposal, and any dated framework.
- **A production-class (FAL-01) hit anywhere**: Khurais facility class, Rabigh cause and damage, the KKIA 10/08 outcome.
- **The Petroline restart date** (minister ~9/16–17 vs reports 9/22) and its **daily flow** (5.8 has no unit; there is no metered series).
- **The "14 incidents in 14 days" basis** (I5). **The UANI ~50-tanker count** (flagged source). **Forties >$140 at an assessment publisher** (Kemp only).
- **A Hormuz transit LEVEL.** Every count is a floor, and the instruments disagree.
- ⛔ **Not carried (guard kills):** "record" as a cross-instrument absolute · "Iran will block the Oman corridor" (an inference) · "blockade of the Strait of Hormuz" · "highest since the war began" (Forties) · "Aramco says Abqaiq and Khurais attacked" (2019) · "5.8 million bpd" as a quoted unit, or "7 mb/d" as flow or loss · "US-Iran ceasefire unravelled" (ADD#20) · "Iran ruled out nuclear talks" (Report.az gloss) · OilPrice's "12 attacks Sept 28–Oct 2 per JMIC" · ON PEACE = 158-26 · any new Jeddah strike on 10/06.
