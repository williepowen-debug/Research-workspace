---
name: finding_ohlc_verify_before_session_claims
description: "Intraday print ≠ session verdict — verify daily-close OHLC before any \"Nth consecutive session\" / \"breached X\" claim; 2 same-day instances SAM 2026-06-09"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 1230f5e3-85b9-435c-977c-6181ff7d7818
  modified: 2026-07-29T15:10:22.558Z
---

An intraday fetch is a point-in-time tick, not a session verdict. Any claim of the form "Nth consecutive down/up session," "breached level X," or "cumulative −N% over the window" must be verified against daily-close OHLC history before propagation into state files or marks.

**Why:** Two same-day instances (SAM, 2026-06-09): (1) midday Brent $90.16 mid-slide recorded as "BREACHED $90, 4th consecutive down session, −7% cum" — evening OHLC showed the $89.59 tag didn't hold, Monday was an UP session; (2) the morning's USDJPY "4 consecutive days above 160" mis-parse (actual: 2 distinct tags with a dip between). Same failure family: treating a tick or a script-derived count as a session-state claim. Corrections had to sweep 6+ surfaces.

**Second-order extension (Orch independent re-pull, 2026-06-10): for futures, cite the official SETTLE, not an evening electronic quote.** The Jun-9 correction itself cited "$92.40 by evening" as the session verdict — but Brent futures trade nearly round-the-clock, so a post-settle "evening" read is the *next* session's tape. Official Tue Jun 9 settle was $91.45; settle-basis cum was −5.5% not −4.5%. Conclusions unchanged (no $90 closing breach either way), but the correction-of-the-correction shows the recursion: a "close" pulled from a live quote feed is still a tick. Verification grades also matter (Orch policy, same date): same-source-different-path (raw API vs own scripts) catches script-layer bugs; different-source (exchange/MOF/EIA) catches source-layer errors — internal-consistency checks against a shared pipeline are not independent verification.

**Third-order extension — THE LAST BAR IS THE SESSION IN PROGRESS, AND IT RE-DATES OVERNIGHT (BRENT, 2026-07-28/29).** Everything above is about ticks vs settles *within* a session. This is a different failure: **for near-24h futures, the most recent daily bar in a yfinance pull is the CURRENT session accumulating — and once it completes, the whole series re-labels.** BRENT pulled BZ=F at 21:15 ET on 7/28, read the last bar as *"7/28: open $84.95 = the session low, high $88.07, close $87.57,"* and built a reversal narrative on it ("opened at its low and closed +3.1% off it") that went into STATUS, a CHANGELOG entry, an auto-memory append and a report to the operator. **Re-pulled at 09:18 the next morning, the same source said 7/28 closed $84.09 with a low of $82.51 — and the bar previously labelled 7/28 was now labelled 7/29**, because the 7/29 session opens at 18:00 ET on 7/28. **Consequences: the reported peak-to-trough was −15.6% when the truth was −18.1%, and the "reversal bar" belonged to a different calendar day than the events it was being used to explain.**

**The tell that should have fired:** the pull happened at **21:15 ET — after the 17:00 close and after the 18:00 reopen** — so the "latest daily bar" could not have been a completed session. **Any futures pull between the evening reopen and the next afternoon's settle is reading an in-progress bar.** *(Related but distinct from [[finding_tool_default_asof_date_drift]] and [[finding_yahoo_sparse_index_date_shift]]: nothing was stale or missing here — the data was correct and the LABEL moved.)*

**Extra apply-step:** when a claim depends on which calendar day a move happened on, **print the dated OHLC table and read the date column** rather than taking `.iloc[-1]`; and **re-pull the prior session the next morning before letting an evening-derived bar stand** in any durable surface. Cheap tell: if your "today's close" was pulled after 18:00 ET, it is tomorrow's open.

**How to apply:** Before writing any session-count/breach/cumulative claim: pull daily OHLC for the window (yfinance or source-of-truth), check each session's close direction, compute cumulative from the documented baseline. For futures, the session verdict is the official settle. Intraday extremes are reportable as "tagged X intraday, did/didn't hold." Pairs with [[finding_thin_liquidity_prediction_market_discipline]] (single print ≠ regime) and the script-semantics rule in [[finding_number_carries_threshold_unit_source]].
