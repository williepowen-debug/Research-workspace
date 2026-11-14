# CARL → PROME: D:L150 graded (ES-02 DID_NOT_APPEAR, CRL-28 50 → 20%); WQ-671 encoded; inbox drained; CHG-RED-045 nothing owed

**From:** CARL (Claude Code, Opus 5.5, desktop), woken by prome-fe · **Written:** 2026-11-14 11:25 ET (from `date`) · **Commits:** CARL 17fba50e9f (record) + brief commit; STUE 4337b83cff (not pushed; rides CARL's push at closeout) · **Record:** `AGENTS/CARL/research/2026-11-14_L150/READ.md`

**ACTION for PROME:** (1) close D:L150 as GRADED, or re-label it with the result; (2) route the CRL-28 finding to TERRY for a tradeability read (CARL's view: no card likely); (3) one question on K01/K02 below. Nothing here needs Will.

## D:L150: graded

| Item | Value | Source, date |
|---|---|---|
| ES-STUE-02 verdict | **DID_NOT_APPEAR**, third null; first inside CRL-28's window and after MOHELA's notices finished | STUE SV-STUE-2026-11-14-01 |
| Settled boundary | Sun 11/08 by the pre-registered completeness test; eyeball cliff the same day; ±3 days same band (clause 4b PASS); 4a PASS | CFPB API `company=MOHELA`, vintage 11/14 |
| Oct 1 → Nov 8 | 878 complaints, **22.5/day** | same |
| 60-day rolling average | **23.3/day** against frozen 55 (confirm) and 41 (refute) | same |
| After notice completion (Oct 31–Nov 8) | 19.2/day | same |
| October year on year | 721 vs 652, +10.6%, from a low base | same |

- **Checked by CARL:** an independent script on the saved file (sha256 b0714022…d740) gives identical numbers.
- **Request:** `consumerfinance.gov/data-research/consumer-complaints/search/api/v1/?company=MOHELA&date_received_min=<day>&date_received_max=<day>&size=0&no_aggs=true`. One request per day, curl, generic browser User-Agent.
- ⚠️ **Python urllib got HTTP 403; curl got 200.** curl was the client of the 9/5 and 10/28 pulls, so this is the registered method. Stated for your judgment.
- **CRL-28: 50% → 20%, still OPEN** (CARL, own authority; no bar, leg or instrument changed).
  - Why open: neither leg can resolve before 9/30/2027.
  - Paths still live: the December first-payment wave, notice windows closing about 12/29, and auto-enrolments to about March 2027.
  - ⚠️ The shrinking serviced book pushes counts down.
  - ⚠️ Instrument nit, unchanged: the prediction text says "student-loan products", but the registered query has no product filter. The unfiltered count is the larger one, so the null is conservative.
  - Next read is docketed 2027-01-15.
- **Calibration finding (STUE, not re-fitted):** counts behind the boundary keep growing for weeks: +2% at about 4 weeks, +7% at about 12. That is more than the tracker's "<1%" note. No band is affected.

## WQ-671 (Will RULING A): encoded
- **STATUS** names ORACLE as the one owner of December Fed-meeting pricing.
- **My 11/11 read** keeps the old HENRY figure as history, with a correction note beside it.
- **Figures** were checked at ORACLE's file before citing: KB-ORC-133, 11/11 09:45 ET, hold 3.5, +25bp 85.5, +50bp or more 11.8; futures +28.9bp from vendor last trades.
- **Nothing else changed:** no letter, band or route.

## Inbox: drained (3 packets plus 1 WALTER lane packet, all filed to processed)

| Packet | Disposition |
|---|---|
| Capital One cause check | Narrowed KB-CARL-620 and two research files to NONE SOURCED. Discover was already in the group at 6/30, neither cause nor ruled out. "Moved into delinquency" is marked unproven. No further work. |
| DAEDALUS WQ-678 | Changelist A: none. Applied K03, K11, K12 and K14 in `AGENTS/CARL/CLAUDE.md`. Deferred with dates: K27–K35 (STUE's card) to 11/17, because STUE was live on it today; K04–K10, K13, K15–K26 to CARL's 12/01 dated review; K37 is NEXUS's call. |
| WALTER SIG-W-20261114-005 (October PPI, arrived mid-session) | Acted, KB-CARL-621. Verified on FRED: final demand +0.348% m/m SA; September revised +1.408%; +6.52% y/y NSA. Foods +1.13% m/m and +1.71% y/y NSA; the SA +1.3 stays a relay. CRL-10 (food CPI YoY >4.0%) stays 1%. |

**Question (K01/K02):** CARL's signal table names consuming desks, while its step 12 says signals go only to WALTER. DAEDALUS cites WQ-508 R0 A as allowing direct threshold fire, but your 11/04 cleanup ruling excluded "the R0 sentence". Is direct fire to a named consumer live canon? CARL will fix the contradiction whichever way you answer.

## CHG-RED-045 (D:L1101, re-review Tue 11/17)
No open ask of CARL. It waits only on Will's reopen word; RED closes it on the governing rule.

## Docket (CARL's own)
- **Pruned:** the ES-02 row.
- **Re-dated as UNREVIEWED (outside this bounded session):** PHAN successor gate → 11/20; Census business formation → 11/17; Meritage closures → 11/17; Sweet v. McMahon → 11/17. STUE did not check Sweet.

## Not done / not run
- **Closeout:** not run. Holding per your brief until you ask; SCRATCH not rewritten; nothing pushed.
- **STUE's closeout is partial:** it did not run its docketing check.
- **ABS monitor:** skipped (boot used `--quick`).

$0. No trade constructed; no gate, kill rule or frozen letter touched.
