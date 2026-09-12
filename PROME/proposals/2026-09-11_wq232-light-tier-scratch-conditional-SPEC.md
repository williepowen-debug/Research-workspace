# WQ-232 — Light-tier SCRATCH: conditional targeted update, not a mandated full rewrite

**Status:** SPEC, ready to apply. **NOT APPLIED** — `PROME/CLOSEOUT.md` is closed for the
session (WQ-178: third read spent, residue declared). First edit of the next session.
**Drafted:** 2026-09-11 21:0x ET, session `prome-d2`. **Source:** CODEX external review.

---

## Part 1 — Corrections to claims this session made to Will

Five claims of mine were wrong or overstated. All verified at the artifacts before recording.

| # | What I said | Correct |
|---|---|---|
| 1 | "Fleet-Ops skippable within 72h — the vintage advisory is the backstop" | **Unsafe as stated.** The advisory measures AGE, not agreement; a dashboard built an hour ago can already disagree with changed gates or positions. Skipping needs a freshness window **AND** unchanged relevant inputs. This is `[[finding_freshness_check_cannot_catch_a_fresh_lie]]` — the lesson BOOT.md already cites for the position-agreement gate, and I made the error anyway. |
| 2 | "The Helm feed is append-only, so skipping loses nothing" | **False for unobserved intermediate changes.** `will_brief.py:369` `update_changes` reads the SAVED snapshot and diffs it against the current one. A gate going LIVE → FIRED → LIVE between builds diffs as LIVE → LIVE and records nothing. Append-only storage preserves *recorded* events; it cannot recover events never observed. ⚠️ **The feed's contract — net change vs intervening events — is UNSETTLED and must be settled before its cadence is touched.** |
| 3 | "Deck: 4 of 24 rebuilds had no input change" | **Provisional — wrong dependency set.** `decision_deck.py:282` `parse_docket(today)` computes days-to-deadline from the clock; `:307` `days_dark(desk)` derives desk inactivity from git history + the clock. Deck content changes with NO edit to any queue file. The measure keyed on files-in-the-same-commit, which cannot see either. Needs the complete dependency set and a comparison against the PREVIOUS BUILD. |
| 4 | "Churn says no — SCRATCH is not being fully rewritten" | **Overstated.** Git records the resulting difference. A full rewrite that preserves half the text produces the same diff as half edited in place. The diff is consistent with either; it does not discriminate. Withdrawing the causal claim was right; asserting its negation was not. |
| 5 | "INDEPENDENTLY VERIFIED as text only" | **Still too strong.** Three reviews followed by MY fixes do not verify those fixes — the final round was never read. Accurate: **reviewed; reported findings corrected; final corrections and live execution NOT independently verified.** Gate PASS and identical runner copies establish narrower properties. |

### Correction to the ATTENTION raised to Will

I reported: *"`prome_gate.py` has NO `wq_ledger` check — covered by no gate run at all."*
**Literally true about the aggregate gate, misleading about coverage.** `CLOSEOUT.md:54`
mandates `wq_ledger.py sync` then `check` (**rc 0 required**) at the WQ LEDGER symmetry row.
The ledger IS checked by a mandated step; it is absent from the AGGREGATE gate only.
⚠️ Absence from the aggregate does not prove the artifact is unchecked. It stays a **separate,
open finding** — whether it belongs in the aggregate — not a defect in this repair.
⛔ The committed canon sentence still carries the overstatement; per root canon a damaged
message is never rewritten, so the correction rides the NEXT commit.

## Part 2 — The change

**Boundary: Light tier only. Publication cadence is NOT touched** — corrections 1–3 show the
three publication dependencies are not yet understood well enough to redesign together.

**Now** — `CLOSEOUT.md` tier table: `| **Light** | … | SCRATCH full rewrite + STATUS surgical |`
against `CLOSEOUT.md:91`: *"if no owner state changed, do not write back — state bloat is worse
than a quiet closeout."*

**Proposed** — Light tier performs a **targeted SCRATCH update conditional on changed
next-session information**, never a mandated full rewrite.

**Preserve unconditionally** (write these whether or not anything else changed):
a new **obligation** · a new **blocker** · a **decision** taken or owed · the **resume pointer**
(★ NEXT entry point). If none changed, the stated no-op is the correct closeout.

