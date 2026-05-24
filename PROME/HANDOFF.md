# PROME HANDOFF
**Date:** 2026-05-17 10:45 ET
**Status:** ✅ Fresh after GitHub pull; local Prome/OpenClaw state refreshed from REGINALD + WALTER commits.

---

## What Just Happened

Will said the Claude Code agents' updates were likely committed/pushed and asked Prome to pull/check.

Completed:
- Ran `git pull --rebase` safely.
- Pull fast-forwarded cleanly from `544faaf5` to `270b6d1d`.
- Local `master` now matches `origin/master`.
- No conflicts; working tree was clean after pull.
- New pulled work included REGINALD WAL Investor Day closeout and WALTER multi-session closeout.
- Ran dashboard May 17 10:38 ET before refreshing state; levels unchanged from May 16 evening.
- Refreshed Prome local state files so future sessions no longer inherit stale dirty-tree warnings from May 16.

---

## Current Git State

- Branch: `master`
- HEAD: `8a44dbe2` / `origin/master`
- Pull result: fast-forward, clean
- Local state refresh may create a new Prome-only diff after this handoff.

If committing this refresh:
- Stage explicit files only (`PROME/SCRATCH.md PROME/TODAY.md PROME/STATUS.md PROME/HANDOFF.md PROME/CLAUDE_CODE_HANDOFF.md PROME/SYSTEM.md` and any explicitly edited root file).
- Do **not** use `git add .` or `git add -A`.

---

## Current Market / Thesis State

Dashboard recheck May 17 10:38 ET:
- HY OAS **276bps 🟢**; VIX **18.43 🟢** — broad cascade still unconfirmed.
- CCC OAS **922bps 🟡**.
- Brent **$109.26 🔴**, gas **$4.50 🔴**.
- USD/JPY **158.73 🔴**.
- KRE **$66.97 🟡**, WAL **$74.42 🟡 / below bear line**.
- APO **$135.38**, above `$130` watch.
- BIZD **$12.61 🔴**.
- Claims: initial **211k**, continuing **1.782M**, shadow-adjusted estimate **266k** — directionally softer, not labor-break confirmation.

Core read:
- FSK validates BDC/private-credit stress.
- Public-credit/vol contagion has not confirmed.
- Energy/Japan/BDC/regional-bank channels remain live pressure points.

---

## New Pulled Intelligence to Incorporate

### REGINALD May 17 closeout
- WAL Investor Day findings shipped.
- Bucket E B3 fired: management held 25-35bps NCO guide despite Q1 ex-fraud 39bps.
- REG-25 moved **55% → 65%+**; bear-slow **23% → 27%**; no V2.2 promotion yet.
- WAL 10-Q filed 5/11 but not integrated; Schedule O / Table 16 cross-credit inventory test pending.
- MI3 / FFIEC PDD mid-May update window passed; status check pending.
- SSB $95P May 15 execution ladder written; outcome pending Will confirmation.

### WALTER May 17 closeout
- WALTER confirms Prome chief-of-staff model and root-level signal-routing split:
  - WALTER owns signal/news routing.
  - Prome owns tasking, rails, and Will-facing synthesis.
- BOARD count now 213.
- May 18 callbacks:
  - Iran-war anchor re-verify boundary.
  - TIC March release / Japan UST-flow watch.
- WALTER flags HENRY/LIQUID/NEXUS/BROCK staleness and pending routing-pressure items.

---

## Position / Decision Rails

Pending decisions remain:
- 🔴 **APO puts — hold/roll/cut**: APO is above `$130`; reassess with live option chain before any roll/cut/add.
- 🔴 **FSK / BDC downside**: Fresh downside discussion allowed; needs live bid/ask and Will approval.
- 🟠 **ARES Jun $95P**: hold only if BDC wave continues confirming; theta risk rising.
- 🔴 **KRE/WAL/OZK/ZION/SSB bank cleanup**: use REGINALD May 17 as latest bank-state input; Call Report/MI3 checks are now due.

No trades executed. No external/public messages sent.

---

## Claude Code Prome State

Claude Code Prome scaffold/runtime docs exist and are committed. Phase 2 architecture integration is complete. Phase 3 dry run remains pending.

