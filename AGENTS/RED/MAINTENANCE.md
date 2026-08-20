# RED Maintenance Log

Reverse-chronological log of **structural** changes to RED's docs, folders, schemas, and tooling. Each entry: what changed, why, files touched, boot-impact.

**Distinct from `thesis/CHANGELOG.md`**, which logs **analytical** changes (confidence shifts, hypothesis re-weighting, challenge resolutions, prediction scoring). If a change moves a number or a probability → CHANGELOG. If it moves a *file, schema, or boot path* → here.

**Conventions (adopted from SAM, S16):**
- Archive-next-to-active-doc where practical; `archive/` root holds legacy/superseded.
- Verify-before-archive: confirm content is captured elsewhere before cutting (lossless by construction).
- Loop-closer: when a structural change adds/moves a file, update `CLAUDE.md`'s FILES tables + boot steps in the same pass, so a future RED knows it exists.

---

## 2026-08-20 (S32 closeout) — boot step 5.6 added: GENERAL INBOX SCAN — the lane the boot spec never enumerated

**Trigger:** 18 unprocessed packets found accumulated 8/12–8/20 in `inbox/` top level — including the MI3 primary data the docket carried as "unfetched," two decision asks aging 5 days, and two same-day SAM asks. Root cause structural: the boot sequence enumerated BOARD (1.5) and the retired WALTER lane (5.5) but never the general packet directory; the disposition obligation followed the *enumerated lanes*, not the *delivery directory*. Root-cause-consistent with two independent fleet reads same morning (YEYOU YEY-011: 27 unprocessed elsewhere; WALTER's repaired ACTION telemetry) — per PROME, DAEDALUS's ~9/2 pass has the lane class.

**What changed:** `CLAUDE.md` boot step **5.6** added (read/triage every top-level `inbox/*.md`, disposition in `board_log.tsv` `source=INBOX_GENERAL`, `git mv` to `processed/`, answer superseded packets against CURRENT state). No renumbering — 5.6 slots between existing cited steps. **Boot-impact:** one new read step; the S30 architecture audit graded the boot symmetric without seeing this lane, so the audit's coverage claim was about the enumerated set (`finding_scan_keyed_on_naming_reads_local_form_as_absence` class) — flagged to DAEDALUS in OUTBOX -019.

---

## 2026-08-20 (S32) — FT-10 registered (registry 10 → 11 rows) + boot.py: `cmp_op` four-op dispatch, ^SKEW in TICKERS, SKEW-CBOE in METRIC_MAP

**Trigger:** the SKEW ruling (SIG-20260818-004, action:RED) — registering the tail-bid-reload line surfaced that `boot.py`'s comparator silently evaluated every non-`>` operator as `<` (a `>=` row with data would have printed a SIGN-INVERTED verdict — `>=150` read as `<150` = false FIRING at 142.93; FT-08 was shielded only by being unmapped). ML-RED-178.

**What changed.**
- **`registry/FALSIFICATION_TRIGGERS.tsv`** — RED-FT-10 appended (`SKEW-CBOE >= 150 s=4`, ACUTE +2 / MANAGED −2, exit = the standing <140 s=4 kill line; full basis + base-rate provenance in-row). Append verified: trailing newline pre-checked, whole-file field-count 11/11 rows × 15 cols, zero literal quotes kept (the registry's quote-free state is the only reason csv round-trips ever survived it — ML-RED-168).
- **`scripts/boot.py`** — (1) `cmp_op` rewritten to explicit `>` / `<` / `>=` / `<=` dispatch, unknown op now **raises** instead of silently picking a branch; (2) `^SKEW` added to TICKERS (tape section + FT-10's price source); (3) `SKEW-CBOE` added to METRIC_MAP with the lag note (Yahoo ^SKEW publishes lagged → the tool reads completed sessions — the *inverse* of the FT-06 ^VIX-runs-ahead defect, ML-RED-176).
- **Functional verify both directions:** FT-10 renders 🟢 `clear, live 142.93 vs >=150 (dist -7.07)`; `schema_check.py` exit 0 (10/10 files conform); WATCHLINES ops audited (`<`/`>` only — no watchline hits the new paths).

**Boot-impact:** trigger check now evaluates 9 of 11 registry rows live (FT-08 stays unmapped by design). WALTER notified same-pass — co-signed surface, row addition + the comparator fix both named.

---

## 2026-08-12 (S30) — `archive/` recreated (Will-ruled) + 14 files retired into it + the dead-path pointers repaired (T8 / audit R4+R14)

**Trigger:** Will's ruling — *"RED should have its own archive"* — which unblocked T8. Audit R4 (dead `archive/` paths) + R14 (archive backlog) + PROME's prune-scan delta.

**What changed.**
- **`archive/` recreated** with a `README.md` that records what it is, what was archived, what was **held back**, and why the directory had to be recreated at all.
- **14 files `git mv`'d in** from `challenges/`, `reports/`, `research/` — every one verified unreferenced under **both** a loose and a strict reading of *"referenced by a live doc"*.
- **Dead-path pointers repaired** in `CLAUDE.md` (FILES table) and `MEMORY.md` (a **live markdown link in a boot-read file**), repointed to `git show 1cb18fbc3^:…` rather than left claiming paths that do not exist.

**⚠️ The prune's premise was false, and the pointers outlived the content by six weeks.** `1cb18fbc3` (2026-06-30, *"prune dead 0-ref agent archives, public-prep track A"*) deleted **38 RED files**. Two were demonstrably referenced: **`archive/RED_SKELETON.md`** (cited in `CLAUDE.md`'s own table AND `MEMORY.md`) and **`archive/status_snapshots/STATUS_2026-04-02.md`** (a live markdown link in boot-read `MEMORY.md`). **All 38 remain recoverable at `1cb18fbc3^` — the content was never lost, only the pointers broke.** **The prune is NOT reversed**: it was a deliberate public-prep decision that is not RED's to undo, and restoring any file is a Will/PROME call.

**⚑ THE FINDING, and it inverts the audit's own estimate.** The audit reported *"5 of 5 oldest spot-checked UNREFERENCED."* **True of those five, and badly unrepresentative: a full check of all 33 candidates found 19 REFERENCED (58%).** The cause is structural — **age correlates with reference-status** (old files are old precisely because nothing kept pointing at them), so **ranking by age and sampling the head over-estimates the unreferenced share**. **Acting on the extrapolation would have retired 19 files that live surfaces cite.** Same family as ML-RED-163: *a rate computed on a ranked head is a claim about the head, not the population.* ML-RED-175.

**Held back deliberately:** `challenges/KRE_EXECUTIVE_SUMMARY.md` qualifies on the strict reading but is **one half of the R13 name collision** — two documents sharing a basename with **opposite verdicts** (45% *"WILL LOSE MONEY"* vs `workbook/`'s 75% *"A-"*). **Archiving one half while the other stays live makes the collision worse**: the survivor would carry no signal that a contradicting twin exists. Resolve the collision (T11), then retire.

**Boot-impact: NONE.** No boot step reads `archive/`. `schema_check.py` unaffected (it maps files explicitly). **Retirement backlog after this pass: 19 referenced files stay in place; the >60d rule is now satisfiable because a destination exists.**

---

## 2026-08-12 (S30) — disposition-ledger obligation moved off the retired lane + `boot.py` §⑤ makes it checkable (T10 / audit R6)

**Trigger:** Audit R6 — *"the disposition-ledger obligation stayed attached to the retired lane."*

**The defect.** RED's `board_log.tsv` rule lived in **boot step 5.5**, the `inbox/WALTER/` lane, which went **NO-OP on 2026-07-09** when WALTER granted RED the §3.5 pull-complete exemption. **Boot step 1.5 — the whole-BOARD scan that BECAME RED's sole WALTER channel on that same date — carried no ledger obligation at all.** For 34 days the rule governed a channel receiving nothing while the channel receiving everything was ungoverned. Result: `board_log.tsv` dormant **8/07 → 8/12** while RED consumed **two action-addressed signals** unlogged. ⚠️ **The S29 remedy fixed *running* step 1.5 and not *recording* it — which is why the gap survived its own fix.**

**What changed.**
- **`CLAUDE.md` boot 1.5** now carries the obligation as its canonical home: the row schema, the disposition vocabulary (`acted`/`noted`/`deferred`/`info-only`/`skipped`), `source=BOARD`, and the reason it moved.
- **`CLAUDE.md` boot 5.5** demoted to a forward-pointer rather than deleted — *a reader landing there from an old reference needs to be sent forward, not left with silence.*
- **`CLAUDE.md` boot 9** notes that `boot.py` now grades the obligation.
- **`scripts/boot.py` — NEW section ⑤ `BOARD DISPOSITION GAP`.** Compares the newest BOARD signal **addressed to RED** (`action:`/`info:` header scan, reading only files newer than the last logged disposition) against the newest `board_log` row.

**⚑ Why a CHECK and not just a relocated rule.** A moved rule is still a remembered ritual, and the original failed precisely because **nothing checked it** (`[[finding_mechanize_the_cap_not_the_ritual]]`). **And why NOT a staleness alert, for two independent reasons:** `board_log.tsv` is **excluded fleet-wide** from `ledger_staleness`'s outside-glob warning **by design** (~15 agents carry it at top level; counting it would false-fire across the fleet), **and** age cannot distinguish *"no signals arrived"* from *"signals arrived and went unlogged"* — it would fire every quiet week and stay **silent in the exact failure mode**.

**Verified both directions** (the T2 standard — functionally, not by inspection): clean state prints **🟢 nothing addressed to RED is undispositioned**; reproducing the 8/07 state prints **🔴 27 RED-addressed signal(s) … 3 are action:**. `board_log.tsv` restored byte-identical after the test.

**Boot-impact:** one new section at the end of `boot.py` (~+1s, reads only BOARD files newer than the last disposition). No existing section changed.

---

## 2026-08-12 (S30) — VX.tsv review-or-carry pass + PAT-044 two-clock header closes the staleness blind spot (T7 / audit R9)

**Trigger:** Audit R9 (VX = "the one genuinely stale ledger… silent-rot middle, no banner") + RED's own standing open thread that `ledger_staleness.py RED` ran CLEAN while VX was stale.

**What changed.**
- **`workbook/VX.tsv` — 13 of 25 rows touched: 6 MEASURED (instrument pulled, `Flip_If` graded leg by leg), 7 CARRIED.** Carried rows' `Last_Reviewed` **deliberately NOT bumped**; each carries an explicit `CARRIED` marker naming its owner and the instrument that would move it, plus a 2026-09-12 re-review.
- **VX-RED-013 RETIRED** (`WEAK` → `RESOLVED-SUPERSEDED`) at **129 days**, the oldest row in the ledger: its premise *"Sanctions expire Apr 11"* resolved on 2026-04-11 and the Russia ban now runs to 2027-01-31, so its central contingency expired four months before anyone looked. Retired rather than re-dated — re-dating preserves a live-looking row whose contingency no longer exists.
- **`workbook/VX_HISTORY.tsv` +2 rows** (VX-013 retirement; VX-017 evaluated-no-change, logged because the flip condition was *graded and found ungradeable*).
- **`workbook/CHALLENGES.tsv` — both dangling cross-links cleared** (CHG-RED-024 → `VX-RED-022` + `KB-RED-041`; CHG-RED-027 → `VX-RED-022`). These are the **only** gaps in otherwise contiguous sequences (VX 001-026, KB 001-086) — the signature of an ID **cited in a link whose row was never authored**, not a deleted row. Refs removed from the ref-only link columns; the fact recorded in `Resolution` so the claim is not silently erased.
- **`workbook/VX.tsv` gains a PAT-044 two-clock banner at line 0**; **`scripts/schema_check.py` FILES map updated to `skip=1`** for it (same shape as FLOW.tsv).

**⚑ The staleness blind spot, and the repair site was not where RED had it filed.** The standing thread said *"fix the check, not just the file."* **Right about the diagnosis, wrong about the repair site:** `ledger_staleness.py` has *preferred* an in-content two-clock date since 2026-07-22 and falls back to git-commit time only when none is present — and VX.tsv had none while being committed regularly, so it graded permanently fresh. **The fix needed no shared-code edit and no PROME dependency: write the header.** Set to **2026-06-02, the OLDEST LIVE row's `Last_Reviewed`, NOT the pass date**, so the alert stays lit while 7 live vectors remain carried. **Before: `rc=0`, no VX line. After: `⚠️ STALE +72d … → 1 stale`.**

**Boot-impact:** boot step 9a now surfaces VX as stale (intended). `schema_check.py` still reports **10 of 10 conform**. No boot step parses VX.tsv.

**⚠️ Deferred on purpose, and grouped so it is not lost:** every `Flip_If` threshold in VX needs the `instrument_basis` treatment the falsification registry got in T5 — **VX-017 proved an unlabeled threshold is ungradeable** (three instruments, three answers). That is a threshold change and belongs in its own dated pass, alongside FT-07's `sustain=1` and `VX.Strength`'s strength/lifecycle conflation.

---

## 2026-08-12 (S30) — SCHEMA.tsv refreshed against measured reality + `scripts/schema_check.py` shipped (T6 / audit R8 + DAEDALUS sweep item 3)

**Trigger:** Audit R8 ("a co-signed contract that silently drifted") + DAEDALUS's completeness-sweep rider on `CHALLENGES.Resolved_Date`. **T5 widened the gap** — the registry went to 15 columns against a schema documenting 8 — so T6 could not slip.

**What changed.**
- **`workbook/SCHEMA.tsv` 84 → 111 rows.** Registry block rewritten 8 → **15** columns (the `exit_*` quad, undocumented since 7/29, plus S30's `instrument_basis`/`state`/`action_magnitude`). **`docket/CATALYSTS.tsv` (65 rows) and `docket/WATCHLINES.tsv` (12 rows) gained coverage — they had NONE.**
- **Value domains re-declared against MEASURED usage** in 11 columns. **Disposition split by kind rather than flattened wholesale.**
- **`scripts/schema_check.py` NEW** — read-only structural conformance check, exit 1 on drift.

**DATA fixed (only where genuinely wrong):**
- **KB.tsv `Status` + `Epistemic` case-folded to upper — 50 cells.** `ACTIVE` 31 + `Active` 18 → **49**. The split was *temporally clean* (every row after 7/5 lowercase), so an exact-match consumer **silently dropped the 18 newest live rows while reporting success.** ⚠️ **`Epistemic` was worse than the audit found and was never flagged: 18 distinct values on 85 rows against 3 declared, same case split (`FACT` 4 / `Fact` 7).** Case-only — **proven**: 25 lines changed, **0 of them non-case**.
- **PREDICTIONS.tsv RED-21 `Status` `CORRECT` → `RESOLVED`.** A category error, not a vocabulary choice: correctness already lived in `Outcome` (`"RESOLVED CORRECT. BLS USDL-26-1378…"`). Status domain is now exactly `ACTIVE;RESOLVED`.

**CONTRACT widened (where the vocabulary is legitimately richer — data untouched):**
- **`ML.Thesis_Impact` redeclared Categorical → String.** 4 values declared; **104 distinct on 167 rows**, mostly full sentences. For several rows it is *the only prose record of why a weight moved* — flattening would destroy information. The contract was wrong, not the data.
- **`CHALLENGES.Grade`** — the contract said "letter grade A+ to F" while **40 of 46 rows use the WEAK…COMPELLING strength scale**. Two incompatible scales in one column; strength is canonical, 5 letter-graded rows frozen as pre-05/2026 legacy.
- `CHALLENGES.Status` (12 distinct — `RESOLVED-CONVERGED` encodes a real adversarial-cycle outcome), `ML.Status` (19), `ML.Category` (+`CHALLENGE-GRADE`, `CALIBRATION`), `KB.Status`/`KB.Epistemic`.
- **`CHALLENGES.Resolved_Date`** — DAEDALUS's 5 prose-in-a-date-field rows: **shape documented** (split on first space) rather than the rationale stripped; new prose forbidden.
- **`VX.Strength` conflation DOCUMENTED, deliberately NOT fixed** — 13 values across **two axes** (strength `WEAK…COMPELLING` vs lifecycle `RESOLVED-*`/`FIRED`) on 25 rows. Splitting it is a 25-row migration and belongs in its own dated pass; recorded so the next reader doesn't mistake the mess for meaning.
- **`FLOW.tsv`** — noted that line 0 is the FROZEN banner, so a header-keyed parser reads the banner as the header.

**Boot-impact: NONE** (no boot step reads SCHEMA.tsv). **Verified:** `schema_check.py` reports **10 of 10 files conform exactly and in order**, and was tested **both directions** — induced drift (removed one KB column) → exit **1** with the correct diagnosis; restored → exit **0**.

**⚠️ INCIDENT DURING THIS PASS — a fourth member of the S30 tooling class, and the most dangerous.** The first attempt used `csv.reader`/`csv.writer` on KB.tsv and PREDICTIONS.tsv. **Python's csv module treats a literal `"` inside a TSV cell as field quoting**, so a read-modify-write round-trip **silently rewrote PREDICTIONS RED-08's `Outcome` cell from `"` to `W`** — a row the pass was not editing. **The tell was a diff LARGER THAN THE EDIT: 6 rows changed for a 1-row edit.** Restored via `git checkout` (uncommitted) and redone with raw tab splitting. Quote counts: **ML 36 · CHALLENGES 10 · KB 6 · PREDICTIONS 6**; the registry has **0**, which is the only reason S30's two earlier csv round-trips on it were safe — **verified field-by-field against a pre-change backup, 0 unintended changes.** **Rule now in the checker's docstring: never use the csv module on these TSVs.** ML-RED-168.

---

## 2026-08-12 (S30) — FALSIFICATION_TRIGGERS.tsv re-spec: 12 → 15 columns, 7 UNDEFINED exits closed (T5 / audit R7a-R7b / PROME Amendment 3)

**Trigger:** DAEDALUS audit R7 (a: no instrument-basis column; b: no state column) + PROME Amendment 3 (action-magnitude column) + WALTER's `SIG-W-20260811-002` §5 N5 ask, which converges independently on the same file.

**What changed.** `registry/FALSIFICATION_TRIGGERS.tsv`: **12 → 15 columns.** Added `instrument_basis`, `state`, `action_magnitude`, **inserted after `action`** (positions 7-9); `exit_*` moves from 9-12 to 12-15. All existing columns keep their relative order; no column renamed, no row added or removed (9 rows).
- **`instrument_basis`** — exact series/venue/basis + publication cadence + which date governs the sustain count. **N5 scope stated per row rather than assumed**: cash/derived series (HY OAS, CCC OAS, ICSA, VIXCLS, T5YIFR) say explicitly that N5 (i)/(ii) do not bind them.
- **`state`** — closed set `ARMED` / `FIRING-BANKED` / `FIRED-BANKED` / `UN-FIRED` / `BLOCKED`. Aimed at the banner on WALTER's own `FALSIFICATION_FIRED_LOG.tsv` (*"cite this log ONLY for 'did X ever fire', never for 'is X fired now'"*) — `state` answers the second question in a machine-readable cell.
- **`action_magnitude`** — the pre-registered size, or explicit `NONE` with a reason. Closes ML-RED-144.
- **Exits:** 7 rows moved off `UNDEFINED` (FT-02/03/04/05/07/08/09), all set pre-data. **`UNDEFINED` no longer appears in the file.**

**Files touched.** `registry/FALSIFICATION_TRIGGERS.tsv` (the change) · `STATUS.md` §11 + falsification-table note + priority 0 · `thesis/CHANGELOG.md` (A4-mandated) · `OUTBOX.md` (RED-TO-PROME-...-013) · `NEXUS_BRIEF.md` (2 corrections, in-place, still 100/100 lines) · `workbook/ML.tsv` (ML-RED-159..162) · packets to `AGENTS/WALTER/inbox/` and `AGENTS/BRENT/inbox/` (carve-out ①).

**Boot-impact: NONE, and this was verified functionally rather than by inspection.** `boot.py` is header-keyed (`dict(zip(head,row))`), so column count and position are irrelevant to it; WALTER's step 6b/6c is a human read-loop. Re-ran `boot.py` after the change: **all 9 triggers still evaluate, 15/15 fields on every line, 10 lines total (no embedded newlines).**

**⚠️ LANDMINE FOUND BEFORE IT FIRED — record this, it generalizes.** `boot.py`'s `tsv()` keeps a row only if `len(row) >= len(head) - 2`. **Adding 3 header columns without widening all 9 data rows would have failed `12 >= 13` on every row and printed an EMPTY trigger section — no error, no warning, no exit code**, on the very scan that decides whether a pre-registered falsifier fired. **A parser tolerance written to survive dirty data becomes a silent-failure amplifier under schema change, because the two are indistinguishable to it.** ML-RED-159; promoted to auto-memory.

**Why the columns went mid-file and not appended:** the actual consumption path is WALTER's *human* read-loop, and `state`/`action_magnitude` are useless to a human sitting behind `exit_source`, which on FT-06 is ~1,900 characters. Checked for positional parsers before choosing (boot.py header-keyed; WALTER human; their FIRED_LOG banner states the exit quad is parsed by no code on either side), and **notified WALTER before the change landed** with an explicit offer to move the columns to the end if any positional reader exists on their side.

**Not done in this pass, deliberately:** FT-07's sustain=1 (32.5% base rate) and FT-04's regime-descriptor level (64.5%) are flagged in-row but **not re-cut** — threshold changes belong in their own dated pass, and re-cutting bear-side thresholds in the session the bear lost six points is indistinguishable from moving goalposts. Queued.

---

## 2026-08-12 (S29f) — ADDENDUM CLOSEOUT (W-A) spec added to CLAUDE.md; Amendment 10 reconciled

**Trigger:** DAEDALUS audit R2 (root cause of R2/R3) + PROME's sequencing guidance + RED's own per-ending self-audit of 2026-08-12.

**What changed:** `CLAUDE.md` gains a **§ADDENDUM CLOSEOUT (W-A)** block after W10, running at **every session ending after the first in the same day**. 3-step always-floor (A1 STATUS addendum · A2 SCRATCH addendum · A3 commit+push) + 6 conditionals each keyed to a checkable FACT, of which **A4 is load-bearing**: *any* weight / confidence / registered-trigger-state change makes **W3 and W8 MANDATORY**. Plus a one-question self-check with the explicit rider that **"they already know via another route" is not routing**.

**⚠️ Amendment 10 RECONCILED, not overridden:** *"the NEXUS_BRIEF fold goes LAST"* is now **per-ENDING, not per-day**. It was authored for single-ending sessions and is self-refuting in a multi-ending one — on 8/12 the brief declared itself folded-last while four further endings and several commits followed. NEXUS_BRIEF footer updated to flag the revision.

**Evidence base (measured, in the spec):** S29 ended five times; each addendum ran ~3 of 10 W-steps; **W8 skipped 4-of-4, W3 3-of-4**. The repair became its own session (T14).

**Boot-impact: NONE on boot** — this is a write-back-side addition only; boot steps 0-9a unchanged. Sessions that end once are unaffected. **Fleet:** DAEDALUS holds this as a PAT candidate (RED validates, fleet inherits after one clean multi-ending day = audit L5 gate (a)).

**Immediate catch by the new rule:** A4 run against 8/12's own record found the **S29d Policy Rescue 2→4 / Managed 34→32 move had never reached `thesis/CHANGELOG.md`.** Entry written same session with its lateness disclosed rather than backdated.

---

## 2026-08-12 (S29d/e) — DAEDALUS audit + PROME amendments: FT-08 machine form corrected, FT-09 wired into boot.py, WAL V4 docket row added

**Trigger:** `AGENTS/DAEDALUS/upgrades/RED_AUDIT_2026-08-12.md` (18 findings, Will-directed) + PROME's three amendments (durable record in DAEDALUS's inbox; relayed to RED as an addendum packet) + PROME's prune-scan R4 delta packet.

**What changed:**
1. **`registry/FALSIFICATION_TRIGGERS.tsv` — FT-08 machine form CORRECTED (audit R7c).** Was `CORE-CPI-MOM >= 0.4, sustain 1` with the AND-leg (3-mo ann ≥3.0%) stranded in the notes column *beside the sentence explaining why single-leg firing is noise*. boot.py and WALTER read machine columns only → **the row fired on exactly what its own registration forbade.** Now `CORE-CPI-3MO-ANN >= 3.0, sustain 1` — the 3-month annualized figure **is** the conjunction as one machine-readable quantity, so no consumer can fire a half-test. Instrument basis written into the row (R7a). Defect was self-created ~3h after ML-RED-144 diagnosed the class.
2. **`scripts/boot.py` — `T5YIFR` added to `FRED_SERIES` + `METRIC_MAP` (audit R17, promoted to hours-tier by PROME amendment 2).** FT-09 was 24bps from firing while rendering `unmapped metric, manual check`. **`CORE-CPI-3MO-ANN` deliberately left unmapped** — a release-derived 3-month compound has no FRED series and failing loud is correct for it; recorded as a decision, not an omission.
3. **`scripts/boot.py` — numeric precision fixed in two formatters, a defect introduced by change 2 and caught before commit.** Thresholds printed at `.0f` rendered FT-09's 2.55 as **`>3`** (a 24bp-away line displaying as 69bp-away), and the FRED tape printed `2%` for 2.31%. Evaluation was correct throughout; only display rounded. Thresholds now print at registered precision (2dp when sub-100 and non-integer, else integer); tape at 2dp for sub-100 series. **Regression-verified: HY 272bps / CCC 1,023bps / claims 199K unchanged.**
4. **`docket/CATALYSTS.tsv` — WAL V4 row added for 8/13 (audit R5).** Named the next binding test in four narrative surfaces with no docket row; boot.py §3 iterates `status=pending` only, so **the T-1 catalyst RED called binding would not have printed.** Verified now printing ⏰ T-1. Violation of RED's own W4 mirror rule.

**Boot-impact:** §① tape gains a `5y5y Breakeven` row; §② now evaluates FT-09 live (**8 of 9** hard triggers auto-evaluated, up from 7 — FT-08 stays manual by design). CLAUDE.md:59's full-coverage claim is closer but still not literally true; queued with the hygiene batch.

**DEFERRED, deliberately, per PROME's sequencing:** R3 dispute-marking **HELD for BRENT's basis ruling** (one relabeling pass after the ruling, not a marking pass before it — the four existing ⚠️ marks stay); **amendment 3's ACTION-MAGNITUDE column** and R2/R7b/R8/R9/R4/R10-R18 → **dedicated hygiene session.** Absorbing an 18-finding list into a live catalyst day is the R2 failure mode itself.

---

## 2026-08-12 (S29) — two NEW registry triggers (FT-08 core CPI, FT-09 5y5y breakeven); FT-06 fired and exposed a magnitude spec-gap; KB-RED-067 doubly corrected

**Trigger:** S29 write-back (W4/W6/W9) on a live catalyst day + PROME packet `2026-08-11_from-PROME_forum4-close-weights-inputs-and-corrected-references.md` (MIDAS DFII10 flag) + DAEDALUS packet `2026-08-11_..._weekday-range-guard-shipped`.

**What changed:**
1. **`registry/FALSIFICATION_TRIGGERS.tsv` — 2 rows APPENDED, 1 row updated.** **RED-FT-08** (`CORE-CPI-MOM >= 0.4`, sustain 1, action `STAGFLATION-RE-ARM`, +3 — compound: also requires 3-mo annualized ≥3.0%) and **RED-FT-09** (`BREAKEVEN-5Y5Y > 2.55`, sustain 5, action `EXPECTATIONS-UNANCHOR`, +4). Both registered **PRE-DATA** so the S29 −6 Stagflation move reverses on registered lines rather than by argument. **RED-FT-06 marked FIRED** (8/11 close).
2. **⚠️ Registry spec-gap DISCLOSED, not silently patched: FT-06's `action` column named a DIRECTION but no MAGNITUDE** (`MANAGED-DECLINE-CONFIRM`), unlike FT-01 (−2) and the SKEW kill (−2). The −2 was set **post-data** by analogy and is labelled as such in STATUS, the registry notes, CHANGELOG, OUTBOX and NEXUS_BRIEF. **Structural follow-up owed: audit the whole registry for other direction-only actions before the next one fires** — the hole is invisible until a trigger fires. Logged in SCRATCH NEXT SESSION #3. ML-RED-144.
3. **`workbook/KB.tsv` — KB-RED-067 CORRECTED on two axes** and `Stale_By` pushed 2026-08-15 → 2026-09-15. (a) the dead **"DFII10 series high" label** (post-2024 / ~2.75-yr high; all-time 3.15 [11/2008]; owner **BOND**) — flagged by MIDAS via PROME; (b) a **stale LEVEL** nobody flagged (2.37-2.39 vs an actual **2.43 [FRED 8/10]**), found only as a side effect of chasing the label, three days before its own Stale_By. **The same string in `thesis/CHANGELOG.md`, `workbook/ML.tsv`, an outbox packet and `research/FOMC_FRAMEWORK_JUL28-29_2026.md` was DELIBERATELY LEFT INTACT** — those are dated historical records, and rewriting them would damage an accurate account of what was believed when (same principle as the S28 `claim_check` false-positive ruling). ML-RED-149.
4. **`docket/CATALYSTS.tsv`** — rows 48 (July CPI) and 58 (FT-06) resolved with outcomes; **3 forward rows appended**: ~8/17 CARL V2 on OTTO's 10-D panel · Fri 9/11 Aug CPI (RED-FT-08's first live test) · Nov 2026 HHDC (CHG-RED-045 resolution).
5. **`workbook/CHALLENGES.tsv`** — **CHG-RED-045** opened (CARL HHDC kill-rule, resolves Nov HHDC).
6. **Auto-memory:** 1 NEW (`finding_hypothesis_needs_an_instrument_for_its_defining_mechanism`) + **2 EXTENDED IN PLACE** rather than created — `finding_prereg_verdict_boundary_must_be_a_number` (the ACTION-magnitude half of the same defect) and `finding_standing_guard_is_a_false_negative_risk` (the scoped-exemption-read-wider form). **Dedup-before-create honoured: 3 findings, 1 new index row**, against a MEMORY.md sitting at 72% of its byte cap. Edits done in-place via python to preserve the harness hardlinks (verified: inode unchanged).

**Boot-impact:** `boot.py` §2 now evaluates **9** registry triggers instead of 7 — **verified by running it after the edit, not assumed.** FT-08 and FT-09 are not in `boot.py`'s metric map, and it degrades correctly: both render **`⚪ RED-FT-0x <METRIC> — unmapped metric, manual check`**, which is an explicit instruction rather than a silent `n/a`. **They must be graded MANUALLY** — FT-08 at the Fri 9/11 CPI release, FT-09 on the daily breakeven check (FRED `T5YIFR`) — **until someone wires `T5YIFR` into the `FRED_SERIES` map**; `CORE-CPI-MOM` is a release-derived MoM figure and is probably not worth wiring at all. Recorded as a known, correctly-signposted gap. ⚠️ **Also observed on the same run: FT-06 renders `FIRING … sustain '5' needs trail/judgment`** — its VIX source is the live price feed, which carries no close-trail, so boot.py **cannot auto-count a sustain window for it.** That is why this session's fire was graded by hand against FRED `VIXCLS` closes; **do not read boot.py's FT-06 line as a completed sustain count.** Boot steps and CLAUDE.md FILES tables otherwise unchanged; no files created, moved or retired.

---

## 2026-08-07 (S28) — CATALYSTS.tsv blank-row repair + 4 forward rows; NEXUS Amendment 10 brief-fold ordering adopted

**Trigger:** S28 write-back (W4/W9) + PROME fleet-propagation packet `2026-08-04_from-PROME_nexus-amendment-10-brief-fold-ordering.md`.

**What changed:**
1. **`docket/CATALYSTS.tsv` — pre-existing blank row removed** (was line 40 in the committed file, confirmed against `git show HEAD:`). It predates this session; found when a schema check threw on it. File is now 60 rows, all NF=9. *A blank row is invisible to eyeball review and throws any strict TSV reader — worth the 5-second check at every write-back.*
2. **4 forward rows added:** `2026-08-11` FT-06 earliest completion (with the DIET-guard disposition **pre-decided before the print**) · `2026-08-19` July FOMC minutes (makes LABOR's 7/29 grade final) · **`2026-08-21` CHG-027 HARD BACKSTOP** (self-imposed; carries its own declared failure mode) · `2026-08-28` QCEW preliminary benchmark (largest scheduled labor risk in the window).
3. **Two rows re-statused:** the `2026-08-04` BDC cluster row → **`BLOCKED`** (printed but never graded — see CHANGELOG S28 ⑥); the `2026-08-07` CHG-044 amendment window → `resolved` (closed with no response, explicitly not scored as vindication).
4. **`registry/FALSIFICATION_TRIGGERS.tsv`** — FT-01 `exit_source` rewritten for the re-fire + composition adjudication; **FT-06 `exit_source` now carries the broken-streak-resets ruling** so the semantics live with the trigger rather than only in STATUS prose. **`docket/WATCHLINES.tsv`** — WL-03 re-armed as FT-01's live exit.
5. **NEXUS Amendment 10 ADOPTED:** the `NEXUS_BRIEF.md` fold is now the session's **LAST** write-back — after the final STATUS write, immediately before git commit (checkable form: brief commit timestamp ≥ STATUS commit timestamp). Executed that way this session. *Rationale worth keeping: the 7/31 fleet audit found 5-of-5 content-stale briefs had refreshed and then kept working — refreshing is not the fix, ordering is.*

**Files touched:** `docket/CATALYSTS.tsv`, `docket/WATCHLINES.tsv`, `registry/FALSIFICATION_TRIGGERS.tsv`, `NEXUS_BRIEF.md`, `MAINTENANCE.md`.

**Boot-impact:** `boot.py` DUE-scan and catalyst countdown now surface the 8/11 / 8/19 / 8/21 / 8/28 rows; the BLOCKED status makes the ungraded BDC gate visible at boot instead of reading as a benign pending row. No schema or boot-path change — `CLAUDE.md` needs no edit.

## 2026-07-24 (S25, evening) — FOMC framework versioned to v1.1; docket re-anchored ±2 months; KB.tsv stray blank line removed

**Trigger:** CARL inbox packet falsifying a load-bearing premise in `research/FOMC_FRAMEWORK_JUL28-29_2026.md` (shipped ~6h earlier in S24) + LABOR packet correcting a docket date + adding a fleet-unowned FOMC leg.

**What changed (structural only — analytical content in `thesis/CHANGELOG.md` 2026-07-24 S25):**

| File | Change | Boot-impact |
|---|---|---|
| `research/FOMC_FRAMEWORK_JUL28-29_2026.md` | **Versioned v1.0 → v1.1.** Added §0 (correction + evidence table), §0b (CHG-028 three-rung re-spec), §L (oil-language sub-axis), §LAB (labor-language sub-axis), Guards 6-7. **Corrections are struck-and-marked in place, not silently rewritten** — v1.0's priors remain readable so the amendment can be graded separately. | None (research/, not boot-read). Execute on 7/28-29. |
| `docket/CATALYSTS.tsv` | KFRC row re-dated **8/04 → 7/27**; July-CPI row re-specced to a pre-registered non-event (priority 🔴→🟠); **5 rows added** — Aug CPI **9/11**, Sept CPI **10/14**, Oct CPI **11/10**, ECI **7/31**, Sept FOMC **9/15-16** (added as `[DATE EST]`, all verified later the same session — see below). | boot.py catalyst countdown now surfaces KFRC at T-3 instead of missing it; ≤14d window gains ECI. |
| `STATUS.md` | CHG-028 row rewritten; priorities 1/6 rewritten, 7-8 added; scorecard 2→3 ACTIVE; missing-data gains a date-verification block. | Still <200 lines. |
| `workbook/` | ML-RED-110…115 (6); KB-RED-070…076 (7); PREDICTIONS RED-21; CHALLENGES CHG-028 row updated in place (Status → `LIVE-RE-ANCHORED`). | — |
| `workbook/KB.tsv` | **Hygiene: removed a stray mid-file blank line (old line 55, between KB-054 and KB-055).** Pre-existing and committed — confirmed via `git show HEAD:` before touching, so it was not introduced this session. A 0-field row breaks naive TSV parsers. | Removes a silent-fail risk in any future KB reader. |
| `board_log.tsv` | 5 dispositions logged; 5 packets `git mv`'d to `inbox/processed/`. | Inbox empty again. |

**✅ Follow-up CLOSED same session (S25b, Will-directed) — and it mattered: 3 of the 4 CPI dates were wrong.** Verified vs the **OMB/White House PFEI CY2026 schedule** + usinflationcalculator (independent 2nd) + federalreserve.gov. **July CPI = Wed 8/12 (the fleet, including me, carried 8/13)** · Aug = **Fri 9/11** · Sept = **Wed 10/14** · Oct = **Tue 11/10 ✅** · Sept FOMC = **9/15-16 ✅, carries an SEP** · ECI = **Fri 7/31 ✅**. All `[DATE EST]` markers removed from the docket; framework → **v1.1a**; correction packet routed to HENRY/CARL/PROME + `outbox/2026-07-24_to-FLEET_cpi-calendar-correction-july-print-is-8-12.md`.

**🔧 Tooling finding (fleet-relevant, KB-RED-077):** **`bls.gov` returns HTTP 403 to WebFetch *and* to curl with a full browser UA** — the usual user-agent workaround does not work. Use the **OMB PFEI CY2026 PDF as the accessible primary**, and extract it with **`pdftotext -layout`**; plain `pdfminer.extract_text` scrambles the month-grid into unusable fragments.

**📋 Process rule adopted:** **verify a date in the same pass that creates the dated row.** I created five `[DATE EST — verify]` rows and deferred verification to "next boot" — the ML-RED-064 MI3 failure mode exactly, missed by one day only because Will redirected. A row marked "verify later" is a row that will be cited before it is verified.

**⚠️ Fleet hygiene flagged to PROME (not RED's to fix):** **PROME has two live inbox paths** — `PROME/inbox/` and `AGENTS/PROME/inbox/` — both receiving traffic from different agents on the same day, with root `CLAUDE.md` asserting the second doesn't exist. Delivered to both; needs a precedence ruling.

**Not changed:** no hypothesis weights, no confidence, no VX vectors (checked — none of this session's data touches a vector's `Flip_If`). `CLAUDE.md` unchanged (no new boot step; the framework was already a `research/` artifact).

---

## 2026-07-24 (S25, late) — ⚠️ CROSS-DIR: `AGENTS/PROME/` migrated and removed on Will's explicit instruction

**Logged here even though it is outside RED's tree**, because a future RED reading `git log` will find RED commits touching `PROME/`, `AGENTS/WALTER/` and `AGENTS/DEWEY/` and needs to know why that was authorized.

**Trigger:** RED's S25 hygiene flag (PROME had two live inbox paths receiving traffic from different agents the same day) → Will ruled in-session: *"PROME uses PROME/inbox — kill the AGENTS/PROME one"*, then *"tell PROME to fix BOOT.md step 6."*

**Authority:** Will, explicit, per-instance. **This is not a precedent** — root CLAUDE.md's "never write outside your own dir" stands; the carve-out here was a direct operator instruction, and the self-authored-packet carve-out covered the notices.

**What was actually there — the reason this wasn't a one-line delete:** **55 files**, including **5 live unprocessed packets** (2× DEWEY 7/24, 1× WALTER 7/24, 1× RED, + WALTER signal `SIG-W-20260724-006` written 2026-07-24T23:55Z, still `written_not_delivered_pending` in WALTER's own delivery log).

| Content | Destination | Commit |
|---|---|---|
| 5 live unprocessed | `PROME/inbox/` (flat, top level — unmissable at boot) | `46d79cd8` |
| 16 `inbox/processed` + 33 `WALTER/processed` | `PROME/archive/AGENTS_PROME_LEGACY_2026-06-24/reaccumulated_2026-06-25_to_07-24/` + README | `46d79cd8` |
| `.claude/settings.local.json` — **gitignored**, so git history would NOT have preserved it | copied to that archive as `PRESERVED_settings.local.json.txt`, then `gio trash` (no `trash`/`trash-put` binary on this box — root rule 11 honoured via the available tool) | `46d79cd8` |
| Notices to WALTER / DEWEY / PROME | their `inbox/` dirs, per the self-authored-packet carve-out | `46d79cd8`, `8a84190a` |

**★ The finding worth keeping, not the deletion:** `AGENTS/PROME/` **had already been archived on 2026-06-24 — and regrew to 55 files in one month**, because ~30 rows of WALTER's `routed/delivery_log.tsv`, DEWEY's routing, and **PROME's own `BOOT.md` step 6** all still pointed at it. *Deleting a dead shared path does nothing; the writers are the root cause.* RED flagged all three owners and edited none of their files. **Promoted to auto-memory** (`finding_dead_path_regrows_unless_senders_repointed`).

**Also flagged, not fixed (owners' calls):** `PROME/CLOSEOUT.md:24` carries the same stale claim as BOOT step 6; `PROME/GIT_COORDINATION.md` lines 34/131/142 read *more* correctly post-deletion and must **not** be swept by a find-and-replace; the preserved settings file granted a bare `Bash(git *)` that PROME's live settings lacks.

**Boot-impact on RED:** none. Watch item added to SCRATCH OPEN THREADS: **if `AGENTS/PROME/` reappears, that is the sender-routing regression, not a delivery surface.**

---

## 2026-07-24 — NEXUS_BRIEF refresh hardened into W8 (was un-listed in the write-back sequence; sat one session stale)

**Trigger:** Will asked at S24 close whether RED's `NEXUS_BRIEF.md` had been updated today — it hadn't (stamped 7/17/S23), despite its own footer promising per-closeout freshness. Root cause: the brief was stood up 7/6 (PROME/NEXUS ask, `inbox/processed/2026-07-06_from-PROME_via-NEXUS_write-nexus-brief.md`) but was never added to the SPAWN PROTOCOL's W1-W10 write-back list, so the S24 closeout — which ran every listed W-step — skipped it cleanly. A checklist can only protect what's on it.

**What changed:** `CLAUDE.md` W8 now includes "Refresh `NEXUS_BRIEF.md` whenever state moved this session"; also folded the root-canon self-authored-packet carve-out (ratified 7/23) into W8's "never write into another agent's directory" line, which had gone stale against root CLAUDE.md. Brief itself rewritten to vS24 in the same pass.

**Files touched:** `CLAUDE.md` (W8), `NEXUS_BRIEF.md` (vS23→vS24), this file.

**Boot-impact:** none at boot; write-back gains one conditional step. Skip-condition is explicit: a session that moved NO state (pure read/verify session) may leave the brief untouched — the footer stamp then honestly shows the last state-moving session.

**Trigger:** WALTER notice `inbox/2026-07-09_from-WALTER_pull-complete-exemption.md` (Will-approved design-walkthrough 7/9) — RED added to BOARD_CONSUMPTION_SPEC §3.5 v0.8 alongside CARL: boot step 1.5's whole-INDEX BOARD scan already IS RED's complete pull (auto-cc INFO-only, never ACTION owner on a WALTER dispatch → zero ACTION-miss risk from dropping the per-signal handoff lane, which was 24% of delivery-lane volume and the largest unconsumed-INFO pile).

**What changed:** `CLAUDE.md` step 5.5 rewritten — WALTER stops writing to `inbox/WALTER/`; the step is now a no-op / cheap empty-check rather than live intake. Step 1.5 corrected 10→12 cluster sections (CLIMATE_MACRO added 6/28, missed in the original count). Drained the pre-exemption backlog same session (8 files: `board_log.tsv` rows + `git mv` to `processed/`) before the lane went dormant.

**Boot-impact:** step 5.5 no longer needs a live glob-and-disposition pass each boot; step 1.5 is now the sole WALTER-signal channel. Friction → log here if `inbox/WALTER/` ever gets a stray post-exemption file (should route to `walter_doctor` as a to-ARCHIVE flag per WALTER's own doctor script).

---

## 2026-07-05 (Session 22) — 12-day catch-up: board_log.tsv created, 98-signal inbox drain via workflow, 6/26 partial-closeout swept, FLOW frozen

**Trigger:** Will-directed 12-day catch-up (last full closeout S21b 6/23). A **6/26 partial session** had filed CHG-RED-041 + its challenge report but never updated STATUS/SCRATCH/CALENDAR/CHANGELOG (left anchored 6/23) — swept this session.

**(1) `board_log.tsv` created (v0.2 schema).** First WALTER-lane delivery log for RED (`timestamp_read / signal_id / disposition / source / notes`). 98 backlogged `inbox/WALTER/` signals triaged via a background **Workflow** (10 agents, batches of 10, structured-schema classification: 0 ACTION / 26 moves-weight / 66 watch), then bulk board_log'd + `git mv`'d to `processed/`. Commit `4917ea0e`.

**(2) Workflow `args` gotcha (tooling lesson).** The Workflow tool delivered `args` to the script as a JSON-**encoded string**, not an array (`files.slice().map` threw on the string). Fix: defensive `Array.isArray(args) ? args : JSON.parse(args)` atop any workflow taking `args`. First run failed 0-agents; second succeeded.

**(3) Pre-commit sanity caught a concurrent NEXUS session.** During the drain, `git diff --cached` surfaced 3 foreign-staged NEXUS files + HEAD had moved to a PROME commit since boot = an active concurrent NEXUS+PROME session. Pathspec commits (`git commit AGENTS/RED/…`) correctly excluded all of it. **Push held (Will-coordinated)** — do not sweep-push while NEXUS is mid-flight.

**(4) FLOW.tsv FROZEN.** +87d stale behind STATUS (ledger_staleness flag). Prepended a `# FROZEN 2026-07-05` banner (audit-only, Apr-vintage rows); STATUS/VX/CHALLENGES are canonical for live break-pathway logic.

**(5) CATALYSTS date corrections.** WAL Q2 re-dated ~7/16 (was 7/30 — REGINALD, 2wk earlier); OZK 7/21 pinned; +3 rows (30Y auction 7/9, EGBN 7/22, DISH-rebalance 7/31 mechanical-CCC trap).

**Boot-impact:** `board_log.tsv` is new (boot step 5.5 now has a log to append to). `inbox/WALTER/` top-level empty again. FLOW frozen (staleness alert clears). No schema/boot-path changes. KB +7 / ML +3 / VX 3-reviewed / CATALYSTS +3.

---

## 2026-06-23 (Session 21 + 21b) — Crash recovery + 40-signal WALTER inbox sweep + CRLF tooling lesson

**Trigger:** S21 session (6/23 ~8:38 PM) crashed mid write-back; Will then directed a chunked sweep of the WALTER inbox backlog.

**(1) Crash recovery (no data loss).** The crash hit during the *atomic rename* of STATUS.md (write-to-temp → rename never landed). Recovered by completing the interrupted write from the `.tmp.<pid>` atomic-write temp (lost exactly one edit — the Brent/OVX 6/23 counter-signal row). HEAD object-integrity clean (no repeat of the SAM 6/22 git-corruption); fleet tree clean. Commit `74af4477`. Crash temp parked in session scratchpad (redundant once STATUS recovered).

**(2) WALTER inbox fully drained — 40 signals → `inbox/WALTER/processed/`.** Processed in 5 themed chunks (A banks/credit 5 · B oil/Hormuz 11 · C FL/housing 5 · D Japan/FX/rates 5 · E positioning/consumer 12), each git-mv'd and committed separately (`3bac8c26`/`2928a378`/`5a144add`/`4ec9ffb2`/`0477eae6`). Analytical content → `thesis/CHANGELOG.md` (NO weight change; 3 residuals). `inbox/WALTER/` top-level now empty; processed/ holds all 40.

**(3) CRLF tooling lesson (boot-relevant for any TSV editor).** RED's workbook/docket TSVs are MIXED line-endings: VX.tsv, KB.tsv, CATALYSTS.tsv, CHALLENGES.tsv are **CRLF**; ML.tsv, VX_HISTORY.tsv are **LF**. A Python *text-mode* read/write silently converts CRLF→LF across the WHOLE file → destructive whole-file diff + merge risk on the shared branch (hit once on VX.tsv mid-sweep, caught pre-commit via `grep -c $'\r'`, restored from HEAD, re-applied in **binary mode** preserving `\r`). **Rule: edit CRLF TSVs in binary mode (split on `b"\n"`, preserve trailing `b"\r"`); `printf`-appended rows (LF) into CRLF files are non-destructive (clean +N) and fine.** Promoted to auto-memory `finding_crlf_textmode_tsv_flip`.

**Boot-impact: neutral.** No file added/moved/renamed structurally; STATUS/SCRATCH/CHANGELOG/CALENDAR refreshed in place; 6 KB + 5 ML + 3 catalyst + 1 challenge rows appended, VX-025 refined. Next boot's BOARD-consumption pass finds inbox/WALTER/ empty (all 40 filed).

---

## 2026-06-02 (Session 16) — SAM-pattern adaptations: CATALYSTS.tsv backbone + this MAINTENANCE log + boot-slim

**Trigger:** Will — "other agents developed meaningful structure; adapt some for RED." Studied SAM; adopted three patterns.

**(1) New `docket/CATALYSTS.tsv`** (structured forward-catalyst backbone, adapted from SAM `docket/CATALYSTS.tsv`). 28 forward catalysts (imminent→Dec), 9 cols: date / window / event / bear_signal / bull_signal / red_threshold / priority / status / notes. **Now the queryable source of truth for catalyst dates/thresholds** (row-by-row prunable — the fix for *why* CALENDAR went stale: prose tables are hard to update incrementally).
- **`CALENDAR.md` slimmed:** removed the IMMINENT + IMMEDIATE + NEAR-TERM + MEDIUM-TERM date-tables (~85 lines, migrated to TSV) → replaced with a pointer + top-imminent summary. **Also dropped a genuinely stale "IMMEDIATE (May 22-29)" section** (already-past events: Tokyo CPI 5/22, calibration retro 5/25, AFT 5/28, OZK 5/29). CALENDAR keeps the narrative layer: RESOLVED history, FALSIFICATION WATCH, scoring windows, exit backstops.

**(2) New `MAINTENANCE.md`** (this file, adapted from SAM `MAINTENANCE.md`). Splits structural-change logging out of `thesis/CHANGELOG.md` (which was carrying both). Going forward, file/schema/boot changes log here.

**(3) Boot-slim `MEMORY.md`** (adapted from SAM boot-slimming discipline). MEMORY's methodology section had grown to multi-hundred-word bullets read in full every boot. Moved the verbose bodies to `MEMORY_ARCHIVE.md` (lossless), kept one-line lesson + `→ MEMORY_ARCHIVE.md#anchor` pointer inline. Load-bearing lessons stay scannable at boot; full depth one pointer away.

**(4) Loop-closer — `CLAUDE.md` updated** so future-RED finds the new structure: boot step 3 now scans `docket/CATALYSTS.tsv`; boot step 4 notes structural changes live here not CHANGELOG; Core-Files table updated (MEMORY = one-liners + archive; CALENDAR = narrative layer; CATALYSTS.tsv added); new "Reference/archive" table rows for `MAINTENANCE.md` + `MEMORY_ARCHIVE.md`. (Did NOT touch the 3 separately-flagged charter items — dual PREDICTIONS, RED_SKELETON refs, TIMELINE staleness — those await Will.)

**Boot-impact: positive** — CALENDAR ~150→88 lines (15.7→11.3KB); MEMORY 35.7→17.6KB (−50%, methodology bodies → MEMORY_ARCHIVE.md); combined RED-owned boot read ~73→~51KB. CATALYSTS.tsv read selectively (status=pending next ~14d), not in full.

**Also this session (logged in `research/STALENESS_AUDIT_2026-06-02.md`, summarized here for the structural record):**
- **Repaired missing `.venv`** (didn't exist; `python3 -m venv --without-pip` + get-pip bootstrap + `pip install yfinance requests`). Market tool live again. NOTE: `.venv` is gitignored; proper fix is `sudo apt install python3.12-venv` (needs Will's sudo).
- **Dedupe:** removed 5 md5-identical `archive/`↔`challenges/` copies (kept challenges/).
- **Relocated** completed VIOLET skew-recheck bundle (10 files incl 1.78MB CSV) → `archive/violet_skew_recheck_apr2026/`; 3 old-format TSVs → `archive/superseded_workbook/`; loose HAWK signal → `inbox/processed/`.
- **Schema fix:** normalized 2 ragged `workbook/KB.tsv` rows (12/14-col) → all 42 rows uniform 13-col.

---

## 2026-06-02 (Session 16, cont.) — retired the duplicate/contradictory `thesis/PREDICTIONS.tsv`

**Trigger:** Will — "take a look at Predictions." Investigation of the dual-file flag (audit §C item 1).

**Finding:** `thesis/PREDICTIONS.tsv` wasn't just stale — it was the **unreconciled pre-ML-RED-068 fork** with *contradictory IDs*. It numbered the May predictions RED-11–14 (conflicting with canonical, where RED-11–14 = the Apr-18 batch and the May predictions = RED-16–19), and was missing the Apr-18 batch + RED-15–19 entirely (14 rows, ragged 6/7-col, last touched May 17). The Session-14 ML-RED-068 cleanup reconciled STATUS/MEMORY/CALENDAR but **missed this file.**

**Fix (lossless):**
- `git mv thesis/PREDICTIONS.tsv → archive/superseded_workbook/PREDICTIONS_thesis_unreconciled_PRE-ML-RED-068.tsv` (verbatim preserved). Verify-before-archive: confirmed `workbook/PREDICTIONS.tsv` is a complete superset (RED-01–19, uniform 10-col) and the only genuinely-unique content (BRENT v2.0 challenge-rationale phrasing) lives in `CHG-RED-024` / `challenges/BRENT_V2_CHALLENGE.md`.
- New breadcrumb `thesis/PREDICTIONS_README.md` — points to the canonical file + warns against re-forking.
- **`CLAUDE.md` updated:** removed `thesis/PREDICTIONS.tsv` from the Thesis-Directory table; added a callout that `workbook/PREDICTIONS.tsv` is sole canonical.

**Resolves:** charter-flag item 1 (dual PREDICTIONS). Remaining flagged items: RED_SKELETON refs in CLAUDE.md; `thesis/TIMELINE.md` staleness.

---

## 2026-06-02 (Session 16, cont.) — cleaned up retired `RED_SKELETON.md` references in CLAUDE.md

**Trigger:** Will — "look at the RED_SKELETON references" (audit §C item 2).

**Finding:** `RED_SKELETON.md` was retired Apr 5 (superseded by `workbook/VX.tsv`), but `CLAUDE.md` still cited it as a **live** reference in 3 places — "Reference for deep work," "Rebuild when time permits," and an anti-pattern — risking a future RED consulting or rebuilding a **Feb-12-vintage** file (per-agent counter-evidence registry incl. a stale agent roster: CREED, old MARCO framing). Verified VX.tsv (per-target vectors) fully supersedes its counter-evidence content; nothing unique to salvage.

**Fix:**
- `CLAUDE.md`: removed the `RED_SKELETON.md` row from the WHAT YOU READ table; removed the "Reference (not boot-critical)" subsection and re-filed it under **Archive** as `archive/RED_SKELETON.md` **RETIRED** (do-not-rebuild); generalized the anti-pattern to "don't trust stale registry data — verify VX/KB `Last_Reviewed`/`Stale_By`."
- `MEMORY.md`: corrected the Apr-5 "DELETED" note (archived copy retained; CLAUDE.md mentions cleaned up).
- `archive/RED_SKELETON.md` itself kept as historical record (correctly placed).

**Resolves:** charter-flag item 2. **Remaining flagged item:** `thesis/TIMELINE.md` staleness (Apr 20, predates channel-migration).

---

## Pre-S16 (retroactive note)

Before S16, structural and analytical changes were both logged in `thesis/CHANGELOG.md`. Earlier structural history (folder reorganizations, the Apr 5 RED_SKELETON deletion, workbook 7-col→14-col migration, the May WALTER LIAISON file instantiations) lives in `thesis/CHANGELOG.md`, `MEMORY.md` "Cleanup Done" notes, and git history. This file starts the clean separation.

---

## STANDING HYGIENE CHECKLIST (run periodically — candidate for a future maintenance-steward sub-agent)

- [ ] `workbook/VX.tsv` — review each vector's Last_Reviewed; flip/resolve any whose Flip_If fired; log to VX_HISTORY.tsv. (S16: was 7 weeks stale — don't let it recur.)
- [ ] `workbook/KB.tsv` — review entries past Stale_By; supersede point-in-time facts overtaken by events; extend live themes.
- [ ] `docket/CATALYSTS.tsv` — prune resolved (status→resolved + move to CALENDAR RESOLVED), add upcoming, refresh thresholds vs live anchors.
- [ ] `CALENDAR.md` FALSIFICATION WATCH — refresh spot values vs live (market tool: `.venv/bin/python FORGE/tools/market-data/fetch.py price <tickers>`).
- [ ] `STATUS.md` ≤200 lines; archive detailed reports to `reports/`.
- [ ] Dedupe `archive/` vs `challenges/`; relocate completed research to `archive/`.
- [ ] Cross-file consistency: PREDICTIONS scoring matches across STATUS/CALENDAR/workbook (S16 caught a RED-19 contradiction).

---

## 2026-06-10 (S17) — Market-tool "breakage" diagnosed: interpreter selection, NOT a broken tool (S16 venv punchlist item CLOSED)

**Symptom:** `python3 FORGE/tools/market-data/fetch.py price ...` → `ModuleNotFoundError: No module named 'yfinance'`. Looked like the S16 "yfinance missing" regression.

**Diagnosis (verified, not assumed):** NOT broken, NOT API overload. The error is a deterministic import failure — it fires before any network call, so rate-limiting/overload is excluded. Root cause: bare `python3` = Ubuntu system interpreter, which is PEP-668 externally-managed (`/usr/lib/python3.12/EXTERNALLY-MANAGED`) — packages can never be pip-installed there by design. All repo packages live in `.venv/`.

**Verified healthy state:** `.venv/bin/python3` = Python 3.12.3 with yfinance 1.2.0 + pandas 3.0.2 + working pip; `fetch.py price` returns live quotes; `dashboard.py` renders Tier 1/2 clean (tested 6/10 ~3:15 PM ET).

**Rule:** always invoke market tools as `.venv/bin/python3 FORGE/tools/market-data/fetch.py ...` (venv activation does not persist across shell calls). The hygiene checklist below already says this — the S17 boot miss was using bare `python3` from muscle memory before re-reading it.

**Closes:** S16 punchlist item 4 ("proper venv fix: sudo apt install python3.12-venv; pin pandas; test dashboard.py") — overtaken by events. Venv exists with working pip (no apt package needed for current state); pandas 3.0.2 runs dashboard.py without error (no pin needed); dashboard tested ✅.

**Optional shared-tooling improvement (Prome-side, NOT RED's file to edit):** `fetch.py`/`dashboard.py` could self-re-exec under the repo venv when imported modules are missing, making them interpreter-agnostic for all agents. Flagged via OUTBOX rather than edited directly (FORGE is shared tooling).

---

## 2026-06-10 (S17) — SPAWN PROTOCOL codified: BOOT / EXECUTE / WRITE-BACK (closeout hardening, Will-approved)

**Trigger:** Will asked whether RED has a proper closeout vs SAM/BRENT/VIOLET. Audit verdict: RED had the network's best boot and its weakest closeout — write-list buried in boot step 10, one handoff line, no DUE-resolution rule, no live-event override, handoff fragmented across LAST_COMPLETION.md + numbered archive/handoffs/. Plan approved on all defaults (D1-D5) 6/10.

**What changed:**
- `CLAUDE.md`: "BOOT SEQUENCE" → "SPAWN PROTOCOL" with BOOT (read, steps 0-9 — preserved BOARD b1-b4 scan; added DUE-scan to step 3, live-anchors step 9 w/ venv path) / EXECUTE (step 10 + **live-event override**, VIOLET pattern) / **WRITE-BACK W1-W10** (read→write pairings; W2 loop-closure "never OPEN-but-stale" extended to CHALLENGES.tsv — RED-unique; W10 git block w/ local-commit default) / discipline overlay (+ RED-specific: counter-signal weights carry as-of dates) / **Doc-Mirror table** (CATALYSTS.tsv→CALENDAR; PREDICTIONS.tsv→STATUS scorecard; CHALLENGES.tsv→STATUS table; canonical wins).
- `SCRATCH.md` NEW — canonical handoff, template at top, rewritten in place at W5. `LAST_COMPLETION.md` RETIRED (breadcrumb left). `archive/handoffs/` FROZEN (README_FROZEN.md; git history versions SCRATCH).
- File tables in CLAUDE.md updated (WHAT YOU READ, Core Files, Archive).

**Dogfood result (Phase 3, same session):** first DUE-scan run found the predictions ledger materially wrong — RED-12/13/14/15/17 ACTIVE-but-stale since late Apr/May, RED-07 canonical lagging its mirrors, RED-08 STATUS-drifted. **TRUE tally 7W/7C/5A vs published "5W/2C/4A" — wrong on all three numbers.** Dispositioned same session; mirrors synced. Validates the recipe's core claim: mechanical scan > vigilance.

**Boot-impact:** next session boots on the new protocol — reads SCRATCH.md (not LAST_COMPLETION), runs DUE-scan at step 3, uses `.venv/bin/python3` per step 9. Friction → log here.

**Out of scope (deliberate):** NEXUS_BRIEF enrollment (Will/NEXUS-phase decision, D3), scripts/boot.py build, KOYOMI-analog steward (Will-deferred S16).

---

## 2026-06-10 (S17, evening) — `scripts/boot.py` built (boot kit; closes the last parity carve-out)

**Trigger:** Will: "FORGE may be a little dated… keep as-is or build?" Plan approved on all defaults (D1-D5).

**What changed:**
- `scripts/boot.py` NEW (~250 lines, READ-ONLY): ① TAPE (11 tickers via FORGE `fetch.py` imported as a library + FRED HY/CCC/claims) ② TRIGGER CHECK (registry hard triggers + WATCHLINES soft lines, live distance + FIRING/NEAR/clear, true sustain-trail evaluation on FRED metrics) ③ CATALYST COUNTDOWN (docket pending ≤14d, fuzzy-date tolerant) ④ DUE-SCAN (predictions past-timeframe → 🔴; unparseable timeframe → ⚠️ manual; ACTIVE challenges listed with age). Venv self re-exec shim — bare `python3` now works for this script.
- `docket/WATCHLINES.tsv` NEW (11 rows): soft/display thresholds (VIX>23 VIOLET line, VIX>20 window, HY 280 re-cross, CCC 955/1000 gates, USDJPY 160, KRE/WAL/SPY position legs, Brent<95 sub-trigger-d). Deliberately separate from `registry/FALSIFICATION_TRIGGERS.tsv` (WALTER auto-fire surface — display rows there could cause unwanted dispatches).
- `CLAUDE.md` boot step 9 → run boot.py; Doc-Mirror table gained the triggers row.

**Dogfood (live test vs known answers):** ①-③ matched the hand-built S17 picture exactly (FT-01 sustained-firing 278/275/276, FT-07 firing, VIX>20 firing, re-cross NEAR −2, CCC gate NEAR −4, T-1 backstop). **④ found catch #3 of the day: 14 stale ACTIVE challenges from April (CHG-RED-006..022, 53-69d old)** — never status-dispositioned (e.g. CHG-RED-008 "rescue revised to 20%" vs current 4%; CHG-RED-018 owed-closure from Apr). Queued as next-session cleanup pass (needs per-row resolution notes, not a rush job).

**Boot-impact:** boot steps 3+9 mechanical halves now one command. Friction → log here. Known limits: yf metrics can't evaluate multi-day sustain (flagged inline); fuzzy timeframes print ⚠️ manual rather than silently passing.

## 2026-07-31 — S27
- **Trigger:** boot found two write-back misses from the S26 night session (PROME-spawned, post-outage). **What changed:** (1) `thesis/CHANGELOG.md` — S26's owed W3 entry (weights 62→68) was never written; backfilled at S27, explicitly labeled BACKFILLED. (2) `NEXUS_BRIEF.md` — skipped its promised per-closeout refresh a SECOND time (first: 7/24); rewritten to vS27, stale 8/13-CPI catalyst row purged. Pattern note: both misses came from a spawned night session running a 4-item task packet — the write-back tail is exactly what a scoped spawn skips (cf. auto-memory `finding_spawned_agents_ship_artifact_skip_writeback`). **Files touched:** thesis/CHANGELOG.md, NEXUS_BRIEF.md. **Boot-impact:** none structural; W3/W8 unchanged as rules — the gap was invocation, not specification.
- **Registry:** FT-01 row rewritten to EXIT-EXECUTED/RE-ARMED state (first exit ever executed off `registry/FALSIFICATION_TRIGGERS.tsv`); WL-03 note updated to COMPLETED-but-live-as-exit-semantics. No schema change.
- **CLAUDE.md amendment (same day, follow-on):** `feedback_red_edge` one-liner embedded into the IDENTITY block per PROME's Phase-2 embed packet (memory three-tier restructure — the row no longer auto-loads from MEMORY.md; CLAUDE.md is now its auto-loading home). Confirmation routed via OUTBOX #4; packet → `inbox/processed/`.
- **New file (same day, S27b): `CHALLENGE_IMPACT_LEDGER.md`** — harmful-revision measurement over CHG-RED-001..043 (PROME 7/25 P6 task). Rubric pre-registered in its own commit before grading (task guard). Re-grade cadence: UNRESOLVABLE-YET rows at their named windows (see ledger footer). Boot-impact: none (not a boot-read file; DUE-scan picks up the CHG-010 stale-ACTIVE flag it surfaced).
- **S27b (same day): CLAUDE.md W2 amendment** — added the undated-ACTIVE rule ("every ACTIVE challenge row must carry a resolution date/event or named re-review date"; CHG-RED-010 root cause, ML-RED-125). New file `CHALLENGE_IMPACT_LEDGER.md` (logged above). `workbook/CHALLENGES.tsv`: 27 legacy rows with non-10-field counts found (pre-existing at HEAD, quoting/schema-evolution artifacts) — queued for a dedicated audit pass, NOT mass-edited (frozen record the impact ledger graded against). Boot-impact: W2 text only.

## 2026-07-31 — S27 Phase 3 (workbook data-integrity repair)
- **Diagnosis correction first:** the earlier S27b note above ("27 legacy rows with non-10-field counts, quoting/schema artifacts") was WRONG in both count and cause — the file's true canon is **11 columns** (`BOARD_Refs` added 2026-05-06, correctly documented in `SCHEMA.tsv` all along; RED's CLAUDE.md workbook table carried the stale 10-col line and my audit inherited it). Real defect set: **30 short rows** (missing trailing empty cells — incl. the two rows I appended earlier today), **1 stray blank line**, **1 content-placement defect** (CHG-028's Resolved_Date cell held a narrative blob), **1 misfiled ref** (CHG-016 VX-RED-015 in KB_Links).
- **Repair executed (content-preserving, verified programmatically):** all rows padded to 11 fields (empty cells only); blank line removed; CHG-028 blob relocated VERBATIM into Resolution with a relocation marker + window date `2026-11-10 (two-print 10/14+11/10)` installed; CHG-016 ref moved to VX_Links; W2 dates installed on CHG-042 (`2026-08-24 re-review`), 043 (`2026-08-15 re-review`), 044 (`2026-11-30 final window`). Post-repair: 44/44 rows at NF=11; every non-empty original cell verified present.
- **RED-21 Timeframe** made machine-parseable (`2026-08-12`, prose → Notes) — boot.py DUE-scan now 🟢 clean, the standing ⚠️ retired.
- **CLAUDE.md** workbook table corrected to 11-col (SCHEMA.tsv named canonical). **Files touched:** workbook/CHALLENGES.tsv, workbook/PREDICTIONS.tsv, CLAUDE.md, SCRATCH.md. **Boot-impact:** DUE-scan noise eliminated; no schema change (the schema was always 11 — the docs and my audit were behind it).

## 2026-07-31 — S27 Phase 4 (CALENDAR narrative layer + WATCHLINES labels)
- **Trigger:** closeout-sweep items 9-11 + 15-remainder. **What changed:** (1) CALENDAR "Top imminent" paragraph rewritten to 7/31 vintage (S22-vintage narrative retired to the resolved tables); (2) PREDICTION SCORING WINDOWS reconciled to canonical PREDICTIONS.tsv — RED-17/10 were carried stale-ACTIVE though CORRECT, RED-18 stale-ACTIVE 26 days though WRONG; section now = ACTIVE windows (RED-21 8/12, RED-04 9/30) + resolved history; (3) FALSIFICATION WATCH section **FROZEN whole** (root Data-Hygiene option (a)) — canonical homes are the registry/WATCHLINES TSVs boot.py evaluates; the section had presented S17/S20 anchors as "active triggers"; (4) EXIT-WINDOW BACKSTOPS **FROZEN — all realized/expired**; (5) WATCHLINES role labels re-pointed on WL-02/07/08/09/10 (Jun-stack/blackout vintage tokens retired; **thresholds untouched**).
- **⚠️ Self-introduced bug caught by the mirror check:** the morning docket re-date set the BDC rows' status to `redated-2026-08-04`, which boot.py's `status=pending` filter DROPS — the CHG-027 capitulation-review gate had silently vanished from the catalyst countdown for ~5 hours. Fresh 🔴 pending row (2026-08-04) added; countdown verified restored. Class: a status-token change on a LIVE row must preserve scanner visibility — resolve-and-REPLACE, never re-label in place (state-token lesson, cf. finding_state_token_sweep_all_surfaces).
- **Files touched:** CALENDAR.md, docket/CATALYSTS.tsv (+1 row), docket/WATCHLINES.tsv. **Boot-impact:** countdown restored; watchline evaluation unchanged (labels only).

## 2026-07-31 — S27 Phase 5 (LAST_COMPLETION reconciliation + the class fix; sweep CLOSED 20/20)
- **LAST_COMPLETION.md reconciled, kept:** investigation (PROME/COMPLETION_SPEC.md + file git history) showed the S26 spawned session wrote it CORRECTLY — the fleet spawn contract REQUIRES every spawned sub-agent to overwrite `AGENTS/<name>/LAST_COMPLETION.md`; RED's S17 local retirement was never reconciled with that spec. CLAUDE.md reference table now documents the dual role: spawn-contract surface only, per-spawn report to PROME, expected stale between spawns, never boot-read; SCRATCH stays sole canonical handoff. No deletion (would put the next spawn in breach), no PROME packet needed (no conflict remains).
- **Class fix for the sweep's signature:** Discipline-overlay line added to CLAUDE.md WRITE-BACK — a dated section stamp older than the previous session forces re-read-or-restamp-or-freeze; a date is a TRIGGER, not a shield. Promoted to auto-memory `finding_dated_stamp_is_a_trigger_not_a_shield` (generalizes: the SKEW clock masked 8d behind a dated anchor, the pre-FOMC priorities surviving two sessions, two predictions ACTIVE 26d post-resolution). Mechanization (a date-token grep script) deliberately DEFERRED — the manual rule gets one chance first; build the script only if it fails once.
- **Sweep ledger: all 20 flagged items CLOSED** — P1: 16/17/18/20 · P2: 1-8 · P3: 12/13/14/15-rows · P4: 9/10/11/15-labels · P5: 19 + class fix. Two self-caught bonuses along the way: the SKEW 2-of-4 clock (P2) and the boot.py pending-filter bug from my own morning re-date (P4).
