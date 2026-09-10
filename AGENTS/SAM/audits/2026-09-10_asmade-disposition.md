# As-made confidence audit — SAM disposition, 2026-09-10 (JST) / 2026-09-09 (ET)

**Input:** DAEDALUS packet 2026-09-07 (harvest H2; `scripts/asmade_audit.py SAM` → 34 rows · SAME 8 · MISMATCH 15 · NOT-FOUND 11). **Owner method:** for every flagged row, (1) the ledger's own commit history was traced mechanically — every change to the `Confidence` cell across all 59 ledger commits (`workbook/PREDICTIONS.tsv` to 2026-03-31, `thesis/PREDICTIONS.tsv` after) — and (2) STATUS history was text-walked by prediction wording (not ID) from the first SAM STATUS commit (034b0119e, 2026-02-03). The tool's two named limits both fired here: its "STATUS earliest" cell is the first bare percentage after the ID on a prose line, and SAM's early rows lived as a numbered prose table before IDs existed.

**Governing rule:** WQ-112 (Will, 2026-09-01; `FORGE/PREDICTION_DISCIPLINE.md` § Grading & re-marking): (i) the latest dated pre-resolution mark governs scoring, the original is retained as first-call calibration; (ii) a re-mark is valid only when it lands in the machine field with its date.

## 1. The 15 MISMATCH candidates

| Row | Ledger as-made | Tool's "STATUS earliest" cell | What that cell actually is | Ledger born (commit, date, value) | Disposition |
|---|---|---|---|---|---|
| SAM-28 | 40% | 2% @cf2b9479c | NFP prose (U-3 4.2%) | 74e958e57 2026-06-22 @40% | **False match.** Retain. |
| SAM-29 | 65% | 85% @a0ce790b1 | CFTC "85% of peak" line | 74e958e57 2026-06-22 @65% | **False match.** Retain. |
| SAM-30 | 30% | 85% @a0ce790b1 | same CFTC line | 74e958e57 2026-06-22 @30% | **False match.** Retain. |
| SAM-31 | 35% | 2% @cf2b9479c | NFP prose | 74e958e57 2026-06-22 @35% | **False match.** Retain. |
| SAM-38 | 55% | 85% @f27fc1961 | SAM-34's hold @85% | 1ee62bf4d 2026-07-29 @55% | **False match.** Retain. |
| SAM-24 | 85% | 72% @ee4479afb | a different item on the Jun-16 line | 7348f4346 2026-05-12 @85% | **False match.** Retain. |
| SAM-25 | 40% | 200% @3851059ee | the ESR threshold | f0a246c50 2026-05-21 @40% | **False match.** Retain. |
| SAM-32 | 72% | 85% @27ab67130 | CFTC peak % in a catalysts line | e886a73db 2026-06-30 @72% | **False match.** Retain. |
| SAM-20 | 60% | 70% @bc7bdb1f1 | SAM-21's June-hike line | c48c5b455 2026-04-13 @60% | **False match.** Retain. |
| SAM-22 | 65% | 25% @2d8659eb5 | calibration note on SAM-40's branch | 86a37e1c9 2026-04-24 @65% | **False match.** Retain. |
| SAM-27 | 75% | 74% @3b493ea00 | CPI prose | f0a246c50 2026-05-21 @75% | **False match.** Retain. |
| SAM-36 | 50% | 85% @a749cb999 | "85% of peak" | 934ad1787 2026-07-10 @50% | **False match.** Retain. |
| SAM-37 | 55% | 85% @e16b5466f | "85% of peak" | e16b5466f 2026-07-17 @55% | **False match.** Retain. |
| **SAM-26** | 70%→~25% | 4% @3b493ea00 | the 4.0% yield level | f0a246c50 2026-05-21 @70%; ~30% 3b493ea00 05-26 (dated 05-22 in Notes); ~25% d4015ec6a 05-27; FAILED 06-16 | Cell was a false match, **row is a real two-vintage record.** Converted to `25% [2026-05-27] (was 70% [2026-05-21])`. Scoring vintage ~25%, unchanged. |
| **SAM-08** | 85%→90% | 70% @bc7bdb1f1 | SAM-21's line | STATUS 67d336e32 2026-02-12 carries "If Strong Shunto → 85% April BOJ hike to 1.00%"; field born 91c301279 03-04 @85% (placeholder Date_Made 02-15); 90% landed 42c03829e 03-31; FAILED 04-28 | Cell was a false match, **row is a real two-vintage record.** Converted to `90% [2026-03-31] (was 85% [2026-02-12])`; Date_Made corrected 02-15 → 02-12. Scoring vintage 90%, unchanged (matches the preamble). The 03-04 STATUS prose "60% hike if Shunto strong AND conflict fading" never reached the field — not a mark under (ii). |

