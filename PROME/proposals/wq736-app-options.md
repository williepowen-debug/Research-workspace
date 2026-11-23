# WQ-736 — explicit decision card

Question, options, context and conditions are decision terms. Queue Notes are operational; put changed conditions here or in the question, not only in Notes.

```decisions-options
{
  "schema_version": "decisions-options/3",
  "wq_id": "736",
  "queue_terms_sha256": "5ebf601c0bd46ccb7ded018df1c55981eaf51f42a96c00b1d78d3aa247716aba",
  "choices": [
    {
      "id": "A",
      "label": "Adopt the number",
      "meaning": "The energy-demand score goes to 4 when the EIA Henry Hub spot price is at or above 1.5 times its median of the prior 60 trading days on 3 straight trading days, Nov 1 to Mar 31, and heating demand ran at least 10% above the 1991 to 2020 normal in the 7 days before.",
      "consequence": "AEOLUS writes the step into its current table. Nothing fires today: $3.10 on 11/17 against a line of $4.43."
    },
    {
      "id": "B",
      "label": "BRENT reads it first",
      "meaning": "BRENT, which owns gas prices, reviews the level in its next ordinary session and the question comes back to you with its view.",
      "consequence": "The step stays without a number until then."
    },
    {
      "id": "C",
      "label": "Retire the step",
      "meaning": "The gas-price step is removed from the score.",
      "consequence": "The energy-demand score can reach 4 only through its other written conditions."
    }
  ],
  "recommended_choice_id": "A",
  "context": "AEOLUS's weather score has a step named 'Henry Hub break' that never had a number. It owed one by 11/01 and missed. On 11/23 it proposed this one with its history.",
  "conditions": [
    "It would have fired in 6 of 29 winters, and in 0 of the 3 strong El Nino winters; three winters is a small count.",
    "The number was chosen after looking at the history, which flatters the count.",
    "The step is missing from AEOLUS's current table, so retiring loses nothing in use today.",
    "No score moves on any answer. No money.",
    "Every app answer needs Will's confirming word in chat."
  ],
  "confirmation": {
    "mode": "chat",
    "scope": "other",
    "reason": "Matching PROME-chat confirmation remains required under the installed fallback."
  }
}
```