**Explicitly out of scope:** the generated blocks (`DOCKET-VIEW`, `WILLQ-VIEW`) keep their own
regeneration rules; STATUS stays surgical; Bounce and Standard/Heavy unchanged.

**Acceptance conditions**
- **A1** No obligation, blocker, decision or resume pointer that changed this session is absent
  from SCRATCH after a Light closeout.
- **A2** A Light session that changed none of the four writes no SCRATCH narrative at all, and
  says so explicitly rather than silently.
- **A3** The tier table and `:91` state one rule; neither contradicts the other. (This is the
  defect being fixed — verify BOTH directions, not just the table.)
- **A4** No change to Bounce, Standard, Heavy, or to any publication cadence.

**Neighbour tests (WQ-229 — considered):** *ordinary* — a Light session that changed one
obligation writes one line, not a rewrite · *overlap* — a fact that is both an obligation and a
resume pointer is written once, in the owning section · *wrong owner* — a blocker owned by
another desk is a pointer, never a restatement of their state · *missing information* — an
obligation whose owner is unknown is still written, marked UNKNOWN, never dropped for tidiness ·
*concurrent activity* — a Light closeout racing another session's SCRATCH write is the existing
pathspec/index problem and is NOT in scope here.

## Completion state
**NOT IMPLEMENTED. NOT REVIEWED.** No blind read has seen this text. It is the next session's
first edit, and it needs its own plan read before it touches `CLOSEOUT.md`.

---

## APPLIED 2026-09-11 21:0x ET — validation record

**Will-directed** (*"Implement and validate only the Light-tier SCRATCH change"*), which overrides
this session's WQ-178 file-closed state on `CLOSEOUT.md`. Publication cadence and every other
state file untouched, as instructed.

### The rule as applied
One test — **does the boot path already reach it?** Registered in `DOCKET.tsv` / `WILL_QUEUE.md`
§ OPEN / `GATES.tsv` ⇒ a generator or gate check reaches it ⇒ **SCRATCH does not restate it**.
Registered nowhere, or the ★ NEXT resume pointer (which has no generator) ⇒ **SCRATCH writes it.**
Nothing in those five rows changed ⇒ **stated no-op, no narrative.**

### What was tested — disposable fixtures, all four PASS
| # | Scenario | Method | Result |
|---|---|---|---|
| C | unchanged session | re-ran `docket_view.py --write` on an unchanged DOCKET into a SCRATCH copy | **byte-identical** ⇒ no SCRATCH edit required |
| A | new obligation, registered in DOCKET, **no** SCRATCH narrative | appended fixture row `…-ZQ7` to a DOCKET copy, regenerated | **surfaces** in the generated block |
| D | new decision, registered in WILL_QUEUE, **no** SCRATCH narrative | inserted fixture row `WQ-899` into a queue copy, ran `willq_view.py --queue` | **surfaces**, 1 occurrence **inside** the markers |
| B | same obligation registered **nowhere** | regenerated against unmodified sources | **invisible to every generator** ⇒ SCRATCH is its only carrier |

A+D establish that registered items need no SCRATCH copy; B establishes the floor that keeps the
rule from silently dropping things; C establishes the no-op. No repo file was touched by any test.

### What this removes from an ordinary session
The **mandated SCRATCH full rewrite at Light tier**. Replaced by: write unregistered items and a
changed resume pointer, or state a no-op. It removes a rewrite, not a check.

### Remaining limitations — five, none closed
1. ⚠️ **This change ADDED 1,962 B to `CLOSEOUT.md`, now 30,176 B = 92.7% of the 32,550 B read cap
   (headroom 2,374 B).** A rule that reduces closeout work cost bytes on a capped manual. The
   saving is in operations; the price is in a surface that is read whole.
2. **Fixture-validated, NOT execution-validated.** No Light closeout has run under this rule.
   A reading or fixture pass verifies mechanism; only execution verifies executability.
3. **The test assumes the generators actually run.** If `docket_view.py --write` / `willq_view.py
   --write` are skipped, a registered item is NOT discoverable and the rule silently under-writes.
   It leans entirely on Chunk 1's regeneration steps.
4. **Nothing mechanically detects "registered nowhere."** That judgment is PROME's each time; no
   check fires when an unregistered obligation goes unwritten.
5. **Not independently reviewed.** No plan read and no result read has seen this rule's text.
