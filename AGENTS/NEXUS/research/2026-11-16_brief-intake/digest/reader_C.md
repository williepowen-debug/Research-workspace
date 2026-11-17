# Digest reader C: 10 briefs (BRENT FALCON OSPREY YURI AEOLUS WATT VULCAN ZHAO CYPHER MIDAS)

Reader: read-only digest reader for NEXUS (Claude, Opus). Run start 2026-11-16 20:58 EST, file written 2026-11-16 21:00 EST (both from `date`). Every brief was read whole from the working tree. None of the 10 briefs or their STATUS.md files show ` M` or `??` in `git status --short`, so the working-tree copy equals each desk's committed HEAD version.

Baseline for "moved since" = the last commit at or before 2026-11-10 11:19 ET (`git log -1 --before`), diffed against the current file.

## Pin check (verbatim)

```
BRIEF-PIN 0 OK: 10 brief(s) checked against amendment 11 (pin-follows-STATUS-HEAD) — OK-PINNED 4 · OK-SAME-COMMIT 6. A PASS proves the pin, never the brief's content; UNPINNED briefs are not A11-checked.
  ✅ BRENT     OK-SAME-COMMIT  brief and STATUS last committed together in baf1a5b7c
  ✅ FALCON    OK-PINNED       pin f6c07361db = STATUS HEAD
  ✅ OSPREY    OK-SAME-COMMIT  brief and STATUS last committed together in f512dd012
  ✅ YURI      OK-SAME-COMMIT  brief and STATUS last committed together in 8389e02f8
  ✅ AEOLUS    OK-SAME-COMMIT  brief and STATUS last committed together in 21515129a
  ✅ WATT      OK-PINNED       pin b03bd802a1 = STATUS HEAD
  ✅ VULCAN    OK-PINNED       pin 4d0dbcebd8 = STATUS HEAD
  ✅ ZHAO      OK-SAME-COMMIT  brief and STATUS last committed together in bb54d1486
  ✅ CYPHER    OK-PINNED       pin ba365a70d961b42e74bb9f1493eb048be369496b = STATUS HEAD
  ✅ MIDAS     OK-SAME-COMMIT  brief and STATUS last committed together in 1d561a14b
```

## Commit times and sizes

| Desk | Brief last commit | STATUS last commit | Baseline commit | Brief bytes | Working tree |
|---|---|---|---|---|---|
| BRENT | 2026-11-16 16:30:01 -0500 | 2026-11-16 16:30:01 -0500 | 8cf784d32e | **24,103 (over 22 KB)** | clean |
| FALCON | 2026-11-16 13:59:10 -0500 | 2026-11-16 13:59:03 -0500 | 5ea23794c0 | 20,102 | clean |
| OSPREY | 2026-11-14 11:42:03 -0500 | 2026-11-14 11:42:03 -0500 | 1489e2eddd | 16,679 | clean |
| YURI | 2026-11-11 09:44:01 -0500 | 2026-11-11 09:44:01 -0500 | 850427799b | 13,581 | clean |
| AEOLUS | 2026-11-11 09:46:09 -0500 | 2026-11-11 09:46:09 -0500 | f908dc61e9 | 3,411 | clean |
| WATT | 2026-11-16 14:24:44 -0500 | 2026-11-16 14:24:27 -0500 | aba50f8dd4 | 16,875 | clean |
| VULCAN | 2026-11-16 13:57:30 -0500 | 2026-11-16 13:53:55 -0500 | 3ec4146094 | **23,484 (over 22 KB)** | clean |
| ZHAO | 2026-11-16 14:18:03 -0500 | 2026-11-16 14:18:03 -0500 | 2cbc0f65d4 | 15,551 | clean |
| CYPHER | 2026-11-16 16:04:28 -0500 | 2026-11-16 16:04:16 -0500 | fe7bd20744 | 18,579 | clean |
| MIDAS | 2026-11-14 16:13:42 -0500 | 2026-11-14 16:13:42 -0500 | f9c4a3028f | 20,370 | clean |

Stale as-of dates (5 days or more behind 11/16): **YURI (11/11), AEOLUS (11/11)**. OSPREY and MIDAS are 2 days old (11/14).

---

## BRENT

