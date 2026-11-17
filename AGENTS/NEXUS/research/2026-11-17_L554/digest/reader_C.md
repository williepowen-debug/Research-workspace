# Reader C digest: FALCON, BRENT, RED, CORAL, MARCO

Read-only digest for NEXUS. All five briefs were read whole from the working tree. None of the five briefs had uncommitted changes (`git status` was clean for each). The baseline is 3db8291eff (2026-11-16 21:04 ET). Figures are copied as the briefs write them. "Undated" means the brief gives no date.

Brief commits since the baseline (`git log 3db8291eff..HEAD`):
- MARCO ab3278e9e5, 2026-11-16 21:28 ET
- RED 7bcfd11889, 2026-11-17 08:46 ET
- CORAL 7c3aea3c26, 2026-11-17 08:47 ET
- FALCON bc4550b642, 2026-11-17 09:44 ET (pinned d76d6e9568), then ae527a00a3, 2026-11-17 11:56 ET (pinned 9b62fc7ae6)
- BRENT 3bfbe07d7d, 2026-11-17 14:51 ET

Pin check (`python3 scripts/brief_pin_check.py`, run from the repo root). The fleet result was "BRIEF-PIN 1 STALE: 31 briefs; OK-PINNED 15, OK-SAME-COMMIT 10, STALE-PIN 3, UNPINNED 3". The lines for these five desks:
- ✅ BRENT OK-SAME-COMMIT: brief and STATUS were last committed together in 3bfbe07d7
- ✅ CORAL OK-PINNED: pin aa2ee5f29d = STATUS HEAD
- ✅ FALCON OK-PINNED: pin 9b62fc7ae6 = STATUS HEAD
- ✅ MARCO OK-SAME-COMMIT: brief and STATUS were last committed together in ab3278e9e
- ⚠️ RED UNPINNED: no STATUS hash in the first 40 header lines, so A11 cannot be checked. A10 fallback: brief commit 7bcfd1188 is BEFORE STATUS HEAD a1ce39979. That later commit is "RED: S66 closeout, board_log rotated, SCRATCH handoff, ML-333, charter line re-stated", 08:48 ET 11/17, two minutes after the brief.

A PASS proves the pin, not the content.

---

## 1. FALCON

**HEADER:** As of 2026-11-17, about 12:00 ET. STATUS commit `9b62fc7ae6`. Evidence cutoff about 16:50Z 11/17 (second C8 wake, PROME prome-19).
- Sources that returned 403: Bloomberg, ukmto.org, USNI and the JMIC PDFs.
- Sources reachable: the IMO table, NAVAREA IX, PortWatch, Anadolu, AP/PBS and gCaptain.
- Pin check: OK-PINNED.

**VIEW:**
- 11/17: pressure is on hulls near Musandam and on US sites in Bahrain, both below what FALCON's letters measure. No Gulf-ally crude production is stated lost and nothing in the rung's class has been hit.
- The regime question is a US reply (FAL-09) or a production hit; neither is in evidence. Marks B 1 / C 14 / D 85 are HELD; "held means no letter fired, not that D 85 was re-earned".
- The Qatar track is the live variable: a plan is on Trump's desk, terms are unconfirmed by any government, and only a signed, dated text confirmed by both sides moves the letters.

**MOVED SINCE 3db8291eff** (two commits, bc4550b642 and ae527a00a3):

Marks and letters:
- B 1 / C 14 / D 85 HELD, re-read twice on 11/17; no letter met.
- Losses 7. Census 7.
- FAL-08..12 OPEN to 12/31.
- FAL-09: 0 of 5. "11/16, 11/17 not strike days by its letter; a confirmation would make 11/17 day 1."
- Rung NOT FIRED; "Rung OUT" on hulls and radar.
- D→C NOT MET. FAL-12 not engaged (no authority says mine). FAL-08 not engaged (no stated crude loss; "TARA GAS is gas").
- No fire, grade or kill this window.
- GATE-FALCON-001: LIVE, leg 2 NOT MET, "last read 11/16, lowest 72.5%". Override NOT TRIGGERED. Next review 11/18. The baseline header had read "lowest 72.5% at 11/11, 93.7% at 11/15, vs ≤65%"; this is a wording change, not a new figure.

Retraction or supersession:
- KB-479 said "USS Theodore Roosevelt third carrier NOT ESTABLISHED: Changi 11/5, join vs relieve George Washington unresolved."
- It now reads "[11/17: ARRIVED 11/15, see top row; this cell was true at 11/13]". The new row says it "Supersedes the KB-479 'Roosevelt not established' row".

