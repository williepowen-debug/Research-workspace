# SAM — Recurring Releases Reference

**Purpose:** Canonical source-of-truth for *when* recurring Japan-macro and cross-market events publish, so KOYOMI (and SAM) can verify a date by lookup instead of a web search or a guess. This file holds **schedules and cadence rules only** — no analysis, no live data, no event interpretation.

**Maintained by:** SAM (KOYOMI may propose additions via escalation). **Read by:** KOYOMI at boot (date-verification source for `CATALYSTS.tsv` rows).

**How to use:** When a `CATALYSTS.tsv` row's date can't be corroborated from STATUS/THESIS/TIMELINE, check the cadence rule here first. If the cadence resolves it, use that. If still ambiguous, confirm at the linked official source, then (optionally) record the confirmed date below.

---

## Cadence rules (derive the date from these)

| Event | Cadence | Notes |
|-------|---------|-------|
| **CFTC JPY COT** | Every **Friday** ~15:30 ET; data as-of prior **Tuesday** | Weekly. The lag is the key gotcha — Friday's release reflects Tuesday positioning. |
| **Tokyo CPI** | ~**last Friday** of the month, for the **current** month | Leading indicator for National CPI ~3 weeks later. |
| **Japan National CPI** | ~**3 weeks after** month-end, on a **Friday** | Follows the Tokyo print for the same reference month. |
| **Japan GDP — 1st preliminary** | ~**6 weeks after** quarter-end | Q1 (Jan–Mar) → mid-May. |
| **Japan GDP — 2nd preliminary (revised)** | ~**3 weeks after** the 1st prelim | Q1 → early-mid June. |
| **BOJ MPM** | **8 meetings/year**, pre-scheduled (2-day) | Decision on day 2. See official schedule link. |
| **BOJ Summary of Opinions** | ~**8 business days after** each MPM | — |
| **BOJ MPM Minutes** | released after the *following* MPM | Longer lag than Summary of Opinions. |
| **JGB auctions** | Monthly by tenor, per MOF issuance calendar | 30Y, 20Y, 10Y, 5Y, 2Y, 40Y, liquidity-enhancement each have their own slot. |
| **MOF weekly ITS flows** | Every **Thursday**, for the prior **Sun–Sat** week | CP932-encoded CSV. 🔧 **CORRECTED 2026-08-04** (was "Sat–Fri" — this file was the error, not STATUS/CALENDAR). **Resolved from MOF's own period labels in `workbook/MOF_FLOWS.tsv`**, weekday-checked: 7/19→7/25, 7/12→7/18, 7/5→7/11, 6/28→7/4, 6/21→6/27, 6/14→6/20 — **6 of 6 run Sunday→Saturday.** |
| **MOF monthly trade balance** | ~**3 weeks after** month-end | Customs basis. |
| **FOMC** | 8 meetings/year, pre-scheduled | Dot plot at Mar/Jun/Sep/Dec meetings. |
| **US CPI** | Monthly, ~mid-month | BLS schedule. |

---

## Official schedule sources (verify here when cadence is ambiguous)

| Source | What | URL |
|--------|------|-----|
| Cabinet Office / ESRI | GDP (QE) release schedule | https://www.esri.cao.go.jp/en/sna/kouhyou/kouhyou_top.html (carries the dated release calendar; `sokuhou_top` is the data page, not the schedule) |
| Statistics Bureau (MIC) | CPI release schedule (National + Tokyo) | https://www.stat.go.jp/english/data/cpi/ |
| BOJ | MPM dates, Summary of Opinions, minutes | https://www.boj.or.jp/en/mopo/mpmsche_minu/ |
| MOF | JGB auction / issuance calendar | https://www.mof.go.jp/english/policy/jgbs/auction/calendar/ |
| MOF | International transactions in securities (weekly) | https://www.mof.go.jp/policy/international_policy/reference/itn_transactions_in_securities/ |
| Japan Customs | Monthly trade statistics | https://www.customs.go.jp/toukei/info/index_e.htm |
| CFTC | Commitments of Traders | https://www.cftc.gov/MarketReports/CommitmentsofTraders/ |
| Federal Reserve | FOMC calendar | https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm |
| BLS | US CPI schedule | https://www.bls.gov/schedule/news_release/cpi.htm |

---

## Confirmed dates (2026 — record here once verified at source)

