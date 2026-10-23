# WATT — STATUS

**Record maintained:** 2026-10-23 01:04 EDT — D:L789 touch: L546 float graded DONE, AEOLUS interchange test run (KB177–180); RBP carried; inbox drained. Prior record 2026-10-22 09:54 EDT (D:L717/L650). **Observation cutoff:** PJM tape complete October 15–22 plus October 23 through 00:50 EPT; board and EIA-930 demand read 00:59 ET October 23; EIA-930 interchange September 14–21 pulled 01:0x ET October 23; DOE index and Inside Lines feed last read 08:34–08:36 ET October 22; board, DOE index and Inside Lines feed read 08:34–08:36 ET October 22; outage forecast executed October 22; gas quote 08:33 ET October 22 (NG=F $2.782). Auction result July 14; IRAS order October 9; RBP order September 29; generator order October 15. No fresh all-issuer guidance census. **P1/P2/P3/P4 = 3/5/4/2; composite 14/20 (was 16/20; P1 5→3 forced by the D:L717 letter).**
**Class:** market-agent, grid stress → wholesale price → industrial/data-center cost. **Maturity:** L4, ConfH (DAEDALUS September 5); spawnable by Will/PROME. Historical records and operating explanations: `archive/2026-10-20_before-sweep/` byte-exact snapshots and manifest; earlier status archives retained. Whole-read budget32,550B; measured by checks.

## CONVERGENCE MATRIX

| # | Channel | Score (1–5) | Local state | Independence | Key signal | Upgrade trigger |
|---|---|:---:|---|---|---|---|
|P1|Stress→price|3|De-escalated 5→3 October 22 on the registered letter (L717 MET): October 15–21 clear on every limb|Outage-season root; backup authority shares event root|202-26-50 lapsed October 16 unrenewed; no new PJM 202(c); only postings 105575 Capacity Advisory (not EEA-class) and 105576 local warning; 0 of 2,008 prints ≥$1,000, window max $471.98 October 16 [KB173/174]. October 22 complete day max $79.98, 0 ≥$500 despite the 71.5 GW outage forecast [KB179]|RED letter re-fire (≥$1,000 for 2+ consecutive 5-min AND posting or demand ≥97% of trailing peak) or EEA2+ → 5, as on October 7 |
|P2|Structural capacity cost|5|Three at-cap clears/two shortfalls remain historical fact; prospective shortfall disputed by IMM scenario. IRAS core rejected; RBP suspended to February 28, 2027, subject to proceedings|P2/P3 share demand-forecast root; not independent confirmations|28/29$325/MWday=100%owncap,6831MWshort [PJMJuly14]. IRAS rejectedOct9/readOct12, WATT10MISS, DoorB~50% [KB140/141]|December 2026 29/30 BRA below cap AND queues drain for thesis-kill; exact day and cost allocation unresolved |
|P3|Data-center demand|4 HELD|July 31 funding discriminator held; forward load-realization confidence weaker after IMM demand counterevidence. Current active-queue limb UNKNOWN|Shares P2 load forecast; site execution reports not independent demand proof|IMM tracks 4,016.9 MW cancelled/delayed projects, not an adopted PJM forecast [KB165]. Cycle 1 Phase I 168.6 GW is generation, not total active queue [KB159]. Nuclear uprates planned from 2028; not online [KB166/167]|ACTIVE queue>2x forecastpeak OR IPPload-growthguide RAISED. No evidence for5; do not replace total withcycle-only |
|P4|Gas→power|2|NOT-FIRED; positive power-window proxy, no direction inference|Shares P1 price root; gas basis remains unmeasured|Oct 15–19onpeak49.7217,n958; Oct 20NG=F2.970→HR7spark+28.93/HR8+25.96 [KB161]|Negative3+sessions on consistentbasis; proxy is not matched daily settlements |

**Composite 14/20** transparent arithmetic 3+5+4+2. The P1 move is the letter executing on a clear seven-day window, not a judgment that the shoulder-season fragility is gone: October 13 RED and the September 17 EEA2 remain historical fires. No deploy-posture change or security mispricing measurement.

## NEWS / NEW DATA — primary reads October 20 (KB165–172)

**Demand counterevidence:** The Market Monitor's September 25 filing identifies **4,016.9 MW cancelled OR delayed** as of September 21, about **42% of 9,481 MW forecast growth**, not total data-center load. Scenario 3 shortfall **3,055 MW** versus historical auction **6,831.3 MW** is a sensitivity, not PJM's revised forecast. IIR/public-data tracking; monitor lacks EDC project-level adjustments, and WATT did not independently verify projects. P3 stays4 on its registered funding discriminator, with weaker forward realization confidence. Generation-queue attrition is a different population.

