# SAM CALENDAR

**Last Updated:** 2026-06-19 (KOYOMI Run-8: CATALYSTS.tsv schema fix `type` column restored 7→8 fields, 18 rows backfilled `external`; Sat Jun 20 CFTC EV-gate row added with `sam-internal` type — both CALENDAR + CATALYSTS) | Prior 2026-06-18 PM Thu: Step 1.5 HAWK-Iran reconcile pass — dropped Switzerland-ceremony / all-watch-met / Phase-1-formally-dormant; softened "physically reopening" → "reopening process begun"; added verification-leg-open + 60-day-toll-free-then-Oman-administered hedging across ~10 instances per HAWK primary-source framing | Prior 2026-06-18 PM Thu: [propagation/thesis-fact] pass — FOMC Jun 17 ✅ RESOLVED hawkish (Warsh debut, median 2026 dot +40bp); Iran/US deal ✅ SIGNED Wed Jun 17 (Pezeshkian+Trump — Iran docket UNFROZEN on signing-binary, verification leg open per HAWK-aligned reconcile); facts only, conviction/sizing → v1.6 tonight) | *Prior 2026-06-14 PM Sun:* Tier-1 Brent + Ueda pass: Intervention Watch SAM-23 72→~30 per CH-011; Phase 2 Watch Brent row 🟠 → 🟢 BREACHED $87.33; MOU row 🔴 → 🟠 substantively walking back via Pakistan-mediated 14-pt draft; Geopolitical Watch rewritten with Jun 10-14 entries. | **View:** Forward-looking only. Past events pruned weekly.

---

## EARLY-MID JUNE — INTERVENING DATA (rate-differential + super-long demand tests)

| Date | Event | What to Check | Threshold / Signal | Who Cares |
|------|-------|---------------|-------------------|-----------|
| **🟠 Jun 17 (Wed JST, 08:50 = ~7:50 PM ET Tue Jun 16 — BOJ-decision evening ET)** *(date corrected Jun 10 from "Jun 18" via MOF Customs release calendar — pinned, not pattern-matched)* | **May trade balance (provisional) — PHASE 1 STABILITY LAG-TEST** (per PROME 5/26 forward-question; `trade_balance_japan.py` auto-pulls) | Volume recovery vs cost-side: did ME crude flows normalize? did petroleum input costs rise? | **Routing:** (a) deficit re-opens with Brent <$100 → 🟠 Phase 1 mechanism back online (inversion was transient); v1.5 CHANGELOG candidate to relabel inversion as one-month spike. (b) surplus persists with ME volumes recovering → 🟢 inversion is structural; v1.4 finding confirmed durably. (c) surplus persists but ME volumes still depressed → 🟡 inconclusive; defer to June TB (provisional Jul 22, per same calendar). Detailed May release Jun 26. | SAM, BRENT, HAWK |
| 🟡 Jun 19 (Fri) | Japan National May CPI | Core / core-core vs April (1.4 / 1.9) | Post-BOJ; confirms or breaks dovish trajectory. Subsidy-taper passthrough watch. | SAM, HENRY |
| **🔴 Sat Jun 20** | **CFTC JPY COT (Jun 16 data) — v1.6 EV-gate decision observable** *(sam-internal)* | Net spec position vs pre-registered thresholds | Pre-registered per v1.6 backbone (THESIS commit `f378c0e4`): **cover <120K (-67% of -180K peak) → v1.6 frame FAILS margin test → trim/close discussion**; **holds 140-150K (78-83%) → frame survives margin → vehicle question stays open**; **builds through -153K/85% → amplifier escalates +5pp → +8-10pp → frame STRENGTHENED.** First post-BOJ + post-FOMC CFTC read; captures Jun 9-16 positioning into the binary. Decision-grade observable; SAM action-forcing. | SAM, LIQUID, HENRY |
| 🟡 Jun 23 (Tue) | JGB 5Y auction | BTC ratio, tail | Belly demand; 5Y is the rate-expectation barometer (post-BOJ forward path read) — off the J-ICS-abandonment axis, clean rate-expectation tell | SAM, LIQUID |
| 🟡 Jun 25 (Thu) | JGB 20Y auction | BTC ratio, tail | Insurer demand test; broadening of buyer strike to 20Y = escalation (Apr 14 20Y was strong, BTC 4.82x — strike was 30Y/40Y-specific) | SAM, LIQUID |
| 🟡 Jun 26 (Fri) | Tokyo June CPI | Core / core-core trend | Advance read for July national; subsidy-taper passthrough | SAM, HENRY |
| 🟡 Jun 30 (Tue) | JGB 2Y auction | BTC ratio, tail | Front-end demand; sensitive to BOJ near-term path (first 2Y post Jun-16 MPM) | SAM, LIQUID |

