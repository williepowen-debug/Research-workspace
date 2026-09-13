# WQ-240 — closeout simplification · L338 sizing decision · verifiable completion
**RULED + IMPLEMENTED 2026-09-12 21:2x–21:4x ET** (LAPTOP `WilliePOwen`, session `prome-cg`) · **Will-directed**, four outcomes and five validation cases given verbatim in-session.
**⛔ This is the ONE record for this change.** `CLOSEOUT.md` carries no historical explanation; amendment history is `git log -p -- PROME/CLOSEOUT.md`.

**Success measure, in Will's words: *less repeated writing and a trustworthy final result — not simply fewer bytes or more passing checks.*** The byte figures below are consequences, not the goal.

---

## §0 Acceptance conditions — written before the edit (WQ-229)

**① Update facts once**
- A1. `[C1]` Each fact has exactly ONE owning surface, named in one table; every other mention is a pointer.
- A2. `[C1]` The targeted-update test (*does the boot path already reach it?*) governs **every tier**, not Light alone.
- A3. `[C1]` Generated views are preserved and **regenerated**, never hand-restated.
- A4. `[C1]` A surface whose column did not change gets a **stated no-op**, never silence and never a rewrite.

**② L338 sizing decision, made while editing**
- B1. `[INV]` The routine sequence stays concise; conditional procedures sit behind **explicit pointers**.
- B2. `[INV]` No live procedure is lost — every cold section is reachable from the hot file.
- B3. `[ART]` Historical explanation lives in existing records, not in the manual.
- B4. ⛔ **Not a rotation.** Will: *"Don't start with another rotation pass."* Rotation archives; a split keeps every procedure live and reachable.

**③ Audit the finished candidate**
- C1. `[C3]` The candidate is COMPLETE before review: all source edits, all checks that can still produce edits, and local generation.
- C2. `[C3]` The reviewed **content identity** is recorded, not merely the path list.
- C3. `[C3]` If a correction changes the candidate, the changed portion is re-reviewed and affected outputs regenerated.
- C4. `[C3]` The committed contents are verified to match the reviewed result.
- C5. `[C3]` No manifest ⇒ **UNKNOWN, never clean**.

**④ Finish delivery explicitly**
- D1. `[C4]` Publication prerequisites are checked **early**, not at the render.
- D2. `[C4]` COMMITTED · PUSHED · PUBLISHED are reported as three distinct states.
- D3. `[C4]` A publication that cannot finish is reported as **PARTIAL with its concrete blocker** — ⛔ never silently waived because it became inconvenient.

**Preserved invariants (Will, explicit):** live obligations · existing authority boundaries · **fired-unexecuted protection** · required publication. `[INV]`

**Neighbour categories (WQ-229):** ordinary `[C1]` · **overlap** `[C5]` — another desk's dirty path adjacent to PROME's reviewed set · wrong owner `[C5]` · missing information `[C3]` — the no-manifest case · concurrent activity `[C5]`.

---

## §1 L338 — the sizing decision, and why it is a SPLIT

**Decision: hot/cold split. `PROME/CLOSEOUT.md` keeps the routine sequence; `PROME/CLOSEOUT_PROCEDURES.md` holds what runs only on a trigger.**

⛔ **Rotation was the wrong instrument and Will named why.** Rotation moves text to an archive, where it stops being canon. Everything in this file is still live procedure — byte-flow recipes, the blind-reader stop rule, Chunk-3 triggers, skip rules. **The problem was never that the content was dead; it was that the sequence a session actually executes was buried inside procedures most closeouts never run.** A split fixes the reading problem without retiring anything.

**Guard against the failure a split invites:** a cold file nobody points at is dead text. Every cold section is asserted reachable from the hot file (`test_every_cold_section_is_reachable_by_an_explicit_pointer`).

**L338's own legs, dispositioned:** (a) the `wq_ledger` question — the mandated step is sufficient; it stays in the routine. (b) the sizing decision — **taken here.** (c) the WQ-232 rule text — now governs all tiers and is exercised by C1. (d) `:46`/`:118` mandating a SCRATCH "full rewrite" that `:29` had removed — ⛔ **dissolved, not patched: the three surfaces became one table.** (e) no ledger rows owed. (f) unchanged. (g) the dashboard build must SUCCEED, not merely run — carried by the existing L339 receipt guard, which the gate already enforces.

