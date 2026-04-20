---
signal_id: SIG-W-20260420-010
precedence: PRIORITY
timestamp: 2026-04-20T23:34:00Z
source: WALTER
origin: "Will Telegram image 2026-04-20 23:03 UTC (msg 954). Screenshot of Deutsche Bank Asset Allocation note content (Binky Chadha team presumed), data labeled 'as of 16-Apr-2026.' Chart = Figure 73 'Total net call volume (5d ma, thousands) — Calls minus puts.' Source line: CBOE, Haver Analytics, Deutsche Bank Asset Allocation. Image format suggests repost/aggregator, not direct DB terminal pull. Primary DB note NOT obtained (subscription-gated inside-research.db.com, verify sub-agent could not access)."

to: HENRY (ACTION — MARKET_VOL / positioning cluster-refinement)
info: RED, LIQUID, NEXUS, REGINALD
group: ROUTINE_PLUS
dispatched: 2026-04-20T23:34:00Z
dispatch_note: "DB Asset Allocation claims: total net call volume (5d MA) ~2M contracts = highest on record, +400k above post-Liberation-Day peak; equity call/put ratio 1.50 = highest since 2020 recovery; higher only 5% of time in 16 years; +36% above 2005-avg ~1.10; 'frenzy bigger than 2021 meme mania.' Follow-up to SIG-W-20260419-023 (Barchart CPC 0.66 most bullish since 2021) — same underlying phenomenon (call-dominance extreme), DB adds structural/historical percentile context and absolute-volume dimension. VERIFY-RESEARCH VERDICT: INDETERMINATE (leaning CONFIRMED-directional). Primary DB note unverified (subscription-gated). CBOE primary data (YCharts Apr 14-17) corroborates DIRECTION: equity P/C 0.41-0.50 well below historical ~0.65 norm; Nasdaq call volume ~3.9M contracts/day reported 'second-highest ever.' Specific DB numbers (2M 5dMA, 1.50 C/P, 5%/16yr, +36%) NOT independently verified. Confidence lowered from initial 0.80 target → 0.65 assessed to reflect unverified-specifics."

signal_type: context
confidence: 0.65
confidence_language: assessed
resources: 0
safety_net: clear

word_count: 445
---

## Signal

**Deutsche Bank Asset Allocation note (secondhand, data as of 2026-04-16):**

> Total net call volume (calls minus puts, 5d MA) surged to ~2,000,000 contracts, the highest on record. Exceeds post-Liberation-Day recovery by ~400,000. Equity call/put ratio rose to 1.50, highest since 2020 crisis recovery. Over 16 years, call/put ratio higher only 5% of the time. Long-term avg since 2005 is ~1.10, current ~+36% above historical norm. "Frenzy bigger than 2021 meme mania."

Chart label: Figure 73, "Total net call volume (5d ma, thousands) — Calls minus puts," Jan 2024 → ~Apr 2026, spike at right margin circled. Sources cited: CBOE / Haver Analytics / Deutsche Bank Asset Allocation.

### Verify-research verdict

**INDETERMINATE (leaning CONFIRMED-directional).** WALTER spawned verify-research sub-agent prior to dispatch (Phase 1.5 trigger pattern (a) — secondhand citing primary DB note, not direct terminal pull). Sub-agent findings:

- **Directional support from primary CBOE data:** YCharts CBOE equity put/call ratio Apr 14–17 2026 = 0.41–0.50, 24% below YoY and near low end of multi-year range. Direction (extreme call-dominance / bullish positioning) holds against primary source.
- **Methodology note:** CBOE equity P/C 0.41–0.50 translates to C/P ~2.0–2.44, which is numerically MORE extreme than DB's claimed 1.50 C/P. The two measurements are not directly comparable (5-day MA vs. daily spot, total-market vs. equity-only, etc.) but both read "record-extreme call dominance."
- **Corroborating reporting:** Nasdaq call volume ~3.9M contracts/day reported "second-highest ever" (MEXC citing public data). Chadha Apr 2026 bullish-positioning commentary is on record (Sherwood, CNBC, Schafer Mar/Apr 2026).
- **NOT verified:** Primary DB note with Figure 73; specific "2M contracts 5d MA highest on record"; "1.50 highest since 2020"; "+400k vs post-Liberation"; "5% of time in 16yrs"; "+36% above 2005 avg ~1.10." DB Asset Allocation is subscription-gated.

Verdict handling per FILTER_SPEC: route with lowered confidence, signal-body flags unverified framing. Originally would have landed at `reports` 0.80; INDETERMINATE adjusts to `assessed` 0.65 — specifics unverified but directional story primary-source-corroborated.

