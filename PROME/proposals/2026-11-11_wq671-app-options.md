# WQ-671 — explicit app options

PROME's queue options and recommendation. The exact queue row remains authoritative, including all caveats. This card is not an approval or ruling.

```decisions-options
{
  "schema_version": "decisions-options/2",
  "wq_id": "671",
  "queue_row_sha256": "6610d83ddf418a0fe420f3cf94e37c5f8d54a1dae975812305ba11aeb8c96fb4",
  "recommended_choice_id": "A",
  "confirmation": {
    "mode": "chat",
    "scope": "other",
    "reason": "The installed fallback requires matching confirmation in PROME’s chat for every answer."
  },
  "choices": [
    {
      "id": "A",
      "label": "ORACLE owns both",
      "meaning": "ORACLE owns the December Fed meeting's market price: one dated read with the betting-market odds and the futures-implied move beside them; every other desk cites ORACLE's read",
      "consequence": "PROME records this choice against the complete proposal and conditions shown on the card. The app executes no action; added changes require your words."
    },
    {
      "id": "B",
      "label": "Split it: ORACLE and BOND",
      "meaning": "ORACLE keeps the betting-market odds; BOND owns the figure implied by fed funds futures; desks cite each for its own number and PROME reconciles the two when they differ",
      "consequence": "PROME records this choice against the complete proposal and conditions shown on the card. The app executes no action; added changes require your words."
    },
    {
      "id": "C",
      "label": "Leave it as it is",
      "meaning": "no owner is named; PROME asks ORACLE for a read when one is needed, as it did today",
      "consequence": "PROME records this choice against the complete proposal and conditions shown on the card. The app executes no action; added changes require your words."
    }
  ]
}
```
