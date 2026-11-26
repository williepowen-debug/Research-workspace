# WQ-754 — explicit decision card

Question, options, context and conditions are decision terms. Queue Notes are operational; put changed conditions here or in the question, not only in Notes.

```decisions-options
{
  "schema_version": "decisions-options/3",
  "wq_id": "754",
  "queue_terms_sha256": "ac1019eb4e87ea2199f9edaacd0192506dddf8142e3042b3f0d5acdc9bf79fe3",
  "choices": [
    {
      "id": "A",
      "label": "Score it CONFIRMED",
      "meaning": "BRT-23 is graded CONFIRMED on Glencore's 30 April 2026 production report: cobalt output down 39%, its Congo assets prioritising copper under the late-2025 export quota.",
      "consequence": "BRENT's scorecard gains a hit. No position, gate or money changes."
    },
    {
      "id": "B",
      "label": "Score it FAILED",
      "meaning": "BRT-23 stays FAILED on the letter: nothing was announced within 60 days of the Hormuz closure persisting, and the report describes a cut already under way before the forecast was made.",
      "consequence": "The row keeps the grade it carries now. No position, gate or money changes."
    }
  ],
  "recommended_choice_id": "B",
  "context": "BRENT forecast in March that a major Congo copper-cobalt operator would announce a significant curtailment within 60 days of the Hormuz closure persisting. On the morning of 11/25 it upgraded the grade to CONFIRMED citing a Glencore force majeure; that evening it found the notice dates from June 2025, before the forecast, withdrew the upgrade and restored FAILED. Its rule reads two ways and it does not choose.",
  "conditions": [
    "Scoring only: no position, gate, card or money.",
    "BRENT says the forecast's mechanism is falsified either way.",
    "PROME verified neither Glencore document.",
    "Not urgent."
  ],
  "confirmation": {
    "mode": "chat",
    "scope": "other",
    "reason": "Matching PROME-chat confirmation remains required under the installed fallback."
  }
}
```
