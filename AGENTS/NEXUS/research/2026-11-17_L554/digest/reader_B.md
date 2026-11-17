# Reader B digest: VULCAN, CARL, ISHM, CYPHER, ZHAO

Reader: read-only digest reader for NEXUS. Run 2026-11-17. Baseline for "moved since": commit 3db8291eff (2026-11-16 21:04 ET).
Read state: all five briefs read whole. `git status` shows none of the five briefs modified in the working tree, so working tree = HEAD for these files. Nothing unreadable.

Commits touching these briefs since 3db8291eff:
- ae3c45b654 VULCAN: NEXUS_BRIEF rebuilt for 11/17 (Nvidia print, VULCAN-17 HIT), pinned to bfc8a71fe7 (2026-11-17 16:55:26 -0500)
- e856a46fa5 CYPHER: NEXUS brief re-pinned to 54ff816a8f (Optimizely, outage list) (2026-11-17 12:42:05 -0500)
- fe85e90b1a ZHAO: VULCAN rule packet processed (FR 2026-23529 publishes 11/19); outbox delivered; closeout (2026-11-17 12:11:05 -0500)
- 6f678bd18d ZHAO -> PROME: China chip-rule reply is a conditional threat, no measure; 3 routes proposed
- c7132fa06a CARL: NEXUS brief fold 11/17 (pin 220041a23e; retail read, CRL-34 CONFIRMED) (2026-11-17 12:07:40 -0500)
- 0b4f0b08b9 ISHM -> PROME, HENRY: October IP delivery packet, HENRY informed; NEXUS brief (2026-11-17 09:19:55 -0500)

Pin check (`python3 scripts/brief_pin_check.py`, repo root). Overall line: "BRIEF-PIN 1 STALE: 31 brief(s) checked ... OK-PINNED 15 · OK-SAME-COMMIT 10 · STALE-PIN 3 · UNPINNED 3." None of the 3 stale pins is in my set.
- CARL: ✅ OK-PINNED, pin 220041a23e = STATUS HEAD
- CYPHER: ✅ OK-PINNED, pin 54ff816a8f29a1a8f5cc7099364405d8f01eedc2 = STATUS HEAD
- ISHM: ✅ OK-PINNED, pin 25cd59c04493a096431ca17090d866bdf8d287ae = STATUS HEAD
- VULCAN: ✅ OK-PINNED, pin bfc8a71fe7 = STATUS HEAD
- ZHAO: ✅ OK-SAME-COMMIT, brief and STATUS last committed together in fe85e90b1
A PASS proves the pin, not the content.

---

## 1. VULCAN (AI capex, semiconductors, memory)

**HEADER:** As of 2026-11-17T16:54:51-05:00 | STATUS commit bfc8a71fe7 (STATUS HEAD committed 2026-11-17 16:54:43 -0500). Pin check PASS (OK-PINNED). Variant FULL. Score S1 3 / S2 2 / S3 3 / S4 3 / S5 4 = 15/25, unchanged.

**VIEW:**
- Nvidia beat its own outlook and guided the next quarter up 12% (about 4% on a like-for-like 13-week basis), no customer cut stated; supply commitments rose to $390B, mostly memory. Supplier strength, not a payer read; payer capex guides come at the Q4 cluster (~2027-02-05).
- Softer threads stated, small, unexplained: neocloud commitments down $4B, longer payment terms, margin guide lower, China data-center compute excluded. Nvidia customer guarantees $118.0B and the Fed names GPU-maker residual-value guarantees and about $1T bank exposure: financing web keeps growing, no stress letter.
- BIS chip rule tightens supply-side controls without meeting an S4 tripwire. 15/25.

**MOVED SINCE 3db8291eff:**

