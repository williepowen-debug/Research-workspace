# Falsification Freshness Sweep (recurring — sweep #3)

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
5. **Method:** Mode-A Sonnet reader fan-out (one reader per 3-4 agents), each returns per-surface: `surface | live-thesis-version/date | surface's cited-version/stamp | verdict (CURRENT / STALE-FLAGGED / FROZEN-OK) | one-line why`. DAEDALUS synthesizes; no reader edits anything.

## Dispositions (approval-gated — same model as sweep #1)

- **Detection: autonomous, read-only.**
- **STALE-FLAGGED on a live/active agent → task packet to owner** (never direct-edit a falsification surface: re-scoping kill criteria is DOMAIN judgment, not hygiene — the one sweep where the dormant-freeze pre-approval class does NOT extend, because a wrong "fix" here silently changes what would falsify a thesis).
- **Retired-but-unfrozen kill tree → FROZEN banner** is the ONLY pre-approvable mutation class (mechanical, reversible, PAT-023 form) — and only idle-verified.
- Cross-agent consumed-doc staleness → flag BOTH sides (owner + consumer).

## Run Log

| Date | Scope | Findings | Dispositions |
|---|---|---|---|
| 2026-07-11 | VIOLET/LIQUID/HENRY/SAM (PROME-directed pilot, pre-registry) | 4/4 agents had falsification-surface rot (see Purpose) | Instances fixed in-session by owners; process ownership → this sweep (registered 7/12) |
