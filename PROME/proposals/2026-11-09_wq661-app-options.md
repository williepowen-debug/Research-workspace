# WQ-661 — explicit app options

PROME's queue options and recommendation. The exact queue row remains authoritative, including all caveats. This card is not an approval or ruling.

```decisions-options
{
  "schema_version": "decisions-options/2",
  "wq_id": "661",
  "queue_row_sha256": "1a395b6d5fa6271391354fb76bb8894a93ce89718a9efae98ec7666290394228",
  "recommended_choice_id": "A",
  "confirmation": {
    "mode": "chat",
    "scope": "other",
    "reason": "The installed fallback requires matching confirmation in PROME’s chat for every answer."
  },
  "choices": [
    {
      "id": "A",
      "label": "Blanket word does not spend the cap",
      "meaning": "launches under your blanket word are yours, not PROME's allowance; before launching PROME lists the desks and the due row for each in chat, limits them to rows already due at that moment, and the word lasts for that boot only",
      "consequence": "PROME records this choice against the complete proposal and conditions shown on the card. The app executes no action; added changes require your words."
    },
    {
      "id": "B",
      "label": "Blanket word spends the cap",
      "meaning": "a blanket word still counts against four per boot (eight under C6); past the cap PROME brings you a slate and you name the desks",
      "consequence": "PROME records this choice against the complete proposal and conditions shown on the card. The app executes no action; added changes require your words."
    }
  ]
}
```
