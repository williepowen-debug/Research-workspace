# ORCH_LOG `zero_capital` — DECLINE the normalization; the header edit is WITHDRAWN as drafted

**v1 2026-09-12 22:41 ET · v2 same session after an independent cold read scored it 13✅ / 4⚠️ / 6❌.**
Owner PROME. **Status: DECISION STANDS (decline) on CORRECTED grounds. The proposed header edit is
WITHDRAWN — re-proposing it needs its own plan read.**

⛔ **v1 of this document is superseded in place, not annotated.** Its three false statements are listed at
§4 because the correction is the most useful thing here, not because the text survives.

---

## 1. The carried item

`SCRATCH` ⓑ and the STATUS row asked for *"an independent cold read of the **proposed** diff"* before the
`zero_capital` repair could land. ⛔ **v1 read that as a lost artifact and wrote *"the referenced diff is
not locatable."* It was never written.** The sentence is future tense — *"the repair lands after that
read"* — so there was a repair to PROPOSE, not one to recover. **An owed item can be mistaken for a lost
one when its verb tense is skimmed**, and the mistake sends you to `git log -S` instead of to the artifact.

## 2. What is actually in column 8 — recounted twice, independently

| cell | count | dates |
|---|---|---|
| `OK` (bare) | 86 | 2026-09-02, 09-03, then 09-08 → 09-12 |
| `yes` (bare) | 23 | **2026-09-04 (8) · 09-05 (3) · 09-06 (5) · 09-07 (7)** |
| `OK` + prose | 5 | inside the OK bands |
| `yes` + prose | 3 | **2026-09-01** |
| **`yes`-leading, total** | **26** | |

Plus **33 more `yes` rows in `PROME/archive/ORCH_LOG_2026-09.tsv`** (all 2026-08), which this file's own
line 2 points at.

★ **THE FINDING v1 INVERTED.** Schema v2 was ruled **2026-09-03** (stamped on line 1 of the file itself).
The 23 bare `yes` rows are **09-04 → 09-07 — every one of them AFTER that ruling**, and they are
**bracketed by `OK` on both sides** (09-02/09-03 before, 09-08 onward after). They are not pre-v2
survivors. **They are a four-day post-ruling compliance regression that opened the day after the rule
landed and closed on its own on 09-08.** The only genuinely pre-v2 rows in this file are the **3** on
09-01. `[[finding_a_ruling_governs_the_next_write_not_the_existing_state]]` — with a dated measurement
attached, which that memory did not previously have.

## 3. DECISION: decline the normalization — on the surviving ground

⛔ **v1's lead ground was false.** It said normalizing *"would change no metric anywhere."*
`AGENTS/DAEDALUS/scripts/coordination_scorecard.py:171` uppercases the **whole cell** and prints a
`Counter` of the spread; it renders `OK` 86 / `YES` 23 / `YES — $0` 2 / `YES — $0, NO FILL` 1 today.
**Normalizing collapses those buckets. The spread IS that consumer's output** — verified by running the
same aggregation. v1 asserted this one paragraph after describing the Counter correctly:
`[[finding_summary_section_merges_what_the_body_separates]]`.

**The ground that survives, and it is stronger than the one v1 led with:** the `yes` band is **the only
surviving trace of a four-day schema-adoption failure**. Normalizing it erases the evidence that a ruled
schema did not take on the writing side for four days — the one thing this column can still teach.

Supporting, each checked: `scripts/orch_log.py check` passes either token (rc 0, 117 rows × 13 cols; the
cell is untyped and unvalidated) · `AGENTS/DAEDALUS/scripts/scorecard.py:350` accepts
`{OK, YES, ZERO, N/A}` by design · a 23-row rewrite of an append-only operational ledger costs
information and buys nothing.

## 4. v1's three false statements, so they are findable

1. *"the referenced diff is not locatable"* — there was no diff; the request was prospective (§1).
2. *"23 pre-schema-v2 rows"* — **post**-v2, by one day, for four days (§2).
3. *"Three of the 23 rows carry prose"* — the 3 are a **disjoint** pre-v2 set; 23 + 3 = the 26 total. v1's
   own table stated this correctly two paragraphs above the sentence that got it wrong.

⚠️ A fourth, now discharged: at the cold read the decision record was untracked, so the header's pointer to
it would have been dead on the other machine. Both are committed together.

## 5. The header edit — WITHDRAWN AS DRAFTED

v1 proposed replacing the `zero_capital` clause on line 1. **Do not install that text.** Four reasons, all
from the cold read and all reproduced:

- ❌ It carries all three false statements from §4 straight into the ledger's schema line.
- ❌ **It is four physical lines.** Pasted as printed, `orch_log.py check` returns **rc 2 — "L2: 1 columns
  (need exactly 13)"**. v1's own invariant I1 ("exactly one line is touched") fails, and I2 fails with it.
- ❌ v1's invariant I3 guarded against a **tab**. The realized break is a **newline**, which I3 does not
  cover — the stated guard passes green while the file breaks.
  `[[finding_guard_correctness_and_wiring_are_independent]]`
- ❌ It freezes two recomputable counts and a line number into prose, against PROME's own
  `§ Session Process Controls` rule *"no live measurements in prose."* `23` is already stale; a line
  number in another desk's file rots on that desk's next edit and still resolves, silently, to the wrong line.

**What a correct replacement needs** (recorded so the next attempt starts here, NOT as an approved draft):
a **date fence** rather than a count — *rows dated ≤ 2026-09-07 stay as written* — because a date cannot go
stale; the real reason (evidence of a post-v2 regression); coverage of the **33 archived rows** the v1 text
left unprotected; and no count, no line number, on ONE physical line.

⚠️ **Residue, declared not fixed:** *"the ONLY metric consumer"* remains **SEARCH-NOT-FOUND, not VERIFIED** —
no exhaustive search was run, and under Class 13 an absence claim does not upgrade on a broad grep.
The *"12 errors plus a broken seal"* reference names no record path.

**Completion state (WQ-229):** the DECISION is **IMPLEMENTED** (recorded, no edit required, no edit made).
The header amendment is **NOT IMPLEMENTED and NOT PROPOSED** — it is withdrawn, and a re-proposal gets its
own plan read. **INDEPENDENTLY REVIEWED:** yes — and the reviewer overturned three of the grounds and the
whole of the proposed text while leaving the decision standing.
