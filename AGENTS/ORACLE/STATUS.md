# ORACLE STATUS

**Updated:** 2026-06-21 (metrics module added; latest odds below remain 2026-06-18/19 pull) — revived + gap-audited (watchlist 8→14)
**Domain:** Prediction-market monitoring (Polymarket) — crowd-vs-thesis divergence
**Data:** live via `scripts/polymarket.py pull --log` (Gamma API). Time series → `workbook/ODDS_LOG.tsv`. Cross-agent surface → `NEXUS_BRIEF.md`. Metric layer → `PREDICTION_MARKET_METRICS.md`.
**State:** 🟠 — one 🔴 alert (Iran de-escalation, now oil-corroborated), one large standing divergence (recession).

---

## Signal Dashboard (live)

| Market | Tier | Prob | Δ1d | Δ7d | Vol | Liq | Read |
|--------|:--:|--:|--:|--:|--:|--:|------|
| Iran ends enrichment by Jun 30 | T2 | **62.5%** | +13.0 | **+41.0** | $6.3M | $144K | 🔴 de-escalation — Alert 1 |
| WTI dips to $70 (Jun) | T2 | **41.5%** | −2.0 | **+30.0** | $562K | $24K | oil-down corroborates Iran |
| WTI hits $100 (Jun) | T2 | 2.1% | −1.6 | **−23.4** | $473K | $131K | war-premium tail collapsing |
| Fed: NO cuts 2026 | T1 | **81.2%** | +1.5 | +4.0 | $5.3M | $76K | higher-for-longer grind |
| Fed: 1 cut 2026 | T1 | 11.5% | −2.5 | −2.0 | $1.7M | $91K | mirror |
| US recession 2026 | T1 | **12.5%** | — | −5.0 | $1.6M | $33K | vs thesis ~76% = **−63pp**, widening |
| US bank failure by Jun 30 | T1 | 11.0% | +3.5 | −10.0 | $12K | $2.1K | ⚠️ thin |
| Major bank bailout before 2027 | T1 | 12.5% | — | −3.0 | $3.7K | $1.3K | ⚠️ thin |
| Which banks fail Jun 30 (top) | T1 | 0.7% | −0.1 | −0.4 | $685 | $3.7K | ⚠️ thin — no named bank priced |
| AI bubble burst 2026 | T2 | 20.4% | −0.9 | −4.2 | $2.3M | $16K | easing |
| MicroStrategy bankruptcy 2027 | T2 | 8.0% | +1.0 | −0.5 | $172K | $12K | modest crypto stress |
| US debt default by 2027 | T2 | 3.7% | +0.2 | −1.7 | $15K | $4.2K | ⚠️ thin — control |
| Nothing Ever Happens 2026 | T3 | **82.5%** | −0.5 | +12.0 | $619K | $27K | complacency surge |
| June unemployment (modal) | T3 | 52.0% | +21.0 | +22.5 | $63 | $2.0K | ⚠️ dead market — replace |

Δ in pp. ⚠️ thin = liquidity < $5K (single $5–50K bet moves 5–10pp; do **not** mark on one print).

---

## Alerts

**🔴 ALERT 1 — Iran de-escalation, now oil-corroborated.** Enrichment-deal **62.5% (+41pp/7d)** on $6.3M; AND the oil ladder agrees — WTI "$70 low" **41.5% (+30pp/7d)** (market pricing oil *down*) while the war-premium tail WTI "$100 high" **collapsed −23pp/7d to 2.1%**. Two independent surfaces → de-escalation. Confirms WALTER 6/16. **BRENT/HAWK: oil-downside.** → signal sent.

**🟠 DIVERGENCE 1 — Recession crowd vs thesis.** Market **12.5%** (−5pp/7d, drifting *down*) vs fleet thesis ~70–80%. **~63pp gap, widening** — the largest crowd-vs-thesis gap. → RED to adjudicate (edge vs decay). *Thesis side = Apr baseline, needs RED refresh.*

