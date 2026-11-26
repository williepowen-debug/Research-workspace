# WQ-755 — explicit decision card

Question, options, context and conditions are decision terms. Queue Notes are operational; put changed conditions here or in the question, not only in Notes.

```decisions-options
{
  "schema_version": "decisions-options/3",
  "wq_id": "755",
  "queue_terms_sha256": "3e27087ca3e68f1226fa7e967528dd379842a69e54ac82a134dcce16958563f7",
  "choices": [
    {
      "id": "A",
      "label": "Live and binding",
      "meaning": "BG-02 is in force. BRENT's trade file, which says it remains binding and lists it as a check at any trigger, governs; BRENT corrects its gate-spec file and registry header to match.",
      "consequence": "The safeguard stays on. Nothing changes tonight: the Jazan Port hit does not meet it."
    },
    {
      "id": "B",
      "label": "Lapsed on 9/25",
      "meaning": "BG-02 ended when its window closed on Friday 9/25. BRENT's gate-spec file and registry header govern; BRENT corrects its trade file to match.",
      "consequence": "The safeguard is off the books. Nothing changes tonight."
    }
  ],
  "recommended_choice_id": "A",
  "context": "BG-02 is BRENT's frame-breaker rule: a confirmed event destroying Gulf export capacity would stop its oil thesis from being acted on. BRENT's own files disagree on whether it still applies. It surfaced tonight when BRENT graded the Houthi hit on Jazan Port against it (not met).",
  "conditions": [
    "It matters only if a future event meets the rule's head clause.",
    "Energy is stood down and the energy arm is retired, so nothing can be acted on without your word either way.",
    "PROME did not read the three BRENT files; the description of them is BRENT's.",
    "PROME's recommendation is low conviction: a safeguard that costs nothing to keep.",
    "Not urgent."
  ],
  "confirmation": {
    "mode": "chat",
    "scope": "other",
    "reason": "Matching PROME-chat confirmation remains required under the installed fallback."
  }
}
```
