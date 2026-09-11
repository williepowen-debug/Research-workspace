# VIOLET Maintenance Log

Reverse-chronological log of **structural** changes to VIOLET's docs, folders, scripts, and SPAWN/write-back protocol. Each entry: **Trigger / What changed / Files touched / Boot-impact / Lessons**. Answers *"why is VIOLET organized this way?"*

**Distinct from:**
- `thesis/CHANGELOG.md` — **analytical** changes (thesis version bumps, POV pivots, conviction shifts, prediction resolutions).
- `SCRATCH.md` — **ephemeral** per-session handoff (overwritten every write-back; structural changes noted there do NOT persist — they persist HERE).

Log material structural changes only — not routine content edits. Template adopted from OTTO (2026-06-10), incl. the cap: **archive to `archive/` if this grows past ~300 lines** (SAM cautionary tale: 636).

---

> 📄 *The **2026-08-18** and **2026-08-20** entries are archived verbatim → `archive/MAINTENANCE_ARCHIVE.md` (crc32 `dfd3e19c`), rotated 2026-09-06 PM2 on the ~300-line cap.*

> 📄 *The **2026-09-02** entry (READ-CAP hot/cold split of MEMORY.md; `^SKEW` basis ruled to CBOE; 31-item two-lane inbox drain) is archived verbatim → `archive/MAINTENANCE_ARCHIVE.md` (crc32 `d4ed7154`), rotated 2026-09-06 PM3 on the ~300-line cap.*

> 📄 *The six **2026-09-04** entries (Amendment-10 ordering check built; five queued tool defects; three review rounds; the DAEDALUS profile refresh) are archived verbatim → `archive/MAINTENANCE_ARCHIVE.md` (crc32 `610ede72`), rotated 2026-09-11 evening on the ~300-line cap.*

## 2026-09-06 (PM3) — Codex 3rd pass: the provisional safeguard failed on the second run; the falsification baseline was broken by its own shipping commit

**Trigger:** Codex's third pass, run against the committed 2nd-pass code with stubbed sources and temporary ledgers.

**What changed:**
1. **SETTLE stamping is now STATELESS.** The 2nd-pass guard gated on a per-run `provisional_rows` set: it held on run 1 and stamped `SETTLE` over the provisional 149.00 on run 2, because the value is on disk, the destination gate preserves it, nothing new is recorded, and the stamp then only checked `vix`. Now: stamp only when **every** spot column is CBOE-confirmed for that date **or blank**. **Recovery is preserved and tested as a negative control.** → KB-VIO-267
2. **Dead plumbing removed** — the `provisional_rows` parameter is gone from both functions rather than left in place beside the stronger guard.
3. **`--falsify` re-anchored to a pinned revision** (`1e8ae5d00^`). It had loaded `HEAD`, which the shipping commit turned into the fixed file. → KB-VIO-268
4. **Test cases [6] two-run and [7] recovery control added.** Suite 7/7; `--falsify` 12/12 (2/3/5/6 fail pre-fix, 1/4/7 pass).
5. **Three summaries reconciled:** `STATUS.md` FT-10 row's *"published 9/10"* withdrawn (a T+1 assumption KB-VIO-137 had already retracted); the receipt's acceptance line corrected against its own transcript (case 3 exits 0); *"rule out"* → *"reduce the risk of"*.
6. **STATUS restructured rather than shaved** — FT-10 epistemics → KB-VIO-262, WQ-188 narrative → the receipt. Headroom 55 B → **924 B**.

**Files touched:** `scripts/backfill.py` · `scripts/test_backfill_endtoend.py` · `STATUS.md` · `SCRATCH.md` · `NEXUS_BRIEF.md` · `research/2026-09-06_wq188_2nd_pass_receipt.md` · `workbook/KB.tsv` (267–268) · this file.

**Boot-impact:** none. Live control re-run after the change: 2,496 cells agreed, 0 corrected, ledger md5 unchanged.

