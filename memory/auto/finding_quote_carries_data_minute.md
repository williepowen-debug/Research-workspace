---
name: finding-quote-carries-data-minute
description: "A quote carries its data-minute, not the wall-clock you wrote it down at. Two failure modes — mixed-timestamp ratios, and pull-time stamped as data-time on a delayed feed — both publish wrong-provenance \"live\" numbers. Intraday generalization of KB-VIO-092 (T-1 settle default)."
metadata: 
  node_type: memory
  type: finding
  originSessionId: 2f5f449d-ea73-441e-bfb6-559ab4498a45
---

A quote carries its **data-minute**, not the wall-clock minute at which it was transcribed. Two failure-mode variants both publish a "live" number with a wrong minute, and both showed up in one hour on VIOLET 2026-06-12:

1. **Mixed-timestamp ratio across per-index timestamps that don't co-occur.** `yf.download(['^VIX','^VIX9D',...])`-style batch pulls return whatever each ticker has cached individually — coherent for a table of single values, fiction for any ratio computed across them. VIX from a ~11:15 ET stale-cache snapshot @18.57 alongside VIX9D from the open @~21.42 produced an "implied" VIX9D/VIX = 1.1292 with NO coincident moment that day. Real coherent recompute (yfinance 1m bars, per-ticker `last_trade_time` verified inside one minute): 1.0494.

2. **Pull-time stamped as data-time on a delayed feed or stale-buffered pipeline.** Within the same hour the fix was registered, the cross-agent surface (NEXUS_BRIEF) was stamped "As of 12:30 ET" with values that were genuinely coherent but were the 11:59 ET data. The 30-minute delta isn't necessarily a feed-delay problem — it's the discipline of *carrying the source's observation timestamp through every write*, instead of overwriting it with `datetime.now()` at the point of transcription. Same failure class.

## Why this is the same finding as KB-VIO-092

KB-VIO-092 was the EOD/T-1 variant: `vix_futures.py` defaulted to `date.today()-1` because the official settle prints at 16:15 ET, and every VX_DAILY row got stamped with the *fetcher's row date* instead of the *settle's data date*. The intraday version is mechanically identical: per-tick (or per-bar) data carries its own minute, and the pipeline must propagate it. The siblings: **a value carries its date (092), a number carries its anchor (083), a duration carries its unit (085), and a quote carries its data-minute (this finding).** Provenance is part of the number.

## Mechanization (uniform across variants)

- Carry the source's `last_trade_time` / `observation_time` / `bar_close_time` through the entire pipeline, end-to-end.
- For batch pulls of multiple tickers, capture per-ticker timestamps. Refuse to compute ratios when constituent stamps span more than N minutes (or label `[MIXED-TS]`).
- For delayed or 1-minute-bar feeds, label `[DELAYED]` when wall-clock − data-time exceeds the feed's intrinsic latency.
- **Never** overwrite a data-time with `datetime.now()` when transcribing into state files, dashboards, or cross-agent surfaces.
- CBOE delayed_quotes JSON (`cdn.cboe.com/api/global/delayed_quotes/quotes/_VIX9D.json`) carries `last_trade_time` natively — viable reconciliation source for VIX-family ratios.

## Why the recurrence-in-one-hour fact matters

The lesson from variant (a) didn't transfer to the very next stamping action. Variant (b) was caught not by VIOLET re-reading her own work but by an external verifier (Orc) reading the cross-agent surface. **Without the verifier, the wrong stamp would have shipped to consumers** (HENRY, RED, NEXUS) who would have read a 30-min-stale tick as current. That is the cross-agent failure mode that makes this auto-memory-grade rather than just VIOLET-local KB-row-grade: the discipline has to live above the agent boundary, because a single agent can't catch its own provenance errors in the moment of writing.

## Where this shows up across the fleet

- **BROCK FRED pulls**: same class if `latest_print_date` is shadowed by `pull_date`. The FRED ALFRED API exposes vintage; use it.
- **HENRY equity batch fetches**: index OI, gamma surfaces, dark-pool prints — anything pulled across multiple tickers in one batch is exposed to variant (a).
- **SAM JGB / yen intraday**: cross-asset ratios (e.g. 10Y JGB yield × USDJPY) computed across feeds with different tick frequencies.
- **NEXUS_BRIEF stamps generally**: the cross-agent surface is the highest-leverage place to get provenance wrong, because downstream readers trust the As-of line and don't re-verify.

## Family pointer

Siblings: [[finding_circular_corroboration_via_state_file]] (state-file narrative re-derives wrong numbers; a number must come from raw series, not from prose about the series), [[feedback_verify_counts_before_propagating]] (any count/scope/staleness claim verified before propagating). The unifying rule: **provenance is part of the number; transcribing the number without its provenance is a transcription error.**

*Authored 2026-06-12 from VIOLET KB-VIO-100 + KB-VIO-101, Orc verification rounds 1 and 2. Mechanization owed to VIOLET's boot.py + cross-agent equivalents.*
