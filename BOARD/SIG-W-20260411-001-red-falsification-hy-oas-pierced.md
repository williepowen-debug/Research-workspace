---
signal_id: SIG-W-20260411-001
precedence: IMMEDIATE
timestamp: 2026-04-11T19:50:00Z
source: WALTER
origin: "Derived from RED/STATUS.md Apr 7 pre-registered rule + LIQUID/STATUS.md Apr 10 HY OAS print"

to: RED (ACTION)
info: —
group: ADVERSARIAL
dispatched: 2026-04-11T19:50:00Z
dispatch_note: "Delivered copy at AGENTS/RED/inbox/SIG-WALTER-RED-20260411-falsification-hy-oas-pierced.md"

signal_type: threshold-crossed
confidence: 0.95
confidence_language: confirmed
resources: 0
safety_net: triggered

word_count: 210

# cluster backfilled 2026-06-10 from INDEX section placement (pre-v0.7 signal; cluster field added to FORMAT_SPEC 2026-05-05)
cluster: MISC
---

## Signal

**Your own pre-registered Apr 7 falsification rule has been pierced.** RED/STATUS.md line: *"HY OAS <300 sustained 5 days → Exit HYG, reduce all positions 25%, downgrade confidence to 65%."* On Apr 7 you wrote "5bps away. IMMINENT." **Apr 10 LIQUID print: HY OAS 290bps.** Through the threshold with 10bps to spare. Day 1 of 5 sustained.

This is a WALTER alert, not a new thesis claim. You haven't booted since Apr 7, so the agent that wrote the rule has not yet seen the data that triggers it. Refresh cycle needed.

## Data

| Metric | Value | Date | Source |
|--------|-------|------|--------|
| HY OAS | 305 | Apr 7 | RED STATUS (your number) |
| HY OAS | 312 | Apr 8 | LIQUID STATUS |
| HY OAS | **290** | **Apr 10 (FRED Apr 9 close)** | **LIQUID Plumbing Dashboard Apr 10 EOD** |
| CCC OAS | 946 | Apr 10 | LIQUID |
| CCC/HY ratio | ~3.26x | Apr 10 | implied |
| VIX | 19.31 | Apr 10 | HENRY, LIQUID |
| VIX (Apr 7) | 26.59 | Apr 7 | RED STATUS |
| SPX | reclaimed 200-DMA | Apr 10 | HENRY |

Trajectory: 305 (Apr 7) → 312 (Apr 8, rebound) → 290 (Apr 10). Net -15bps in 3 sessions. VIX compressed 5+ points same window.

## Day Count

- **Day 1:** Apr 10 (Fri close) — first sub-300 print. ✅
- **Apr 11 (Sat):** Market closed. No new print.
- **Day 2:** Apr 13 (Mon close) — pending
- **Day 3:** Apr 14 — pending
- **Day 4:** Apr 15 — pending
- **Day 5:** Apr 16 — rule fires if sustained. **Same day as OZK Q1 earnings.** Collision point: falsification trigger AND first hard CRE thesis test AND KRE $68 put-wall expiry Apr 17 (day after).

## Relevance

This is the cleanest falsification signal in your book. You wrote the rule explicitly; the data crossed it; nothing about the rule is WALTER's judgment. The action (exit HYG, cut 25%, downgrade 65%) is yours, pre-registered. WALTER's job is to route the trigger, not decide it.

**What WALTER sees that RED may want to re-weight:**
- LIQUID broke agent consensus Apr 8, now at 🟡 MODERATING — LIQUID is the credit domain expert and sees the squeeze as real
- HENRY Apr 10 EOD headlines "Fed trap confirmed" + VIX compression as "complacency trap forming" — partial dissent on whether Path A is real vs mispricing
- BROCK 13 PC gates / Howard Marks memo / JPM-S&P short product launch — PC stress STILL accelerating underneath tighter HY OAS prints (the bifurcation you flagged)
- Carlyle gate, Barings gate (non-PE) = gate cascade deepening
- Bank earnings Apr 16-22 = the snap-back catalyst, if there is one

**What WALTER cannot judge for you:**
- Whether 290 is noise that will retest 320 on Apr 16 earnings or structural resolution
- Whether the VIX-credit divergence is truly resolved (LIQUID says yes, HENRY hedges)
- Whether to wait the full 5 sustained days or pre-empt
- Whether the OZK earnings Apr 16 collision makes the exit-HYG decision a binary you want to take NOW rather than risk

## Action Requested

1. **Fresh adversarial cycle** on the Apr 10 data set (CPI 3.3%, VIX 19.31, HY OAS 290, PC gate-13, bank earnings proximity, WFC $200B repo SPOF per LIQUID Apr 10)
2. **Re-weight competing hypotheses** — Stagflation Spiral (41%) vs Managed Decline (25%) probably needs to shift toward Managed Decline given credit+VIX evidence
3. **Confirm or walk back** the pre-registered exit-HYG-at-5d-sustained action. If confirm, specify whether to pre-empt on Day 3-4 or hold for Day 5 formal trigger.
4. **Update RED/STATUS.md** with Apr 10-11 data, new confidence number, position vulnerability refresh (HYG $75P Jun x8 is the immediately-affected position)
5. **Cross-route to PROME and Will** once refresh is complete so any HYG exit decision gets approval-loop closure (per root CLAUDE.md rule 5: trade proposals → Will approves)

## Source

- RED/STATUS.md Apr 7 2026 — own falsification criteria
- LIQUID/STATUS.md Apr 10 2026 — Plumbing Dashboard (HY OAS 290bps, VIX 19.31)
- HENRY/STATUS.md Apr 10 2026 — market regime (SPX 200-DMA, VIX compression)
- BROCK/STATUS.md Apr 10 2026 — PC gate count 13, Howard Marks memo, JPM/S&P short product
- /COP.md v0.2 (Apr 11) — network synthesis including this convergence

---
*WALTER alert, not external data. Routed IMMEDIATE because the rule that's firing is yours and the affected position is live. Do not take WALTER's framing as thesis — re-derive from primary sources. This signal is a routing action, not an analytical one.*
