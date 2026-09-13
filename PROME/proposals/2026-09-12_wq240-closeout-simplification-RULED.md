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

**23 tests, all passing. Falsified in both directions:** against the pre-change `argus_scope.py` → **7 errors**; against the pre-change `CLOSEOUT.md` → **7 failures**. A suite that passes against the old code would be measuring nothing.

⚠️ **One defect of my own, in this task, caught by its own run:** the first Case-1 test asserted that the **live** `SCRATCH.md` was divergence-free. It failed on three pre-existing divergences it was never written to police — a test pinned to a live surface, which rots on the next edit (`[[finding_regression_test_pinned_to_a_live_surface_rots_on_the_next_edit]]`). Rewritten as a fixture property test.

---

## §4 Residue — declared, not dissolved
- **R1.** The "live artifact viewed this session" half of D1 is a **harness fact the repo cannot see**. The gate carries only the explainer-coverage half; the rest is procedural placement (Pre-closeout 0b). ⛔ Stated rather than claimed as mechanized.
- **R2.** `ARGUS review manifest` is advisory at rc 2 so Light/Bounce do not false-block. A Standard closeout that simply never records a review therefore passes — **the tier is not machine-known.** The honest limit of this control.
- **R3.** Three pre-existing `docket_view --check` divergences in SCRATCH prose, surfaced by this work and **left alone** per Will's scope instruction.
- **R4.** `ACTIVE_DECISIONS:38` D-49 contradiction — unchanged, proceeds independently.
- **R5.** The cold file was moved verbatim and **has had no cold read**; its content is unchanged text, but its new framing has not been read by a stranger.

**Four-state completion note (WQ-229):** **IMPLEMENTED** · **TESTED** (23, falsified both directions) · ⛔ **NOT INDEPENDENTLY VERIFIED** — this record's own audit is the next closeout's ARGUS run under the new order, which is also the first live exercise of the freeze/verify loop · **STILL UNRESOLVED:** R1, R2.
