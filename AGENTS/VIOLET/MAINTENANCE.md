# VIOLET Maintenance Log

Reverse-chronological log of **structural** changes to VIOLET's docs, folders, scripts, and SPAWN/write-back protocol. Each entry: **Trigger / What changed / Files touched / Boot-impact / Lessons**. Answers *"why is VIOLET organized this way?"*

**Distinct from:**
- `thesis/CHANGELOG.md` — **analytical** changes (thesis version bumps, POV pivots, conviction shifts, prediction resolutions).
- `SCRATCH.md` — **ephemeral** per-session handoff (overwritten every write-back; structural changes noted there do NOT persist — they persist HERE).

Log material structural changes only — not routine content edits. Template adopted from OTTO (2026-06-10), incl. the cap: **archive to `archive/` if this grows past ~300 lines** (SAM cautionary tale: 636).

---

> 📄 *The **2026-08-18** and **2026-08-20** entries are archived verbatim → `archive/MAINTENANCE_ARCHIVE.md` (crc32 `dfd3e19c`), rotated 2026-09-06 PM2 on the ~300-line cap.*

> 📄 *The **2026-09-02** entry (READ-CAP hot/cold split of MEMORY.md; `^SKEW` basis ruled to CBOE; 31-item two-lane inbox drain) is archived verbatim → `archive/MAINTENANCE_ARCHIVE.md` (crc32 `d4ed7154`), rotated 2026-09-06 PM3 on the ~300-line cap.*

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

## 2026-09-04 — A crash exposed that Amendment 10 was a sentence, not a check; `writeback_order_check.py` built and wired BLOCKING; the 7/1 tail-hedge framework stood down; MAINTENANCE archived to clear its cap

**Trigger:** Will-spawned boot after a session crash — *"We had a crash so we may have some incomplete files ideas from the previous session. Please check."* Three VIOLET sessions ran on 9/4; the second died mid-write-back.

**What changed (structural only — the analytical work of the 10:0x session is in KB-VIO-227→233 and its own commit `ef3e0be9c`):**

1. **NEW `scripts/writeback_order_check.py` — the write-back ordering contract, now code.** The crashed session committed `STATUS.md` (10:06) and `SIGNAL_INTAKE.md` (10:08) and died before its tail, leaving `SCRATCH.md`, `LAST_COMPLETION.md` and `NEXUS_BRIEF.md` at their 08:47 commit — **79 minutes behind STATUS**, each addressed to a consumer who is not VIOLET (my own next boot · PROME · NEXUS). **At the next boot `boot.py` returned 14/14 OK, `ledger_staleness.py` rc=0, `corrections_boot_check.py` rc=0, and `closeout_guard.py` was red only on the pre-existing COT contract. Four checks, all green, over a live breach.** The check computes effective vintage per surface and fails if any handoff surface lags STATUS.
2. **Wired BLOCKING into `closeout_guard.py`.** Added to `BLOCKING` alongside the CANARY_MAP, grading-note and workbook contracts; docstring records why.
3. **`TRADE.md` — the Gated Tail-Hedge Packet stood down (WQ-177).** Heading token **ARMED → RETIRED-SUPERSEDED**; a banner above it names the 2026-07-31 supersession (DOCKET L163) and Will's 9/4 11:11 stand-down, and marks Gates A/C dead letters against their 2026-07-02 print. **Body kept verbatim.** KB-VIO-113 → `SUPERSEDED`, KB-VIO-230 → `CONFIRMED`.
4. **`MAINTENANCE.md` cap cleared, second archival pass.** 317 lines against the ~300 cap (boot had flagged it every session for weeks). The three oldest live entries (2026-06-13 · 06-14 · 06-23) moved verbatim to `archive/MAINTENANCE_ARCHIVE.md` under a dated banner; live log now keeps 2026-07-11 onward. **317 → 268 before this entry.**
5. **`board_log.tsv` lane closure completed.** `SIG-W-20260904-001` had its disposition row written at 08:46 but the file was never `git mv`'d to `processed/` — the crash split a two-step act. Move completed; WALTER lane empty.

**Files touched:** `scripts/writeback_order_check.py` (new) · `scripts/closeout_guard.py` · `TRADE.md` · `STATUS.md` · `SCRATCH.md` · `LAST_COMPLETION.md` · `NEXUS_BRIEF.md` · `MAINTENANCE.md` · `archive/MAINTENANCE_ARCHIVE.md` · `workbook/KB.tsv` · `inbox/WALTER/processed/`.

