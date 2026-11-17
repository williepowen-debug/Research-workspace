# WQ-705 — explicit decision card

Question, options, context and conditions are decision terms. Queue Notes are operational; put changed conditions here or in the question, not only in Notes.

```decisions-options
{
  "schema_version": "decisions-options/3",
  "wq_id": "705",
  "queue_terms_sha256": "cf104542bb725df571da6fa279dce1d47d91ad9ac4bd0516443ed961e42d9fdd",
  "choices": [
    {
      "id": "A",
      "label": "Test it, and fix that one search if the test shows the miss",
      "meaning": "PROME runs the Gulf search once as it is and once limited to the last 24 hours with Bahrain added. If the changed form returns current Gulf headlines that the unchanged form does not, PROME changes that one search in the collector and tells WALTER. If not, nothing changes.",
      "consequence": "One round trip. The Gulf search stops being crowded out by old stories if that is the cause. Other searches are untouched."
    },
    {
      "id": "B",
      "label": "Test only, and bring me the result",
      "meaning": "PROME runs the same one comparison and reports what each form returned. No change to the collector without a second word from you.",
      "consequence": "You see the evidence before anything changes, at the cost of a second decision."
    },
    {
      "id": "C",
      "label": "Leave it",
      "meaning": "No test and no change. FALCON's own reading stays the backstop for Gulf events.",
      "consequence": "The lane may miss the next Gulf event the same way; how often is unknown."
    }
  ],
  "recommended_choice_id": "A",
  "context": "On Fri 11/13 Iran's Revolutionary Guards claimed an attack on a US early-warning radar in Bahrain; CENTCOM said two drones were shot down with no damage. The news collector saved no headline about it on 11/13 or 11/14, so WALTER's news lane never carried it; FALCON found it on its own read on 11/16. WALTER traced a likely cause in the collector's code: it keeps the first 15 results of each search and only then removes ones already seen, and the Gulf search has no recency limit and no Bahrain term.",
  "conditions": [
    "The cause is suspected, not established: the raw 11/13 response was not stored, so the test runs on today's news and cannot replay 11/13.",
    "The same 15-result limit may affect other broad searches; this decision does not test or change them.",
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
