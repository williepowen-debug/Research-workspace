# Digest reader C: BRENT, WATT, CORAL, MARCO, AEOLUS, HOMER (whole briefs) + FERT, CREED, CRUISE (STATUS diffs)

Written 2026-11-25 16:11 ET. Baseline dc3ec2b130 (2026-11-25 00:37 ET); HEAD read b346e54387 (16:07:52 ET). Read-only, no web. All six briefs and all three STATUS files moved since the baseline. Owner artifacts beyond the briefs were read only where noted. Cite owners, not this digest.

Pin check (`python3 scripts/brief_pin_check.py`, repo root): `BRIEF-PIN 0 OK: 31 brief(s) ... OK-PINNED 21, OK-SAME-COMMIT 8, STALE-PIN 1, UNPINNED 1`. These desks: BRENT OK-SAME-COMMIT 641e20924 | WATT OK-PINNED 806f5cbae8 | CORAL OK-PINNED 150b89b947 | MARCO OK-SAME-COMMIT 229a2e2ac | AEOLUS OK-SAME-COMMIT 39fcde10a | HOMER OK-PINNED 842b154462. (STALE-PIN = LIQUID, UNPINNED = RED; not in this set. FERT, CREED, CRUISE keep no brief.) A pass proves the pin, not the content.

---

## 1. BRENT
**HEADER.** As of 11/25, 10:23 EST boot (DOCKET L1224). MIXED-VINTAGE, SCOPED-PARTIAL: only the Status line, the 11/25 SENDING row, the EIA wait row and NEXT DECISION POINT were re-verified. Folded with STATUS in 641e20924 (10:43 ET). Thesis v5.13.

**VIEW.** (1) Energy WAIT kept, nothing armed, no probability or threshold changed. (2) Brent January up 2.3% with a steeper front and no confirmed barrel lost; part of it is January expiry-week mechanics (last trade 11/30). (3) Crude loose, products tight split stays; the escalation has not moved a registered oil gate.

**MOVED SINCE THE BASELINE.**
- Brent January BZF27 93.46 at 10:12 ET 11/25, +2.3% on the 91.40 settle (settle secondhand). Front: M1-M2 +3.40 against +2.63 (11/24 window); M1-M3 about +6.07 against +4.81 [EST vendor proxy, not settles]. Prior brief: 90.15 at 23:29 ET 11/24, "tape shrugged".
- Contract-month trap: vendor `BZ=F` has been FEBRUARY since 11/18 (90.06). Quotes near 89 are February, not a fall. WALTER card 008's "-2.4%" was February measured over the January settle.
- Ras Tanura: four drones intercepted (coalition); refinery hit CLAIM ONLY, no Aramco statement (STATUS). Hodeidah struck again; the Houthi condition on Saudi Red Sea ports is met a second time; no Saudi Red Sea port hit found.
- EIA week 11/20 [CONF EIA, own capture 10:30:58 EST]: utilization 97.5% (+1.8 in STATUS), crude +1.1M (+1.109M), Cushing 25.613M (prior 26.147M), distillate 105.616M (prior 104.901M), crude exports 3.27 mb/d (-1.22). STATUS adds SPR 273.465M, gasoline supplied 8,714 against 8,726 a year ago.
- GRADE, BRT-31 week seven: -0.2190%, NON-QUALIFYING. MET unreachable; NOT MET also unreachable; window-end label NO-VERDICT (or NO-VERDICT-CONTAMINATED only if a listed tax cut took effect by 11/27) at the 12/02 print. Price leg +18.98%, counter 1 of 3. The standing 40% stays on the open row until the print.
- BRT-34 third print: 105,616, 10,616 above 95,000, not below.
- GRADES on the letter (C10): BRT-23 CONFIRMED, BRT-28 FAILED; BRT-22 held for Will.
- BRT-33: valid 11, none under +3.50 (unchanged; the 11/25 and 11/27 windows are not read yet).
- Retail gasoline $3.642 [EIA 11/23] sent to CARL. WQ-735: two scripts switched; GIE API refuses the honest client name, so EU-STORAGE is unavailable.
- Dropped from the Status line, not retracted: January diesel crack (HO-CL) 71.64 at the 11/24 window (79.73 on 11/19); Yanbu 2.5 to 3.1 mb/d, about 40% of Saudi crude exports (still in the 11/24 SENDING row); COT open-interest share 7.3697%.