**Boot impact:** none at boot — the new check runs at **closeout**, deliberately. Closeout now has **four** blocking contracts instead of three, and a session cannot exit past a lagging handoff surface. No new boot-time whole-read; no read-cap change.

**Lessons:**
- **🔑 The rule was never missing. It was already written as an arithmetic comparison and nothing computed it for 31 days.** Write-back step 12 states Amendment 10 as *"the brief's commit timestamp ≥ the session's last STATUS commit timestamp"* — two integers. **Third instance in six weeks of this desk's own named class:** KB-VIO-165 (enums "validated" by remembering — 11 rows violating, one for 109 days), KB-VIO-190/226 (a mechanical re-arm line inherited as a fresh judgement call — 3 sessions), now this. **When auditing this desk, do not ask "is there a rule?" — ask "is there a rule stated as an arithmetic comparison that nothing computes?"**
- **The failure mode has a timing bias that makes "remember to do it" the wrong remedy.** A tail step done from memory fails *precisely when the session ends badly* — crash, interrupt, context exhaustion — **which is exactly the population where the handoff surfaces matter most.** A discipline that holds on every good day and breaks on every bad one is not a control.
- **Guard correctness and guard wiring were tested separately, and both tests were available for free.** The check was falsified against the live *unfixed* repo state before being trusted (fired 3/3, rc=1), then re-run against the fixed state (rc=0, exercising the dirty-file branch); the wiring was proved by running `closeout_guard.py` and confirming the new contract appears in its RED list. `[[finding_guard_correctness_and_wiring_are_independent]]` · `[[finding_test_the_guard_not_just_the_guarded]]`
- **Dirty working-tree files count as fresh, and that is a design decision, not a shortcut.** `closeout_guard.py` runs *before* the session's commit, so comparing raw commit timestamps would flag every honest closeout — and **a guard that cries wolf on the correct path is one you learn to bypass**, which is the exact warning already written into `closeout_guard.py` about its non-blocking thesis check.
- **⚠️ The check compares VINTAGE, never CONTENT, and that limit is written into it.** A brief re-stamped with a fresh `As of:` over a stale body passes green. It catches the surface **left behind**, not the surface **refreshed badly**. `[[finding_header_edit_is_the_edit_most_mistaken_for_maintenance]]`
- **The crashed session's best decision was a refusal, and the crash did not cost it.** It found `TRADE.md` ARMED on a 64-day-old gate whose legs today's tape satisfies and **did not fix it** — standing an authorized gate down is an *authorization* change, not a staleness edit, and PROME relaying a recommendation is not the operator speaking. It wrote that reasoning into its commit message, where the recovery session found it. **Will's word arrived 63 minutes later; the edit took one minute.** `[[finding_relayed_recommendation_is_not_an_approval]]`

---

## 2026-09-04 (PM) — Five queued tool defects built in one pass; closeout guard now carries five blocking contracts and is green

**Trigger:** Will, after the crash-recovery and inbox sessions: *"Can we work on these"* — the four "code that should exist and doesn't" items I had listed as still hanging.

**What changed:**

1. **`canary_staleness.py` — COT graded on the publication SCHEDULE, not calendar age (KB-VIO-226).** CFTC TFF report dates are always Tuesdays released the *following* Friday 15:30 ET (fixed +3d lag), so a perfectly current ledger reads 10d old every Friday morning and the old `>9d` rule fired a **guaranteed false DARK once a week, forever**. New rule: expected = the latest Tuesday whose following-Friday 15:30 ET release has passed; **DARK iff the ledger's max date is older than that.** Zero free parameters. New `SCHEDULED` table + `expected_report_date()`; a `--selftest` mode with **14 checks in both directions**.
2. **`catalyst_countdown.py` — NYSE holiday table (2026–2027).** The counter was weekend-only and printed Labor Day (Mon 9/7) as **1 trading day** out from Fri 9/4. Now 0; CPI 9/11 went 5d→4d, FOMC 9/16 8d→7d. `HOLIDAY_COVERAGE` bounds the table and **warns** outside it rather than degrading silently. Half-days deliberately excluded (a 13:00 close is still a full session for a session count).
3. **`move.py` — phantom `GATE-VIO-116 re-open > 71.00` leg removed (KB-VIO-219).** Printed at every boot for ~7 weeks for a gate **RESOLVED 2026-07-16** that is not even a row in `PROME/GATES.tsv`. **F1 (72.41) stays** — the live MOVE re-arm, which shares the KB-VIO-116 id, and that shared id is why the dead leg survived.
4. **NEW `scripts/skew_integrity.py` (KB-VIO-241)** — `^SKEW` mirror integrity **at the moment of use**, comparing **values** cell-by-cell against CBOE at |Δ| > 0.005. Detects **both** modes (omission *and* disagreement). Fails **closed** (rc=2) on an unreachable endpoint. Emits a one-line verdict meant to be pasted beside the claim.
5. **NEW `scripts/twin_check.py` (KB-VIO-235)** — `CALENDAR.md` ⇄ `CATALYSTS.tsv`, and it **refuses to nominate a winner.** Wired **BLOCKING** into `closeout_guard.py`.