| Date | Event | Confirmed? | Source checked |
|------|-------|-----------|----------------|
| 2026-05-19 | Japan Q1 2026 GDP — 1st preliminary | ✅ resolved (TIMELINE) | released; +2.1% ann |
| 2026-06-02 | JGB 10Y auction (Issue #382 reopening) | ✅ resolved (workbook) | MOF Jun calendar (auction/calendar/2606e.htm); result BTC 3.530x, tail 0.7bp |
| 2026-06-08 | Japan Q1 2026 GDP — 2nd preliminary | ✅ CONFIRMED — Mon Jun 8, **8:50 AM JST** (= ~7:50 PM ET Jun 7) | ESRI release schedule (kouhyou_top), checked 2026-05-31 |
| 2026-06-10 | JGB 30Y auction | ✅ CONFIRMED | MOF Jun calendar (auction/calendar/2606e.htm), checked 2026-06-02 |
| 2026-06-16 | BOJ MPM (day 2 decision) | ✅ CONFIRMED — Tue Jun 16 (day 2 of Jun 15-16 MPM); Outlook Report meeting | BOJ schedule (en/mopo/mpmsche_minu/index.htm), checked 2026-06-02 |
| 2026-06-17 | FOMC decision + dot plot | ✅ CONFIRMED — Wed Jun 17 (day 2 of Jun 16-17*); SEP meeting | Fed calendar (monetarypolicy/fomccalendars.htm), checked 2026-06-02 |
| 2026-06-23 | JGB 5Y auction | ✅ CONFIRMED | MOF Jun calendar (auction/calendar/2606e.htm), checked 2026-06-02 |
| 2026-06-25 | JGB 20Y auction | ✅ CONFIRMED | MOF Jun calendar (auction/calendar/2606e.htm), checked 2026-06-02 |
| 2026-06-30 | JGB 2Y auction | ✅ CONFIRMED | MOF Jun calendar (auction/calendar/2606e.htm), checked 2026-06-02 |
| 2026-07-02 | JGB 10Y auction | ✅ CONFIRMED | MOF Jul calendar (auction/calendar/2607e.htm), checked 2026-06-02 |
| 2026-07-07 | JGB 30Y auction | ✅ CONFIRMED | MOF Jul calendar (auction/calendar/2607e.htm), checked 2026-06-02 |
| 2026-07-09 | JGB 5Y auction | ✅ CONFIRMED | MOF Jul calendar (auction/calendar/2607e.htm), checked 2026-06-02 |
| 2026-07-14 | JGB 20Y auction | ✅ CONFIRMED | MOF Jul calendar (auction/calendar/2607e.htm), checked 2026-06-02 |
| 2026-07-22 | JGB 40Y auction | ✅ CONFIRMED | MOF Jul calendar (auction/calendar/2607e.htm), checked 2026-06-02 |
| 2026-07-28 | FOMC meeting day 1 (Jul 28-29; non-SEP) | ✅ CONFIRMED | Fed calendar, checked 2026-06-02 |
| 2026-07-29 | FOMC decision (Jul 28-29; non-SEP) | ✅ CONFIRMED | Fed calendar, checked 2026-06-02 |
| 2026-07-30 | JGB 2Y auction | ✅ CONFIRMED | MOF Jul calendar (auction/calendar/2607e.htm), checked 2026-06-02 |
| 2026-07-30 | BOJ MPM day 1 (Jul 30-31) | ✅ CONFIRMED | BOJ schedule, checked 2026-06-02 |
| 2026-07-31 | BOJ MPM day 2 decision + Outlook Report | ✅ CONFIRMED — Outlook Report meeting | BOJ schedule (en/mopo/mpmsche_minu/index.htm), checked 2026-06-02 |
| 2026-06-10 | US CPI (May 2026 data) | ✅ RETROSPECTIVE-CONFIRMED (clears Run-7 backlog; page needs a User-Agent header — WebFetch 403s, curl -A works) | BLS schedule (bls.gov/schedule/news_release/cpi.htm), checked 2026-07-02 |
| 2026-07-14 | US CPI (June 2026 data), 8:30 AM ET | ✅ CONFIRMED — same day as JGB 20Y auction | BLS schedule, checked 2026-07-02 |
| 2026-07-22 | Japan trade balance, June (provisional whole-month) | ✅ CONFIRMED (3rd date-column of the Jun row = whole-month provisional; 4th = definite Jul-30) | Japan Customs calendar (customs.go.jp/toukei/calendar/calend_e.htm), checked 2026-07-02 |
| 2026-07-24 | Japan National CPI, June | ✅ CONFIRMED | Stats Bureau schedule (stat.go.jp/english/data/cpi/1582.html), checked 2026-07-02 |
| 2026-07-31 | Tokyo CPI, July (preliminary) | ✅ CONFIRMED — releases the morning of the BOJ Jul-31 decision (JST) | Stats Bureau schedule (1582.html), checked 2026-07-02 |
| 2026-08-04 | JGB 10Y auction | ✅ CONFIRMED | MOF Aug calendar (auction/calendar/2608e.htm), checked 2026-07-02 |
| 2026-08-06 | JGB 30Y auction | ✅ CONFIRMED | MOF Aug calendar (2608e.htm), checked 2026-07-02 |
| 2026-08-12 | US CPI (July 2026 data), 8:30 AM ET | ✅ CONFIRMED | BLS schedule, checked 2026-07-02 |
| 2026-08-17 | Japan Q2 2026 GDP — 1st preliminary (Mon, 8:50 AM JST) | ✅ CONFIRMED | ESRI release schedule (kouhyou_top), checked 2026-07-02 |
| 2026-08-18 | JGB 5Y auction | ✅ CONFIRMED | MOF Aug calendar (2608e.htm), checked 2026-07-02 |
| 2026-08-20 | JGB 20Y auction | ✅ CONFIRMED | MOF Aug calendar (2608e.htm), checked 2026-07-02 |
| 2026-08-20 | Japan trade balance, July (provisional whole-month) | ✅ CONFIRMED | Japan Customs calendar, checked 2026-07-02 |
| 2026-08-21 | Japan National CPI, July — ⚠️ FIRST release on the 2025 base (Stats Bureau row carries "Revision to 2025-Base Consumer Price Index" remark) | ✅ CONFIRMED | Stats Bureau schedule (1582.html), checked 2026-07-02 |
| 2026-08-28 | JGB 2Y auction | ✅ CONFIRMED | MOF Aug calendar (2608e.htm), checked 2026-07-02 |
| 2026-08-28 | Tokyo CPI, August (preliminary) | ✅ CONFIRMED | Stats Bureau schedule (1582.html), checked 2026-07-02 |
| 2026-09-08 | Japan Q2 2026 GDP — 2nd preliminary (Tue, 8:50 AM JST) | ✅ CONFIRMED (beyond Jul-Aug audit window; recorded for the next audit) | ESRI release schedule, checked 2026-07-02 |
| 2026-09-16 | FOMC decision + SEP (Sep 15-16) | ✅ CONFIRMED — no FOMC in August | Fed calendar (fomccalendars.htm), checked 2026-07-02 |
| 2026-09-18 | BOJ MPM day 2 decision (Sep 17-18; no Outlook Report) | ✅ CONFIRMED — no MPM in August; ⚠️ lands ON the LOCKED Sep-18 convexity window-end | BOJ schedule (mpmsche_minu), checked 2026-07-02 |
| 2026-07-31 | CFTC COT print (Jul-28 data), 3:30 PM ET | ✅ CONFIRMED — cadence-derived (Jul-28 = Tuesday, Jul-31 = Friday same week) | Weekly Fri-release/prior-Tue-data cadence rule, weekday-verified 2026-07-31 |
| 2026-08-07 | CFTC COT print (Aug-4 data), 3:30 PM ET | ✅ CONFIRMED — cadence-derived (Aug-4 = Tuesday, Aug-7 = Friday same week) | Weekly cadence rule, weekday-verified 2026-07-31 |
| 2026-08-31 | MOF monthly intervention data (last business day of Aug) | ✅ CONFIRMED — Aug-31 2026 = Monday; Aug-29/30 = Sat/Sun, so Aug-31 is the last business day of August | Weekday-verified 2026-07-31 (no MOF-specific holiday conflict found) |
| 2026-09-01 | JGB 10Y auction | ✅ CONFIRMED | MOF Sep calendar (auction/calendar/2609e.htm), checked 2026-07-31 |
| 2026-09-03 | JGB 30Y auction | ✅ CONFIRMED | MOF Sep calendar (2609e.htm), checked 2026-07-31 |
| 2026-09-08 | Japan Q2 2026 GDP — 2nd preliminary | ✅ CONFIRMED (reused Run-11 pre-confirm; beyond that audit's window, now in-window) | ESRI release schedule, checked 2026-07-02, reconfirmed no change 2026-07-31 |
| 2026-09-11 | US CPI (August 2026 data), 8:30 AM ET | ✅ CONFIRMED via cross-checked secondary sources (macroornoise.com CPI calendar + cpiinflationcalculator.com, independently agreeing) — BLS primary (bls.gov/schedule + /schedule/2026/09_sched.htm) returned 403 this session (curl+UA also blocked, unlike the Jun-10 precedent). ⚠️ **Primary re-verify RE-ATTEMPTED 2026-08-02 (KOYOMI Run-14): still HTTP 403 with curl + browser User-Agent** — the Jun-10 curl+UA workaround remains dead, n=2 sessions. Caveat retained per SAM ruling 2026-08-02; re-attempt at the next audit. | Secondary-source cross-check, 2026-07-31; primary re-attempted (403) 2026-08-02 |
| 2026-09-15 | JGB 20Y auction | ✅ CONFIRMED | MOF Sep calendar (2609e.htm), checked 2026-07-31 |
| 2026-09-16 | FOMC decision + SEP (Sep 15-16) | ✅ CONFIRMED (reused Run-11 pre-confirm) | Fed calendar, checked 2026-07-02, reconfirmed no change 2026-07-31 |
| 2026-09-16 | Japan trade balance, August (provisional whole-month) | ✅ CONFIRMED (3rd date-column of the Aug. row = whole-month provisional, same convention as the Jun/Jul rows) | Japan Customs calendar (customs.go.jp/toukei/calendar/calend_e.htm), checked 2026-07-31 |
| 2026-09-18 | Japan National CPI, August | ✅ CONFIRMED — ⚠️ SAME DAY as the BOJ Sep-18 decision + the Sep-18 convexity window-end retire-check (triple-stack) | Stats Bureau schedule (1582.html), checked 2026-07-31 |
| 2026-09-29 | JGB 40Y auction | ✅ CONFIRMED — no 40Y auction in August; first since Jul-22 | MOF Sep calendar (2609e.htm), checked 2026-07-31 |
| 2026-09-30 | JGB 2Y auction | ✅ CONFIRMED | MOF Sep calendar (2609e.htm), checked 2026-07-31 |
| 2026-10-02 | Tokyo CPI, September (preliminary) — ⚠️ NOT within September | ✅ CONFIRMED — Stats Bureau's own schedule shows Tokyo's September-survey release landing Oct-2, breaking the "Tokyo CPI = same-month, ~month-end" pattern seen Apr–Aug (out-of-window for the Sep baseline audit; flag for the October audit / next run) | Stats Bureau schedule (1582.html), checked 2026-07-31 |

| 2026-08-04 | BOJ current-account projection `jd20260803.xlsx` — T+2 semi-confirm of the 7/30 MOF op | ✅ CONFIRMED — cadence/weekday-derived (Aug-4 = Tuesday; T+2 off Thu 7/30). Method = Tanshi-forecast fiscal-factor gap, `MOF_INTERVENTION_PLAYBOOK.md` S1-A | Date + method transcribed from STATUS 2026-08-02 § INTERVENTION STATUS; weekday-verified 2026-08-02 |
| 2026-08-05 | BOJ current-account projection `jd20260804.xlsx` — T+2 discriminator for the 7/31 CANDIDATE op | ✅ CONFIRMED — cadence/weekday-derived (Aug-5 = Wednesday; T+2 off Fri 7/31) | Same source as above; weekday-verified 2026-08-02 |
| 2026-08-06 | MOF weekly ITS flows — the week after "wk 7/19-25" (3rd-week BND-11 confirm) | ✅ CONFIRMED **date** — cadence rule (Thursday release for the prior week); Aug-6 = Thursday, and it is the next release after the currently-posted 7/19-25 week. ✅ **Week-LABEL discrepancy RESOLVED 2026-08-04 in favour of STATUS/CALENDAR (Sun–Sat).** Adjudicated against the primary rather than by preference: MOF's own period strings in `workbook/MOF_FLOWS.tsv` are **6-of-6 Sunday→Saturday** (7/19 Sun→7/25 Sat, 7/12 Sun→7/18 Sat, 7/5 Sun→7/11 Sat, 6/28 Sun→7/4 Sat, 6/21 Sun→6/27 Sat, 6/14 Sun→6/20 Sat). **This file's "Sat–Fri" rule was the error and is corrected above.** ⇒ **The Aug-6 label "wk 7/26-8/1" is CORRECT** (7/26 Sun → 8/1 Sat) and the 3rd-week BND-11 confirm can be read as written — the flag is cleared *before* the print, not after. *(KOYOMI correctly escalated rather than guessing; the cadence rule was SAM's to own.)* | MOF weekly cadence rule (this file) + STATUS 2026-08-02 § LIVE MARKET DATA; weekday-verified 2026-08-02 |

| 2026-08-07 | MOF quarterly FX-intervention per-operation disclosure, Apr-Jun 2026 (Q2) | ✅ CONFIRMED (retrospective; own primary pull, closes the Run-5 [2026-06-03] PENDING date-pin item) — `feio/quarter/2026_2Qe.html` lists 3 ops by date (Apr-30 ¥6,278.7B / May-4 ¥780.2B / May-6 ¥4,675.9B), total ¥11,734.9B for the quarter, matching STATUS's already-known MOF-monthly-sourced aggregate exactly | `mof.go.jp/english/policy/international_policy/reference/feio/quarter/2026_2Qe.html`, checked 2026-08-17 |
| 2026-05-12 | MOF quarterly FX-intervention per-operation disclosure, Jan-Mar 2026 (Q1) | ✅ CONFIRMED (retrospective; cadence baseline) — ¥0 for the quarter | `feio/quarter/2026_1Qe.html`, checked 2026-08-17 |
| ~2026-11-09 | MOF quarterly FX-intervention per-operation disclosure, Jul-Sep 2026 (Q3) — the JAPANESE-side definitive per-op record of the 7/30-31 ops | ⚠️ ESTIMATE, not announced. Cadence derived from 2 data points: Q1(Jan-Mar quarter-end)→published May-12 = +42d; Q2(Jun-30 quarter-end)→published Aug-7 = +38d. Applying +38 to +42d to the Sep-30 quarter-end gives Nov-7 to Nov-11; used the midpoint. Lands within days of the already-tracked FRBNY Q3 estimate (~Nov-13) | Cadence derived from the two confirmed rows above; re-confirm at `feio/quarter/` index in early November |

*MOF Sep auction-calendar alteration page (`2609ae.htm`) checked 2026-07-31: 404 — no alterations exist for September yet (consistent with the Jul/Aug precedent of alterations appearing mid-month, not at month-start). **Re-check due early September** (or at the October audit).* 🔧 **OBLIGATION DISCHARGED — re-checked 2026-09-11, still 404; September closed with no alterations. See the KOYOMI Run-21 block below. Do not re-run this re-check.**

| 2026-08-27 | MOF monthly intervention data (feio index) — re-check, NOT a new confirm | ⚠️ **STILL UNRESOLVED between ~Fri 8/28 and ~Mon 8/31.** Fetched `mof.go.jp/english/policy/international_policy/reference/feio/` at primary: latest posted release is still Jul-31 (Jun29-Jul29 window); no August window posted as of this check. This is consistent with either candidate date — the page carries no forward-looking "next release" date, so it cannot itself distinguish 8/28 from 8/31. Re-confirm again next session (after 8/28 has passed). 🔧 **CLOSED at KOYOMI Run-19 (2026-09-02): the release landed Fri 2026-08-28** (¥15,399.3B for the Jul-30→Aug-26 window, own primary) — the 8/28 branch of the cadence estimate was right. This row is historical; the question is not open. | `mof.go.jp/english/policy/international_policy/reference/feio/`, checked 2026-08-27 |

| 2026-09-09 | BOJ Sep-9 provisional results / Sep-10 projection publication | ✅ CONFIRMED cadence-derived — normal business day around 18:00 JST; these are not final Sep-9 actuals | https://www.boj.or.jp/en/statistics/boj/fm/juq/index.htm, checked 2026-09-09 UTC/JST (2026-09-08 ET) |
| 2026-09-10 | BOJ Sep-9 final results publication | ✅ CONFIRMED cadence-derived — following business day around 10:00 JST (= Sep-9 21:00 ET) | https://www.boj.or.jp/en/statistics/boj/fm/juq/index.htm, checked 2026-09-09 UTC/JST (2026-09-08 ET) |
| 2026-09-09 | SOFR for Sep-8 transactions | ✅ CONFIRMED cadence-derived — next business day around 08:00 ET; publication date differs from transaction date | https://www.newyorkfed.org/markets/reference-rates/sofr, checked 2026-09-09 UTC/JST (2026-09-08 ET) |
| 2026-09-09 | EIA September Short-Term Energy Outlook | ✅ CONFIRMED — Wednesday Sep-9; normal release window noon–12:15 ET | https://www.eia.gov/outlooks/steo/release_schedule.php, checked 2026-09-09 UTC/JST (2026-09-08 ET) |
| 2026-09-10 | EIA Weekly Petroleum Status Report, week ending Sep-4 | ✅ CONFIRMED — Thursday Sep-10, 12:00 ET; Labor Day exception | https://www.eia.gov/petroleum/supply/weekly/schedule.php, checked 2026-09-09 UTC/JST (2026-09-08 ET) |
| 2026-09-11 | US CPI, August data | ✅ CONFIRMED at BLS primary — Friday Sep-11, 08:30 ET; supersedes prior access-failure caveat | https://www.bls.gov/schedule/2026/09_sched.htm, checked 2026-09-09 UTC/JST (2026-09-08 ET); SAM first primary-confirmed Sep-8 |


**KOYOMI Run-21 source-fetch block — all checked 2026-09-11 ET.** These are the October/September dates fetched at primary for the forward-completeness audit. Every row that became a TSV-proposal row in `KOYOMI_MEMORY.md ## PENDING` is recorded here per audit step 6, whether or not SAM applies the delta.

| Date | Event | Confirmed? | Source checked |
|------|-------|-----------|----------------|
| 2026-09-16 | Japan trade balance, August (provisional whole-month), **08:50 JST** | ✅ RE-CONFIRMED at primary, raw-HTML parse (the WebFetch summary garbles this table — Run-13 precedent). The `Aug.` row reads `Aug.28 / Sep.8 / **Sep.16** / Sep.29`; the **3rd date column is the whole-month provisional**, anchored empirically by the `Jul.` row's 3rd column `Aug.20`, which is the July trade balance the docket already graded. Time 08:50 JST from the table's own "Provisional" header. | `customs.go.jp/toukei/calendar/calend_e.htm`, checked 2026-09-11 |
| 2026-09-16 | FOMC decision (Sep 15-16) — **SEP meeting** | ✅ RE-CONFIRMED — asterisked as "associated with a Summary of Economic Projections". Remaining 2026: **Oct 27-28 (no SEP)**, **Dec 8-9 (SEP)**. | `federalreserve.gov/monetarypolicy/fomccalendars.htm`, checked 2026-09-11 |
| 2026-09-18 | BOJ MPM day 2 — **NOT an Outlook Report meeting** | ✅ **CONFIRMED — but the provenance first written here was NOT what happened, and is corrected.** This row originally read *"RE-CONFIRMED at the BOJ schedule table (Outlook column shows '—' for Sep 17-18)"*. 🔴 **KOYOMI self-reported that it had not seen that cell when it wrote that line** — it INFERRED the quarterly Jan/Apr/Jul/Oct pattern and then checked the inference against the docket, i.e. against the artifact under audit. **SAM re-fetched the BOJ primary independently 2026-09-11 and the cell IS a dash: Sept. 17-18 Outlook column = "—", no Outlook Report.** The claim was true; the stated basis was not. Recorded because a correct figure with a fabricated basis passes every check that reads the figure ([[finding_attribution_authenticates_a_figure_its_named_source_never_produced]]). ⚠️ **Oct 29-30 is a DIFFERENT matter and is NOT settled** — three reads of this same page disagreed on that one cell (raw-table read "Oct. 30 (Fri.)"; an earlier fetch a dash; SAM's fetch "no entry shown"), with no evidence the page changed between them. Do not assert Oct-30's Outlook status from any summarizer. Both docket files say "no Outlook Report" and both are correct. Remaining 2026 MPMs: **Oct 29-30**, **Dec 17-18**. | `boj.or.jp/en/mopo/mpmsche_minu/index.htm`, checked 2026-09-11 |
| — | MOF **September** auction-calendar alteration page `2609ae.htm` | ✅ **NULL-CHECK CLOSED — HTTP 404 as of 2026-09-11**, i.e. no alterations exist for September. This closes the Run-20 PENDING item, which recorded only a tool Internal Error and therefore could conclude nothing. The Run-13 "re-check due early September" obligation is discharged. | `mof.go.jp/english/policy/jgbs/auction/calendar/2609ae.htm`, checked 2026-09-11 |
| 2026-10-06 | JGB 10Y auction | ✅ CONFIRMED | MOF Oct calendar (`auction/calendar/2610e.htm`), checked 2026-09-11 |
| 2026-10-08 | JGB 30Y auction | ✅ CONFIRMED — ⚠️ first fetch of this page omitted the 30Y row; a second, explicitly exhaustive fetch surfaced it. Treat single-pass summaries of this table as incomplete. | MOF Oct calendar (`2610e.htm`), checked 2026-09-11 |
| 2026-10-08 | MOF Balance of Payments, **August 2026 (Preliminary)**, 08:50 JST | ✅ CONFIRMED at primary — the same release also carries **BoP 2nd quarter 2026 (Second Preliminary)**. Next two: **Nov-10** (September BoP + 1st-half FY2026) and **Dec-8** (October BoP). | `mof.go.jp/english/policy/international_policy/reference/balance_of_payments/index.htm`, checked 2026-09-11 |
| 2026-10-14 | JGB 5Y auction | ✅ CONFIRMED | MOF Oct calendar (`2610e.htm`), checked 2026-09-11 |
| 2026-10-14 | US CPI, September data, 08:30 ET | ✅ CONFIRMED at BLS schedule | `bls.gov/schedule/news_release/cpi.htm`, checked 2026-09-11 |
| 2026-10-20 | JGB 20Y auction | ✅ CONFIRMED | MOF Oct calendar (`2610e.htm`), checked 2026-09-11 |
| 2026-10-21 | Japan trade balance, **September** (provisional whole-month), 08:50 JST | ✅ CONFIRMED — `Sep.` row, 3rd date column (`Sep.29 / Oct.7 / **Oct.21** / Oct.29`), same convention as the Sep-16 row above. | `customs.go.jp/toukei/calendar/calend_e.htm`, checked 2026-09-11 |
| 2026-10-23 | Japan National CPI, **September** | ✅ CONFIRMED at the Stats Bureau schedule — Friday, ~3 weeks after month-end, cadence-consistent. ⚠️ The rest of that page's summary was unreliable on this fetch; only the Sep-survey National (Oct-23) and Tokyo (Oct-2) rows are recorded here. | Stats Bureau schedule (`stat.go.jp/english/data/cpi/1582.html`), checked 2026-09-11 |
| 2026-10-27 / 28 | FOMC (Oct 27-28) — **no SEP** | ✅ CONFIRMED | `federalreserve.gov/monetarypolicy/fomccalendars.htm`, checked 2026-09-11 |
| 2026-10-29 | JGB 2Y auction | ✅ CONFIRMED — ⚠️ **same day as BOJ MPM day 2 (Oct 29-30 is day 1-2, decision Oct-30)**; the 2Y auction is Oct-29, MPM day 1. | MOF Oct calendar (`2610e.htm`), checked 2026-09-11 |
| 2026-10-30 | BOJ MPM day 2 decision (Oct 29-30) | ✅ CONFIRMED | `boj.or.jp/en/mopo/mpmsche_minu/index.htm`, checked 2026-09-11 |
| ~2026-10-01 | BOJ Tankan, September 2026 survey (Q3) | ⚠️ **ESTIMATE — cadence-derived, NOT confirmed at a dated schedule.** The BOJ Tankan page shows the June-2026 survey released **Jul-1**; the quarterly pattern is ~1st business day of Apr/Jul/Oct/mid-Dec. The BOJ statistical-release-schedule URL in the table above (`statistics/outline/rele/index.htm`) returned **404** this check — the link needs repair (SAM's file to fix). | `boj.or.jp/en/statistics/tk/index.htm`, checked 2026-09-11 |
| 2026-10-22 / 2026-10-27 | JGB liquidity-enhancement auctions (5-11y / 11-39y) | ✅ CONFIRMED present — recorded for completeness only; **out-of-universe** per KOYOMI.md, deliberately excluded from the TSV. | MOF Oct calendar (`2610e.htm`), checked 2026-09-11 |
| — | MOF **October** auction-calendar alteration page `2610ae.htm` | ⬜ NOT CHECKED this run. | — |

*Add rows as dates are confirmed. Keep this table short — it's a verification scratchpad, not a full calendar (the calendar is `CALENDAR.md` / `CATALYSTS.tsv`).*
