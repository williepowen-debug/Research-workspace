# WQ-738 — explicit decision card

Question, options, context and conditions are decision terms. Queue Notes are operational; put changed conditions here or in the question, not only in Notes.

```decisions-options
{
  "schema_version": "decisions-options/3",
  "wq_id": "738",
  "queue_terms_sha256": "b4cad87271151b8b246d3725161a4b339779ee2965dba5cf23bee448de204bcb",
  "choices": [
    {
      "id": "A",
      "label": "Both regions at their existing lines",
      "meaning": "'A second region confirming' means South Africa's maize AND Australia's wheat are both cut 15% or more at the same monthly USDA report. With the cereals index condition also met, the crops score goes to 4.",
      "consequence": "No new number. Nothing fires today: South Africa is down 8.65% and Australia 5.98%."
    },
    {
      "id": "B",
      "label": "AEOLUS counts the history first",
      "meaning": "AEOLUS counts how often both regions were down 15% together, proposes a meaning with that record, and the question returns to you.",
      "consequence": "The step to 4 stays ungradeable until then."
    },
    {
      "id": "C",
      "label": "Retire the step to 4",
      "meaning": "The crops score stops at 3 on these conditions.",
      "consequence": "The cereals condition you adopted today is removed with it."
    }
  ],
  "recommended_choice_id": "A",
  "context": "On 11/23 you adopted the cereals price condition only beside a second crop region. AEOLUS encoded it and reported that the second half has no number, so the step cannot be graded.",
  "conditions": [
    "Nobody has counted how often both regions fell 15% in one season; A could be very hard or easier than it sounds.",
    "Neither new step has a rule for coming back down.",
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
