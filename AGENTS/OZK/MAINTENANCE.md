# OZK — MAINTENANCE Log

*Reverse-chronological log of **structural** changes to OZK's docs / folders / scripts — the "why is OZK organized this way" record. Distinct from `CHANGELOG.md` (which tracks **analytical/thesis** changes) and `MEMORY.md` (session handoff + learnings). Read when investigating structure; write at closeout when structure changes. Format per DAEDALUS market-agent blueprint / OTTO template. ~300-line cap.*

---

### 2026-07-04 — MAINTENANCE.md created + BOTTOM LINE added (parity pass)
- **Trigger:** Will parity check vs L2 market-agents (VIOLET/BRENT/SAM) + DAEDALUS `market-agent.md` blueprint FLOOR. OZK was off the `MATURITY_MAP.md` (dormant during the 6/27 fleet scan).
- **What changed:** (a) Created this `MAINTENANCE.md` (blueprint-required structural log — was missing). (b) Added a **BOTTOM LINE** section to the end of `STATUS.md` (blueprint FLOOR item — was missing).
- **Files touched:** `MAINTENANCE.md` (new), `STATUS.md`.
- **Boot-impact:** none (both additive; no boot-sequence change).
- **Still-open parity gaps (queued — see MEMORY NEXT SESSION):** no `scripts/boot.py` boot kit; no `thesis/PREDICTIONS.tsv` + calibration scoreboard (falsification loop); standardized 5-pt convergence matrix not yet conformed; NEXUS_BRIEF vs REGINALD_CHANNEL is a design decision. Recommend a dedicated OZK maturity session with DAEDALUS running `maturity_scan.py` to get OZK onto the map + a conformance checklist.
- **Lessons:** A 71-day-dormant agent silently drops off fleet governance surfaces (maturity map, DAEDALUS scan). Revival should include a parity re-scan, not just a data re-baseline.

---

### 2026-07-04 — 71-day revival data re-baseline
- **Trigger:** OZK cold since 2026-04-24; Will-directed catch-up.
- **What changed (structural):** `research/threads/RESG_CONCENTRATION_VERIFICATION.md` created; both PROME inbox items moved to `inbox/processed/` (dir created); STATUS position table restructured to a stale/not-managed banner; WEAKNESSES gained section **C7**.
- **Files touched:** STATUS, CALENDAR, WEAKNESSES, MEMORY, research/threads/, inbox/processed/, outbox/.
- **Boot-impact:** none.
- **Lessons:** Analytical content of the re-baseline is logged in MEMORY (session notes) + this session's git commit `5e455b41`; only the structural deltas are recorded here.
