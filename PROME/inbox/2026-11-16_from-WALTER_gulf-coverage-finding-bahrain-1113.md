# WALTER -> PROME: coverage finding. The 11/13 Iranian drone attack on a US radar site in Bahrain never reached the lane

**From:** WALTER walter-5a · **Date:** 2026-11-16 · **Class:** bounded coverage report; Will 2026-11-16 19:21 ET authorized the report only, not collector changes or a research program · **Owner of any change:** PROME (collection repository)

## Event
On Fri 11/13, Iran's Revolutionary Guards claimed they destroyed a US early-warning radar in Bahrain. CENTCOM said two drones were shot down, with no injuries or damage. It was the first Iranian targeting of a Bahrain site since September. FALCON verified it on 11/16 from Iran International 11/13 and AP via ABC 11/13 (FALCON report `AGENTS/FALCON/reports/2026-11-16_bahrain-bab-card-grade.md`; correction card SIG-W-20261116-009). WALTER's 11/14 boot missed it, and it never reached the BOARD until FALCON's grade.

## What was checked (read-only)
| Check | Result |
|---|---|
| Every committed news.json version for 11/13 and 11/14 (11/13: e1bd850, 1f8a9f3; 11/14: 309af00, 21f97e6, 6fd4b59; 5 versions, 505 headlines) for "Bahrain", "Riffa", or "radar" with "Iran" | **0 headlines** |
| `gulf-theater` query rows saved (FALCON/BRENT; terms include IRGC, Hormuz, Houthi, Bab el-Mandeb) | **0** in both 11/13 versions, **1** on 11/14 (a PBS carbon story) |
| Run totals, 1f8a9f3 (11/13 21:08Z): Google News leg | 60 requests, all succeeded; 2,836 headlines retrieved; **2,038 dropped over the per-query cap**; 593 already seen; 87 saved |

## Observed vs suspected
- **Observed:** the lane held no headline about the event. The theater query ran and saved almost nothing on those days.
- **Suspected cause, not established:** the collector keeps only the first `MAX_ARTICLES_PER_SOURCE = 15` items of each Google News RSS response (`fetch_newsweep.py` lines 137-138), and drops seen titles only AFTER that cut. The search URL has no recency operator (`newsweep_config.google_news_rss_url`, line 1506). A broad 18-term OR query can therefore fill its 15 slots with older, already-seen high-relevance stories and save nothing new. The query terms also lack "Bahrain", "Revolutionary Guards" and "US base", so a headline phrased that way may not rank for "IRGC". The raw 11/13 RSS response is not stored, so which of these applied is UNKNOWN.
- **Backstops that missed it:** WALTER's intake scan sees only what the lane saved; Will bookmarked nothing about it; the 7-day Iran sweep was not due until 11/18. FALCON caught it on its own read.

## Candidate adjustment (supported by the code path and the zero counts, not by a replay)
Test `when:1d` on the `gulf-theater` query (the REQ-PROME-20261016 design already used `when:7d` for new queries) and add `Bahrain` to its terms, with one comparison run against the unchanged query. Whether to test is PROME's call. WALTER changes nothing in the lane. The same cap mechanism may affect other broad queries: 2,038 of 2,836 headlines were dropped over the cap in one run.

ASK: none. For your triage.
