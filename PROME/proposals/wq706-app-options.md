# WQ-706 — explicit decision card

Question, options, context and conditions are decision terms. Queue Notes are operational; put changed conditions here or in the question, not only in Notes.

```decisions-options
{
  "schema_version": "decisions-options/3",
  "wq_id": "706",
  "queue_terms_sha256": "1814f805df9f9b64594339ac8b1b350de43bfd4ac8e11003c03bf173bfe55524",
  "choices": [
    {
      "id": "A",
      "label": "Fix the Gulf search and check the others",
      "meaning": "PROME replaces the one long Gulf search with short ones that between them keep every current term and add Bahrain. Each is tested to return current items before it is committed. PROME also runs the same one-time freshness check on every other search and brings you one list of any that are stale.",
      "consequence": "The Gulf lane sees current news again. You learn whether other theaters are blind the same way. Fixing those would be a second decision."
    },
    {
      "id": "B",
      "label": "Fix the Gulf search only",
      "meaning": "The same replacement for the Gulf search. No check of the other searches.",
      "consequence": "The known hole is closed. Any other search with the same fault stays unseen until it misses something."
    },
    {
      "id": "C",
      "label": "Leave it",
      "meaning": "No change. FALCON's own reading stays the only backstop for Gulf events.",
      "consequence": "The news lane keeps returning old Gulf stories."
    }
  ],
  "recommended_choice_id": "A",
  "context": "Under WQ-705 PROME tested the Gulf news search on 2026-11-17. The search as it stands joins 18 terms with OR. It returned 32 items, none newer than about four days and most months old, whether or not a last-24-hours limit was added. A seven-term search returned 100 items, nearly all from the last day. The fix WQ-705 named did not work, so nothing was changed. The same test surfaced titles about a new Iranian strike in Bahrain and a tanker struck in Hormuz that the lane was not carrying.",
  "conditions": [
    "Why the long search fails is inferred, not established; how many terms is too many was not measured.",
    "That this caused the 11/13 miss is not established; that day's response was not stored.",
    "More short searches mean more items kept per run; the 15-per-search limit stays.",
    "No cost, no new source, no schedule change.",
    "Before any write in the collection repository PROME asks WALTER whether a scan is open.",
    "Every app answer needs Will's confirming word in chat."
  ],
  "confirmation": {
    "mode": "chat",
    "scope": "other",
    "reason": "Matching PROME-chat confirmation remains required under the installed fallback."
  }
}
```
