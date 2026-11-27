# AEOLUS STATUS

**Last Updated:** 2026-11-27 10:05 ET (PROME due-row wake D:L1256: NorCal 11/25 highs confirmed on complete-day data, St. Johns read, WQ-735 recipes switched, inbox drained; KB-338…341; no score moved). Prior: 2026-11-25 14:41 ET. **Rotated 11/27 for read-cap headroom (DAEDALUS packet 11/25): the whole prior file is verbatim at `archive/STATUS_ARCHIVE_2026-11-27_full-pre-rotation.md`** (crc in its banner); older history `git log -p -- AGENTS/AEOLUS/STATUS.md`.
**Status:** 🟠 **Floods LIVE, no score consequence.** FL: St. Johns at DeLand 6.21 ft [08:30 ET 11/27], forecast 6.6 ft 12/01 to 12/04 vs the 6.33 record (KB-340). CA 11/25 records (PRELIMINARY) confirmed: Arena Cove 9.216, Santa Barbara 8.209, San Diego 8.654, La Jolla 8.114 ft MLLW (KB-334/338). 🟠 **C5 3:** Rhine recovered; Mississippi forecast to a new autumn low. 🔴 **C6 4:** Colorado deal unsigned, Orange from 12/02, MWD vote 12/08. 🟡 C3 2: vortex rebuilt.
**Class:** Market-agent (climate → economy) · **Self-level:** L2

> Data is primary-sourced and dated below. Per Critical Rule #3, verify against the primaries (CPC/NHC/USBR/WSV/ACP/NIFC/NWPS/CO-OPS) before any trade use. No naked numbers.
> **STATUS budget: 32,550 B (`READ_CAP.md`); keep under 70% (22,785 B) after the 11/27 rotation · <250 lines.** Measure with `PROME/tools/measure.py`. **Rulings that still govern:** `wksst9120.for` is the sole weekly ENSO figure (KB-088); CPC prose quotes the RELATIVE monthly index, never "weekly" (KB-181) · §C6 "USBR's path projects a breach" is SATISFIED-AT-WRITE-TIME, never a live leg · **SLOTS ≠ TRANSITS** · grade the Rhine on **UNROUNDED** means only · Mississippi on **UTC-day** means (KB-159) · NHC intensity in **KNOTS as stated** · coastal record = above BOTH NOAA top-ten and the 6-min series; between = name the basis (KB-335).

---
## CONVERGENCE MATRIX

