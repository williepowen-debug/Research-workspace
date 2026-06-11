---
signal_id: SIG-W-20260419-023
precedence: PRIORITY
timestamp: 2026-04-19T23:02:00Z
source: WALTER
origin: "@Barchart X/Twitter post screenshot (image #5 in Will Telegram PM-5 batch, 2026-04-19 22:44 UTC). Post text: 'Options Traders are the most bullish on the Stock Market since 2021 after the Total Put/Call Ratio plunged to 0.66' plus chart emojis. Embedded chart: $CPC 1D from ~Jan 2021 through Feb 2026, range 0.60-2.00, most recent print marked at 0.66 with red dashed reference line. Timestamp: 2:19 AM · 4/19/26 · 51K Views · 27 replies / 98 RT / 485 ❤️ / 76 bookmarks. Account: @Barchart, verified. Intaken via Will Telegram batch 2026-04-19 22:44 UTC."

to: HENRY (ACTION — MARKET_VOL / positioning primary)
info: RED, LIQUID, NEXUS
group: ROUTINE_PLUS
dispatched: 2026-04-19T23:02:00Z
dispatch_note: "@Barchart: Total CPC (Put/Call Ratio) at 0.66 — reported as most bullish since 2021. CPC 0.66 means 66 puts traded per 100 calls = call-volume dominance = aggressive bullish positioning. Historically contrarian: extremes below 0.7 have preceded short-term pullbacks more often than not, though timing is unreliable. Chart visual confirms 0.66 is at bottom-of-range for the 5-year window — matches 'most bullish since 2021' claim (2021 had multiple sub-0.70 prints during meme-stock phase). Direct cluster-augmentation signal: 5TH CHANNEL in positioning pillar (alongside HF cover Apr 14, DB financials gap, BofA MMF outflow, S3 $93B cover). HENRY primary for regime read. RED info — steelman fuel (CPC extremes have unreliable timing; 2021 stayed bullish for MONTHS before cracking). LIQUID info — positioning-heavy markets amplify unwinds. NEXUS info for cluster integration (positioning pillar now = 5 channels, arguably cluster's strongest). Confidence 0.78 — Barchart is reliable data source, CPC is standard metric, chart visual confirms claim."

signal_type: threshold-crossed
confidence: 0.78
confidence_language: likely
resources: 0
safety_net: clear

word_count: 290

# cluster backfilled 2026-06-10 from INDEX section placement (pre-v0.7 signal; cluster field added to FORMAT_SPEC 2026-05-05)
cluster: POSITIONING_VALUATION
---

## Signal

**@Barchart (verified, 2026-04-19 2:19 AM ET, 51K views):**

> "Options Traders are the most bullish on the Stock Market since 2021 after the Total Put/Call Ratio plunged to 0.66"

Embedded chart: $CPC (Total Put/Call Ratio) 1D, window Jan 2021 → Feb 2026, latest print 0.66 marked at red dashed floor. Visual confirms 0.66 is at low end of 5-year range; comparable prints only in 2021 (meme-stock peak window).

### Reference
- **CPC = CBOE Total Put/Call Ratio.** Ratio of put option volume to call option volume across all US equity options.
- **Interpretation:** CPC > 1 = more puts than calls (bearish/hedged). CPC = 1 neutral. CPC < 0.70 = aggressive call-dominance, historically a contrarian short-term signal.
- **Typical range:** 0.70-1.10 baseline; extremes below 0.70 or above 1.50 are tails.
- **2021 comparison:** Multiple sub-0.70 prints during 2021 meme-stock / retail YOLO phase. Market continued higher for months AFTER those prints before 2022 drawdown — so CPC extremes have unreliable short-term timing.

## Relevance

- **HENRY (ACTION):** MARKET_VOL / positioning. Direct cluster-augmentation — positioning pillar now 5 channels: (1) HF short cover Apr 14 (SIG-006), (2) DB financials gap (SIG-008), (3) BofA MMF outflow (SIG-016), (4) S3 $93B short cover MTD (SIG-018), (5) CPC 0.66 options-bullish extreme. All 5 point same direction. Positioning has become the cluster's STRONGEST pillar (vs 4 implied-vol channels, 2 valuation, 2 breadth mid/long-horizon, 2 Iran/oil, 1 small-biz credit, 1 foreclosure).
- **RED (info):** Steelman material — CPC extremes have UNRELIABLE short-term timing. 2021 had multiple sub-0.70 prints while market continued to new highs for 6-9 months. Extreme positioning is not a reliable timing signal, only a condition-of-risk indicator. Also: CPC captures option-volume only, not equity flow; market-maker hedging distorts the ratio.
- **LIQUID (info):** FUNDING — positioning-heavy markets amplify unwind. If short-dated call-buying is a big share of the 0.66 print, gamma-unwind pressure is latent.
- **NEXUS (info):** Cluster integration — positioning pillar grows to 5 channels. Consider for cluster-classification ask. Cluster now has both positioning-EXTREME (this signal + 4 others) AND positioning-MODEST-flow (SIG-019 LTM equity flows only 0.4% AUM) — NOT a contradiction: tactical/options positioning is extreme, strategic/retail AUM flows are modest. Two different time horizons and two different investor sets.

## Caveats

- **CPC extremes have unreliable TIMING.** Market can stay at sub-0.70 CPC for extended periods (2021 meme window: 6+ months of recurring sub-0.70 prints before 2022 reversal). Positioning extreme is a condition-of-risk, NOT a timing trigger.
- **Total CPC includes INDEX options + EQUITY options.** Equity-only (CPCE) is typically a better retail-speculation proxy; Index CPC is partially hedge-driven. Total CPC 0.66 could be partially driven by lower put-hedging on indices (different than retail call-YOLO).
- **Market-maker dynamics.** CPC ratio does not show whether trades are OPENING or CLOSING positions — opening short-dated calls = aggressive bullish; closing short puts = defensive-turning. Directionality inferred, not directly measured.
- **Single-day print.** CPC is noisy daily; 5-day or 10-day SMA is more signal-robust. Single 0.66 print could mean-revert in next session.
- **Barchart chart window 2021-2026 hides pre-2021 context.** Pre-2021 CPC regularly printed below 0.66 in 2017-2018 low-vol regime. "Most bullish since 2021" is true but not necessarily historically unprecedented.
- **2:19 AM ET posting time** = end-of-day Apr 18 data, presumably. By market open Apr 21 this print will be 2 trading sessions stale.

## Source

- @Barchart post on X (verified account)
- URL: x.com/Barchart/status/... (not captured in image)
- Post timing: 2026-04-19 2:19 AM ET
- Data: CBOE Total Put/Call Ratio ($CPC), 1-day
- Image #5 of Will Telegram PM-5 batch, 2026-04-19 22:44 UTC
- Primary source: cboe.com options market statistics
