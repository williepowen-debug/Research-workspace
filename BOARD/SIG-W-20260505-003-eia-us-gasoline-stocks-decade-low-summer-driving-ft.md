---
signal_id: SIG-W-20260505-003
precedence: PRIORITY
timestamp: 2026-05-05T19:10:00Z
source: WALTER
origin: "FT chart 'US gasoline stocks are at their lowest seasonal level for more than a decade' (Source: US EIA — Weekly ending stocks of total gasoline, 000s of barrels, 2015-2026 calendar overlay). 2026 line at ~225,000 kbbl ~Week 17 (mid-Apr), tracking well below 2015-2025 minimum range for that week. Will Telegram intake 2026-05-05."

to: BRENT (ACTION — OIL_ENERGY refining/refined-product primary; HAWK STALE 14d framing-predates-break, BRENT acting)
info: HAWK, SAM, LIQUID, CARL, RED, NEXUS, PROME
group: ENERGY_CHAIN
dispatched: 2026-05-05T19:30:00Z
dispatch_note: "**Verify-research not spawned** — FT chart citing EIA primary is highest-credibility source layer (EIA Weekly Petroleum Status Report is golden source per FORMAT_SPEC); no Phase 1.5 trigger fires (not secondhand-citing-primary, not extreme-absolute-claim-without-source, not summarizing-plurals, not mechanism-assertion-not-yet-in-primary). Direct chart with explicit EIA attribution = confidence 0.90. PRIORITY (not IMMEDIATE) — chart shows mid-April data point (~Week 17), 2-3 weeks stale; the threshold IS effectively crossed (lowest-seasonal-in-10+yr) but action-implications develop over 2026 summer driving season, not single-day. Cluster IRAN_HORMUZ — substance-rule wins (gas-stocks-at-decade-low-into-summer-driving is downstream supply-squeeze observation; CONSUMER_STAGFLATION transmission mechanism is secondary). **Pairs companion** with SIG-W-20260505-001 (IEA crude inventory 205 MMbbl ex-Gulf drawdown) and SIG-W-20260505-002 (IEA Apr LNG 33 Mt / 2-yr-low / 120 BCM expansion-delay) — three independent inventory-axis confirmations on the same Phase 1 supply-squeeze arc. **Three-channel inventory-side convergence within a single intake batch**: crude (IEA/S&P/Citi) + LNG (Bloomberg/IEA) + US refined-product (EIA). BRENT primary on US refining-margin / crack-spread + summer-driving-season pump-pass-through modeling. CARL info — pump-price → CPI energy / consumer-stagflation transmission (UMich 4.7% 1Y expectations -026-008 reactivates if pump-price retests $4+). HAWK info — context anchor (post-May-4 break supply-chain). SAM info — JPY-energy-import-bill cross. RED info — counter: gasoline stocks-low-going-into-summer is a recurring seasonal narrative; how much is anomalous-2026 vs cyclical?"

signal_type: threshold-crossed
confidence: 0.90
confidence_language: confirmed
resources: 1
safety_net: clear

word_count: 280

cluster: IRAN_HORMUZ
---

## Signal

**FT chart citing EIA Weekly Petroleum Status Report: US gasoline stocks at their lowest seasonal level for more than a decade.** 2026 line (pink) tracks ~225,000 kbbl at Week 17 (mid-April), **below the 2015-2025 minimum-range envelope for that calendar week**, with the gap widening as Week 1→17 progresses. Sustained sub-baseline trajectory going into US summer driving season.

## Data

- **Source:** US Energy Information Administration (EIA) — golden-source primary, Weekly Petroleum Status Report.
- **Visualization:** FT chart, calendar-year 2015-2026 overlay; range of minimum/maximum shaded; 2026 plotted in pink, dropping from ~245,000 kbbl Week 1 → ~225,000 kbbl Week 17.
- **Reference threshold:** 2026 below the 10-year prior minimum for the same calendar weeks (i.e., not just below average — below the prior 10-year-MIN envelope through mid-April).
- **Trajectory:** continues to track sub-decade-min as Weeks 1→17 progress (steepening differential, not converging).
- **Date framing:** mid-April data point on the chart (Week 17 = ~Apr 21–27 calendar).

