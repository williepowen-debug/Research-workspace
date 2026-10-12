# WATT — L654: PJM capacity advisory and FERC IRAS grade

**Observed October 12, 2026.** Power tape through **10:35 EPT**; board fetched about 10:42 ET; FERC issuance query 10:45 ET; order text read by 10:49 ET. This is a morning observation. October 12's full-day outcome remains pending.

FERC rejected the proposed IRAS/BYONC framework on October 9. **WATT-10 is a MISS**. The broader forecast that large loads bear most assigned costs (WATT-08) stays OPEN, with confidence reduced from the latest **~70% to ~50%** under its registered failure branch. Only the large-load definition and registry were accepted. The order removes the proposed IRAS tariff obligation; it does not remove existing power expenses or establish an amount passed to households.

## Owner grades

| Referent | Grade on its registered test | Consequence |
|---|---|---|
| L654 | Morning read completed; full-day outcome PENDING | Recheck after October 12; advisories also cover October 13–14 |
| P1 RED | No new observed fire October 9–12 through 10:35 EPT | P1 stays 5 from October 7; morning quiet does not earn early de-escalation |
| P1 de-escalation | NOT YET DUE: seven clear calendar days October 8–14 end 23:59 October 14 | Earliest execution October 15, conditional on no EEA-class posting or new PJM DOE order; recheck pending request |
| KILL_MEMO C1/C2/C3 | NOT-FIRED on available evidence | No EEA2+; no verified new order plus named curtailment; no high-peak conjunction |
| WATT-10 | **MISS**, substantive rejection October 9, graded October 12 | Archived original forecast and criteria; notify VULCAN/HENRY/CARL |
| WATT-08 | OPEN, **~50% Door B**, June 30, 2027 unchanged | Broader majority-cost assignment unresolved; registry acceptance is not cost allocation |
| WATT-09 | OPEN; verified response deadline **November 16**, outer November 30 unchanged | Qualifying section 205 filing may suspend that respondent's response duty |
| WATT-12 | Already HIT on October 7, graded October 9 | No second grade or new prediction from this advisory |
| P2 / P3 / P4 | Auction trigger FIRED / queue trigger NOT-FIRED / spark trigger NOT-FIRED | Scores remain **5 / 4 / 2**; historical fired-count stays **2 of 4**, P1 + P2 |

Composite **16/20**, P1/P2/P3/P4 **5/5/4/2**. No trade proposed or executed.

## PJM: operators are mitigating tight capacity