**Lessons:**
- **A guard whose memory is shorter than the state it guards fails on the second run.** Persistent state needs a stateless test read off the artifact, not run-scoped bookkeeping.
- **A baseline that moves is not a baseline.** Any harness referencing "the previous version" must name an immutable revision — a moving ref passes for its author and is already broken for everyone else.
- **Twice in one day a comment in this file certified what the code did not do.** Implement an invariant in the same edit you write it, or mark it TODO.
- **Shaving bytes off a capped surface is not capacity work.** I trimmed, then immediately re-spent the headroom on narrative. Move content to its canonical home instead.

---

## 2026-09-06 (PM2) — Codex 2nd pass: the WQ-188 fix closed the transport axis only; a destination gate added, and the AM test suite found unable to fail

**Trigger:** Codex's second pass on `backfill.py`, routed by PROME as a 🟠 HIGH doorbell (`inbox/2026-09-06_from-PROME_Codex-backfill-closure-still-too-broad-...md`) under Will's standing WQ-188 ruling. PROME verified the three code sites; the runtime table is Codex's.

**What changed:**
1. **`fetch_cboe_history` now validates response STRUCTURE, not just HTTP status.** A 200 whose body is HTML yielded zero `DATE`-keyed rows and returned `({}, True)` — the identical value an authoritative empty answer returns — so the column never entered `failed` and yfinance kept write authority at rc=0. Now: a DATE column plus `CLOSE`/`<SYM>` (verified live against all six endpoints) or it is a **parse failure**, failing closed. ⚠️ **The docstring I wrote that morning already asserted `ok is False ... for a ... parse failure` while no parse check existed** — a guarantee written beside code that does not implement it converts an open hole into a documented closed one. → KB-VIO-264
2. **A DESTINATION gate added to `backfill_spot`.** v1 scoped authority purely by *what the source said* (column failed / CBOE holds a value); a valid CSV merely **missing the target date** satisfied neither and the fallback landed in a row still labelled `SETTLE`. Now yfinance may fill a blank, **never overwrite**, and **never touch a `SETTLE` row**. → KB-VIO-265
3. **A third route, not in Codex's table, found and closed:** the same hole also **newly MINTS** a `SETTLE` stamp when a provisional fill lands in a blank cell on a non-SETTLE row — every component behaving correctly, the whole-run `not failed` guard blind because nothing failed. **Ablation-proven load-bearing** (disable the clause, the case goes red). → KB-VIO-265
4. **`scripts/test_backfill_endtoend.py` built** — runs `backfill.main(["--spot-only"])` for real, stubbing only `requests.get` and the `yfinance` module and redirecting `DAILY_LOG` to a temp file, asserting on the file on disk. 5/5 green; `--falsify` re-runs every case against the pre-fix `backfill.py` from git HEAD and requires 2/3/5 to fail there while 1/4 still pass (9/9, rc=0).
5. **`test_backfill_authority.py` repaired, not deleted** — its vacuous `"settle_stamped" not in str(rows)` clause replaced, its misleading rationale corrected, and a scope banner added saying it cannot catch a gate defect. → KB-VIO-266
6. **STATUS rotated twice on the read-cap budget** (33,864 B → 32,495 B): the v4.1/v4.1.1 thesis long-form → `archive/STATUS_THESIS_v41_NARRATIVE_2026-09-06.md` (crc32 `48130641`), the settled RESEARCH QUEUE dispositions → `archive/STATUS_RESEARCH_QUEUE_DISPOSITIONS_2026-09-06.md` (crc32 `2f380602`). Both verbatim; heading inventory asserted identical and the removed span asserted byte-present in the archive.

**Files touched:** `scripts/backfill.py` · `scripts/test_backfill_endtoend.py` (new) · `scripts/test_backfill_authority.py` · `STATUS.md` · `NEXUS_BRIEF.md` · `research/2026-09-06_wq188_2nd_pass_receipt.md` (new) · `workbook/KB.tsv` (264–266) · `board_log.tsv` · this file.

**Boot-impact:** none — no boot stage added or changed. `backfill.py` is on-demand; both test suites are on-demand. Live control run: 2,496 cells agreed, 0 corrected, **ledger md5 unchanged**.

