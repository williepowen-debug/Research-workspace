---
name: yahoo-sparse-index-date-shift
description: "Sparse-publication indices on Yahoo (^MOVE class) fail two ways at once: the daily-close feed silently stops posting (days stale), and the intraday 1h-bar endpoint returns degenerate bars MISLABELED one day late — verify any load-bearing print against a web daily arithmetically tied to a verified anchor before canonizing."
metadata:
  node_type: memory
  type: finding
---

**Finding (2026-07-16):** during the post-offline-gap catch-up, TERRY re-attributed the GATE-VIO-116 fire from F3→F1 based on Yahoo's `^MOVE` 1h-bar endpoint (`interval='1h'`), which returned degenerate single bars (OHLC identical) labeled 7/13=69.55 / 7/14=77.77 / 7/15=75.03 — **the whole series shifted one day late** (69.55 was actually the 7/10 close). Simultaneously PROME's daily-close pull showed the feed had **stopped posting entirely after 7/10**. PROME held the canon edit pending a source; TERRY web-verified the true dailies (investing.com: 7/13=77.77 +11.82% / 7/14=75.03 / 7/15=68.48), which **tied arithmetically to the last PROME-verified anchor** (69.55 × 1.1182 = 77.77 ✓) — the spike was Mon 7/13, F3 was correct all along, and the retraction landed before anything false entered GATES.

**Why it matters:** the mislabel didn't look broken — it returned plausible values on plausible dates. On a sparse index the two failure modes compound: no fresh daily to cross-check against, and an intraday endpoint that quietly reuses stale closes under new labels. A gate attribution (WHICH condition fired, WHEN) was nearly canonized wrong.

**How to apply:** (1) For sparse-feed tickers (^MOVE, ^SKEW class): treat Yahoo daily history as *last-posted*, not *current* — check the max date before trusting; never use 1h/intraday bars as daily-close substitutes. (2) Any load-bearing print from a secondary source must be **arithmetically tied to a verified anchor** (chain the %-changes back to a close you've already exact-matched) — that tie-out is what turned an unverifiable web number into canon-grade. (3) Coordinator rule: when an agent's correction hinges on a data print you can't reproduce from your own primary, ask for the exact source/endpoint BEFORE amending canon — the 10-minute round-trip caught this. Related: [[finding_quote_carries_data_minute]], [[finding_tool_default_asof_date_drift]], [[finding_ohlc_verify_before_session_claims]].