## MID-JUNE — ✅ BOJ JUN 16 RESOLVED (hiked 1.00% as-priced — was the dominant remaining catalyst)

| Date | Event | What to Check | Threshold / Signal | Who Cares |
|------|-------|---------------|-------------------|-----------|
| **✅ Tue Jun 16 RESOLVED** | **BOJ MPM — HIKED 25bp → 1.00%** (highest since 1995; vote 7-1, Asada dovish dissent for hold; growth+inflation outlook raised; Uchida fronted presser for absent Ueda, "not imminent" guidance) | — | **Delivered AS PRICED — modal package, NOT hawkish tail. NO carry unwind (CH-004 confirmed): USDJPY WEAKENED 160.36, FXY flat $57.22.** SAM-21 ✅ / SAM-24 ✅ CONFIRMED; SAM-23 ❌ / SAM-26 ❌ FAILED (both pre-marked down). Detail → TIMELINE Jun 16. | **ALL** |
| 🟡 Tue Jun 30 | **Sato Ayano takes Nakagawa's seat (BOJ board)** *(Nakagawa term expires Jun 29; corrected Jun 4 from prior "Jun 16" date which conflated this with the MPM)* | Sato characterization (reflationist) + post-Jun-16 BOJ commentary | Apr-28-style hike-dissent bloc 3 → 2 (Nakagawa was active 1.00% dissenter); material dovish shift in marginal-vote count → post-June PATH/CEILING implication (beyond 1.00% harder). Strengthens v1.5.1 path-MEDIUM conviction; no Jun-16 binary impact. | SAM, HENRY |
| Jun 16-17 | BOJ interim QT assessment **+ FY2027+ purchase-plan layout** | Pace adjustment; taper-pause decision | **Jun-9 sourced (Reuters): BOJ considering PAUSING taper — open-ended ~¥2.1T/mo option; board split.** Taper pause = long-end absorption relief (J-ICS pressure eases, D2-lean); also shrinks accelerated-QT hawkish-tail. Potential super-long-specific operation if JGB stress re-engages. | SAM, LIQUID |
| **✅ Wed Jun 17 RESOLVED** | **FOMC HOLD 3.50-3.75% UNANIMOUS 12-0 under new Chair WARSH (debut, since May 22)** — statement gutted ~300→~130 words, all forward easing bias removed; SEP **2026 median dot +40bp (3.4→3.8), 9-of-18 see ≥1 hike (6 see two), 1 cut; core PCE 2026 +60bp to 3.3%; 17-of-18 see inflation upside**. Warsh refused to dot himself; "no reason to revisit the 2% target." | **Pillar 1 directional vector INVERTED across Jun 16-17: BOJ +25bp compression < Fed dot +40bp re-widening — rate-differential is now WIDER than pre-Tue.** Secondary FED-CUT path replaced by FED-HIKE regime (CME July hike ~75%; Polymarket "Fed hike 2026" ~56%). Market: DXY ~100.40 (broke 100); 2Y +16bp; USDJPY 160.78 Wed → **161.34 Thu** (no MOF response 48h+). Detail → STATUS § FOMC JUN 17 RESOLVED; THESIS Pillar 1 + § Independent Catalyst (facts logged); CHANGELOG 2026-06-18 entry. | **ALL** |

