# WQ-664 — explicit app options

PROME's queue options and recommendation. The exact queue row remains authoritative, including all caveats. This card is not an approval or ruling.

```decisions-options
{
  "schema_version": "decisions-options/2",
  "wq_id": "664",
  "queue_row_sha256": "fc84bc0e96c88c897fccbac802bf41226dbc05fae9f09b05f4c408c345dd775e",
  "recommended_choice_id": "B",
  "confirmation": {
    "mode": "chat",
    "scope": "other",
    "reason": "The installed fallback requires matching confirmation in PROME’s chat for every answer."
  },
  "choices": [
    {
      "id": "A",
      "label": "Draft a successor test",
      "meaning": "you authorize NEXUS to draft a new falsifier letter for the 26/41/33 split; its thresholds come back to you for a ruling before anything is registered",
      "consequence": "PROME records this choice against the complete proposal and conditions shown on the card. The app executes no action; added changes require your words."
    },
    {
      "id": "B",
      "label": "Retire the numbers",
      "meaning": "the split becomes judgment with no number, as NEXUS did on 11/10 for M-01, M-05 and M-04; 26/41/33 is no longer quoted as current on any surface",
      "consequence": "PROME records this choice against the complete proposal and conditions shown on the card. The app executes no action; added changes require your words."
    },
    {
      "id": "C",
      "label": "Leave as is, labelled",
      "meaning": "26/41/33 stays and every use carries the label that no registered test can currently prove it wrong",
      "consequence": "PROME records this choice against the complete proposal and conditions shown on the card. The app executes no action; added changes require your words."
    }
  ]
}
```
