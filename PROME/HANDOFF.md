# PROME HANDOFF
**Date:** 2026-05-16 21:23 ET
**Status:** ✅ Clear-ready, but repo has fresh post-push news-sweep dirt. Do not pull/rebase/stash/reset until the dirty batch is reviewed.

---

## What Just Happened

Will asked to preserve local Prome work without losing Claude Code agents' remote git updates.

Completed safely:
- Committed the remaining dirty work in small chunks.
- Fetched remote and rebased Prome work on top of remote agent commits.
- Verified dry-run push was fast-forward after handling a late SENTRY remote update.
- Pushed successfully to `origin/master`.

Published commits now on remote, newest first:
1. `da7242c2` — `PROME: refresh heartbeat May 16 evening`
2. `f83bd66c` — `PROME: add synthesis intel packets`
3. `c120fa1f` — `PROME: refresh heartbeat May 16`
4. `150a3ffc` — `PROME: clarify chief-of-staff operating model`
5. `f95b16a3` — `PROME: route May 14 signal batch`
6. `dfcb1983` — `BOND: refresh market-structure monitors and trade read`
7. `992fa4b7` — `PROME: refresh state after FSK Q1 read`
8. `61c6a966` — `PROME: add Claude Code runtime scaffold`

Important: after push, a fresh automated/news-sweep update appeared locally. It was **not included in the push**.

---

## Current Git State

As of the last check, branch was synced with remote at:
- `HEAD = origin/master = da7242c2`

But the working tree is dirty from the latest sweep/heartbeat refresh:

Modified:
- `FORGE/tools/news-sweep/.cache/seen.json`
- `FORGE/tools/news-sweep/latest.json`
- `FORGE/tools/news-sweep/latest.md`
- `HEARTBEAT.md`

Untracked sweep inbox files:
- `AGENTS/BROCK/inbox/sweep_2026-05-16_2306.md`
- `AGENTS/CARL/inbox/sweep_2026-05-16_2306.md`
- `AGENTS/HENRY/inbox/sweep_2026-05-16_2306.md`
- `AGENTS/LABOR/inbox/sweep_2026-05-16_2306.md`
- `AGENTS/LIQUID/inbox/sweep_2026-05-16_2306.md`
- `AGENTS/OTTO/inbox/sweep_2026-05-16_2306.md`
- `AGENTS/REGINALD/inbox/sweep_2026-05-16_2306.md`
- `AGENTS/SAM/inbox/sweep_2026-05-16_2306.md`

Recommended next git step:
1. `git status -sb`
2. Inspect exact diff for the sweep batch.
3. Check remote overlap before committing agent inbox files: `git fetch --prune` then `git log HEAD..origin/master -- <paths>`.
4. If safe, commit as one batch: `PROME: route May 16 news sweep` or similar.
5. Do **not** stash/reset/pull/rebase while dirty unless Will explicitly approves.

---

## Current Market / Thesis State

Latest `HEARTBEAT.md` says **Updated: 2026-05-16 19:06 ET**.

Core read:
- Private-credit thesis has re-accelerated from grind to **BDC credit/mark stress confirmed**, led by FSK Q1.
- Public-credit contagion remains **unconfirmed**: HY OAS **276bps** and VIX **18.43** remain benign.
- Stress is concentrated in physical/Japan/BDC/bank channels:
  - Brent **$109.26 🔴**
  - Gas **$4.50 🔴**
  - USD/JPY **158.73 🔴**
  - BIZD **$12.61 🔴**
  - KRE **$66.97 🟡**
  - WAL **$74.42 🟡 / below bear line**
  - APO **$135.38**, above `$130` watch line.

May 16 updates:
- 19:06 ET dashboard was unchanged from 18:09.
- News sweep routed internally: **12 alert-level items + 1 WATCH_FOR hit** to REGINALD/LIQUID/BROCK/HENRY/SAM/CARL/OTTO/LABOR inboxes.
- No user interruption was required unless Monday prep needs escalation.

---

## Position / Decision Rails

Pending decisions remain:
- 🔴 **APO puts — hold/roll/cut**: reassess if APO remains >$130 or HY OAS drifts toward <260 thesis-kill zone.
- 🔴 **FSK / BDC downside**: Strong Bear FSK Q1 allows fresh BDC/private-credit downside discussion, but needs live bid/ask and Will approval.
- 🟠 **ARES Jun $95P**: only hold through BDC wave if GCRED/OTF/BDC marks keep confirming; otherwise theta dominates.
- 🔴 **KRE/WAL/OZK bank shorts**: regional-bank Call Report triage is still the next decision-support task.

No trades executed. No external/public messages sent.

---

## Claude Code Prome State

Claude Code Prome integration is no longer just planning; the scaffold/runtime docs were committed and pushed.

Relevant files:
- `PROME/CLAUDE.md`
- `PROME/CLAUDE_CODE_PROME.md`
- `PROME/CLAUDE_CODE_PROME_PLAN.md`
- `PROME/CLAUDE_CODE_PROME_TASKS.md`
- `PROME/CLAUDE_CODE_HANDOFF.md`
- `PROME/SYSTEM.md`
- `AGENTS/PROME/CLAUDE.md`
- root `CLAUDE.md`

Next suggested Claude Code step remains a low-risk dry run / readiness report before granting autonomous commit/push behavior.

---

## Highest-Value Next Actions for Fresh Session

1. **Run boot sequence from `PROME/BOOT.md`.**
2. **Handle dirty news-sweep batch carefully** before any pull/rebase:
   - inspect diffs,
   - check remote overlap,
   - commit only if safe and Will approves / context supports it.
3. **Refresh live dashboard before citing any market level.**
   - `python3 FORGE/tools/market-data/dashboard.py --compact`
4. **Regional-bank Call Report triage** using `PROME/action-cards/REGIONAL_BANK_WEEKEND_TRIAGE_MAY9.md`.
5. **Monday decision prep** for APO/ARES/BDC and WAL/KRE/OZK.
6. **If working Claude Code Prome**, read the Claude Code Prome plan/tasks and keep first dry run non-mutating except for its handoff report.

---

## Rules / Constraints

- No trade execution without Will approval.
- No external/public messages without approval.
- Do not spawn persistent/managed agents: **CARL, REGINALD, SAM, RED, BRENT**.
- WALTER owns signal/news routing; Prome owns tasking, rails, and synthesis.
- Do not commit/stash/pull/rebase/reset dirty git state without deliberate review and Will approval.
- Use explicit path staging only; no broad `git add .`.
- Remote agent work must not be overwritten.

---

## Suggested Fresh-Session Prompt

> Continue from `PROME/HANDOFF.md`. Run `PROME/BOOT.md`, but do not pull/rebase while dirty. First inspect the post-push news-sweep/heartbeat dirty batch from May 16 23:06Z, check remote overlap, and prepare a safe commit if appropriate. Current market model: BDC/private-credit stress confirmed by FSK, but broad public-credit/vol contagion unconfirmed because HY OAS/VIX remain benign. Stress is concentrated in Brent/gas, USDJPY, BIZD, WAL/KRE. Prioritize repo hygiene, then Monday decision prep for APO/ARES/BDC and regional banks. Do not trade or send external messages without Will approval.
