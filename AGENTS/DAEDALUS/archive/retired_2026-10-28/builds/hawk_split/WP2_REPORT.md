# WP-2 Report — OSPREY Scaffold + Migration

> 🗄 **DATED BUILD-EXECUTION RECORD (2026-07-12; bannered 2026-08-17, self-audit F5 — same class as the 8/11 upgrades/ pass, which was scoped to upgrades/ only).** One-shot record; not maintained.

**Build agent:** DAEDALUS sub-agent (WP-2) · **Date:** 2026-07-12 · **Scope:** `AGENTS/OSPREY/` only (write), read-only everywhere else, zero git operations run (DAEDALUS commits after verification per build spec WP-4).
**Contract:** `AGENTS/DAEDALUS/builds/OSPREY_FALCON_BUILD.md` §5 (scaffold structure) + OSPREY-specific notes in the WP-2 task packet.

---

## Files created

| Path | Lines/Rows | Seeded from |
|---|---:|---|
| `CLAUDE.md` | 235 lines | Composed fresh: identity/scope disaggregated from HAWK `CLAUDE.md` (DOMAIN SCOPE, CROSS-AGENT SIGNALS hand-split per MANIFEST_A §2); boot/closeout sequence inherited verbatim structure with OSPREY-specific steps (5b strike-ledger staleness, 11 strike-sweep+mark-advance); KB schema + Admiralty rules verbatim-inherited; EXIT RULES built fresh Russia-coded (marked thin-at-launch); channel-model section replaces convergence-matrix-rubric+scenario-ladder sections (neither ported — per spec, OSPREY has no A/B/C/D construct) |
| `STATUS.md` | 72 lines | HAWK `STATUS.md` line-49 off-core Russia paragraph, expanded into a 3-channel dashboard using `SUMMARY.md`'s sourced aggregates + both 7/12 BRENT outbox packets (crude-terminal flip-trigger correction, tanker-campaign notice) |
| `SCRATCH.md` | 54 lines | HAWK `SCRATCH.md` ADDENDUM block (HAW-15 miss + correction) + NEXT SESSION item #3, reframed as OSPREY's founding-incident inherited context + first OSPREY-session next-steps; first-increment flags per task packet (4 items) |
| `NEXUS_BRIEF.md` | 66 lines | Fresh, theater-scoped, following `AGENTS/NEXUS/templates/NEXUS_BRIEF_SCHEMA.md` (same shape as HAWK's brief) — SENDING edges to BRENT (direct) + HAWK (routine synthesis) |
| `LESSONS.md` | 25 lines | HAWK `LESSONS.md` item 4 (mechanism-not-target + ledger-staleness corollary, marked PRIMARY INHERITOR / founding lesson) + item 2 copied (day-by-day gap-sweep methodology, Iran-sourced, provenance-noted) + the parallel-channels correction (sourced from `SUMMARY.md`, not originally in LESSONS.md — added per MANIFEST_C §6 surprise #6) |
| `MEMORY.md` | 26 lines | Fresh; hand-picked durable bullets from HAWK `MEMORY.md` (see-saw discipline, conf-code discipline, unconditional-no-void-path, dormant-armed framing, 529-concurrency) marked `[inherited]`, plus one fresh founding-incident entry |
| `SOURCES.md` | 117 lines | HAWK `SOURCES.md` generic sections copied verbatim (Military/Diplomatic/Think-tank/News-wire/Defense-journalism/OSINT) + Russia/Ukraine Regional Focus subsection only; Energy/Commodity BRENT-deferred note carried, scoped to OSPREY's terminal/tanker-transit use |
| `workbook/SCHEMA.tsv` | 15 rows (14 fields + header) | HAWK `workbook/SCHEMA.tsv`, copied verbatim |
| `workbook/KB.tsv` | 1 row (header only) | Fresh, zero data rows, per build spec (freeze-in-place KB decision) |
| `workbook/VX.tsv` | 3 data rows | HAWK `workbook/VX.tsv` rows VX-HAWK-UKR-01, VX-HAWK-SHADOW-01, VX-HAWK-SHADOW-02 — verbatim content, IDs kept unrenamed, provenance comment line added |
| `workbook/FLOW.tsv` | 3 data rows | HAWK `workbook/FLOW.tsv` rows FLOW-HAWK-07, -08, -20 — verbatim content, IDs kept, header note re: owed vol/credit rows |
| `thesis/PREDICTIONS.tsv` | 1 data row (OSP-01) | Fresh ledger; OSP-01 = HAW-17 verbatim content, re-homed with `←HAW-17` pointer in Notes; preamble carries HAW-15 full founding lesson + cross-cutting HAW-07/08-09/10-14 discipline notes |
| `thesis/THESIS.md` | 35 lines | **New file, not a HAWK inheritance** (HAWK had no Russia-side THESIS.md — its THESIS.md was 100% Iran and went to FALCON wholesale). Marked v0.1 spinout-seed, built only from STATUS/SUMMARY/outbox content already read, no new research |
| `domain/energy-strikes/STRIKES.tsv` | 32 data rows | HAWK `domain/energy-strikes/STRIKES.tsv`, all 32 RU-UA-tagged rows verbatim (4 GULF-IRAN rows excluded, went to FALCON); Tier-1 header: `# swept-complete through: 2026-07-12` + scope label added |
| `domain/energy-strikes/ANALYSIS_2026-07-12.md` | 80 lines | HAWK `domain/energy-strikes/SUMMARY.md` — schema/materiality/metric-discipline templates, sourced aggregates, Patterns ①-④ + CUT (incl. the 7/12 Pattern-① correction verbatim), Watch/flip-trigger table (trigger #2 marked FIRED), RU-only open-verify items, KB cross-refs — all ported, GULF-IRAN-specific lines excluded |
| `research/RUSSIA_OIL_INFRA_STRIKES_MAY-JUN2026.md` | 62 lines | Copied verbatim from HAWK `research/`, with an appended dated OSPREY note flagging that its "no new Baltic-terminal strike" line is now superseded by the 7/12 correction (points to ANALYSIS file, does not edit the original body) |
| `board_log.tsv` | 1 row (header only) | Fresh header, mirrors HAWK's fresh-KB pattern per build spec §2 gap-disposition |
| `templates/SCRATCH.template.md` | 36 lines | HAWK's template, copied with OSPREY-specific field labels (channel state instead of scenario %) |
| `inbox/processed/.gitkeep`, `inbox/WALTER/processed/.gitkeep`, `outbox/delivered/.gitkeep` | — | Fresh, per scaffold spec |

**File count: 21 files created** (17 content files + 4 `.gitkeep`s, counting `SCHEMA.tsv` and the 4 workbook/thesis/domain TSVs as content files). No `scripts/` directory created — instrument-light per build spec §1 decision #4 (PAT-048).

---

## Deviations from the task packet + why

1. **VX.tsv / FLOW.tsv provenance comment line.** The task packet said "header note re provenance" for VX and didn't explicitly ask for one on FLOW, but I added an equivalent comment line to FLOW.tsv too (owed-rows note), for symmetry and because the build spec's §2b ruling on FLOW-04/05 needed a place to land — a bare header would have silently lost that context.
2. **THESIS.md scope.** The task packet asked for "a thin thesis/THESIS.md... marked v0.1 spinout-seed" — I built it framed explicitly as *not* a HAWK inheritance (HAWK had zero prior Russia-side thesis document; FALCON's is the one that inherits wholesale), to avoid a reader assuming there was a fuller HAWK original that got trimmed.
3. **ANALYSIS_2026-07-12.md Watch-table status column.** I updated the trigger-status column's framing from "Status Jun 18" (SUMMARY.md's original) to "Status 2026-07-12" and added an explicit note that triggers #1/#3/#4 were "not re-verified since mid-June" — SUMMARY.md's aggregates were dated to the Jun 18 ORC pass; I did not fabricate fresher figures, I flagged the staleness instead (per the no-fabrication constraint).
4. **STATUS.md channel scoring.** The build spec's channel model has no pre-existing 1-5 scoring convention in HAWK's source material (HAWK never scored Russia as vectors on a 1-5 scale in STATUS — only in VX.tsv's color-bands). I derived 1-5 scores from the VX.tsv color-band states (RED→4-5, ORANGE-trending-up→3) rather than inventing an unrelated number — flagging this as a judgment call, not a sourced figure.
5. **No `scripts/` dir, no baghdad_watch-class tool.** Per build spec §1 decision #4, confirmed correct: OSPREY launches with zero scripts.

## Open items (not blocking, flagged for OSPREY's first live session / DAEDALUS WP-4 verification)

1. **Independent re-verification owed.** Every fact in STATUS.md/SCRATCH.md is HAWK-inherited as of 2026-07-12 — explicitly flagged in both files as not yet independently re-verified by OSPREY. This is by design (spinout day, not a live session) but WP-4's boot-doc dry-run should confirm the flag reads clearly.
2. **First-increment backlog (4 items, in SCRATCH.md):** Russia strike-feed/sanctions-tracker automation (priority), Russia-war vol/credit FLOW rows, firming the thin EXIT RULES, EU/Druzhba angle expansion. None block launch.
3. **Vessel-strike claim reconciliation** (21 vs 12 vs 42 tankers, channel 3) — flagged unreconciled in STATUS.md, inherited directly from HAWK's own outbox packet's unreconciled figures. Did not attempt to resolve — no new research was in scope for this build.
4. **`ledger_staleness.py` invocation** — CLAUDE.md boot step 5a wires `python3 "$(git rev-parse --show-toplevel)/scripts/ledger_staleness.py" OSPREY --quiet` (workbook ledgers). Step 5b (strike-ledger, Tier-1 fix #2) is written as a manual 3-line boot-doc check using in-content dates rather than a script invocation, per the build spec's explicit instruction ("in-content dates, not git-time, PAT-039") — this is NOT wired into `ledger_staleness.py`'s glob (which is git-time-based and workbook/*.tsv only). Confirmed correct per spec, flagging so WP-4's verification pass doesn't mistake this for a missed wiring.
5. **KB VOCABULARIES cross-check not run.** Boot step 4 references `AGENTS/VOCABULARIES.tsv` for Group/Entity/Source controlled vocab — not read/verified during this build since KB.tsv ships with zero rows. First real KB write should confirm OSPREY's Group values (WAR, ENERGY, UKR_ENERGY, TANKERS, etc., inherited from HAWK's KB.tsv Group-column distribution) still match current VOCABULARIES.tsv.
6. **No git operations performed** — per hard constraint. All 21 files are untracked on disk, awaiting DAEDALUS's own commit pass (path-scoped `AGENTS/OSPREY/`) after WP-4 verification.

---

*WP-2 complete. Confirmed zero writes outside `AGENTS/OSPREY/` and this report file; confirmed `AGENTS/HAWK/` shows no diff (`git status --porcelain -- AGENTS/HAWK/` empty).*
