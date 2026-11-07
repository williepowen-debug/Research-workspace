# WQ-652 — explicit app options

PROME's queue options and recommendation. The exact queue row remains authoritative, including all caveats. This card is not an approval or ruling.

```decisions-options
{
  "schema_version": "decisions-options/2",
  "wq_id": "652",
  "queue_row_sha256": "560cd3e32a5f96cb4f13309264b7a4e8c15d174563508d08520334c0112662e4",
  "recommended_choice_id": "A",
  "confirmation": {
    "mode": "chat",
    "scope": "other",
    "reason": "The installed fallback requires matching confirmation in PROME’s chat for every answer."
  },
  "choices": [
    {
      "id": "A",
      "label": "All four",
      "meaning": "apply all four wording fixes",
      "consequence": "PROME records this choice against the complete proposal and conditions shown on the card. The app executes no action; added changes require your words."
    },
    {
      "id": "B",
      "label": "Only (3) and (4)",
      "meaning": "apply the two charter fixes only",
      "consequence": "PROME records this choice against the complete proposal and conditions shown on the card. The app executes no action; added changes require your words."
    },
    {
      "id": "C",
      "label": "Not now",
      "meaning": "make none of these changes now",
      "consequence": "PROME records this choice against the complete proposal and conditions shown on the card. The app executes no action; added changes require your words."
    }
  ]
}
```
