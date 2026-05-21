# SCRATCH.md — Ephemeral Session State
**Last Updated:** 2026-05-21 ~17:00 ET (end-of-day Standard closeout, second of the day)

## What Just Happened

Today ran in two CC-Prome sessions.

**Morning + early afternoon (10:54-14:30 ET) — first session:** Heaviest single-session coordination day to date. Boot from cleared context; absorbed BROCK + REGINALD live closeouts in parallel; revived HENRY + VIOLET via teams mode + LIAISON channel; shipped FRED publication-lag fix Phases 1-3; ran BOND for 1pm Treasury auction; caught TIPS-vs-nominal correction + cross-flagged to BROCK + HENRY; closed out at commit `d2231c3c`.

**Late afternoon (15:35-17:00 ET) — second session:** Will respawned CC-Prome to handle OpenClaw COMM mailbox inbound. Stretched into focused staleness audit of auto-injected / boot-read state files. 6 commits this stretch:

- `28dd3e13` COMM mailbox boot integration + first two ACKs
- `8f3fa922` HEARTBEAT.md Path B refresh (98→38 lines, Will-authorized cross-surface boundary write)
- `d60616cc` MEMORY.md focused sweep (Will-authorized; 2 new entries + 3 footnotes)
- `a0aa4232` HEARTBEAT surgical fix + FORGE rehab handoff
- `00fe9247` Standard closeout (STATUS surgical + daily log addendum)
- this commit pending — closeout finalization (SCRATCH rewrite + HANDOFF surgical + 2 new auto-memory entries + 1 existing memory updated)

Full session narrative lives in `memory/2026-05-21.md` + `PROME/CLAUDE_CODE_HANDOFF.md`. This file is the next-session entry point, not the audit trail.

## Current Git State

Clean of PROME-scoped work — everything committed and pushed. Working tree contains only:
- Foreign uncommitted: `AGENTS/RED/` (active session), `AGENTS/WALTER/MEMORY.md`, `AGENTS/BRENT/inbox/` (RED→BRENT signal)
- `WILL/share/` image (Will's)

Behavior-language summary: clean, synced to origin, foreign agent work left untouched per protocol.

## Next Planned Work

**🔴 Top priority for next session: FORGE rehab.**

Surfaced via SAM's outbox-to-PROME signal (`AGENTS/SAM/outbox/2026-05-21_to-PROME_sam-position-state-for-forge-rehab.md`). FORGE is significantly worse than HEARTBEAT / MEMORY / TODAY were:
- `FORGE/STATUS.md` last touched Mar 25 (~2 months)
- `FORGE/PORTFOLIO.md` Feb 19 (~3 months)
- `FORGE/JOURNAL.md` Feb 27
- Per-trade folders (KRE, OZK, WAL) Mar 17
- FXY shown as "4 shares @ $59.77" — actual is 13 shares + 1 Jun-18 $58C
- Six expired options still listed as active: USO Mar 27, OWL Apr 2, APO Apr 17, SOFI May 1, OZK May 15, TLT May 15
- "Immediate Actions" all past deadline

Scope question for Will at next-session start: full rehab (STATUS + PORTFOLIO + JOURNAL + per-trade folders, reconciliation against SAM/BROCK/RED position state) vs incremental (fix FXY + flag expired options first; deeper work later). 6/18 Jun expiry cluster is 28 days out — bounded urgency, not crisis-urgency.

**Live Will-decision carries:**
- SAM Sep-18 $60C × 5-10 contracts — pending post-CPI cheaper entry window
- TODAY.md Path B refresh — drafted but not shipped; all inputs ready (live data, catalysts from CALENDAR, SAM correction)
- CALENDAR.md refresh — 3/27 stale; queued after TODAY.md
- HEARTBEAT refresh-cadence design question — self-referenced inside HEARTBEAT as a "Blocking on Will" item
- PROME execution-rails design note — BROCK LESSONS #16; especially relevant to 6/18 expiry cluster
- OZK STATUS hygiene refresh — low priority

## Cautions for Next Session

- **🔴 Outbox scanning at boot is now an enforcement gap.** Saved as auto-memory `feedback_scan_agent_outboxes_at_boot.md`. Until BOOT.md is updated with the explicit scan step, agent-to-PROME signals routed via own-outbox (Convention B — SAM's pattern) will keep arriving late. Boot procedure should `git log --since="3 days ago" --diff-filter=A --name-only -- 'AGENTS/*/outbox/*'` and filter for `*to-PROME*` patterns.

- **Structural staleness inheritance is real.** The "Verify state before propagating" rule was violated TWICE in today's late-session stretch — first for HEARTBEAT (propagated "owed" claim across multiple sessions without opening the file), then for SAM Tranche 2 (wrote HEARTBEAT row from inherited PROME state without checking SAM's morning commits). Auto-memory entry updated with structural-vs-behavioral framing: mental discipline alone doesn't fix the failure mode; boot-time automated cross-verification is the structural fix.

- **HEARTBEAT + MEMORY now refreshed and current.** Auto-injected files reflect 5/21 ~16:25 state on OpenClaw's next boot. FORGE rehab is visible as top blocking item.

- **OpenClaw's HANDOFF.md got a surgical update this closeout** to flag the cross-surface state shift. He'll see refreshed HEARTBEAT auto-inject + the new COMM channel with two ACKs from CC + FORGE blocking item.

- **Cross-surface validation pattern just got its first concrete instance** (TIPS-vs-nominal catch by both surfaces independently). Saved as auto-memory `finding_cross_surface_validation_pattern.md`.

- **No persistent-agent spawns at boot.** Do not spawn: CARL, REGINALD, OZK, SAM, RED, BRENT, Claude Code Prome. HENRY/VIOLET/BOND were teams-mode standing-by during the morning session but released to closeout.

- **TODAY.md remains 4 days stale.** Path B draft is in conversation history. Skip rule in CLOSEOUT.md says "usually skip" — fine for now since HEARTBEAT now explicitly flags TODAY.md staleness in its Pointers section.

- **CALENDAR.md is itself 3/27 stale** but contains the load-bearing upcoming catalysts: 5/25 Memorial Day, 6/16-17 FOMC + SEP + dot plot, 6/18 Jun expiry cluster (WAL/KRE/HYG/APO/AAL/ARES/EGBN/CF — the cluster that BROCK LESSONS #16 references for execution-rails gap).
