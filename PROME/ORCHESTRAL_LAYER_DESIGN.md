# ORCHESTRAL LAYER DESIGN

**Date drafted:** 2026-05-18
**Status:** design captured; prototype not yet started
**Drafted in:** Prome theory-crafting session with Will, post-memory-audit-001

---

## Problem statement

Will's bottleneck is not execution speed — it's **direction overhead**. The fleet has ~13 active agents plus catalysts, open proposals, contradictions, and stale states. Tracking what each agent should be doing requires Will to carry the full landscape in his head every session, which doesn't scale.

Will's framing: "It is hard to know how to direct the agents. There is so much data and so many threads to manage that I think I would benefit from help with an orchestral layer."

Note: this is exactly the role Prome is supposed to play per `AGENTS/PROME/CLAUDE.md` ("chief of staff, coordinator, second brain"). The role is named correctly; the discipline hasn't been consistent. This document is the design for the discipline.

## Goal

An orchestral layer that converts the fuzzy "what should I be doing" cognitive load into a one-page, on-demand situation report with ranked next moves and pre-drafted task packets, without blowing out Prome's context window in the process.

## Three required capabilities

| Capability | Output | Trigger (initial) |
|---|---|---|
| **Fleet scan** | Situation report: stale agents, open proposals, catalysts, contradictions, red flags | On Will's request (manual; automate later if useful) |
| **Top-N move generator** | "Highest-value next 3-5 actions with reasoning and time estimates" | Within fleet scan output |
| **Task-packet drafting** | Pre-drafted inbox packets ready for one-touch approve | On demand after top-N selection |

## Architecture: layered with context discipline

The key constraint is **Prome's context window** — Prome cannot read 13 STATUS files + inboxes + HEARTBEAT + commits without polluting its conversation context. Solution: delegate heavy reading to subagents/teammates; Prome only sees synthesized decision-grade outputs.

```
Will requests "fleet scan"
        ↓
Prome spawns fleet-scanner subagent (general-purpose, foreground)
        ↓
Scanner reads (read budget):
  - first ~30 lines per AGENTS/*/STATUS.md
  - git log --oneline -5 -- AGENTS/<NAME>/  (per agent)
  - each agent's inbox/ for unprocessed items
  - HEARTBEAT.md catalyst calendar
  - PROME/TOSCANINI/QUEUE.md (currently stale; rebuild may be part of this)
        ↓
Scanner writes PROME/FLEET_SCAN.md (fixed-section template)
Scanner returns to Prome a ~10-line summary only
        ↓
Prome reviews PROME/FLEET_SCAN.md
        ↓
(Optional) Prome spawns adversarial-pair team to refine top-N moves:
  - Scanner-proposer: argues all 8 candidate moves matter
  - Challenger: argues 5 are noise, 3 are real
  - Reconciliation: forced-rank top 3 with reasoning
        ↓
Prome presents to Will: "here's the situation; here are the top 3 moves;
                        want me to draft task packets for any?"
        ↓
Will approves N moves
        ↓
(Optional) Prome spawns revival-proxy teammates for stale agents
whose revival is in top-N:
  - Each proxy briefed with target agent's STATUS + KB + inbox + recent commits
  - Each does catch-up pass + drafts STATUS updates + proposes top-3 domain moves
  - Writes "Prome-sourced revival packet" to target agent's inbox
  - Real persistent agent integrates on next boot
```

Each layer protects Prome's context:
- Scanner does heavy reading → Prome sees a summary
- Adversarial pair does heavy prioritization debate → Prome sees the ranked list
- Revival proxies do heavy catch-up reading → Prome sees revival packets ready for delegation
- Prome only synthesizes the decision-grade outputs for Will

## FLEET_SCAN.md template (proposed v1)

```
# FLEET_SCAN — [date]

**Scanner:** fleet-scanner-001 (subagent of Prome)
**Coverage:** [agents covered]
**Read budget:** first 30 lines per STATUS; last 5 commits per agent dir; inbox file counts
**Heavy reads delegated; this file is Prome's working surface.**

## 1. Health Table
| Agent | STATUS age (days) | Last commit (days) | Inbox unprocessed | Position relevance | Catalyst proximity (days) |

## 2. Stale Agents — Decision Needed
| Agent | Days stale | Why it matters now | Revive / defer recommendation |

## 3. Open Proposals Awaiting Will
| Date sent | Agent | Proposal summary | Days waiting |

## 4. Upcoming Catalysts (next 14 days)
| Date | Catalyst | Owning agent | Readiness status |

## 5. Cross-Agent Contradictions (if any)
[free-form: Agent X says Y; Agent Z says not-Y; resolution path]

## 6. Top-N Moves (pre-adversarial-pair)
1. [Move] — [reasoning] — [agent owner] — [time estimate]
2. ...

## 7. Open Loops
| Proposal | Agent | Status | Next action |
```

Will opens this file at session start. Two minutes of reading replaces an hour of carrying state in head.

## Ranking criteria for Section 6 (Top-N Moves)

Distilled from the retired `PROME/TOSCANINI/HUNTING.md` (now in `PROME/archive/TOSCANINI_2026-03/`). The fleet-scanner uses this rubric to rank candidate moves rather than eyeballing it.

**Score each candidate move on six dimensions (0-3); apply weights; sum. Max 22.5.**

