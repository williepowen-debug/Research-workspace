# WQ-657 — explicit app options

PROME's queue options and recommendation. The exact queue row remains authoritative, including all caveats. This card is not an approval or ruling.

```decisions-options
{
  "schema_version": "decisions-options/2",
  "wq_id": "657",
  "queue_row_sha256": "bde4167ab4593ecf9ea1c46811ea79f8efb3882413e15e4c2f5174a07d8aaf9a",
  "recommended_choice_id": "B",
  "confirmation": {
    "mode": "chat",
    "scope": "other",
    "reason": "The installed fallback requires matching confirmation in PROME’s chat for every answer."
  },
  "choices": [
    {
      "id": "A",
      "label": "Keep as built",
      "meaning": "keep the fleet view as delivered; PROME uses it in ordinary work; no further build",
      "consequence": "PROME records this choice against the complete proposal and conditions shown on the card. The app executes no action; added changes require your words."
    },
    {
      "id": "B",
      "label": "Keep, one bounded trim",
      "meaning": "keep it; DAEDALUS collapses routine signal cards, protocol files, undated rows and today's launch records to counts so exceptions open the page; full lists stay on demand",
      "consequence": "PROME records this choice against the complete proposal and conditions shown on the card. The app executes no action; added changes require your words."
    },
    {
      "id": "C",
      "label": "Set it aside",
      "meaning": "do not use the fleet view; nothing further is built",
      "consequence": "PROME records this choice against the complete proposal and conditions shown on the card. The app executes no action; added changes require your words."
    }
  ]
}
```
