---
signal_id: "SIG-W-20261022-031"
date: "2026-10-22"
timestamp: "2026-10-22T20:26:29Z"
dispatched: "2026-10-22T20:26:29Z"
source: "X-BOOKMARK"
origin: "Will's X bookmark @Hedgeye 2026-10-22T12:56Z (id 2113253036013318277); verified via Reuters (Valetkevitch, Cooper) on live.euronext.com 10/22 and FORGE fetch.py"
domain: "EUROPE_MACRO"
cluster: "FED_FRAMEWORK"
cluster_secondary: "POSITIONING_VALUATION"
action: ["HANS"]
info: ["BOND", "LIQUID", "REGINALD", "HENRY", "RED", "PROME"]
precedence: "IMMEDIATE"
signal_type: "divergence"
confidence: 0.8
confidence_language: "Reuters levels are intraday secondary; HANS grades on ideal-investisseur; US close is vendor, FRED prints 10/23"
resources: 2
safety_net: "clear"
word_count: 470
entities: ["France", "OAT", "US-Treasury", "Moody's", "Meta", "Reuters", "Hedgeye", "VX-HANS-3.07", "HANS-T-10", "RED-FT-11"]
event_window: "closed"
dispatch_note: "EUROPE_MACRO sovereign-stress row (IMMEDIATE); BOND info under the row's time-critical limb. Not a registered-threshold fire graded by WALTER: HANS owns T-10 and VX-HANS-3.07 on its own basis."
---
# France's 10-year yield rose to about 5.06% (touched 5.14%, highest since July 2002) and moved ABOVE the US 10-year for the first time since 2013, on the same day the US 10-year fell about 18bp to below 5% in a flight to safety from the AI-stock selloff. France is now through HANS's 5.00% red tier the day before Moody's reviews France

**What happened (Reuters, Valetkevitch and Cooper, 10/22, intraday):** "France's 10-year government bond yields rose above those of equivalent US Treasuries for the first time since 2013." France's 10-year was "up 6.5 basis points at 5.06%, after earlier touching 5.1415%, its highest level since July 2002." The US 10-year was "down 15.17 basis points at 4.994%, from 5.146%", below 5% "for the first time since September 23"; Reuters ties the US fall to "equity declines related to the sustainability of the AI outlook" (Meta's non-voting stock plan, already routed in SIG-W-20261022-006 and SIG-W-20261021-015).

| Series | Level | Basis |
|---|---|---|
| US 10-year | 4.95% (−3.75%, about −19bp) | vendor ^TNX after the close, 20:19Z 10/22 |
| US 10-year, prior | 5.13% [10/21] | FRED DGS10 first-published; 10/22 prints tomorrow |
| US 5-year / 30-year | 4.77% (−4.1%) / 5.29% (−2.8%) | vendor ^FVX / ^TYX, same pull; TLT +1.87% |
| France 10-year | 5.06%, intraday high 5.1415% | Reuters, secondary; HANS's last graded value 4.99 [i-i 10/21] |

**Why it matters, per desk:**
- **HANS ACTION:** your `VX-HANS-3.07` red tier is OAT 5.00 and your STATUS had OAT 1bp under it [10/21]; `HANS-T-10` is open and deepening, and **Moody's reviews France on Friday 10/23** (your own STATUS). Grade 10/22 on the ideal-investisseur basis; WALTER has not graded it. The crossover above US yields comes from **both legs**: about 70% of the 21.7bp swing is the US rally (−15.2bp) and 30% the French rise (+6.5bp), on Reuters’ figures, so it is not on its own a measure of French stress.
- **BOND (info, time-critical limb of the row):** an about 19bp one-day fall in the US 10-year and about 20bp in the 5-year, read by Reuters as safe-haven buying.
- **LIQUID, REGINALD (info):** HANS asked LIQUID on 10/21 whether the wider French spread shows on the US-funding side; French bank stocks reportedly sold off with French bonds (HANS, secondary). Lower US yields ease the 10-year-into-CRE-refinancing channel CREED and REGINALD named in 012/015, for one day.
- **HENRY (info):** stocks down and Treasuries up on the same day; VIX 18.90 (+13.3%) at the close, no safety net.
- **RED (by BOARD):** `RED-FT-11` (US 30-year 5-session fall of at least 10.2bp) is a conditional classifier; the 10/22 FRED DGS30 print tomorrow may meet its window again. RED classifies; WALTER does not.

**Do not relay as:** "France is now riskier than the US" (the crossover is mostly the US rally), or "OAT closed at 5.06%" (an intraday Reuters level; HANS's basis governs). "First time since 2013" is Reuters' claim, not checked against a series by WALTER. No trade is implied.
