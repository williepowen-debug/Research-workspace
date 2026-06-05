---
name: revival-proxy-pattern
description: Step 4 of PROME/ORCHESTRAL_LAYER_DESIGN.md — foreground general-purpose subagent briefed as revival proxy for a stale persistent domain agent. Produces decision-grade catch-up + inbox-deposited revival packet for target agent to integrate on next boot.
metadata: 
  node_type: memory
  type: project
  originSessionId: dfa2a11b-572d-41ae-90a2-9fb90c7415f3
---

First Step 4 prototype validated 2026-05-18 on LIQUID (32d self-commit stale, 19 inbox items, HY-OAS-260-kill watch unmanaged for a month). Pattern: foreground general-purpose subagent that acts as a proxy for a stale persistent agent, produces decision-grade catch-up and a revival packet in the target agent's inbox, never edits target's owned files, and lets target integrate on its next boot.

**Why:** *32-day-stale persistent agents accumulate KB drift, missed signals, and stale thesis state. Naive "spawn the agent" approaches blow context on integration and risk identity-smearing. The proxy pattern delegates the heavy catch-up to a single bounded subagent and produces decision-grade output that the real agent integrates on its own terms — preserves identity attribution, respects agent-file-isolation rule, and keeps Prome's main context clean.*

**How to apply:**

1. **Trigger:** stale persistent CC agent (self-commit-age >7d) whose domain is decision-relevant this session and gates active position decisions.

2. **Spawn:** foreground general-purpose subagent, **no `name` parameter** (named spawns trigger teams mode — see [[named-spawn-teams-mode]]).

3. **Brief structure (10 sections):**
   - Identity-attribution rules (you are PROXY not AGENT; PROVENANCE preamble on every file you write; `_prome-spawned.md` filename suffix; NO edits to target's STATUS/KB)
   - Working dir + today's date + agent dir path
   - Agent's domain (one paragraph)
   - **Strict read budget:** target's `STATUS.md` (full), `workbook/KB.tsv` tail-30, top-5 inbox items by priority (NOT all 19), `git log -10` for target's dir, `PROME/FLEET_SCAN.md` (substrate), `HEARTBEAT.md`. Forbid reading research/, full KB, cross-agent files.
   - **Live tape pass-through inline** (proxy does NOT re-run dashboard — Prome passes today's numbers as a code block)
   - The decision-grade question (kill-level proximity, regime call, cross-signal coherence)
   - **3 output deliverables:**
     - `AGENTS/<AGENT>/inbox/<AGENT>_REVIVAL_PACKET_<date>_prome-spawned.md` — analytical artifact (live-tape diff table, thesis-kill verdict, top-3 moves, top-5 inbox processed, deferred items table, open questions)
     - `AGENTS/<AGENT>/inbox/<AGENT>_STATUS_DRAFT_<date>_prome-spawned.md` — surgical proposed STATUS edits (NOT auto-applied; format as "replace this block with that block")
     - Return to Prome: ~15 lines summary (NOT full files)
   - **Anti-patterns to refuse explicitly:** "recover 32 days of work" (no — decision-grade only); "speak in agent's voice" (no — hedge as `based on STATUS + tape within proxy budget...`); "auto-edit target's STATUS/KB" (no — inbox writes only); "process all 19 inbox items" (no — top-5).
   - Verify arithmetic explicitly (math-discipline rule — see [[verify-counts-before-propagating]]).
   - End with: "Be honest in your return-to-Prome about what worked and what was awkward — pattern feedback matters."

4. **After proxy returns:** do NOT commit target's inbox files. They sit untracked until target's next boot per [[agent-git-isolation]]. This is by design — keeps identity attribution clean.

5. **Surface to Will:** the headline diagnostic (one-liner), the top-3 moves the proxy proposed, and the proxy's pattern-feedback for v2 of the pattern.

**Open design questions parked for v2 of the pattern (LIQUID-run feedback):**
- **Directional semantics of kill levels** — brief should state ("kill = bull floor; rising OAS = thesis healing") explicitly to avoid the proxy hedging the direction.
- **5-7-point time series in pass-through** (not just current snapshot) — enables cleaner rate-of-change math.
- **Sweep-file internal triage** — when inbox sweep files contain many signals each, brief should call for top-3 within the sweep, not just count the sweep as 1 slot of 5.
- **Closeout authorization for prior open questions** — proxy was unsure whether to declare April SOFR-IORB "resolved mechanical"; brief should authorize/disauthorize.

**Pattern validated on:** LIQUID 2026-05-18 (plumbing/credit domain). **Not yet tested on:** market-structure (HENRY), BDC/PC (BROCK), bank-domain (REGINALD — persistent + CC self-spawn so probably not applicable), geopolitical (HAWK), or insurer-PE (SHADE). Generalization across domains is the next-prototype question.

**Cross-references:** [[named-spawn-teams-mode]] · [[agent-git-isolation]] · [[break-multifile-updates]] · [[verify-counts-before-propagating]] · [[adversarial-brief-for-pair-teams]] (related pattern — adversarial pair on top-N output)
