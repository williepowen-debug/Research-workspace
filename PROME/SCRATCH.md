# SCRATCH.md — Ephemeral Session State
**Last Updated:** 2026-06-26 ~14:35 ET (Claude Code Prome — full session: reshape proposal → STANDING RULE → detection/action HARDENING cluster → arch peer-review → HEARTBEAT reconcile → closeout → boot de-bloat thread → **AUTO-PUSH MIGRATION (pilot live)**. **All PUSHED, synced 0/0.** Agents released.)

## ★ Auto-push pilot LIVE (Will 6/26) — behavior change for next Prome
- **Prome now AUTO-PUSHES at closeout** via `./scripts/safe-push.sh` (wired into `PROME/CLOSEOUT.md` Chunk 4). No more manual "push window" for Prome. The script is **ff-gated + fails safe**: a non-ff ABORT = a 2nd machine pushed → STOP, don't force, flag Will (tripwire that single-machine was violated).
- **Mid-pilot / soak:** canonical docs (root `CLAUDE.md`, `PROME/GIT_COORDINATION.md`) + the ~17 agent CLAUDE.md still read "Will-coordinated" — DELIBERATE divergence during soak. Don't "fix" them yet.
- **Plan + next steps:** `PROME/AUTOPUSH_MIGRATION_PLAN.md`. After a clean soak → Tier 1 canonical policy → remaining closeouts → lazy-sweep agent files. Decisions: single-desktop ✅, closeout-step, lazy-sweep, pilot-first.
- Precondition: single-desktop only. If you ever push from a 2nd machine, auto-push aborts safely → switch to per-agent branches.

## What happened this session (6/26)
1. **Bank-put reshape proposal** → `PROME/proposals/2026-06-26_bank-put-reshape-roll.md`. Book dated 2026 / thesis 2027 = duration mismatch; (b) AOCI + (c) WAL live, (a) regional trimmed. **SHELVED** as the ready "if HY 280" card per the standing rule — NOT executed.
2. **★ STANDING RULE (Will 6/26):** fresh capital deploys ONLY on a fired trigger, never mechanical book-reshape; limited funds = dry powder. Memory `feedback_deploy_on_trigger_not_calendar`. **Max-loss $500/card.**
3. **Detection/action HARDENING cluster** (LIQUID/SENTRY/TERRY, Prome-directed):
   - **Detection** — `config.py` retuned (HY 265/280, 10Y 4.40, wrapper series ARCC/FSK/OBDC, FXY dropped) + **LIVE `liquid-hy-watch` systemd timer** (Mon–Fri 13:00 ET, enabled+active, VERIFIED firing 278→amber → `AGENTS/LIQUID/alerts/`). Closes the "HY 281 reads GREEN / nobody pulled FRED" blind spot.
   - **Action/grading** — `AGENTS/TERRY/scripts/chain_fetch.py` (live chain CLI) + `TRADE_CARD_TEMPLATE_FIRE.md` (+2 setups, $500) + `grade_print.py` (Jul grader, 3 mis-grade traps as hard guards).
4. **Arch peer-review** (3-way, `PROME/cluster/2026-06-26_arch_review_synthesis.md`) → fix round: LIQUID STATUS 28→7KB + watcher `--selftest` (8 PASS) + X1 dedupe→KILL_MEMO; TERRY +MEMORY +CLOSEOUT + honest STATUS.
5. **HEARTBEAT reconciled**: HY 276→278 [6/25], cushions corrected, X1/kill→canonical KILL_MEMO, auto-watch noted.
6. **Boot de-bloat thread** — pruned `project_ozk_spinout_direction` (done) + condensed `project_automem_symlink_migration` (stable); **archived CC-Prome `PLAN`/`TASKS` off the boot path** → `PROME/archive/`; **SYSTEM.md surgical refresh** (de-date-pinned to behavior-language, CC-Prome→operational, stale May items cleared). **Boot-read weight ~117→95 KB (~18% lighter).**

## Live regime (verified this session)
- **HY OAS 278 [6/25]** — grinding 271→276→278, **2bp from the >280 X1-trigger** (closest yet; NOT fired). Timer auto-catches a 280 cross between sessions.
- 10Y ~4.39. Wrapper-decoupling half (BROCK) unfired. Energy deflated. Banks green.

## Forward-watch / carry
- **Watch is automated** — `liquid-hy-watch.timer` daily 13:00 ET; next-boot echoes any between-session cross. Boot should check `AGENTS/LIQUID/alerts/HY_OAS_ALERTS.log`. Don't rebuild manual HY checks.
- Jul-print grading is now LIVE tooling (`grade_print.py`) — CFG/OZK Jul16 → monolines Jul21 GATE → EGBN Jul22 → WAL Jul30.
- Trade construction (b)/(c): pre-built card shelved; fires ONLY on HY>280 sustained or WAL Jul-30. $500/card. Needs live broker book at fire-time.
- 10Y 6/30 re-pull scheduled (cloud routine `trig_01Ps7pv1WaupKwBG9mWds46T`).

## Repo state
- **All Prome work committed + auto-pushed, synced 0/0.** (Prome closeouts now self-push.)
- **Not Prome's, left untouched:** `AGENTS/WALTER/REGISTRY.tsv` modified-uncommitted (WALTER active 6/26 afternoon — WALTER's to commit); `WILL/trading-journal/` 3 journal deletions (Will intentional) + 2 book JPGs (Will's).

## Cautions
- Position/broker truth = Will/FORGE, not these files. Refresh dashboard/FRED before citing levels. `git add` own-dir paths only; config.py + HEARTBEAT = shared (Prome-coordinated). No push without Will window.
