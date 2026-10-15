# Iran full sweep 2026-10-14 — LEG C: diplomacy · US military posture · Iran internal

**Executor:** read-only verify-research helper for WALTER · **Written:** 2026-10-15T01:08:51Z (stamp from `date -u` in the writing command) · **Window:** EVENT dates 2026-10-08 → 2026-10-15 (baseline = `research/2026-10-08_iran-full-sweep.md` claims C, D, H, I1–I3).
**Read first:** `anchors/IRAN_WAR.md` (whole) · `anchors/IRAN_WAR_GUARDS.md` (whole, 428 lines, 27 blocks) · 10/08 sweep (whole) · FALCON STATUS head (10/10) + `reports/2026-10-09_iran-limb-and-ladder.md` · BOARD `SIG-W-20261011-002`, `-20261014-002`, `-20261014-025`, `-20261014-026` (+ context `-20261008-020/-034/-047`, `-20261011-006`, `-20261012-040`, `-20261013-008`) and helper files `2026-10-12_boot/iran-verify.md`, `2026-10-14_morning-news/verify-war-cftc.md`, `2026-10-14_evening-routing/verify-energy-geo.md`. **I report facts; FALCON grades.** No repo file other than this one was written.
**Guards applied:** mediated ≠ bilateral (+ "do not score a two-track contradiction as one side lying": Rezaei 10/11 vs Baghaei 10/12) · POTUS = tape · "US and Iran are negotiating" not established · ADD#14 (no "deal SIGNED", no "US accepted Iran's demands") · ADD#15 (do not merge condition lists; Aug-12 list ≠ Oct seven conditions) · ADD#20 ("ceasefire" = wrong word; wires still use it) · Mojtaba status-quo + ADD#22 (authenticate, don't dismiss — no artefact surfaced) · 'US struck nuclear sites' (none found) · ROUTING-GUARDS FOLD (Iranian "energy" target lists ≠ FAL-01) · flagged source hngn (not carried) · search-summary contamination (several summaries asserted "no October coverage" for items I then fetched; summaries not cited as fact) · METHOD NOTE (each "nothing found" is search-based, stated as such).

## §0 Unreachable / partial primaries

| Source | Result | Consequence |
|---|---|---|
| centcom.mil (press releases) | curl **403** | CENTCOM content only via relays: Ocean Molica 10/10 (Israel National News, fetched); dhow 10/14 X post embedded in Shafaq (fetched); 10/14 "fact check" via Maritime Executive (fetched) |
| apnews.com | curl 403; WebFetch blocked | Rezaei 10/11 read via Roya News embed of his X post + Reuters copy; AP not read |
| axios.com, wsj.com, nytimes.com | not read | Axios 10/13 via Iran International (fetched); WSJ 10/12–13 via CTP-ISW + Times of Israel (fetched) |
| en.mfa.gov.ir | 307, not followed | Baghaei 10/12 via Reuters (Yahoo UK copy, fetched) + Arab News PK (fetched) |
| tasnimnews.com, mofa.gov.pk | connection failure (000) | Pakistan side only via Oman MFA readouts |
| en.irna.ir | 200 shell (6 KB) | not used |
| Times of Israel 10/13 liveblog | curl 403; WebFetch read chars 0–200k of 448k | Netanyahu-pressed-Trump entry: headline only |
| globalsecurity.org tracker | WebFetch 402; curl 200, read whole (Day 229, cutoff 05:00 ET 10/14) | secondary tracker; used for "none found 13–14 Oct" only with that label |
| gov.uk joint statement | WebFetch summary only | signatory count taken from **State Dept primary** (fetched) instead |
| Qatar MOFA | listing reachable; no Iran-mediation item on 10/14 page; no 10/06 or 10/13 Al-Ansari briefing found by search | Qatar channel status = Iranian/US relays only |
| **Reachable primaries actually read:** Oman MFA (wp-json, 41 posts 10/07–10/14), White House news listing (10/9–10/14), State Dept (Rubio–Miliband readout 10/12; Fairford joint statement 10/12) | | |

## §1 US kinetic / posture (10/08 → 10/15)

