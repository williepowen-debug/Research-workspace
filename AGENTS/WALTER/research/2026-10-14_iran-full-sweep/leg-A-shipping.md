# Iran full sweep 2026-10-14, LEG A: shipping / Hormuz / Red Sea

**Executor:** read-only verify-research helper for WALTER. **Written:** 2026-10-15T01:09:34Z (from `date -u` in the writing command). **Window:** EVENT dates 2026-10-08 → 2026-10-15 (UTC). Last full sweep: 2026-10-08 ~12:20Z.
**Read first (owner records):** `anchors/IRAN_WAR.md` (whole); `anchors/IRAN_WAR_GUARDS.md` (whole, 428 lines, in chunks); `research/2026-10-08_iran-full-sweep.md` (§2 hull table through 158-26); FALCON `STATUS.md` (head), `reports/2026-10-09_iran-limb-and-ladder.md`, `domain/vessel-incidents/VESSELS.tsv` (header + VI-0035..0059); BOARD `-1009-005`, `-1011-006`, `-1011-007`, `-1012-009`, `-1012-040`, `-1013-010`, `-1013-011`, `-1014-002`, `-1014-025` (bodies), plus `-1008-034` and `-1009-015` for 159-26 and freight; WALTER helper files 10/11, 10/12, 10/13 and 10/14.
**Guards applied:** date before mechanism (§8 lists 17 rejects) · "vessel sunk" theater-checked before gate-checked · ADD#26 five discriminators on every UKMTO row (event vs REPORT date is the live trap this week: 166–169 and 172–173 are time-late) · maritime clock collision (MPA uses Singapore time, UTC+8; India uses IST) · ADD#24 (a wire's geography is not a fix) · Tasnim/IRGC mine-claim block (a claim on relay is not a detonation) · ⭐ denominator (88 canonical; gCaptain's "130–140" = ~140 peak-day mis-cite; "~125" is a different base; transit counts are FLOORS) · intercepted→struck / claim→fact in retelling (vesseltracker turns the IRGC mine claim into a declarative) · ADD#13 (which sea) · declaratory-control (move on behavior). **I do not grade; FALCON owns the loss census, gate eligibility and the ladder.**

## §0 Unreachable primaries (stated up front)

| Source | Result | Workaround |
|---|---|---|
| ukmto.org (site, warning PDFs, JMIC 104 PDF, VRA PDF) | **403** (curl browser UA and WebFetch, 2026-10-15 ~00:55Z) | **UKMTO's own PNG renderings attached to @UK_MTO posts, via api.fxtwitter.com — read for 159-26…173-26, JMIC 103/104 p.1, VRA No.10 cover.** Post times decoded from X IDs. JMIC 104 **page 2+ unread**. Latest UKMTO post at check: **173-26, 2026-10-14 10:23:27Z** (rechecked 01:04Z 10/15) |
| IMO Middle East incidents table | **Fetched** (indexed query URL). "As at 14 October 2026: 113" incidents, 24 seafarer fatalities | — |
| Singapore MPA release (10/14) | **Fetched** | — |
| CENTCOM | centcom.mil not tried. **@CENTCOM posts read via fxtwitter** (10/7–10/14) | — |
| IMF PortWatch | **Fetched** (ArcGIS FeatureServer, chokepoint6 + chokepoint4, 2026-10-15 00:58Z; newest print **10/11**; vintage may revise) | — |
| Baltic Exchange weekly tanker | **Bot challenge** (200 "Challenge Validation") | The Edge Malaysia relay of Baltic data (fetched) |
| Seatrade, Splash247, IranWire, Albawaba | **403** | search snippets only; flagged where used |
| CNN 10/11 analysis | **451** | not used |
| Kpler / LSEG / Windward / Lloyd's List vessel counts 10/8–10/14 | **not found** (search) | Kpler barrels via Al Jazeera and Anadolu relays only |
| Reuters (direct) | not opened; Reuters text read via Cyprus Mail (10/14 20:40) and Internazionale (10/14) syndications | — |

## §1 Hull table: UKMTO 159-26 → 173-26 (continues the 10/08 table)

All rows below were **read in UKMTO's own product image** (fetched) unless the cell says otherwise. "Posted" = decoded X post time (UTC). UKMTO names no hull in any of these; every name comes from another source, which is stated.

