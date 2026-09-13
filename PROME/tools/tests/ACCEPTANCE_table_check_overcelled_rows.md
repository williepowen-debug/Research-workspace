# ACCEPTANCE — `table_check.py`, the over-celled markdown row

**Written 2026-09-12 22:3x ET BEFORE any code**, per `PROME/CLAUDE.md` § Session Process Controls
(WQ-229 repair-completion discipline). The test list below IS these conditions; it is not a restatement
of the reported symptom.

---

## The defect, in its own terms

`PROME/STATUS.md` L21 carried **five cells in a three-column table**. In GitHub-Flavored Markdown a row
may not exceed its header's column count: the excess cells are **dropped from the rendered output with no
error and no visual tell.** Two cells of that row — a live claim about the closeout dashboard-build
procedure (L339 leg g) and the account of the L338 date slip — were therefore invisible to every reader of
the rendered file, while remaining fully visible to a raw-text reader.

⛔ **The reason this matters more than one bad row:** the surface is a *boot-read state file*. A raw reader
(a Claude session using `cat`) sees the content and believes it was communicated; a rendered reader (the
operator, the Will-facing views, any markdown viewer) never saw it. **The two readers disagree and neither
one can tell.** Spine audit #13 ran over this exact file the same day the row was written and did not catch
it, because a spine audit reads *claims*, and this defect destroys a claim rather than falsifying one.

`[[finding_silent_blank_evades_review]]` · `[[finding_truncation_returns_a_plausible_answer_not_an_error]]`

---

## Acceptance conditions — the properties the repair must hold

1. **A row with MORE cells than its header is flagged.** This is the silent-drop direction and the only
   direction that loses content.
2. **A row with FEWER cells is a different fact and is not reported as the same class.** Markdown pads
   short rows; nothing is lost. Reporting both under one label would train the reader to ignore the flag.
3. **An escaped pipe (`\|`) inside a cell is not a separator.** Prose in these files quotes shell
   (`` `ls \| wc` ``); counting those would false-flag well-formed rows and the check would be turned off.
4. **A pipe inside an inline code span IS a separator**, because GFM splits on it. The check must agree with
   the *renderer*, not with what an author intended. A check that is kinder than the renderer certifies
   rows the renderer will still break.
5. **The perimeter is derived, never hand-listed** — PROME's `mode=whole` rows in
   `PROME/registry/READS.tsv`. A hand-list is a second source of truth that goes stale against the manifest.
6. **The report locates the fix without a second pass** — file, 1-indexed line number, header width,
   observed width, and the text of the cells that will be dropped.
7. **Absence of tables is not a failure.** A file with no table, or a `|`-leading line that is not a table,
   produces no finding and rc 0.

---

## Neighbour categories — CONSIDER all five (`PROME/tools/tests/README.md`)

| # | Category | Disposition |
|---|---|---|
| 1 | **Ordinary** | TESTED — a well-formed 3-cell row in a 3-column table produces no finding. |
| 2 | 🔴 **Overlap** | TESTED — a row that is BOTH over-celled AND contains an escaped pipe. The escape must be discounted *and* the row must still flag; the two rules interact and either one alone gets it wrong. |
| 3 | **Wrong owner** | TESTED — a table inside a fenced code block is an *example*, not a live table, and must NOT flag (`[[finding_a_file_that_examples_its_own_structure_is_ambiguous]]`). Conversely a real table immediately after a fence closes MUST flag. |
| 4 | **Missing information** | TESTED — a header line with no separator row beneath it is not a table; a file that does not exist; an empty file. Each returns no finding and never crashes. Fail loud on an unreadable path (rc 2), never silently clean. |
| 5 | **Concurrent activity** | **N/A, justified** — the check is a read-only single-pass over file text and holds no state across runs. There is no cursor, no receipt and no baseline to race. A concurrent write changes *what is read*, which the next run re-reads; there is no interleaving that can produce a wrong verdict about the bytes actually read. |

---

## What passing establishes

**IMPLEMENTED · TESTED** against the conditions above. **NOT INDEPENDENTLY VERIFIED** — that needs a reader
who did not write this and who devises a counterexample of their own (`[[finding_adoption_is_not_validation]]`).
This is a small self-contained check over PROME's own surfaces, not a gate on a shared contract, so under
WQ-229 it does not require an independent reader before being called fixed — but it is also not to be
described as verified.
