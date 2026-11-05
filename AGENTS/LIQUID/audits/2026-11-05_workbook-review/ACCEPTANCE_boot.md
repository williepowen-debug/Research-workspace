# Bounded repair: boot.py countdown and TSV header tolerance, 2026-11-05

Authority: Will in LIQUID's window 11:08 ET, "yes to all" (workbook review decision 2); STATUS §3 boot.py row, PROME prome-5c C4 self-edit. Acceptance written before code edit.

1. A catalyst whose event text begins with ✅ does not print in the countdown and does not count toward IMMINENT. A one-line count of hidden rows prints, so hiding is visible.
2. Every other row behaves as before, including `REVIEW GRADED` and `PENDING` rows, which do not begin with ✅. Bad dates and wrong field counts still report as malformed, whether or not the event begins with ✅.
3. CATALYSTS and PREDICTIONS readers and `--selftest` skip leading lines beginning `#`, before the column header only. A `#` line after the header is still a malformed row.
4. With no comment line present, parsed rows are unchanged (bytes of the current files give the same rows).
5. `boot.py --selftest` passes before and after. New checks fail against a copy with each change reverted.

Out of scope: no TSV is stamped. DOCKET L869 has the shared convention undecided, `asmade_audit.py` reads PREDICTIONS.tsv and LIQ-04 is Kernel-pinned. No gate, threshold or grading logic moves.
