# Digest reader A: VULCAN, HENRY, VIOLET, BOND, SAM, ZHAO

Written 2026-11-25 16:10 EST (from date). Repository HEAD at read: b346e54387. Baseline: dc3ec2b130 (2026-11-25 00:37 ET). All six briefs read whole; "MOVED" built from git diff of each brief against the baseline, plus the matching STATUS diffs. Read-only; nothing else written. All desk intraday figures are vendor quotes, not closes; no 11/25 official close was in any of the six briefs.

## 0. Pin check and staleness summary

Result line (python3 scripts/brief_pin_check.py, repo root): "BRIEF-PIN 0 OK: 31 brief(s) checked against amendment 11 — OK-PINNED 21, OK-SAME-COMMIT 8, STALE-PIN 1, UNPINNED 1." The stale one is LIQUID (2 STATUS commits behind) and the unpinned one is RED; neither is in this set.

| Desk | Pin result | Brief commit (ET) | Newer than baseline | Content stale against own STATUS or owned state? |
|---|---|---|---|---|
| VULCAN | OK-PINNED 4e13fa0a02 | da99e03e44, 11:55 | yes | One figure older in the brief than in STATUS: CoreWeave 5Y CDS about 1,065bp [11/12] in the brief, about 1,314bp [11/24] in STATUS S5 (both dated). Unread inbound: CoreWeave 1,363 cancelled (LIQUID 11:52) still sits in KB-VULCAN-483, not in brief or STATUS. CoreWeave loan cards 031, 035, 036 unread. |
| HENRY | OK-PINNED 34ebb1ebf0 | 7954439e78, 15:37 | yes | Self-flagged: header says body intraday marks are overtaken (S&P 7,162.29, RSP +0.66% at 15:36) but View, odds and broadening markers still read 11:46 to 11:50 values (RSP -0.91%, S&P 7,004). STATUS body has the same 11:50 values, so this is brief and STATUS both behind the tape, disclosed. |
| VIOLET | OK-PINNED 1acf4452c4 | 218fbc9553, 10:19 | yes | Figures match STATUS. Both overtaken: HY 11/24 posted 372 (brief says "your 11/24 and 11/25 cells decide it"); VIOLET logged it at 15:40 and DEFERRED the grade to the registered 11/25 close read (D:L1280 item c). STATUS still says 11/24 HY not posted. D:L1280 is the DOCKET wake row carrying VIOLET's "D:L1229 item 4"; same obligation. |
| BOND | OK-SAME-COMMIT 230948aacc | 13:40 | yes | Figures match STATUS. WQ-750 RULED A (Will 13:54 ET, after the brief) settles the open question STATUS carries ("question with PROME"): scores stand, two rows to be rewritten as drafts 12/3. |
| SAM | OK-PINNED 547a7c6691 | e5e2974585, 09:40 | yes | Figures match STATUS. Overtaken by unread LIQUID packet (SoftBank CDS, 11:49) and 13 unread WALTER cards. |
| ZHAO | OK-SAME-COMMIT 9c862f7a44 | 11:06 | yes | Headline current. Lower blocks STALE on sends and waits: see section 6. |

## 1. VULCAN

HEADER: as of 2026-11-25T11:55:13 ET, STATUS pin 4e13fa0a02. S1 3, S2 2, S3 3, S4 3, S5 4 = 15/25 unchanged. One fired channel, S5 (WQ-464 retains 4; read together with S1, WQ-689 B).

VIEW: (1) 11/25 is a third supplier-led fall (11/20, 11/24, 11/25), equal weight holding and credit barely moving: an AI valuation de-rating, not a financing break. (2) Nothing fired; no capex cut by payers (next payer read about 2027-02-05), no pulled or flexed AI-infrastructure deal found. (3) The "new" export rule is the 11/16 rule repeated; Section 301 leaves AI hardware out except China-origin goods, a small slice.

