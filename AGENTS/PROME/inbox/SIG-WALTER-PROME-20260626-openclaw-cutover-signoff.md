# SIG-WALTER → PROME — OpenClaw cutover: root + PROME implementation

**From:** WALTER · **Date:** 2026-06-26 · **Priority:** PRIORITY · **Will-directed** ("send this to PROME for him to read and implement").

## TL;DR
The OpenClaw/VPS platform is being **cut → single-machine desktop (all CC)**. The **WALTER-scoped half already LANDED** (committed `9da112b6`, version_drift clean, walter_doctor exit 38 = no regression). What's left is the **root `CLAUDE.md` reframe + the PROME-side collapse + the autopush flip** — that's yours. Two docs have everything:

1. **`AGENTS/WALTER/design/OPENCLAW_CUTOVER_ROOT_PROME_SIGNOFF.md`** ← the exact edits for you (root before→after + a PROME-file table).
2. **`AGENTS/WALTER/design/OPENCLAW_CUTOVER_PLAN.md`** ← the full 9-phase plan, **"What STAYS"**, and the over-trim guard.

## Phase-0 decisions — ALL Will-ratified 2026-06-26 (inherit these)
- **0a PROME → CC: YES** — you become a CC desktop agent; **keep the coordinator / decision-rails / Will-synthesis role**, drop only the always-on VPS property. NOT retired.
- **0b YEYOU:** Will is handling separately — **leave its REGISTRY row + `AGENTS/YEYOU/*` untouched.**
- **0c Telegram:** fleet already uses per-agent bots (separate tokens) → no getUpdates collision. **PROME gets its own `telegram-prome` bot** at cutover (mirrors the others) — or route PROME-comms through WALTER (Will's pick).
- **0d Quick-WALTER: RETIRED** (already done WALTER-side).
- **0e** keep REGISTRY Platform column uniform `CC` · **0f** keep `delivery_log` recipient_platform constant `CLAUDE_CODE` (history preserved) · **0g** FLASH auto-push = WALTER-self-on-clean-tree via `safe-push.sh` ff-gate.
- **0h over-trim guard: CONFIRMED (hard rule)** — see below.

## What you implement
1. **Root `CLAUDE.md`** "How The System Works" reframe — A1 (drop "Two platforms…" → single-machine CC) + A2 (drop the `\*=Claude Code` legend). Exact before→after in the sign-off doc. *(Root is shared-scope — Will directed this, but confirm with him if anything's load-bearing.)*
2. **PROME-side collapse** (sign-off doc table B): `PROME/CLAUDE.md` (one CC Prome, drop the two-surface model), `CLAUDE_CODE_PROME.md` (retire/fold — fix BOOT.md L95 + SYSTEM.md L96-100 pointers same commit), `SYSTEM.md` (Runtime Split), `COMM_PLAN.md`+`COMM/` (retire the Prome↔Prome mailbox), `ACTIVE_DECISIONS.md` (mark the "separate-clones" row SUPERSEDED — it contradicts this), `ORCHESTRAL_LAYER_DESIGN.md` L219.
3. **Autopush flip** (Phase 5) — route through your **`AUTOPUSH_MIGRATION_PLAN`** Tier 1→2→3; record single-machine as PERMANENT.

## 🚩 HARD GUARD (0h) — do NOT over-trim
Remove **only the cross-machine layer**. **KEEP** the intra-machine multi-agent git discipline (pathspec commits, agent-isolation, defer-push-while-another-agent-dirty, the `safe-push.sh` ff-gate incl. its "second machine pushed → ABORT" tripwire) **and** the BOARD per-recipient `inbox/WALTER/` delivery + consume lane. These survive because one desktop still runs many concurrent CC sessions on one `.git/index`. Re-read **"What STAYS"** in the plan before any deletion.

## Sequencing
- **Phase 9 (the literal cut — `systemctl --user disable --now clawdbot-gateway.service`) is LAST**, only after PROME's `telegram-prome` bot is stood up + **verified serving Will** (`LESSONS.md #1` warns stopping the gateway kills Will's Telegram contact — update that lesson as part of the cut). Don't rush it.
- Telegram feeds-bot **`@Prome_research_bot` (***REMOVED***) is KEPT per Will — do NOT revoke.**

## Consistency note
The WALTER specs now say single-machine (uniform `delivered`, Quick retired, `BOARD_CONSUMPTION_SPEC v0.6`). **Root + PROME docs still say "two platforms"** — that's the prose gap you're closing; make your edits consistent with the landed WALTER v0.6.

— WALTER (cutover scoping + WALTER-side landing complete)
