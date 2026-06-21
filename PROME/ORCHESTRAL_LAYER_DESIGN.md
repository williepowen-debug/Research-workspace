# ORCHESTRAL LAYER DESIGN

**Date drafted:** 2026-05-18
**Last updated:** 2026-05-19 (v3 brief-spec folded in after LIQUID + HENRY proxy prototypes)
**Status:** design + Step 1 (fleet-scan) + Step 4 (revival-proxy) prototyped; iterating on revival-proxy v3 brief spec
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
  - PROME/ACTIVE_DECISIONS.md + PROME/STATUS.md (open blockers/work queue)
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

Distilled from the retired `PROME/archive/TOSCANINI_2026-03/HUNTING.md`. The fleet-scanner uses this rubric to rank candidate moves rather than eyeballing it.

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

1. **Step 1 ✅ Prototyped 2026-05-18 (v1 + v2):** Spawned fleet-scanner subagent (general-purpose, foreground). v1 produced `PROME/FLEET_SCAN.md`; Will feedback drove v2 with six improvements (two-column staleness — header age vs self-commit age; dormant pre-filter; merged open-loops section; explicit HUNTING-math; math discipline; as-of price labels). v2 is the live working surface.

2. **Step 2 ✅ In progress:** Template iteration ongoing. v2 production-ready; v3 fleet-scan items deferred (directional semantics of kill levels; 5-7-point time series in pass-through; sweep-file internal triage; closeout-authorization of prior open questions) — **now codified into the Revival-proxy v3 brief spec below, since they apply identically to revival proxies and Section 6 ranking inputs.**

3. **Step 3:** Layer adversarial-pair team on the top-N section. Scanner produces unranked candidates; pair refines to forced-rank top 3 with reasoning. (Same pattern as memory-audit-001.) **Not yet prototyped.**

4. **Step 4 ✅ Prototyped 2× (2026-05-18):**
   - **LIQUID** (plumbing/funding agent) — first prototype. Validated pattern. Headline diagnostic: bear thesis migrated PLUMBING → DURATION (10Y +30bps over 32d, TLT broke 🔴) not CREDIT (HY OAS only -5bps). Returned 4 v2 improvements (now in v3 brief spec).
   - **HENRY** (market-structure agent) — second prototype, tests generalization from plumbing → market-structure. Validated pattern transfer. Headline diagnostic: COMPLACENCY TRAP invalidation triad approaching firing while substance accelerates the wrong way → trap clinching, not dying. Returned 5 additional v3 improvements (now in v3 brief spec). Also introduced **framing-precision overlay** as a new artifact type — see v3 spec.

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

## Revival-proxy v3 brief spec

Distilled from LIQUID (2026-05-18) and HENRY (2026-05-18) prototypes. The brief sent to a revival-proxy subagent should include all of the following. Items marked **[L]** came from LIQUID v2; **[H]** from HENRY v3.

### Tape pass-through (§1 of the packet)

- **[L]** Include a **5-7-point time series** for any metric where trajectory matters (HY OAS, 10Y, Brent, VIX, USD/JPY, KRE, WAL, APO). Single-point deltas hide direction-of-travel; the dangerous read is "compressing toward kill for 30 days" vs "noise around a stable mean."
- **[L]** Include a **zone-change column** in the tape-diff table (e.g., 🟢→🟡 or 🟠→🔴). Threshold crossings are operationally distinct from in-zone drift.
- **[H]** **"Cheap domain-relevant data pull" is explicit permission, not conditional.** If the proxy can pull a missing tape datum via yfinance/FRED in <60s and it's load-bearing for the verdict, do it. The Apr-17-vs-current-dashboard tier-mismatch problem (HENRY case: SPX/SKEW/VIX3M not in current dashboard) is solved cheaply.

### Thesis-kill proximity verdict (§2)

- **[L]** State **directional semantics explicitly**: which direction = thesis healing vs thesis approaching death. "OAS rising = healing, OAS compressing toward 260 = approaching death" is one sentence that prevents an entire class of misreads downstream.
- **[L]** Distinguish **literal trigger state** from **trajectory toward trigger**. Don't count "compressing toward" as "fired." See HENRY framing-precision note (2026-05-19) for what overspecification looks like.

### Cross-channel cohere/contradict (§3)

- **[H]** **Flag in-flight sister revivals** in the brief so the proxy cites rather than re-derives. HENRY's §3 (PLUMBING → DURATION migration) was load-bearing and came directly from the LIQUID packet shipped the same day; without the brief mentioning LIQUID, HENRY proxy would have re-derived it from raw data and wasted budget.
- **[H]** **Authorize peer-owned sub-domain KB reads.** When the revival target's thesis depends on a peer agent's domain (HENRY→VIOLET on vol; LIQUID→BRENT on energy-CPI loop), proxy reads peer KB entries that are load-bearing. Brief should permit this explicitly, not leave it as a guess.

