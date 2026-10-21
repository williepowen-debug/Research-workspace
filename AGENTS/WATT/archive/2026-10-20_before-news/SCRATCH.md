# WATT — SCRATCH (next-session pickup)

> **⚠️ STANDING OPERATIONAL CONSTRAINTS — re-homed here 2026-09-02 because they lived only in rotated session notes and a hot/cold split nearly retired them. These are constraints, not history.**
> **PJM DM2 rate limit:** non-member tier = **6 calls/min**. `power_watch.py` spends **1 per run** (boot spends 2 — LMP + on-peak window). **Never loop the instrument.** *2026-09-06 spend: 10 over ~30 min — 3 boot runs × 2, plus 4 deliberate pulls (9/3–9/5 tape, clean + stress spark windows, the 8/10–8/23 retention probe). Spaced, never bursted.*
> **DM2 verified hourly (`rt_hrl_lmps`) is BATCH-published with a VARIABLE ~1–4 day lag** — weekend days queue and land together. ***Measure the frontier at use time; never assume a fixed lag in either direction*** (L-34). The 5-min feed fails **LOUD** (0 rows); **`solar_gen`/`wind_gen` fail SILENT** (a full 24 rows of `0.0`) — **never infer absence semantics from a sibling feed** (L-37).
> **An unfiltered `rt_hrl_lmps` query + a row cap = silent truncation, not an error.** Always pass `pnode_id`.
> **File sizes are capped by fleet rule, not by me:** every boot-read surface **< 32,550 B** (root `CLAUDE.md` §Data Hygiene). This file and `STATUS.md` are both boot-read. **Check before writing, not after.**


---

## CURRENT PICKUP — 2026-10-20T22:39:45-04:00; October 20sweep completed

**State:** P1/P2/P3/P4=5/5/4/2,16/20unchanged. TapeOct15–19completecalendarcoverage with2isolatedmissingOct15prints;Oct 20through22:20with1missing. No observedRED. DOE202-26-50expiredperterm/noextensionindexed;October 19CapacityAdvisorynotEEA. P1held untilOct22grade.

**Completed:** report `reports/2026-10-20_WATT_SWEEP.md`; KB156–164; correctedKB122/154andhistoricalqueueKB084/085; VX/FLOW/THESIS/TRADE/STATUSreconciled. COR-20261015-05applied(15.83%Oct 14HYG2032fund-evaluation, nottrade). Nineinboxfiles read/dispositioned; filemoves/receipt/checks/persistence reconciled in sweepreport. Priorpickupandotherreplacedrecords archivedbyte-exact `archive/2026-10-20_before-sweep/`,SHA256manifest. FinalNEXUSfold pinsfinalSTATUScommit.

**Discharged:** September 17EEA2primaryposting105532verified; historicalC1MET frompriorKB121price-runoverlap, rawreplayunavailable. PJMOct15explicitnegative closesOctober14large-loadbackup-useunknown; no negativeclaimafterOct15. October 22wakeis actuallyregistered atPROME DOCKETphysicalL717; no longer “rowrequested”. VULCANacknowledgeshedge/IRASandcalendarcorrections; otherconsumerreceiptsunknown.

**Next owner touch:** firstboot>=Oct 22 completeOct20–21tape/board/DOE and gradeunchangedde-escalationletter. IsolatedmissingOct15/20prints have non-REDneighbors; boardinvalidids cannot distinguishwithdrawn/unissued. Do not claimautomaticmonitoring or earlyall-clear. Currenttotalactivequeue/remainder atPJMneeded; old250 GW/1.56xhistorical,168.6GWcycle-onlynotreplacementtotal. P3=4demanddiscriminator unchanged.

**Other clocks:** L650metered-vs-DR,L546demandfloat,AEOLUSinterchangeOct23;nextweekly<=Oct 27(Oct 22eventearlier);L487wakelistOct31;IRAScompliancewithin30daysOct9(~Nov 8unadjusted, verifylegalclock);EL26-67responsesNov16/answersDec16withqualifying205proviso;WATT09outerNov30;B1closed/T1Nov10–11Beijing,positiveT2notestablished;NERCDec31;wintergateHELDKB076.

**Source walls:** CoreWeavehedgesharesunknown;Amazonprivateemails/recordingandsitefirmgridrightsnotinspected, rebuttalretained;Loughtonwithdrawalreported/rightsunknown;NG=Fsettlementroll/Appalachianbasisunknown;meteredDRfinalnotfound;6.5GWgap/ERCOTpairedforwardstrips/Aug 13–16sparkcauseopen. No newmonitor,trade,thresholdorpaid-feedapproval. KILL_MEMOC1historical“neverobserved”premiseobsolete, ruleunchanged; flaggedtoPROME.

**Runtime:** Codex/OpenAI, exactmodelUNKNOWN; session01a15b41-3b2c-71f1-b0b1-7fcaba915bd9, independentWill-launchedowner. Shell/networkapproved forcaptures; nofleetwideownerdiscovery/notificationchannelverified, presenceUNKNOWN. GitpullskippedforeignWALTERcachework; exactownedpathcommits only. Publication/consumptionreceipts belonginsweepreport. NoWilldecision.
