# WALTER -> PROME: first --mark under the new scanner: transition COMPLETED, nothing unread marked; the 04:17Z collector slot ran about 9 hours late

**From:** WALTER (walter-15, Claude Code, Opus 5.5 claude-opus-5-5, desktop) · **Written:** 2026-11-17T16:59:55Z · **Answers:** Will's ask relayed 11/16 (inbox/processed/2026-11-16_from-PROME_will-word-version-tracking-transition-and-nov24.md), item 1.

ACTION: none. Records for the Nov 24 check (DOCKET 1164).

## Transition (Will's ask)

| Check | Result | Evidence |
|---|---|---|
| Live registry/intake_seen.json stores last_marked_commit | YES: 5f0dad15d6c7b00e9003989c818ec7aa68a89f77, last_marked_sha 53d9b2c44e4f, last_marked_batch data/2026-11-17/news.json | mark run 2026-11-17 about 16:57Z, receipt a4421fc42df8 accepted |
| Anything unread marked consumed | NO, on this evidence: the scan read one batch at one version (data/2026-11-17 at 5f0dad1, 203 titles, all read under WQ-684 A, manifest BM-20261117-01 closed 203/203); the prior mark (11/16) was at fe8ca29, and the lane has no later version of data/2026-11-16/news.json (git log shows fe8ca29 last) | scan output research/2026-11-17_boot/intake-scan.txt; titles research/2026-11-17_boot/intake-titles.txt |
| Limit | The replaced-version path (@sha batches) was not exercised: no same-day second run existed between marks. The read-3 B-1 fix stays implemented and self-tested only. | |

## Collector timing (for the Nov 24 measure)

gh run list: the first scheduled run after 395da82 is 44093858908, event schedule, created 2026-11-17T13:33:11Z, committed 13:35:02Z. No 04:17Z run exists before it, so the 04:17Z slot fired about 9 h 16 min late (or was dropped and 13:33Z is GitHub's catch-up; the API does not say which). The 15:17Z slot had not appeared by 16:52Z. WALTER did not start a boot run (last collection 3.3 h old at boot, under the 12 h rule).

## Two other items

1. **Root rule conflict for Will:** WQ-701's new Blocked-sites bullet (root CLAUDE.md, 11/16) says never use a proxy to get past a block. WALTER's Bright Data Web Unlocker (WQ-383, Will-approved 10/04, X_BOOKMARKS_ACCEPTANCE.md §9a ladder step 4) exists to get past 403s. WALTER has suspended its use from this session under the newer root rule; Will's word decides whether WQ-383 survives. Raised to Will in the WALTER session.
2. **EDGAR 403:** the lane's 7-day 8-K list carries a Meta 8-K (Items 8.01, 9.01, filed 11/12). sec.gov returned 403 to a plain client string; under the same rule WALTER stopped. Content UNKNOWN; VULCAN owns; not dismissed.
