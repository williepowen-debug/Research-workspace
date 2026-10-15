# FALCON — catch-up 10/10→10/14 · 7-day scenario review · GATE-FALCON-001 review · loss census · casualty ratchet

**Session:** 2026-10-14 ~21:23 ET → (Wed). Will-launched boot (*"please boot up. We need to catch up on recent news"*); PROME (`prome-8e`) messaged at ~21:35 ET naming the three owed reviews and three owner calls. Runtime: Claude Code, model Opus (`claude-opus-5-5`), desktop. Inputs: 16 WALTER handoffs (10/11–10/14, all consumed), WALTER's full re-verify (`AGENTS/WALTER/research/2026-10-14_iran-full-sweep/`), my own instrument runs (PortWatch transit + bypass, TankerMap JSON bars, NASA FIRMS 40-day pull), and two Opus helpers (independent day-by-day news sweep; war-risk re-pull). Prior read: 10/10 (`falcon-1010b`).

## Decision read

> ⚖️ **RULED 2026-10-14 22:01 ET** (Will in the PROME session, verbatim *"Approve 431, 432 and 433"*; record `PROME/proposals/2026-10-14_wq431-433-RULED.md`): **WQ-431** class-(ii) re-mark = HOLD · **WQ-432** leg 2 KEPT PROVISIONAL + amendments ① ④ as §5.2 (encoded in `domain/FRESH_LEG_BASELINE.md`) · **WQ-433** FAL-06 dated-search text as §7 (encoded on the row). ➕ Abqaiq geometry added after the memo: KB-293 (heat on the processing facility's two mapped flare stacks).

**The marks hold at B 1 / C 14 / D 85, but two things lit that did not exist on 10/10: two more ships are total losses (both non-tankers), and the casualty ratchet is RED.** Neither moves a mark by its letter. The production rung (D 85→92) did not fire: the only in-class candidate (Abqaiq, 10/08) has real satellite heat behind it and no counting source.

| Item | Verdict | Basis (dated) |
|---|---|---|
| 7-day scenario review (due 10/14) | **HELD B 1 / C 14 / D 85** | D→C needs a 72h two-sided halt — hulls struck 10/09, 10/10, 10/11, 10/13, 10/14 ⇒ unmet. C→B needs a DATED framework — Iran says it has stopped responding (Rezaei 10/11), Oman–Pakistan met 10/14 with no date ⇒ unmet. Above 85 only the production rung is registered, not fired |
| Production rung D 85→92 | **ARMED, NOT FIRED** | Dhahran 10/13 = an office (OUT); Abqaiq 10/08 = own FIRMS anomaly + claims, no counting source; Haradh 10/13 = intercepted; Shedgum/Hawiyah/Tanajib = gas plants (OUT), claims only (§3) |
| Ship losses (`VX-FALCON-SUNK-01`) | **3 → 5: two CLASS-(ii) total losses** — GFS PRIDE (container ship, sank 10/13, MPA + IMO) and CAPE DAO (bulker, struck 9/23, IMO "Sunk" as at 10/14) | Letter: class (ii) ⇒ convergence input + **same-day re-mark proposal to PROME** — sent; **FALCON recommends HOLD** (§2). Not tankers ⇒ the EXIT §5 "third class-(iii)" trigger does not fire |
| Casualty ratchet (EXIT §3 #5) | **🔴 RED rate-step LIT · 🟠 ORANGE (i) LIT** — killed 21 vs 6 (3.5×); injured 376 vs 151 | GACA: KKIA 10/10 12 killed / 309 injured (+1 Indian Embassy), 10/11 1 killed / 11 injured. An indicator ⇒ EXIT §3 goes **7 of 8** limbs lit; no mark move (§4) |
| GATE-FALCON-001 (review_by 10/14) | **Leg 2 NOT FIRED; event override NOT TRIGGERED; gate LIVE** | TankerMap completed UTC days 10/08–10/14: none qualified (10/14: `100×71 = 7,100` vs `65×76 = 4,940`); no Houthi act on shipping found (§5). Next review_by **2026-10-21** |
| DOCKET L619 (leg-2 provisional letter) | **Recommend KEEP PROVISIONAL**, plus the vintage rule as an R1 amendment | §5.2 |
| FAL-06 (70%, to 11/05) | **OPEN, no route fired** | no force majeure; no stated production offline; IEA September Gulf crude exports +4.4 mb/d m/m (a recovery print) |
| Thesis-kill (EXIT §1) | **0/7** | unchanged |
| War-risk (WARRISK.tsv) | **1 of 5 legs re-pulled** (Hormuz 6–10%, FT brokers ~10/06); the registered falsifier (WC Saudi ~3%) has no newer quote | data clock NOT advanced (§6) |

## 1. What happened, 10/10 → 10/14 (graded)

| Date (UTC unless noted) | Event | Source class | Grade |
|---|---|---|---|
| 10/08 day, 09:05–12:10Z | **Heat anomaly at Abqaiq's flare point** — own FIRMS, 24 detections / 4 sensors, max 62 MW, day-sum 626 MW (40-day median 6.3); out by 22:08Z. Same date: Soar Atlas imagery (Newsquawk 09:07Z), Tasnim "massive fire", YPA "two fires… fuel storage tank" | own FIRMS + claimant/imagery | IN-class site, **no counting source** ⇒ rung NOT FIRED (KB-280) |
| 10/10 ~12:00Z | **KKIA (Riyadh airport) strike: 12 killed, 309 injured (GACA)**; 13th death 10/11 (Indian Embassy) | state | airport OUT; ratchet input (CAS-026/027) |
| 10/10 1920Z | UKMTO 162-26: outbound tanker struck, fire (VALTHERA, INFERRED) | UKMTO | hull, afloat (VI-0060) |
| 10/10 | CENTCOM: US jet disabled OCEAN MOLICA, Gulf of Oman (blockade) | CENTCOM | US action (VI-0066) |
| 10/11 | Six UKMTO attack warnings incl. 164-26 (E of Musandam, damage) and 168-26 (products tanker) | UKMTO | hulls afloat (VI-0061/0063; others not rowed) |
| 10/11 | **PETRO DOLPHIN hit by a drone AT Sohar anchorage, Oman; 2 of 11 Indian crew missing** | UKMTO + India MoS | first hull hit inside a GCC anchorage since 9/28 (the spent rung's trigger (c) class) — record only (VI-0062, CAS-029) |
| 10/11 | KKIA Terminal 4 hit: 1 killed, 11 injured; KFIA Dammam attacked | GACA | airports OUT (CAS-028) |
| 10/11 | Rezaei: US reply to Iran's 7 conditions "insufficient"; Iran "no longer… responding" | Iranian state media | no framework (KB-284) |
| 10/11 | Hawiyah gas plant heat spike (196 MW, MODIS 16:50Z); Saree claims Shedgum + "Tanajib oil facility" | own FIRMS + claim | gas plants OUT (KB-282) |
| 10/13 (SGT) | **GFS PRIDE sank in the Strait of Hormuz** after an "unknown projectile"; 21 crew safe (MPA); IRGC mine claim names no ship | flag state + IMO | **class-(ii) total loss** (KB-276, VI-0064) |
| 10/13 | **Aramco Dhahran administrative building / HQ tower hit** — MoE "limited fire", 0 casualties; Reuters sources "extensive damage" | state + wire | office OUT (KB-279) |
| 10/13 | BMs toward Dhahran and **Haradh** (southern Ghawar) intercepted (coalition); Riyadh debris 4 injured | coalition | intercepted ≠ struck (KB-281, CAS-030) |
| 10/14 | IMO table marks **CAPE DAO "Sunk"** (struck 9/23); GFS GISELLE struck, safe anchorage | IMO, MPA | **class-(ii) total loss** (KB-277, VI-0036/0065) |
| 10/14 | Houthi Saba "military source": Aramco shareholders should "dispose of their shares" | claimant | threat statement (KB-285) |
| 10/14 | IEA OMR: September Gulf crude exports 13.9 mb/d (+4.4 m/m) | institution | FAL-06 context, BRENT's (KB-288) |
| 10/08–10/14 | No US or Israeli strike on Iranian territory found; Red Sea: no Houthi act on shipping found | search-based | US-kinetic vector unchanged; Bab override not triggered |

*Independent sweep verification: see §8.*

## 2. Ship losses — the census, and the class-(ii) proposal (owner call ①)

**Four instruments, four sets — never added (KB-277):**

*Verified at the primary 10/15 01:55Z (own fetch of the IMO table; KB-291).*

| Instrument | What it counts | Members |
|---|---|---|
| FALCON `VX-FALCON-SUNK-01` | hostile-action total losses, all attackers, since spinout (7/12) | dhow Faize Noore Oliya 8/4 (i) · Kylo 9/5 (iii-B, US) · Riesco 9/8 (iii-B, US) · **CAPE DAO** (ii; IMO basis, sinking date unstated) · **GFS PRIDE 10/13** (ii) ⇒ **5** |
| IMO Middle East table (as at 10/14: 113 incidents, 24 seafarer deaths) | ships "Sunk" since 2/28 | SAFEEN PRESTIGE 3/4 (pre-spinout) · CAPE DAO · GFS PRIDE ⇒ 3; **no Kylo, no Riesco** (US actions on sanctioned hulls fall outside it, INFERRED) |
| UKMTO VRA overview No 10 (to 10/07) | "5 confirmed total losses YTD" | membership not published |
| CENTCOM | "10 tankers destroyed since 7/14" | "destroyed" ≠ sunk (9/8 lesson) |

**The letter.** `VX-FALCON-SUNK-01` class (ii) — a non-tanker SOLAS merchant total loss — carries *"convergence input + SAME-DAY re-mark proposal to PROME."* There is no registered rung on class (ii), and the only rung above D 85 is the production rung. **Proposal (Will's word, via PROME): HOLD B 1 / C 14 / D 85.** Reasons:
1. **D 85 already prices sinkings.** D-indicator #6 (vessel sunk) fired 9/5; the D scenario's own definition names "vessel sunk" as a hard gate already tested.
2. **The class is now the regime, not a step out of it.** Two class-(ii) losses in 21 days (Cape Dao struck 9/23, GFS PRIDE 10/13). An event that recurs at that rate cannot be a step-change signal at D 85; a rung keyed to it would fire repeatedly. (Contrast the production rung: two episodes in 7 months.)
3. **Both losses are attacker-UNATTRIBUTED** (MPA "unknown projectile"; the IRGC mine claim names no ship), so neither carries the attribution a step move would rest on.
4. **What WOULD justify a move** is outside this event: a counting-source production hit (registered → 92), or a (iii-A) tanker loss (its D 75→85 rung is spent; a new rung would need registration with a base rate).

⚠️ **Disclosed, so it is not lost in the HOLD:** the escalation this week is real and one-directional: container ships are now being hit, two GFS (Dubai) box ships in two days (operator concentration, INFERRED identity), a hull hit inside an Omani anchorage, a missile on Aramco's headquarters, and the deadliest strike on Saudi soil in this war. The convergence matrix (43/50, 7 vectors at ceiling) cannot register any of it. **The marks are a rail cap, not a judgment that nothing changed.**

## 3. Production rung D 85→92 (owner call ③ — Abqaiq)

| Candidate | Facility class (EXIT §2a) | Counting source? | Grade |
|---|---|---|---|
| **Abqaiq 10/08** | crude stabilisation = **IN** | **None** (imagery, Tasnim, YPA = never count; no Saudi/Aramco/coalition/named-wire word found by WALTER through 10/14) | **NOT FIRED** |
| Dhahran 10/13 | office = OUT | MoE confirms the hit | NOT FIRED by class |
| Haradh 10/13 | production locality, target unnamed | coalition: **intercepted** | NOT FIRED (no strike) |
| Shedgum 10/09→, Hawiyah 10/11 | gas plants = OUT | none | NOT FIRED by class |
| Tanajib (Saree 10/11) | gas plant (Aramco 2/26 primary) = OUT | none | NOT FIRED |

**Abqaiq, what the heat does and does not say.** Own FIRMS, 40 days (9/05–10/14): the routine flare point at 25.9305N 49.7003E detected on 39 days, median day-sum 6.3 MW. On **10/08 daytime** it showed **24 detections across four sensors between 09:05Z and 12:10Z, max pixel 62.1 MW, day-sum 626.5 MW** — the largest day in the window by about 6× (next: 9/26 at 99.9 MW). By the 22:08Z night pass it was back to 1.4 MW. **A single high pixel is not unique there (three days >10 MW in 40); a three-hour, four-sensor event is.** The Soar Atlas imagery claim hit Newsquawk at 09:07Z, two minutes after my first detection. **What it establishes:** something burned or flared hard at the Abqaiq flare point for at least three hours on 10/08. **What it cannot establish:** cause (a process-upset flaring surge fits as well as a fire), facility (YPA says "fuel storage tank", which would be OUT class even if confirmed), or damage. **It cannot fire the rung by letter.** Evidence: `domain/firms/2026-10-14_FIRMS_own-pull_ghawar-abqaiq-recheck.csv`.

**Ghawar follow-up (the 10/10 standing test):** Shedgum's max pixel fell 139 → 93 → 35 → 33 → 12 MW (10/10→10/14; pre-fire 4–9). The Ain Dar GOSP1-area upstream heat fell 144 → 36 → 16 → 34 → **dark** over the same days. **The upstream heat faded with the gas-plant fire, which is what the GOSP-flaring inference predicted** (crude still flowing, associated gas flared while Shedgum was down). Consistent, not proof; FIRMS cannot exclude GOSP hits.

## 4. Casualty ratchet (owner call ②)

Recomputed **from `domain/casualties/CASUALTIES.tsv`** (script, not prose), windows ending 2026-10-14; CAS-025's 10/10 counts superseded by CAS-026 (GACA):

| Window | Killed | Rows | Injured |
|---|---:|---|---:|
| 9/15–10/14 | **21** | Cape Dao 1 · airports 10/07 3 · KKIA 10/08 3 · KKIA 10/10 12 (GACA) + 1 (Indian Embassy) · KKIA T4 10/11 1 | **376** |
| 8/16–9/14 | **6** | Sirik 5 (contested) · Hercules Star 1 | **151** |

**RED rate-step: 21 ≥ 2×6 and ≥ 5 ⇒ LIT** (excluding contested Sirik: 21 vs 1; GACA-only: 20 vs 6 — lit on every count). **ORANGE (i): 376 ≥ 2×151 ⇒ LIT** (soft edge: Sirik's "~70" injured; it would fail only at ≥ ~107). **Class-step: UNFIRED** — no US, GCC-military or coalition death. ⚠️ [10/14 self-catch] the "no US death since 6/27" baseline is FALSE — 2 US service members KILLED in Jordan 7/17 (CENTCOM; CAS-2026-032, KB-294); the MILITARY_US class-step is AMBIGUOUS on the letter, routed to PROME/Will; interim: a US death on/after 9/8 = RED class-step. **Consequence by letter (`domain/CASUALTY_RATCHET.md`):** an INDICATOR feeding EXIT §3 #5 ⇒ **EXIT §3 lit limbs 6 → 7 of 8**; no mark moves. PETRO DOLPHIN's 2 missing are not counted until confirmed dead; ACERS (158-26) casualties still have no published count.

**Forward behaviour (computed from the ledger, assuming no new deaths or injuries after 10/14):** RED stays lit until about **11/08** (one-day flicker off on 11/07: 14 vs 8). On **11/09** the 10/10 KKIA strike leaves the current window and enters the comparison window: killed 1 vs 20, injured 18 vs 366, so both bands go dark. For the following ~30 days, relighting would need **≥40 confirmed deaths in a 30-day window**. ⚠️ **Instrument property, disclosed:** a ratio of adjacent windows is LUMPY. One mass-casualty event lights it, then raises the bar for the next month. That is information for reading it, not a proposal to change it.

**Self-catch (10/14, after the memo):** two US service members were KILLED in an Iranian attack on a base in Jordan on **7/17** (CENTCOM). The ledger built 9/8 lacked the row, so the letter's "zero US military deaths since 6/27" is false. The MILITARY_US class-step is therefore **ambiguous** (consumed 7/17, or re-anchored to 9/8 by its bracket). Routed to PROME/Will; the interim reading, chosen to fail loud, is that a US death on/after 9/8 = RED class-step. CAS-2026-032, KB-294. Today's rate-step grade is unaffected.

## 5. GATE-FALCON-001 — the 10/14 review

### 5.1 Grade

Own TankerMap read 2026-10-15 01:27Z (JSON daily bars; sourceWatermark 00:33:37Z; coverage 92.2%); saved `domain/tankermap/2026-10-14_bab_daily_bars.csv`.

| UTC day | 7-day total | prior-7 | `100×cur` vs `65×ref` | Qualifies? |
|---|---:|---:|---|---|
| 10/08 | 73 | 80 | 7,300 vs 5,200 | no |
| 10/09 | 74 | 80 | 7,400 vs 5,200 | no |
| 10/10 | 77 | 80 | 7,700 vs 5,200 | no |
| 10/11 | 72 | 75 | 7,200 vs 4,875 | no |
| 10/12 | 77 | 71 | 7,700 vs 4,615 | no |
| 10/13 | 79 | 70 | 7,900 vs 4,550 | no |
| 10/14 | 71 | 76 | 7,100 vs 4,940 | no |

**Leg 2 NOT FIRED** (no completed day qualified ⇒ no run open; R1 satisfied by read-back; 10/15 partial ⇒ not a print-day). 7dma ~10/day, flat. **Leg 1 FIRED 7/23 and leg 3 FIRED 8/15 stand. Event override NOT TRIGGERED:** no Houthi maritime attack, boarding, toll or executed restriction found 10/08–10/14; Houthi fire went at Saudi land targets. **Gate LIVE. Next review_by 2026-10-21** (owner-set; weekly tanker cadence; Bab is still not where the escalation is).

### 5.2 DOCKET L619 — keep provisional · re-fit · retire: **recommend KEEP PROVISIONAL**

1. **It grades cleanly.** Three reviews on the letter (10/01, 10/07, 10/14) produced unambiguous integer verdicts from the vendor's own daily bars, with no UNGRADEABLE episode.
2. **Re-fit has nothing new to fit to.** The bar was fitted to n=1 (the 7/22 embargo); the 10/07 backtest found it also catches April (Petroline derating, excluded by the clause) and late August (AMZAN hit + Yanbu collapse). No new positive has arrived since. A re-fit now would re-fit the same sample.
3. **Retiring it removes the only quantitative Bab execution tripwire** while the Houthis are at war with Saudi Arabia on land and still hold Hanish and the coast near Mokha. ⚠️ Perim/Mayyun — the geography that makes enforcement executable — was **reportedly retaken by Yemeni government-aligned forces on 10/09** (CTP-ISW; anti-Houthi sources + geolocated footage, no wire), so the precursor is weaker than on 9/14; the recommendation does not rest on it.
4. **The live risk is the confound, and the letter already names it:** Bab tanker counts now ride Saudi Red Sea loadings (~10/day since the Yanbu restart), so the next fall will most likely be loadings-driven ⇒ the exclusion clause does the work.

**Two amendments proposed with it (DAEDALUS 10/08 asks ① and ④, deferred to today; prospective; Will's word via PROME):**
- **① Vintage rule (into R1):** *"Grade COMPLETED UTC print-days only, on the vendor's CURRENT vintage at the grading read. When a live read and a read-back differ, the read-back wins; save both."* (Practice since 10/07. **Against DAEDALUS's "grade as first read":** the vendor revises upward — 10/07's total went 72 → 76 across vintages — so a first read biases toward a false step-DOWN; current vintage fails in the safe direction.)
- **④ Letter clarifications (record-only for two fired legs):** (a) *post-fire:* "the gate fires on ANY leg; a fired leg stays FIRED and the gate stays LIVE so unfired legs keep grading; a second leg firing is a new adjudication, never a re-fire"; (b) *"declared zone"* — leg 1 is FIRED and cannot re-fire, so the definition is moot for gate state; **define it only if leg 1 is ever re-armed** (writing a geography now would be a new threshold with no live use); (c) *leg-3 dating* — add "dated on the first week for which ≥2 dark-fleet-capable trackers agree at or below the bar; a single-tracker print is a watch" (this matches how the 8/15 fire was actually dated; leg 3 is fired, so state is unaffected).

## 6. War-risk re-pull (registered falsifier expired)

Helper re-pull 10/14 (report kept in the session scratchpad): **Hormuz 6–10% of hull value** (FT, unnamed brokers, ~10/06; read via Marine Insight 10/08 / TradeWinds 10/07 / Insurance Business 10/14; FT original not reachable) — top +1 pt, back to the July Marsh ceiling, **quoted before the 10/11–10/13 run, so it may lag**. **WC Saudi (registered falsifier), Southern Red Sea, spread: SEARCH-NOT-FOUND** — and their quote date is corrected **9/25 → 9/24** (Reuters original 9/24 18:40). **Bab:** a "~3%" figure (Sourcing Journal 10/14) with no unit and a population conflict (Reuters 0.2–0.3% for non-Saudi transits) — not adopted. **JWC:** no change (JWLA-035, 16 Sep). **Data clock NOT advanced** — a fresh file clock over an expired falsifier is the false-green the per-row check exists to prevent.

## 7. Other owed items answered here

- **DAEDALUS ② FAL-06 dated search floor/ceiling (WQ-172 form), proposed prospectively, before 11/05:** *"A CONFIRMED resolution requires a dated search attempt INSIDE the window, run on 2026-11-05 (floor = ceiling = the resolve date): operator/state force-majeure notices and production statements (Aramco/Tadawul, MoE/SPA, ADNOC/WAM, KPC/KOC/KUNA, QatarEnergy/QNA, BNA, ONA) and the latest Kpler/Vortexa weekly aggregate export print per Gulf-ally country available that day (vendor lag stated in the resolution). An attempt after 11/05 = NO-VERDICT. The search limb grades the world-state only."*
- **DAEDALUS wiring ⑰ (VX IRAN-02 bands vs instrument): DONE** — the row now names one instrument (PortWatch total transits/day via `hormuz_transit_watch.py`), the four canonical bands sit in the band columns, the UKMTO-tanker text is labelled legacy. No boundary moved.
- **DAEDALUS brief-pin wiring (10/14): DONE** — `CLAUDE.md` step 14 names `scripts/brief_pin_check.py`.
- **Corrections:** COR-20261012-04 (August copy displayed as October — false-fire register row ⑦), COR-20261012-09 (UKMTO/IMO identities — VESSELS), COR-20261014-31 (IMO three sunk — census) **all APPLIED**; check PASS.

## 8. Independent sweep verification

Independent day-by-day helper sweep (Opus, 10/10–10/15 UTC; SPA/UKMTO/Reuters/Bloomberg/ISW originals blocked, quoted via named carriers):

- **Confirmed as WALTER stated:** GACA 12 killed / 309 injured (10/10) — the **13th death is the Indian Embassy's, not GACA's**; 10/11 KKIA 1 killed (Pakistani) / 11 injured; Haradh interception; PETRO DOLPHIN + VALTHERA (India MoS); Rezaei, Baghaei, Trump statements; UKMTO numbers it could see; Bloomberg on Fujairah. Oman–Pakistan 10/14 meeting **not confirmed**.
- **Corrections applied:** Dammam had **two** events (10/10 projectile near KFIA per coalition; 10/11 GACA-confirmed attack). Dhahran: ISW says unclaimed on 10/13; Saree claimed it 10/14. **"Operations/production continuing" at Aramco is not verified at an Aramco or Saudi primary** (KB-279 corrected).
- **One helper correction REJECTED at the primary:** it relayed Reuters/JPost 10/14 (*"the second vessel to sink"*) and found no Cape Dao sinking. **My own fetch of the IMO table (as at 14 Oct: 113 incidents, 24 fatalities) reads, verbatim: CAPE DAO (IMO 9219020) "Damaged. No pollution. One seafarer fatality. Sunk."** — the Reuters copy predates the IMO update. Census 5 stands (KB-291). The same fetch named six more hulls (VI-0067..0072, incl. AL SAADIYAT 10/13, not in any routing) and 3 more mariner injuries (CAS-031).
- **New, none fires a letter (KB-292):** Perim reportedly retaken by government forces 10/09 (claim-only) · Supreme Leader still no verified appearance · Netanyahu 10/14: no pre-emptive strike before Israel's 10/27 election · Trump: considering strikes on the Houthis; "promised" to stop killing Iranian officials · coalition struck Houthi fuel sites 10/13 · Iran threatening cables/data centres and UAE digital/energy targets (threats only; cyber vector stays 2) · Kpler Hormuz exports 8.5 mb/d week to 10/12 (weekly rate — never blend with daily barrel counts) · CENTCOM destroyed an Iran-affiliated surveillance dhow 10/06 (released 10/14) · Sirik fishing boat drone 10/14 (3 injured; "US" = local sources) · Saudi air-defence failure probe; KKIA closed to ~10/17 · US weighing shadow-fleet sanctions easing (Reuters, early 10/15).

## 9. Limits that travel

- UKMTO primaries mostly 403 from this box; hull identities are INFERRED unless UKMTO/IMO/MPA named them. UKMTO 161, 163, 165–167, 169–173-26 are not individually rowed — **absence of a row is not absence of an incident.**
- GACA counts are taken from WALTER's sourced relay (§6 of its leg-B file), checked by my helper (§8).
- FIRMS is heat only. The Abqaiq anomaly is physical, not counting.
- Safeen Prestige (IMO, 3/4) is pre-spinout and was not checked against HAWK's frozen record this session — **owed before anyone states that FALCON's census covers the whole war.**
- No prices re-pulled (BRENT's). No trade, no capital grade (WQ-192 holds).
