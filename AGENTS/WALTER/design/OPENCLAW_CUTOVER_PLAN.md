# OpenClaw Cutover — Migration Plan (single-machine / desktop CC)

**Authored:** 2026-06-26 by WALTER (scoping pass, Will-directed). **Status:** SCOPING DRAFT — execution Will-coordinated; touches root/PROME/infra scope (WALTER does not edit those unilaterally). **Method:** 4-agent parallel discovery (115 touchpoints) → synthesis → adversarial completeness critic. Verified load-bearing facts live (committed tokens, dead paths, walter_doctor Platform-index, the active gateway unit).

---

## Goal & scope

Move to a **single-machine default** (the desktop, Claude Code / "CC"); cut the OpenClaw VPS. This removes **only the cross-machine layer** (the VPS host, two-platform framing, platform-nuanced delivery, the push-authority split). Push becomes "commit → push" with no cross-machine rebase.

### What STAYS (do not cut these by accident — see #1 hazard)
- **GitHub remote = single source of truth.** We cut the second *local*, not the remote. GitHub Actions still read/write `master`.
- **Intra-machine multi-agent git discipline** — pathspec commits (`git commit <path>` modified / atomic add+commit new), agent-git-isolation (never touch another agent's files), defer-push-while-another-agent-is-dirty, stash/pull/pop, never `git reset HEAD`, the `scripts/safe-push.sh` ff-gate. These survive because **one desktop still runs many concurrent CC sessions against one `.git/index`.**
- The **BOARD + per-recipient `inbox/WALTER/` delivery lane + `delivery_log.tsv` + consume-and-git-mv** mechanism, and the **12 per-agent consume boot-step blocks** (HAWK/LABOR/LIQUID/BRENT/ORACLE/HENRY/BROCK/NEXUS/CORAL/SHADE/BOND/VIOLET) — all intra-machine and **platform-agnostic**.
- **GitHub-Actions always-on feeds** (the Scout build) — the go-forward for cron feeds; PROMOTED from plan to build, not cut.
- **PROME's coordinator / decision-rails / Will-synthesis ROLE** — PROME is NOT retired; only its always-on VPS property drops.
- Append-only history (42 OPENCLAW rows in `delivery_log.tsv`, all spec version-history) — **never rewrite; append a collapse entry.**

### 🚩 #1 hazard — OVER-TRIM
Removing the cross-machine layer must NOT remove the intra-machine concurrency guards or the consume lane. This is the dominant failure mode of the whole migration. Issue it as a standing instruction to every executing agent.

---

## 🔴 URGENT — do regardless of any decision (security + active breakage)

1. **Two exposed secrets — rotate/invalidate now:**
   - **Telegram bot token** committed in plaintext at `FORGE/tools/news-sweep/cron_sweep.sh:10` (and in git history). Deleting the file does NOT un-compromise it → **rotate + move to a GitHub Secret** (also a Scout prerequisite).
   - **`CLAWDBOT_GATEWAY_TOKEN=***REMOVED***…`** in plaintext in the systemd unit `~/.config/systemd/user/clawdbot-gateway.service` → invalidate when the gateway is decommissioned (Phase 9).
2. **Dead `/home/moltbot/.openclaw/workspace` paths — broken on the desktop right now:** `dashboard/server.py` (~10 joins + `.bak`), `AGENTS/DOC/CLAUDE.md` (9 paths), `FORGE/tools/news-sweep/config.py:430`, **7 `tools/calendar/*.py`**, `FORGE/tools/market-data/cron_dashboard.sh` + `morning_briefing.sh`. Dashboard, DOC, and calendar-sync are silently broken until repointed to `/home/willi/Research-workspace` (or `__file__`/env-derived).

---

## ⚠️ THE actual cut — and why it must come LAST (Phase 9)

The literal OpenClaw on this box = **`clawdbot-gateway.service`** (systemd user unit, **enabled + active now**) + git-tracked **`config/openclaw-multiagent.json5`** (the gateway config it reads). The migration is "cut OpenClaw," so the terminal act is `systemctl --user disable --now clawdbot-gateway.service` + archive the config + invalidate the gateway token.

**Hard ordering dependency:** this is NOT parallelizable with Phase 0. `LESSONS.md #1` warns that stopping the gateway **kills Will's Telegram contact**. Sequence: **(Phase 0 Telegram decision) → stand up + verify a CC-native Telegram poller is serving Will → disable the gateway → archive config + invalidate token.** `LESSONS.md` itself must be updated as part of this (it currently forbids the act).

---

## Phase 0 — Lock the gating decisions (everything downstream inherits these)

> **✅ 0e / 0f / 0g RATIFIED by Will 2026-06-26:** keep-uniform-`CC` · keep-constant `CLAUDE_CODE` · FLASH/IMMEDIATE auto-push = WALTER-self-on-verified-clean-tree via the `safe-push.sh` ff-gate. **No schema migration needed.** Remaining Phase-0 gates: **0a** PROME→CC · **0b** YEYOU keep/cut · **0c** Telegram ownership · **0d** Quick-WALTER retire/repurpose · **0h** standing over-trim instruction.

| # | Decision | Recommendation | Risk if unresolved |
|---|----------|----------------|--------------------|
| 0a | **PROME fate** | → **CC desktop agent** (keep coordinator/decision-rails/Will-synthesis; drop always-on). NOT retired. | HIGH — ~15 PROME-doc edits + the root reframe cascade from this. |
| 0b | **YEYOU disposition** | move-to-CC **vs CUT** (never went live, 0 reviews; Codex/PROME covers deep review → cut is low-cost). **Prereq either way:** land the live YEYOU branch `origin/claude/busy-rubin-bo2hu5` + dirty `AGENTS/YEYOU/*` first, or that work strands. | MED |
| 0c | **Telegram ownership** (HIGH foot-gun) | PROME-on-CC + WALTER-on-CC sharing one token → `getUpdates` delivers each inbound to only ONE poller → **~half of Will's messages silently dropped** (proven, commit `887b8d73`). Pick: (a) WALTER-scope-only + route PROME comms through WALTER, (b) separate PROME token, (c) one coordinator-of-record. | HIGH |
| 0d | **Quick-WALTER RUN MODE** | RETIRE (only Full WALTER) **vs** REPURPOSE as a CC-spawned route-only session (strip VPS framing, keep the registry-only whitelist + Iran-anchor guard). Cascades to 4 files. | MED |
| 0e | **REGISTRY Platform column** | **keep-uniform-CC** (recommend; vestigial, zero blast radius) vs drop (TSV schema change — must land in lockstep with `walter_doctor` `header.index('Platform')` or ValueError → silent stale fallback). | MED |
| 0f | **`delivery_log.tsv` recipient_platform** (col 5) | **keep-as-constant `CLAUDE_CODE`** (recommend; zero migration, preserves the 42 historical OPENCLAW audit rows) vs drop (forces 191-row + doctor + CHECKLIST + STATE lockstep). | MED |
| 0g | **FLASH/IMMEDIATE auto-push authority** (was PROME's per §3.4/§7) | reassign → Will-coordinated window **or** WALTER-self-on-verified-clean-tree via safe-push ff-gate. | MED |
| 0h | **Standing instruction** | Confirm: intra-machine concurrency discipline STAYS; the cut removes ONLY cross-machine. (The over-trim guardrail.) | HIGH |

---

## Phase 1 — Urgent hot-fixes & security (no decision; run up front, parallel with Phase 0)
- Rotate the committed Telegram token → GitHub Secret. *(INFRA/Will)*
- Repoint `dashboard/server.py` WORKSPACE off `/home/moltbot` → repo root or env-derived. *(INFRA)*
- Migrate the 9 `/home/moltbot` paths in `AGENTS/DOC/CLAUDE.md` (route to DOC's owner). *(OTHER-AGENT)*
- Repoint `FORGE/tools/news-sweep/config.py:430` WORKSPACE (AGENTS_DIR derives from it — a **Scout prerequisite**, not a no-op), `tools/calendar/*.py` (×7), `FORGE/tools/market-data/cron_dashboard.sh` + `morning_briefing.sh`. *(INFRA)*
- Land/reconcile the live YEYOU branch + dirty `AGENTS/YEYOU/*` into master **before** the 0b disposition. *(PROME/Will)*

## Phase 2 — Collapse the CANONICAL specs first (WALTER canonical-source rule)
- **Root `CLAUDE.md`** — drop "Two platforms share this git repo" + the OpenClaw(VPS)/CC split; state PROME is a CC desktop agent; collapse the `*=Claude Code` legend. KEEP file-based inbox/outbox + "Prome is chief of staff" + GitHub-as-source. *(ROOT — Will/root-owner; land in lockstep with Phases 2-WALTER + 4-PROME.)*
- **`BOARD_CONSUMPTION_SPEC.md` → v0.6** — retire the §3.3 two-row platform table → `delivered = handoff committed AND on-origin`; collapse §1/§6.1/§6.2 (keep the shallow-clone INFO guard); §3.4 drop the `(Claude-Code recipients)` qualifier (keep the clean-tree scoped-push *mechanism*, reassign authority per 0g); §7 push-authority per 0g; §8 all recipients self-apply consume (drop "PROME installs OpenClaw boot steps"); §9 Quick per 0d; §4 recipient_platform per 0f; §10 drop VPS justification. **APPEND** a history entry, don't rewrite. *(WALTER — may be owned by a parallel WALTER agent; coordinate.)*

## Phase 3 — Propagate to WALTER dependents (after Phase 2; bump versions, pass version-drift)
- **`walter_doctor.py`** — retire/constant-ify `_cc_agents()`/`_CC_FALLBACK` (the `header.index('Platform')` at L66) per 0e; drop the `platform=='OPENCLAW'` short-circuit in `delivered_but_unconsumed` (L430); retire the OpenClaw branch in `written_but_undelivered` (L470) → single on-origin ladder; **repoint `cron_liveness` (L222-240)** off the 3 dead feeds → Scout digest (else false-MED forever). KEEP the shallow-clone/origin/sync guards. **Must land in the same commit as any Platform-column drop.**
- **WALTER `CLAUDE.md`** — RUN MODES per 0d; step 0.5 drop the "runs on the VPS" clause (keep portable-python fallback); step 7c repoint feeds → Scout; step 11 + RULE 10 collapse platform-nuanced `delivered` → uniform committed+on-origin; KEY DESIGN FILES / CANONICAL-SOURCE rows drop "platform-nuanced"/"scoped-push". **KEEP git-protocol 16a-16f intra-machine half.**
- **`SIGNAL_PROCESSING_CHECKLIST.md`** — Phase 3.5 collapse to uniform delivered (keep precedence→push: FLASH still Telegram-pings); Quick L414 per 0d; bump version + sweep STATE §1.
- **`REGISTRY.tsv`** — Platform per 0e (PROME `OC+CC`→CC, YEYOU per 0b, all uniform CC, or drop in lockstep with doctor).
- **`delivery_log.tsv`** — per 0f (keep-as-constant = stamp `CLAUDE_CODE` forward, never rewrite the 42 OPENCLAW rows).
- **`STATE.md`** — append version-history mirrors, drop "runnable by PROME on the VPS"/"platform-nuanced", §1 pointers in lockstep with the spec bumps.
- Run `version_drift_check.py` + `walter_doctor.py` to confirm no regression; fix `BRENT_LIAISON_PREP.md` L13 (`Platform: OC`→CC), `DEEP_RESEARCH_FLAG_PROPOSAL.md` L100/172 (Quick framing); retire the LAST_COMPLETION `§3.4 scoped-push runbook` open item.

## Phase 4 — PROME two-surface collapse (after 0a; PROME owns these — route to a PROME pass)
- `PROME/CLAUDE.md` — collapse "One Prome, two work surfaces" → one CC Prome; remove the "Telegram/OpenClaw Prome" counterpart + defer-to-it clauses (L18/53/59); reconcile commit/push with autopush.
- `PROME/CLAUDE_CODE_PROME.md` — retire (fold principles into `PROME/CLAUDE.md`) or rewrite; if retired, fix the `BOOT.md` L95 + `SYSTEM.md` L96-100 pointers in the **same commit** or boot breaks.
- `PROME/SYSTEM.md` — collapse the "Prome Runtime Split" (L44-104) → one CC Prome (HANDOFF/SCRATCH become plain session continuity).
- **Retire the Prome-to-Prome mailbox** `PROME/COMM_PLAN.md` + `PROME/COMM/` (TO_OPENCLAW/TO_CLAUDE_CODE/ACKS/PROTOCOL — it only bridges two Prome surfaces).
- Close stale design items: `ORCHESTRAL_LAYER_DESIGN` L219, `ACTIVE_DECISIONS` L41 (separate-clones → **SUPERSEDED**, it contradicts this direction) / L36 / L43, `STATUS` L12; scrub `MEMORY_DRAFT_2026-05-17` "two surfaces" before any merge.

## Phase 5 — Autopush canonical flip (route THROUGH the existing `PROME/AUTOPUSH_MIGRATION_PLAN`)
The OpenClaw cut confirms single-machine **permanent**, which unblocks the already-greenlit, mid-soak autopush migration. Do NOT run these independently — sequence via the plan's Tier 1→2→3 (20+ files) to avoid double-edits.
- Update `AUTOPUSH_MIGRATION_PLAN.md` (single-machine = permanent; resolve its Decision C/YEYOU per 0b).
- `PROME/GIT_COORDINATION.md` (Tier 1.2) — drop "OpenClaw/" → "concurrent CC sessions"; Will-flush-lease → auto-push-at-closeout via safe-push.sh. KEEP pathspec/ownership hard rules.
- Root `CLAUDE.md` Git Protocol (Tier 1.1) — "Do NOT push by default" → auto-push-at-closeout (ff-gated). KEEP the entire "Before pulling"/"Never" intra-machine half.
- `PROME/BOOT.md` + `CLOSEOUT.md` + the two auto-memories (`finding_push_train_pattern`, `feedback_defer_push_coordinate`) + Tier-3 17-agent CLAUDE.md push lines — via the plan. **KEEP the "second machine pushed → ABORT" ff tripwire** (cheap insurance).
- **Also (critic):** `docs/GIT_PROTOCOL.md` — reconcile "Prome does not auto-commit", drop the RETIRED `git add AGENTS/<AGENT>/` broad pattern (contradicts the pathspec auto-memory), drop the "Persistent (Telegram) vs (Claude Code)" agent table. KEEP its "don't touch another agent's files" intra-machine guidance.

## Phase 6 — YEYOU execution (after 0b + branch landing)
- **If CUT:** `git mv AGENTS/YEYOU/` to archive, remove its REGISTRY row, retire `YEYOU_PROME_COORDINATION.md` + the `GIT_COORDINATION` YEYOU sections/Landing Rail.
- **If KEPT:** rewrite runtime → CC (drop "on the VM/always-on/24-7 Sentinel" — a CC YEYOU is a behavior change, not a lift-and-shift), keep "Reports to PROME", collapse its branch/merge protocol into standard intra-machine pathspec+defer-push.

## Phase 7 — Always-on feeds: promote Scout, retire VPS cron + SENTRY
- Promote `SCOUT_BUILD_PLAN.md` PLAN → BUILD (VPS cut removes the last reason to defer); verify the §2 Will-prereqs (rotated token, `SCOUT_BOT_TOKEN`/`SCOUT_CHAT_ID` Secrets, group chat_id).
- Build the Scout GitHub Action (runs `sweep.py` + `poll_edgar.py` **after** their `config.py` WORKSPACE is repointed — Phase 1; posts a Telegram digest, never commits). Repoint WALTER step-7c + `walter_doctor` cron_liveness → Scout digest.
- Retire `cron_sweep.sh` (dead, token rotated); `feeds.yml` (SENTRY) DELETE vs leave-INERT (SCOUT §6 = inert); kill SENTRY "Vision-via-Prome" ROADMAP items; reconcile DEWEY `REVIVAL_PLAN` Scout-track.

## Phase 8 — Root/infra docs sweep (OpenClaw-saturated playbooks; dedup with Phase 2)
- `docs/BUILD_AGENT.md` — RETIRE/rewrite to CC reality (build an agent = create `AGENTS/<NAME>/` + a REGISTRY row; no `openclaw.json`/`~/.openclaw`/`openclaw agents add`/hermes). Every command currently fails on the desktop.
- `docs/ARCHITECTURE.md` (describes the abandoned OpenClaw-instance conversion — the OPPOSITE of this) → replace with a short single-machine note. `docs/OPERATIONS.md` L305-308 `~/.openclaw` agent-add → CC scaffold; KEEP `systemctl --user` dashboard lines.
- `AGENTS_DIRECTORY.md` + `AGENTS.md` + `AGENTS/_INDEX.md` — drop the OpenClaw VPS row + "CC Prome vs OpenClaw Prome".
- **Critic adds:** `docs/AUTO_MEMORY.md` ("Working with two machines" L101-114 + cross-machine conflict L223); `LESSONS.md` (#1 forbids stopping the gateway, #11 OpenClaw push-notif limits) — **update as part of Phase 9**; root `MEMORY.md` L45-46 ("Real Agent-Work Surface Is CC… VPS/OpenClaw is Prome's orchestration"); `TOOLS.md` L6 ("built-in OpenClaw tools"); root `CLAUDE.md` L96 stale `systemctl --user status dashboard` pointer (that unit does NOT exist — dashboard runs via server.py). **SAM doc family** (`STATUS.md`, `MAINTENANCE.md`, `MOF_INTERVENTION_PLAYBOOK.md`, `scripts/AUTOMATION_PLAN.md`) + **archive the contradicting `AGENTS/SAM/proposals/2026-06-04_separate_clones_*` docs**; `WILL/API_KEY_MIGRATION.md` (obsolete `~/.openclaw` cutover); per-agent platform lines (TERRY L5); decide the redundant `AGENTS/CARL/scripts/safe-push.sh`; update `memory/auto/project_phone_signal_architecture.md` + `project_openclaw_prome_degraded.md`.

## Phase 9 — Runtime decommission (THE cut — gated LAST, after Telegram re-home verified)
1. (Prereq) Phase 0c Telegram decision resolved + a CC-native Telegram poller stood up and **verified serving Will.**
2. `systemctl --user disable --now clawdbot-gateway.service`; remove the unit + `default.target.wants/` symlink. **Scope to ONLY this unit** — do NOT sweep `liquid-hy-watch.service`/`.timer` (LIQUID's HY-OAS watcher, not OpenClaw).
3. `git mv config/openclaw-multiagent.json5` to archive; invalidate `CLAWDBOT_GATEWAY_TOKEN`.
4. Update `LESSONS.md` #1/#11 (the gateway is intentionally gone) so the doc no longer contradicts reality.

---

## What WALTER can do now (no decision needed)
1. **Draft `BOARD_CONSUMPTION_SPEC` v0.6** platform-collapse with decision-placeholders for the 0f/0g slots (WALTER owns this canonical spec).
2. Drop the decision-independent VPS framing: WALTER `CLAUDE.md` step-0.5 "runs on the VPS" clause + `STATE.md` L63 "runnable by PROME on the VPS" (keep portable-python fallback).
3. Fix `BRENT_LIAISON_PREP.md` L13 `Platform: OC`→CC; annotate the PROMPT8 research artifact "two platforms" as superseded.
4. **One-page recommended-defaults memo** for Will to ratify fast: 0e keep-uniform-CC · 0f keep-as-constant `CLAUDE_CODE` · 0g WALTER-self-on-clean-tree via safe-push.
5. Baseline `walter_doctor` + `version_drift_check` before any edit (prove no regression after).
6. Correct WALTER's own carry-forward at closeout (stop describing PROME/YEYOU "on the VM"; retire the `§3.4 scoped-push runbook` parked item).

## Needs coordination (not WALTER-unilateral)
- Root `CLAUDE.md` (ROOT, auto-injected fleet-wide) — Will/root-owner; lockstep with Phases 2-WALTER + 4-PROME.
- `BOARD_CONSUMPTION_SPEC.md` — possible parallel-WALTER ownership; coordinate before editing.
- All PROME docs (Phase 4/5) — PROME owns; gated on 0a.
- The autopush flip — route through `PROME/AUTOPUSH_MIGRATION_PLAN` Tier 1→2→3.
- Telegram token (0c) — spans WALTER `.claude/settings.json` + PROME.
- `docs/` + roster docs (Phase 8) — INFRA/ROOT, likely another owner; dedup with Phase 2.
- Owner-scoped: DOC (9 dead paths, HIGH), SAM (heavy OpenClaw doc family + contradicting proposals), TERRY, CARL, SENTRY, DEWEY, the 12 consume-block agents (verify-NOT-delete).

## Rollback / regression risks (top)
- **Over-trim** (the intra-machine guards + consume lane) — #1 hazard.
- Platform-column drop without the lockstep `walter_doctor` edit → ValueError → silent stale fallback set.
- Spec bump without sweeping `STATE.md` §1 → version-drift HIGH at closeout.
- Half-editing the Quick construct → dangling refs across 4+ files (rule once, sweep all).
- Disabling the gateway before the CC Telegram poller is verified → **Will-contact blackout.**
- Rewriting append-only history (delivery_log OPENCLAW rows) → corrupts the audit.
- Token NOT rotated (deleting the file ≠ un-compromising it).

---

*Scoping artifact — supersedes the LAST_COMPLETION "OpenClaw cutover" placeholder. When execution starts, this becomes the running checklist; check off per phase. Source: workflow `wm0048wmx` (115 touchpoints, 4 discovery + synth + critic).*
