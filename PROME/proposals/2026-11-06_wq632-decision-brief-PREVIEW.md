# WQ-632 decision brief — PREVIEW, not installed

**Status:** preview under Will's 2026-11-06 11:08 ET instruction. No pointer is in the queue row, so the app does not read this yet. It approves nothing and changes no answer-confirmation rule.

```decisions-brief
{
  "schema_version": "decisions-brief/1",
  "wq_id": 632,
  "queue_row_sha256": "eb73eceb6fa9f5ad565ad3f0fbc79e81d62744f24fdee8c73f58b3fb8f05f031",
  "prepared_at": "2026-11-06 11:10 ET",
  "stale_after": "2026-11-13",
  "question": "A car-loan forecast from CARL, the consumer-credit desk, missed. Should its old instruction to trim your bearish positions by 25% and push their dates out now be acted on?",
  "what_changes": "On 7/24 you held this forecast and said to revisit it once the October data came in. It has, and the forecast missed: Ally's 2025 car loans are running better than the forecast required, not worse. The clause sits with you until you close it. Closing it changes nothing in your book. Acting on it would mean cutting bearish positions, and your rules treat a trim as saying the thesis is broken.",
  "recommendation": {
    "status": "RECOMMENDED",
    "text": "Close it with no action (A). CARL and PROME agree: it was written for a book that has since changed, and no trade card names it."
  },
  "conditions": [
    "The miss is not an all-clear. Ally's 2025 loans are worse than its 2024 loans, 2026 early delinquencies run above 2023, and this is one lender.",
    "The grade can be contested: the measure was chosen after the fact. CARL will reverse it on your word.",
    "The clause's three written versions disagree: two say it was met, and the strictest says not.",
    "New today: LABOR's hiring rule fired, and the bank desk lists that as one reason a bank put could be wrong. TERRY changed no card and gives no hold or sell view; it is a hiring read, not a layoffs read.",
    "The only visible candidate is 14 bank and credit put lines, worth $554 on a $6,644 cost, priced mid-day 11/5 before that afternoon's fall. No desk's card covers them."
  ],
  "supporting": [
    {
      "label": "CARL's report",
      "path": "PROME/inbox/processed/2026-11-06_from-CARL_L843-CRL21-missed-predictions-themes.md"
    },
    {
      "label": "REGINALD's bank-put refuters",
      "path": "AGENTS/REGINALD/TRADE.md"
    },
    {
      "label": "TERRY's re-grade",
      "path": "AGENTS/TERRY/research/2026-11-06_regrade/NOTE.md"
    }
  ]
}
```

```decisions-options
{
  "schema_version": "decisions-options/1",
  "wq_id": 632,
  "queue_row_sha256": "eb73eceb6fa9f5ad565ad3f0fbc79e81d62744f24fdee8c73f58b3fb8f05f031",
  "choices": [
    {
      "id": "A",
      "label": "Close it, no action",
      "meaning": "The old 25% trim instruction ends.",
      "consequence": "No position changes."
    },
    {
      "id": "B",
      "label": "Have TERRY review it first",
      "meaning": "TERRY checks whether the clause fits today's positions and market.",
      "consequence": "TERRY reports back. Any trade would still come to you as its own card."
    },
    {
      "id": "C",
      "label": "Something else",
      "meaning": "You name a different answer.",
      "consequence": "PROME reads it back before recording it."
    }
  ]
}
```
