# LESSONS.md — HENRY Mistake Patterns & Rules

*Read at boot. Learn once, prevent forever.*

---

### [Data] — Always Pull Fresh Values
**Pattern:** STATUS.md values go stale between spawns (days/weeks). Citing stale VIX, HY OAS, or SPX levels produces wrong analysis.
**Rule:** If STATUS.md says "Known Data Issues" or values are >24h old, pull live data via web_search before any analysis. Never cite STATUS.md values as current without verifying.

### [Analysis] — VIX Spikes Can Be Artificial
**Lesson from Aug 2024:** VIX spike to 65 was 85% bid-ask widening, not real fear. 0DTE volume dropped 26%, recovery in 3 sessions. Don't treat VIX spikes as ground truth — check the mechanism (real selling vs liquidity withdrawal).

### [Analysis] — Credit Leads Equities, Not Vice Versa
**Rule:** Never call an equity bottom until HY OAS has peaked. Credit reprices before equity every time. If someone asks "has the selloff bottomed?" — check HY OAS first, not SPX technicals.

### [Process] — Distinguish Margin Trade vs Credit Trade
**Lesson from KRE:** Regional banks can sell off because the yield curve flattens (margin trade) or because credit quality deteriorates (credit trade). The distinction determines speed — margin trades grind, credit trades gap. Always identify which is driving the move before forecasting trajectory.

### [Verification] — Don't Cite Own STATUS.md for Live Prices
**Rule:** STATUS.md is for thresholds, frameworks, and thesis. It is NOT a live data feed. When asked about current VIX, SPX, or spreads, pull from web sources. Citing your own stale dashboard as "current" is circular.

---

*Last reviewed: 2026-02-27*
