# L920 independent read — candidate 2663082a0c (2026-11-04 21:14 ET)
Reader: one Opus read-only counterexample reader, spawned by PROME prome-b2. Episode read 1. Text below is the reader's return, verbatim.

**VERDICT: NOT ACCEPTED.** The 2e-7 tolerance is sound. What fails is the amendment's neighbour claims.

**Conditions 1–5: all pass at code.** Worst float32 gap 5.94e-8 across a 2M-price sweep, 0 refused. SPY, ^VIX, JPY=X and BTC-USD carry no session key.

**"Far below any tick": holds.** Tightest case is NQ at 27,000: tolerance 0.0054 against tick 0.25 (46×). BTC at 120,000: 0.024 against 5. YM at 45,000: 0.009 against 1. No wrong admission unless price/tick ≥ 5,000,000. A stale quote passes only at the same tick, as before.

**Counterexample 1, live (real price_fetch, /tmp copy, 21:1x ET, 6 rounds):** fetch.py:915 samples the quote, fetch.py:983 the chart, in separate requests. 14 of 66 pulls were refused, excluding ZB. BZF27 2/6: 93.99 vs 93.96. ES 4/6. A real move between requests is INFERRED. The refusal is safe, but the amendment's "concurrent activity = N/A, no shared state" is false. "Ordinary = serves a change" is UNVERIFIED: every pass was evening-next-session, withheld by design. Day session unmeasured; n is small.

**Counterexample 2:** ZB=F refused 6/6. Quote 108.84375, chart 108.8438 (vendor rounding, gap 4.6e-7). So "single precision" is not the only vendor gap (fetch.py:1514). No fleet config uses ZB.

**Re-pin:** nothing breaks. HEARTBEAT.md:10,32 still show BZZ26 $117.70, base 10/31. last_run.json has the new key yellow, the old key red: rename, no transition printed.

## PROME disposition
Code kept: the refusal of every named future is gone and conditions 1-5 pass at code. NOT called fixed. STILL UNRESOLVED: intermittent safe refusals on moving contracts between the two vendor requests; ZB-style vendor rounding beyond single precision; day-session behaviour unmeasured. No further edit tonight: this is the second correction pass on fetch.py today, so any further correction needs its own independent read inside the budget.