## 2. The 11 NOT-FOUND rows

| Row | Ledger | Evidence | Disposition |
|---|---|---|---|
| SAM-04 | 60%, Date_Made 02-15 (placeholder) | STATUS 034b0119e **2026-02-03**: "JGB 30Y stays <4.0% through Q1 … 60%" | Value verified; **Date_Made corrected → 2026-02-03.** |
| SAM-05 | 70%, 02-15 | STATUS 034b0119e 2026-02-03 @70% | Value verified; **Date_Made → 2026-02-03.** |
| SAM-06 | 75%, 02-15 | STATUS 034b0119e 2026-02-03 @75% | Value verified; **Date_Made → 2026-02-03.** |
| **SAM-07** | 48%→75%, 02-15 | STATUS 67d336e32 **2026-02-12** @48%; the "→75%" entered the field in 42c03829e 2026-03-31 — **the same commit that recorded CONFIRMED / Date_Resolved 2026-03-23**; no dated 75% anywhere in STATUS before 03-23 | **Post-resolution annotation, not a mark (WQ-112 ii). Scoring vintage corrected 75% → 48%** (binary Brier 0.0625 → 0.2704, +0.2079 on this row). Cell → `48% [2026-02-12]`; Date_Made → 2026-02-12; narrative kept in Notes. |
| SAM-13 | 55%, 02-15 | No pre-rollout STATUS prose with a % (02-03 … 03-03 walked); field born 91c301279 03-04 @55% | Placeholder retained, now labelled; as-made = 55% (no prior vintage found). |
| SAM-14 | 60%, 02-15 | Same; field born 03-04 @60% | Placeholder retained, labelled; as-made = 60%. |
| SAM-15 | 80%, 03-20 | No STATUS % prose 03-20…03-31; field born 42c03829e 03-31 @80% | Registration date retained; as-made = 80%. |
| SAM-16/17/18/19 | 70/65/55/75%, 04-13 | Born in the field at Date_Made (c48c5b455 2026-04-13) | NOT-FOUND expected; no prior vintage. |

## 3. Same-class rows the tool did NOT flag (fixed as a class, not a row list)

| Row | Old cell | New cell | Dated chain (Notes) | Scoring vintage |
|---|---|---|---|---|
| SAM-21 | 70%→~57%→~50%→70%→75%→~90% | `90% [2026-06-14] (was 70% [2026-04-24])` | 70 [04-24] → ~57 [05-25] → ~50 [05-28] → 70 [05-31] → 75 [06-09] → ~90 [06-14]; CONFIRMED 06-16 | ~90%, unchanged |
| SAM-23 | 75%→~55%→~72%→~30% | `30% [2026-06-14] (was 75% [2026-05-12])` | 75 [05-12] → ~55 [05-25] → ~72 [06-01] → ~30 [06-14]; FAILED 06-16 | ~30%, unchanged. ⚠️ The ~30% reached the FIELD in the resolution commit (ee4479afb 06-16) but is dated 06-14 in the row and carried in STATUS blobs fa70cbaa3 / 93eaa93e2 of 06-14 — treated as valid; flagged as the one ambiguous landing. |

SAM-38 and SAM-40 carry branch tables (one vintage each) — untouched.

## 4. What moved

- **Scoring vintage changes: 1 of 34 rows — SAM-07 (CONFIRMED) 75% → 48%.** Every other scored value is unchanged; five rows now carry their dates in the machine field. Scoreboard 16 / 14 / 1 / 3 unchanged. SAM keeps no aggregate Brier cell, so no ledger score to restate; the per-row delta is above.
- **Date_Made corrections: 5** (SAM-04/05/06 → 2026-02-03; SAM-07/08 → 2026-02-12), all from first STATUS appearance at the same value. **Placeholders retained and labelled: 2** (SAM-13/14). The 2026-02-15 rollout placeholder was 9–12 days late for every row it was checked on, in the same direction.
- **Local lesson (MEMORY):** on this desk the tool's MISMATCH list was 13/15 noise from level percentages, while the real defects were in rows it could not flag — an undated chain and a re-mark that landed with its resolution. Check arrow cells for the landing commit vs the resolution commit, not for the tool's cell.

Evidence commands: ledger trace over `git log --reverse -- AGENTS/SAM/workbook/PREDICTIONS.tsv AGENTS/SAM/thesis/PREDICTIONS.tsv` parsing the Confidence cell per commit; STATUS walks over `git log --reverse --since=2026-02-01 -- AGENTS/SAM/STATUS.md` by wording. Written 2026-09-10 ~02:4x UTC.
