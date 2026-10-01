# FALCON 2026-10-01 — L0 drain: Ghawar-area fire, four Hormuz hulls, US reply to Iran, Iraq deadline, GATE-FALCON-001 leg-2 magnitude

**Session:** `falcon-1001`, PROME-spawned Tier 1 (prome-0c, WQ-184 due row, Will "spawn the slate" 12:13 ET). Opus. Written 2026-10-01 from ~12:20 ET.
**Marks unchanged: B 1 / C 14 / D 85.** Nothing on my registered rail fires today. Convergence 43/50 unchanged.

## 0. Bottom line (plain words)

1. **The Ghawar / Ain Dar fire: I can neither confirm nor refute a strike, and nothing on my rail would fire even if it were confirmed.** My own NASA satellite pull (FIRMS, three VIIRS sensors + MODIS) shows a **real, new heat source at the published point (25.839N 49.227E)**. It was absent for the six days and nights before 9/29, appeared on **9/29 at 09:30Z** (about 21 hours *before* the OSINT plume claim of 06:45Z 9/30), was seen again on 9/30 (09:11–12:02Z, peak 26.7 MW), and was **not** seen on the 9/29 and 9/30 night passes or on the 10/01 midday passes. That rules out a routine flare (flares show at night) but does not say what burned, whether anything was struck, or which facility it is. **No Saudi MoD, SPA, Aramco, CENTCOM or wire statement exists as of ~12:20 ET 10/01.** The only "attack" sources are IRNA citing anonymous sources and a Houthi-aligned Yemeni outlet (Yemen Press Agency, 10/01) relaying unverified video and "explosions overnight"; my night passes saw nothing at the point overnight 9/30→10/01.
   - ⚠️ **Why it is still a tell-Will item if it ever confirms:** a Ghawar gas-oil separation plant is an oil-PRODUCTION asset, the class both sides have spared all war. FAL-01 (the registered production-hit row) already resolved FAILED on 7/25 and the D 75→85 rung already fired on 9/28; **nothing is registered above D 85.** So a confirmed hit would move no mark by rule. It would be the most consequential unregistered event on the board, and it is now a named input to FAL-06's design.
2. **Four tankers hit in Hormuz 9/28–9/29 (UKMTO late reports): no rung fires.** None sank, no casualties reported, positions unpublished. Losses stay at 3. They end the 9/24–9/27 lull and push the D→C downgrade trigger (72h two-sided halt) further away.
3. **The US answered Iran's 7-day plan (Doha 9/29, Iran confirmed 9/30): diplomacy stays at 3.** New state name: **MEDIATED EXCHANGE LIVE, NO FRAMEWORK.** C→B needs a DATED framework AND verified Hormuz reopening steps. Neither exists (PortWatch 1/88 on 9/27).
4. **Iraq at the 9/30 deadline: the US withdrawal is COMPLETE (Pentagon 9/30) and no kinetic event was found.** Kataib Hezbollah declared victory on 10/01 and denied any disarmament deal; disarmament slipped to 2027-06-30. Read: US exposure in federal Iraq drops toward zero (good for rung (d)), and the militias' hands are freer against Saudi targets (Rubio named KH for Petroline on 9/22). HAWK owns VX-HAWK-IRAQ-01.
5. **GATE-FALCON-001 leg-2 magnitude, proposed to DAEDALUS: a 35% week-over-week drop in TankerMap's 7-day Bab tanker total, on two consecutive print-days, against the prior 7-day total frozen at the first qualifying read; floor 21 tankers in the reference week.** Base rate: one episode in 1,868 pre-war days, and the only war-time episode is the known enforcement positive (the 7/22 Saudi-hull embargo). **Adopting it into the letter is a threshold registration: Will's word via PROME.** Leg 2 today: NOT FIRED (TankerMap 10/01 7-day average 11.1 tankers/day, +144% w/w, the wrong sign).
6. **Bu Hasa (UAE) "143 MW fire": the number is real and dated 9/29, but the same spot burned just as hot on 9/14–9/15 with no attack reported.** Reads as episodic flaring or a plant upset; INDETERMINATE.
7. **A new confound for leg 2:** Bab tanker counts now ride Saudi Red Sea loadings. The +144% coincides with Yanbu's restart, so a later Petroline re-shutdown would look like a step-down without any Houthi enforcement. The proposal carries an attribution exclusion for that.

