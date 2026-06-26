# SCRATCH.md — Ephemeral Session State
**Last Updated:** 2026-06-26 ~13:00 ET (Claude Code Prome — full session: bank-put reshape proposal → STANDING RULE set → detection/action HARDENING cluster (P1/P2/P3, all verified) → arch peer-review + fix round → HEARTBEAT reconcile → closeout. Agents released. Commits local, push pending.)

## What happened this session (6/26)
1. **Bank-put reshape proposal built** → `PROME/proposals/2026-06-26_bank-put-reshape-roll.md`. Read off the verified thesis: book is dated for a 2026 event, thesis is 2027 → duration mismatch. (b) AOCI + (c) WAL the live paths; (a) regional trimmed. **SHELVED** as the ready "if HY breaks 280" card per the new standing rule — NOT executed.
2. **★ STANDING RULE set (Will 6/26):** fresh capital deploys ONLY on a fired trigger, never mechanical book-reshape; limited funds = preserve dry powder. Memory: `feedback_deploy_on_trigger_not_calendar`. **Max-loss = $500/card.**
3. **Detection/action HARDENING cluster** (LIQUID/SENTRY/TERRY, teams-mode, Prome-directed):
   - **P1 detection** — `config.py` retuned to thesis lines (HY 265/280, 10Y 4.40, wrapper series ARCC/FSK/OBDC, FXY dropped) + **LIVE systemd --user watch timer** `liquid-hy-watch` (Mon–Fri 13:00 ET, enabled+active, VERIFIED firing 278→amber). Closes the "HY 281 reads GREEN / nobody pulled FRED" blind spot.
   - **P2 action** — `AGENTS/TERRY/scripts/chain_fetch.py` (live chain CLI) + `TRADE_CARD_TEMPLATE_FIRE.md` + 2 pre-locked setups ($500 locked).
   - **P3 grading** — `AGENTS/TERRY/scripts/grade_print.py` + config (Jul-print grader, 3 mis-grade traps as hard guards).
4. **Arch peer-review** (3-way, `PROME/cluster/2026-06-26_arch_review_synthesis.md`) → **fix round**: LIQUID STATUS de-bloat (28→7KB) + watcher `--selftest` added (8 assertions PASS) + X1 dedupe to KILL_MEMO; TERRY added MEMORY.md + CLOSEOUT.md + honest live STATUS.
5. **HEARTBEAT reconciled** (Prome, shared file): HY 276→278 [6/25], cushions corrected (2bp from 280 / 18bp from kill), X1/kill def → canonical KILL_MEMO, auto-watch noted.

## Live regime (verified this session)
- **HY OAS 278 [6/25]** — grinding up 271→276→278, **2bp from the >280 X1-trigger** (closest yet; NOT fired). The new watch timer auto-catches a 280 cross between sessions → `AGENTS/LIQUID/alerts/`.
- 10Y ~4.39. Wrapper-decoupling half (BROCK) still unfired. Energy deflated. Banks green.

## Forward-watch / carry
- **The watch is now automated** — `liquid-hy-watch.timer` fires daily 13:00 ET; next-boot echoes any between-session cross. Don't re-build manual HY checks.
- Jul-print grading instrument is now LIVE tooling (`grade_print.py`) — use it on CFG/OZK Jul16 → monolines Jul21 GATE → EGBN Jul22 → WAL Jul30.
- Trade construction (b)/(c): pre-built card on the shelf; fires ONLY on HY>280 sustained (or WAL Jul-30 print). Max-loss $500/card. Needs live broker book at fire-time.
- 10Y 6/30 re-pull still scheduled (cloud routine `trig_01Ps7pv1WaupKwBG9mWds46T`).

## Pending push (Will-coordinated)
- This session: 5 earlier commits (`029957a3`..`c993b8a8`) + closeout batch (HEARTBEAT + LIQUID fixes + TERRY durable-layer + arch docs + SCRATCH/HANDOFF). **NOT pushed.**
- **WILL/trading-journal:** 3 journal deletions (Will intentional, old) + 2 book JPGs — left UNTOUCHED, Will's to commit on his push.

## Cautions
- Position/broker truth = Will/FORGE, not these files. `git add` own-dir paths only. config.py + HEARTBEAT = shared (Prome-coordinated). No push without Will window.