**Files touched:** `scripts/canary_staleness.py` · `scripts/catalyst_countdown.py` · `scripts/move.py` · `scripts/skew_integrity.py` (new) · `scripts/twin_check.py` (new) · `scripts/closeout_guard.py` · `CANARY_MAP.md` · `workbook/KB.tsv` · `MAINTENANCE.md`.

**Boot impact:** boot still 14/14 OK and **no longer prints the weekly COT false DARK**; countdown numbers shift by one across Labor Day; `move.py` prints 3 lines not 4. Closeout guard now has **five** blocking contracts (was three this morning) and returned **rc=0 — the first fully green closeout of the day.** `skew_integrity.py` is wired into **neither** boot nor closeout, deliberately (see Lessons).

**Lessons:**
- **🔑 None of the five needed new analysis.** Every remedy was already derived and written on a surface — the COT spec in full on `CANARY_MAP`, the holiday gap in SCRATCH, the phantom leg in STATUS *with its KB id*, both `^SKEW` modes in packets from RED. They sat as **prose** for between 2 days and 7 weeks. **The gap was never diagnosis; it was the hour of typing.** Same shape as KB-VIO-234, now n=6 in one day.
- **⚠️ The falsification earned its keep — `twin_check` shipped a bug and the falsification caught it before the commit.** Its first version read `date_class` from free prose, so a row correctly marked **CONFIRMED** was reported as **MODELED** — because its own supersession note read *"CORRECTED from ~9/22 MODELED to 2026-09-30."* **The supersession note contained the superseded token.** Fixed to parse an explicit `date_class` declaration, event field winning over notes, failing toward *unlabelled = not a tiebreaker* (the safe direction: wrongly withholding a tiebreak costs one glance; wrongly granting one propagates an error). `[[finding_marker_word_in_prose_disables_the_scanner_that_reads_for_it]]`
- **⚠️ Removing a false alarm risks removing the true one, so the COT selftest is CODE, not a run.** It asserts a genuinely-behind ledger still goes DARK (1 behind → DARK; 3 behind → DARK counting 3 publications) alongside the 15:29/15:30 boundary and the 9d-old-and-correct Thursday. A one-off manual check would have proved the alarm was quiet, never that it could still speak.
- **⛔ `skew_integrity.py` is deliberately NOT boot-wired, and that omission is the design.** Its whole argument is that a check run *before* the work does not bound the work — the defect **heals**, so the gap can open between boot and use. Wiring it to boot would recreate the false assurance it exists to refute. The standing rule lives on `CANARY_MAP`: run it when a `^SKEW` value is **consumed**, and record the verdict **with** the claim.
- **⚠️ Measurement discipline, because I got it wrong twice today:** `cmd | tail; echo $?` reports **tail's** exit code, not `cmd`'s. I mis-read `closeout_guard` as rc=0 when it was 1, and `skew_integrity` as rc=0 when it was 1. **Both times the tool was right and my measurement was wrong.** Measure exit codes without a pipe, or use `PIPESTATUS`.

---

## 2026-09-04 (PM, second) — External review found 4 defects in a "5/5 green" closeout; two new checks were materially under-specified

**Trigger:** Will routed a Codex review of the four latest VIOLET commits, 90 minutes after I closed out claiming five blocking contracts green. **All four findings reproduced.**

**What changed:**

