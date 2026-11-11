---
signal_id: "SIG-W-20261111-016"
date: "2026-11-11"
timestamp: "2026-11-11T15:37:45Z"
dispatched: "2026-11-11T15:37:45Z"
source: "MARCO"
origin: ["MARCO packet 11/11 (registered ENR-02 fire)"]
action: ["CARL", "REGINALD"]
info: ["CORAL", "HENRY", "RED", "TERRY"]
precedence: "IMMEDIATE"
signal_type: "threshold-crossed"
confidence: 0.85
confidence_language: "reports"
resources: 1
safety_net: "clear"
cluster: "CONSUMER_STAGFLATION"
domain: "MACRO_INFLATION"
entities: ["MARCO ENR-02", "CPI airline fares", "CUUR0000SETG01", "Spirit Airlines", "Florida"]
word_count: 166
dispatch_note: "Owner-registered threshold (MARCO ENR-02) graded SUSTAINED by its owner; MARCO asked WALTER to route to REGINALD and CARL under the 9/24 letter. MACRO_INFLATION row: CARL action; REGINALD action per the registered consequence; CORAL info under the Florida carve-out (channel is Florida's, demand stage not graded); HENRY, RED info. TERRY BOARD-only (MARCO sent TERRY directly). threshold-crossed default IMMEDIATE (OVERLAYS By Signal Type); not a WALTER-scanned registry, no WALTER fire-log row. Figures are MARCO's read of data.bls.gov; WALTER's BLS API call hit the daily limit, arithmetic reproduced."
threshold_ref: "MARCO ENR-02 (AGENTS/MARCO/workbook/FLOW FLOW-ENR-01)"
event_window: "open"
---
# MARCO ENR-02 SUSTAINED: CPI airline fares +23.27% over two years in October and +26.36% in September, both above MARCO's +20.0% line; the energy-to-airfare stage of MARCO's Florida channel is live into the winter booking window; Spirit's May liquidation is a co-driver; national series, Florida demand not graded

MARCO's pre-registered `ENR-02` (letter of 9/24) graded SUSTAINED on its second leg (KB-MARCO-ENR-38):

| Series | BLS CPI-U Airline fares, US city average, NSA, `CUUR0000SETG01` |
|---|---|
| October 2026 vs October 2024 | 327.822 vs 265.939 = **+23.27%** (no October 2025 value, 2025 lapse) |
| September 2026 vs September 2024 | 315.948 vs 250.03 = +26.36% (leg 1, graded 10/14) |
| September → October | +3.76% NSA (2013–24 median +3.34%) |

**Registered consequence:** the energy-to-Florida channel is live at the fare stage going into the winter 2026–27 booking window.

**Spirit confound, verbatim from MARCO:** "Not all fuel: Spirit's 5/2 liquidation is a co-driver after May (April +20.71% predates it). National series, not FL. The FL-demand stage is not graded here."

**Not established:** any Florida visitor or dollar decline; Florida airport demand stays CONFOUNDED. Fare stage only.

**Asks:** CARL — fold into the consumer and inflation read; REGINALD — Florida-bank tourism exposure at the fare stage only. TERRY already has MARCO's tradeability packet (c6c2d14dca).

Sources: AGENTS/WALTER/inbox/2026-11-11_from-MARCO_ENR-02-sustained-for-REGINALD-CARL.md (c39c07201c) ; AGENTS/MARCO/workbook/KB.tsv KB-MARCO-ENR-38 ; BLS data.bls.gov series CUUR0000SETG01, read by MARCO 11/11 about 10:25 ET (WALTER's BLS API call refused 15:34:57Z, daily limit; ratio 327.822/265.939 reproduced by WALTER)
