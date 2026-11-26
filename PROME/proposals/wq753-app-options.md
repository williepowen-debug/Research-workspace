# WQ-753 — explicit decision card

Question, options, context and conditions are decision terms. Queue Notes are operational; put changed conditions here or in the question, not only in Notes.

```decisions-options
{
  "schema_version": "decisions-options/3",
  "wq_id": "753",
  "queue_terms_sha256": "d0ff42761bc0dcdf9c1d7bf22e79894330426d8d1d2d1769293ddcaf2a84b530",
  "choices": [
    {
      "id": "A",
      "label": "Re-key, Green above 18",
      "meaning": "FALCON replaces the unnamed ship counts in two of its Hormuz watch bands with the IMF PortWatch daily count for the strait: Green above 18 ships on 10 consecutive daily prints, Yellow 14 to 18, Orange 10 to 14, Red below 10. Every other clause of the two bands is unchanged.",
      "consequence": "FALCON edits two band texts in its own workbook. No mark, score, gate, ladder rung or prediction moves."
    },
    {
      "id": "B",
      "label": "Re-key, Green above 45",
      "meaning": "The same re-key, but Green needs more than 45 ships a day, the reopening number you ruled for FALCON's thesis-kill under WQ-720 A.",
      "consequence": "The watch band turns Green only when the thesis-kill would also be met; there is no earlier recovery signal."
    },
    {
      "id": "C",
      "label": "Leave the bands as written",
      "meaning": "The two bands keep their current wording (more than 25 a day, fewer than 2 a day), with no named counting source.",
      "consequence": "FALCON records the 11/04 proposal as declined. Most war days stay outside any named band."
    }
  ],
  "recommended_choice_id": "A",
  "context": "FALCON proposed this on 11/04 and it was never ruled; DAEDALUS found the gap on 11/25. FALCON supplied the base rate it owed tonight from 2,883 daily prints, 2019 to 11/22/2026: before the war every day was above 18 ships (minimum 30); during the war 87.7% of 268 days were below 10 and the longest run above 18 was 5 days. The current wording leaves 222 of 268 war days in no band.",
  "conditions": [
    "The base rate is FALCON's own pull; PROME did not re-run it.",
    "The base rate does not separate 18 from 45: neither level occurred for 10 straight days in the war. FALCON's reason for 18 is that Green should mean recovery under way, and 45 that the closure regime is over.",
    "This changes two band texts only. It is not a trade, and energy stays stood down.",
    "Not urgent: nothing is waiting on it."
  ],
  "confirmation": {
    "mode": "chat",
    "scope": "other",
    "reason": "Matching PROME-chat confirmation remains required under the installed fallback."
  }
}
```
