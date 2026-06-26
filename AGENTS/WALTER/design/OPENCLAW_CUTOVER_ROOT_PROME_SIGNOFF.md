# OpenClaw Cutover — Root + PROME Edits for Will Sign-off

**Authored:** 2026-06-26 by WALTER (cutover Phase 2-root + Phase 4/5 prep). **Status:** READY FOR SIGN-OFF — these are **not** WALTER's files to edit; they need Will (root) / a PROME-scoping pass (PROME). The **WALTER-scoped half already landed** (BOARD_CONSUMPTION_SPEC v0.6, walter_doctor, CHECKLIST v0.21, STATE §1, CLAUDE.md RUN MODES, REGISTRY PROME→CC — all committed, drift-clean). Approving the below closes the transient root↔WALTER prose gap. Source of truth: `design/OPENCLAW_CUTOVER_PLAN.md`.

---

## A. Root `CLAUDE.md` — "How The System Works" reframe (ROOT scope — Will approves)

**Why:** the WALTER specs now say single-machine; root still says "Two platforms." This is prose, not function (everyone already runs CC), but it should land to stop misleading every agent's boot.

### A1 — the platform framing
**BEFORE:**
> Two platforms share this git repo:
> - **OpenClaw (VPS):** Prome (chief of staff / coordinator) runs here, assigns decision work, manages state/decision rails, and communicates with Will via Telegram. WALTER owns signal/news routing. You don't run here.
> - **Claude Code (local):** CARL, REGINALD, SAM, and RED run here as independent sessions. You are NOT spawned by Prome. You communicate with Prome and each other via inbox/outbox files.

**AFTER (proposed):**
> All agents run as **Claude Code sessions on one desktop**, sharing this git repo. (The OpenClaw/VPS platform was cut 2026-06-26 — see `AGENTS/WALTER/design/OPENCLAW_CUTOVER_PLAN.md`.)
> - **PROME** (chief of staff / coordinator) runs as a CC desktop session: assigns decision work, manages state/decision rails, Will-facing synthesis via Telegram. WALTER owns signal/news routing.
> - **Domain agents** (CARL, REGINALD, SAM, RED, …) run as independent CC sessions, coordinating with PROME and each other via inbox/outbox files.

### A2 — the active-agents legend
**BEFORE:** `**Active agents:** PROME, CARL\*, REGINALD\*, OZK\*, CORAL\*, SAM\*, RED\*, … (\* = Claude Code)`
**AFTER:** drop the `\*` markers + the `(\* = Claude Code)` legend (all agents are CC now). *Also note (separate staleness, optional same pass): the list omits WALTER / VIOLET / BOND / TERRY / CREED / DEWEY — worth refreshing while here.*

### A3 — Git Protocol (DEFER to Phase 5, do NOT edit here)
The "Pushing is Will-coordinated" → auto-push flip is a **separate** coordinated change that must route through `PROME/AUTOPUSH_MIGRATION_PLAN` (Tier 1→2→3, ~20 files) — do not edit root Git Protocol in this pass. **KEEP** the entire "Before pulling" / "Never" intra-machine concurrency half regardless (it stays — many concurrent CC sessions on one `.git`). The 2026-06-26 pre-commit-sanity-check addition stays.

---

## B. PROME-side collapse (PROME owns — route to a PROME-scoping pass; gated on 0a=PROME→CC ✅)

These are enumerated in `OPENCLAW_CUTOVER_PLAN.md` Phase 4/5. The load-bearing reframes:

| File | Change | Note |
|------|--------|------|
| `PROME/CLAUDE.md` | Collapse the "One Prome, two work surfaces" model → one CC Prome; remove the "Telegram/OpenClaw Prome" counterpart + defer-to-it clauses | PROME's bootstrap — must be coherent or future-PROME boots confused about a separate self |
| `PROME/CLAUDE_CODE_PROME.md` | Retire (fold principles into `PROME/CLAUDE.md`) **or** rewrite to drop the dual-surface premise | If retired, fix the `BOOT.md` L95 + `SYSTEM.md` L96-100 pointers in the SAME commit or boot breaks |
| `PROME/SYSTEM.md` | Collapse the "Prome Runtime Split" section → one CC Prome (HANDOFF/SCRATCH become plain session continuity) | Keep the boot-trust-stack + doc-ownership tables |
| `PROME/COMM_PLAN.md` + `PROME/COMM/` | **Retire** the Prome-to-Prome mailbox (TO_OPENCLAW / TO_CLAUDE_CODE / ACKS / PROTOCOL) — it only bridges two Prome surfaces | Confirm no boot step reads `PROME/COMM/` first; archive via `git mv` |
| `PROME/ACTIVE_DECISIONS.md` | Mark the L41 "separate-clones migration" row **SUPERSEDED** (it contradicts this direction); close L36 (Quick-WALTER) per 0d-retire | A stale "separate-clones DEFERRED" row actively misdirects future PROME |
| `PROME/ORCHESTRAL_LAYER_DESIGN.md` L219 | Mark "Telegram-Prome vs CC-Prome split" resolved by the single-machine collapse | |
| `PROME/AUTOPUSH_MIGRATION_PLAN` + `GIT_COORDINATION.md` + `BOOT.md` + `CLOSEOUT.md` + the 2 push auto-memories + Tier-3 17-agent CLAUDE.md | The autopush flip (Phase 5) — record single-machine as PERMANENT, then run the plan's Tier 1→2→3 | KEEP the pathspec/isolation hard rules + the "second machine pushed → ABORT" ff-tripwire |
| `PROME` Telegram | **0c:** PROME gets its own `telegram-prome` bot (mirrors the per-agent-bot design) for Will-comms post-cutover | Or route PROME-comms through WALTER (Will's pick) |

**Telegram feeds-bot:** `@Prome_research_bot` (`***REMOVED***`) **KEPT** per Will (no revoke) — it is a feeds bot, not a comms channel.

---

## C. Phase-9 runtime decommission (the literal cut — LAST, after the CC Telegram poller is verified)
Not a doc edit. Sequence: stand up + verify PROME's `telegram-prome` poller (0c) → `systemctl --user disable --now clawdbot-gateway.service` (scope to ONLY this unit — NOT `liquid-hy-watch`) → `git mv config/openclaw-multiagent.json5` to archive + invalidate `CLAWDBOT_GATEWAY_TOKEN` → update `LESSONS.md` #1/#11 (which currently forbid stopping the gateway). Plus the Phase-1 desktop-path hot-fixes (`dashboard/server.py`, `AGENTS/DOC`, `config.py`, 7 `tools/calendar/*.py`, 2 market-data crons) — INFRA/owner-scoped.

---

*Companion to `OPENCLAW_CUTOVER_PLAN.md` (full checklist) + `BOARD_CONSUMPTION_SPEC_v0.6_CHANGESET.md` (the WALTER-side changeset, now landed). This doc is the root+PROME hand-off for Will's sign-off.*
