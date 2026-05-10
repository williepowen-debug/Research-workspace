---
signal_id: SIG-W-20260509-012
precedence: ROUTINE
timestamp: 2026-05-10T03:12:00Z
source: WALTER (mirror-archive — original dispatch by PROME 2026-05-09; STEPPED DOWN PRIORITY → ROUTINE post-verify)
origin: ["First Squawk X screenshot 5/8 21:31 ET via Will Telegram batch", "TIC monthly data via ticdata.treasury.gov (verified retroactively)", "MoF May 2026 announcement feed (verified retroactively)", "PROME 2026-05-09 dispatch FORGE/signals/2026-05-09_japan-ust-selling-yen-defense-claim.md"]

to: SAM (ACTION)
info: LIQUID, HENRY, ZHAO, RED
group: —

signal_type: context
confidence: 0.40
confidence_language: unconfirmed
resources: 1
safety_net: clear

word_count: 130

cluster: FED_FRAMEWORK
cluster_secondary: ASIA_CHINA
event_window: closed

dispatched: 2026-05-10T03:12:00Z
mirrored_ts: 2026-05-10T19:30:00Z
dispatch_note: "PROME pinch-hitter dispatch 5/9 PRIORITY; WALTER mirror-archive 5/10 STEPPED DOWN to ROUTINE. Verify-research cluster D: CORRECTED-FRAMING-leaning-FALSE — TIC Feb 2026 shows Japan ACCUMULATING +$14B (opposite of dumping); MoF May = zero Treasury-sale entries. RED auto-cc per CORRECTED-FRAMING."
---

## WALTER verify verdict (mirror-archive 2026-05-10)

**VERDICT: CORRECTED-FRAMING leaning FALSE 0.40** — claim is unsupported by every data point currently available; only directly-relevant data point (March TIC) still 8 days out.

Primary: TIC monthly data (ticdata.treasury.gov) + MoF May 2026 announcement feed + Bloomberg 4/30 + CNBC 5/7:
- **TIC Feb 2026 (latest)**: Japan UST holdings **rose** $1,225.3B → **$1,239.3B** = **+$14B** Jan→Feb. **Accumulating, not dumping.**
- **MoF May 2026 What's New**: **Zero entries** about Treasury sales or intervention announcements. Routine JGB auctions only.
- **Confirmed sub-fact:** Japan DID intervene in FX — ~¥5T (~$31B) Apr 30 yen-buying; further early-May ops. NOT confirmed: USTs were sold to fund it.
- Conflation pattern: people conflate "FX intervention" with "UST dumping." Historically MoF uses existing reserve cash/coupons, not direct UST liquidation.

**Critical caveat:** TIC has ~6-week lag. **March 2026 TIC release on May 18** — that's the file that would show any actual selling tied to Apr-30 intervention. So claim isn't disproven outright; it's unsupported by every currently-available data point.

**Step-down rationale:** PROME originally PRIORITY because of UST-plumbing-transmission importance IF true. But "if true" is currently disconfirmed by primary. Stepped to ROUTINE with reframing: "intervention active, UST funding mechanism speculative, watch May 18 TIC."

Verify sub-agent a93ada83efeec5d7f.

## Original PROME dispatch (2026-05-09)

# Signal — Japan may be selling USTs to defend yen
**Date:** 2026-05-09 23:12 ET
**Source:** Will image batch via Telegram; First Squawk X screenshot
**Priority:** 🟠 Medium-high / verify source
**Routes:** SAM, LIQUID, HENRY, ZHAO
**Status:** Routed to agent inboxes

## Extracted facts

First Squawk screenshot claims:
- "Japan may be dumping U.S. Treasuries to save the yen, adding more pressure on America's bond market and pushing U.S. borrowing costs higher."
- Timestamp visible: 9:31 PM, 5/8/26.
- No dollar amount or official source visible.

## Signal read

This is exactly the SAM/LIQUID Japan-carry/Treasury-demand-hole channel, but it is still a claim until official/flow evidence confirms it.

If true:
- Yen defense via reserve sales adds marginal pressure to UST yields.
- Higher UST yields tighten U.S. financial conditions and pressure mortgage/CRE/private-credit refinancing.
- Potential feedback loop: high UST yields → risk asset stress → carry unwind / funding volatility.

## Verification queue

1. Check MoF intervention announcements and USD/JPY levels.
2. Check TIC/custody/reserve flow data when available.
3. Compare UST auction tails, term premium, and long-end yield move around the claim.
4. Determine whether selling is actual reserve liquidation, FX swaps, or market rumor.

## Routing rationale
- SAM: Japan/yen/carry core domain.
- LIQUID: Treasury market/funding/liquidity impact.
- HENRY: equity discount-rate and market-structure impact.
- ZHAO: Asia reserve-flow context.
