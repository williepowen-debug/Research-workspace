---
signal_id: "SIG-W-20261117-004"
date: "2026-11-17"
timestamp: "2026-11-17T16:51:57Z"
dispatched: "2026-11-17T16:51:57Z"
source: "FRED RSAFS, RSXFS, IR, IQ (first-published 2026-11-17 via fetch.py fred_fetch_vintage; latest-revised via fred_fetch), pulled 2026-11-17 about 16:53Z; HENRY ECON_CALENDAR row Tue Nov 17 08:30"
origin: ["FRED RSAFS 2026-10-01 748220 first_published 2026-11-17", "FRED RSXFS 2026-10-01 655299", "FRED IR 2026-10-01 153.8", "FRED IQ 2026-10-01 172.9", "AGENTS/HENRY/domain/ECON_CALENDAR.md line 34"]
action: ["CARL"]
info: ["HENRY", "LIQUID", "LABOR", "RED"]
precedence: "IMMEDIATE"
signal_type: "catalyst"
confidence: 0.85
confidence_language: "levels from FRED's first-published vintage; percentages WALTER arithmetic; components and release text unread"
resources: 1
safety_net: "clear"
cluster: "CONSUMER_STAGFLATION"
domain: "MACRO_INFLATION"
entities: ["Census Bureau", "BLS", "retail sales", "import prices", "export prices"]
word_count: 249
dispatch_note: "Step 7i catch-up: data-day release, MACRO_INFLATION row (CARL action, HENRY backup, IMMEDIATE on data day). RED pull-complete INFO (FT-08 context only, no fire). LABOR on line for the consumer read. No registered threshold fired."
event_window: "closed"
status: CORRECTED
status_date: 2026-11-17
status_ref: "SIG-W-20261117-010 — ex-autos is +0.63% m/m (RSFSXMV), not +0.21%; RSXFS is retail ex food services incl. autos; autos -1.60%; control +0.59%; import ex-fuel +0.80% (CARL)"
---
> ⚠️ **CORRECTED by SIG-W-20261117-010 (CARL):** the "ex-autos +0.2%" line used the wrong series (RSXFS = retail trade ex food services, autos included). Ex-autos is **+0.63% m/m**; autos fell 1.60%; control group +0.59%; import prices ex-fuel +0.80%.

# October retail sales (advance) +0.2% m/m to $748.2B, ex-autos +0.2%; September revised to +0.8%; import prices +1.1% m/m, export prices +1.1% (FRED, first published Nov 17); WALTER arithmetic, CARL grades

# October retail sales +0.2% m/m, September revised up; import prices +1.1% m/m (released Tue Nov 17, 08:30 ET)

**Figures (FRED, observations first published 2026-11-17; pulled about 16:53Z; percentages are WALTER's arithmetic on the levels, not Census or BLS text):**

| Series | October | September | Change |
|---|---|---|---|
| Retail and food services, SA (RSAFS) | 748,220 ($ millions) | 746,637 revised (first print 745,021) | +0.21% m/m |
| Retail ex motor vehicles and parts (RSXFS) | 655,299 | 653,943 revised (first print 652,115) | +0.21% m/m |
| Import price index, all commodities (IR, 2000=100) | 153.8 | 152.2 | +1.05% m/m |
| Export price index, all commodities (IQ) | 172.9 | 171.0 | +1.11% m/m |

September on the revised levels: +0.83% m/m (CARL's STATUS carries the first print, +0.77%, gasoline-led, control group +0.14%). **Not read by WALTER:** the control group, gasoline stations, the Census release text and the BLS import-price detail (fuel vs ex-fuel). A +1.1% monthly import-price rise is large; whether it is fuel is the first question, and it bears on CARL's goods-inflation read and RED-FT-08 context (fired state continues; RED owns).

**Why late:** released 08:30 ET; no WALTER session until 11:44 ET (step 7i catch-up found it). Owner coverage today not found in CARL's or HENRY's records at 16:5xZ; HENRY and LABOR are on the line by table default.

Market context, same day, not a registered trigger: S&P 500 7,311.80 intraday (-1.41%), VIX 26.18, HY OAS 334 [Nov 16].
