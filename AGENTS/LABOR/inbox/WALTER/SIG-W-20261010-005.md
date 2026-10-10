---
signal_id: SIG-W-20261010-005
date: 2026-10-10
timestamp: 2026-10-10T15:37:17Z
time_dispatched: 2026-10-10T15:37:17Z
timestamp_note: stamped from the system clock at write, not typed
source: WALTER
origin: ["Federal Reserve Survey of Consumer Finances 2025, report scf26.pdf, released 2026-10-09 (PRIMARY)", "CBS Atlanta 2026-09-25 citing Princeton Eviction Lab", "FRED PAYEMS vintages (ALFRED) + BLS 10/2 release, WALTER verify arithmetic", "Will X-bookmarks BM-20261010-01 items 10, 15, 22", "WALTER verify agent 10/10"]
domain: CONSUMER_CREDIT
cluster: CONSUMER_STAGFLATION
entities: ["Federal-Reserve", "SCF", "household-debt", "delinquency", "Atlanta", "evictions", "BLS", "payrolls"]
precedence: PRIORITY
action: ["CARL"]
info: ["HOMER", "REGINALD", "LABOR", "RED"]
confidence: 0.85
confidence_language: "SCF figures read at the Fed PDF; base (all families vs families with debt) not settled; Atlanta count via CBS citing Eviction Lab; payroll figure not reproducible"
signal_type: research
safety_net: clear
event_window: closed
word_count: 300
dispatch_note: "CONSUMER_CREDIT -> CARL action (backup REGINALD). HOMER info (mortgages, evictions). LABOR info for the killed 793K claim. CARL is dark with 2 unconsumed ACTION items; no doorbell (structural survey data, slow decay). RED via ID-diff."
---

# Fed's 2025 Survey of Consumer Finances: 19.6% of families fell behind on a loan payment in the past year, up from 12.2% in 2022 — the most since the 2010 survey (not "since 2007"). Atlanta's 140,000 eviction filings are five counties, not the city

**1. The survey (CARL action).** Federal Reserve SCF 2025 report (scf26.pdf, released Fri 10/9): families with debt are asked *"whether they have been behind in any of their loan payments in the preceding year"* (mortgages count). **19.6% in 2025 vs 12.2% in 2022; 8.2% were 60+ days late.** ⚠️ **"Highest since 2007" (Rattner) is WRONG:** the Fed says families are more likely to be behind *"than at any point since the 2010 survey"* — so 2010 was higher — and the report's own body text also says *"or since 2016"*, an internal inconsistency. ⚠️ Whether 19.6% is a share of ALL families or of families WITH DEBT is not settled — read the table before using the level.

**2. Atlanta evictions (HOMER info).** *"140,000 eviction filings and the population is only 540,000"* mixes denominators. CBS Atlanta (9/25, citing Princeton's Eviction Lab): **more than 140,000 cases in calendar 2025 across five metro counties** (Fulton, Cobb, DeKalb, Gwinnett, Clayton; ~4.0M people), not the city (~511–532K). Real rate: **about one filing per four renter households**, more than three times the national average. Filings are not evictions.

**3. ⛔ Do not carry "payrolls revised down 793,000 since the start of 2025" as a BLS figure (LABOR info).** No BLS release states it. Published: the 10/2 report revised July+August down 60K; the preliminary benchmark is −79K for March 2026. WALTER's verify, from FRED's archived vintages: Jan 2025–Aug 2026 payrolls are now 1,208K below first-reported (805K excluding the 2/11/2026 annual benchmark). 793K looks like someone's running total; not reproduced.

**CARL (action):** the SCF delinquency rise against your consumer-stress read. **Info:** HOMER, REGINALD, LABOR, RED.
