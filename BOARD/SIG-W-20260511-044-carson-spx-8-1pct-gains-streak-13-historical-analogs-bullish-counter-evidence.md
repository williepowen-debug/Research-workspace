---
id: SIG-W-20260511-044
date: 2026-05-11
origin: WALTER image-batch 2026-05-11 — Carson Investment Research / Ryan Detrick chart pair (footer "Source: Carson Investment Research, FactSet 05/08/2026"); skip-verify (institutional aggregator + mechanical SPX data)
domain: MARKET_VOL
cluster: POSITIONING_VALUATION
signal_type: counter-evidence
precedence: PRIORITY
confidence: 0.80
to: HENRY
info: [RED, NEXUS, VIOLET, LIQUID, BOND]
signal_role: standalone
event_window: closed
verify_research_verdict: SKIP-VERIFY (institutional aggregator, mechanical SPX data, FactSet primary)
---

# Carson/Detrick: SPX 8 Consecutive 1% Gains Without 1% Decline — 13 Historical Analogs Since 1950, Mean Forward Returns Positive (Counter-Evidence to Positioning-Fragility Thesis)

**Verbatim claim (verified — Carson Investment Research / Ryan Detrick):**

Two companion charts (footer "Source: Carson Investment Research, FactSet 05/08/2026"):

**Chart 1 — Line chart:** "Eight 1% Gains In A Row Without A 1% Decline For S&P 500 (1950 - Current)" — marks 13 historical signal-dates on SPX log chart 1950-2026; most recent signal current.

**Chart 2 — Histogram:** "S&P 500 1% Gains Without A 1% Decline (1950 - Current)" — frequency distribution of streak-lengths; current 8 is in same bucket as historical 8-11 streaks. Notable high-counts: 11 (1963), 11 (1986), 10 (1992), 9 (1999-2000), 9 (2004), 9 (2016 era), 8 (multiple periods).

**Historical forward-return statistics (13 instances):**

| Window | Average | Median | % Higher | Higher | Lower | Count |
|--------|---------|--------|----------|-------:|-----:|-----:|
| 1-Month | +0.9% | +0.4% | 53.8% | 7 | 6 | 13 |
| 3-Month | +2.2% | +3.5% | 69.2% | 9 | 4 | 13 |
| 6-Month | +7.1% | +5.4% | 61.5% | 8 | 5 | 13 |
| 12-Month | +10.2% | +10.3% | 76.9% | 10 | 3 | 13 |

**Source attribution:**
- Carson Investment Research / Ryan Detrick (@ryandetrick on X)
- Data source: FactSet (institutional primary)
- Date stamp on chart footer: 05/08/2026

## Substance

- **8 consecutive 1% gains without a 1% decline** is a relatively rare technical occurrence — 13 instances since 1950 = ~once every 5.8 years
- **Historical forward returns POSITIVE across all 4 windows** — mean +0.9% (1mo) / +2.2% (3mo) / +7.1% (6mo) / +10.2% (12mo); median higher than mean on 3-mo + 6-mo windows = right-skewed distribution; 12-mo 76.9% positive hit-rate
- **Analog set is NOT ominous** — most recent prior was post-2016 election rally; 1992/1999-2000/2004 also bullish setups. None of the analogs cited are "1929/1973/1999"-style top-marker patterns
- **Counter-evidence to current POSITIONING_VALUATION bear cluster** (per SIG-W-20260509-007 defensives underweight / SIG-W-20260506-009 HF Mag 7 12-mo low / SIG-W-20260508-013 SPX $2.6T calls / SIG-W-20260509-016 SPX 5%+ at 52w-lows analogs / SIG-W-20260506-010 Shiller PE 41.24 at 93% Dot Com peak)

## Dispatch notes

**Skip-verify-by-design** — Carson Investment Research is an institutional aggregator (Ryan Detrick = ex-LPL Chief Market Strategist, now Carson Chief Market Strategist; well-credentialed); FactSet primary data is institutional-canonical; SPX 1% gains over 1950-2026 is mechanically computable. Confidence 0.80 reflects institutional-credibility-ceiling minus the limited-sample-size discount (N=13).

**Sample-size caveat:** 13 instances over 76 years is a small sample. Median > mean on 3mo + 6mo suggests right-skewed distribution with a few large positive outliers driving mean. Forward returns are real but bounded inferentially — not statistically-significant-vs-random unconditional-SPX-baseline.

**`signal_role: counter-evidence`** — explicit bull-data delivery into a bear-leaning cluster (POSITIONING_VALUATION currently at 30 sigs with bear-positioning extreme as dominant frame). Counter-evidence routes RED info per ROUTING_TABLE v0.5 By Signal Type meta-row.

**Combine #13 (line) + #14 (histogram) into single dispatch** — same Carson 5/8 note, two views of same underlying analysis. Single signal entry per Format-Spec one-signal-multi-recipient discipline.

**RED steelman context** — per the "always present strongest bull case" rule (auto-memory `feedback_red_edge.md`), this signal is the strongest current bull-data input. Carson historical analogs say "ride higher" not "bubble pop"; matched against Shiller 41.24 / Buffett 227% / HF Mag 7 12-mo low / breadth at 5.6% 52w-lows = the substance-vs-tape question. Carson's 8-streak forward returns are TAPE-side; the cluster-mediating signals (HF de-crowding + valuation extremes) are SUBSTANCE-side. Recurring tape-vs-substance bifurcation pattern (per `feedback_tape_vs_substance_bifurcation`); Carson sits firmly on tape-side.

**Calibration cycle 1 input (post-RED/BRENT 5/20-27):** in 1-3 months we can compare Carson's forward-return prediction (mean +0.9% 1mo / +2.2% 3mo) against realized SPX 5/8 → 6/8 / 8/8 — empirical calibration of historical-analog reliability.

## Recipient routing

- **HENRY action** — POSITIONING_VALUATION cluster owner; positioning-extreme vs forward-return-distribution context.
- **RED info** — counter-evidence routes per Counter-Evidence default + bull-steelman rule.
- **NEXUS info** — convergence-scoring input; balances bear cluster signals.
- **VIOLET info** — vol-regime adjacent (low-VIX correlation to 1%-gain streak windows).
- **LIQUID info** — credit-spread implication if tape-side persists.
- **BOND info** — UST-equity correlation context.
