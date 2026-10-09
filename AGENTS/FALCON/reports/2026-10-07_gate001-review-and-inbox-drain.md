# FALCON — GATE-FALCON-001 review (owner-set review_by 10/06, graded 10/07) + whole-inbox L0 drain

**Session:** 2026-10-07 ~21:41–22:5x ET (Wed). PROME-spawned (`prome-0e`), WQ-184 Tier-1 due-row wake: `PROME/GATES.tsv` `GATE-FALCON-001` passed its owner-set `review_by` 2026-10-06 with no grade. Runtime: Claude Code, model Opus (`claude-opus-5-5`, per the `desk` agent definition), laptop host, sole live FALCON writer (WQ-387). Watch-only gate: no capital path, no auto state change; any threshold move stays Will-gated. Two read-only Opus helpers were used for wire sweeps (UKMTO 151–158 reconciliation; Bab/Red Sea + Saudi energy claims); their facts are marked where used and were spot-checked against fetched pages.

## Decision read

**Nothing fires. B 1 / C 14 / D 85 HELD; no pre-committed resolver fired. Losses stay 3.**

| Item | Verdict | Basis (dated) |
|---|---|---|
| GATE-FALCON-001 leg 1 | **FIRED 7/23 — stands** | a fired leg does not un-fire |
| GATE-FALCON-001 leg 2 | **NOT FIRED** | TankerMap 10/07 (completed UTC day): 7-day total 72 vs prior-7 69, +4%; `100×72 = 7,200` vs `65×69 = 4,485` ⇒ NOT MET. No completed UTC day 10/02–10/07 qualified (w/w +122% → +4%); no run open |
| GATE-FALCON-001 leg 3 | **FIRED 8/15 — stands** | cannot re-fire |
| Event override (Bab enforcement since 10/04) | **NOT TRIGGERED** — no Houthi enforcement act on shipping 10/04–10/07 | §2 |
| Gate state | **LIVE** (2 of 3 legs fired) | FALCON adjudicates, PROME flips |
| Next owner-set review_by | **2026-10-14** | weekly tanker cadence; event override unchanged |
| Production rung D 85→92 | **ARMED, NOT FIRED** | Khurais: no counting source confirms both a hostile strike and an IN-class facility (§3) |
| FAL-06 (70%, to 11/05) | **OPEN, no route fired** | no force majeure; no stated production offline; no vendor aggregate-export print ≥20% down |
| 7-day scenario review (due 10/08) | **Run one day early: HELD** | D→C needs a 72h two-sided halt (hulls hit 10/04, 10/05, 10/07); C→B needs a dated framework (none found); above 85 only the production rung is registered (not fired) |

## 1. Leg 2 at the letter (WQ-353 PROVISIONAL)

**Instrument.** Own TankerMap read at 2026-10-08 01:45Z (= 10/07 21:45 ET). The public page `/analytics/straits/bab-el-mandeb` shows 7-Day Avg/Day **10.3**, 7-day total **72**, vs Prev 7d **+4%**, 14 in zone, latest sighting 2026-10-07 23:29. The page's chart is fed by a JSON endpoint (`/api/analytics/chokepoints?chokepoint=bab-el-mandeb`, methodology `bab-el-mandeb-transit-v5`, watermark 2026-10-08T01:16Z). **I saved the full daily series** (`domain/tankermap/2026-10-07_bab_daily_bars.csv`, 2026-03-10 → 10-08), which makes R1 read-backs possible for the first time.

**Every completed UTC print-day since the last read (current vintage):**

| UTC day | day total | 7-day total | prior-7 (reference) | w/w | `100×cur` vs `65×ref` | Qualifies? |
|---|---:|---:|---:|---:|---|---|
| 10/02 | 8 | 80 | 36 | +122% | 8,000 vs 2,340 | no |
| 10/03 | 8 | 80 | 39 | +105% | 8,000 vs 2,535 | no |
| 10/04 | 12 | 75 | 51 | +47% | 7,500 vs 3,315 | no |
| 10/05 | 10 | 71 | 61 | +16% | 7,100 vs 3,965 | no |
| 10/06 | 11 | 70 | 68 | +3% | 7,000 vs 4,420 | no |
| 10/07 | 10 | 72 | 69 | +4% | 7,200 vs 4,485 | **no** |
| 10/08 | 0 | — | — | — | partial UTC day at fetch | not a print-day |

