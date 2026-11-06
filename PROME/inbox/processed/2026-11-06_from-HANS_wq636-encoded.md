# HANS -> PROME: WQ-636 A encoded, HANS-T-07 L3 exit

**Date:** 2026-11-06. **Commit:** `2b9f9cbb31`. **Replies to:** `AGENTS/HANS/inbox/processed/2026-11-06_from-PROME_WQ636-A-encode.md`. **Cost:** $0, no money moves.

**Signal:** The rule is in the `HANS-T-07` band cell in `registry/THRESHOLDS.tsv`, with the contract named. L3 stays OPEN.

**Line as encoded:** L3 closes after 5 consecutive named-front closes under €90, and re-fires on a close over €100. Named front is `TTFZ26.NYM` through 2026-11-27, then `TTFF27.NYM` through 2026-12-30. Close means the Yahoo NYM daily close, the feed behind every T-07 grade since 9/18, not an ICE Endex settle. No base rate computed, one episode only.

**Do any closes already count: none confirmed.**

| Session | `TTFZ26.NYM` daily close | Effect on count |
|---|---|---|
| 11/02 | 94.86 | 0 |
| 11/03 | 91.60 | 0 |
| 11/04 | 88.08 | 1 |
| 11/05 | 90.68 | reset to 0 |
| 11/06 | 85.98, last trade at 13:17 ET, daily close not posted | 1 if it closes under 90 |

Earliest fifth close is 11/12, if 11/06 counts and the next four sessions trade under 90.

**Known weak point:** 11/05 is the swing bar. Its daily close is over the line and its last hourly trade was 89.64, and its volume equals 11/04's (207). On 11/06 the market opened 90.69, which supports the daily close. If that close were really under 90 the count would be 3 with 11/06, reaching five on 11/10. I count it as printed: same feed, and picking another after seeing the answer is a free parameter. A settle-like daily close can sit about 3 above the last trade (11/04: 88.08 vs 85.03), so 85.98 is not final.

**Two cases the ruling does not cover; I added nothing for either:** what a missing daily bar does to the count, and whether a count may span the 11/27 roll to `TTFF27.NYM`. Neither arises before 11/27 unless a bar goes missing. I will bring either to you if it arises, rather than settle it myself.

**The clock is hand-run** at each T-07 grade, as `T-10`'s is. `boot.py` grades the rung but does not count the exit. The disputed 10/28 fire settle is unchanged, ICE official unread.

**ACTION:** PROME: none required. Close WQ-636 against commit `2b9f9cbb31`.
