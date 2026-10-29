# LABOR LESSONS archive — L-30 worked case + addendum (rotated verbatim 2026-10-28 when L-34 was written; HOT keeps the 3 most recent in full)

## L-30 — "Verified in git" names an ARTIFACT, and the artifact I verified against did not exist when the value I was verifying was set

**Bought 2026-09-07, on my own calibration record, while sourcing a routine backfill.**

`PREDICTIONS_SCOREBOARD.md` §A scores every prediction at its **as-made** confidence, says so in bold, explains *why* in three sentences, and states that the as-made was **"verified in git … not read off the current ledger value."** All of that was true. **Four of twelve rows were still scored at a walked-down number**, and the book's headline Brier was **0.299 when it should have been 0.342**.

| | |
|---|---|
| **What I verified against** | `workbook/PREDICTIONS.tsv` |
| **When that file was created** | **2026-03-04**, by a fleet-wide bulk seeding for 24 agents |
| **What the seeding stamped** | `Date_Made = 2026-02-18` on **seven** LABOR rows at once |
| **When six of those rows were actually live** | **2026-02-02**, in `STATUS.md`, at their true as-made values |
| **What a walk-down between 2/02 and 3/04 does** | it is captured by the seeding **as if it were the registration value** |

**So the verification could not have failed.** The ledger is downstream of the registration surface, and every later commit of it agrees with the first — which is what "verified across commits `b50c6ada`/`0838327f`" actually measured: **agreement among vintages that all postdate the event.** Corrections: **LAB-02 65→70 · LAB-05 55→70 · LAB-07 65→60 · LAB-13 30→55.**

⇒ **The rule: "verified" is a two-part claim — the METHOD and the ARTIFACT — and only the method gets stated.** Before writing *verified*, name the artifact and ask **"did this artifact exist, in this form, at the moment the value I am checking was set?"** If it was created later, agreement inside it is not evidence about the event.

⚠️ **The three second-order costs, because the number was never the worst of it.** (1) It changed **sentences about my own conduct**: LAB-05 at a walked-down 55% read as *"mild overconfidence on a coin-flip call"*; at its as-made 70% it is a high-conviction single-firm miss. (2) It **manufactured a finding**: "LAB-17 and LAB-13 are two consecutive correctly-hedged threshold calls" was the one genuinely new positive result in two months, and **LAB-13 was never a hedge**. (3) It **understated the book's central regularity** — 0-for-4 at ≥60%, not 0-for-5 — *in the very sentence used to justify a reprice*, which is L-25 one level down.

🔒 **Mechanical fix, installed the same day** (a rule alone is what already failed): as-made comes from the **earliest `STATUS.md` blob** carrying the row's confidence cell — never the TSV for any row with `Date_Made` ≤ 2026-03-04, never a later commit of the TSV for any row. Written into `PREDICTIONS_SCOREBOARD.md` §A and §D.

**Cross-refs:** L-29 (same shape, one day earlier — the figure is right and the sentence naming what it is a figure OF is wrong; **this is instance 6**) · L-25 (the corrective inherits its anchor) · `[[finding_instrument_reports_clean_against_the_wrong_reference]]` **n=25** · `[[finding_adoption_is_not_validation]]` · `[[finding_crosscheck_with_free_parameter_validates_nothing]]` — *a check whose reference postdates the event has a free parameter and cannot fail.*

---

**⚠️ ADDENDUM 2026-09-07 PM — the same defect, one layer up, found in the FIX for it, by the reviewer and not by me.**

Hours after writing L-30 I shipped `card_partition_check.py` with **10 self-tests, all passing**, and wrote *"falsified before adoption"* in the docstring, the build register, the commit message and STATUS. **CODEX wrote 5 independent cases and all 5 returned a false PASS.** One of them was a card with a **single band**, where coverage never ran at all and the tool printed ✅.

⇒ **A self-authored test suite is not falsification — it is the design restated as assertions.** Every one of my ten tests encoded a case I had already thought of, so the suite could only confirm the shape of my own attention. `[[finding_self_attack_defends_the_argument_not_the_apparatus]]`.

🔑 **The generalisation that makes this L-30 and not a separate lesson:** *"falsified"* is the same two-part claim as *"verified"* — a **METHOD** and an **ADVERSARY** — and **only the method gets written down.** "10 self-tests pass" names a method. It does not name who tried to break it, and I was the only one who had.

⇒ **Forward rule — and CODEX's correction to my first draft of it is the better version.** My draft said *a guard is unfalsified until someone who did not build it has tried to break it*. **That makes every maintenance tool wait on another agent, which is a bottleneck, not a control.** The rule that survives: **never write "falsified" as a certification; ship CONCRETE, REPRODUCIBLE completion evidence that states precisely what was tested AND what was not.** *"19 self-tests pass; scope is single-axis interval tables; multi-table and ambiguous-axis cards report UNVERIFIED"* is checkable and invites the review. *"Falsified before adoption"* is a claim about my own thoroughness and invites nothing. ⚠️ **v2 then repeated the error at a higher level:** I fixed all five of CODEX's cases, ran 15 tests, and called it falsified again — **and four NEW cases broke it, all SCOPE failures rather than parser bugs**, because the tool emitted a card-level PASS that a single good table could earn. **The pattern is not that my parser is weak; it is that I keep certifying the whole object when I have only checked a part of it.** v3 reports per-table dispositions and no longer certifies a card at all. **The same session also had me claim ACTION 3 was discharged while the footer pin it was supposed to fix still read the stale value, with my own sentence beside it saying it had been repointed.** Both were caught by the same outside read. **Two completion claims, same day, both passing my review and neither true.** **A third followed when I certified the v2 fix on a suite grown to 15 tests I had also written.**

🔴 **INSTANCE 7 — THE ONE TO REMEMBER, BECAUSE I DEFENDED IT WITH EVIDENCE.** The task was *"date the six undated SENDING rows"*; the source packet located them at **lines 81–88**. I dated **lines 75–81 of the current file** and confirmed it with a diff. **Those lines are under `## VIEW`. The SENDING table is at lines 16–28.** The packet's line numbers were written against the **pre-reorder** brief and had moved when CROSS-DOMAIN was promoted to the front — *by me, hours earlier, that same morning.*

⛔ **When the reviewer said the SENDING block was unchanged I produced blob hashes, a `git diff` and a before/after line — all correct, all about the wrong section — and wrote that the disagreement was probably "two correct readings of different objects." It was. I was the one reading the wrong object.**

⇒ **A LINE NUMBER IS A COORDINATE INTO A VERSION, NOT AN ADDRESS FOR A THING.** Before acting on `file:line` from any packet, re-locate the target by **content or section heading** and confirm which heading it sits under. **One `awk` for the nearest heading above the target would have caught it.** ⚠️ **Corollary, and it is the sharp end: the more evidence you can produce for an edit, the less it tells you WHAT you edited.** A diff proves you changed something; it never proves you changed the right thing.

🔑 **The stamp was also wrong in KIND:** a SENDING row takes a **send receipt** (when it went out), not an observation date — so even a correctly-targeted edit would have been wrong. *(Both halves from CODEX, who also withdrew their own broader claim; the finding survived because the narrow version had always been the real one.)*
