# WQ-674 — explicit app options

PROME's queue options and recommendation. The exact queue row remains authoritative, including all caveats. This card is not an approval or ruling.

```decisions-options
{
  "schema_version": "decisions-options/2",
  "wq_id": "674",
  "queue_row_sha256": "76094fc2f5963492380c9542d1ce05a674ca42a70bf0f84ccf24f80da0ace3f0",
  "recommended_choice_id": "A",
  "confirmation": {
    "mode": "chat",
    "scope": "other",
    "reason": "The installed fallback requires matching confirmation in PROME’s chat for every answer."
  },
  "choices": [
    {
      "id": "A",
      "label": "Retire all four",
      "meaning": "freeze the mapping table, drop the ledger column, leave the closeout gap documented and unfixed, and let the spine audit serve as the independent read",
      "consequence": "PROME records this choice against the complete proposal and conditions shown on the card. The app executes no action; added changes require your words."
    },
    {
      "id": "B",
      "label": "Keep all four",
      "meaning": "PROME keeps maintaining the table, builds the column and the fix, and spends the separate reader rounds",
      "consequence": "PROME records this choice against the complete proposal and conditions shown on the card. The app executes no action; added changes require your words."
    },
    {
      "id": "C",
      "label": "I'll name which",
      "meaning": "you say in chat which of the four to retire",
      "consequence": "PROME records this choice against the complete proposal and conditions shown on the card. The app executes no action; added changes require your words."
    }
  ]
}
```