Attacks CONFIRMED (by an authority or the operator):
- **11/16, about 05:58Z:** outbound oil tanker hit by an unidentified projectile. Engine-room fire, crew safe (UKMTO 207-26). Name ON PHOENIX **PROBABLE** (NAVAREA IX 444/26, 2.4 NM E of Ras Hindi).
- **11/16, about 19:00Z:** LPG carrier TARA GAS, 7 NM N of Khasab, disabled, engine-room fire, drifting (NAVAREA IX 445/26). 25 crew safe (India's minister). Attacker and cargo NOT STATED for either hull.
- **IMO 138 / 25, as at 17 Nov,** adds AL DHANNAH 11/15 (Damaged). In the second wake: "IMO 138 unchanged", "NAVAREA IX newest 445/26" (own fetches).
- **11/17 drones on Bahrain:** CENTCOM says multiple one-way attack drones were intercepted, no damage, no injury. BDF says several aerial threats were destroyed. This is the third Iranian drone attempt on Bahrain in five days; the attempt is confirmed as intercepted.
- **USS Theodore Roosevelt arrived 11/15** (a US official via AP): "three carriers now". USNI says it relieves George Washington; which reading holds is NOT ESTABLISHED.

CLAIMS only:
- **11/17 Qeshm:** Iran says the US attacked several locations on Qeshm Island, no damage. Sources: Hormozgan deputy governor Nafisi to IRNA via CBS/AFP; Mehr; IRNA via Reuters, "five to six explosions Tuesday evening"; Fars, "one explosion, cause unclear".
  - FALCON: "No CENTCOM, Department or White House statement, no denial, no US official quoted, no independent evidence: CLAIM ONLY, US strike NOT ESTABLISHED."
  - "A Reuters headline citing an Iranian 'official' is an Iranian claim relayed."
  - ⚠️ "Unannounced US strikes are invisible to my sweep."
- **11/17 mines:** Iran's mine claims (one to three tankers, none named): CLAIM ONLY.
- **11/16 mines:** Iran claims four tankers mined and calls the southern route a "minefield of fire": CLAIM ONLY.
- **11/17 Isa Air Base:** the IRGC claims the radar was hit. CENTCOM says intercepted.

Measured flow change versus risk statements:
- **Measured:** the status line says "Hormuz transit count readable again: 2 a day at 11/15, DEEPENING." The baseline said "⚠️ Hormuz transit count unreadable (PortWatch now requires a token)". PortWatch is listed as reachable 11/17. The brief has no body row carrying this figure.
- No barrel loss is measured or stated. "no Gulf-ally crude production is stated lost".
- Bab el-Mandeb TankerMap (unchanged row, own read 11/16): 7-day 74 at 11/15, 93.7% of the prior week.

Combination tags and KB rows:
- combo:us-strike-preparations
- combo:mine-claim-vs-hull
- combo:gulf-host-state-fire
- KB-495..498, KB-499, KB-500, KB-502, KB-503..505

WATCH, added items: "US strike in reply to Bahrain; IMO rows for ON PHOENIX and TARA GAS; a neutral authority naming a mine; whether three carriers persist."

**CROSS-DOMAIN / CALIBRATION:**

Calibration (unchanged):
- FAL-07 CONFIRMED at 65%, "on a limited strike, not the campaign my posture evidence described".
- FAL-06 CONFIRMED at 70%, "route (c) never graded".
- 3C / 3F / 1P / 0V / 5 OPEN.
- Convergence 43/50, "saturated composite".
- Scale call (KB-402, undated within the row; row era 11/5): FAL-09 40%, FAL-10 12%, FAL-11 20%, all to 12/31.

Uncertainties:
- Unannounced US strikes are invisible to the sweep.
- "No Yanbu loadings reader here"; flows are BRENT's.
- Route (c) never graded, so FAL-06 is "not proof of no net loss".
- ⚠️ SPA text unread (Madinah).
- CENTCOM X unread.

Domains FALCON names as other desks':
- "Flow reading is BRENT's."
- "Petroline R1 is BRENT's."
- "BRENT owns the price read."
- "Polymarket legs resolved NO is ORACLE's and not an event grade."
- The ORACLE 11/05 reads are cited.

**FORWARD:**
- 2026-11-18: weekly scenario plus GATE-FALCON-001 review (needs current TankerMap bars and enforcement events); combination-themes review.
- 2026-12-31: FAL-08..12 resolve. The FORWARD table says "FAL-08..11"; the status line and NEXT DECISION POINT say "FAL-08..12".
- On event: a CENTCOM or White House line on Qeshm (a confirmed strike would make it FAL-09 day 1); a signed Qatar/US/Iran text; a Saudi MoE or Aramco damage statement at an IN-class plant (D 85→92); a NAVAREA IX or IMO RITI status update; a stated mine (FAL-12).

**NEXUS-NAMED** (verbatim): "| BRENT / NEXUS | KB-474 corrected to BRENT's Saudi October figure: EIA STEO 9.3 mb/d (survey 9.2); the 10.563 self-report is not BRENT's figure (closes NEXUS C3) | P2 | KB-489 |". Unchanged since the baseline. The CROSS-DOMAIN row for Lahij and Roosevelt routes "| 🟡 | NEXUS brief |".

---

## 2. BRENT

**HEADER:** "As of: November 17 closeout (2026-11-17 14:50 EST, from `date`; PROME wake prome-19) — MIXED-VINTAGE / SCOPED-PARTIAL."
- Re-verified ONLY the new November 17 SENDING row and NEXT DECISION POINT. Sources for that: vendor one-minute bars (09:33–11:51 and the 14:45 EST window capture), FALCON's two 11/17 grades (18868da6ce, 43e70832e5), and WALTER cards 001, 005, 006, 015, 016.
- Every other row carries its stated earlier vintage.
- No explicit STATUS hash appears in the header.
- Pin check: OK-SAME-COMMIT 3bfbe07d7.
- ⚠️ The **Status line is stale-vintage**: it still leads with EIA week 11/6, Brent January $91.49 on 11/10, the November 11 window, and COT #13 as of 11/3. It was not updated this window.

**VIEW:**
- Energy WAIT is retained. There is no measured barrel loss from the 11/16 Hormuz hits. "no oil line, gate or prediction moves; BG-02 NOT MET".
- The thesis split stands: crude loose, products tight (THESIS v5.13). The IEA 11/13 OMR surplus "is at sea" (land stocks lowest since at least 2016).
- The tape sold through the hits and partly rebounded. The front structure stays positive (BRT-33 not under +3.50).

**MOVED SINCE 3db8291eff** (one commit, 3bfbe07d7d; only the new SENDING row and NEXT DECISION POINT changed):

Attacks and claims, as relayed from FALCON:
- **Confirmed:** "Two tankers hit in Hormuz 11/16 (FALCON: ON PHOENIX probable, TARA GAS LPG disabled; attacker and cargo NOT STATED)".
- **Claims:** "Iran's Qeshm-strike and mine claims (CLAIM ONLY)".

Measured barrel or flow change: none.
- "no oil line, gate or prediction moves; BG-02 NOT MET".
- What would move oil: "a laden crude loss, a stated Gulf-ally production loss, or US-facilitated transits falling".
- Risk statement: "If TARA GAS sinks with cargo, BG-02 perimeter (LPG) goes to PROME for Will, not self-graded."

Price and structure (all EST vendor proxy, not settles):
- BZF27 95.67 → 92.43, window 11/16
- 93.86 at 09:33 ET 11/17
- 93.1479 at the 14:30 window 11/17
- **BRT-33 +5.0920 (11/17), valid 7 of 8, not under +3.50.** The baseline was +4.5200 (11/16), valid 6 of 7.
- M1−M2 +2.7662 against +2.3874

**Retraction:**
- "⚠️ I first flagged my invalidation item 4 met at the margin and withdrew it before closeout: +5.09 is inside the early-November range of about +3.76 to +6.33 (my own 11/5–11/8 TRACKER stamps)."
- The met-claim was in STATUS-side commit a6efd265ef (14:46 ET, subject "invalidation item 4 met at the margin"). It never reached the brief.
- Corrected in 3bfbe07d7d: "invalidation item 4 NOT met (correction of a6efd265ef)".

Tooling and procedure:
- "`cot_grade.py` browser identity removed (Blocked sites rule)."
- TERRY: "no investment implication, no packet (WQ-696 lines in both notes)".

NEXT DECISION POINT, rewritten. Friday 11/20, one session (PROME DOCKET row dated 11/20):
- BRT-33 eighth valid window [14:28,14:30) ET. Fallback 11/23 or later, before 11/27.
- COT #15 (as-of 11/17), about 15:30 ET, under G:GATE-BRENT-COT-35B, review_by 11/20. "plain client string, Socrata cross-check".
- Diesel and refining commission (DOCKET line 783).
- "outside-audit items 1–3" (new).

Carried, unchanged from the baseline (the 11/16 row was already in the baseline): COT #14 (as-of 11/10) JOINT NOT-SPENT, 8th consecutive.
- Shorts 122,378 (−3,276)
- OI share 6.3823% (−0.2008 points)
- Leg A 4,052 above the floor
- Leg B needs shorts at or under about 94,128

**CROSS-DOMAIN / CALIBRATION:**

Forecasts (11/5):
- BRT-32 Yanbu loading halt 20%
- BRT-33 F-a crossing by 11/27 20%
- BRT-34 distillate under 95M 45%
- BRT-35 retail under $4 70%, CONFIRMED 11/10 at 3.995, Brier 0.09

Live tension: EIA January spare 0.01 against Saudi-stated production 10.563 (implied room 1.2–1.3). The IEA OMR 11/13 "did NOT adjudicate it in any readable account (spare figure missing; Will's browser on the IEA Highlights page is the route)". Also "OPEC (2026 demand +0.18) against IEA (−2.7) and EIA (−2.0)".

ORACLE cross-domain (11/8): "the crowd prices about 76 for another US land strike within 14 days while its oil legs stay flat (ORACLE)".

Neither BRENT nor FALCON reads Yanbu loadings directly.

PortWatch waiting-for row (11/16, unchanged): "UNREADABLE-AT-SOURCE ... 'Token Required' (error 499; BRENT probe 16:23 EST; FALCON reported the same)". See the cross-brief section: FALCON now says it is readable.

Uncertain: D-78 VLO share scope, source freshness and access, delivered diesel, consensus vintage, and others (long list, unchanged).

**FORWARD:**
- 11/18 (Wed, modeled): WPSR week 11/13. BRT-31 week six qualifies at or under 8,890 kb/d (MET if week 11/13 ≤ 8,890 and weeks 11/13 + 11/20 sum ≤ 17,054). BRT-34 second print.
- 11/20 (Fri): BRT-33 eighth window; COT #15; diesel commission; outside-audit items 1–3.
- 11/27: BRT-33 deadline (F-a by 11/27).
- 11/29: OPEC+ January letter. Spare CONTESTED, IEA figure missing.
- 11/30 (Mon): COT #16 (Thanksgiving).
- 12/11: IEA December OMR.
- 12/14: OPEC MOMR (PDF via Will).

**NEXUS-NAMED:** NEXUS appears only as an addressee, in the 11/16 COT #14 row's To column: "PROME / TERRY / OSPREY / FALCON / HAWK / HENRY / NEXUS". No sentence names NEXUS.

---

## 3. RED

**HEADER:** "vS66 (2026-11-17 08:45 ET)". The brief carries no STATUS hash.
- Pin check: ⚠️ UNPINNED. The brief commit 7bcfd1188 is before STATUS HEAD a1ce39979 (S66 closeout, 08:48 ET).
- The thesis version line: S63 (2026-11-12) "vS66 11/17 moved no weight".
- The SENDING, WAITING-FOR and daily-monitor tables are stamped [2026-11-12]; they were not refreshed this window.

**VIEW:**
- HOLD 72, net-bear 67, unchanged; no weight moved. Stag 32, Managed 26, Acute 20, War 15, Soft 4, Rescue 3.
- The bear holds levels, not momentum. The new bear-relevant fact is a real-rate shock (not an inflation scare), which is BOND's to attribute.
- FT-06's exit is running again (2 of 5). If it completes on 11/19 it executes Stag +2 / Managed −2 mechanically.

**MOVED SINCE 3db8291eff** (one commit, 7bcfd11889; the whole status block was replaced, vS63 → vS66):

FT-06 exit run restarted, 2 of 5:
- VIXCLS 18.70 [11/12] and 19.30 [11/13] (FRED).
- Cboe **22.91 [11/16]** "indicates 3 (FRED cell unpublished at read; only VIXCLS completes)".
- Conditional: if 11/17 and 11/18 both close ≥18, the exit completes on the 11/19 read and executes **Stag +2 / Managed −2 mechanically (net-bear 67 → 69)**. A close under 18 on either day breaks it.
- Context: the baseline's vS63 showed the exit BROKE at 4 of 5 (17.49 [11/11]) and RED-29 WRONG. That was already in the baseline.

**CHG-RED-045 CLOSED (RESOLVED) 11/17:**
- "no reopen word from Will; the governing re-spec stands NOT FIRED (23bp of 100bp)."
- "On the official measure the evidence runs against CARL's household-credit thesis; CARL's to weigh."

Real-rate shock [FRED], 11/09 → 11/13:
- DFII10 2.66 → **2.91**
- DGS10 4.88 → **5.15**
- DGS30 5.26 → **5.47**
- DGS2 4.56 → 4.88
- 5y5y **2.15 [11/16]**. The baseline carried 2.15 [11/10].
- "Bull point 1 (expectations anchored) holds; the bear-relevant fact is the real leg, BOND's to attribute."

**Retraction of RED's own bull steelman:**
- "'real wages negative four straight months' fails on the current vintage."
- AHETPI was revised up: Aug −0.05 → **+0.01pp**, Sep −0.42 → **−0.33pp**. October is unreadable (no Oct 2025 CPI).
- VX-002 is held 20/80 by discretion, pending a vintage letter before 12/10.
- "Do not relay the four-month claim."

Tape:
- HY 323 / CCC 1,316 [11/13] (gap 993bp, "widest on RED's record")
- SPX 7,416.59 [11/16], under its 50-DMA 7,661, "after an Nvidia governance shock (WALTER 11/16)"
- SKEW 146.33 [11/16]
- OVX 49.59 [11/16, vendor]

Carried items:
- FT-08 HOLDS (3.66; exits 12/10 only on Nov core ≤0.0).
- CHG-057 MODERATE, re-review 11/19 ("Nvidia results 11/17 after the close are new input").
- CHG-054 MODERATE, 11/30.
- SoftBank own-basis 22.5% (SAM 11/11).

Dropped from the status block (were in vS63; now only in the rotated file `reports/2026-11-17_NEXUS_BRIEF_vS63_rotated.md`):
- The S63 discretionary move detail.
- The DEWEY bank-population caveat: "$10–100B band did NOT worsen ... Do not relay as uniform bank deterioration".
- The non-session FRED ICE OAS cells caveat (HY 330, CCC 1,330, BB 193 dated 11/11).
- The FALCON marks note "1/14/85 unchanged [11/11]".

Internal staleness:
- The VIEW section still carries HY 334 [11/09] and CCC 1,311 [11/09], against the status block's HY 323 / CCC 1,316 [11/13].
- Daily monitors still say "FT-06 exit 0 of 5" [2026-11-12], against the status block's 2 of 5.
- The scorecard is still "generated count 2026-11-12": 14 CORRECT, 11 WRONG, 6 ACTIVE.
- "Open challenges: 6" still lists "045 household debt 11/17", although it is now CLOSED.

**CROSS-DOMAIN / CALIBRATION:**

Uncertain about:
1. Whether the 12/9 Fed goes 50, and what that does to the AI-funding edge.
2. Whether paper oil's fall is de-escalation or deal hope that flows contradict.
3. Whether the FRED cell dated 11/11 is the 11/10 session relabelled (LIQUID's call).

Domains RED names as other desks':
- "CARL's to weigh" (household credit).
- "BOND's to attribute" (real leg).
- "LIQUID owns the 11/10 cell" (dropped with vS63).
- "Hormuz transits at a floor, BRENT" (VIEW, undated within the bullet; the bullet cites 11/9–11/11 events).
- "WL-11 Brent <95 price leg met (91.49 [11/10]), flow leg BRENT's".
- ORACLE odds: 12/9 +50bp at 11.8 (ORACLE 11/11); "pause by 11/15 54.5, WTI $110 in November 7.0".

War weight: VIEW "FALCON adopts two November 10 hulls, census 7, no rung". WAITING FOR: "FALCON weekly grade 11/18 → War weight".

Independence cautions:
- "the oil decline is one root (deal hopes plus Saudi supply); RED uses it once, on Stag."
- "Rates, banks and part of HY share one antecedent; count it once."

**FORWARD:**
- 11/17 and 11/18 VIX closes ≥18 decide the FT-06 exit, read on 11/19.
- 11/18: FALCON weekly grade (War weight).
- Thu 11/19: CHG-057 re-review; ING auction; NVIDIA 10-Q guarantee line. MODERATE → STRONG only on a qualifying fact.
- About 11/25: FT-10 outcome horizon.
- Thu 11/26: Thanksgiving (VIX bar bridged).
- Fri 11/27: VX-006 Zweig grade (tree due by 11/20).
- Mon 11/30: CHG-044 and CHG-054.
- 12/04: payrolls (next discretionary re-derivation).
- Wed 12/9: FOMC, 25 vs 50.
- Thu 12/10: November CPI. FT-08 exits only on core ≤0.0 (RED-28).
- Falsifiers: HY <300 ×3 un-fires FT-02 (−3 Acute); FT-12 <260; 5y5y >2.55 ×5 (FT-09).

**NEXUS-NAMED:** No sentence names NEXUS. The only reference is the footer: "Brief format follows the NEXUS_BRIEF schema (R3 + amendment 7)."

---

## 4. CORAL

**HEADER:** "As of: 2026-11-17 08:5x ET (Tue, coral-ah, due-row wake; MATERIAL: CORAL-02 graded FALSE, WQ-704 research delivered) | STATUS commit: aa2ee5f29d (prior: 2026-11-16 coral-ag, 8c9ef1ff6b)". Pin check: OK-PINNED.

**VIEW:**
- The thesis split holds: household and condo stress confirmed; bank-loss transmission NOT confirmed. The bank rail is NOT met, NOT armed.
- The GSE financing leg is "not yet". CORAL-02 is FALSE: condo financed sales fell less than single-family. The 2024–25 condo step-down looks like a condo-wide cost shock, not financing-specific.
- The supply-side MSI leg stays 🟠, 4 of 5 metros, with Cape Coral at a series low. Florida stress is localized (SW and Central FL), not statewide.

**MOVED SINCE 3db8291eff** (one commit, 7c3aea3c26):

Grade: **CORAL-02 FALSE (11/17)** at the first Florida Realtors October print.
- Financed (closed − cash) condo **3,266, −8.34%** vs single-family **13,502, −12.43%**.
- ⚠️ "Oct-2025 SF base strong (+12.2%), likely post-Milton rebound (inference)."
- Status: "GSE financing leg: 'not yet'".

WQ-704 research delivered: condo financed per 100 SF financed, Aug–Oct:
- 25.5 (2024)
- 23.3 (2025)
- 23.3 (2026)
- 12 months to Oct-2026: condo financed **+2.1% = SF +2.1%**; condo cash +9.7%.
- "condo-wide cost shock, not shown to be financing-specific."
- Blind spot: non-agency loans count as financed.
- "No investment implication"; TERRY "no card: stated in the research doc".
- File: `research/2026-11-17_WQ704_fl-condo-financing-channel.md`.

October Florida Realtors, condo:
- Median $290K −3.3% (mix toward cheaper units; under-$200K closings +5.1%)
- Original-list ratio 93.3% vs 92.3%
- 64 vs 76 days
- **8.0 months (9.3)**

October Florida Realtors, single-family:
- $420K +2.2%
- **4.6 months (5.1)**
- Pendings −15.7%
- Short sales 95 vs 48
- "MARCO copies months supply from CORAL."

Status-line changes:
- MSI reading #15 (11/15): 4 of 5, Cape Coral **5.74** series low, re-fire fails. The baseline status said #14 (11/10), Cape Coral 5.82. The baseline as-of line had already noted #15 and 5.74.
- "Falsify grade 11/15 run 11/16: 1.5 of 6, 🟠 holds." This was already in the baseline as-of line: bank half C1 HALF + C2 MET, household half 0 of 4.
- Next: MSI #16 by 11/26; FL Realtors November 12/16.

No colour moves; no kills.

**CROSS-DOMAIN / CALIBRATION:**

CROSS-DOMAIN routings:
- HOMER: one figure for the FL condo-SF read.
- REGINALD: no rail change.
- RED: "a CORAL leg tested and not confirmed".
- NEXUS: see NEXUS-NAMED.

Conviction (unchanged): mechanism-HIGH, bank-transmission-LOW until Q3, timing-MEDIUM (winter 2026-27 window).

11/11 confound: the December hike priced above one move (HENRY 11/10: +28.2bp; 10Y 4.98%). This moves condo-vs-SF financed sales apart with unknown sign, so L227 leg (a) "needs a national control".

Carried and older items that are not refreshed:
- CARL row: FL bankruptcy 225.9/100k, +21.3% YoY to 9/30/26, 1.256× US (read 10/29).
- MARCO row: "Reconcile CLOSED 10/10 — MARCO adopted ... months supply 7.7/4.3". Now superseded by October's 8.0 / 4.6; the row was not updated.
- MARCO WAITING-FOR row: "FL–Canada air seats winter 25-26 −17.67% ... are MARCO's".
- WATCH table is stale:
  - "by Thu 11/19 MSI-01 reading #14 ... Cape Coral 5.84 at #13", although #15 is already done.
  - "Mon 11/16 FL Realtors October", although it was consumed 11/17.
  - "Nov 15 / Nov 17 Falsify grade / Amendment 3 certified": no certification result appears in the brief.
- NEXT DECISION POINT still reads "late Oct → 11/15". It was not refreshed after the grade ran.

Uncertain and known errors: "Known errors this cycle (all corrected)". RED counter-frame: "if Q3 banks cure again and bankruptcy growth converges to the US rate, CORAL is a real-estate/demand story".

**FORWARD:**
- 11/17: Amendment 3 certification (no result shown).
- 11/20: L784 re-date proposed (DR-4955 Federal Register cost share).
- By 11/26: MSI #16.
- About mid-November: Citizens 10/31 month-end; Avidia 10-Q; OIR Isaias claims (68,071 / $735.5M at 11/06).
- November to December: FLDOE Survey 2.
- 12/11: NFIP authorization ("Lapse = FEMA stops writing").
- 12/16: FL Realtors November.
- 12/31: Call Report (BKU).

**NEXUS-NAMED** (verbatim):
1. "| NEXUS | Geography read: statewide firming vs SW/Central-FL MSI still above 6.00 in four of five metros, edging down — the stress is localized, not statewide | 🟠 | Synthesis should not treat FL as uniformly improving or uniformly breaking |"
2. "| 5 | **MARCO correction applied:** "MIA is the clean tell" WITHDRAWN (MIA also carried Spirit); one number = MARCO's MIA Sep −1.82% YoY, trigger MET, mechanism CONFOUNDED | NEXUS — check your own demand premise |"
3. In the new 11/17 WQ-704 row's So-what column: "TERRY (no card: stated in the research doc), HOMER, NEXUS".

---

## 5. MARCO

**HEADER:** "As of: 2026-11-16 21:28 ET (session 41, PROME doorbell + post-restart recovery; closeout). **STATUS commit:** folded in the same commit as this brief." Pin check: OK-SAME-COMMIT ab3278e9e. The brief committed 24 minutes after the NEXUS baseline.

**VIEW:**
- Channel 2 (Canada) is the strongest transmitting channel. ID-01 is IDENTIFIED 11/16: after the 9/8 counter-tariffs, Canadian car trips fell further behind flights. Canadian 2-yr Oct −26.88%, BREACHED 12th month.
- Florida demand is unidentified but overseas visitors are holding (Sep −1.21% vs national −4.33%). The fare stage (ENR-02) is transmitting into the winter booking window.
- Channel 1 (labor) stays split until the 12/4 November jobs survey grades SDL-01.

**MOVED SINCE 3db8291eff** (one commit, ab3278e9e5):

**ID-01 IDENTIFIED 11/16** on the pre-committed both-months letter:
- Land−air gap Sep −12.41 / Oct −9.34pp vs Aug −4.72; air improved, land worsened.
- ⚠️ "Oct's move alone is inside the pre-tariff range."
- Canadian 2-yr Oct **−26.88%**, BREACHED 12th month. The SENDING row says this "replaces CORAL's Aug −26.63%".
- Basis: StatCan; the brief does not name the release here.
- Earlier, the baseline NEXT DECISION POINT required "an October gap move ≤ −2.5pp from the August −4.72 baseline (September met, −7.69pp)". The September figure now reads −12.41. The brief gives no explanation of −7.69pp vs −12.41; it may be a different measure (move vs level). Flag for the owner; not inferred here.

**MAR-11 CONFIRMED:** H-2A FY2026 **435,980** certified (+9.55%). Florida is now the #1 worksite state (**62,425**). Date: the status line says 11/16 (commit subject).

Florida overseas visitors (NTTO Prelim): first-address Sep **−1.21%** / YTD **−0.68%**, vs national **−4.33% / −5.67%**. "holding".

Two new SENDING rows dated 11/16 s41:
- To CORAL, "Florida overlap": Canadian 2-yr Oct −26.88%; FL overseas Sep −1.21% / YTD −0.68%; "Citizens one figure" (no figure given in MARCO's brief); "FAA ground-stop November confounder"; "FL #1 H-2A state 62,425". "CORAL wakes 11/17."
- To PROME, doorbell return: ID-01 IDENTIFIED, MAR-11 CONFIRMED, VX refreshed; WQ-696 lines ("no investment implication named, reasons given"); "WQ-678 held for Will's own word".

Removed from VIEW without a retraction label:
- "Existing-series refresh: ... BEA nominalSA Travel actual trailing12months throughAugust shows−$3.125B,ELEVATED ..."
- It was deleted, not marked as superseded, and no replacement figure is given.
- The Las Vegas bullet was merged into the AZ-01 bullet (content unchanged).

NEXT DECISION POINT is now SDL-01, the November jobs survey, on 12/4 (BLS schedule).
- Falsifier: "November foreign-born labor force YoY a decline ≥250K ⇒ September's flip was noise".
- MAR-29 at 90% says it will not.

Unchanged context figures (11/11):
- ENR-02 SUSTAINED: Oct 327.822 vs Oct-24 265.939 = +23.27% 2-yr (Sep +26.36%).
- Foreign-born labor force 33,121k, +842K m/m.
- AZ-01 Oct +35.3pp CRITICAL.
- Remittances Sep count −6.27%.

**CROSS-DOMAIN / CALIBRATION:**

Conviction: direction HIGH, timing MEDIUM, magnitude LOW. No thesis-version change (v3.2).

Uncertain about:
- Later LAS filings (MARCO/BTS)
- January CPS control size (LABOR)
- "current source-comparable Florida migration (CORAL)"
- H-2A later court state and new rates

Cross-agent tensions it lists:
- "CORAL's live STATUS/brief carry the superseded MIA clean-tell premise; correction packet saved through WALTER, consumption pending."
- WAITING-FOR: "CORAL currently calls MIA the clean tell."
- ⚠️ This is **stale relative to CORAL's brief**, which already says "the 'MIA clean tell' is WITHDRAWN (MARCO 10/25)" (row dated 10/29).
- "FL migration divergence remains documented-not-merged."

REGINALD: the FL winter 2026-27 loss estimate is "⛔ unsupported/retracted-pending, do not model it" (older row).

**FORWARD:**
- 11/17–21: Amendment 3 certification; CA second check; state BLS; MIA October report (the MIA trigger; "November carries the ground stop").
- 12/3: H-2A court reports (11/12 + 12/3).
- About 11/30 to 12/4: NTTO October, BTS August, LVCVA October, Banxico October, November CPS, AZ-01. Covers VX-1.02 and MAR-30, MAR-28, MAR-29.
- 12/4: SDL-01 grade.

**NEXUS-NAMED** (verbatim, older row, unchanged): "| NEXUS | Channel-1 re-instrumentation is a **measurement** change, not a direction change — and the s32 `SDL-01` flip is one print, not a reversal | 🟡 | Avoids reading either as a thesis reversal |"

---

## CROSS-BRIEF (at most 10 lines)

1. **PortWatch / Hormuz transits: DISAGREE.** FALCON 11/17 says "Hormuz transit count readable again: 2 a day at 11/15, DEEPENING; PortWatch reachable". BRENT's WAITING-FOR row (11/16, not re-verified 11/17) says "UNREADABLE-AT-SOURCE ... 'Token Required' (error 499) ... FALCON reported the same". RED VIEW says "Hormuz transits at a floor, BRENT" (11/9–11/11 era).
2. **11/16 Hormuz hulls: AGREE.** FALCON says ON PHOENIX PROBABLE, TARA GAS disabled, attacker and cargo NOT STATED, census 7, no rung. BRENT relays the same and adds "no oil line, gate or prediction moves; BG-02 NOT MET". Qeshm 11/17 is CLAIM ONLY on both.
3. **Brent January (BZF27): consistent, different vintages.** BRENT: 95.67 → 92.43 window 11/16; 93.86 09:33 ET 11/17; 93.1479 at 14:30 11/17 (EST vendor proxy). RED cites only "91.49 [11/10]" (BRENT's settle) and OVX 49.59 [11/16].
4. **Saudi October output: AGREE.** FALCON KB-489 says EIA STEO 9.3 mb/d (survey 9.2), "10.563 not BRENT's figure". BRENT says OPEC secondary 9.194, EIA 9.3, survey 9.2 (11/11).
5. **War weight input: no disagreement.** RED waits for FALCON's 11/18 weekly grade. FALCON holds B 1 / C 14 / D 85, review 11/18. RED's brief no longer carries a dated FALCON mark (the "1/14/85 [11/11]" line was dropped with vS63).
6. **Canadian 2-yr visitors.** MARCO says Oct −26.88% "replaces CORAL's Aug −26.63%". CORAL's brief carries neither figure (grep: no match), so there is no visible conflict but also no visible consumption. CORAL's VIEW defers tourism to MARCO.
7. **Months supply: STALE ROW, not a live conflict.** CORAL Oct condo 8.0 / SF 4.6 (11/17) says "MARCO copies months supply from CORAL". CORAL's MARCO row still says "MARCO adopted ... 7.7/4.3" (10/10 to 10/15). MARCO's brief carries no months-supply figure.
8. **MIA clean tell: MARCO is stale against CORAL.** MARCO's WAITING-FOR and CALIBRATION say CORAL "currently calls MIA the clean tell". CORAL's brief says WITHDRAWN (MARCO 10/25), with MIA Sep −1.82% matching MARCO's 10/28 figure.
9. **Amendment 3: AGREE** at 61.98% unofficial (CORAL and MARCO). Both list 11/17 certification; neither brief reports the certified result. **Citizens:** CORAL 215,397 at 11/06. MARCO says "Citizens one figure" with no value shown.
10. **Rates.** RED: DGS10 5.15, DGS2 4.88 [11/13 FRED]. CORAL cites "HENRY 11/10: +28.2bp; 10Y 4.98%" (an older vintage, not a conflict). RED says CHG-045 evidence "runs against CARL's household-credit thesis", while CORAL tells CARL that FL bankruptcy is "+21.3% YoY ... widening" (to 9/30). These are different measures (national household credit vs FL filings), so it is a tension for CARL to reconcile, not a figure clash.

Could not read: nothing. All five briefs and diffs were read in full.
