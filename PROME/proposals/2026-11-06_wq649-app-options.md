# WQ-649 — explicit app options

PROME's queue options and recommendation. The exact queue row remains authoritative, including all caveats. This card is not an approval or ruling.

```decisions-options
{
  "schema_version": "decisions-options/2",
  "wq_id": "649",
  "queue_row_sha256": "3507534b78ca71044b25914a28214afa3838cf798f22cd89e42b7821e2415bdc",
  "recommended_choice_id": "A",
  "confirmation": {
    "mode": "chat",
    "scope": "trade",
    "reason": "The installed fallback requires matching confirmation in PROME’s chat for every answer."
  },
  "choices": [
    {
      "id": "A",
      "label": "Keep the clause",
      "meaning": "keep the missing-file clause",
      "consequence": "PROME records this choice against the complete proposal and conditions shown on the card. The app executes no action; added changes require your words."
    },
    {
      "id": "B",
      "label": "Strike the clause",
      "meaning": "strike the missing-file clause",
      "consequence": "PROME records this choice against the complete proposal and conditions shown on the card. The app executes no action; added changes require your words."
    }
  ]
}
```
