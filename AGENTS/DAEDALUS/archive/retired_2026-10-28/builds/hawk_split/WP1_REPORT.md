# WP-1 Report — FALCON scaffold + content migration

> 🗄 **DATED BUILD-EXECUTION RECORD (2026-07-12; bannered 2026-08-17, self-audit F5 — same class as the 8/11 upgrades/ pass, which was scoped to upgrades/ only).** One-shot record; not maintained.

**Executed by:** DAEDALUS build sub-agent (WP-1) · **Date:** 2026-07-12 · **Scope:** `AGENTS/FALCON/` only (created), + this report.
**Contract:** `AGENTS/DAEDALUS/builds/OSPREY_FALCON_BUILD.md` (§1 decisions, §2/§2b dispositions, §4 Tier-1 fixes, §5 scaffold structure) + `AGENTS/HAWK/design/2026-07-12_war-agent-split-spec.md` + `builds/hawk_split/MANIFEST_{A,B,C}`.
**Constraints honored:** read-only on everything outside `AGENTS/FALCON/` and this report; zero writes/moves/deletes under `AGENTS/HAWK/`; zero git commands executed (add/commit/mv) — verified via `git status --porcelain -- AGENTS/HAWK/` (empty) and `git status --porcelain -- AGENTS/FALCON/` (shows `?? AGENTS/FALCON/`, fully untracked) at report time. All TSV row migrations were done by `awk` extraction from the HAWK source files (never hand-retyped) to eliminate transcription risk — verified column counts match source schemas exactly (VX 11 cols/row, FLOW 9 cols/row, STRIKES 16 cols/row, SCHEMA byte-identical `diff`).

---

## 1. Files created (22 files + 3 `.gitkeep`)