| Item | Event date | Speaker / source (read?) | Fact | Verdict |
|---|---|---|---|---|
| Executed US strike on **Iranian territory** (incl. grid/power/bridges, Kharg, nuclear) | 10/08–10/14 | CTP-ISW Iran Updates 10/8, 10/9, 10/10, 10/12, 10/13 "US and Partner Military Operations: Nothing significant" (fetched); GlobalSecurity Day 229: "no American or Israeli strike on Iranian territory was reported for 13-14 October"; "No strike on an Iranian nuclear site … since 7 July" (fetched) | none found | **NONE FOUND (search/tracker-based; CENTCOM 403).** Ladder #3 (grid) and #4 (Kharg seizure) NOT FIRED; no Kharg item dated in-window |
| Axios 10/07 "conclude preparations" | — | — | **No decision, no date found.** Trump 10/08 post (below) pledges no attack before 11/3 | Preparation reporting not superseded by any execution |
| Trump–Netanyahu | "last week" (≈10/5–10/9) reported 10/13 | Axios via Iran International 10/13 (fetched): US official says Trump told Netanyahu "to prepare for a possible operation but made no commitment"; Netanyahu raised Iran rebuilding nuclear program. **White House official disputed** the discussion and reiterated no attack before 11/3. ToI 10/13 21:15 headline: "Netanyahu pressed Trump to renew Iran fighting before election; PMO denies" (body unread) | anonymous, two denials | REPORT, contested; not a decision |
| Trump "decision on Iran very soon" | 10/13 | Trump, South Lawn (Iran International, fetched) | decision unspecified | TAPE (§7) |
| NYT three-day campaign option | reported 10/08 | BOARD `-047` (relay) | plan | unchanged; no execution |
| Carriers | departed ~9/27–28 | relays (The National 10/01 etc., search) | TR CSG + Makin Island ARG en route; arrival "end-Oct" (AP-sourced) vs "end-Nov"; GW + GHWB in Arabian Sea; Lincoln to San Diego (KOMO/TNND 10/08, fetched) | **pre-window; no in-window change found** |
| B-1s / RAF Fairford | plot 9/27; withdrawal ~10/04 | **State Dept primary 10/12 (fetched):** joint statement of **30 governments** "recognize the United Kingdom's attribution of Iran's involvement in the incident at RAF Fairford on 27 September"; UK concluded it shows "the IRGC's continued willingness to project hostile activity beyond its borders" | **DELTA vs 10/08 I3** ("UK: no public Iran link"): the UK attribution now exists and is recognized by 29 partners | CONFIRMED (primary) |
| Dhow destroyed | **10/06** (disclosed 10/14) | CENTCOM X post 10/14, embedded in Shafaq 10/14 21:22Z (fetched): "On Oct. 6, U.S. forces destroyed an Iranian-affiliated dhow conducting surveillance and targeting U.S. Navy ships in the Gulf of Oman … Crew members were safely removed prior to destruction" | at sea, not Iranian territory; = Reuters 10/14's "previously unreported" spotter-dhow incident | CONFIRMED (CENTCOM via embed); pre-window event |
| CENTCOM "fact check" | 10/14 | Maritime Executive 10/14 10:47 (fetched): CENTCOM asserts the "IRGC's navy commander has no navy" and that 19 million barrels of crude passed through the Strait "yesterday" (10/13) | party claim; barrels not vessels; not a transit measurement | CONFIRMED as statement (relay). ⚠️ distinct from the **9/28** "no navy because we sank it" fact check (Sayyari) — §8 |
| UAE–US naval commanders | ~10/13–14 | Iran International via GlobalSecurity (not independently fetched) | coordination meeting, Abu Dhabi | relay-only |

## §2 US blockade of Iranian ports / shipping

