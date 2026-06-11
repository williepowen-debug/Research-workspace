---
signal_id: SIG-W-20260419-008
precedence: PRIORITY
timestamp: 2026-04-19T18:30:00Z
source: WALTER
origin: "X.com post by Data Driven Stocks (@stockdatamarket, verified) Apr 17 2026 4:12 PM, 77K views. Statistical claim: 'The S&P 500 just experienced its biggest rally of the century that lasted 13 days - an event with only a 0.63% probability of occurring. To put that into perspective, that's roughly a 1 in 160 chance — similar to flipping a fair coin and getting heads 7 times in a row.' Embedded image: 3-panel rolling-return distribution chart (5-day / 10-day / 13-day) labeled 'S&P 500 — Rolling Return Distributions & Probability Analysis,' with annotation 'Probability is 12.20%' visible on one panel and 'Mar 30 - Apr 17 Event' marked. Intaken via Will Telegram batch 2026-04-19 18:15 UTC."

to: HENRY (ACTION — MARKET_VOL primary)
info: RED, LIQUID, NEXUS
group: VOL
dispatched: 2026-04-19T18:30:00Z
dispatch_note: "Author-asserted statistical extremity claim. The 0.63% / 1-in-160 number is methodology-dependent (depends on baseline period, rally definition, what 13-day metric — chart shows 12.20% on one panel inconsistent with 0.63% in tweet text, suggesting the headline number may pull from a different conditional than the chart shows). Routing PRIORITY (not IMMEDIATE) — directionally consistent with the BOARD positioning-extreme cluster (HF cover, NDX RSI, SKEW divergence, VOLET POSTURE, Buffett 232%, Wyckoff, NDX parabolic). Lands as cluster-augmentation channel, not standalone trigger. Methodology caveat in body."

signal_type: pattern-match
confidence: 0.55
confidence_language: possible
resources: 0
safety_net: clear

word_count: 280

# cluster backfilled 2026-06-10 from INDEX section placement (pre-v0.7 signal; cluster field added to FORMAT_SPEC 2026-05-05)
cluster: POSITIONING_VALUATION
---

## Signal

**Data Driven Stocks (@stockdatamarket) Apr 17 2026 statistical claim:**

- SPX 13-day uninterrupted rally Mar 30 – Apr 17 2026
- Author-computed probability: **0.63%** (1 in 160; "7 heads in a row" analog)
- Embedded chart: 5-day / 10-day / 13-day rolling return distribution histograms with current event marked

**Internal inconsistency:** Tweet text says 0.63% probability, but the chart annotation visible in the image shows "Probability is 12.20%" on one panel. The 12.20% may be the 5-day stat and 0.63% may be the 13-day stat (consistent with the headline framing), but the screenshot doesn't make this clean. **Treat 0.63% as author-asserted, not visually verified.**

## Relevance

- **HENRY (ACTION):** MARKET_VOL primary. Extremity-of-rally claim adds a positioning-stretch data point distinct from the vol-side observations (VIOLET) and the breadth observations (-003, -009 below). If even directionally accurate, adds to the case that recent SPX strength is statistical-tail rather than regime-shift.
- **RED (info):** Counter-case fodder. Steelman: probability framing is highly sensitive to definition — "biggest rally of the century" is ambiguous (which century, which gain magnitude, which baseline). 0.63% claims about market moves are common in author-defined frameworks and rarely survive replication.
- **LIQUID (info):** Surface-level rally consuming positioning fuel; relevant to amplification-on-reversal channel.
- **NEXUS (info):** **10th node** in the valuation/positioning convergence cluster. Each node individually is weak; the *number* of independent observations pointing the same direction is the convergence signal.

## Caveats

- **Author-asserted statistic.** 0.63% is not from a primary methodology source — it's the author's computation. Verify-research not spawned this batch (cluster-augmentation framing tolerates the lower-confidence input).
- **Chart-text inconsistency.** 12.20% vs 0.63% — one is 5-day, one is 13-day, but unclear from crop. Don't quote the 0.63% number as a fact downstream — quote it as a *claim*.
- **Survivorship of 'biggest rally' framing.** A 13-day uninterrupted rally is unusual but the magnitude-equivalent metric (% gain over 13 days) determines actual extremity. Without the magnitude, the framing alone may be cherry-picked.
- **77K views = high attention.** This claim is propagating; expect to see it cited downstream regardless of methodology rigor.

## Source

- @stockdatamarket X.com post, 4:12 PM 4/17/26, 77K views
- Embedded chart: "S&P 500 — Rolling Return Distributions & Probability Analysis" 5/10/13-day panels
- Intake: Will via Telegram screenshot, 2026-04-19 18:15 UTC
