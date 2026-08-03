# Falsification Freshness Sweep (recurring — sweep #3)

> Sizing note (2026-07-22): the 8/1 first run inherits 8 live agents with NO profile (AEOLUS/WATT/VULCAN/MIDAS/OSPREY/FALCON/HOMER/OZK, +WAL post-cutover) and 13 Δ-bannered profiles — the surface-inventory step will be the bulk of the run; budget accordingly.

**Purpose:** falsification surfaces rot silently while live theses re-scope — kill trees, validation docs, thesis tails, conviction marks, and *-consumed research headlines lag the thesis they're supposed to falsify, becoming decorative. The 2026-07-11 four-agent pilot found this in **4/4 agents** (HENRY: retired kill tree running unfrozen + HEN-35 at 2× live probability · VIOLET: thesis tail 3 version-bumps stale · LIQUID: conviction mark 16d/5-regime-facts stale, CHANGELOG pivot log stopped 5/19 · SAM: BOND-consumed doc leading with a twice-superseded mechanism). One sweep fixed instances; this sweep owns the decay *process*. Scoped by DAEDALUS 2026-07-12 per PROME ask (Will-approved 7/11).

**Cadence:** 21d (canonical row in `REGISTRY.tsv` — cite, don't restate). Offset ~1wk from the Staleness Sweep so the two don't stack in one session.

**Relationship to sweep #1 (Staleness):** #1 asks "is this LEDGER two-state clean (frozen-or-alive)?" — a file-level mtime/banner question. #3 asks "does this falsification SURFACE still describe the live thesis?" — a content-consistency question. A surface can pass #1 (recently touched) and fail #3 (touched by a hygiene pass, not re-scoped — the PAT-044 laundering case).

## Mechanism (design decisions, ratified 2026-07-12)

1. **Content-diff on in-content stamps, NEVER mtime/git-time.** PAT-039 (two instances: cloud-clone flatten + hygiene-edit clock-reset) and PAT-044 both show time-based signals launder freshness. Compare: surface's own version/date stamp + the thesis version it cites ↔ the agent's LIVE thesis version + STATUS as-of date.
2. **Flag threshold:** a falsification surface is STALE-FLAGGED when it is **>1 thesis-revision behind** the live thesis version OR its in-content stamp is **>21d older** than the live STATUS while the agent/theater is ACTIVE (dormant agents: surface may lag legitimately — check the dormant book's own re-sweep clock instead).
3. **Surface classes** (per agent, the checklist):
   - kill trees / exit protocols / channel-kill criteria (incl. retired-but-unfrozen kill trees — the HENRY case)
   - validation / falsification docs + pre-registered discriminator lists
   - thesis TAILS (the trailing sections of THESIS.md-class files — decay end per PAT-043)
   - conviction / regime marks and CHANGELOG pivot logs
   - ***-consumed research headlines** — any doc another agent reads by name (check the consumer's boot list); a stale lead paragraph here propagates cross-agent (the SAM→BOND case)
4. **Surface inventory source:** `profiles/<AGENT>.md` §3 "Invalidation / exit" rows (the comprehension layer already maps where falsification lives per agent — this is what the profiles are FOR) + the 7/11 pilot reports (`AGENTS/{VIOLET,LIQUID,HENRY,SAM}/reports/2026-07-11_threads-sweep.md`) as the seed. Agents without a profile row for invalidation → inventory at first sweep, add to the profile.
5. **Method — mechanized detection FIRST, then a judgment read of every flag** *(amended 2026-08-03 after run #1)*. Run `python3 AGENTS/DAEDALUS/scripts/falsification_scan.py` (read-only, cwd-proof): it emits `surface | class | verdict | stamp | live-ref | age | cited/live version | why` per surface, flags first, and always prints what it did **not** look at. Then read each flag in context before it leaves the desk — run #1 over-flagged **4 of 13** and every withdrawal came from opening the file. *(Mode-A Sonnet reader fan-out, one reader per 3-4 agents, remains the alternative when subagents are available — use it for the embedded-rail class in §3, which no file-level instrument can date.)*
   - **Verdict classes:** `STALE-FLAGGED` · `UNSTAMPED` (no dated claim — **never** graded CURRENT) · `CURRENT` · `FROZEN-OK` (dead-bannered = correct) · `EVENT-LOG` (fills only when a trigger fires — age measures the world, not the surface) · `DORMANT-SKIP`.
   - ⚠️ **Two surface KINDS, two vintage rules — the run-#1 lesson (PAT-077).** A **state** surface (thesis, validation doc, exit protocol, kill memo) is dated by its **header's labelled claim**, because its newest interior date is usually an event date inside a criterion. An **append-only** surface (changelog, decision log, TSV ledger) is dated by its **newest entry** — for a markdown changelog that means the newest *entry heading*, not the newest date anywhere in the body. Getting this backwards fails in **both** directions: reading a state doc loosely laundered HENRY's 38d surface as 17d-fresh; reading an append log's header flagged WALTER's live `kill_log.tsv` at 106d off its birth date.
   - ⚠️ **Check the REFERENCE for the defect you are detecting.** A thesis file can itself be dead-bannered (REGINALD's is `STALE-VINTAGE` do-not-cite). Grading children against a retired parent's version makes staleness read as conformance — when the reference is bannered, assert **no** live version and use STATUS as the only clock.
6. **Self-inclusion (2026-07-12, PAT-050):** DAEDALUS is IN SCOPE — its "falsification surfaces" = PATTERNS.tsv rows still asserted true, blueprint prescriptions vs live practice, and the maturity ladder's criteria vs how grades are actually given. Check that the standard still describes reality.

## Dispositions (approval-gated — same model as sweep #1)

- **Detection: autonomous, read-only.**
- **STALE-FLAGGED on a live/active agent → task packet to owner** (never direct-edit a falsification surface: re-scoping kill criteria is DOMAIN judgment, not hygiene — the one sweep where the dormant-freeze pre-approval class does NOT extend, because a wrong "fix" here silently changes what would falsify a thesis).
- **Retired-but-unfrozen kill tree → FROZEN banner** is the ONLY pre-approvable mutation class (mechanical, reversible, PAT-023 form) — and only idle-verified.
- Cross-agent consumed-doc staleness → flag BOTH sides (owner + consumer).

## Run Log

| Date | Scope | Findings | Dispositions |
|---|---|---|---|
| 2026-07-11 | VIOLET/LIQUID/HENRY/SAM (PROME-directed pilot, pre-registry) | 4/4 agents had falsification-surface rot (see Purpose) | Instances fixed in-session by owners; process ownership → this sweep (registered 7/12) |
| **2026-08-03** | **RUN #1 (first registered), +2d over cadence.** 32 surfaces / 19 agents, fleet-wide. Solo — fan-out barred by session rules, so detection was **mechanized** (`scripts/falsification_scan.py`, new) | **9 STALE-FLAGGED · 1 UNSTAMPED · 4 WITHDRAWN on read.** F1 REGINALD ×7 per-bank theses 105-125d unbannered (parent + validation doc both correctly bannered — PAT-068 shape) · F2 HENRY validation layer 38d **(recurrence)** · F3 LIQUID pivot log 39d **(recurrence)** · F4 HAWK EXIT_PROTOCOL unstamped · **F5 = the finding, and it is DAEDALUS's: 5 agents (AEOLUS/MIDAS/OSPREY/VULCAN/WATT) have a live thesis and NO falsification surface — all 5 my builds, one blueprint cause.** Instrument found **5 defects in itself** first (all one family) | Packets → REGINALD/HENRY/LIQUID · F4 **held** to the overdue HAWK sunset ruling · F5 → blueprint change + 8/5 ladder question · Full run doc: `runs/2026-08-03_FALSIFICATION_SWEEP_01.md` |