## 1. The five WALTER signals, graded

### 1a. SIG-W-20260930-005 + SIG-W-20261001-003 — the 9/30 smoke west of Abqaiq

**Own FIRMS pull** (key from `FORGE/tools/market-data/.env`; bbox 48.6–50.0E, 25.3–26.4N; NOAA-20, NOAA-21, SNPP VIIRS + MODIS; windows 9/23–10/01; pulled 10/01 ~12:15–12:20 ET). Detections within 3 km of 25.8392N 49.2268E:

| Date (UTC) | Detections | Passes | Max FRP |
|---|---:|---|---:|
| 9/23–9/28, day and night | **0** | 6 days × ~2 day + ~3 night passes, bbox carried 30–44 night detections/night elsewhere | — |
| **9/29** | 2 | N20 09:30Z, N21 10:13Z (day) | 12.4 MW |
| **9/30** | 5 | N20 09:11Z ×2, SNPP 10:32Z, N20 10:51Z, Aqua MODIS 12:02Z (day) | **26.7 MW** |
| 9/29 + 9/30 nights (21:38–23:18Z) | **0** | 3 sensors each night; bbox had 36 / 41 detections elsewhere | — |
| 10/01 day (to 10:34Z) | **0** | N20 10:34Z, SNPP 10:13Z covered the bbox | — |

**What this establishes:** a NEW thermal anomaly at the published point, two consecutive days, daytime only, modest intensity (12–27 MW; the 9/10 Petroline fire reached 158 MW). It is **not a routine flare** (a flare is persistent and shows at night; this pixel was dark at night throughout). The first detection is **9/29 09:30Z, ~21 h before the OSINT plume onset (06:45Z 9/30)**, so the event began a day earlier than reported, or recurred.
**What it does not establish (LESSONS FAL-11/FAL-12):** what burned, whether anything was struck, which facility, or any damage or production effect. Non-detection on night and 10/01 passes is not proof the fire was out (smoke, cloud, detection limits). FIRMS assigns no cause.
**Facility:** NOT identified. The point sits ~45 km WSW of the Abqaiq plant (WALTER geometry, consistent with my coordinates), south of Ain Dar. Candidates: a gas-oil separation plant (production) or Petroline-origin pumping infrastructure (transport). I have no facility GIS layer that resolves it.

| State | Status | Source |
|---|---|---|
| Fire / heat observed | **CONFIRMED by own instrument** (9/29–9/30) | own FIRMS pull |
| Attacked | **NOT ESTABLISHED** | no Saudi/Aramco/CENTCOM/wire; IRNA anonymous; Yemen Press Agency 10/01 (Houthi-aligned) relays unverified video, "explosions overnight" |
| Damaged / production affected | **NOT ESTABLISHED** | nothing; CNBC 10/01 oil piece silent |
| "Overnight explosions, fires into Thursday" | **NOT SUPPORTED by my night passes** (21:38–23:18Z 9/30 = 00:38–02:18 local Thursday, 0 detections at the point) | own FIRMS pull |
| "Routine flaring" (2nd-hand digest) | **CONTRADICTED** as a description of this pixel (no night signal, dark six prior days) | own FIRMS pull |

**Grade against my rail:** FAL-01 is RESOLVED (FAILED 7/25), so it cannot fire again; the production-hit class it named is the question. §3 indicator #1 is already LIT (9/28). The D 75→85 rung fired 9/28, one move, nothing registered above 85. **⇒ On the letter nothing fires, confirmed or not.** If an operator, state or named-wire primary confirms a strike on a Ghawar production facility: tell Will the same hour (WALTER re-routes IMMEDIATE per -003), log a STRIKES row, and treat it as the decisive design input for FAL-06 (first upstream-production hit of the war). **Today: CANNOT EVALUATE the strike; CAN confirm a new two-day heat source at the point; CAN refute the "routine flare" and "overnight fires" descriptions as applied to that pixel.**