**CROSS-DOMAIN and CALIBRATION.** Sends 11/25: TERRY (tradeability packet, no card), WALTER (name the contract month), CARL (gasoline volume flat on a year ago), HENRY (distillate building at record-high runs). Conviction moderate, unchanged. Tensions named by BRENT: EIA January spare of 0.01 mb/d against Saudi-stated 10.563 production (room 1.2 to 1.3), not adjudicated by the IEA report; OPEC demand +0.18 against IEA -2.7 and EIA -2.0; crowd price for another US land strike against flat oil legs (ORACLE). CME and ICE settles unavailable from this box. No quantified market edge claimed.

**FORWARD.** BRT-33 graded from one vendor capture at the 11/30 session (NO unless a window is under +3.50; 11/27 holiday hours unread). 11/29 OPEC+ January letter. 11/30 COT #16 (as-of 11/24; a short fall of 19,472 or more puts Leg A in the dead band) and BZF27 last trade. 12/02 EIA week 11/27 (BRT-31 label, BRT-34 fourth print). 12/11 IEA. 12/14 OPEC. Five combo reviews 11/30 and 12/02 (STATUS).

**NEXUS-NAMED (verbatim).** Only the 11/16 SENDING row names NEXUS as a recipient: "PROME / TERRY / OSPREY / FALCON / HAWK / HENRY / NEXUS | November 16: COT #14 (as-of 11/10) JOINT NOT-SPENT, 8th consecutive ...". Overtaken by COT #15. Nothing new to NEXUS on 11/25.

## 2. WATT
**HEADER.** Mixed-vintage, latest read 11:39:45 ET 11/25 (intraday equities). Pin 806f5cbae8 = STATUS HEAD. P1/P2/P3/P4 = 3/5/4/2, composite 14 of 20, unchanged.

**VIEW.** (1) The power and grid-equipment selloff is equity repricing, not a demand break, on the record as it stands. (2) The contracted record still grew at the last prints, but the newest hard prints are a month old. (3) PJM price tape from 11/14 11:00 ET is UNKNOWN (key refused since 11/16, WILL_QUEUE 695), not quiet.

**MOVED SINCE THE BASELINE.**
- KB225, 11/25: across 11/20, 11/24 and 11/25 (Wednesday intraday) GEV -17.6%, VRT -21.3%, NRG -16.3%, VST -12.9% against SPY -6.8%, SMH -23.1%, XLU -0.6%. AEP signed +15 GW in Q3, 84 GW contracted by 2031 (ESA and LOA only). Consultant CRA for PJM (LAS 11/02): about 11.5 GW of 2030 data-center demand unservable under the supply limit. No named November cancellation, utility forecast cut or queue-withdrawal wave found (bounded search; Dominion and Exelon figures secondary).
- KB226, 11/25: proposed Section 301 on transformers, switchgear and cable: ASSUMPTION-grade $0.1 to 0.3M per MW of IT load, 0.2 to 0.6% of all-in data-center cost; most lands in rate base (CARL). Not in force; import shares, Section 232 stacking and lead time unsized; VULCAN's exempt-list read PROVISIONAL.
- KB227: the 2024 No. 46 clause 2 clock (includes graphite) moved from 11/27/2026 to 1/27/2027 under MOFCOM 2026 No. 59; WATT holds no row. Replaces the baseline's "November 27 clock".
- PJM key refusal still live at 11:36 ET 11/25 (baseline read 11/19). WATT-13 cannot be graded 12/02 without it.
- No score, fire, kill or prediction grade. Five corrections receipted.
- STATUS only, not in the brief: EIA-930 demand 107,114 MW at 14Z 11/25 was 100% of the trailing window peak (the demand limb is met often in winter, KB206 and KB222); PJM West proxy for 11/25 $80.21 and Henry Hub $3.662; weekly coverage due 11/21 was MISSED (desk dark 11/19 to 11/25).

