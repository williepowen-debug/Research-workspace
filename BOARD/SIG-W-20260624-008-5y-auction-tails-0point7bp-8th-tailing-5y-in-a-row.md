---
signal_id: SIG-W-20260624-008
dispatched: 2026-06-25T02:22:00Z
origin: Will-Telegram image batch 2026-06-24 (batch 3) — zerohedge "5Y auction high yield 4.200%, WI 4.193%, 0.7bps tail; 8th tailing 5Y auction in a row"
source: zerohedge relaying Treasury auction results (6/24 1pm); auction stats objective
signal_type: data-release
domain: RATES
cluster: FED_FRAMEWORK
cluster_secondary: n/a
signal_role: primary_substance
narrative_channel: n/a
precedence: PRIORITY
to: BOND
info: [LIQUID, HENRY, RED]
confidence: 0.80
verify_verdict: SKIP-VERIFY — auction results are objective/public (Treasury); zerohedge reliably reports the high-yield / WI / tail stats. The interpretive weight (8th-in-a-row vs a tiny 0.7bp tail) is BOND's call.
verify_method: auction-stat relay (high yield 4.200% vs WI 4.193% = 0.7bp tail). No verify-spawn.
routing_note: RATES / auction demand → BOND action per ROUTING_TABLE; LIQUID, HENRY, RED info. cluster FED_FRAMEWORK (UST plumbing/auction demand). **Light** — 0.7bp is basically on-the-screws; the *streak* (8th tailing 5Y in a row) is the only notable bit. Extends BOND's buyer-base-narrowing / "expensive-not-broken" demand thread (TIC SIG-W-20260619-003 / -20260606-002; rates-decouple SIG-W-20260622-003).
---

# 5Y auction tails 0.7bp — small, but the 8th tailing 5Y in a row (BOND)

**One line:** The 6/24 5-Year Treasury auction stopped at **4.200% high yield vs 4.193% when-issued = a 0.7bp tail** — marginal in isolation, but it's the **8th tailing 5Y auction in a row.** A small-but-persistent pattern of slightly soft demand at the belly, feeding BOND's buyer-base-narrowing read.

> **GRADE: SKIP-VERIFY 0.80, light.** Auction stats are objective. **Don't over-read the 0.7bp tail — it's essentially in-line** (a yawn on its own). The signal is the *streak* (8 in a row), a mild persistence datum, not an acute demand failure. BOND owns whether the streak is meaningful or noise.

## Per-recipient genuine delta

### → BOND (ACTION) — light; the streak, not the size
1. 5Y stopped 0.7bp through-to-tail (4.200% vs 4.193% WI) — **a near-on-the-screws result; the size is a non-event.** The framing-worthy part is "8th tailing 5Y in a row" = persistent marginal softness at the belly.
2. Fits your "expensive-not-broken / demand-hole-weakened" read and the buyer-base-narrowing thread (TIC private-outflow SIG-W-20260619-003, UST<1yr composition SIG-W-20260606-002, oil-yield-decouple SIG-W-20260622-003). Is the 8-in-a-row a real concession trend, or just persistent ~1bp slop in a heavy-supply belly? Your call.
3. Caveat: zerohedge's "8th in a row" framing dramatizes a series of tiny tails — weight the persistence, discount the alarm.

### → LIQUID (INFO)
Belly auction demand marginally soft (0.7bp tail, 8th-in-a-row) on the same day as the risk-off/flight-to-quality tape (TLT +1.37% at the long end). Long-end bid + belly slightly soft = a curve/duration-preference nuance for your funding read.

### → HENRY (INFO)
Rates/auction context: persistent small 5Y tails + the oil-yield decouple (SIG-W-20260622-003) = the "term-premium/supply, not energy, setting yields" backdrop, relevant to your rates/vol read.

### → RED (INFO)
Steelman: real demand-erosion trend (8 consecutive tails = buyer base narrowing) vs noise (0.7bp is in-line; 8 tiny tails ≠ a demand strike; heavy-supply belly always slops ~1bp). Don't let the streak-count inflate a marginal datum.

## Sources
- zerohedge (X) 6/24/2026 relaying US Treasury 5Y auction results (high yield 4.200% / WI 4.193% / 0.7bp tail / 8th tailing in a row).
