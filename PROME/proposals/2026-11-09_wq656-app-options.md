# WQ-656 — explicit app options

PROME's queue options and recommendation. The exact queue row remains authoritative, including all caveats. This card is not an approval or ruling.

```decisions-options
{
  "schema_version": "decisions-options/2",
  "wq_id": "656",
  "queue_row_sha256": "e38aaa9370c308376a2abd6bc5f78cbe26e391b4b2494401773ee64576b381bd",
  "recommended_choice_id": "A",
  "confirmation": {
    "mode": "chat",
    "scope": "other",
    "reason": "The installed fallback requires matching confirmation in PROME’s chat for every answer."
  },
  "choices": [
    {
      "id": "A",
      "label": "Approve CARL's grading rule",
      "meaning": "CRL-15 grades only on a published figure labelled an SBA 7(a) default rate for a period ending 2026-12-31; disagreeing versions across 6.5%, or none by the FY2026 annual-report season, close it with no verdict",
      "consequence": "PROME records this choice against the complete proposal and conditions shown on the card. The app executes no action; added changes require your words."
    },
    {
      "id": "B",
      "label": "Close it now, no verdict",
      "meaning": "close CRL-15 today as ungradeable as written",
      "consequence": "PROME records this choice against the complete proposal and conditions shown on the card. The app executes no action; added changes require your words."
    },
    {
      "id": "C",
      "label": "Leave as is",
      "meaning": "no rule now; CARL picks a calculation at year-end",
      "consequence": "PROME records this choice against the complete proposal and conditions shown on the card. The app executes no action; added changes require your words."
    }
  ]
}
```