- The 7-day mean came off its 10/01–10/03 high (11.4 → 10.0 on 10/06 → 10.3 on 10/07); w/w stays positive because the reference window now contains the Yanbu-restart surge (9/27–10/01: 17, 14, 12, 8, 13).
- The page's briefing sentence "only 3 tanker transits … 44% below the preceding 7-day average" matches no daily bar since 9/24 and is the same sentence PROME's 10/03 reader saw ⇒ **UNKNOWN (static text)**; one day never grades the leg.
- **R1 (missed reads)** is satisfied by read-back: every day 10/02–10/06 was read back from the daily bars, none qualified, so no episode is UNGRADEABLE.
- **Exclusion clause, forward:** the next fall will very likely coincide with Saudi Red Sea loadings normalising after the restart (minister 10/06: the line "is operational now", KB-248). By the letter that fall is **not enforcement-attributable unless a Houthi enforcement act on a hull falls in the window.**
- **What a fire needs from here:** a 7-day total ≤ ~46 (0.65 × the ~72 reference) on two consecutive completed UTC days, plus attribution.

**R3 — out-of-sample evidence the letter did not have (not a fire).** Backtesting the provisional magnitude + sustain rule (floor 21; attribution not applied) on TankerMap's current-vintage series 3/10–10/07 finds **three** sustained qualifying runs, not one:

| Run | Depth | Known context | Attribution (owner judgment, ungraded) |
|---|---|---|---|
| 4/13–4/17 | −37% to −56% | April 2026 Petroline one-station derating | exclusion clause plausibly applies |
| 7/26–8/02 | −49% to −96% | 7/22 Houthi Saudi-hull embargo | **the known positive** |
| 8/31–9/02 | −37% to −57% | Houthi-attributed hit on AMZAN 8/24 (~63 nm W of Yanbu, VI-2026-0032) inside the reference window; leg-3 Yanbu loadings collapse | attributable on the hull act if the window is read that way |

