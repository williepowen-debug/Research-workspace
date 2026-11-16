# WQ-694 A step 1 and the overwrite finding (walter-5a, 2026-11-16 22:3xZ)

Ruling: Will 2026-11-16 17:18 ET "694 A, 693 A, 697 A approved" (PROME packet, processed; record PROME/proposals/2026-11-16_wq693-694-697-RULED.md).

| Item | State | Evidence |
|---|---|---|
| Step 1, follow-up 6 | DONE, local commit ff1bd682aa | intake_scan.settled_key: at --mark a rewritten batch's `news:<cls>:<batch>@<sha>` count key is stored plain when the stored last_marked_sha is that sha. Tests R11/R12 fail on HEAD~ code, pass now; 26/26 catch-up, cruise 15, GPU 3, boot-repairs 15 pass. Live read-only scan: 0 new, 17 suppressed |
| Overwrite loss under two runs a day | OPEN, blocks step 3 | Research-Intake scripts/fetch_newsweep.py line 119 names data/<UTC date>/ and news.json holds only headlines new since the last run (news_seen.json dedup). 04:17Z and 15:17Z share a UTC date, so run 2 replaces run 1's file. Without a WALTER scan and mark between them, run 1's headlines never reach a scan. Lane precedent: data/2026-11-13/news.json written by e1bd850 (15:18Z) and 1f8a9f3 (21:08Z) |
| Options sent to PROME | (a) scanner reads every committed version since the mark from lane git history, read-only (WALTER recommendation; bounded independent read before step 3); (b) collector writes one file per run (collection-repo write, changes the glob the cruise/GPU queues use); (c) ruling B, which needs Will's word because the B fallback is ruled for rate limits only | message to prome-6f 2026-11-16 22:3xZ |
| Rate limits | No feed known to breach at two runs a day; Google News RSS publishes no limit; provider terms NOT re-read this session (recall, not a check) | — |
