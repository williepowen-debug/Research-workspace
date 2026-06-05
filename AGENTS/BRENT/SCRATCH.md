# BRENT SCRATCH — Jun 4-5, 2026 (Wed PM → Fri AM session: INCIDENTS scope-close + BRT-15 table + FASTOW build)

**Purpose:** Ephemeral session handoff — the canonical "where are we / what next" file. Read at boot (SPAWN PROTOCOL step 2), rewritten in full at closeout (step 11). Disposable: rewritten every session, not appended to. Persistent learnings live in `MEMORY.md`; dated forward catalysts live in `docket/CATALYSTS.tsv` (maintained by [FASTOW](docket/FASTOW.md) sub-agent); this file is the bridge between sessions.

---

## CHANGES SINCE LAST SESSION (Jun 3 PM → Jun 4-5)

- **Brent intraday turn:** AM/post-EIA high $97-98 area → faded to $94.99 by Thu PM close (-2.88%). USO -3.31%, WTI $92.92 (-3.23%). War-risk premium leg of BRT-15 has FADED — STNG flat-on-down-Brent day = market pricing OUT the kinetic tail.
- **CF position update:** decoupled from crude two days running — Mon +1.62% on oil +4.30% (underperformed); Thu +1.49% on oil -3.31% (inverse). HOLD-thesis rationale ("fertilizer catches when oil pops") weakened — the cross-trade is broken this week.
- **Origin sync:** clean throughout. 4 commits arrived during session (SAM separate-clones proposal, 2x HENRY KB prune, BROCK 6/4 sweep + Thesis-Kill Decision Tree). My BRENT commit landed in the linear history without divergence drama (auto-sync mechanism handled the rebase invisibly).
- **Concurrent-commit race observed:** commit `6c7d840b` in log explicitly notes "8ac5bf7 carries HENRY's work under a SAM message due to concurrent git add" — confirms the multi-agent git race that auto-memory `[[finding_concurrent_commit_index_race]]` + `[[finding_pathspec_commit_race_safety]]` (both Jun 4) already captured. No action needed; just awareness that the race is real.

## NEW THIS SESSION

