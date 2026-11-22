# WQ-729 — explicit decision card

Question, options, context and conditions are decision terms. Queue Notes are operational; put changed conditions here or in the question, not only in Notes.

```decisions-options
{
  "schema_version": "decisions-options/3",
  "wq_id": "729",
  "queue_terms_sha256": "4d25d58f4c328d4c2966c09abbe75c8d38aa2d6d3632a502216ea825cdc31400",
  "choices": [
    {
      "id": "A",
      "label": "Yes to all four",
      "meaning": "PROME sends CATO the one-sentence launcher change (first reads of USER.md and BOOT.md through the bounded reader), and makes the three changes to its own checks: drop special and dormant desks from the standing-backlog line, remove the calendar view's size warning, and make the closeout-receipt checker accept an ask-and-receipt row as written or retire it.",
      "consequence": "Boot reports stop reading PARTIAL for the plain-reader reason, and three lines that are read past at every boot or closeout go away. No gate, threshold or authority changes."
    },
    {
      "id": "B",
      "label": "The launcher fix only",
      "meaning": "CATO gets the launcher change. PROME's three checks stay as they are until you say otherwise.",
      "consequence": "The PARTIAL-for-the-same-reason boot report is fixed; the three noisy lines remain."
    },
    {
      "id": "C",
      "label": "None of them",
      "meaning": "Nothing changes.",
      "consequence": "The boot report keeps reading PARTIAL when the launcher's plain reads come first, and PROME keeps naming it each time."
    }
  ],
  "recommended_choice_id": "A",
  "context": "On 11/22 you asked for one short retirement list, not a programme, with the launcher fix as one item for your word. Items 2 to 4 are PROME's own process checks, which the done-without-asking class C12 already lets PROME retire one at a time; they are listed because you asked for the list. The launcher is a shared script that CATO owns, so it needs your word.",
  "conditions": [
    "Basis: what fired with no action at the 11/22 boot and in the daily notes of 11/16 to 11/21. A full 60-day record check of every check was NOT done.",
    "The 11/20 checks from WQ-713 and WQ-716 are not on the list, by your word: they are judged after they have a record.",
    "The launcher change is CATO's to make and test; PROME sends it by packet and reads the diff.",
    "No money, gate, level, threshold or desk charter is involved.",
    "Every app answer needs Will's confirming word in chat."
  ],
  "confirmation": {
    "mode": "chat",
    "scope": "other",
    "reason": "Matching PROME-chat confirmation remains required under the installed fallback."
  }
}
```
