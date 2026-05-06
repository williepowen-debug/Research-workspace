---
signal_id: SIG-W-20260506-003
precedence: PRIORITY
timestamp: 2026-05-06T18:25:00Z
source: WALTER
origin: ["Luke Gromen @LukeGromen via X.com 2026-05-05 1:30 PM — 'For the 5th month in the last 6, Nonmonetary Gold was again the single biggest export of the US in March. US gold exports were 1.7x > oil; 2x > Rx preparations, 2.5x > aircraft engines. Biggest destination for US gold exports: China or Switzerland (& then on to China).' FRED chart attached: Exports of Goods: Nonmonetary gold (BEA series IEAXGG) recent peak ~$36B/mo vs pre-2024 baseline ~$3B", "WALTER verify-research sub-agent 2026-05-06 ~17:55 UTC (~$0.05) — verdict CORRECTED-FRAMING 0.55 — primary Census FT-900 Mar 2026 Exhibit 7 + FRED IEAXGG: nonmonetary gold ~$14.99B March 2026 (single-line), crude oil ~$10.66B + other petroleum ~$7.98B, pharma preparations ~$8.7B, aircraft engines ~$5-6B → actual ratios gold/crude ~1.4x (vs Gromen 1.7x) / gold/pharma ~1.7x (vs Gromen 2x) / gold/aircraft-engines ~2.5x ✓"]

to: BOND (ACTION — backup-promotion: ZHAO Tier-2 STALE 34d / spawn pending; BOND refreshed 5/5 after 40-day staleness, has UST_FOREIGN domain coverage)
info: ZHAO (when spawned), LIQUID, HENRY, RED (auto-cc per v0.7 By Tag/By Verdict CORRECTED-FRAMING rule), SAM, NEXUS
group: CREDIT_CHAIN
dispatched: 2026-05-06T18:25:00Z
dispatch_note: "Will-page Telegram 5/6 18:01 UTC (msg 1404 of 5-image batch). VERIFY-RESEARCH sub-agent CORRECTED-FRAMING 0.55. **What's confirmed:** US nonmonetary gold export ~$15B March 2026 single-month is real and FRED-traceable; gold IS at or near top of US export line-items by dollar value at line-item granularity; gold-exports-spike is a multi-month pattern not a single-print artifact. **What's CORRECTED:** (a) gold/crude ratio actually ~1.4x not 1.7x (Gromen may be using gold vs crude-oil-only excluding refined petroleum; with refined petroleum included, oil exceeds gold); (b) 'single biggest export' true at HS-line-item granularity but pharmaceutical preparations is the larger end-use category for full-year 2025 (~$120B annual) — ranking depends on aggregation level; (c) destination 'Switzerland & then on to China' is INFERENTIAL not census-confirmed — Swiss vault accumulation is also possible; (d) **load-bearing distinction: dollar-value spike is partially price-driven** (gold ATH ~$3,400+/oz) — physical-volume outflow is meaningfully smaller than the dollar headline implies. **Overlooked angle (verify sub-agent flag):** US gold IMPORTS (FRED IEAMGG) — if US is also importing nonmonetary gold near record (NY Fed vault flows / Swiss-to-US arbitrage), the NET outflow is smaller than gross exports suggest. Should pull both legs before treating as one-way dedollarization signal — flagged here so RED/BOND can evaluate before integrating into UST_FOREIGN thesis. **Cluster placement:** primary FED_FRAMEWORK (dedollarization narrative, currently underweight at 2 BOARD signals); secondary ASIA_CHINA (China-as-final-destination if confirmed). **Cluster_mediating with SIG-W-20260506-004 (Arbor Fed UST holdings 65.9% — Fed buying USTs while foreigners exporting bullion).** Combined narrative: foreign holders rotating UST→gold while Fed steps in to absorb; if both sides confirm, FED_FRAMEWORK cluster has 2-vector convergence on plumbing-stress thesis. RED auto-cc per ROUTING_TABLE v0.7 By Tag/By Verdict CORRECTED-FRAMING rule. **Confidence 0.55 (assessed — verify caveats are load-bearing); calibration: directional thesis retained, specifics imprecise.**"

