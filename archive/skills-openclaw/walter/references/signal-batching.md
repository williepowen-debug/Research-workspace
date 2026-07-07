# SIGNAL BATCHING — Spawn Threshold Rules

**Source:** PROME/TOSCANINI/SIGNAL_BATCHING.md  
**Purpose:** When accumulated signals trigger agent spawn proposals

---

## Default Rule: 3-Signal Threshold

An agent becomes **spawn-ready** when it accumulates ≥3 unprocessed inbox signals.

**Signal sources:**
- Will's direct input (news, screenshots, observations)
- Cross-agent outbox deliveries
- Threshold breaches from HEARTBEAT.md

**At threshold:** Agent gets added to QUEUE.md as spawn proposal. Does NOT auto-spawn — requires Will's approval per Toscanini protocol.

---

## Volume Tiers (Adjusted Thresholds)

| Tier | Agents | Threshold | Typical Volume | Notes |
|------|--------|-----------|----------------|-------|
| **High-volume** | HAWK, BRENT, LABOR, CARL | **2 signals** | 5-10+/week | War + macro = constant flow |
| **Standard** | HENRY, LIQUID, BROCK, REGINALD, ZHAO, SAM | **3 signals** | 3-5/week | Default rule |
| **Low-volume** | MARCO, OTTO, HANS, SHADE | **3-4 signals** | 1-2/week | Slower domains, longer windows |
| **Synthesis** | NEXUS, RED | **On-demand** | N/A | Spawn after check-ins or major clusters |

---

## 🔴🔴 Critical Exceptions

| Rule | Condition | Action |
|------|-----------|--------|
| **Critical single** | Any 🔴🔴 signal (threshold breach, thesis-breaking) | Immediate proposal — don't wait for threshold |
| **Time-sensitive cluster** | Multiple signals with same-day catalyst | Bundle into single proposal regardless of count |
| **Position-proximate** | Signal affects open position with <7 day catalyst | Counts as 2 signals toward threshold |

---

## What Counts as Signal

| Counts | Does NOT Count |
|--------|----------------|
| New data point with date and source | Prome's own notes or commentary |
| Cross-agent outbox delivery | Duplicate of already-processed signal |
| Will's direct input | Stale data refresh (same number, new date) |
| Threshold breach | System/infrastructure messages |

---

## Post-Spawn Cleanup

After agent processes inbox:

1. Move processed signals to `AGENTS/{AGENT}/inbox/processed/`
2. Update KB.tsv with new data points
3. Write COMPLETION block per COMPLETION_SPEC.md
4. Prome resets inbox count to 0

---

## WALTER Integration

WALTER implements hybrid routing:

1. **Route immediately** — All signals logged to inbox
2. **Track counts** — Monitor accumulation per tier
3. **Flag thresholds** — Note spawn-ready agents in output
4. **Escalate 🔴🔴** — Critical singles bypass batching

Toscanini handles the spawn decision queue.
