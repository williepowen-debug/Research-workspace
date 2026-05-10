---
signal_id: SIG-W-20260509-016
precedence: PRIORITY
timestamp: 2026-05-10T03:20:00Z
source: WALTER (mirror-archive — original dispatch by PROME 2026-05-09)
origin: ["Jason Goepfert X screenshot 5/9 23:20 ET via Will Telegram", "Hedgeye Risk Management 5/9 (verified retroactively as actual primary for 5.6%/3-analog framing)", "PROME 2026-05-09 dispatch FORGE/signals/2026-05-09_spx-record-high-breadth-deterioration.md"]

to: HENRY (ACTION)
info: VIOLET, RED, LIQUID
group: —

signal_type: pattern-match
confidence: 0.85
confidence_language: reports
resources: 1
safety_net: clear

word_count: 145

cluster: POSITIONING_VALUATION
cluster_secondary:
event_window: closed

dispatched: 2026-05-10T03:20:00Z
mirrored_ts: 2026-05-10T19:30:00Z
dispatch_note: "PROME pinch-hitter dispatch 5/9; WALTER mirror-archive 5/10. Verify-research cluster B: CONFIRMED 0.85 — but ATTRIBUTION CORRECTED. Hedgeye is source of 5.6%/3-analog (1929/1973/1999), NOT Goepfert. Goepfert's own X post cited 4%/2-analog (1929 + today). Body needs attribution fix before downstream propagation."
---

## WALTER verify verdict (mirror-archive 2026-05-10)

**VERDICT: CONFIRMED 0.85 — but ATTRIBUTION CORRECTED**

Primary verification:
- **Goepfert's actual X post** (status 2052110616622485834) cites **>4% at 52w lows** as "2nd time in 100 years" — i.e., 1929 + today only (single analog, not three).
- **The 5.6% / three-analog (1929/1973/1999) framing is from Hedgeye Risk Management**, NOT SentimenTrader / Goepfert. Per [247WallSt — Hedgeye attribution](https://247wallst.com/investing/2026/05/10/the-sp-500-just-did-something-its-only-done-3-times-before-why-trumps-ai-rally-is-in-danger/), Hedgeye published the 1929/1973/1999/today three-analog frame on May 9 2026.
- The breadth divergence at ATH is **real and historically extreme** at either threshold (4% Goepfert / 5.6% Hedgeye).

**Implication for downstream consumption:** body needs attribution fix. The two threshold/analog framings are NOT interchangeable:
- 4% threshold → 2 analogs (1929 + today) — Goepfert
- 5.6% threshold → 3 analogs (1929 / 1973 / 1999 / today) — Hedgeye

**Substantive cluster cross-reference:** reinforces SIG-W-20260509-007 (defensives underweight) + SIG-W-20260509-015 (positioning extremes / call-chase) — index leadership narrow, internal lows rising, three positioning-fragility channels converging.

Verify sub-agent a699b6def2c21b7cb.

## Original PROME dispatch (2026-05-09)

# Signal — S&P record high with 5% of members at 52-week lows
**Date:** 2026-05-09 23:20 ET
**Source:** Will image batch via Telegram; Jason Goepfert X screenshot
**Priority:** 🟠 Medium-high / verify
**Routes:** HENRY, VIOLET, RED, LIQUID
**Status:** Routed to agent inboxes

## Extracted facts / claims

Jason Goepfert screenshot claims:
- S&P 500 / SPY hit a record high while **5%+ of members fell to 52-week lows**.
- Claimed historical parallels:
  1. July 1929
  2. January 1973
  3. December 1999
  4. Today
- Visible table: S&P 500 members at 52-week lows highlighted around **5.60%**.
- Other visible values: NASDAQ 100 ~4.00%, S&P 100 ~6.00%, S&P 400 ~2.25%, S&P 600 ~2.17%, Dow Industrials ~3.33%, Transports/Utilities ~0.00%.

Web check:
- Exact phrase search did not confirm in this pass. Treat as unverified until breadth data is pulled.

## Signal read

This is a classic **index concentration / bad breadth** warning.

Why it matters:
- New highs with rising internal lows suggest leadership is narrow and index resilience may be hiding sector/member-level deterioration.
- Historical analogs named in the post — 1929, 1973, 1999 — are not timing tools, but they are useful regime warnings.
- This reinforces prior signals: defensive underweight, AI/semi melt-up, record call notional, and growth concentration.

Trigger to watch:
- Breadth fails to repair while index keeps rising.
- VIX/credit spreads lag until first leadership break.
- 52-week lows broaden beyond S&P 500 into mid/small caps and cyclicals.

## Verification queue

1. Pull current S&P 500 new-high/new-low breadth from a primary/market-data source.
2. Compare with equal-weight S&P and sector breadth.
3. Check whether lows cluster in defensives, healthcare, cyclicals, regional banks, or rate-sensitive sectors.
4. Pair with VIX term structure/gamma exposure.

## Routing rationale
- HENRY: equity market structure and index concentration.
- VIOLET: volatility/breadth-to-vol lag.
- RED: adversarial read on bearish analogs and concentration risk.
- LIQUID: risk-asset liquidity / unwind channel.