**Bu Hasa (UAE), same signal — own FIRMS pull (VIIRS ×3, box 53.20–53.42E, 23.45–23.62N, 9/12–10/01):** the OSINT "143 MW" is a real pixel: **143.3 MW at 23.545N 53.326E on the 9/29 day pass** (posted 9/30 17:44Z, so the figure is a day old when quoted), with 118.7 MW the night before and 172.0 MW the night after; by 9/30 the spot is back under 10 MW. **The same spot ran a burst of the same size two weeks earlier with no reported attack: 141.9 MW (9/14 day) and 108.4 MW (9/15 day).** Between bursts it reads 1–16 MW. That pattern is episodic large flaring or a plant upset, and it repeated. **⇒ The thermal reading does not support an attack claim on its own. INDETERMINATE, leaning flare/upset.** No ADNOC/WAM/wire statement. ⚠️ Limits: site identity as Bu Hasa is from the OSINT post's coordinates, not a facility layer; pulls for 9/19–9/26 returned no rows at the spot (a gap, not a measured quiet).

### 1b. SIG-W-20260929-011 — Petroline pump stations 8 and 9

| State | Status |
|---|---|
| ATTACKED (9/10) | confirmed (MoE 9/11) |
| SHUT | MoE 9/11; restart at low rate reported 9/22; exports reported 9/28 |
| DAMAGED at stations | **PARTLY SUPPORTED, not operator-confirmed:** Reuters industry sources + imagery said "three pumping stations" (KB-206); EGYOSINT's PS-8/PS-9 account is consistent with that count but is one OSINT read with no provider, date or resolution |
| Bears on the restart rate? | **Plausible mechanism, not established.** Reuters 9/29 (Kpler): line throughput ~2.65 mb/d, expected 3–4 mb/d in days, pre-attack ~5.5 mb/d "could take another month". A slow ramp is what damaged pumping capacity would produce; it is also what a cautious restart would produce |

PS-8/PS-9 are NOT merged with Al Mesba'ah / Al Dhekra (C3): no coordinates reconcile them. No STRIKES row (extends the existing 9/10 rows). Nothing fires.

### 1c. SIG-W-20261001-001 — four tankers struck 9/28–9/29

Rowed `VI-2026-0038..0041` in `domain/vessel-incidents/VESSELS.tsv` (AL FUNTAS 9/28; MERSIN PROSPERITY, SINBAD, AL RUWAIS 9/29). Names from trackers, not UKMTO; UKMTO warning 146/26 unread (403).

| Rail item | Grade | Distance from firing |
|---|---|---|
| D 75→85 rung (a) total loss | n/a — rung FIRED 9/28, one move | none sank; no CTL |
| rung (c) hit IN a GCC port/anchorage | n/a — rung already fired | positions unpublished; no port named |
| §3 #6 / VX-FALCON-SUNK-01 | not re-firing; **losses stay 3** | — |
| §5 rewrite leg "third class-(iii) hull loss" | NOT MET | needs a tanker total loss |
| §2 D→C (72h two-sided halt) | NOT MET, moved further away | the 9/24–9/27 lull ended 9/28; plus Houthi salvo 9/26 |

**Reconciliation with my 9/28 "no attacks since 9/23":** that was true on what UKMTO had published by 9/28 evening; AL FUNTAS (9/28 evening) and the three 9/29 hits were reported late (9/30). Dated sequence, not a contest. **CAPE DAO (VI-0036):** WALTER flags "two torpedoes"; my row already carries that as the seafarers' union only, and the death (1) is already rowed. No change.

### 1d. SIG-W-20261001-002 — US reply to Iran's 7-day plan

