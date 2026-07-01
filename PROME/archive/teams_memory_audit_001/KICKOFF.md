# Memory Audit 001 — Kickoff Brief

**Team:** memory-audit-001
**Team lead:** Prome (Telegram/OpenClaw surface, this session)
**Members:** curator, critic
**Date:** 2026-05-18
**Test purpose:** First bounded test of the Claude Code Agent Teams primitive. The work output is valuable (we need this audit done), but the **primary goal is to evaluate whether the teams primitive adds value over solo work** — specifically the adversarial-pair pattern.

---

## What we're auditing

`PROME/MEMORY_DRAFT_2026-05-17.md` — 8 candidate entries (6 main, 2 lower-confidence) drafted by Claude Code Prome for integration into the **root** `MEMORY.md` (curated thesis-level discoveries, last updated 2026-04-05).

**Do not confuse two memory layers:**
- **Root `MEMORY.md`** at `/home/willi/Research-workspace/MEMORY.md` — curated thesis-level discoveries, ~49 lines, used by Telegram/OpenClaw Prome. THIS is the integration target.
- **Auto-memory** at `~/.claude/projects/-home-willi-Research-workspace/memory/` — Claude Code persistent layer for user preferences and feedback patterns. NOT the integration target, but a useful cross-reference for redundancy checks.

## Output target

The audit produces a **keep/reject/rephrase** verdict for each of the 8 candidates, with reasoning, that Prome can hand to Will for a final 3–5 entry selection (per the draft's stated process: "Picks the 3–5 that meet the lasting-discovery bar").

## Roles

### curator
Argue **what's worth saving.** For each of the 8 candidates:
- Score keep / reject / rephrase
- Tone-match check against existing MEMORY.md entries (terse, event-dated, ends with `→ <file pointer>`)
- Note where it should live: root MEMORY.md / auto-memory / both / nowhere
- Flag entries that overlap existing MEMORY.md entries (e.g., draft #4 OZK overlaps Mar 25 "WAL + OZK Complementary Shorts"; draft #5 may overlap "Persistent Agents — Do Not Spawn")

Output: `curator_recommendations.md` in this directory.

### critic
**Adversarial pass.** Independently — without reading curator_recommendations.md — score the same 8 candidates with a skeptical lens:
- Which entries are NOT lasting discoveries (mid-session state that will be stale in a week)?
- Which are miscategorized (would be auto-memory feedback, not root thesis discovery)?
- Which are vague, redundant with existing entries, or over-claim?
- Which entries are weakly evidenced and should be rejected on integrity grounds?

Output: `critic_concerns.md` in this directory.

Critic should default to **adversarial**: the existing MEMORY.md bar is high (4-12 month thesis-relevant discoveries). Default verdict on weak entries: reject.

### Reconciliation (Round 2)
After both outputs land, **curator** initiates a DM exchange with **critic** via SendMessage to resolve disagreements. Output: `joint_decision.md` — per-candidate final verdict (keep/reject/rephrase + which layer + final phrasing if kept).

---

## Constraints

**Read-only on the repo except for your assigned scratch file.**

- ✅ Read freely: `PROME/MEMORY_DRAFT_2026-05-17.md`, `/home/willi/Research-workspace/MEMORY.md`, `AGENTS/*/STATUS.md`, `AGENTS/PROME/CLAUDE.md`, `/home/willi/Research-workspace/CLAUDE.md`, `~/.claude/projects/-home-willi-Research-workspace/memory/MEMORY.md` (index of auto-memory)
- ✅ Write: ONLY your assigned file in `PROME/scratch/teams_memory_audit_001/`
- ❌ Forbidden: editing root `MEMORY.md`, editing any auto-memory file, editing `MEMORY_DRAFT_2026-05-17.md`, running `git` commands, spawning sub-agents, sending external messages, modifying any other file in the repo

## Task list (shared)

The team has 3 shared tasks. Claim by setting `owner` to your name via TaskUpdate.
- **T1** — curator: score 8 candidates → `curator_recommendations.md`
- **T2** — critic: adversarial pass on same 8 → `critic_concerns.md`
- **T3** — curator + critic: reconcile via DM → `joint_decision.md` (blocked on T1+T2)

Mark tasks `in_progress` when you start and `completed` when done.

## Communication

- **Within team:** SendMessage by name (`curator`, `critic`, `team-lead`).
- **Going idle is normal.** After your turn ends you idle until messaged. Don't treat that as failure.
- **No JSON status messages.** Plain text. Use TaskUpdate for status, not chat.

## Done criteria

`joint_decision.md` exists with per-candidate verdicts and final phrasings; both teammates marked their tasks complete; both teammates ready for shutdown.