MOVED SINCE BASELINE:
- 11/25 open, 09:32 ET vendor intraday (KB-479): NVDA 142.38 -8.37%, AMD -8.44%, MU -9.02%, ARM -8.68%, CRWV 38.75 -9.05%, IREN -10.31%, SMH -6.26%; payers -2.3% to -5.5%; SPY -2.40%, RSP -0.96%, HYG -0.20%, VIX 31.73. Moves S1 away from red. STATUS 11:47 to 11:49: NVDA -8.82%, RSP beat SPY by 1.84pp (KB-483). No letter.
- Export-rule headline (09:23 ET wire, citing The Information, unread) = FR Doc 2026-23529 re-reported (Federal Register API 11:43:50 ET; public inspection 11:44 ET, no BIS item). 90-day licence window for existing service ends 2027-02-17 (own count). Nvidia Q3 China incl. HK 11.05B dollars, 9.5%; outlook zero China data-center compute; Jefferies 44 to 62B is a relay. KB-480.
- AI capex as imports (FT-900, Jan to Sep): total computers, accessories, chips 590.8B (+94.3%): computers 296.7B (+99.5%), accessories 189.4B (+88.2%), semiconductors 104.7B (+91.1%). ATP: Taiwan 185.2B (+76.6%), Mexico 179.2B (+68.0%), Thailand +138%, Korea +176%, Malaysia +78%, China 39.8B (-16.6%, 4.2%). Answers ISHM's G.17 vs BEA gap; price not separated. KB-482.
- Entity List, 91 FR 76148, effective 11/23, published 11/25: seven Megaspeed-network entities (Malaysia 3, Singapore 3, Thailand 1). S4 YELLOW "new entity-list" label MET, first since 2025-10-09; score stays 3; VULCAN-193 not met. KB-476.
- CORRECTION (KB-481, KB-477 struck): China Section 301 notice CHARGES servers 8471, parts 8473.30, chips 8541/8542, fab tools 8486 up to 10%, no Section 232 exemption text. Exempt in Taiwan, Korea (up to 15% net of MFN), Malaysia (up to 18%) and, per ZHAO, Japan, Singapore, Vietnam, Thailand. 10% on all China tech imports at most about 5.3B a year; AI share unmeasured. Large transformers, switchgear, cable not found (PROVISIONAL).
- Tail named: a final notice dropping the Taiwan exemption, about 247B a year of Taiwan ATP.
- VULCAN-194 DEFERRED to 11/27 (10-Q not on EDGAR 09:33:27 and 11:47:34 ET); VOID by own criterion if none dated 11/25. Counts: 24 registered, 17 resolved, 7 open.
- Treasury 10-day ask to Nvidia's board: checked 11/25, no answer filed, row swept.
- S5 counterevidence: SpaceX GPU lease notes about 32.1B, A3 8.259%, upsized (COR-20261123-12); Fermi prepayment funded (8-K 11/23, amount and lease absent).
- "AI selloff predated the Huang news" holds on Reuters 11/6 (the 11/5 rout, about 3T dollars); the quote itself not found.

CROSS-DOMAIN: sends to TERRY, WALTER, ZHAO, BROCK, CARL, ISHM, HENRY, VIOLET, LIQUID, HAWK. Standing: Nvidia gross guarantees 118.0B at 10/25; S5 and S1 not to be counted as two alarms (addressed to NEXUS by name in the Desk column). CALIBRATION: VULCAN-194 P 0.15, VULCAN-193 P 0.20.

