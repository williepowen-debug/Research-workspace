# WQ-694 — explicit decision card

Question, options, context and conditions are decision terms. Queue Notes are operational; put changed conditions here or in the question, not only in Notes.

```decisions-options
{
  "schema_version": "decisions-options/3",
  "wq_id": "694",
  "queue_terms_sha256": "c8bc9ceb4dfb4bd3b939fc3c446c431c5ae3f7e01afdc2b0c715c8efa08f87ed",
  "choices": [
    {
      "id": "A",
      "label": "Two runs a day, off the hour",
      "meaning": "The news collector gets a second scheduled run at 04:17 UTC (11:17 PM Eastern) and its existing run moves from 15:00 to 15:17 UTC. WALTER first lands a small fix in its own scanner so a same-day second batch does not raise a false 'new' alert; PROME and WALTER then make the schedule edit together, check the feeds' rate limits before it goes live, and measure the first week's actual start times. If the limits do not allow two runs, PROME falls back to B without a second ask.",
      "consequence": "Even at the worst delay seen (8.6 hours), the overnight batch lands by about 7:55 AM Eastern. No unattended agent session is involved: this is the collector's own schedule on GitHub. WALTER's run at session start stays as the backstop."
    },
    {
      "id": "B",
      "label": "One run a day, moved to the overnight slot",
      "meaning": "The single run moves from 15:00 UTC to 04:17 UTC. Nothing else changes.",
      "consequence": "The morning is covered; the afternoon's news then waits until the next night unless a session starts and runs the collector by hand. No rate-limit question."
    },
    {
      "id": "C",
      "label": "Leave the schedule as it is",
      "meaning": "No change. Coverage of the morning keeps depending on when a session starts and runs the collector.",
      "consequence": "Nothing to build. The 4.6 to 8.6 hour delay stays, and an 8:30 AM release can go unread until someone boots."
    }
  ],
  "recommended_choice_id": "A",
  "context": "The news collector is scheduled for 15:00 UTC (10:00 AM Eastern) each day, and GitHub starts it 4.6 to 8.6 hours late every day: the last seven scheduled starts ran between 19:37 and 23:38 UTC, and the two weeks before were the same (WALTER's read of the run list, November 16). So overnight and early-morning stories reach the desks late unless a session starts and runs the collector by hand, which you allowed on November 12 (WQ-681 A). WALTER, which owns the lane, recommends option A.",
  "conditions": [
    "Whether two runs a day fits the feeds' rate limits has NOT been checked; option A is conditional on that check passing, with B as the fallback.",
    "The delay at an overnight slot has never been measured. GitHub's delay depends on its load, and it can skip a scheduled run outright, so the run at session start stays.",
    "A second run on the same UTC date rewrites that day's file; WALTER's scanner handles the rewrite but would raise one false 'new' alert a day until its small fix lands. WALTER says it can do that this week, and the schedule change waits for it.",
    "Free feeds only; nothing here costs money or sends your name anywhere. No unattended agent session is opened (WQ-388 stands).",
    "Every app answer needs Will's confirming word in chat."
  ],
  "confirmation": {
    "mode": "chat",
    "scope": "other",
    "reason": "Matching PROME-chat confirmation remains required under the installed fallback."
  }
}
```
