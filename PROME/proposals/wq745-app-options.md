# WQ-745 — explicit decision card

Question, options, context and conditions are decision terms. Queue Notes are operational; put changed conditions here or in the question, not only in Notes.

```decisions-options
{
  "schema_version": "decisions-options/3",
  "wq_id": "745",
  "queue_terms_sha256": "4e6fef2c395f24a1c45c6ac78a7dcef240cf3a6db7d9e3be040d4b0d6a1cb842",
  "choices": [
    {
      "id": "A",
      "label": "Approve as a standing idea",
      "meaning": "TERRY's CoreWeave February 2027 $40/$30 put spread, 1 contract, at most $3.25 ($326.30 at risk), is approved as a not-yet-triggered idea, including your choice to pass the closed sizing gate (X1) on this one card. It may be entered only on a green day with CoreWeave closing at $48 or higher and its debt-insurance cost at 12% a year or more, through 12/11.",
      "consequence": "TERRY re-prices on the live chain if it triggers and brings it to you; you place any order. Nothing is executed by an agent."
    },
    {
      "id": "B",
      "label": "Decline",
      "meaning": "No card. TERRY records the idea as declined.",
      "consequence": "No new AI exposure; your approved HYG card is unchanged."
    },
    {
      "id": "C",
      "label": "Approve the idea, not the X1 pass",
      "meaning": "The idea is recorded and tracked, but the closed sizing gate stays in force on it.",
      "consequence": "It stays on paper unless X1 opens or you say otherwise."
    }
  ],
  "recommended_choice_id": "A",
  "context": "REGINALD's high-yield line fired on 11/23. LIQUID finds new borrowing still open for ordinary companies and refused mainly in AI data-centre lending; HENRY finds the average stock flat since September while chips fell about a third. TERRY built one idea on that channel. Tonight it cannot be entered: the spread screens at about $4.03 against the $3.25 cap.",
  "conditions": [
    "CoreWeave's next earnings date is not verified; TERRY reads it from the company before any entry.",
    "Every price is an after-hours screen of 11/24, not a fill price; re-priced on the live chain before any order.",
    "With the approved HYG card this puts up to $632.80 on related ideas, 1.27 times the $500 default.",
    "LIQUID's 45% odds cover the whole group of AI-infrastructure borrowers, not CoreWeave; most of its deal facts are relayed reports.",
    "PROME's recommendation is low conviction; declining is equally sound.",
    "Every app answer needs Will's confirming word in chat. You place any order."
  ],
  "confirmation": {
    "mode": "chat",
    "scope": "other",
    "reason": "Matching PROME-chat confirmation remains required under the installed fallback."
  }
}
```
