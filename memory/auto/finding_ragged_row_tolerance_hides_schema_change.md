---
name: finding_ragged_row_tolerance_hides_schema_change
description: "Three ways scripted TSV-ledger writes fail SILENTLY — ragged-row tolerance, truncate-then-raise, and append onto a missing trailing newline. All pass a naive check."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: ad692cde-f719-41c5-97b2-f45a621a1f7f
  modified: 2026-08-12T20:57:02.934Z
---

The tooling **around** a shared TSV ledger is more dangerous than any edit **to** it. Three distinct silent-failure modes hit RED in one session (2026-08-12, T5/T4); each destroys or hides data and each passes a naive check.

**① Ragged-row tolerance turns a header-only edit into a zero-row read.** A forgiving filter (`if len(row) >= len(header) - 2`) exists to survive dirty data. Widen the header without widening every data row and *every* row now fails it — the consumer reads **zero rows and reports success**. Found in `AGENTS/RED/scripts/boot.py:tsv()` while adding 3 columns to a 9-row registry: a header-only commit would have printed an **empty trigger section**, no exception, exit 0, on the scan that decides whether a pre-registered falsifier fired.

**② `csv.writer` with `QUOTE_NONE` truncates the target, then raises.** `open(path,'w')` truncates *before* the first row is written, so an exception partway through `writerows()` does not fail safe — it leaves a destroyed file. One cell needing an escape took **KB.tsv from 86 rows to 9**. Recovered only because the file was uncommitted and `git checkout` had a clean HEAD.

**③ Appending to a file whose last line lacks a trailing newline merges two records.** An `'a'`-mode write landed a new row directly onto the previous row's last cell: one 27-field line instead of two 14-field lines, and the new row **ceased to exist as a record** — in an append-only audit trail. It passed validation because the check validated *the row being written*, not *the file being written into*, and the field-count check used `awk END{}`, inspecting only the last line, which was clean by construction.

**How to apply:**
- **Read the consumer's parser before editing the file it reads.** The landmine is in the consumer, not the data.
- **Never open a live ledger with `'w'`.** Read → modify in memory → write `.tmp` → `os.replace` (atomic).
- **Ensure the file ends with a newline before appending.**
- **After every write, field-count the WHOLE file**, not the last line: `awk -F'\t' 'NR==1{c=NF} NF!=c&&NF>0{print NR": "NF}'`. Then re-run the actual consumer and confirm the expected **row count** appears in its output — inspection and exit codes both pass on a file nothing will read ([[finding_test_the_guard_not_just_the_guarded]]).
- **Commit a ledger BEFORE a scripted pass, not after** — git HEAD is the recovery path, and it only works if the good version is in it.
- Related silent-zero class: [[finding_verification_zero_is_ambiguous]], [[finding_discovery_tool_wrong_slice_false_zero]]. Related invisible-content class: [[finding_a_file_that_examples_its_own_structure_is_ambiguous]].