| Path | Lines/rows | Seeded from |
|---|---|---|
| `CLAUDE.md` | 298 lines | Composed fresh: HAWK's CLAUDE.md (boot/closeout skeleton, KB schema, Admiralty rules, EXIT RULES, SCENARIO FRAMEWORK, git citation) hand-disaggregated per MANIFEST_A §2 DOMAIN SCOPE/CROSS-AGENT SIGNALS split; Tier-1 fixes (build spec §4) added as new boot/closeout steps; BLUEPRINTS/market-agent.md conformance (PAT-031 cwd-proof, PAT-023 ledger staleness) |
| `STATUS.md` | 122 lines (≤250 cap OK) | HAWK STATUS.md lines 1-6 (header, trimmed to FALCON-only), 7-29 (Scenario Posture ladder, verbatim), 32-47 (10-vector convergence matrix, verbatim), 53-71 (CONFIRMED/CLAIMED/UNVERIFIED, verbatim), 75-90 (Next-Rung Tells, verbatim), 93-104 (Cross-Agent Implications — FALCON-relevant rows only: BRENT/HENRY/LIQUID/SAM/CARL/REGINALD; VULCAN/MIDAS + RED/NEXUS rows dropped to HAWK-synthesis per MANIFEST_A §1), 108-115 (predictions — HAW-14 kept as frozen reference row, HAW-16 re-homed as FAL-01), 119-121 (Bottom Line, adapted) |
| `SCRATCH.md` | 51 lines | HAWK SCRATCH.md CURRENT MARKS (Iran line only) + NEXT SESSION items #1,2,4,5,6,7 (Russia item #3 and the HAW-14-post-mortem item #8 dropped per MANIFEST_A §3) + 3 new FIRST-INCREMENT items per build-spec instructions (Gulf-Iran backfill, scripts refresh-candidates, THESIS rewrite backlog) |
| `NEXUS_BRIEF.md` | 74 lines | HAWK NEXUS_BRIEF.md filtered to FALCON-theater content; SENDING table adds routing column (direct+HAWK-cc for 🔴 vs via-HAWK-synthesis for 🟠, per spec §3/§10); added a HAWK row (routine reads) and OSPREY row (WAITING FOR, cross-war teams-mode case) |
| `LESSONS.md` | 20 lines | HAWK LESSONS.md items 1, 2, 4 verbatim + provenance header (item 3, Venezuela, stays HAWK's own per build spec §2 ruling) |
| `MEMORY.md` | 26 lines | Fresh file; 3 hand-picked bullets copied (not moved) from HAWK MEMORY.md: conf-code discipline, see-saw discipline, deferral-dynamic anchor — exactly the three named in the work-package brief |
| `SOURCES.md` | 115 lines | HAWK SOURCES.md generic sections (Military/Diplomatic/Think-tank/News-wire/Defense-journalism/OSINT) copied verbatim + Iran/ME regional subsection kept; Russia/Ukraine + China-Taiwan + Venezuela/LatAm regional subsections dropped (moved to OSPREY/HAWK respectively); Energy/Commodity BRENT-deferred note kept |
| `board_log.tsv` | 1 line (header only) | Fresh — header copied verbatim from HAWK's board_log.tsv column spec |
| `workbook/KB.tsv` | 2 lines (comment + header, 0 data rows) | Fresh — 13-col schema, comment line states provenance-citation convention (`KB-HAWK-NNN`) |
| `workbook/SCHEMA.tsv` | 14 lines | Copied verbatim from HAWK (`diff` confirms byte-identical) |
| `workbook/VX.tsv` | 9 lines (comment + header + 7 data rows) | `awk`-extracted verbatim from HAWK's VX.tsv: IRAN-01, IRAN-02, USIRAN-KINETIC-01, GULFSTATE-01, DIPLOMACY-01, ISR-01, BABMANDAB-01 — IDs retain `VX-HAWK-` prefix per instructions |
| `workbook/FLOW.tsv` | 13 lines (comment + header + 11 data rows) | `awk`-extracted verbatim: rows 01,02,03,04,05,06,09,11,12,14,17 per build-spec §2b ruling; IDs retain `FLOW-HAWK-` prefix |
| `workbook/EXIT_PROTOCOL.md` | 60 lines | Copied from HAWK's `workbook/EXIT_PROTOCOL.md` + inheritance-provenance banner |
| `thesis/PREDICTIONS.tsv` | 15 lines (comment preamble + header + 1 data row) | Fresh scoreboard (0C/0F/0P/0V/1 OPEN); inherited calibration-lessons preamble per MANIFEST_C §2 (HAW-06/07/08-09/10/11/14 + cross-cutting mechanism-not-target/ledger-staleness); FAL-01 = HAW-16 verbatim terms, re-homed, `←HAW-16` in Notes |
| `thesis/THESIS.md` | 170 lines | Copied wholesale from HAWK's `thesis/THESIS.md` (100% Iran content per MANIFEST_C §3 finding — no surgery needed); SUPERSEDED banner kept + 1 inheritance line added |
| `thesis/TIMELINE.md` | 224 lines | Copied wholesale, same treatment; added a note flagging Forward Branch Points table as stale/superseded by live STATUS |
| `thesis/CHANGELOG.md` | 189 lines | Copied wholesale + 1 new dated entry (2026-07-12 FALCON SPINOUT) documenting the mechanical copy per changelog's own audit-trail convention |
| `domain/energy-strikes/STRIKES.tsv` | 7 lines (2 comment lines + header + 4 data rows) | `awk`-extracted verbatim: the 4 GULF-IRAN rows (GI-20260307-HAIFA, GI-20260319-YANBU/MINAAHMADI/MINAABDULLAH); Tier-1 header fixes applied (`swept-complete through: 2026-03-19` high-water-mark + scope label, per build spec §4 fixes #1/#5) |
| `domain/energy-strikes/ANALYSIS_2026-07-12.md` | 43 lines | Schema/materiality-bar/metric-discipline template sections copied from HAWK's SUMMARY.md (Russia-specific Patterns/flip-triggers/aggregates explicitly excluded — those went to OSPREY); explicit founding-mandate statement per instructions |
| `templates/SCRATCH.template.md` | 36 lines | Copied verbatim (`diff` confirms byte-identical) |
| `inbox/processed/.gitkeep`, `inbox/WALTER/processed/.gitkeep`, `outbox/delivered/.gitkeep` | 0 lines each | Fresh placeholders |

**Not created (by design):** `AGENTS/FALCON/scripts/` — `baghdad_watch.py` + state JSON arrive via a WP-3 `git mv` from `AGENTS/HAWK/scripts/`, which is DAEDALUS's HAWK-recut work package, not WP-1. CLAUDE.md boot step 5b documents this explicitly (the invocation path is written correct-for-after-WP-3, with a note that it will 404 until the git mv lands). `domain/sources/` (STATUS archive dir) — not created since it holds no content yet (created-when-first-needed per blueprint convention, noted in FILES table).

---

## 2. Deviations from the build spec + why

1. **STATUS.md predictions table:** kept HAW-14 as a full reference row (not just a footnote) alongside FAL-01, since the work-package brief explicitly asked for "predictions table rows HAW-14 (FAILED, historical ref) + FAL-01 (OPEN)." This slightly duplicates content that also lives frozen under HAWK, but it matches the literal brief instruction and gives FALCON's STATUS a complete, self-contained predictions section without a forced cross-file jump for the most recent resolved prediction in its own theater.
2. **THESIS.md SCENARIO FRAMEWORK note:** the work-package brief said "SCENARIO FRAMEWORK wholesale" but HAWK's CLAUDE.md scenario table (4-tier A/B/C/D) doesn't match the live STATUS.md 3-tier B/C/D ladder (the live ladder dropped the discrete "A — Surgical" and "D — Collapse/Nuclear" framing sometime after the CLAUDE.md table was last touched). I inherited CLAUDE.md's A/B/C/D table wholesale as instructed (blueprint conformance, generic floor definition) but added an explicit note flagging the live-vs-frozen-table mismatch so a future FALCON session doesn't silently cite the wrong ladder. This is a **pre-existing HAWK inconsistency**, not something WP-1 introduced — flagging for DAEDALUS verification (WP-4) rather than silently resolving it.
3. **NEXUS_BRIEF.md `STATUS commit:` field:** left as "pending (build-phase, uncommitted at write time)" since no commit exists yet at scaffold time (DAEDALUS commits after WP-4 verification, per the work-package's read-only/no-git constraint on this sub-agent). Whoever runs the first live FALCON session should refresh this to a real hash at first closeout.
4. **MEMORY.md scope:** the work-package brief named exactly three bullets to copy (see-saw, conf-code, deferral-dynamic). I stayed strictly to those three rather than also pulling HAWK's more-generic findings (e.g. "FLOW=canonical/KB=pointer," "dormant-armed framing") that would also have been defensible — erring toward literal instruction-following over my own judgment on an under-specified "durable Iran-relevant" boundary. Flagging in case DAEDALUS wants a broader MEMORY.md at verification.
5. **`domain/energy-strikes/ANALYSIS_2026-07-12.md` dated filename:** used today's date (2026-07-12) per the Tier-1 fix #4 "dated, regenerated" convention — matches the filename the work-package brief specified.

No other deviations. All row/ID migrations verified column-count-consistent against source schemas (§ above); no data was hand-transcribed.

---

## 3. Open items for DAEDALUS verification (WP-4)

1. **Boot-doc dry run:** `python3 "$(git rev-parse --show-toplevel)/scripts/ledger_staleness.py" FALCON --quiet` has not been run against the new `AGENTS/FALCON/workbook/` — worth a live check that the fresh KB.tsv (0 rows) and migrated VX/FLOW don't trip a false-positive staleness alert on first real boot.
2. **`baghdad_watch.py` git mv (WP-3 dependency):** FALCON's CLAUDE.md boot step 5b and FILES table both reference `AGENTS/FALCON/scripts/baghdad_watch.py`, which does not exist yet — confirm the WP-3 git mv lands before FALCON's first live session, or FALCON's boot will rc=2 on that step (documented as expected-until-WP-3 in CLAUDE.md, but worth a WP-4 checklist item so it isn't forgotten).
3. **Scenario-ladder mismatch (item 2 above):** HAWK's CLAUDE.md 4-tier A/B/C/D table vs STATUS.md's live 3-tier B/C/D ladder — pre-existing inconsistency inherited into FALCON's CLAUDE.md verbatim per instructions; recommend DAEDALUS decide whether to reconcile CLAUDE.md's table to match STATUS.md's live ladder now or leave both as-is pending the THESIS.md rewrite backlog.
4. **STATUS.md line count:** 122 lines, well under the 250-line cap — no action needed, noted for completeness.
5. **Seam grep (no orphaned refs):** not run by this sub-agent (out of WP-1 scope, explicitly a WP-4 job per build spec §7) — recommend checking that nothing outside `AGENTS/FALCON/` references a not-yet-existing FALCON path (e.g. ROSTER.md, root CLAUDE.md transmission chain — those are WP-5 registration items and shouldn't yet reference FALCON, but worth confirming no premature refs exist).
6. **Git:** zero commits made by this sub-agent per instructions. `AGENTS/FALCON/` is fully untracked (`git status --porcelain` confirms `?? AGENTS/FALCON/`). DAEDALUS commits after verification, path-scoped `AGENTS/FALCON/`.

---

## 4. Summary

22 files + 3 `.gitkeep` placeholders created under `AGENTS/FALCON/`. All TSV data rows mechanically extracted (never hand-retyped) from HAWK's live 2026-07-12 source files, verified column-count-consistent. `AGENTS/HAWK/` was read-only throughout — zero writes, zero git operations. Two items flagged for DAEDALUS's WP-4 verification pass are genuinely open (scenario-ladder table mismatch inherited from a pre-existing HAWK inconsistency; the `baghdad_watch.py` WP-3 dependency) — neither blocks FALCON's scaffold correctness, both are pre-flagged so they aren't rediscovered cold.
