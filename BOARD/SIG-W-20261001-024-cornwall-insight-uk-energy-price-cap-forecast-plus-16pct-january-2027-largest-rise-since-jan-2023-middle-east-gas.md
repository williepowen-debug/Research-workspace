---
signal_id: SIG-W-20261001-024
date: 2026-10-01
timestamp: 2026-10-01T18:33:30Z
time_dispatched: 2026-10-01T18:33:30Z
timestamp_note: "stamped from the wall clock in the same process as the write (MEMORY #34)"
source: RESEARCH-INTAKE 2026-09-30 RSS batch (BBC Business 14:36Z headline), triaged in the CATO bounded comparison; batch manifest BM-20261001-06 item 4
origin: ["BBC Business 2026-09-30 14:36Z headline: Household energy bills forecast to see biggest rise in four years (BBC not fetchable)", "Cornwall Insight press release 2026-09-30: 16% price cap rise forecast in January (PRIMARY, read)", "ITV 2026-09-30 (headline); Yahoo/Reuters 'Britain's energy price cap to rise 16% in January, Cornwall Insight says' (headline)"]
domain: EUROPE_MACRO
cluster: INFLATION_TRANSMISSION
cluster_secondary: IRAN_HORMUZ
entities: ["Cornwall Insight", "Ofgem", "United Kingdom", "energy price cap", "Strait of Hormuz"]
confidence: 0.85
confidence_language: "A consultancy FORECAST, read at its primary. Not an Ofgem decision: the January cap is announced by Ofgem later; the observation window was about half complete at publication."
signal_type: pattern-match
safety_net: clear
verdict: "Cornwall Insight forecast on 9/30 that the UK default tariff cap will rise 16% in January 2027 to 1,999.28 GBP a year for a typical dual-fuel household, up 276 GBP from October, the largest rise since January 2023. It attributes the rise mainly to Middle East disruption of gas supply, with EU storage ~65% full in early September. About half of Ofgem's observation window had passed, so September's wholesale rises are 'already locked in, making a January increase all but certain'. The size still depends on how the US-Iran conflict develops."
precedence: PRIORITY
action: ["HANS"]
info: ["BOND", "LIQUID"]
dispatch_note: "Lane omission found in the CATO comparison (BBC headline, plain NEW, never surfaced); 0 hits on BOARD 9/20-10/01. EUROPE_MACRO carve-out: HANS action (UK household energy -> UK headline CPI and the BoE path; note HANS-T-17 is UK CORE CPI, which EXCLUDES energy, so no registered HANS band is graded by this). Info: BOND (gilts; HANS carve-out backup), LIQUID (carve-out info). REGINALD and CARL dropped from the carve-out info line: no US bank or US consumer channel. INFLATION_TRANSMISSION primary (cost-push to CPI), IRAN_HORMUZ secondary (mechanism = Hormuz gas disruption, per the geography-vs-mechanism rule)."
---

# UK energy bills forecast to jump 16% in January, the biggest rise since January 2023, on Middle East gas disruption.

- **Forecast (Cornwall Insight, 9/30, primary):** the January 2027 price cap rises **16% to £1,999.28 a year** for a typical dual-fuel household, **+£276** vs October. The **largest rise since January 2023.**
- **Why:** Middle East conflict disrupting gas supply; EU storage **~65% full in early September**, well below normal.
- **How firm:** Ofgem's observation window was about half done, so September's price rises are *"already locked in, making a January increase all but certain."*
- **Swing factor:** the size depends on how the US-Iran conflict develops. Even an immediate end would leave the disruption and the already-captured prices in place through Q1 2027.

**So what:** a scheduled +16% household energy step in January feeds UK headline inflation and the BoE's path. It is the Hormuz gas shock reaching European households.

## Caveats
- A **consultancy forecast, not an Ofgem decision.**
- UK **core** CPI (HANS-T-17) excludes energy, so no HANS band is graded by this directly.
- BBC original not fetchable; figures are from the Cornwall Insight release itself.

Action HANS: fold the January energy step into your UK inflation and BoE read. Canon: HANS.
