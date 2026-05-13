---
signal_id: SIG-W-20260513-007
precedence: PRIORITY
timestamp: 2026-05-13T17:48:00Z
source: WALTER
origin: "SentimenTrader @sentimentrader 5/12/26 10:35 PM — ROBO Put/Call Ratio analog study (10 instances since 2002, median fwd 1yr return +20.76%); SPX last 7,398.93 / ROBO Put/Call Ratio last 0.54"

to: HENRY (ACTION)
info: RED, NEXUS, VIOLET, LIQUID, BOND

signal_type: counter-evidence
confidence: 0.80
confidence_language: assessed
resources: 1
safety_net: clear

word_count: 200

cluster: POSITIONING_VALUATION
signal_role: counter_evidence
event_window: closed

verify_research_verdict: SKIP-VERIFY-BY-DESIGN (SentimenTrader institutional aggregator — Jason Goepfert / Kaeppels established quantitative-systematic credentials; ROBO Put/Call OCC primary data; 10-analog quantitative-historical claim mechanical from CBOE / OCC time series)
---

# SentimenTrader: Retail Buying Puts at Historic Rate While SPY at ATH — 10 Analogs Since 2002 / All Higher 1Yr Later / Median Forward Return +20.76% (Counter-Evidence to Bear POSITIONING Cluster)

**Verbatim claim (SentimenTrader @sentimentrader 5/12/26 10:35 PM, 31K views):**

- **Setup**: "Retail traders are buying puts at a historic rate while $SPY hits all-time highs"
- **Analog set**: This has happened **10 times since 2002**
- **Forward return**: **One year later: higher every single time. Median return: +20.76%.**
- **Data**: ROBO Put/Call Ratio (Last = 0.54) overlaid on SPX (Last = 7,398.93); chart 2000-2026
- **Source**: SentimenTrader user research (Kaeppels et al.) — institutional-systematic publisher

## Substance

- **Bull-side counter-evidence to bear POSITIONING cluster.** Pattern (retail-puts-at-ATH) is contrarian-bullish historically: small traders chasing protection AT a top = signal that retail is wrong-positioned for the trend continuation.
- **10-analog quantitative-historical anchor**: Not opinion / not anecdote — explicit n=10 sample with binary 1yr-later-higher and median +20.76%. Backward-looking; forward-looking generalizability bounded by analog set (2002-present = mostly secular bull regime).
- **ROBO Put/Call 0.54 (current)**: Different metric from CBOE Total P/C — ROBO is ROBOTOPCALL retail-flow-focused subset. 0.54 = elevated put-buying retail side; cleaner read than aggregate market P/C ratio.
- **Cross-cluster pairing with SIG-W-20260511-044 Carson/Detrick** (8-streak forward returns +0.9/+2.2/+7.1/+10.2%): now 2 institutional-bull-side analog studies firing within 2 days. Cluster has structured bull-counter-evidence growing.

## Dispatch notes

**`signal_role: counter_evidence`** — explicit bull-data delivery; RED auto-cc per ROUTING_TABLE Meta row. Sample-size caveat (n=10 over 23 years = ~1 instance per 2.3yr).

**Skip-verify-by-design** — SentimenTrader is institutional-systematic publisher; ROBO Put/Call is OCC-primary derivative. Confidence 0.80 reflects institutional credibility minus small-sample-size discount.

**Pattern note: Tape-vs-substance cluster regime input.** Today's macro convergence (CPI 3.8% + PPI 6.0% + NY Fed HHDC stress) is substance-side bearish; SentimenTrader retail-puts-at-ATH analog says tape-side likely-bullish-into-12mo. **Same tape-vs-substance bifurcation pattern as 5/5-5/6 Brent + 5/11 Aramco** — substance hardens, tape softens. Now at 4th consecutive observation (5/5 / 5/6 / 5/11 / 5/13). **Calibration cycle 1 input HARDENS** — bifurcation regime-state confirmed.

**Calibration test pre-registered**: SPX from 7,398.93 (5/12 close) → 5/12/27 SPX close. Median +20.76% would target ~8,933. Track quarterly.

## Recipient routing

- **HENRY action** — POSITIONING_VALUATION cluster owner; counter-evidence routing.
- **RED info** — counter-evidence default + bull-steelman rule.
- **NEXUS info** — convergence-classification; counter-evidence cluster-composition input.
- **VIOLET info** — ROBO P/C is vol-related sentiment proxy; cross-feed with VIX/SKEW regime tracking.
- **LIQUID info** — equity-credit-spread correlation context.
- **BOND info** — UST-equity correlation context.

## Sources

- SentimenTrader @sentimentrader X post 5/12/26 10:35 PM, 31K views, image displayed: ROBO Put/Call Ratio analog study
- Full Analysis link in tweet: users.sentimentrader.com/users/kaeppels...
- ROBO Put/Call OCC primary data
- Background SentimenTrader research methodology (Jason Goepfert / Kaeppels institutional publishers)
