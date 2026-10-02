# X → WALTER intake: findings and a bounded pilot plan

**Written:** 2026-10-02 (evening, walter-61), at Will's terminal request ("Can you look into this") about the X-posts → durable queue → WALTER idea from his earlier conversation.
**Status:** PROPOSAL ONLY. Nothing built, no account created, no money spent, no boot step added. Adding any intake sweep to WALTER's boot is a protocol change (RULE 8) and needs Will's word first.

## 1. What Will actually forwards from X (WALTER's own logs, 2026-08-03 → 10-02)

| Measure | Value |
|---|---|
| X-origin items Will sent (Telegram screenshots/links) | **187** over 19 active days (median 6/day, max 45) |
| Dispatched / killed | **78 / 109** (42% became a signal) |
| Distinct accounts behind them | **132**; **98 appeared only once** |
| Share covered by the most-frequent 10 / 20 / 40 / 60 accounts | 30% / 44% / 62% / 70% |

Method: `@handle` regex over `route_log.tsv` origin cells and `kill_log.tsv` origin+summary cells where the origin names Will, plus rows mentioning X/x.com/tweet. **Limits:** the coverage figures are in-sample (the top accounts were picked from the same items), so a list chosen in advance would do worse. A handle quoted inside a post can be miscounted as its source. 11 items had no handle recorded.

**So what:** Will's useful X content comes from a long tail. A fixed 40-account feed would have missed at least ~40% of what he forwarded. It would also ingest every other post from those 40 accounts (a squawk account posts dozens a day), most of it noise for WALTER to kill.

## 2. What X's API can and cannot do (verified 2026-10-02)

| Fact | Source |
|---|---|
| Pay-per-use, no subscription: **$0.005 per post read**, $0.010 per user read, **$0.001 per owned-data item (your own bookmarks, likes, posts)**; same item re-read in one UTC day is free; cap 3M post reads/month | docs.x.com/x-api/getting-started/pricing, **read by WALTER** |
| **No endpoint exposes notifications or the "For You" feed.** The nearest is the reverse-chronological Following timeline | subagent, docs.x.com endpoint map |
| **Bookmarks endpoint** (`GET /2/users/:id/bookmarks`) needs a one-time user login (OAuth2 PKCE, `bookmark.read`); 100 per page, 180 calls/15 min | subagent, docs.x.com |
| Selected accounts: user timeline, X List timeline, recent search (`from:a OR from:b`, 512-char queries) or filtered stream (1,000 rules) are all available on pay-per-use | subagent, docs.x.com |
| Terms: stored X content must be **deleted or updated within 24h** when a post is deleted or edited; no training/fine-tuning of models on X content (analysis not explicitly barred) | subagent, X Developer Agreement/Policy |

Cost arithmetic (subagent, at $0.005/read):
- 40 accounts × ~30 posts/day ≈ 36k reads/month ≈ **$180/month**
- 10–15 accounts, excluding replies and reposts ≈ **$45–70/month**
- Bookmarks, 10–30/day ≈ **$1–2/month**

**Not confirmed:** whether empty polls are billed, minimum credit purchase, whether bookmark folders need Premium, and whether sending post text to an LLM API counts as "distribution" under X's policy.

## 3. The design point the earlier conversation missed

**Will's picks are the signal, and X already stores them durably: his bookmarks.** If Will bookmarks a post instead of screenshotting it, the bookmark list *is* the durable queue:
- It covers recommended posts and followed accounts alike, because Will chose them, not a fixed list.
- It needs no collector or cron. WALTER reads new bookmarks at boot, the same way it reads the intake lane.
- It costs about $1–2/month on official, compliant access.
- The trigger problem is unchanged but no worse: today's screenshots also wait until WALTER is launched. Telegram can drop messages; bookmarks can't.

Already half-built for the same purpose: the **phone → GitHub signal path** (`design/PHONE_SIGNAL_INGESTION.md`). The receiving side has been shipped since 7/27. The remaining step is Will's ~15–20 min setup (a GitHub token plus an iOS Shortcut). It suits free-text notes and non-X links; bookmarks suit X posts.

⚠️ **Disclosed:** WALTER already reads single posts by URL through `api.fxtwitter.com`, an unofficial, free service not covered by any X agreement (used twice today). It works, but it carries terms risk and could stop working at any time. Official bookmark reads would replace it for bookmarked posts.

## 4. Recommended pilot (2 weeks, bounded)

**Phase 1: bookmarks (about $10 of prepaid credit covers it)**
1. **Will:** create an X developer app, buy a small prepaid credit (e.g. $10), and authorize bookmark read once. The token lives in a local `.env`, never in git.
2. **WALTER:** build `tools/x_bookmarks_scan.py` (a sibling of `phone_scan.py`). It pulls bookmarks newer than the last-seen ID, dedups on post ID, and keeps post text out of git (IDs and WALTER's own signal text only) to honour the 24h deletion rule. It also surfaces malformed or failed reads loudly. Wire it in as a boot step **only after Will approves** (RULE 8).
3. **Will:** for two weeks, bookmark instead of screenshot where convenient. Telegram keeps working in parallel; nothing is cut over.

**Measure:** bookmarks per day; WALTER's dispatch rate against the 42% screenshot baseline; time from post to WALTER's disposition; and which accounts appear (would a 15-account feed have caught them?).

**Phase 2, only if Phase 1 shows a gap:** a 10–15-account official feed (exclude replies and reposts, ~$45–70/month cap), compared against the bookmarks for the same weeks.

**Not in the pilot:** unattended WALTER runs. A scheduled, unwatched WALTER session that writes to the repo conflicts with the one-machine-at-a-time git rule and is the same authority question as WQ-369. If faster pickup matters, the cheapest step is an alert, not autonomy: a lane-side check that pings Will when a bookmark matches a high-priority term.

## 5. Will's decisions

1. **Account access and spend:** create the X developer app and fund roughly $10 of prepaid credit? (Yes/no; any monthly cap.)
2. **Storage:** keep X post text out of git (IDs only, WALTER's summary in the signal)? This is WALTER's recommendation because of the 24h deletion rule. Note that BOARD signals already quote posts today, which is the same exposure at a smaller scale.
3. **Trigger:** accept "processed at the next WALTER launch" for the pilot?

**Owner notes:** WALTER would own the scan tool and boot step (after approval). RESEARCH-INTAKE is untouched in Phase 1. PROME carries WQ-369, the related autonomy question.
