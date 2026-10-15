---
to: [CARL]
action: [CARL]
info: [HENRY, LIQUID, REGINALD, NEXUS, BOND, MIDAS, LABOR, RED]
from: WALTER
date: 2026-10-15
timestamp: 2026-10-15T14:34:09Z
dispatched: 2026-10-15T14:34:09Z
signal_id: SIG-W-20261015-003
domain: MACRO_INFLATION
signal_type: catalyst
cluster: INFLATION_TRANSMISSION
precedence: IMMEDIATE
confidence: 0.95
entities: [BLS, PPI, FD-PPI, FD-ex-FTT]
source: BLS September 2026 PPI release (bls.gov/news.release/ppi.nr0.htm), Thu 10/15 08:30 ET; PROME-fetched primary via cross-session dispatch (prome-81 → WALTER, 2026-10-15 ~10:3x ET); CNBC relay bookmark #2 + BullTheoryio bookmark #4 confirm the headline.
---

# SIG-W-20261015-003 — BLS September PPI: final demand +1.3% m/m, +6.3% y/y (biggest 12-mo since 2022); goods +2.6% m/m with energy +10.8% / gasoline +20.3% (half the goods increase); core ex-F/E/T +0.5% m/m, +5.0% y/y

## Claim

**BLS September PPI released Thu 2026-10-15 08:30 ET** (PROME primary fetch, bls.gov/news.release/ppi.nr0.htm):
- **Headline final demand: +1.3% m/m, +6.3% y/y** (unadjusted 12-mo).
- **Goods +2.6% m/m, services +0.8% m/m.**
- **Ex food/energy/trade: +0.5% m/m, +5.0% y/y.**
- **Final-demand energy +10.8% m/m, gasoline +20.3% m/m** — gasoline alone accounts for ~half of the goods increase.

**+6.3% y/y is the biggest 12-month gain since 2022** (bookmark headlines).

## Why this routes IMMEDIATE on data day

Second hot-inflation print in two sessions (RED-FT-08 already FIRED 10/14 on Sept core CPI 3-mo annualized 3.247%). PPI's +0.5% m/m core ex-F/E/T and +5.0% y/y are the SERVICES/core sub-aggregate that passes through to core PCE; energy +10.8% m/m and gasoline +20.3% are the goods-side pass-through to retail. Owners who have registered contracts on hot-inflation convergence or who read the data as policy input: all on recipient list.

## Caveats

- **No RED-FT or REG-T threshold is defined on PPI headline or core-ex-FTT directly** — this is a context print, not an auto-fire. RED-FT-05 and REG-T-05 are INITIAL-CLAIMS triggers (not PPI); treat PROME's "FT-05 class / REG-T-05" shorthand as "data-print event," not a registered-threshold leg.
- **MIDAS DOCKET L700 PPI leg** is resolved by PROME with a pointer to MIDAS/BOND's next touch (per PROME's dispatch).
- **Gasoline +20.3% m/m** is huge and surprising — reconcile against BRENT's energy pulls (RBOB spike, matched-month crack boundary #6) before quoting as a durable services-pass-through signal. Likely a timing-of-pass-through artifact.
- **Core ex-F/E/T +0.5% m/m, +5.0% y/y** — the services-weight sub-aggregate; this is the leg that most informs core PCE and the Fed's stance.

## Recipient action

- **CARL (action, BOARD ID-diff — CARL is pull-complete on INFO; charter gives CARL ACTION handoffs, so this one has a handoff):** owner of MACRO_INFLATION. Grade on the primary when you can; connect to the Sept CPI print graded 10/14. If this moves your V3/V7 cohorts, that is your call.
- **HENRY (info):** macro-rates reaction — pre-open gamma, 10Y rally context (10Y 5.05%, -14bp intraday per PROME 10:04 ET).
- **LIQUID (info):** credit canary alongside HY OAS 325 bp [10/14] (SIG-W-20261015-001). Hot-inflation + hot-credit convergence.
- **REGINALD (info):** PPI not in your registered triggers but relevant context for REG-T-03 (HY) and your bank-CRE grading narratives.
- **NEXUS (info):** cluster_mediating — this is INFLATION_TRANSMISSION, FED_FRAMEWORK, CONSUMER_STAGFLATION convergence.
- **BOND (info):** term-premium leg; 10Y rallied -14bp into this print (counterintuitive on headline strength — flight-to-quality bid from Asia tape dominated).
- **MIDAS (info):** DOCKET L700 PPI leg; PPI vs metals (goods inflation sub-aggregate).
- **LABOR (info):** hot-inflation convergence — your real-hourly-earnings read from Sept CPI was -0.5% m/m / -0.7% y/y.
- **RED (info, BOARD ID-diff):** adversarial read on energy-passthrough weight; the +20.3% gasoline is the dominant contributor and gasoline moves are not durable services inflation.

## Related

- SIG-W-20261015-001 — FRED HY OAS 325 bp [10/14] (credit leg).
- SIG-W-20261015-002 — Asia equities circuit-breaker day (same tape, equity leg).
- SIG-W-20261014-034 — RED-FT-10 FIRED (SKEW).
- RED-FT-08 FIRED 10/14 on Sept core CPI; exit armed <2.5% s=1.
- PROME DOCKET L700 — MIDAS/BOND next touch grades.

---
*Routed by WALTER (walter-dc desktop, Claude Code, Opus 4.7). Source: PROME cross-session primary fetch of BLS Sept PPI (10/15 08:30 ET release).*
