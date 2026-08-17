# FLEET_DIRECTORY — Build Plan

> 🗄 **DATED AUDIT/WORK RECORD (last content 2026-07-22; bannered 2026-08-17, self-audit F5).** Findings were routed at write time; this doc is history, not a live queue. Closure state of individual findings lives with the owning agents.

> ✅ **EXECUTED** — `scripts/render_directory.py` + generated `FLEET_DIRECTORY.md` live since 7/10; regenerated at every FLEET_MAP change since. This plan is a dated build record.

**By:** DAEDALUS · **Date:** 2026-07-10 · **Trigger:** Will — "DAEDALUS needs a reliable map/directory of what agents exist + what they do, and what's missing."
**Goal:** ONE readable, reliable, drift-proof view answering per agent: *what is it · what does it do · is it active · what's it missing.* The charter Job #3 deliverable ("the one view Will can't make by hand"), currently split across ROSTER (exists/does, PROME's) + FLEET_MAP (missing, DAEDALUS's) and buried.

## Design principles
- **Rendered, never hand-maintained.** A generated `FLEET_DIRECTORY.md` with a `DO NOT EDIT — generated from ROSTER + FLEET_MAP` banner. Editing it by hand resurrects the PAT-006 drift the frozen MATURITY_MAP was frozen to kill.
- **One column, one owner (PAT-006).** "What it does" + "status" render FROM `PROME/ROSTER.md` (PROME owns who-exists). "Missing / next" renders FROM `FLEET_MAP.tsv` (DAEDALUS owns gaps). The directory JOINS; it duplicates nothing.
- **Fail loud (PAT-035/finding_fail_loud_on_incomplete_data).** If ROSTER's table format changes or an agent can't be matched, the script errors — never renders a silently-wrong or half-empty map.
- **Recurring, not one-off (PAT-041).** Regeneration wired into the Production Review so the artifact can't rot; a one-time render is one dropped rewrite from stale.

## Source contract (verified 2026-07-10)
- **ROSTER.md** — per-group markdown tables; `Domain` = col 2 always; **status derived from group** (ACTIVE→🟢 · TIER-2→🟡 spawn-as-needed · DORMANT→⚪ · RETIRED/ARCHIVE→⚫). Parser keys on group headers (`## ACTIVE`, `## TIER-2`, …).
- **FLEET_MAP.tsv** — join on Agent col 1; pull `Class`, `Level`, and the missing-one-liner. Dormant/unscanned agents (in ROSTER, absent from FLEET_MAP) → blank missing-cell, still listed.

## Steps (each = one commit; pause for review between)

### Step 1 — Parsers + join (plumbing; prove the join is complete)
`scripts/render_directory.py`: parse ROSTER group-tables → `{agent: (group, domain)}`; parse FLEET_MAP → `{agent: (class, level, gap1liner)}`; **join on agent, print a plain dump + a reconciliation report** (agents in ROSTER-only, FLEET_MAP-only, matched). Fail loud on: no group tables found, malformed row, unexpected FLEET_MAP-only agent. NO formatting yet — the deliverable is a verified-complete join. Commit.

### Step 2 — Render the grouped directory
Emit `FLEET_DIRECTORY.md`: DO-NOT-EDIT + generated-timestamp + source note header; grouped by ROSTER's sections; columns **Agent | Class | What it does | Status | Missing / next**. Resolve the one-liner-length question (see Decision 2). Commit.

### Step 3 — Wire it in (make it recurring)
Add a "regenerate FLEET_DIRECTORY" step to `sweeps/PRODUCTION_REVIEW.md` (runs every 14d / on-demand) + reference the artifact in CLAUDE.md FILES table + STATUS. Closes the PAT-034/PAT-041 installed-but-unexercised loop. Commit.

## Open decisions (confirm before Step 1)
1. **Maturity level in or out?** Will leaned "purely directory + what's-missing." Options: (a) leave levels out entirely — cleanest directory; (b) include a compact `Level` column but lead with does/missing so it reads directory-first. *Recommend (b)* — one extra column is cheap and the level is occasionally useful, but the doc is framed as a directory, not a scoreboard.
2. **Missing-one-liner source.** FLEET_MAP's `Gaps`/`Next_upgrade` cells are long/dense. Options: (a) machine-truncate `Next_upgrade` to first clause on render — zero curation, but truncation can read awkwardly; (b) add a curated `gap_1liner` (≤60 char) column to FLEET_MAP.tsv — reliable + improves FLEET_MAP itself, but ~28 rows of one-time curation. *Recommend (a) for v1* (ship fast, see it render), curate (b) later if the truncations read badly.
3. **Filename / location:** `AGENTS/DAEDALUS/FLEET_DIRECTORY.md`. (Confirm name.)
