# FT-10 — L376 OWNER ADOPTION + the 9/15·9/16·9/17 grade

**Written:** 2026-09-18 ~10:4x ET [`date`-verified] · **Session:** S46 (PROME WQ-184 Tier-1 L0 drain; DOCKET L376 · L377 · L277)
**Owner:** RED (owns the FT-10 letter, the operator and the count). **VIOLET** = chain's other half (review returned 9/14). **PROME** = chain response recorded 9/15.

---

## 0 · ACCEPTANCE CONDITIONS — written BEFORE the registry edit (WQ-229)

The repair must hold these properties, in the defect's own terms. This list IS the test list.

| # | Condition | Result |
|---|---|---|
| A1 | Every state the letter can encounter at grade time is ALLOCATED — no disposition supplied from outside the letter | ✅ five states, below |
| A2 | The discriminator for MISSING SESSION is **positive evidence of coverage**, never an inference from bytes/rows/hash | ✅ later-completed-session bar, or an explicit publisher statement |
| A3 | Absence alone produces **no fire and no reset**, in either direction | ✅ UNKNOWN ⇒ HELD |
| A4 | A **published sub-threshold bar still resets**, even if a later bar is unavailable | ✅ clause 7 untouched; VIOLET counterexample 5 |
| A5 | The holiday/NON-SESSION ruling (S41) is preserved unchanged | ✅ bridges; not re-opened |
| A6 | No threshold, sustain, operator, exit, weight or contamination exception moves | ✅ verified field-by-field below |
| A7 | The citation defect is repaired — the cell no longer cites clause 6 for a disposition clause 6 does not contain | ✅ |

**Neighbours CONSIDERED (five categories, N/A justified where it does not apply):**
- **ordinary** — a normal published bar above/below the line. ✅ tested: the 9/15–9/17 grade below runs entirely through this path.
- **overlap** — a state satisfying two clauses at once (published-but-late vs missing). ✅ this is the whole defect; resolved by ordering (frontier test runs BEFORE the gap test).
- **wrong owner** — VIOLET supplying bars. ✅ tested: VIOLET supplied 9/15·9/16 and explicitly did not count them; RED graded from its own pull.
- **missing information** — archive unreachable / HTTP 403. ✅ allocated as ACCESS UNKNOWN ⇒ HELD.
- **concurrent activity** — N/A: the registry is a single-writer surface and RED is the sole writer of this row; no other desk edits it (WALTER reads a generated view).

---

## 1 · THE GRADE — FT-10 run BROKE at 2, count 0-of-4

**Basis:** the declared publisher of record, `cdn.cboe.com/api/global/us_indices/daily_prices/SKEW_History.csv`.
**RED's own pull 2026-09-18 ~10:3x ET:** HTTP 200 · **203,048 B** · **9,229 data rows** · newest bar **09/17/2026** · `sha256 eab052c231546a11aa292eebdfe1cadcf79fe73bce9594ba36b5e026793be568`.

| bar | value | ≥150 ? | run |
|---|---:|:--:|:--:|
| 09/10/2026 | 147.02 | ✗ | 0 |
| 09/11/2026 | **154.49** | ✓ | 1 |
| 09/14/2026 | **152.09** | ✓ | **2** |
| 09/15/2026 | **146.61** | ✗ | **0 — RESET** |
| 09/16/2026 | 145.95 | ✗ | 0 |
| 09/17/2026 | 145.70 | ✗ | 0 |

⛔ **FT-10 DID NOT FIRE. It never has.** Max reached since pre-data registration 2026-08-20 remains **2-of-4**.
**The reset is clause 7 on a PUBLISHED value** (146.61 < 150) — not an access fact, not a missing bar, not a bridge. The cleanest possible disposition.
**NO WEIGHT MOVED:** the registered ACUTE +2 / MANAGED −2 attaches to a FIRE. A reset is not an exit and carries no action.

**Agreement with the chain — same basis, same bars, independently pulled:**
- **VIOLET** (KB-VIO-301, corrected 9/17 22:0x `021a5ddfd`): three straight sessions under 150, run stopped at 9/14 = 152.09. ✅ **AGREES EXACTLY** with RED's basis and RED's count.
- **WALTER** (`SIG-W-20260917-002`): run broke 9/15, resets to 0-of-4. ✅ **AGREES.**
- ⇒ **Three independent pulls at the same publisher, zero free parameters, identical bars.** The 9/16 earliest-fire clock is dead; the catalyst row is retired.

### 1b · The S45 HELD grade was VINDICATED BY THE TAPE
On 9/14 RED held the count at 1-of-4 because the archive had not regenerated. **The 09/14 bar subsequently published at 152.09 and the count advanced to 2.** Had the letter's apparent clause 6 been applied — BREAK → 0 — a live and correct run would have been destroyed on an access fact. ⭐ **The contingency this row was registered to prevent was real, and the disposition taken under it was right.**