- **`refinery_damage/INCIDENTS.tsv`** — added scope header: `# SCOPE: facility-damage only ... Military ops / intercepts / kinetic-without-facility-hit → HAWK domain (LESSONS #3)`. Closes Jun 1 Kuwait missile-intercept carry-forward as out-of-scope (not refinery damage; HAWK domain). Prevents re-spawn next session.
- **BRT-15 TABLED** (Option B per Will) — wait for fresh kinetic-trigger re-fire. War-risk leg faded since Jun 1 (STNG $75.53 vs $76.33 then; flat-on-down-Brent today = market dismissing the catalyst we'd be betting on). Cheaper mark is a *consequence* of thesis weakening, not a reason to enter. Trade idea ALIVE — discipline is the constraint, not conviction.
- **Sub-agent naming system-pattern ratified:** Path (a) — BRENT uses Enron exec names (FASTOW now; SKILLING/LAY/WATKINS candidates for future sub-agents). System-wide functional naming (CATALYST/WORKBOOK shared across agents) explicitly rejected — runtime coordination cost > one-time setup cost. New auto-memory `[[finding_subagent_naming_identity_over_functional]]`.
- **`docket/` subdirectory created** mirroring SAM/docket pattern. `git mv workbook/CATALYSTS.tsv → docket/CATALYSTS.tsv` (history preserved).
- **CATALYSTS.tsv schema bumped** — added `date_class` column (8th column, end-of-row). Values: `confirmed` (default, source-locked) | `modeled` (projection, revises as data evolves). 9 confirmed + 2 modeled rows (SPR 350M floor Jun 10, Cushing 20M floor Jul 1).
- **`catalyst_countdown.py`** — path updated, ~ prefix renders for modeled rows, header legend explains the marker. Verified clean.
- **`docket/FASTOW.md`** spec built (192 lines, tight adaptation of SAM/docket/KOYOMI.md). BRENT-specific deltas: modeled-date revision step (job step 4), position-expiry row class explicitly admitted, recurring-release universe inlined (10 release classes — EIA WPSR/STEO, CFTC COT, Baker Hughes, OPEC MOMR, IEA OMR, OPEC+ meetings, FOMC, US CPI, position-expiries, modeled-thresholds). Deferred from KOYOMI pattern: CALENDAR.md narrative twin (STATUS § CATALYST CALENDAR serves the role; FASTOW must surface STATUS-vs-TSV divergence as ESCALATION, not edit STATUS), RELEASES.md cadence file (inlined), `type` column (no BRENT-internal triggers yet).
- **`docket/FASTOW_MEMORY.md`** initial state — Run 1 NEXT RUN HINTS seeded (monthly audit fires by definition; modeled-date check against STATUS; Jun 3 EIA FIRED row retained 1d old per 1-week rule; 6 source URLs listed for baseline-audit sweep).
- **`CLAUDE.md` SPAWN PROTOCOL step 10** updated — CATALYSTS path → `docket/`, FASTOW spawn-pattern reference added, INCIDENTS scope-header noted.
- **`templates/SCRATCH.template.md`** + **SCRATCH.md WORKBOOK HEALTH** updated — paths + FASTOW reference.
- **2 new auto-memories** (see § NEW AUTO-MEMORY THIS SESSION below).

## WHAT I DID THIS SESSION

- 5-chunk build sequence executed with checkpoints (per `[[feedback_break_multifile_updates]]`):
  - Chunk 1: TSV migration + schema change + script update + verify (commit `1a1462a9`)
  - Chunk 2: FASTOW.md spec drafted (tight KOYOMI adaptation)
  - Chunk 3: FASTOW_MEMORY.md + housekeeping (CLAUDE.md + template + SCRATCH refs)
  - Chunk 4: FASTOW Run 1 smoke test — DEFERRED to next session per Will
- Front-loaded all 5 D-decisions (D1-D5) before execution per `[[feedback_front_load_planning]]` — Will batch-approved; zero mid-execution escalations.
- INCIDENTS.tsv carry-forward investigated and closed cleanly — initially proposed wrong rationale ("May 31 pass already excluded Kuwait" — fabricated precedent); Will caught it; refined the false-precedent failure mode into existing `[[feedback_verify_counts_before_propagating]]` memory body.
- BRT-15 entry-now framing presented; Will asked clarifying "what changed?"; honest re-read revealed nothing thesis-material had changed (war-risk faded, only mark improved). Recommendation revised to Option B (wait); Will agreed.

## NEXT SESSION (dated, future-verifiable)

1. **Fri Jun 5** — CFTC COT (May 26 data) = first post-Fri-drop read; Trigger #3 re-fire watch. Baker Hughes (BRT-26 vs 457 threshold; 429 last).
2. **Sun Jun 7** — OPEC+ regular meeting (first into a suspended-MOU regime; defense posture more probable; unwind likely deferred).
3. **Wed Jun 10** — **EIA WPSR (week Jun 5) = THE BIG PRINT.** SPR ~350M floor-touch (directional read — throttle = bullish, drain-through = near-term bearish + medium-term bullish, **NOT symmetric**). First clean post-Memorial-Day demand read (BRT-08/09 resolution candidate).
4. **Wed Jun 11** — EIA STEO June (first post-suspension; Q2 Brent peak likely revised UP not down).
5. **Sun Jun 15** — BRT-27 walkback deadline (Iran re-engages indirect talks within 14d of Jun 1 suspension?).
6. **Wed Jun 18** — CF $130C expiry.
7. **~Jul 1** — Cushing 20M operational floor (REVISED LATER from ~Jun 10-14); BRT-28 Bab al-Mandab 30-day window closes.

## NEXT SESSION (Tier 2 — architecture priorities carried forward)

8. **FASTOW Run 1 smoke test** — first real spawn against the spec built this session. Canonical invocation in `docket/FASTOW.md` § ORIENTATION. Will: "We will run the test for FASTOW in a future session - I wont forget." Model caveat: Agent tool `model` enum is `["sonnet", "opus", "haiku"]` — version selection (4.7 vs 4.8) not directly possible; passing `opus` inherits parent version. Run 1 is monthly-baseline-audit by definition (no prior run = trigger fires); expect ~10-12 min runtime (source-fetch + reconciliation across 10 release classes).
9. **SKILLING/LAY/WATKINS — next BRENT sub-agent (workbook-keeper equivalent)** — KURA-analog still TBD pending workbook revive-vs-demote decision (item 10). When/if you decide to revive KB/VX/FLOW, name will be picked from Enron-exec convention per `[[finding_subagent_naming_identity_over_functional]]`.
10. **BRENT-KURA-analog assessment** — workbook KB/VX/FLOW dormant 6+ wks; revive-vs-demote decision still OPEN with Will. Tier 2 carry.
11. **THESIS.md substantive rewrite** still deferred (v3.0 inverted Jun 1, reinforced-Phase-1 Jun 3, no further disambiguation Jun 4-5). Trigger event remains: Trump/Rubio response OR Iran walkback OR Jun 7 OPEC+ outcome.

## OPEN THREADS / WATCHES

- 🔴 **SPR ~350M floor watch (Jun 10 EIA)** — DIRECTIONAL, not symmetric. Don't lock to throttle-as-given.
- 🔴 **MOU suspension durability** — Iran walkback by Jun 15 (BRT-27) is the resolution event; Trump/Rubio rhetoric stays tape-tactical only per `[[feedback_trump_rhetoric_tape_not_info]]`.
- 🔴 **Bab al-Mandab credibility (NEW vector)** — BRT-28 by Jul 1.
- 🔴 **Cushing 20M floor pushed ~Jul 1** (was ~Jun 10-14) — still approaches but at slower pace; baton-passed to SPR for near-term forcing.
- 🟠 **BRT-15 — tabled but ALIVE** — re-arm watch: fresh kinetic event (Bab al-Mandab op, US-Iran direct exchange, Hormuz vessel attack) OR barnacle thesis re-surfacing in FT/Reuters.
- 🟠 **CF cross-trade decoupling** — 2-day pattern of CF moving inverse-to-crude. HOLD thesis assumed correlation. If decoupling persists, near-write-off odds tighten ahead of Jun 18 expiry. Watch.
- 🟠 **Trigger #3 re-fire** (Jun 5 COT first post-Fri-drop; Jun 12 COT first post-suspension).
- 🟠 **BRT-08/09 demand panel CONTAMINATED — re-read Jun 10** (first clean post-MD).
- 🟠 **BRT-26 shale response** (rigs 429 → 457; Baker Hughes Jun 5 + weekly).
- 🟠 **WTI-Brent spread direction watch** — PADD-3 export-pull narrative said spread should widen NEGATIVE (Brent premium); today's narrowed to -$2.07 (from Mon's -$3.27). Either fading or noise.
- 🟡 **HY energy OAS catch-up** — credit dismissed Brent moves; mechanism-vs-threshold note per `[[finding_threshold_vs_mechanism]]`.
- 🟡 **Crude import 4-wk YoY -4.5%** (deepened from -1.5%) — direction real, cause unconfirmed (supply vs demand/inventory mix).

