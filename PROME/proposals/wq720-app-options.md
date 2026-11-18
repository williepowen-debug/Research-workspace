# WQ-720 — explicit decision card

Question, options, context and conditions are decision terms. Queue Notes are operational; put changed conditions here or in the question, not only in Notes.

```decisions-options
{
  "schema_version": "decisions-options/3",
  "wq_id": "720",
  "queue_terms_sha256": "e10285c889664fb129fa2248c730a331acb43a84336f958800282129cad6241a",
  "choices": [
    {
      "id": "A",
      "label": "Adopt FALCON's wording as drafted",
      "meaning": "The test reads: mine clearance complete AND, on the IMF PortWatch daily count for the Strait of Hormuz (all vessel types), 45 or more transits on each of 10 consecutive calendar days. A day with no published figure breaks the run. No other tracker's count substitutes; if PortWatch cannot be read the test is ungradeable, never graded on a substitute. FALCON encodes it in its exit rules and updates the files that cite it.",
      "consequence": "The level does not move: 45 is the first whole number above half of 88 a day, the pre-war median of the same series. The test can fire late (PortWatch publishes 5 to 8 days behind) but not early."
    },
    {
      "id": "B",
      "label": "Adopt it, but with a 10-day average instead of every day",
      "meaning": "Same named series and the same missing-day rule, but the bar is a 10-day average above 44 transits rather than 45 or more on each of the 10 days.",
      "consequence": "Easier to meet: one very busy day can carry a 10-day average over the bar. FALCON recommends against it for that reason."
    },
    {
      "id": "C",
      "label": "Leave the wording as it is",
      "meaning": "The test keeps reading \"transits >50% of 88/day for 10 days\" with no named series. Nothing is encoded.",
      "consequence": "The ambiguity stays: a count from another tracker could be graded against the wrong baseline, and \"for 10 days\" could be read two ways on the day it matters."
    }
  ],
  "recommended_choice_id": "A",
  "context": "FALCON, the Gulf desk, keeps seven conditions that would end its thesis. The second reads, verbatim: \"Hormuz verifiably reopened: mine clearance complete AND transits >50% of 88/day for 10 days\". It does not say whose ship count is used, whether \"for 10 days\" means every day or an average, or what a missing day does. FALCON flagged this on 11/11 and drafted replacement wording on 11/18. Naming the data series changes the letter of the test, so it needs your word; nothing is encoded yet.",
  "conditions": [
    "The test is far from met under any reading: the newest PortWatch figure is 2 transits [11/15], and in 261 war days the count reached 45 or more on 3 days, longest run 2. These are FALCON's own figures from 11/18; PROME did not re-run them.",
    "88 a day is the pre-war median of this one series. Other trackers have other baselines, so a count from another tracker cannot be graded against 88.",
    "PortWatch publishes 5 to 8 days late and sometimes skips days. Under the draft a skipped day restarts the count.",
    "The words \"mine clearance complete\" also name no authority. FALCON did not draft that part and flags it for a later row if you want one.",
    "A tankers-only count instead of all vessels would need a new baseline and a separate proposal.",
    "No position, order or other threshold is involved.",
    "Every app answer needs Will's confirming word in chat."
  ],
  "confirmation": {
    "mode": "chat",
    "scope": "other",
    "reason": "Matching PROME-chat confirmation remains required under the installed fallback."
  }
}
```