- **HEADER:** "As of: November 16 closeout (2026-11-16 16:3x EST, from `date`; PROME assignment prome-6f) — MIXED-VINTAGE / SCOPED-PARTIAL: re-verified ONLY the new November 16 SENDING row, the PortWatch WAITING-FOR row and NEXT DECISION POINT". Pin: none in the brief; brief and STATUS committed together (baf1a5b7c). Thesis v5.13.
- **VIEW:** Energy WAIT. Crude is loose and products are tight (a second agency, the IEA, now agrees); the 11/13 IEA surplus is "at sea" (October oil on water +86 mb, land stocks about −34 mb). Strikes and claims around Saudi and Gulf assets have not removed a measured barrel; the market prices bypass risk before loss.
- **MOVED SINCE baseline (11/10 10:12 EST closeout):**
  - Status line: EIA week 11/6 (read at primary 11/12): commercial crude +4.657M to 414.417M, distillate +4.071M to 103.330M (8% below 5-yr), refinery utilization 95.2% [CONF EIA]; replaces week 10/30 distillate 99.259M (now "the low"). Brent January settled $91.49 on 11/10 [EST vendor daily row, relay match], replacing $98.32 on 11/6. Window proxies 11/11: BZF27 92.7234, CLZ26 86.4586, M1−M3 +3.8713 [EST vendor, not settles]. Saudi October crude to the market 9.194 mb/d [CONF MOMR 11/11 Table 5-7].
  - **11/16 row:** COT #14 (as-of 11/10) JOINT NOT-SPENT, 8th consecutive, raw CFTC file posted 15:33:41 ET: shorts 122,378 (−3,276), OI share 6.3823% (−0.2008 points). BRT-33 window +4.5200, valid 6 of 7. BZF27 window 92.43 vs 95.79 on 11/13 [EST vendor proxy]. Bahrain drone attempts 11/13 and 11/15 intercepted; no barrels lost. Russian diesel-export drop (Bloomberg title) and Omsk/Volgograd strikes (about 36 Mt/yr nameplate, no halt) logged, not met. PortWatch needs a token.
  - **11/14 row:** IEA OMR (11/13) via five secondaries, iea.org not read: Q4-26 +1.7 mb/d surplus is a FORECAST vs EIA +1.47. October world stocks +52 mb, oil on water +86 mb, land about −34 mb (own arithmetic). Dated Brent 92.14 vs 92.76 on 11/11 [FRED]. IEA spare NOT FOUND.
  - **11/13 row:** Houthi claim on East-West Pumping Station 7 and Yanbu = CLAIM ONLY. Settle proxy BZF27 92.76 → 95.82 (+3.30%), M1−M3 +3.87 → +4.24; 11/13 window 95.7853, M1−M3 +4.9903 [EST vendor proxy, CME 403]. **Correction:** COT #14 delayed by Veterans Day to Mon 11/16 ("my 11/13 date was wrong").
  - **11/12 row:** WPSR as above; refinery utilization 95.2%, "TRACKER line 3 CROSSED"; crude exports 3.455 mb/d (−220 kb/d). **BRT-31** week five −1.0346%, non-qualifying, "NOT MET is no longer reachable (OPEN 40%)". **BRT-34** first print 103,330, 8,330 above 95,000 (OPEN 45%). CATO M12-4 withdrew an earlier holiday caveat.
  - **11/11 row:** Saudi October crude to market about 9.2 on every measure (OPEC secondary 9.194, Saudi supply 9.203, EIA 9.3, survey 9.2); 10.563 is Saudi-stated production with +1.36 to storage. EIA 2.5 mb/d Middle East shut-in CONFIRMED on the level. **CONTESTED:** BRENT's own 11/10 "a January OPEC+ increment is paper". Window M1−M3 +3.8713.
  - **11/10 row:** BZF27 settled 92.57 on 11/9, low 89.15 on 11/10 [EST wire, vendor]. STEO 11/10: Q4-26 balance from a 0.69 mb/d draw to a 1.47 mb/d build; COPS_OPEC 0.01 [CONF EIA]. **BRT-35 CONFIRMED**, GASREGW 3.995 (11/9); calibration adds Brier 0.09. Window c1 14:46 EST M1−M3 +3.7552; January 3:2:1 $37.02; December crack $87.44; WTI−Brent −$6.60 [EST vendor proxy]. Petroline hit near Madinah 11/9, operations unaffected (SPA).
  - WAITING: WPSR now Wed 11/18 (modeled); the BRT-31 rule is now written as "at or under 8,890 kb/d" for week 11/13 and a two-week sum "at or under 17,054" (previously stated as two prints at or under −1.5%; same letter in a different unit, not reconciled in the brief). PortWatch row: "UNREADABLE-AT-SOURCE" (ArcGIS error 499, probe 16:23 EST), replacing "UNRESOLVED, date UNKNOWN".
  - Rotations: the 11/4 and 11/5 SENDING rows went to archive 2026-11-12 (crc32 `a9dd940d`); the 11/14 as-of entry went to archive (crc32 `6b70debe`).
- **CROSS-DOMAIN / CALIBRATION:** To TERRY: sizing modifier at base case, no entry implication. To FALCON/HAWK: the Bab shore is a risk to Yanbu's Asia-bound exit, not a closure. To OSPREY: strikes read as capacity, not barrels, until a halt or export volume is reported. CARL owns the retail-under-$4 read. FALCON owns attribution. "Neither BRENT nor FALCON reads Yanbu loadings directly." Tensions: EIA January spare 0.01 vs Saudi-stated 10.563 (implied room 1.2–1.3), not adjudicated by the IEA (spare figure missing); OPEC 2026 demand +0.18 vs IEA −2.7 and EIA −2.0. Uncertain: delivered incremental diesel, strike offsets, source access (CME 403), issuer margin capture, holding-source grade.
- **FORWARD:** COT #15 (as-of 11/17) Fri 11/20 about 15:30 ET (G:GATE-BRENT-COT-35B, review_by 11/20); COT #16 Mon 11/30. BRT-33 window every session through 11/27 (8 valid needed). WPSR week 11/13 Wed 11/18 (modeled): BRT-31 week six, BRT-34 second print. Diesel and refining commission Fri 11/20 (DOCKET line 783). OPEC+ January letter 11/29. IEA December OMR 12/11; OPEC MOMR 12/14.
- **NEXUS-NAMED:** "| PROME / TERRY / OSPREY / FALCON / HAWK / HENRY / NEXUS | **November 16:** **COT #14 (as-of 11/10) JOINT NOT-SPENT, 8th consecutive** at the raw CFTC file ..." (recipient cell of the 11/16 SENDING row). No other line names NEXUS.
- **FLAGS:** Over 22 KB (24,103 B). The Status line is not current with the body: it still says "COT #13 NOT-SPENT, 7th ... as-of 11/3" while the 11/16 row reports COT #14, and its price sentence stops at 11/11 while the body has 11/13 and 11/16 marks. The as-of line discloses that only three rows were re-verified, so this is disclosed mixed vintage, but the headline line is stale. Glued words: "October26 supersedes the October21", "relayed14mb/d", "Kpler24.6", "prior95.0479", "October22 card", "October23 pair".

## FALCON

- **HEADER:** "As of: 2026-11-16 13:59 ET | STATUS commit: `f6c07361db` | Evidence cutoff about 18:55Z 11/16; ukmto.org and JMIC PDFs 403; GitHub unreachable from this box (commits local); PortWatch chokepoints 499 Token Required".
- **VIEW (Status line, current):** 🔴 B 1 / C 14 / D 85 HELD, re-read 11/16 against Iran's drone attempts on US sites in Bahrain (11/13, 11/15, both intercepted) and the Yemeni government pullback from Bab el-Mandeb (11/15): no letter met. Losses 7. GATE-FALCON-001 LIVE, leg 2 NOT MET.
- **MOVED SINCE baseline (11/9 10:55 ET):**
  - Bahrain: 11/13 IRGC claims a US radar destroyed; CENTCOM says two drones shot down, no damage. 11/15 IRGC six drones at the Riffa base radar; Bahrain says intercepted. "First Iranian targeting of Bahrain since September". Rung OUT; D→C NOT MET; FAL-09 0 of 5 (KB-483..485, KB-490).
  - Bab el-Mandeb: Yemeni government forces pulled back from Dhubab 11/15; Houthis hold the shore. Own TankerMap 11/16: Bab 7-day 74 at 11/15, 93.7% of prior week; gate override NOT TRIGGERED; leg 2 NOT MET, "lowest 72.5% at 11/11" (KB-486, 487, 491).
  - IMO 137 / 25 as at 16 Nov: damaged TARIF 11/7, FUJAIRAH ENERGY 11/10, DOMINICA PROSPERITY 11/11, DAR SALWA 11/13; no new sinking; census 7. **Correction:** 199-26 is NAVIG8 MACALLISTER ("the NAVIG8 MESSI OSINT ID below was wrong"). 11/10 settled as two distinct hulls.
  - **Correction KB-474 → KB-489:** Saudi October figure corrected to "EIA STEO 9.3 mb/d (survey 9.2)"; the 10.563 self-report "is not BRENT's figure (closes NEXUS C3)".
  - Houthi claims on Saudi bypass route (Pumping Station 11 on 11/11; Pumping Station 7, "Yanbu oil facility", Aramco Riyadh 11/12) graded 11/13: CLAIM ONLY. Only 11/9 Madinah confirmed (state; operations unaffected; attacker not established). D 85→92 NOT FIRED (pipeline is a route, out of class).
  - Qatar track 11/9–11/10: Trump holds off new strikes, keeps the blockade; FAL-10 and ladder item 5 NOT MET; Diplomacy 3.
  - GATE-FALCON-001 review 11/11: Bab 7-day 75 at 11/10, 94.9%; next review 11/18 (was 11/11).
  - USS Theodore Roosevelt third carrier NOT ESTABLISHED.