FORWARD: 11/27 VULCAN-194 grade, mag7 slot 12, GPU reading 12 (13:00 close) · 11/30 FERC EL26-67 via WATT · about 12/1 to 12/3 congressional Nvidia hearings (dates UNVERIFIED) · 12/4 Nvidia 10-Q deadline (12/9 with 12b-25, own arithmetic), GPU 13, mag7 13 · 12/8 FT-900 October (STATUS only, not in the brief's WATCH table) · 12/10 TSMC November 6-K, ERCOT Batch Zero, Ohio OPSB hearing · about 12/15 Oracle 10-Q (leg 4 reading 1) · 12/16 Micron (inferred date).

NEXUS-NAMED (row addressed "PROME / LIQUID / BROCK / VIOLET / NEXUS", unchanged since baseline, verbatim): "**WQ-689 RULED B (Will 11/16 11:39 ET):** S5 keeps 4 and core status; read it TOGETHER with S1 ('independence unsupported this quarter') until a test supports independence. Successor VULCAN-192, VULCAN-13's letter unchanged, to 2027-02-15. Do not count S5 as a separate alarm from S1 meanwhile."

## 2. HENRY

HEADER: as of 2026-11-25 15:37 ET (CoreWeave line and header note only; all else 11:46 to 11:50 ET), STATUS pin 34ebb1ebf0. Four HENRY STATUS/brief folds since baseline (09:09, 11:55, 15:37).

VIEW: Inflation steady at 0.3 with goods doing more of the work; the selloff held at 7,000 by same-day options (measured path; dealer side inferred); stress single-name, not index. Header overtakes this: S&P 7,162.29, RSP +0.66% at 15:36 ET vendor.

MOVED SINCE BASELINE:
- October core PCE (BEA 11/25): +0.2925%, 3.261% y/y (from 3.14); headline +0.3175%, 3.845%; real PCE 0.0%. Split: core goods +0.348% (Sep +0.178; fastest since Feb), housing +0.287%, services ex energy and housing +0.270% (from +0.389). Hot line (>0.3) NOT FIRED by 0.0075. Tariff attribution INFERRED (layer in force, not 301).
- Q3 GDP second estimate +4.3% (from +3.4), STATUS only, not in the brief.
- December hike: futures about 93% at 11:30 ET (own conversion; about 100% at 11/24 close). HEN-63 0.70 registered, NOT re-marked; unscored about 0.80.
- S&P 11/24 close 7,201.09 and VIXCLS 26.36 CONFIRMED on FRED: 11/21 upside marker's hold CONFIRMED (over yellow by 1.09). Was vendor at baseline.
- 11/25 intraday: low 6,970.11 at 09:45; 7,004.17 at 11:50 (-2.73%, 33 under red 7,037.04); 15:36 7,162.29.
- Red line: not fired on a close; a red close is a WALTER signal.
- Gamma (vendor chain, unpublished): NEGATIVE, flip 7,303 to 7,341 (baseline 7,300 to 7,439); walls withheld. 0DTE 7,000 top strike 61,000; pin expires 16:00.
- Credit FRED 11/24: HY 372 (+9), BB 225, CCC 1,405 (+18), CCC minus BB 1,180 (+55 in five sessions). REG-T-04 FIRED 11/23 (REGINALD grades).
- CORRECTION 15:37: CoreWeave 5Y 1,363 [11/25] withdrawn (trade CANCELLED); 1,314 clean [11/24], 4Y 1,379, Oracle 370 clean.
- Broadening markers at 11:50: HY over 376 on an RSP-down day: RSP -0.91%, HY 11/25 unread (by 15:36 RSP +0.66%, so the RSP leg would not qualify at that level); KRE under 65 NOT MET (69.18); HYG under 75.50 NOT MET (76.32).
- Odds (unscored, 11:50, conditions since reversed): close under 7,037.04 today about 65%, by 12/4 about 80% (baseline 35%); range 40 / broadening 45 / V 15 (baseline 50/30/20); HEN-65 (close at or below 6,700 by 12/4, frozen 0.40) about 12% (baseline 5%); 12/9 hike about 0.80.

CROSS-DOMAIN / CALIBRATION: TERRY handoff 2026-11-25_from-HENRY_midday-7000-pin-and-pce-split.md. No level, band, trade or gate changed. Brief has no separate CALIBRATION block. DROPPED from the brief since baseline without a retraction: the two-clocks table (RSP flat while HY widened, SMH -32.5%, staples +12.3%) and the n=6 HY-over-350 record; both remain in its 11/24 research.
FORWARD: 11/25 close vs 7,037.04 (docket CLOSE CHECK after 16:15) · 11/26 to 27 FRED HY 11/25 · 11/27 13:00 close · 12/4 payrolls, HEN-65 · 12/9 FOMC · 12/10 CPI · 12/23 PCE November.
NEXUS-NAMED: none.

## 3. VIOLET

HEADER: as of 2026-11-25 10:19 ET, STATUS pin 1acf4452c4. Thesis v4.1.10, no live gate moved.

VIEW: Monday's fade reversed in two sessions; cash curve inverted six straight closes (11/17 to 11/24). Vol led, credit followed, credit the stickier (gave back 13 of 24bp while VIX gave back 26%). No single cause established; chips carried the second leg.

MOVED SINCE BASELINE:
- History closes confirmed: VIX 26.62 [11/23], 26.36 [11/24]; VIX3M/VIX 0.9579, 0.9662; VVIX 114.07, SKEW 139.16 [11/24]; OVX 49.39, ratio 1.87 CALM; COR1M 24.62.
- 11/25 intraday: over 30 from 06:28, high 34.95 at 09:45, 31.91 at 09:58; VIX3M/VIX low 0.8587; VVIX high 129.05. Not graded.
- Regime RISING_VOL on 11/23 and 11/24 closes; a 30-plus close returns HIGH_VOL.
- HY 363 [11/23] between fade line (under 350) and lasting line (370 or more).
- Prediction 2': arms on a 7th inverted close, 11/25. Record since 2009-09: 13 reached 7; VIX stayed over 25 for ten closes in 5 of 13: 5 of 7 when day-7 VIX was 31 or more, 0 of 6 under. Unscored: 7th inversion about 90%, consequent about 40%.
- PRED-11 (close over 35.89 by 12/16, frozen 50%) unscored view 40%, up from 25%. Fade 60 to 65% and second-leg 35 to 40% lines dropped.
- FT-10 exit count on VIOLET's reading: 1 [11/20], reset 11/23, 1 [11/24]; RED grades.
- 40/50 convergence unchanged (11/20 basis), not re-scored.
- From VIOLET's 15:34 boot (VX_DAILY.tsv TICK, not brief): VIX 28.04, VIX3M/VIX 0.9372, VVIX 116.12, RISING_VOL; KB-VIO-408 CTA theme opened. At that level the 7th inversion arms but on the "under 31" side (0 of 6). Intraday, not a close.

CROSS-DOMAIN / CALIBRATION: LIQUID asked (11/24, 11/25 HY cells); RED owns FT rows; TERRY packet two-sided, no structure. Vendor print matched History on every spot cell; History high and low cells carry bad prints.
FORWARD: 11/25 close read (DOCKET L1280, carrying D:L1229 item 4) · 11/24 and 11/25 HY cells · about 12/4 Nvidia 10-Q · 12/16 December SOQ vs Z6 23.9769, PRED-11.
NEXUS-NAMED: none.

## 4. BOND

HEADER: last refresh 2026-11-25 13:3x ET, same-commit 230948aacc. thesis v1.2.13, posture FLAT. Was 11/18 at baseline (desk dark 11/19 to 11/24).

VIEW (brief is pointers; from STATUS): two of three month-end notes soft on indirect bidding, no failure: directs took the gap, dealers light ("expensive, not broken"). Yields fell the same week, front-led. HY crossed BOND's 350 line; no pulled deal verified.

MOVED SINCE BASELINE:
- Registered grades: 10Y TIPS 11/19 CLEAN (68.56) · 2Y 11/23 I-prime FIRE (51.54 vs 54.67) · 5Y 11/24 I-prime FIRE (54.28 vs 59.42; OLD indirect leg -0.03pp, dealer not met) · 7Y 11/25 CLEAN (58.20 vs 57.43; cover +0.01 thin). Clean-nominal counter 2 to 0 to 0 to 1. VX-BND-13 2 to 3. Auction health 3 unchanged.
- WQ-291 kill window opened by the 5Y fire: dealer leg FR2004 3 to 6Y as-of 11/18 to 11/25, MET if +8.6B or more, due about 12/3; funding window UNGRADED; 2Y fire has no dealer letter. Sleeve flat.
- Rates 11/24: 2Y 4.63, 5Y 4.69, 10Y 4.91, 30Y 5.30 (down 17/20/16/11bp from 11/18); real 10Y 2.79 (run 52 over 2.50); 30Y run 98 over 5.00; ACM 0.6518 (was 0.7475 [11/17]). Vendor 10Y 4.84 at 13:15 ET.
- Credit: HY 352 [11/19], 376, 363, 372 [11/24], over 350 four sessions; CCC 1,405, IG 98. HY function 3 to 4; BND-34 TRUE (11/19). Matrix 17 to 18/35. Open predictions 4 to 3 (BND-35 to 37).
- SOFR minus IORB +4bp [11/24]. FR2004 long end 150.4B [11/11]; as-of 10/21 REVISED to 138.0B from 150.816B.
- PMMS 7.21 [11/25] minus 10Y 4.92 [11/23] = 229bp (was 213), inside 180 to 230, 1bp under the edge.
- Buybacks next 12/2, 12/8. After the brief: WQ-750 A (Will 13:54 ET): VX-BND-13 3 and VX-BND-02 4 stand, two rows to be rewritten as drafts 12/3.

CROSS-DOMAIN / CALIBRATION: LIQUID owns tier and funding verdicts; ORACLE owns December odds; TERRY told no card. No CALIBRATION block.
FORWARD: about 11/27 FR2004 as-of 11/18 · 12/2 and 12/8 buybacks · 12/3 WQ-291 grade, freeze bars for 12/7 3Y, 12/8 10Y, 12/10 30Y · 12/9 FOMC · 12/17 BND-36.
NEXUS-NAMED: title only, "BOND → NEXUS — current owner pointers".

## 5. SAM

HEADER: as of 2026-11-25T14:40Z (09:40 ET), STATUS pin 547a7c6691.

VIEW: SoftBank is at its own 25% loan-to-value line (estimate). Yen: no carry unwind and no haven bid. BOJ rate support for the yen softened.

MOVED SINCE BASELINE:
- SoftBank LTV, SAM arithmetic, Arm 146.41 (09:36 ET vendor; 11/24 close 161.56), USD/JPY 159.23, all else at 9/30: 24.7% / 25.0% / 25.3%; 25.9 to 26.5% if ABB closed on debt. Was 22.4 to 22.5% at Arm 183.26. Reported 15.9% at 9/30. 25% is policy, not a covenant (none found); 35% needs Arm about 42 to 58. OpenAI mark -10% = about +0.9 point.
- RETRACTED: the 11/18 "+2.3 points if the 11B junk bond is new money" bracket (title matches the September deal already in base). Also 25% crossing prices re-cut: Arm 142.8 / 146.2 / 150.1 (STATUS) vs 146 to 150 at baseline.
- SoftBank equity -14.8% in Tokyo (2,696.5 yen); no bank or household break found.
- USD/JPY 159.23; no touch of 160 since 11/13 (H 160.188); velocity not fired (largest range 1.433 on 11/20, yen strength). VIX-over-30 days 11/20 and 11/25: yen +0.77% and about 0; AUDJPY -1.9% since 11/18. CFTC 11/17 +116,317 long (was +123,113).
- BOJ December 71% (Totan 11/25, incremental equivalent, not a probability; 84% on 11/18). JGB 10Y 2.781, 30Y 3.990 (MOF 11/24; peak 4.082 11/18). National October core-core 2.2 (from 2.4). 40Y 11/25 2.625x, lowest of 2026, descriptive.
- MOF monthly total about 11/30: SAM expects zero, 85 to 90% unscored. H.4.1 11/18 shows no Japanese funding move (LIQUID).
- 11/18 material dropped: New York Fed Q3 FX report, auction SOFT grades (still in STATUS).

CROSS-DOMAIN: PROME packet; TERRY packet (no card asked). WAITING: MOF total, TERRY answer, SoftBank filings, offshore basis. CALIBRATION: 35 rows, 16 CONFIRMED / 16 FAILED / 1 special / 1 qualified / 1 OPEN (SAM-33 72%); November ops after 11/18 not audited.
FORWARD: 11/26 MOF weekly, BOJ ops · 11/27 Tokyo CPI · 11/30 MOF monthly total, 2Y auction · 12/17 to 18 MPM · 12/31 SoftBank quarter-end LTV. Fork: Arm under about 130 (central 26.5% plus).
NEXUS-NAMED: schema footer only, "Schema owner NEXUS (`AGENTS/NEXUS/templates/NEXUS_BRIEF_SCHEMA.md` §4.1)."

## 6. ZHAO

HEADER: as of 2026-11-25 11:05 ET, STATUS folded in the same commit 9c862f7a44. 29/60 ELEVATED unchanged (two-sided shadow 32 in STATUS; the brief's 10/29 bullet still prints 28/60 and shadow 31, dated).

VIEW: Section 301 proposal re-creates the truce's 20% China layer in a new legal form; not escalation unless the 40% branch survives. China answered with words plus an extension, no countermeasure. Home demand still contracting (October NBS); no forced Treasury selling.

MOVED SINCE BASELINE:
- USTR China notice (pre-publication, read at USTR): up to 20% net of the forced-labor s.301 rate only (2018 duties stack; about +7.5 points if that is 12.5%, INFERRED); up to 10% on 2,122 lines every other notice exempts; 77 consumer lines exempt; 40% alternative; comments 1/5, hearing 1/25, no effective date (KB-290, 291).
- MFA "a false proposition"; MOFCOM Ga/Ge/Sb/graphite pause for the US extended to 2027-01-27 (公告2026年第59号, KB-293). 11/27 clock closed EXTENDED.
- Chen Jining (Politburo, Shanghai) under CCDI investigation, Xinhua 11/24: no market read separable (KB-294).
- NFRA rural NPL 2.895: watch (2.9) NOT MET (KB-295). Trump–Xi 11/19: no instrument (KB-296). STATUS: Shanghai -2.03%, USD/CNY 6.66, Brent 89.65 at 10:58 ET.
- Re-graded rows written 11/18 to 11/20 as checked: ZHA-22 YES (Brier 0.16, not new). No score changed.

CROSS-DOMAIN / CALIBRATION: V5b rescore owed. ZHA-23 (November mfg PMI under 50.0) 68%. Conviction China UST selling MEDIUM, DECELERATING (LT -15.8, -7.7, -4.8, -3.5B).
FORWARD: 11/30 NBS PMI ZHA-23 plus construction second print (new orders clear 47 with headline over 47.5) · any Chinese numbered answer to 301 · about 12/17 October TIC (date unconfirmed) · 1/5, 1/25, 1/9, 1/10, 1/27 clocks (five texts, do not merge).
NEXUS-NAMED (new 11/25, verbatim): "★ **11/25 — for NEXUS: the US Section 301 'excess capacity' proposal re-creates the truce's 20% China layer in a new legal form; it is not an escalation unless its 40% branch survives.**" Older ones still in the header or VIEW, unchanged: "★ **11/17 — for NEXUS: China's answer to the new US chip rule is a conditional threat, not a measure**"; "★ **11/16 — for NEXUS: China's October home demand is still contracting**"; "★ **11/11 — for NEXUS: the December Fed hike now priced (ORACLE: +25bp 85.5, +50bp or more 11.8) does NOT make China a forced Treasury seller.**"; "**★ 11/06 — FOR NEXUS: the two-clock story is now one clock, and the domestic read weakened.**"; "**★ 10/29 — FOR NEXUS: the PBOC's currency posture has fully reversed, and the desk's gauges could not see it until today.**"; "**🟠 10/9 — FOR NEXUS: a pre-registered tripwire fired and I applied it AGAINST my own read.**"

STALENESS (trigger (a), brief vs its own STATUS, sends and waits): SENDING table carries none of the five 11/25 sends STATUS lists (WALTER, VULCAN, CARL, TERRY, MIDAS); the 11/17 header star still says the Ga/Ge/Sb ban "re-arms 11/28 unless renewed" although the same Status line says it was extended to 1/27; NEXT DECISION POINT still reads 11/19 Trump–Xi as ahead while its own FORWARD table closes it; FORWARD's "Sat Nov 7" row is unticked; WAITING rows for VULCAN and LIQUID date from 11/10 and 9/19; the Entity-List binary says "next 11/9". Figures at the top are current.

## 7. Cross-brief section

1. HY OAS 372 [11/24] is cited by HENRY and BOND (and TERRY, LIQUID), from the same FRED ICE series: one observation. VIOLET's brief still carries 363 [11/23]; VIOLET's own written "lasting" condition (370 or more) is met by 372, grade deferred to the 11/25 close read. TERRY STATUS already treats 370 as met (VIX leg, no build today).
2. Threshold meanings differ on the same series: BOND 350 (function 3 to 4), HENRY 320 yellow / 376 broadening marker / 400 orange, VIOLET 350 fade and 370 lasting, REGINALD 350 three days (FIRED 11/23). Agreement on the print, four ladders.
3. Credit read splits: BOND lifts HY function to 4 and HENRY holds broadening at 45%, while VULCAN calls the 11/25 leg a de-rating with credit barely moving (HYG -0.20%) and HENRY calls stress single-name. Not a clash of figures: index ETF and single-name CDS vs the option-adjusted spread; HENRY and BOND also say no pulled deal verified.
4. VIX basis: VULCAN 31.73 (09:32), VIOLET 34.95 high (09:45), HENRY 33.71 (11:50), VIOLET's 15:34 tick 28.04: one instrument, different clocks. VIOLET's split at 31 on day 7 is the line the close decides; the 15:34 tick sits below it.
5. S&P red 7,037.04: HENRY's 65% for a close under it was set at 11:50 with S&P 7,004; by 15:36 S&P was 7,162. Treat the 11:50 odds as dead; the close decides. VIOLET's record of the session low (6,970 at 09:45) matches HENRY's.
6. December Fed hike has three figures: HENRY about 93% (futures 11:30 ET), BOND about 96% (STATUS, vendor 13:12), ORACLE 97 (Kalshi, 11/18 dated read, owner). ZHAO's header still prints ORACLE's 11/11 read (85.5 and 11.8). HENRY's own forecast 0.70 is a different object and not re-marked.
7. CoreWeave 5Y CDS: HENRY corrected (1,314 clean [11/24]; 1,363 CANCELLED). VULCAN's KB-483 still holds the cancelled trade; VULCAN STATUS S5 uses 1,314; VULCAN's brief carries only 1,065 [11/12]. LIQUID now headlines dirty 1,359 [1,314 clean]; mixing bases would look like a widening.
8. Arm price links SAM and VULCAN: VULCAN ARM -8.68% at 09:32, SAM at 146.41 (09:36), LIQUID 148.23 at 11:47. SAM's CENTRAL case is the 25.3% leg (carry plus SB7; 25% at Arm 150.1, per its re-roll table); the other legs cross at 146.2 (carry) and 142.8 (no drift). At 148.23 the central leg is still over 25% and the other two are under. One price input, not two confirmations. SAM's brief prints three figures without saying which is central. LIQUID's SoftBank CDS (5Y 466 clean / 471 dirty [11/24]; 3.5Y 548 / 555 [11/25 09:32 ET], 5Y near 560 to 600 INFERRED from one trade) is unread by SAM.
9. China 301 and export rule: ZHAO and VULCAN agree after VULCAN's correction (China annex charged up to 10%; exempt elsewhere). VULCAN's "servers and chips left out" from its own morning is struck. WALTER card 015 carries the same fix. Remaining gap: neither read the "Scope Limitations" column row by row.
10. Rates and foreign demand: BOND says yields fell and indirects drew less in front-end notes (inference, not established); ZHAO says China is not a forced seller; SAM says no Japanese operation seen; HENRY calls the rate path hike-side. Compatible, but BOND's inference is the only one offering a foreign-demand cause and it is marked unestablished.

Common-root note for the antecedent map (reader's inference, for NEXUS to test): the 11/25 selloff entries in VULCAN, HENRY, VIOLET and SAM (Arm) are one price event; credit widening in HENRY and BOND is one series; BOND's auction fires are the only item in the set with a separate origin.