⚠️ **Out of scope by Will's instruction** (*"Corrections such as D-49 should proceed independently of archival work"* / *"Keep unrelated repairs outside this task"*): the `ACTIVE_DECISIONS:38` D-49 contradiction, and the three pre-existing `docket_view --check` divergences in SCRATCH prose that this work's own test run surfaced. **Both recorded here, neither touched.**

---

## §2 What changed

| Surface | Change |
|---|---|
| `PROME/CLOSEOUT.md` | Routine only. The symmetry table and the "Prome Write-Back Contract" — which stated the same rules twice in different words — **replaced by ONE "ONE HOME PER FACT" table**. Chunks 1–4 became a 12-step ordered routine. New § Delivery. |
| `PROME/CLOSEOUT_PROCEDURES.md` | **NEW.** Byte-flow + rotation recipes (incl. blind-reader) · Chunk 3 triggers · Skip rules · Cross-session rules · closeout-class memories. Moved **verbatim**. |
| `.claude/skills/closeout/SKILL.md` ×2 | Rewritten as an index over the new order; both copies one unit, parity green. |
| `PROME/tools/argus_scope.py` | `--record-review` freezes the reviewed candidate's **content identity** (sha256 per path); `--verify-review` compares the tree against it. rc 0 unchanged · 1 changed/unreviewed · **2 CANNOT-EVALUATE**. |
| `PROME/tools/prome_gate.py` | `ARGUS review manifest (content, not paths)` — **BLOCKING** when the candidate changed after the audit; advisory UNKNOWN when no review was recorded (Light/Bounce run none). `publication prerequisites (Deck explainer coverage)` — the mechanical half of D1. |

**Replaced, not appended:** the duplicated write-back table is gone rather than annotated; the Light-only WQ-232 rule is gone rather than supplemented.

---

## §3 Validation — Will's five cases

| Case | Result |
|---|---|
| **1** Standard closeout changes one DOCKET obligation: views update, no narrative copies | ✅ `Case1` ×3 — the generator owns its block on a fixture, is idempotent, touches nothing outside the markers; the manual forbids restating a registered row; the every-tier rule is installed and the Light-only text is gone |
| **2** A fact changes late: the final candidate has no contradictory current claims | ✅ `Case2` ×2 — step 7 is declared the last step that may edit, and the test asserts the freeze comes **after** it by position in the file |
| **3** Content changes after ARGUS reviews | ✅ `Case3` ×7 — changed content fails closed · a path added after review reads UNREVIEWED · a deleted reviewed path is a change · no manifest is UNKNOWN not clean · **the prescribed remedy works** (fix → re-freeze → verify) · the gate treats it as BLOCKING |
| **4** Publication fails | ✅ `Case4` ×3 — three states + PARTIAL + concrete blocker in the manual; prerequisites precede the render in **both** manual and runner (positional assert); the gate carries the mechanical prerequisite |
| **5** Another agent has dirty files | ✅ `Case5` ×3 — exact-path commits; the foreign-work rule survives; **a foreign path edited after the freeze does not fail PROME's review** |
| — Preserved invariants | ✅ `PreservedInvariants` ×5 — fired-unexecuted BLOCKING in manual **and** gate · authority boundaries in the cold file · publication still Standard+ mandatory · every cold section reachable · hot file under its line |

**23 tests, all passing.** ⛔ **The falsification figure this line first carried (*"7/7 both directions"*) was measured on an earlier draft and was stale by the time it shipped — ARGUS re-measured it and it was wrong.** Re-measured at the end of the patch, per file reverted to `HEAD` in turn: `CLOSEOUT.md` → **2 not-OK here, 5 in the CLI suite**; `argus_scope.py` → **12 in the CLI suite**; `prome_gate.py` → **8 in the CLI suite**. Command: revert one file, run both suites, count `^(FAIL|ERROR):`.

⚠️ **One defect of my own, in this task, caught by its own run:** the first Case-1 test asserted that the **live** `SCRATCH.md` was divergence-free. It failed on three pre-existing divergences it was never written to police — a test pinned to a live surface, which rots on the next edit (`[[finding_regression_test_pinned_to_a_live_surface_rots_on_the_next_edit]]`). Rewritten as a fixture property test.

---

