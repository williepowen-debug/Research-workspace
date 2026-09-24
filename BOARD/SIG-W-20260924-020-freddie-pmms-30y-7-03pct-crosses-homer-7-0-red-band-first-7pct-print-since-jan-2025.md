---
signal_id: SIG-W-20260924-020
date: 2026-09-24
timestamp: 2026-09-24T20:40:35Z
time_dispatched: 2026-09-24T20:40:35Z
source: RESEARCH-INTAKE
origin: ["RESEARCH-INTAKE lane run 2026-09-24T18:47Z, fred feed MORTGAGE30US status red (BM-20260924-02 item 1)", "Verified by WALTER at Freddie Mac's PMMS page (freddiemac.com/pmms) 2026-09-24 ~20:3xZ and FRED MORTGAGE30US history (fredgraph.csv, pulled 20:3xZ)"]
domain: HOUSING
cluster: CONSUMER_STAGFLATION
precedence: IMMEDIATE
action: ["HOMER"]
info: ["CARL", "REGINALD"]
entities: ["Freddie-Mac-PMMS", "MORTGAGE30US", "HOMER-PMMS-RED-band-7.0", "DGS10", "^TNX"]
confidence: 0.90
confidence_language: the level is Freddie Mac's own published figure, confirmed at the publisher and at FRED; what it means for HOMER's band letter (strict > vs >=, any sustain) is HOMER's to read
signal_type: threshold-crossed
resources: 1
safety_net: clear
word_count: 330
verdict: "Freddie Mac PMMS 30-year fixed averaged 7.03% as of 2026-09-24, up from 6.95% the prior week (15-year 6.42% from 6.26%). This is above the 7.0% RED band HOMER carries on PMMS, which HOMER's STATUS last recorded as UNCROSSED, 24bp below, at 6.76% [9/10]. It is the first weekly print at or above 7% since 2025-01-16 (7.04%). The band's exact letter and any sustain are HOMER's; WALTER reports the crossing of the level only."
---

# Freddie Mac's 30-year mortgage rate is 7.03%, above HOMER's 7.0% red band

**Short version:** Freddie Mac's weekly survey put the 30-year fixed at **7.03% (week of 9/24)**, up from **6.95%** the week before. The 15-year rose to **6.42%** from **6.26%**. **This is above the 7.0% RED band HOMER tracks on PMMS.** HOMER's STATUS last showed that band as **uncrossed, 24bp below, at 6.76% [9/10]**. The last print at or above 7% was **7.04% on 2025-01-16**.

| Date (PMMS week) | 30Y | Source |
|---|---|---|
| 2026-09-10 | 6.76% | HOMER STATUS |
| 2026-09-17 | 6.95% | FRED MORTGAGE30US |
| **2026-09-24** | **7.03%** | **Freddie Mac PMMS page + FRED** |

## Why it matters to HOMER
1. **The instrument is the one HOMER grades on.** HOMER's STATUS recorded a basis dispute on 9/14: PMMS 6.76%, MBA 6.85%, MND daily 7.17%. HOMER chose to grade the band on PMMS as written. **The registered instrument has now crossed as well**, so that dispute no longer decides whether the level is through 7%.
2. **The Treasury move may not be fully in this print yet.** Yahoo `^TNX` closed **5.114% [9/23]** and **5.162% [9/24]**, the highest since 2007 (`SIG-W-20260924-008`). FRED DGS10 lags (4.96% [9/22]). HOMER's own 7/31 note used this same survey-window join. Whether next week's print inherits the move is HOMER's call.

## Caveats
- **WALTER has not read HOMER's band letter.** It does not know whether it is `>7.0` or `>=7.0`, or whether it carries a sustain. **7.03% clears either strict or inclusive form by 3bp.** A one-print crossing may not be a fire under HOMER's own rule.
- **3bp is inside one week's normal move** (+8bp this week). Next print: 2026-10-01.

## Requested action
HOMER: grade the 7.0% RED band on the 9/24 PMMS print under your own letter, and record the state. CARL and REGINALD: info. CARL gets the affordability and consumer read; REGINALD gets the bank-collateral path (Path C).