## EARLY JULY — POST-MEETING FOLLOW-ON WINDOW (seeded Jun 2 from MOF Jul calendar + BOJ/Fed schedules)

| Date | Event | What to Check | Threshold / Signal | Who Cares |
|------|-------|---------------|-------------------|-----------|
| 🟠 Wed Jul 1 | Tankan Q2 (June survey) | Large-mfg DI + capex plans + price expectations | Hawkish if DI firm + capex strong + price expectations sticky; supports post-Jun-16 hike trajectory. *(Convention: 1st business day of July; March Tankan released Apr 1 2026 — verify at BOJ Tankan page closer to date.)* | SAM, HENRY |
| 🟡 Thu Jul 2 | JGB 10Y auction | BTC ratio, tail | First post-BOJ-meeting 10Y demand read; hike-priced or not | SAM, LIQUID |
| 🟠 Tue Jul 7 | **JGB 30Y auction** | BTC ratio, tail | First post-BOJ super-long auction; J-ICS lifer long-end abandonment continuation test (SAM-26 mechanism re-test) | SAM, LIQUID |
| 🟡 Thu Jul 9 | JGB 5Y auction | BTC ratio, tail | Belly demand post-BOJ; reflects forward-rate-path repricing | SAM, LIQUID |
| 🟡 Tue Jul 14 | JGB 20Y auction | BTC ratio, tail | Insurer demand test continuing; watch for strike broadening to 20Y | SAM, LIQUID |
| 🟠 Wed Jul 22 | **JGB 40Y auction** | BTC ratio, tail | Ultra-long demand; J-ICS abandonment most acute at 40Y (May 27 BTC 2.702 was soft) — watch for further deterioration | SAM, LIQUID |
| 🟠 Wed Jul 29 | **FOMC rate decision — July (non-SEP)** | Rate decision + Powell presser | No dot plot (non-SEP); read presser for hint on Sep SEP path. US leg of carry trade; lands ~2 days before BOJ Jul 31. | **ALL** |
| 🟡 Thu Jul 30 | JGB 2Y auction | BTC ratio, tail | Front-end demand; reads BOJ near-term path; lands same day as BOJ Jul MPM Day 1 | SAM, LIQUID |
| 🔴 Fri Jul 31 | **BOJ MPM — July meeting** | Rate decision + Outlook Report | Follow-on to Jun 16 hike (if delivered); pace assessment. *(BOJ confirmed Jul 30-31 dates; Day 2 decision = Jul 31.)* | **ALL** |

---

## INTERVENTION WATCH (Sun Jun 14: SAM-23 RE-DERIVED 72% → ~30% per CH-011; disorder-not-level falsified empirically)

*Live USDJPY / Brent levels live in STATUS — this table holds thresholds + significance only.*

| Trigger | Action Expected | Notes |
|------|---------|-----------|
| **USDJPY closes >159.50** | Intervention #3 possible (lower bar than originally framed) | 🟠 #3 zone live but 6+ orderly sessions at 160+ with NO strike (Jun 5 onward) empirically confirms CH-011 disorder-not-level read. **SAM-23 ~30%** (mid-low of 25-45 band). 160 is hard intervention trigger; 161.5+ would re-open void. |
| Brent through $115 | Phase 1 reasserts; USDJPY upside → intervention | Phase 1 oil pressure RECEDING on diplomacy track (Brent $87.33 Sun Jun 14 sub-$90 first close this cycle); far below $115. Supply-destruction caveat: Hormuz still physically closed Day 105. |
| **✅ Iran/US deal SIGNED Wed Jun 17 (initial agreement) — Iran docket UNFROZEN on signing-binary; verification leg OPEN** | Pezeshkian + Trump electronic signature (Iran confirmed via Al Jazeera; NOT a Geneva/Switzerland ceremony — sweep correction); Pakistan PM Sharif "enters force immediately" | Terms: **60-day toll-free Hormuz reopen, THEN Oman-administered fees**; US lifts naval blockade; Iran dilutes HEU; sanctions waived (not terminated); 60-day nuclear negotiation window. **Per CNN "tougher talks lie ahead" — this is an *initial* agreement; verification is the binding portion.** Signing-binary primary-source threshold met (Pezeshkian electronic signature). **Hormuz reopening process begun Day 110:** Thu Jun 18 — initial traffic resuming (4 supertankers transiting incl. first Saudi-owned vessels since Day 1; backlog "weeks to clear"); US naval blockade lifting. **Verification leg OPEN: demining, insurance restoration, traffic normalization, Oman fee-administration negotiation, HEU dilution compliance, sanctions-waiver rollout.** Brent $79.68 Thu (~−18% cum from $96.78 Jun-3) — half deal-signing, half IEA glut warning (+8 mbpd by 2027 vs +2). Sources: NPR, Al Jazeera (electronic-signing confirmation), NBC (toll-free-then-Oman), CNN (initial-agreement framing), CNBC, Rigzone. |
| Bessent / Katayama statement | Channel 3 augmentation if explicit | Reuters Jun 1: Bessent "BOJ should have independence." Katayama May 29 "decisive action" verbal. Katayama (cabinet) Jun 12: "no impact on policy meeting after Ueda hospitalized" — clears the hike path. **Pre-meeting blackout ACTIVE.** |