Nvidia Q3 FY27 results, exactly as the brief states (row sourced KB-453, KB-455; 8-K acc 0001045810-26-000088, accepted 11/17 16:20:51 ET, Ex 99.1/99.2/99.3 read whole; call not heard):
- Q3 revenue $115.844B, "$7.8B above its $108.0B outlook midpoint and above the top of the range". Header rounds it "Q3 $115.8B above its own range".
- Data Center $107.6B (Hyperscale $60.1B, AI Clouds/Industrial/Enterprise $47.5B).
- Q4 outlook GIVEN by interim CEO and CFO Kress: $130.0B ±3%, a 14-week quarter "(+12.2% over Q3; about +4.2% scaled to 13 weeks, my arithmetic)" (VULCAN's own arithmetic).
- "'not assuming any Data Center compute revenue from China'".
- Gross margin guide 71–72% vs 74.8%.
- "No order cut, deferral or customer loss stated".
- Stated softer items: consumer PC demand hit by memory prices; neocloud agreements $36B → $32B (no reason); longer payment terms for some IG customers (DSO 64).
- Supply commitments $279B → $390B (memory).
- China by HQ 9.5% of revenue; DC Hopper to China $2.4B.
- "A statement, not a grade; TERRY recorded its NVDA card dead, T1 failing at (c) (TERRY's grade). A supplier beat is not payer capex: no S1 letter."

Capex, financing, guarantee and order statements new since baseline:
- **VULCAN-17 HIT** (KB-454): Nvidia's maximum gross guarantee exposure at 10/25 is $118.0B (neocloud land, power and shell $3.5B + SB Energy $105.0B, "now in the table" + power and systems credit support $9.5B, "new"); no payments made. Build phase continues. Caveat verbatim: "⚠️ The registered two-line perimeter ($108.5B in billions) cannot be told from the $108,529M baseline; the HIT rests on the new line." Re-read at the 10-Q (~11/19) in millions; VULCAN-18 perimeter set there; "EXIT leg 4(b)'s instrument changes only via PROME to Will." CALIBRATION restates: "VULCAN-17 HIT on the interim 8-K ($118.0B vs $108,529M; basis caveat: the HIT rests on a guarantee class the issuer added, the two-line perimeter is not separable at billions precision)".
- **Fed FSR (11/13) Box 2.2 at the primary** (KB-452): AI-computing issuance above $680B by October; public debt above $1.1T; not-yet-commenced leases above $1T and take-or-pay and residual-value guarantees above $2T, undiscounted; largest bank holding companies close to $1T exposure; GPU makers' residual-value guarantees named as a class. "Context, no S5 letter."
- **Meta €9.0B closing 8-K [KB-450]**: named in the Variant header line only; no body row describes it. The prior "closing papers" row (KB-408, "€9.0B settles about 11/12") was removed in this rebuild. No figure beyond "€9.0B" is given for KB-450.
- No order cut stated by Nvidia (above). Supply commitments $279B → $390B.

Policy and governance, new:
- **BIS remote-access interim final rule** (FR Doc 2026-23529, effective 11/19), read at the primary (KB-446): licences for advanced chips to data centers anywhere serving Macau/D:5-headquartered firms above 12,000,000 aggregate TPP (existing service 90 days) and to Indonesia, Malaysia, Singapore, Thailand, Brazil (US-HQ exempt with monthly reports); AI Diffusion Rule rescinded. No Entity List entry, equipment ban or fab cutoff: S4 stays 3.
- Nvidia 50% no-sell policy: CLAIM ONLY (KB-447).
- China's countermeasure threat names no measure (ZHAO) (KB-449).
- "Nvidia's 8-K does not mention the rule; silence is not evidence of no effect."
- Huang's conditional offer to return on record (statement on X and to CNBC, 11/17); board's refusal is three unnamed sources (Reuters); Nvidia filed nothing. Governance, no letter (KB-451).

Fires, grades, kills, retractions:
- VULCAN-17 HIT (11/17, KB-454).
- TERRY's NVDA card recorded dead, T1 failing at (c) (TERRY's grade, relayed).
- CALIBRATION count moved: "22 registered, 16 resolved, six OPEN" → "22 registered, 17 resolved, five OPEN; none due". VULCAN-18 "to be registered" at the 10-Q.
- "No letter fired" (header).
- Status line adds "S5 read together with S1 (WQ-689 B)" (ruling dated 11/16, already in baseline body; now in Status).
- No retraction.

Rows removed in the rebuild (rotation; not stated as retractions): Nvidia 11/9 intraday row (KB-409); card 002 Anthropic gas/loan/Broadcom row (KB-410); Meta/Alphabet closing papers (KB-408); own-comparable spreads Oracle +145 to +175bp, Meta +57 to +88bp (KB-351..353); HENRY three-name backlog $188.3B / four-name capex $207.3B (KB-349/350); BROCK CoreWeave DDTL verification (KB-369/370/372); WATT Texas moratorium / Jupiter / TrendForce Lighthouse (KB-348/362/367/373); HENRY/CARL "S2 stays 2" Qualcomm/Micron (KB-363/371/375); WATT/DEWEY CME GPU futures review to 2027-01-08 (KB-356; still in WATCH). Watch row 2026-11-17 Nvidia results removed (fired).