| # | Channel | Score (1–5) | Local state | Independence | Key Signal | Upgrade Trigger |
|---|---|:--:|---|---|---|---|
| C1 | Insurance / reinsurance | **2 🟡** | no Gulf/FL system since Isaias | El Niño root (suppress) | ACE 19.53 = 17.06% of to-date normal; NHC 11/23 none expected 7 d (KB-309); Isaias DR-4955-FL IA all 8 counties (KB-276) | re-arms on the next Gulf/FL system; season ends 11/30 |
| C2 | Agriculture / food | **2 🟡** | El Niño crop: SA maize (2027 harvest) | drought root w/ C4; Hormuz fertilizer = second root (KB-209), count once | USDA 11/10: SA corn 15,000 kt = −8.65% vs 16,421; Aus wheat 32,500 = −5.98%; NOT FIRED (KB-273) | **→3:** SA ≤13,958 kt (−15%) OR Aus ≤−15%, each WASDE (next 12/10) · **→4 (WQ-737/738):** both regions at −15% in one USDA reading AND FAO cereals ≥+20% y/y on 2 straight first prints (PROVISIONAL) |
| C3 | Energy demand | **2 🟡** | winter heating; shoulder season | El Niño root (w/ C1/C6) | CPC 11/19 DJF leans warm (KB-301); 10 hPa 60N +23.22 [11/23 00Z], rebuilt (KB-309); 30-d HDD to 11/21 MidAtl −19.9%, ENC −31.1%; Henry Hub $3.10 [11/17] vs WQ-736 line $4.43 (KB-314) | **→3:** DJF 30-d MidAtl/ENC HDD ≥0% vs 1991-2020 OR EEA2+ weather-caused · **→4 (WQ-736):** HH spot ≥1.5× prior-60-day median 3 straight days Nov–Mar AND CPC 7-d HDD ≥+10% within 7 days before (in-sample, 6 of 29 winters; counts only from 11/23) |
| C4 | Property / physical | **2 🟡** | fire cool; **flood leg LIVE in FL and CA, not a band input**; loss leg Isaias $1–4.5bn | fire = drought; Isaias = SAME event as C1; king tide = wind + SLR root | FL St. Johns major flooding, DeLand forecast above record (KB-340); CA 11/24–25 tide records, roads/waterfronts/municipal piers only (KB-338/339); Gallagher Re 9M 71.9% of 10-yr; Aon 9M $91bn (KB-251); NIFC PL 1 | Q3 cat tally ≥110% OR a >$10B insured cat OR PL ≥4 |
| **C5** | Supply chain / logistics | **3 🟠** (4→3 11/22) | Rhine recovered; Panama eased; live leg = Mississippi forecast fall | European basin own root; Mississippi = US-interior drought (w/ C2); Panama = ENSO (w/ C6) | Kaub 236.4 / 228.3 [11/25–26] (KB-341); Memphis −2.57 [11/23] → NWPS −5.1 (11/26), −6.9 (12/10), −7.8 (12/21) (KB-304); St. Louis barge 529.7% [wk 11/17] (KB-298); Panama draft 50.0 ft (KB-299) | **→5:** Rhine 40/180 test passing again · ⛔ no Mississippi level is a trigger (9/18) · **→2:** judgment, if observed Memphis does not follow the forecast fall and barge rates keep falling |
| C6 | Water scarcity / allocation | **4 🔴** | physical band ORANGE (Mead 6.33 ft above 1,035) · agreement band YELLOW since 11/02 · score 4 (judgment) | El Niño Western hydrology; Powell↔Mead ONE system | Mead 1,041.33 [11/22]; Nov 24MS Mar-27 1,033.20, min 1,014.00 Jul-27, Hoover ~309 MW May–Sep 2027 (KB-280/281); MWD board 12/08 (KB-291) | **→5:** §C6 legs below; leg 1 projected to fire March 2027 on the Nov path |

**Composite: 15/30 · fired 0/6.** Conservation: 2+2+2+2+3+4 = 15. ⚠️ Isaias is ONE event for C1 and C4. ⚠️ C6 held at 4 on the regulatory/legal leg, not on water; no December test stands. C5 stops at 3 because the Mississippi fall is a forecast, not an observation (11/22).

---
## 🔴 UPGRADE TRIGGERS — live rules

**C1:** Isaias graded NOT FIRED 10/09 (90 kt vs ≥96 kt, KB-189). Exit leg 2 live to 11/30. **VEHICLE (TRADE.md, L-47):** long RNR arms on a Gulf/FL major landfall or credible track → same-session TERRY packet. Not armed.

**C5 →5 — NOT FIRED since the window ending 11/13** (fired 11/04–11/12, first fire of the 40/180 key). Rule: Kaub ≤40 AND Duisburg-Ruhrort ≤180 cm, 3 most recent complete days (unrounded, ≥90 readings). Exit/re-entry = the same test. **"European low water ended" (WQ-741 A): Kaub ≥77 cm 10 complete days = 9 of 10 at 11/26 (11/18–26); 11/27 partial 201.7 (n=64) completes at 18:00 ET 11/27** (KB-341). Daily rows → archive.

