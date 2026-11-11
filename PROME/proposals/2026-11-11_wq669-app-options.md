# WQ-669 — explicit app options

PROME's queue options and recommendation. The exact queue row remains authoritative, including all caveats. This card is not an approval or ruling.

```decisions-options
{
  "schema_version": "decisions-options/2",
  "wq_id": "669",
  "queue_row_sha256": "7db3e8b519c29cc4ec75f6368a14578c8f9089dcff1f2ce68dc81dbfcc7a9eb8",
  "recommended_choice_id": "A",
  "confirmation": {
    "mode": "chat",
    "scope": "other",
    "reason": "The installed fallback requires matching confirmation in PROME’s chat for every answer."
  },
  "choices": [
    {
      "id": "A",
      "label": "Count it",
      "meaning": "the 11/11 Ust-Luga strike counts as an export-terminal row; the stand-down clock restarts and the earliest stand-down is 12/11; OSPREY's forecast OSP-08 grades FAILED on 11/20",
      "consequence": "PROME records this choice against the complete proposal and conditions shown on the card. The app executes no action; added changes require your words."
    },
    {
      "id": "B",
      "label": "Do not count it",
      "meaning": "the strike is logged but does not count; the earliest stand-down stays 11/17 and OSP-08 stays live",
      "consequence": "PROME records this choice against the complete proposal and conditions shown on the card. The app executes no action; added changes require your words."
    },
    {
      "id": "C",
      "label": "Decide on the 11/16 re-read",
      "meaning": "count it only if OSPREY's re-read about 11/16 finds a second source placing the damage in the liquids terminal or shows loadings disrupted; otherwise do not count it; OSPREY applies whichever the re-read shows without coming back",
      "consequence": "PROME records this choice against the complete proposal and conditions shown on the card. The app executes no action; added changes require your words."
    }
  ]
}
```