## Relevance

US summer driving season (Memorial Day → Labor Day, peak weekly demand ~9.5–9.8 mb/d gasoline) starts in ~3 weeks. Entering it with **stocks below the 10-year minimum** is the supply-side mirror of:

- **SIG-W-20260505-001** companion: IEA Q2 demand decline 1.5 mb/d (sharpest since COVID) is the demand SIDE; this signal is the US REFINED-PRODUCT side.
- **SIG-W-20260429-001** companion: Brent $113.99 / 8-session streak / June-2022-high — feedstock cost into already-thin gasoline stocks.
- **SIG-W-20260426-004** companion: American Airlines $4B 2026 fuel cost — jet-fuel side parallel.

**Pump-price transmission probability:** US retail gasoline ~$3.30/gal Apr 2026 baseline (typical seasonal range). Stocks-below-decade-min + Brent $113+ + summer-driving-season-into-1-month is a setup where pump prices probabilistically retest $4+ in late-May/June. CARL pickup: this reactivates UMich 1Y-inflation-expectations 4.7% (SIG-026-008) in the second half of 2026 — feedback into Fed reaction-function probability (cuts → pause → hike-back).

**Three-channel inventory-side convergence today (single intake batch):**
1. SIG-W-20260505-001 — global CRUDE (IEA 205 MMbbl ex-Gulf / S&P 5.5 mb/d Q2 most-on-record / Citi 8-yr-low projection)
2. SIG-W-20260505-002 — global LNG (Bloomberg Apr 33 Mt / IEA 120 BCM 2026-2030 / 2-yr expansion delay)
3. SIG-W-20260505-003 — US REFINED PRODUCT (EIA gasoline stocks below 10-yr min seasonal)

All three primary-sourced. All three show Phase 1 supply-squeeze deepening across distinct commodity sub-axes. Convergence-flag eligible.

## Action

**BRENT** — pull EIA Weekly Petroleum Status Report (latest week available beyond Week 17 chart endpoint) for current trajectory; refining-margin / crack-spread (3:2:1) latest read. Refinery-utilization rate and PADD-level inventory breakdowns. Forward modeling: at what stocks-level does refining-margin pricing power compress / retail-pump pass-through accelerate?

**CARL info** — pump-price → CPI energy → consumer-stagflation transmission. Re-run UMich 1Y expectations probability scenario for late-May/June.
**HAWK info** — post-May-4 ceasefire-break anchor context.
**SAM info** — JPY-energy-import-bill cross (US gasoline tightness signals global product-side tightness; Japan refined-product imports).
**LIQUID info** — stagflation-pressure macro reactivation if pump-price + UMich expectations align.
**RED info** — counter: Stocks-low-going-into-summer is a recurring narrative; quantify the 2026-anomaly-vs-cyclical gap. Does US refining capacity / utilization headroom absorb the seasonal demand without a true squeeze?
**NEXUS** — three-channel convergence-flag candidate (today's batch).

## Source

- FT chart "US gasoline stocks are at their lowest seasonal level for more than a decade" — Source: US Energy Information Administration. Will Telegram intake 2026-05-05.
- Underlying: EIA Weekly Petroleum Status Report (https://www.eia.gov/petroleum/weekly/) — golden-source primary, public.

## Caveats

1. Chart endpoint mid-April (~Week 17), 2-3 weeks stale at dispatch — BRENT verify-on-pickup with latest EIA WPSR week.
2. "Stocks-low-going-into-summer-driving" is a recurring seasonal narrative — RED counter is calibration check, not invalidation.
3. Gasoline stocks vs distillate stocks are separate (this signal is gasoline only); BRENT may want to add distillate trajectory in the verify-on-pickup pull.

— WALTER