**C6 →5 — enter on ANY leg, exit by the door you came in**
| Leg | Enter | Exit | State |
|---|---|---|---|
| 1 economic | Mead ≤1,035 ft (REALISED) | ≥1,045 × 5 d | 1,041.33 [11/22] NOT FIRED; Nov 24MS projects 1,033.20 end-Mar 2027 (projection, not graded) |
| 2 regulatory | Most Probable 24MS Mead <1,010 in 12 mo while Guidelines in effect, else <1,000 (KB-205); **line today 1,000** | next min ≥ line +10 | Nov 24MS min 1,014.00 NOT FIRED; December study re-grades |
| 3 operational | REALISED Powell ≤3,510, never a 24MS table (KB-143) | ≥3,520 × 5 d | 3,540.62 [11/19] NOT FIRED |

**Milestone band (KB-205):** Y = LB agreement unexecuted ≤60 d before 1/1/27 (from 11/02) · O = ≤30 d (from **12/02**) OR a PI motion in *Nevada v. Burgum* · R = unexecuted at 1/1/27 OR a court vacates/enjoins. **State: 🟡 YELLOW since 11/02.** MWD board item 8-7 on 12/08 (committee 12/07); no PI/TRO reported; federal answer due 12/10; absent a deal §5.3.A.3 Secretary sets the split, §5.4 no new ICS after 12/31/26; 1.25 maf CY2027 cut proceeds (KB-283/291/307).

---
## LIVE CHANNEL READS

| Ch | Metric | Current | As-of | Band | Source |
|---|---|---|---|---|---|
| ENSO | Weekly Niño-3.4 | **+3.3**; Niño-3 +4.7, 1+2 +5.7, 4 +1.4 (KB-309) | 18NOV | 🔴 | `wksst9120.for` |
| ENSO | ONI · RONI | ONI ASO **+2.46** · RONI ASO **+1.97** · Oct monthly +3.25; RONI record +2.40 (1982-83) | ASO | 🔴 | CPC files (KB-240) |
| ENSO | CPC odds | Advisory; historic (RONI ≥2.5) ~60% OND/NDJ [11/12]; next discussion **12/10** (KB-284) | 11/12 | 🔴 | CPC ensodisc |
| C1 | Basin + ACE | ACE 19.5325 / 114.4631 = 17.06%; 10 NS / 1 H / 1 MH; none expected 7 d [11/23] | 11/23 | 🟡 | ATCF + HURDAT2 (KB-218) |
| C1/C4 | Loss leg | Isaias $1–4.5bn industry (never average); FL OIR 68,071 claims / $735.5M [11/06] = CORAL's number; Aon 9M $91bn, no event ≥$10bn, European drought >$8.5bn; 1/1/27 expectations −7.5% to −20% (KB-251/252/276) | 11/06 | 🟡 | SECONDARY |
| **C4** | 🟠 **Floods (FL river, CA coast)** | **St. Johns:** DeLand **6.21 ft [08:30 ET 11/27]** (+0.17/24 h), forecast 6.3 tonight, 6.4 Sat, 6.5 Sun, **6.6 from 12/01 held to 12/04**, record 6.33; Sanford 8.82 → 8.9 vs 8.96; Astor 4.45 → 4.5 today (homes on Riverview Dr and Claire St); DR-4956-FL not amended (no Volusia/Seminole/Lake); no flash flood emergency or South FL watch [09:56 ET] (KB-340) · **California 11/25 (PRELIMINARY, complete-day):** Arena Cove **9.216** record (30-min mean 9.030 still above 8.93); Santa Barbara 8.209, San Diego 8.654, La Jolla 8.114 records; LA tie 8.194; SF 8.213, North Spit 9.814 final, Crescent City 9.741 not records; impacts roads, waterfronts, municipal piers (Pacifica pier partly knocked down) (KB-334…339) · West Coast residual raised since Aug, consistent with El Niño (KB-313); CPC DJF wet FL 70%, S. Calif. 60% (KB-319/320) | 11/27 | 🟠 | NWPS · CO-OPS · NWS · FEMA |
| C2 | Crops | USDA 11/10 SA corn −8.65%, Aus wheat −5.98% (KB-273); SA CEC maize area −12.37% y/y (KB-224); FAO cereals 116.8, +12.5% y/y [Oct] (KB-260) | 11/10 | 🟡 | PSD · CEC · FAO |
| C2 | Drought | CONUS D1–D4 42.03%, D4 2.42 (MS/AR/LA 89% of the D4 rise) (KB-300/308) | valid 11/17 | 🟡 | USDM |
| C3 | Outlook · vortex · HDD | CPC DJF leans warm (KB-301); CPC heating forecast MidAtl −6.9%, ENC −6.6% vs 1981–2010 (KB-317); 10 hPa 60N +23.22 [11/23], event low −2.71 [11/11] (KB-286/309); 30-d HDD MidAtl −19.9%, ENC −31.1% [to 11/21] (report only until 12/30) | 11/23 | 🟡 | CPC · NOMADS |
| C5 | Rhine + freight | Kaub **236.4 / 228.3** daily means [11/25–26] (KB-341); Contargo page still dated 19.11, no tier from 21.11 (KB-297) | 11/26 | 🟢 | PEGELONLINE · Contargo |
| **C5** | 🟠 Mississippi | Memphis −2.57 [18Z 11/23]; NWPS −5.1 (11/26), −6.0 (12/01), −6.9 (12/10), −7.8 (12/21) still falling; ~48 h of rain counted; autumn low −4.68 [9/14]; **levels only, NO GRADE**; St. Louis barge 529.7% = $21.14/t [wk 11/17] (KB-298/304) | 11/23 | 🟠 | NWPS · USDA AMS |
| C5 | Panama | transits Oct 33.19/day · draft 50.0 ft (A-42) · slots 34/day · Gatún 86.58 [11/22] (KB-312) | 11/22 | 🟢 | ACP |
| — | Other rivers | Danube above LKV [11/23]; Paraná last 4.04 m Rosario [11/05] (FICH bot page); Yangtze not refreshed (timeouts) | 11/23 | 🟡 | FICH · OVF |
| **C6** | 🔴 Mead · Powell | Mead **1,041.33 [11/22]**; Powell **3,540.62 [11/19]**; Nov 24MS as in §C6 (KB-280) | 11/22 | 🔴 | USBR 921/919 |

