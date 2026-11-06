# WQ-645 — explicit app options

PROME's queue options and recommendation. The exact queue row remains authoritative, including all caveats. This card is not an approval or ruling.

```decisions-options
{
  "schema_version": "decisions-options/2",
  "wq_id": "645",
  "queue_row_sha256": "ad6ea878ca8a6d75a7019baaa53d142320a4fd42d5bf549c619d51cbe6352a0c",
  "recommended_choice_id": "A",
  "confirmation": {
    "mode": "chat",
    "scope": "reversible_internal",
    "reason": "The installed fallback requires matching confirmation in PROME’s chat for every answer."
  },
  "choices": [
    {
      "id": "A",
      "label": "Keep the tool",
      "meaning": "yes, keep it as a DEWEY tool with a README and one selftest, no schedule",
      "consequence": "PROME records this choice against the complete proposal and conditions shown on the card. The app executes no action; added changes require your words."
    },
    {
      "id": "B",
      "label": "Leave it a one-off",
      "meaning": "no, leave it a one-off",
      "consequence": "PROME records this choice against the complete proposal and conditions shown on the card. The app executes no action; added changes require your words."
    }
  ]
}
```
