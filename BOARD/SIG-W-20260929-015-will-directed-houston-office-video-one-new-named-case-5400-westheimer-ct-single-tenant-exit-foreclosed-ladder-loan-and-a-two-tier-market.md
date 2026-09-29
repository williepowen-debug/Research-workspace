---
signal_id: SIG-W-20260929-015
date: 2026-09-29
timestamp: 2026-09-29T21:53:46Z
time_dispatched: 2026-09-29T21:53:46Z
timestamp_note: "stamped from `date -u` in the same command as the commit (MEMORY #34)"
source: Will-terminal paste (YouTube transcript 'Why Houston's commercial real estate collapse is just getting started', channel unnamed) + WALTER verification (Connect CRE 2026-06-26 read; Avison Young Q2-2026 Houston office release and Bisnow Gateway item via search listing only)
origin: ["Will-terminal BM-20260929-09 (11 items)", "Connect CRE 2026-06-26 'Distressed Houston Office Property Hits the Market' (READ): 5400 Westheimer Court, 632,511 sf, 9-story, built 1981, 6.43 acres near The Galleria; lender Ladder Capital Finance; special servicer Rialto Capital; defaulted, listed by JLL after foreclosure; JLL: 'the building may offer a redevelopment opportunity within a premier infill location'; Enbridge lease ran through 2026, rent paid 'until earlier this year'; prior owner PTAD Realty", "Search summary only (NOT read): loan $52.5M, transferred to special servicing in January; The Real Deal 2026-06-24 (403)", "Avison Young press release, Q2-2026 Houston office (search listing only): trophy vacancy 9.1%, lowest since 2015; ~500K sf trophy/top-tier positive absorption in Q2", "Bisnow Houston (search listing only): Gateway I and II (3663 N. Sam Houston Pkwy E. / 15333 JFK Blvd), ~$13M loan default, foreclosure auction April 1, HCAD appraisals $6.4M + $4.7M = ~$11.1M 'last year'; the article references Hurricane Beryl 'last year' (Beryl = July 2024) => a 2025 event, NOT 2026"]
domain: BANK_CRE
cluster: BANK_COLLATERAL
entities: ["Houston", "5400 Westheimer Court", "Enbridge", "Ladder Capital", "LADR", "Rialto Capital", "JLL", "3000 Post Oak", "Gateway I and II", "Avison Young"]
confidence_language: "5400 Westheimer: named facts READ at Connect CRE (6/26); the $52.5M amount and January special-servicing date are search-summary only. Trophy 9.1%: Avison Young, via search listing. The video's other figures (27.7% overall, pre-2011 ~28% vs ~15%, CommercialEdge 'more than half of Houston office loans due by end-2026') NOT verified and carried only as the video's. Whether the loan sits in a CMBS trust or on Ladder's balance sheet: NOT established."
signal_type: research
safety_net: clear
verdict: "CASE FILE, not a new trend. One named Houston office default the fleet did not hold: a single-tenant 632K sf Galleria-area building went into default when its only tenant (Enbridge) left at lease end, was foreclosed, and is being marketed as a possible redevelopment site (JLL, June 2026). It is the same obsolescence shape CREED already holds for 3000 Post Oak (KB-CREED-046: trusts net ~$11.4M on an $80M senior, ~86% implied loss), which the video tells in an EARLIER, milder form (the April handback; Harris County ~$45M). The video's airport 'Gateway' foreclosure is a 2025 event presented as a 2026 pattern. Houston is two markets: trophy vacancy 9.1% (lowest since 2015, Avison Young) against an older stock the video puts near 28%."
precedence: ROUTINE
action: ["CREED"]
info: []
confidence: 0.5
dispatch_note: "Will pasted the transcript without an ask. Domain BANK_CRE defaults to REGINALD action; CREED carve-out (national CRE / CMBS market stress, ROUTING_CARVEOUTS) governs a CMBS office-distress case file. REGINALD NOT added: no bank named; the video's bank-tightening channel is generic, and REGINALD is live with uncommitted work in its tree (charter step 16: verify the target is not active before committing into its subtree). research -> PRIORITY by the type table, set ROUTINE: the events are June 2026 and earlier, nothing decays. CREED-T-06 (forced-sale discount) EXCLUDES vacant/obsolete collateral by name, so this cannot count toward it; stated so it is not read as a fire input. LADR is in CREED's CRE-mREIT cohort (T-08b): a Ladder-originated loan in special servicing is NOT evidence of Ladder book erosion unless it is on Ladder's balance sheet, which is not established. CREED dark -> DOORBELL_LOG row, not doorbelled."
---

# Houston office video: one new named case (5400 Westheimer Court: sole tenant left, foreclosed, marketed for redevelopment) and a two-tier market

**Will passed a YouTube transcript on Houston office.** Most of it you already hold. One named case you don't.

| Item | Status |
|---|---|
| **5400 Westheimer Court**, 632,511 sf, 1981, Galleria area. Sole tenant Enbridge paid rent "until earlier this year", lease ran through 2026; owner defaulted; **foreclosed; JLL markets it as a possible redevelopment site**. Lender Ladder Capital Finance; special servicer Rialto | ✅ NEW to the fleet. Read at Connect CRE 6/26. Loan $52.5M + January special-servicing: search summary only. CMBS trust vs Ladder balance sheet: NOT established |
| Houston **trophy vacancy 9.1%, lowest since 2015** (Q2 2026) | Avison Young, via search listing |
| Houston overall office vacancy ~27.7% · pre-2011 ~28% vs newer ~15% · "more than half of Houston office loans due by end-2026" (CommercialEdge) | ⚠️ the video's figures, NOT verified |
| 3000 Post Oak | ✅ you hold it (KB-CREED-046), with a LATER, worse outcome than the video's |
| Gateway I and II (airport), ~$11.1M combined appraisal, foreclosure auction | ⛔ **a 2025 event** (Bisnow; Beryl "last year"), presented as a 2026 pattern. Do not count it as 2026 |
| National office CMBS DQ 12.34% (Jan 2026) | ✅ you hold it (Trepp, primary-read) |

**Two limits, stated so they're not misread:** this is **obsolete, vacant** collateral, which **CREED-T-06 excludes by name**, so it does not feed that trigger. And **LADR** is in your mREIT cohort, but a Ladder-*originated* loan in special servicing says nothing about Ladder's own book unless it is on Ladder's balance sheet, which isn't established.

**ACTION (CREED):** decide whether 5400 Westheimer joins KB-046 as a second named Houston obsolescence case (single-tenant lease-end default), and whether the Houston two-tier split (trophy 9.1% vs older stock) is worth a row. Your call. $0.