---
## EXIT / INVALIDATION — standing rule | state | FIRED?

| Ch | Standing rule | Current state | Verdict |
|---|---|---|---|
| C1 | ACE <90% normal + no major US landfall by 11/30 | 17.06%; Isaias Cat 2 only | NOT FIRED — channel-kill in progress (resolves 11/30) |
| C2 | 2026-27 El Niño: DJF ONI ≥1.5 AND SA corn >13,958 kt at 5/12/27 WASDE AND Aus final >−15% | in window | NOT FIRED (live to 5/12/27) |
| C3 | MidAtl AND ENC 30-d HDD <0% vs 1991-2020, 4+ sessions, windows ending Dec 30–Feb 28 | out of window | NOT FIRED (opens 12/30) |
| C4 | cat-loss <110% AND non-renewals stable 2+ qtrs | leg 2 has no instrument (KB-235) | CANNOT-FIRE |
| C5 | Kaub ≤40 AND Duisburg ≤180, 3 complete days | Kaub 236.4 / 228.3 [11/25–26] | NOT FIRED · low water ended 9 of 10 |
| C6 | Mead ≤1,035 ft | 1,041.33 [11/22] | NOT FIRED |

**Fired count: 0 of 6.**

---
## PREDICTIONS
Canonical: `workbook/PREDICTIONS.tsv` (states dated in each row). **OPEN (12):** AEO-01 Atlantic below-normal 96% (11/30) · AEO-02 Niño-3.4 ≥1.5 NDJ 99% (12/31) · AEO-03 1/1/27 ROL ≤+5% 90% (1/15/27) · AEO-07 PJM DJF mean above normal 70% (3/15/27) · AEO-08 ≥1 PJM cold alert 65% (3/1/27) · AEO-10 Mead no breach of 1,035 by 12/31 80% · AEO-12 Panama draft ≤47.0 ft Jan–Apr 55% (4/30/27) · AEO-13 SA maize ≤13,958 kt 65% (5/12/27) · AEO-14 AO ≤−1.0 5 days in 11/07–12/04 40% (12/10) · AEO-17 RONI OND ≥+2.50 40% (first OND print; NV 1/20/27) · AEO-18 MWD authorizes 12/08 50% (12/11; NV 12/18) · AEO-19 FL DJF rain ≥9.78 in 75% (~3/10/27). **RESOLVED:** AEO-15 HIT, AEO-16 MISS (11/19); AEO-04/05/06/09/11 earlier.

