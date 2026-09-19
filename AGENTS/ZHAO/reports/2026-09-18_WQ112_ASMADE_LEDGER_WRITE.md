# WQ-112 as-made ledger write — ZHAO, 2026-09-18

**Discharges:** NEXT ACTIONS #2, carried since the DAEDALUS 9/7 packet. **Supersedes the write instruction in** `reports/2026-09-17_ASMADE_VERIFICATION.md` (the verification leg of that report stands; its *action* column does not — see §3).

**Canon applied:** `FORGE/PREDICTION_DISCIPLINE.md` §Grading & re-marking — **WQ-112** (ratified Will 2026-09-01) and **WQ-161 ②/③** (ratified Will 2026-09-10, encoded 2026-09-14).

---

## 1. Method — mechanical, not narrated

Every mark below is reconstructed from the ledger's own git history:

```
git log --reverse --format=%H|%ad --date=short -- AGENTS/ZHAO/workbook/PREDICTIONS.tsv
# one blob per commit; record the first appearance of each distinct Confidence value per Pred_ID
```

**Why mechanically and not from the Notes prose:** the prose disagreed with the ledger twice, and in both cases the prose was wrong (§4). A mark history is a property of the machine field; reading it out of commentary re-introduces the error the machine field exists to prevent.

## 2. The write

| Row | Governing mark (scores) | Earlier marks | First call | Status |
|---|---|---|---|---|
| ZHA-01 | 18% [2026-08-21] | 25% [07-04], 55% [03-09] | 70% [2026-03-04] | OPEN |
| ZHA-02 | 65% [2026-03-04] | — | 65% | CONFIRMED |
| ZHA-03 | 25% [2026-07-04] | — | 65% [2026-03-09] | RESOLVED NO |
| ZHA-04 | 42% [2026-07-16] | 65% [07-04], 60% [07-04] | 65% [2026-03-09] | RESOLVED YES |
| ZHA-05 | 55% [2026-03-09] | — | 55% | OPEN |
| ZHA-06 | 72% [2026-07-16] | — | 60% [2026-03-09] | OPEN |
| ZHA-07 | 70% [2026-03-09] | — | 70% | OPEN |
| ZHA-08 | 60% [2026-03-09] | — | 60% | FALSIFIED |
| ZHA-09 | 10% [2026-07-09] | — | 10% | RESOLVED NO |
| ZHA-10 | 40% [2026-07-09] | — | 40% (⚠️ §5) | OPEN |
| ZHA-11 | 68% [2026-07-16] | — | 65% [2026-07-09] | RESOLVED YES |
| ZHA-12 | 80% [2026-08-03] | — | 55% [2026-07-16] | RESOLVED YES |
| ZHA-13 | 50% [2026-07-16] | — | 50% | RESOLVED NEUTRAL |
| ZHA-14 | 30% [2026-07-16] | 35% [07-16] | 35% | RESOLVED NO |
| ZHA-15 | 18% [2026-08-03] | — | 55% [2026-07-16] | RESOLVED NO |
| ZHA-16 | 45% [2026-09-02] | — | 35% [2026-09-02] (⚠️ §5) | **OPEN** |
| ZHA-17 | 55% [2026-09-02] | — | 55% | RESOLVED NO |

### Mass-neutrality proof (WQ-161 ③), stated once for the whole patch

- **Mass-bearing branches before and after: identical.** No branch was added, removed, relabelled or renormalised on any row.
- **Governing confidence before and after: identical on all 17 rows.** The patch writes provenance into the `Confidence` field; it does not change the number that governs scoring anywhere.
- **Scored set, branch-to-outcome mapping, thresholds and every other grading condition: unchanged for every previously resolvable case.** No threshold moved; no outcome definition was touched; no resolved grade changes.
- ⇒ The patch is mass-neutral. It is therefore permitted on rows of any age under WQ-161 ②.

