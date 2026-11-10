# WQ-665 — explicit app options

PROME's queue options and recommendation. The exact queue row remains authoritative, including all caveats. This card is not an approval or ruling.

```decisions-options
{
  "schema_version": "decisions-options/2",
  "wq_id": "665",
  "queue_row_sha256": "726de99641a276c5470ed3b92a9d9da8ffe8ed3f59faef3da286b0098be34e6a",
  "recommended_choice_id": "B",
  "confirmation": {
    "mode": "chat",
    "scope": "other",
    "reason": "The installed fallback requires matching confirmation in PROME’s chat for every answer."
  },
  "choices": [
    {
      "id": "A",
      "label": "Two-month reading",
      "meaning": "the question closes if November food at home prints under +0.4%, because the alarm test always needed two months in a row; this is FERT's recommendation",
      "consequence": "PROME records this choice against the complete proposal and conditions shown on the card. The app executes no action; added changes require your words."
    },
    {
      "id": "B",
      "label": "Per-month reading",
      "meaning": "October's +0.4% already blocks a close at the November print; the question stays open and FERT proposes a new end window for your ruling",
      "consequence": "PROME records this choice against the complete proposal and conditions shown on the card. The app executes no action; added changes require your words."
    }
  ]
}
```
