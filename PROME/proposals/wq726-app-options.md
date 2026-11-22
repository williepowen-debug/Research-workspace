# WQ-726 — explicit decision card

Question, options, context and conditions are decision terms. Queue Notes are operational; put changed conditions here or in the question, not only in Notes.

```decisions-options
{
  "schema_version": "decisions-options/3",
  "wq_id": "726",
  "queue_terms_sha256": "3385bdf372af2e0e9fc951ed7605e93981a55f71064320690806bf99f08c9dc1",
  "choices": [
    {
      "id": "A",
      "label": "Not now: keep the score a judgment call",
      "meaning": "CARL's upper-income wealth-stress score (V14, now 3 of 5) keeps no written rule for going up. CARL says so on its score sheet and may bring the rule back once the 4 percent cut has been tested against history.",
      "consequence": "Nothing changes today. A move from 3 to 4 stays CARL's judgment, stated with its reasons."
    },
    {
      "id": "B",
      "label": "Adopt CARL's draft rule",
      "meaning": "The score goes 3 to 4 only when BOTH hold: the S&P 500's average close over a calendar month is at or below 7,037.04 (10 percent under the 7,818.93 peak), first testable on December's average; AND within the following quarter American Express billed-business growth is at or below 4 percent year on year (the third quarter was 8 percent).",
      "consequence": "A new written threshold on a desk score. The 4 percent cut is half of the third-quarter figure, not taken from history, and American Express is one issuer."
    }
  ],
  "recommended_choice_id": "A",
  "context": "CARL, the consumer desk, has a written rule for lowering this score and none for raising it. After the S&P closed under 7,037.04 on 11/20 it drafted one. Both CARL's own alternative and PROME's recommendation are to wait until the cut is tested.",
  "conditions": [
    "7,037.04 is the level 10 percent under the cycle peak of 7,818.93; it is not the peak. The queue row's wording has this backwards.",
    "The 4 percent threshold is CARL's guess by its own word.",
    "CARL's first-logged probabilities run about 45 points too confident on its own count.",
    "No money is involved and no trade follows from either answer.",
    "The 12/01 date exists only so that a rule, if adopted, is written before December's closes accumulate. Unanswered, nothing changes.",
    "Every app answer needs Will's confirming word in chat."
  ],
  "confirmation": {
    "mode": "chat",
    "scope": "other",
    "reason": "Matching PROME-chat confirmation remains required under the installed fallback."
  }
}
```
