# WQ-742 — explicit decision card

Question, options, context and conditions are decision terms. Queue Notes are operational; put changed conditions here or in the question, not only in Notes.

```decisions-options
{
  "schema_version": "decisions-options/3",
  "wq_id": "742",
  "queue_terms_sha256": "cfe6598fed2f66442efce151596fac0c74abcf0346abcc8247444bddf42ac26a",
  "choices": [
    {
      "id": "A",
      "label": "Hold RED for now",
      "meaning": "RED does not take the Florida flood assignment until the five desks' first findings have been corrected and re-read. PROME then asks again.",
      "consequence": "RED's Florida packet stays unacted. Its Tuesday grade of its own 30-year Treasury forecast goes ahead."
    },
    {
      "id": "B",
      "label": "RED starts now",
      "meaning": "RED argues the strongest case that Florida banks are not hiding flood losses and the flood does not reach bank credit, starting at its Tuesday 11/24 session.",
      "consequence": "The hold packet is withdrawn. The Tuesday forecast grade goes ahead as well."
    }
  ],
  "recommended_choice_id": "A",
  "context": "On 11/23 at 17:15 ET you assigned RED to argue the other side of the Florida flood thread. Two minutes later you pasted CATO's review, which says not to add a separate RED exercise yet. RED has been held since.",
  "conditions": [
    "The first sweep overstated three things that are still being corrected; that is the reason to wait.",
    "CATO's text is a reviewer's recommendation, not your instruction.",
    "No money and no trade. Every app answer needs Will's confirming word in chat."
  ],
  "confirmation": {
    "mode": "chat",
    "scope": "other",
    "reason": "Matching PROME-chat confirmation remains required under the installed fallback."
  }
}
```
