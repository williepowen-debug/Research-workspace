---
name: Exit Recommendations Need Mark-Context
description: When recommending cleanup of near-dated theta-killers, surface execution mark (vol regime, IV percentile, spot vs recent range) before recommending exit; if at unfavorable mark, propose pre-registered window-trigger framework with backstop dates rather than mechanical close-now
type: feedback
originSessionId: c371d62f-1e3d-4fef-9f9c-7c441c8cc25f
---
When recommending cleanup of near-dated theta-killing options at unfavorable execution mark (e.g., SPY at ATH + VIX at floor + IV percentile low), do NOT recommend mechanical "close now" — that crystallizes the worst-mark exit. Will pushed back on RED's mechanical-close recommendation 2026-05-06: *"I dont want to sell the puts into all time market highs though. I think I need to find a better opportunity between now and expiration to sell."*

**Why:** Vol-floor + spot-ATH = puts marked at theoretical worst exit. Even small vol expansion (VIX 16 → 20 ≈ 25% IV bump) or 1-2% spot dip materially improves marks before expiry. Mechanical-close ignores execution wisdom. But "wait for better" without rules drifts to expiry-by-default at the same bad mark — the textbook retail mistake. Both extremes are wrong; the discipline is rule-form middle ground.

**How to apply:** Before recommending cleanup of any near-dated theta-killer, surface execution-mark context (vol regime / IV percentile / spot vs recent range) in the recommendation itself. If mark is unfavorable, convert "close now" to a 3-piece framework:

1. **Pre-registered window-trigger menu** — ANY trigger opens the exit window (e.g., VIX intraday >20, SPY single-session ≤−2%, credit re-widening past inverse threshold, position-specific catalyst hot-print)
2. **Hard backstop date** (typically T-3 for short-dated, T-7 for longer) — theta floor; mechanical exit even at bad mark before delta-1 territory
3. **Loop closure in workbook** owed regardless of final exit mark — even if the answer is "we waited and ate it." Rule discipline is preserved by the framework, not by execution timing

This converts "wait and hope" into rule-form discipline. Applies to RED's adversarial recommendations to Will and to any agent surfacing position-cleanup recommendations. Canonical case: Session 11 EXIT-WINDOW FRAMEWORK (RED `STATUS.md` + `CALENDAR.md` POSITION EXIT-WINDOW BACKSTOPS + workbook `ML-RED-058`).
