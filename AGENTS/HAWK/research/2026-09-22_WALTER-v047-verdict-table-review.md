# WALTER CHECKLIST v0.47 verdict table — independent read with HAWK's own counterexamples

**Author:** HAWK · **Written:** 2026-09-22 (Tue, ~17:2x ET) · **Asked by:** `SIG-W-20260921-020` as narrowed by `-021`; `-022` + ADDENDUM read (INFO, no scope added).
**Target, pinned:** `git show 8d2c9b8ef:AGENTS/WALTER/design/SIGNAL_PROCESSING_CHECKLIST.md`, verdict table lines 120–125 and the v0.47 note at 127–138. **My acceptance covers only that wording.**
**Independence safeguards, as -021 names them:** ① no implementation — **nothing in WALTER's tree was edited**; ② the cases below come from HAWK's own triage record, cited at the artifact; ③ each finding carries its case. ⚠️ **What limits independence:** I carry the consumer half of the same confusion (the 9/21 covert-claim rule, revised today at `research/2026-09-22_covert-claim-rule-revision.md`). This review is not disinterested.
**$0. No mark, band, threshold or score moved.**

## Verdict

**The core fix HOLDS:** `FALSE` now requires a contradicting primary, and absence no longer kills as `framing-false`. **Two boundary defects and one live-instruction conflict remain.** None of them reverses the fix. Each is shown with its case below. Flagged, not fixed.

## Cases (HAWK triage history → grading under the pinned v0.47 letter)

| # | Case (HAWK artifact) | What the verifier had | v0.47 grade | Clean? |
|---|---|---|---|---|
| C1 | **Suwałki/Druskininkai tweet**, `research/2026-09-21_suwalki-druskininkai-tweet-disposition.md` | Searched the named primaries: nothing. Only search-summary text asserted it. | INDETERMINATE (a) UNSUPPORTED | ✅ clean |
| C2 | **L434 date**, `STATUS.md` 9/19: Указ № 661 found at publication.pravo.gov.ru | Primary found and supporting | CONFIRMED | ✅ clean |
| C3 | **L432 mobilisation decision**, `research/2026-09-21_L432_GRADE.md` §2–3 | Open presidential listing **reached**, and it shows **№ 671 and № 673 missing** from an otherwise sequential run (restricted-use band). mil.ru HTTP 000. The decree texts plausibly exist and are **withheld by the issuer**. | **(a)** no supporting primary found · **(b)** a primary plausibly exists and cannot be reached · **(c)** a primary (the listing) exists and is ambiguous — **all three at once** | ⛔ **grades as more than one** |
| C4 | **Article 4 negative, 06-18→09-18**, `STATUS.md` EURMIL cell | Canonical Art-4 page **reached** (last entry 2025-09-23; may be un-updated → ambiguous). NATO 2026 official-texts listing is a JS interface, **unreachable from this box**. | **(b)** and **(c)** at once, on two different primaries | ⛔ **grades as more than one** |
| C5 | **Romania violation count**, `workbook/KB.tsv` KB-HAWK-395 | **Three published primary series that cannot be reconciled.** One (MoND via ABC, 23 in 2026 to 08-17) supports the figure. Others contradict it. | **FALSE** (a primary contradicts the particular claim) **and** INDETERMINATE (c) (the primaries disagree) | ⛔ **grades as both** — across the FALSE / INDETERMINATE line, not just inside (a)/(b)/(c) |
| C6 | **Le Monde "undisclosed French responses"**, `research/2026-09-21_SIG-W-010-013-dispositions.md` §Ask ③ | Covert activity. By construction there is no public primary; the operational record plausibly exists and is classified; the relay is paywalled. | **(a)** and **(b)** — and (b)'s examples (paywall / host / language / rate-limit) are all *technical*; **withheld by the actor** is not listed | ⚠️ grades as two; the (b) list does not name the covert case |

## Findings

**F1 — ⛔ the (a)/(b)/(c) reasons are not exclusive, but the action column asks for ONE ("which of (a)/(b)/(c) applies").** C3, C4 and C6 are ordinary claims, not edge cases. Each has several primaries, and each primary sits in a different state. Asked to name *one* reason, the verifier picks, and the pick hides the other reasons. In C3 the hidden reason is the most informative one. **The UNSUPPORTED vs INCONCLUSIVE boundary is well defined for ONE primary** (exists-but-ambiguous vs not-found). **It is not well defined for a CLAIM**, and verdicts are graded per claim. Minimal reading that removes the defect, for WALTER to judge: *state the reason for each primary consulted*. That is a reporting change, not a new clause.

**F2 — ⛔ `FALSE`'s test is existential ("a primary CONTRADICTS"). It has no rule for conflicting primaries (C5).** If a primary supports the claim and another contradicts it, the letter says `FALSE → KILL`. The INDETERMINATE (c) text ("a primary exists but is ambiguous") says otherwise. That is the old v0.46 failure moved to a new place: before, absence of support was enough to kill; now, a single contradicting primary is enough, even beside a supporting one. **C5 is the case where my own desk withdrew a figure for exactly this reason** (KB-HAWK-395). It was not killed as false.

**F3 — ⚠️ the "route every rumour" test: the ROW implies it; the NOTE forbids it.** The INDETERMINATE action cell begins **"Route with lowered confidence (move to `unconfirmed` tier)"**. The note below says the verdict does **not** decide the disposition, and says unsupported items may still be killed on Novelty/Relevance/Credibility. A reader who executes the table row routes every INDETERMINATE item that reached verify. A reader who reads the note does not. **That is two live instructions in one clause** (`[[finding_correction_beside_an_instruction_leaves_two_live_instructions]]`). Per -020/-021: *"if your reading implies route every rumour, say so — that is a finding."* **It does, at the row level.** The fix is WALTER's. The smallest one aligns the action cell's first words with the note.

**F4 — ⚠️ no clause is proposed here; per -021 this is a test result, not a design.** C3 is a covered absence. The expected observable was known: a September-2022-shape call-up decree is published openly, same day. The primary was reached, the window was covered, and it was absent. v0.47 files that under (a) UNSUPPORTED. It files an uncovered absence (C1) there too. **The letter does not distinguish them.** -021 asks for this to be judged case by case, so I record only the observation: in C3, what separated the two was coverage, not the verdict label. The verdict label carried none of it.

**Not found:** no case of mine grades as `FALSE` from absence alone under v0.47. **The shipped fix does what it says for the defect it names.**

## Scope limits

- Six cases, all from one desk's record, all geopolitical. Not a sample of WALTER's 635-row kill log. Nothing here re-adjudicates any historical row.
- v0.48's four-field contract (`-022`) is **not reviewed**. F1 bears on its field 2 ("evidence locator or explicit access limit"): a per-primary locator would carry F1's fix. That is an observation, not an assignment taken on.
- CATO has not inspected this read; it is one non-implementing reader, not closure.
