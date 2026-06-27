# Auto-Push Migration Plan
**Created:** 2026-06-26 · **Owner:** Prome · **Status:** TIER 1 PROMOTED (canonical flipped 2026-06-26, soak passed). **GENUINELY COMPLETE 2026-06-27 PM** (after audit correction). ⚠️ The earlier "18/21 complete" claim was **over-counted** — the 2026-06-27 fleet-protocol audit found **7 active agents still on defer-push** (NEXUS, BRENT, VIOLET, REGINALD, BROCK, HAWK [contradictory], SHADE — three of which were never even in the Tier-3 inventory below). All 7 swept 2026-06-27 PM (commit `c7d216e1`). **Now: all 19 active domain agents on auto-push EXCEPT the 2 intentional holdouts** (TERRY = self-sweep, WALTER = architectural per `BOARD_CONSUMPTION_SPEC §7`); YEYOU = manual/branch by design. (CREED Tier-2 has no git section at all — separate low-pri item.) See the 2026-06-27 PM audit note below.
**Goal:** Replace the manual "Will-coordinated push" ceremony with **auto-push at closeout**, safely, predicated on single-machine operation.

> **2026-06-26 promotion (Will-approved, full):** Soak passed (multiple clean ff pushes, zero tripwire). Tier 1 canonical flipped — root `CLAUDE.md` Git Protocol, `PROME/GIT_COORDINATION.md` Push Discipline, `memory/auto/feedback_defer_push_coordinate.md` (rewritten, slug kept), `finding_push_train_pattern.md` (re-automated), `MEMORY.md` hooks. Tier 3 sweep STARTED: **RED + HAWK** flipped (both active this session). **Remaining Tier-3 (16):** BOND, BRENT, CARL, CORAL, DEWEY, LABOR, MARCO, NEXUS, ORACLE, OTTO, OZK, SHADE, TERRY, WALTER, + their CLOSEOUT.md (Tier 2.2–2.4 LIQUID/TERRY/YEYOU) — lazy-swept when next active. YEYOU stays manual/branch (Decision C). Un-swept agents are safe: they commit-local and ride the next agent's auto-push.

> **2026-06-27 AM progress (PROME, Will-approved):** Swept: **BOND, CARL, CORAL, DEWEY, HENRY, LABOR, MARCO, OZK** (8 — commit `07d04796`; **OZK got a full git-block rehab**, removing forbidden `git reset HEAD` ×2 + dir-`add`). **ORACLE self-flipped** its own block mid-session (commit `824a713e`). **Tier-2: `LIQUID/CLOSEOUT.md` flipped**. *(This was logged as "18/21 complete" — WRONG, see below.)*

> **2026-06-27 PM audit + correction (PROME, Will-approved):** A read-only fleet-protocol audit (20-agent Workflow fan-out; `PROME/cluster/2026-06-27_fleet_protocol_audit.md`) **disproved the "18/21 complete" claim** — it counted agents it never verified. **7 active agents were still on defer-push**: NEXUS, BRENT, VIOLET, REGINALD, BROCK, HAWK (internally contradictory: defer summary vs auto detail), SHADE. **Root cause:** the Tier-3 inventory below was incomplete — VIOLET/REGINALD/BROCK were never listed, so the lazy-sweep never reached them. **All 7 swept 2026-06-27 PM** (commit `c7d216e1`, verified residual-defer=0). **Net now: 17 auto-push + 2 intentional holdouts (TERRY/WALTER) = all 19 active; YEYOU manual.** Migration genuinely complete. **Lesson:** a self-reported migration count is not a verification — confirm by reading the actual files (`[[finding_verify_counts_before_propagating]]`).

## Decisions (Will, 2026-06-26)
- **Precondition:** ✅ single-desktop only (no VPS/laptop/web pushing) → plan greenlit.
- **A — Wiring:** closeout step (not a Stop hook).
- **B — Tier 3:** lazy-sweep + canonical pointer (no 17-file big-bang).
- **C — YEYOU:** (default) keep manual/branch model until reviewed.
- **D — Rollout:** Prome pilot first, then fleet after soak.

## Pilot status (DONE this session)
- ✅ Tier 0.1/0.2 — `scripts/safe-push.sh` promoted (PROME-owned copy); header de-prohibited → closeout-authorized; `--dry-run` tested green.
- ✅ Tier 2.1 — `PROME/CLOSEOUT.md` Chunk 4 wired to `safe-push.sh` + documented divergence (canonical docs unchanged during soak).
- ⏳ NEXT (after soak): Tier 1 canonical policy (root `CLAUDE.md`, `GIT_COORDINATION.md`, 2 memories) → then Tier 2.2–2.4 closeouts → then lazy-sweep Tier 3.

---