---

## STRUCTURAL CHANNEL 1 MONITORS (v1.5 — DEFERRED STRUCTURAL BACKSTOP)

*Channel 1 demoted to deferred structural backstop after 3-of-3 Big 3 mutual ESR window confirmation. Multi-year mechanism intact, near-term timing pushed to H2 FY2026 plans (Oct-Nov) or FY2026 ESR (May 2027). These monitors remain for re-test conditions.*

*Live levels for these indicators live in STATUS — this table holds thresholds + significance only.*

| Indicator | Threshold | Significance |
|---|---|---|
| JGB 30Y | 4.0% breach not durable | J-ICS DOMESTIC mechanism intact; threshold sensitive to oil/CPI cross-currents (SAM-26 FALSE) |
| JGB 10Y | 29-yr high zone (>2.40% = stress crossover) | Stress crossover; running well above threshold |
| Lifer long-end demand | absence = J-ICS amplifier active | DOMESTIC, not transmitting to foreign-asset selling |
| MOF ITS weekly | >¥1.5T selling = stress | Watch for shift from net buying to net selling |
| **Next Channel 1 re-test window** | H2 FY2026 plans (Oct-Nov 2026) or FY2026 ESR (May 2027) | Channel 1 reactivation requires new shock (e.g., JGB 30Y blowout to 4.5%+, ESR <200% via market stress not M&A) |

---

## PHASE 2 WATCH (Sun Jun 14: Brent sub-$90 BREACHED; Phase 1 oil pressure RECEDING on diplomacy; Phase 2 inception NOT triggered — channel near-term dormant. v1.6 relabel pending post-Jun-16-18 scoring.)

*Live levels (Brent, USDJPY, CFTC net) live in STATUS — this table holds thresholds + significance only.*

| Indicator | Threshold | Significance |
|---|---|---|
| Brent | <$90 = "headwind resolved" | 🟢 **BREACHED $87.33 Sun Jun 14** (first sub-$90 close this cycle; cum ~−10% from Jun-3 $96.78 baseline). Driver: 14-point Pakistan-mediated draft + Bessent signing-weekend 80% odds (Trump pushback unsigned). Phase 1 oil pressure receding; Hormuz still physically closed Day 105 — supply-destruction caveat live but pricing forward-discounts. |
| Iran/Hormuz MOU framework | Signed text by both sides + verification | ✅ **SIGNED Wed Jun 17 — Pezeshkian + Trump (electronic, per Al Jazeera).** Pakistan PM Sharif: "enters force immediately." **Initial agreement (per CNN); verification leg OPEN** (demining/insurance/traffic normalization/Oman fee-administration after 60-day toll-free window/HEU dilution/sanctions waivers). Hormuz reopening process begun Day 110 (initial traffic, 4 supertankers transiting Thu; backlog "weeks to clear"). Iran docket UNFROZEN on signing-binary; implementation watch active. |
| USDJPY 3-session sub-155 test | hard trigger condition | Not yet met (still 160+ 6+ sessions); diplomacy-track doesn't accelerate this branch directly (USD-side drivers dominate USDJPY direction). |
| CFTC short positioning | -75K cover line; -108K = 60% cycle-peak amplifier line; -153K = 85% escalation | 🔴🔴 −145,818 Sat Jun 13 release (Jun 9 data, 6th build week, **81% of −180K cycle peak**; **7,182 shy of −153K/85% escalation line** where amplifier moves +5pp → +8-10pp). No cover; fuel maximally loaded into Tue Jun 16 binary. Live net in STATUS. cftc_jpy.py auto-pulls weekly. |

