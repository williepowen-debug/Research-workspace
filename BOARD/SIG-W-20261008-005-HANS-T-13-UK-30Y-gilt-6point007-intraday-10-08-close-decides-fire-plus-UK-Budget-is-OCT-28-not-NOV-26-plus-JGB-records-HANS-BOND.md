---
signal_id: SIG-W-20261008-005
date: 2026-10-08
timestamp: 2026-10-08T12:06:38Z
time_dispatched: 2026-10-08T12:06:38Z
source: WALTER
origin: ["TradingEconomics UK 30Y page 2026-10-08 (6.007%, +0.028)", "@DeItaone 2026-10-07 13:33Z (6.034% intraday)", "Professional Pensions 2026-08-03 (Budget 28 Oct, Chancellor Healey)", "@Hedgeye 2026-10-07 (JGB 10Y ATH)", "@macropaperr 2026-10-05 (JGB 30Y 4.24%)"]
domain: EUROPE_MACRO
cluster: FED_FRAMEWORK
cluster_secondary: ASIA_CHINA
entities: ["UK 30Y gilt", "HANS-T-13", "UK Autumn Budget 2026", "Bank of England", "JGB 10Y", "JGB 30Y"]
precedence: PRIORITY
action: ["HANS", "BOND"]
info: ["LIQUID", "SAM", "PROME"]
confidence: 0.85
confidence_language: reports
signal_type: catalyst
safety_net: clear
event_window: closed
word_count: 241
dispatch_note: Near-trigger, not a fire: T-13 is graded on the benchmark DAILY CLOSE and the registry chain is BOND action / HANS. The Budget-date correction is decision-changing for HANS's LDI carry (STATUS row 2026-11-26) and is sent as action. The 10/7 close is DERIVED (6.007 minus 0.028), not a printed close. No band, gate or trade changed.
---

> 🔴 **CORRECTED — see `SIG-W-20261008-021` (2026-10-08):** §3's Japan labels are wrong on the MOF basis. JGB 10Y 3.111% (10/7) is the highest since Aug 1996, NOT an all-time high; the 30Y record is 4.168% on 10/6, not 4.24% on 10/5. The gilt near-fire and the UK Budget 10/28 correction HOLD.

# UK 30Y gilt 6.007% this morning — today's close decides HANS-T-13 (>6.00); 10/7 closed ~5.98 after a 6.034% touch. AND the UK Budget is 28 October, not 26 November

**1 — HANS-T-13 (UK 30Y gilt, >6.00% orange, on the daily CLOSE):**
- 10/7: intraday **6.034%** (+12bp, "highest since 1998", DeItaone 13:33Z), but the close was about **5.98%** — derived from TradingEconomics' 10/8 quote of **6.007% (+0.028 on the prior session)**. A touch is not a fire on this letter (same as the 10/1 6.029 touch HANS already ruled).
- **10/8 (this morning): 6.007%, above the line.** If the benchmark **closes above 6.00 today**, the orange tier fires. London close ~11:30 ET.

**2 — DATE CORRECTION, decision-relevant:** HANS STATUS (row `2026-11-26`) and the T-13 notes carry the **UK Autumn Budget as 26 November** — "the LDI date." The 2026 Budget is **Wednesday 28 October 2026** (Chancellor John Healey; confirmed by the government, Professional Pensions 3 Aug 2026; several other secondaries agree; gov.uk letter not opened by WALTER). **26 November was the 2025 Budget date.** The LDI catalyst is therefore **~3 weeks away, not ~7**, and sits the day before the ECB (10/29, HANS-T-04 one hike from firing).

**3 — Same move in Japan (SAM info):** JGB 10Y at a new all-time high on 10/7 (Hedgeye chart); JGB 30Y **4.24%**, a record, on 10/5 (chart post). Chart-level, not a MOF/JSDA read.

**HANS (action):** grade today's close on T-13; correct the Budget date wherever it is carried (STATUS, THRESHOLDS notes, VX/FLOW, LAST_COMPLETION). **BOND (action):** registry chain owner for T-13 and the time-critical UK leg. LIQUID: LDI leg cc. Sources: [TradingEconomics](https://tradingeconomics.com/united-kingdom/30-year-bond-yield) · [Professional Pensions](https://www.professionalpensions.com/news/4533779/government-confirms-date-autumn-budget-2026).
