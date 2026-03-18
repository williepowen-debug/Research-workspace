# Signal Triage Protocol

**Owner:** PROME (or dedicated triage session)
**Purpose:** Sort, cap, enrich, and route inbound signals before agent spawning.
**Extends:** `PROME/SIGNAL_PROTOCOL.md` (packaging format unchanged)
**Created:** 2026-03-17

**Relationship to SIGNAL_PROTOCOL.md:** The signal protocol defines the full signal *package* (SIG-NNN format with Admiralty, KB staging, etc.) that gets written to agent inbox files. This triage protocol operates *upstream* of packaging — it sorts, caps, and enriches signals before they're packaged. The enrichment card (below) is a **spawn prompt summary**, not a replacement for the full package. Agents receive: (1) enrichment cards in their spawn prompt for orientation, (2) full signal packages in their inbox for integration.

---

## Why This Exists

Context is not RAM. Every signal loaded into an agent's context competes for attention with every other signal. Empirically, agents processing 5 signals produce deeper analysis per signal than agents processing 7+. Capping inputs forces quality.

**Principle:** An agent that receives 5 well-enriched signals with a clear question outperforms an agent that receives 8 raw signals with an open mandate.

---

## Triage Flow

```
Will sends signals
    ↓
Step 1: EXTRACT — pull the fact from each signal
    ↓
Step 2: ROUTE — assign primary domain (1 agent per signal, 2 max)
    ↓
Step 3: RANK — within each domain bucket, rank by urgency
    ↓
Step 4: CAP — max 5 signals per agent per spawn
    ↓
Step 5: ENRICH — write signal card for each (see template below)
    ↓
Step 6: PRESENT — show routing table to Will for approval
    ↓
Step 7: SPAWN — fire approved batches
    ↓
Step 8: QUEUE — overflow goes to next batch
```

---

## The Cap Rule

**Hard cap: 5 signals per agent per spawn.**

- If an agent's bucket has ≤5 signals → spawn as single batch
- If >5 signals → rank by urgency, top 5 go first, remainder queues
- Queued signals spawn in a follow-up batch after first completes
- Exception: a single 🔴🔴 signal can spawn immediately regardless of queue state

**Why 5?** Sweet spot between batch efficiency (don't spawn for 1 🟢 signal) and cognitive load (don't flood context). Matches SWE-agent research on capped search results.

---

## Priority Ranking (within domain buckets)

| Rank | Criteria | Examples |
|------|----------|---------|
| 1 | Threshold breach or imminent breach | HY OAS crossing 320, claims >280K |
| 2 | Position-affecting — changes sizing, timing, or conviction | Earnings miss, regulatory action, fraud |
| 3 | Thesis-confirming with new data | New filing validates existing model |
| 4 | Thesis-adjacent — builds context | Industry trend, analogous situation |
| 5 | Background / confirmatory | General news, already-priced information |

When two signals tie, prefer: actionable > informational, primary source > secondary, novel > confirmatory.

---

## Domain Routing Rules

