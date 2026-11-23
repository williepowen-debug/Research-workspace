# WQ-737 — explicit decision card

Question, options, context and conditions are decision terms. Queue Notes are operational; put changed conditions here or in the question, not only in Notes.

```decisions-options
{
  "schema_version": "decisions-options/3",
  "wq_id": "737",
  "queue_terms_sha256": "a3272279c8a51e81fddada11ad8d354b0594c9f3c1e97c2bbbebc6b805e113f0",
  "choices": [
    {
      "id": "A",
      "label": "Adopt only beside a second region",
      "meaning": "The crops score goes to 4 only when the FAO cereals index is up 20% or more on a year earlier on 2 straight first prints AND a second crop region confirms.",
      "consequence": "AEOLUS writes the paired step into its current table. Nothing fires today: +12.5% in October."
    },
    {
      "id": "B",
      "label": "Adopt it alone",
      "meaning": "The index condition by itself lifts the crops score to 4.",
      "consequence": "The score could rise on a price move that has nothing to do with weather."
    },
    {
      "id": "C",
      "label": "Retire the step",
      "meaning": "The cereals-index step is removed from the score.",
      "consequence": "The crops score reaches 4 only through its regional conditions."
    }
  ],
  "recommended_choice_id": "A",
  "context": "AEOLUS's crop score has a step named 'cereals index breaking' that never had a number. It owed one by 11/10 and missed. On 11/23 it proposed this one with its history.",
  "conditions": [
    "Six episodes in 1991 to 2026, none in the strong El Nino years 1997-98, 2015-16 or 2023-24.",
    "The number was chosen after looking at the history, and the count uses revised data while the rule reads first prints.",
    "The 12/04 print would need about 126.7 to start the count.",
    "No score moves on any answer. No money.",
    "Every app answer needs Will's confirming word in chat."
  ],
  "confirmation": {
    "mode": "chat",
    "scope": "other",
    "reason": "Matching PROME-chat confirmation remains required under the installed fallback."
  }
}
```