**Supply response:** Google/Constellation October6: **890 MW new uprates**, first expected2028,20-yearPPA; separate **2,700 MW existing-fleet** agreement not new supply. Amazon/Constellation September30: **690 MW total includes190 MW new**, planned2030–32. Issuer announcements, no contracts/permits or deliveredMW inspected. Not immediate2026/27relief, not an adopted IRAS cost rule, and no nameplate subtraction from UCAPshortfall.

**Policy and clocks:** September29RBPorder accepts for filing but suspends to **February28,2027**, subject torefund/furtherproceedings. No September30procurementstart. PrimaryOctober22MCagenda9am-noon confirms consultation onsection205revisions. October29refile/October21motionanswerdates remain secondaryleads awaiting primarydocuments. **Next2029/30BRA is December2026 perPJM, not WATT's old~mid2027**; exactday/latestcalendarunverified. October21FERCAD26-8conference10am–2:40pmEDT is an agenda, not ruling. ER24-2045October15generatororder requires60daycompliance and laterCycle3effectiveness; not data-center ride-through law or immediatequeueclearance.

**Backdrop and current read:** EIAOctober6forecast/inputcutoffOct1primarychecked:2026US11hubmean$52/MWh,PJM+41%YoY;2027USmean$49. Forecasts, not spotprices; noOct13–14information incorporated. FreshPJMthrough22:45:$30.82latest,max$315.14,n273,0observedRED;unverified/partialday,21:15missing. Fullreport:`reports/2026-10-20_NEWS_SWEEP.md`. Priorhistoricalcorrections/sourcewalls below remainbinding.

## LIVE READS AND CORRECTIONS

**P1 (graded October 22, KB173/174):** complete October 15–21 tape n=2,008 of 2,016; zero ≥$1,000, zero ≥$500; daily max 268.62/471.98/387.92/295.18/380.98/315.14/257.81 dollars/MWh. Missing October 15 10:35, 22:20; October 20 21:15; October 21 12:05, 15:10, 15:20, 15:40, 22:00 — no two adjacent, so no hidden RED run. Board ids 105577–105640 invalid/unavailable (cannot distinguish unissued from withdrawn); Inside Lines feed newest operations update is the October 16 Capacity Advisory for October 19. Same-day outage forecasts 70.2 GW October 21, 71.5 GW October 22 (planned 48.4, maintenance 12.7, forced 10.4), 57.3–69.2 GW October 23–28: forecasts, not live availability. October 22 complete day n=285 of 288 (missing 09:40, 15:05, 15:15, none adjacent): max $79.98 at 07:30 EPT, 0 ≥$500 [KB179]. October 23 through 00:50 EPT: latest $29.03, max $39.93; demand 88.7% of 24h peak at 04Z; board one routine local warning (105478), 0 emergency-class. Captures: `sources/2026-10-22/`; report `reports/2026-10-22_DOCKET-L717-P1-retest-L650-grade.md`.

**DOE:** 202-26-50 lapsed per its October 13–16 term; order page last modified October 14 14:44, docket ends at PJM Exhibit A of October 14; DOE 2026 index newest order still 202-26-50 at 08:34 ET October 22. Bounded public-index negative. **PJM October 15 retrospective says large-load backup authority was not used to date**, covering October 13–14 [KB158]; no claim after October 15; para E reports still unavailable. PJM says ninth authorization in 2026.

**Historical September 17 correction:** posting105532 explicitly EEA2,14:00–22:00BGE/DOM/PEPCO [primary re-readOct20]. KB122 “no EEA2found” withdrawn; **historical C1 MET** from overlap with dated KB121consecutiveREDtimings17:05–17:10/18:20–20:05. Raw5-minreplay unavailable (retentionelapsed, originalcapture not located); confidence limit travels. No live emergency now, no namedbackup-use/loadshedding inferred. KILL_MEMO C1never-observed history obsolete; thresholds unchanged, correction flagged toPROME. WATT02horizonSept7 predates event; grades unchanged [KB160]. **Interchange test (AEOLUS 9/28 hand-back) run October 23 [KB177]:** on the 9/16–17 afternoons PJM imported from TVA (−404/−246 MW) and the south-5 group, exported to MISO (+3,034/+2,161 MW) but less than 9/15 (+4,343), net interchange +742/−34 MW. No export surge into the hotter neighbours: export pull NOT SUPPORTED as an incremental driver; outage-driven read stands. ⚠️ EIA-930 pair flows do not reconcile to total interchange (+3.2 to +6.2 GW gap per afternoon): directions and day-over-day changes only.