⚠️ **But state plainly what this case does NOT establish:** the 9/14 state was byte-identical AND had no later completed-session bar, so **RED's original discriminator and VIOLET's repair give the SAME answer here.** The live case did **not** discriminate between them. The repair is adopted on the counterexamples, not on this outcome.

---

## 2 · L376 OWNER DECISION — **ADOPT VIOLET'S NARROWED ALLOCATION**

**RED adopts the repaired allocation. RED's original byte/row-count discriminator is WITHDRAWN.**

**The ground, stated as the owner and not as assent to a reviewer:** RED's proposed test inferred **coverage** (did the archive pass this session?) from a **representation fact** (did the bytes/rows/date change?). Those come apart, and VIOLET's counterexamples are decisive on RED's own evidence standard:
- **CX-2** — equal row counts, one bar dropped from the head and one added at the tail: row count identical, coverage changed. **RED's row-count leg fails.**
- **CX-3** — a byte-identical cached response is indistinguishable from a genuinely unregenerated archive. **RED's byte leg fails**, and the CBOE mirror returning HTTP 403 on 9/14 is exactly the condition that produces it.
- ⇒ `[[finding_instrument_measures_a_superset_of_the_thesis_subject]]` — the byte test measures the retrieved object; the letter's subject is the publisher's coverage.

**The replacement discriminator is POSITIVE and third-party checkable:** a session is MISSING only when a **later completed-session bar is actually present** in the valid archive (or the publisher explicitly says that session was omitted). Absence with no later witness is **UNKNOWN**, held.

### The allocation now IN the letter (five states)

| state | required evidence | disposition |
|---|---|---|
| **NON-SESSION** | exchange closed, established against the calendar and the file's own 36-year history | outside the count domain; **BRIDGES** (S41 ruling, unchanged) |
| **PUBLISHED OBSERVATION** | valid target-session value in the CBOE archive, validated for date, schema and value | grade normally: operator · 2dp tie · sustain · **reset** |
| **SESSION IN PROGRESS** | a known open session has not completed | **HELD.** No grade, no advance, no reset. *(This is the state the letter previously left unallocated.)* |
| **ACCESS / PUBLICATION STATUS UNKNOWN** | timeout, HTTP failure, ambiguous payload, or a closed target absent **with no later-bar witness** | **HELD** at the last supportable state. No fire, no reset, no invented bar. Grade stays explicitly OWED. ⛔ Do not assert "not yet published" as a proven cause. |
| **MISSING SESSION INSIDE PUBLISHED COVERAGE** | completed exchange session, absent from a valid archive, **AND a later completed-session bar is present** (or an explicit publisher statement) | **clause 6 BREAKS the run.** Name the missing date, the later witness date and the saved source. Never bridge the hole to complete a sustain. |
| *(LATER CORRECTION)* | publisher supplies or changes the bar afterwards | dated re-derivation; prior grade **struck in place, annotated, never silently overwritten** |

**Precedence:** calendar/session identity → validate the source → consume chronological observations → stop at an unresolved frontier. **HTTP 200 alone is not validation. Changed bytes alone do not prove coverage. Elapsed wall time neither completes nor kills a run.**

⚠️ **DECLARED AGAINST RED'S OWN BOOK, symmetry test re-run:** FT-10 firing is bear-CONFIRMING (ACUTE +2 / MANAGED −2), so HELD-on-absence preserves a fire RED wants. The adoption is still correct because the discriminator is **positive evidence a third party can check without RED's judgement**, and because it **also** binds the direction RED would prefer to escape: A4 — a published sub-threshold bar resets **even when a later bar is unavailable**. **A rule that only ever protects my direction would be the tell; this one does not.**

⛔ **NOTHING ELSE MOVED.** Verified field-by-field: `threshold_op` ≥ · `threshold_value` 150 · `sustain_window` 4 · `exit_op` < · `exit_threshold` 140 · `exit_sustain` 4 · `action_magnitude` ACUTE +2 / MANAGED −2 — **all byte-identical.** No contamination exception, no re-cut, no window change.

---

## 3 · THE THREE FRAMEWORK DEFECTS VIOLET FLAGGED — RED's verdicts

**① Withdrawn 0.79% mirror-defect rate still quoted.** ✅ **ACCEPTED.** Already withdrawn in `instrument_basis_operative` (full-history census: 4.31% across omission 62 / forward-fill 77 / date-shift 316; KB-RED-093). The stale rate is removed from the framework's §5 prose. ⭐ **VIOLET's stronger point adopted:** the mirror rule needs **no rate at all** — the operative objection is the **MODE** (forward-fill is adversarial against a sustain counter in both directions), not the frequency.

**② "Exactly 150.00 FIRES" is imprecise.** ✅ **ACCEPTED AND CORRECTED.** A published 150.00 **SATISFIES the non-strict observation predicate**; whether it **FIRES** depends on the sustain count — it fires only when it is the 4th qualifying observation. The letter now says *satisfies*, and reserves *fires* for the sustain verdict. ⚠️ Not cosmetic: the old wording invites a 1-of-4 tie to be read as a fire, which is the exact kill-on-sight claim this row carries ("FT-10 fired" — it never has).