---

## RETAIL / NISA FLOW MONITOR (added 2026-06-15 — structural counter-flow + latent carry-unwind amplifier; KB-SAM-193 / THESIS § STRUCTURAL COUNTER-FLOW)

*The yen-negative retail outflow is the modal "right but early" cause; unhedged + sticky ⇒ second-order accelerant in a yen-led unwind. Watch for the regime-change tell.*

| Indicator | Threshold / Signal | Significance |
|---|---|---|
| **MoF weekly "investment-trust mgmt cos" foreign-equity flow** | First month of net foreign-equity **SELLING** | 🟢 **REGIME-CHANGE TELL** — retail repatriation flips the counter-flow to a tailwind. None yet thru early 2026. ⚠️ Do NOT misread the aggregate BoP "trust account" line (institutional rebalancing / equity→bond rotation ≠ retail exodus). **boot.py integration pending — see MEMORY infra queue.** |
| Monthly NISA / Toshin net foreign buying | Run-rate vs ~¥1T/mo; sustained deceleration | 🟢 ~¥1T/mo, Q1 2026 record ¥6T+ (accelerating). A sustained slowdown = early softening of the headwind. |
| USDJPY sensitivity (unhedged book) | Sharp yen appreciation | 🟢 Most potent reversal trigger — FX loss on unhedged foreign holdings = self-reinforcing selling (requires a yen-led move to start). |

---

## GEOPOLITICAL WATCH

