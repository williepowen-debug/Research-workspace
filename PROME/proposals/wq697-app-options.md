# WQ-697 — explicit decision card

Question, options, context and conditions are decision terms. Queue Notes are operational; put changed conditions here or in the question, not only in Notes.

```decisions-options
{
  "schema_version": "decisions-options/3",
  "wq_id": "697",
  "queue_terms_sha256": "10d69c4006c37c40fa9e7048dcaf0ed28624b6ae6aecf7f90c907834ec1f50ae",
  "choices": [
    {
      "id": "A",
      "label": "Drop the scan from HENRY's start-up",
      "meaning": "HENRY removes step (g), the fleet-wide scan for other desks citing a level HENRY has replaced, from its start-up script, and updates one line of its own instructions and one maintenance row. PROME verifies the edit at HENRY's files.",
      "consequence": "HENRY's start-up falls from about 190 seconds to about 10. The same check still runs at HENRY's closeout, when a figure is actually replaced, and can be run on demand. What is lost is a start-up warning that another desk still cites a replaced level."
    },
    {
      "id": "B",
      "label": "Keep it as it is",
      "meaning": "No change. The scan keeps running at every HENRY start-up.",
      "consequence": "HENRY's start-up stays at about 3 minutes, and on the last two runs the scan timed out at 180 seconds and printed nothing, so it currently adds the wait without the warning."
    }
  ],
  "recommended_choice_id": "A",
  "context": "HENRY, the desk that reads market structure, runs a start-up step that scans the whole fleet for other desks still citing a market level HENRY has since replaced. On November 5 it took 2.7 of a 3-minute start-up and found no real stale figure. On November 13 and November 16 it timed out at 180 seconds and printed nothing. HENRY proposes dropping it from start-up and keeping the closeout check; it held the edit for your word.",
  "conditions": [
    "The closeout check (root closeout step 1c) is fleet-wide and stays; only HENRY's start-up copy is dropped.",
    "The one recorded catch of this kind was the July 28 VIOLET case; under A the same class is caught at HENRY's closeout, not at its next start-up.",
    "No threshold, gate, published level or other desk's file changes.",
    "Every app answer needs Will's confirming word in chat."
  ],
  "confirmation": {
    "mode": "chat",
    "scope": "other",
    "reason": "Matching PROME-chat confirmation remains required under the installed fallback."
  }
}
```