- **CROSS-DOMAIN / CALIBRATION:** Flows and the Yanbu loadings read are BRENT's ("⚠️ No Yanbu loadings reader here"); priced odds are ORACLE's. Calibration: FAL-07 CONFIRMED at 65%, FAL-06 CONFIRMED at 70% (route (c) never graded); 3C / 3F / 1P / 0V / 5 OPEN; "Convergence 43/50, saturated composite". Uncertain: no CENTCOM 11/15 statement; UKMTO and JMIC unreadable (403); Hormuz transit count unreadable (PortWatch token).
- **FORWARD:** 11/18 weekly scenario + GATE-FALCON-001 review + combination themes review. 12/31 FAL-08..12 resolve.
- **NEXUS-NAMED:** "| BRENT / NEXUS | KB-474 corrected to BRENT's Saudi October figure: EIA STEO 9.3 mb/d (survey 9.2); the 10.563 self-report is not BRENT's figure (closes NEXUS C3) | P2 | KB-489 |"
- **FLAGS:** The VIEW section is the 11/9 vintage ("The live variable is the Qatar track: a plan is on Trump's desk"; "the war did not pause over the weekend") and does not mention the Bahrain drones or the Bab pullback that the Status line now leads with. WAITING FOR table not refreshed since 11/9. "Lowest 72.5% at 11/11" appears only in the Status line; the 11/11 review row gives 94.9% at 11/10, so the 72.5% point has no row behind it in the brief. Attribution of BRENT's Saudi figure differs from BRENT's own headline (see cross-brief).

## OSPREY

- **HEADER:** "As of: 2026-11-14 (Sat) 11:41 ET (from `date`; osprey-1114, PROME prome-fe drain + follow-up) | STATUS commit: `5a1b7f27ed`".
- **VIEW (Status line):** Elevated, active Russia/Ukraine energy campaign; scores 5 / 5 / 3 unchanged. Will ruled the Ust-Luga 11/11 hit counts for C2 (WQ-669 A; earliest re-kill 12/11). Omsk 11/11 and Volgograd 11/13 refinery strikes rowed; C1 step-down earliest 11/27.
- **MOVED SINCE baseline (11/9 12:11 ET):**
  - **Ruling:** WQ-669 A (Will, 11/11 10:01 ET): Ust-Luga 11/11 port-zone hit COUNTS for C2. C2 clock 3/30 on 11/14, earliest re-kill 12/11 (was 11/17). OSP-08 "expected FAILED at 11/20". General Staff claim of 5 tanks (150,000 m3) and a hydrocracker damaged, unverified; no loading halt found (KB-282, 288).
  - Refineries: Omsk (Gazprom Neft, about 21 Mt/yr) 11/11, special forces confirm; Volgograd (Lukoil, about 15 Mt/yr) 11/13, governor confirms 4 killed, General Staff claims four crude units hit (unverified). Eight November refinery rows vs Bloomberg's nine. C1 1/30; leg A earliest 11/27 (was 11/23). CAPACITY, not barrels (KB-287).
  - 11/11 block: Reuters 11/10 (two unnamed industry sources): about 30% of refining capacity disrupted, nine of 35 plants, processing about 700k → 500k t/d; desk conversion about 3.7 M bpd, runs proxy about 31–34%, inside the ~30% band (B3; band not moved). Bloomberg 4-week crude 3.63 M bpd to 11/8, Kozmino paused (KB-277, 278). Abu Dhabi talks did not change strike tempo (KB-279).
  - C3: unverified "unprecedented" Black Sea war-risk headline (finway 11/11) is a lead, not evidence; earliest kill 11/27 (KB-286).
  - Clocks 11/14: C1 1/30 (leg A 1/14) · C2 3/30 · C3 39/21, limb-2 window 8/21.
- **CROSS-DOMAIN / CALIBRATION:** Prices are BRENT's; HAWK grades C3. Combination watch: Trump, Putin and Xi meeting after 11/19 has Ukraine off the agenda; the US raised NATO membership for leaving Donbas (KB-283). "The diesel headlines conflict ("doubled" FT 11/12 vs "drop" Bloomberg 11/13), and the IEA says Russian crude output rebounded; BRENT owns the figures." Calibration: conviction on products-impairment direction high, incremental lost volume low. OSP-07 OPEN (60%, refinery strike 10/30–11/15, graded on or after 11/18); OSP-08..11 OPEN. Uncertain: Kirishi 11/9 halt unknown; maritime news-only (Palaemon 9–16 Nov unpublished); no independent capacity-offline aggregate since 9/8.
- **FORWARD:** 11/18 GATE-OSPREY-001 review + OSP-07 grade; 11/20 OSP-08 grade (expected FAILED); 11/24–27 C3 canvass; 11/27 earliest C3 kill and C1 leg A; 12/11 earliest C2 re-kill; by 12/6 §5 re-read.
- **NEXUS-NAMED:** none.
- **FLAGS:** The lower half is stale and contradicts the top block: VIEW is dated 2026-10-29 ("C1: quiet since 10/16"; "C2 ... Earliest re-kill 11/17"); NEXT DECISION POINT still lists "11/17 earliest C2 re-kill" and "11/10 Bloomberg print, Abu Dhabi 11/10–11"; WATCH lists Abu Dhabi 11/10–11 and Palaemon 2–9 Nov as upcoming; SENDING calls Abu Dhabi "the next test". The VIEW heading says "the 11/6 block at the top governs where they differ", but the governing block is now 11/14. The Coverage footer is dated 2026-11-06. OSP-07's window (10/30–11/15) has closed with strikes on record, but it is still shown OPEN pending the 11/18 grade.