| Domain | Agent | Routes Here |
|--------|-------|-------------|
| Employment, claims, JOLTS, NFP, DOGE workforce | LABOR | Job cuts, hiring data, UI claims, federal layoffs |
| Consumer credit, DQ, spending, gas prices, food CPI | CARL | Credit card, auto DQ, retail spending, gas pump, food/ag |
| Regional banks, CRE, FHLB, bank earnings | REGINALD | Bank-specific news, CRE data, regulatory actions, deposit flows |
| BDC, private credit, PE, NAV, gates, PIK | BROCK | BDC earnings, PC defaults, fund gates, PE marks, insurance-PC plumbing |
| Market structure, VIX, gamma, econ releases | HENRY | CPI/PPI/PCE, ISM, retail sales, VIX moves, equity flows |
| Treasury, funding, RRP, auctions, SOFR | LIQUID | Auction results, RRP, funding stress, Treasury buybacks |
| Japan, BOJ, JGB, yen, carry trade | SAM | BOJ policy, JGB yields, USD/JPY, carry unwind signals |
| China, capital flows, TIC, PBOC, HK | ZHAO | TIC data, PBOC moves, capital controls, CNY, Belt & Road |
| Europe, ECB, sovereign spreads (US lens) | HANS | ECB policy, European bank stress, UST demand from Europe |
| Geopolitical, military ops, conflict | HAWK | Military actions, escalation, sanctions, diplomatic moves |
| Oil fundamentals, tankers, storage, energy credit | BRENT | Oil prices, supply/demand, refinery, tanker rates, energy infrastructure |
| Auto credit, vehicle markets | OTTO | Auto DQ, dealer inventory, fleet/RV markets |
| Migration, labor mobility | MARCO | Immigration policy, labor flow data |

**Cross-routing:** If a signal touches two domains, assign PRIMARY (gets the signal card) and tag SECONDARY (FYI in cross-agent field). Don't duplicate signals across agents — that wastes spawn budget.

---

## Signal Enrichment Card

Every signal entering an agent batch gets enriched from raw input to structured card:

```
┌─────────────────────────────────────────────┐
│ SIGNAL CARD                                 │
├─────────────────────────────────────────────┤
│ Signal:    [one-line factual description]    │
│ Source:    [who + type + Admiralty grade]     │
│ Priority:  🔴 / 🟡 / 🟢                     │
│ Domain:    [primary agent]                   │
│ Secondary: [cross-agent FYI if any]          │
│ Data:      [key numbers/facts extracted]     │
│ Thesis:    [why this matters — 1-2 sentences]│
│ Question:  [what the agent should answer]    │
│ Refs:      [specific files agent should load]│
└─────────────────────────────────────────────┘
```

**The "Question" field is the key innovation.** Instead of "analyze this signal," the agent receives a specific analytical question. This focuses the entire context budget on answering, not on figuring out what to ask.

Examples:
- ❌ "Process this signal about China fertilizer exports"
- ✅ "Does China's urea export halt accelerate our fertilizer calendar to Week 4-6? Update food CPI timeline."
- ❌ "Here's data on retail investor flows"
- ✅ "Does JPM's -30% retail purchase data remove the BTFD floor? What's the next support level without retail bid?"

**The "Refs" field controls context loading.** Instead of the agent booting with its full STATUS + KB, it loads only what's relevant to this batch. Lighter context = more room for analysis.

**Implementation note (Phase 1):** Refs is a prompt instruction, not mechanical enforcement. The spawn task prompt says "For this batch, read [X, Y, Z] — you don't need your full KB." Agents may still load extra files. This becomes mechanical in Phase 3 when we redesign spawn prompts.

---

## Routing Table Format

Before spawning, present this table to Will for approval:

```
TRIAGE ROUTING — [date]
Signals received: [N]

| Agent    | Count | Priorities        | Top Signal                        | Status  |
|----------|-------|-------------------|-----------------------------------|---------|
| BROCK    | 5/7   | 🔴×1 🟡×3 🟢×1   | FFIEC $1.54T NDFI exposure        | READY   |
| HAWK     | 3     | 🔴🔴×2 🔴×1      | Iran PSAB strike                  | READY   |
| CARL     | 4     | 🔴×1 🟡×3        | China fertilizer halt             | READY   |
| REGINALD | 5     | 🟡×4 🟢×1        | FL completions +35%               | READY   |
| BROCK    | 2/7   | 🟡×2             | [overflow from batch 1]           | QUEUED  |
| SAM      | 2     | 🟡×2             | USD risk reversals +92bps         | READY   |
| HENRY    | 1     | 🟡×1             | JPM retail fatigue                | HOLD*   |

*HOLD = <3 signals, not urgent. Accumulate or bundle with next cycle.

Chains detected: BRENT → CARL (oil → gas pump pricing)
Recommendation: Spawn BRENT first, feed output to CARL batch.
NOTE: Chain detection is judgment-based in Phase 1. Becomes systematic in Phase 4.

[Approve All] [Approve Selective] [Adjust]
```

