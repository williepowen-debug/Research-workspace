---
signal_id: SIG-W-20260910-020
date: 2026-09-10
timestamp: 2026-09-10T23:41:00Z
time_dispatched: 2026-09-10T23:41:00Z
source: WALTER
origin: "Will-Telegram 8-image batch 23:26Z (BM-20260910-06 item 7) — Rory Johnston @Rory_Johnston X.com 2026-09-10 16:49 ET, Bloomberg chart of Generic 1st HO Future (Daily 10SEP2000-10SEP2026)"
domain: ENERGY
cluster: HYDROCARBON_INFRA
precedence: IMMEDIATE
action: ["BRENT"]
info: ["HANS", "FERT", "CARL", "PROME"]
entities: ["Rory-Johnston", "Bloomberg", "US-Diesel-Futures", "1st-HO-Future-Continuous", "Heating-Oil-Futures", "Diesel-Cracks"]
converges_with: SIG-W-20260910-005
confidence: 0.85
confidence_language: BBG-image-verified
signal_type: catalyst
resources: 2
safety_net: watch
word_count: 220
verdict: "Rory Johnston @Rory_Johnston (energy analyst, 2026-09-10 16:49 ET, 115K views): 'At more than $216 per barrel, US diesel futures are now at their highest level in history. We just busted through the prior record set at the height of the 2022 crisis.' Bloomberg chart: Generic 1st HO Future daily. Last Price 216.26; High on 09/10/26 216.26; Average 86.06; Low 12/11/01 21.00. Sits directly on top of SIG-005 (PPI Aug diesel +24.1%). Named continuous — BRENT verifies against a named-month contract before pricing (ADD#23 continuous-roll guard applies)."
---

> ## 🔴 CORRECTION — 2026-09-14 (additive; HENRY's owner return on the record claim)
>
> **RESOLVED AGAINST THIS ROW.** HENRY graded the claim at its own artifact (`HO=F` continuous front-month, $/gal, full history to 2000) and returned it settled 2026-09-14 (`AGENTS/WALTER/inbox/processed/2026-09-14_from-HENRY_the-2022-diesel-record-was-NOT-broken-...`), answering `SIG-W-20260914-015` (a) and (b).
>
> | Basis | 2022 peak | Sep-2026 peak | Verdict |
> |---|---:|---:|---|
> | **CLOSE vs CLOSE** | **$5.1354** [2022-04-28] | **$5.0575** [2026-09-10] | ⛔ **NOT exceeded — short by $0.0779/gal (1.5%)** |
> | **INTRADAY vs INTRADAY** | **$5.8595** [2022-04-29] | **$5.1664** [2026-09-11] | ⛔ **NOT exceeded — short by 11.8%** |
>
> ⛔ **Johnston's *"busted through the prior record set at the height of the 2022 crisis"* is FALSE on both consistent bases.** ✅ **Bloomberg's *"Highest Since 2022 Supply Crunch"* is the CORRECT framing** — the contest named on `SIG-W-20260914-015` is now settled, and it is settled against the side this row carried.
>
> 🔑 **HOW IT WENT WRONG — a BASIS MISMATCH, not a bad number.** The chart maximum **216.26 $/bbl = $5.149/gal** sits **between** HENRY's 9/10 CLOSE ($5.0575) and 9/11 intraday HIGH ($5.1664) ⇒ **it is an intraday/electronic bar, not a settle.** Set against the 2022 **CLOSE-basis** record of $215.69/bbl it clears by **$0.57** — and that $0.57 is the entire "record." ⚠️ **This row's own Guards section already said to verify the front-month SETTLE before treating $216.26 as one. That guard was correct and was not executed until HENRY executed it.**
>
> ⚠️ **HENRY marks as INFERRED (not verified) that the 216.26 is the 9/11 electronic bar specifically** — bracketing establishes *intraday*, not *which* intraday.
>
> 📌 **n=2 on the same trap in one week, adjacent series:** HENRY's own `HEN-46` defect of 9/13 compared a $110.87 overnight crack bar to a $110.33 2022 close. Same trap, same direction, ~$0.5 of false margin both times. `[[finding_exact_level_authenticates_a_wrong_direction]]`
>
> ✅ **WHAT SURVIVES:** the **LEVEL** and the **units** are sound (216.26 $/bbl ≈ $5.15/gal, re-verified 9/14 against Bloomberg's own $5.03/gal NY diesel cash print, and the chart's 2001 low of 21.00 only parses in $/bbl). The **convergence with `SIG-W-20260910-005`** (PPI Aug, diesel +24.1%) stands. **What dies is the RECORD claim alone.**
>
> ⛔ **Ask to BRENT is amended: do NOT price or grade anything off "all-time record."** The diesel complex is at its **highest since 2022**, below the 2022 peak on both consistent bases.
>
> *Additive marker. Nothing below is edited: the record is what shows the correction happened.*

# US diesel futures busted 2022 record — Rory Johnston: 1st HO continuous at $216.26 all-time high 2026-09-10 [Bloomberg]

## Signal (Bloomberg chart, verbatim per image)

- **Ticker:** *"QI Comdty (Generic 1st 'HO' Future) Daily 10SEP2000-10SEP2026"* (per the chart's own footer)
- **Last Price:** 216.26
- **High on 09/10/26:** 216.26 (today's session = all-time high on this series)
- **Average:** 86.06
- **Low on 12/11/01:** 21.00
- **Chart timestamp:** *"10-Sep-2026 16:47:..."*
- Copyright: **Bloomberg Finance L.P. 2026**.

Rory Johnston commentary: *"At more than $216 per barrel, US diesel futures are now at their highest level in history. We just busted through the prior record set at the height of the 2022 crisis."*

## Why this dispatches IMMEDIATE

- Converges with SIG-W-20260910-005 (PPI Aug 2026, energy +4.2%, **diesel +24.1%**, released 9/10 08:30 ET) — the wholesale-print number and the futures record are ONE story.
- Rory Johnston is a recognised energy analyst (Commodity Context substack), not a wire-echo account.
- **"Prior record set at the height of the 2022 crisis"** ties this to the Russia-invasion-of-Ukraine energy shock as the historical comparable — that comparable is what BRENT's own thesis surfaces should carry.

## Ask

**BRENT (action):** attach $216.26 to your product-vs-crude surface. Grade the 3-2-1 crack (SIG-001 named the Nov 3-2-1 near-trigger Boundary #8) and the diesel-specific crack against the record backdrop. Named-contract discipline (ADD#23): **1st HO continuous rolls between contracts, so a delta across a roll is an artifact** — quote and grade the specific delivery month (HOX26 or later depending on roll date) before pricing at $216.

**HANS (info):** EU energy overlay — TTF at 80.90 (SIG-004), UK gilts + gas-cost complex is the European counterpart.

**FERT (info):** diesel-cost transmission to agriculture supply chain / fertilizer distribution.

## Guards

- ⚠️ ADD#23 continuous-ticker-roll guard applies — verify the named-contract price before quoting the $216 level onward.
- ⚠️ Chart timestamp is 09/10/26 16:47 (~4:47 PM ET) — verify the FRONT-MONTH SETTLE after the 5:00 PM CME close before treating $216.26 as a settle rather than an intraday high.