Diplomacy vector stays **3**. New state: **MEDIATED EXCHANGE LIVE, NO FRAMEWORK** — counter-proposal delivered by Qatar (Doha 9/29), receipt on record (Mohajerani 9/30), contents undisclosed, gap = sequencing (Reuters), no US on-record confirmation; Axios reports a Rubio expulsion order 9/28 (Iran denies; order precedes handover, so no contradiction). Trump 10/01 (CBS): *"I don't think you could ever have peace"*; strikes "possible" after the midterms if talks fail — POTUS channel, tape not information. **C→B distance:** a dated framework (none) AND verified reopening (PortWatch 1/88 on 9/27; Windward 16–17/day on 9/28–29 — vendors disagree ~17×). Folded into the 10/05 rewrite.

## 2. Rung (d) and the 9/14 Marines

Rung (d) = a US service member **KILLED** by Iranian/proxy action on/after 9/8. 9/14: 8 Marines **injured** (NBC, 3 unnamed officials; all returned to duty) ⇒ NOT MET. US KIA unchanged at 19 (last hostile death 7/17). Moot for the marks (the rung fired 9/28 on (b), one move) but recorded: the near-miss was one cruise missile from a death. The Iraq withdrawal removes the largest pool of exposed US personnel from militia range.

## 3. Iraq read at the 9/30 deadline (HAWK owns VX-HAWK-IRAQ-01)

| Fact | Source |
|---|---|
| US withdrawal COMPLETE 9/30: "orderly departure" from the Irbil air base; training/intel support continues | Pentagon spokesperson Parnell via PBS/AP 9/30; LWJ 9/30 |
| KH 10/01: "The resistance has won this round"; no disarmament deal with PM Al Zaidi; weapons stay "a trust in the hands of our mujahideen" | The National 10/01 |
| Disarmament deadline slipped to 2027-06-30; PM calls 10/01 the start of "serious" disarmament | The National / CBS 10/01 |
| Kinetic event at the deadline | **none found** (CBS 10/01 live page; The National; PBS). Baghdad embassy feed QUIET since 9/19 (backstop only) |

**Read:** the deadline passed without a kinetic backlash: §3 indicator #4's next rung (a *damaging* follow-on) did **not** fire. Two forward effects: (i) rung-(d)-class exposure in federal Iraq falls; (ii) Iraq-origin attacks on Saudi energy (Petroline 9/10, US-attributed to KH) lose their main deterrent (US forces in range of retaliation). ⚠️ CTP-ISW 9/30–10/01 not read this session (SEARCH-NOT-FOUND on a scoped search); the primary-source protocol in `domain/IRAQ_PMF_DISCRIMINATOR_REVIEW.md` is not fully met.

## 4. GATE-FALCON-001 leg 2 — proposed MAGNITUDE and REFERENCE WINDOW (owed to DAEDALUS 9/30, one day late)

**Today's grade:** NOT FIRED. TankerMap `analytics/straits/bab-el-mandeb`, latest sighting 2026-10-01 13:09 (ATLANTIS ARTEMIDA): **7dma 11.1 tankers/day, 7d total 78, +144% w/w, 12 in zone.** Path 3.1 → 4.0 → 4.4 → 5.4 → **11.1**. The jump coincides with the Yanbu restart (Kpler 8.5 mb/d Saudi 7-day loadings, AGBI 9/30).

**Base rate, computed BEFORE choosing the number.** TankerMap exposes no machine-readable history from here, so the base rate uses IMF PortWatch `chokepoint4` daily tanker counts (2,000 contiguous days, 2021-04-07 → 2026-09-27; the letter's corroborator, ~2–2.6× TankerMap's level). Event = 7-day tanker total ≤ (1−M) × the prior 7-day total, on two consecutive days.

| M | 2021-04 → 2023-10 (925 d) | 2024–2025 Houthi regime (731 d) | War 2026-02-28 → 09-27 (212 d) |
|---|---:|---:|---:|
| 30% | 0 | 3 | 2 (7/25 embargo · 9/1 unattributed) |
| **35%** | **0** | **1** (2025-01-07) | **1 (7/27 = the 7/22 Saudi-hull embargo, the known enforcement positive)** |
| 40% | 0 | 0 | 0 — **misses the known positive** (−44% then −39%) |