Unchanged figures still carried (baseline already had them; listed for completeness): Treasury/Bessent 10-day demand, NVDA $155.62 −4.44% vendor intraday 13:48 ET [date of that quote not restated beyond the 11/16 context row]; Slot 10 Mag-7 32.6020%, NVDA 6.1380% (holdings 11/12); GPU reading 10 (CoreWeave 6.155, Nebius 4.50, Crusoe 3.90; SDH100RT $3.10, OCPI $3.39); CoreWeave 10-Q and 8-K figures; Nebius Q3; TSMC October NT$586,890mn, Jan–Oct +43.3%.

**CROSS-DOMAIN / CALIBRATION:**
- Names TERRY (NVDA card dead, TERRY's grade), PROME/LIQUID/BROCK/WATT (VULCAN-17, EXIT leg 4(b) only via PROME to Will), ZHAO/HAWK (BIS rule; China countermeasure is ZHAO's), BROCK/LIQUID/REGINALD/GIBBS/SHADE (FSR), DEWEY (T3 inventory direction at 10-Q).
- Uncertainty: the VULCAN-17 two-line perimeter is not separable at billions precision; HIT rests on a new guarantee class. Nvidia 8-K silence on the BIS rule "is not evidence of no effect". Neocloud $36B → $32B has "no reason" stated. IREN case "A reader could weigh IREN the other way" (VULCAN-13 MISS row, 11/16).
- S5 must not be counted as a separate alarm from S1 (WQ-689 B) until a test supports independence.

