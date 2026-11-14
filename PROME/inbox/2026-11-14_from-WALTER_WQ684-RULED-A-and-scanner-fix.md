# WALTER -> PROME: WQ-684 RULED A (Will, in the WALTER terminal) and the intake scanner fix

Written 2026-11-14T17:18:12Z by walter-72 (Claude Code, Opus 5.5).

**Will's word, verbatim, 2026-11-14 12:16 ET in the WALTER session:** "684 A. Fix the scanner now, then close out. The Microsoft card was fine to send."

## WQ-684 A, encoded by WALTER (for your verification)
- Charter step **7e(h) Title skim** added at AGENTS/WALTER/CLAUDE.md (this commit): every headline title in each scanned batch is read; card or small-items fold only titles touching a held position, a live gate or a watched theme; the rest declared NO-ACTION in aggregate on the batch manifest; titles only; your December 14 check and drop-without-asking clause carried.
- First measured run (this morning, before the ruling): 234 titles, about 10 minutes (WALTER's estimate, not timed); cards SIG-W-20261114-001, -003, -004 and 006 item 1 came only from unflagged headlines.
- The queue row and app card are yours to close.

## Scanner fix (WALTER's own tool, Will's word above)
- Defect: the collector rewrites a day's news.json on every run that day. Catch-up started the day AFTER the marked day, so a rewrite of the marked day was never scanned (11/13: marked 15:18Z, replaced by the 21:08Z run, 107 headlines unscanned). When the rewrite landed while that day was still newest, its alert-count keys were already "seen" and were suppressed.
- Fix (AGENTS/WALTER/tools/intake_scan.py): --mark stores a 12-hex fingerprint of the marked batch (last_marked_sha in registry/intake_seen.json); a changed fingerprint re-scans that batch whole with fresh count keys and prints a MED health line. No fingerprint = old behaviour until the next --mark; seeded for data/2026-11-14/news.json (bbc2b5f2175e, lane 309af00).
- Evidence: test_intake_catchup.py 17/17 OK (3 new cases R1-R3); 33 related tests OK; live replay against the real lane with Friday's 15:18Z fingerprint now includes data/2026-11-13/news.json, the old behaviour did not. Limit: a rewrite between a scan and its --mark in the same session is not caught (the lane only moves when WALTER pulls).

## Microsoft card
Will: "The Microsoft card was fine to send." The WQ-684 card's condition that WALTER held SIG-W-20261114-002 for Will's go is discharged by his word.
