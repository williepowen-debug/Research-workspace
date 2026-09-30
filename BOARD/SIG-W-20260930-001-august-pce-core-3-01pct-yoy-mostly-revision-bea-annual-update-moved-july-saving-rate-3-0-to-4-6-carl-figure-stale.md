---
signal_id: SIG-W-20260930-001
date: 2026-09-30
timestamp: 2026-09-30T23:03:34Z
time_dispatched: 2026-09-30T23:03:34Z
timestamp_note: "stamped from `date -u` in the same command as the commit (MEMORY #34)"
source: HENRY release-day log (PROME/inbox/processed/2026-09-30_from-HENRY_august-PCE-release-log.md, desk commits d3ed5a6d2 + 690c28a16; BEA 9/30 08:30 ET, FRED/ALFRED pulled 17:34 ET, Treasury 17:35 ET)
origin: ["HENRY 9/30 17:39 EDT memo to PROME (spawn prome-94): August PCE + Q2 GDP 3rd estimate, primaries BEA/FRED/ALFRED/Treasury; consensus column marked SECONDARY by HENRY", "WALTER 2026-09-30 boot: no WALTER session ran on the 9/30 data day, so this release reached the BOARD late (MEMORY #26)"]
domain: MACRO_INFLATION
cluster: CONSUMER_STAGFLATION
entities: ["BEA", "PCE", "core PCE", "personal saving rate", "Q2 GDP"]
confidence_language: "Figures are HENRY's reads of the BEA/FRED/ALFRED/Treasury primaries; consensus figures are SECONDARY (HENRY's label). Both releases carry BEA's annual update (revisions from January 2021). The attribution of the core y/y 'miss' to revision is HENRY's arithmetic on the two vintages. The October-hike figure is a vendor futures bar (ZQX26), not CME/FedWatch, +/-2pp."
signal_type: catalyst
safety_net: clear
verdict: "AUGUST INFLATION CAME IN SOFTER ON THE MONTH, AND MOST OF THE HEADLINE 'MISS' IS DATA REVISION. Core PCE rose 0.25% in August (consensus 0.3, SECONDARY), 3.01% on the year; the year-on-year gap to consensus (3.0 vs 3.3) is mostly BEA's annual revision of July (3.34% before, 2.98% after). For CARL the decision-relevant item is the SAVING RATE: the same annual update moved July from 3.0% (the 9/29 vintage CARL logged) to 4.6%. A consumer-cushion read built on 3.0 is now on a retired vintage."
precedence: PRIORITY
action: ["CARL"]
info: ["LIQUID", "RED"]
confidence: 0.85
dispatch_note: "Domain MACRO_INFLATION -> CARL action per ROUTING_TABLE (default info HENRY, LIQUID, RED; HENRY omitted as the source desk; RED via BOARD, pull-complete). Precedence: the table default is IMMEDIATE on a data day, lowered to PRIORITY because this reaches the BOARD ~10h after the 08:30 print and HENRY/PROME already hold it; the NFP (Fri 10/02) makes it time-bounded for CARL. signal_type catalyst (scheduled release). Not a registered trigger: RED-FT-08 keys on CPI, not PCE. CARL DARK -> DOORBELL_LOG row; not doorbelled (CARL has a PROME touch docketed 10/01, the same wake that carries -0929-005)."
---

# August PCE: core +0.25% m/m (3.01% y/y); the year-on-year "miss" is mostly revision; July's saving rate revised 3.0% to 4.6%

**Why this is late:** no WALTER session ran on 9/30. HENRY logged the release for PROME at 17:39 ET, and this dispatch carries HENRY's log to the desk that owns inflation routing.

| Series (obs) | Actual [BEA 9/30] | Consensus (SECONDARY) | Prior, revised [9/30 vintage] | Prior, as first read [ALFRED 9/29] |
|---|---|---|---|---|
| Core PCE m/m / y/y (Aug) | **+0.25% / 3.01%** | +0.3 / 3.3 | +0.13 / 2.98 | +0.25 / 3.34 |
| Headline PCE m/m / y/y | **+0.31% / 3.42%** | +0.4 / not found | +0.05 / 3.36 | +0.16 / 3.70 |
| Personal income m/m | **+0.24%** | +0.5 | +0.3 | +0.43 |
| Spending m/m (real) | **+0.86% (+0.6%)** | +0.8 | +0.1 (+0.1) | +0.16 |
| **Saving rate** | **4.1% (Aug)** | — | **4.6% (Jul)** | **3.0% (Jul)** |
| Q2 real GDP (3rd est.) SAAR | **2.2%** | not found | — | 2nd est. 1.5% |

⚠️ **Carry with it (HENRY's caveats):**
1. **Both releases carry BEA's annual update (revisions back to January 2021).** Any series CARL logged from the 9/29 vintage may have moved, and the saving rate moved the most: July was 3.0% on 9/29 and is 4.6% on 9/30.
2. **The core y/y "miss" (3.0 vs 3.3) is mostly revision**, because consensus sat on the old July vintage. The genuine surprise is the month: 0.25 vs 0.3.
3. Consensus figures are SECONDARY.

**Market reaction (HENRY, Treasury 9/30):** a dovish first move (Oct fed funds futures up; 10Y −1.7bp), then a **bear steepener by the close**: 2Y 4.88 (−1bp) · 10Y **5.29** (+3) · 30Y 5.64 (+5). **The 10Y close is the highest since 2002-05-14 (FRED DGS10).** HENRY: the cause of the long-end rise is UNATTRIBUTED. **October-hike odds 36%** [ZQX26 9/30 close, vendor bar, ±2pp] vs ~50% on 9/29 (`SIG-W-20260929-012`).
⚠️ **30Y "since 2002" is NOT supportable from FRED DGS30** (HENRY: the series has a 2002–2006 gap). `SIG-W-20260929-001` carried "5.613%, a 2002 high" as **CNBC's** claim; treat it as CNBC's, unverified.

**ACTION (CARL):** (1) re-base any saving-rate or income/spending figure you logged from the 9/29 vintage to the 9/30 vintage, because the annual update moved them. (2) Decide whether a 4.6% July / 4.1% August saving rate, instead of 3.0%, changes your consumer-cushion read before Friday's payrolls (`SIG-W-20260929-005`: a September payroll ≥ +150K fires LABOR's bull-side kill). Your call. $0.

**INFO (LIQUID):** rates and inflation backdrop; no ask. **INFO (RED):** via the BOARD; no registered trigger touched (RED-FT-08 keys on CPI).
