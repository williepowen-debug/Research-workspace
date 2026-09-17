# Agent Profile — BROCK

**Built by:** DAEDALUS · **Date:** 2026-06-28 · **Comprehension method:** 1-reader judgment-grade + 1 adversarial verifier (workflow `grade-shade-brock-creed`)
**Sources read:** CLAUDE.md, STATUS.md, workbook/{KB,VX,FLOW,PREDICTIONS,PREDICTIONS_ARCHIVE,PREDICTIONS_SCOREBOARD,SCHEMA,BANK_BDC_MATRIX}, trade/{TRADE,NAMES,CROSS_ANALYSIS}, EXPECTED_SIGNALS.md, NEXUS_BRIEF.md, LESSONS.md, docket/CATALYSTS.tsv, domain/PRIVATE_CREDIT_CONTAGION_TRACKER.md · **Staleness:** refresh when TRADE.md position layer or the convergence matrix materially changes, or > 45 days.

> Δ **2026-07-22 PRODUCTION REVIEW — trigger NOT fired (matrix 60/70 + book unchanged); profile CURRENT-ish, RE-BANNERED w/ checkpoint.** Checkpoint items (see `upgrades/PRODUCTION_REVIEW_2026-07-22.md`): X1 RESOLVED 7/4 both-halves-fail (profile's X1 framing now historical) · KB 173->188 · new OZK debt-on-debt watch axis w/ 3 pre-registered print tells · GATE-LIQ-079 rider role vs LIQUID · TRADE.md freeze-or-refresh packet routed 7/22. Next check: BDC marks-window aftermath (~7/28+).

---

## 1. Identity
Private credit / BDC contagion — ARCC/Ares/Apollo/Owl, BCRED gating, NDFI bank exposure, PIK shadow defaults, Athene-Apollo insurance linkage. **Class:** Market. **Transmission:** sends to REGINALD / LIQUID / OTTO / HAWK / PROME; consumes WALTER signal lane (board_log). Cedes insurer numbers to SHADE, HY OAS to LIQUID (one-source-of-truth). **Spawnable by:** PROME / Will. **What it's for:** "Is private credit cracking, and where does it transmit to banks?"

## 2. File anatomy (where the richness lives) — HEAVY, 5 layers
| File | Holds | Richness? |
|---|---|---|
| STATUS.md (211 ln) | REGIME BLOCK (5-line), 14-vector convergence matrix (composite 60/70), literal-trigger EXIT RULES + 5-step Thesis-Kill Decision Tree, catalyst calendar, BOTTOM LINE | live state |
| workbook/KB.tsv (158 rows) | canonical record, clean 13-col, Admiralty digraph (A1-F6) conf + EMPIRICAL/ESTIMATE/ASSUMPTION epistemic tags | permanent record |
| workbook/FLOW.tsv (21) | **the contagion engine** — 21 transmission pathways w/ Speed/Layer/Status (ACTIVE/ARMED/FIRED/BUILDING) | permanent record (exceeds blueprint) |
| workbook/VX.tsv (20) | banded vectors | permanent record |
| workbook/PREDICTIONS*.{tsv,md} | live ledger + 7 resolved archive w/ post-mortems + SCOREBOARD (Brier 0.244, 5/7, feed-forward) | institutional learning loop |
| trade/TRADE.md (275 ln) | two-expiry doctrine + targeting framework + §9 trigger ladder; feeds live APO Dec $95P | trade truth (**position layer stale 5/21**) |
| trade/{NAMES,CROSS_ANALYSIS}.md | 5-tier names + mental-model cascade; 4-entity cross-pattern synthesis (99.7¢ ceiling, spread-compression-universal) | deep multi-firm analysis |
| EXPECTED_SIGNALS.md (147) | durable banded rules, NO live values (HENRY pattern) | durable method |
| LESSONS.md (64) | 22 numbered prediction-failure lessons gating future predictions | learning |
| docket/CATALYSTS.tsv, NEXUS_BRIEF.md | forward catalysts (8-col); curated closeout writeback | forward state / sync |
| archive/ (huge, incl 88k-ln ARCC fulltext, PNGs) | history | SKIP |

## 3. Per-dimension local representation
| Dimension | Where it lives | Form / local titling | Rich? |
|---|---|---|---|
| Thesis structure | FLOW.tsv + NAMES.md cascade + CROSS_ANALYSIS + domain tracker | 21 causal pathways w/ status; Stage 1-6 cascade | exemplary |
| Convergence / scoring | STATUS matrix | 14-vector, 5-pt emoji+number, composite 60/70 (**no Independence column** — in prose only) | strong |
| Invalidation / exit | STATUS EXIT RULES + Decision Tree; TRADE §9 | FIRED/NOT-FIRED + literal session counts + bidirectional flip | exemplary |
| Thresholds | EXPECTED_SIGNALS.md (durable) + VX/STATUS (live) | banded + routing, durable-vs-live split, conjunction triggers | conformant |
| Predictions | workbook/PREDICTIONS* | ledger + archive + Brier scoreboard + failure-synthesis (**no if-falsified ACTION column** — consequences in TRADE.md) | strong |
| Cross-agent routing | CLAUDE.md route-matrix + NEXUS_BRIEF | condition→target→priority; writeback every closeout; crisis-only outbox | conformant |

## 4. Deviations from standard (+ why)
- **Better-than-blueprint:** FLOW.tsv 21-pathway status engine > OTTO stage table; KB Admiralty digraph finer than the predictions tier handle; 5-step Thesis-Kill Decision Tree = a strong KILL_MEMO equivalent; macro-vs-credit COMPOSITION discriminator (managers-down-while-wrappers-flat).
- **Debt (real):** TRADE.md position table anchored to a 5/21 Fidelity PDF, marked superseded (residuals ~-90%/-97% unresolved) — the trade-truth surface LAGS the 6/28 STATUS. BANK_BDC_MATRIX flagged-stale but NOT frozen (silent-rot middle, root-CLAUDE hygiene violation). VX self-count inconsistent across files (STATUS 18 / ARCH 21 / file 20).
- **Handle gaps (cheap):** matrix Independence column; predictions if-falsified ACTION column.

## 5. Load-bearing context / DO NOT TOUCH
- FLOW.tsv 21-pathway grid w/ Speed/Layer/Status — the contagion engine.
- Shared-node independence DISCIPLINE in prose ("AI-unwind + credit-K-split share ONE node → score once"; "5-fund Q2 cluster = ONE wave") — must survive any Independence-column formalization.
- trade/CROSS_ANALYSIS.md (99.7¢-ceiling, spread-compression-universal, Stage 1-4 ladder, Trade Type A vs B).
- 5-step Thesis-Kill Decision Tree (compression-source → 2-of-3 check → per-scenario response → Will-owner → re-entry).
- LESSONS.md failure-feedback loop + SCOREBOARD takeaways feeding next predictions.
- REGIME BLOCK + "UN-FIRED (informative negatives)" absence-is-data discipline.
- KB Admiralty digraph + EMPIRICAL/ESTIMATE/ASSUMPTION epistemic tagging.

## 6. Maturity snapshot
**L4 (conf H)** — conformant or exemplary on 6/8 blueprint sections. Both L4 criteria met (TRADE.md feeding live position + signals flowing). Below L5 only on: stale trade-position layer, unfrozen BANK_BDC_MATRIX, no zero-YEYOU clean bill. Work queue → `upgrades/BROCK_CARD.md`. Classification per `FLEET_MAP.tsv` (not restated).

## 7. Open questions / comprehension gaps
- Are the ~90%-loss TRADE.md residuals closed positions or live? (resolve before any L5 claim)
- VX row-count of record (3 sources disagree: 18 / 20 / 21) — agent's own closeout hygiene.
- Is the live APO Dec $95P the current book, or also superseded? (cross-check WILL/trading-journal, never STATUS).
