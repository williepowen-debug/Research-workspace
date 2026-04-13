**Task:** Four-Model Research Synthesis — Credit-VIX Lead-Lag Analysis

**Date:** 2026-04-12

**Status:** COMPLETE

**Research Sources:**
- **Gemini** (Google): Microstructure, Merton model, VIX futures lead dynamics
- **Perplexity**: Episode granularity, exact dates/magnitudes, 2024 yen unwind
- **Claude** (Anthropic native): Academic literature, firm-level vs aggregate distinction, yield curve filter
- **Grok** (xAI): Data source specificity, Granger causality, 7-month cycle lead time

**Key Findings:**
1. **Aggregate HY OAS leads VIX by 2-6 weeks** at tactical level (100bps → spike) when VIX < 20
2. **Cycle level lead: ~7 months** from HY OAS trough to equity peak (Grok)
3. **Hit rate: ~70%** | **False positive rate: 25-30%** (15-20% with yield curve filter)
4. **Regime-dependent:**
   - VIX < 15: 6-16 week lead (highest signal quality)
   - VIX 15-20: 3-8 week lead (high quality)
   - VIX 20-30: 1-4 week lead (moderate)
   - VIX > 30: Near-simultaneous (too late)
   - VIX > 40: VIX leads credit (relationship inverts)
5. **Academic reconciliation:** Equity leads individual CDS, but aggregate HY OAS leads equity vol due to cross-sectional deterioration
6. **Yield curve filter:** Combining credit spreads with yield curve slope "dramatically reduces" false positives (Fed research)

**Episode Database Completed:**
| Episode | Direction | Lead Time | Regime | False Positive? |
|---------|-----------|-----------|--------|-----------------|
| GFC 2007-08 | Credit led | 6-10 weeks | Low vol → rising | No |
| 2011 EU crisis | Credit led | 8-10 weeks | Rising vol | No |
| 2015-16 Energy | Credit led | 12-18 months | Low vol | Partial (sector-specific) |
| Q4 2018 | Coincident | 0-2 weeks | Rising vol | No (macro-driven) |
| Feb 2018 Volmageddon | VIX led | N/A | Low vol | **Yes** (technical) |
| COVID 2020 | Near-simultaneous | Days | Rising → crash | No (exogenous) |
| 2022 Rate Shock | VIX led | 10-12 weeks | Low vol → rising | **Yes** (rates-driven) |
| Aug 2024 Yen Unwind | VIX led | N/A | Low vol | **Yes** (positioning) |

**Files Updated:**
- `STATUS.md` — Added four-model synthesis framework, regime-dependent lead times, confirmation checklist
- `SIGNAL_INTAKE.md` — Added historical episode database, false positive patterns
- `TRADE.md` — Updated Credit-Vol Lag Trade with four-model framework, entry criteria, historical performance
- `thesis/VIX_THESIS.md` — v3.0 with academic nuance, complete episode database, regime-dependent behavior
- `MEMORY.md` — Added credit-to-vol transmission synthesis, yield curve filter

**Current Status:**
- VIX: 19.23 (low vol regime, 🟡)
- HY OAS: 2.90 (tight, no stress)
- Convergence Score: 1/25 (4%)
- **No actionable signal** — monitoring for HY OAS >100bps widening with VIX < 20

**Next Actions:**
1. Establish daily data workflow for VX.tsv updates
2. Add yield curve data (10Y-2Y spread) to confirmation checklist
3. Paper trade when HY OAS approaches 4.0% (currently 2.90%)
4. Test cross-agent signal flow to HENRY/LIQUID

**Research Gaps Closed:**
- ✅ Lag quantification by regime
- ✅ False positive sources and mitigation
- ✅ Academic literature reconciliation
- ✅ Historical episode database
- ⚠️ Real-time yield curve integration (pending data source)
