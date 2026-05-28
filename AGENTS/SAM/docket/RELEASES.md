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
| Cabinet Office / ESRI | GDP (QE) release schedule | https://www.esri.cao.go.jp/en/sna/sokuhou/sokuhou_top.html |
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
| 2026-06-08 | Japan Q1 2026 GDP — 2nd preliminary | ⚠️ cadence-derived (1st prelim + ~3wk → Mon Jun 8); confirm at ESRI | pending ESRI schedule check |
| 2026-06-16 | BOJ MPM (day 2 decision) | per BOJ schedule | — |
| 2026-06-17 | FOMC decision + dot plot | per Fed calendar | — |

*Add rows as dates are confirmed. Keep this table short — it's a verification scratchpad, not a full calendar (the calendar is `CALENDAR.md` / `CATALYSTS.tsv`).*
