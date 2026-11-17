---
name: feedback_batch_ledger_commits_at_break_points
description: PROME batches its ledger and receipt commits at natural break points in a session (a pickup, a dispatch round, a desk's closeout with its rows), never one commit per line and never held to closeout
symptoms: about to commit a one-line ORCH_LOG, DOCKET, SCRATCH or CALENDAR edit by itself; several desk closeout receipts arriving minutes apart; PROME's commit count far above every desk's; four commits in fifteen minutes
metadata:
  type: feedback
---

Will, 2026-11-17 15:39 ET in PROME's chat, verbatim: "and yes I agree/approve you can start batching". He said it after an outside read-only audit counted PROME's commits for 11/10 to 11/17 (PROME recounted 703 of 1,756, of which 194 to 389 touched only its own ledgers, depending on which files count) and after PROME noted it had made four commits in fifteen minutes around one desk's closeout that afternoon.

**Why:** no rule requires a commit per ledger line or per receipt; WQ-249 requires the closeout ask and the held answer, not a commit for each. The commit cookbook already names a mid-session batch as an ordinary route. One-line commits swell the history and cost attention for no added safety.

**How to apply:** collect ledger edits (ORCH_LOG, DOCKET, WILL_QUEUE, WQ_LEDGER, SCRATCH, CALENDAR, GATES, inbox filings) and commit them together at a natural break: the end of a pickup or boot, a dispatch round, a desk's delivery and closeout taken together, or about hourly while work is steady. Record several closeout receipts in one commit. Do NOT hold edits to the session closeout: the working tree is shared, and a modified tracked file makes every other desk's rebase pull refuse (root Git Protocol). Commit before any context reset, checkpoint, desk launch that will pull, or machine switch. Exact-path commits through `PROME/tools/commit_check.py` as before. My reading, not Will's words: a self-authored inbox packet to another desk is still committed promptly, because an uncommitted packet never reaches its recipient (root carve-out ①).
