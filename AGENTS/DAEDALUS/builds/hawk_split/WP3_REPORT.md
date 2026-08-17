# WP-3 Report — HAWK re-cut to synthesis + dormant book

> 🗄 **DATED BUILD-EXECUTION RECORD (2026-07-12; bannered 2026-08-17, self-audit F5 — same class as the 8/11 upgrades/ pass, which was scoped to upgrades/ only).** One-shot record; not maintained.

**Executed by:** DAEDALUS build sub-agent · **Date:** 2026-07-12 · **Scope:** `AGENTS/HAWK/` only (OSPREY/FALCON read-only, untouched — hard constraint honored throughout).
**Contract:** `AGENTS/DAEDALUS/builds/OSPREY_FALCON_BUILD.md` §2 dispositions, §2b FLOW rulings, §3 pre-freeze hygiene (as amended), §6 HAWK residual + `AGENTS/HAWK/design/2026-07-12_war-agent-split-spec.md` §5-6.

---

## Files rewritten / bannered / created

| File | Action | Detail |
|---|---|---|
| `CLAUDE.md` | **Full rewrite** | Identity → synthesis+dormant; new SYNTHESIS DISCIPLINE section (thin/derived, boot-read sibling briefs, reconcile-not-re-narrate); boot sequence rebuilt (added step 4 = read OSPREY+FALCON NEXUS_BRIEFs, step 6b = dormant-book 45d re-sweep cadence check; removed baghdad_watch step 5b, strike-ledger closeout line); removed SCENARIO FRAMEWORK / CONVERGENCE MATRIX / EXIT RULES (war-thesis-kill) sections entirely — replaced with a closeout "synthesis-consistency check" step; DOMAIN SCOPE rewritten to dormant-book + synthesis seams only, explicit NOT-OWNED (theater tracking → siblings, oil price → BRENT); CROSS-AGENT SIGNALS rewritten (routine-only send table, explicit note that acute 🔴 signals are the siblings' own right, not gated through HAWK); KB schema section kept verbatim except the stale "currently through KB-HAWK-034" line fixed to "≤223 pre-split / 224+ synthesis-dormant"; FILES table fully rewritten (live vs. 🧊 frozen surfaces, pointers to siblings). 235 lines (was 276). |
| `STATUS.md` | **Full re-cut** | New ≤120-line synthesis dashboard: CROSS-WAR READ (decoupling-gap reconciliation + double-count check), WAR-RISK/SHIPPING AGGREGATE (pointer-form, seeded from SUMMARY.md's cross-war timing line), DORMANT BOOK table (8 VX rows w/ Last_Updated + 45d re-sweep-cadence column + Taiwan/Venezuela NEVER-ACTIONED flag from OPEN_THREADS), PREDICTIONS section (re-totaled scoreboard + REHOMED pointers), POINTERS block, synthesis-form BOTTOM LINE. **57 lines** (target ≤120, well under). |
| `workbook/VX.tsv` | **Reduced, verbatim rows** | 18→8 data rows (VEN-01, TWN-01, IRAQ-01, TRADE-01, TRADE-02, SULPHUR-01, FININFRA-01, CEASEFIRE-01) — extracted via `sed` from the original file by line number (not retyped) to guarantee byte-verbatim content; split-note header line prepended. Verified via `cut -f1` that the extracted ID set exactly matches the manifest's HAWK-disposition list. |
| `workbook/FLOW.tsv` | **Reduced, verbatim rows** | 20→6 data rows (FLOW-10, -13, -15, -16, -18, -19) — same `sed`-extraction method; split-note header states FLOW-19 = live canonical decoupling home, FLOW-18 = open owner-lane question, net split FALCON 11 / OSPREY 3 / HAWK 6. |
| `workbook/KB.tsv` | **Header note only** | One `#SPLIT-NOTE` comment line prepended via `sed -i` (file untouched otherwise — 225 data rows, no row surgery, per freeze-in-place-but-stays-live ruling). |
| `thesis/PREDICTIONS.tsv` | **Preamble + 2 rows edited** | Scoreboard preamble re-totaled to `5 CONFIRMED / 8 FAILED / 1 PARTIALLY / 1 VOIDED / 0 OPEN` (was stale: listed HAW-15 OPEN, undercounted FAILED by one). HAW-16 and HAW-17 rows: Status column `OPEN` → `REHOMED`; Notes appended with `REHOMED → FAL-01 (FALCON)` / `→ OSP-01 (OSPREY)` pointers. All other 15 rows untouched. |
| `thesis/PREDICTIONS_ARCHIVE.md` | **5 sections backfilled** | HAW-10, HAW-12, HAW-13, HAW-14, HAW-15 added (verbatim Outcome/Notes copied from PREDICTIONS.tsv at time of backfill), each stamped `[backfilled-at-split 2026-07-12 — mechanical; ...]` with a pointer to where the fuller analytical post-mortem lives (LESSONS.md entries, SCRATCH trail, OSPREY's founding lesson). HAW-10 inserted between HAW-09/HAW-11 (chronological placement); HAW-12/13/14/15 appended after HAW-11. Archive now has all 15 closed-row sections (HAW-01..15 minus the 2 OPEN-turned-REHOMED, which have no archive section since REHOMED isn't a closed status). |
| `domain/energy-strikes/STRIKES.tsv` | **FROZEN banner** | `#FROZEN 2026-07-12` comment line prepended, pointing to OSPREY's (32 RU-UA) and FALCON's (4 GULF-IRAN) live ledgers. Content otherwise untouched (36 rows preserved). |
| `domain/energy-strikes/SUMMARY.md` | **FROZEN banner** | Blockquote banner inserted after the H1, same pointer content + pointer to the new CROSS_WAR_SUMMARY.md. |
| `domain/energy-strikes/CROSS_WAR_SUMMARY.md` | **New file** | Thin, explicitly-regenerated-not-maintained cross-theater table: one row per theater (ledger path, row count, date range, swept-through mark [OSPREY current 7/12, FALCON stale 3/19 — asymmetry stated explicitly, not absorbed], channel state, pointer) + the one genuine cross-war timing observation (Russia campaign peak coincided with Iran's MOU signing week) + a reading-caveat section. |
| `SCRATCH.md` | **Full rewrite** | SPLIT-COMPLETION NOTE section added (what WP-3 did, pointer to this report); CURRENT MARKS / WHAT I DID / NEXT SESSION (5 items: first independent synthesis pass, Taiwan/Venezuela re-sweep, FLOW-18 disposition, HAW-14 deeper post-mortem, sibling swept-through-mark check) / OPEN THREADS / PREDICTIONS DUE (none) / MAIL STATE / PENDING PUSH — MAIL STATE and PENDING PUSH pattern kept per instruction. |
| `NEXUS_BRIEF.md` | **Full re-cut** | VIEW = reconciled both-theater delta read (kinetic-high/decoupled-both, double-count-check clean); CALIBRATION = pointer to frozen HAW-01..17 record + HAWK's own no-open-predictions state; SENDING = BRENT/HENRY/LIQUID/SAM routine-only (explicit note acute sends bypass HAWK); WAITING-FOR = OSPREY's and FALCON's first independently-verified (non-seeded) briefs. |
| `LESSONS.md` | **Header note added** | Split-note: items 1-2 primary-inherited by FALCON (item 2 copy-worthy to OSPREY), item 4 by OSPREY (its founding lesson), item 3 (dormant re-sweep) = HAWK's own standing operating lesson, wired into CLAUDE.md boot step 6b. Full 4-entry history preserved, nothing removed. |
| `SOURCES.md` | **Trimmed + notes** | Removed Iran/Middle East and Russia/Ukraine regional subsections (kept China/Taiwan + Venezuela/LatAm); generic sections (Military/Diplomatic/Think-tank/News-wire/Defense-journalism/OSINT/Energy-Commodity) untouched (already theater-agnostic, copied to siblings separately by WP-1/WP-2); header + footer notes added pointing Iran/ME → FALCON, Russia/Ukraine → OSPREY. |
| `board_log.tsv` | **Comment line appended** | `# --- 2026-07-12 split: pre-split entries above span both theaters; OSPREY/FALCON log their own from here ---` appended after the existing 66 rows. Log continues (not reset), per the build spec's WP-3 amendment. |
| `OPEN_THREADS_2026-07-09.md` | **Top banner added** | `🧊 SUPERSEDED 2026-07-12 (split)` blockquote, pointing live residue to FALCON SCRATCH (Iran items), OSPREY SCRATCH (Russia items), HAWK STATUS DORMANT BOOK (Taiwan/Venezuela re-sweep — carried forward, not dropped). |

**Not touched (correctly out of WP-3's 14-item scope, verified consistent with the manifests):** `MEMORY.md` (stays live per build spec §3 amendment, HAWK's own, no action needed), `thesis/THESIS.md`/`TIMELINE.md`/`CHANGELOG.md` (already carry — or in THESIS.md's case, already carried pre-split — frozen/superseded framing; FALCON inherited a working copy; noted in CLAUDE.md's FILES table but files themselves left as-is to avoid scope creep beyond the assigned 14 items), `research/RUSSIA_OIL_INFRA_STRIKES_MAY-JUN2026.md` (OSPREY has its own working copy; HAWK's is now historical — noted in FILES table, not re-bannered), `CALENDAR.md`/`TRADE.md`/`REMARK_20260628.md`/`DECK_EVIDENCE.md`/`audits/*`/`domain/sources/*` (already frozen or out-of-scope historical, per Manifest A — no split-specific action needed), `scripts/*` (already git-mv'd out for baghdad_watch.py by DAEDALUS pre-WP-3; remaining Iran-scenario-coded scripts stay frozen in place, noted in CLAUDE.md FILES table).

---

## Deviations from the literal instruction + why

1. **VX.tsv / FLOW.tsv extraction method:** used `sed -n` line-number extraction from the original file rather than manually retyping rows, to guarantee byte-verbatim content per the hard constraint ("never fabricate data"). Verified post-extraction via `cut -f1` that the ID sets exactly match each manifest's row-disposition list before committing to the replacement.
2. **CLAUDE.md EXIT RULES / SCENARIO FRAMEWORK / CONVERGENCE MATRIX sections:** the task's 14-item list didn't explicitly rule on these three CLAUDE.md sections. Removed them entirely (rather than leaving a war-scenario ladder HAWK no longer runs) since the spec is explicit HAWK's job is thin reconciliation, not scenario-holding — kept a lightweight "synthesis-consistency check" as the closeout-11 replacement so the read→write symmetry (boot step ↔ closeout step) isn't broken.
3. **PREDICTIONS_ARCHIVE.md ordering:** inserted HAW-10 in chronological position (between HAW-09 and HAW-11) rather than appending all 5 backfills at the end, for readability; HAW-12/13/14/15 appended after HAW-11 since that was already the file's tail.
4. **No banner added to THESIS.md/TIMELINE.md/CHANGELOG.md/RUSSIA_OIL_INFRA_STRIKES.md**, despite these being logically "dead-ish" surfaces now that FALCON/OSPREY have working copies — left untouched because they weren't in the explicit 14-item list and THESIS.md already self-identifies as superseded; flagged in CLAUDE.md's FILES table instead so a future HAWK session isn't confused, without expanding the edit surface beyond the assigned scope.

## Open items (for DAEDALUS WP-4 verification pass or a future HAWK session)

- HAWK's STATUS/NEXUS_BRIEF are a **mechanical re-cut**, not an independently-verified synthesis session — flagged explicitly in both files' build notes and as SCRATCH NEXT SESSION #1.
- Taiwan/Venezuela dormant-vector content re-sweep is still owed (carried forward from pre-split OPEN_THREADS, not resolved by the split itself).
- FLOW-HAWK-18 (China SPR) disposition question (retire vs. route to ZHAO/BRENT) remains open per the build spec — not resolved in this WP.
- HAW-14's deeper analytical post-mortem (beyond the mechanical archive backfill) remains HAWK-owner-lane, not written this session.
- FALCON's strike-ledger swept-through mark is known-stale (2026-03-19) as of this report — their founding mandate to fix, noted in CROSS_WAR_SUMMARY.md for HAWK's own future closeout checks.

---

## Verification snapshot (self-check, run at report time)

- CLAUDE.md: 235 lines; no `baghdad_watch` boot-step reference remains (only a historical FILES-table pointer); no `SCENARIO FRAMEWORK`/`CONVERGENCE MATRIX`/`EXIT RULES` headers remain.
- STATUS.md: 57 lines (≤120 target).
- `workbook/VX.tsv`: 10 lines (1 split-note + 1 header + 8 data rows).
- `workbook/FLOW.tsv`: 8 lines (1 split-note + 1 header + 6 data rows).
- `workbook/KB.tsv`: split-note prepended, 225 data rows otherwise untouched.
- `thesis/PREDICTIONS.tsv`: preamble re-totaled; exactly 2 `REHOMED` rows (HAW-16, HAW-17).
- `thesis/PREDICTIONS_ARCHIVE.md`: 15 `## HAW-NN` sections present (01-15 inclusive; 16/17 correctly absent — REHOMED, not closed).
- `domain/energy-strikes/STRIKES.tsv` + `SUMMARY.md`: both carry a `FROZEN 2026-07-12` banner pointing to the siblings' ledgers.
- `board_log.tsv`: split-marker comment line appended after the pre-existing 66 rows.
- `OPEN_THREADS_2026-07-09.md`: `SUPERSEDED 2026-07-12` banner present.
- **AGENTS/OSPREY/ and AGENTS/FALCON/ confirmed untouched** (read-only throughout this session).
