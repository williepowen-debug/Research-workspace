# PROME SPINE & WILL-FACING SURFACES SWEEP (judgment tail)

**Registered:** 2026-07-28 (T3-a of the PROME architecture program — audit §7b; Will green-light relayed via PROME's disposition packet ~17:20 ET) · **Cadence:** every 21d (`REGISTRY.tsv` is canonical — this doc doesn't restate it) · **Posture:** READ-ONLY, always. PROME is presumed LIVE; findings route as inbox packets, never edits.

## Why this exists

PROME is the fleet's only agent with no reader above it, and its Will-facing outputs fail SILENT-BLANK — invisible from inside (the publisher can't see its own blank panels). The founding audit (run #0, 2026-07-28) found a 4-day-degraded Will-facing artifact on the first-ever external read. This sweep makes the outside reader structural. It is also the third leg of PROME's own L5 gate (FLEET_MAP row).

## Scope — the JUDGMENT tail (what a script cannot do)

**PROME's ruling at green-light (do not re-absorb the mechanical core here):** scriptable checks must not wait 21d for an external reader — dashboard_state emptiness/vintage, GATES/DOCKET token-vocabulary, last_checked ages, and overdue-unresolved rows all belong to `prome_gate.py` at EVERY BOOT (second wave, 8/6-8/9).

This sweep keeps:
1. **Content-level silent-blank on Will-facing surfaces** — fetch/read the live dashboard artifact + HEARTBEAT: does each section still SAY something, and is what it says consistent with the rails? (A nonempty panel carrying a stale or self-contradictory read passes every mechanical check.)
2. **Does-the-surface-still-mean-what-canon-means** — walk SYSTEM.md's Mirror Map: for each row, does the mirror still agree with its owner surface in MEANING, not just token-match? Check PROME's always-loaded CLAUDE.md ¶s against root canon ratifications since last run.
3. **Spine skim** — BOOT/CLOSEOUT/COMPLETION_SPEC/AUTONOMY/HANDOFF (deliberately including `spine_audit.workflow.js`'s blind spots until its GROUPS extension lands): stamp honesty, steps-vs-execution drift, own-rule-unexecuted instances.
4. **Format-consumer check on any HEARTBEAT/BOARD re-base since last run** (PAT-069) — if a parsed surface was re-based, verify its named consumers re-ran clean.
5. **Disposition write-back spot-check** (PAT-032 class) — sample proposals/packets closed since last run for missing terminal banners.

**Bridge clause: CLOSED 2026-07-28, same day it was written** — `prome_gate.py` shipped that night (Will pulled the schedule in) and DAEDALUS verified in-file that the gate carries all four mechanical families (dashboard-state emptiness/vintage · GATES token-vocabulary/fired/ages · DOCKET overdue · symmetry diff; BOOT:55 + CLOSEOUT:42 wiring). Scope is FINAL at judgment-tail-only from run #1 onward.

## Method

Light Mode-A: 1-2 readers max (spine skim + Will-facing content read) or inline if the diff since last run is small — `git log --oneline --since=<last_run> -- PROME/` first to size it. Findings packet → `PROME/inbox/`, urgent-first format (the run-#0 packet is the template). Update REGISTRY row (`last_run` + `last_findings`) + Run Log below. L5-gate note: a run with ZERO unexecuted-own-rule findings satisfies the third leg of PROME's L5 gate — say so explicitly in the packet when it happens.

## Run Log

| # | Date | Form | Findings |
|---|---|---|---|
| 0 | 2026-07-28 | Founding 4-reader audit (Will-directed, pre-registration) | 5 wrong-now (all fixed <4h) + 5 structural + housekeeping; verdict well-built-but-lagging. `upgrades/PROME_AUDIT_2026-07-28.md` |
| 1 | 2026-08-16 | 2-reader Mode-A (Will-directed 2d early; 478-commit window sized first — inline form ruled out) | 3 URGENT (dashboard one-liner INVERTED to a kill-on-sight claim, live 3d/6 builds · will_brief dead 12-13d w/ superseded directives, Will-gate rewire-vs-retire · fleet grid all-ok vs agent_freshness 8×STALE>7d) + 9 STANDARD + 7 TRIVIA. **L5 leg NOT satisfied: own-rule-unexecuted = 4** (CLOSEOUT stamp · AUTONOMY FORGE-grant log+mirror · DOCKET row-35 write-back · WILL_QUEUE registration ×2); legs 1-2 banked, re-test run #2 ~9/6. Strong side verified: 4/4 closeouts step-for-step, 8/9 dispositions CLEAN, fire-ledger exact. PAT-105 born (guards certify nonemptiness, not truth — every live failure was nonempty) + PAT-069 n+2 (both HEARTBEAT re-bases unchecked at consumers). Evidence: `upgrades/PROME_SWEEP_RUN1_2026-08-16_READER_REPORTS.md`; packet in PROME/inbox same name. |
