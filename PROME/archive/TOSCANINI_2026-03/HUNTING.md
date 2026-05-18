# HUNTING — How Prome Finds and Prioritizes Work

**Created:** 2026-03-25
**Purpose:** Systematic framework for deciding what becomes a proposal. Replaces vibes-picking with a scoring function.

---

## When This Runs

**Every session start**, after reading SCRATCH → STATUS → QUEUE (boot sequence step 2.5). Prome scans all potential work items, scores them, and ranks the queue before presenting proposals.

---

## Scoring Dimensions

| Dimension | Weight | 0 | 1 | 2 | 3 |
|-----------|--------|---|---|---|---|
| **Position Proximity** | **×2** | No connection to any position or trade decision | Indirect — feeds a thesis that feeds a position | Direct — informs sizing, timing, or exit of an open position | Urgent — position at risk without this information |
| **Time Pressure** | ×1.5 | No deadline | Weeks away | Days away | Hours away or window closing |
| **Blindness Risk** | ×1 | Full coverage, recent data | Slightly stale (<3 days) | Stale (3-7 days) or missing key data | Flying blind on something that matters (>7 days stale, active domain) |
| **Convergence Potential** | ×1 | Isolated — affects one agent only | Touches 2 agents | Touches 3+ agents or feeds NEXUS synthesis | Could shift scenario probabilities or thesis confidence |
| **Decay Rate** | ×1 | Signal is stable — same value next week | Moderate — loses some context over days | Degrades meaningfully within 48h | Perishable — value drops to zero if not acted on today |
| **System Freshness** | ×1 | No upstream agents refreshed recently | 1-3 agents refreshed since last run | 4-8 agents refreshed | 9+ agents refreshed — full system state changed (synthesis pass) |

**Max score: 22.5** (all 3s with weights applied)

**Note on System Freshness:** This dimension exists specifically for synthesis agents (NEXUS, RED) whose value scales with how much upstream data has changed. A NEXUS pass after 14 agent refreshes is qualitatively different from a NEXUS pass cold. Scoring 0 for non-synthesis work is fine — the dimension is inert for single-agent tasks.

---

## How Prome Uses This

1. **Scan sources** — agent STATUS table, inbox counts, calendar catalysts, HEARTBEAT thresholds, QUEUE backlog, WILL_QUEUE blockers
2. **List candidate work items** — everything that could become a proposal
3. **Score each** — five dimensions, apply weights
4. **Rank** — highest scores become top proposals (up to 5 per batch)
5. **Discard low-scorers** — anything scoring <5 doesn't make the queue unless nothing else is available
6. **Present** — top 5 to Will with the priority prefix (🔴/🔵/🟢) derived from score:
   - **🔴** = score ≥14
   - **🔵** = score 7-13
   - **🟢** = score <7

---

## Source Scan Checklist

At session start, Prome checks these for potential work:

| Source | What to look for |
|--------|-----------------|
| Agent STATUS table | Severity indicators, stale dates, inbox counts |
| HEARTBEAT.md | Threshold breaches or near-breaches |
| QUEUE.md | Pending proposals from prior sessions |
| Calendar/catalysts | Data drops, earnings, expirations within 72h |
| SCRATCH.md | Unresolved items from last handoff |
| Cross-agent outboxes | Signals that crossed the 3-signal spawn threshold |
| WILL_QUEUE.md | Blockers that might have been resolved |
| POSITIONS.md | Upcoming expirations, rolls needed, decision points |

---

## Anti-Patterns

- **Busywork bias** — "refresh stale agent" and "clean up files" feel productive but score low on position proximity. Don't let them crowd out real work.
- **Loudness bias** — the most dramatic signal isn't always the most actionable. A quiet analyst downgrade on WAL might matter more than a flashy geopolitical headline.
- **Completionism** — not every gap needs filling. Some agents can stay stale if their domain isn't active.
- **Recency bias** — the signal that just arrived isn't automatically more important than the one from two days ago that's still unprocessed.

---

## Hunting Directive

Will can point Prome in a direction at any time. Format is loose — "bias toward credit this week," "something feels off in Japan, go dig," "I want more on WAL." Prome logs it here and it acts as a **score multiplier (×1.5)** on all dimensions for work items in that domain until Will cancels it or it's explicitly resolved.

**Active Directives:**

| Directive | Domain/Agent | Set | Expires |
|-----------|-------------|-----|---------|
| **Consolidation first** — fix gaps, fill holes, strengthen existing position-relevant domains before expanding coverage | SYSTEM-WIDE | 2026-03-25 | Until cancelled |

**Rules:**
- Max 3 active directives (forces prioritization — if Will adds a 4th, ask which one to drop)
- Prome can *suggest* a directive ("I think we're underweight on X") but never self-assigns one
- Directives don't override the scoring — they amplify it. A zero-value busywork task in a directed domain still scores low.
- Log resolved directives below for pattern tracking

**Resolved Directives:**

| Directive | Domain | Set | Resolved | Outcome |
|-----------|--------|-----|----------|---------|
| *None yet* | — | — | — | — |

---

## Evolution

This is v1. As DECISIONS.md accumulates data, calibrate:
- Are high-scoring proposals actually producing high value? If not, adjust weights.
- Is position proximity the right dominant weight? Check against outcomes.
- Should NEXUS run periodic deeper scoring passes? (Deferred — revisit when A alone feels insufficient.)
