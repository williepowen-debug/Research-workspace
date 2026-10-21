# WATT — SCRATCH (next-session pickup)

> **⚠️ STANDING OPERATIONAL CONSTRAINTS — re-homed here 2026-09-02 because they lived only in rotated session notes and a hot/cold split nearly retired them. These are constraints, not history.**
> **PJM DM2 rate limit:** non-member tier = **6 calls/min**. `power_watch.py` spends **1 per run** (boot spends 2 — LMP + on-peak window). **Never loop the instrument.** *2026-09-06 spend: 10 over ~30 min — 3 boot runs × 2, plus 4 deliberate pulls (9/3–9/5 tape, clean + stress spark windows, the 8/10–8/23 retention probe). Spaced, never bursted.*
> **DM2 verified hourly (`rt_hrl_lmps`) is BATCH-published with a VARIABLE ~1–4 day lag** — weekend days queue and land together. ***Measure the frontier at use time; never assume a fixed lag in either direction*** (L-34). The 5-min feed fails **LOUD** (0 rows); **`solar_gen`/`wind_gen` fail SILENT** (a full 24 rows of `0.0`) — **never infer absence semantics from a sibling feed** (L-37).
> **An unfiltered `rt_hrl_lmps` query + a row cap = silent truncation, not an error.** Always pass `pnode_id`.
> **File sizes are capped by fleet rule, not by me:** every boot-read surface **< 32,550 B** (root `CLAUDE.md` §Data Hygiene). This file and `STATUS.md` are both boot-read. **Check before writing, not after.**


---

## CURRENT PICKUP — 2026-10-20T22:56:04-04:00; outward news/data sweep

**State:** P1/P2/P3/P4=5/5/4/2,16/20unchanged. LatestPJMOctober20through22:45:273prints,$30.82latest,max315.14,0observedRED;21:15missing,dayunfinished. October22grade pending, no earlyde-escalation. October20newsreport:`reports/2026-10-20_NEWS_SWEEP.md`; precedingrecord/inboxsweep:`reports/2026-10-20_WATT_SWEEP.md` remainshistory/currentobligationreference.

**New evidence applied:** KB165–172. IMMoriginalSept25filing tracks4,016.9MWcancelled/delayedprojects,42%offorecastgrowth; scenario3,055MWshortfall not officialPJMrevision, noEDCprojectdata and noindependentIIRaudit. P3score4fundingdiscriminatorheld, forwardrealizationconfidenceweaker. Google890MWnewfirst2028(notexisting2700MW);Amazon190MWnewwithin690MWtotal,2030–32. IssuerannouncementsnotdeliveredMW. RBPaccepted/suspendedFeb28,2027subjectproceedings,October22MCconsultationprimary. GeneratororderER24-2045further60daycompliance/Cycle3effectiveness, notloadrule. EIAOctoberforecastprimaryupgrade, no newforecastrelease.

**Clock correction:** next2029/30BRA **December2026**, notmid2027, exactday/latestcalendarneedverification. October21FERCAD26-8conference10am–2:40pmEDT isnotaruling;October22MC9am-noonconsultationnotoutcome. October29RBPrefileplan/October21motionanswerclocksecondaryleadsnotpromotedwithoutprimarydocuments.

**Next:** existingOctober22grade completesOct20–21tape/board/DOE; same-dayMCpublicmaterialcanbereadatexistingtouch. L650metered/DR,L546float,AEOLUSinterchangeOct23;weekly<=Oct27;wake-listOct31;IRAS30daycompliance~Nov8unadjusted;EL26-67Nov16responses/Dec16answerswith205proviso;WATT09outerNov30;B1Nov10–11Beijingclosedunscored;NERCDec31;wintergateHELDKB076. Noautomaticmonitorpromise.

**Retained source walls:** activegenerationqueue/transitionremainderunknown(168.6GWcycleonly,old250GW/1.56xhistorical);hedgeshares/privatefirmgridrightsunknown;Amazonrebuttalretained;Appalachianbasis/NG=Fsettlementroll;6.5GWgap/ERCOTpairedstrips/Aug13–16sparkcauseopen. Sept17EEA2/C1historicalcorrectionstands(priorKB121priceoverlap,norawreplay);Oct15PJMstatementclosesOct13–14backupuseunknown,nolaternegative. No newpredictiongrade,trade,threshold,channel,spendorresearchmonitor.

**Persistence:** priorpickupandaffectedprose preservedbyte-exact `archive/2026-10-20_before-news/`,SHA256manifest. STATUS/VX/FLOW/THESIS/TRADEupdated;finalNEXUSfoldpinsexactSTATUScommit. Checks/publication/delivery receipts belonginnewsreport. Prior9inboxitemsfiledandR1receiptedinprecedingsweep;initialnewinboxenumerationempty. Nativecross-fleetpresence/notification/consumptionUNKNOWN;no inferredDARK/spawns. RuntimeCodex/OpenAI/exactmodelUNKNOWN,sameWill-launchedsession01a15b41-3b2c-71f1-b0b1-7fcaba915bd9. Foreigndirtyworkexcludespull/staging;exactownedpathsandself-authoredpackets only. NoWilldecision.
