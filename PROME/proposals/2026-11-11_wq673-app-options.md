# WQ-673 — explicit app options

PROME's queue options and recommendation. The exact queue row remains authoritative, including all caveats. This card is not an approval or ruling.

```decisions-options
{
  "schema_version": "decisions-options/2",
  "wq_id": "673",
  "queue_row_sha256": "4295494f21b26e630fd380691dfe93bf62d871283ac0b1ae08bd2138ec8ec87c",
  "recommended_choice_id": "A",
  "confirmation": {
    "mode": "chat",
    "scope": "other",
    "reason": "The installed fallback requires matching confirmation in PROME’s chat for every answer."
  },
  "choices": [
    {
      "id": "A",
      "label": "Grant all four",
      "meaning": "PROME gets all four standing permissions as worded in the row, each reported the same day and undone by naming it",
      "consequence": "PROME records this choice against the complete proposal and conditions shown on the card. The app executes no action; added changes require your words."
    },
    {
      "id": "B",
      "label": "Grant the first two only",
      "meaning": "the forecast-grading permission (1) and the next-step permission (2); retiring process items and manual wording edits keep coming to you",
      "consequence": "PROME records this choice against the complete proposal and conditions shown on the card. The app executes no action; added changes require your words."
    },
    {
      "id": "C",
      "label": "Grant none",
      "meaning": "nothing changes; these kinds of question keep coming to you",
      "consequence": "PROME records this choice against the complete proposal and conditions shown on the card. The app executes no action; added changes require your words."
    },
    {
      "id": "D",
      "label": "I'll name which",
      "meaning": "you say in chat which of the four to grant, or reword any of them",
      "consequence": "PROME records this choice against the complete proposal and conditions shown on the card. The app executes no action; added changes require your words."
    }
  ]
}
```
