---
signal_id: SIG-W-20260419-005
precedence: PRIORITY
timestamp: 2026-04-19T17:55:00Z
source: WALTER
origin: "X.com screenshot intaken via Will Telegram batch 2026-04-19 17:41 UTC. Author/handle not captured in screenshot crop; chart shows Wilshire 5000 / GDP ratio at 232.6% labeled ATH, surpassing dot-com bubble (~190%) and Q4 2021 (~210-215%). Verified via parallel research sub-agent across Fortune (Apr 19), Invezz (Apr 13), Advisor Perspectives, GuruFocus, Current Market Valuation, Longtermtrends, Motley Fool."

to: HENRY (ACTION — MARKET_VOL primary)
info: RED, LIQUID, NEXUS
group: VOL
dispatched: 2026-04-19T17:55:00Z
dispatch_note: "Verify-research sub-agent confirmed 232% reading across 5+ independent sources. Methodology caveat: 232.6% is at the high end of Wilshire/GDP variants — GuruFocus shows 223.5% on Wilshire/GNP basis; the gap is denominator (GDP vs GNP) not data integrity. Routing as PRIORITY (not IMMEDIATE) — extreme reading is the news, but Buffett Indicator alone is not actionable; lands as 6th node in the 8-point valuation/positioning convergence cluster. HENRY for vol-regime context, RED for counter-case fodder, NEXUS for convergence engine."

signal_type: threshold-crossed
confidence: 0.85
confidence_language: confirmed
resources: 0
safety_net: clear

word_count: 280

# cluster backfilled 2026-06-10 from INDEX section placement (pre-v0.7 signal; cluster field added to FORMAT_SPEC 2026-05-05)
cluster: POSITIONING_VALUATION
---

## Signal

**Buffett Indicator (Wilshire 5000 / U.S. GDP) printed 232.6% on Apr 19, 2026 — verified ATH.**

Surpasses prior peaks:
- Dot-com bubble (2000): ~190%
- Q4 2021: ~210-215%
- Mar 2025 ATH: ~209%

Cross-source verification (sub-agent Apr 19):
- Fortune (Apr 19, 2026)
- Invezz (Apr 13, 2026)
- Advisor Perspectives, Current Market Valuation, Longtermtrends, Motley Fool — all reporting ~230% range
- GuruFocus shows 223.5% on Wilshire/**GNP** basis (denominator difference, not data conflict)

Buffett's own framing (1999 Fortune interview, repeated): readings >200% indicate "playing with fire." 232% is the highest sustained print in the indicator's history.

## Relevance

- **HENRY (ACTION):** MARKET_VOL/regime context. Extreme valuation reading establishes the *backdrop* against which the SKEW/VVIX divergence (VIOLET POSTURE 🟠) and HF positioning data are landing. Not a vol trigger on its own, but reframes the conditional probability of a regime break.
- **RED (info):** Counter-case fodder. Buffett Indicator has historically been early (was elevated 1996-2000 before the top, again 2017-2019 before COVID dip). Steelman: high CapEx/buyback regime + foreign listings on U.S. exchanges inflate Wilshire numerator vs domestic GDP denominator.
- **LIQUID (info):** Backdrop for capital-flow sensitivity — at 232% market-cap/GDP, even modest positioning unwinds have outsized index-level impact.
- **NEXUS (info):** **6th node** in the emerging valuation/positioning convergence cluster (now 8 points with Wyckoff + parabolic from -004):
  1. SIG-W-20260414-006 (HF short cover fastest since 2020)
  2. SIG-W-20260414-008 (DB financials positioning gap)
  3. SIG-W-20260416-003 (NDX RSI 30→70 + SPX neg-breadth at 7000)
  4. SIG-W-20260419-002 (VIOLET VIX-family — SKEW divergence)
  5. SIG-W-20260419-003 (VIOLET POSTURE 🟡→🟠)
  6. **THIS SIGNAL** (Buffett Indicator 232.6% verified ATH)
  7-8. SIG-W-20260419-004 (Wyckoff + NDX parabolic)

## Caveats

- **Methodology variance:** 232.6% is the high-end variant. Wilshire/GNP basis prints ~223.5%. The reading is real either way; the precise number depends on denominator choice.
- **Indicator latency:** Buffett Indicator has been a poor short-term timing tool. Above-200% readings have persisted for quarters before mean-reversion.
- **Numerator inflation:** Foreign-domiciled companies listed on U.S. exchanges (TSMC, ARM, etc.) inflate Wilshire vs domestic GDP. Real "extreme" threshold may have drifted higher than the 1999 Buffett framing assumed.

## Source

- X.com screenshot, Apr 19, 2026 — Wilshire 5000 / GDP chart at 232.6%
- Verify-research sub-agent (parallel spawn 2026-04-19): cross-referenced Fortune, Invezz, Advisor Perspectives, GuruFocus, Current Market Valuation, Longtermtrends, Motley Fool
- Intake: Will via Telegram screenshots, 2026-04-19 17:41 UTC