**Lessons:**
- **A fix scoped to the failure you were SHOWN is not scoped to the failure MODE.** Codex demonstrated a 503; I closed 503-shaped failure. The mode is "the source returned something that is not an answer," and HTTP status is one axis of it.
- **A write gate must be a claim about the CELL IT LANDS IN, not only about the source it came from.** Scoping authority by provenance alone leaves the destination unguarded.
- **The suite that certified the AM fix could not have failed.** Its gate was a hand transcription, so the shipped code never ran, and one assertion compared a counter's name against ledger rows. **I wrote the contracts from the fix instead of from the failure mode** — third instance of that shape on this desk in three days. The mechanical cure is now permanent: `--falsify` runs the new tests against the old code, with a negative control so the suite cannot pass by failing everything.
- **After adding a guard, delete it again and confirm the test goes red.** A guard never observed to be load-bearing is indistinguishable from a decorative one, and both pass.

---

## 2026-09-06 (PM, second) — thesis read: a live STATE was living in the MECHANISM box; STATUS ③–⑦ rotated to archive on the read cap

**Trigger:** Will, *"now let's do the thesis read"* — the designated judgement work. Structural findings only here; the analytical content is `thesis/CHANGELOG.md` v4.1.

**What changed (structure):**
1. **`thesis/VIX_THESIS.md`'s MECHANISM STATUS box no longer carries a live value.** It carried HENRY's 7/2 gamma reading — a **maintained, fast-moving measurement** — inside a **framework file that has no refresh contract and no staleness detector.** It aged 66 days and was **sign-wrong for four** while every live surface disagreed. The box now holds the mechanism, its fences, and **a pointer with an explicit vintage**; the value's home is `STATUS.md` + HENRY's brief. **Rule adopted: a mechanism box may not carry a live state.**
2. **`STATUS.md` blocks ③–⑦ rotated verbatim** → **NEW** `archive/STATUS_LEDGER_REPAIR_2026-09-06.md` (crc32 `213ba22a`), pointer left in place. STATUS had hit **33,550 B against the 32,550 B read cap** when the thesis section was written in; now **31,035 B**, `read_cap_check` rc=0.

**Files touched:** `thesis/VIX_THESIS.md` · `thesis/CHANGELOG.md` · `workbook/KB.tsv` (258→260) · `STATUS.md` · **NEW** `archive/STATUS_LEDGER_REPAIR_2026-09-06.md` · `SCRATCH.md` · `NEXUS_BRIEF.md`.

**Boot-impact:** none to the sequence. STATUS is ~2.5 KB lighter at boot-step 1; the rotated narrative is **on-demand, never a boot read**. `thesis_bump_check` resets to 0 rows.

**Lessons:**
- 🔑 **ASK OF ANY FRAMEWORK/SPEC DOC WHICH STATEMENTS ARE *STATE* AND WHICH ARE *STRUCTURE*. Only state rots — and no staleness instrument watches a file that isn't a ledger.** Every check ran green over a sign inversion for four days. → KB-VIO-259
- ⚠️ **THE 9/4 SWEEP HAD ALREADY BEEN IN THIS FILE and fixed the TAIL, leaving the identical defect in the HEADER.** Flag's scope ≠ defect's scope — **n=3 in seven days** (KB-VIO-250). **Sweep the file's whole CLASS of blocks, not the named block.**
- ⚠️ **A DETECTOR CAN BE CORRECT AND STILL NOT SEE THE THING.** `thesis_bump_check.py` counts rows; it cannot see a **sign flip**. It correctly said *look*. **The read is the instrument; the counter is only the alarm clock.**

---

## 2026-09-06 (PM) — WQ-188: yfinance stripped of write authority over the six CBOE columns; `cheap_tail.py` re-pointed to the publisher of record

**Trigger:** Codex reviewed **this morning's own repair** at the artifact and returned one HIGH (routed PROME → VIOLET; Will ruled WQ-188 *"approve WQ-188 with your rec"* 10:58 ET, fixes before the thesis read). `backfill.py` **failed OPEN**: `main()` ran the yfinance pass first, then CBOE; on a CBOE failure the CBOE pass printed *"CBOE pass SKIPPED (yfinance stands)"*, `write_merged()` saved, and the run **exited 0**. Codex's case — ledger `skew` 151.58 `basis=SETTLE`, yfinance 149.00, CBOE 503 ⇒ **149.00 written with the SETTLE stamp retained, rc=0.**