## §4 Residue — declared, not dissolved
- **R1.** The "live artifact viewed this session" half of D1 is a **harness fact the repo cannot see**. The gate carries only the explainer-coverage half; the rest is procedural placement (Pre-closeout 0b). ⛔ Stated rather than claimed as mechanized.
- **R2.** ⛔ **SUPERSEDED by §5 and rewritten rather than left standing beside its own correction** (`finding_correction_beside_an_instruction_leaves_two_live_instructions` — ARGUS found the pre-patch text and its fix both live in this record). **What actually remains:** the tier is **self-declared**. `--tier` is optional, so a Standard closeout that omits it is not held to the review requirement. The gate now says so in its own line (*"no --tier given: review requirement NOT enforced"*), which makes the gap visible but does not close it: **no instrument knows what tier a session ran.**
- **R3.** Three pre-existing `docket_view --check` divergences in SCRATCH prose, surfaced by this work and **left alone** per Will's scope instruction.
- **R4.** `ACTIVE_DECISIONS:38` D-49 contradiction — unchanged, proceeds independently.
- **R5.** The cold file was moved verbatim and **has had no cold read**; its content is unchanged text, but its new framing has not been read by a stranger.

**Four-state completion note (WQ-229):** **IMPLEMENTED** · **TESTED** (23, falsified both directions) · ⛔ **NOT INDEPENDENTLY VERIFIED** — this record's own audit is the next closeout's ARGUS run under the new order, which is also the first live exercise of the freeze/verify loop · **STILL UNRESOLVED:** R1, R2.


---

## §5 PATCH — finishing the review mechanism (Will-directed 2026-09-12 21:41, same record)

**Will kept the one-home-per-fact table and the hot/cold split and named five defects in the mechanism I shipped alongside them. All five reproduced before being fixed.** ⛔ **The sharpest one is that my own delivery receipt for §1–§4 read `verdict: REVIEWED` for a change ARGUS never saw** — the tool asserted an audit at FREEZE time, and it did so on the very commit that introduced it.

| # | Defect, reproduced | Fix |
|---|---|---|
| 1 | `--verify-review` never passed `paths`, so unreviewed-addition detection was **dead code**; and it hashed the **working tree** while the manual claimed it verified the committed contents | `--paths` and `--ref` are now real CLI arguments; step 10 passes the exact intended commit paths and `--ref HEAD`. `_committed_content_id()` reads `git show <ref>:<path>` |
| 2 | The receipt and the baseline record were **inside their own candidate** — the baseline is rewritten *after* the commit, so the next verify was guaranteed to fail; and a prior session's manifest read as **this** session's failure | `RECEIPT_PATHS` are excluded from every manifest. A manifest records the baseline it was frozen against; a different baseline ⇒ **CANNOT-EVALUATE "PRIOR closeout"**, never a failure |
| 3 | Freezing wrote `REVIEWED` | `--record-review` writes **`FROZEN`**; only `--mark-reviewed` writes `REVIEWED`, and it **refuses** if the candidate moved. The gate takes `--tier`: at standard/heavy, missing · unevaluable · **merely-FROZEN** all BLOCK |
| 4 | Step 10 rendered **after** the declared last editing step, and renders write tracked snapshots (`dashboard_state.json`, `brief_snapshot.json`, `brief_changes.jsonl`, `artifacts/*.html`) | **All generation moved to step 7**, before the freeze. Step 11 only **publishes** artifacts already generated and verified |
| 5 | Tests drove the library, not the CLI — which is precisely where the wiring defects lived | New suite runs the **real CLI in throwaway git repos with real commits** |

**Also fixed, from ARGUS's own earlier ⚠️:** `.claude/skills/**` is now `OWNED` in `AUDIT_PERIMETER.tsv`. Both boot and closeout runner copies are in review coverage — previously only the `PROME/` copy was, so half of a unit the parity gate treats as one could ship unreviewed.

**Validation: the CLI suite now stands at 28 tests** (21 at first delivery, +7 in the patch below). Includes two consecutive closeouts and the edited-then-reverted case that only `--ref HEAD` can catch. ⛔ **The "full suite 195 / 2 pre-existing failures" receipt was wrong twice over:** `unittest discover` silently fails to load `test_spawn_list_fail_closed.py` and counts that loader error as a failing test. Measured per file with `python3 <file>`: **198 across the 10 unittest suites, plus 15 in `test_spawn_list_fail_closed.py`'s own harness** (which contributes 0 to the 198 — it is not unittest-based, which is also why `discover` cannot load it). **One file not-OK: `test_heartbeat_projection.py`, pre-existing.** There is ONE pre-existing failure, not two. ⚠️ The count differs by runner (`discover` reports 202); the method is part of the receipt.

⚠️ **Two of my own §3 tests failed after this patch** — they pinned exact manual wording that the patch correctly reworded. Rewritten to assert **order** rather than sentences. That is the same live-surface brittleness §3 already recorded, reappearing one level down in the tests written to catch it.

