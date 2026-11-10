# WQ-668 — explicit app options

PROME's queue options and recommendation. The exact queue row remains authoritative, including all caveats. This card is not an approval or ruling.

```decisions-options
{
  "schema_version": "decisions-options/2",
  "wq_id": "668",
  "queue_row_sha256": "9fc4ef1ab36f33b9220f22b7cac899cedee45533a22b7939ff653410a15734b0",
  "recommended_choice_id": "A",
  "confirmation": {
    "mode": "chat",
    "scope": "other",
    "reason": "The installed fallback requires matching confirmation in PROME’s chat for every answer."
  },
  "choices": [
    {
      "id": "A",
      "label": "Resubmit",
      "meaning": "CORAL drafts a new request with the nine street addresses at its next session; you paste it into the portal; any fee still needs your written approval",
      "consequence": "PROME records this choice against the complete proposal and conditions shown on the card. The app executes no action; added changes require your words."
    },
    {
      "id": "B",
      "label": "Drop it",
      "meaning": "the records request is abandoned; CORAL records that the associations' own filings were not obtained",
      "consequence": "PROME records this choice against the complete proposal and conditions shown on the card. The app executes no action; added changes require your words."
    }
  ]
}
```
