# WQ-730 — explicit decision card

Question, options, context and conditions are decision terms. Queue Notes are operational; put changed conditions here or in the question, not only in Notes.

```decisions-options
{
  "schema_version": "decisions-options/3",
  "wq_id": "730",
  "queue_terms_sha256": "f791c0ce7901d8144bb480a0e4c5316eebf995c42a10ca6cfcf54b23fdae6598",
  "choices": [
    {
      "id": "A",
      "label": "Retire stage two",
      "meaning": "The paper book's second stage (a pretend 1,500 dollar monthly budget that forces TERRY to choose which cards get paper money) is retired. TERRY removes the gate line from its marking script and marks stage two RETIRED in its design file. Stage one keeps paper-filling every would-fire card.",
      "consequence": "One counter stops printing TRIPPED. Nothing real changes. Every row keeps its date and dollars, so a month can be re-tested later; you can bring stage two back by word."
    },
    {
      "id": "B",
      "label": "Not now: keep the gate, fix the count",
      "meaning": "Stage two stays deferred behind its gate. TERRY fixes the counter so one trade split into two rows counts once.",
      "consequence": "The counter drops to about 5 of 6 and may trip later."
    },
    {
      "id": "C",
      "label": "Switch stage two on",
      "meaning": "TERRY adds a funding column, a 1,500 dollar monthly paper tranche, ranks each fire by edge, logs unfunded cards and keeps a paper equity curve.",
      "consequence": "More bookkeeping per card. On the corrected figures no month has reached the budget, so it would not yet test prioritising."
    }
  ],
  "recommended_choice_id": "A",
  "context": "Restated on 11/23 with the corrected figures you asked for. Stage two has three separate conditions. Six paper trades in 90 days: the counter reads 7, the honest peak is 5. Four cards in a month: peak 3. Spending over 1,500 dollars in a month: July 1,204.70, November to date 845.",
  "conditions": [
    "Your 2,128.76 dollars for July adds the rows PB-0002a to d. Those rows are your real fill of the same TLT card PB-0001 already paper-filled; they are one fill of 346.90 dollars, and the same 25-contract lot appears in three row cells, so adding rows counts it three times.",
    "If the TLT card is charged for both its paper fill and its real fill, July is 1,551.60 dollars, over the budget, with 841.90 dollars on one card against the 500 dollar cap. The design charges a card once.",
    "TERRY's 11/22 note left PB-0002 out without saying why; that defect is corrected.",
    "PROME checked the row cells at the file; the monthly table and the honest count are TERRY's.",
    "All of it is paper. No money, real position or card moves on any answer.",
    "Every app answer needs Will's confirming word in chat."
  ],
  "confirmation": {
    "mode": "chat",
    "scope": "other",
    "reason": "Matching PROME-chat confirmation remains required under the installed fallback."
  }
}
```