## Relevance

- **HENRY (ACTION):** MARKET_VOL / positioning. Cluster-refinement, not new pillar. SIG-W-20260419-023 already routed the TOTAL CPC 0.66 "most bullish since 2021" framing to HENRY as channel 5 in the positioning pillar. This DB note is the **structural/percentile-context overlay** on that same phenomenon — says the current extreme is not just "most bullish since 2021" (point-in-time comp) but "top 5% of all readings in 16 years" (historical percentile) and "+36% above long-term average" (structural deviation). Same direction as SIG-023; adds percentile calibration useful for probability-weighting, not a new channel.
- **RED (info):** Probability-weighting input. DB's 16-year-5%-percentile framing gives RED a historical-base-rate number for positioning-extreme → forward-return analysis. PAIRS WITH SIG-W-20260419-017 (Bilello VIX/SPX extremity 3-wk counter-channel — "avg fwd returns +22%/+48%/+58% at 6m/1Y/2Y"). Positioning extreme is a condition-of-risk, not a timing signal. Note: sub-0.70 CPC in 2021 persisted 6+ months before cracking — DB's "bigger than 2021 meme mania" framing if accurate implies the 2021 comparison is on volume, not ratio.
- **LIQUID (info):** FUNDING / amplification. Record absolute call volume (~2M 5dMA per DB) means dealer short-gamma exposure is elevated. Gamma-unwind pressure latent if/when positioning reverses.
- **NEXUS (info):** Cluster integration. Does NOT add a new channel — refines pillar 5 (positioning) already-documented via SIG-023. Cluster node count unchanged (13 at last NEXUS update, pending).
- **REGINALD (info — added vs SIG-023 routing):** Equity-side positioning context for the Apr 21 WAL/ZION earnings read. If options-positioning is at 16-year extreme call-dominance into a high-expectation earnings print, any miss transmits more aggressively via gamma unwind. Not action-required, context overlay.

## Caveats

- **Specifics unverified.** The primary DB Asset Allocation note was not obtained. CBOE data direction-confirms but does not confirm DB's specific numerics. If the "1.50 highest since 2020" claim is wrong by a wide margin or DB's 5dMA methodology differs from how CBOE publishes, the percentile framing is suspect. REGINALD/HENRY should treat the STORY as corroborated and the NUMBERS as approximate.
- **Liberation Day reference is ambiguous.** "Post-Liberation-Day recovery" could refer to either the Apr 2024 rally window or the Apr 2, 2025 tariff-"Liberation Day" framing (and its post-shock recovery). Context suggests the latter (more recent + relevant to 2026 comparison window). Not dispositive to the signal.
- **Measurement inconsistency with SIG-023.** SIG-023 was TOTAL CPC 0.66 (put/call). This is EQUITY-only C/P 1.50 (call/put). 1/1.50 = 0.667 ≈ SIG-023's 0.66 for total. Consistent, but measurement-conflation risks overstating the convergence if reader treats them as independent.
- **Timing caveat carries over from SIG-023.** Positioning extremes have unreliable timing. 2021 meme-window sub-0.70 CPC persisted through multiple new all-time highs before the 2022 reversal. "Condition-of-risk" ≠ "timing trigger."
- **Single-image source.** WALTER did not pull DB primary. Image is formatted like a Twitter/Threads repost of DB research. Origin integrity subject to the repost faithfulness.

## Source

- Will Telegram image message 954, 2026-04-20 23:03 UTC
- Chart: "Figure 73: Total net call volume (5d ma, thousands) — Calls minus puts"
- Source line: CBOE, Haver Analytics, Deutsche Bank Asset Allocation
- Data as of: 2026-04-16
- Primary DB note: NOT obtained (inside-research.db.com subscription-gated)
- Primary-data corroboration: YCharts CBOE Equity Put/Call Ratio https://ycharts.com/indicators/cboe_equity_put_call_ratio
- Chadha positioning commentary: Josh Schafer X https://x.com/_JoshSchafer/status/1993451753162129720 ; Sherwood https://sherwood.news/markets/one-of-wall-streets-biggest-bulls-on-what-to-expect-in-2026/
- CBOE Mar 2026 volume report: https://ir.cboe.com/news/news-details/2026/Cboe-Global-Markets-Reports-Trading-Volume-for-March-2026/default.aspx
- Related prior signals: SIG-W-20260419-023 (Barchart CPC 0.66), SIG-W-20260419-017 (Bilello VIX/SPX extremity counter), SIG-W-20260416-003 (equity internals NDX RSI / SPX breadth), SIG-W-20260419-018 (triple short-squeeze)
