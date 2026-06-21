---
signal_id: SIG-W-20260621-003
dispatched: 2026-06-21T22:12:00Z
origin: Will Telegram intake (6-image batch, msgs 2539-2544, 2026-06-21 ~22:30 UTC)
source: Topdown Charts (chart: Topdown Charts / AAII / ICI / Fed Flow of Funds / LSEG) — "Investor Asset Allocations — Treasuries"
signal_type: positioning-extreme
domain: RATES
cluster: POSITIONING_VALUATION
signal_role: cluster_mediating
cluster_secondary: FED_FRAMEWORK
narrative_channel: n/a
precedence: PRIORITY
to: BOND
info: [HENRY, LIQUID]
confidence: 0.80
verify_verdict: SKIP-VERIFY (named sources — Topdown/AAII/ICI/Fed FoF/LSEG; secular survey series; recency caveat below)
verify_method: BOARD-grep dedup (novel — no prior Topdown / Treasury-allocation positioning chart in BOARD); named-source chart, no verify-spawn
---

# Investor portfolio allocation to Treasuries ~7% — near a multi-decade low (the flip-side of the equity-crowding regime)

## Substance (SKIP-VERIFY 0.80)

Topdown Charts (compiling AAII / ICI / Fed Flow-of-Funds / LSEG): **investor portfolio allocation to Treasuries has fallen to ~7%**, near the **lowest in the series' multi-decade history** — a secular slide from ~15-16% in 1987-92, through ~12% at the 2002 equity-bear peak and ~11% post-GFC (2010-12), down to a persistent ~7-8% since ~2020 and now grinding to the series low.

**Pairs directly with the same-batch AI/equity-concentration signal (SIG-W-20260621-002):** investors are at record concentration in AI/equities AND at multi-decade-low allocation to Treasuries — the two halves of one positioning regime (crowded risk-on, under-owned duration/safe-haven).

## Why it matters — two-sided (cluster_mediating), BOND owns the read

**BOND (action) — UST positioning / demand structure:** this is a positioning datum on the demand side of BOND's domain. **Two-sided:**
- **Contrarian-bullish-duration read:** under-allocation to USTs at a multi-decade low = a large potential marginal-buyer pool if/when risk-off or a growth scare hits; the "expensive, not broken" long-end (BOND's standing frame) has under-owned demand that could snap back hard on a catalyst.
- **Structural-demand-hole read:** the secular decline is consistent with the foreign-official-bid erosion + supply-deluge theme (ties the TIC April / UST-composition-shift signals BOND already holds) — domestic investors structurally light on Treasuries means thinner price-insensitive demand into heavy issuance, i.e. a higher term-premium / weaker-auction backdrop.
- **Recency caveat:** the chart's x-axis appears to end ~2023-24 and carries no fresh print date — treat the **level as a secular/structural observation, not a this-week tactical signal.** BOND validates against its live AAII/ICI/positioning sources before treating the "series low" as current.

**HENRY (info) — the equity-side mirror:** confirms the crowding HENRY is tracking from the other direction (everyone in equities/AI, no one in Treasuries = same regime; SIG-W-20260621-002 is the equity leg).

**LIQUID (info) — flows/funding:** under-owned USTs feeds the funding/collateral-demand and the "who's the marginal Treasury buyer" question LIQUID tracks; pairs with the TIC official-vs-private-flow thread.

## Source framing

Named sources; secular survey series — reliable as a structural-positioning picture. The honest framing: **multi-decade-low UST allocation is a real structural fact; the actionable edge is the asymmetry it sets up (snap-back demand vs structural demand-hole), not a dated trigger.** Flag the chart's apparent staleness so it isn't read as a fresh weekly move.

## AIGs / cross-refs

- BOARD: SIG-W-20260621-002 (AI/equity concentration — the paired flip-side), SIG-W-20260506-003 (foreign UST→gold rotation), the 6/6 UST<1yr composition-shift + CB-gold pair (BOND-routed)
- BOND STATUS 6/20 ("expensive, not broken" held a 5th straight resolution; TIC April official-bid)

## Provenance

- Intake: Telegram 6-image batch msgs 2539-2544, 2026-06-21 ~22:30 UTC
- Pipeline: BOARD-grep novel + SKIP-VERIFY (named institutional survey chart) → dispatch to BOND (created BOND inbox/WALTER dir, first dispatch to BOND since the delivery layer shipped)
