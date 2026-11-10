# WQ-662 — explicit app options

PROME's queue options and recommendation. The exact queue row remains authoritative, including all caveats. This card is not an approval or ruling.

```decisions-options
{
  "schema_version": "decisions-options/2",
  "wq_id": "662",
  "queue_row_sha256": "5847142c52d323e8f0222fc8e6c4a82672d91f51d828eeea30eb7073bcb9f31d",
  "recommended_choice_id": "A",
  "confirmation": {
    "mode": "chat",
    "scope": "other",
    "reason": "The installed fallback requires matching confirmation in PROME’s chat for every answer."
  },
  "choices": [
    {
      "id": "A",
      "label": "WALTER's dated line counts",
      "meaning": "a line in WALTER's completion file saying the brief was shown to you in its chat, with the time, counts as delivery; PROME then gives the changes only, with every material caveat kept",
      "consequence": "PROME records this choice against the complete proposal and conditions shown on the card. The app executes no action; added changes require your words."
    },
    {
      "id": "B",
      "label": "Only your word counts",
      "meaning": "PROME gives a full brief unless you say you already have WALTER's; no file line counts as delivery",
      "consequence": "PROME records this choice against the complete proposal and conditions shown on the card. The app executes no action; added changes require your words."
    }
  ]
}
```