| UKMTO | EVENT (UTC) | Posted | Vessel (who named it) | Flag / manager | Dir. | Mechanism / damage / casualties | UKMTO position | Sea | Identity verdict / conflicts |
|---|---|---|---|---|---|---|---|---|---|
| 159-26 ATTACK | **06 Oct 1709Z** (time-late, verified source) | 10/08 14:54Z | crude oil tanker; JMIC 104 "Name withheld UFN" | — | "transiting" | unknown projectile; JMIC 104: **port aft quarter, vessel lost power, en route to Ras Al Khaimah with tug assistance**; no casualties | circle N of Musandam | Hormuz | **Event before window** (reconciliation only). FALCON VI-0056. Weak candidate: IMO's **ST1** (6 Oct, "2NM off coast of Oman, near Jazirat", damaged). NOT ESTABLISHED |
| 160-26 ATTACK | **09 Oct 1000Z** | 10/09 12:57Z | **GEM NO.2** (named by **JMIC 104**, a primary; IMO 9735373 on IMO table) | Panama (relays) | at anchor | unknown projectile; fire extinguished; crew status unknown at report. JMIC: India's ministry confirmed all Indian crew safe | "13NM west of Al Jazeera, UAE"; JMIC: "Arabian Gulf, at anchor in UAE TTW about 11–13 NM off the coast" | **Persian Gulf (UAE TTW), not the Strait** | **CONFIRMED** identity (JMIC). India's minister called it a drone hit at "Sharjah anchorage"; carry both. Second fire and 22-crew rescue 10/10 = BOARD -006 |
| 161-26 ADVISORY | 10 Oct 1850Z | 10/10 19:31Z | several masters | — | at anchor | **directed via VHF broadcast to move from their anchorages** (broadcaster not named); non-kinetic | vicinity Ras Al Khaimah | Gulf (UAE) | Non-kinetic. Not attributed by UKMTO |
| 162-26 ATTACK | **10 Oct 1920Z** | 10/10 22:09Z | outbound tanker; JMIC "withheld UFN". **VALTHERA** (IMO 9296389) is IMO's 10 Oct "Strait of Hormuz, Oman TTW" row; India named Valthera hit "on October 11" with fire | Marshall Is. (India) | outbound | port side, unknown projectile, **fire**; crew safe; JMIC: fire out, no longer needs assistance | circle just N of Musandam tip | Hormuz (Omani side) | **VALTHERA ↔ 162-26 INFERRED-STRONG**: date (1920Z 10/10 = 00:50 IST 10/11, which resolves India's date), sea, fire, IMO date. UKMTO/JMIC do not name it. FALCON rules |
| 163-26 ADVISORY | 10 Oct, time TBC | 10/11 03:01Z | "a tanker" | — | — | "incident involving a tanker and military forces" (source: military authorities) | circle off N Oman coast | Gulf of Oman | Same as CENTCOM's **Ocean Molica** (US jet, 10/10, Gulf of Oman, "cargo vessel")? **INDETERMINATE** (tanker vs cargo) |
| 164-26 ATTACK | **11 Oct 1200Z** | 10/11 13:26Z | outbound tanker. **ANGOLA PROSPERITY** (IMO 9896414; Sinokor) named by vesseltracker 10/14 digest (fetched): struck 11 Oct 1200 UTC outbound, port side/stern; steering-gear room and port-side water tank damaged; proceeded to Fujairah anchorage. IMO: 11 Oct, "8NM from the coast of Oman", damaged | Liberia (vesseltracker) | outbound | port side, unidentified projectile; damage; crew safe; no environmental impact. **No fire stated by UKMTO**; vesseltracker says the crew fought "the blaze" | circle just E of Musandam tip | Hormuz (Omani side) | **INFERRED-STRONG** (all five discriminators match; the damage detail is the same as JMIC 104's 164 narrative quoted in BOARD -1013-011). The IRGC Sunday "mine" claim (BOARD -006 T4) vs 164-26 stays **INDETERMINATE** |
| 165-26 ATTACK (UPD 001) | **11 Oct, time TBC** | upd 10/11 21:02Z | tanker; **PETRO DOLPHIN** (IMO 1072294; India's minister; IMO table) | Nicaragua (India) | at anchor | reclassified to attack: **struck by an Uncrewed Aerial Vehicle**; local authorities assisting crew evacuation. IMO: **"Two seafarers missing"** | vicinity of Sohar anchorage, Oman | **Gulf of Oman, outside the Strait** | Consistent (BOARD -007, -1012-003). Not new |
| 166-26 ATTACK | **11 Oct, TBC** (time-late) | 10/12 16:13Z | outbound tanker | — | outbound | unknown projectile; crew confirmed safe; environmental impact unknown | circle N of Musandam | Hormuz | Weak candidate: **AL MAQAM** (IMO 9732577; IMO table 11 Oct, Hormuz, damaged). ⚠️ The IRGC's video of AL MAQAM is claimed for **"Monday morning" (10/12)** (Herald 10/13 05:49, zone unstated, via Sepahnews); IMO dates it **11 Oct**. Date conflict. NOT ESTABLISHED |
| 167-26 ATTACK | **11 Oct, TBC** (time-late) | 10/12 18:22Z | **container vessel** | — | **inbound** | unknown projectile | circle E of Musandam tip | Hormuz | vesseltracker: "unidentified India-flagged containership, inbound". Weak candidate: **DP WORLD KAVERI** (IMO 9363429; IMO 11 Oct, **"One seafarer injured"**). NOT ESTABLISHED |
| 168-26 ATTACK | **11 Oct, TBC** | 10/12 18:37Z | **products tanker** | — | outbound | unknown projectile | circle W of Musandam tip | Hormuz | Candidate **KITION M** (IMO 9321160): Vanguard via Seatrade snippet (product tanker, Panama; page 403); IMO 11 Oct, **"Limited pollution reported"**. vesseltracker garbles its type. MEDIUM, not established |
| 169-26 ATTACK | **11 Oct, TBC** | 10/12 18:58Z | **crude oil tanker**; vesseltracker: "UKMTO #169 corresponded with the **EVER VICT** (IMO 9266774)", outbound, ~11.5 nm NW of Khor Khwair, UAE; AIS dark; resumed 10/12 16:41Z, then drifting "Not Under Command" (10/12 18:01Z, 10/13) | Bahamas (vesseltracker) | outbound | unknown projectile. IMO: **"Two seafarers injured"** | circle W of Musandam tip | Hormuz (western approach) | Single-aggregator mapping. IMO confirms an EVER VICT hit on 11 Oct with 2 injured. ⚠️ The name reads like an Evergreen box ship; IMO number and vesseltracker say a tanker |
| 170-26 ATTACK | **13 Oct, TBC** | 10/13 19:03Z | **container ship** | — | n/s | unknown projectile; **no damage or casualty stated** | circle N of Musandam | Hormuz | Best candidate for **GFS PRIDE** (sank; see §2): the only 13 Oct container warning without "minor damage". MPA: struck "13 October **Singapore Time**". INFERRED, not established. **UKMTO has not reported a sinking in any product** |
| 171-26 ATTACK | **13 Oct, TBC** | 10/13 19:06Z | **tanker** | — | n/s | unknown projectile | circle N of Musandam | Hormuz | vesseltracker mentions a tanker **ALFONSO** (IMO 9256298) "targeted … the same day". Single aggregator, day ambiguous, not on IMO table as at 10/14. NOT ESTABLISHED |
| 172-26 ATTACK | **13 Oct 1640Z** (time-late) | 10/14 10:17Z | "a **50,000 tonne** Container ship" | — | **inbound** | unknown projectile; **minor damage, no casualties, continued on its passage** | circle at Musandam tip | Hormuz | **GFS GISELLE ↔ 172-26 INFERRED-STRONG.** Size: GISELLE ~54,117 dwt / GT 44,887 (registries). Clock: MPA "14 October **SGT**" = from 13 Oct 16:00Z, so 1640Z fits. MPA: hull damage, reached safe anchorage under own power, 22 crew safe. IMO: 13 Oct, 6NM off Oman |
| 173-26 ATTACK | **13 Oct 1700Z** (time-late) | 10/14 10:23Z | "a **19,000 tonne** Container ship" | — | **outbound** | unknown projectile; minor damage, no casualties, continued | circle at Musandam tip | Hormuz | Candidate **AL SAADIYAT** (IMO 9760598; IMO 13 Oct, "1 NM from the coast of Oman", damaged; vesseltracker: a container ship). INFERRED by elimination; size not verified. ⛔ **Not GFS PRIDE** (39,446 dwt; sank) |

**Also in the window, outside the UKMTO series:**
- **CENTCOM, posted 10/14 19:41Z:** "On Oct. 6, U.S. forces destroyed an Iranian-affiliated dhow conducting surveillance and targeting U.S. Navy ships in the Gulf of Oman"; crew removed first. US action; event before window. It **reconciles** Reuters 10/14's unnamed US official on unarmed small-boat spotters.
- **Fujairah DHALGOUT fire (10/8):** still no UKMTO number and not on the IMO table. Stays cause-unknown (FALCON VI-0059).
- **IRGC claims (CLAIM-ONLY):** 10/10 and 10/11 mines (BOARD -006); "third tanker, Monday morning" 10/12 (BOARD -040), whose video shows a hull marked **AL MAQAM, Monrovia** (Herald, fetched); 10/14 GFS PRIDE "mine" (BOARD -025).

**Tally, event-dated 10/08–10/14 UTC (UKMTO products posted to 10/14 10:23Z):**
- **12 ATTACK warnings** (160, 162, 164–173) and **2 advisories** (161, 163).
- By event day: 10/9 ×1, 10/10 ×1, **10/11 ×6**, **10/13 ×4**.
- By sea: Hormuz 10; Persian Gulf (UAE) 1; Gulf of Oman 1 (+ advisory 163); **Red Sea 0**.
- **No UKMTO product is event-dated 10/8, 10/12 or 10/14.**

⚠️ **Report-date traps (ADD#26):**
- Anadolu's "six ships attacked **Monday** alone" (10/12) and the 10/12 "highest daily tally" framing describe the **10/11** events, posted 10/12.
- MEE and AVA's "container ship struck **Wednesday Oct 14**" is 172-26's **post** date; the event was 13 Oct 1640Z.

**Other counts (separate instruments; never average):**
- **IMO:** 100 incidents (as at 10/9) → 104 (10/12) → **113 (10/14)**; 24 fatalities unchanged.
- **Al Jazeera (UKMTO basis):** "15 attacks 10/6–10/14, 11 in the past four days". This matches warnings **issued** 10/6–10/14 (157, 158, 159, 160, 162, 164–173), a report-date basis.
- **vesseltracker:** UKMTO October tally "24 warnings + 3 advisories" (147–173). Consistent with the numbering.

## §2 Losses, sinkings, mines

| Item | Verdict | Basis (event date · source · fetched/relayed) |
|---|---|---|
| **GFS PRIDE sank** | **CONFIRMED** (flag state + IMO) | **Singapore MPA, 14 Oct (fetched):** Singapore-registered container vessel, "reportedly struck by unknown projectiles" while transiting the Strait of Hormuz on **13 Oct Singapore Time**; "sustained damage and a fire on board, and has since sunk"; all 21 crew evacuated, no injuries; MPA calls the attacks "unprovoked, unjustifiable" and a breach of international law; **no attacker named, no mine mentioned.** **IMO table (fetched):** "13 October · GFS PRIDE (IMO 9349045) · Strait of Hormuz · Sunk. No pollution." Reuters 10/14 (Cyprus Mail syndication, fetched): manager GFS Ship Management FZE (UAE) unreachable; 2,824 TEU. Position: "one mile east of Ras Makhbuq" appears only in vesseltracker (aggregator, unverified). UKMTO mapping (170-26) INFERRED |
| GFS PRIDE **cause**: projectile vs mine | **INDETERMINATE (mechanism) / mine = CLAIM-ONLY** | Projectile: MPA (flag state) and Reuters maritime-security sources. Mine: the IRGC Navy PR office via Tasnim, Mehr and Fars on the morning of 10/14 (BOARD -025), naming no ship. Marisks: "no independent evidence" of a mine. gCaptain 10/14: Iran claimed it "without evidence". ⛔ vesseltracker's sentence "was struck by a mine and caught fire" is the claim restated as fact by an aggregator. Not adopted |
| **IMO "second vessel lost"; who was first** | **CORRECTED. IMO table now marks THREE "Sunk"** | IMO table as at 14 Oct (fetched; rows quoted verbatim): **SAFEEN PRESTIGE** (IMO 9593517) "4 March · 2NM north of Oman · Sunk. Oil slick detected. No injuries." · **CAPE DAO** (IMO 9219020) "23 September · 15NM northeast of Khasab, Oman · Damaged. No pollution. One seafarer fatality. Sunk." · **GFS PRIDE** "13 October · Sunk". Reuters 10/14 ("an analysis of IMO casualty data"): PRIDE and Cape Dao "are the second and third vessels to have sunk since the US-Iran war began on February 28"; Safeen Prestige (Maltese-flag) was hit by a projectile in March and later sank north of the Strait. ⇒ The first was **Safeen Prestige**. "PRIDE = second" (gCaptain, BOARD -025) is superseded; PRIDE is 2nd or 3rd depending on Cape Dao's unknown sinking date |
| **CAPE DAO sank** | **CONFIRMED at IMO primary; sinking DATE NOT ESTABLISHED** | IMO row above (fetched) + Reuters 10/14: Cape Dao "sank close to the strait, weeks after being struck" by a projectile on 9/23, per IMO data "on Wednesday". This upgrades BOARD -025's "reportedly sinking (Vanguard, single source)". ⚠️ A Substack's "Cape Dao sank on October 14" is the **report** date, not an established sinking date. ⚠️ Position conflict: IMO "15NM northeast of Khasab" vs FALCON VI-0036 "2.5 nm off Musandam / 5.2 nm N of Kumzar". FALCON's row reads NO total loss as of 9/28 |
| **FALCON census basis** | **FOR FALCON** (no grade here) | FALCON's 3 losses are VI-0016 **Faize Noore Oliya** (dhow, 8/4), VI-0024 **Kylo** (9/5, US strike, sanctioned-Iran tanker) and VI-0028 **Riesco** (9/8, US strike). **Zero overlap with IMO's three sunk rows**, and neither Kylo nor Riesco appears on the IMO table. Other instruments, never to be summed with these: UKMTO VRA No.10 "5 confirmed total losses YTD" (BOARD -1012-009); CENTCOM 10/11 release "destroyed 10 tankers linked to the IRGC's … shadow network" since 7/14 ("destroyed" ≠ sunk) |
| **Any CONFIRMED mine detonation on a hull** (non-Iranian authority) | **NOT ESTABLISHED** | **UKMTO:** "projectile" in all 12 in-window attack warnings, and UAV for 165-26. **MPA:** projectile. **IMO:** no mechanism field. **CENTCOM:** silent on the claims; its 10/8 17:02Z post says it "successfully cleared sea mines from primary transit lanes". That says mines were present and cleared; **it is not a detonation on a hull.** Analyst Mercogliano (The National 10/13): the 10/10 IRGC video does not look like a mine strike. IRGC mine claims 10/10, 10/11, 10/12 and 10/14 are all **CLAIM-ONLY** |
| Other sinking / constructive total loss | **NONE established** | GEM NO.2 (two fires, crew evacuated 10/10): IMO "Damaged". EVER VICT drifting "Not Under Command" (AIS, 10/12–13; vesseltracker): IMO "Damaged". No CTL declaration found for either |

## §3 Transits (FLOORS, not levels; 88/day canonical; never blend vendors)

| Vendor / instrument | Basis | Dates → values | Read |
|---|---|---|---|
| **IMF PortWatch** chokepoint6 | AIS daily transits, all types (impeached as throughput, BRENT 8/21) | 10/05 **8** · 10/06 **2** · 10/07 **6** · 10/08 **4** · 10/09 **3** · 10/10 **4** · 10/11 **2** (newest). 7d 10/05–10/11 = **29 (4.1/day ≈ 4.7% of 88)**; prior 7d (9/28–10/04) = 19 (2.7/day). Tankers 4 vs 6 | **Fetched** 2026-10-15 00:58Z |
| Anadolu (10/14 18:16, zone unstated) | "commercial ships", **no vendor named** | 10/8 **32** · 10/9 **24** · 10/10 **11** · 10/11 **12** · Mon 10/12 **6**; "lowest since July 22" (unattributed) | Fetched; vendor unknown ⇒ not comparable with PortWatch |
| **Kpler barrels** (relayed) | oil moved through the strait, one-day volume | 10/8: **20.8 mb** (Al Jazeera) / **21.1 mb** (Anadolu) · 10/11: **2.9 mb** (Al Jazeera) vs **6.7 mb** (Anadolu), a **CONFLICT** within the same vendor (vintage or scope) · Mon 10/12: **10.4 mb** (Anadolu) · Tue 10/13: **8.3 mb** (Anadolu) · weekly average 17 mb (Anadolu) | Relays (Al Jazeera 10/14, Anadolu 10/14), both fetched. ⛔ Two "prewar" bases: **17.1 mb/d** (Al Jazeera, vendor unnamed) vs **~23.3 mb/d** (Anadolu). Never blend |
| **CENTCOM "19 mb"** | US self-report: "assisted Gulf partners in shipping more than 19 million barrels of crude oil through the strait" | **Mon 10/12** ("Just yesterday", @CENTCOM post **10/13 20:40Z**, fetched). Earlier, 10/7 21:59Z: "20 million barrels of crude oil", **no time unit** | Primary, unverifiable. **Versus Kpler 10/12 = 10.4 mb (relay): about a 2× gap.** CENTCOM's escorted/dark movements may be included; it names no vendor. Contrary signal, not a measurement |
| Kpler / LSEG vessel counts | commodity vessels / all vessels | **No 10/8–10/14 print found.** Last: Kpler 7 (Tue 10/6), 10 (Wed 10/7); LSEG 8 (10/6), 14 (10/5) | prior sweep |
| Windward, Lloyd's List | — | **No October print found** (the Lloyd's List "39 transits" result is the week of July 20–26, rejected in §8) | — |
| UKMTO VRA composite | AIS + US-NCAGS movements | 129 out / 146 in (7d to 10/7, VRA No.10). No No.11 posted as at 10/14 10:23Z. VRA No.10 cover: 133 warnings, 18 advisories, 122 Iran–US conflict incidents, 6 Red Sea attacks on shipping, 41 piracy-related YTD | UKMTO image (fetched) |

**Trend:** the instruments **disagree on direction.** PortWatch's 7-day floor rose (19 → 29); Anadolu's unnamed-vendor daily count fell 32 → 6 (10/8 → 10/12); Kpler barrels fell from ~21 mb (10/8) to 2.9–10.4 mb (10/11–10/13). No instrument shows a sustained climb toward 88. ⛔ Prewar figures seen this week: gCaptain 10/14 "roughly 130 to 140 vessels" (**KILL**, ~140 peak-day mis-cite) and Al Jazeera/Reuters "~125 large commercial vessels" (a different denominator from 88).

## §4 Red Sea / Bab el-Mandeb

| Item | Finding | Basis |
|---|---|---|
| Hull attacks 10/08–10/15 | **None found** | No Red Sea or Bab UKMTO product among 159–173 (fetched). Last Bab item: 151-26 CHRYSTAL SKY near-miss, 10/04 (JMIC 103: ~15 NM off Yemen, airburst within 100 m, no damage). Searches returned only July/August 2026 events (§8) |
| Houthi maritime claims | **None found** in window | Saree statements in the window target Saudi land (airports; Aramco Dhahran 10/13); the 10/14 Aramco-shareholder threat = BOARD -025. Stated embargo scope is **Saudi-only** (Saree 9/11 and 9/13; ABC 10/8: "exempted non-Saudi vessels") |
| Closure order / Iran-ordered closure | **None found** | ABC 10/8 (fetched): "No formal closure declaration". ADD#13: the Houthi campaign's stated cause is the Saudi–Houthi war |
| Transit | **No collapse** | PortWatch chokepoint4 (fetched): 7d 10/05–10/11 = **198 (28.3/day)** vs 207 (29.6/day) prior, **−4.3%**; tankers 60 vs 63. Anadolu (vendor unnamed): 35 (10/8), 39 (10/10), 46 (10/11), 32 (10/12). FALCON's TankerMap is a separate instrument (74 vs 80 to 10/09) |
| Control of the strait | **CONTESTED (unchanged in kind)** | Government forces claimed Mocha, Dhubab and "Bab al-Mandeb" positions on 10/5–6 (Reuters/AP/Bloomberg; the Houthis dispute Mocha). **Perim:** Houthi-seized 9/11; no report of a change found. Nothing dated 10/10–10/14 found. Al Hadath naval-mines report (10/10): no new corroboration (FALCON graded it) |

## §5 IRGC maritime posture / corridor

| Item | Date | Status | Source |
|---|---|---|---|
| VHF order to leave anchorages, Ras Al Khaimah | 10/10 1850Z | **CONFIRMED event**; broadcaster unnamed | UKMTO 161-26 (fetched) |
| IRGC hail / turn-back | 10/08–10/14 | **None in the UKMTO series** (last: 152-26, 10/5) | UKMTO products (fetched). JMIC (via Al Jazeera 10/14): "targeted surveillance", "UAV overflight", "occasional VHF hailing"; threat level **SEVERE** (JMIC 103/104 headers, fetched) |
| Small-boat spotters | dhow destroyed **10/6**; reported 10/14 | **CONFIRMED** (CENTCOM primary) + Reuters 10/14 (anonymous US official) | @CENTCOM 10/14 19:41Z (fetched); Reuters via Internazionale (fetched) |
| Boardings / seizures | 10/08–10/15 | **None found** (search-based; the Talara result is Nov 2025, §8) | — |
| Strike / mine claims | 10/9, 10/10, 10/11, 10/12, 10/14 | **CLAIM-ONLY**; AL MAQAM named in the IRGC's video (10/12 claim) | BOARD -005/-006/-040/-025; Herald 10/13 (fetched) |
| Control / perimeter declarations | 10/13 IRGC Navy commander: the Strait is "under IRGC control" and approaching US warships would be "sunk" (as quoted by CENTCOM, which replied "has no navy"). Press TV 10/13 (via Al Jazeera): the Iranian Navy deployed "east of the Strait of Hormuz and across the Sea of Oman and the Arabian Sea". Naqdi (Fars; carried by The National 10/13): will close "illegal" routes **including passages along Oman's coast**. Reuters 10/14 (two unnamed Iranian officials): tactics changed ~10 days ago; scope to expand beyond Hormuz. Rezaei (per Al Jazeera): "five or six" vessels struck nightly | **DECLARATIONS** (declaratory-control guard: move on behavior). ⚠️ The **perimeter half** has unattributed behavioral corroboration this week (hits at Sohar 165-26, RAK 160-26, off Qatar 158-26), but UKMTO and IMO attribute none. FALCON grades | as cited |
| PGSA non-compliant list | — | **No October update found** (latest: 9/30 amendment per Global Trade Alert; 77 vessels as of 9/14) | search |
| Cable permit / "fee" authority | — | **No October enactment found.** Traces to **May 2026**: Zolfaghari's "We will impose fees on internet cables" (5/9), the Tasnim/Fars proposals, Euronews 5/15. The 10/12 HormuzLetter attribution (BOARD -040) is still unrecovered. Novelty **UNKNOWN**; recirculation likely | search; Albawaba "imposes" page 403, so not adopted |
| **Iran–Oman "safe corridor"** | Baghaei 10/7; TASS (Rabat dateline) 10/8 | Coordinates "agreed"; notification to "the relevant international body" **"soon"**. **No body named, no coordinates published, no IMO circular found** through 10/14. Not an implemented, dated framework | TASS (fetched); Gulf News/New Arab (search) |
| US blockade | 10/9–10/11 | 133 vessels redirected as of 10/9; the 10/11 release gives 135 turned around, 4 disabled and 10 IRGC-linked tankers "destroyed" since the 7/14 resumption; **Ocean Molica** disabled 10/10 | @CENTCOM (fetched) |
| Iran at the IMO | ~10/14 | Iran's IMO ambassador complained of US "threatening, abusive" language; CENTCOM: "FALSE" | @CENTCOM 10/14 14:11Z (fetched) |

## §6 War-risk insurance / freight

| Item | Value (date · basis) | Source |
|---|---|---|
| Gulf/Hormuz war-risk premium | **No dated quote for 10/08–10/14 found.** Newest dated: Reuters 9/25, Hormuz **6–9%** of hull (FALCON). Reuters 10/14: "high shipping and insurance costs" (qualitative) | ⛔ Not adopted: straitofhormuz.report "~1.5% … as of 2026-10-08" (its body cites Lloyd's JWC data of **4/9**, so the date is inconsistent); BigGo "6–10%" (undated aggregator) |
| **TD3C, Baltic, week 41** | **WS1,318.75 ≈ US$1,412,594/day** round-trip TCE ("climbed 115 points") · report **10/9** | The Edge Malaysia relay of Baltic data (fetched); Baltic site bot-gated |
| TD34 (Gulf of Oman → China), Baltic wk41 | **WS841.07 ≈ US$912,660/day** (+62.5 pts) · 10/9 | same |
| ⚠️ Baltic prior-week basis | Baltic's "+115 points" implies the prior weekly print was **WS1,203.75**. BOARD -1009-015 carries "Baltic 10/2 WS1,145 / $1,221,893", the **same WS as Gibson's 10/1**. **BRENT to reconcile**; I compute no week-on-week % | — |
| Gibson TD3C | WS1,319 / $1,478,500 (10/8), already on BOARD; a **different convention** from Baltic. Never blend | BOARD -1009-015 |
| **TD3C week 42** | **NOT PUBLISHED / NOT FOUND** (Baltic and Gibson weeklies due ~10/16; no mid-week print found) | — |
| Receiving tonnage | ≥10 empty VLCCs and several Suezmaxes stopped or reversed near Fujairah "in recent days" (Bloomberg 10/13), already BOARD -1013-010 | gCaptain syndication (fetched) |

## §7 Ladder items touched

| Ladder item | Verdict | Basis |
|---|---|---|
| **#2: a vessel CONFIRMED SUNK by hostile action, or a CONFIRMED mine detonation on a hull** | **Sinking limb: FACTS ON RECORD, FOR FALCON TO ADJUDICATE. Mine limb: NOT FIRED** | **GFS PRIDE:** sinking confirmed by the flag state (MPA) and the IMO; "struck by unknown projectiles" in the Strait of Hormuz (the **right theater**; the ADD#13 check passes); MPA describes it as an attack; attacker unattributed. **CAPE DAO:** "Sunk" on the IMO table (struck 9/23, Omani side of Hormuz, 1 killed); sinking date unknown. **Neither is in FALCON's current 3-loss census**, and that census uses a different population (a dhow and two US-struck sanctioned tankers). The anchor's immediate re-verify trigger, "a FOURTH confirmed sinking", depends on FALCON's census and attacker-identity rules. I do not count it. **Mine:** no non-Iranian authority confirms a mine detonation on any hull (§2) |
| **#3b: Bab el-Mandeb conditional** (an Iran-ordered closure, or a transit collapse) | **NOT FIRED** | No closure order; no Red Sea hull event (UKMTO 159–173, fetched); PortWatch Bab 7d −4.3% (28.3/day); stated Houthi embargo Saudi-only; control contested on land (§4). #3 (the grid campaign) is outside this leg |
| **#6: Hormuz transit RECOVERY** | **NOT FIRED** | PortWatch 4.1/day (10/05–10/11) ≈ 4.7% of 88, a floor; Anadolu daily count down to 6 (10/12); Kpler barrels 2.9–10.4 mb on 10/11–10/13, down from ~21 mb on 10/8. CENTCOM's ">19 mb" on 10/12 is a US self-report, contrary and unverified. No sustained climb on any instrument |

## §8 Date-trap and framing rejects (seen and not carried)

1. **MEE "IRGC says it attacked six vessels near Strait of Hormuz"**: dated **5 Sep 2026** (fetched); surfaced against an October query.
2. **GFS GALAXY** (Cyprus-flag container ship hit **7/13/2026**, one Indian missing, towed to Khor Fakkan): a different GFS hull, surfaced on "GFS Pride". Do not merge.
3. **Maritime Executive "Hormuz transits fall to lowest level in two months"**: the page displays 10/14 but was **published 10/8 14:15**, with data for **10/5–10/6**. Not a fresh print.
4. **Lloyd's List "39 transits"**: the week of **July 20–26**.
5. **Luni** partial sinking (**July**): surfaced on a Cape Dao query. Cause-unconfirmed and a different hull (anchor ladder #2 note).
6. **Tihamah (8/11)** and the **Yanbu tanker (8/24)** Houthi attacks: surfaced on an "October Red Sea" query.
7. **2017** SPA Bab mine warning and the **2018** Saudi Bab shipment suspension (the anchor's 2018 trap): both surfaced.
8. **Cable fees**: the Tasnim/Zolfaghari material is **May 2026**, not an October enactment.
9. **June 2026** Oman–IMO temporary corridor: a different instrument from the 10/7 Iran–Oman coordinates.
10. **Talara** seizure: **Nov 2025**.
11. **"Container ship struck Wednesday Oct 14"** (MEE, AVA): the **report** date of 172-26; the event was 13 Oct 1640Z (ADD#26).
12. **Anadolu "six ships attacked Monday" (10/12)**: the report day for the 10/11 events. Its "Houthi militias intensified attacks … in the Strait of Hormuz" is **MISATTRIBUTION**: UKMTO and IMO attribute none, and the Houthi campaign is Red Sea / Saudi land.
13. **"Cape Dao sank on October 14"** (Substack): the IMO data's report date; the sinking date is unestablished.
14. **gCaptain "roughly 130 to 140 vessels typically passed … each day"**: **KILL** (~140 peak-day mis-cite; 88 is canonical).
15. **straitofhormuz.report war-risk "1.5% as of 2026-10-08"**: date-inconsistent (its data is from the April JWC).
16. **Kpler blog "VLCC freight may have peaked"**: undated, with internal date **21 Sep**, so a September vintage.
17. **vesseltracker "GFS Pride … was struck by a mine"**: the IRGC claim laundered into a declarative sentence (claim → fact in the retelling). The same digest's ALFONSO line is also not carried as an attribution ("targeted by Iran").

## §9 Summary: what changed since 10/08

The hull war kept its pace and moved further out. UKMTO's own products (read as UKMTO's images; the PDFs are 403) number **159-26 → 173-26**. That is **12 attack warnings event-dated 10/09–10/13**: six on **10/11** alone, most of them reported late on 10/12, and four on **10/13**. Most are in the Strait. One was inside the Gulf off Ras Al Khaimah (GEM NO.2, named by JMIC) and one at **Sohar in the Gulf of Oman** (a UAV hit; 2 seafarers missing per IMO). **None was in the Red Sea**, and **none is event-dated 10/8, 10/12 or 10/14**. **Container ships are now being hit**: 167, 170, 172, 173. The IMO incident count rose from 104 (10/12) to **113 (10/14)**.

The material change is **losses**. **GFS PRIDE is CONFIRMED SUNK** by its flag state (Singapore MPA: struck by unknown projectiles in the Strait on 13 Oct Singapore Time; 21 crew safe) and by the IMO table. **CAPE DAO is also marked "Sunk" on the IMO table** (struck 9/23; sinking date unknown). That upgrades BOARD -025's single-source "reportedly sinking", and the IMO now lists **three** sunk ships: **Safeen Prestige (first, March)**, Cape Dao and GFS PRIDE. None of the three is in FALCON's 3-loss census (a dhow plus two US-struck sanctioned tankers), so **whether ladder #2's sinking limb fired, and whether this is the anchor's "fourth" loss, is FALCON's call; the facts are on the record.** The IRGC's GFS PRIDE **mine** claim stays **CLAIM-ONLY**: the flag state says projectile and no non-Iranian authority confirms a mine. **The mine limb did not fire.**

Identity work for FALCON, all INFERRED:
- VALTHERA ↔ 162-26 (strong)
- ANGOLA PROSPERITY ↔ 164-26 (strong)
- GFS GISELLE ↔ 172-26 (strong; the Singapore-time clock resolves the date)
- EVER VICT ↔ 169-26 (one aggregator)
- KITION M ↔ 168-26 (medium)
- GFS PRIDE ↔ 170-26 (best fit; UKMTO has reported no sinking)
- AL MAQAM: IMO dates it 10/11 while the IRGC video claims 10/12

Transits stay at floors with **instruments disagreeing on direction**: PortWatch 4.1/day (10/05–10/11); Anadolu 32 → 6 (10/8 → 10/12, vendor unnamed); Kpler barrels ~21 → 2.9–10.4 mb. CENTCOM's ">19 mb" for **10/12** is a self-report about 2× Kpler's 10.4 mb for the same day. **Ladder #6 not fired.**

Red Sea: no attack, no closure, PortWatch Bab traffic −4.3% w/w. **#3b not fired.**

IRGC posture: declarations widened (control, Sea of Oman / Arabian Sea deployment, routes along Oman's coast). One spotter dhow was destroyed by the US on 10/6. There were no boardings or turn-backs in the window. The Iran–Oman corridor has **no IMO notification or published coordinates**, and the cable-fee claim traces to May.

Freight: Baltic wk41 TD3C **WS1,318.75 ≈ $1.41M/day** (10/9). Week 42 is not out, and no dated October war-risk quote was found.
