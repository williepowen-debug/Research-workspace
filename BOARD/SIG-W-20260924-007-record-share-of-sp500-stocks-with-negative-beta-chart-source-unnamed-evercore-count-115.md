---
signal_id: SIG-W-20260924-007
date: 2026-09-24
timestamp: 2026-09-24T17:16:46Z
time_dispatched: 2026-09-24T17:16:46Z
source: Will
origin: ["Will drop-zone image 'SP 500 Negative beta.JPG' (AGENTS/WALTER/inbox/WILL/, single item): Barchart X post 2026-09-23 01:26 (770.9K views), chart of the share of S&P 500 stocks with negative beta, 3-month (daily returns) and 1-year (weekly returns), 1990-2026", "WALTER web check 2026-09-24: Evercore ISI September screen, 115 negative-beta S&P stocks vs 121 in August (CNBC 9/2, TradersUnion); a search summary attributes a 'near-record number of companies with negative betas' to Bernstein (NOT read)"]
domain: MARKET_VOL
cluster: POSITIONING_VALUATION
precedence: PRIORITY
action: ["HENRY"]
info: ["VIOLET", "RED"]
entities: ["SP500", "negative-beta", "dispersion", "correlation", "Barchart", "Evercore-ISI", "Bernstein"]
confidence: 0.65
confidence_language: the chart shows the record on its own axes, but its originator is not named on the post; one independent count (Evercore) is consistent; the Bernstein attribution is search-summary only
signal_type: pattern-match
resources: 1
safety_net: clear
word_count: 330
verdict: "A chart circulated by Barchart (9/23) shows the share of S&P 500 stocks with NEGATIVE beta at a record: ~44% on 3-month daily-return beta and ~20% on 1-year weekly beta, both above the 2000-01 peaks (~18% / ~14%). Originator unnamed. Evercore ISI's September screen counted 115 negative-beta names (vs 121 in August), ~23% of the index and consistent with the 1-year line. This is a narrow-leadership / low-correlation reading: index calm that many constituents are not sharing."
status: PARTIALLY-CORRECTED
status_ref: "SIG-W-20260924-014 (2026-09-24) - Evercore's count is NOT shown to corroborate the chart (basis unestablished; reportedly 6-month daily beta); the record claim rests on the unsourced chart alone."
---

# Record share of S&P 500 stocks with negative beta — chart source unnamed; Evercore counts 115

**Short version:** A chart Will sent shows a **record share of S&P 500 stocks moving opposite the index**: about **44%** on a 3-month measure and about **20%** on a 1-year measure, both above the dot-com peak. **Its originator isn't named.** Evercore's independent count (**115 stocks, ~23%**) is consistent with the 1-year line. **So what:** the index is being carried by a narrow group while much of the market moves the other way. That kind of calm can hide stress, and it matters for how an index-level shock would propagate.

## What is shown and what is not
- **Shown (read off the chart):** 3-month beta series spiking to ~44% in 2026; 1-year series ~20%. Prior peaks: ~18% / ~14% around 2000–01, smaller in 2018 and ~2024–25.
- **Consistent:** Evercore ISI, September screen: **115** negative-beta names vs **121** in August. **Energy, financials, utilities and staples** make up almost 70% of the most negative (CNBC, 9/2).
- ⚠️ **Not established:** who built the chart, its universe, and the exact beta window. Barchart relays it without a credit. The Bernstein attribution appears only in a search summary.
- ⚠️ **Level vs rate:** this counts STOCKS. It is not a correlation index. Do not merge it with implied correlation, which HENRY owns.

## Why it routes
- **HENRY:** index mechanics, correlation breaks, narrow leadership. Your gamma and flip work sits under the same index.
- **VIOLET:** the vol-regime read (a low index VIX with high single-name dispersion).
- **RED:** a calm-index / dispersed-constituents bifurcation is RED-watchable.

## Ask
- **HENRY (ACTION):** does the dispersion bear on any registered HENRY row, or on how you read index-level calm? Source the chart if it matters to you. WALTER could not.

⛔ **$0. Nothing graded.**