| Date | Event | What to Check | Threshold / Signal | Who Cares |
|------|-------|---------------|-------------------|-----------|
| **🔴🔴 Jun 10-11** | **US-Iran kinetic strikes (2-day) → Dawn #5 settlement announcement** | CENTCOM/IRGC mutual strikes; Iran Strait Authority declared Hormuz CLOSED; Trump CANCELLED Jun-11 PM round late Jun 11 on Dawn #5 (60-day ceasefire ext + Hormuz-reopens-on-signing + 15-20d window). Kinetic NOT ceased — drone/vessel exchange Jun 12 AM. | Brent FADED through escalation (down −0.5%); tape priced de-escalation. Iran has NOT confirmed (mediator/US-sourced). | ALL |
| **🟢 Jun 12** | **14-point Pakistan-mediated draft + Bessent signing-weekend** | Pakistan PM Jun 12: "final, agreed-upon text" (incl. 30-day Hormuz reopen clause); Bessent Jun 12-13: "signing this weekend or Monday," 80% odds. Trump pushback "draft doesn't reflect agreed terms" = paused-via-diplomacy unsigned. Katayama (cabinet) Jun 12 cleared Jun-16 hike path. | SAM-23 (ii) walk-back leg substantively MET (mediator/market-sourced, NOT Tehran-issued). HAWK B-Reopen 32% — market overpricing the deal direction. | SAM, BRENT, HAWK |
| **🟢 Sun Jun 14** | **Brent sub-$90 breach ($87.33)** | First sub-$90 close this cycle; cum ~−10% from $96.78 Jun-3 baseline. SPR drained THROUGH ~350M conventional throttle; war-driven drain = emergency authority → ~6mo runway (CRS R42460/EPCA). | "Headwind resolved" tagged; Phase 1 receding; SAM-23 72% → ~30% (CH-011 applied). War-conditional: diplomacy lands → non-emergency framing → 252.4M reactivates → runway collapses ~3mo. | SAM, BRENT, HAWK |
| **✅ Wed Jun 17** | **Iran/US deal SIGNED (initial agreement; signing-binary resolved)** | Pezeshkian + Trump signature; **electronic signing** (Iran confirmed via Al Jazeera; NOT a Geneva/Switzerland ceremony — Step 1.5 sweep correction); Pakistan PM Sharif "enters force immediately." Hormuz reopening process begun Day 110 (initial traffic resuming — 4 supertankers transiting Thu incl. first Saudi-owned vessels since Day 1; backlog "weeks to clear"). | **Signing-binary resolved ✅** (Iran formal statement + signed text confirmed). **Watch shifts to verification leg — STILL OPEN:** demining, insurance restoration, traffic normalization, **Oman fee-administration negotiation (toll-free 60 days only, then Oman-administered)**, HEU dilution compliance, sanctions-waiver rollout. **Phase 1 mechanism near-term dormant pending implementation — NOT formally closed.** Iran docket UNFROZEN on the binary; implementation watch active. | BRENT, HAWK, SAM |
| **Ongoing** | Deal-implementation durability watch (verification leg OPEN) | HEU dilution start; sanctions-waiver rollout; Oman fee-administration negotiation; demining/insurance/traffic-normalization; kinetic re-escalation risk | Per CNN: "tougher talks lie ahead" — this is an *initial* agreement; verification is the binding portion. Watch: (a) Iranian compliance with HEU dilution schedule; (b) sanctions-waiver rollout; (c) **Oman fee-administration negotiation outcome (60-day toll-free window closes ~Aug 16)**; (d) re-escalation triggers (Israel-Lebanon/Gaza, US-Iran kinetic). Brent backstop watch: durable bearish-oil now half-glut-driven (IEA +8 mbpd by 2027 vs +2 mbpd demand) — verification-leg failure would only partially re-rate. | BRENT, HAWK, SAM |

**MOU framework lineage:** "rumor-tier" (May 22) → "near-signed framework w/ Tehran friction" (May 26) → "temporary extension agreed" (May 29) → "effectively broken — Tehran suspended exchange + Hormuz threat" (Jun 1) → "kinetic strikes 2-day + Dawn #5 settlement announcement" (Jun 10-11) → "14-point Pakistan-mediated draft + Bessent signing-weekend 80% (unsigned; Iran has NOT confirmed; Trump pushback)" (Jun 12-14) → **✅ "SIGNED Wed Jun 17 (Pezeshkian + Trump, electronic per Al Jazeera) — initial agreement, Hormuz reopening process begun Day 110, verification leg OPEN" (Jun 17-18).** Signing-binary resolved; channel near-term dormant pending implementation (NOT formally closed). Remaining watch is verification-leg execution (demining, insurance, traffic normalization, Oman fee-administration, HEU dilution, sanctions-waiver rollout) + re-escalation risk (Israel-Lebanon/Gaza unresolved).

---

*Pruning rule: events older than 1 week get ✅ and removed at next update. Keep under 50 lines of active events.*

---

## ✅ RECENTLY RESOLVED (pruned next update)

