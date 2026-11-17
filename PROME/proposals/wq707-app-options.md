# WQ-707 — explicit decision card

Question, options, context and conditions are decision terms. Queue Notes are operational; put changed conditions here or in the question, not only in Notes.

```decisions-options
{
  "schema_version": "decisions-options/3",
  "wq_id": "707",
  "queue_terms_sha256": "ef53e3a0ac7632936dff0f35f592daae54f449061cea41f53bd3d6e8e08c395f",
  "choices": [
    {
      "id": "A",
      "label": "Add the limit to all 46 and split the China search",
      "meaning": "PROME adds the collector's existing last-7-days limit to every search that lacks one, and splits the 18-term China search into short ones as for the Gulf. Each changed search is tested before and after and the table is brought to you. WALTER is told.",
      "consequence": "Every theme returns current stories in the places the collector keeps. More items per run for WALTER's lane to read."
    },
    {
      "id": "B",
      "label": "Only the broad themes",
      "meaning": "The same change for the broad searches only: China, volatility, credit spreads, funding stress, bank stress, consumer stress, housing, Florida, Russia and Ukraine energy. The narrow single-phrase searches stay as they are.",
      "consequence": "The core themes are repaired with less added volume. Narrow searches keep returning old matches."
    },
    {
      "id": "C",
      "label": "Leave the rest",
      "meaning": "Only the Gulf search is repaired, under WQ-706.",
      "consequence": "The other searches keep returning mostly old stories."
    }
  ],
  "recommended_choice_id": "A",
  "context": "After the Gulf search was found returning only old stories, PROME ran one read-only pass over all 61 news searches on 2026-11-17. Of the first 15 results each search returns (what the collector keeps), 15 searches had none under 48 hours old and 20 had one to three. On most of those the places are filled by stories more than a month old, because the search has no recency limit and comes back ranked by relevance. The 15 searches that already carry a limit show none that old.",
  "conditions": [
    "One pass at one time of day; the 48-hour yardstick is PROME's.",
    "A narrow search can truthfully have nothing new; stale is weaker evidence there.",
    "The collector's direct publisher feeds are a separate leg and were not tested; the lane is not blind overall.",
    "More items will be kept per run; a 7-day limit cannot surface an older story that newly matters.",
    "No cost. Before any write in the collection repository PROME asks WALTER whether a scan is open.",
    "Every app answer needs Will's confirming word in chat."
  ],
  "confirmation": {
    "mode": "chat",
    "scope": "other",
    "reason": "Matching PROME-chat confirmation remains required under the installed fallback."
  }
}
```