First dry run should remain low-risk:
- Read the Claude Code Prome docs.
- Inspect git status and Prome state.
- Do not edit anything except `PROME/CLAUDE_CODE_HANDOFF.md`.
- Produce readiness / repo-hygiene report.
- Do not commit, stash, reset, or message externally.

---


## CC-Prome Cross-Surface Update — 2026-05-21 (for OpenClaw next-boot orientation)

CC-Prome ran a Will-authorized cross-surface refresh pass during 5/21 PM. OpenClaw's next-boot context will land in materially changed shared state. Brief reorientation:

- **`HEARTBEAT.md` is refreshed and trimmed.** Path B treatment: 98→38 lines per its SYSTEM.md "pointer-shape" design role. Auto-injects fresh on next boot. New stress-dashboard line + thresholds table (added 10Y + TLT rows + tightened VIX green band to <15) + new "Blocking on Will" 4-row table with FORGE rehab as the top 🔴 item. Commits: `8f3fa922` (Path B) + `a0aa4232` (surgical fix). Refresh-cadence question (who writes / how often) is now self-referentially listed inside HEARTBEAT as a blocking item — design discussion happened in CC session.

- **`MEMORY.md` (root) is refreshed.** Additive sweep only — 2 new SYSTEM ARCHITECTURE entries (Execution-Rails Are Part of the Framework; Stamp content as well as metadata) + 3 footnotes on still-valid framework entries that aged into testable / contradicted states (Timing Thesis, Hamilton Framework, PC Contagion Mechanics). Commit `d60616cc`. Will-authorized cross-surface boundary.

- **`PROME/COMM/` mailbox is live and integrated.** Will-routable channel between OpenClaw and CC-Prome. First two TO_CLAUDE_CODE messages already ACKed in `PROME/COMM/ACKS/`. CC-Prome's BOOT.md updated to check the mailbox at step 7. OpenClaw should mirror that boot-step on his side (`PROME/HANDOFF.md` was previously the only Telegram-Prome continuity surface; COMM is now the targeted message channel). Templates: `PROME/COMM/TEMPLATE_MESSAGE.md` + `TEMPLATE_ACK.md`. Cold-boot guide: `PROME/COMM/README.md`.

- **🔴 FORGE rehab is the top blocking item.** SAM filed `AGENTS/SAM/outbox/2026-05-21_to-PROME_sam-position-state-for-forge-rehab.md` flagging: FORGE/STATUS Mar 25 (~2 months), PORTFOLIO Feb 19, JOURNAL Feb 27, per-trade folders Mar 17. FXY shown wrong (4 shares @ $59.77; actual 13 + 1 Jun-18 $58C). 6 expired options listed as active. Will plans to have PROME do the rehab. 6/18 expiry cluster is 28 days out — bounded urgency.

- **TIPS-vs-nominal correction landed.** Today's 1pm auction was the 9Y8M TIPS reopening (CUSIP 91282CPU9), not the nominal 10Y the BOND matrix Q4 conditional rule depended on. BOTH surfaces caught this independently — OpenClaw via FiscalData's `inflation_index_security` flag (filed as COMM message); CC via PDF inspection + CUSIP-family heuristic. First concrete instance of cross-surface validation; saved as auto-memory finding. Matrix Q4 deployment reschedules to next nominal 10Y reopening ~June 9-11 (CUSIP family `91282CQ*`).

- **Other shifts to fold mentally:** WAL REG-T-02 sustain BROKE today ($78.53 reclaimed $78 for first time since 5/11 fire); SAM Tranche 2 executed at $57.66 (13 shares + 1 Jun-18 $58C); WALTER bull-counter response landed (both Tier-2 with forced steelman "regime may LAST not BREAK"); WALTER IRAN_WAR refresh shifted Iran picture to "partial-thaw on diplomatic + tape side, full-pressure on enforcement side, kinetic theater shifted to land-against-infrastructure with 5/17 Barakah strike."