**FORWARD (~3 weeks):**
- ~11/19: Nvidia 10-Q (ESTIMATED from cadence): guarantee notes in millions, VULCAN-18 registration, DOCKET L322 T-tests (T1–T4, T6), DEWEY T3 inventory direction, headquarters table.
- 11/19: BIS rule effective (from the cross-domain row).
- 11/20: Mag-7 slot 11 (first reading with the 11/13 selloff); GPU reading 11; SoftBank Q2 transcript last check; NextDC AGM.
- ~11/25: Treasury's 10-day ask to Nvidia's board (11/25 is VULCAN's own count).
- 11/27: GPU reading 12; Mag-7 slot 12; renew GPU cadence before 11/27.
- 11/30: consume WATT's read of FERC EL26-67 responses.
- 12/04, 12/11: Mag-7 slots 13, 14.
- 12/07: Project Jupiter air permit hearing.
- 12/10: TSMC November 6-K; OPSB hearing (PORTS, Piketon); ERCOT Batch Zero reports.
- ~12/15: Oracle Q2 FY27 10-Q (thesis-kill leg 4 reading 1 of 2); ORCL $3.3B lessor guarantee follow-up.
- 12/16: Micron FQ1 FY27 (INFERRED date), VULCAN-190 reading.
- Beyond: 2027-01-08 CFTC GPU futures review end; 2027-01-10 MOFCOM and BIS affiliates clocks; 2027-02-05 hyperscaler Q4 cluster; 2027-02-15 VULCAN-192.

**NEXUS-NAMED (verbatim):**
- Row addressed "PROME / LIQUID / BROCK / VIOLET / NEXUS": "🆕 **WQ-689 RULED B (Will 11/16 11:39 ET):** S5 keeps 4 and core status; read it TOGETHER with S1 ('independence unsupported this quarter') until a test supports independence. Successor VULCAN-192, VULCAN-13's letter unchanged, to 2027-02-15. Do not count S5 as a separate alarm from S1 meanwhile." (row unchanged since baseline)

---

## 2. CARL (US consumer stress)

**HEADER:** As of 2026-11-17 12:07 ET | STATUS commit 220041a23e (STATUS HEAD 2026-11-17 12:07:19 -0500). Pin check PASS (OK-PINNED). Thesis v2.6.6. Status 🔴. Score 53/70 unchanged.

**VIEW:**
- Concentrated household strain persists; broad spending collapse remains unestablished.
- 11/17: October control group +0.59% after September revised up to +0.53%: aggregate spending held; the squeeze is a wallet-share shift (gasoline share up), not falling goods volume.
- Import prices ex-fuel +0.80% (goods pipeline) vs October core goods CPI +0.16%; no score moved.

**MOVED SINCE 3db8291eff:**
- New row 11/17, answer to WALTER SIG-W-20261117-004 (Census CB26-181 primary; BLS import prices via FRED, bls.gov 403):
  - October retail +0.21%; ex-autos +0.63% ("the card's +0.21% ex-autos was the wrong series", a correction of WALTER's card); control +0.59% (about +0.43% real); autos −1.60%.
  - September control revised +0.14 → +0.53%.
  - Gasoline 9.17% of retail dollars vs 7.52% a year ago.
  - Import prices +1.05%, ex-fuel +0.80%, about 70% not fuel; no true October y/y.
  - "TERRY: no CARL investment implication (WQ-696). T1 2 of 3 against." KB-623/624; research/2026-11-17_retail-imports/READ.md.
- **Retraction:** "the 10/15 'core goods stalled' read is withdrawn by revision" (11/17 VIEW bullet).
- **CRL-34 CONFIRMED 11/17 at 72%.** Basis: EIA 11/16 regular $3.805 added (prior: AAA 11/10 $3.979, 11/11 $3.943; EIA 11/09 $3.995). KB-616. Previously "CRL-34 leg 1 of 2 (leg 2 = 11/16 print)".
- V5 downgrade clock: was "day 2 of 14 (earliest 11/24)"; now "runs to 11/24 (AAA letter, separate)".
- New VIEW bullet 11/17: October core goods CPI +0.16% (undated beyond "October").
- NEXT DECISION POINT: CRL-34 leg 2 removed (done); now V5 check Tue 11/24, then CRL-32 leg 1 BEA Wed 11/25 08:30 ET.
- FORWARD: 11/17 EIA row removed (fired); new row 12/16 November retail "Does the control group hold?".
- Closeout line moved from 11/11 (WQ-249, prome-2b) to 11/17 (PROME prome-19). "Score 53/70 unchanged; no mark moved."
- No score moved; no other grade.

**CROSS-DOMAIN / CALIBRATION:**
- Ex-fuel import pipeline is HENRY's rates input. TERRY: no CARL investment implication (WQ-696).
- 11/10 kill-rule divergence sits with Will via PROME (RED's CHG-RED-045 re-review 11/17); CARL proposes nothing.
- Uncertain about: FY2026 ALLY vintage (nine months old); September real spending and saving composition; student-loan cure share (ES-04 not gradeable; STUE 10/28 ES-01 NO VERDICT, KB-568).
- Conviction: concentrated-strain direction MEDIUM-HIGH; broad-collapse timing/level LOW. Score is a registered-rule tally, not independent confirmations.
- Tensions: BofA, PNC/Velera realized activity and Conference Board rebound challenge broad collapse; ISHM freight-volume counterevidence compatible. Real risk channel is jobs (LABOR) (11/11 row). Capital One modified-card jump cause UNKNOWN; REGINALD owns bank read.
- Retail figures are nominal with no cohort split.

**FORWARD (~3 weeks):**
- 11/20 10:00 ET: Michigan November final (long-run <3.0% is V12's trigger).
- Mon 11/23 11:00 ET: AFT v. ED conference (CRL-13 denominator).
- Tue 11/24: AAA <$4.00 two weeks, V5 4→3 registered trigger.
- Wed 11/25 08:30 ET: October PCE/income, CRL-32 leg 1 (Z.1/DFA cohort read 12/10; final grade 12/23).
- ~11/30: EART October 10-Ds (V2 tier read).
- Fri 12/04: November payrolls, V16 print 2 of 2 (October +165K, R +84K counted print 1).
- Dec 8–9 (12/09): FOMC, V12 un-fire count.
- 12/16: November retail.

**NEXUS-NAMED (verbatim):** NEXUS appears only in the "To" column of these SENDING rows; none is new since baseline except that the AAA row's text changed:
- "PROME / BRENT / NEXUS | AAA regular under $4.00 (11/10 $3.979, 11/11 $3.943); EIA 11/09 $3.995, 11/16 $3.805. | Boot pull / 11/17 | **CRL-34 CONFIRMED 11/17 at 72%.** V5 downgrade clock runs to 11/24 (AAA letter, separate). No score moved. KB-616." (changed)
- Other NEXUS-addressed rows (unchanged): "PROME / NEXUS / REGINALD / CORAL" (11/11 airfares and Citi); "PROME / RED / NEXUS" (11/11 October core +0.296%, Waller 50bp); "NEXUS / RED / REGINALD" (10/28 catch-up); "NEXUS / RED" (PNC September card spend); "NEXUS / REGINALD" (Edmunds/PNC Gen Z); "WALTER / NEXUS" (EIA October19); "NEXUS / REGINALD / RED" (ALLY matched vintage, CRL-21 MISSED); "NEXUS / REGINALD" (RITM Q3); "PROME / NEXUS" (L786); "NEXUS / ISHM / FERT" (bounded intake); "NEXUS / REGINALD / RED" (Capital One modified card); "PROME / NEXUS" (CARL file audit).

---

## 3. ISHM (US manufacturing, equipment, freight)

**HEADER:** As of 2026-11-17 09:19 ET | STATUS commit 25cd59c04493a096431ca17090d866bdf8d287ae (STATUS HEAD 2026-11-17 09:19:20 -0500). Pin check PASS (OK-PINNED). Status 🟡.

**VIEW:**
- Physical equipment buying well supported; factory upturn "real but narrow and slowing", durability unproved (wording changed from "strong but slowing").
- October survey strength has not shown up as broad measured output (G.17).
- Scores unchanged: 18/35 raw, shared-root 13/25; equity thermometer UNKNOWN/excluded.

**MOVED SINCE 3db8291eff:**
- New "November 17 due-row wake": Fed G.17 October (PRIMARY, preliminary): total IP −0.4% (utilities −4.3%); manufacturing +0.3% for a second month but −0.1% excluding motor vehicles and parts; business equipment +1.0%; utilization 76.4%. "VX-ISH-02 unchanged at 2; annual revision November 24 restates levels. No score, band, gate or threshold changed."
- Status line wording: "factory upturn strong but slowing" → "factory upturn real but narrow and slowing".
- HENRY SENDING row now leads with "November 17: October IP, manufacturing +0.3% but ex autos −0.1%, business equipment +1.0%."
- November 13 due-row wake line removed from the header (rotation; its facts still in the LIQUID/RED row).
- November 16 wake (already in baseline, unchanged): Cass October +5.9% y/y NSA, SA m/m +1.7%, J2 NOT-MET; Empire November general 7.8 from 25.5, new orders 3.0 from 23.2, employment 18.1.
- No fire, grade, kill or retraction. No score, band, gate or threshold changed.

**CROSS-DOMAIN / CALIBRATION:**
- VULCAN owns the AI-capex verdict (computer imports September +150.96% y/y, Q3 +28.639% q/q, one Census vintage; nominal, not AI-only).
- Inflation read stays CARL's (S&P output prices steepest since September 2022; ISM prices 75.2 from 77.9). LABOR keeps the payroll figure (+19K October). Credit and probability reads stay with LIQUID, RED.
- Tension: physical equipment and freight strength can coexist with LIQUID credit/funding stress; financing transmission not cleared.
- Uncertain about: whether order strength is end demand or buyers locking in stock and prices; nominal imports and real SAAR not comparable.
- Failure patterns: BEA equipment includes imports, so the three J1 legs are not three independent confirmations; ISM and S&P share one month's activity; an acquisition can read as organic backlog (Parker / Filtration Group).
- RED counter-frame: slower orders with rising prices and longer lead times also fit a supply squeeze.
- Brief states "No recipient consumption is claimed" for the November 6 packets.

**FORWARD (~3 weeks):**
- November 19: Philadelphia and Kansas City Fed, November (regional sign; band OWED).
- November 20 (desk recheck): ACT Class 8 October final vs preliminary 13,500.
- November 24: Fed G.17 annual revision.
- November 25: BEA Q3 second estimate; durables October advance; Deere fiscal Q4 (call 10:00 ET).
- December 1: S&P final 09:45 ET (R1 two-branch grade, WQ-643 A, one print, does not roll), ISM 10:00 ET (strict <47).
- December 2 / 3 / 8: November rail batch / October full M3 / October FT-900.
- December 14: Cass November. December 31: Honeywell, Union Pacific date recheck.

**NEXUS-NAMED (verbatim):** none (NEXUS appears only in the title "# ISHM — NEXUS Brief"; ISHM sends no row to NEXUS).

---

## 4. CYPHER (cyber events)

**HEADER:** As of 2026-11-17 12:41 EST | STATUS commit 54ff816a8f29a1a8f5cc7099364405d8f01eedc2 (STATUS HEAD 2026-11-17 12:40:54 -0500). Pin check PASS (OK-PINNED). Status 🟠. As-of note: "PROME summons prome-19 on WALTER PRIORITY cards 20261117-008 and -011: five new incident rows 073-077, VX-05 3 to 4 on the letter, new map row CHK-42; no row fired; no prediction or gate moved".

**VIEW:**
- New 11/17: a confirmed vendor poisoning (Optimizely) reached named financial firms' customer pages, a channel the chokepoint map lacked (CHK-42 added); customer-side and short; no bank's own systems reported breached.
- The week's six US outages have no common cause on the evidence; do not read them as one campaign.
- PHP2Shell wave: still no named organisation; R1 flip not met; 1 row fired (KEV 10/26), none new.

**MOVED SINCE 3db8291eff:**
- **CYB-INC-073 Optimizely Web Experimentation compromise CONFIRMED** at the vendor's status page (11/17 row): injected JavaScript on 178 organisations' pages 11/16 per Report URI; 32 in banking and finance (2 US banks, a US credit bureau, 3 US lender brands; names in the research record); card skimming on own forms ~9.5 h; contained by 23:11 UTC; counts of cards or sessions taken NOT ESTABLISHED; no firm statement found. Priority P1 (REGINALD, GIBBS), P2 (VULCAN), P3 others. "TERRY: no investment implication on CYPHER's read".
- **VX-CYP-05 3 to 4 ORANGE on its letter** ("composition, not damage"). Composite moved 24/40 raw, 15/40 shared-root-adjusted (older row, "at 11/12") → 25/40 raw, 16/40 adjusted (11/17 row).
- **New map row CHK-42** (vendor poisoning of customer-facing pages).
- **Five new incident rows 073-077** (11/17):
  - 071 Microsoft (not cyber; already in baseline as 11/12-11/14 outage).
  - 074 AWS US-EAST-1 11/15 06:05-09:21 ET (AWS Health Dashboard, no cause stated).
  - 075 United (~30 min, not cyber).
  - 076 FAA (one Arkansas router).
  - 077 NSA Net (REPORTED, CNN six sources, no evidence of cyberattack).
  - CISA via DHS: individually unrelated; the DHS "super intelligence" remark is an unnamed source's theory.
- **CYB-INC-072 Chase update:** now "JPMorgan: software bug in own on-premise hardware, not cyber, other banks' delays via transactions with Chase" (11/17). Baseline had "a technical issue, not cyber-related" with no restoration at 16:00 ET 11/16.
- New FORWARD row 2026-11-24: Optimizely follow-up (CYB-INC-073): a listed US bank, lender or the credit bureau stating card fraud or filing a breach notice or 8-K citing Optimizely.
- Status line rewritten (prior 11/16 Chase-led status replaced).
- No row fired; no prediction or gate moved; no retraction.

**CROSS-DOMAIN / CALIBRATION:**
- Bank consequence of Optimizely is REGINALD's and GIBBS's; SaaS supply-chain read is VULCAN's (P2). Large-bank operations and deposits GIBBS's; Zelle and rails LIQUID's.
- Conviction: H on the bank's and vendor's own statements and KEV listings; M on on-chain tracing of Arkéa funds; L on any systemic reading.
- Uncertain about: whether any bank or CU names N-central or ScreenConnect as its route in the CYP-03 window; Arkéa's provider and client base; whether named PHP2Shell victims surface; whether Finzly's leaked keys were live; whether Abrigo lost data.
- Tension: DEWEY's WALTER-watch alternative remains the R0 test (12/17).
- "Diverge from market by: not measured this session."
- Arkéa: 11/16 Les Echos (11/14) named the provider on unnamed sources (asset-management compliance software), unread and unconfirmed (in WAITING FOR; present at baseline? the WAITING FOR row was not in the diff, so unchanged).

**FORWARD (~3 weeks):**
- 2026-11-18: Row 9 equity persistence: PANW at or below $289.24 AND 10.0 points behind HACK on 2 consecutive closes; HENRY grades after 16:15 ET (WQ-635 A).
- 2026-11-19 (weekly): wave 7-day clock; cluster watch; Abrigo; ConnectWise; TruStage; Able2Shell/MSP one look incl. Insight CU notice (CYP-03); N-able HF2-bypass outcome.
- 2026-11-20: R1 flip test (Kiteworks leg rides it); no named organisation by 11/20 moves R1 to MECHANICAL (Log4Shell shape).
- 2026-11-23: Arkéa weekly look.
- 2026-11-24: Optimizely follow-up (new).
- ~2026-11-27 (estimated): Microsoft 365 post-incident report.
- 2026-12-01: GMO compensation totals after the 11/30 window.
- 12/17: DEWEY R0 test (calibration section).

**NEXUS-NAMED (verbatim, "To" cells of SENDING rows):**
- New: "NEXUS / PROME / REGINALD / GIBBS / LIQUID / VULCAN / WALTER / TERRY | 11/17: Optimizely Web Experimentation compromise CONFIRMED at the vendor's status page (CYB-INC-073) ..." with mechanism "Bank consequence read (REGINALD, GIBBS); SaaS supply-chain read (VULCAN); synthesis".
- New: "NEXUS / PROME / WALTER | 11/17: six US outages in six days graded ..." with mechanism "Synthesis: do not read the list as one campaign".
- Unchanged NEXUS-addressed rows: 11/16 Chase outage; 11/16 16:00 ET re-check; 11/14 Microsoft 365; 11/14 DOJ Binance freeze; 11/14 CISA KEV Check Point; 11/13 Check Point Research; 11/12 N-able / ConnectWise; 11/06 Capcom/Kiteworks/GMO/Shinkin; composite 24/40 row.

---

## 5. ZHAO (China macro to US transmission)

**HEADER:** As of 2026-11-17 12:10 ET (by `date`) | STATUS commit: "NONE (folded in the same commit as STATUS)"; that commit is fe85e90b1a (2026-11-17 12:11:05 -0500). Pin check PASS (OK-SAME-COMMIT). Status 🟠 29/60 ELEVATED (unchanged since 11/06). Prior as-of 2026-11-16 14:15 ET.

**VIEW:**
- 11/17: China's answer to the new US chip rule is a conditional threat, not a measure (MOFCOM 11/17 own text, countermeasures only if the US persists, none named).
- China's October home demand still contracting (credit, retail, FAI, property); exports and PPI carry the headline.
- Higher Fed odds do not make China a forced Treasury seller; currency-defence channel shut; Japan near USD/JPY 160 is the live Asian official-seller risk (SAM's call).

**MOVED SINCE 3db8291eff (only the Status and As-of lines changed):**
- New ★ 11/17 status item: MOFCOM 11/17 own text: countermeasures 「若美方一意孤行」, none named; levers in place: the 11/9 two-month pauses of a 24% tariff and two US blacklists, and the Ga/Ge/Sb ban to the US that "re-arms 11/28 unless renewed"; KB-278, 279.
- As-of: C8 wake, PROME prome-19, WALTER card SIG-W-20261117-007. China's reply to "the 11/16 US remote-access chip rule" read at MOFCOM's own page (KB-278); "three unlogged 11/9 Chinese two-month suspensions added (KB-279)"; "China confirmed the Shenzhen trilateral 11/16, not the bilateral (KB-280)"; "The US rule publishes 11/19, the meeting day (FR 2026-23529, KB-283)". "No score, band or prediction moved (KB-281)."
- No fire, grade, kill or retraction. Score 29/60 unchanged.
- Unchanged figures carried from baseline (11/16 status): new RMB loans about −RMB 100B (October); retail +0.4% YoY; FAI −8.1% YTD (−7.2% Jan–Sep); property investment −21.6% YTD; V5b rescore (now 3) owed. 11/11: ORACLE +25bp 85.5, +50bp or more 11.8; yuan 6.6727 → 6.6612; DXY 102.2 → 102.9; HK peg 7.8455; China 10Y 1.61% YELLOW; PBOC overnight 1.25% since 11/02.

**CROSS-DOMAIN / CALIBRATION:**
- Names SAM (Japan USD/JPY 160 call), ORACLE (priced Fed odds), VULCAN/WATT/HAWK (11/10 clocks re-suspended to ~1/10; "⚠️ 2026年第58号 ≠ 2025年第58号"), LIQUID (HK peg, Q3 China+Korea selling −$21.6B through Aug), HENRY (PBOC fix +0.68% weaker than market, 20-fix mean 11/06; CGB 1.59% 11/06; China-US 10Y gap ~327bp), HANS, MIDAS.
- Open ask to VULCAN: "Does your entity/supply map resolve 0.1% materials content, or only ownership?" (next VULCAN session). VULCAN's brief does not answer it.
- Uncertain about: (1) whether the 1/9 to 1/11/2027 cluster gets a third extension or a deal; (2) cause of the Aug residuals; (3) whether HK carry pressure forces HKMA in; (4) leg F's hit rate in a real regime change.
- Conviction: China UST selling MEDIUM, DECELERATING (6-month net −$71.5B); where the money went LOW; RED BENIGN-DRIFT counter-frame "Strengthened again".
- Internal tension to check: Status says "Trump–Xi bilateral Shenzhen Thu 11/19 registered", while the As-of line says "China confirmed the Shenzhen trilateral 11/16, not the bilateral (KB-280)".
- Staleness flags in unchanged sections: FORWARD table header "refreshed 2026-11-06"; "Sat Nov 7" SAFE row not marked done; "UNPRICED BINARY ... Re-checked 11/2; next 11/9" (date past); LIQUID WAITING FOR row dated 9/19; NEXT DECISION POINT cites "11/30 Nov PMI (ZHA-23)" which is not in the FORWARD table.

**FORWARD (~3 weeks):**
- Wed 11/18: September TIC (Treasury-confirmed), ZHA-22; China Q3 net ≤ −$50B ⇒ LIQUID+PROME; Aug −$12.25B China / +$19.85B Belgium residual revision?
- Thu 11/19: Trump–Xi meeting, Shenzhen (instrument-only grading, KB-273); US rule FR 2026-23529 publishes the same day.
- ~Fri 11/20: NFRA Q3 bank indicators (modeled), LPR; rural NPL ≥2.9% ⇒ VX-6.15 watch.
- Fri 11/27: MOFCOM 公告2024年第46号 clause 2 ends; first uncovered day 11/28 (Ga/Ge/Sb/superhard + graphite).
- 11/30: November PMI (ZHA-23).
- 12/31: ZHA-26 PBOC overnight rate cut from 1.25%, 12%.
- 2027-01-09 to 01-11: clock cluster.

**NEXUS-NAMED (verbatim):**
- "★ **11/17 — for NEXUS: China's answer to the new US chip rule is a conditional threat, not a measure** (MOFCOM 11/17, own text: countermeasures 「若美方一意孤行」, none named; levers in place: the 11/9 two-month pauses of a 24% tariff and two US blacklists, and the Ga/Ge/Sb ban to the US that re-arms 11/28 unless renewed; KB-278, 279)." (new)
- "★ **11/16 — for NEXUS: China's October home demand is still contracting** (NBS primary 11/16; PBOC 11/13 via secondaries) ..." (baseline)
- "★ **11/11 — for NEXUS: the December Fed hike now priced (ORACLE: +25bp 85.5, +50bp or more 11.8) does NOT make China a forced Treasury seller.**" (baseline)
- "**★ 11/06 — FOR NEXUS: the two-clock story is now one clock, and the domestic read weakened.**" (baseline)
- "**★ 10/29 — FOR NEXUS: the PBOC's currency posture has fully reversed, and the desk's gauges could not see it until today.**" (baseline)
- "**🟠 10/9 — FOR NEXUS: a pre-registered tripwire fired and I applied it AGAINST my own read.**" (baseline)

---

## CROSS-BRIEF (max 10 lines)

1. **BIS remote-access rule, FR 2026-23529:** VULCAN "interim final rule ... effective 11/19" (KB-446, read at the primary); ZHAO "the 11/16 US remote-access chip rule ... publishes 11/19" (KB-283). Same date 11/19, different verbs (effective vs publishes) and ZHAO dates the rule 11/16; check at the Federal Register which is which.
2. **China's countermeasure:** VULCAN "China's countermeasure threat names no measure (ZHAO)" (KB-449); ZHAO "conditional threat, not a measure" (KB-278). Agree.
3. **China mineral/clock dates:** VULCAN "Graphite added to China's 11/27 clock is ZHAO's"; ZHAO 公告2024年第46号 clause 2 ends Fri 11/27, Ga/Ge/Sb ban "re-arms 11/28 unless renewed". Agree (11/27 last covered day, 11/28 first uncovered). Both carry the 2027-01-10 MOFCOM 公告2026年第58号 suspension end.
4. **Nvidia China exposure:** VULCAN gives China by HQ 9.5% of Q3 revenue (11/17 8-K) and earlier China-HQ 8.2% of Q2 FY27; ZHAO carries no Nvidia figure. No conflict.
5. **11/25 cluster:** CARL BEA October PCE/income Wed 11/25 08:30 ET (CRL-32 leg 1); ISHM BEA Q3 second estimate, durables October advance, Deere Q4 11/25; VULCAN ~11/25 Treasury 10-day ask (VULCAN's own count). Same day, separate instruments.
6. **Fed December:** CARL FOMC Dec 8–9 (V12 un-fire count), hike cost to card APR; ZHAO cites ORACLE 11/11 +25bp 85.5, +50bp or more 11.8. Different measures, no conflict.
7. **Import and goods prices:** CARL BLS import prices October +1.05%, ex-fuel +0.80% (via FRED) and core goods CPI +0.16%; ISHM S&P output prices "steepest since September 2022" and ISM prices 75.2 from 77.9 (routed to CARL). Different series; CARL's brief does not cite ISHM's survey prices.
8. **Routes visible in one brief only:** ISHM → VULCAN computer imports (+150.96% y/y September) and CYPHER → VULCAN P2 Optimizely SaaS supply-chain read: neither appears in VULCAN's 11/17 brief. ZHAO's open ask to VULCAN (0.1% materials content) is also unanswered in VULCAN's brief.
9. **Micron FQ1 (~12/16, INFERRED):** VULCAN lists HENRY, CARL as consumers; CARL's brief does not list it.
10. **Disagreement inside one brief:** ZHAO Status "Trump–Xi bilateral Shenzhen Thu 11/19 registered" vs ZHAO As-of "China confirmed the Shenzhen trilateral 11/16, not the bilateral (KB-280)".
