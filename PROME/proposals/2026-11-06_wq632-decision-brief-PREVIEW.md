# WQ-632 decision brief — PREVIEW, not installed

**Status:** preview under Will's 2026-11-06 11:08 ET instruction. No pointer is in the queue row, so the app does not read this yet. It approves nothing and changes no answer-confirmation rule.

```decisions-brief
{
  "schema_version": "decisions-brief/1",
  "wq_id": 632,
  "queue_row_sha256": "eb73eceb6fa9f5ad565ad3f0fbc79e81d62744f24fdee8c73f58b3fb8f05f031",
  "prepared_at": "2026-11-06 11:10 ET",
  "stale_after": "2026-11-13",
  "question": "CARL's car-loan forecast missed. Should its old instruction to trim your short positions by 25% and push their dates out now be acted on?",
  "what_changes": "When you ruled on 7/24, you held this forecast and said to revisit it once the October data came in. That data is in and the forecast missed: car loans held up better than CARL expected. Nothing happens by itself, so the clause sits with you until you close it. Closing it changes nothing in your book. Acting on it would mean cutting bearish positions, and your rules treat a trim as saying the thesis is broken.",
  "recommendation": {
    "status": "RECOMMENDED",
    "text": "Close the clause and take no action (A). CARL and PROME agree: it was written for a book that has since changed, and no trade card names it."
  },
  "conditions": [
    "A closes an old instruction. It is not a view that your put positions are right.",
    "New today: LABOR's hiring rule fired, and REGINALD lists that as one reason a bank put could be wrong. TERRY changed no card and gives no hold or sell view. It is a hiring read, and REGINALD's case rests on commercial real estate losses.",
    "The only positions it could apply to are 14 bank and credit put lines, marked $554 on $6,644 paid. Those marks are from mid-day 11/5, before that afternoon's fall.",
    "The clause's three written versions disagree. The strictest one was not met, but only because results came in too good for its range, so that is no reason to keep the shorts."
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
      "consequence": "No position changes. TERRY and CARL record it closed."
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
      "consequence": "PROME reads your wording back before anything is recorded."
    }
  ]
}
```
