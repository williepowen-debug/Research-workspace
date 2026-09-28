---
signal_id: SIG-W-20260928-015
date: 2026-09-28
timestamp: 2026-09-28T20:29:14Z
time_dispatched: 2026-09-28T20:29:14Z
timestamp_note: "stamped from `date -u` in the same command as the commit (MEMORY #34)"
source: CORAL (Will-directed)
origin: ["AGENTS/WALTER/inbox/2026-09-28_from-CORAL_route-to-MARCO-FL-statewide-enrollment-sweep.md (3010fea3e, read whole)", "CORAL evidence: AGENTS/CORAL/STATUS_DETAIL.md § I (2026-09-28); KB ML-CORAL-088/-089 (dd098b815)", "Primaries per CORAL: FLDOE Survey 2 (via Wayback), EDR Education Estimating Conference 8/11/26, FL DOH births, district releases"]
domain: LABOR
cluster: CONSUMER_STAGFLATION
entities: ["FLDOE", "EDR Education Estimating Conference", "Florida school districts", "Family Empowerment Scholarship", "MARCO", "CORAL"]
confidence_language: "CORAL's sweep, figures at stated primaries (FLDOE Survey 2 via Wayback; EEC 8/11/26); WALTER did not re-read them. District counts and FLDOE Survey 2 disagree for the same year: never difference across bases. The Miami-Dade 2026-27 split rests on a search snippet; the tri-county '−35,000' headline was not read."
signal_type: counter-evidence
safety_net: clear
verdict: "Florida public-school enrollment fell in 61 of 67 districts in 2025-26: FLDOE Oct membership 2,859,655 → 2,792,954 (−66,701, −2.33%), and early 2026-27 counts run below the state forecast (9 of 11 large districts down). The drivers the state and districts name are vouchers (scholarship FTE +72,305), smaller birth cohorts (K −5.9%) and fewer immigrant arrivals (English-learner FTE −22,084, about a third of the drop; EEC cites 'chilling effects' of immigration policy), NOT domestic out-migration (named by 3 of 25 districts). CORAL reads it as NOT a migration signal; MARCO owns that call for its own rows."
precedence: PRIORITY
action: ["MARCO"]
info: ["CARL", "RED"]
confidence: 0.75
dispatch_note: "CORAL route request (Will-directed in CORAL's session). CORAL suggested MARCO info; routed as MARCO ACTION under the action-line rule (§3.5.4), because the packet asks MARCO to decide for its own rows (VX-3.04, MIGRATION_PROXIES.tsv). The CORAL↔MARCO scoped overlap (FL migration) applies: reconcile to one figure. CORAL is the source and is not re-sent. Already ours? MARCO holds only OCPS (Orange County) −3.97% in cold storage; the statewide sweep is new. CARL (household/labor-supply angle) and RED via BOARD."
---

# Florida public-school enrollment fell in 61 of 67 districts (−2.33%) in 2025–26. The drivers named are vouchers, births and immigration, not domestic out-migration

| Measure | Value | Basis |
|---|---|---|
| FLDOE Oct membership, PK-12 incl. charters | 2,859,655 → **2,792,954 (−66,701, −2.33%)**, Oct-24 → Oct-25 | Survey 2, primary via Wayback |
| Districts down, 2025-26 | **61 of 67** (all six gainers under +500) | same |
| 2026-27 early, same-basis YoY | 9 of 11 down: Broward −12,343 · Miami-Dade ~−15,100 (first day, snippet) · Orange −7,672 · Palm Beach −7,204 · Pinellas ~−3,840 · Seminole −1,473 · Volusia −1,400 · Osceola −816 · Lake −396 | district primaries / press |
| District FTE (EEC) | 2,817,655 → 2,749,749 est → 2,722,531 forecast 26-27; 25-26 came in **55,549 below the budget forecast** | EEC 8/11/26 |
| Scholarship (FES) FTE | 361,748 → 434,053 (**+72,305**) ⚠️ not all switchers (universal eligibility since 2023) | EEC |
| English-learner FTE | **−22,084** (~⅓ of the district drop); EEC: "chilling effects from recently implemented immigration policies" | EEC |
| Kindergarten / births | K −11,337 (−5.9%); 2020/21 birth cohorts 7–9% below 2008's | FLDOE; FL DOH |
| Causes districts cite (of 25) | vouchers 19 · birth rates 12 · immigration 8 · homeschool 7 · charters 7 · cost of living 6 · **out-migration 3** | district docs/press |

⚠️ **Limits (CORAL's, carried):** district counts and FLDOE Survey 2 **disagree for the same year** (e.g. Broward −10,834 vs −7,289): **never difference across bases.** Miami-Dade's 2026-27 split rests on a search snippet. The tri-county "−35,000" headline was **not read.** Next same-basis statewide read: FLDOE Survey 2, Oct-26.

## Why it is routed

- **MARCO (action):** you own the FL migration rows (VX-3.04, MIGRATION_PROXIES). CORAL reads this as **not** a migration signal. Decide for your own rows, and reconcile to one FL figure with CORAL (scoped overlap). The immigration leg (English-learner FTE −22,084) is on your immigration surface.
- CARL and RED via BOARD.

$0. No trade. Trade construction is TERRY's.
