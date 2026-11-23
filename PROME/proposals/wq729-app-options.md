# WQ-729 — explicit decision card

Question, options, context and conditions are decision terms. Queue Notes are operational; put changed conditions here or in the question, not only in Notes.

```decisions-options
{
  "schema_version": "decisions-options/3",
  "wq_id": "729",
  "queue_terms_sha256": "21361d7aa09937119bfa113e7022b937f1010978a5ce7f9df0aa4659c484ed7d",
  "choices": [
    {
      "id": "A",
      "label": "Approve all three",
      "meaning": "(1) The boot runner, a PROME file, gets the literal first commands for the manual reads and re-reads USER.md through the bounded reader even when the launcher's plain read came first; no launcher change. (3) The calendar view's size target goes from 6,000 to 16,000 bytes. (4) Every closeout row PROME writes carries the receipt and names the launch row it resolves.",
      "consequence": "No rule changes. Boots stop reading PARTIAL for PROME's own plain reads; the calendar warning fires only on real growth; new desk closeouts read as receipted."
    },
    {
      "id": "B",
      "label": "Pick",
      "meaning": "You name which of the three to do.",
      "consequence": "The others stay as they are."
    },
    {
      "id": "C",
      "label": "None",
      "meaning": "Nothing changes.",
      "consequence": "The three lines keep printing as they do today."
    }
  ],
  "recommended_choice_id": "A",
  "context": "You asked on 11/23 that these wait for a diagnosis. Result: the PARTIAL boots were mostly PROME's own plain reads after a reset, not the launcher (one of the cited boots is recorded as launcher-started, and its start text orders a plain read of USER.md only). The calendar's 6,000-byte target dates from when the calendar sat inside another page. The receipt checker is right and PROME's rows omit two fields.",
  "conditions": [
    "For three of the cited boots (11/16 morning, 11/16 21:17 ET, 11/20) the record does not say how the session started.",
    "After item 1 a boot can still read PARTIAL for: an unfinished mandatory read, the memory hooks or macro check not run, an owed gate action without a disposition, the regime memo not re-based, an overdue spine audit, a missing tool.",
    "Counting a complete plain read as acceptable would be a rule change and is not proposed.",
    "The receipt checker keeps reading 1,559 rows written before its format existed as UNKNOWN; cutting those off would be a rule change and is not proposed here.",
    "Item 2 (RAV and BARON off the backlog line) is already approved and done.",
    "Every app answer needs Will's confirming word in chat."
  ],
  "confirmation": {
    "mode": "chat",
    "scope": "other",
    "reason": "Matching PROME-chat confirmation remains required under the installed fallback."
  }
}
```