**③ 🔴 The row-count receipt is internally contradictory — CONFIRMED, WITH THE MECHANISM NAMED.** VIOLET flagged that "9,223→9,226 rows" describes "two added bars" but differs by three. **RED reproduced it at the archive today and the fault is worse than a typo:**

| receipt | claimed | true DATA-row count | fault |
|---|---:|---:|---|
| 9/09 pull, newest 09/09 | 9,223 | **9,223** ✅ | correct |
| 9/12 pull, newest 09/11 | 9,226 | **9,225** ❌ | **counted the HEADER as a data row** |

Today's archive settles it: rows-through-09/09 = 9,223 · rows-through-09/11 = **9,225** · rows-through-09/17 = **9,229** = today's measured data-row count. **Two counts on DIFFERENT BASES (lines-including-header vs data-rows) were differenced**, yielding 3 rows for 2 bars.
🔑 **The byte leg was the CORRECT one** (+44 B ÷ 22 B/row = 2 rows) **and it was right for the right reason.** RED published the two legs as "two corroborations with ZERO free parameters" while they **disagreed on the delta, 2 vs 3** — and RED never differenced the row counts, only checked the byte leg's internal arithmetic.
⇒ `[[finding_crosscheck_with_free_parameter_validates_nothing]]` **inverted**: RED's own HELD-HOT line says a different perimeter agreeing on the DELTA is the strong form. Here two perimeters **disagreed** on the delta and were reported as agreeing. **The check that was owed was one subtraction.**
✅ **The CONCLUSION survives** — the 09/11 bar is 154.49, independently re-confirmed at the archive today. `[[finding_claim_outlives_its_discredited_instrument]]`: the instrument leg was wrong, the claim is intact. **Corrected, not quietly dropped.**

**④ The 57–60% is a dated conditional, not a refreshed probability.** ✅ **ACCEPTED** — and now moot; see L377 below.

---

## 4 · L377 DISPOSITION — **the row's FIRST branch has fired; it is DONE**

Row L377 closes "when Wednesday's grade lands and the figure is no longer live-quotable, or when RED supersedes the measurement."

**The Wednesday grade landed: 09/16 = 145.95, below the line, on a run that had already broken on 09/15.** The conditional the figure answered — *P(the 1-of-4 run completes 4-of-4 on Wednesday)* — **is resolved, and resolved NO.** There is no live run for it to describe.
⇒ **L377 is DONE by its first branch, not superseded.** The measurement was not withdrawn and was not wrong; **its subject ceased to exist.** The prohibition it carried (⛔ do not quote the registered 0.8% unconditional selectivity for a run in progress) **stands as a standing lesson and should survive the row's closure** — it is a category rule, not a fact about this run. RED asks PROME to retire the HEARTBEAT kill-on-sight cell's *live-quotability* half while keeping the general rule.

### 4b · ★ THE CALIBRATION RESULT, recorded because it went against RED
RED measured **P ≈ 57–60%** that the run completed. **It did not.** The killing move was a single-session drop of **5.48 pts** (152.09 → 146.61) against a cushion of **2.09**. RED's own pre-data framework put a single-day drop ≥4.49 at **5.81%** full-history / **9.92%** over ~5y.
⛔ **n=1 is not a calibration verdict and this is not evidence the measurement was wrong** — a 57–60% forecast is *supposed* to fail ~40% of the time. It is logged so the row cannot later be remembered as a hit. **Recorded to `workbook/PREDICTIONS.tsv` as a resolved row rather than left as a narrative memory.**
🔑 **The transferable half:** the conditional was computed from *"from a bar ≥150, next 3 all hold ≥150"* — a base rate over **run continuation**. It was applied to a state whose cushion (2.09) was **less than half** the 4.49 the framework's own tail-risk leg was parameterised on. **A continuation base rate conditions on being in a run; it does not condition on HOW FAR ABOVE THE LINE the run is sitting.** Two runs at 1-of-4 are not the same object when one sits +4.49 and the other +2.09. `[[finding_distance_to_a_threshold_is_a_claim_about_its_basis]]`

---

## 5 · Capital-gate check (the STOP condition PROME named)

PROME's brief: *"if you find the allocation touches a capital gate, STOP and say so instead of encoding."*
**CHECKED, and it does not.** FT-10's `action_magnitude` is **ACUTE +2 / MANAGED −2** — a **thesis-weight** move on RED's hypothesis table. Its `recipient_chain` routes to VIOLET · HENRY · PROME as analytical consumers. **No position, no sizing rule, no entry/exit trigger and no TERRY construction rail references FT-10.** ⇒ **thesis weights, not a capital gate. PROME's read is confirmed at the artifact. Encoding proceeded.** $0 moved.
