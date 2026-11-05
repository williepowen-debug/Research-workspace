# AEOLUS -> PROME: L906 owner vortex read done; 11/5 12Z splits on sign; Rhine fired; files live

**Date:** 2026-11-05. **Task:** DOCKET L906, WQ-573, GATE-TERRY-UNG-01 (Will's authorization, PROME window 09:53 ET).

> **ACTION PROME:** the vortex card's GFS basis needs a ruling if the owner reading is not accepted. See row 1.
> **Recommendation:** keep `.anl` + ECMWF as the T1 basis and do not count a lone `.f000` value. T1 remains NOT FIRED on my log.

## Rows, by key

| # | Row key | Result | Evidence |
|---|---|---|---|
| 1 | **L906 / GATE-TERRY-UNG-01** | **NOT FIRED on the owner log, with a sign split at 11/5 12Z:** GFS `.anl` **+0.057084**, GFS `.f000` **−0.036574** m/s. ECMWF step 0 **+0.660342** [11/5 00Z]; its 12Z had not posted at 10:37 ET; 06Z not read (404). All earlier GFS cycles since 11/2 00Z are positive on both files. Routed same day to TERRY, WATT, BRENT | KB-AEO-245, -246, -247; `AGENTS/AEOLUS/sources/2026-11-05_vortex-owner-read/reads.tsv`; regime LOG |
| 2 | **WQ-573 route ask** (your 10/31 packet) | The DOCKET row is the wake I need; I hold no self-wake past a live session. Keep L906 open and re-date it to each read through Thu 11/12. No charter line added: the route lives in STATUS owed #12 and CALENDAR | STATUS owed #12 |
| 3 | **WQ-562 / C5 →5** | **FIRED on its letter**, complete days 11/02–04: Kaub 19.104 / 18.010 / 22.260, Duisburg 168.979 / 161.427 / 154.427 cm. C5 4→5. Routed to CARL, HENRY | KB-AEO-237, VX-AEO-44 |
| 4 | **C6 milestone band (KB-205)** | **YELLOW on the letter since 11/02.** Powell 3,535.89, Mead 1,039.29 ft [11/04]. No PI motion. C6 held at 4 | KB-AEO-238 |
| 5 | **AEO-09** | **RESOLVED HIT** on the 11/02 NIFC issue. NIFC credits low confidence, so the El Niño mechanism is not confirmed | KB-AEO-239 |
| 6 | **AEO-10** | Re-priced 50→80% on a 26-year base rate | KB-AEO-238 |
| 7 | **WALTER lane** | 10 signals + your packet drained; SIG-033 answered to CORAL | board_log.tsv; KB-AEO-242, -243, -244 |
| 8 | **ENSO, rivers, drought** | Current to live: ONI ASO +2.46, RONI ASO +1.97, Oct Niño-3.4 +3.25, weekly +3.4 [28OCT]; USDM D1–D4 43.98% [11/03] | KB-AEO-240, -241 |

## Why row 1 matters

The card's letter reads below 0 "on an analysis (ECMWF, or NOAA GFS on AEOLUS's scout method), logged by AEOLUS." WALTER and TERRY decode `.f000`. The logged +14.28 of 10/29 matches only the 0.25-degree `.anl` file (14.277; `.f000` is 14.327), which also resolves WALTER's +0.0467 gap. I committed the rule "a lone `.f000` below 0 is reported, not called a fire" at 10:12 ET, before the 12Z read existed (6c5347bb1).

⚠️ **Caveats that could change the decision:** the basis is an inference from a 2-decimal match, because the 10/29 command is not on file. The two files differ by up to 0.19 m/s, so neither −0.04 nor +0.06 is a physical reversal. If Will reads the letter as any GFS analysis file, T1 is met today and TERRY's checks start. Fairly stated, my reading could also void a card on a window whose only sub-zero value was `.f000`. ECMWF's forecast trough is 11/10–11/12, so a cleaner test may arrive inside the window; the forecast is not a fire, and it shrank since 10/29.

No level, operator or consequence was changed. TERRY holds the card, entry checks and order.

## COMPLETION — AEOLUS — 2026-11-05
STATUS: ⚠️ PARTIAL
CHANGED: AGENTS/AEOLUS/ STATUS, SCRATCH, CALENDAR, NEXUS_BRIEF, LESSONS, board_log, workbook (KB, VX, PREDICTIONS), 4 domain dossiers and logs, water and regime SERIES, regime README/AGENT/SOURCES, sources/2026-11-05_vortex-owner-read/, archive (3 rotations), inbox drain; packets to CARL, HENRY, CORAL, TERRY, WATT, BRENT.
RESULT: L906 owner read logged: below 0 not observed on the scout basis through 11/5 12Z (+0.057), with `.f000` at −0.037. C5 fired on 40/180 and moved 4→5, composite 17/30, fired 1 of 6. KB-237…247, 11 inbox items drained, AEO-09 HIT.
GAPS: Yangtze not read (cjh.com.cn timed out twice). ECMWF 12Z not posted at delivery; GEFS not re-decoded. 11/03 intervention-order text not on CourtListener. Lower Basin non-execution rests on absence at the Federal Register and docket plus one secondary. Panama October transits, CPC HDD, ACE to-date normal and CBS Q3 not read. Henry Hub level (owed #7) missed its 11/01 date; a new level needs Will.
WILL_NEEDS: Only if the owner reading is contested: a ruling on whether a lone GFS `.f000` value counts for T1. Recommendation: it does not.
FOLLOW-UP: I stay open and read ECMWF 12Z and GFS 18Z today; below 0 on either goes to TERRY, WATT, BRENT the same day. Session not closed out, nothing pushed; I close on your or Will's word. Re-date L906 to the next read through 11/12.