1. **`canary_staleness.py` — the COT guard encoded a FALSE INVARIANT (finding #1, High).** I asserted a fixed Tue-report / Fri-release +3d lag and certified it *"zero free parameters, self-calibrating."* Per CFTC's published schedule, federal holidays move **both** ends: a **Monday** holiday slips the **report date** Tue→Wed; a **Friday** holiday slips the **release** to the following Monday. **Juneteenth (Fri 2026-06-19) and Christmas (Fri 2026-12-25) would each have produced a multi-day false DARK — the same failure direction as the bug I replaced.** Now: `FEDERAL_HOLIDAYS` table (**distinct from** the NYSE table in `catalyst_countdown.py` — Good Friday is NYSE-only, Columbus/Veterans are federal-only), holiday-aware `report_and_release()`, `HOLIDAY_COVERAGE` that **fails closed** outside it, and a **fail-safe**: one report behind *with a holiday in the window* is 🟡 **PENDING**, not 🔴 DARK; **two or more behind is DARK regardless** (no single holiday delays two releases). Selftest **14 → 24 checks**, holiday cases named as regressions.
2. **`twin_check.py` — returned GREEN on inconsistent twins (finding #2, High).** v1 ran only CATALYSTS→CALENDAR, let **one** calendar row satisfy **many** catalyst rows, never ran the reverse direction, and never flagged past-dated rows under `## ACTIVE FORWARD CATALYSTS`. Live proof: **8 catalyst rows vs 7 calendar rows at rc=0**, with **three August events sitting under the forward heading for 14 days** — while the check was **BLOCKING at closeout**, so the false green was material. Now bidirectional, **strict 1:1 claiming**, past-row detection on **both** surfaces. **6-scenario falsification; all six fire, baseline clean.**
3. **Data defects the fixed check then exposed** — three fired August rows moved from CALENDAR's forward section into **RESOLVED with grades**; the combined `Sep 16` row **split into two** (FOMC and the VIX quarterly expiry) so it maps 1:1 to `CATALYSTS.tsv`; the same three fired rows **pruned from `CATALYSTS.tsv`** per write-back step 10. Twins now **5:5**.
4. **Contradictory live state swept (finding #3, Medium)** — STATUS said the `move.py` phantom leg was still queued (two places), NEXUS_BRIEF told downstream readers both that fix and the holiday table were outstanding, and LAST_COMPLETION's GAPS line contradicted its own BUILT line.
5. **`writeback_order_check.py` gains a provenance half (finding #4, Medium).** The brief was stamped **"~14:3x ET"** and committed at **13:56** — 34 minutes in its own future — and cited STATUS commit `ef3e0be9c` when the latest was `ec5d05b69`. Now checked: the cited hash must be the current STATUS head, the brief's own commit, or a **`same-commit` marker verified after the fact**; and the As-of stamp may not post-date its own commit. **Both reproduce Codex's finding exactly.**
6. **STATUS rotated twice** on the read-cap budget (33,311 → 31,788 B); process narrative archived **byte-verbatim, crc-stamped and recomputed** (`064361a7`, `3d5af6f8`).

**Files touched:** `scripts/canary_staleness.py` · `scripts/twin_check.py` · `scripts/writeback_order_check.py` · `CALENDAR.md` · `workbook/CATALYSTS.tsv` · `workbook/KB.tsv` · `STATUS.md` · `SCRATCH.md` · `NEXUS_BRIEF.md` · `LAST_COMPLETION.md` · `CANARY_MAP.md` · `archive/STATUS_SESSION_LOG_2026-09-04.md` · `MAINTENANCE.md`.

**Boot impact:** none new — boot still 14/14. Closeout keeps five blocking contracts; two of them now actually enforce what they claimed to.

**Lessons:**
- **🔑 A SELFTEST PROVES THE CASES YOU ENUMERATED, NEVER THE CASE YOU DID NOT IMAGINE — AND THE ENUMERATION COMES FROM THE SAME HEAD THAT WROTE THE MODEL.** My 14 checks were real, passed, and covered only the weeks I had thought of. The holiday exception is **published on CFTC's own release-schedule page, which I never opened before asserting the invariant.** **I verified my arithmetic and never verified my premise.** This is the whole finding: a guard's test inherits the blind spot of its author, so a *green selftest* is evidence about internal consistency and almost none about the world.
- **⚠️ I spent the day building guards against unmechanized rules and then certified the result with an unchecked claim.** "5/5 green" and "zero free parameters" were both assertions about my own work that nothing tested. **The mechanisms were right; the certification of them was not.**
- **⚠️ FIXING ONE DIRECTION OF A SYMMETRIC CHECK LEAVES THE DEFECT ALIVE IN THE OTHER — and the review did not catch this half.** My corrected `twin_check` still silently skipped past-dated rows on the *CATALYSTS* side while reporting them on CALENDAR; both surfaces carried the **same** three fired rows. **Taking a reviewer's scope as the full scope would have left half the bug.** `[[finding_verify_recommended_fix_not_just_finding]]`
- **⚠️ The new stamp check shipped UNTRIPPABLE and was caught only by running it against the real defect:** its minute parser fell back to `00` on VIOLET's own `~14:3x` fuzzy stamps, so it could not fire on the format this desk actually writes. **Test a guard on the real artifact, not on a fixture you shaped.** `[[finding_banded_threshold_with_no_metric_surface_is_untrippable]]`
- **⚠️ Finding #3 is the limitation I had written into `writeback_order_check.py`'s own docstring that morning — *"it compares VINTAGE, never CONTENT"* — landing on its author the same day. Writing a limitation down bought exactly nothing.** The mechanizable part of "content" is now mechanized; the rest still is not, and the docstring still says so.
- **⚠️ My anchor splice deleted `UNLEDGERED` while rewriting `canary_staleness.py`** — `s[:i] + new + s[j:]` across a span containing an unrelated block. Caught by a `NameError` on the next run and restored verbatim from `HEAD`. This is `[[finding_anchor_splice_deletes_everything_between_nested_anchors]]`, which is **my own memory**, reproduced hours after citing it.

---

## 2026-09-04 (PM, third) — Review round 2: the correction was wrong too; three attempts at one guard, and the fix was LESS model

**Trigger:** A second Codex review of the correction pass. It confirmed the twin-check repair and found the rest overstated.

**What changed:**

1. **`canary_staleness.py` v4 — ALL CALENDAR SYNTHESIS REMOVED (KB-VIO-243).** My v3 asserted a **Monday federal holiday slips the CFTC report date Tue→Wed**. **That is fabricated.** CFTC shows **Tue 2024-09-03** and **Tue 2023-09-05** immediately after Labor Day, its 2026 calendar lists 9/11 as an ordinary release — and **`COT_VIX.tsv` itself contains `2026-05-26`, a Tuesday directly after Memorial Day.** The only non-Tuesday report dates in the whole ledger are two **Mondays**, the opposite direction. v4 keys solely on the ledger's observed cadence plus a grace window: **0 = nothing owed · 1 = PENDING (a delayed release and a missed pull are indistinguishable) · 2+ = DARK.** No holiday table, no release arithmetic.
2. **`writeback_order_check.py` — three fail-open holes closed.** (a) a numeric STATUS citation passed if it matched the brief's own commit **even when that commit never touched STATUS**; (b) a missing/malformed `As of:` stamp **silently skipped** validation, making deletion the cheapest way to pass; (c) **the whole check returned early on a dirty brief — and it is wired into `closeout_guard.py`, where the brief is ALWAYS dirty.** It ran green at boot and was **inert at exactly the moment it was meant to block.** All three falsified in the dirty (closeout) condition.
3. **RESEARCH QUEUE rebuilt from scratch** — it still carried **seven completed items as live**. My first sweep fixed the three sentences the reviewer quoted and left the list they sat in.
4. **`CALENDAR.md` and `LAST_COMPLETION.md`** corrected where they still asserted "no holiday table" and "zero free parameters, 14-check".
5. **9/1 COT ingested** (the real remedy for the live DARK): Lev Money **−26,258 / p51.9 · OI 410,574** vs **−30,143 / p42.3 [8/25]**. **The deepening stopped.** Dashboard row, matrix leg 🔴4 → 🟠3, convergence **26 → 25**.
6. **KB-VIO-242 marked CORRECTED** (its "all four fixed" claim was too strong); **KB-VIO-243** filed; STATUS rotated a third time (crc `d6091a4c`).

**Files touched:** `scripts/canary_staleness.py` · `scripts/writeback_order_check.py` · `STATUS.md` · `SCRATCH.md` · `NEXUS_BRIEF.md` · `LAST_COMPLETION.md` · `CALENDAR.md` · `workbook/KB.tsv` · `workbook/COT_VIX.tsv` · `archive/STATUS_SESSION_LOG_2026-09-04.md` · `MAINTENANCE.md`.

**Boot impact:** COT canary reads 🟢 with an explicit "nothing owed until <date>" note; boot still 14/14; closeout keeps five blocking contracts, one of which now actually runs on its own path.

**Lessons:**
- **🔑 A SELFTEST CANNOT FALSIFY THE PREMISE IT WAS DERIVED FROM.** All three wrong versions passed their own tests, because I wrote the tests from the same synthesized model as the code. **The count went 14 → 24 while the premise got *more* wrong** — so a rising green test count read as rising confidence and measured nothing. ⇒ **When a guard models an external schedule, the FIRST test must be against OBSERVED HISTORY, not the model.** The falsifying record was in my own ledger both times; I never queried it, because I was testing whether the code implemented my belief rather than whether my belief was true.
- **⇒ THE STRUCTURAL FIX WAS LESS MODEL, NOT A BETTER ONE.** Given a precise rule I keep getting wrong versus a loose rule derived from observed data, the loose one wins **here** — the failure this guard exists to catch persists and gets louder, while a false alarm is read once and dismissed. Detection latency on a weekly instrument is a cheap price; **a guard nobody believes is worth nothing.**
- **⚠️ CORRECT AND WIRED ARE INDEPENDENT, AND I TESTED ONLY THE FIRST.** The provenance check was demonstrably correct and demonstrably inert on the path it was installed on. **"Does it fire?" and "does it fire *here*?" are two questions.**
- **⚠️ A REVIEWER'S CITATIONS ARE A SAMPLE, NOT THE POPULATION.** My first sweep fixed exactly the lines quoted to me. `[[finding_ranked_head_sample_is_not_the_population]]`
- **⚠️ My own new assertions were wrong twice at the grace boundary (21d, 35d).** I corrected them by **deriving from the stated semantic**, not by reading the implementation's output — the distinction is the whole difference between a test and a transcript.

---

## 2026-09-04 (evening) — DAEDALUS profile refresh: five 🔴 closed; four of them were checks that ran and were not load-bearing

**Trigger:** DAEDALUS packet (Will-directed, 4 read-only Opus readers) — 18 findings, five 🔴, each with its line. Every one verified at my files before acting; **none declined.**

**What changed:**

1. **🔴1 `thesis/VIX_THESIS.md` tail rotated.** A present-tense *"Current status / Current posture"* block **dated 2026-06-10 sat at the end of a v4.0 file for 86 days** — live Iran/oil leg, a standing *"NO short-vol while the war leg is live"*, an invalidation of **CLOSE-AND-HOLD above 23** against a VIX of 14.32, and *"6/10 EOD is the next decision point."* Moved **verbatim** to `archive/THESIS_TAIL_2026-06-10_FROZEN.md` and replaced with **pointers, not a refresh** — a thesis should not carry a live state block at all; that is STATUS's job, and a second copy can only drift. Footer version corrected (read `v3.0 → v3.5` through two major bumps).
2. **🔴2 Convergence matrix reconciled and the checker made load-bearing.** **Three totals were live at once** — header 25, narrative 26, cells summing 33 — while `scripts/convergence_score.py` existed to catch exactly that and was **wired into nothing**. Two errors underneath: **cheap-tail, an OPPORTUNITY vector, was being summed into a STRESS score** (it inflates "stress" precisely when the market is calm), and the SKEW cell read `🔴 5` when a 5 requires `🔴🔴`, so badge and digit disagreed silently. Cheap-tail removed, **scale declared 10 × 5 = 50**, computed = declared = **29/50**. Checker hardened — **fails closed** on an unparsed row (v1 warned and *dropped* it, changing the denominator) and **cross-checks badge against digit** — then wired **BLOCKING**.
3. **🔴3 Six CANARY_MAP CURRENT cells, 31–38 days stale, refreshed** (MOVE, COT, JPY, OVX, cheap-tail, GEX). **Cheap-tail read `DORMANT 1/4` for 31 days while the live alert printed `OPEN 4/4` at every boot**; GEX carried `[HENRY 7/28]` **across a sign inversion**. Matcher widened — it required a **digits-only bracket**, so `[8/4 SETTLE]` and `[7/28 report]` were invisible and it saw **2 of 6**; year now picks the one minimising |age|; **a missing/unreadable map is now RED** instead of clean.
4. **🔴4 `MEMORY.md:168` rewritten.** It taught the Tue→Fri CFTC calendar **retracted at 17:28 the same day** — on a **boot whole-read**, while STATUS rotates.
5. **🔴5 Three guard holes closed and falsified.** (a) `closeout_guard.run()` returned `(0, "skipped")` for a **missing script** — deleting a guard certified the closeout; now rc 2 **CANNOT CERTIFY** (proved by hiding `twin_check.py`). (b) `boot.py` printed **"✓ ran cleanly"** for any stage exiting non-zero without a recognised marker — the case most needing a loud line got the quietest. (c) `move.py` ran without `--strict` on the boot path, so a **primary-source failure read as a clean stage**.
6. **🟠6 STATUS rotated a fourth time** (4 B of headroom): the graded POST-NFP detail (canonical in KB-VIO-233) and the **CROSS-AGENT SIGNALS table — a verbatim twin of `NEXUS_BRIEF.md`**, so rotation also fixed a one-source-of-truth violation. crc `08b5f907`, verbatim.
7. **🟡15 Eight summary/body contradictions swept** — "THREE SESSIONS" vs "SIX", the thesis-row count published as 12 / 20 / 29 on three surfaces (now stated **once**, from `thesis_bump_check`: 31 rows, 3 retractions), "deepened three reports running" against "the deepening STOPPED", a `~09:0x` footer on an evening commit.
8. **🟠/🟡 6–18 triaged with a per-row disposition** in `STATUS.md § RESEARCH QUEUE`, including **two DECLINED-BY-DESIGN with reasons** (outbox retirement is a routing change scoped out by `MESSAGING/`; an rc change on `implied_corr.py`'s documented fallback would put a routine source-switch on the blocking path). **D-Q1 and D-Q3 answered on the surface.**

**Files touched:** `thesis/VIX_THESIS.md` · `archive/THESIS_TAIL_2026-06-10_FROZEN.md` (new) · `CANARY_MAP.md` · `MEMORY.md` · `scripts/{closeout_guard,boot,canary_staleness,convergence_score}.py` · `STATUS.md` · `SCRATCH.md` · `NEXUS_BRIEF.md` · `LAST_COMPLETION.md` · `workbook/KB.tsv` · `board_log.tsv` · `archive/STATUS_SESSION_LOG_2026-09-04.md` · `MAINTENANCE.md`.

**Boot impact:** boot 14/14; a failing stage can no longer print a clean line; MOVE primary failure now surfaces as rc 1. Closeout carries **six** blocking contracts (added convergence arithmetic), and a **missing** guard script now blocks instead of certifying.

**Lessons:**
- **🔑 FOUR OF THE FIVE 🔴 ARE ONE SHAPE: A CHECK EXISTED, RAN, AND WAS NOT LOAD-BEARING.** The score checker was called by nothing; the CANARY_MAP matcher couldn't parse the cells I actually write; the closeout guard passed a missing check; boot passed an unparsed failure. **In every case the instrument was present, executed, and returned green over the very thing it was built for.**
- **⇒ "IS THERE A CHECK?" AND "DOES IT SEE MY DATA?" ARE DIFFERENT QUESTIONS, AND THE SECOND ONE DECAYS.** A matcher is written against the house style of the day it was written, and the house style keeps moving. **Audit a checker by feeding it the current artifact and counting what it FINDS against what is THERE — never by reading its source.**
- **⚠️ The cheap-tail cell is the sharpest instance this desk has produced: `DORMANT 1/4` on the map for 31 days while the live alert printed `OPEN 4/4` every morning.** Both surfaces mine, both read daily, and nothing compared them.
- **⚠️ The convergence fault was a CATEGORY error wearing an arithmetic disguise.** Summing an opportunity vector into a stress score makes the score rise as conditions get calmer. Three wrong totals are what made me look; the design was the thing that was wrong.
- **✅ Method worth copying from DAEDALUS: it pre-corrected its own readers** ("the LIQUID and TERRY packets ARE delivered; prediction #7 IS graded") so I did not chase three dead ends. **A multi-reader review that ships its own false positives, labelled, costs the recipient nothing.**

---

## 2026-09-04 (night) — Review round 3: five defects behind a fully green gate; the fix is coverage, not another sweep

**Trigger:** Third Codex review. Its closing line is the finding: *"the remaining defects are specifically outside current test coverage."* Every invoked test passed while five real defects sat where none of them looked.

**What changed:**

1. **NEW `scripts/surface_agreement.py`, BLOCKING (7th contract).** The convergence score was live as **29/50** on STATUS and a **superseded 26/55** in the brief's VIEW and SCRATCH, with LAST_COMPLETION narrating a superseded *"26 → 25"* beside it — **four surfaces, three numbers, guard green.** The new check requires a registered figure to read identically on STATUS · NEXUS_BRIEF · SCRATCH · LAST_COMPLETION. **This is the third recurrence of the summary/body class in one day and the first time it has been mechanized;** the two prior "sweeps" fixed exactly the instances a reviewer quoted.
2. **`CANARY_MAP` contract body rewritten.** It still **taught** the retracted CFTC model — *"DARK after nine days"*, the Monday→Wednesday report shift, the deleted holiday table, the obsolete one-cycle-is-DARK behaviour — while the code had moved to cadence+grace with one cycle = PENDING. The stale "FIXED" banner was replaced with the three-attempt record.
3. **`check_map_states()` — the comparison the docstring only promised.** `check_map_agreement`'s docstring claimed it compared each map date against the backing ledger's newest row; **it never opened a ledger.** So the 31-day cheap-tail DORMANT-vs-OPEN defect was **still uncovered after being "fixed."** Now: for canaries whose ledger carries a `state` column, compare the state the **map** asserts against the state the **ledger** holds.
4. **Multi-surface stamp check.** Future timestamps reappeared **within one commit** of the last fix (18:19 commit, 19:xx labels) because the provenance check covered NEXUS_BRIEF only. Now STATUS and CANARY_MAP too.
5. **`same-commit` no longer passes open on a dirty closeout** — if the brief is dirty, STATUS must be dirty too, or they provably are not landing together.
6. **STATUS:87/:97 contradiction closed** ("deepening STOPPED" vs "deepened three reports running").

**Files touched:** `scripts/surface_agreement.py` (new) · `scripts/canary_staleness.py` · `scripts/writeback_order_check.py` · `scripts/closeout_guard.py` · `CANARY_MAP.md` · `STATUS.md` · `SCRATCH.md` · `NEXUS_BRIEF.md` · `LAST_COMPLETION.md` · `workbook/KB.tsv` · `MAINTENANCE.md`.

**Boot impact:** boot 14/14, no failed stages. Closeout now carries **seven** blocking contracts.

**Lessons:**
- **🔑 "ALL TESTS PASS" IS A STATEMENT ABOUT COVERAGE, NOT CORRECTNESS — AND I QUOTED IT AS THE SECOND, THREE TIMES TODAY.** Three review rounds each found real defects behind a fully green gate. **The gate was never lying; it was answering a narrower question than the one I reported.** ⇒ **When claiming a clean gate, state what it covers.** "Six contracts green" means nothing without "and here is what none of them reads."
- **⚠️ A FALSE DOCSTRING IS WORSE THAN A MISSING CHECK.** It is what a reader trusts *instead of* looking — and I had read this one twice while auditing its own file.
- **🔑 THE NEW MAP↔LEDGER CHECK PAID FOR ITSELF ON ITS FIRST REAL RUN, ON A MARKET FACT:** CANARY_MAP and STATUS both said **OVX FIRE** while `OVX.tsv`'s 9/4 settle said **WATCH** (ratio 3.09 vs the p95 line 3.21). **I had published an intraday tick as the state of a canary that grades on the settle.** Both surfaces were fresh; one was wrong. No age check can see that.
- **⚠️ THREE OF MY NEW CHECKS SHIPPED INERT OR NOISY, AND ONLY FALSIFICATION FOUND IT** — an option strike list (`October 30/35/60 calls`) read as a convergence score; the date `9/4` read as an FT-10 count; a state comparison whose membership test could never fire; a JPY **threshold label** read as an asserted state. **Every one was caught by running the check against the real artifact with the real defect injected. None by reading the code.**
- **⚠️ And the cross-surface check immediately caught my own new prose** — I restated the retracted 26/55 without a history marker while *describing* the defect. **Writing about a dead number reintroduces it.** Fixed the phrasing, not the check.
