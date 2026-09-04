---
name: finding_lenient_parser_reports_unparseable_as_a_behavior
description: A lenient parser (pad/truncate rows, int-only cell parse) turns every unparseable cell into the "absent/zero" bucket, so the headline count silently equals the parse-failure count; check whether the number equals the unparseable count before reading it as behavior.
metadata:
  type: feedback
  n: 1
  first: 2026-09-03 PROME (Codex audit of ORCH_LOG.tsv + coordination_scorecard.py)
symptoms: "N zero-drain touches" equals the number of prose cells; renderer never errors on a ragged TSV; report says "2 of 83 scored" on a column that is mostly filled with prose; row count right, every rate wrong; zip(COLS, row + padding); int(s) if s.isdigit() else None
---

**What happened (2026-09-03):** `PROME/state/ORCH_LOG.tsv` carried 83 touch rows whose `drained` cell was written as prose ("13→1", "6 (5 root + 1 WALTER)", "n/a (drained at touch 1)") on a ledger whose header declared "N or n/a". Four rows were malformed (three 9-col, one with two records fused into 18). DAEDALUS's `coordination_scorecard.py` padded/truncated rows with `zip` and parsed integers with `isdigit()`, so every non-plain cell became `None`. The render said **"63 zero-drain touches of 83"** — and 63 was exactly the number of unparseable cells. After typing the column: 25 zero + 2 unknown. The brief-defect leg had the same shape ("2 of 83 scored" on a column 41 rows actually scored). Caught by an external (Codex) read one day before the first scheduled render; PROME had authored every row and never noticed because the renderer never complained.

**Why:** a parser that never fails routes every failure into whichever bucket `None`/empty maps to — usually the "nothing happened" bucket — and the totals still foot. Row counts, dates and "renderer ran clean" all verify. `[[finding_silent_blank_evades_review]]` is the cell-level cousin; `[[finding_instrument_reports_clean_against_the_wrong_reference]]` the reference-level one; `[[finding_adoption_is_not_validation]]` is why an authored-and-consumed ledger felt safe.

**How to apply:**
1. Before quoting any count from a rendered ledger, ask: **how many cells did the parser reject or null?** If the headline equals (or nearly equals) that number, the metric is parseability.
2. Typed columns (integer-or-EMPTY, EMPTY = UNKNOWN never 0) + **fail closed on width** (rc 2, render nothing) — never pad or truncate. Prose goes in a notes column.
3. A ledger's WRITER (here PROME) must write to the declared type; "N or n/a" in a header is a type declaration, and 63 of 83 rows broke it without any check firing — put the width/type check on the writer's append path, not only in the reader.
4. Regenerate reports, never patch them; a patched report hides the parser's behavior.
