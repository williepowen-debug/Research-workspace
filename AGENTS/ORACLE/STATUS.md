# ORACLE STATUS

**Updated:** 2026-06-18 20:18 ET (pull `2026-06-19T00:18Z`) — **REVIVED** after 79-day dormancy (prior: 2026-04-01)
**Domain:** Prediction-market monitoring (Polymarket) — crowd-vs-thesis divergence
**Data:** live via `scripts/polymarket.py pull` (Gamma API, public). Time series → `workbook/ODDS_LOG.tsv`.
**State:** 🟠 — one 🔴 alert firing (Iran de-escalation), one large standing divergence (recession).

---

## Signal Dashboard (live)

| Market | Tier | Prob | Δ1d | Δ7d | Vol | Liq | Read |
|--------|:--:|--:|--:|--:|--:|--:|------|
| Iran ends enrichment by Jun 30 | T2 | **66.5%** | +19.0 | **+43.0** | $6.0M | $114K | 🔴 de-escalation repricing — see Alert 1 |
| Fed: NO cuts 2026 | T1 | **81.9%** | +1.9 | +3.0 | $5.3M | $74.8K | hawkish grind; deep market |
| Fed: 1 cut 2026 | T1 | 13.5% | −1.0 | — | $1.7M | $91.9K | mirror of above |
| US recession 2026 | T1 | **12.5%** | −0.5 | −5.0 | $1.6M | $31K | vs thesis ~76% = **−63pp**, widening |
| AI bubble burst 2026 | T2 | 20.4% | −0.9 | −4.8 | $2.3M | $15.9K | stable/easing |
| US bank failure by Jun 30 | T1 | 9.0% | +1.5 | −10.5 | $12K | $2.1K | ⚠️ thin — discount the move |
| US debt default by 2027 | T2 | 3.5% | −0.2 | −1.8 | $15.5K | $4.5K | ⚠️ thin — control |
| Nothing Ever Happens 2026 | T3 | **82.5%** | — | +12.0 | $619K | $27.3K | complacency surge (44%→82.5% since Apr) |

Δ in percentage points. ⚠️ thin = liquidity < $5K (single $5–50K bet moves 5–10pp; do **not** mark on one print).

---

## Alerts

**🔴 ALERT 1 — Iran de-escalation pricing in fast.** "Iran ends uranium enrichment by Jun 30" **+43pp/7d (+19pp/1d) → 66.5%** on a deep $6.0M / $114K-liquidity market (not thin). Crosses ORACLE's "Iran shift >20pp → HAWK, BRENT" threshold. Corroborates **WALTER 6/16 "DE-ESCALATION PENDING."** Read for **BRENT/HAWK: oil-downside** as war premium drains. → signal sent to HAWK, BRENT.

**🟠 DIVERGENCE 1 — Recession crowd vs thesis.** Market **12.5%** (−5pp/7d, drifting *down*) vs fleet thesis ~70–80%. **~63pp gap and widening** — the single largest crowd-vs-thesis divergence in the book. Either our edge or our thesis decaying. → RED to adjudicate. *(Thesis side is the Apr baseline — needs RED/SENTRY refresh.)*

**🟢 CONFIRM 1 — Higher-for-longer entrenching.** Fed "no cuts 2026" **81.9% (+3pp/7d)** on a deep $5.3M market — moved *past* the 57–70% zero-cut HENRY anchored to in HEN-33. Supports the regional-bank/CRE-refi pressure thesis (KRE/OZK/WAL). → LIQUID, HENRY.

**🟠 SENTIMENT — Broad complacency.** "Nothing Ever Happens 2026" **82.5% (+12pp/7d)** + recession↓ + AI-burst↓ = the crowd de-risking tail expectations across the board. Pairs with VIOLET's complacency tape. Bear-contrarian. → VIOLET, PROME.

---

## Thesis Divergence Map

| Domain | Market (live) | Fleet thesis | Gap | Reading |
|--------|--:|--:|--:|--------|
| Recession 2026 | 12.5% | ~70–80% | −63pp | **Market far behind us** — biggest gap |
| Bank failure (near) | 9.0% ⚠️thin | ~25–30% | −16 to −21pp | Market behind; but thin, low-signal |
| Fed cuts 2026 | 81.9% no-cuts | higher-for-longer | aligned | **Confirms** our regime read |
| Iran de-escalation | 66.5% (+43/7d) | de-escalating | aligned | **Confirms** WALTER; oil-down |

*Thesis column = Apr-1 baseline carried forward; flag to RED/SENTRY for a current refresh.*

---

## Convergence Matrix

| # | Market | Score | Status | Key Signal | Upgrade Trigger |
|---|--------|:--:|:--:|------------|-----------------|
| 1 | Iran enrichment / de-esc | 4 | 🔴 | +43pp/7d, $6M deep | sustained >70% or oil confirms |
| 2 | Recession 2026 divergence | 3 | 🟠 | 12.5% vs ~76% thesis | gap >70pp OR market turns up |
| 3 | Fed no-cuts 2026 | 3 | 🟠 | 81.9%, deep | >90% or shift >15pp/wk |
| 4 | Nothing Ever Happens | 2 | 🟠 | 82.5%, +12/7d | <30% (tail re-pricing) |
| 5 | AI bubble burst | 2 | 🟡 | 20.4%, $2.3M | >40% |
| 6 | Bank failure (thin) | 1 | 🟢 | 9.0%, $2.1K liq | vol >$50K (real signal) |

**State:** de-escalation confirmed + macro complacency vs a still-live stress thesis. The gap between crowd (calm) and thesis (stress) is *widening* — contrarian edge OR early warning we're wrong.

---

## BOTTOM LINE

The crowd has moved hard toward **calm** — recession 12.5% and falling, "nothing ever happens" 82.5%, Iran de-escalating, bank-failure odds bleeding out. Your thesis says stress. **That divergence is the whole point of ORACLE** — it's now ~63pp on recession and widening. Two clean confirmations (Fed higher-for-longer, Iran→oil-down) and one fast-moving 🔴 (Iran +43pp/7d) routed to agents. Watch whether the calm is the crowd being early-wrong (our edge) or us being late-wrong (thesis decay) — RED owns that adjudication.

*Re-pull: `python3 AGENTS/ORACLE/scripts/polymarket.py pull --log`*