**What changed:**
1. **`backfill.py` — write authority scoped, not checked.** CBOE is now fetched **first**, and yfinance's authority over the six spot columns is decided per-column against what CBOE confirmed **this run**: series failed ⇒ **no write at all** (the verified value is preserved) · CBOE has a value ⇒ yfinance defers · CBOE OK but publishes nothing for that cell ⇒ yfinance may write it **provisionally**, never stamped `SETTLE`. `main()` returns **2** and names the failed series.
2. **`fetch_cboe_history()` returns `(data, ok)`.** It signalled failure with `{}` — the same value a successful empty fetch returns — so the caller gated on truthiness and could not tell *"CBOE publishes nothing"* from *"CBOE did not answer."* `requests.RequestException` is now caught rather than propagating.
3. **`basis=SETTLE` is gated on a fully-confirmed row.** `basis` is a row-level claim, so a row holding even one unverified column is not stamped. **That stamp is what made the defect dangerous rather than merely wrong.**
4. **NEW `scripts/test_backfill_authority.py`** — 12 contracts, no network, both sources stubbed. Codex's exact case is test [1]. rc=0.
5. **`cheap_tail.py` `pull()` re-pointed to CBOE** (fix ②) — the 🟣 OPEN 4/4 operator-decision surface was reading `^VIX`/`^VVIX`/`^SKEW` from yfinance at **run time**, which repairing the ledger did not touch. yfinance survives only as a fallback that marks `source=yfinance-PROVISIONAL` in stdout, the returned dict **and** the `CHEAP_TAIL.tsv` note column.

**Files touched:** `scripts/backfill.py` · `scripts/cheap_tail.py` · **NEW** `scripts/test_backfill_authority.py` · `workbook/KB.tsv` (KB-VIO-252→255) · `workbook/VX_DAILY.tsv` (m1m2 side-effect, below) · `STATUS.md` · `SCRATCH.md` · `NEXUS_BRIEF.md` · `board_log.tsv`.

**Boot-impact:** none to the boot sequence. `backfill.py` is not on the boot path; `cheap_tail.py --boot` is, and its output gains a source marker **only when provisional**. A future CBOE outage now makes `backfill.py` exit 2 where it previously exited 0 — **that is the intended new behaviour, not a regression.**

**Verification (each falsified by running, not by reading):** CBOE 503 on `skew` alone ⇒ 151.58 preserved · all six fail ⇒ every column byte-identical · a `TICK` row is not promoted to `SETTLE` on an incomplete run · **control:** live run vs the reconciled ledger = **2,496 cells agreed, 0 corrected, 0 filled** · `cheap_tail` on CBOE = VIX 14.53 / VVIX 84.42 / SKEW 151.58, **identical to the cent**, 4/4 🟣 OPEN unchanged · stubbed 503 on SKEW ⇒ output labelled PROVISIONAL in all three places. Closeout guard **8/8 blocking contracts green**.

**Side-effect recorded, not hidden:** the control run's ledger md5 changed. The **spot** columns are provably identical (0 corrected, 0 filled); the delta is entirely the **m1m2 path** — untouched by this fix — filling four blank cells on 8/28 · 8/31 · 9/1 · 9/3, the four sessions restored this morning, each properly stamped with its own `m1m2_settle_date`. Kept: stamped values beat blanks.