---

## Overflow Handling

When a domain exceeds the cap of 5:

1. Top 5 by priority → Batch 1 (spawn now)
2. Remainder → Batch 2 (spawn after Batch 1 completes)
3. Batch 2 receives Batch 1's conclusions as confirmed context (don't re-derive)
4. If overflow is all 🟢, consider holding for next cycle instead of spawning

---

## HOLD Policy

Not every signal justifies a spawn. Single 🟢 or 🟡 signals can accumulate:

- **Spawn immediately:** Any 🔴, or ≥3 signals in one domain
- **Hold for accumulation:** 1-2 🟡/🟢 signals in a domain — queue until batch fills or next cycle
- **Exception:** Will says "go" on any batch regardless of count

**HOLD storage:** Held signals are written to `AGENTS/{AGENT}/mail/inbox/` as normal signal packages (they exist as files regardless of spawn status). The routing table tracks their HOLD status. On next triage cycle, Prome checks inbox counts before routing new signals. This means HOLD state survives session clears — it's in the filesystem, not in memory.

---

## Structured Agent Output Template

Every agent spawn under this protocol must return output in this format:

```
## [AGENT] Batch Output — [date]

### Signal Results
For each signal processed:
- **Signal:** [one-line]
- **Delta:** [what changed in the domain — factual]
- **Threshold:** [did any threshold move? YES/NO + which]
- **Positioning:** [what this means for trades — 1 sentence]
- **Confidence:** HIGH / MEDIUM / LOW

### Synthesis
- **Domain state change:** [net assessment — better/worse/unchanged]
- **Convergence score change:** [if applicable]
- **Action items:** [concrete next steps]
- **Cross-agent flags:** [signals that matter for other domains → feeds HERMES routing]

### [Optional: Domain-Specific]
[Agents may add domain-specific sections — e.g., HAWK scenario probabilities, BROCK NAV marks, SAM carry unwind probability. Core fields above are mandatory; this section is flexible.]
```

---

## Anti-Patterns

| ❌ Don't | ✅ Do |
|----------|-------|
| Dump all signals into one agent regardless of count | Cap at 5, overflow to next batch |
| Give agents open-ended "analyze this" mandates | Frame specific analytical questions |
| Load full STATUS + KB for every spawn | Load only refs relevant to this batch |
| Fire all agents in parallel when chains exist | Sequence dependent agents, parallelize independent |
| Spawn for a single 🟢 signal | Hold until batch fills or urgency demands |
| Route one signal to 3+ agents | 1 primary, 1 secondary max |
| Skip the routing table | Always present for approval before spawning |

---

## HERMES Integration

Cross-agent flags from agent output templates feed into HERMES routing. When an agent's batch output includes cross-agent flags, those get written to the flagged agent's inbox as AGENT-type signals (Source Type = AGENT in SIGNAL_PROTOCOL.md). HERMES delivers on its normal 2x daily cycle unless flagged 🔴.

---

## Known Limitations (Phase 1)

| Limitation | Addressed In |
|------------|-------------|
| Refs field is prompt instruction, not mechanical | Phase 3 |
| Chain detection is judgment-based | Phase 4 |
| Output template compliance is not verified | Phase 3 (NEXUS as quality gate) |
| HOLD state requires manual inbox count check | Phase 5 (automated monitoring) |

---

## Changelog

- 2026-03-17: Created. Phase 1 of harness improvement project.
- 2026-03-17: Patched — clarified relationship to SIGNAL_PROTOCOL.md, HOLD storage, Refs implementation status, HERMES integration, output template flexibility, chain detection scope.
