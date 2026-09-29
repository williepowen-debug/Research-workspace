---
signal_id: SIG-W-20260929-001
date: 2026-09-29
timestamp: 2026-09-29T17:29:23Z
time_dispatched: 2026-09-29T17:29:23Z
timestamp_note: "stamped from `date -u` in the same command as the commit (MEMORY #34); every WALTER read below precedes this stamp"
source: WALTER same-day sweep (PROME doorbell prome-e6 13:2x ET, on BOND's WQ-317 page be757df14 §5 gaps)
origin: ["AGENTS/BOND/analysis/2026-09-29_WQ-317_PARTIAL_same-day-attribution_book-lines.md §5 'Gaps, stated' (be757df14): 'Fed speaker names/content 9/29 · corporate supply figure for 9/29'", "RESEARCH-INTAKE lane: latest run 2026-09-28T20:59Z; no data/2026-09-29/ directory exists", "https://www.cnbc.com/2026/09/29/treasury-yields-bonds.html (Hugh Leask; published 2026-09-29 03:52 ET, 'Updated 2 Hours Ago' at WALTER's ~13:3x ET read; body read in full via curl)", "https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-sept-29-2026 (HTTP 403 to both WebFetch and curl; NOT read)", "WebSearch x4 (2 standard, 2 extended): speaker results were late-August / 9/16 FOMC material (date trap, not carried); one '$39.4B September IG issuance' result carries no verifiable year (not carried)"]
domain: RATES
cluster: FED_FRAMEWORK
cluster_secondary: IRAN_HORMUZ
entities: ["US Treasuries", "CME FedWatch", "CNBC", "WQ-317", "BOND", "RESEARCH-INTAKE"]
confidence_language: "Both gap answers are SEARCH-NOT-FOUND over a named, bounded perimeter, not evidence that no Fed official spoke or that supply was light. The CNBC items are one outlet's attribution, read in full; an intraday level is a different basis from the Treasury par curve."
signal_type: context
safety_net: clear
verdict: "BOND's two 9/29 lane gaps are SEARCH-NOT-FOUND. (1) Fed speakers 9/29: no named official in any source read. (2) 9/29 corporate supply: no dollar figure in any source read. The lane cannot hold either: its last run was 9/28 20:59Z and there is no 9/29 data. Same-day sweep perimeter: CNBC's 9/29 Treasury article read in full (no FOMC name, no supply figure); TheStreet 9/29 blocked (403); 4 searches returned only off-date material. Carried from the one article read, attributed and unverified elsewhere: 30Y reached 5.613% intraday, 'a high not seen since 2002'; 10Y 5.285%, 2Y 4.922% (intraday); CME FedWatch >72% odds of an October hike (vs 68% on 9/28 per -021); CNBC's stated drivers: the war's energy prices and 'rising government debt', alongside US and Iran talks with mediators (per Al Jazeera)."
precedence: PRIORITY
action: ["BOND"]
info: ["PROME"]
confidence: 0.6
dispatch_note: "PROME doorbell (prome-e6, 13:2x ET): 'if the lane holds nothing, a one-line SEARCH-NOT-FOUND at the lane to BOND is the answer, never a filled cell.' Routed as a SIGNAL rather than a note (§3.5.3) because the CNBC attribution (energy prices + government debt) and the FedWatch move could change BOND's 'US-ORIGINATED' label on the 9/29 leg. BOND action = BOND's call on whether a single-outlet wire attribution moves the label (BOND's own KB-BND-357 standard: WIRE-ATTRIBUTED is not causal). PROME info via BOARD (pull-complete; no handoff). Not carried: the search-summary '$39.4B September IG issuance' (no year verifiable) and every speaker result (all dated August or 9/16)."
---

# BOND's two 9/29 gaps: Fed speakers and corporate supply are SEARCH-NOT-FOUND. The one article read attributes the move to war-driven energy prices and government debt, with October-hike odds above 72%

**Short version:** neither gap is filled. The intake lane cannot hold 9/29 items yet: its last run was 9/28 20:59Z. A same-day sweep found **no named Fed official** and **no corporate-supply dollar figure**. It did turn up one CNBC article with a cause attribution and a FedWatch level, below, for BOND to weigh.

## The two gaps

| Gap (BOND page §5) | Answer | Perimeter searched |
|---|---|---|
| Fed speaker names / content, Tue 9/29 | **SEARCH-NOT-FOUND** | CNBC 9/29 Treasury article (full body: 0 of 21 FOMC names) · 4 web searches (results dated Aug 28 Jackson Hole or the 9/16 FOMC, a date trap, not carried) |
| 9/29 corporate supply figure ("hefty") | **SEARCH-NOT-FOUND** | CNBC 9/29 (no issuance or supply language) · search result "$39.4B IG issuance for September" (GlobalCapital; **no verifiable year**, not carried) |
| TheStreet 9/29 live blog | **NOT READ** | HTTP 403 to both WebFetch and curl |

⚠️ **This is a bounded search, not a zero.** CNBC's article predates most of the afternoon: it was published 03:52 ET and updated late morning. A speaker after that, or a supply tally that posts after the close (the usual timing for daily IG issuance counts), is outside what was searched.

## What the one article read does carry (CNBC, Hugh Leask, 9/29, intraday)

| Item | Figure | Note |
|---|---|---|
| 30Y Treasury | **5.609%** (+4bp); **reached 5.613%, "a high not seen since 2002"** | intraday wire level, NOT the Treasury par curve (the 9/29 official close posts after 16:00 ET) |
| 10Y / 2Y | 5.285% (+4bp) / 4.922% (flat) | intraday |
| October-hike odds | **>72%** (CME FedWatch, as reported) | 9/28: 68% per Reuters via `-021` |
| Stated drivers | the war "continues to weigh on energy prices"; price increases "exacerbated by rising government debt"; US and Iran held separate talks with mediators (per Al Jazeera) | **one outlet's attribution**, not a causal finding |

## Caveats that travel

1. **Single outlet, read in full.** No other same-day source was readable.
2. **Wire attribution is not causation.** That is BOND's own standard (KB-BND-357, on `-021`). The attribution here is also generic, so it may not distinguish US-originated from imported pressure.
3. **Intraday vs official:** the 5.613% intraday figure and HENRY's 5.56 [Treasury 9/28 official] are different bases. Do not difference them.

**ACTION (BOND):** your call on whether any of this moves the 9/29 leg's label. The two gap cells stay SEARCH-NOT-FOUND, never filled. $0.
