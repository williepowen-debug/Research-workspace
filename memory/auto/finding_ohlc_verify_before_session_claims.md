---
name: finding_ohlc_verify_before_session_claims
description: "Intraday print ≠ session verdict — verify daily-close OHLC before any \"Nth consecutive session\" / \"breached X\" claim; 2 same-day instances SAM 2026-06-09"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 1230f5e3-85b9-435c-977c-6181ff7d7818
---

An intraday fetch is a point-in-time tick, not a session verdict. Any claim of the form "Nth consecutive down/up session," "breached level X," or "cumulative −N% over the window" must be verified against daily-close OHLC history before propagation into state files or marks.

**Why:** Two same-day instances (SAM, 2026-06-09): (1) midday Brent $90.16 mid-slide recorded as "BREACHED $90, 4th consecutive down session, −7% cum" — evening OHLC showed the $89.59 tag didn't hold, Monday was an UP session; (2) the morning's USDJPY "4 consecutive days above 160" mis-parse (actual: 2 distinct tags with a dip between). Same failure family: treating a tick or a script-derived count as a session-state claim. Corrections had to sweep 6+ surfaces.

**Second-order extension (Orch independent re-pull, 2026-06-10): for futures, cite the official SETTLE, not an evening electronic quote.** The Jun-9 correction itself cited "$92.40 by evening" as the session verdict — but Brent futures trade nearly round-the-clock, so a post-settle "evening" read is the *next* session's tape. Official Tue Jun 9 settle was $91.45; settle-basis cum was −5.5% not −4.5%. Conclusions unchanged (no $90 closing breach either way), but the correction-of-the-correction shows the recursion: a "close" pulled from a live quote feed is still a tick. Verification grades also matter (Orch policy, same date): same-source-different-path (raw API vs own scripts) catches script-layer bugs; different-source (exchange/MOF/EIA) catches source-layer errors — internal-consistency checks against a shared pipeline are not independent verification.

**How to apply:** Before writing any session-count/breach/cumulative claim: pull daily OHLC for the window (yfinance or source-of-truth), check each session's close direction, compute cumulative from the documented baseline. For futures, the session verdict is the official settle. Intraday extremes are reportable as "tagged X intraday, did/didn't hold." Pairs with [[finding_thin_liquidity_prediction_market_discipline]] (single print ≠ regime) and the script-semantics rule in [[finding_number_carries_threshold_unit_source]].