**CROSS-DOMAIN and CALIBRATION.** Sends to HENRY, VULCAN, TERRY, PROME, CARL, NEXUS; TERRY packet says no card. Counted once: PJM outage-driven fires are one root. Unknowns: SoftBank dropped equipment direction, active queue total, hedge shares, November 1 run cause. Market divergence unmeasured.

**FORWARD.** WATT-09 outer 11/30 | WATT-13 on or after 12/02 (blocked) | ERCOT Batch Zero 12/10, PUCT 12/17 | 12/09 to 12/15 capacity auction window, results 12/22 (WATT-14 cap clear 88%, WATT-15 45%) | PJM LAS 12/18 | WATT-16 12/18 | WATT-17 12/31 | Section 301 comments 1/05, hearing 1/25.

**NEXUS-NAMED (verbatim, the one new row).** "HENRY / VULCAN / TERRY / PROME / NEXUS | AI power demand, November 25 [KB225]: the November 20/24/25 selloff (GEV −17.6%, VRT −21.3%, NRG −16.3%, VST −12.9% vs SPY −6.8%, SMH −23.1%, XLU −0.6%; Wednesday intraday) is equity repricing; the contracted record still grew at the last prints ... No named November cancellation, utility forecast cut or queue-withdrawal wave found | Bounded search; newest hard prints a month old". Standing rows also name NEXUS: winter demand test ("A met demand limb on a winter morning is not a stress reading"), price limb "UNKNOWN, not quiet", equipment figure KB208, year-over-year tail KB186.

## 3. CORAL
**HEADER.** As of 2026-11-25 11:52 ET. Pin 150b89b947 = STATUS HEAD. Status ORANGE, unchanged.

**VIEW.** (1) Household and condo stress confirmed; bank-loss transmission NOT confirmed; no colour moves. (2) The federal declaration is confirmed but narrow: a permission, not money. (3) Florida stress stays localized; four of five tracked metros above 6.00 months of supply.

**MOVED SINCE THE BASELINE.**
- RESOLUTION: DR-4956-FL CONFIRMED (OpenFEMA 16:39Z 11/25; declared 11/24 on the 11/09 request). Household aid Brevard, Indian River, Martin, Okeechobee, Palm Beach, St. Lucie. Public assistance A to B only; Hardee public assistance only; no Hazard Mitigation; DeSoto and Highlands not designated. 0 registrations, 0 projects. Replaces "REPORTED, NOT CONFIRMED". (STATUS: public assistance in six counties, not St. Lucie.)
- Second request (Seminole, Volusia, Broward, Orange, Flagler, Putnam) pending, not denied. WALTER watches to 12/07.
- DeLand forecast 6.3 from 11/28 against the 6.33 record (5.84 observed, STATUS). Cocoa no fall to 12/02 (18.44, STATUS).
- NFIP still 1,157 (data 11/16): 623 zone X (insured homes only); 14 condo-association claims, 11 in Brevard, $0 paid (new). Southeast rain 11/25 heaviest in undeclared Broward and Miami-Dade; not yet a large event.
- MSI reading #16 (data 11/24): 4 of 5 above 6.00, Cape Coral 5.78 (was 5.74 at #15), re-fire fails, clock zero. STATUS: Tampa 7.09, Punta Gorda 6.05 (6.02 on 11/23), North Port 6.13, Lakeland 6.22. Next #17 by 12/03.
- Uninsured share remains a HYPOTHESIS. No gate, grade, kill or retraction.

