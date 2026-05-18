# SIGNAL BATCHING — When Agents Spawn

**Created:** 2026-03-25
**Purpose:** Codify when accumulated signals trigger an agent spawn. Prevents both under-response (signals pile up) and over-response (spawning on every headline).

---

## Default Rule: 3-Signal Threshold

An agent becomes **spawn-ready** when it accumulates ≥3 unprocessed inbox signals. Signals come from:
- Will's direct input (news, screenshots, observations)
- Cross-agent outbox deliveries (routed by HERMES or Prome)
- Threshold breaches from HEARTBEAT.md

**At threshold:** Agent gets added to QUEUE.md as a spawn proposal. Does NOT auto-spawn — still requires Will's approval per TOSCANINI protocol.

---

## Exceptions

| Rule | Condition | Action |
|------|-----------|--------|
| **🔴🔴 CRITICAL single** | Any single signal tagged 🔴🔴 (threshold breach, thesis-breaking) | Immediate proposal — don't wait for 3 |
| **Time-sensitive cluster** | Multiple signals with same-day catalyst (earnings, data drop) | Bundle into single spawn proposal regardless of count |
| **Position-proximate** | Signal directly affects an open position with <7 day catalyst | Weight ×2 toward spawn threshold (counts as 2 signals) |

---

## Volume Tiers

Not all agents receive signals at the same rate. Expectations:

| Tier | Agents | Typical Volume | Notes |
|------|--------|---------------|-------|
| **High volume** | HAWK, BRENT, LABOR, CARL | 5-10+ signals/week | War + macro = constant flow. Spawn more frequently. |
| **Medium volume** | HENRY, LIQUID, BROCK, REGINALD, ZHAO, SAM | 3-5 signals/week | Domain-specific catalysts. Standard 3-signal rule. |
| **Low volume** | MARCO, OTTO, HANS, SHADE, NEXUS, DARWIN | 1-2 signals/week | Slower domains. May need longer accumulation windows. |
| **Synthesis** | NEXUS, RED | On-demand | Spawn after check-in rounds or major signal clusters, not on inbox count. |

---

## Signal Sources (what counts)

| Counts as signal | Does NOT count |
|-----------------|----------------|
| New data point with a date and source | Prome's own notes or commentary |
| Cross-agent outbox delivery | Duplicate of already-processed signal |
| Will's direct input (news link, screenshot, observation) | Stale data refresh (same number, new date) |
| Threshold breach (HEARTBEAT indicator moves) | System/infrastructure messages |

---

## Current State (as of 2026-03-25 post-routing)

| Agent | Inbox | Spawn-Ready? |
|-------|-------|-------------|
| PROME | 14 | N/A (triage, not spawn) |
| LIQUID | 11 | ✅ |
| HENRY | 10 | ✅ |
| NEXUS | 8 | ✅ (synthesis pass) |
| REGINALD | 6 | ✅ |
| CARL | 5 | ✅ |
| HAWK | 5 | ✅ |
| SAM | 4 | ✅ |
| ZHAO | 3 | ✅ |
| BRENT | 3 | ✅ |
| LABOR | 3 | ✅ |
| OTTO | 3 | ✅ |

---

## Post-Spawn Cleanup

After an agent processes its inbox:
1. Move processed signals to `inbox/processed/`
2. Update KB.tsv with any new data points
3. Write COMPLETION block per COMPLETION_SPEC.md
4. Prome resets that agent's inbox count to 0