## 3. ⛔ THREE ROWS WERE NOT RE-SCORED, AND THE INSTRUCTION TO RE-SCORE THEM WAS WRONG

`reports/2026-09-17_ASMADE_VERIFICATION.md` marked **ZHA-03, ZHA-04 and ZHA-15** "**RE-SCORE**", and `STATUS.md` NEXT ACTIONS #2 carried that forward. **It is contrary to ratified canon.** WQ-112(i), verbatim:

> *"the **LATEST dated pre-resolution mark governs scoring** — you score the forecast you held; the original Date_Made confidence is retained and reported separately as first-call calibration."*

All three governing marks are dated, and all three landed **before** resolution:

| Row | Governing mark | Landed | Resolved | Gap | Verdict |
|---|---|---|---|---|---|
| ZHA-03 | 25% | 2026-07-04 | 2026-08-21 | 48 days | valid — grade stands |
| ZHA-04 | 42% | 2026-07-16 | 2026-08-21 | 36 days | valid — grade stands |
| ZHA-15 | 18% | 2026-08-03 | 2026-08-21 | 18 days | valid — grade stands |

✅ **The ambiguity that made the re-score look necessary is resolved.** The cells read `25% (at resolution)` / `42% (at resolution)` / `18% (at resolution)`, which could have meant *a number chosen while grading* — which would indeed be hindsight scoring and would have to be undone. The history shows **the value did not change at the 2026-08-21 grading commit in any of the three cases.** `(at resolution)` was a **label on the standing mark**, not a new mark. The grades were sound.

⚠️ **Recorded because the direction matters:** re-scoring would have **worsened** ZHA-03 (Brier 0.0625 → 0.4225) and ZHA-15 (0.0324 → 0.3025) and **improved** ZHA-04 (0.3364 → 0.1225) — net strongly against this desk. So the error was not self-serving, and it would still have corrupted the record. **A correction that costs you something is not thereby correct.** `[[finding_a_correction_pass_is_unreviewed_work]]`

⚠️ **And note what produced it:** the 9/17 report was written **16 days after WQ-112 was ratified**, citing `PREDICTION_DISCIPLINE.md` in its own header as canon-read. The canon was read and the rule was still mis-derived. `[[finding_adoption_is_not_validation]]`

## 4. Two places the prose disagreed with the ledger — prose wrong both times

1. **ZHA-04's Notes narrate "cut twice (65%→30%→42%)".** The ledger contains **no 30% mark**: 65% [03-09] → 60% [07-04] → 65% [07-04] → 42% [07-16]. The 30% lived in STATUS prose only, so under **WQ-112(ii)** — *"a re-mark is valid only when it lands in the machine field with its date"* — it never scored. Prose left in place as history; the machine form carries the ledger's record.
2. **ZHA-11's 68% mark.** The 9/17 report asked to "confirm the 68 date from history" and guessed **2026-08-21**. It landed **2026-07-16**, five weeks earlier.

## 5. Two defects flagged, neither repaired here

- **ZHA-10 `Date_Made`** reads `2026-03-09`; the row's first ledger appearance is **2026-07-09**, and the 9/17 report sources an as-made 45% to a `[PROPOSAL]` block in STATUS at blob `77f56870c` (2026-03-22). The 45% never entered the machine field ⇒ a pre-registration draft, not a mark. **The registration date is left as found:** correcting it is not a provenance write, and on an OPEN row it could move scored mass. Raise separately.
- **ZHA-16 first call 35%** was likewise a STATUS pre-registration figure, amended to 45% in the same session and still before the event; the ledger only ever carried 45%. Recorded with that qualification. **The row is OPEN and 6 days from its event — branches, thresholds and confidence untouched.**

## 6. What this does not do

It does not re-grade anything, does not re-register anything, and does not touch ZHA-16 ahead of the 9/24 summit. It makes every mark in the ledger carry its own date, so the next person reading a Brier score can see which forecast was actually being scored.
