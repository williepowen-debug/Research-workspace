> RETIRED 2026-09-24 — CLOSED/SUPERSEDED 2026-07-22 (own banner); scoreboard built (AGENTS/LABOR/workbook/PREDICTIONS_SCOREBOARD.md), items resolved per upgrades/PRODUCTION_REVIEW_2026-07-22.md:30; >60d since last commit, not boot-read; referrers at retirement: none live.

# LABOR — Gap Assessment (what it lacks / is missing), 2026-07-10

> ✅ **CLOSED/SUPERSEDED 2026-07-22 (self-sweep fix-batch, Will-approved):** the ★ scoreboard was **BUILT+WIRED same-arc 7/10** (`workbook/PREDICTIONS_SCOREBOARD.md`, Brier-as-made 0.277, boot B4 + closeout C2) and ALL 4 owner-lane items resolved — in-file verified 7/22. No known LABOR substance gap remains. Current truth = FLEET_MAP row + `upgrades/PRODUCTION_REVIEW_2026-07-22.md`. States below are HISTORICAL.

**By:** DAEDALUS · **Trigger:** Will-directed ("look for what LABOR might lack or be missing") while Will works LABOR live in another window.
**Method:** Fresh read-verify of live surfaces (STATUS, CLAUDE, PREDICTIONS, workbook, inbox/outbox, git log) vs the 6/29 `profiles/LABOR.md` + `upgrades/LABOR_CARD.md`. PAT-029 (the read is load-bearing) — the card is 11 days stale and LABOR has booted ~5× since.
**AUTHORITY — LABOR is LIVE right now → ZERO direct edits.** Everything below routes as a task-packet (owner-lane hygiene) or a Will-approved BUILD (the scoreboard). Nothing here is applied. Grade unchanged: **L4 (conf H).**

---

## Headline: LABOR has self-closed ~its entire 6/29 upgrade card

Between 6/29 and 7/10 LABOR resolved, on its own closeouts, nearly every gap I had queued. This is the honest lead — most of "what it lacks" is already fixed:

