# WQ-676 — explicit app options

PROME's queue options and recommendation. The exact queue row remains authoritative, including all caveats. This card is not an approval or ruling.

```decisions-options
{
  "schema_version": "decisions-options/2",
  "wq_id": "676",
  "queue_row_sha256": "e4792bd39ac7a448d8f6081cef57fef6449975b391d2ed3b6e9f8c6c3103b970",
  "recommended_choice_id": "A",
  "confirmation": {
    "mode": "chat",
    "scope": "other",
    "reason": "The installed fallback requires matching confirmation in PROME’s chat for every answer."
  },
  "choices": [
    {
      "id": "A",
      "label": "Repair and re-read the five",
      "meaning": "WALTER repairs its scan to read every batch since its last mark, and triages the five skipped batches (85 items) once through its ordinary workflow, then stops and reports",
      "consequence": "PROME records this choice against the complete proposal and conditions shown on the card. The app executes no action; added changes require your words."
    },
    {
      "id": "B",
      "label": "Repair only",
      "meaning": "WALTER repairs its scan going forward; the five skipped batches are not re-read",
      "consequence": "PROME records this choice against the complete proposal and conditions shown on the card. The app executes no action; added changes require your words."
    },
    {
      "id": "C",
      "label": "Leave it",
      "meaning": "no repair; a batch replaced between WALTER sessions stays unscanned",
      "consequence": "PROME records this choice against the complete proposal and conditions shown on the card. The app executes no action; added changes require your words."
    },
    {
      "id": "D",
      "label": "I'll say",
      "meaning": "you say in chat what you want done",
      "consequence": "PROME records this choice against the complete proposal and conditions shown on the card. The app executes no action; added changes require your words."
    }
  ]
}
```