## YURI

- **HEADER:** "As of: 2026-11-11 ET (primary fetches 2026-11-11T14:37–14:41Z: pravo presidential block, Kremlin feed and acts, government.ru docs) | STATUS commit: this brief and STATUS are committed together".
- **VIEW:** Score 2/5 unchanged. Russia runs two tracks at once: rapprochement with Washington alongside widening custody of Western assets (a new Decree-302 amendment in the Abu Dhabi talks week). The diesel ban runs to 31.01.2027.
- **MOVED SINCE baseline (11/2):**
  - **YUR-006 HIT 2026-11-11:** Указ №817 (05.11) and №832 (06.11) put seven JTI (Japan Tobacco) Russian companies (ten interests) under temporary management by АО «Промышленные активы», no disposal clause; Brier 0.09. Japan Tobacco (TSE 2914) ¥7,769 → ¥5,562 (−28.4%, 05.11→11.11, two locked limit-down sessions). Russia about 10% revenue / about 25% adjusted OP and MoF 37.55% stake: "press relays, issuer not read".
  - New SENDING: Government №1443 (31.10): 3-month export ban outside the EAEU on benzene, toluene, o-/p-xylene, phenol. №1457 (05.11): fertilizer export quotas >18.8 Mt (N >11.3, AN >2.3, complex >7.5) for 01.12.2026–31.05.2027 ("routine renewal, not potash").
  - YUR-F02 re-test to 11/28; call record YUR-C01 written 11/11.
- **CROSS-DOMAIN / CALIBRATION:** Japan Tobacco pricing and tradeability are TERRY's ("no YURI trade"); delivered diesel supply is BRENT's. Uncertain: how the 500 kt diesel permission is administered; whether the №686 code list exists as a restricted act; unpublished decree numbers; closed parts of Kremlin meetings.
- **FORWARD:** YUR-F02 dated cross-channel calls, DAEDALUS grades 11/28. Mid-November RU–US–UA talks (calendar only).
- **NEXUS-NAMED:** none.
- **FLAGS:** As-of 11/11 is 5 days stale; no commit since. Large parts contradict the header: WAITING FOR still lists the №954 amendment "Signed ≤31.10" (YUR-005, resolved HIT), the "Further Decree-302 list amendment ... ≤15.11" (YUR-006, resolved HIT 11/11) and "DAEDALUS YUR-F01 grade 10/24" (past). CALIBRATION still carries "YUR-005 p=0.60, YUR-006 p=0.70". NEXT DECISION POINT and WATCH still list "YUR-006 grade ... 2026-11-15" as open. VIEW bullets are dated 21.10 / 22.10. The Japan Tobacco yen levels have no stated basis (close vs intraday, source).

## AEOLUS

- **HEADER:** "Last writeback: 2026-11-11 09:45 ET (PROME catch-up wake prome-2b; LAST write before commit. Every channel re-read on live data; no score moved.)" No pin in the brief; same-commit with STATUS (21515129a). Compact routing variant (Amendment 9).
- **VIEW:** Composite 17/30, fired 1/6, moved 0 since 11/05. Rhine (C5, score 5) fired on the 40/180 key and went deeper; Colorado C6 4 with water still rising and the deal unsigned; vortex (C3) weakened deep but not reversed below 10 hPa, with no US-cold signal.
- **MOVED SINCE baseline (11/6 07:44 ET):**
  - Rhine: complete days 11/08–10 Kaub 10.479 / 12.333 / 13.542, Duisburg 149.531 / 144.792 / 142.260; held every day 11/04–11/10 (KB-269). Contargo [11/11] Kaub top row €1,075 per 20ft; Ruhrort €445 (from €335). Score "fired, deeper".
  - Vortex: GFS `.anl` 10 hPa 60N −1.92 [11/11 00Z], −2.71 [06Z] (event low); 30 hPa +1.84; forecast +21 by day 10 (KB-271). Heading changed from 🟠 to 🟡; "UNG card ended 11/07". CPC 6–10: cold before 11/16, then mostly above normal (KB-278).
  - C6: Mead 1,040.21, Powell 3,539.30 [11/10]; AEO-10 80%, margin 5.21 ft; FR 0 Reclamation documents 11/05–11/11; docket unread 11/11 (403).
  - ENSO weekly Niño-3.4 +3.3 [04NOV] (KB-272). C2: USDA 11/10 SA corn 15,000 kt (−8.65%), Aus wheat 32,500 (−5.98%), not fired (KB-273).
  - Florida/Georgia: Oct 31–Nov 3 FL rain max 24.69 in (WPC prelim, Valkaria Airport / near Malabar) (KB-275), CORAL holds the number; DR-4955 IA in all 8 counties; OIR 68,071 claims / $735.5M [day 28] = CORAL's (KB-276). North Georgia 1-in-1000 rain, no insured figure (KB-277). New theme combo:el-nino-winter-rain.
