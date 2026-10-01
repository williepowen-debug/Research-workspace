---
signal_id: SIG-W-20261001-025
date: 2026-10-01
timestamp: 2026-10-01T20:45:42Z
time_dispatched: 2026-10-01T20:45:42Z
timestamp_note: stamped from `date -u` at write, not typed
source: Will-Telegram
origin: ["Will via Telegram 2026-10-01T20:43:40Z (msg 4845): FT post x.com/FT/status/2105745683613430037, posted 2026-10-01T19:44:28Z, 'US mortgage rates jump the most in four years as bond sell-off hits Main Street' (text read via the fxtwitter mirror; FT article body NOT read, paywalled)", "Verified by WALTER at Freddie Mac's PMMS page (freddiemac.com/pmms, fetched ~20:4xZ: 7.28%, October 1, 2026) and FRED MORTGAGE30US history (fredgraph.csv, pulled ~20:4xZ)"]
domain: HOUSING
cluster: CONSUMER_STAGFLATION
cluster_secondary: FED_FRAMEWORK
entities: ["Freddie-Mac-PMMS", "MORTGAGE30US", "HOMER-PMMS-RED-band-7.0", "HOMER-PMMS-2026-10-01-PRE-REGISTRATION", "DGS10"]
confidence: 0.90
confidence_language: the level and the weekly change are Freddie Mac's own published figures, confirmed at the publisher and FRED; the 'largest since' rank is WALTER's computation on FRED's weekly history; the grade of HOMER's pre-registration is HOMER's
signal_type: threshold-crossed
safety_net: clear
verdict: "Freddie Mac PMMS 30-year fixed averaged 7.28% on 2026-10-01, up from 7.03% on 9/24. That +25bp is the largest weekly rise since 2022-10-13 (+26bp) and the level is the highest since 2023-11-22 (7.29%). It falls in HOMER's pre-registered HOLD state (>=7.05%). It is about 5-7bp above HOMER's own Treasury-implied value, inside HOMER's 10bp residual tolerance."
precedence: PRIORITY
action: ["HOMER"]
info: ["CARL", "REGINALD"]
dispatch_note: "Second print above HOMER's 7.0% RED band; resolves HOMER's 9/29 pre-registration. No new band crossed (HOMER's ladder has no rung above RED). PRIORITY, not IMMEDIATE: the state did not change, the speed did. CARL is pull-complete for INFO (no handoff)."
---

# Freddie Mac's 30-year mortgage rate is 7.28%, up 25bp in a week, the biggest jump since October 2022

**Short version:** Freddie Mac's weekly survey put the 30-year fixed at **7.28% (week of 10/01)**, up from **7.03%** on 9/24. **+25bp is the largest one-week rise since 2022-10-13 (+26bp).** The level is the highest since **2023-11-22 (7.29%)**. This is the print HOMER pre-registered on 9/29, and it lands in **HOLD (≥7.05%)**: RED band, second print above the line.

| PMMS week | 30Y | Weekly change | Source |
|---|---|---|---|
| 2026-09-03 | 6.71% | | FRED MORTGAGE30US |
| 2026-09-10 | 6.76% | +5bp | FRED |
| 2026-09-17 | 6.95% | +19bp | FRED |
| 2026-09-24 | 7.03% | +8bp | FRED (`SIG-W-20260924-020`) |
| **2026-10-01** | **7.28%** | **+25bp** | **Freddie Mac PMMS page + FRED** |

Four weeks: **+57bp**.

## Against HOMER's pre-registration (`AGENTS/HOMER/reports/2026-09-29_PMMS-2026-10-01_PRE-REGISTRATION.md`)
1. **State: HOLD (≥7.05%).** HOMER fixed this before the print: "RED, second print above the line." The 9/24 caveat that 3bp sat inside one week's move is the one HOMER said would retire on HOLD. Retiring it is HOMER's call.
2. **Residual diagnostic (HOMER's §3.1, computed by WALTER, HOMER to confirm):** HOMER's formula is the Wednesday 10Y plus 1.92–1.94. FRED **DGS10 = 5.29% [9/30]** implies **~7.21–7.23%**. The residual is **+5 to +7bp**, inside HOMER's 10bp line, so the move still reads as Treasury-driven. ⚠️ HOMER's input is the Treasury daily par-curve CSV. DGS10 is the same H.15 constant-maturity series, but WALTER did not open the Treasury CSV.
3. **Year check (HOMER's §3.2):** the Freddie Mac page reads **October 1, 2026**.
4. **15-year:** reported, not graded: **6.60%, up from 6.42%** (Freddie Mac page text). A year earlier the 30-year was **6.34%**.

## Caveats
- **The 'largest since' rank is WALTER's arithmetic on FRED's weekly series**, not a Freddie Mac statement. It agrees with the FT headline ("most in four years").
- ⚠️ **The comparison crosses a method change.** On **2022-11-17** Freddie Mac switched PMMS from a lender survey to Loan Product Advisor application data (stated on the PMMS page). The +26bp comparator on 2022-10-13 is from the old method. **Under the current method, +25bp is the largest weekly rise in the series' history.** The two methods are not strictly comparable week to week.
- **The FT article body was not read** (paywall). Only its headline and dek reached WALTER, through a mirror of the post. Nothing here relies on the FT beyond the headline.
- HOMER's ladder has **no rung above RED**, so this print crosses no new line. What changed is the speed.

## Requested action
HOMER: grade the 10/01 print against your 9/29 pre-registration, confirm or correct the residual with your own Treasury input, and record the state. CARL and REGINALD: information only. CARL gets the affordability read, REGINALD the bank-collateral path.
