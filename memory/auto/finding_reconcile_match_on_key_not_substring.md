---
name: finding_reconcile_match_on_key_not_substring
description: "A reconcile/sweep script must match on the KEY (id + path), never a bare substring that can appear in free-text notes — the failure returns success and can be right by luck."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 3c210a4b-b04e-49b8-a5fd-862bfb269f64
  modified: 2026-07-27T23:21:12.763Z
---

**A reconcile or bulk-update script must match on the KEY — id, recipient, path — never on a bare substring of the line. Free-text columns will eventually contain your match token.**

**The instance (WALTER, 2026-07-27).** A closeout one-liner flipped `delivery_log.tsv` rows from `written_not_delivered_pending_push` → `delivered` by testing whether the line contained the string `CORRECTION`. That word also appeared in the **free-text notes column** of two unrelated rows from a different date, so it flipped **8 rows when 6 had been written.**

**🔑 THE DANGEROUS PART IS THAT THE RESULT WAS CORRECT.** Both extra rows *were* genuinely delivered (their paths were in git — consumed-by-delete), so the value written was right. **Right answer, wrong method, and nothing would ever have flagged it.** It was caught only by reconciling the reported count against the number of files actually created.

**⇒ Match on `id + recipient + path` columns. Compare the affected-row COUNT against what you intended to change, and treat a mismatch as a stop, not a curiosity.**

**Same family as** `[[finding_printf_format_tsv_append_corruption]]` (a `%` in TSV text silently mangled and dropped a row) and `[[finding_pathspec_wildcard_ending_at_directory_matches_nothing]]` (a git pathspec that matched 0 files and returned success): **the loose matcher that silently does slightly the wrong thing and reports success.**

**It also surfaced a real finding underneath.** 774 rows still read `pending` while **all 774 paths were in git** — the column was only ever swept for the *current* session's rows at closeout, so historical rows never got reconciled and the field had become decorative, systematically **understating** delivery.

**Two durable lessons from the fix:**
- **A status column that is only ever updated by a remembered ritual WILL rot.** Mechanize it (`[[finding_mechanize_the_cap_not_the_ritual]]`). The fix shipped as a script that is dry-run by default, only ever flips one direction, refuses to write on a non-uniform field count, and reports true orphans without sweeping them.
- **Don't delete the stale column — check what CONSUMES it first.** "Drop the column" was the tempting simplification, but a health check consumed that exact claim to compare against git; removing it would have blinded the check. `[[finding_external_consumer_check_before_restructure]]`.

**And the sweep un-blinded the check:** it had been *skipping* every row that claimed `pending`, so it evaluated 187 rows afterwards where it had seen 17 before. **A reconcile can restore a check's coverage, not just a log's accuracy.**
