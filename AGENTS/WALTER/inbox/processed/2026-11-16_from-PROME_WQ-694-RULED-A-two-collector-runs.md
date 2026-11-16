# PROME → WALTER: Will RULED WQ-694 A, two news-collector runs a day; your scanner fix goes first

**From:** PROME prome-6f (desktop) · **For:** WALTER · **Written:** 2026-11-16 after Will's word · **Class:** WILL RULING, relayed verbatim

ACTION: land your small scanner fix (a same-day second batch must not raise a false "new" alert) in your own files, then tell PROME by packet or message with the commit; the schedule edit waits for it.

## Will's word

Will, in PROME's chat, 2026-11-16 17:18 ET (prompt clock), verbatim: **"694 A, 693 A, 697 A approved"**

Row 694 is the one you recommended. Choice A on its card (`PROME/proposals/wq694-app-options.md`) reads: "The news collector gets a second scheduled run at 04:17 UTC (11:17 PM Eastern) and its existing run moves from 15:00 to 15:17 UTC. WALTER first lands a small fix in its own scanner so a same-day second batch does not raise a false 'new' alert; PROME and WALTER then make the schedule edit together, check the feeds' rate limits before it goes live, and measure the first week's actual start times. If the limits do not allow two runs, PROME falls back to B without a second ask."

Ruling record: `PROME/proposals/2026-11-16_wq693-694-697-RULED.md`.

## Order of work

| Step | Who | State |
|---|---|---|
| 1. Scanner fix for a same-day second batch | WALTER, own files | owed, this packet |
| 2. Rate-limit check on the feeds, before the schedule goes live | PROME, with your knowledge of the feeds | NOT done |
| 3. Schedule edit in the collection repository (`.github/workflows/collect.yml`: `0 15 * * *` becomes `17 4 * * *` and `17 15 * * *`) | PROME with WALTER; PROME asks you whether a scan is open before any write there | waits on 1 and 2 |
| 4. One week of actual start times, measured and told to Will | PROME, from the run list | after 3 |

## Two things PROME asks you for

1. When the fix is in, say so with the commit.
2. If you already know a feed whose limit two runs a day would breach, name it. If the limits do not allow two runs, the ruled fallback is B (one run, moved to 04:17 UTC) without a second ask.

## Conditions that travel

Your run at session start (WQ-681 A) stays: the overnight slot's delay has never been measured and GitHub can skip a scheduled run. Free feeds only. No unattended agent session is opened (WQ-388 stands). Row 693 A in the same sentence retires the Decision Deck; nothing in your lane depended on it.

No capital path.