| Date | Source (read?) | Fact |
|---|---|---|
| 07/14 | CENTCOM via Israel National News 10/10 (fetched) | "CENTCOM forces resumed America's blockade against all ships entering or departing Iranian ports on July 14." **Resolves the 10/08 I2 "mid-July, unverified" reinstatement date to a CENTCOM-stated 7/14 (relayed).** |
| 10/10 | same | US fighter jet struck the stern of Panama-flag **M/V Ocean Molica ("Arika Sun")**, Gulf of Oman, after it left an Iranian port and ignored warnings; propulsion disabled, no crew harm. **Tally since 7/14: 4 commercial vessels disabled, 135 turned around, 10 IRGC-linked tankers destroyed.** UKMTO 163-26 may be the same event (UNKNOWN, BOARD `-20261011-006`) |
| 10/08 | Trump Truth Social (KOMO/TNND, fetched) | "The blockade will remain in full force and effect, with Oil flowing in Record Numbers of Barrels through the Hormuz Strait" (TAPE) |
| 10/08 | Treasury sb0653 (BOARD `-034`, primary read by WALTER then) | 17 shadow-fleet vessels; a search relay's "27 companies / 22 vessels" figure is unreconciled, not carried |
| 10/14 | Reuters (Hafezi/Saul/Stewart), Internazionale syndication (fetched) | US "pressing its own naval blockade of Iranian ports and extending sanctions" |
| 10/11–10/14 | GlobalSecurity Day 229 (fetched) | "No new CENTCOM interdiction was located for 13-14 October." 10/11–10/12: none found by search |

**Status:** executed policy, enforced in the Gulf of Oman; one kinetic enforcement event in-window (10/10). Not "a blockade of the Strait of Hormuz" (wrong object; 10/08 guard stands).

## §3 Diplomacy

| Event date | Channel | Speaker | Content (verbatim where read) | Source / read | Verdict |
|---|---|---|---|---|---|
| 10/08 | Turkmenistan (Avaza), Putin meeting | Pezeshkian | Iran and US "exchanged new proposals" aimed at ending the war and reopening Hormuz | Anadolu (search snippet only) | context; mediated (Pezeshkian same day: "through intermediaries", BOARD `-047`) |
| 10/08 | Mediators (Qatar) | Araghchi (IRNA via TRT, BOARD `-020`) | will respond "within a few days" to the US reply on the "seven-day plan" | BOARD | baseline |
| **10/11** | via intermediaries (Pakistan, Qatar, Iraq per Iran) | **Mohsen Rezaei, SNSC Secretary** (title corroborated by CTP-ISW and Gulf News; appointed ~Aug) | X post (embedded in Roya News 10/12 00:18, fetched): **"The U.S. has agreed to some of Iran's seven conditions, but we consider its response INADEQUATE. Iranian diplomacy has changed and there will be no return to the status quo ante."** State media: some conditions accepted, others "unclear", "ambiguities"; no reopening or negotiation until conditions "fully met". Also 10/11: Iran targets ~5–6 small STS vessels nightly (CTP 10/12); threat to undersea cables / data centres / AI infrastructure (PressTV via CTP 10/12) | Roya (fetched); CTP (fetched) | **Iran's account of a US reply.** NOT a US accept/reject. ⛔ "US accepted Iran's demands" (ADD#14). Conditions list unpublished in full — do not merge with Aug-12 list (§8) |
| 10/11 | — | Rezaei (per Iran, BOARD `-002`) | US rejected Iran's proposal to manage the strait jointly with Oman, citing free passage under international law | BOARD (The National / Reuters / Anadolu) | Iran's report of the US position; **no US statement found** (searched) |
| **10/12** | via intermediaries; "Pakistan and Qatar continue to play the role of mediator" | **Baghaei, MFA weekly presser** | Iran "is still reviewing a US response to its proposal regarding the reopening of the Strait of Hormuz and will reply to Washington via intermediaries when the review is over"; "continues to exchange messages via intermediaries" | Reuters DUBAI 10/12 09:17 UTC via Yahoo UK (fetched); Arab News PK 10/12 16:15 (fetched) | **TWO-TRACK with Rezaei ("no longer in the process of responding"), not a contradiction to score.** Exchange LIVE, mediated, stalled. Reuters: core dispute = US insists on nuclear file first; Iran wants Hormuz first |
| 10/12 | US–UK | State Dept (Rubio–Miliband readout, fetched) | "shared commitment to safeguarding transit in the Strait of Hormuz and the importance of holding Iran to account" | primary | US posture statement; no deal content |
| 10/12–13 | back-channel via Arab officials and mediators | Iranian officials (WSJ, anonymous; relayed by CTP 10/13 and ToI 10/13 11:45) | Iran would target US forces/vessels "more aggressively" and regional energy incl. **Saudi oil facilities** if war resumes; hinted "land incursions into neighboring countries"; fortifying nuclear sites | relays (WSJ not read) | threat datum via mediators; not an event |
| 10/13 | Egypt–Iran call | Egypt FM Abdelatty → Araghchi | Houthi attacks on Saudi "cannot be accepted" | ToI 10/13 13:18 (WebFetch); Iran International (fetched) | third-state pressure; no Hormuz content |
| 10/13–14 | Iran–Oman call | Araghchi–Albusaidi "on Yemen and regional stability" | — | GlobalSecurity relaying Iran International (not fetched) | ⚠️ **not on Oman MFA's own feed 10/07–10/14** (41 posts read). Relay-only |
| **10/14** | Oman–Pakistan (Islamabad) | Albusaidi; Pakistan DPM/FM Ishaq Dar; PM Sharif | Albusaidi praised Pakistan's "efforts to help create space for dialogue between Iran and the United States"; Dar: ministers "exchanged views on the war between the United States and Iran, the closure of the Strait of Hormuz, developments in the Bab Al Mandab Strait"; Sharif praised Oman's role "in bringing views closer together" | **Oman MFA primary** (fetched) | mediator coordination; **no date, no instrument, no talks scheduled** |
| 10/14 | Reuters, two senior Iranian officials (anonymous) | — | "It will be complete closure soon"; strategy decided "at the highest levels"; "Tehran would not allow Trump to bring down oil prices before the November elections" | Reuters (fetched) | stated intent, attributed; Pentagon/MFA no comment |
| 10/14 | UN (UNOPS) | Moreira da Silva | fertilizer mechanism not activated; needs US–Iran deal "in the next few weeks"; 7–10 day activation lag | BOARD `-026` (Reuters) | **No delta found** (no WH/State/Iran comment found; UNOPS 9/24 interview shows the same stall) |
| 10/08–10/14 | UNSC / IMO | — | no UNSC action found (search; GlobalSecurity "No United Nations Security Council action was located for 13-14 October"); no IMO Hormuz statement in-window found | search-based | none |
| any | Qatar MOFA | Al-Ansari | latest briefing found = **9/29** ("exchanging messages … common ground") | Doha News 9/29 (fetched) | no in-window Qatari readout found |

