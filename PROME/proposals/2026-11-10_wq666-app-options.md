# WQ-666 — explicit app options

PROME's queue options and recommendation. The exact queue row remains authoritative, including all caveats. This card is not an approval or ruling.

```decisions-options
{
  "schema_version": "decisions-options/2",
  "wq_id": "666",
  "queue_row_sha256": "d9ce70115dd430afd9ee96481896bd74d3938548b181daf6e997debd7b94d5ee",
  "recommended_choice_id": "A",
  "confirmation": {
    "mode": "chat",
    "scope": "other",
    "reason": "The installed fallback requires matching confirmation in PROME’s chat for every answer."
  },
  "choices": [
    {
      "id": "A",
      "label": "Three clean months",
      "meaning": "the question closes if food at home prints under +0.4% in each of November, December and January, the last release being 2/11/27, with no USDA outlook revised up citing input costs",
      "consequence": "PROME records this choice against the complete proposal and conditions shown on the card. The app executes no action; added changes require your words."
    },
    {
      "id": "B",
      "label": "Two clean months",
      "meaning": "November and December only, ending with the 1/13/27 release; faster, but one clean month after October is weaker evidence",
      "consequence": "PROME records this choice against the complete proposal and conditions shown on the card. The app executes no action; added changes require your words."
    }
  ]
}
```
