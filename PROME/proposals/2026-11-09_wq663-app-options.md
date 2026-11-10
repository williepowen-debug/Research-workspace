# WQ-663 — explicit app options

PROME's queue options and recommendation. The exact queue row remains authoritative, including all caveats. This card is not an approval or ruling.

```decisions-options
{
  "schema_version": "decisions-options/2",
  "wq_id": "663",
  "queue_row_sha256": "be026a60708958061c5c1699b465fa85b94926be32120e973efd0f022fdfe75b",
  "recommended_choice_id": "B",
  "confirmation": {
    "mode": "chat",
    "scope": "other",
    "reason": "The installed fallback requires matching confirmation in PROME’s chat for every answer."
  },
  "choices": [
    {
      "id": "A",
      "label": "Keep the up-day rule",
      "meaning": "the card stays exactly as approved: buy only on a day HYG is up, at $0.60 or less on your broker screen",
      "consequence": "PROME records this choice against the complete proposal and conditions shown on the card. The app executes no action; added changes require your words."
    },
    {
      "id": "B",
      "label": "Waive it for this card",
      "meaning": "for this one card only, you may buy on any day the broker shows $0.60 or less; TERRY records the break on the card with its figures; no other term changes",
      "consequence": "PROME records this choice against the complete proposal and conditions shown on the card. The app executes no action; added changes require your words."
    }
  ]
}
```
