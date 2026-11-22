# WQ-730 — explicit decision card

Question, options, context and conditions are decision terms. Queue Notes are operational; put changed conditions here or in the question, not only in Notes.

```decisions-options
{
  "schema_version": "decisions-options/3",
  "wq_id": "730",
  "queue_terms_sha256": "0d94fb290c58398883f4bf5227ff716583eb636e9fd16d4fd338f07e1b86b323",
  "choices": [
    {
      "id": "A",
      "label": "Retire stage two",
      "meaning": "The paper book's second stage (a pretend 1,500 dollar monthly budget that forces TERRY to choose which cards get paper money) is retired. TERRY removes the gate line from its marking script and marks stage two RETIRED in its design file. Stage one keeps paper-filling every would-fire card.",
      "consequence": "One counter stops printing TRIPPED. Nothing real changes. You can bring stage two back by word."
    },
    {
      "id": "B",
      "label": "Not now: keep the gate, fix the count",
      "meaning": "Stage two stays deferred behind its six-in-90-days gate. TERRY fixes the counter so one trade split into two rows counts once.",
      "consequence": "The counter drops to about 4 to 5 of 6 and may trip again later."
    },
    {
      "id": "C",
      "label": "Switch stage two on",
      "meaning": "TERRY adds a funding column, a 1,500 dollar monthly paper tranche, ranks each fire by edge, logs unfunded cards and keeps a paper equity curve.",
      "consequence": "More bookkeeping per card. At current card flow the budget would not bind, so it would not test prioritising."
    }
  ],
  "recommended_choice_id": "A",
  "context": "On 7/24 you set a gate: the paper book's second stage opens when six paper trades land in 90 days. The counter reads 7 of 6. TERRY's read on 11/22 is that the 7 is mostly a counting artifact and that card flow never approached the paper budget.",
  "conditions": [
    "The honest count of 4 to 5 and the dollar figures (845 dollars in the busiest week; 1,204.70 dollars across 7/17 to 7/30) are TERRY's; PROME did not re-count them.",
    "All of it is paper. No money, real position or card moves on any answer.",
    "The gate and its budget are your own ruling of 2026-07-24.",
    "Every app answer needs Will's confirming word in chat."
  ],
  "confirmation": {
    "mode": "chat",
    "scope": "other",
    "reason": "Matching PROME-chat confirmation remains required under the installed fallback."
  }
}
```