Full CC-Prome audit trail (today's 2 sessions, 10+ commits) in `PROME/CLAUDE_CODE_HANDOFF.md`. Session-state entry-point in `PROME/SCRATCH.md`. Daily narrative in `memory/2026-05-21.md`.

---

## Active Thread — May 17 evening

**Agent View install:** ✅ done on this machine and the laptop. Persistent dashboard / session manager now operational.

**New active experiment:** `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`. Discovered during the Agent View install that the teams feature maps more directly onto the architecture we've been building — chief-of-staff lead, named teammates, mailbox messaging, shared task lists. The frontier work from here is whether teams is a useful coordination layer for the fleet. A small bounded test is planned, likely later today.

This supersedes the earlier "install Agents View" next-priority. Agent View is part of the runtime now; the open question is the teams layer on top.

Last completed git checkpoint:
- `8a44dbe2 SENTRY: feed update 2026-05-17-2240`
- Local `master` matches `origin/master`.

Next session start:
1. Run `PROME/BOOT.md` sequence.
2. Confirm `git status --short` is clean and pull/rebase if safe.
3. If teams experiment is mid-flight, read `PROME/CLAUDE_CODE_HANDOFF.md` for the latest CC-Prome session record.
4. Keep changes scoped per the standing show-diff-then-approve commit policy.

## Highest-Value Next Actions

1. Commit/push this Prome/OpenClaw state refresh if Will wants it saved.
2. Build Monday regional-bank decision prompt: WAL/KRE/OZK/ZION/SSB, Call Report/MI3, live chain pricing.
3. Build BDC/private-credit decision prompt: APO/ARES/BIZD/ARCC options, FSK implications, fresh pricing.
4. May 18 watch: Iran re-verify + TIC/Japan flows.
5. Run Claude Code Prome Phase 3 dry run when Will is ready.

---

## Rules / Constraints

- No trade execution without Will approval.
- No external/public messages without approval.
- Do not spawn persistent/managed agents: **CARL, REGINALD, SAM, RED, BRENT**.
- WALTER owns signal/news routing; Prome owns tasking, rails, and synthesis.
- Use explicit path staging only; no broad `git add .`.
- Remote Claude Code agent work must not be overwritten.

---

## OpenClaw Session — 2026-05-22 HAWK armed-pause consolidation

**Relocated 2026-05-24:** This entry was originally written into `PROME/CLAUDE_CODE_HANDOFF.md` in error. Moved here (OpenClaw's continuity surface) during the 5/24 CC-Prome handoff archive pass.

**What landed:** HAWK was booted from stale state, audited in bounded phases, and consolidated into `AGENTS/HAWK/audits/HAWK_SYNTHESIS_2026-05-22.md`. Local frame: **armed pause / controlled grind**; C 57% / D 35% / B 8%.

**Files edited:** `AGENTS/HAWK/STATUS.md`, `AGENTS/HAWK/CALENDAR.md`, `AGENTS/HAWK/LAST_COMPLETION.md`, `AGENTS/HAWK/audits/*`, `AGENTS/HAWK/workbook/KB.tsv`, `AGENTS/HAWK/board_log.tsv`, HAWK processed inbox moves, and routing notes to BRENT / LIQUID / RED / NEXUS / ZHAO. Prome closeout updated `PROME/SCRATCH.md`, `PROME/STATUS.md`, `PROME/CLAUDE_CODE_HANDOFF.md` (in error — see relocation note above), and `memory/2026-05-22.md`.

**Decisions Will made:** proceed with HAWK boot; switch to stale-data audit; break work into phases; run Phase 1, Phase 2, Phase 3, inserted Phase 3.5 after Will flagged US aircraft staging in Israel, then Phase 4; stop research and consolidate; prepare for GitHub push but pull/rebase first.

**Decisions needed from Will:** explicit `git push` approval. (Subsequently approved + pushed as commit `888a5e9d`.)

**Risks / blockers:** HAWK Phase 5 maintenance remains deferred (2 duplicate KB IDs + 58 stale active/watch/confirmed rows). May 23 close requires re-check of Gulf/framework text; if none, HAWK STATUS/CALENDAR should mark hold expired without framework.

**Next suggested work:** Push if approved; then scan BROCK / REGINALD / HENRY replies for 6/18 trigger-set v0.2 by 2026-05-24 EOD.

**Rules held:** no trade execution, no external messages, no persistent-agent spawns except HAWK (spawnable), explicit path staging only, no GitHub push without explicit approval.