## POSITION DECISIONS PENDING

- **CF $130C Jun 18** — HOLD CONFIRMED (Will, Jun 1 PM). 13 trading days to expiry. **CAVEAT (new this session):** CF decoupled from crude 2 days running. If decoupling persists, holding rationale weakens. No re-eval scheduled per Will Jun 1, but worth a check-in if you want to revisit.
- **XLE $65C Sep 30** — HOLD (live kinetic-gap-up insurance; ~12% OTM; ~4 mo to expiry).
- **Tanker BRT-15** — TABLED Jun 4 (Option B / wait-for-kinetic-trigger). Re-arm watch in Open Threads above.

## MAIL STATE (one line per signal)

- **Inbox:** clear (cross-agent intake on hold per `[[project_messaging_overhaul]]`).
- **Outbox:** clear (cross-agent signals deferred per same direction).

## WORKBOOK HEALTH

- **`thesis/PREDICTIONS.tsv`:** green; 28 rows (11 OPEN). No edits this session. All OPEN rows have future timeframes; no DUE-stale rows.
- **`docket/CATALYSTS.tsv`:** MIGRATED Jun 4 from `workbook/` → `docket/` + added `date_class` col. 11 rows (9 confirmed, 2 modeled). Maintained by [FASTOW](docket/FASTOW.md) sub-agent (built Jun 4-5; Run 1 pending smoke test).
- **`docket/FASTOW.md` + `docket/FASTOW_MEMORY.md`:** NEW this session. Spec + initial-state files for BRENT's first sub-agent. Run 1 will populate `## LAST RUN` and clear initial NEXT RUN HINTS.
- **`workbook/KB.tsv` / `VX.tsv` / `FLOW.tsv`:** DORMANT 6+ wks (still). **OPEN DECISION for Will: revive vs demote in CLAUDE.md step 8.** Tier 2 carry; if revive, the workbook-keeper sub-agent (SKILLING/LAY/WATKINS) gets built next.
- **`thesis/THESIS.md`:** still v3.0 "Phase 2 pricing dominant via diplomatic" — inverted Jun 1, reinforced-Phase-1 Jun 3, no further disambiguation Jun 4-5. Substantive rewrite still deferred.
- **`refinery_damage/INCIDENTS.tsv`:** 35 rows + scope-header (added Jun 4 PM). Green. Kuwait intercept carry-forward closed as out-of-scope (HAWK domain).

## GIT STATE

- **Commit this session:** `1a1462a9` (FASTOW build + INCIDENTS scope-header). Landed cleanly on origin/master via auto-sync mechanism between commit and explicit push attempt.
- **Closeout commit:** pending after this SCRATCH rewrite.
- **Origin state at closeout:** check via `git status` + `git log HEAD..origin/master` (per `[[feedback_behavior_language_over_hash_pinning]]`). Likely riding push-train of other agents' commits.
- **Other agents' uncommitted local at session start:** SAM (3 files in workbook/), BROCK (LESSONS.md). Both left untouched per `[[feedback_agent_git_isolation]]`. SAM has since pushed several commits.

## NEW AUTO-MEMORY THIS SESSION

- `[[finding_subagent_naming_identity_over_functional]]` — At current scale, prefer identity-naming (KOYOMI/FASTOW per parent) over functional-naming (CATALYST shared). Runtime coordination cost > one-time setup cost. Revisit threshold ~10+ agents × 3+ sub-agents. Validated Jun 4-5 on BRENT FASTOW build. Cross-agent applicable.
- **Refinement to existing `[[feedback_verify_counts_before_propagating]]`** — rule applies to EVERY factual claim, including throwaway-reinforcement-of-arguments-already-won. False-precedent decoration ("X was already decided," "Y already happened") creates downstream miscue when future sessions restate it as established fact. INCIDENTS Kuwait carry-forward investigation surfaced this; Will caught the fabricated "May 31 pass excluded Kuwait" claim that would have miscued against future real Kuwait facility events.