### Domain catalyst prep (§4)

- **[H]** §4 is **"domain catalyst prep if 0-7d catalyst exists, else overflow register."** Originally LIQUID's §4 was a deferred-items register; HENRY's §4 was NVDA 5/20 prep. Generalize: if the target agent owns a live 0-7d catalyst, §4 is prep for it; otherwise §4 is the overflow register.

### Inbox triage (§5)

- **[L]** For all unprocessed inbox items at revival target, mark each as **STILL LIVE** (integrate), **SUPERSEDED** (newer data overrides), or **STALE** (event resolved, archive without integrating). Don't let unprocessed backlog land on the real agent as undifferentiated.
- **[H]** Read instruction is "**top N then stop and judge**," not "top N by relevance." Better to stop one-short and judge whether more reading would change the verdict than to pull a fixed N and find the last one was noise.

### Open questions / closeout authorization (§6)

- **[L]** For each prior unresolved open question, **authorize closeout or hold**: if data has since resolved them, recommend closeout; if still open, recommend hold. This gives the real agent mechanical first-20-minutes-of-revival work.

### Recommendations (§7)

- Concrete actions in priority order with effort estimates. Treat as Prome-sourced suggestions, not commitments — real agent owns final order.

### Artifact discipline (across all sections)

- **File naming:** `<TARGET>_REVIVAL_PACKET_<date>_prome-spawned.md` + `<TARGET>_STATUS_DRAFT_<date>_prome-spawned.md`. Suffix is load-bearing.
- **PROVENANCE header** on every file: "drafted by Prome-spawned proxy on <date>, not by <TARGET> itself. Treat as input, not as agent self-state. <TARGET> owns integration on next boot."
- **Untracked-by-design.** Prome does not commit the files; real agent commits them on next boot per agent-file-isolation rule.

### Framing-precision overlay (new artifact type, HENRY 2026-05-19)

When Will + Prome review a proxy packet and find the framing useful conceptually but overspecified on a literal claim, write a third artifact: `<TARGET>_FRAMING_NOTE_<date>_prome-spawned.md` in the same inbox. The note keeps the conceptual win, removes the overspecified count/claim, and tells the real agent how to integrate both packet and note coherently. Cross-agent inbox write requires explicit per-instance Will authorization (per existing memory).

---

## Open questions / decisions deferred

- ✅ **TOSCANINI revival — resolved 2026-05-18.** TOSCANINI retired; FLEET_SCAN.md replaced QUEUE.md as the open-loops surface; AUTONOMY.md + COMPLETION_SPEC.md salvaged to `PROME/`; HUNTING dimensions distilled into the Section 6 ranking rubric above; remaining files in `PROME/archive/TOSCANINI_2026-03/`.
- ✅ **Revival proxy attribution — resolved by convention 2026-05-18.** Files use `_prome-spawned.md` suffix + PROVENANCE header; real agent owns commit on next boot. Validated on LIQUID + HENRY without identity smearing.
- ✅ **Scanner read budget — resolved 2026-05-18.** First-30-lines proved insufficient for STATUS files with current-state headers further down; v2 budget includes inbox file counts + HEARTBEAT (full) + POSITIONS head + SCRATCH. v2 production-ready.
- **Telegram-Prome vs CC-Prome split:** Fleet scan is naturally a CC-Prome task (subagent spawning, file writes). Will-facing synthesis is naturally Telegram-Prome. The handoff between the two surfaces during a fleet-scan flow needs to be smooth — TBD how. Open.
- **Adversarial-pair on Section 6 top-N (Step 3):** Not yet prototyped. Open.

## Related artifacts

- `PROME/scratch/teams_memory_audit_001/META_EVAL.md` — first teams test; established that adversarial-pair pattern produces measurably better output than solo for judgment-heavy bounded tasks. Same pattern proposed here for top-N refinement.
- Auto-memory `feedback_adversarial_brief_for_pair_teams.md` — reusable lesson on how to brief adversarial teams (explicit "default to negative" + "engage genuinely, don't be agreeable" framing).
- `AGENTS/PROME/CLAUDE.md` §"Operating Model — Chief of Staff" — names the role this design is implementing.
- `PROME/CLAUDE_CODE_PROME.md` — CC-Prome surface; orchestral layer is naturally a CC-Prome workflow.
