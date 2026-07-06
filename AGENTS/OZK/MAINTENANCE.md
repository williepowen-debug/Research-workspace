# OZK — MAINTENANCE Log

*Reverse-chronological log of **structural** changes to OZK's docs / folders / scripts — the "why is OZK organized this way" record. Distinct from `CHANGELOG.md` (which tracks **analytical/thesis** changes) and `MEMORY.md` (session handoff + learnings). Read when investigating structure; write at closeout when structure changes. Format per DAEDALUS market-agent blueprint / OTTO template. ~300-line cap.*

---

### 2026-07-06 — Staleness sweep (Will-directed): archive moves, KB schema repair, index re-base, new primary-source channel
- **Trigger:** Will asked for a tree-wide stale-info sweep + inbox check. Found an April-era band of docs that never received the 7/4 revival corrections.
- **Archive moves (git mv):** `THREAD3_ROLL_MATH.md` → `archive/` (dead — May roll passed unlogged); `AUDIT.md` → `archive/AUDIT_2026-04-24.md`; `workbook/KB_INDEX_AUDIT.md` → `archive/` (drift it flagged was fixed same day). Pointers updated in INDEX/TODO/CLAUDE.md.
- **KB.tsv schema repair:** rows 088/091 fixed (were 12-col — missing empty Vectors field, Notes had slid left); 055/138 demoted ACTIVE → REFUTED (Aug-2028 extension claim, refuted by Q1'26 call primary); KB-200 added (insider refresh); KB-200 group typo fixed (INSIDERS→INSIDER). Now 200 rows / 28 groups / 0 malformed.
- **KB_INDEX.md restructure:** new "Post-Q1 / Revival Clusters" section — the 12 groups that existed in KB.tsv but were never indexed (TODO §H1 Phases 2-4+6, now closed). Phase-2 decision: singletons stay standalone (no fold, no KB churn).
- **New primary-source channel:** `raw/Q1_2026_10Q.pdf` (60 pp, filed 5/6) retrieved via the **FDIC securities-filings JSON API** (see MEMORY Findings 7/6) — first scripted retrieval; bypasses the 403'd IR page. Insider Form 4 pipeline now one-command.
- **Boot-impact:** none structural. CLAUDE.md FILES table updated (THREAD3 row removed); core-thesis line re-based to Call Report figures; EFR URL modernized.
- **Content re-bases (analytical log → CHANGELOG v1.4):** THESIS/SCENARIOS/INDEX/subdomain STATUS files re-based to Call Report primary ($487.5M/1.48% past-due, 0.56% NCO); Boston-sponsor erroneous 7/4 re-open reconciled (resolved 4/23 via UCC-1, KB-195); Lincoln Yards 284K→320K residue fixed in SEVEN_CREDIT roster + TIMELINE; INSIDERS refreshed from fresh pull (16 new Form 4s).
- **Lessons:** (a) partial propagation is the dominant failure mode — three separate instances found (SEVEN_CREDIT roster vs dossier; STATUS re-open vs TODO resolution; GEOGRAPHY "Lincoln Yards sold" vs foreclosed). Fix = sweep ALL surfaces carrying a corrected figure, not just the doc where the correction landed. (b) A revival re-baseline can itself introduce errors by keying off stale secondary surfaces — verify against the resolution doc before re-opening a closed question.

---

### 2026-07-04 — `scripts/boot.py` v0.1 added (boot kit)
- **Trigger:** Will parity build — mature agents (VIOLET/BRENT/SAM) each have a one-command `scripts/boot.py`; OZK had none (booted manually off shared `market.py`).
- **What changed:** Created `scripts/` dir + `boot.py` v0.1 — self-contained (~150 lines): live prices via FORGE `fetch.py --json` (OZK + bank cohort, price-band + big-move flags), catalyst countdown (inlined list, trading-day counts, ⏰≤14d), standing-watch reminders (NCO kill-line / past-due / IQHQ reserve), inbox scan, STATUS/CALENDAR staleness. `--verbose` + `--horizon N` flags. Tested both modes clean.
- **Boot-impact:** CLAUDE.md boot **step 5 rewired** market.py → boot.py (market.py retained as manual fallback); step 6 inbox now folded into boot.py output.
- **Files touched:** `scripts/boot.py` (new), `CLAUDE.md` (boot step 5-6).
- **Deliberately v0.1 (not full parity):** catalysts/thresholds are **inlined** (hand-synced to CALENDAR/STATUS), not read from a machine feed; no separate `catalyst_countdown.py`/`thresholds.py`/FDIC-EFR fetcher. Decomposition → DAEDALUS blueprint pass.
- **Lessons:** reused FORGE `fetch.py --json` rather than reimplementing yfinance — one price source of truth, no drift.

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