**CROSS-DOMAIN and CALIBRATION.** Sends: HOMER (FHA 90-day to about 2/22/2027, HOMER's derived date), REGINALD (Seacoast trigger), WALTER, AEOLUS, CARL, PROME (GATES). TERRY no card. Conviction: mechanism HIGH, bank transmission LOW, timing MEDIUM (winter window). Counter-evidence carried: August statewide condo firming, Citizens drop mechanical, CREED zero-Florida CMBS names.

**FORWARD.** 11/28 DeLand | 11/30 second request and NFIP load (D:L1244) | 12/03 MSI #17 | declaration amendment watch to 12/07 | 12/11 NFIP authorization | 12/16 Florida Realtors November | 12/31 SIRS deadline | 1/1/2027 Citizens flood mandate | 1/4 Fannie 15% reserve test.

**NEXUS-NAMED (verbatim).** "NEXUS | Geography read: statewide firming vs SW/Central-FL MSI still above 6.00 in four of five metros, edging down — the stress is localized, not statewide | 🟠 | Synthesis should not treat FL as uniformly improving or uniformly breaking". Also 11/17: "TERRY (no card: stated in the research doc), HOMER, NEXUS" on the condo financing channel.

## 4. MARCO
**HEADER.** As of 2026-11-25 (session 42, drain-only, no clock; STATUS stamps 13:44 ET). Same commit as STATUS, 229a2e2ac1 (13:46 ET). Status ORANGE, thesis v3.2, position none.

**VIEW.** (1) No flood effect is measured: every MARCO print predates the 10/31 incident and its instruments do not reach the declared counties. (2) Canada channel strongest; Florida overseas visitors holding. (3) Florida net migration sign under Amendment 3 not identified.

**MOVED SINCE THE BASELINE.**
- VECTOR FIRE: VX-2.06 construction-wage gap NORMAL to ELEVATED (revised September +2.21pp, October preliminary +2.05pp; three months at or above 2.0, per STATUS; margin 0.05pp; vector only).
- DR-4956-FL carried (declared 11/24, same six counties, second request pending). First flood-capable reads: MIA November and Florida Realtors November about 12/21, NTTO Florida November about January, BTS November about February. MIA, FLL and MCO all outside the declared list; November airport counts also carry the 11/13 FAA ground stop.
- Florida condo supply October 8.0 months, single-family 4.6 (CORAL's figure): first rise after the decline ended.
- Amendment 3 certification NOT CONFIRMED as of 11/25 (baseline said certification 11/17). Revenue triple re-based to CORAL's 7/10 vintage: -$4.93B, -$8.71B, -$11.83B.
- MAR-25 confidence cell 95% to 80% by WQ-112 (the 95% was written after the outcome). WQ-735: seven scripts switched. WQ-678 and WQ-712 charter lines HELD for Will's own word (arrived by agent message).
- Two October packet rows merged and compacted; no figure changed. No prediction graded.

**CROSS-DOMAIN and CALIBRATION.** Direction HIGH, timing MEDIUM, magnitude LOW. Standing: ID-01 identified, Canadian 2-year October -26.88%, BREACHED 12th month; MAR-11 confirmed. Tensions: MIA clean-tell (see staleness below); CBO2025 range withdrawn; documented-not-merged Florida migration with CORAL.

**FORWARD.** 11/28 DeLand and second request | 11/30 to 12/04 NTTO October, BTS August, LVCVA October, Banxico October, AZ-01, November jobs survey | 12/04 SDL-01 (MAR-29 90%) | 12/03 H-2A court reports | 12/17 to 12/21 state BLS November (VX-2.06), Florida Realtors, MIA reports, Amendment 3 certification.

**NEXUS-NAMED (verbatim).** "NEXUS | Channel-1 re-instrumentation is a **measurement** change, not a direction change — and the s32 `SDL-01` flip is one print, not a reversal | 🟡 | Avoids reading either as a thesis reversal".

## 5. AEOLUS
**HEADER.** Last writeback 2026-11-25 14:42 ET (PROME due-row wake, owed #23). Same commit as STATUS, 39fcde10ab. Composite 15 of 30, fired 0 of 6; moved 1 since 11/19 (C5 4 to 3, already in the baseline period).

**VIEW.** (1) C6 Colorado (score 4) is the channel with a dated consequence; the Hoover capacity loss does not depend on a signature, the water split does. (2) West Coast tide records are real but damage was roads and waterfronts (NFIP or uninsured). (3) No score moved.

**MOVED SINCE THE BASELINE.** All tide values PRELIMINARY, ft MLLW.
- California 11/25: San Diego 8.654 and La Jolla 8.114 beat the 10/27 records by 0.131; LA ties 8.194; Orange County has no NOAA gauge. 11/25 PM observed: Arena Cove 9.216 record (beats 8.862 on 11/24 and NOAA's listed 8.93); Santa Barbara 8.209 record; Monterey on one sample; NOT records: San Francisco 8.213 (record 8.663), North Spit 9.814 (10.359), Crescent City 9.741 (10.663). 11/24 road closures US-101 (Marin, Humboldt), Webster Tube (KB-332 to 336).
- Forward view, unscored: new high at one or more of San Diego, La Jolla, Santa Barbara or Arena Cove on 12/23 to 12/25 about 60%; San Francisco about 20%.
- Florida: new storm under the same 11/23 watches, heaviest in undeclared Broward and Miami-Dade (2 to 3 in by 11 ET). DeLand forecast first 6.3 (Sat 11/28), then RAISED to 6.4 (valid 19:00 ET Sat as written '19:00 ET') against 6.33 record (KB-337, CORAL told, d9e9e20756).
- The baseline's waiting item (second CA tide read) is discharged; new waits: 11/28 DeLand, by 12/22 West Coast residual re-read.

**CROSS-DOMAIN and CALIBRATION.** Routed CORAL, TERRY. Root notes: Rhine, Mississippi (shared with C2 drought), ENSO cluster (C1, C2, C3, C5-Panama, C6) and coastal are separate roots; C6 is one root with two legs. Predictions: AEO-17 NO-VERDICT by 1/20/27 otherwise; AEO-18 MWD vote 50%; AEO-19 Florida rain 75%; AEO-12 55%. Nothing is a trade; TERRY holds the WQ-704 and C5 handoffs.

**FORWARD.** 11/26 SA CEC final, Memphis forecast -5.1 ft | 11/27 Kaub 10th day | 11/28 DeLand | 11/30 hurricane season end (AEO-01, C1 kill resolves) | 12/02 C6 Orange window | 12/03 CAP board | 12/07 to 12/08 MWD vote | 12/10 WASDE, CPC ENSO, Nevada v. Burgum, Memphis -6.9 ft | 12/17 CPC seasonal | 12/21 Memphis -7.8 ft | 12/23 to 12/25 king tides.

**NEXUS-NAMED (verbatim).** Section heading "WHAT NEXUS/PROME SHOULD KNOW": "Root independence: C5-Rhine (European basin) · C5-Mississippi (US-interior drought, shared with C2) · ENSO cluster (C1/C2/C3/C5-Panama/C6) · coastal (wind + sea level) are separate roots." and "The Hoover consequence does not depend on the signature; the water split does. Count them as one C6 root, two legs."

## 6. HOMER
**HEADER.** As of 2026-11-25 15:30 ET. Pin 842b154462 = STATUS HEAD. The most heavily rewritten brief of the set (77 lines of diff; several closeouts 11:37 to 15:30 ET). Status RED held. Will decision required: none (STATUS).

**VIEW.** (1) Thesis paragraph ADOPTED 11/25 (Will): stress is building and converting at once, labelled by channel. Happening now: apartment lenders and bonds, FHA and mortgage-insured borrowers, builders. Early, not settled: bank-held apartment loans, nonbank servicers, residential construction jobs. Not showing yet: a national nominal price decline. (2) Older FHA distress is converting; fresh FHA distress is not shown accelerating. (3) The October multifamily highs are about one loan each, not breadth; no evidence held of broad bank losses on home mortgages (not proof of absence).

**MOVED SINCE THE BASELINE.**
- No leg killed: 0 of 5; kill tests, scores and RED unchanged. Handle 21 of 25. D13 closed 11/24; A1 reads 0 of 2 and PROME answered 11/25 (UNGRADED with halves reported if the first half is not met; at most 1 of 2 by 2027-02-20).
- PMMS 7.21% [11/25], -7bp (was 7.28 [11/19]). Spread about 230bp on the Tue 11/24 10Y of 4.91% (was 221). A2 71bp from its kill.
- HUD FHA September (issuer, new): Q3 foreclosure starts 31,396 (+36% YoY, +3% QoQ); in foreclosure 54,973 (+51%); claims 2,114 (+57%); NEW 90+ 158,492, -18.4% YoY; serious delinquency 6.56% SA, -24bp QoQ; loss severity 28.5 to 35.4%. HUD's own October-2025 rule change lifts the serious rate.
- New defaults rotating out of FHA (ICE September, YoY): all -2%, FHA -14%, GSE +17%, VA +14%. Fannie single-family serious 0.63% October (+9bp YoY), primary-MI 1.38% (+22bp YoY).
- Negative equity (ICE September): 1.1M underwater (2%, largest Q3 share since 2018); 362K also three or more payments behind against 208K (+74%). Vintages since 2022 underwater: VA 19%, FHA 13%, conventional 1.2%. Cape Coral 11.2%, Lakeland 8.9%, Tampa 6.1%. ICE HPI +1.0% YoY October (Aug +1.44), condos -1.2%.
- CORRECTION (Trepp, multifamily): special servicing 9.22% October, +69bp, is wholly one loan (Blackjack $517.7M, about 69bp); without it about 8.5%, flat. Delinquency 8.09%, +5bp: one loan (Cove at Tiburon $210M, about 28bp) exceeds the rise; ex-Cove flows about -3bp: flat, NOT improving. All DERIVED on Trepp's August $75.48B base.
- RETRACTIONS and withdrawals: "maturity defaults are now the channel" (book-wide read) WITHDRAWN; "converting, not curing" WITHDRAWN; "past its peak" narrowed; Fannie single-family provision withdrawn as default evidence (mainly rates; NEXUS correction f4d16dca2c). The multifamily Fannie provision $446M against $259M stands. "No MF balance held" was wrong.
- Blackjack was NOT in Trepp's October delinquency count (Trepp's largest new loan was $384M), so November is two-sided: Cove reverting about -28bp, Blackjack entering about +69bp. HOM-05 (<8.09%) stays 55%, frozen.
- Fitch 11/16: nine affirmed, no rating cut (Fitch via Will 11/25), outlook NEGATIVE on Pennymac BB, Planet B, Freedom BB-; Provident Positive to Stable; sector leverage 3.4x (2.5x YE25); 60+ delinquency 2.5% (2.4%); Freedom $500M 10% note expected 11/19 beside $540M due January 2027 (corrected figure); class A fired a second time. UWM 5.3x Fitch leverage now only in STATUS.
- GSE multifamily October: Fannie 0.65% (+3bp, at the Orange line, not over it), Freddie 0.62% (+4bp, 12bp above Red).
- United Fidelity: about 89% of the FDIC Q3 multifamily past-due rise (1.404 to 1.742%); ex-bank about 1.41 to 1.43%. Broad bank-multifamily read weaker.
- DR-4956-FL confirmed; FHA pause on all seven counties (Hardee included, HUD ML 2025-12) to 2027-02-21/22, then 90 days servicing time, not a ban; 13.4% of Florida housing units, not an FHA share.
- Case-Shiller September +2.1%, unchanged; 16th real decline. Census new-home October 701K (+14.2%, not significant); September REVISED 676K to 614K; average price -12.1% YoY (about half or more mix). Q3 residential investment -3.4% second estimate (first -3.3%). MBA purchase -16% YoY week 11/20 (was -18% wk 11/13). HMI 25 unchanged.
- Own-odds record: 1 of 4, Brier 0.358; HOM-04 was called at 30%.
- Dropped rows (archived, not retracted): loanDepot, October rates row, Freddie September, S2, EO policy.

**CROSS-DOMAIN and CALIBRATION.** Sends to CARL, REGINALD, HENRY, LABOR, CREED, CORAL; WAITING: Trepp November, ICE First Look October (404 on 11/25), ATTOM Q3 (404), ICE Monitor. Tensions: Trepp securitized-Freddie 0.80% (August) and K-Series 0.96% (October) unresolved against issuer 0.64% and 0.62%, issuer governs. Conviction: direction HIGH, timing and level MEDIUM.

**FORWARD.** ICE First Look October 11/25 to 11/30 (C1; HOM-07, HOM-08) | Apartment List November (HOM-06) | FMHPI October about 11/30 | Trepp November 12/01 to 12/05 (HOM-05) | PMMS 12/03 | builders and HMI December | Case-Shiller October 12/29 | next formal grade 2027-02-20. Projections unscored: RED holds at 2027-02-20 about 90%.

**NEXUS-NAMED.** None (text search: NEXUS appears only in the title and two archive filenames). NEXUS packets to HOMER at 15:20, 15:28, 16:01 and 16:07 ET are partly unread on the brief.

---

## 7. STATUS-only desks (no brief)

**FERT (13f4d0e5f3, 13:45 ET).** GATE-FERT-G5 FIRED, first fire in 15 graded prints: retail MAP $1,004 [DTN, week Nov 16 to 20, first-party], $4 over the strictly-above-$1,000 line, +$9, eleventh straight rise, first above since September 2022; DAP $948. FERT-13 HIT (55%, Brier 0.203). Tier YELLOW to ORANGE on retail level only; score held 3; watch-only, no capital path; a post-fire hold read is set for 12/02 but the letter has no hold clause. FERT's own limit: a lagging retail series crossed a round line; international DAP $803.1/mt (Oct) flat, Tampa sulfur -$90; not evidence of food pass-through (ERS 11/24 T2 NOT FIRING; 2027 food-at-home 1.0 to 1.9% with no input cited). Also: anhydrous $1,011 (+$14); Mosaic selling Faustina ammonia plant to CF for about $600M; Section 301 China proposal lists all Chapter 31 lines at up to 10% (not in force). Packets to CARL, HENRY, TERRY (no card), PROME. Next: 12/02, 12/03, 12/10, 12/16, 12/23.

**CREED (18e3f606a9, 13:28 ET).** CREED-T-03 GRADED NOT FIRED at the FDIC Q3 report: large-bank nonfarm-nonresidential past-due 2.48% to 2.27% (third fall) decides; reserve-coverage leg 172.70% to 169.26% met for the first time; S3 held 2, score 28 of 45 unchanged; broad CRE-to-bank transmission not confirmed. Not called healing: foreclosed nonfarm-nonres property rose in every size tier (+15.9% all banks; $10B to $250B $915.3M to $1,085.6M, about three quarters OZK), large-bank charge-offs about 0.30% annualized. The 3.40 base identified as the FDIC's over-$250B non-owner series (2.781 in Q3), correcting KB-024/026; the 8/27 "episodic" claim was a retrieval error. Multifamily past-due jump about 90% one private bank (United Fidelity). Forward, unscored: 15% T-03 fires on the Q4 QBP (late February 2027), 60% regional foreclosed CRE rises a third quarter. DR-4956 verified, exposure screen not run.

**CRUISE (0f14cd146b, 13:42 ET).** Aged-inbox drain, no score moved at the latest close: desk 9 of 20. Carnival touched ORANGE on one close, 11/20 ($26.59, -21.77%, a market day), back to YELLOW 11/24 ($28.40, -16.45%; 4.44% above the ORANGE line). Norwegian revolver test: reversal window closed 11/23 with no 8-K; NOT SPRUNG stands, provisional to the 10-K. NCLH $17.10, -31.65% from peak. Elliott 17.686M shares at 9/30 (+20.4%). HY OAS 343bp [11/17] is named as a B-tier context read that moves no score.

---

## 8. Cross-brief section (10 lines)
1. DR-4956-FL: CORAL, HOMER, MARCO (and REGINALD's brief) carry the same six household-aid counties and Hardee public assistance only; AEOLUS's brief still carries "no federal declaration" in its South Florida line (see 9).
2. DeLand crest: CORAL 6.3, AEOLUS 6.4 (14:42 ET, later), AEOLUS's own body 6.3 twice; record 6.33. The later AEOLUS figure is ABOVE the record; CORAL's "0.03 ft under" and MARCO's "vs record" predate it.
3. Seacoast: CORAL's brief says REGINALD "grades"; REGINALD's STATUS says the check is MET on DR-4956 (KB ML-REG-326, exposure map, no grade).
4. Trepp Blackjack and Cove: HOMER's one-loan correction is the owner read; CREED's STATUS names Blackjack only as a special-servicing item (KB-119). No conflict on the fact; CREED does not restate HOMER's 8.5% ex-Blackjack.
5. United Fidelity: HOMER about 89%, CREED and REGINALD about 90% of the FDIC Q3 multifamily past-due rise. Same root, rounding only; counts once. It is the same one-bank explanation across three desks.
6. Mortgage spread: HOMER about 230bp (PMMS 7.21 on 10Y 4.91 [11/24]); BOND 229bp (10Y 4.92 [11/23]), inside its 180 to 230 band. One survey, two 10Y dates; HOMER reads a +9bp widening as possibly timing. Level is at BOND's band edge.
7. Gulf and Red Sea: FALCON and BRENT both hold the Hodeidah strike; Ras Tanura is on BRENT's brief but no Ras Tanura text was found in FALCON's STATUS or brief (FALCON security grade owed or not yet written). BRENT says no barrel lost. Contract-month trap: any desk quoting near 89 is February.
8. Section 301 (proposed 11/25, not in force): WATT (equipment), FERT (Chapter 31 all lines up to 10%), VULCAN, ZHAO. One legal root; four cost reads, all PROPOSED; do not count as four signals.
9. Retail gasoline $3.642 [EIA 11/23]: BRENT and CARL agree. Amendment 3: CORAL and MARCO agree at 61.98%, certification NOT CONFIRMED.
10. Disagreement worth NEXUS's eye: HOMER labels bank-held apartment loans "early, not settled" while CREED and REGINALD's reading says one bank explains about 90%. Same datum, different label; the kill-side reading is CREED's "broad transmission not confirmed".

## 9. Staleness against own STATUS or against later peers
- **AEOLUS brief (content):** C4 paragraph says "no federal declaration" and DeLand "6.3 on 11/28, KB-331" beside its own waiting line "RAISED to 6.4 (KB-337)". AEOLUS STATUS carries 6.4; STATUS text does not mention DR-4956 (search found no hit). Correct by next writeback; the brief's own header is right.
- **CORAL brief:** DeLand 6.3 is overtaken by AEOLUS's 6.4 (packet d9e9e20756 14:42 ET, after CORAL's 11:52 write). MSI, NFIP, DR rows match STATUS. Stale internal rows, unrelated to this session: NEXT DECISION POINT dated "late Oct to 11/15"; WATCH table rows 11/15 to 11/19 already past, still naming Cape Coral 5.84 and MSI #14; VIEW fiscal line and "DR-4955" lines superseded; SENDING row to MARCO carries months supply 7.7/4.3 against STATUS 8.0 (Oct); Conviction "bank-transmission-LOW until Q3" though the Q3 frame is FINAL.
- **MARCO brief:** CALIBRATION and WAITING still say CORAL calls MIA the clean tell; CORAL STATUS and brief both show it WITHDRAWN (COR-20261029-04). Otherwise matches STATUS.
- **HOMER brief:** ICE First Look row carries foreclosure starts "40.0K, -2.9%"; STATUS carries 40,400 (Monitor revised), -3%. One cross-desk send not on the brief: HOMER to PROME 15:34 ET (af6b272c3a, after the 15:30 pin): PennyMac's leverage is mostly hedge cash ($964M hedge losses, liquidity down $500M to $3.5B), not delinquency advances (+$52M in nine months); Freedom not sizable. This narrows the "nonbank servicer credit" mechanism toward rate risk. Figures are search excerpts, filing unopened.
- **WATT brief:** 11/25 rows match STATUS. FORWARD table rows 11/17 and 11/20 (Wagner, 202-26-40) are past, and STATUS says Wagner's renewal is not yet read. STATUS-only facts listed in section 2. "NEXT" omits the missed 11/21 weekly coverage.
- **BRENT brief:** matches STATUS on every 11/25 figure. Re-verified scope is narrow by its own statement; older rows still carry 11/04 to 11/18 vintages (for example BRT-33 calibration 20% as first registered). M1-M3 +6.07 is near the +6.3 level BRENT named as what would move oil (only with flat prices rising); BRENT did not call it a trigger.
