# WQ-647 — explicit app options

PROME's queue options and recommendation. The exact queue row remains authoritative, including all caveats. This card is not an approval or ruling.

```decisions-options
{
  "schema_version": "decisions-options/2",
  "wq_id": "647",
  "queue_row_sha256": "44d174ea20743c33afbdd35914f8d995cd51ca78850e22e718c306941701b0a6",
  "recommended_choice_id": "A",
  "confirmation": {
    "mode": "chat",
    "scope": "reversible_internal",
    "reason": "The installed fallback requires matching confirmation in PROME’s chat for every answer."
  },
  "choices": [
    {
      "id": "A",
      "label": "Withdraw and re-register",
      "meaning": "withdraw ZHA-24 and re-register on the overnight rate from 1.25%",
      "consequence": "PROME records this choice against the complete proposal and conditions shown on the card. The app executes no action; added changes require your words."
    },
    {
      "id": "B",
      "label": "Leave as registered",
      "meaning": "leave it as registered and let it grade on the old rate",
      "consequence": "PROME records this choice against the complete proposal and conditions shown on the card. The app executes no action; added changes require your words."
    },
    {
      "id": "C",
      "label": "Something else",
      "meaning": "something else",
      "consequence": "PROME records this choice against the complete proposal and conditions shown on the card. The app executes no action; added changes require your words."
    }
  ]
}
```
