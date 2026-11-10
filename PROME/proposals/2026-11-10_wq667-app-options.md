# WQ-667 — explicit app options

PROME's queue options and recommendation. The exact queue row remains authoritative, including all caveats. This card is not an approval or ruling.

```decisions-options
{
  "schema_version": "decisions-options/2",
  "wq_id": "667",
  "queue_row_sha256": "dfc93a0b5a04408969a8ebf014d45d0e0855bc6e9e647b6239fd7956b24fb688",
  "recommended_choice_id": "A",
  "confirmation": {
    "mode": "chat",
    "scope": "other",
    "reason": "The installed fallback requires matching confirmation in PROME’s chat for every answer."
  },
  "choices": [
    {
      "id": "A",
      "label": "One number: eight",
      "meaning": "PROME may wake up to eight desks per boot on any due row, aged action or aged wait, reported the same day; past eight needs your word",
      "consequence": "PROME records this choice against the complete proposal and conditions shown on the card. The app executes no action; added changes require your words."
    },
    {
      "id": "B",
      "label": "No number",
      "meaning": "PROME wakes every desk whose row is due, limited only by memory measured at launch, and lists them the same day; no count limit",
      "consequence": "PROME records this choice against the complete proposal and conditions shown on the card. The app executes no action; added changes require your words."
    },
    {
      "id": "C",
      "label": "Keep four and eight",
      "meaning": "nothing changes: four per boot, eight when every wake is a due catalyst or review date; your blanket word stays outside it",
      "consequence": "PROME records this choice against the complete proposal and conditions shown on the card. The app executes no action; added changes require your words."
    }
  ]
}
```
