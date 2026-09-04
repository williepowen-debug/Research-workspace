---
signal_id: SIG-W-20260904-006
date: 2026-09-04
time_dispatched: 2026-09-04T14:02Z
origin: Will-terminal 5-image batch 2026-09-04 ~09:4x ET, item 5 — a Grok "story summary" on X ("EIA Delays June Petroleum Report Due to Technical Glitch") + @poordart ("the very first time in the history that a 'technical issue' has prevented the release of this data"). A generated summary is not a source; verified below.
source: Investing.com (ng.investing.com) "EIA delays June petroleum supply data release due to system issue"; investinglive.com "US oil production data delayed as EIA cites technical glitch"; QCIntel "US EIA says June oil data report delayed to September on tech issues" (all 9/3–9/4, headline + summary level, none opened whole); EIA PSM page (eia.gov/petroleum/supply/monthly, OPENED 9/4: "Release Date: September 1, 2026 · Next Release Date: September 30, 2026", no delay notice); EIA notice.php (OPENED 9/4: records the November-2025 PSM postponed from 2026-01-30 to 2026-02-06 for a Census Bureau appropriation lapse).
domain: OIL_ENERGY
cluster: HYDROCARBON_INFRA
precedence: ROUTINE
action: []
info: [BRENT, HAWK]
entities: [EIA, Petroleum-Supply-Monthly, PSM, Weekly-Petroleum-Status-Report, Census-Bureau, Cushing, SPR]
signal_type: context
confidence: 0.75
confidence_language: assessed
verdict: CONFIRMED that EIA postponed the June-2026 Petroleum Supply Monthly (due 8/31) citing an issue between its back-end and public-facing systems, with release "in September"; UNRESOLVED at the primary whether the 9/1 date now shown on EIA's PSM page is the actual release or a stale schedule. CORRECTED-FRAMING: "the very first time in history" is FALSE — EIA's own notice page records the November-2025 PSM slipping 1/30 → 2/6/2026. The Weekly Petroleum Status Report is unaffected, so headline inventories, Cushing and the SPR keep printing; what is delayed is the granular monthly production / import / export / state-level series.
consumer_lens: BRENT — if any BRENT vector keys on PSM June data (state-level production, exports by destination), expect the gap; the Cushing Boundary-#3 scan runs on the weekly and is unaffected. HAWK — the "data is being withheld amid Hormuz" insinuation is the relay's; EIA cited an operational issue and there is a documented precedent of a scheduling slip. No view.
corrects: none
---

# EIA postponed the June Petroleum Supply Monthly past 8/31 on a systems issue. NOT "the first time ever": the Nov-2025 PSM slipped a week in January. Weekly data unaffected.

## 1. What is confirmed, and at what tier

| Claim | Status | Basis |
|---|---|---|
| June-2026 PSM (due 8/31) postponed, "release in September," systems issue between back-end and public-facing systems | **CONFIRMED (carriers)** | Investing.com · investinglive · QCIntel, 9/3–9/4 |
| Actual release date | **UNRESOLVED at primary** | EIA PSM page shows *Release Date: September 1, 2026* — could be the delayed release landing 9/1 or an un-updated schedule cell; no delay banner on the page |
| "Very first time in history a technical issue prevented release" | ❌ **FALSE** | EIA `notice.php`: *"PSM data for November 2025"* postponed from **2026-01-30 to 2026-02-06** (Census appropriation lapse); a carrier headline 9/4 reads *"EIA Delays Key Oil Data Again, Continuing a Year of Disruptions"* |
| Weekly Petroleum Status Report continues | **CONFIRMED** | EIA weekly schedule unchanged; Cushing 22.51M [8/28] came from it |

## 2. What is affected
The PSM is the granular monthly series: national and **state-level crude production**, imports, **exports by destination**, movements, monthly inventories. The weekly keeps headline inventories, Cushing, SPR and implied demand flowing. ⇒ **WALTER's Boundary-#3 Cushing scan is unaffected.**

## 3. What is NOT in this signal
No claim that data is being withheld for political reasons — EIA cited an operational issue and there is a documented January precedent. The Hormuz / SPR-at-1982-low context in the Grok summary is true and already on the BOARD; it does not connect to the delay.

**Confidence 0.75** — the delay is multi-carrier but no carrier was opened whole and EIA's own page is ambiguous on whether it has since released; the "first time" refutation is at the EIA primary.