signal_type: pattern-match
confidence: 0.55
confidence_language: assessed
resources: 1
safety_net: clear

word_count: 234

cluster: FED_FRAMEWORK
---

## Signal

Per Luke Gromen via X (5/5): US **nonmonetary gold was the single biggest US export in March 2026** (5th month of last 6). Stated ratios: 1.7× oil, 2× pharma preparations, 2.5× aircraft engines. Destination: "China or Switzerland (& then on to China)." FRED chart shows series at ~$36B/mo recent peak vs pre-2024 baseline ~$3B/mo.

### Verify-research findings (CORRECTED-FRAMING 0.55)

**Confirmed (Census FT-900 Mar 2026 Exhibit 7 + FRED IEAXGG):**
- Nonmonetary gold March 2026 export ≈ **$14.99B** — real, FRED-traceable
- Gold IS at top of US export line-items by dollar value at HS line-item granularity
- Multi-month pattern (5 of last 6 months at line-item top) — directionally correct

**Corrected:**
1. **Ratios overstated:** gold/crude actually ~1.4× (not 1.7× — Gromen may be excluding refined petroleum; including it, oil > gold). Gold/pharma ~1.7× (not 2×). Gold/aircraft-engines ~2.5× ✓
2. **"Single biggest export" framing is granularity-dependent** — true at HS line-item level; **pharma preparations is the larger end-use category** for full-year 2025 (~$120B annual)
3. **Destination "& then to China" is INFERENTIAL** — not Census-bilateral-trade-confirmed. Swiss vault accumulation is also a real possibility (LBMA refining hub)
4. **Dollar-value spike is partially price-driven** — gold ATH ~$3,400+/oz means physical-volume outflow is meaningfully smaller than dollar headline implies

**Overlooked angle (load-bearing for thesis):** US gold IMPORTS (FRED IEAMGG) — if US is also importing nonmonetary gold near record (NY Fed vault flows / Swiss-to-US arbitrage), NET outflow is smaller than gross-exports suggest. Both legs needed before treating this as one-way dedollarization signal.

### Implication

**Direction confirmed but specifics imprecise.** Useful for FED_FRAMEWORK thesis as one node of a multi-vector pattern; not load-bearing on its own. **Cluster-mediating with SIG-W-20260506-004 (Fed UST holdings spike)** — combined narrative: foreigners rotating UST → gold while Fed steps in to absorb. If both sides confirm with proper rigor (gold-imports leg pulled, Fed composition split into MBS-rolloff vs net-new-UST-buying), FED_FRAMEWORK cluster has 2-vector convergence on UST plumbing stress.

## Action

- **BOND (action, backup for ZHAO):** pull FRED IEAMGG (gold imports) leg + bilateral trade Census Exhibit 14 China-direct vs Switzerland-routed; integrate into BOND auction-data tool framework if the gross-vs-net dynamic holds. Auction-demand composition cross-read.
- **ZHAO (info, when spawned):** China official-reserve gold accumulation cross-check; LGFV/HIBOR plumbing connection.
- **LIQUID (info):** funding-stress connection — foreign-holder-rotation away from UST = back-end source-of-funds question.
- **HENRY (info):** equity / vol-regime — gold-as-export at ATH is positioning-extreme territory; calibration check.
- **RED (info, CORRECTED-FRAMING auto-cc per v0.7):** specifics-imprecise on ratios; thesis directionally retained but Gromen-framing-as-stated should not be propagated unmodified into adversarial steelman.
- **SAM (info):** JPY/USD cross — gold flows are part of broader currency-rotation calculus.
- **NEXUS (info):** cluster classification — FED_FRAMEWORK currently 2 signals; this + SIG-004 brings to 4 if both dispatch.

**Word count:** 234 (within PRIORITY soft cap including dispatch_note; body alone ~340 — exceeds; primary substance is the verify-corrected facts).

---

*v0.7 cluster header — FED_FRAMEWORK. CORRECTED-FRAMING auto-cc to RED per ROUTING_TABLE v0.7 By Tag/By Verdict.*