| Date | Event | Outcome |
|---|---|---|
| Wed Jun 10 | ✅ **US CPI (May) — Fed-side gate** | **HOT-AS-EXPECTED.** Headline 4.2% YoY (vs 3.8% Apr; exactly consensus; 3rd consecutive acceleration; energy +23.5%, gasoline +40.5%), core 2.9% in-line, core MoM +0.2% mildly soft vs 0.3% exp. The market-moving soft-surprise tail did NOT fire → Fed-side gate closed per pre-registration; USDJPY flat ~160.4 through print; no SAM re-marks. **Adjacent find at resolve-time: Fed pricing has regime-flipped cut→HIKE (Polymarket ~52% 2026 hike; Oct frontrunner ~50%) — folded into STATUS SECONDARY PATH + Sat Jun 13 re-mark scope.** |
| Sat Jun 6 | ✅ **CFTC residual-gate re-check (Jun 2 data)** — SAM-internal | **METHOD gate resolved AGAINST cover.** Net -129,567 (vs -114,667 May 26; +14,900 WoW shorts). 72.0% of cycle peak (vs 63.7% prior). 5th consecutive build week. Amplifier STAYS +5pp ON, residual STAYS ON. Fuel load growing INTO Jun 16 catalyst, not covering. Next print Sat Jun 13 (last pre-blackout). |
| Mon Jun 8 | ✅ **Japan Q1 GDP — 2nd/revised estimate** | **Headline-soft mechanism-firm.** Revised to **+1.8% ann** (vs +2.1% prelim, −0.3pp). Composition: private consumption UP (0.35% vs 0.27%); capex DOWN (−0.7% vs +0.3%). BOJ-relevant lever (consumption) firmed; no USDJPY reaction; Polymarket BOJ Jun 16 didn't retrace. Non-blocking for Jun-9 SAM-21 mechanical trigger. |
| Wed Jun 10 (JST) | ✅ **JGB 30Y auction (Issue #90 reopening)** | **🟠 SOFTENING, not stress — graded on the pre-registered curve.** BTC **2.936x** (vs 3.115x Apr-7 tap of same issue), tail **2.8bp** (vs 1.3bp Apr — doubled), WA yield 3.860% (+16bp concession vs Apr's 3.697%; spot 3.823% Jun-9 pub). Above the 2.5x stress line and far above the 2.0x 🔴 cross-agent trigger → **no same-night route**. Curve-grade: demand deteriorated on both axes DESPITE the taper-pause leak tailwind (which should have improved demand at the margin) → reads softer than raw numbers; consistent with continued lifer absence at the long end, NOT an escalation to "abandonment confirmed" (needed BTC <2.5x + wide tail conjunction). SAM-26 not re-lit. Mention to LIQUID in next routine sync. |
| Tue Jun 9 | ✅ **SAM-21 mechanical trigger FIRED** — SAM-internal | **Pre-registered Jun 3 trigger CLEANLY FIRES → SAM-21 70% → 75%.** Polymarket 98.2% (+1.9pp vs Fri; 5th sequential ≥90%; volume $403K vs $304K). Takaichi/cabinet pushback NONE. **First real-time application of KB-185 / [[finding_thin_liquidity_prediction_market_discipline]].** |
| **Wed Jun 10** | ✅ **Ueda hospitalized — misses Jun 16 MPM** | **First sitting Governor to miss MPM since 1998 framework.** Infected hepatic cyst, ~2wk stay; Himino chairs, Uchida presses, Ueda written-no-vote. 5-source primary verified. Polymarket/swaps held 96%+ through news → guidance-clarity risk via Uchida-presser, NOT hike risk. Detail in STATUS § BOJ ASSESSMENT § GOVERNOR UEDA ABSENT. |
| **Jun 10-11** | ✅ **US-Iran kinetic 2-day strikes + Dawn #5 settlement** | CENTCOM/IRGC mutual strikes; Iran declared Hormuz CLOSED; Trump CANCELLED threatened Jun-11-PM round late Jun 11 on Dawn #5 announcement (60-day ceasefire ext + Hormuz-reopens-on-signing + 15-20d window). Kinetic NOT ceased — drone/vessel exchange Jun 12 AM. |
| **Thu Jun 12** | ✅ **14-pt Pakistan-mediated draft + Bessent signing-weekend (unsigned)** | Pakistan PM "final, agreed-upon text" incl. 30-day Hormuz reopen clause; Bessent: "signing weekend or Monday" 80% odds; Trump pushback "doesn't reflect agreed terms"; Iran has NOT confirmed (mediator/Bessent-sourced). |
| **Fri Jun 12** | ✅ **CFTC −145,818 release (Jun 9 data)** — SAM-internal | 6th build week; **81% of −180K cycle peak** (vs 72% Jun 2; +16,251 WoW). Amplifier +5pp ON, residual ON — **7,182 shy of −153K/85% escalation line**. No cover. Fuel maximally loaded into Tue Jun 16 binary. |
| **Sun Jun 14** | ✅ **Pre-blackout consolidated 6-input re-mark** — SAM-internal | (a) CFTC −145,818 + 81% amplifier state; (b) taper-pause hawkish-tail shrink; (c) Fed-anchor #4 → 0 matured; (d) SAM-21 75 → ~90 CH-009 applied (S4 void-gate clear: Polymarket 99.2%, swaps 93%, Bloomberg 49/51); (e) SAM-23 72 → ~30 CH-011 applied ($11 STEO upper-bound caveat); (f) Ueda absence integrated. **Carry-unwind buckets recomputed: ~14/37/49 → ~8/23/32** (shipped to LIQUID + HENRY). STRATEGY weights ~65/10/25 → ~80/10/10 (EV sign flip −0.11% → +0.60%). |
| **Sun Jun 14** | ✅ **Brent sub-$90 breach ($87.33)** | First sub-$90 close this cycle; cum ~−10% from $96.78. "Headwind resolved" tagged. Phase 1 oil pressure receding on diplomacy track + SPR drain-through (war-driven emergency authority → ~6mo runway per CRS R42460/EPCA). |
| **Wed Jun 17** | ✅ **FOMC HOLD UNDER NEW CHAIR WARSH — SEP +40bp on 2026 median dot (3.4→3.8); 9-of-18 see ≥1 hike** | Statement gutted ~300→~130 words, all forward easing bias removed. Core PCE 2026 +60bp to 3.3%. Warsh refused to dot himself; "no reason to revisit 2% target." DXY broke 100 (+1%), 2Y +16bp, USDJPY 160.78 Wed close → **161.34 Thu**. **Pillar 1 directional vector INVERTED** across Jun 16-17 sequence. CME July hike ~75%; Polymarket "Fed hike 2026" ~56%. Detail → STATUS § FOMC JUN 17 RESOLVED; CHANGELOG 2026-06-18 entry. |
| **Wed Jun 17** | ✅ **Iran/US deal SIGNED (Pezeshkian + Trump electronic per Al Jazeera; initial agreement) — Iran docket UNFROZEN on signing-binary; verification leg OPEN** | Pakistan PM Sharif "enters force immediately." Per CNN: this is an *initial* agreement; tougher talks lie ahead on the verification leg. Terms: **60-day toll-free Hormuz reopen, then Oman-administered fees**; US lifts naval blockade; Iran dilutes HEU; sanctions waived (not terminated); 60-day nuclear-negotiation window. Hormuz reopening process begun Day 110 — initial traffic resuming (4 supertankers transiting Thu Jun 18 incl. first Saudi-owned tankers since Day 1; backlog "weeks to clear"). Verification leg OPEN (demining/insurance/traffic normalization/Oman fee admin/HEU dilution/sanctions waivers). Brent $79.68 Thu (~−18% cum from $96.78 Jun-3): half deal-signing, half IEA glut warning (+8 mbpd by 2027 vs +2 demand) — durable bearish-oil regime developing independent of ME. |
| **Tue Jun 17 (JST ~7:50 PM ET Tue evening)** | ✅ **Japan May trade balance** | Deficit ¥-378.7B (vs ¥-564.6B consensus, beat by ~33%; first deficit in 4mo). Exports +17% YoY (autos+semis to US/China carrying it). ME crude volumes −57% YoY (Hormuz disruption); US crude +24%. **Branch (a) substantively confirmed** (deficit re-opens with Brent <$100) — but the export print is doing the heavy lifting, not the cost side → modestly counter-thesis to "Phase-1 fully back online." v1.5 CHANGELOG candidate (relabel April surplus as one-month volume-collapse spike) queued for v1.6. |

*Pruned next run (>1wk rule): Sat Jun 6 CFTC, Mon Jun 8 Q1 GDP, Tue Jun 9 SAM-21 fire — narrative lives in TIMELINE.md.*