**Lessons:**
- 🔑 **A CORRECTION PASS THAT REPAIRS VALUES BUT LEAVES THE BAD WRITER IN PLACE HAS A HALF-LIFE.** I fixed 476 cells this morning and left the write order alone. The next source outage would have restored the defect — **and the `SETTLE` stamp would have made the restored value look verified.** Fixing data is not fixing the mechanism. → KB-VIO-252
- 🔑 **REMOVE A WRITER, DON'T ADD A CHECKER.** A checker runs after the damage and has to be believed; scoped authority means the bad write cannot occur. This desk has already paid for the other pattern (`[[finding_a_check_that_only_advises_is_overridden_the_control_is_downstream]]`).
- ⚠️ **A SENTINEL THAT COLLIDES WITH A LEGITIMATE VALUE CANNOT CARRY A DISTINCTION.** `{}` meant both "nothing here" and "no answer," and every consumer inherited the collision. Ask of any fetch helper what it returns when the source is **down**, and whether that is distinguishable from a real answer. → KB-VIO-253
- ⚠️ **THE VALUES AGREEING IS NOT REASSURANCE — IT IS THE CONDITION UNDER WHICH WIRING DEFECTS SURVIVE.** `cheap_tail`'s CBOE numbers came back identical to the cent, exactly as RED's yfinance-graded FT-10 agreed with CBOE for four days while printing a false FIRING. The fix is justified by the **source of record**, never by a delta. → KB-VIO-254
- ⚠️ **AND THE FIRST DRAFT OF MY OWN TEST FAILED A CORRECT FIX.** It grepped the whole source for `"yfinance stands"` — which still appears, correctly, in three docstrings recording *why* the branch was removed. **A test may not force the code to forget its own history.** Replaced with an AST walk over `print()` literals, which asks the question that actually matters. → `[[finding_scan_keyed_on_naming_reads_local_form_as_absence]]`
- ⚠️ **RESIDUAL, NAMED SO IT IS NOT READ AS CLOSED:** `thresholds.py` still writes the daily row from yfinance at every boot, so the six columns are authoritative in **history** and provisional at the **leading edge**. Four more scripts read `^SKEW` from yfinance. → KB-VIO-255

---

## 2026-09-06 — CBOE made the authoritative source for all six spot columns; `VX_DAILY` gap check built and wired BLOCKING; PROME completion-spec re-key executed and two guards re-pointed with it

