# WQ-702 — explicit decision card

Question, options, context and conditions are decision terms. Queue Notes are operational; put changed conditions here or in the question, not only in Notes.

```decisions-options
{
  "schema_version": "decisions-options/3",
  "wq_id": "702",
  "queue_terms_sha256": "fd51c01638ae1c97b66c898f33a4c5e9fbe29a8d91a74d93a751e1ba8b81782b",
  "choices": [
    {
      "id": "A",
      "label": "Label them as my own trades",
      "meaning": "Each line is recorded as Will's own trade with no desk card, and the desk whose thesis it belongs to is named beside it for information only (the WAL lines to WAL, ZION and VLY and KRE to REGINALD, FLG to FLG). No card, no management plan, no reminders. The reconcile clerk writes the labels at the next broker capture.",
      "consequence": "The UNKNOWN flags close and stop recurring. A named desk means a later postmortem can say whether the idea was right. Nothing about any position changes."
    },
    {
      "id": "B",
      "label": "TERRY writes a short card for each",
      "meaning": "For each line still open at the next broker capture, TERRY writes a one-paragraph record of the thesis and what would prove it wrong. No sell-or-roll plan, per your standing rule.",
      "consequence": "More complete records and a firmer basis for grading, at the cost of a TERRY session and cards written after the trade."
    },
    {
      "id": "C",
      "label": "Leave them flagged",
      "meaning": "No change. The mirror keeps marking them UNKNOWN.",
      "consequence": "Each reconcile re-raises the same flags and nothing grades these trades."
    }
  ],
  "recommended_choice_id": "A",
  "context": "The position mirror is a record built from your broker screenshots. On the 11/10 captures, seven bank put lines carry no owner, card or approval on file: two WAL 70 put lines, ZION 62.5 puts, a VLY 12 put, an FLG 10 put, and KRE 71.5 and KRE 25 puts. They appear to be trades you placed yourself outside the card process. An outside audit on 11/16 asked that each be given an owner or flagged. This decision is only about how the record labels them.",
  "conditions": [
    "The audit counts 14 bank and credit lines; PROME finds 7 on the mirror and has not reconciled the two counts.",
    "The mirror is your 11/10 captures; PROME infers nothing about whether any line is still open.",
    "No reminders, sell-or-roll prompts or management plans follow from any choice.",
    "The desk named under A is PROME's proposal from the ticker; you can change any of them.",
    "Every app answer needs Will's confirming word in chat."
  ],
  "confirmation": {
    "mode": "chat",
    "scope": "other",
    "reason": "Matching PROME-chat confirmation remains required under the installed fallback."
  }
}
```