## Diagnosis (why this is safe to do)
- **OpenClaw is not the blocker.** Zero OpenClaw commits in the last 100; all committers are Claude Code agents. The push ceremony exists for **concurrent shared-tree/branch writers**, and the genuine hazard is **cross-MACHINE** non-fast-forward races (OpenClaw = the VPS = the 2nd machine).
- **Collapsing to one machine removes that hazard.** Same-machine multi-session concurrency (e.g. WALTER committed between Prome's commits today) is handled by git serialization + the push-train (one push sweeps all local commits — a feature).
- **The mechanism already exists and fails safe.** `AGENTS/CARL/scripts/safe-push.sh` is fast-forward-gated: it never pulls a shared tree, never forces, and **ABORTS cleanly if origin has commits we don't** (the cross-machine case). So even if a 2nd machine ever returns, auto-push degrades to a clean refusal, not corruption.

## Precondition (Will to confirm)
- [ ] **Single-machine operation** — all agent sessions run on this one desktop (no VPS/laptop/web-app pushing to master). If ever false → auto-push aborts safely, but we'd want per-agent branches instead.

---

## Change Inventory — tallied by tier

### TIER 0 — Mechanism (build/promote first)
| # | File | Action |
|---|---|---|
| 0.1 | `AGENTS/CARL/scripts/safe-push.sh` → promote to `scripts/safe-push.sh` | Move to a fleet-shared location (its own header says "PROME owns fleet-wide promotion"). |
| 0.2 | `scripts/safe-push.sh` header | Reverse the "DO NOT wire into closeout/hook" prohibition → "closeout-wired; ff-gated, fails safe." Keep all the safety logic. |
| 0.3 | Wiring | **Decision A (below):** call from `PROME/CLOSEOUT.md` Chunk 4 and/or a `Stop` hook in `.claude/settings.json`. |
| 0.4 | `scripts/fallback/stop_sync.sh` | Reconcile — it already auto-pushes memory via `pull --rebase --autostash && push`; align it to the safe-push model (or let safe-push supersede it). |
| 0.5 | `.claude/settings.local.json` | Push permission already allowed ✅. Add Stop hook here only if Decision A picks the hook route. |

### TIER 1 — Canonical policy (the source of truth — update these, not the 17 copies)
| # | File | Current | New |
|---|---|---|---|
| 1.1 | `CLAUDE.md` (root) — Git Protocol | "Pushing is Will-coordinated… commit locally" | "Auto-push at closeout via `scripts/safe-push.sh` (ff-gated); single-machine assumption." |
| 1.2 | `PROME/GIT_COORDINATION.md` — "Push Discipline" lease model | "Push only after Will coordinates the flush" | New auto-push-at-closeout policy + the single-machine precondition + safe-push as the gate. |
| 1.3 | `memory/auto/feedback_defer_push_coordinate.md` | "commit local, defer push until Will" | Rewrite → "auto-push at closeout (single-machine); safe-push ff-gate." **Keep the slug** (referenced by ~20 agent files — update the anchor, don't break refs). |
| 1.4 | `memory/auto/finding_push_train_pattern.md` | push-train = manual window | Still true; note it's now automated at closeout. |
| 1.5 | `memory/auto/MEMORY.md` | index hooks for 1.3/1.4 | Update the one-line hooks. |

### TIER 2 — Closeout protocols (behavior docs that say "defer push")
| # | File | Action |
|---|---|---|
| 2.1 | `PROME/CLOSEOUT.md` Chunk 4 | "push only on Will's call" → "run `scripts/safe-push.sh` as the closeout tail." |
| 2.2 | `AGENTS/LIQUID/CLOSEOUT.md` | Same flip. |
| 2.3 | `AGENTS/TERRY/CLOSEOUT.md` | Same flip. |
| 2.4 | `AGENTS/YEYOU/CLOSEOUT.md` | Same flip (note YEYOU is review-only / branch model — confirm it should auto-push). |

### TIER 3 — Agent CLAUDE.md copies (the big surface — ~17 files)
BOND, BRENT, CARL, CORAL, DEWEY, HAWK, LABOR, MARCO, NEXUS, ORACLE, OTTO, OZK, RED, SHADE, TERRY, WALTER, YEYOU each carry a "don't push / Will-coordinated" git block.
**Decision B:** big-bang sweep all 17 now, **or** update canonical (Tier 1) + add a one-line "push policy: see `GIT_COORDINATION.md` (auto-push at closeout)" and lazy-sweep each agent's full block when next touched. *Recommend lazy* — avoids a 17-file edit + the fleet-wide reference risk we hit on the git-cluster memory consolidation.

### TIER 4 — Incidental mentions (NO action)
~30 STATUS/SCRATCH/MEMORY/research/handoff files mention push-coordination in passing — historical narrative, leave them.

---

## Recommended sequence (pilot-first, reversible)
1. **Will confirms single-machine** (precondition).
2. **Tier 0:** promote `safe-push.sh`, de-prohibit header, test `--dry-run`. (No behavior change yet.)
3. **Pilot:** wire only `PROME/CLOSEOUT.md` (Tier 2.1) to call it — Prome auto-pushes at closeout for a session or two. Watch for any non-ff aborts.
4. **If clean:** update canonical policy (Tier 1) + remaining closeouts (Tier 2.2–2.4).
5. **Lazy-sweep** Tier 3 agent CLAUDE.md blocks as each agent is next active (or big-bang if Will prefers).

## Decisions needed from Will
- **A — Wiring:** closeout-step (explicit, per-agent), Stop-hook (fires every session-end automatically), or both?
- **B — Tier 3 scope:** big-bang sweep 17 agent files now, or lazy-sweep + canonical pointer?
- **C — YEYOU:** YEYOU is repo-wide-reviewer on a branch model — keep it manual/branch, or include in auto-push?
- **D — Pilot vs all-at-once:** Prome-pilot first (recommended), or flip the whole fleet in one pass?

## Risk / rollback
- **Primary safety:** `safe-push.sh` fails SAFE — aborts on non-ff (cross-machine), never force/pull-on-shared-tree. Worst case = a clean refusal that surfaces the problem.
- **Rollback:** revert the closeout-step + restore the "Will-coordinated" line = one commit. Fully reversible.
- **Accepted tradeoffs:** (1) lose the manual "is this ready?" review gate; (2) pushed history can't be cleanly amended/rebased — mitigated by pushing at *closeout* (coherent units), not per-change.
- **Tripwire:** if a 2nd machine ever returns, safe-push starts aborting — that's the signal to switch to per-agent branches.