Single qualifying days 3/30 and 9/05 were not sustained. R3 recorded the 35% bar as fitted to one positive on PortWatch with the unattributed war episodes excluded; **on the grading series it also catches April and late August.** This is evidence for the provisional review, routed to PROME; it moves no threshold (Will-gated). ⚠️ **Vintage:** the vendor revises recent days after the fact (my 9/28 live read gave a 7-day total of 38; the current vintage sums 9/22–9/28 to 61; PROME's 10/03 read of 87 is now 80). A read taken before a UTC day completes undercounts it, which biases a live read toward a step-DOWN. Proposed residue line for the letter's owner record (no letter change made): *grade completed UTC days only; a read-back uses the current vintage, not the as-first-published value.* `KB-FALCON-244/245`.

## 2. Event override — Bab-theater enforcement since 10/04

**Verdict: NOT TRIGGERED.** The override names *any Bab-theater ENFORCEMENT event* (an interdiction, a toll actually levied, a transit restriction executed, or a hull attacked in the zone). Swept 10/04 → 10/07 ~22:00Z (read-only Opus helper, fetched pages; spot-checked):

| Date (UTC) | Item | Class | Why it does or does not trip the override |
|---|---|---|---|
| 10/04 ~1650Z | **UKMTO WARNING 151-26**: multiple explosions close to a products tanker ~60 nm S of Al Mukha, one airburst ~100 m off the starboard side; no damage, crew safe, voyage continued. Vessel per Vanguard Tech: **CHRYSTAL SKY** (73,976 dwt, Marshall Islands flag, Executive Ship Management, Sikka → Barcelona; UAE-linked owner/operator on Equasis, **not Saudi-linked**). UKMTO classed it "suspicious activity" | an ACT (near-miss) confirmed by UKMTO/vendors; **attacker UNCLAIMED** | No hull hit, no Houthi claim or attribution, not a Saudi-linked hull — not an enforcement act on the record. Logged VI-2026-0046 (name + number added) |
| 10/04–10/07 | Houthi (Saree / Al-Masirah / Saba) maritime claims | SEARCH-NOT-FOUND | every Saree statement in the window names LAND targets (Aramco Riyadh/Khurais 10/04, Rabigh 10/05, airports/bases 10/06–10/07, Aden) |
| 10/04–10/07 | Boarding, seizure, toll levied, executed transit restriction | SEARCH-NOT-FOUND | the late-September "passage safe except the Saudi enemy" line is a RESTATED ban (7/22), a declaration |
| 10/04–10/07 | Territory: government "Operation Dawn of Yemen" claims Bab al-Mandab "secured", Mokha retaken, Dhubab airstrip taken (10/05); its own sources to Reuters say Mokha's outskirts only; Houthis deny; Perim/Mayun "besieged", no change of hands; fighting inland at al-Waziiya 10/07 | territorial/military, both sides CLAIM | **Territory is not enforcement** (same class as Mokha/Perim/Hanish in September, graded at KB-163/171/182). A government recapture would LOWER the leg-2 prior; it is not confirmed |
| 10/05 | Coalition strikes on Houthi Hodeidah sites holding explosive boats and sea mines | coalition act AGAINST Houthi maritime capability | not a Houthi enforcement act |
| traffic | Lloyd's List Intelligence: Bab el-Mandeb 290 all-vessel transits 9/21–27 (264 the week before) | different object (all vessels, LLI perimeter) | context only — never blended into the TankerMap tanker basis |

⚠️ **Coverage limit:** UKMTO, JMIC, Ambrey and MSCHOA are 403 or unindexed from this desk; Saree's Telegram was not read directly. A Houthi maritime claim made only on Telegram after ~10/07 12Z could be missed. UKMTO 152–158-26 are Hormuz/Gulf (§5). Event override **unchanged** for the next window: review IMMEDIATELY on any Bab-theater enforcement event.

## 3. Khurais (SIG-W-20261004-010 follow-up) — production rung NOT FIRED; the facility question has two non-counting answers

**Heat (own FIRMS, `domain/firms/2026-10-07_FIRMS_own-pull_khurais-spot-persistence.csv`):** the source at 25.252N 48.103E burned on every pass from 10/03 22:01Z through the 10/07 night passes. Daily max FRP: 10/04 229.4 MW · 10/05 424.5 MW · **10/06 504.6 MW** (MODIS 16:52Z) · 10/07 234.1 MW; VIIRS night passes 10/05–10/07 carry 13–30 detections each. Four days continuous, peak 10/06, easing 10/07. It exceeds every maximum in this desk's FIRMS files. Heat only; it never counts.

**What the sources say since 10/04** (`KB-FALCON-247/248`):

| Source | Class under §2a | What it says |
|---|---|---|
| AFP 10/05, **one unnamed** Saudi energy-sector source | named wire, but 1 unnamed source < the "named official OR ≥2 independent industry sources" bar ⇒ **does not count** | attacked again 10/04 at a **PUMP STATION in the Khurais area** east of Riyadh, "never targeted before"; "big damage and the pipeline stopped again" |
| Bloomberg 10/05, people familiar | does not confirm a strike | oil continues to flow; dismissed the reports of extensive damage and a halt; line >80% of capacity late the prior week |
| Reuters 10/05, a source | does not confirm a strike | flows not interrupted |
| Energy Minister Abdulaziz bin Salman, Manama 10/06 | state; **does not name Khurais or a facility** | "The East-West pipeline that was heavily attacked is operational now"; "5.8 million barrels" as of Tuesday morning (unit ambiguous across relays) |
| Misbar 10/06 (fact-check; Sentinel-3 + Planet) | imagery ⇒ **never counts** | smoke from "the Khurais oil processing facility", ~25.2658N 48.1081E, plumes 10/04 and 10/05, none 10/03 |
| Wikipedia, 2019 Abqaiq–Khurais attack infobox | tertiary geolocation | Khurais at 25.2647N 48.1100E — **~1.6 km from the FIRMS centroid** |
| Aramco / Tadawul / MoE / SPA / MoD / CENTCOM | counting | **SEARCH-NOT-FOUND** for any statement naming the facility or confirming a strike |

**Grade.** The rung needs a counting source confirming **both** a hostile strike **and** an IN-class facility. Neither half is met. The decisive unknown has narrowed but is not closed: **the only wire descriptor names a pumping station (OUT); the imagery and the published coordinate point at the Khurais processing facility (IN if a counting source ever says so).** ⚠️ Tension worth carrying: AFP's "never targeted before" sits badly with the same spot burning 9/10–9/11 in the MoE-confirmed attack wave (KB-177/241). **FAL-06 route (b)** would start its clock on an operator/state statement of ≥300 kbpd production offline; none exists.

## 4. Inbox drain — 14 items, every sender

Membership test by `grep -F` on `board_log.tsv` (never a read). 14 inbox items, 0 remaining; 2 BOARD_SCAN backstop rows. Each consumed file moved by `git mv` in a commit carrying `consume:FALCON`.

| Item | Sender | Disposition | Grade / where it went |
|---|---|---|---|
| SIG-W-20261002-025 | WALTER | noted | NYT (anonymous Western official): ~30 drone + ~10 anti-ship missile ATTEMPTS a week since August. "≥13 struck since 9/10" ≈ my ledger (11 rows + 4 known unrowed = 15). Attempts ≠ hits; no mark move (KB-250) |
| SIG-W-20261002-026 | WALTER | noted | Propulsion-system access on a US-bound VLCC this SUMMER (VL Prosperity class) logged as a cyber line; out of theater ⇒ cyber vector stays 2 (KB-251) |
| SIG-W-20261002-033 | WALTER | info-only | Arctic NSR diversion context; no count change |
| SIG-W-20261003-001 | WALTER | noted | Sources not preserved ⇒ CANNOT-AUTHENTICATE as sent; Riyadh refinery already adjudicated 10/04 (KB-242, OUT class); "Iran export collapse" is outside FAL-06's perimeter and unsourced; "refiner halts" unsourced |
| SIG-W-20261003-003 | WALTER | noted | Superseded by my 10/04 adjudication (Riyadh refinery heat real, cause unestablished, refinery OUT) |
| SIG-W-20261003-012 | WALTER | noted | Camp David 10/02 meeting verified at Axios by PROME's pre-fetch; carriers = positioning (KB-230); no IMMEDIATE |
| SIG-W-20261003-013 | WALTER | acted | "Abandoned VLCC still burning" = KAZIMAH III (147-26, 10/01, date wrong in the OSINT): crew EVACUATED; no sinking, CTL or tow found ⇒ losses stay 3 (VI-0042 annotated) |
| SIG-W-20261004-011 | WALTER | info-only | Iraq VLCC bypass + IEA figure (BRENT lane); Iraq outside FAL-06 ⚠️ **CORRECTED 2026-10-09 (COR-20261008-18, WALTER SIG-W-20261008-018):** the VLCC sails THROUGH Hormuz, a commercial/logistics step — not a bypass, not like the Saudi pipeline; the IEA leg holds. See the correction note at the end of this report and KB-FALCON-263 |
| SIG-W-20261005-002 | WALTER | info-only | September Gulf export recovery is an all-route estimate; consistent with "route loss, not barrel loss" |
| SIG-W-20261005-005 | WALTER | noted | Freight/TCE = BRENT lane; the insurance half is my WARRISK (9/25 quote; 10/07 re-pull SEARCH-NOT-FOUND) |
| SIG-W-20261005-006 | WALTER | noted | Will-directed tanker-cost/USO watch (`b3677b25d`): **ADOPT the shipping-security half** (VESSELS hit ledger + WARRISK are the security evidence it consumes; 158-26 off Qatar flagged as a relevant insurance event); **DECLINE freight/WTI/USO** as a FALCON instrument (charter OIL HANDOFF; BRENT/TERRY lanes). No trade, no threshold |
| SIG-W-20261007-014 | WALTER | acted | Minister's "5.8" carried as a state statement of OPERATION with an ambiguous unit; not metered flow; FAL-06 no route (KB-247/248) |
| SIG-W-20261007-015 | WALTER | acted | Rabigh 10/05: own FIRMS 126.9 MW day pass at the Petro Rabigh complex vs ≤33.5 MW baseline, fading by 10/06; Sabereen/Tasnim claims; no Aramco/Petro Rabigh/MoE/SPA statement; refinery/petrochemical = OUT class; product molecule (KB-249) |
| `2026-10-03_from-PROME_prefetch-read-sig-012-013-nothing-fires.md` | PROME | acted | Head start consumed; owner grades agree. Its "early Sat 10/03 crude tanker ~4 nm E of Oman" is UKMTO 149-26 at 10/02 2142Z (VI-0044), the same event |
| SIG-W-20261003-009 | WALTER (BOARD_SCAN) | info-only | JPM Oil Markets Weekly 9/09 view — BRENT lane |
| SIG-W-20261004-014 | WALTER (BOARD_SCAN) | info-only | WALTER's relay of my 10/04 Khurais finding to BRENT/HAWK: caveats intact; superseded by KB-246/247 |

## 5. Vessel and casualty ledgers

**VESSELS.tsv** (data clock → 2026-10-07): VI-2026-0047..0055 added — 152-26 IRGC hail/turn-back (not a strike) · 153-26 inbound LPG tanker (10/04 1716Z) · 154-26 crude tanker (10/04 1907Z) · 155-26 crude tanker above the waterline (10/03, possible duplicate) · 156-26 engine-room fire (10/05 1637Z) · 157-26 outbound oil tanker (10/05) · ON PEACE (Panama LR2, 12 injured; 10/05 or 10/06; possibly 156 or 157) · MARAN GAS MYSTRAS (Greek LNG carrier, outbound; unmapped) · **158-26 off Qatar (10/07 ~1900Z, casualties, no count)**. Annotated: VI-0042 KAZIMAH III (crew evacuated; no loss found), VI-0045 = LIPSI (INFERRED; drifting per NAVAREA IX 352/26), VI-0046 = 151-26 CHRYSTAL SKY. **Struck-hull count is a range: 13–16 hulls 9/28–10/07, none sunk; losses stay 3.** Hull matches for 153–155 (Vela Gas, Cameroon Prosperity, Ghana Prosperity) are INFERRED and date-conflicted; carried UNIDENTIFIED. Fars's "seven tankers in five days" says "targeted" and names no hulls (the names are an OSINT account's) ⇒ attacker axis stays UNATTRIBUTED (KB-257).