| 6/29 carded gap | State 7/10 | Evidence |
|---|---|---|
| §2 Independence column (net-new handle) | ✅ DONE 7/2 | STATUS matrix `Indep` col ("don't multi-count"), "per DAEDALUS BATCH_02" |
| §5 If-Falsified ACTION column (net-new handle) | ✅ DONE 7/2 | Homed on the convergence matrix (per-vector, from TRADE §3) rather than PREDICTIONS.tsv — equivalent placement, accepted |
| Threshold bands homeless (§3, the "one real structural drag") | ✅ DONE 7/2 | KEY THRESHOLDS re-established as a **durable home in STATUS** (LABOR-10), TRADE §1 T-numbers are the canonical cross-refs |
| NEXUS_BRIEF stuck As-of Jun 16, not re-pinned | ✅ DONE 7/9 | NEXUS_BRIEF.md mtime 7/9 21:20 |
| board_log.tsv absent | ✅ EXISTS 7/9 | WALTER intake now logging (SIG-022/007 drained) |
| LAB-04 in CARL-pickup limbo since Jun-16 | ✅ DISPOSITIONED 7/9 | Will re-homed to **CORAL** (foreclosure-by-metro already CORAL's mandate); employment-signature cross-flag preserved |
| STATUS over 250-line cap | ✅ NOT A GAP | **224 lines** (my "45KB = acute cap breach" hypothesis was WRONG — 45KB is line *density*, not count. Verify-before-propagate, PAT-038.) |

**Takeaway:** LABOR's closeout discipline is working as designed — the read→write-back protocol (B/C symmetric) is clearing debt without DAEDALUS intervention. That is the more important signal than any single remaining gap.

---

## What LABOR still genuinely lacks

### 1. ★ THE ONE REAL GAP — prediction calibration scoreboard (missing SUBSTANCE, L5 lever)

**What:** LABOR has **8 RESOLVED predictions** (LAB-01/02/05/07/09/14/15/16) with genuinely excellent post-mortems in the Notes fields (anchor-vs-measure, wrong-gauge/denominator, announcement-type) **and 7 durable LESSONS (L-01..L-07)** — but **no aggregated scoreboard, no PREDICTIONS_ARCHIVE, no Brier tally, and no failure-modes-as-gating-checklist.** The learning material is all captured; it is never rolled up or fed forward as a structured gate.
**Why it matters:** This is the OTTO/PAT-014 institutional-learning pattern — the fleet's best prediction-discipline standard, which LABOR (head-of-chain, 16 predictions logged) is a natural home for. It was previously "HELD until upkeep justified" (like BROCK/ORACLE). **The justification has now arrived:** 8 resolutions is enough n for a real scoreboard, the failure taxonomy is already 7-deep, and — crucially — **the loop is already half-built**: boot step B4 literally says "before writing any NEW prediction, load the calibration context / separate mechanism from threshold." It references the discipline but there is no artifact the boot can point the reader at. The scoreboard IS that artifact.
**Effort:** M (one build session). Not a monitor-machinery build — a single `workbook/PREDICTIONS_SCOREBOARD.md` (or archive tab): resolved-table + hit-rate/Brier-ish calibration read + the L-01..L-07 failure-modes lifted into a pre-write checklist. Reuses existing data; no new plumbing.
**Expected value:** Closes the last L5 substance gap for a head-of-chain agent; converts 7 hard-won lessons from prose-in-LESSONS into an at-write-time gate; makes the calibration the B4 boot already promises real. HIGH for a top-transmission agent.
**First step:** Task-packet/Will-approval to LABOR to stand up the scoreboard from existing PREDICTIONS.tsv Notes + LESSONS at its next non-live closeout. **LABOR's own domain work — DAEDALUS does not build it.**

### 2. HYGIENE — CLAUDE.md KEY THRESHOLDS is a stale, boot-loaded duplicate (BRENT-line-168 class)

**What:** `CLAUDE.md` §KEY THRESHOLDS still shows a stale `Current` column — Initial Claims **213K** (live: 215K), U-3 **4.3%** (live: 4.2%), DOGE **312-327K** (LAB-07 resolved 403K), and a **"Shadow Payroll Gap — resolves Mar-Apr" row presented as THE forward "critical test"** even though that test resolved in **March** (LAB-09 CONFIRMED). Since 7/2, STATUS is the *durable home* for these thresholds (LABOR-10) — so CLAUDE.md now carries a stale, self-contradicting **duplicate** in a file loaded at every boot.
**Why it matters:** Boot-loaded stale "Current" values are the exact drift class we've been killing fleet-wide (BRENT line-168, ZHAO D-cluster, `finding_governance_doc_stale_default_drift`). A resolved test shown as forward is actively misleading at boot.
**Fix (owner-lane, S):** Replace the KEY THRESHOLDS table body in CLAUDE.md with a one-line **pointer to STATUS's durable home** ("KEY THRESHOLDS live in STATUS.md §KEY THRESHOLDS — durable home since 7/2"), or strip the `Current` col and keep only Metric/Threshold/Implication. One source of truth per metric (PAT-006).

### 3. HYGIENE — outbox residue, one file now OBSOLETE

**What:** `outbox/` root holds `2026-06-16_to-CARL_LAB-04-foreclosure-reclassification.md` — but LAB-04 was **re-homed to CORAL, not CARL**, on 7/9, so this packet is now *wrong*, not just old. Also `2026-06-16_to-NEXUS_warn-forward-radar.md` (stale). `outbox/delivered/` exists as the correct sink.
**Fix (owner-lane, S):** Trash/relocate the obsolete to-CARL file (superseded by the CORAL handover); confirm the to-NEXUS radar landed then move to `delivered/`.

### 4. MINOR — surface staleness (owner-closeout, note-only)
- **STATUS header accretion:** 4 stacked `**Last Updated:**` blocks at the top (7/9, 7/9, 7/6, Status). It DOES archive the spine ("Prior spine → domain/sources/…"), but 4-deep is the `finding_status_spine_staleness_under_appended_top` shape — roll older headers to the archive pointer.
- **EXPECTED_SIGNALS.md + FRAMEWORK_SUMMARY.md** (both Mar-17, v1.0 Feb-stale): now that bands are re-homed to STATUS (item 1 of the closed card), EXPECTED_SIGNALS is a candidate for a **stale banner or retirement**, not a live durable surface. `KB_old_11col.tsv` (44KB legacy) sits un-bannered beside the live KB.
- These are exactly what LABOR's own C3/research-retirement checklist catches — flag, don't queue.

### Not gaps (verified, do not propose)
- **New 7/9 tools** (`form4_scanner.py`, `job_postings_tracker.py`): structurally sound; the 4 owner-lane fixes (7/20 docket row per PAT-041, the `sell_value` null-branch bug, `DECEL_FLAG_PT` sourcing, cwd-proof docstrings) are **already routed** via PROME's 7/10 packet. FDIC backend spec also already in LABOR's inbox. Nothing to re-raise.
- **thesis/ dir absent:** thesis lives in STATUS (CORE TENSION + FED TRAP) by design — floor-not-ceiling, not a defect (PAT-015).
- **Two unprocessed PROME inbox packets (7/10):** LABOR is live and will consume them — sequencing, not a structural gap.

---

## Disposition / routing (LABOR is LIVE — nothing applied)

| # | Item | Type | Route |
|---|---|---|---|
| 1 | Calibration scoreboard | BUILD (M) | **Will approval** → task-packet to LABOR (its own domain work) |
| 2 | CLAUDE KEY THRESHOLDS stale dup | Hygiene (S) | task-packet to LABOR inbox / hand to Will in-session |
| 3 | Outbox obsolete to-CARL file | Hygiene (S) | task-packet to LABOR inbox |
| 4 | STATUS header / EXPECTED_SIGNALS / KB_old | Minor | note-only; LABOR's own closeout catches these |

**DO-NOT-TOUCH (per profile §5) unchanged:** CROSS-DOMAIN CONTEXT sign-separation, Kill A/B literal counts + revised-series rule, PREDICTIONS Status OPEN/RESOLVED controlled vocab (predictions_due.py:132 exact-match), FROZEN banners, LAB-04 handling, boot.py fail-loud gate.

**BOTTOM LINE:** LABOR is a healthy L4 that has cleared almost its whole 6/29 card on its own closeouts — the standout remaining item is the **prediction calibration scoreboard** (PAT-014/OTTO pattern), now well-justified (8 resolved + 7 lessons, boot B4 already references the discipline it lacks the artifact for). Everything else is small boot-loaded/outbox staleness that LABOR's own hygiene loop handles. Because LABOR is live, all of it is route-not-edit.