**Proposed letter repair (to DAEDALUS; adoption = Will's word via PROME):**
- **MAGNITUDE:** TankerMap 7-day Bab tanker total **≤ 65% of the reference 7-day total** (a step-down of **≥35%**).
- **REFERENCE WINDOW ("prevailing 7dma"):** the 7 days immediately before the current 7-day window, as TankerMap's own week-over-week figure defines it, **frozen at the first qualifying read** — the second read is graded against the same frozen reference, so a decline cannot re-base itself downward.
- **SUSTAINED:** two qualifying reads on **two consecutive UTC print-days**; a non-qualifying read between them resets.
- **PRECISION / TIE:** compute from totals where shown (prior = current ÷ (1 + w/w)); a page-printed w/w of exactly −35% counts as MET.
- **LOW-COUNT FLOOR:** reference 7-day total < 21 (3/day) ⇒ UNGRADEABLE, not fired (small-number noise).
- **ATTRIBUTION (unchanged judgment limb, one exclusion added):** a step-down coinciding with a Saudi Red Sea loadings change (Yanbu/Petroline halt or slowdown) is NOT enforcement-attributable unless a Houthi enforcement act on a hull falls in the window.
- **Disclosed limits:** proxy base rate (PortWatch ≠ TankerMap); n=1 known positive; reads are manual (no pipeline); TankerMap restatement policy unknown — grade as first read.

## 5. Line 540 (due 10/05) — what is done, what remains

**Not finished today, by choice:** the EXIT_PROTOCOL + THESIS rewrite and FAL-06 deserve a dedicated session; doing them at the end of a drain would repeat the correction-pass pattern (LESSONS FAL-10, MEMORY 9/14).
**Inputs gathered today for 10/05:**
1. **Composition disagreement (carry, never rescue):** route loss at Yanbu 9/11–9/28 vs no demonstrated barrel loss (Sept Saudi exports >5 mb/d; Kpler 8.5 mb/d 7-day loadings 9/30, "highest of the war"; Aramco CEO 9/24 "We never stopped"). FAL-05's fire stands on its letter.
2. **FAL-06 must separate four quantities** (nameplate 7 mb/d · routed flow 2.65 Kpler / 3.5 Bloomberg · stated offline capacity, none on record · net supply loss, not demonstrated) and must not over-fire on a re-routable terminal halt (route (c)'s defect).
3. **New design question:** a Ghawar/Ain Dar production hit is now a live candidate class with no registered consequence above D 85. FAL-06 (or a registered rung) must decide whether an upstream production hit is the next test.
4. **Diplomacy state** for the rewrite: MEDIATED EXCHANGE LIVE, NO FRAMEWORK (§1d).
5. KB-168 Yanbu terminus proxy: still unbuilt; carried with FAL-06.
**Remaining for 10/05:** FAL-06 base rate → number → registration in `thesis/PREDICTIONS.tsv`; EXIT_PROTOCOL rewrite (also clears its 44,914 B read-cap breach); THESIS v3.0; 7-day scenario review.

## 6. Mail and records

Inbox drained 6/6: five WALTER handoffs + the WQ-295 R3 packet (answered: `PROME/inbox/2026-10-01_from-FALCON_wq295-r3-watch-verdicts.md`). Packets: DAEDALUS (leg 2), PROME (session memo). KB-FALCON-213..218; VI-2026-0038..0041.

Sources: own FIRMS pull 10/01; WALTER `research/2026-10-01_iran-full-sweep.md`; The National 10/01 ("Resistance has won this round"); PBS/AP 9/30 (US withdrawal complete); CBS live 10/01; Yemen Press Agency 10/01 (en.ypagency.net/407067); TankerMap 10/01; IMF PortWatch chokepoint4/chokepoint6; Reuters 9/29 via MarineLink; AGBI 9/30.
