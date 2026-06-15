---
name: feedback_henry_macro_focus_not_positions
description: "HENRY focus is macro + market trends, NOT trade-position management; Will's open trade positions (TLT puts etc.) are retired as dead/closed"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 7a815061-eba9-40b2-aaed-ac5dc571ec3e
---

Will 2026-06-15: "Consider these trading positions either dead (no value) or closed out. I don't want us to focus on them and instead focus on macro and market trends."

Directive: HENRY stops doing position-management (close/hold/roll calls, TLT Jun/Sep $85P decisions, WILL_NEEDS position asks). Will's open trade positions are treated as dead/closed — do not track P/L, expiry decisions, or exit timing for them.

**Why:** Will wants HENRY's bandwidth on macro-regime and market-trend reads (cascade mechanics, vol regime, credit transmission, data releases, thresholds, cross-agent macro signals), not on managing specific options legs that have decayed.

**How to apply:** Keep market indicators that double as position-relevant (10Y/TLT = duration channel, APO = alts/private-credit proxy) but frame them as *market-trend reads*, not position decisions. Drop "Will's $85P strike / OTM / decision point / defer-to-mark" language. Cross-agent signals about OTHER agents' positions (e.g. APO→BROCK put-trigger) become FYI cross-reads, not action items. Supersedes the position-decision emphasis in prior closeouts. Related: [[feedback_exit_recommendations_need_mark_context]] (still applies IF positions ever return to focus).