The [October 12 advisory #105546](https://emergencyprocedures.pjm.com/ep/pages/viewposting.jsf?id=105546) was posted October 8. [#105549](https://emergencyprocedures.pjm.com/ep/pages/viewposting.jsf?id=105549) covers October 13; [#105551](https://emergencyprocedures.pjm.com/ep/pages/viewposting.jsf?id=105551) covers October 14. [Maintenance recall #105552](https://emergencyprocedures.pjm.com/ep/pages/viewposting.jsf?id=105552) recalls all active generator maintenance tickets RTO-wide: end by **October 14 noon EPT**, or become forced outages. These actions do not meet an EEA-class posting bar.

**Issuance caveat:** notice #105553 at October 11 20:48 said a section 202(c) order had been obtained, but ended at 20:49. Replacement [#105554](https://emergencyprocedures.pjm.com/ep/pages/viewposting.jsf?id=105554) says **requested**. The [DOE 2026 index](https://www.energy.gov/ceser/2026-doe-202c-orders) showed no new PJM order after 202-26-45 at this read. Do not carry the superseded wording, count a fifth emergency episode, or infer generators ran. A request can precede publication: issuance remains a live recheck. The de-escalation is neither earned nor reset on a request alone.

| EPT tape date | Rows observed | Observed max $/MWh | Intervals ≥$1,000 |
|---|---:|---:|---:|
| October 9 | 283 | 316.17 | 0 |
| October 10 | 287 | 295.19 | 0 |
| October 11 | 288 | 624.66 at 07:55; two intervals ≥$500 | 0 |
| October 12 **through 10:35** | 127 | 52.90 at 08:00; latest 21.77 | 0 |

Source: PJM DM2, pnode 1, **unverified 5-minute operational data, not settlement**. Query returned 985 of 985 total rows. October 9 has five missing intervals; October 10 has one. Observed maxima cannot certify the missing intervals. Published EIA-930 latest load was **87,837 MW at 13Z**, **95.6%** of the prior 24-hour peak **91,870 MW**. Publication lags current time; a cache hit within one hour is indistinguishable from a fresh pull in the shared client.

Same-execution-day outage forecasts: **70,793 MW October 9 → 70,749 October 10 → 68,045 October 11 → 62,592 October 12**. Latest split: **46,499 planned + 5,759 maintenance + 10,334 forced MW**; total down **8,201 MW** from October 9. These are daily forecast snapshots, not live dispatch availability. The decline cannot be causally assigned to recall alone; planned plus maintenance still totals **52,258 MW**. No structural reserve-margin erosion finding follows from this evidence alone.

P4's boot spread is **+$37.23/MWh**, HR 7: $59.20 on-peak mean October 6–11 (n=1,142) minus 7 × NG=F $3.139 dated October 12; HR 8 gives +$34.09. **Gas is intraday, not an established settlement**, and October 7's $117.44 daily mean is an outlier against the $52.50 window median. No widening/compression inference against the clean September baseline. The stale ICE proxy spread was refused for its 12-day vintage mismatch.

## FERC: the proposed cost and curtailment package failed

[197 FERC ¶61,019, ER26-3515-000, accession 20261009-3055](https://elibrary.ferc.gov/eLibrary/docinfo?accession_Number=20261009-3055), paragraphs 2 and 13–15, accepts only the large-load definition and registry effective October 12, with a compliance filing within 30 days of October 9. It rejects the integrated IRAS/BYONC package, new-capacity designation requirement and exclusion of unsupplied loads from the capacity-auction demand curve. Paragraph 77 cites retail-jurisdiction problems; paragraphs 94–95 insufficient support for discriminatory treatment; paragraphs 103–105 insufficient support for fixed capacity accreditation. Paragraph 111 permits a revised section 205 filing.

**Economic inference:** the proposed IRAS-specific burden is removed, weakening Door B and increasing the relative risk of consumer pass-through. **No dollar of actual socialization is established. Physical electricity expense, existing PPAs, state tariffs and other compliance costs remain.** Companion reliability backstop ER26-3380 is not graded here. Definition/registry acceptance supplies information, not generation or a demand reduction. Allocation paths are alternatives, not additive shocks.

The valid FERC issuance query recovered **six hits: the known five notices plus the October 9 order**. This positive control matters: invalid undated requests returned server errors; an invalid date-field trial returned zero and was discarded. Final query uses `filed_date` with ISO dates, `classTypes`, and `groupBy: NONE`. Query/result and order PDF/text are saved. October 9's 10:01 ET no-order observation is superseded by the later issuance; it was a time-bounded observation, not a permanent claim.

[196 FERC ¶61,129, accession 20260814-3059](https://elibrary.ferc.gov/eLibrary/docinfo?accession_Number=20260814-3059), paragraphs 8–10, granted all three EL26-67 abeyance motions August 14: **responses November 16, answers December 16**. A qualifying section 205 filing by November 16 suspends that respondent's response obligation pending further Commission directive. [September 21 rehearing dismissal](https://elibrary.ferc.gov/eLibrary/docinfo?accession_Number=20260921-3020) does not answer WATT-09's substantive reform test. IRAS is a separate section 205 filing informed by the show-cause context; its rejection does not establish fulfilment of all four directed areas or suspend every respondent's duty.

## Boot, inbox and follow-up

Repository root: `/home/willi/Research-workspace`. Explicitly read root CLAUDE.md, AGENTS.md, USER.md, WATT CLAUDE.md/boot sequence, COMPLETION_SPEC and Runtime mechanics. Runtime: **OpenAI Codex**, root task `/root`; exact model/session UUID **UNKNOWN**. Verified shell/files/web/Git; no verified fleet-wide session discovery or cross-runtime notification transport. No agent spawned. Will's direct assignment is the owner authority.

Startup pull deferred under root Git protocol because other desks have uncommitted work. Initial sandbox boot rc2 (DNS); network retry rc1 (outlier and trade staleness), all five fetch legs succeeded. Corrections check rc0, no named outstanding correction. TRADE refreshed. Sources and workbook use their observation dates; historical predictions retain original criteria.

Four inbox items integrated at KB-WATT-143. AEOLUS's n=5 mild heating-demand composite remains weather background, not peak-load or no-emergency evidence; its cold near-cutoff example and early-winter exceptions travel. Oracle's ~4× trucked-gas claim remains one unread Bloomberg relay. No primary multi-GW Lordstown cancellation is established. SEC 7(A) withholding does not prove an issuer investigation. The storm packet is not proof of a PJM generation outage. Three WALTER consumption receipts recorded.

**Next owned checks:** after October 12's window, board/tape/DOE; October 14 noon recall and advisory close; first boot on/after October 15 for the complete de-escalation test; next weekly boot by October 19. PROME owns L654/L200 and related calendar updates. Consumer packets convey the grades without editing another desk's records. No operator ruling requested. Notification and recipient consumption remain unverified until recipients acknowledge the artifact version.
