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
| **MOF weekly ITS flows** | Every **Thursday**, for the prior **Sat–Fri** week | CP932-encoded CSV. |
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

*Add rows as dates are confirmed. Keep this table short — it's a verification scratchpad, not a full calendar (the calendar is `CALENDAR.md` / `CATALYSTS.tsv`).*