- **CROSS-DOMAIN / CALIBRATION:** CORAL owns the Florida rain and claims figures (asks CORAL's word on 24.69 in as the event maximum, packet 11/11). Routed TERRY on the vortex ("answer, no card owed"). "Nothing here is a trade." Uncertainty: Rhine is a level, not a proven traffic halt (no cargo-volume evidence after 10/30); C6 docket unread, absence not proof. No CALIBRATION section.
- **FORWARD:** each session C5 exit test (AEO-15, break by 11/29); 11/12 CPC ENSO; ~11/15 November 24-Month Study; 11/26 SA CEC final; 11/30 hurricane season end (AEO-01); 12/02 C6 Orange window; 12/10 WASDE.
- **NEXUS-NAMED:** "Compact routing-first variant (NEXUS Amendment 9, Will-approved 7/31)." and the section "## WHAT NEXUS/PROME SHOULD KNOW — Root independence: C5-Rhine (European basin) · ENSO cluster (C1/C2/C3/C5-Panama/C6) · coastal (wind + sea level) are separate roots. **The C6 conditional still stands:** execution moves leg 2 to the 1,010 line; the November study decides whether it fires. **Nothing here is a trade.**"
- **FLAGS:** As-of 11/11 is 5 days stale. Two forward items have passed unreported (11/12 CPC ENSO, ~11/15 24-Month Study, which "decides whether [C6] fires"). Several figures carry no unit: Kaub and Duisburg gauge readings, Mead and Powell elevations, and the vortex numbers (the 30 hPa context implies m/s, not stated on the figures).

## WATT

- **HEADER:** "As of: verified 5-min tape to November 12 23:55 EPT; unverified 5-min to 11:00 EPT November 14 (no later tape: DM2 HTTP 401 from 14:12 ET November 16); EIA-930 demand to 18Z November 16; posting board read 14:12 ET November 16 ... NG=F $3.230 close November 13 ... STATUS commit b03bd802a1."
- **VIEW (Status line):** P1/P2/P3/P4 = 3/5/4/2, composite 14/20 unchanged. The PJM P1 price tape from 11/14 11:00 EPT is UNKNOWN, not quiet (key refused). The Market Monitor's view supports a 2029/30 auction clearing at the cap.
- **MOVED SINCE baseline (11/5 vintage):**
  - **P1 price limb 11/14 11:00 EPT to 11/16 14:21: UNKNOWN** (DM2 401; WILL_QUEUE 695). Demand limb met in 7 of 52 hours (11/15 23Z–11/16 02Z and 12Z–14Z), peak 103.5% / 103,260 MW at 13Z [KB220]. New boot leg `tape_scan.py`.
  - 11/5–11/14: zero PJM prints ≥$1,000; top $641.45 verified 11/9; $607.87 unverified 11/13 17:55; overnight $446.50 11/14 02:55; WATT-16 no fire through 11/14 11:00. Winter demand limb passes in 30 of 154 hours, so P1 is price-gated this season [KB205/206/212/216].
  - Market Monitor Q3 report: RBP delayed past December "effectively ensures" the 2029/30 BRA clears at the maximum price, +$5–10B data-center cost; Jan–Sep total wholesale cost $111.61/MWh, +40.9% YoY, capacity +81.1% [KB214]. Sent to TERRY.
  - IRAS registry compliance filed 11/9 (ER26-3515-002); OCC and PJM Industrial Customer Coalition rehearing requests the same day [KB215].
  - **Grid-equipment figure refreshed, replaces KB-097:** Eaton Electrical Americas orders +39% organic, backlog +33%; GE Vernova orders $29B, backlog $197B, gas backlog plus slots 116→122 GW; Siemens July–September 0 GW converted, firm gas backlog 69→65 GW, reservations 26→39 GW; GE Vernova converted 13 GW [KB208].
  - SoftBank SB7 $2.9B write-off plus $0.9B settlements: direction for power demand not established [KB209].
  - B1 T1 re-dated to 2027-01-10/11 Beijing under MOFCOM 2026 No. 58; 11/27 clock includes graphite [KB210].
- **CROSS-DOMAIN / CALIBRATION:** Wholesale per MWh, not retail bills (CARL's). Siemens's zero is "one supplier, not an industry stall". Unknowns: SoftBank's dropped equipment direction; Eaton segment backlog dollars; what the ER26-3515 rehearing requests seek; amended RBP docket and order date; cause of the 11/1 run; current active queue; hedge shares.
- **FORWARD:** weekly coverage by 11/21; DOE PJM plant orders end 11/17 and 11/20 (renewal reads); EL26-67 responses 11/16, answers 12/16; WATT-13 resolves 12/2; OPSB Ohio gas-plant hearing 12/10; ERCOT Batch Zero 12/10, PUCT 12/17; BRA window 12/9–15, results 12/22 (WATT-14 clear at cap 88%, WATT-15 45%); WATT-16 grades 12/18; WATT-17 12/31; EO 14421 clocks 12/24 and 2027-02-22; B1 T1 2027-01-10/11.
- **NEXUS-NAMED:** recipient cells only: "HENRY / AEOLUS / PROME / NEXUS" on the P1 UNKNOWN row and the 11/5–14 no-print row; "ISHM / VULCAN / HENRY / NEXUS / PROME" on the grid-equipment row; "VULCAN / HENRY / CARL / NEXUS" on the SoftBank row; plus older rows and "October 29 packets: ... NEXUS a862a30c4".
- **FLAGS:** VIEW section is October vintage (EIA 10/6 forecast, Oct 28–Nov 3 tape) and does not mention the Market Monitor read or the tape outage; NEXT DECISION POINT is headed "November 14 catch-up". No contradiction found, only age.

## VULCAN

- **HEADER:** "As of: 2026-11-16T13:57:23-05:00 | STATUS commit: 4d0dbcebd8". Variant FULL.
- **VIEW:** S1 3 / S2 2 / S3 3 / S4 3 / S5 4 = 15/25, unchanged. The suppliers that report first show no slowdown; delivery slips a quarter at a time at rented sites but financing still flows; demand quality (Altman's "double counting") is the open question, not a band.
- **MOVED SINCE baseline (11/10 10:12 ET):**
  - **WQ-689 RULED B (Will 11/16 11:39 ET):** S5 keeps 4 and core status, labelled "independence unsupported this quarter"; do not count S5 as a separate alarm from S1; successor VULCAN-192 to 2027-02-15 (KB-444).
  - **VULCAN-13 MISS (11/16):** no qualifying in-window S5 independence case; IREN GPU Financing 2.0 NOT COUNTED, recorded as a disagreement ("A reader could weigh IREN the other way") (KB-437).
  - **VULCAN-15 HIT (11/16):** curtailability offset still 0 GW (FERC 197 FERC ¶61,019 rejected the IRAS core), on WATT's 11/14 record, not re-read at eLibrary (KB-438).
  - **VULCAN-188 HIT** (TSMC October NT$586,890mn, Jan–Oct +43.3%) and **VULCAN-191 MISS** (CoreWeave FY2026 capex $37–39B, low end raised).
  - Treasury demand on Nvidia (Fox 11/15; Bloomberg, Fox Business, AFP read): answers in 10 days from board and outside counsel; "No authority, consequence or start date stated; 11/25 is my count". NVDA $155.62 −4.44% vendor intraday 13:48 ET (11/16). Bessent's "about 1% stayed in Singapore" matches Nvidia's filed footnote.
  - Nvidia CEO exit 8-K 5.02 (accepted 11/12 08:52 ET): Huang resigned effective 11/11; CFO Kress interim CEO; Jones Chair; no reason or outlook; no letter keys on leadership (KB-430).
  - Slot 10 (holdings 11/12, 11/12 close): Mag-7 32.6020% (slot 9 33.4972%), NVDA 6.1380%, breadth +1.72pp, YELLOW → below-yellow, NOT FIRED. 11/13 chip selloff (vendor about 16:02 ET): SMH −2.99%, NVDA −2.01%, S&P −0.40%, RSP +0.21%.
  - GPU reading 10: CoreWeave 6.155, Nebius 4.50, Crusoe 3.90; SDH100RT $3.10 (from $2.99), OCPI $3.39 (from $3.13).
  - Nebius Q3 (issuer release): New Jersey rest slips to 2Q27; 2026 revenue to the low end of $3.0–3.4B; capex about $27B (above $20–25B); S3 NOT FIRED (KB-424).
  - CoreWeave Q3 10-Q: recourse debt $41.6B net, non-recourse $5.27B, 2027 principal due $10.97B, OEM vendor financing $6.89B (from $3.52B), covenants met (KB-429). Reported $4B-plus Meta-contract loan: headlines only, no filing at 11/16 15:19Z (KB-439).
  - Siemens Energy FY2026: no data-center cancellation wording; 0 GW converted from slot reservations in Q4 (KB-422).
- **CROSS-DOMAIN / CALIBRATION:** Spreads are LIQUID's; remote-access or transshipment rules ZHAO's; Nvidia tradeability TERRY's (do-not-trade line). Calibration: 22 registered, 16 resolved, six OPEN; none due. "VULCAN-13's perimeter was written after the outcome was seen, disclosed." Uncertainty: demand quality; IREN weighting; SoftBank's SB7 supplier UNKNOWN; Anthropic not extending SpaceX compute is one unconfirmed source.
- **FORWARD:** 11/17 Nvidia Q3 FY27 results (about 1:20 PM PT, call 5 PM ET); 11/19 NVDA 10-Q (ESTIMATED) with VULCAN-17 and DOCKET L322 T-tests; 11/20 SoftBank Q2 transcript, GPU reading 11, mag7 slot 11, NEXTDC AGM; ~11/25 Treasury 10-day ask (own count); 11/27 GPU 12 and slot 12; 11/30 consume WATT's EL26-67 read; 12/7 Jupiter hearing; 12/10 OPSB hearing and ERCOT Batch Zero; 12/10 TSMC November 6-K; ~12/15 Oracle 10-Q; 12/16 Micron (inferred).
- **NEXUS-NAMED:** "| PROME / LIQUID / BROCK / VIOLET / NEXUS | 🆕 **WQ-689 RULED B (Will 11/16 11:39 ET):** S5 keeps 4 and core status; read it TOGETHER with S1 ('independence unsupported this quarter') until a test supports independence. Successor VULCAN-192, VULCAN-13's letter unchanged, to 2027-02-15. Do not count S5 as a separate alarm from S1 meanwhile. | KB-444 |"
- **FLAGS:** Over 22 KB (23,484 B). **VIEW contradicts the header:** VIEW ends "S5 stays 4 on its two fired events until Will rules", but the header and SENDING record WQ-689 RULED B at 11:39 ET the same day. Possible date slip: the GPU reading 10 row (an 11/13 reading) says "Lambda still shows only 11/16 prices".

## ZHAO

- **HEADER:** "As of: 2026-11-16 14:15 ET (by `date`) — PROME prome-6f assignment ... Closed out 2026-11-16 14:17 ET on PROME's ask. | STATUS commit: NONE (folded in the same commit as STATUS) || Prior as-of: 2026-11-11 10:20 ET."
- **VIEW (Status line):** 🟠 29/60 ELEVATED, unchanged since 11/06. China's October home demand is still contracting while exports and PPI carry the headline. A priced December Fed hike does not make China a forced Treasury seller, because the currency-defence channel is shut (the PBOC is resisting appreciation); the live Asian official-seller risk is Japan near USD/JPY 160 (SAM's call).
- **MOVED SINCE baseline (11/10 11:15 ET):**
  - 11/16: new RMB loans about −RMB 100B in October (PBOC 11/13 via secondaries); retail +0.4% YoY; FAI −8.1% YTD (−7.2% Jan–Sep); property investment −21.6% YTD (NBS primary 11/16) (KB-270, 271). V5b rescore (now 3) owed; no score moved.
  - 11/11: ORACLE +25bp 85.5, +50bp or more 11.8 (December Fed); yuan 6.6727 → 6.6612 while DXY 102.2 → 102.9; HK peg 7.8455, no intervention; China 10Y 1.61%, back to YELLOW; PBOC overnight 1.25% since 11/02 (KB-266).
  - Trump–Xi bilateral Shenzhen Thu 11/19 registered, instrument-only grading (KB-273). NFRA Q3 not out (KB-272).
  - Calibration: exports figure changed from "+36.3% (Sep)" to "+35.2% (Oct, secondaries; imports +41.6%)"; PPI from "+5.0%" to "+5.7% (Oct ...; consumer goods −0.1%)".
  - Forward: 11/27 MOFCOM 2024 No. 46 clause 2 content now "Ga/Ge/Sb/superhard + graphite; no extension yet (KB-261)" (was "content UNVERIFIED").
  - ZHA-19 YES (Brier 0.1225) and ZHA-20 YES (Brier 0.0225) graded 11/10 (already in baseline as pending).
- **CROSS-DOMAIN / CALIBRATION:** December Fed odds cited from ORACLE. Japan's official-seller risk is SAM's. Uncertain: whether the 1/9–1/11/2027 cluster gets a third extension or a deal; the cause of the August TIC residuals; whether HK carry pressure forces HKMA in; leg F's hit rate in a real regime change. Counter-frame (RED BENIGN-DRIFT) "strengthened again".
- **FORWARD:** 11/18 September TIC (Treasury-confirmed; ZHA-22; China Q3 net ≤ −$50B ⇒ LIQUID+PROME); 11/19 Trump–Xi Shenzhen; ~11/20 NFRA Q3 and LPR (modeled); 11/27 MOFCOM 2024 No. 46 clause 2 ends (first uncovered day 11/28); 11/30 November PMI (ZHA-23); 1/10 cluster.
- **NEXUS-NAMED:** "★ **11/16 — for NEXUS: China's October home demand is still contracting** (NBS primary 11/16; PBOC 11/13 via secondaries) ..." and "★ **11/11 — for NEXUS: the December Fed hike now priced (ORACLE: +25bp 85.5, +50bp or more 11.8) does NOT make China a forced Treasury seller.**" Older VIEW bullets: "★ 11/06 — FOR NEXUS: the two-clock story is now one clock, and the domestic read weakened."; "★ 10/29 — FOR NEXUS: the PBOC's currency posture has fully reversed ..."; "🟠 10/9 — FOR NEXUS: a pre-registered tripwire fired and I applied it AGAINST my own read."
- **FLAGS:** The VIEW section's newest bullet is 11/06; current view lives only in the Status line. The FORWARD CATALYSTS heading says "refreshed 2026-11-06" but holds 11/13–16 rows, and "Sat Nov 7 SAFE Oct reserves + PBOC gold" is past and unmarked (MIDAS graded it 11/8). SENDING rows carry 11/06-dated figures (20-fix mean, CGB 1.59%) and "PBOC gold +0.74 Moz ≈ 23 t in Sep" to MIDAS, now superseded by the October print. "China-US 10Y gap ~327bp" and kill-line levels ("now $590.7B", "now −$71.5B") carry no date.

## CYPHER

- **HEADER:** "As of: 2026-11-16 16:10 EST (PROME summons on IMMEDIATE card SIG-W-20261116-006 plus its 16:00 ET re-check, prome-6f: one new incident row 072; no score, band, gate or prediction moved; no row fired) | STATUS commit: `ba365a70d961b42e74bb9f1493eb048be369496b`". POSITION N/A.
- **VIEW:** 🟠. The PHP2Shell wave has one fired trigger (CISA KEV 10/26) and vendor-verified compromises but still no named victim, so the R1 flip is not met. Off the wave, the bank-vendor channel is live (Finzly, Abrigo, Arkéa); Arkéa is a new class, a bank's own funds stolen through a provider.
- **MOVED SINCE baseline (11/8 12:07 EST):**
  - 11/16: Chase online-banking outage from about 09:53 ET (CYB-INC-072, INFRA-OUTAGE); 16:00 ET re-check: Chase "This is a technical issue, not cyber-related" (to Fox Business); Zelle "Zelle is not down"; U.S. Bank "not directly impacted"; Wells Fargo notice per NBC only; no restoration announced at 16:00 ET. Fires no row. WALTER correction packet sent.
  - 11/14: Microsoft 365 global outage 11/12 about 17:54 GMT to early 11/14 (about 24h, 70+ countries; CYB-INC-071); not cyber per Microsoft; banks affected, none named; CHK-20 CONFIRMED-OFF-WAVE. DOJ 11/12 (PRIMARY): more than $2.7B of the Binance theft frozen; court authority over more than $1.2B; FBI names TraderTraitor. CISA KEV added Check Point CVE-2026-123039 on 11/13.
  - 11/13: N-central 4EverAble2Shell defeats the 11/10 fix where the Legacy API is on; 21 live servers running one operator's miner, 19 on the fix; CYB-INC-065 → CONFIRMED. Check Point Research: unnamed PHP2Shell compromises from 10/30, wiper at some Israeli victims (CYB-INC-070). GMO Internet Q3: JPY 3.05B direct cost assumed for Q4, about 32% of FY operating-profit forecast, forecast not revised.
  - 11/12: Sawyer Savings Bank (NY, about $285M) CONFIRMED on the Vermont AG record (16,069 people per Indiana via American Banker); Storm-1175 lists five US banks (about $6.1B assets) and Insight CU (Florida); two confirmed. ConnectWise ScreenConnect: about 400 environments disabled.
  - Composite 24/40 raw, 15/40 shared-root-adjusted; rows 1, 3–9 NOT-FIRED now dated 11/12 (was 11/05); rows 1, 3, 4, 7 re-checked 11/13.
  - Arkéa: Les Echos (11/14) named the provider on unnamed sources (asset-management compliance software), unread and unconfirmed; weekly look moved to 11/23.
- **CROSS-DOMAIN / CALIBRATION:** Large-bank operations and deposits are GIBBS's; Zelle and rails LIQUID's; regional-bank consequence REGINALD's; Japan SAM's; PANW price leg HENRY's (VULCAN declined). Tension: DEWEY's WALTER-watch alternative is the R0 test (12/17). Uncertain: whether any bank or CU names N-central or ScreenConnect in the CYP-03 window; Arkéa's provider and client base; whether named PHP2Shell victims surface; whether Finzly's keys were live; whether Abrigo lost data.
- **FORWARD:** 11/18 Row 9 equity persistence (PANW at or below $289.24 AND 10.0 points behind HACK on 2 consecutive closes; HENRY grades); 11/19 weekly wave clock, Abrigo, ConnectWise, N-able one look; 11/20 R1 flip test (no named organisation ⇒ R1 to MECHANICAL, Log4Shell shape); 11/23 Arkéa weekly; ~11/27 Microsoft post-incident report (estimated); 12/01 GMO compensation totals.
- **NEXUS-NAMED:** recipient cells: "NEXUS / PROME / GIBBS / LIQUID / WALTER" (11/16 Chase row), "NEXUS / PROME / WALTER" (11/16 16:00 re-check), "NEXUS / PROME / REGINALD / VULCAN / WALTER" (M365), "NEXUS / PROME / LIQUID" (DOJ Binance), "NEXUS / PROME" (Check Point KEV), "NEXUS / PROME / TERRY" (Check Point Research), "NEXUS / PROME / REGINALD" (N-able 11/12), "NEXUS / PROME / SAM" (11/06 Capcom), "| NEXUS / PROME | Composite 24/40 raw, 15/40 shared-root-adjusted (VX-01 corrected 2->3 on the letter, VX-08 3->4 on the attribution; neither is new bank damage). Rows 1, 3-9 NOT-FIRED at 11/12 | P3 | Wave state for synthesis. ...".
- **FLAGS:** None material. The first Chase row still says "unresolved at last report 13:42 ET" beside the later 16:00 re-check row; both are dated, so this is sequential, not contradictory. VIEW bullets are 10/29–11/06 vintage but consistent with the header.

## MIDAS

- **HEADER:** No as-of line and no pin. The newest block is "November 14 — gold's 11/12 fall was UNEXPLAINED-DOWN, not liquidation (current read for peers)". Same-commit with STATUS (1d561a14b).
- **VIEW:** Gold is mostly trading on real yields again (11/06 RATE, 11/10 RATE), but 11/12 was UNEXPLAINED-DOWN (a residual beyond the rate effect, with no equity stress), not liquidation. The real 10Y is near the WQ-451 3.00% line that would withdraw the positive three-month gold lean. Composite 13/20 unchanged.
- **MOVED SINCE baseline (11/8 block was newest):**
  - **11/14 grade:** GLD −2.82% to $354.89 on 11/12 (PRIMARY issuer); PRIMARY real 10Y +8 bp explains 1.22 points (43%), residual −1.59%, just outside the RATE band; S&P −0.35%, VIX +1.21; trust −0.38 t. Two days 11/10 → 11/12: GLD −3.92%, real-yield-implied −1.22%, unexplained −2.70% while DXY +0.92% and 2Y +13 bp (MIRROR). PRIMARY real 10Y 2.91% on 11/13, 9 bp from the WQ-451 3.00% five-print line. Hypothesis (untested): a near-term Fed-path repricing through the dollar and front end; Fed odds are ORACLE's. Contract map reviewed 11/14; December roll due before late-November first notice. TERRY packet for a tradeability read.
  - **11/11 grade:** GLD −2.68% ($379.53 → $369.36, PRIMARY issuer) as the PRIMARY real 10Y rose 2.66 → 2.78% (+12 bp) after October core CPI +0.3% (PRIMARY BLS, 11/10 8:30 ET); beta implies −1.83% (68%); residual −0.85% (−0.61 sd) = RATE; trust −0.29 t; 2Y +17 bp. L2 stays 2 of 10. MIDAS-13's HIT condition met 11/09 ($379.53 ≥ $378.95), formal at the 11/23 retrieval. Bands 11/10: SLV −25.99% (4), PPLT −17.13% (3), PALL −25.59% (4). Palladium about +5.3% live 11/11, no sourced driver.
- **CROSS-DOMAIN / CALIBRATION:** For BOND: real 10Y 2.91% vs the 3.00% line. For LIQUID/HENRY: Fed-path hypothesis, untested. For TERRY: "no new tradeable finding" (11/11), then a tradeability read requested (11/14); GLD is not book protection (from 10/23). For ZHAO: copper-location theme; LME build still not located. Uncertainty: the 11/12 residual is unexplained; gold settlement certification still missing (older blocks).
- **FORWARD:** WQ-451 3.00% five-print line on the real 10Y; MIDAS-13 formal retrieval 11/23; December roll before late-November first notice; TIC sign (L821) about 11/18; WGC October (L822) early December.
- **NEXUS-NAMED:** none.
- **FLAGS:** No as-of or pin header and no VIEW / CALIBRATION / NEXT DECISION / FORWARD sections in schema form; the brief is a stack of dated blocks (20,370 B, approaching the size flag). Internal contradiction: lower blocks still say "Current reading basis: October 26 ..." and "Current close/context, October 26", with October 26 futures prices and "Next existing clocks: October 30 ...; November 2 ...", which conflict with the 11/14 block. Glued words, mostly in the October 25–26 blocks: "versus23", "real 10Y2.66%", "d200−20.09%", "SLV−24.96%/PALL−27.07%", "M2would-be 4/I2would-be 4", "Feb28", "first-session+1.29%,21 sessions−14.30%,126−15.47%", "Ukraine2022", "Hamas2023", "WGC64%", "in14", "March2026", "throughOct23", "pre2026", "Oct9→22", "Jan29→Oct20", "latestOct20", "remain23", "diagnostic4", "recent120".

---

## Cross-brief (instruments cited by 2 or more of these desks; disagreements)

1. **Saudi October crude:** BRENT's headline is OPEC secondary sources 9.194 mb/d [CONF MOMR 11/11], with EIA 9.3 and survey 9.2 listed beside it. FALCON KB-489 calls "EIA STEO 9.3 mb/d (survey 9.2)" "BRENT's Saudi October figure". **Minor attribution mismatch:** same "about 9.2" read, different named figure. FALCON's older row (Vortexa 6.5 / TankerTrackers 6.99 / Kpler 5.4) is exports, a different perimeter.
2. **Bahrain drones 11/13 and 11/15, Bab shore 11/15, Houthi Pumping Station 7 / Yanbu claim (CLAIM ONLY), Madinah 11/9 confirmed, PortWatch error 499:** BRENT and FALCON agree on all of these. Neither reads Yanbu loadings, and both say so.
3. **Omsk and Volgograd:** OSPREY has about 21 + about 15 Mt/yr (11/11, 11/13); BRENT has "about 36 Mt/yr nameplate, no halt". They agree. **Russian diesel exports:** OSPREY records a conflict (FT 11/12 "doubled" vs Bloomberg 11/13 "drop") and says BRENT owns the figure. BRENT logs only the Bloomberg "drop" title, so the FT counter-headline is not in BRENT's brief.
4. **Russian producer diesel ban №1436 to 31.01.2027:** YURI, OSPREY and BRENT agree. **Ust-Luga 11/11:** OSPREY counts it for C2 (WQ-669 A); BRENT says it was not the stated cause of the 11/11 +3.2% intraday move. Consistent.
5. **US-China clocks:** BIS affiliates stay to 2027-01-10, MOFCOM 2026 No. 58 to 2027-01-10/11, USTR to 1/9 23:59 ET, and the 11/27 2024 No. 46 clause 2 clock including graphite. VULCAN, ZHAO and WATT all agree.
6. **Siemens Energy (0 GW converted, backlog 65 / reservations 39 GW) and SoftBank SB7 ($2.9B + $0.9B, supplier unnamed):** WATT and VULCAN agree. **EL26-67 (responses 11/16, answers 12/16), Jupiter hearing 12/7, OPSB hearing 12/10, ERCOT Batch Zero 12/10:** they also agree. VULCAN-15 HIT rests on WATT's 11/14 record, not re-read at eLibrary.
7. **PBOC gold:** ZHAO's SENDING to MIDAS has "+0.74 Moz ≈ 23 t in Sep"; MIDAS has the October SAFE print, +25.82 t (78.30 vs 77.47 Moz). These are different months, not a conflict, but ZHAO's row is stale. **TIC 11/18:** ZHAO (ZHA-22) and MIDAS (L821) both wait on it.
8. **December Fed path:** ZHAO cites ORACLE (+25bp 85.5, 11/11). MIDAS defers Fed odds to ORACLE and offers an untested Fed-path hypothesis for gold's 11/10–11/12 fall. Same direction, no conflict.
9. **Nvidia:** VULCAN carries the Bessent demand (no authority or start date; 11/25 is VULCAN's own count) and results on 11/17. ZHAO registers Trump–Xi on 11/19, with instrument-only grading, as the next venue for any chip-rule instrument. No conflict.
10. **Staleness that touches shared reads:** OSPREY's lower half (C2 re-kill 11/17), YURI's open-looking YUR-006, and AEOLUS's past 11/12 and ~11/15 catalysts. Peers citing these sections would carry superseded states.
