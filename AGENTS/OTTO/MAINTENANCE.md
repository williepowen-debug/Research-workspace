# OTTO Maintenance Log

Reverse-chronological log of **structural** changes to OTTO's docs, folders, scripts, and
SPAWN/closeout protocol. Each entry: **Trigger / What changed / Files touched / Boot-impact /
Lessons**. Answers *"why is OTTO organized this way?"*

**Distinct from:**
- `CHANGELOG.md` — **analytical** changes (thesis/POV pivots, conviction shifts, prediction moves).
- `STALE_PUNCHLIST.md` — **forward** to-do (what's stale, needs fixing).

This log is the **structural** record (what infra/protocol changed and why). The CLAUDE.md version
stamp is the one-line index; the full entry lives here. Log material structural changes only — not
routine content edits. Archive to `archive/` if it grows past ~300 lines (SAM cautionary tale: 635).

---

## 2026-06-08 — Peer-parity push: boot automation + closeout maturation + MAINTENANCE.md (v2.1 → v2.5)

**Trigger:** Will-directed comparison to the mature agents (SAM, BRENT) across boot, then closeout, then structural logging. Capped with a domain data-refresh. Multi-part, collaborative — Will chose scope at each fork.

**What changed (by version bump):**
- **v2.2 — Boot automation.** Built `scripts/boot.py` orchestrator (price snapshot + predictions-due scan + catalyst countdown, ~2s) + `scripts/predictions_due.py` + `scripts/catalyst_countdown.py`. Created `docket/CATALYSTS.tsv` (8-col machine feed, backfilled from CRITICAL TIMELINE). Boot steps 4-5 rewritten as script-driven (was manual web-sweep that got skipped → staleness). Closed OTTO's long-deferred "Phase 4."
- **v2.3 — Closeout maturation toward SAM/BRENT.** STATUS line-cap (~250) + archive discipline (closeout step 1); created `CHANGELOG.md` thesis-pivot log + closeout step 1a; promotion-scan step (step 5) routing transferable lessons → auto-memory + remove-local; Git section fixed to pathspec pattern + Will-coordinated push (was the forbidden `git reset HEAD`/`git add <dir>`).
- **v2.4 — NEXUS_BRIEF.** Created `NEXUS_BRIEF.md` as a **Tier-2 opt-in** (locked schema is Tier-1-only; OTTO normally brief-exempt — Will approved the opt-in). Closeout step 7a (mandatory write-back). WALTER→NEXUS awareness signal dropped for scope ruling.
- **v2.5 — This log.** Created `MAINTENANCE.md`; trimmed CLAUDE.md version footer to point here; added closeout step 1b. Registered `STALE_PUNCHLIST.md` in CLAUDE.md (File Structure + Doc Ownership) after a Jun-8 re-audit (so the stale-doc plan survives MEMORY rewrites).

**Files touched:** `CLAUDE.md` (v2.1→v2.5), `STATUS.md` (417→163, archived), `MEMORY.md`, `LAST_COMPLETION.md`, `PREDICTIONS.tsv`, `workbook/ML.tsv`; **new:** `scripts/{boot,predictions_due,catalyst_countdown}.py`, `docket/CATALYSTS.tsv`, `CHANGELOG.md`, `NEXUS_BRIEF.md`, `MAINTENANCE.md`, `PEER_PARITY_ROADMAP.md`, `workbook/STATUS_archive_20260608.md`, 4 auto-memory files, WALTER inbox signal.

**Boot-impact:**
- Boot steps 4-5 now run `boot.py` (~2s) instead of manual sweep — the catalyst countdown + predictions-due scan are mechanized; boot read-sequence (STATUS→LAST_COMPLETION→MEMORY) unchanged.
- Closeout gained: 1a (CHANGELOG), 1b (MAINTENANCE), STATUS archive in step 1, promotion-scan in step 5, NEXUS_BRIEF write-back step 7a.
- `STALE_PUNCHLIST.md` now registered as a standing doc — next major session should re-audit it.

**Lessons (transferable — promoted to auto-memory):** date-specificity-weakest-link, forward-discovery-prediction-spirit, subagent-web-tools-not-autoloaded, litigation-allegation-weighting. Parity-audit recipe: compare boot first, then closeout, then structural logging — each pass surfaces a distinct doc-class gap.

---

## 2026-06-02 — Boot/closeout protocol hardening (v2.0 → v2.1, Phases 1-3b)

**Trigger:** Will-directed multi-phase protocol redesign (boot/closeout loop made self-closing).

**What changed:**
- **P1 Startup Protocol:** git-pull step 0 (+blocked-pull fallback); PREDICTIONS scan flags due-in-7d AND passed-but-OPEN; calendar past-due-catch (unswept vs acknowledged-pending); report-last ordering.
- **P2 Closing Protocol:** rewritten as write-back **mirror** of boot (read→write spine); catalyst-sweep BEFORE prediction-resolve (deliberate cross).
- **P3a:** live-state stripped from CLAUDE.md (Current Thesis → framing only; Thresholds drop Current col; STATUS = single source of truth).
- **P3b:** new `## Evidence & Hygiene Conventions` (evidence-grade tags `[CONF]/[PRESS]/[ALLEG]/[EST]`, `[STALE]` marking) + audit-finalized Doc Ownership table.

**Files touched:** `CLAUDE.md` (v2.0→v2.1); **new:** `STALE_PUNCHLIST.md` (9-item cross-doc rot inventory).

**Boot-impact:** boot/closeout became self-closing — boot flags overdue predictions + past-due catalysts; closeout must resolve them. First live catch: the new past-due-catch surfaced 3 unswept First Brands hearings, resolved same session.

**Lessons:** boot/closeout hardening recipe (mirror closeout to boot, strip live-state to single-source, doc-ownership table + deferred stale-punchlist) — auto-memory `[[finding_boot_closeout_hardening_recipe]]`.

---

*Pre-2026-06-02 structural history (Feb-Mar system build) not backfilled — reference root `archive/` graveyard + git log if needed.*
