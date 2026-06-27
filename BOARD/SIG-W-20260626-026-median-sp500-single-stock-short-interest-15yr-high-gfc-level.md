---
signal_id: SIG-W-20260626-026
dispatched: 2026-06-27T00:32:00Z
origin: Will-Telegram image batch 2026-06-27 (re-send, 6/8-dated) — Ryan Detrick (@RyanDetrick) citing @JC_ParetsX
source: Ryan Detrick / Carson Group, X post 9:28 PM 6/8/26 (9.8K views) — chart "Median Single Stock Short Interest Within S&P 500 Index — highest reading in over 15 years" (Bloomberg; median stock short interest as % of market value, monthly)
signal_type: pattern-match
domain: MARKET_VOL
cluster: POSITIONING_VALUATION
cluster_secondary: n/a
signal_role: cluster_mediating
narrative_channel: n/a
precedence: PRIORITY
to: HENRY
info: [RED, TERRY]
confidence: 0.70
verify_verdict: SKIP-VERIFY 0.70 — Detrick/Carson is a credible, non-hyperbolic source (contrast SIG-W-20260604-008's 0xChainMind aggregate-SI claim, which earned CORRECTED-FRAMING). ~3wk stale (6/8 post = mid-May settlement data); distinct metric from the aggregate index short interest. Two-sided read.
verify_method: none (credible curator + Bloomberg chart; HENRY/RED weight).
routing_note: positioning extreme (median single-stock short interest) → HENRY action. RED info (cluster_mediating — two-sided bear-vs-squeeze). TERRY info (positioning extreme → squeeze-risk on any short, bears on sizing/timing per ROUTING_TABLE v0.13). cluster POSITIONING_VALUATION. DISTINCT from SIG-604-008 (aggregate index SI ~3.0%) — this is the MEDIAN single stock = breadth/dispersion of shorting.
---

# Median S&P 500 single-stock short interest = highest in ~15 years (last seen mid-GFC) (HENRY)

**One line:** Per Ryan Detrick (citing @JC_ParetsX, 6/8): the **median** stock in the S&P 500 now has the **highest short interest as a % of market cap in ~15 years** — "the last time it was up around here was in the midst of the GFC." Breadth of shorting is GFC-level: shorts are spread broadly across the index, not concentrated in a few names.

> **GRADE: SKIP-VERIFY 0.70, cluster_mediating.** A genuinely DISTINCT cut from the aggregate-index short-interest we already hold (SIG-604-008, ~3.0%, CORRECTED-FRAMING) — this is the *median single stock*, i.e., dispersion/breadth of shorting. Source is credible (Detrick, non-hyperbolic). Caveats: ~3wk stale (mid-May settlement); inherently **two-sided** (broad bearish positioning vs broad squeeze fuel).

## Per-recipient genuine delta

### → HENRY (ACTION) — a breadth metric, not the aggregate
SIG-604-008 was the *aggregate* index short interest (~3.0%, and the "3.8%/2008-analog" framing got corrected). THIS is the **median single stock** — a breadth read: the typical S&P name is more heavily shorted than any time since the GFC. That's a different signal (dispersion of bearish positioning), and it pairs the froth/positioning thread from the short side. Two-sided: max-broad-short is both a bearish-positioning tell AND classic squeeze fuel on any risk-on rip.

### → RED (INFO) — cluster_mediating / adversarial
The contrarian read is at least as strong as the bearish one: "highest since the GFC, broadly shorted" = crowded shorts that unwind violently on good news (the SOXS/SOXL washout SIG-622-009 is the same family). Also, median-SI elevation can partly reflect index composition (more shortable/expensive names) rather than pure bearishness. Distinct from the aggregate-SI 604-008 you flagged — log as a separate, two-sided positioning datapoint.

### → TERRY (INFO)
Positioning extreme → **squeeze-risk** on any single-name or index short: broad GFC-level short interest means a sharp upside reversal can force-cover hard. Bears on sizing + invalidation on the short side (size for squeeze risk; don't add into a washout). ~3wk stale — confirm current SI before acting.

## Sources
- Ryan Detrick (@RyanDetrick), Carson Group, X 9:28 PM 6/8/26 (9.8K views): "As @JC_ParetsX noted today, the median stock in the S&P 500 has the highest short interest as a % of market cap in about 15 years. In other words, the last time it was up around here was in the midst of the GFC." Chart: "Median Single Stock Short Interest Within S&P 500 Index — highest reading in over 15 years" (Bloomberg; median stock SI as % of market value, monthly, ~1995–2026). Re-send; data as of ~mid-May (6/8 post).
