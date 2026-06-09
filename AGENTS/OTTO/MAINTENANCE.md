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

## 2026-06-09 (PM) — WINTERKORN docket-steward sub-agent (v2.6 → v2.7)

**Trigger:** Same-session follow-on to thesis/ consolidation (v2.6). Will-directed TIER-1 audit identified the docket-keeper sub-agent as the highest-leverage next move — the Jun-8 First Brands `Jun 17 → Jun 12` catch was precisely the failure mode FASTOW's `[[finding_subagent_pre_fire_date_verification]]` was built to prevent. Planned-before-built: spec sub-agent identity, scope, autonomy gradient, recurring-release universe, spawn cadence, 7 open scope questions answered by Will before any file written.

**What changed:**
- **New `docket/WINTERKORN.md` (spec, ~250 lines).** FASTOW-pattern scoped owner. Mandate: maintain `docket/CATALYSTS.tsv` + verify forward dates against bankruptcy dockets, SEC EDGAR, rating-agency calendars, ABS pricing windows. Busy-work only — no analytical judgment. Owns write to CATALYSTS.tsv + WINTERKORN_MEMORY.md only; never touches STATUS / THESIS / CHANGELOG / PREDICTIONS / workbook / scripts. Pre-fire date verification within 7d window is the load-bearing job step (Jun-17→Jun-12 catch made cadence). Monthly baseline audit + post-miss audit with decline-memory (CALIBRATION is OTTO-owned; WINTERKORN reads but never writes).
- **New `docket/WINTERKORN_MEMORY.md` (state, ~120 lines, seeded blank).** Inaugural — no LAST RUN history. STANDING MONITORS seeded with per-case watches (First Brands highest activity; Tricolor Ch.7 cert-blocked source pattern; SDNY criminal selective; Carvana derivative) + recurring releases (Fitch ABS Index monthly, NY Fed HDC quarterly, S&P/KBRA/Moody's surveillance) + bank-earnings cycle (named-banks subset) + ABS pricing windows (modeled). NEXT RUN HINTS includes bootstrap-specific guidance for the imminent Jun 12 First Brands UST hearing.
- **CLAUDE.md Doc Ownership** — added 2 new rows for WINTERKORN.md + WINTERKORN_MEMORY.md; refactored `docket/CATALYSTS.tsv` row to flag WINTERKORN as maintainer (OTTO doesn't normally edit during session — applies WINTERKORN escalations).
- **CLAUDE.md Coordination** — new `### Sub-Agents` subsection codifying the sub-agent pattern + WINTERKORN row (pattern / owns / cadence) + spawn protocol pointer. References `[[finding_subagent_naming_identity_over_functional]]` for future sub-agent naming convention.
- **CLAUDE.md File Structure tree** — docket/ subtree expanded from 1 entry to 3 (CATALYSTS.tsv + WINTERKORN.md + WINTERKORN_MEMORY.md).

**Will-decided scope decisions (locked in spec):**
- **Naming = WINTERKORN.** Auto-domain reference (VW Dieselgate executive-knew-and-didn't-disclose archetype) matching OTTO's cockroach pattern. SAM (METSUKE — Tokugawa inspector) + BRENT (FASTOW — Enron CFO) precedent of identity-named people sub-agents preserved.
- **SDNY criminal track = SELECTIVE.** Trial date + cooperator-witness motions only. Routine motion practice excluded (would inflate TSV without driving OTTO action).
- **Bank earnings = NAMED-BANKS SUBSET ONLY.** JPM/5-3/BCS/Regions/MTB/OBK. REGINALD owns sizing; OTTO tracks disclosure escalation (different signal).
- **Spawn cadence = WEEKLY TUE + ON-DEMAND T-3 PRE-HEARING.** Outside that cadence, spawn cost > value.
- **ABS pricing rows = MODELED.** Issuer cadence projectable; revise within 7d via SEC EDGAR FWP search. Without this, OTTO walks into Jun 30 OTTO-05 resolve cold.
- **STATUS divergence rules = FASTOW PATTERN.** STATUS CRITICAL TIMELINE is a curated load-bearing subset of TSV (all 🔴 + position expiries + tracked-case hearings + OTTO-NN prediction resolves). Rolling monthly recurring releases live in countdown only, not in STATUS.
- **Build order = SPEC FIRST, MEMORY SEEDED BLANK.** Spec is the durable contract; first run populates MEMORY organically.

**Files touched:**
- New: `docket/WINTERKORN.md`, `docket/WINTERKORN_MEMORY.md`
- Edits: `CLAUDE.md` (Doc Ownership table + File Structure tree + new Sub-Agents subsection + version footer), `MAINTENANCE.md` (this entry), `STATUS.md` (boot-pointer refresh)

**Boot-impact:**
- No boot script changes — WINTERKORN spawns on demand via Agent tool, not via `scripts/boot.py`.
- OTTO's `scripts/catalyst_countdown.py` still reads `docket/CATALYSTS.tsv` directly; WINTERKORN edits flow through that pipeline unchanged.
- First WINTERKORN spawn is the validation test. Bootstrap NEXT RUN HINTS in MEMORY flag the Jun 12 First Brands UST hearing as the T-3 pre-hearing canonical first-run trigger.

**Lessons:**
- **Pre-fire date verification is the load-bearing argument for a docket-keeper sub-agent.** Not the "save context" framing — that's secondary. The Jun-17→Jun-12 catch costs OTTO real signal credibility when missed; making the verification cadence-driven (every run, every 7d-window row) is the value.
- **Selective scope on adjacent domains (SDNY criminal, bank earnings) prevents TSV inflation.** Without explicit scope decisions, baseline audits would over-propose. Recording Will's scope decisions in the spec (not just in CALIBRATION) makes them durable across future-WINTERKORN spawns who haven't seen the conversation.
- **FASTOW's decline-memory pattern (CALIBRATION as OTTO-owned, sub-agent reads but never writes) prevents the "audit nags monthly" failure mode.** Critical for a propose-only sub-agent that runs on cadence.
- **Inaugural MEMORY seeding is a real design step, not boilerplate.** A blank-MEMORY first run would have no STANDING MONITORS to anchor against; seeding with current OTTO domain state (per-case watches + known cert-blocked sources + bootstrap T-3 flag) gives the first run productive footing without ambiguity. Otherwise first-run quality is poor.

---

## 2026-06-09 — thesis/ subdir + canonical THESIS.md v1.0 (v2.5 → v2.6)

**Trigger:** Will-directed peer-parity audit (post-v2.5) surfaced thesis content scattered across 7 docs (STATUS § THESIS, CLAUDE.md "Current Thesis", top-level CHANGELOG, workbook/PREDICTIONS, MEMORY § Findings, ML.tsv, research/outputs/) with no canonical home. SAM model (`thesis/THESIS.md` + `thesis/CHANGELOG.md` + `thesis/PREDICTIONS.tsv` + `thesis/PREDICTIONS_ARCHIVE.md`) chosen as target. Planned-before-built: thesis content was articulated explicitly (Primary Cockroach + Secondary Invisible Exit + Carvana sub-thesis carve-out + transmission chain + why-now timing) before the folder was created — moving scattered artifacts into a new folder without nailing what the thesis IS would have just relocated the sprawl.

**What changed:**
- **New `thesis/` subdir** with 4 files:
  - **`thesis/THESIS.md` v1.0** — 12-section canonical thesis: header w/ decomposed conviction (Pattern HIGH / Magnitude HIGH / Near-term timing VARIABLE / Carvana LOWER), one-liner, Primary Cockroach (mechanism + 4-case table + falsification), Secondary Invisible Exit (mechanism + Tricolor industrial validation + falsification), **Carvana sub-thesis carved out** (was bundled at equal weight to 4 confirmed → now separate-conviction layer), transmission chain (7-stage end-to-end with current state), why-now timing claim (2022 vintage / Fed-pause / auditor cycle — defensible against "noise" alternative), expanded risk matrix (prob/impact/mitigation per row, was 4-row sketch in CLAUDE.md), position view (acknowledges TRADE.md stale), predictions w/ failure-pattern synthesis, cross-agent links.
  - **`thesis/CHANGELOG.md`** — moved from top-level (`git mv`); anticipated by header note in v2.5.
  - **`thesis/PREDICTIONS.tsv`** — moved from `workbook/` (`git mv`); 9-col schema unchanged.
  - **`thesis/PREDICTIONS_ARCHIVE.md`** *(NEW)* — 5 resolved-row post-mortems (OTTO-01/08/09/26/27) + calibration scoreboard (5/5 substance, 4/5 substance+window) + failure-pattern rules. Knocks STALE_PUNCHLIST items #4-5 (PREDICTIONS_ARCHIVE + calibration scoreboard preamble).
- **STATUS.md § THESIS block** — replaced 5-row case table + 2 prose paragraphs with **3-line summary + case-status mirror table + pointer to `thesis/THESIS.md`**. STATUS retains live case-status visibility (so dashboard remains self-contained for spawns) but the canonical narrative is single-sourced. Mirror-consistency direction: thesis/ canonical, STATUS mirrors live-state only.
- **CLAUDE.md Current Thesis section** — collapsed two ~4-line case mechanism paragraphs to a one-line bullet pointer. Was a "durable framing" home; canonical thesis now owns that. CLAUDE.md still names the two theses for SPAWN-time keyword orientation, then routes to thesis/THESIS.md.
- **CLAUDE.md Doc Ownership table** — added 2 new rows (`thesis/THESIS.md`, `thesis/PREDICTIONS_ARCHIVE.md`); refactored `STATUS.md` row to specify "live thesis-state *mirror*" not owner; refactored `thesis/CHANGELOG.md` and `thesis/PREDICTIONS.tsv` rows for the move; refactored `CLAUDE.md` self-row to drop "durable thesis framing" claim (now thesis/ owns).
- **CLAUDE.md File Structure tree** — top-level CHANGELOG.md removed; new `thesis/` subtree added; `workbook/` lost PREDICTIONS.tsv row.
- **CLAUDE.md Prediction Convention** — path updated `workbook/` → `thesis/`; added pointer to ARCHIVE for post-mortems; failure-pattern *rules* now home in THESIS.md § Predictions.
- **CLAUDE.md INBOX Processing + Closing Protocol** — path updates for PREDICTIONS.tsv (`workbook/` → `thesis/`).
- **CLAUDE.md Trade Flow** — path update for PREDICTIONS.tsv.
- **Scripts** — `scripts/predictions_due.py` PRED_TSV path updated (`workbook/PREDICTIONS.tsv` → `thesis/PREDICTIONS.tsv`); docstring + `scripts/boot.py` header text updated. **Important silent-pass bug found and fixed**: script silently returned "ran cleanly, no alerts" on file-not-found rather than erroring; first edit on the in-flight file-rename caught this. Now verified to read the new path.
- **STATUS boot-pointer** refreshed to summarize the Jun 9 session.

**Files touched:**
- New: `thesis/THESIS.md`, `thesis/PREDICTIONS_ARCHIVE.md`, `thesis/CHANGELOG.md` (via git-mv), `thesis/PREDICTIONS.tsv` (via git-mv)
- Edits: `CLAUDE.md`, `STATUS.md`, `scripts/predictions_due.py`, `scripts/boot.py`, `MAINTENANCE.md` (this entry)
- Deleted: `CHANGELOG.md` (top-level → moved), `workbook/PREDICTIONS.tsv` (→ moved)

**Boot-impact:**
- Boot step 4 (`predictions_due.py`) now reads `thesis/PREDICTIONS.tsv`. Verified clean: 12 OPEN ledger renders correctly.
- Future boot will hit the new layout naturally — boot step 1 (read STATUS) still works; if a spawn reads CLAUDE.md "Current Thesis" they'll be routed to thesis/THESIS.md within 3 lines.
- One-time call: if a spawn pattern-matches the old top-level CHANGELOG.md path, it should auto-recover via the SAM-style `thesis/CHANGELOG.md` find.

**Lessons:**
- **Plan the substance before the folder.** The structural move is the cheap part (5 min of git-mv + Edit). The hard part is articulating what the thesis IS in the form that the canonical doc needs (12 sections worth of synthesis). Doing the planning pass first surfaced the Carvana carve-out as the most important substantive change — without that, this would have been a relocate-and-rename exercise.
- **Silent-pass bugs hide in path-rename edits.** `predictions_due.py` returned "ran cleanly, no alerts" when the TSV file didn't exist — a wrong path produced false success. Caught only because I re-ran the script after the path edit and noticed it claimed clean against a file that no longer existed at that path. Path-renames should always be followed by an end-to-end verify, not just "edit succeeded."
- **STATUS-as-mirror requires explicit direction encoding.** New ownership rows had to specify "live thesis-state MIRROR" not "live thesis state" to signal the canonical-wins direction. Auto-memory `[[finding_doc_mirror_consistency_check]]` pattern applies: encode the direction, then a closeout/boot check can verify the mirror agrees.
- **OTTO's thesis was meaningfully more mature than its STATUS block suggested.** The 5-row case table in STATUS gave a flat view; the actual thesis — once articulated — has structural depth (4 mechanism features, 2 interlocked theses with explicit explanatory link, 7-stage transmission chain, why-now timing claim, decomposed conviction). The lesson: when an agent has been doing the thinking but storing the conclusions in a flat dashboard, the thesis already exists — it just hasn't been written down.

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