**Scheduled talks:** none found. **US accept/reject statement:** none found (White House news listing 10/9–10/14 and State releases 10/9–10/14 contain no Iran-deal statement; only Iran's account of the US reply). **"US and Iran are negotiating"** remains NOT established as bilateral: every party statement in-window says intermediaries.

## §4 Ladder #5 verdict + FALCON-relevant facts

**Ladder #5 — NOT FIRED.**
- **Formal MOU-withdrawal instrument:** none (the MOU already expired 8/17; Rezaei's "no return to the status quo ante" is a statement, not an instrument).
- **Dated Hormuz-management framework / Iran–Oman corridor with a date:** none. Baghaei's 10/07 "geographical coordinates … agreed" (Iran International 10/07, search) is still **undated, coordinates unpublished, no Omani confirmation** — Oman MFA's own feed 10/07–10/14 carries no corridor, coordinates or IMO item; no IMO circular found. hngn 10/13 "close to implementation" = flagged source, not carried. Per Iran, the US **rejected** Iran–Oman joint management (10/11).

**FALCON C→B (needs a DATED framework):** not met. Facts: exchange is live and mediated (Baghaei 10/12 "still reviewing"); Iran calls US reply inadequate (Rezaei 10/11); mediators Pakistan/Qatar/Oman active (Oman MFA 10/14), no date; Trump "decision on Iran very soon" (10/13, unspecified, tape).
**FALCON D→C (needs a 72h two-sided halt):** not met. Iran-side hull events continued 10/10 (UKMTO 162-26), 10/11 (164-26; Sohar 165-26), 10/12 (IRGC third-tanker announcement), 10/13 (GFS PRIDE struck; Singapore MPA says it sank), 10/14 (GFS GISELLE struck) — BOARD `-20261011-006`, `-20261012-040`, `-20261014-002`, `-025` (legs A/B own these). US-side: Ocean Molica disabled 10/10 (CENTCOM). No 72h window without a two-sided kinetic event found.

## §5 Iran internal (incl. ladder #7)

| Event date | Speaker / source (read?) | Fact | Verdict |
|---|---|---|---|
| 10/08 | Mojtaba Khamenei, **written** statement on X for Police Week (Fox 10/11 16:34 EDT, fetched; Iran International) | praised FARAJA; "malicious attacks … have not caused the courageous personnel of the Police Force to waver" | **Ladder #7 NOT FIRED** — text only; no video/appearance surfaced, so no ADD#22 authentication case arose. "Supreme Leader" title = status quo |
| 10/09, 10/11, 10/13 | IRGC Navy (CTP 10/9); IRGC Navy cmdr **Rear Adm. Ali Ozmaei/Azmaei** (CTP 10/12; Iran International 10/13, fetched) | 10/9: will attack vessels "anywhere in the region" using unauthorized routes; 10/11: AIS-off vessels treated as hostile, response "severely and decisively"; 10/13: forces waiting for US warships to approach the strait to be "sunk" | declarations (KILL ③ logic: move on behavior) |
| 10/13 | Naqdi, adviser to IRGC C-in-C (Iran International, fetched) | a US ground attack would see large numbers of US troops captured | declaration |
| 10/11; ~10/13–14 | IRGC spokesman Hossein Mohebi/Mohebbi (CTP 10/12; GlobalSecurity relaying Iran International) | image of missiles targeting a US carrier; "the Trump administration needs an achievement before the midterm elections"; Iran would respond more forcefully | statement |
| 10/14 (pub.) | Reuters, two senior Iranian officials, anonymous (fetched) | new tactics began ~10 days earlier; one goal to influence the US vote; geography to expand to Gulf of Oman "and waters further afield"; "a game of chess"; vessels "safe nowhere" | **Election objective = attributed, unauthenticated intent** (BOARD `-002` already carries the core; deltas = highest-level decision, complete-closure claim, geography expansion, JMIC "severe" 10/11) |
| 10/10–11 | AEOI's Eslami (GlobalSecurity relay) | enrichment abandoned "under no circumstances" | relay-only |
| 10/11 | independent Iran-based outlet (CTP 10/13, "unable to verify") | ~30 Emad/Kheibar Shekan BM tests; Jaljaleh AA system test | UNVERIFIED |
| ~10/13–14 | Fars via Iran International (GlobalSecurity) | proposed defence minister Mehrdad Akhlaghi met IRGC commander Ahmad Vahidi on wartime production | relay-only |
| 10/07–10/09; ~10/13–14 | CTP 10/8–10/9 (fetched); Tasnim via GlobalSecurity | Baloch MPF attacks (Jalgh, Zahedan, Makran, LEC officer killed 10/9); Mehrastan: Basij women's unit commander and a police officer killed | insurgency in the southeast, elevated since early Sept; **no mass unrest found** |
| ~10/13–14 | Mizan via GlobalSecurity | execution of Ali-Sina Mostafavi (38, Kerman) | relay-only; no in-window espionage hanging found by search |

## §6 Other states

| State | Event date | Fact | Source (read?) |
|---|---|---|---|
| **Israel** | 10/08–10/14 | **No Israeli strike on Iran found** | CTP / GlobalSecurity (fetched); search |
| Israel | 10/13 | Axios: Netanyahu raised Iran nuclear rebuilding with Trump; ToI: "Netanyahu pressed Trump to renew Iran fighting before election; PMO denies"; Eisenkot: PM "not fit to carry out another operation"; Israel election 10/27 (Fox) | Iran International; ToI (partial) |
| Israel | 10/14 | heightened alert for a possible Houthi land/sea attack | GlobalSecurity relaying JPost |
| **Iraq** | 10/08 | Iranian drones hit a Khabat (Iranian Kurdish) camp near Erbil — first since US withdrawal 9/30 | CTP 10/9 (fetched) |
| Iraq | 10/09; 10/13 | militias surrender only some weapons, into the PMF; Coordination Framework constraining PM Zaydi | CTP (fetched) |
| Iraq | 10/14 | Zaydi Gulf tour incl. Saudi, Kuwait (planned); Kirkuk roadside bomb killed an army brigadier (Reuters, per GlobalSecurity note) | CTP 10/12; GlobalSecurity |
| **Oman** | 10/08, 10/10, 10/11, 10/13, 10/14 | condemned Abha/KKIA strikes; Albusaidi–Faisal bin Farhan call ("contain tensions"); King Salman message; Lavrov call (no content); Islamabad visit (§3) | **Oman MFA primary** (fetched) |
| **Saudi** | 10/13 | cabinet warned Houthis of "consequences"; Saudi strikes on Houthi fuel facilities in Sanaa/Hodeidah/Dhamar; Iran reportedly told mediators Saudi oil facilities would be targets (WSJ) | CTP 10/13; GlobalSecurity |
| Mecca pact | 10/05 activated (baseline) | no in-window activation step found; Pakistan's "by whatever means" pledge is **9/29**; Pakistan called NYT jets-in-strikes report "fake and fabricated" | search |
| Turkey | 10/13 | Erdogan told MBS Turkey stands by the kingdom; Trump "might" ask Erdogan to help | Iran International; Reuters (fetched) |
| Qatar | 10/13 | emir: headline that damage to energy facilities disrupted LNG exports (text unread); called for stepped-up security of Gulf/Hormuz routes | GlobalSecurity (Khaleej Times headline); ToI — **UNVERIFIED** |
| UAE | — | no in-window MFA/Gargash statement found | search |
| **Russia** | 10/08; 10/13 | Putin–Pezeshkian (Avaza); Lavrov–Albusaidi call. **Trump 10/12:** China and Russia not helping Iran "at all" | Anadolu (search); Oman MFA; ToI |
| **China** | — | no in-window Hormuz statement found (latest found 7/13, Lin Jian) | search |
| Europe | 10/12–13 | 30-government joint statement (State primary); MI5's McCallum on Iranian "harder targets, like military sites" (ToI 10/13 15:23); Merz urged Iran to negotiate seriously (Iran International) | primary + relays |

## §7 POTUS / administration tape (TAPE, not information)

| Date | Quote | Source (read?) |
|---|---|---|
| 10/08 | "we will not be attacking Iran at any time prior to the Midterm Elections … November 3rd" (BOARD `-034`); "productive discussions with the Islamic Republic of Iran"; "very bad condition, both Economically and Militarily"; "The blockade will remain in full force and effect, with Oil flowing in Record Numbers of Barrels through the Hormuz Strait"; claimed 22 mb moved the previous night | KOMO/TNND 10/08 (fetched); exact post minute still UNRESOLVED |
| 10/10 | considering whether the US will strike the Houthis after the KKIA attack | AP via CTP 10/11 |
| 10/12 | midterms: "No, it has no impact"; "as soon as the war ends, which will be very soon with Iran, the [price of] oil will drop like a rock"; China/Russia: "They have too much to lose, and we would know about it" | ToI liveblog 10/13 01:44 / 08:42 (WebFetch) |
| 10/13 | "Iran is a failed country. They have no economy. They have 300 percent inflation … We'll make a decision on Iran very soon." | Iran International (fetched) |
| 10/13 | Truth Social: Houthis "probably at the behest of Iran, which is a Failing Nation, with No Navy, No Airforce … purposefully trying to drive up Oil Prices, probably prior to the U.S. Elections — NOT NICE"; "I'll be there after the elections, and I will never forget!"; "President Erdogan, I think, would do as I ask" | Reuters via Al-Monitor and BusinessDay (fetched); Iran International |
| 10/13 | White House official (Axios): disputed that Trump and Netanyahu discussed resuming the war; reiterated no attack before 11/3 | Iran International |

⚠️ The "no attack before 11/3" pledge is silent on after 11/3; Trump's 10/13 "decision very soon" sits beside it unexplained. Neither is a decision record.

## §8 Date-trap and merge rejects

| Item | Real date / object | Why it surfaced |
|---|---|---|
| "Trump rejected Iran's seven-point / seven-day proposal" (GlobalSecurity 10/14 carries it as standing) | **2026-09-26** (Al Jazeera, NPR, The Hill) | not a new in-window rejection |
| Gulf News "Rezaei sets sweeping conditions": $300B compensation, $100B assets, US withdrawal, transit fees | **2026-08-12** | do not merge with the Oct-11 "seven conditions" (ADD#15 class); Oct list unpublished in full |
| "Iran rejects Oman's proposal for joint Hormuz management" | **late July 2026** (i24; Enterprise 7/29) | the INVERSE object of the Oct-11 item (per Iran, the US rejected Iran–Oman joint management). Also a name collision: **Ebrahim** Rezaei (Majlis committee spokesman) ≠ **Mohsen** Rezaei (SNSC) |
| CENTCOM "Iran has no navy because we sank it" | **2026-09-28** (Sayyari) | ≠ the 10/14 fact check |
| CENTCOM fact checks: tanker Nora, F-35 losses | **~2026-07-30** | blockade query |
| NBC "Mojtaba urges Gulf rulers in written message" | **2026-08-30** | Mojtaba query |
| Mojtaba "first video" (Mehr, 12 s, undated) / archive release | **~8/08–09; 8/18** | not an October appearance |
| B-2s to Diego Garcia | **2025** (Houthi campaign) | bomber query |
| Axios "Netanyahu raised round-2 strikes" | **2025-12-31** | Trump–Netanyahu query |
| Qatar Al-Ansari "mediation continues" | **2026-09-29** | latest Qatari briefing found |
| Pakistan "defend Saudi by whatever means" | **2026-09-29** | Mecca-pact query |
| The National (UNOPS, 9/24): "A US-Iran framework agreement was signed" | refers to the **June** instrument | ADD#14 "SIGNED" trap; not current |
| UNSC Bahrain Hormuz draft vetoed / follow-up | **2026-04-07 / May** | UNSC query |
| Iran–Oman/UN stranded-ships corridor; Iran–Oman temporary route | **6/24; 8/26** | corridor query |
| Kharg strikes / "may take over Kharg" | **3/13, 4/07, ~9/05; 7/08** | Kharg query; nothing in-window |
| Oman–Iran FM calls surfaced | **2026-03-01; 2025-12-30** | not the reported 10/13–14 call |
| Wire vocabulary "June interim ceasefire crumbled/collapsed" (Reuters 10/12, 10/14) | the **mid-June Islamabad MOU**: Iran repudiation 7/13, expiry 8/17 (Wikipedia gives "collapsed 8 July") | ADD#20: not carried as "ceasefire"; collapse date not adjudicated |
| hngn 10/13 "Iran … pushes own Oman corridor … close to implementation" | flagged source | not carried |

## §9 What changed since 10/08 (one paragraph)

No US or Israeli strike on Iranian territory was found for 10/08–10/14 (search- and tracker-based; CENTCOM 403). On 10/08 Trump pledged no attack before the 11/3 midterms and said the blockade stays in "full force". By 10/13 he was saying "a decision on Iran very soon", and Axios reported (anonymous, White House-disputed) that he told Netanyahu to prepare for a possible operation, with no commitment. So the 10/07 "conclude preparations" report has produced no decision, date or execution. The blockade is confirmed as policy reinstated **7/14** (CENTCOM, relayed). Its one in-window kinetic event was the 10/10 disabling of *Ocean Molica*; the tally is 4 disabled, 135 turned back and 10 tankers destroyed. CENTCOM on 10/14 disclosed a 10/06 dhow destruction and issued a "no navy / 19 mb" fact check. Diplomacy moved from "Iran's initial position via Qatar" (10/04) to a two-track Iranian line. On 10/11 Rezaei said the US reply accepted "some" of Iran's seven conditions but is "INADEQUATE", and Iran will not reopen or negotiate until all are met; per Iran, the US rejected Iran–Oman joint management. On 10/12 Baghaei said Iran is "still reviewing" and will reply via intermediaries, so the exchange is stalled but not closed. Both are Iranian accounts; there is no US accept/reject statement, and no talks are scheduled. Oman and Pakistan conferred in Islamabad on 10/14 about "creating space" for US–Iran dialogue, with no date or instrument. **Ladder #5 is NOT FIRED**: no dated framework, the Iran–Oman coordinates are still undated and unconfirmed by Oman's own feed, and there is no withdrawal instrument. **Ladder #7 is NOT FIRED**: Mojtaba issued only a written 10/08 Police Week statement. For FALCON, C→B is unmet (no dated framework) and D→C is unmet (two-sided kinetic events every day 10/10–10/14). New Iranian signalling is declaratory and attributed. In the Reuters 10/14 piece, two anonymous officials claim an election-timed, highest-level tactic shift, "complete closure soon" and wider geography. WSJ reported back-channel threats via mediators to hit US forces and Saudi oil. The IRGC Navy commander threatened to "sink" US warships. Outside Iran, the 10/12 State Dept joint statement of 30 governments recognized the UK's attribution of the 9/27 RAF Fairford plot to Iran. That updates the 10/08 "no UK Iran link" baseline. The UN fertilizer plan shows no movement beyond the 10/14 conditional warning.