| Dimension | Weight | 0 | 1 | 2 | 3 |
|---|---:|---|---|---|---|
| **Position Proximity** | ×2.0 | No connection to any position | Indirect — feeds a thesis that feeds a position | Direct — informs sizing/timing/exit of an open position | Urgent — position at risk without this work |
| **Time Pressure** | ×1.5 | No deadline | Weeks away | Days away | Hours away / window closing |
| **Blindness Risk** | ×1.0 | Full coverage, recent data | Slightly stale (<3d) | Stale (3-7d) or missing key data | Flying blind on something live (>7d stale, active domain) |
| **Convergence Potential** | ×1.0 | Single agent | Touches 2 agents | Touches 3+ agents or feeds NEXUS | Could shift scenario probabilities or thesis confidence |
| **Decay Rate** | ×1.0 | Stable — same value next week | Moderate — loses context over days | Degrades within 48h | Perishable — value → 0 if not acted on today |
| **System Freshness** | ×1.0 | No upstream refreshes | 1-3 agents refreshed | 4-8 agents refreshed | 9+ refreshed — synthesis trigger (NEXUS/RED territory) |

**Priority prefix from score:** 🔴 ≥14 · 🔵 7-13 · 🟢 <7. Section 6 lists top 5 ranked by total score; show the score next to each entry.

**Anti-patterns to refuse (do not let these dominate Section 6):**
- **Busywork bias** — "refresh stale agent" scores high on Blindness but low on Position Proximity. Don't let hygiene crowd out real moves.
- **Loudness bias** — the most dramatic signal isn't always the most actionable. Quiet analyst downgrades can beat flashy geopolitical headlines.
- **Completionism** — not every gap needs filling. Stale agents whose domain isn't active stay stale.
- **Recency bias** — the signal that arrived 10 minutes ago isn't automatically more important than the one from two days ago still unprocessed.

## Prototype path (5 steps)

1. **Step 1 (next session, ~10 min):** Spawn `fleet-scanner` subagent (general-purpose, foreground). It produces `PROME/FLEET_SCAN.md` v1 against the template above. Will reads it. Will tells Prome what's useful vs noise, what's missing, what compression's too aggressive.

2. **Step 2 (iterate, ~2-3 cycles):** Refine the template based on Will's feedback. Keep iterating until the output is genuinely useful at first read.

3. **Step 3:** Layer adversarial-pair team on the top-N section. Scanner produces unranked candidates; pair refines to forced-rank top 3 with reasoning. (Same pattern as memory-audit-001.)

4. **Step 4:** If revival of stale agents is in top-N, prototype revival proxies. One stale agent at a time; verify the proxy's output is integrated cleanly by the real persistent agent on its next boot. (Identity-attribution risk — see open questions.)

5. **Step 5:** Once Will finds the manual flow valuable, decide on cadence:
   - On-request (current plan)
   - Session-start ritual
   - Daily scheduled routine
   - Telegram push for exception alerts only

## Next session entry point

When Prome next boots, the entry point for this work is **Step 1**:
- Will requests fleet scan (or Prome offers if no other priority displaces it)
- Prome spawns a fleet-scanner subagent with the template above as its brief
- Subagent produces `PROME/FLEET_SCAN.md` v1
- Will and Prome review; iterate template

Subagent brief should specify:
- Output: `PROME/FLEET_SCAN.md` with the 7 fixed sections from the template above
- Coverage: all `AGENTS/<NAME>/` directories present in the repo
- Read budget: first 30 lines per STATUS; last 5 commits per agent dir; inbox file counts; HEARTBEAT catalyst calendar; TOSCANINI QUEUE
- Return to Prome: ~10-line summary only (full output to file)

## Open questions / decisions deferred

- **TOSCANINI revival:** The proposal queue at `PROME/TOSCANINI/QUEUE.md` is stale since Mar 26. The orchestral layer's "Open Proposals Awaiting Will" section overlaps with TOSCANINI's purpose. Should TOSCANINI be rebuilt as part of fleet scan output, or kept separate?
- **Telegram-Prome vs CC-Prome split:** Fleet scan is naturally a CC-Prome task (subagent spawning, file writes). Will-facing synthesis is naturally Telegram-Prome. The handoff between the two surfaces during a fleet-scan flow needs to be smooth — TBD how.
- **Revival proxy attribution:** When a proxy writes to BROCK's inbox as "Prome-sourced revival packet," is that work attributed to Prome or to BROCK in the audit trail? Worth deciding before pattern goes live to avoid identity smearing.
- **Scanner read budget:** First 30 lines per STATUS is a guess; some STATUS files put the current-state header further down. Will iterate the budget based on Step 1 output quality.

## Related artifacts

- `PROME/scratch/teams_memory_audit_001/META_EVAL.md` — first teams test; established that adversarial-pair pattern produces measurably better output than solo for judgment-heavy bounded tasks. Same pattern proposed here for top-N refinement.
- Auto-memory `feedback_adversarial_brief_for_pair_teams.md` — reusable lesson on how to brief adversarial teams (explicit "default to negative" + "engage genuinely, don't be agreeable" framing).
- `AGENTS/PROME/CLAUDE.md` §"Operating Model — Chief of Staff" — names the role this design is implementing.
- `PROME/CLAUDE_CODE_PROME.md` — CC-Prome surface; orchestral layer is naturally a CC-Prome workflow.
