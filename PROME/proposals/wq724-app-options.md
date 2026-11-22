# WQ-724 — explicit decision card

Question, options, context and conditions are decision terms. Queue Notes are operational; put changed conditions here or in the question, not only in Notes.

```decisions-options
{
  "schema_version": "decisions-options/3",
  "wq_id": "724",
  "queue_terms_sha256": "e2a427443de6798da1fc6d695cc7c8d5e43b587472539101abc7acee3247befe",
  "choices": [
    {
      "id": "A",
      "label": "Decline now",
      "meaning": "The idea is dropped today. TERRY records it as declined on its card and nothing is ordered.",
      "consequence": "No money moves. If tech bounces from here, this trade is not on."
    },
    {
      "id": "B",
      "label": "Conditional yes: take it if both conditions are met",
      "meaning": "If the high-yield spread prints at 350 or under on the 11/20 or 11/23 figure, and QQQ then has a down day by Wed 11/25 at or under 635 dollars, you place one QQQ 640/650 call spread expiring 12/18 for at most 4.50 dollars. PROME brings you TERRY's grade of each condition as it prints.",
      "consequence": "Risk 451.30 dollars to make 548.70 dollars; it needs QQQ above 644.50 dollars by 12/18. The order is yours, at the broker's price. A fill goes past the closed sizing gate (X1) by your choice."
    },
    {
      "id": "C",
      "label": "Let it lapse",
      "meaning": "No answer. The idea expires by itself on Wed 11/25.",
      "consequence": "Same result as declining, three days later."
    }
  ],
  "recommended_choice_id": "A",
  "context": "TERRY, the trade-construction desk, offered a small contrarian bet on a tech bounce on 11/20 (IDEA-QQQ-CAPIT-NOV20) and leans against its own idea. It has not triggered and is not approved. The history behind it: 17 panic closes since 2007; QQQ was higher 20 sessions later in 76 percent of them and this spread would have paid in full in 11 of 17.",
  "conditions": [
    "The first condition (panic closes) was met on the Friday 11/20 closes by TERRY's grade. The second waits on the high-yield figure for 11/20, which FRED publishes Monday 11/23; the last published figure is 352 [11/19], above the 350 bar.",
    "The six losers in the sample were the credit-led crashes (2008, 2020), and credit is widening now.",
    "The sample starts in 2006, so the 2000 to 2002 tech unwind, the closest analog to an AI unwind, is not in it.",
    "No desk holds a bullish view. The trade bets against the approved HYG put card and against your own QQQ puts.",
    "Option prices are vendor screens of 11:24 ET on 11/20, not broker quotes.",
    "A trigger firing is not an approval.",
    "Every app answer needs Will's confirming word in chat."
  ],
  "confirmation": {
    "mode": "chat",
    "scope": "other",
    "reason": "Matching PROME-chat confirmation remains required under the installed fallback."
  }
}
```
