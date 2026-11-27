# WQ-757 — explicit decision card

Question, options, context and conditions are decision terms. Queue Notes are operational; put changed conditions here or in the question, not only in Notes.

```decisions-options
{
  "schema_version": "decisions-options/3",
  "wq_id": "757",
  "queue_terms_sha256": "b122b04187fa94f6c6bfa736621645c349c08042d81cf5cc391ec5e89226e49f",
  "choices": [
    {
      "id": "A",
      "label": "Four small changes and one prompt",
      "meaning": "The collector flags articles more than 7 days old. The confidence field becomes one keyword then free text. No new rule on corrections. PROME asks SAM, SHADE and BRENT whether their action cards are useful. WALTER's card tool prompts for the alert-log row.",
      "consequence": "PROME changes one script in the collection repository; WALTER edits its format spec and card tool. One added check, the prompt. No kill rule changes and WALTER still reads every title."
    },
    {
      "id": "B",
      "label": "The same, without the prompt",
      "meaning": "Everything in A except the alert-log prompt in WALTER's card tool. WALTER keeps writing those rows by hand.",
      "consequence": "No added check at all. The alert log depends on WALTER remembering, which failed on 11/24 and again on 11/26."
    },
    {
      "id": "C",
      "label": "Change nothing",
      "meaning": "The review is filed as a report. No collector flag, no field change, no desk questions, no prompt.",
      "consequence": "The filter runs as it does today. Old articles keep arriving unflagged and WALTER keeps discarding them by hand. The next review comes after about 200 more cards or 30 days."
    }
  ],
  "recommended_choice_id": "A",
  "context": "WALTER sampled 228 news cards from 11/12 to 11/26 and the 37 items its filter discarded. No discard was a miss and cards reach the right desks. The problems are around the filter: 31 of 37 discards were old articles the collector re-served as new; one card in seven is a correction; a third of the cards asking a desk to act show no trace in that desk's work beyond being filed; the confidence field is free text on 74% of cards; the alert log had gaps on two days.",
  "conditions": [
    "$0. No trade, gate, threshold or score changes under any choice.",
    "The figures are WALTER's; PROME did not recompute them.",
    "'Filed with no trace' is an upper bound: a desk can use a card without citing its number.",
    "The collector flag is a label only. It discards nothing.",
    "Not urgent."
  ],
  "confirmation": {
    "mode": "chat",
    "scope": "other",
    "reason": "Matching PROME-chat confirmation remains required under the installed fallback."
  }
}
```