**Four-state note:** **IMPLEMENTED** · **TESTED** (51 across the two WQ-240 suites; 198 executed fleet-wide, 1 pre-existing failure) · ✅ **INDEPENDENTLY REVIEWED** — ARGUS audited the frozen candidate and returned **7 ❌ / 7 ⚠️ over 43 claims**; all 7 ❌ are applied below · ⛔ **STILL UNRESOLVED:** the self-declared tier (R2).

---

## §6 ARGUS findings on this patch — 7 ❌, all applied

⛔ **The control had a demonstrated bypass and ARGUS found it, not me.** `--mark-reviewed` and the closeout gate both called `verify_review()` **with no path list**, so a file created after the freeze passed the promotion AND the `--tier standard` gate; only the post-commit check saw it. **Fix: with no list supplied the verifier now falls back to the tool's OWN computed scope**, so every caller detects additions. Reproduced before and after — promotion now returns `REFUSED`, the gate `🔴 BLOCKING`.

| # | Finding | Applied |
|---|---|---|
| 1 | The ⚡ block's `grep -c brief_ / WQ_EXPLAINERS / argus_baseline` receipt read `0,0,0`, and **this very change made it `0,3,0`** by adding a gate check that reads `WQ_EXPLAINERS.tsv` | the whole block was already replaced by a pointer; the stale receipt is gone |
| 2 | "Full suite 195 / 2 pre-existing failures" | re-measured: **198 executed, 1 pre-existing failure** |
| 3 | "23 tests falsified 7/7 both directions" (Will-facing) | re-measured per reverted file |
| 4 | "LAST step that may write anything tracked" — contradicted by steps 8 and 12, which write two tracked receipts | reworded to *inside the reviewed candidate*, naming the two exceptions and why they are exempt |
| 5 | **The addition bypass** (above) | verifier falls back to computed scope |
| 6 | The two tier tests asserted on the printed severity **label**, which appears on passes too | already rewritten to construct each condition from a fixture and assert `aggregate_rc` |
| 7 | §4 R2 declared as UNRESOLVED the limit §5 had fixed | R2 rewritten to the surviving limit only |

**Two ⚠️ taken as well, both class fixes rather than the named instance:** `.claude/agents/**` is now OWNED — carving out only `argus.md` left `coldreader.md` and `anvil.md` excluded on the identical argument (`finding_hand_fixing_named_rows_is_not_fixing_the_class`); and an untiered gate run now states that the review requirement is unenforced instead of passing quietly.

⚠️ **Carried, not fixed:** step 7 calls `will_handbook.py`, which **makes a git commit** via `will_brief.py` auto-persist — a stranger reading "generation" would not expect a commit. Named here; the sequence is unchanged. And both WQ-240 suites still read the live manual to assert its order; that is deliberate (they assert the *installed* rule) but it is a live-surface dependency and is declared.

**Delta re-review (ARGUS, second pass over the changed portion only): all 7 fixes HOLD at the artifact, 2 new ❌ — and both were the SAME defect as fix 4, untravelled.** The step-7 scope correction landed in the manual and did **not** reach (a) the ONE-HOME table cell, which still taught *"renders run after"* the gate — the exact ordering the ⚡ block above it names as the defect — or (b) either runner copy, which kept the unscoped *"may write anything"* claim fix 4 had just declared false. **Two live orderings and two live scope claims, created BY the repair.** `[[finding_an_amendment_read_for_one_item_leaves_the_others_derived_from_the_original_live]]` — both applied.

⚠️ **Carried from the delta re-review, not fixed:** running the full suite from the repo root **mutates the candidate after the freeze** — `test_heartbeat_projection.py`'s failed-render test patches `STATE_PATH` and `argv` but not `fd.BUILD_PATH`, so `fleet_dashboard.main()` writes the live gate-read receipt `PROME/tools/dashboard_build.json` with `ok:false`. It was restored before this commit. ⛔ **Left unfixed deliberately** — that suite is the one pre-existing failure and is outside this task's scope — but it is a real interaction with the new mechanism, and **the new fallback is what surfaced it** (`--verify-review` reported `UNREVIEWED: PROME/tools/dashboard_build.json`). Registered rather than patched.

⚠️ **This session's recurring defect, now four instances:** tests pinned to exact prose, breaking when the prose was correctly reworded. Each was rewritten to assert **order or commands** instead of sentences. The last two were the suite catching my own behaviour change — which is the suite working, not failing.