**P2:** cap/short evidence unchanged; **197FERC61,019Oct9** rejects integratedIRAS/BYONC, acceptsdefinition/registry effectiveOct12 with30daycompliance. Removes proposed tariff burden, not physical/contract costs; no observed cost socialization. EL26-67responseNov16,answersDec16; qualifyingsection205filing can suspend affectedrespondent duty. No comprehensive newFERCfiling census this sweep. WATT08~50%OPENJune30,2027;WATT09OPENouterNov30.

**P3:** 617PhaseIprojects/168.6GWgenerationnameplate vs811initialapplications/~220GWintake. Currenttransition remainder unmeasured: **current totalactivequeue and its ratio UNKNOWN**; old~250 GW/1.56x withdrawn from current use. 168.6/160.451=1.051x is cycle-only sensitivity on older2027forecast, not triad. Signed49GWunbuilt is separate; never add historical30GWremainder. **Generation attrition is not cancelled data-center demand.** FirstEIT3projects1660 MWstorage+455 MWgasuprate,plannedmid2029; acceptance≠online/firmcapacity [KB159]. Carried demand-side bases remain~32GWfirmcoincidentpeak vs~55GWutility-reportedaggregate, never netted/averaged; July 31demanddiscriminator supports4, not newguidanceraised.

**Execution leads:** Amazon reportedpower-readiness+earlypayment reinforces existingdelay/carrymechanism, no measuredstock/idleperiod/loss/capexcut. Amazon disputes companywideforecastabsence and describes routine staging. Privateemails/recording uninspected; WALTER publisherbodyverification reliedon. Loughton firmgridrights/removal/substitution unknown; withdrawalsecondary. PortsPike4.25GWcommittedIT/3.8optionIT/10.37requestedgridload/10.17grossgeneration are fourpopulations, not energizedrights/netload [KB162].

**P4:** October 15–19RTonpeak versus October 20gas is an explicit multi-daypower-window proxy, not matchedsettlements. No comparison to priorOctober9–14stresswindow as a widening/compression series. Gas settlement/roll and Appalachianbasis remain unknown. Retail backdropJulyindustrial9.77c/kWh/residential18.31, not freshretailpass-through. National AugustFedall-utilitiesutilization71.3% is not PJMregionalreserve/headroom; electric-only70.3924% attributed toWALTER, not reproduced [KB163].

**CoreWeave correction:** October 14HYG2032YTW15.83%, replacing~14.5%relay; evaluations, nottrades/executablerefinancing. KB154historyannotated; KB156/R1receipt carrycorrection. NoWATTscoredependedonrelay. Hedged/floatingpower shares **UNKNOWN**, no “materialtail”tilt; priorKB047inference remains withdrawn [KB152]. Conditional~Decunhedgedcostmark is NOT a datedcatalyst until hedgepremise established.

**B1 battery:** closed/unscored, outsidecomposite. MOFCOM70primary suspension throughNov10 stillfound; officialtargetedsearch and ZHAOOct20ownerrelay found no positiveT2trigger withincoverage. Not exhaustiveinstrumentcensus; silence≠positive. T1Nov10–11Beijing; positivePRCofficialtermination/58implementingmaterial needed forT2. Magnitudeunknown; no300Wh/kgsparesstationarystorage claim [KB164].

## EXIT / INVALIDATION — standing rule and current state

|Channel|Standing rule|Current state|FIRED?|
|---|---|---|---|
|P1|EEA2+ OR LMP>=1000 for 2+ consecutive 5-min AND (posting OR demand>=97% trailing peak)|No fire October 14–22 (complete tape) or October 23 through 00:50; last fire October 13. Score de-escalated 5→3 October 22|NOT-FIRED at this read; historical fire on 5 days: 9/2, 9/16, 9/17, 10/7, 10/13 |
|P2|BRAatcap AND reliabilityshort|Threeatcap/twoshort, July 14basis|FIRED |
|P3|ACTIVEgenerationqueue>2xforecastsummerpeak|Currentactive-total UNKNOWN; old250 GW/1.56xhistorical; currentcycle168.6GWnotwholequeue|UNKNOWN limb; no newgrade/upgrade |
|P4|Negative spark3+sessions, consistentbasis|Positive+28.93windowproxy; no matcheddailysettlementseries|NOT-FIRED onavailableevidence |