---
## OPEN / NEXT — the OWED REGISTER
| # | Owed | By | State |
|---|---|---|---|
| 1 | C5 →5 watch on 40/180 each session; record "low water ended" when 11/27 completes; observed Memphis vs the NWPS path; weekly GTR barge print | each session | 🟠 LIVE |
| 3 | December 24-Month Study: re-grade leg 2 and AEO-10 | ~mid-Dec | OPEN |
| 4 | Colorado execution watch: Orange from 12/02 if unsigned; CAP 12/03; MWD 12/08; federal answer 12/10; AZ legislature ~1/11 | 12/02 | 🔴 OPEN |
| 9 | Q3 cat tally: Aon PDF unread; Swiss Re 9M not found | ~Dec | PARTIAL |
| 10 | Paraná and Yangtze reads (blocked); on PROME's 12/07 list | 12/07 | BLOCKED |
| 12 | regime: IOD instrument unregistered; CPC 12/10 | 12/10 | LIVE |
| 13 | Hurricane worker proposals P2, IEM AFOS, P6 (TWOAT archive) | next hurricane pass | OPEN |
| 17 | AEO-13 attribution; SA CEC final 2026 estimate (11/26) not yet read | next pass | WATCH |
| 18 | King-tide follow-ups: (b) annual NWS-moderate+ tide days at FL gauges; (d) Florida Current transport; December view: re-read the mid-December West Coast residual (CO-OPS 12/1–15) before 12/23 | 12/22 | OPEN |
| 19 | Water proposals 11/05 (WSV fairway depths, `parameter=Q`); Hoover release; wildfire P21 | next pass | OPEN |
| 20 | Gatún at 1/1 and on each ACP draft advisory | 1/1 | WATCH |
| 22 | Summer CDD re-spec | 5/1/27 | OPEN |
| 23 | NorCal 11/25 highs ✅ confirmed 11/27 on complete-day data (KB-338); residue: CO-OPS verified (q=v) values | ~12/31 | ✅ DONE (PRELIMINARY data) |
| 24 | St. Johns crest: DeLand observed vs 6.33 (CORAL wakes 11/30, D:L1244; WALTER IMMEDIATE on an observed record) | 12/04 | 🟠 WATCH |
| 25 | Alert-vs-measurement pass on the other channels (promised to Will 11/23) | next session | OPEN |

Closed rows (#2, #5–8, #14, #16, #21) → archives named in the 11/27 full-file rotation.

---
## BOTTOM LINE

**2026-11-27 10:05 ET (PROME due-row wake, D:L1256):** No score moved; composite 15/30, fired 0 of 6. **The Northern California record held up on full-day data:** Arena Cove reached 9.216 ft MLLW on 11/25, a record even when the wave noise is averaged out; San Francisco, Humboldt Bay and Crescent City did not set records, and damage was roads, waterfronts and municipal piers, nothing of economic consequence. **Florida's St. Johns River is the live event:** DeLand read 6.21 ft at 08:30 ET, 0.12 ft under its 6.33 record, and the official forecast now holds 6.6 ft from Tuesday through Friday 12/04; I put an observed record by Sunday at about 85%. No condominium or apartment building is in reach on the current forecast: the first one named in the gauge tables (Sanford Landing Apartments) is at 9.5 ft at Sanford against a forecast 8.9. Colorado (C6, 4) is still the most important channel: Orange from 12/02, MWD vote 12/08 (AEO-18 50%).
