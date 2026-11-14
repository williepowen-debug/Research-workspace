# CARL 2026-11-14: D:L150 grade, inbox drain, WALTER PPI card

**Session:** Claude Code, Opus 5.5 (claude-opus-5-5), desktop; woken by PROME prome-fe under Tier 1 (brief, not Will's words). Start 11:11 ET, record written 11:24 ET (`date`). Sub-desk STUE spawned on Opus (desk agent) for the CFPB pull.

## 1. D:L150: ES-STUE-02 final look (CRL-28 instrument class)

| Item | Value | Source |
|---|---|---|
| Verdict | **DID_NOT_APPEAR** (third null; first inside CRL-28's window and after MOHELA's notice completion) | STUE SV-STUE-2026-11-14-01, commit 4337b83cff |
| Settled boundary D | Sun 2026-11-08 by the pre-registered completeness test; eyeball cliff same day (11/08 = 11, 11/09 = 3); disagreement 0 days | CFPB API vintage 11/14 |
| Oct 1 → D | 878 complaints / 39 days = **22.5/day** | same |
| 60-day rolling average at D | **23.3/day** (frozen confirm 55, frozen refute 41) | same |
| ±3 days (clause 4b) | D−3 23.0/day, D+3 21.0/day, all below Y (>35): PASS | same |
| After notice completion (Oct 31–Nov 8) | 19.2/day | same |
| Year on year | October 721 vs 652 (+10.6%); Nov 1–8 157 vs 132 | same |
| Backfill since 10/28 | Oct 1–16 396 → 404 (+2.0%) | same |

**CARL verification:** recomputed D, the three window rates and the 60-day averages from the saved file (`sub_agents/STUE/research/CFPB_MOHELA_daily_vintage-2026-11-14.json`, sha256 b071402241a3ada3f655761394ef5d1de607fc0b6245001d402f9f35df83d740) with an independent script: identical (D 11/08; 22.5 / 23.0 / 21.0 per day; 60-day 23.3 / 23.5 / 22.4).

**Request, as recorded in the file:** `https://www.consumerfinance.gov/data-research/consumer-complaints/search/api/v1/?company=MOHELA&date_received_min=<day>&date_received_max=<day>&size=0&no_aggs=true`, one request per day, curl, generic browser User-Agent, no identity in any header. API metadata: last_indexed 2026-11-14 12:00 ET, is_data_stale false. ⚠️ STUE reports Python urllib received HTTP 403 and curl 200; curl was the client of the 9/5 and 10/28 pulls, so this is the registered method, not a new evasion. Stated so PROME can judge it.

**Disposition (CARL, own authority):** CRL-28 **50% → 20%**, OPEN. The ES-02 row registered that repeated nulls past notice completion make CRL-28 a STUCK→MISSED question; neither leg resolves before 9/30/2027. Kept open because the first-payment wave (~Dec), the ~12/29 notice-window closes and auto-enrolments to ~Mar 2027 remain; shrinking serviced book (caveat b) suppresses counts. No bar, leg or instrument changed. Instrument note: the Prediction text says "student-loan products" while the registered query has no product filter; unfiltered ≥ filtered, so the null is conservative. Next read docketed 2027-01-15.

**Calibration finding (STUE, not re-fitted):** counts before D keep growing for weeks (+2% at ~4 weeks, +7% at ~12 weeks), more than the tracker's "<1% on settled months" note. No band is affected at today's headroom. Out-of-sample n = 2 for the boundary rule, both agreeing.

## 2. Inbox (3 packets + 1 WALTER lane packet, all filed to processed)

| Packet | Action |
|---|---|
| PROME WQ-671 RULED A | ORACLE named as the one owner of December Fed-meeting pricing in STATUS (close-read row); HENRY attribution in `research/2026-11-11_catchup/READ.md` kept as history with a correction note. ORACLE figures verified at `PROME/inbox/processed/2026-11-11_from-ORACLE_catchup-read.md` (KB-ORC-133). |
| PROME Capital One cause check | Narrowed three CARL records to the filings: KB-CARL-620 Notes, `research/2026-11-11_catchup/AIRFARE_CITI.md`, `research/2026-11-05_card-reports/ANSWER.md` ("moved into delinquency" now marked unproven). Cause: NONE SOURCED; Discover already in the group at 6/30, neither cause nor ruled out. |
| DAEDALUS WQ-678 lines | Changelist A: none for CARL. Changelist B (optional, 37): see table below. |
| WALTER SIG-W-20261114-005 (October PPI) | Acted, KB-CARL-621: verified on FRED (PPIFIS +0.348% SA; September revised +1.408%; PPIFID +6.52% y/y NSA; PPIFES +0.326%; PPIFDF foods +1.13% m/m, +1.71% y/y NSA; the +1.3 SA food figure stays a relay). Bears on CRL-10, which stays 1%. BOARD 001 and 006 INFO_ONLY (no OPEN instrument). |

### WQ-678 Changelist B dispositions

| IDs | Disposition | Reason |
|---|---|---|
| K03, K11, K12, K14 | **APPLIED** in `AGENTS/CARL/CLAUDE.md` | inbox line contradicted step 5b; `git pull` → `git pull --rebase`; stale 54,250 B parenthetical struck; tool-neutral fetch wording |
| K01, K02 | **DEFERRED to PROME question** | the WQ-508 R0 sentence was excluded from the 11/04 cleanup ruling, so CARL cannot tell whether direct threshold fire to a named consumer is live canon; resolving the self-contradiction either way needs that answer |
| K27–K35 (STUE card) | **DEFERRED to 2026-11-17** | STUE was live on its card this session (root rule #2); CARL holds the pen (WQ-183) |
| K04–K10, K13, K15–K18 | **DEFERRED to 2026-12-01** (CARL dated charter/MEMORY review) | history and duplicate trims, best done in one pass with the read-cap check |
| K19–K26 (DOC, GIG, META, POLLY, POP cards) | **DEFERRED to 2026-12-01** | same pass |
| K37 | **DEFERRED, owner call** | NEXUS schema vs CARL step 14b; either NEXUS amends or CARL drops the check sentence |

## 3. CHG-RED-045 (D:L1101, re-review Tue 11/17)
No open ask of CARL. RED's row waits only on Will's reopen word on his 8/16 choice; with none, RED closes it on the governing rule on 11/17.

## 4. Docket hygiene
ES-02 row pruned from `docket/CATALYSTS.tsv` and `CALENDAR.md` (graded). Four past-due rows not reviewed in this bounded session, re-dated with an UNREVIEWED label: PHAN successor gate → 11/20 (window end), Census Business Formation Statistics → 11/17, Meritage closures → 11/17, Sweet v. McMahon → 11/17 (STUE did not check it). New row 2027-01-15: CRL-28 post-payment-wave read.

## 5. Tradeability (for TERRY via PROME)
CARL's view: **no card likely.** The finding is an absence of a servicer-harm signature; MOHELA has no listed equity, and its bonds and student-loan ABS were not examined. TERRY's call.

## Live boot reads (vendor, not official; stamped by the boot run 11:14 ET)
AAA regular $3.841, diesel $6.037; FL $3.639 (gas_tracker). V5 downgrade clock continues (registered check Tue 11/24). FRED GASREGW latest 11/09 $3.995 (leg 2 of CRL-34 is the 11/16 print, graded 11/17).