**Current firing channels:1(P2); historical fire evidence on2of4(P1/P2)**. Earlier “2of4” was historical-plus-current, not2currentfires. P3unknown is notbenign. Current C1/C2/C3 not established; historicalSept17C1MET as above. Thesis-kill remains29/30BRAwellbelowcap AND queuesdrain. Shoulder-seasonstress confirmedpartialFL15, not measuredreserve-marginerosion.

## OPEN / WAKE SET

|Next touch|Date / owner|Reason|
|---|---|---|
| FERC reliability conference | Oct21,10:00–14:40EDT | AD26-8 agenda; not pending-case ruling; next existing-source touch, no automatic monitor |
| RBP stakeholder consultation | Held Oct 22; CARRIED to Nov 5 (next Special MC per the Oct 15 agenda) or PJM's section 205 filing, whichever first | Outcome still unread: pjm.com returned HTTP 403 to the agenda and MC page at 01:0x ET Oct 23 (it served on Oct 20); not cheap this touch. Not an approved outcome |
| Next2029/30BRA | December2026, exactdaytoverify | Corrects old~mid2027; registered thesis test, no threshold change |
|P1 de-escalation re-test, L717|DONE October 22 — MET, P1 5→3 executed|Re-escalation stays on the RED/EEA2 letter; registered wake discharged, no running monitor |
|Currentactivegenerationqueue/remainder|NextP3primarytouch,WATT|Withdrawoldratio; do notmanufacturetotalfromdifferentdates/populations |
|Metered vs DR July record, L650|GRADED October 22 (one day early) — DR-verified figure NOT PUBLISHED|DM2 RTO hourly 162,186 MW HB17 still is_verified=False; record = preliminary unrestricted 168,158 only; one figure with AEOLUS KB-AEO-206 [KB175]. Residual verified leg at next P1 primary touch, no new wake |
|L546 demand float; AEOLUS interchange|DONE Oct 23 (D:L789)|L546: power_watch rounds demand % to printed 1 dp before compare, 5/5 edge tests [KB178]. Interchange: export pull not supported [KB177]; packet to AEOLUS |
|IRASregistrycompliance/refile|Within30daysOct9;~Nov 8unadjustedarithmetic|No verifiedfilingdatehere; checkgoverningdeadline/businessdayrule beforedatedlegalclaim |
|EL26-67response/answers|Nov 16/Dec 16,WATT|Qualifying205suspensionproviso;WATT09outerNov30unchanged |
|Wake-listreviewL487|Oct 31,WATT (confirmed Oct 23)|Landed16terms;16termlistnot14title; noautomaticmonitorclaim |
|B1T1|Nov 10–11Beijing|Officialinstrumentonly; T2notestablishedOct20 |
|Weeklycoverage,WQ295|Last done Oct 20; next <=Oct 27 (confirmed Oct 23, not done at the L789 touch)|Priceonlyeventsneedtape; priorOct19cadenceone-daylate |
|ERCOTBatchZero|Dec 10|Energizationpausefilingwindow; nonewWATTgrade |
|NERCride-through|ByDec31|Compliancecostunsized, standardsprocess |
|WinterP1|MidJan–Feb 2027,gateHELD|KB076basis, peak-based/sign-agnostic; never “noEEAbecauseElNiño” |

Other retainedopenwork:6.5GWhistoricalgap viaoutages;CoreWeavehedgeshares;Loughtonfirmrights;ERCOTCal27power/gaspairedstrips(chartread≠settle);Aug 13–16sparkcause;Appalachianbasis/NG=Fsettlementroll;Oracle/WeEnergies,Hut8,TSMC-AZ,EIA923heat-rate(lowerurgency). No newsourcesevidence warranting closure. HistoricalSept17EEAquestion and October 14backup-useunknown discharged as above.

## BOTTOM LINE

P1 stays 3 (composite 14/20): October 22 ran its whole day with a $79.98 top price and no emergency, even with about 71.5 GW of generation forecast offline, and the overnight October 23 read is quiet. That is not an all-clear: a renewed price spike with an emergency posting would take P1 straight back to 5. The September 16–17 interchange test finds no export surge into hotter neighbours, so those emergencies stay read as outage-driven. The forward scarcity case still carries the Market Monitor's 4.0 GW of delayed or cancelled data-center projects; the next 2029/30 capacity auction is December 2026, exact day unverified. No trade or Will decision.
