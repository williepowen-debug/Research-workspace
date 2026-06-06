---
name: feedback-single-month-subcomponent-skepticism
description: "Single-month sub-component metric moves (ISM internals, CMBS by-property-type, single-trust ABS, single-print sentiment, etc) must be flagged \"needs 2nd-print confirmation\" before treating as load-bearing thesis evidence; rule applies regardless of magnitude"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 97a0fc9c-bf53-4fae-8e5d-2da56800198c
---

When integrating a print where a SUB-COMPONENT metric (ISM internals like New Orders / Prices Paid / Employment; CMBS DQ by-property-type; single ABS trust loss; single-month sentiment cohort; single Atlanta-Fed-Wage-Tracker cut; single-trust prepay/CNL; single-month bankruptcy filings YoY%, etc) moves sharply, flag it `[FLAG: single-month, needs 2nd-print confirmation]` in STATUS/KB before treating as load-bearing for a vector score, prediction confidence change, or thesis call. Magnitude alone does not earn load-bearing status; sustained 2-month direction does.

**Why:** Validated CARL Jun 5 2026. ISM Svc Apr 2026 New Orders -7.1pp single-month decel was treated as load-bearing stagflation sub-component anchor in late-May STATUS / KB-CARL-279 — FULLY REVERSED +3.8pp to 57.3 in May print one month later. Single-month sub-component move turned out to be noise, not signal. Pattern is generic: any sub-component of a composite index, sliced metric, or single-trust/single-cohort cut is noisier than the headline; cross-agent risk includes CFTC positioning (single-week noise vs trend), VIX Z-scores (single-day spike), wage tracker tier cuts (single-month tier shift), CMBS by-property (single-month +137bps without follow-on).

**How to apply:**
- Before any STATUS row update / VX status color change / KB row creation that treats a sub-component move as evidence, ask: "is this single-print or sustained?"
- If single-print: include explicit `[FLAG: single-month, needs 2nd-print]` text in Notes and DO NOT let it move a vector score or prediction confidence on its own
- Wait for 2nd print in same direction (any magnitude) OR a 3rd-source corroborating signal before promoting to load-bearing
- Composite headline moves (ISM headline, NFP headline, CPI headline) are NOT sub-components — this rule is for the slices and internals
- Sustained 2-month direction beats sharp 1-month magnitude. Direction at 2 months > magnitude at 1 month.

Related: [[finding_threshold_vs_mechanism]] separates mechanism intact from threshold breached; this rule prevents single-month thresholds from triggering false mechanism conclusions. Compounds with [[feedback_yoy_baseeffect_use_multiyear_stack]] (also a print-isolation discipline).