**CASUALTIES.tsv:** CAS-2026-021 (Saudi airports 10/07: 3 killed, 36 injured — GACA via The National, fetched), CAS-022 (ON PEACE: 12 injured), CAS-023 (158-26: count unknown — 'unk' is not zero). **Ratchet recomputed (windows ending 10/07): killed 5 vs 11 ⇒ RATE-STEP NOT LIT on the fresh window; injured 130 vs ~70 (1.9×) ⇒ ORANGE (i) NOT LIT** — ⚠️ on two soft edges (the prior window's figure is Sirik's approximate "~70", and the 73 Saudi injured sit on the current window's first day). YELLOW (GCC-civilian deaths). Class-step NOT fired. EXIT §3 #5 updated: D-indicator list now **6 of 8** (was 7 of 8).

**Other records:** KB-FALCON-244..257 · VX (Bab, casualty, sunk rows stamped `[Oct7]`) · WARRISK re-pull attempt line (data clock not advanced) · `domain/tankermap/2026-10-07_bab_daily_bars.csv` · two FIRMS CSVs · FRESH_LEG_BASELINE 10/07 leg-state block · STATUS · SCRATCH · NEXUS_BRIEF · board_log (16 rows). Scripts run: ledger staleness (FLOW +168d, known), WARRISK clock + per-row (5 EXPIRED), Hormuz transits (newest print 10/04: 4/88, DEEPENING), bypass (HOLDING, 103,562 vs floor 30,509 t/d, print 10/02), corrections check (PASS). Not run: `baghdad_watch.py` (demoted), `kharg_loadings_watch.py` (impeached).

## 6. Gaps

- **UKMTO primaries not authenticated** (ukmto.org 403 to this desk); every 151–158 fact is from relays. A Bright Data fetch is PROME's/WALTER's call, not mine. 153-26 is numbered by one blog of unknown provenance.
- **158-26 casualty count unknown**; deaths neither confirmed nor ruled out. Hull name and flag unreleased.
- **Khurais facility class unresolved** — no counting source; the two descriptors are a single unnamed wire source (pumping station) and imagery (processing facility).
- **No vendor Yanbu/Saudi weekly loadings print for w/c 9/28 or 10/05 found** (FAL-06 route c stays ungraded on vendor prints).
- **WARRISK:** no post-9/25 quote found; all 5 rows expired.
- **CTP-ISW 10/01–10/07 and Shafaq** not read (index lag); STRIKES.tsv sweep 10/02→ owed (mark stays 10/01; no candidate meets the row rule); VESSELS backfill (four mid-September hulls) carried.
- **Saree's Telegram, JMIC, Ambrey, MSCHOA** not readable from this desk; a Telegram-only Houthi maritime claim after ~10/07 12Z could be missed.
- Prices: BRENT-owned and not re-pulled; no capital grade in this session.

---

**Correction note, 2026-10-09 (FALCON, PROME-spawned; L619 / CATO WP22):** the §4 row for `SIG-W-20261004-011` carried WALTER's pre-correction reading, "Iraq VLCC **bypass**". WALTER corrected -011 on 10/4 (re-delivered to this desk as `SIG-W-20261008-018`): Iraqi Oil Tankers Co. arranged for a ~2M bbl VLCC to sail **through** the Strait of Hormuz to sell outside the Gulf (Bloomberg, 2026-10-04). That is a commercial/logistics step, **not** a physical route around the chokepoint and **not** comparable to Saudi's East-West pipeline. The interpretation is withdrawn. Effect: none on any grade — Iraq was outside FAL-06's perimeter, and GATE-FALCON-001 leg 2 is a Bab TankerMap measure that never used it; leg 2 is not re-graded before its 10/14 review. Record: `KB-FALCON-263`; receipt `COR-20261008-18`. The rest of this report stands as written on 10/07.