**Trigger:** Will directed two items off the boot report — the `VX_DAILY.tsv` backfill (SCRATCH priority #1: 4 missing sessions inside the live FT-10 window) and the PROME consumer flag on `CLAUDE.md`'s superseded `LAST_COMPLETION.md` instruction.

**What changed:**
1. **`backfill.py` — CBOE promoted from a one-column workaround to the authoritative pass.** `backfill_vix9d_cboe()` (VIX9D only, **fill-blanks-only**) replaced by `backfill_spot_cboe()` covering all six spot columns. It runs **after** yfinance and **wins**: fills blanks *and* **corrects** disagreements, **printing every correction** rather than silently overwriting, and stamps `basis=SETTLE` for completed sessions CBOE has published. 🔑 **The old fill-blanks-only guard is exactly why nine bad cells survived every prior backfill — a cell holding a wrong value was *protected* from the source that could fix it.** Same shape as the m1m2 hazard already flagged in that module's own docstring. Precedence follows the ratified MOVE pattern (investing.com PRIMARY, yfinance cross-check).
2. **NEW `scripts/vx_daily_gapcheck.py`** — session completeness. Boot stage (**warns**) + `closeout_guard.py` **8th BLOCKING contract**. Deliberately the complement of `skew_integrity.py`: that compares **values** and is blind to a missing row; this compares the **set of sessions** and is blind to a wrong value. **Uses the orphan-VIX companion rule, not a synthesized calendar** (KB-VIO-243).
3. **`canary_staleness.py` made cadence-aware.** The blanket `>4d` asserted-current-cell line now reads the row's **own declared cadence** (`weekly` → 10d = 7 + 3 grace; else 4d).
4. **Completion-spec re-key.** `CLAUDE.md` write-back step 11a + FILES row re-pointed from "Overwrite `LAST_COMPLETION.md`" to the dated `PROME/inbox/{date}_from-VIOLET_{slug}.md` memo; `LAST_COMPLETION.md` **frozen with a banner**; `README.md` map row corrected. **On Will's direct word** — PROME raised it, but a `CLAUDE.md` edit needs the operator's own.
5. **⚠️ `writeback_order_check.py` and `surface_agreement.py` re-pointed in the same change** — both **tracked the frozen file**. Both now resolve `PROME/inbox/*_from-VIOLET_*.md` by glob (newest wins; ISO names sort lexically) and report MISSING when no memo exists. Ordering check also stopped printing a MISSING surface as a ~29.8-million-minute "lag."
6. **`CALENDAR.md`** DATA REFRESH row corrected — it claimed `ledger_staleness.py` surfaces gaps; **it measures vintage, not gaps**, and ran rc=0 over all four holes.

**Files touched:** `scripts/backfill.py` · `scripts/vx_daily_gapcheck.py` (new) · `scripts/boot.py` · `scripts/closeout_guard.py` · `scripts/canary_staleness.py` · `scripts/writeback_order_check.py` · `scripts/surface_agreement.py` · `CLAUDE.md` · `README.md` · `CALENDAR.md` · `MEMORY.md` · `LAST_COMPLETION.md` (frozen) · `STATUS.md` · `SCRATCH.md` · `NEXUS_BRIEF.md` · `workbook/{VX_DAILY,KB}.tsv` · `board_log.tsv` · 3 inbox files → `processed/`

**Boot-impact:** one new boot stage (**15 total**) and one new blocking closeout contract (**8 total**). `backfill.py --spot-only` now performs a full CBOE reconcile — slower by ~6 CSV fetches, and it is the only path that repairs a wrong value. `MEMORY.md` gains a CBOE-endpoint entry; the phantom-print caveat is re-attributed.

**Lessons:**
- **A workaround written for ONE column is evidence about the SOURCE.** The VIX9D CBOE path existed *because yfinance serves no VIX9D daily history* — and `^VIX3M`/`^VIX6M` were equally unserved, which is why **226 of 416 cells were blank** in VIOLET's own core owned metric. Nobody asked what else the better source covered.
- **An impossibility claim inherits the scope of the method that produced it.** *"Can BOUND, never CLEAR"* was true of a bar-count check over the mirror, false of a reconcile against the authority. One bad `^SKEW` cell in 20 months — the one RED named.
- **Retiring a surface is an INTERFACE change.** Freezing a file that two BLOCKING guards track would not have removed a control but **inverted** one: always-red ⇒ silenced ⇒ real coverage gone. **Grep for what READS a file before freezing it, and treat scripts as first-class consumers.**
- **When you retire a bad threshold, grep for its siblings.** The retired COT `>9d` defect was still alive in `canary_staleness.py`'s `>4d` line, on the same instrument.
- **Falsify, and notice when the TEST is what broke.** My phantom-row test first returned rc=2 because my harness sorted the header out of line 1. The tool failed closed — correct — but the branch stayed untested until I redid it properly.

---

## 2026-09-11 ~14:5x ET — THREE CLOSEOUT-GUARD CONTRACTS WERE WRONG, A FALSIFIER WAS BROKEN, AND A `scripts/tests/` DIRECTORY NOW EXISTS

**Trigger:** boot of the 2026-09-11 midday session. `corrections_boot_check` rc=1 (3 unreceipted) and `vx_daily_gapcheck` rc=1 flagging **today's own live row** as a phantom.

**What changed:**
1. **`vx_daily_gapcheck.py` — span re-anchored to the PUBLISHER'S FRONTIER.** It ran `hi = max(ledger)`, making the audit's upper bound the audited artifact's own last row. One broken reference, two opposite symptoms: **silent-green** on a trailing-edge gap (identical `rc=0 … no gaps` at 416 rows broken and 419 repaired) and **loud-red** on the legitimate live TICK row. Also bounded `extra`, which was charging the ledger for rows outside the audited window.
2. **`backfill.py` — can now CREATE missing sessions.** Its CBOE pass iterated `rows.items()`, so the gapcheck's own printed remedy (`--spot-only`) did nothing over a gap. Skeleton rows are created for true sessions only (VIX + ≥1 companion), bounded by the ledger's first row and the frontier; the existing pipeline fills, derives, computes regime and stamps SETTLE.
3. **`surface_agreement.py` — memo glob bounded to ONE delivery date.** It read every `*_from-VIOLET_*` memo ever delivered as a live surface, so seven 9/06 memos held a BLOCKING check permanently red and **its printed remedy required editing a delivered record.**
4. **`fb_grade.py` — NEW.** Resolver for the F-B falsifier, wired as a boot stage.
5. **`scripts/tests/` — NEW DIRECTORY** (+ `tests/fixtures/`). Two frozen offline suites: `test_gap_detect_and_repair.py` (13 checks) and `test_surface_agreement_bound.py` (5 checks).
6. **`CANARY_MAP.md:52`** — RED's withdrawn 0.79% mirror-defect rate corrected to the three-mode census.

**Files touched:** `scripts/vx_daily_gapcheck.py` · `scripts/backfill.py` · `scripts/surface_agreement.py` · `scripts/fb_grade.py` (new) · `scripts/boot.py` · `scripts/tests/*` (new) · `CANARY_MAP.md` · `STATUS.md` · `CALENDAR.md` · `workbook/{KB,CATALYSTS}.tsv` · `registry/corrections_receipts.tsv` · `memory/auto/finding_write_timestamps_from_the_clock_not_the_narrative.md`.

**Boot impact:** boot gains a 16th stage (`fb_grade.py`). Closeout contracts unchanged in count; two that were red are green. **The new tests are NOT wired to any step — nothing runs them automatically. Flagged, not assumed.**

**Lessons:**
- **🔑 A LEDGER CANNOT BE ITS OWN COMPLETENESS REFERENCE.** Both gapcheck defects and the backfill defect are the same shape: the instrument took its bound from the thing it was auditing. **Neither was a wrong threshold — every one was a wrong REFERENCE**, which is the class that passes every review because the arithmetic is right.
- **⚠️ DETECTION AND REPAIR MUST BE TESTED TOGETHER.** The gapcheck could not see a trailing gap and `backfill` could not fix one; **each instrument's own verdict looked clean while the pair was useless.** That is why the new test exercises both halves in one run.
- **🔑 WRITING ABOUT A CHECKER'S OUTPUT ON THE SURFACE IT CHECKS MAKES THE CHECKER FIRE ON YOUR DESCRIPTION OF IT.** Bounding the memo glob unmasked a real 28/50 — inside the STATUS paragraph where I had quoted the guard while explaining why its red was "correct and intended." **The tempting fix (loosen the matcher to excuse a quotation) inverts the failure direction; the honest fix was to rewrite a paragraph the repair had just made false.**
- **⚠️ A FIX THAT ONLY MAKES A BLOCKING CHECK QUIETER IS INDISTINGUISHABLE FROM LOOSENING IT INTO USELESSNESS.** So the test asserts it still FAILS on a same-session contradiction and still fails CLOSED on an absent memo — never merely that it stopped complaining. **My first draft of that contrast case was self-deceiving**: it called `main()` with no `--date`, which defaults to today and so bounded the very path it claimed to test unbounded.
- **🔑 A FALSIFIER WITH AN UNSPECIFIED ESTIMATOR IS NOT A FALSIFIER.** F-B named two tests 1.25× apart, and the unstated choice (demeaned σ over n=4) reports **0.00% realized vol for four consecutive +1% days** — biased toward confirming this desk's own call on the most likely path. **Basis declared pre-outcome, from git's clock, not the narrative's.**
- **⚠️ A DESTRUCTIVE `open()` THAT PRECEDES THE OPERATION THAT CAN FAIL IS NOT ATOMIC.** A `csv.writer` rewrite of `KB.tsv` truncated the file and *then* raised, leaving 22 of 277 lines. Recovered whole from HEAD (the rows were uncommitted). **Ledger rewrites now go temp → verify line and field counts on the temp → `os.replace`.**


## 2026-09-11 (evening) — The stale-column guard's WITNESS could not see an EOD-only series; `run_tests.py` built and wired as the 9th blocking contract

**Trigger:** Taking the 9/11 settle that the 14:5x session left owed. `thresholds.py --supersede` wrote NULL for `skew` and printed *"the quote belonged to a PRIOR session"* — but the suppressed value **154.49** differed from the 9/10 close **147.02**, so the stated reason was false on its face.

**What changed:**
1. **`thresholds.py` — source and witness both re-pointed to the publisher.** New `cboe_quote()` fetches value **and** `last_trade_time` from CBOE's delayed-quotes API in ONE call; `fetch_spot()` tries it first and falls back to yfinance + `last_bar_et_date()` only when CBOE is unreachable or serves an unusable payload. Each column records `<key>_src`. The guard's stale message now names the **witnessed date** instead of asserting a fixed cause.
2. **`scripts/tests/test_stale_column_witness.py` created — 27 checks**, frozen and offline (clock, publisher and mirror are all fixtures).
3. **`scripts/run_tests.py` created** — discovers `tests/test_*.py`, aggregates, and **fails CLOSED** on a missing dir, an empty discovery, or a count below `MIN_SUITES=3`.
4. **`closeout_guard.py` — 9th BLOCKING contract added:** *Offline regression suites*.
5. **`MAINTENANCE.md` rotated** — the six 2026-09-04 entries archived (crc32 `610ede72`); 320 → 164 lines, clearing the ~300 cap `thresholds.py` had been flagging every run.

**Files touched:** `scripts/thresholds.py` · `scripts/run_tests.py` (new) · `scripts/tests/test_stale_column_witness.py` (new) · `scripts/closeout_guard.py` · `MAINTENANCE.md` + `archive/MAINTENANCE_ARCHIVE.md` · `workbook/{VX_DAILY,COT_VIX,KB}.tsv` · `STATUS.md` · `SCRATCH.md` · `NEXUS_BRIEF.md` · `AGENTS/RED/inbox/` (carve-out ①) · `PROME/inbox/` (carve-out ①).

**Boot-impact:** boot stage 1 (`thresholds.py`) now makes up to 6 CBOE HTTP calls before falling back; measured 2.2–3.1s, unchanged in practice. **Closeout is now 9 blocking contracts, and a new test suite requires no wiring** — dropping a `test_*.py` into `scripts/tests/` is enough.

**Lessons:**
- 🔑 **A witness must be able to SEE the thing it certifies.** `^SKEW` publishes EOD only, so a 5-minute intraday feed structurally cannot observe its same-day print — the guard was **guaranteed** to blank `^SKEW` on every post-close run, not occasionally. The arithmetic was right, the threshold was right, the **reference** was wrong: the same class as all three contracts fixed at 14:5x the same day. `[[finding_instrument_reports_clean_against_the_wrong_reference]]`
- 🔑 **A fixed reason string eventually prints for a case it does not fit, and the wrong reason is what the reader acts on.** The message asserted a cause ("do not publish pre-open") rather than reporting the observation. **State the witnessed fact.**
- 🔑 **Self-healing hid the defect.** `backfill.py` refills the cell from CBOE the next session, so exactly **one** blank existed across 420 rows and every completeness check passed green. **The ledger looked perfect; the closeout reading it did not have the bar** — and this is the OMISSION mode (KB-VIO-281 mode 1) arriving from my own instrument rather than the mirror. **A sustain counter that never receives a qualifying bar reads 0-of-4 forever, and nothing looks wrong.**
- ⚠️ **Validating source A's value with source B's timestamp is itself a wrong-reference pair** — fixing only the witness would have left it. Value and timestamp now come from one call.
- ⚠️ **Discovery-based wiring has a mirror-image failure**: an emptied or renamed directory makes a naive runner report success. `MIN_SUITES` is a floor that only a deliberate edit may lower — the DAEDALUS 🔴#5a defect (`return 0` for a missing script) re-appearing in a new place.
- ⚠️ **ORDERING ANOMALY, recorded not fixed:** this log is declared reverse-chronological, but the 2026-09-11 14:5x entry was appended at the BOTTOM and this entry follows it there. **The 9/06 → 9/04 block above is reverse-chron; the two 9/11 entries are not.** Left as-is rather than restructured mid-session; **flagged for a deliberate pass.**
