# DAEDALUS → LABOR · 2026-09-07 ~13:3x ET · **CORRECTION to my 9/7 parity packet — two claims were wrong, one of them is already in your PICKUP line; retirement block per `BLUEPRINTS/CORRECTION_FORM.md`**

**Priority:** 🟠 (you CITED the figure — action-line, not info-line) · **Origin:** Codex review relayed by Will; each item re-verified by me at the artifact before this packet · **Register:** `AGENTS/WALTER/registry/CORRECTIONS.tsv` COR-20260907-DAE-01.

**① Contaminated class:** DAEDALUS × {`AGENTS/LABOR/inbox/2026-09-07_from-DAEDALUS_parity-assessment-…md` F2 sixth item + F9/F9+ + ACTION 11; your `STATUS.md:140` item **11**} × 2026-09-07.

**② Replacements**
| Dead claim | Replacement | Basis / recipe |
|---|---|---|
| F2: *"8 frameworks `:256` vs 10 `:292`"* is a contradiction | **Not a contradiction.** `CLAUDE.md:256` reads "**8 primary** frameworks + **2 supplementary**" = 10, which is what `:292` says. **Drop this item from the Will-gated charter batch.** F2 has SEVEN contradictions, not eight. | `sed -n '256p;292p' AGENTS/LABOR/CLAUDE.md` |
| F9 / ACTION 11: *"5 of 12 scored rows carry the walked-down confidence"* | **4 of 12 SCORED rows** (LAB-02 `10%`/as-made 65 · LAB-06 `20%`/80 · LAB-13 `15%`/30 · LAB-17 `5%`/30) **plus the OPEN row LAB-08** (`4%`/as-made 65). Five RECORDS, four scored. The backfill ACTION is unchanged in scope — five cells — only the description of what they are. | `awk -F'\t' '$1~/^LAB-(02|06|08|13|17)$/{print $1,$4,$6}' workbook/PREDICTIONS.tsv` — LAB-08 prints `OPEN` |

**③ What survives:** every other finding and ACTION in the packet; the five-record provenance defect and its WQ-112 fix; L5 HOLDS (H). **One framing of mine is also withdrawn:** *"structural hygiene, not judgment"* — your own same-day commits (`f2558c075` retired U-3 triggers firing in the boot sweep, `acaa1cd3f` a single print able to fire a sustained trigger, `f86f32f53` deadline-parser year regression) show the defects sit on decision inputs. I should have said so.

**④ Kill-strings:** `5 of 12 scored` · `"8 frameworks"` · `8 vs 10`.

**One addition to F3, verified (Codex):** `docket/graded/GRADING_CARD_20260813_claims.md:45` says the MA declines "in bands C, D, E and F" although Band C (210,000–229,999) starts above the 209,000 pivot and the Band C row (`:34`) itself says "FIRST MA RISE"; `:90` "no enumeration defects" tested only the outcome that occurred. Both belong in the BD-21 exhaustion check's test set (prose-vs-table agreement is the second leg).

**ACTION**
1. LABOR rewrites `STATUS.md:140` item 11 to "4 scored rows + OPEN LAB-08" at the next closeout; the cell count stays five.
2. LABOR removes the frameworks item from the F2 charter batch before proposing it to Will.
3. LABOR adds the `:45`/`:34` prose-vs-table case to BD-21's test set.

**ASK:** none beyond the three lines above; file with the parent packet.

— DAEDALUS *(carve-out ①; self-committed)*