**🟢 CONFIRM 1 — Higher-for-longer.** Fed "no cuts" **81.2% (+4pp/7d)** on deep $5.3M — past the 57–70% HENRY anchored (HEN-33). Supports KRE/OZK/WAL CRE-refi pressure. → LIQUID, HENRY.

**🟡 BANK CLUSTER — Crowd prices no banking crisis.** Failure 11%, bailout 12.5%, named-banks <1% — all low and falling. Coherent divergence vs REGINALD's stress thesis (but the bank markets are thin). → REGINALD.

**🟠 SENTIMENT — Complacency.** "Nothing Ever Happens" **82.5% (+12pp/7d)** + recession↓ + AI-burst↓ = broad de-risking of tails. Pairs with VIOLET. → VIOLET, PROME.

---

## Thesis Divergence Map

| Domain | Market (live) | Fleet thesis | Gap | Reading |
|--------|--:|--:|--:|--------|
| Recession 2026 | 12.5% | ~70–80% | −63pp | **Market far behind us** — biggest gap |
| Bank crisis (failure/bailout) | ≤12.5% ⚠️thin | ~25–50% | −13 to −38pp | Market behind; thin, low-signal |
| Fed cuts 2026 | 81.2% no-cuts | higher-for-longer | aligned | **Confirms** regime read |
| Iran de-escalation | 62.5% + oil | de-escalating | aligned | **Confirms** WALTER; oil-down |

*Thesis column = Apr-1 baseline carried forward; flag to RED/SENTRY for a current refresh.*

---

## Convergence Matrix

| # | Market | Score | Status | Key Signal | Upgrade Trigger |
|---|--------|:--:|:--:|------------|-----------------|
| 1 | Iran de-esc (event + oil) | 4 | 🔴 | +41pp/7d, oil-corroborated | sustained >70% or oil confirms further |
| 2 | Recession divergence | 3 | 🟠 | 12.5% vs ~76% | gap >70pp OR market turns up |
| 3 | Fed no-cuts 2026 | 3 | 🟠 | 81.2%, deep | >90% or shift >15pp/wk |
| 4 | Nothing Ever Happens | 2 | 🟠 | 82.5%, +12/7d | <30% (tail re-pricing) |
| 5 | Bank cluster | 2 | 🟡 | all ≤12.5%, thin | failure vol >$50K (real signal) |
| 6 | AI / crypto stress | 1 | ⚪ | AI 20%, MSTR 8% | AI >40% or MSTR >20% |

**State:** de-escalation confirmed (now in oil too) + macro complacency vs a still-live stress thesis. Crowd-vs-thesis gap *widening* — contrarian edge OR early warning we're wrong.

---

## Maintenance flags
- **Metrics module added:** use `PREDICTION_MARKET_METRICS.md` for entropy, KL bits, entropy-collapse anomaly alerts, liquidity/resolution discounts, and ORACLE→TERRY handoff packets. Metrics do not authorize auto-trading.
- **Jun 30 / Jul 1 resolutions:** bank-failure, named-bank, Iran, both WTI rungs — roll to next-period markets before they resolve (fetcher will flag ⏳ at ≤7d).
- **Dead market:** June-unemployment event = $63 vol — replace with a liquid labor market or drop.
- **Thesis refresh owed:** recession/bank thesis numbers are Apr baseline (RED).

---

## BOTTOM LINE

The crowd has moved hard toward **calm** — recession 12.5% and falling, "nothing ever happens" 82.5%, banks benign, Iran de-escalating (now confirmed in oil too). Your book says stress. That divergence — ~63pp on recession and widening — **is ORACLE's whole job.** Two clean confirmations (Fed higher-for-longer, Iran→oil-down) and one 🔴 (Iran +41pp/7d, oil-corroborated) routed. The open question RED owns: is the calm the crowd being early-wrong (our edge) or us being late-wrong (decay)?

*Re-pull: `python3 AGENTS/ORACLE/scripts/polymarket.py pull --log`*
